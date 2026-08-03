# aidb-transcripts

Arkiv af "The AI Daily Brief" podcast-transcripts (aidailybrief.ai). Autoopdateret dagligt via GitHub Actions.

## Repo
- GitHub: `github.com/NikolasBM/aidb-transcripts`, branch `main`.
- Lokal git-identitet sat **repo-lokalt** (ikke globalt): `user.name "Nikolas Manscher"`, `user.email "nikolas.manscher@gmail.com"`. Maskinen havde ingen global git-identitet ved oprettelse.

## Struktur
```
fetch_transcripts.py       — henter nye transcripts, stdlib-only
.github/workflows/fetch.yml — daglig cron (06:30 UTC) + manuel workflow_dispatch
episodes/YYYY-MM-DD - Titel.md — én fil per episode, titel både i filnavn og linje 1, [HH:MM:SS]-timestamps
README.md                   — offentlig beskrivelse af arkivet
```

## Kilde og datamønster
- URL: `https://aidailybrief.ai/e/YYYY-MM-DD/transcript.md`.
- 404 = ingen episode/transcript den dato (ikke en fejl). 200 = gemmes.
- **Ældste tilgængelige transcript er 2026-06-01** — verificeret ved probing tilbage til 2023; alt før 06-01 giver 404. Transcript.md-featuren findes ikke længere tilbage, uanset hvad man skriver i `--since`.
- Ikke alle datoer har episode selv efter 2026-06-01 (ujævn udgivelse) — det er forventet, ikke en bug i scriptet.

## fetch_transcripts.py
```
python3 fetch_transcripts.py                          # sidste 30 dage (default)
python3 fetch_transcripts.py --since 2026-06-01        # fra given dato til i dag
python3 fetch_transcripts.py --since A --until B       # specifikt interval
```
- Ingen state-fil: filer i `episodes/` er staten. Skipper datoer der allerede har en `{dato} - *.md`-fil (matcher også gammel `{dato}.md` for bagudkompatibilitet).
- Filnavn udledes af episodens titel fra transkriptets første linje (`# Titel — Transcript (dato)`). Regex-parsing, fallback til kun dato hvis linjen ikke matcher forventet format.
- Idempotent — kør vilkårligt mange gange, output slutter altid `{n} new transcripts`.
- Ingen dependencies, kun Python 3 stdlib.

## GitHub Actions
- Trigger manuelt: `gh workflow run fetch-transcripts --repo NikolasBM/aidb-transcripts`
- Tjek status: `gh run list --repo NikolasBM/aidb-transcripts --workflow=fetch.yml --limit 5`
- Workflowet committer kun hvis `episodes/` ændrer sig (git diff --cached --quiet-guard).
- Kører som `github-actions[bot]`, kræver `permissions: contents: write` (allerede sat).

## Kendte forbehold
- Scriptet retryer ikke fejlede requests (5xx/timeout) — de printes som `warn` til stderr og fanges næste kørsel, fordi filen mangler.
- Ingen rate-limit-problemer observeret ved fuld backfill (0.2s pause mellem requests, ~50 requests reelt brugt siden arkivet kun går tilbage til juni 2026).
