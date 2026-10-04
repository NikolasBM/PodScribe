#!/usr/bin/env python3
"""Fetch new transcripts for every podcast in podcasts.toml.

Podcasts with source = "published" publish their own transcripts. Podcasts with
source = "rss" are transcribed from their RSS audio with Azure MAI-Transcribe.
"""
import argparse
import itertools
import json
import os
import re
import sys
import time
import tomllib
import urllib.error
import urllib.request
import uuid
import xml.etree.ElementTree as ET
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
GUID_RE = re.compile(r"<!-- guid: (.+?) -->")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.?!])\s+")
DOMAIN_RE = re.compile(r"\b[\w-]+\.(?:com|ai|io|dev|org)\b", re.IGNORECASE)
SPELLED_DOMAIN_RE = re.compile(r"^That's\b.*(?:\.(?:com|ai|io|dev|org)\b|\b[A-Z](?:-[A-Z])+\b)", re.IGNORECASE)
PARAGRAPH_RE = re.compile(r"^(?:\*\*(?P<speaker>[^*]+)\*\* )?\[(?P<ts>\d\d:\d\d:\d\d)\] (?P<text>.*)$", re.DOTALL)
MAX_AD_SECONDS = 240
JEV_URL = "https://api.typesafe.ai/v1/systemone"
JEV_MODEL = "jev-1.13.0"
JEV_AD_THRESHOLD = 0.5
JEV_EDGE_THRESHOLD = 0.3
JEV_MAX_GAP = 6
JEV_MIN_FLAGGED = 5
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


# --- source = "published" ---------------------------------------------------

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
            title = sanitize_filename(extract_title(content, date_str))
            (out_dir / f"{date_str} - {title}.md").write_text(content, encoding="utf-8", newline="\n")
            print(f"saved {date_str}: {title}")
            count += 1

        # Sleep between requests
        time.sleep(0.2)

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
        episodes.append({
            "guid": (item.findtext("guid") or enclosure.get("url")).strip(),
            "title": " ".join((item.findtext("title") or "").split()),
            "date": parsedate_to_datetime(pub_date).date(),
            "audio_url": enclosure.get("url"),
            "link": (item.findtext("link") or "").strip(),
        })
    return sorted(episodes, key=lambda e: e["date"])


def existing_guids(out_dir):
    """Collect the guids recorded in the header of already saved transcripts."""
    guids = set()
    for path in out_dir.glob("*.md"):
        with path.open(encoding="utf-8") as f:
            match = GUID_RE.search("".join(itertools.islice(f, 10)))
        if match:
            guids.add(match.group(1))
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


def parse_paragraphs(body):
    """Split rendered paragraphs into speaker, timestamp and sentences. None if the body isn't in that format."""
    paragraphs = []
    for raw in body.split("\n\n"):
        m = PARAGRAPH_RE.match(raw)
        if not m:
            return None
        h, mi, sec = m["ts"].split(":")
        paragraphs.append({"speaker": m["speaker"], "ts": m["ts"], "secs": int(h) * 3600 + int(mi) * 60 + int(sec),
                           "sentences": SENTENCE_SPLIT_RE.split(m["text"].strip())})
    return paragraphs


def rule_ads(sentences, text, secs, podcast):
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
        if not has(text(k), start_cues):
            k += 1
            continue
        end = next((e for e in range(k, len(sentences))
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


def jev_call(state, questions):
    """One System One request to TypeSafe (Jev). Retries rate limits and server errors."""
    request = urllib.request.Request(
        JEV_URL,
        data=json.dumps({"state": state, "model": JEV_MODEL, "questions": questions}).encode(),
        headers={"Authorization": f"Bearer {os.environ['TYPESAFE_API_KEY']}", "Content-Type": "application/json"},
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)["answers"]
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 529) or attempt == 3:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
        time.sleep(2 ** attempt)


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


def jev_ads(sentences, secs, scores, near=()):
    """Sentence indexes of sponsor reads according to Jev's scores.

    Code, not Jev, decides what gets cut: sentences scoring >= JEV_AD_THRESHOLD seed a read, runs
    separated by at most JEV_MAX_GAP sentences are joined, a read needs >= JEV_MIN_FLAGGED flagged
    sentences (or to touch a cue-detected ad in `near`) and must fit in MAX_AD_SECONDS. A read then
    grows outwards over sentences scoring >= JEV_EDGE_THRESHOLD, since Jev is least sure at the edges.
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
        start, end = group[0], group[-1]
        while start > 0 and scores.get(start - 1, 0) >= JEV_EDGE_THRESHOLD and secs(end) - secs(start - 1) <= MAX_AD_SECONDS:
            start -= 1
        while end + 1 < n and scores.get(end + 1, 0) >= JEV_EDGE_THRESHOLD and secs(end + 1) - secs(start) <= MAX_AD_SECONDS:
            end += 1
        removed.update(range(start, end + 1))
    return removed


def strip_ads(body, podcast):
    """Remove sponsor reads from rendered paragraphs: first by the podcast's cues, then, if TYPESAFE_API_KEY is set, by Jev."""
    paragraphs = parse_paragraphs(body)
    if paragraphs is None:
        return body
    sentences = [(i, j) for i, p in enumerate(paragraphs) for j in range(len(p["sentences"]))]
    text = lambda k: paragraphs[sentences[k][0]]["sentences"][sentences[k][1]]
    secs = lambda k: paragraphs[sentences[k][0]]["secs"]

    removed = rule_ads(sentences, text, secs, podcast)
    if os.environ.get("TYPESAFE_API_KEY"):
        try:
            scores = jev_scores(sentences, text, skip=removed)
            removed |= jev_ads(sentences, secs, scores, near=removed)
        except Exception as e:
            warn(f"Jev sponsor detection failed, using cues only: {type(e).__name__}: {e}")
    removed = {sentences[k] for k in removed}

    out, pending_speaker = [], None
    for i, p in enumerate(paragraphs):
        kept = [s for j, s in enumerate(p["sentences"]) if (i, j) not in removed]
        if not kept:
            pending_speaker = p["speaker"] or pending_speaker
            continue
        speaker = p["speaker"] or pending_speaker
        pending_speaker = None
        label = f"**{speaker}** " if speaker else ""
        out.append(f"{label}[{p['ts']}] {' '.join(kept)}")
    return "\n\n".join(out)


def check_ads(path, podcast):
    """Print the sponsor reads that the cues and Jev find in a transcript file. Writes nothing."""
    body = Path(path).read_text(encoding="utf-8").partition("\n---\n\n")[2].strip()
    paragraphs = parse_paragraphs(body)
    sentences = [(i, j) for i, p in enumerate(paragraphs) for j in range(len(p["sentences"]))]
    text = lambda k: paragraphs[sentences[k][0]]["sentences"][sentences[k][1]]
    secs = lambda k: paragraphs[sentences[k][0]]["secs"]
    found = {"cues": rule_ads(sentences, text, secs, podcast)}
    if os.environ.get("TYPESAFE_API_KEY"):
        scores = jev_scores(sentences, text)
        found["jev"] = jev_ads(sentences, secs, scores, near=found["cues"])
        for k in range(len(sentences)):
            if 0.1 <= scores[k] < JEV_AD_THRESHOLD:
                print(f"  borderline {format_timestamp(secs(k) * 1000)} p={scores[k]:.2f} {text(k)[:80]}")
    for name, removed in found.items():
        runs = []
        for k in sorted(removed):
            if runs and runs[-1][-1] == k - 1:
                runs[-1].append(k)
            else:
                runs.append([k])
        print(f"{Path(path).name} [{name}]: {len(runs)} sponsor reads")
        for run in runs:
            print(f"  {format_timestamp(secs(run[0]) * 1000)} {len(run)} sentences: "
                  f"{text(run[0])[:70]} … {text(run[-1])[-70:]}")


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
        source = " · ".join(filter(None, [episode["link"], podcast["name"], f"Transcribed with {TRANSCRIBE_MODEL}"]))
        content = (
            f"# {episode['title']} — Transcript ({date_str})\n\n"
            f"{source}\n\n"
            f"<!-- guid: {episode['guid']} -->\n\n"
            f"---\n\n"
            f"{strip_ads(render_transcript(result, names), podcast)}\n"
        )
        title = sanitize_filename(episode["title"]) or date_str
        (out_dir / f"{date_str} - {title}.md").write_text(content, encoding="utf-8", newline="\n")
        print(f"saved {date_str}: {title}")
        count += 1

    return count


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
        elif podcast["source"] == "rss":
            since = since_arg or floor
            count = fetch_rss(podcast, out_dir, since, until, args.limit, args.dry_run)
        else:
            warn(f"{podcast['slug']}: unknown source {podcast['source']!r}")
            continue

        if not args.dry_run:
            print(f"{podcast['slug']}: {count} new")
        total += count

    print(f"{total} new transcripts")
    sys.exit(0)


if __name__ == "__main__":
    main()
