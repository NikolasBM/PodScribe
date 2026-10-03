# PodScribe

An archive of transcripts from AI podcasts. New episodes are fetched or transcribed automatically every day.

## Podcasts

| Podcast | Folder | Source | Since |
|---|---|---|---|
| [The AI Daily Brief](https://aidailybrief.ai/) (NLW) | `transcripts/ai-daily-brief/` | Transcripts published by the show | 2026-06-01 |
| [How I AI](https://podcasts.apple.com/us/podcast/how-i-ai/id1809663079) (Claire Vo) | `transcripts/how-i-ai/` | Transcribed from the audio with Azure MAI-Transcribe | 2026-09-01 |

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
```

Each file is named `YYYY-MM-DD - Episode Title.md`. Characters unsafe in filenames (`/ \ : * ? " < > |`) are replaced with `-`.

Each file starts with the episode title, followed by the full transcript with `[HH:MM:SS]` timestamp markers. Transcribed episodes also label who is speaking: the host by name, other voices as `Speaker 1`, `Speaker 2`, … Speaker labels are machine-generated and can occasionally be wrong.

## How It Works

A GitHub Actions workflow (`.github/workflows/fetch.yml`) runs `fetch_transcripts.py` daily. The script reads [`podcasts.toml`](podcasts.toml) and handles each podcast according to its `source`:

- **`published`** — the show publishes its own transcripts at one URL per date. The script checks the last 30 days and downloads any that aren't in the archive yet. Not every date has an episode.
- **`rss`** — the script reads the podcast's RSS feed, downloads the audio of new episodes and transcribes it with [MAI-Transcribe](https://learn.microsoft.com/azure/ai-services/speech-service/mai-transcribe) through Azure Speech's fast transcription API, with speaker diarization.

New transcripts are committed and pushed to this repo.

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
