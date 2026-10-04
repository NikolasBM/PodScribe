#!/usr/bin/env python3
"""Fetch new transcripts for every podcast in podcasts.toml.

Podcasts with source = "published" publish their own transcripts. Podcasts with
source = "rss" are transcribed from their RSS audio with Azure MAI-Transcribe.
"""
import argparse
import collections
import csv
import difflib
import html
import io
import itertools
import json
import os
import re
import sys
import threading
import time
import tomllib
import urllib.error
import unicodedata
import urllib.request
import uuid
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USER_AGENT = "PodScribe"
LOOKBACK_DAYS = 30

TRANSCRIBE_MODEL = "MAI-Transcribe-2"
TRANSCRIBE_API_VERSION = "2025-10-15"
PARAGRAPH_MS = 60_000
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.?!])\s+")
DOMAIN_RE = re.compile(r"\b[\w-]+\.(?:com|ai|io|dev|org)\b", re.IGNORECASE)
SPELLED_DOMAIN_RE = re.compile(r"^That's\b.*(?:\.(?:com|ai|io|dev|org)\b|\b[A-Z](?:-[A-Z])+\b)", re.IGNORECASE)
PARAGRAPH_RE = re.compile(r"^(?:\*\*(?P<speaker>[^*]+)\*\* )?\[(?P<ts>\d\d:\d\d:\d\d)\] (?P<text>.*)$", re.DOTALL)
TS_RE = re.compile(r"\[(\d\d):(\d\d):(\d\d)\]")
EDIT_MARKER_RE = re.compile(r"^[\w .]{1,40}_EDIT:\s*")
# A marker like "blitzy July_EDIT:" names a sponsor edit; the usual ones start with a date ("260813 hed_EDIT:")
SPONSOR_MARKER_RE = re.compile(r"^(?!\d{6})[\w .]{1,40}_EDIT:")
SPEAKER_LABEL_RE = re.compile(r"^(?:Nathaniel Whittemore(?:'s audio recording)?|Speaker):\s*")
MAX_AD_SECONDS = 240
MAX_AD_SENTENCES = 24
JEV_MIN_INTERVAL = 0.06  # seconds between requests, to stay under the 1,200 requests/minute limit
JEV_URL = "https://api.typesafe.ai/v1/systemone"
JEV_MODEL = "jev-1.13.0"
JEV_AD_THRESHOLD = 0.5
JEV_EDGE_THRESHOLD = 0.45
JEV_MAX_GAP = 6
JEV_SPONSOR_REACH = 2  # sentences a read may grow outwards over, if they name one of the podcast's ad_sponsors
JEV_MIN_FLAGGED = 5
META_MAX_CATEGORIES = 4
META_COMPANY_THRESHOLD = 0.9
META_MAX_CANDIDATES = 40
META_MAX_CHARS = 100_000  # transcript characters sent to Jev (limit is 64k tokens for state and questions together; 160k chars was rejected)
JEV_AD_QUESTION = (
    "Is `sentence` part of a paid sponsor message, where the host reads out an advertisement for a company, "
    "product or service? `before` and `after` are the neighbouring sentences, for context only."
)
JEV_AD_CRITERIA = {
    "true": "Advertising copy for a sponsor: brand pitch, product features, customer claims, an offer for listeners, "
            "or a call to visit the sponsor's web address",
    "false": "The episode's own content, including the host talking about tools she uses or reviews herself, "
             "and the show's own sign-off asking listeners to subscribe or rate the show",
}


def warn(message):
    """Print a warning to stderr, as an annotation when running in GitHub Actions."""
    prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") else "warn "
    print(f"{prefix}{message}", file=sys.stderr)


def parse_date(date_str):
    """Parse YYYY-MM-DD string to date object."""
    return date.fromisoformat(date_str)


def date_range(start_date, end_date):
    """Yield dates from start_date to end_date (inclusive)."""
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


def http_get(url, timeout):
    """GET a URL and return the response body as bytes."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def get_first_line(content):
    """Get the first non-empty line of content."""
    for line in content.split("\n"):
        line = line.strip()
        if line:
            return line
    return "(empty)"


def extract_title(content, fallback):
    """Extract episode title from '# {Title} — Transcript ({date})'."""
    match = re.match(r"^#\s*(.+?)\s*—\s*Transcript\s*\(.+\)\s*$", get_first_line(content))
    return match.group(1).strip() if match else fallback


def sanitize_filename(title):
    """Replace characters unsafe in filenames."""
    return re.sub(r'[\\/:*?"<>|]', "-", title).strip()[:150]


# --- the transcript file format ---------------------------------------------
# ---
# key: value          (YAML frontmatter; values are JSON, which is valid YAML)
# ---
#
# # Title
#
# [HH:MM:SS] ... the transcript ...

FRONTMATTER_KEYS = ["podcast", "podcast_title", "title", "date", "url", "guid", "host", "guests", "format", "level", "length",
                    "categories", "featured", "mentioned", "transcript_source", "transcribed_by", "credit"]
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n\n# [^\n]*\n\n", re.S)


def render_doc(meta, body):
    lines = []
    for key in FRONTMATTER_KEYS:
        value = meta.get(key)
        if value is None or value == "" or (key == "guests" and not value):
            continue
        lines.append(f"{key}: {value if key == 'date' else json.dumps(value, ensure_ascii=False)}")
    return "---\n" + "\n".join(lines) + f"\n---\n\n# {meta['title']}\n\n" + body.strip("\n") + "\n"


def parse_doc(text):
    """(frontmatter dict, body) of a transcript file; (None, text) if it has no frontmatter."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    meta = {}
    for line in match[1].split("\n"):
        key, _, raw = line.partition(": ")
        try:
            meta[key] = json.loads(raw)
        except ValueError:
            meta[key] = raw
    return meta, text[match.end():].rstrip("\n")


def read_doc(path):
    meta, body = parse_doc(path.read_text(encoding="utf-8"))
    if meta is None:
        raise ValueError(f"{path.name}: no frontmatter")
    return meta, body


def episode_meta(podcast, title, date_str, url, guid, **extra):
    meta = {"podcast": podcast["slug"], "podcast_title": podcast["name"], "title": title, "date": date_str,
            "url": url, "guid": guid, "host": podcast.get("host"), "credit": podcast.get("credit")}
    meta.update(extra)
    return meta


# --- source = "published" ---------------------------------------------------

def try_metadata(meta, body, podcast, guests=None):
    """Add Jev's metadata fields when Jev is available; the transcript is saved without them otherwise."""
    if not os.environ.get("TYPESAFE_API_KEY"):
        return meta
    try:
        guests = guest_names(meta["title"]) if guests is None else guests
        return {**meta, "guests": guests, **metadata_fields(meta["title"], meta["date"], body, podcast)}
    except Exception as e:
        warn(f"{meta['date']}: no metadata, {type(e).__name__}: {e}")
        return meta


def fetch_published(podcast, out_dir, since, until, limit):
    """Download transcripts the show publishes itself. Returns number saved."""
    count = 0
    for date_obj in date_range(since, until):
        if limit is not None and count >= limit:
            break
        date_str = date_obj.isoformat()

        # Skip if already fetched (current "date - title.md" or legacy "date.md")
        if any(out_dir.glob(f"{date_str} - *.md")) or (out_dir / f"{date_str}.md").exists():
            continue

        url = podcast["transcript_url"].format(date=date_str)
        try:
            content = http_get(url, timeout=10).decode("utf-8")
        except urllib.error.HTTPError as e:
            # 404 = no episode that day, skip silently
            if e.code != 404:
                warn(f"{date_str}: HTTP {e.code}: {e.reason}")
            content = None
        except Exception as e:
            warn(f"{date_str}: {type(e).__name__}: {e}")
            content = None

        if content is not None:
            title = extract_title(content, date_str)
            head, sep, body = content.partition("\n---\n\n")
            if sep:
                body = strip_ads(body.rstrip("\n"), podcast)
                url = (re.search(r"https?://\S+", head) or [url])[0]
                meta = try_metadata(episode_meta(podcast, title, date_str, url, url, transcript_source="publisher"), body, podcast)
                content = render_doc(meta, body)
            (out_dir / f"{date_str} - {sanitize_filename(title)}.md").write_text(content, encoding="utf-8", newline="\n")
            print(f"saved {date_str}: {title}")
            count += 1

        # Sleep between requests
        time.sleep(0.2)

    return count


# --- source = "substack" ---------------------------------------------------
# A Substack publication whose podcast posts carry the transcript in the post body.

def http_json(url):
    return json.loads(http_get(url, timeout=30))


def substack_episodes(podcast, since, until):
    """Podcast posts (id, slug, title, date) of the publication's archive within the range, newest first."""
    episodes, offset = [], 0
    while True:
        page = http_json(f"{podcast['site']}/api/v1/archive?sort=new&offset={offset}&limit=50")
        if not page:
            break
        offset += len(page)
        for post in page:
            day = date.fromisoformat(post["post_date"][:10])
            if post["type"] == "podcast" and post["audience"] == "everyone" and since <= day <= until:
                episodes.append({"id": post["id"], "slug": post["slug"], "title": " ".join(post["title"].split()), "date": day})
        if date.fromisoformat(page[-1]["post_date"][:10]) < since:
            break
        time.sleep(0.2)
    return episodes


def speaker_guests(body, podcast):
    """Everyone with a speaker label who is not one of the podcast's hosts."""
    return [n for n in dict.fromkeys(re.findall(r"(?m)^\*\*([^*]+)\*\*", body)) if n not in podcast.get("hosts", [])]


def clean_title(title):
    """Leading emoji and symbols (the science podcast's microscope, say) are noise in a title."""
    return re.sub(r"^[^\w]+", "", title).strip()


def stamp(text):
    """'[HH:MM:SS]' or the older '[MM:SS]' as HH:MM:SS."""
    parts = text.split(":")
    return ":".join(["00"] * (3 - len(parts)) + parts)


def substack_body(body_html):
    """Render the transcript of a post body as paragraphs with speaker labels. None if the post has no transcript.

    Handles `<strong>Name [HH:MM:SS]:</strong> text`, `Name [HH:MM:SS]</strong>:`, `Name</strong>: text` and plain
    `Name: text` (for names already seen as labels), with inline [HH:MM:SS] or [MM:SS] markers. Headings (h2/h3) and
    `<strong>[MM:SS] Title</strong>` chapter lines are kept as `## Heading`; a `<br>` starts a new paragraph.
    """
    marker = re.search(r"<h[12][^>]*>(?:<[^>]+>)*\s*Transcript\s*(?:</[^>]+>)*</h[12]>", body_html)
    if not marker:
        return None
    stamp_re = re.compile(r"\[(\d{1,2}:\d\d(?::\d\d)?)\]")
    label_re = re.compile(r"^<strong>(?P<name>[^<\[:]+?)\s*(?:\[(?P<ts>\d{1,2}:\d\d(?::\d\d)?)\])?\s*:?\s*</strong>\s*:?\s*(?P<rest>.*)$", re.S)
    chapter_re = re.compile(r"^<strong>\s*\[(?P<ts>\d{1,2}:\d\d(?::\d\d)?)\]\s*(?P<title>[^<]+)</strong>$")
    now, out, turns = "00:00:00", [], 0

    def clean(fragment):
        return html.unescape(re.sub(r"<[^>]+>", "", fragment))

    plain_re = re.compile(r"^(?:\[[\d:]+\]\s*)?(?P<name>[A-Za-z][\w .'’-]{0,30}):\s+(?P<rest>.*)$", re.S)

    def speaker(name):  # "swyx" and "Swyx" are the same voice
        name = name.strip()
        return name[0].upper() + name[1:]
    seen = collections.Counter()  # names that open lines as "Name: text": speakers, if they do it often enough
    for line in clean(re.sub(r"<br\s*/?>|</p>", "\n", body_html[marker.end():])).split("\n"):
        if m := plain_re.match(line.strip()):
            seen[speaker(m["name"])] += 1
    speakers = {name for name, n in seen.items() if n >= 3} | set(re.findall(r"<strong>([^<\[:]+?)\s*(?:\[[\d:]+\])?\s*:?\s*</strong>", body_html[marker.end():]))

    for kind, inner in re.findall(r"<(h[23]|p)[^>]*>(.*?)</\1>", body_html[marker.end():], flags=re.S):
        inner = inner.strip()
        chapter = chapter_re.match(inner)
        label = label_re.match(inner)
        if chapter:
            out.append(f"## {chapter['title'].strip()}")
            now = stamp(chapter["ts"])
            continue
        if kind != "p" and not label:
            out.append(f"## {clean(inner).strip()}")
            continue
        name, ts = (label["name"].strip(), label["ts"]) if label else (None, None)
        inner = label["rest"] if label else inner
        for n, segment in enumerate(re.split(r"<br\s*/?>", inner)):
            text = clean(segment).strip()
            turn = name if n == 0 else None
            if (n > 0 or not label) and (m := plain_re.match(text)) and speaker(m["name"]) in speakers:
                turn, text = speaker(m["name"]), m["rest"]
                ts = None
            stamps = stamp_re.findall(text)
            start = stamp(ts) if (ts and turn) else now
            text = " ".join(stamp_re.sub("", text).split())
            if turn:
                turns += 1
                name = turn
            if text:
                out.append(f"{'**' + turn + '** ' if turn else ''}[{start}] {text}")
            now = stamp(stamps[-1]) if stamps else start
    return "\n\n".join(out) if turns else None


def fetch_substack(podcast, out_dir, since, until, limit, dry_run):
    """Save the transcripts of a Substack publication's podcast posts. Returns number saved."""
    try:
        episodes = substack_episodes(podcast, since, until)
    except Exception as e:
        warn(f"{podcast['slug']}: archive: {type(e).__name__}: {e}")
        return 0
    done = existing_guids(out_dir)
    todo = [e for e in episodes if f"substack:{e['id']}" not in done]
    if limit is not None:
        todo = todo[:limit]
    count = 0
    for episode in todo:
        date_str = episode["date"].isoformat()
        if dry_run:
            print(f"would fetch {date_str}: {episode['title']}")
            continue
        try:
            post = http_json(f"{podcast['site']}/api/v1/posts/{episode['slug']}")
            body = substack_body(post.get("body_html") or "")
        except Exception as e:
            warn(f"{date_str} {episode['title']}: {type(e).__name__}: {e}")
            continue
        if body is None:  # a podcast post without a transcript (show notes only)
            continue
        title = clean_title(episode["title"])
        url = post.get("canonical_url") or podcast["site"] + "/p/" + episode["slug"]
        meta = try_metadata(episode_meta(podcast, title, date_str, url, f"substack:{episode['id']}", transcript_source="publisher"),
                            body, podcast, speaker_guests(body, podcast))
        (out_dir / f"{date_str} - {sanitize_filename(title)}.md").write_text(render_doc(meta, body), encoding="utf-8", newline="\n")
        print(f"saved {date_str}: {title}")
        count += 1
        time.sleep(0.2)
    return count


# --- source = "folder" ------------------------------------------------------
# Transcripts shared as a Dropbox folder of plain-text files named after the guest. The RSS feed gives each file
# its episode: title, date and link. The folder's link is `folder_url` (or, if it must stay private, the
# environment variable named in `folder_url_env`).

FOLDER_SECONDS_TOLERANCE = 90


def folder_files(url):
    """{file stem: text} for the .txt files of a shared Dropbox folder (downloaded as one zip)."""
    url = re.sub(r"([?&])dl=0", r"\1dl=1", url)
    if "dl=1" not in url:
        url += ("&" if "?" in url else "?") + "dl=1"
    files = {}
    with zipfile.ZipFile(io.BytesIO(http_get(url, timeout=300))) as archive:
        for info in archive.infolist():
            if info.filename.endswith(".txt") and not info.is_dir():
                stem = re.sub(r"#U([0-9a-f]{4})", lambda m: chr(int(m[1], 16)), Path(info.filename).stem)
                files[stem] = archive.read(info).decode("utf-8", errors="replace")
    return files


def plain_last_seconds(text):
    stamps = re.findall(r"\((\d+):(\d\d)(?::(\d\d))?\):", text)
    if not stamps:
        return None
    a, b, c = stamps[-1]
    return int(a) * 3600 + int(b) * 60 + int(c) if c else int(a) * 60 + int(b)


def _words(text):
    return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()).split()


def _name_in(name, words):
    def near(token):  # tolerate a typo in longer names ("Schoenig" for "Schoening")
        return token in words or (len(token) > 4 and any(
            abs(len(w) - len(token)) <= 2 and difflib.SequenceMatcher(None, token, w).ratio() >= 0.85 for w in words))
    tokens = [t for t in _words(name) if len(t) > 1]
    if not tokens:
        return False
    if len(tokens) == 1:
        return tokens[0] in words
    return " ".join(tokens) in " ".join(words) or (near(tokens[0]) and near(tokens[-1]))


def folder_stem_names(stem):
    """The guest name(s) in a file name: "Elena Verna 2.0" -> ["Elena Verna"], "A + B" -> ["A", "B"]."""
    base = re.match(r"^(.*?)(?:[\s_]+V?\d+(?:\.0)?)?$", stem.replace("_", " ").strip())[1]
    base = re.sub(r"(?i)\b(live|part \d)\b", "", base)
    return [p.strip() for p in re.split(r"\s*[&+,]\s*|\s+and\s+", base) if p.strip()]


def match_folder_files(files, episodes):
    """{episode guid: file stem}. A file belongs to the episode whose title names its guest and whose length matches
    the file's last timestamp (guests come back, so the name alone is not enough); then by description, then by
    length alone."""
    seconds = {stem: plain_last_seconds(text) for stem, text in files.items()}

    def close(episode, stem, tolerance=FOLDER_SECONDS_TOLERANCE):
        return None not in (episode["seconds"], seconds[stem]) and abs(episode["seconds"] - seconds[stem]) <= tolerance

    assigned, used = {}, set()

    def free(episode):
        return episode["guid"] not in used

    def pick(stem, candidates):
        candidates = [e for e in candidates if free(e)]
        near = [e for e in candidates if close(e, stem)]
        chosen = min(near, key=lambda e: abs(e["seconds"] - seconds[stem])) if near else (
            candidates[0] if len(candidates) == 1 and seconds[stem] is None else None)
        if chosen:
            assigned[chosen["guid"]] = stem
            used.add(chosen["guid"])
        return chosen

    for stem in files:
        names = folder_stem_names(stem)
        if names:
            pick(stem, [e for e in episodes if all(_name_in(n, _words(e["title"])) for n in names)])
    taken = set(assigned.values())
    for stem in files:
        names = folder_stem_names(stem)
        if stem not in taken and names:
            pick(stem, [e for e in episodes if all(_name_in(n, _words(e["description"])) for n in names)])
    taken = set(assigned.values())
    for stem in files:
        if stem not in taken:
            near = [e for e in episodes if free(e) and close(e, stem, tolerance=45)]
            if len(near) == 1:
                assigned[near[0]["guid"]] = stem
                used.add(near[0]["guid"])
    return assigned


def plain_transcript_body(text, host=None):
    """`Name (H:MM:SS):` followed by lines of speech, in blocks -> `**Name** [HH:MM:SS] speech`, `(H:MM:SS):` -> `[HH:MM:SS] speech`."""
    header_re = re.compile(r"^(?:(?P<name>.+?)\s+)?\((?P<ts>\d+:\d\d(?::\d\d)?)\):\s*(?P<rest>.*)$")
    paragraphs, current = [], None
    for line in text.replace("\r\n", "\n").split("\n"):
        header = header_re.match(line.strip())
        if header:
            current = {"name": (header["name"] or "").strip(), "ts": stamp(header["ts"]), "text": [header["rest"]] if header["rest"] else []}
            paragraphs.append(current)
        elif line.strip() and current is not None:
            current["text"].append(line.strip())
    out = []
    for p in paragraphs:
        name = p["name"]
        if host and name and name == host.split()[0]:
            name = host
        speech = " ".join(" ".join(p["text"]).split())
        if speech:
            out.append(f"{'**' + name + '** ' if name else ''}[{p['ts']}] {speech}")
    return "\n\n".join(out)


def fetch_folder(podcast, out_dir, since, until, limit, dry_run):
    """Import transcripts from the shared folder for the feed's episodes. Returns number saved."""
    try:
        episodes = podcast_episodes(podcast)
    except Exception as e:
        warn(f"{podcast['slug']}: feed: {type(e).__name__}: {e}")
        return 0
    done = existing_guids(out_dir)
    todo = [e for e in episodes if since <= e["date"] <= until and e["guid"] not in done]
    if not todo:
        return 0
    if dry_run:
        for episode in todo:
            print(f"would look for {episode['date']}: {episode['title']}")
        return 0
    url = podcast.get("folder_url") or os.environ.get(podcast.get("folder_url_env", ""))
    if not url:
        warn(f"{podcast['slug']}: {len(todo)} episodes waiting, but the folder link (folder_url) is not set")
        return 0
    try:
        files = folder_files(url)
    except Exception as e:
        warn(f"{podcast['slug']}: folder: {type(e).__name__}: {e}")
        return 0
    matched = match_folder_files(files, episodes)  # all episodes, so a returning guest is matched by length
    count = 0
    for episode in todo:
        stem = matched.get(episode["guid"])
        if stem is None:
            print(f"not in the folder yet: {episode['date']} {episode['title']}")
            continue
        if limit is not None and count >= limit:
            break
        date_str = episode["date"].isoformat()
        body = strip_ads(plain_transcript_body(files[stem], podcast.get("host")), podcast)
        meta = try_metadata(episode_meta(podcast, episode["title"], date_str, episode["link"] or None, episode["guid"],
                                         transcript_source="shared-folder"), body, podcast, speaker_guests(body, podcast))
        (out_dir / f"{date_str} - {sanitize_filename(episode['title'])}.md").write_text(render_doc(meta, body), encoding="utf-8", newline="\n")
        print(f"saved {date_str}: {episode['title']}  <- {stem}.txt")
        count += 1
    return count


# --- source = "rss" ---------------------------------------------------------

def parse_feed(xml_bytes):
    """Return the feed's episodes (guid, title, date, audio_url, link), oldest first."""
    episodes = []
    for item in ET.fromstring(xml_bytes).find("channel").findall("item"):
        enclosure = item.find("enclosure")
        pub_date = item.findtext("pubDate")
        if enclosure is None or not enclosure.get("url") or not pub_date:
            continue
        duration = (item.findtext("{http://www.itunes.com/dtds/podcast-1.0.dtd}duration") or "").strip()
        parts = [int(x) for x in duration.split(":")] if re.fullmatch(r"\d+(:\d+){0,2}", duration) else []
        episodes.append({
            "guid": (item.findtext("guid") or enclosure.get("url")).strip(),
            "title": " ".join((item.findtext("title") or "").split()),
            "date": parsedate_to_datetime(pub_date).date(),
            "audio_url": enclosure.get("url"),
            "link": (item.findtext("link") or "").strip(),
            "seconds": sum(x * 60 ** i for i, x in enumerate(reversed(parts))) if parts else None,
            "description": re.sub(r"<[^>]+>", " ", item.findtext("description") or "")[:1500],
        })
    return sorted(episodes, key=lambda e: e["date"])


def itunes_episodes(itunes_id):
    """The latest 200 episodes from Apple's lookup API, as parse_feed returns them (guid, title, date, seconds ...)."""
    data = http_json(f"https://itunes.apple.com/lookup?id={itunes_id}&entity=podcastEpisode&limit=200")
    episodes = []
    for r in data.get("results", []):
        if r.get("wrapperType") != "podcastEpisode" or not r.get("episodeGuid"):
            continue
        episodes.append({"guid": r["episodeGuid"], "title": " ".join(r["trackName"].split()),
                         "date": date.fromisoformat(r["releaseDate"][:10]), "audio_url": r.get("episodeUrl"),
                         "link": r.get("trackViewUrl", ""), "seconds": (r.get("trackTimeMillis") or 0) // 1000 or None,
                         "description": r.get("description", "")[:1500]})
    return sorted(episodes, key=lambda e: e["date"])


def podcast_episodes(podcast):
    """The podcast's episodes from its feed. Some hosts refuse the feed from GitHub's runners (Substack's api.substack.com
    answers 403); then `itunes_id` gives the same episodes via Apple, with page links from the site's own `site_feed`."""
    try:
        return parse_feed(http_get(podcast["feed"], timeout=30))
    except Exception as e:
        if not podcast.get("itunes_id"):
            raise
        warn(f"{podcast['slug']}: feed: {type(e).__name__}: {e}; using Apple's episode list instead")
    episodes = itunes_episodes(podcast["itunes_id"])
    if podcast.get("site_feed"):
        try:
            links = {e["title"]: e["link"] for e in parse_feed(http_get(podcast["site_feed"], timeout=30)) if e["link"]}
            for episode in episodes:
                episode["link"] = links.get(episode["title"], episode["link"])
        except Exception as e:
            warn(f"{podcast['slug']}: site feed: {type(e).__name__}: {e}")
    return episodes


def existing_guids(out_dir):
    """Collect the guids in the frontmatter of already saved transcripts."""
    guids = set()
    for path in out_dir.glob("*.md"):
        with path.open(encoding="utf-8") as f:
            match = re.search(r"(?m)^guid: (.+)$", "".join(itertools.islice(f, 30)))
        if match:
            guids.add(json.loads(match.group(1)))
    return guids


class TranscribeError(Exception):
    pass


def transcribe(audio, phrases, diarize):
    """Send audio to the fast transcription API with MAI-Transcribe; return the JSON result."""
    definition = {
        "enhancedMode": {
            "enabled": True,
            "model": TRANSCRIBE_MODEL,
            "modelOptions": {"timestamps": "word", "transcribeStyle": "clean"},
        },
        "diarization": {"enabled": diarize},
    }
    if phrases:
        definition["phraseList"] = {"phrases": phrases}

    boundary = uuid.uuid4().hex
    body = b"".join([
        f'--{boundary}\r\nContent-Disposition: form-data; name="definition"\r\n\r\n'.encode(),
        json.dumps(definition).encode(),
        f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="audio"; filename="episode.mp3"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n".encode(),
        audio,
        f"\r\n--{boundary}--\r\n".encode(),
    ])
    endpoint = os.environ["AZURE_SPEECH_ENDPOINT"].rstrip("/")
    req = urllib.request.Request(
        f"{endpoint}/speechtotext/transcriptions:transcribe?api-version={TRANSCRIBE_API_VERSION}",
        data=body,
        headers={
            "Ocp-Apim-Subscription-Key": os.environ["AZURE_SPEECH_KEY"],
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=900) as response:
            return json.load(response)
    except urllib.error.HTTPError as e:
        raise TranscribeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}") from None


def transcribe_episode(audio, phrases):
    """Transcribe with speaker labels, falling back to none if the episode is too long for diarization."""
    try:
        return transcribe(audio, phrases, diarize=True)
    except TranscribeError as e:
        if "AudioLengthLimitExceeded" not in str(e):
            raise
        warn("too long for diarization, transcribing without speaker labels")
        return transcribe(audio, phrases, diarize=False)


def format_timestamp(ms):
    """Format milliseconds as [HH:MM:SS]."""
    s = ms // 1000
    return f"[{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}]"


def guest_names(title):
    """Guests named after a " | " in the title, e.g. "Topic | Jane Doe & John Roe (CEO, Acme)"."""
    if " | " not in title:
        return []
    tail = re.sub(r"\s*\(.*?\)", "", title.rsplit(" | ", 1)[1])
    names = [n.strip() for n in re.split(r"\s*(?:&|,|\band\b)\s*", tail) if n.strip()]
    name_re = r"[A-Z][\w.'’-]+(?: [A-Z][\w.'’-]+){1,2}"
    return names if names and all(re.fullmatch(name_re, n) for n in names) else []


def speaker_names(phrases, podcast, guests=()):
    """Map diarization speaker ids to labels.

    Every speaker id that says one of the host's cues is labelled as the host,
    since the host recorded in two setups (studio intro vs. screen share) can
    get two ids. With exactly one guest, every other id is the guest.
    """
    order = list(dict.fromkeys(p["speaker"] for p in phrases if "speaker" in p))
    host = podcast.get("host")
    host_ids = set()
    if host:
        first_name = host.split()[0]
        cues = [host, f"I'm {first_name}", f"I am {first_name}", f"this is {first_name}",
                *podcast.get("host_cues", [])]
        cues = [cue.lower() for cue in cues]
        for p in phrases:
            text = p.get("text", "").lower().replace("’", "'")
            if "speaker" in p and any(cue in text for cue in cues):
                host_ids.add(p["speaker"])
    others = [sid for sid in order if sid not in host_ids]
    if len(guests) == 1:
        names = {sid: guests[0] for sid in others}
    else:
        names = {sid: f"Speaker {n}" for n, sid in enumerate(others, start=1)}
    names.update((sid, host) for sid in host_ids)
    return names


def render_transcript(result, names):
    """Render phrases as paragraphs that start with [HH:MM:SS], with speaker labels on speaker changes."""
    paragraphs, current = [], []
    speaker, start = object(), 0
    for phrase in result.get("phrases", []):
        name = names.get(phrase.get("speaker"))
        words = phrase.get("words") or [phrase]
        for word in words:
            text = word["text"].strip()
            if not text:
                continue
            offset = word["offsetMilliseconds"]
            new_speaker = name != speaker
            sentence_done = len(current) > 1 and current[-1].endswith((".", "?", "!"))
            if new_speaker or (sentence_done and offset - start >= PARAGRAPH_MS):
                if current:
                    paragraphs.append(" ".join(current))
                label = f"**{name}** " if new_speaker and name else ""
                current = [f"{label}{format_timestamp(offset)}"]
                speaker, start = name, offset
            current.append(text)
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs)


def parse_rendered(body):
    """Paragraphs of our own rendering: optional `**Speaker**`, then `[HH:MM:SS]`, then text. None if the body isn't in that format."""
    paragraphs = []
    for raw in body.split("\n\n"):
        m = PARAGRAPH_RE.match(raw)
        if not m:
            return None
        h, mi, sec = m["ts"].split(":")
        sentences = SENTENCE_SPLIT_RE.split(m["text"].strip())
        paragraphs.append({"raw": raw, "speaker": m["speaker"], "ts": m["ts"], "marker": "", "sponsor_marker": False,
                           "sentences": sentences, "secs": [int(h) * 3600 + int(mi) * 60 + int(sec)] * len(sentences)})
    return paragraphs, ["\n\n"] * (len(paragraphs) - 1)


def parse_published(body):
    """Paragraphs of a show's own transcript: blank-line separated, [HH:MM:SS] inline, optional edit marker and speaker label."""
    parts = re.split(r"(\n{2,})", body)
    paragraphs, now = [], 0
    for raw in parts[::2]:
        text = raw
        marker = EDIT_MARKER_RE.match(text)
        text = text[marker.end():] if marker else text
        speaker = SPEAKER_LABEL_RE.match(text)
        text = text[speaker.end():] if speaker else text
        sentences, secs = SENTENCE_SPLIT_RE.split(text.strip()), []
        for sentence in sentences:
            stamps = TS_RE.findall(sentence)
            if stamps:
                now = int(stamps[-1][0]) * 3600 + int(stamps[-1][1]) * 60 + int(stamps[-1][2])
            secs.append(now)
        paragraphs.append({"raw": raw, "speaker": speaker[0] if speaker else None, "ts": None,
                           "marker": marker[0] if marker else "", "sponsor_marker": bool(SPONSOR_MARKER_RE.match(raw)),
                           "sentences": sentences, "secs": secs})
    return paragraphs, parts[1::2]


def rule_ads(sentences, text, secs, podcast, forced_starts=()):
    """Sentence indexes of sponsor reads found by the podcast's ad_*_cues.

    An ad starts at the first sentence with one of the ad_start_cues and ends at
    the first sentence with a web address or one of the ad_end_cues, plus
    trailing "That's <spelled address>" and ad_tail_cues sentences. Ads without
    a recognised end are kept, with a warning.
    """
    def has(sentence, cues):
        sentence = sentence.lower().replace("’", "'")
        return any(cue.lower().replace("’", "'") in sentence for cue in cues)

    start_cues = podcast.get("ad_start_cues", [])
    end_cues = podcast.get("ad_end_cues", [])
    tail_cues = podcast.get("ad_tail_cues", [])
    removed, k = set(), 0
    while k < len(sentences):
        if k not in forced_starts and not has(text(k), start_cues):
            k += 1
            continue
        end = next((e for e in range(k, min(len(sentences), k + MAX_AD_SENTENCES))
                    if secs(e) - secs(k) <= MAX_AD_SECONDS
                    and (DOMAIN_RE.search(text(e)) or has(text(e), end_cues))), None)
        if end is None:
            warn(f"sponsor read at {format_timestamp(secs(k) * 1000)}: no end found, kept")
            k += 1
            continue
        while end + 1 < len(sentences) and (SPELLED_DOMAIN_RE.match(text(end + 1)) or has(text(end + 1), tail_cues)):
            end += 1
        removed.update(range(k, end + 1))
        k = end + 1
    return removed


_jev_lock = threading.Lock()
_jev_next = [0.0]


def jev_call(state, questions):
    """One System One request to TypeSafe (Jev), paced and with retries on rate limits and server errors."""
    request = urllib.request.Request(
        JEV_URL,
        data=json.dumps({"state": state, "model": JEV_MODEL, "questions": questions}).encode(),
        headers={"Authorization": f"Bearer {os.environ['TYPESAFE_API_KEY']}", "Content-Type": "application/json"},
    )
    for attempt in range(6):
        with _jev_lock:
            now = time.monotonic()
            wait = max(0.0, _jev_next[0] - now)
            _jev_next[0] = max(now, _jev_next[0]) + JEV_MIN_INTERVAL
        time.sleep(wait)
        delay = min(2 ** attempt, 30)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)["answers"]
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 529) or attempt == 5:
                raise
            delay = max(delay, int(e.headers.get("retry-after", 0) or 0))
        except (urllib.error.URLError, TimeoutError):
            if attempt == 5:
                raise
        time.sleep(delay)


def jev_scores(sentences, text, skip=()):
    """P(sentence is part of a sponsor read) per sentence index, from Jev, with two sentences of context on each side."""
    def judge(k):
        state = {"before": [text(i) for i in range(max(0, k - 2), k)], "sentence": text(k),
                 "after": [text(i) for i in range(k + 1, min(len(sentences), k + 3))]}
        answers = jev_call(state, {"ad": {"type": "noul", "instructions": JEV_AD_QUESTION, "criteria": JEV_AD_CRITERIA}})
        return answers["ad"]["noul"]

    todo = [k for k in range(len(sentences)) if k not in skip]
    with ThreadPoolExecutor(max_workers=8) as pool:
        return dict(zip(todo, pool.map(judge, todo)))


def jev_ads(sentences, secs, scores, near=(), sponsor=lambda k: False, anchored=lambda k: True):
    """Sentence indexes of sponsor reads according to Jev's scores.

    Code, not Jev, decides what gets cut: sentences scoring >= JEV_AD_THRESHOLD seed a read, runs
    separated by at most JEV_MAX_GAP sentences are joined, a read needs >= JEV_MIN_FLAGGED flagged
    sentences (or to touch a cue-detected ad in `near`), must fit in MAX_AD_SECONDS and must contain an
    anchor (`anchored`: a web address or a sponsor's name), since ad-like copy elsewhere (a quoted
    product announcement, say) has neither. A read then
    grows outwards over sentences scoring >= JEV_EDGE_THRESHOLD, since Jev is least sure at the edges,
    and over up to JEV_SPONSOR_REACH sentences that name a sponsor.
    """
    n = len(sentences)
    flagged = [k for k in range(n) if scores.get(k, 0) >= JEV_AD_THRESHOLD]
    groups = []
    for k in flagged:
        if groups and k - groups[-1][-1] <= JEV_MAX_GAP + 1 and secs(k) - secs(groups[-1][0]) <= MAX_AD_SECONDS:
            groups[-1].append(k)
        else:
            groups.append([k])
    removed = set()
    for group in groups:
        touches_cue = any(abs(k - c) <= 2 for k in (group[0], group[-1]) for c in near)
        if len(group) < JEV_MIN_FLAGGED and not touches_cue:
            continue
        if not any(anchored(k) for k in range(group[0], group[-1] + 1)):
            continue
        start, end = group[0], group[-1]
        reach = JEV_SPONSOR_REACH
        while start > 0 and secs(end) - secs(start - 1) <= MAX_AD_SECONDS:
            if scores.get(start - 1, 0) >= JEV_EDGE_THRESHOLD:
                start -= 1
            elif reach and sponsor(start - 1):
                start, reach = start - 1, reach - 1
            else:
                break
        reach = JEV_SPONSOR_REACH
        while end + 1 < n and secs(end + 1) - secs(start) <= MAX_AD_SECONDS:
            if scores.get(end + 1, 0) >= JEV_EDGE_THRESHOLD:
                end += 1
            elif reach and sponsor(end + 1):
                end, reach = end + 1, reach - 1
            else:
                break
        removed.update(range(start, end + 1))
    return removed


class Sentences:
    """Flat view of a parsed body: sentence k is paragraphs[i]['sentences'][j]. text() is clean text for cues and Jev."""

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
        self.index = [(i, j) for i, p in enumerate(paragraphs) for j in range(len(p["sentences"]))]

    def __len__(self):
        return len(self.index)

    def text(self, k):
        i, j = self.index[k]
        return TS_RE.sub("", self.paragraphs[i]["sentences"][j]).strip()

    def secs(self, k):
        i, j = self.index[k]
        return self.paragraphs[i]["secs"][j]

    def forced_starts(self):
        return {k for k, (i, j) in enumerate(self.index) if j == 0 and self.paragraphs[i]["sponsor_marker"]}


def detect_ads(flat, podcast, use_jev=True):
    """Returns (cue-found, Jev-found, scores) as sets of sentence indexes."""
    cues = rule_ads(flat.index, flat.text, flat.secs, podcast, flat.forced_starts())
    jev, scores = set(), {}
    if use_jev and os.environ.get("TYPESAFE_API_KEY"):
        scores = jev_scores(flat.index, flat.text, skip=cues)
        sponsors = [re.compile(rf"\b{re.escape(name)}\b") for name in podcast.get("ad_sponsors", [])]
        named = lambda k: any(r.search(flat.text(k)) for r in sponsors)
        jev = jev_ads(flat.index, flat.secs, scores, near=cues, sponsor=named,
                      anchored=lambda k: named(k) or bool(DOMAIN_RE.search(flat.text(k))))
    return cues, jev, scores


def parse_body(body, source):
    return (parse_published if source == "published" else parse_rendered)(body)


def strip_ads(body, podcast, strict=False):
    """Remove sponsor reads from a transcript body: first by the podcast's cues, then, if TYPESAFE_API_KEY is set, by Jev.

    Untouched paragraphs are kept byte for byte. With strict=True a Jev failure raises instead of falling back to cues.
    """
    source = podcast["source"]
    if podcast.get("strip_ads") is False:
        return body
    parsed = parse_body(body, source)
    if parsed is None:
        return body
    paragraphs, separators = parsed
    flat = Sentences(paragraphs)
    try:
        cues, jev, _ = detect_ads(flat, podcast)
    except Exception as e:
        if strict:
            raise
        warn(f"Jev sponsor detection failed, using cues only: {type(e).__name__}: {e}")
        cues, jev, _ = detect_ads(flat, podcast, use_jev=False)
    removed = {flat.index[k] for k in cues | jev}

    out, pending_speaker = [], None
    for i, p in enumerate(paragraphs):
        kept = [(j, s) for j, s in enumerate(p["sentences"]) if (i, j) not in removed]
        if not kept:
            pending_speaker = p["speaker"] or pending_speaker
            out.append(None)
            continue
        if len(kept) == len(p["sentences"]) and not (pending_speaker and not p["speaker"]):
            out.append(p["raw"])
        else:
            speaker = p["speaker"] or pending_speaker
            text = " ".join(s for _, s in kept)
            if source == "published":
                out.append((p["marker"] if kept[0][0] == 0 else "") + (speaker or "") + text)
            else:
                out.append(f"{f'**{speaker}** ' if speaker else ''}[{p['ts']}] {text}")
        pending_speaker = None

    result = []
    for i, paragraph in enumerate(out):
        if paragraph is not None:
            result.append(paragraph)
            if i < len(separators) and any(q is not None for q in out[i + 1:]):
                result.append(separators[i])
    return "".join(result)


def check_ads(path, podcast):
    """Print the sponsor reads that the cues and Jev find in a transcript file. Writes nothing."""
    body = read_doc(Path(path))[1]
    flat = Sentences(parse_body(body, podcast["source"])[0])
    cues, jev, scores = detect_ads(flat, podcast)
    for name, removed in {"cues": cues, "jev": jev}.items():
        if name == "jev" and not scores:
            continue
        runs = []
        for k in sorted(removed):
            if runs and runs[-1][-1] == k - 1:
                runs[-1].append(k)
            else:
                runs.append([k])
        print(f"{Path(path).name} [{name}]: {len(runs)} sponsor reads, {len(removed)} sentences")
        for run in runs:
            print(f"  {format_timestamp(flat.secs(run[0]) * 1000)} {len(run)} sentences: "
                  f"{flat.text(run[0])[:70]} … {flat.text(run[-1])[-70:]}")
    for k in range(len(flat)):
        if 0.1 <= scores.get(k, 0) < JEV_AD_THRESHOLD:
            print(f"  borderline {format_timestamp(flat.secs(k) * 1000)} p={scores[k]:.2f} {flat.text(k)[:80]}")


def clean_ads(out_dir, podcast):
    """Re-run sponsor removal over a podcast's saved transcripts. Needs Jev to succeed: a file where it fails is left alone."""
    changed = 0
    for path in sorted(out_dir.glob("*.md")):
        meta, body = read_doc(path)
        try:
            new = strip_ads(body, podcast, strict=True)
        except Exception as e:
            warn(f"{path.name}: skipped, {type(e).__name__}: {e}")
            continue
        if new != body:
            path.write_text(render_doc(meta, new), encoding="utf-8", newline="\n")
            print(f"cleaned {path.name}: {len(body) - len(new)} characters removed")
            changed += 1
    return changed


# --- episode metadata ----------------------------------------------------------

def load_vocabulary():
    return tomllib.loads((ROOT / "vocabulary.toml").read_text(encoding="utf-8"))


def find_terms(text, vocabulary):
    """Count mentions per canonical technology term. Longest alias wins, so "Claude Code" is not also "Claude"."""
    spans = []
    for exact in (False, True):
        names = {}
        for term in vocabulary["term"]:
            if bool(term.get("exact_case")) == exact:
                for alias in [term["name"], *term.get("aliases", [])]:
                    names[alias if exact else alias.lower()] = term["name"]
        if names:
            pattern = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(a) for a in sorted(names, key=len, reverse=True))
                                 + r")(?![\w-])", 0 if exact else re.IGNORECASE)
            spans += [(m.start(), m.end(), names[m.group(0) if exact else m.group(0).lower()]) for m in pattern.finditer(text)]
    counts, taken_until = collections.Counter(), -1
    for start, end, name in sorted(spans, key=lambda x: (x[0], -(x[1] - x[0]))):
        if start >= taken_until:
            counts[name] += 1
            taken_until = end
    return counts


def episode_text(body):
    """Transcript text for Jev and term matching: no timestamps, edit markers or speaker labels."""
    text = TS_RE.sub("", body)
    text = re.sub(r"(?m)^(?:[\w .]{1,40}_EDIT:\s*)?(?:\*\*[^*]+\*\*|Nathaniel Whittemore(?:'s audio recording)?:|Speaker \d*:)\s*", "", text)
    text = re.sub(r"(?m)^[\w .]{1,40}_EDIT:\s*", "", text)
    return re.sub(r"[ \t]+", " ", re.sub(r"\n{2,}", "\n", text)).strip()


def metadata_fields(title, date_str, body, podcast):
    """Jev-judged metadata for one episode: format, level, length, categories, featured and mentioned technologies."""
    vocabulary = load_vocabulary()
    text = episode_text(body)
    if len(text) > META_MAX_CHARS:
        text = text[:META_MAX_CHARS // 2] + "\n[...]\n" + text[-META_MAX_CHARS // 2:]
    counts = find_terms(text, vocabulary)
    candidates = [(name, n) for name, n in counts.most_common(META_MAX_CANDIDATES) if n >= 2]

    questions = {}
    for name, category in vocabulary["categories"].items():
        questions[f"cat:{name}"] = {"type": "noul", "instructions": category["question"].replace("the episode", "`transcript`")}
    questions["format"] = {"type": "choice", "instructions": "Which format is the episode in `transcript`?",
                           "criteria": dict(vocabulary["formats"])}
    levels = list(vocabulary["levels"].values())
    questions["level"] = {"type": "score", "instructions": "How technical is the episode in `transcript`?", "criteria": levels}
    for i, (name, _) in enumerate(candidates):
        questions[f"tech:{i}"] = {"type": "noul", "instructions":
                                  f"Is {name} one of the main subjects of `transcript`, discussed at length rather than only mentioned in passing?"}
    answers = jev_call({"title": title, "date": date_str, "transcript": text}, questions)

    categories = sorted((n for n in vocabulary["categories"] if answers[f"cat:{n}"]["noul"] >= 0.5),
                        key=lambda n: -answers[f"cat:{n}"]["noul"])[:META_MAX_CATEGORIES]
    companies = {t["name"] for t in vocabulary["term"] if t["kind"] == "company"}
    # Companies are discussed in nearly every episode, so they only count as featured when Jev is quite sure
    featured = [name for i, (name, _) in enumerate(candidates)
                if answers[f"tech:{i}"]["noul"] >= (META_COMPANY_THRESHOLD if name in companies else 0.5)]
    mentioned = [name for name, _ in candidates if name not in featured and name not in companies]
    stamps = TS_RE.findall(body)
    return {"format": answers["format"]["choice"], "level": round(answers["level"]["score"]),
            "length": ":".join(stamps[-1]) if stamps else None,
            "categories": categories, "featured": featured, "mentioned": mentioned}


def add_metadata(out_dir, podcast, force=False):
    """Add (or with force, redo) the Jev metadata of saved transcripts. Returns number of files written."""
    count = 0
    for path in sorted(out_dir.glob("*.md")):
        meta, body = read_doc(path)
        if "categories" in meta and not force:
            continue
        try:
            guests = speaker_guests(body, podcast) if podcast.get("hosts") else guest_names(meta["title"])
            meta = {**meta, "guests": guests, **metadata_fields(meta["title"], meta["date"], body, podcast)}
        except Exception as e:
            warn(f"{path.name}: no metadata, {type(e).__name__}: {e}")
            continue
        path.write_text(render_doc(meta, body), encoding="utf-8", newline="\n")
        print(f"metadata {path.name}")
        count += 1
    return count


def fetch_rss(podcast, out_dir, since, until, limit, dry_run):
    """Transcribe new episodes from the podcast's RSS feed. Returns number saved."""
    try:
        episodes = parse_feed(http_get(podcast["feed"], timeout=30))
    except Exception as e:
        warn(f"{podcast['slug']}: feed: {type(e).__name__}: {e}")
        return 0

    done = existing_guids(out_dir)
    todo = [e for e in episodes if since <= e["date"] <= until and e["guid"] not in done]
    if limit is not None:
        todo = todo[:limit]
    if dry_run:
        for episode in todo:
            print(f"would transcribe {episode['date']}: {episode['title']}")
        return 0
    if todo and not (os.environ.get("AZURE_SPEECH_KEY") and os.environ.get("AZURE_SPEECH_ENDPOINT")):
        warn(f"{podcast['slug']}: {len(todo)} episodes waiting, but AZURE_SPEECH_KEY/AZURE_SPEECH_ENDPOINT is not set")
        return 0

    count = 0
    for episode in todo:
        date_str = episode["date"].isoformat()
        try:
            audio = http_get(episode["audio_url"], timeout=300)
            result = transcribe_episode(audio, podcast.get("phrases"))
        except Exception as e:
            warn(f"{date_str} {episode['title']}: {type(e).__name__}: {e}")
            continue

        names = speaker_names(result.get("phrases", []), podcast, guest_names(episode["title"]))
        body = strip_ads(render_transcript(result, names), podcast)
        meta = try_metadata(episode_meta(podcast, episode["title"], date_str, episode["link"] or None, episode["guid"],
                                         transcript_source="azure-asr", transcribed_by=TRANSCRIBE_MODEL), body, podcast)
        title = sanitize_filename(episode["title"]) or date_str
        (out_dir / f"{date_str} - {title}.md").write_text(render_doc(meta, body), encoding="utf-8", newline="\n")
        print(f"saved {date_str}: {title}")
        count += 1

    return count


# --- catalog --------------------------------------------------------------------

CATALOG_FIELDS = ["podcast", "date", "title", "guests", "format", "level", "length", "categories", "featured", "mentioned", "url"]


def build_catalog():
    """catalog.json and catalog.csv: one row per episode with its frontmatter, newest first. Returns the number of rows."""
    rows = []
    for path in sorted((ROOT / "transcripts").glob("*/*.md")):
        try:
            meta, _ = read_doc(path)
        except ValueError as e:
            warn(f"catalog: {e}")
            continue
        rows.append({**{key: meta.get(key) for key in CATALOG_FIELDS}, "path": path.relative_to(ROOT).as_posix()})
    rows.sort(key=lambda r: (r["date"], r["podcast"]), reverse=True)
    (ROOT / "catalog.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    with (ROOT / "catalog.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[*CATALOG_FIELDS, "path"], lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: "; ".join(v) if isinstance(v, list) else ("" if v is None else v) for k, v in row.items()})
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Fetch new transcripts for the podcasts in podcasts.toml")
    parser.add_argument("--podcast", help="Only process the podcast with this slug")
    parser.add_argument("--since", help="Start date YYYY-MM-DD (default: the podcast's since, "
                        f"or the last {LOOKBACK_DAYS} days for published transcripts)")
    parser.add_argument("--until", help="End date YYYY-MM-DD (default: today)")
    parser.add_argument("--limit", type=int, help="Max new transcripts per podcast")
    parser.add_argument("--dry-run", action="store_true",
                        help="List RSS episodes that would be transcribed, without downloading or transcribing")
    parser.add_argument("--check-ads", nargs="+", metavar="FILE",
                        help="Print the sponsor reads found in these transcript files (needs --podcast), then exit")
    parser.add_argument("--clean-ads", action="store_true",
                        help="Re-run sponsor removal over the saved transcripts of --podcast (needs TYPESAFE_API_KEY), then exit")
    parser.add_argument("--add-metadata", action="store_true",
                        help="Add the metadata block to saved transcripts of --podcast that lack one (needs TYPESAFE_API_KEY), then exit")
    parser.add_argument("--force", action="store_true", help="With --add-metadata: redo transcripts that already have one")
    parser.add_argument("--probe", nargs="+", metavar="URL",
                        help="Print the HTTP status and size of these URLs as this machine sees them (for debugging blocked feeds), then exit")
    args = parser.parse_args()

    # Episode titles can contain characters a Windows console can't encode
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(errors="replace")

    try:
        since_arg = parse_date(args.since) if args.since else None
        until = parse_date(args.until) if args.until else date.today()
    except ValueError as e:
        print(f"Error parsing dates: {e}", file=sys.stderr)
        sys.exit(1)

    if args.probe:
        agents = {"PodScribe": USER_AGENT, "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
                  "apple": "Podcasts/1.0 CFNetwork/1494 Darwin/23.4.0"}
        for url in args.probe:
            for label, agent in agents.items():
                try:
                    request = urllib.request.Request(url, headers={"User-Agent": agent, "Accept": "application/rss+xml, application/xml, */*"})
                    with urllib.request.urlopen(request, timeout=30) as response:
                        print(f"{response.status} {len(response.read())} bytes  [{label}] {url}")
                except Exception as e:
                    print(f"{getattr(e, 'code', type(e).__name__)}  [{label}] {url}")
        sys.exit(0)

    podcasts = tomllib.loads((ROOT / "podcasts.toml").read_text(encoding="utf-8"))["podcast"]
    if args.podcast:
        podcasts = [p for p in podcasts if p["slug"] == args.podcast]
        if not podcasts:
            print(f"Unknown podcast: {args.podcast}", file=sys.stderr)
            sys.exit(1)

    if args.check_ads:
        if len(podcasts) != 1:
            print("--check-ads needs --podcast", file=sys.stderr)
            sys.exit(1)
        for path in args.check_ads:
            check_ads(path, podcasts[0])
        sys.exit(0)

    if args.clean_ads:
        if len(podcasts) != 1 or not os.environ.get("TYPESAFE_API_KEY"):
            print("--clean-ads needs --podcast and TYPESAFE_API_KEY", file=sys.stderr)
            sys.exit(1)
        print(f"{clean_ads(ROOT / 'transcripts' / podcasts[0]['slug'], podcasts[0])} transcripts cleaned")
        build_catalog()
        sys.exit(0)

    if args.add_metadata:
        if len(podcasts) != 1 or not os.environ.get("TYPESAFE_API_KEY"):
            print("--add-metadata needs --podcast and TYPESAFE_API_KEY", file=sys.stderr)
            sys.exit(1)
        print(f"{add_metadata(ROOT / 'transcripts' / podcasts[0]['slug'], podcasts[0], args.force)} transcripts got metadata")
        build_catalog()
        sys.exit(0)

    total = 0
    for podcast in podcasts:
        out_dir = ROOT / "transcripts" / podcast["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        floor = podcast.get("since", date.min)

        if podcast["source"] == "published":
            if args.dry_run:
                continue
            since = since_arg or max(floor, until - timedelta(days=LOOKBACK_DAYS))
            count = fetch_published(podcast, out_dir, since, until, args.limit)
        elif podcast["source"] == "substack":
            count = fetch_substack(podcast, out_dir, since_arg or floor, until, args.limit, args.dry_run)
        elif podcast["source"] == "folder":
            count = fetch_folder(podcast, out_dir, since_arg or floor, until, args.limit, args.dry_run)
        elif podcast["source"] == "rss":
            since = since_arg or floor
            count = fetch_rss(podcast, out_dir, since, until, args.limit, args.dry_run)
        else:
            warn(f"{podcast['slug']}: unknown source {podcast['source']!r}")
            continue

        if not args.dry_run:
            print(f"{podcast['slug']}: {count} new")
        total += count

    if not args.dry_run:
        build_catalog()
    print(f"{total} new transcripts")
    sys.exit(0)


if __name__ == "__main__":
    main()
