# PodScribe

An archive of transcripts from AI podcasts. New episodes are fetched or transcribed automatically every day.

## Podcasts

| Podcast | Folder | Source | Since |
|---|---|---|---|
| [The AI Daily Brief](https://aidailybrief.ai/) (NLW) | `transcripts/ai-daily-brief/` | Transcripts published by the show | 2026-06-01 |
| [Lenny's Podcast](https://www.lennysnewsletter.com/podcast) (Lenny Rachitsky) | `transcripts/lennys-podcast/` | Transcripts from a shared folder, matched to episodes via the podcast feed | 2026-01-01 |
| [How I AI](https://podcasts.apple.com/us/podcast/how-i-ai/id1809663079) (Claire Vo) | `transcripts/how-i-ai/` | Transcribed from the audio with Azure MAI-Transcribe | 2026-09-01 |
| [Latent Space](https://www.latent.space/) (Swyx & Alessio) | `transcripts/latent-space/` | Transcripts published in the show's Substack posts | 2026-06-01 |

## Credits and Rights

The transcripts belong to the people who made the podcasts.

- **Lenny's Podcast:** © Lenny Rachitsky. He [shares the full transcripts publicly](https://x.com/lennysan/status/2011243567340298651) and invites people to use them with AI, and keeps that folder updated. The files here come from it, with title, date and link from the podcast feed.
- **The AI Daily Brief:** the show publishes its transcripts itself (for people and agents, see [`llms.txt`](https://aidailybrief.ai/llms.txt)). Sponsor reads have been removed.
- **Latent Space:** the transcripts are published in the show's own posts.
- **How I AI:** © Claire Vo. There are no published transcripts, so these are machine-made from the audio.

Each file names its source in the frontmatter (`url`, and `credit` where one is needed). If you made one of these podcasts and want something changed or removed, open an issue.

Use this archive to search, summarize, or ask questions across episodes — great for feeding into Claude, NotebookLM, or any search/RAG setup.

## File Layout

```
transcripts/
  ai-daily-brief/
    2026-06-01 - The AI Token Shortage Begins.md
    ...
  how-i-ai/
    2026-09-02 - Grok Bot vs. OpenClaw- How I replaced my entire agent stack.md
    ...
  latent-space/
    2026-09-21 - Jev- System One models for Prod, not God — with Diogo Almeida, CEO, TypeSafe AI.md
    ...
```

Each file is named `YYYY-MM-DD - Episode Title.md`. Characters unsafe in filenames (`/ \ : * ? " < > |`) are replaced with `-`.

Each file starts with YAML frontmatter, then the title, then the full transcript with `[HH:MM:SS]` timestamps:

```markdown
---
podcast: "ai-daily-brief"
title: "Grok 4.6 Shows How Fast Your AI Options Are Expanding"
date: 2026-08-13
url: "https://aidailybrief.ai/e/2026-08-13"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 2
categories: ["models", "funding-markets", "coding", "open-weights"]
featured: ["Grok", "SpaceX AI", "Claude Fable", "GPT-5.6", "DeepSeek"]
mentioned: ["Cursor", "Claude Code", "Kimi"]
...
---

# Grok 4.6 Shows How Fast Your AI Options Are Expanding

[00:00:00] A year ago, if you were talking about frontier models, ...
```

| Field | Meaning |
|---|---|
| `podcast`, `podcast_title`, `title`, `date`, `url`, `guid` | Where the episode comes from |
| `host`, `guests` | Host from the config; guests from the title or the speaker labels |
| `format` | `news-roundup`, `news-analysis`, `commentary`, `review`, `tutorial`, `demo` or `interview` |
| `level` | 0 general audience, 1 informed business/tech audience, 2 semi-technical, 3 hands-on |
| `length` | Approximate: the last timestamp in the transcript |
| `categories` | Up to 4 topics, strongest first (see [`vocabulary.toml`](vocabulary.toml) for the list) |
| `featured`, `mentioned` | Technologies the episode is about / only mentions |
| `transcript_source`, `transcribed_by` | `publisher` (the show's own transcript), `shared-folder` (provided as a file) or `azure-asr` (transcribed here) |

`format`, `level`, `categories`, `featured` and `mentioned` are judged by a small classification model ([Jev](https://typesafe.ai)) against the vocabulary, so treat them as good filters, not as facts. Sponsor reads have been removed from the text.

Speaker labels: in the episodes transcribed here (How I AI) the host is named and other voices are `Speaker 1`, `Speaker 2`, … or the guest's name. Labels are machine-generated and can occasionally be wrong.

## Using the Archive

The archive is plain text on purpose, so you can point whatever tool you like at it.

**[`catalog.csv`](catalog.csv) / [`catalog.json`](catalog.json)** list every episode with its metadata and file path, newest first. Open the CSV in a spreadsheet, or give the JSON to an LLM, to see what's here and pick episodes before reading anything.

Some ways to use it:

- **Claude Code, Cursor or another coding agent:** open the folder and ask questions ("what did the podcasts say about model routing in September?"). The catalog tells the agent which files matter.
- **Obsidian or any Markdown editor:** open the folder as a vault. The frontmatter works as properties.
- **Command line:** `grep -ril "judgment model" transcripts/` or `rg -n "token budget" transcripts/ -g '*.md'`. Timestamps are on every paragraph.
- **Spreadsheet or pandas:** `pd.read_json("catalog.json")`, then filter on `categories`, `featured`, `level` or `guests`.
- **NotebookLM or ChatGPT projects:** upload a handful of episodes picked from the catalog.
- **Your own search:** [`examples/search.py`](examples/search.py) builds a local full-text index (SQLite) with the frontmatter as filters, e.g. `python3 examples/search.py "token budget" --category enterprise --since 2026-08-01`. It is an example to copy and change, not part of the archive.

Search is deliberately left out of this repo, so everyone can decide how they want to search and what is relevant to them.

## How It Works

A GitHub Actions workflow (`.github/workflows/fetch.yml`) runs `fetch_transcripts.py` daily. The script reads [`podcasts.toml`](podcasts.toml) and handles each podcast according to its `source`:

- **`published`** — the show publishes its own transcripts at one URL per date. The script checks the last 30 days and downloads any that aren't in the archive yet. Not every date has an episode.
- **`substack`** — the show's posts on a Substack publication include the transcript. The script lists the publication's podcast posts, and saves those that have a transcript and aren't in the archive yet (some posts only have show notes).
- **`folder`** — the transcripts are plain-text files in a shared Dropbox folder, named after the guest. The script matches each file to an episode in the podcast's RSS feed (by guest name and episode length) and takes title, date and link from the feed. The folder link is a repository secret.
- **`rss`** — the script reads the podcast's RSS feed, downloads the audio of new episodes and transcribes it with [MAI-Transcribe](https://learn.microsoft.com/azure/ai-services/speech-service/mai-transcribe) through Azure Speech's fast transcription API, with speaker diarization.

New transcripts are committed and pushed to this repo, and `catalog.csv`/`catalog.json` are rebuilt.

## Adding a Podcast

Add a `[[podcast]]` block to `podcasts.toml`. For a show without published transcripts, all you need is its RSS feed:

```toml
[[podcast]]
slug = "my-podcast"            # folder name under transcripts/
name = "My Podcast"
source = "rss"
feed = "https://example.com/feed.xml"
since = 2026-10-01             # first episode date to include
host = "Jane Doe"              # optional: labels the host by name
phrases = ["Jane Doe", "MCP"]  # optional: names and jargon to favour
```

## Running Locally

```bash
# Fetch and transcribe everything new
python3 fetch_transcripts.py

# One podcast, a date range, at most 2 new episodes
python3 fetch_transcripts.py --podcast how-i-ai --since 2026-09-01 --until 2026-09-30 --limit 2

# See which episodes would be transcribed, without downloading or transcribing
python3 fetch_transcripts.py --dry-run
```

Transcribing `rss` podcasts needs two environment variables from a Microsoft Foundry (Speech) resource in a [region that supports MAI-Transcribe](https://learn.microsoft.com/azure/ai-services/speech-service/regions?tabs=llmspeech):

- `AZURE_SPEECH_KEY` — the resource key
- `AZURE_SPEECH_ENDPOINT` — e.g. `https://<resource-name>.cognitiveservices.azure.com`

In GitHub Actions these are repository secrets. A manual run can pass extra arguments via the workflow's `args` input.

No dependencies — uses only the Python 3.11+ standard library.

## Using the Archive

Point your favorite AI tool at the `transcripts/` directory (or a single podcast's folder):

- **Claude/Claude.ai**: Ask Claude to analyze the full directory
- **NotebookLM**: Upload episodes or entire folder for interactive summaries
- **RAG/Search**: Index `transcripts/` with any embedding or search tool
- **Local search**: `grep -r "keyword" transcripts/` to find mentions across all episodes

## Credit & Disclaimer

All transcript content belongs to the respective shows and hosts: The AI Daily Brief and NLW; How I AI and Claire Vo. This is an **unofficial, community-maintained archive** — not affiliated with or endorsed by any of the shows. Transcripts made with MAI-Transcribe are machine-generated and may contain errors. Use respectfully and in accordance with each show's licensing terms.

---

Questions? Open an issue. Want to contribute? PRs welcome.
