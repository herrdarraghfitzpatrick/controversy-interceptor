# Controversy Scanner — Detection API (Phase 1)

Scans campaign text/briefs for phrases, imagery references, or concepts that
could trigger a cultural, political, historical, or social-media backlash
in a given target market. This is the Phase 1 build from the v0.1 spec:
the core detection API, library-first matching against a curated case
library, and a single Claude pass for the linguistic, historical, brand,
and imagery lenses. The recent-event lens (live web search) and the web
dashboard are later phases.

## Stack

- FastAPI (Python)
- Postgres via SQLAlchemy + Alembic migrations
- Claude API (`anthropic` SDK) for the non-library detection pass

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# edit .env: set DATABASE_URL and ANTHROPIC_API_KEY
```

Create the database, then run migrations:

```bash
createdb controversy_scanner
alembic upgrade head
```

Seed the case library (spec section 4 — curated real-world cases):

```bash
python -m app.seed.seed_db
```

Run the API:

```bash
uvicorn app.main:app --reload
```

## API

### `POST /scan`

```json
{
  "text": "campaign copy or brief",
  "target_markets": ["IE", "KR", "US"],
  "industry": "fintech",
  "content_type": "PR blog post",
  "imagery_description": "optional: freeform, for the imagery lens only"
}
```

Returns a report: `scan_id`, `scope_applied`, `findings[]`,
`checked_against_library_version`, `live_search_performed`. Each finding
has `span`, `category`, `target_market`, `severity`, `confidence`,
`explanation`, and optional `precedent` / `suggested_fix` — see spec
section 3.

Detection runs in two stages per lens:
1. **Library matching** — the curated `case_library_entries` table is
   filtered by target market, industry, and content type, then matched
   against the scan text (case-insensitive phrase matching). Filtering is
   deliberately permissive: `industry`/`content_type` are freeform strings
   (e.g. "PR blog post"), not the same controlled vocabulary as entry tags
   (e.g. `["pr"]`), so filtering uses word-level overlap rather than exact
   match — over-including an entry here only means it's *considered*, not
   reported, since a finding still requires the phrase to literally appear.
   `imagery`-category entries are only checked against `imagery_description`,
   never plain copy, per spec section 3 lens 5. Many real cases are concept
   summaries rather than literal slogans (e.g. `"Tank Day" tumbler promotion
   on the anniversary of the Gwangju massacre`) — the matcher also tries any
   quoted sub-phrase as its own candidate span, since that's usually the
   actual literal name/hashtag/slogan that would appear in real copy.
2. **Claude pass** — a single Claude API call covers the linguistic,
   historical, brand, and imagery lenses for anything the library didn't
   already catch. It is told which spans the library flagged so it
   doesn't duplicate them. The recent-event lens (live web search) is not
   run in Phase 1 — `live_search_performed` is always `false`.

If `ANTHROPIC_API_KEY` is unset, or the Claude API call fails for any
reason (auth, rate limit, outage), `/scan` still returns 200 with
library-only findings rather than failing the whole request — useful for
local development without API costs, and for resilience against a Claude
API hiccup in production.

### `GET /scan/{scan_id}`

Retrieves a past report.

### `GET /library?region=IE&category=linguistic`

Browses the case library (internal/admin use). Query params: `region`
(substring match against the entry's region code(s)), `category`
(`linguistic | historical | brand | recent_event | imagery`), `active_only`
(default `true`).

## Case library

`app/models/case.py` defines `CaseLibraryEntry` per spec section 4:
phrase/concept, region, category, optional industry/content-type tags,
description, source citation, date, baseline severity, and an `active`
flag for retiring stale entries.

Seed data lives in `app/seed/cases.py` as a JSON-shaped list (57 real,
web-verified cases at time of writing, spanning all five categories and 20+
regions) and is loaded via `app/seed/seed_db.py`, which upserts by
`(phrase_or_concept, region, category)` so re-running it is safe. A few
famous "translation fail" cases (Chevy Nova, Pepsi "ancestors", Coors,
Gerber, KFC "finger lickin'") were deliberately excluded from the seed set
as debunked/unverifiable urban legends rather than seeded as fact.

Adding a new case: append an entry to `app/seed/cases.py` (or insert
directly into `case_library_entries`) with a real, verified `source_url` —
citations are non-negotiable for this product's credibility. Re-run the
seed script to apply.

## Tests

```bash
createdb controversy_scanner_test
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/controversy_scanner_test \
  pytest
```

Tests use a real Postgres database (the models rely on Postgres-specific
`ARRAY`/`JSONB` column types) and mock the Claude API call, so they run
without network access or an API key.

## What's not in Phase 1

Per the build spec's phased roadmap (section 7): live web search / the
recent-event lens (Phase 2), the web dashboard (Phase 3), accounts +
Stripe billing (Phase 4), and the weekly case-library refresh job
(Phase 5).
