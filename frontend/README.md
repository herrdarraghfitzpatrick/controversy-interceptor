# Controversy Scanner — Web Dashboard (Phase 3)

The web dashboard from spec section 6, wrapping the detection API. Next.js
(App Router) + TypeScript + Tailwind. UI primitives are hand-built in the
shadcn/ui style (Radix primitives + `class-variance-authority` + Tailwind)
rather than pulled via the `shadcn` CLI, since this environment's network
policy blocks `ui.shadcn.com`; the components in `src/components/ui/` are
the same pattern the CLI would have scaffolded.

## Scope (matches spec section 6 exactly)

- Paste text + select target market(s) (multi-select tag picker), industry,
  and content type (dropdowns) → submit → report view.
- Report view: findings grouped by severity, each expandable to
  explanation + precedent + suggested fix.
- Scan history, most recent first.
- Nothing else — no team roles, no CMS integrations, no exports. Those
  come later, once someone's paying (per spec section 6).

Scan history isn't scoped per-account yet since accounts don't exist until
Phase 4 — `GET /scans` currently lists every scan.

## Setup

```bash
npm install
cp .env.local.example .env.local
# edit .env.local if the backend isn't on the default http://127.0.0.1:8000
```

Requires the backend running (see the root README) with CORS
`ALLOWED_ORIGINS` covering wherever this dev server runs — the default
`http://localhost:3000` matches `npm run dev`'s default port.

```bash
npm run dev
```

## Notes for local dev in this environment

`ui.shadcn.com` is blocked by this sandbox's egress policy, so `npx shadcn
add ...` will fail here — hand-write new primitives following the existing
pattern in `src/components/ui/` instead (or run the CLI in an environment
with normal network access).

This sandbox's proxy also breaks Turbopack's dev-mode HMR WebSocket
(`net::ERR_INVALID_HTTP_RESPONSE`), which was enough to make Radix
`Popover`/`Select` triggers stop responding to clicks in `next dev` here
specifically — not a real app bug, but worth knowing if a browser check in
*this* environment finds a control that doesn't open: rule out the HMR
socket first (`npm run build && npm run start` sidesteps it entirely, and
is also what real end-to-end testing should target anyway).

## Structure

- `src/app/page.tsx` — scan form
- `src/app/scans/[id]/page.tsx` — report view (server component)
- `src/app/history/page.tsx` — scan history (server component)
- `src/components/ui/` — hand-built shadcn-style primitives
- `src/components/multi-select-tags.tsx` — the target-market tag picker
- `src/lib/api.ts` — typed client for the FastAPI backend
- `src/lib/constants.ts` — market/industry/content-type option lists,
  mirroring `app/services/scope.py` on the backend
