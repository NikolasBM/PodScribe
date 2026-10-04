# Arkitektur

Kort beskrivelse af hvordan arkivet er bygget og hvorfor. Detaljer og kommandoer står i `CLAUDE.md`; brugen i `README.md`.

## Principper

- **Filerne er databasen.** Én Markdown-fil pr. episode i `transcripts/<slug>/`. Ingen state-fil: en episode, der mangler, er en opgave, så hver kørsel kan gentages uden skade.
- **Ét repo, mange podcasts.** Hver podcast er en `[[podcast]]`-blok i `podcasts.toml` med en `source`, der afgør hvordan teksten hentes.
- **Skal kunne køre lokalt.** GitHub Actions er kun en cron-timer, der kører `fetch_transcripts.py` og committer. Scriptet bruger kun Python-standardbiblioteket.
- **Lyd kommer aldrig i git.** Lyd hentes til hukommelsen, transskriberes og kasseres.

## Dataflow

```
podcasts.toml ──► fetch_transcripts.py ──► transcripts/<slug>/*.md ──► catalog.csv / catalog.json
                    │  source = published   (udgiverens egen transcript-URL)
                    │  source = substack    (transcript i selve indlægget)
                    │  source = rss         (lyd → Azure MAI-Transcribe, diarization)
                    ├─ strip_ads   (cues + Jev; fjerner sponsorreads)
                    └─ metadata    (vocabulary.toml + Jev; format, niveau, kategorier, teknologier)
```

## Filformat

YAML-frontmatter, `# Titel`, transcript med `[HH:MM:SS]`. Frontmatter bærer det maskinen skal bruge (guid, kilde, metadata), så ingen behøver parse filnavne. Se README for felterne.

## Bevidste fravalg

- **Ingen søgning i repoet.** Biblioteket deles med andre, som selv vælger hvordan de søger. I stedet er det gjort nemt at bygge søgning ovenpå: frontmatter, `catalog.csv/json`, timestamps på hvert afsnit og `examples/search.py` som et kopierbart eksempel (SQLite FTS5 over afsnit med metadata som filtre).
- **Ingen embeddings.** Nøgleord plus metadata dækker de fleste spørgsmål. Skal der embeddings på, kan de bygges oven på afsnittene uden at ændre arkivet.
- **Ingen adapter-framework.** Tre kildetyper dækker det vi har. Kommer der en podcast, der kræver særlig kode, tilføjes en ny `source`.

## Hvor det kan ændre sig

- Flere podcasts kan gøre den daglige kørsel langsom (Jev-kald til sponsorfjernelse og metadata, Azure-transskribering). Så kan hentning deles i en matrix, men kun selve arbejdet: commit skal stadig ske ét sted for at undgå kapløb om push.
- Metadata skal rettes, hvis kategorierne ikke passer til nye podcasts: ret `vocabulary.toml` og kør `--add-metadata --force` for podcasten.
