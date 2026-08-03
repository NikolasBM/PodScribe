#!/usr/bin/env python3
import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path


def parse_date(date_str):
    """Parse YYYY-MM-DD string to date object."""
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def date_range(start_date, end_date):
    """Yield dates from start_date to end_date (inclusive)."""
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)


def fetch_transcript(date_obj, timeout=10):
    """
    Fetch transcript for a given date.
    Returns (success, body_or_error) tuple.
    - success=True, body is the transcript content
    - success=False, body is the error message
    """
    date_str = date_obj.strftime("%Y-%m-%d")
    url = f"https://aidailybrief.ai/e/{date_str}/transcript.md"

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "aidb-transcripts-archiver"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                return True, response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # 404 is expected for missing dates, return None to skip silently
            return None, None
        else:
            return False, f"HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"Network error: {e.reason}"
    except Exception as e:
        return False, f"Error: {type(e).__name__}: {str(e)}"

    return False, "Unknown error"


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
    return re.sub(r'[\\/:*?"<>|]', "-", title).strip()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch AI Daily Brief transcripts"
    )

    default_until = datetime.now().date()
    default_since = default_until - timedelta(days=30)

    parser.add_argument(
        "--since",
        type=str,
        default=default_since.strftime("%Y-%m-%d"),
        help=f"Start date (default: {default_since})"
    )
    parser.add_argument(
        "--until",
        type=str,
        default=default_until.strftime("%Y-%m-%d"),
        help=f"End date (default: {default_until})"
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="episodes",
        help="Directory to save transcripts (default: episodes)"
    )

    args = parser.parse_args()

    try:
        since_date = parse_date(args.since)
        until_date = parse_date(args.until)
    except ValueError as e:
        print(f"Error parsing dates: {e}", file=sys.stderr)
        sys.exit(1)

    # Resolve episodes directory relative to script location
    script_dir = Path(__file__).resolve().parent
    episodes_dir = script_dir / args.dir
    episodes_dir.mkdir(exist_ok=True)

    count = 0
    for date_obj in date_range(since_date, until_date):
        date_str = date_obj.strftime("%Y-%m-%d")

        # Skip if already fetched (current "date - title.md" or legacy "date.md")
        if any(episodes_dir.glob(f"{date_str} - *.md")) or (episodes_dir / f"{date_str}.md").exists():
            continue

        # Fetch transcript
        result = fetch_transcript(date_obj)
        status, content = result

        if status is None:
            # 404 — skip silently
            continue
        elif status:
            # 200 — save file
            title = sanitize_filename(extract_title(content, date_str))
            file_path = episodes_dir / f"{date_str} - {title}.md"
            file_path.write_text(content, encoding="utf-8")
            print(f"saved {date_str}: {title}")
            count += 1
        else:
            # Other error — warn to stderr
            print(f"warn {date_str}: {content}", file=sys.stderr)

        # Sleep between requests
        time.sleep(0.2)

    print(f"{count} new transcripts")
    sys.exit(0)


if __name__ == "__main__":
    main()
