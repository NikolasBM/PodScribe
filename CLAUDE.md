# PodScribe

Arkiv af podcast-transcripts, autoopdateret dagligt via GitHub Actions. Generelt: hver podcast er en `[[podcast]]`-blok i `podcasts.toml`.

## Repo
- GitHub: `github.com/NikolasBM/PodScribe`, branch `main`. Offentligt repo.
- Lokal git-identitet sat **repo-lokalt** (ikke globalt): `user.name "Nikolas Manscher"`, `user.email "nikolas.manscher@gmail.com"`. Maskinen havde ingen global git-identitet ved oprettelse.
- Push-auth sat **repo-lokalt** til `gh`-login (NikolasBM): `credential.https://github.com.helper` = `""` + `!gh auth git-credential`. Nødvendigt fordi Git Credential Manager globalt har en anden GitHub-konto (`sam-nima`) gemt, og der ingen SSH-nøgle er. Skal sættes igen ved frisk klon.

## Struktur
```
podcasts.toml                — én [[podcast]]-blok per show (slug, name, source, since, ...)
fetch_transcripts.py         — henter/transskriberer nye episoder, stdlib-only (Python 3.11+, bruger tomllib)
vocabulary.toml              — kategorier, formater, niveauer og teknologi-aliaser til metadata
.github/workflows/fetch.yml  — daglig cron (06:30 UTC) + manuel workflow_dispatch med `args`-input
transcripts/<slug>/YYYY-MM-DD - Titel.md — én fil per episode: YAML-frontmatter, `# Titel`, så transcriptet med [HH:MM:SS]-timestamps
catalog.csv / catalog.json   — ét række pr. episode (frontmatter + sti), bygges af scriptet efter hver kørsel
examples/search.py           — eksempel: lokal SQLite FTS-søgning med frontmatter som filtre (ikke en del af arkivet)
README.md                    — offentlig beskrivelse af arkivet
```

## Podcasts
| slug | source | since | Note |
|---|---|---|---|
| `ai-daily-brief` | `published` | 2026-06-01 | `https://aidailybrief.ai/e/YYYY-MM-DD/transcript.md`. 404 = ingen episode den dato (ikke en fejl). **Ældste transcript er 2026-06-01** — verificeret ved probing tilbage til 2023. Ujævn udgivelse er forventet. |
| `latent-space` | `substack` | 2023-01-01 | Swyx & Alessio. Transcript i selve Substack-posten (`https://www.latent.space/p/<slug>`), ingen lyd/Azure. Gæster = alle talere der ikke står i `hosts`. Ingen sponsorfjernelse (`strip_ads = false`). |
| `how-i-ai` | `rss` | 2026-09-01 | Feed `https://anchor.fm/s/1035b1568/podcast/rss` (fundet via iTunes lookup id 1809663079). Ingen officielle transcripts findes. Bruger valgte bevidst kun fra 2026-09-01. ~2 episoder/uge, 25–50 min. |

## Kildetyper
- **`published`**: tjekker sidste 30 dage (eller `--since`), skipper datoer der allerede har en `{dato} - *.md`-fil (også gammel `{dato}.md`). Titel fra den hentede tekst (`# Titel — Transcript (dato)`), fallback til dato; guid = episode-URL.
- **`substack`**: lister `site/api/v1/archive` (paginerer, 50 ad gangen), tager `type == "podcast"` og `audience == "everyone"` i datointervallet, henter `site/api/v1/posts/<slug>` og læser transcriptet i `body_html` (efter en `Transcript`-overskrift): `<strong>Navn [HH:MM:SS]:</strong> tekst`, varianter uden tidsstempel i labelen bruger inline `[HH:MM:SS]`; `h2/h3` bliver `## Overskrift`. Poster uden transcript (🔬 science-serien: kun show notes) springes over og prøves igen næste dag (~11 småkald). Guid = `substack:<post-id>`. Betalingsmur (`only_paid`) gives ikke transcript. Feedet (`/feed`) rummer kun de seneste 20 poster, arkiv-API'et rækker tilbage til 2023 (229 offentlige podcast-poster, 104 med transcript). Ældre poster har andre formater: `Name: tekst` uden `<strong>`, `<br>` i stedet for afsnit, `[MM:SS]`-kapitler og labels i `h2`; `substack_body` håndterer dem (navne der åbner ≥ 3 linjer som `Navn:` tæller som talere; 2023-posterne har kun kapitel-tidsstempler, så afsnit arver kapitlets tid). Kendt svag: 2024-12-24 (generisk "Speaker").
- **`rss`**: læser feedet, transskriberer episoder med pubDate ≥ `since` hvis guid ikke allerede findes. Guid står i frontmatter (`guid:`) — filerne er staten, ingen state-fil. To episoder samme dag er normalt (derfor guid, ikke dato).

## Transskribering (rss)
- Azure Speech **fast transcription API** (`/speechtotext/transcriptions:transcribe?api-version=2025-10-15`) med `enhancedMode` → **MAI-Transcribe-2** (preview). Brugeren valgte MAI-Transcribe.
- Indstillinger: diarization til, `timestamps: "word"`, `transcribeStyle: "clean"` (fjerner fyldord), `phraseList` fra `phrases` i podcasts.toml.
- Lyden downloades og uploades som multipart (ikke `audioUrl`, fordi anchor.fm-URL'er redirecter). Grænse: < 2 timer og < 250 MB pr. fil.
- Docs nævner at diarization har kortere maks-længde end uden, men tallet mangler i docs. Scriptet falder tilbage til uden diarization ved `AudioLengthLimitExceeded`.
- Rendering: nyt afsnit ved talerskift, eller ved sætningsslut når der er gået ≥ 60 s; hvert afsnit starter med `[HH:MM:SS]`. Alle talernumre der siger værtens navn, "I'm <fornavn>" eller en af `host_cues` får værtens navn; øvrige hedder `Speaker 1`, `Speaker 2`, … Derfor flere numre: diarization er akustisk, og i den første test fik Claire to numre (studieintro/reklamer vs. skærmdemo). Showets navn alene er ikke et cue, fordi gæster siger "thanks for having me on How I AI".
- Gæstenavne: står titlen som `Emne | Navn` (evt. `Navn & Navn`, `(Rolle)` ignoreres), og der er præcis én gæst, får alle ikke-vært-talere gæstens navn. Ved flere gæster, eller uden `|` i titlen, forbliver de `Speaker N` — så skal de rettes ud fra teksten (gjort manuelt for 2026-09-14: John Bai, Peng Zheng; Claire havde her to ikke-cuede id'er).
- Sponsorreads fjernes af `strip_ads` i to trin. 1) **Cues** (`ad_start_cues`/`ad_end_cues`/`ad_tail_cues` i `podcasts.toml`): start ved første sætning med en start-cue, slut ved første sætning med webadresse (`xxx.com`/`.ai`/…) eller en slut-cue, plus efterfølgende "That's <stavet adresse>"-sætninger. 2) **Jev** (kun hvis secret `TYPESAFE_API_KEY` er sat; ellers kun cues): hver resterende sætning får en Noul "er den del af en sponsorread?" med to sætningers kontekst på hver side (`jev-1.13.0`, ~$0,003 pr. episode). Koden afgør klipningen: seed ≥ 0,5, løb samlet over huller ≤ 6 sætninger, kræver ≥ 5 flaggede sætninger (eller at ligge op ad en cue-fundet read), vokser udad over sætninger ≥ 0,3, maks 240 s. Fejler Jev, bruges kun cues (warning). Testet på de oprindelige 11 episoder: Jev alene fandt de samme reads som cues, inkl. dem uden "brought to you by", uden falske positiver (en værts-plug af gæsten `mega.dev` gav 3 flaggede sætninger og blev korrekt ikke klippet). Tuning-værdier er `JEV_*`-konstanterne øverst i `fetch_transcripts.py`.
- Gælder både `rss` (vores eget format) og `published` (AI Daily Brief: afsnit adskilt af blanke linjer, inline `[HH:MM:SS]`, redaktionsmarkører `NNNNNN xxx_EDIT:` og `Nathaniel Whittemore:`). I `published` er en markør uden dato-præfiks (`blitzy July_EDIT:`, `KPMG Aug_EDIT:`) en sponsor-redigering og tæller som start-cue. `ad_sponsors` i `podcasts.toml` lader en read vokse ≤ 2 sætninger ud over Jev's kant, hvis sætningen nævner sponsoren. Urørte afsnit bevares tegn for tegn. Cues kigger højst 24 sætninger frem efter en webadresse, fordi AIDB-indhold selv nævner domæner (z.ai m.fl.). "Thank you to today's sponsors"-intro i AIDB fjernes ikke (sætningerne er ofte uden tegnsætning og hænger sammen med indhold).
- Jev-kald er throttlet (~16 req/s, grænsen er 1.200/min) og retries på 429/5xx. Oprydning af gemte filer: `python3 fetch_transcripts.py --podcast <slug> --clean-ads` (kræver `TYPESAFE_API_KEY`; filer hvor Jev fejler, springes over så en gentagelse kan tage dem). Kør via Actions: `-f args="--podcast ai-daily-brief --clean-ads"` (ca. 35 min for 91 episoder, ~$0,01 pr. episode).
- Kontrollér detektion uden at skrive: `python3 fetch_transcripts.py --podcast how-i-ai --check-ads <filer>` (viser fund fra cues og Jev samt "borderline"-sætninger). Via Actions: `-f args="--podcast how-i-ai --check-ads transcripts/how-i-ai/<fil>"` (filnavne uden mellemrum, da args splittes på mellemrum).
- Kræver env/secrets `AZURE_SPEECH_KEY` og `AZURE_SPEECH_ENDPOINT` (`https://<navn>.cognitiveservices.azure.com`). Mangler de, springes rss-podcasts over med en warning; published kører videre.
- Foundry-ressourcen ligger i **North Europe** (MAI-Transcribe kun i centralindia, eastus, northeurope, southeastasia, westus, westus2).
- Pris: fast transcription standard er $0,36/time; MAI-Transcribe-2-prisen kunne ikke aflæses i Azures prisliste (oktober 2026) — tjek faktisk forbrug i Azure.

## Filformat og metadata
- Hver fil: `---` YAML-frontmatter `---`, blank, `# Titel`, blank, transcript. Værdierne er JSON (gyldig YAML): `podcast, podcast_title, title, date, url, guid, host, guests, format, level, length, categories, featured, mentioned, transcript_source (publisher|azure-asr), transcribed_by`. `render_doc`/`parse_doc`/`read_doc` i scriptet læser og skriver formatet (ingen YAML-afhængighed; parseren forstår kun vores egne filer). Tomme felter udelades, `guests` kun hvis ikke tom. Rækkefølgen er `FRONTMATTER_KEYS`. `length` er cirka (sidste timestamp).
- Jev-delen (`format, level, length, categories, featured, mentioned`) skrives af `metadata_fields` og kan genskabes uden at røre resten.
- Koden finder kandidat-teknologier med `vocabulary.toml` (aliaser inkl. talegenkendelsesfejl, længste alias vinder så "Claude Code" ikke også tæller som "Claude"; `exact_case` for ord der også er hverdagsord). Jev vurderer i ét kald pr. episode (hele transcriptet er state): én Noul pr. kategori ("diskuteres emnet udførligt?"), ét Choice for format, én Score for niveau og én Noul pr. kandidat ("er X et hovedemne?"). Kategori ≥ 0,5, teknologi ≥ 0,5 (virksomheder ≥ 0,9, ellers står OpenAI/Anthropic på 2/3 af episoderne). Virksomheder står ikke under "Also mentioned".
- Kategorilisten og formaterne er designet ud fra en gennemlæsning af alle 102+11 transcripts (se kommentarerne i `vocabulary.toml`). 14 kategorier: agents, coding, models, model-strategy, open-weights, enterprise, work, safety-security, policy, infrastructure, funding-markets, consumer, design, marketing. 7 formater: news-roundup, news-analysis, commentary, review, tutorial, demo, interview. Niveau 0–3.
- Nye episoder får blokken automatisk når `TYPESAFE_API_KEY` er sat. Efterfyld/gentag: `--add-metadata` (kun filer uden `categories`) eller `--add-metadata --force`, begge kræver `--podcast`.
- Kendt svaghed: Jev er rundhåndet med kategorier (92 af 113 episoder ramte loftet på 4), så de første to er mest informative.

## fetch_transcripts.py
```
python3 fetch_transcripts.py                                   # alle podcasts
python3 fetch_transcripts.py --podcast how-i-ai --limit 1      # én podcast, højst 1 ny episode
python3 fetch_transcripts.py --since A --until B               # specifikt interval (overstyrer podcastens since)
python3 fetch_transcripts.py --dry-run                         # vis hvad der ville blive transskriberet (gratis)
```
- Efter hver kørsel (også `--clean-ads`/`--add-metadata`) genskabes `catalog.csv`/`catalog.json` af `build_catalog` (lister som `a; b` i CSV). Workflowet committer dem sammen med `transcripts/`.
- Søgning er bevidst *ikke* en del af arkivet: det deles med venner/kolleger, som selv vælger hvordan de søger. README har opskrifter, `examples/search.py` er et eksempel de kan kopiere.
- Idempotent — output slutter altid `{n} new transcripts`. Exit 0 selv ved fejl på enkelte episoder (warn til stderr, fanges næste kørsel).

## GitHub Actions
- Trigger manuelt: `gh workflow run fetch-transcripts --repo NikolasBM/PodScribe` (evt. `-f args="--podcast how-i-ai --limit 1"`)
- Tjek status: `gh run list --repo NikolasBM/PodScribe --workflow=fetch.yml --limit 5`
- Committer kun hvis `transcripts/` ændrer sig. `concurrency: fetch-transcripts` forhindrer at to kørsler transskriberer (og betaler for) samme episode.
- Kører som `github-actions[bot]`, kræver `permissions: contents: write` (allerede sat).

## Kendte forbehold
- Ingen retry af fejlede requests (5xx/timeout) — de printes som `warn` og fanges næste kørsel, fordi filen mangler.
- Talerlabels er maskinelle og kan tage fejl (fx hvis gæsten siger showets navn før værten).
