# LAP — Webapp Task Backlog

**Repo:** `lap-webapp` (renamed from `lap-website/src/app/app/`; marketing separated per ADR-002)
**Stack:** Next.js 14 App Router, React 18, TypeScript strict, Tailwind, TanStack Query v5, Zustand (small UI stores only), `@lap/schemas` generated types. Deployed to Cloudflare Workers via OpenNext.
**Task format:** `WA-NNN`.

---

## Month 1 — Foundation + cleanup

### WA-001 🔴 Extract webapp from monolith, set up new package
- **Month/week:** M1/W1
- **Deps:** none
- **Parallel with:** desktop P0 work
- **AI:** claude-opus (plan) + codex (mechanical moves)
- **Hours:** 10-14
- **Context:** Move `lap-website/src/app/app/**`, `lap-website/src/app/admin/race-control/**`, `lap-website/src/components/**` (app-scoped only), and all `lib/api/**` into a new `lap-webapp/` package. Marketing stays behind (see marketing tasks). Shared utilities extract to `lap-ui` if needed.
- **Acceptance:**
  - `lap-webapp` builds and runs locally
  - `lap-website` becomes marketing-only
  - Routes: marketing on `lap.com`, webapp on `app.lap.com`

### WA-002 🔴 Install `@lap/schemas` and replace local DTO definitions
- **Month/week:** M1/W2
- **Deps:** WA-001, BE-003
- **AI:** claude-sonnet (mechanical replacement)
- **Hours:** 8-12
- **Context:** Every page that currently defines an inline `interface Session { ... }` — replace with `import type { SessionRecord } from '@lap/schemas'`. Bundle v2 types consolidated to `@lap/schemas` only.
- **Acceptance:**
  - `rg "interface Session" src/` returns 0 results (or only renamed view-models prefixed with `View` like `SessionView`)
  - Duplicate `types/bundles.ts` and `lib/api/bundles/types.ts` unified

### WA-003 🔴 API client refactor — one typed client built on @lap/schemas
- **Month/week:** M1/W2-3
- **Deps:** WA-002
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Replace the grab-bag of `api.get('/...')` calls with a typed client. Use `@hey-api/openapi-ts` or similar to generate a fetch client from OpenAPI. All page-level `useQuery` hooks import from the typed client.
- **Acceptance:**
  - `src/lib/api-client.ts` no longer has inline envelope definitions
  - `useSession(id)` returns `SessionRecord` typed
  - No `api.get<any>` calls remain

### WA-004 🔴 Kill-list: delete deprecated pages
- **Month/week:** M1/W2
- **Deps:** WA-001
- **AI:** codex
- **Hours:** 2-3
- **Context:** Per Q92. Delete:
  - `/app/admin/race-control/*`
  - `/app/jobs/*` (move to admin-only internal tool if needed)
  - `/app/exports/*`
  - `/app/dev-plans/*` (CRUD placeholder)
- **Acceptance:**
  - Routes 404
  - Navigation entries removed
  - No broken imports

### WA-005 🔴 Webapp P0: `/api/v1` double-prefix fix + duplicate route cleanup
- **Month/week:** M1/W1
- **Deps:** none
- **AI:** codex
- **Hours:** 2-3
- **Context:** Audit P0 from Q187. Fix in old Flask API + bundle query hooks simultaneously so bundle features don't break during migration.

### WA-006 🔴 Session list page — rework against new API
- **Month/week:** M1/W4
- **Deps:** WA-003, BE-015
- **AI:** claude-sonnet
- **Hours:** 8-10
- **Context:** Current session list has page-local interfaces and stale data. Rewrite on top of new `SessionRecord` contract. Support filtering by source (sim/real), track, car, date range. Paginated with cursor.

### WA-007 🔴 Session detail page — slim down the monolith
- **Month/week:** M1/W4
- **Deps:** WA-003
- **AI:** claude-opus (refactor plan) + claude-sonnet (implementation)
- **Hours:** 14-18
- **Context:** The current `src/app/app/sessions/[id]/page.tsx` is a 1000+ line monolith doing data fetching, editing, tabs, focus mode, gamification, sharing. Break into:
  - `SessionDetailShell` (layout only)
  - `SessionOverviewTab` / `SessionLapsTab` / `SessionTelemetryTab` / `SessionCoachingTab` (data-fetching)
  - `SessionActionsBar` (delete, re-process, share)
- **Acceptance:**
  - Every sub-component file ≤300 lines
  - Each tab fetches its own data with `useQuery` keys
  - Old functionality preserved

### WA-008 🟡 Sentry + PostHog client integration
- **Month/week:** M1/W4
- **Deps:** WA-001
- **AI:** codex
- **Hours:** 3-4
- **Context:** Sentry client SDK with session replay enabled (sampled 10%). PostHog client SDK with event taxonomy matching backend events.

---

## Month 2 — Next-actions migration + Beta prep

### WA-009 🔴 Replace SessionDebrief heuristic with `/api/v1/sessions/:id/next_actions`
- **Month/week:** M2/W6-7
- **Deps:** BE-023
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** Current `SessionDebrief` component generates drill text frontend-side. Replace with a call to `next_actions` endpoint + render the returned `WeaknessEpisode[]` and `ActionPrescription[]`.
- **Acceptance:**
  - No drill-generation logic remains in `src/components/coaching/*`
  - Copy comes from server's templated fields (beginner/intermediate/advanced variant selected by user level)
  - Accept-prescription button wires to backend

### WA-010 🔴 Coaching view on session detail
- **Month/week:** M2/W8
- **Deps:** WA-009
- **AI:** claude-opus + claude-design
- **Hours:** 10-12
- **Context:** New tab in `SessionDetailShell`: "Coaching". Shows:
  - New WeaknessEpisodes opened this session
  - Escalated WeaknessEpisodes (trend getting worse)
  - ActionPrescriptions with accept/skip buttons
  - Evidence links (which laps triggered the episode)

### WA-011 🟡 Beta onboarding UI
- **Month/week:** M2/W8
- **Deps:** WA-006
- **AI:** claude-design + claude-sonnet
- **Hours:** 6-8
- **Context:** First-time-user wizard: welcome → sample session load → first insight view → first prescription accept. Skippable.

---

## Month 3 — Driver OS

### WA-012 🔴 Driver Timeline page
- **Month/week:** M3/W9
- **Deps:** BE-024
- **AI:** claude-opus + claude-design
- **Hours:** 16-20
- **Context:** Per Q84. Top-level page `/app/timeline`. Chronological feed of sessions, grouped by week. Each card: session summary + badges for new/escalated WeaknessEpisodes + prescription actions + sim/real tag. Virtualized scrolling. Cursor pagination.
- **Acceptance:**
  - Loads first 20 sessions in <1s
  - Smooth scroll performance (60fps)
  - Works on mobile viewport

### WA-013 🔴 Driver Profile page
- **Month/week:** M3/W9-10
- **Deps:** BE-026
- **AI:** claude-opus + claude-design
- **Hours:** 18-22
- **Context:** Per Q84 "Strava-like". Top-level page `/app/profile`. Sections:
  - Overall Driver Score + trend
  - Skill dimensions radar chart
  - Currently open weaknesses (top 5)
  - Active prescriptions
  - Readiness for next target event
  - Recent sessions sparkline
  - Archetype tag (once cohort is on)
- **Acceptance:**
  - All data from one round-trip to `/driver/profile`
  - LCP <2s

### WA-014 🔴 Weakness detail page
- **Month/week:** M3/W10
- **Deps:** BE-019
- **AI:** claude-opus + claude-design
- **Hours:** 10-12
- **Context:** `/app/weaknesses/:id`. Shows episode history, confidence trend, evidence sessions, linked prescriptions + outcomes, recommendation to resolve.

### WA-015 🔴 Durable Compare — saved cases
- **Month/week:** M3/W10
- **Deps:** BE-027
- **AI:** claude-opus
- **Hours:** 12-14
- **Context:** Per Q85. New URL pattern `/app/compare/:case_id`. User can save a compare with rationale ("I was trying to see why I was slower at Spa last week"). Outcome section auto-updates if referenced sessions reprocess.

### WA-016 🔴 Onboarding flow
- **Month/week:** M3/W10
- **Deps:** WA-011
- **AI:** claude-design (key UX) + claude-sonnet
- **Hours:** 14-18
- **Context:** First-run post-signup. Four steps:
  1. "Welcome" — what LAP does in 15s
  2. "Try with a sample session" — load a curated sim session, explore UI
  3. "Upload your first real session" — desktop/mobile install link OR .ibt file upload
  4. "Accept your first prescription" — mark activation complete
- **Acceptance:**
  - Time-to-first-value <8 min measured via PostHog funnel
  - Skippable at each step
  - Activation event fires on prescription accept

### WA-017 🔴 Per-dimension drilldown pages
- **Month/week:** M3/W10-11
- **Deps:** WA-013, BE-022
- **AI:** claude-design
- **Hours:** 12-14
- **Context:** `/app/profile/skills/:dimension` (e.g., `/profile/skills/braking`). Shows trend, best sessions, worst sessions, related weaknesses, drills attempted.

### WA-018 🔴 Pricing + checkout flow
- **Month/week:** M3/W11
- **Deps:** BE-030
- **AI:** claude-design + claude-sonnet
- **Hours:** 10-12
- **Context:** `/app/billing` and marketing `/pricing` both point to Stripe Checkout. In-app paywall triggers on trial expiry. Grandfather coupon auto-applied for waitlist users.

### WA-019 🔴 Settings pages
- **Month/week:** M3/W11
- **Deps:** WA-001
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** `/app/settings` with tabs: profile, preferences (user level: beginner/intermediate/advanced per Q149), integrations (desktop/mobile paired devices), data (cohort opt-in, export, delete).

### WA-020 🔴 Desktop/mobile pairing via magic QR
- **Month/week:** M3/W11
- **Deps:** BE-006
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** Per ADR-011. Webapp shows QR with a time-limited token; desktop/mobile scan → exchange token for refresh token → paired.

### WA-021 🔴 Launch-day polish pass
- **Month/week:** M3/W12
- **AI:** claude-opus (review) + codex (fixes)
- **Hours:** 16-20
- **Context:** Lighthouse pass: LCP/INP targets (§4 of KPIs). Fix all critical a11y issues. Audit copy for consistency. Social share images.

---

## Month 4 — Bridge UI

### WA-022 🔴 Bridge view on session detail
- **Month/week:** M4/W13-14
- **Deps:** BE-033, BE-035
- **AI:** claude-opus + claude-design
- **Hours:** 12-14
- **Context:** In SessionDetailShell add "Bridge" tab. Shows:
  - Auto-suggested linked sessions
  - "Link to sim/real equivalent" manual action
  - If linked: summary card linking to full Transfer Report page

### WA-023 🔴 Transfer Report page
- **Month/week:** M4/W14
- **Deps:** BE-036
- **AI:** claude-opus + claude-design
- **Hours:** 14-18
- **Context:** `/app/bridge/reports/:link_id`. Shows:
  - Two session headers side by side (sim + real)
  - Overall shape match, intensity match
  - Per-corner divergence list with mini traces
  - Transferred vs non-transferred skills
  - Generated CoachingInsight summary
  - User "rate this useful" thumbs

### WA-024 🟡 Cohort percentile UI
- **Month/week:** M4/W16
- **Deps:** BE-037
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** On Driver Profile, add percentile-vs-cohort badge per dimension when cohort unlocks. Until then, show "Cohort unlocks at 20 drivers for your car/track combo."

### WA-025 🟡 Target event picker
- **Month/week:** M4/W16
- **Deps:** BE-040
- **AI:** claude-design
- **Hours:** 8-10
- **Context:** In Driver Profile, user can pin an iRacing special event or real track day as target. Readiness score updates to target that event.

---

## Month 5 — V1 Polish

### WA-026 🔴 Endurance session UX
- **Month/week:** M5/W18-19
- **Deps:** BE-039, BE-042
- **AI:** claude-design
- **Hours:** 10-12
- **Context:** Endurance sessions show stint-level breakdown on detail page. Long-run pace decay chart. Tire preservation score.

### WA-027 🔴 V1 release notes page
- **Month/week:** M5/W20
- **AI:** claude-opus (copy)
- **Hours:** 3-4

### WA-028 🟡 In-app changelog widget
- **Month/week:** M5/W20
- **AI:** codex
- **Hours:** 3-4

---

## Month 6 — Scale

### WA-029 🟡 B2B landing + onboarding
- **Month/week:** M6/W22
- **Deps:** BE-046
- **AI:** claude-design
- **Hours:** 10-14
- **Context:** `/for-schools` landing page + multi-seat admin UI if any B2B closes.

### WA-030 🟡 Paid ad landing pages
- **Month/week:** M6/W23-24
- **AI:** claude-design
- **Hours:** 6-8

### WA-031 🟡 Ongoing bug bash + polish
- **Month/week:** M6 throughout
- **Hours:** 20-30

---

## Summary

| Month | Webapp hours | Key deliverable |
|---|---|---|
| M1 | 50-70 | Extraction + contracts migration + P0 cleanup |
| M2 | 30-40 | Next-actions migration + Coaching view |
| M3 | 100-130 | **Driver OS — Timeline + Profile + Compare + onboarding** |
| M4 | 40-55 | Bridge UI |
| M5 | 25-35 | Endurance UX + V1 polish |
| M6 | 35-50 | B2B + scale |
| **Total** | **~300 hours** | |
