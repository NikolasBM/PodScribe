# The AI Daily Brief Transcripts

An archive of transcripts from [The AI Daily Brief](https://aidailybrief.ai/) podcast, hosted by NLW. Transcripts are automatically fetched and updated daily.

## What's Here

This repo contains plain-text markdown transcripts of The AI Daily Brief episodes, organized by date. Each episode includes:

- Episode title (first line)
- Full transcript with `[HH:MM:SS]` timestamp markers throughout

Use this archive to search, summarize, or ask questions across episodes — great for feeding into Claude, NotebookLM, or any search/RAG setup.

## File Layout

```
episodes/
  2026-06-01 - The AI Token Shortage Begins.md
  2026-06-02 - With AI IPOs On the Way, Should the Public Own AI Companies-.md
  ...
  2026-08-02 - Everything You Need to Know About AI Tokens.md
```

Each file is named `YYYY-MM-DD - Episode Title.md`. Characters unsafe in filenames (`/ \ : * ? " < > |`) are replaced with `-`.

## How It Works

A GitHub Actions workflow (`.github/workflows/fetch.yml`) runs daily:

1. Checks for new transcripts at `https://aidailybrief.ai/e/YYYY-MM-DD/transcript.md`
2. Downloads any it finds that aren't already in the archive
3. Commits them with a timestamp
4. Pushes to this repo

Note: not every date has a published transcript (the show doesn't air every day).

## Running Locally

To fetch transcripts on your machine:

```bash
# Backfill from a specific date
python3 fetch_transcripts.py --since 2023-01-01

# Catch up on the last 30 days
python3 fetch_transcripts.py
```

No dependencies — uses only Python 3 stdlib.

## Using the Archive

Point your favorite AI tool at the `episodes/` directory:

- **Claude/Claude.ai**: Ask Claude to analyze the full directory
- **NotebookLM**: Upload episodes or entire folder for interactive summaries
- **RAG/Search**: Index `episodes/` with any embedding or search tool
- **Local search**: `grep -r "keyword" episodes/` to find mentions across all episodes

## Credit & Disclaimer

All transcript content belongs to The AI Daily Brief and NLW. This is an **unofficial, community-maintained archive** — not affiliated with or endorsed by the show. Use respectfully and in accordance with the show's licensing terms.

---

Questions? Open an issue. Want to contribute? PRs welcome.
