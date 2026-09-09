# Controversy Scanner — Detection API (Phase 1 + Phase 2)

Scans campaign text/briefs for phrases, imagery references, or concepts that
could trigger a cultural, political, historical, or social-media backlash
in a given target market. This covers Phases 1-2 from the v0.1 spec: the
core detection API, library-first matching against a curated case library,
a single Claude pass for the linguistic, historical, brand, and imagery
lenses, and an opt-in live-web-search pass for the recent-event lens. The
web dashboard, accounts/billing, and the library refresh job are later
phases.

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
  "imagery_description": "optional: freeform, for the imagery lens only",
  "check_recent_events": false
}
```

Returns a report: `scan_id`, `scope_applied`, `findings[]`,
`checked_against_library_version`, `live_search_performed`. Each finding
has `span`, `category`, `target_market`, `severity`, `confidence`,
`explanation`, and optional `precedent` / `suggested_fix` — see spec
section 3.

Detection runs in up to three stages:
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
2. **Claude pass (lenses 1-3, 5)** — a single Claude API call covers the
   linguistic, historical, brand, and imagery lenses for anything the
   library didn't already catch. It is told which spans the library
   flagged so it doesn't duplicate them.
3. **Recent-event pass (lens 4, opt-in)** — only runs when
   `check_recent_events: true` is set on the request. This lens catches
   copy that's fine in isolation but collides with a very recent news
   story or social-media moment (the "Starbucks Korea" case) — it cannot
   be solved from a static library, so it uses the Claude web-search tool
   to check the copy against current events per target market. It's
   slower and costs more per call than stages 1-2 (an extra Claude call
   plus live web searches), so per spec section 7 it's gated behind opt-in
   rather than running on every scan — recommended for high-stakes scans
   (paid ads, press releases) rather than every scan. `live_search_performed`
   reflects whether a search actually happened (Claude may decide not to
   search if nothing in the copy warrants it), not just whether this stage
   was requested.

If `ANTHROPIC_API_KEY` is unset, or a Claude API call fails for any reason
(auth, rate limit, outage), `/scan` still returns 200 with whatever
findings the other stages produced rather than failing the whole request —
useful for local development without API costs, and for resilience against
a Claude API hiccup in production.

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

## What's not built yet

Per the build spec's phased roadmap (section 7): the web dashboard
(Phase 3), accounts + Stripe billing (Phase 4), and the weekly
case-library refresh job (Phase 5).

Also unvalidated per spec section 8: actual cost-per-scan and latency for
the recent-event pass haven't been measured against real traffic yet —
that needs doing before pricing it into subscription tiers.
