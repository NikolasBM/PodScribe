#!/usr/bin/env python3
"""Example: full-text search over the archive, with the frontmatter as filters. Python 3.8+, no dependencies.

    python3 examples/search.py "judgment models"                      # builds .search.db on first use
    python3 examples/search.py "token budget" --category enterprise --since 2026-08-01
    python3 examples/search.py "Claude Code" --podcast how-i-ai --featured "Claude Code" --limit 5
    python3 examples/search.py --rebuild "query"                      # after pulling new transcripts

Every paragraph of every transcript is one search row, so a hit points at a moment ([HH:MM:SS]) in an episode.
Copy this file and change it: it is a starting point, not part of the archive.
"""
import argparse
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / ".search.db"


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n\n", text, re.S)
    meta = {}
    for line in match[1].split("\n"):
        key, _, raw = line.partition(": ")
        try:
            meta[key] = json.loads(raw)
        except ValueError:
            meta[key] = raw
    return meta, text[match.end():]


def build():
    DB.unlink(missing_ok=True)
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE episodes (id INTEGER PRIMARY KEY, podcast, date, title, url, path, categories, featured, mentioned)")
    db.execute("CREATE VIRTUAL TABLE chunks USING fts5(text, episode UNINDEXED, ts UNINDEXED, tokenize='porter unicode61')")
    for path in sorted((ROOT / "transcripts").glob("*/*.md")):
        meta, body = frontmatter(path.read_text(encoding="utf-8"))
        join = lambda key: "|" + "|".join(meta.get(key) or []) + "|"
        episode = db.execute("INSERT INTO episodes VALUES (NULL,?,?,?,?,?,?,?,?)",
                             (meta["podcast"], meta["date"], meta["title"], meta.get("url"), path.relative_to(ROOT).as_posix(),
                              join("categories"), join("featured"), join("mentioned"))).lastrowid
        for paragraph in body.split("\n\n"):
            ts = re.search(r"\[(\d\d:\d\d:\d\d)\]", paragraph)
            if ts and not paragraph.startswith("## "):
                db.execute("INSERT INTO chunks VALUES (?,?,?)", (paragraph, episode, ts[1]))
    db.commit()
    return db


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query", help="FTS5 query: words, \"phrases\", OR, NEAR(a b)")
    parser.add_argument("--podcast")
    parser.add_argument("--category", help="e.g. policy, agents, coding (see vocabulary.toml)")
    parser.add_argument("--featured", help="a technology in the Featured list, e.g. Jev")
    parser.add_argument("--since")
    parser.add_argument("--until")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()

    db = build() if args.rebuild or not DB.exists() else sqlite3.connect(DB)
    where, params = ["chunks MATCH ?"], [args.query]
    for column, value in (("podcast", args.podcast), ("categories", args.category and f"%|{args.category}|%"),
                          ("featured", args.featured and f"%|{args.featured}|%")):
        if value:
            where.append(f"e.{column} {'LIKE' if '%' in value else '='} ?")
            params.append(value)
    if args.since:
        where.append("e.date >= ?"); params.append(args.since)
    if args.until:
        where.append("e.date <= ?"); params.append(args.until)
    rows = db.execute(f"""SELECT e.date, e.podcast, e.title, c.ts, snippet(chunks, 0, '[', ']', ' … ', 24), e.path
                          FROM chunks c JOIN episodes e ON e.id = c.episode
                          WHERE {' AND '.join(where)} ORDER BY bm25(chunks) LIMIT ?""", [*params, args.limit]).fetchall()
    for date, podcast, title, ts, snippet, path in rows:
        print(f"{date}  {podcast}  {title}\n  [{ts}] {snippet}\n  {path}\n")
    if not rows:
        print("no hits")


if __name__ == "__main__":
    main()
