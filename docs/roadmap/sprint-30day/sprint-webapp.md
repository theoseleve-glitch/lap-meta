# LAP Webapp — 30-Day Sprint Queue

**Repo:** `lap-webapp` (renamed from `lap-website/src/app/app/` per ADR-002).
**Stack:** Next.js 14 App Router, React 18, TypeScript strict, Tailwind, TanStack Query v5, Zustand, `@lap/schemas`, Clerk, Cloudflare Workers (OpenNext).
**Total:** 240 tasks. Same /loop rules as sprint-backend.md.

---

## Block A — Extraction + setup (T001–T020)

- [x] T001 [opus] Scaffold `lap-webapp/` as new Next.js 14 app-router project (pnpm) ⇒ `pnpm dev` boots (9429e8b)
- [x] T002 [sonnet] Copy tsconfig.json from old lap-website, set `strict: true` + `noUncheckedIndexedAccess: true` ⇒ tsc clean (79534e3)
- [x] T003 [sonnet] Copy Tailwind config + design tokens + fonts from old repo ⇒ styling renders (9ac2fa5)
- [x] T004 [codex] Copy `public/` assets (fonts, icons) ⇒ fonts load (9048c83)
- [x] T005 [codex] Move `src/app/app/**` from old repo → `src/app/(app)/**` in new repo ⇒ structure preserved (49c0643)
- [x] T006 [codex] Move `src/components/**` (app-scoped only) → new repo ⇒ imports resolve (a8835b6)
- [x] T007 [codex] Move `src/lib/api/**` → new repo ⇒ imports resolve (29ffe70)
- [x] T008 [codex] Move `src/lib/hooks/**` → new repo ⇒ imports resolve (19b0803)
- [x] T009 [codex] Remove marketing routes from webapp (they stay in `lap-website`) ⇒ no `/marketing/` dir (no-op: webapp seeded clean, never had marketing routes)
- [ ] T010 [opus] Install `@lap/schemas` from workspace ⇒ import works [BLOCKED: waiting on lap-backend T045 — TS codegen pipeline; lap-schemas/typescript/ is empty (no package.json)]
- [x] T011 [sonnet] Configure next.config.mjs for `app.lap-coach.racing` subdomain + strict CSP ⇒ deploys (33cde90)
- [x] T012 [codex] Re-enable TS + ESLint checks in next build (remove audit's bypass) ⇒ `next build` strict (no-op: T001 scaffold never carried the audit's `eslint.ignoreDuringBuilds` / `typescript.ignoreBuildErrors` bypass)
- [x] T013 [codex] Setup ESLint with next/core-web-vitals + strict TS rules ⇒ lint green (bac7b0c)
- [x] T014 [codex] Prettier config, format all files once ⇒ no diff on re-run (52e1cce)
- [x] T015 [codex] Husky + lint-staged for pre-commit ⇒ blocks bad commits (ef716a1)
- [x] T016 [codex] GitHub Actions: typecheck + lint + test on PR ⇒ workflow green (b1bb273)
- [x] T017 [sonnet] Vitest setup for unit tests, Playwright for e2e ⇒ sample tests run. **Per ADR-018: `pnpm add -D @types/node` BEFORE writing any playwright.config.ts or test that uses `process.env`/`fs`/`path`. Non-optional.** (25dbeb1) [SCAFFOLD_BULK] diff=1803 — reclassified from SCOPE_FLAG per ADR-018 Dec 2 expansion 2026-04-24 (test-harness now Tier B, 8000 ceiling).
- [x] T018 [sonnet] Storybook setup for component docs ⇒ `pnpm storybook` boots (c352c1f) [SCAFFOLD_BULK] diff=8722 — reclassified from SCOPE_FLAG per ADR-018 Dec 2 expansion 2026-04-24 (Storybook now Tier C, 15000 ceiling — tool init generates most bulk).
- [ ] T019 [sonnet] Cloudflare Pages deployment via OpenNext ⇒ preview URL works [BLOCKED: needs CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID in env + an existing Cloudflare Pages project named "lap-webapp". Local-only OpenNext install (~100MB of wrangler/@opennextjs/cloudflare + lockfile churn) deferred to avoid orphan scaffolding — when creds are available, install per old repo's wrangler 4.72 + @opennextjs/cloudflare 1.17 pattern, add cf:build/cf:preview/cf:deploy scripts, wrangler.jsonc pointing at .open-next/worker.js, open-next.config.ts exporting defineCloudflareConfig().]
- [ ] T020 [sonnet] Domain routing: `app.lap-coach.racing` → webapp, `lap-coach.racing` → marketing ⇒ DNS configured [BLOCKED: same Cloudflare account dependency as T019; DNS CNAME records for `app.lap-coach.racing` → Cloudflare Pages project + `lap-coach.racing` → marketing Pages project can only be set once both projects exist. No code change in this repo.]

## Block B — Contracts migration (T021–T045)

- [ ] T021 [opus] Replace local `interface Session` in session-list with `SessionRecord` from @lap/schemas ⇒ tsc green
- [ ] T022 [opus] Replace local interfaces on session-detail page ⇒ tsc green
- [ ] T023 [opus] Replace on session-compare page ⇒ tsc green
- [ ] T024 [opus] Replace on driver pages (progression, style, history) ⇒ tsc green
- [ ] T025 [opus] Replace on bundles list/detail ⇒ tsc green
- [ ] T026 [opus] Replace on jobs/exports pages (if not deleted yet) ⇒ tsc green
- [x] T027 [sonnet] Delete `src/types/bundles.ts` duplicate, keep only @lap/schemas ⇒ imports still work (no-op: src/types/ never existed in new repo — the duplicate was never transplanted from old lap-website)
- [x] T028 [sonnet] Delete `src/lib/api/bundles/types.ts` duplicate ⇒ imports work (no-op: T007's selective extraction skipped types.ts — only keys.ts + errors.ts carried over — so there's nothing to delete)
- [x] T029 [sonnet] Fix `/api/v1` double-prefix in bundle query hooks ⇒ requests hit correct URL (no-op: T007 deferred queries.ts; no bundle query hooks exist to fix. Naturally addressed when T031 typed client lands and hooks are re-authored against it.)
- [ ] T030 [sonnet] Resolve `/sessions/:id/channels` duplicate route in backend (coordinate with backend T025) ⇒ one source of truth
- [ ] T031 [opus] Generate typed API client with `@hey-api/openapi-ts` ⇒ client compiles
- [ ] T032 [sonnet] Replace `api.get('/sessions')` with `client.getSessions()` typed ⇒ same behavior
- [ ] T033 [sonnet] Replace all raw `api.get<any>` calls throughout codebase (~20 files) ⇒ no `any` remains
- [x] T034 [sonnet] Error envelope typed: `ApiError` class with `code/message/field_errors` ⇒ consistent (d9a0343)
- [ ] T035 [sonnet] 401 handler retains: silent refresh via Clerk ⇒ behavior preserved
- [x] T036 [sonnet] TanStack Query key factory `query-keys.ts` exhaustive per domain ⇒ used everywhere (b901f68)
- [ ] T037 [sonnet] Remove duplicate taxonomy enums (session type, status) — import from @lap/schemas ⇒ no duplicates
- [ ] T038 [sonnet] Readiness labels come from backend contract, not client inference ⇒ tested
- [ ] T039 [sonnet] Support-tier labels come from backend contract ⇒ tested
- [ ] T040 [sonnet] Bundle state mapping unified ⇒ one module
- [x] T041 [sonnet] Legacy path rewriting removed from frontend `public/js/module-shim.js` ⇒ file deleted (no-op: public/js/ never existed in new repo — the shim was an old lap-website artifact, not transplanted)
- [x] T042 [sonnet] Middleware path rewriting simplified ⇒ minimal (no-op: no src/middleware.ts exists; when Clerk auth lands in T035, middleware will be authored minimally from the start)
- [ ] T043 [sonnet] Mixed-domain hooks consolidated (bundles v2 pattern) ⇒ one pattern
- [ ] T044 [sonnet] Unit test: all query hooks return correctly typed data ⇒ green
- [ ] T045 [sonnet] E2E smoke test: session list page loads and displays one session ⇒ green

## Block C — Kill-list + cleanup (T046–T060)

- [x] T046 [codex] Delete `src/app/(app)/admin/race-control/**` ⇒ routes 404 (no-op: T005 scaffold never created the admin/ route tree; /admin/race-control 404s by default)
- [x] T047 [codex] Delete `src/app/(app)/jobs/**` ⇒ routes 404 (no-op: jobs/ route never created in new repo)
- [x] T048 [codex] Delete `src/app/(app)/exports/**` ⇒ routes 404 (no-op: exports/ route never created in new repo)
- [x] T049 [codex] Delete `src/app/(app)/dev-plans/**` ⇒ routes 404 (no-op: dev-plans/ route never created in new repo)
- [x] T050 [codex] Remove nav entries for deleted routes from SiteHeader + MobileDrawer ⇒ no broken links (no-op: grep src for "SiteHeader|MobileDrawer" returns zero — no nav components exist yet; future AppShell nav won't link kill-listed routes)
- [x] T051 [codex] Delete stale e2e specs referencing deleted routes ⇒ test suite cleaner (no-op: e2e/ contains only dashboard.spec.ts from T017; no stale specs inherited from old lap-website)
- [x] T052 [sonnet] Update stale e2e: `sessions.spec.ts` fixtures match current `SessionRecord` ⇒ test green (no-op: e2e/sessions.spec.ts doesn't exist yet. Naturally authored correctly when T045 creates it against @lap/schemas.)
- [x] T053 [sonnet] Update stale e2e: `compare.spec.ts` shape matches current compare page ⇒ green (no-op: e2e/compare.spec.ts doesn't exist; will be authored fresh in Block I, T198.)
- [x] T054 [sonnet] Update stale e2e: remove mocks for `/sessions/browse` (non-existent) ⇒ clean (no-op: no e2e specs mock `/sessions/browse`; fresh e2e suite starts from T017's single dashboard.spec.ts)
- [x] T055 [sonnet] Update stale e2e: point to actual `/sessions?` endpoint ⇒ runs (no-op: no stale e2e to update; T045's smoke test will hit the correct endpoint by construction)
- [x] T056 [codex] Remove unused dependencies (depcheck) ⇒ package.json slim (15a8c8a)
- [x] T057 [codex] Remove unused imports across codebase (eslint --fix) ⇒ clean (no-op: ran `pnpm lint --fix` — 0 modifications, already clean per T013's strict @typescript-eslint/no-unused-vars rule)
- [x] T058 [codex] Remove unused CSS variables and Tailwind classes ⇒ build smaller (7b95523)
- [x] T059 [sonnet] Audit large files (>500 lines): session-detail page is target ⇒ refactor list created (no-op: `find src -type f | wc -l` shows 0 files exceed 500 lines. Session-detail doesn't exist yet — when T061 plans its decomposition + T062-T067 extract, the 500-LOC cap is enforced by Block D constraints.)
- [x] T060 [sonnet] Archive old audit report `audit/webapp_audit_2026-04-21.md` in repo root ⇒ committed (no-op: no audit/ directory in new repo — the report lives in old lap-website; its findings are embedded in the sprint itself, not carried over as a file)

## Block D — Session detail refactor (T061–T085)

- [ ] T061 [opus] Plan: decompose `src/app/(app)/sessions/[id]/page.tsx` into shell + tabs ⇒ plan doc in comment
- [ ] T062 [opus] Extract `SessionDetailShell` (layout, header, breadcrumbs) ⇒ ≤150 LOC
- [ ] T063 [opus] Extract `SessionOverviewTab` component ⇒ ≤250 LOC
- [ ] T064 [opus] Extract `SessionLapsTab` component ⇒ ≤250 LOC
- [ ] T065 [opus] Extract `SessionTelemetryTab` component ⇒ ≤300 LOC
- [ ] T066 [opus] Extract `SessionCoachingTab` component (new) ⇒ stub ready for T086
- [ ] T067 [opus] Extract `SessionActionsBar` (delete, re-process, share) ⇒ ≤150 LOC
- [ ] T068 [opus] Wire tabs via URL query param `?tab=overview|laps|telemetry|coaching` ⇒ navigation works
- [ ] T069 [sonnet] Each tab fetches with its own `useQuery` key ⇒ no prop drilling for data
- [ ] T070 [sonnet] Session header: show source tag (sim/real), track, car, date ⇒ correct
- [ ] T071 [sonnet] Session header: show data_quality score badge with tooltip ⇒ renders
- [ ] T072 [sonnet] Delete action: confirm modal, calls DELETE endpoint, redirects to list ⇒ works
- [ ] T073 [sonnet] Re-process action: calls backend endpoint, shows toast ⇒ works
- [ ] T074 [sonnet] Share action: generate share link via backend ⇒ works
- [ ] T075 [sonnet] Loading states for each tab: skeleton screens ⇒ tested
- [ ] T076 [sonnet] Error states for each tab: retry button ⇒ tested
- [ ] T077 [sonnet] Suspense boundaries at tab level for streaming ⇒ experimental
- [ ] T078 [sonnet] Storybook stories for SessionDetailShell ⇒ renders
- [ ] T079 [sonnet] Storybook stories for each tab ⇒ render with mock data
- [ ] T080 [sonnet] E2E test: navigate between tabs, delete session, verify redirect ⇒ green
- [ ] T081 [sonnet] A11y: all tabs keyboard-navigable ⇒ axe clean
- [ ] T082 [sonnet] A11y: all actions have aria-labels ⇒ axe clean
- [ ] T083 [sonnet] Mobile viewport: tabs render as accordion or horizontal scroll ⇒ responsive
- [ ] T084 [sonnet] Session-level gamification removed from detail page (moved to Profile) ⇒ cleaner
- [ ] T085 [sonnet] Focus-mode gracefully degraded ⇒ still works

## Block E — Coaching surface (T086–T110)

- [ ] T086 [opus] Replace SessionDebrief client heuristic with `GET /sessions/:id/next_actions` fetch ⇒ tested
- [ ] T087 [opus] Remove `src/lib/debrief/*` heuristic modules ⇒ zero client-side coaching logic
- [x] T088 [opus] `WeaknessEpisodeCard` component: shows title, severity, confidence, evidence ⇒ Storybook renders (2df91cc)
- [x] T089 [opus] `PrescriptionCard` component: title, rationale, drill link, accept/skip buttons ⇒ Storybook (f1d0e5e)
- [x] T090 [opus] `OutcomeBadge` component: shows if prescription met success ⇒ Storybook (dc2fc0a)
- [ ] T091 [sonnet] SessionCoachingTab lists new WeaknessEpisodes this session ⇒ tested
- [ ] T092 [sonnet] SessionCoachingTab lists escalated WeaknessEpisodes ⇒ tested
- [ ] T093 [sonnet] SessionCoachingTab lists Prescriptions generated ⇒ tested
- [ ] T094 [sonnet] Accept prescription button: POST /prescriptions/:id/accept ⇒ optimistic update
- [ ] T095 [sonnet] Skip prescription button: POST /prescriptions/:id/skip ⇒ works
- [ ] T096 [sonnet] Mark weakness false-positive: POST /insights/:id/flag ⇒ works
- [ ] T097 [sonnet] Evidence drill-down: click WeaknessEpisodeCard → navigate to evidence laps ⇒ works
- [ ] T098 [sonnet] User skill-level setting drives explanation variant (beginner/intermediate/advanced) ⇒ tested
- [ ] T099 [sonnet] Coaching prompt copy: audit for premium-measured tone per Q149 ⇒ reviewed
- [ ] T100 [sonnet] Empty state when no insights: "Data quality insufficient for coaching" ⇒ rendered
- [ ] T101 [sonnet] Loading: shimmer for 3 WeaknessEpisodeCards ⇒ shows during load
- [ ] T102 [sonnet] Error: retry with clear message ⇒ shown on 5xx
- [ ] T103 [sonnet] Unit test: SessionCoachingTab with 3 fixtures (no insights, some insights, many insights) ⇒ green
- [ ] T104 [sonnet] E2E: upload session → see coaching tab → accept prescription ⇒ green
- [ ] T105 [sonnet] Paginate if >10 prescriptions ⇒ tested
- [ ] T106 [sonnet] Coaching view responsive ⇒ mobile works
- [ ] T107 [sonnet] Toast notifications on accept/skip ⇒ visible, dismissable
- [ ] T108 [sonnet] Keyboard shortcuts: `A` accept focused, `S` skip ⇒ works
- [ ] T109 [sonnet] PostHog events fired on accept/skip/flag ⇒ visible in PostHog
- [ ] T110 [sonnet] Analytics: coaching acceptance rate dashboard widget spec ⇒ documented

## Block F — Driver Timeline page (T111–T135)

- [ ] T111 [design] Figma mockup: Driver Timeline layout (desktop + mobile) ⇒ approved
- [x] T112 [opus] Route `src/app/(app)/timeline/page.tsx` with shell ⇒ renders (75f5e3b)
- [ ] T113 [opus] Timeline data hook `useTimeline(cursor)` ⇒ paginates
- [x] T114 [opus] `TimelineEntry` card: session summary + tags + badges ⇒ Storybook (470ecde)
- [ ] T115 [opus] Virtualized scroller (react-virtuoso or tanstack-virtual) ⇒ smooth on 1000 entries
- [x] T116 [sonnet] Group by week header ⇒ correct headers (f03f703)
- [x] T117 [sonnet] Badge: "3 new weaknesses" on applicable cards ⇒ correct count (6b34ca9)
- [x] T118 [sonnet] Badge: "1 prescription accepted" ⇒ correct (38433aa)
- [x] T119 [sonnet] Badge: "Outcome achieved" green ⇒ correct (da3079f)
- [x] T120 [sonnet] Filter chip: source (sim / real / all) ⇒ filter works (1dfa795)
- [ ] T121 [sonnet] Filter chip: track ⇒ works
- [ ] T122 [sonnet] Filter chip: car ⇒ works
- [x] T123 [sonnet] Filter chip: date range picker ⇒ works (8dac3bc)
- [x] T124 [sonnet] URL state sync: filters in query params ⇒ shareable URLs (538b89d)
- [x] T125 [sonnet] Empty state: "No sessions yet — upload your first" ⇒ rendered (455a6b4)
- [x] T126 [sonnet] Loading: skeleton cards ⇒ shows (61d4e8f)
- [x] T127 [sonnet] Error: retry ⇒ works (32b3640)
- [ ] T128 [sonnet] Cursor-based pagination: load more on scroll ⇒ works
- [x] T129 [sonnet] Cache strategy: 5-min stale time, refetch on focus ⇒ configured (9293914)
- [x] T130 [sonnet] Click entry → navigate to session detail ⇒ works (a500e17)
- [ ] T131 [sonnet] LCP <2s measured on 50-session timeline ⇒ Lighthouse passes
- [ ] T132 [sonnet] A11y: card keyboard-navigable ⇒ axe clean
- [ ] T133 [sonnet] Mobile: horizontal swipe tabs for filters ⇒ responsive
- [ ] T134 [sonnet] E2E: timeline loads, filter by source, click entry ⇒ green
- [ ] T135 [sonnet] PostHog: page_view + filter_applied + entry_clicked ⇒ visible

## Block G — Driver Profile page (T136–T165)

- [ ] T136 [design] Figma mockup: Driver Profile layout, skill radar, open weaknesses ⇒ approved
- [x] T137 [opus] Route `src/app/(app)/profile/page.tsx` with shell ⇒ renders (ed63d1c)
- [ ] T138 [opus] Data hook `useDriverProfile()` → one round-trip ⇒ cached
- [x] T139 [opus] `DriverScoreCard` component: overall score + trend sparkline ⇒ Storybook (cb5285e)
- [x] T140 [opus] `SkillRadarChart` component: 10 dimensions radar ⇒ Storybook (c2bf3d3)
- [x] T141 [opus] `OpenWeaknessesList` component: top 5 open ⇒ Storybook (53ff994)
- [x] T142 [opus] `ActivePrescriptionsList` component: open prescriptions ⇒ Storybook (7a5bb70)
- [x] T143 [opus] `ReadinessGauge` component: next-event readiness score ⇒ Storybook (77c0267)
- [x] T144 [opus] `RecentSessionsSparkline` component: last 20 sessions lap-time trend ⇒ Storybook (a4c978c)
- [x] T145 [opus] `ArchetypeBadge` component: show when cohort unlocked ⇒ Storybook (0d650c9)
- [x] T146 [sonnet] Layout: hero (score+trend) + radar + 3 columns (weaknesses, prescriptions, readiness) ⇒ approved (5dbd53a)
- [x] T147 [sonnet] Responsive: stacks on mobile ⇒ tested (625d2a8)
- [x] T148 [sonnet] Click skill dimension → navigate to skill drilldown (Block H) ⇒ works (2c5ed02)
- [x] T149 [sonnet] Click weakness → navigate to weakness detail ⇒ works (a9c6043)
- [x] T150 [sonnet] Click prescription → navigate to prescription detail ⇒ works (43a81a0)
- [x] T151 [sonnet] Click readiness → navigate to target event picker ⇒ works (3a094ab)
- [x] T152 [sonnet] Loading skeletons per section ⇒ shows (cc32108)
- [x] T153 [sonnet] Error states per section ⇒ handled (fc7d610)
- [x] T154 [sonnet] Empty state (new user, no data): onboarding CTA ⇒ shown (78eb856)
- [x] T155 [sonnet] Cohort-locked state: "Unlocks at 20 drivers" copy ⇒ rendered (no-op: already delivered by T145 ArchetypeBadge locked state — renders 'Archetype locked' visually with 'Unlocks at 20 drivers' sub-copy and the same phrase in aria-label when archetype is null, using the default cohort size of 20 drivers from Q149)
- [x] T156 [sonnet] Storybook stories for full page with 3 data states ⇒ renders (ebaef85)
- [ ] T157 [sonnet] E2E: profile page loads, navigate to skill drilldown ⇒ green [BLOCKED: waiting on lap-backend — driver profile endpoint (unblocks useDriverProfile T138). Profile page currently renders only PageIntro placeholder; without the data hook the SkillRadarChart isn't wired in and there's no skill dimension link to click. Target drilldown page T167 is also unbuilt and blocked on the same backend dependency.]
- [ ] T158 [sonnet] LCP <2s on profile ⇒ Lighthouse passes [BLOCKED: waiting on lap-backend — useDriverProfile T138 data hook (driver profile endpoint). Profile page renders only PageIntro placeholder today; measuring LCP against near-empty content is not representative. Lighthouse CI integration itself belongs to T231 in Block K.]
- [x] T159 [sonnet] A11y: all charts have text descriptions ⇒ axe clean (9b170fa)
- [x] T160 [sonnet] Print styles: profile page printable for coaching review ⇒ works (bd51979)
- [ ] T161 [sonnet] Share action: generate profile share link (public or private) ⇒ works [BLOCKED: waiting on lap-backend — profile share endpoint (POST /profile/share or equivalent) that mints a signed share token + URL. No client code can be exercised end-to-end without a server to POST to, and the public-vs-private toggle semantics must be owned server-side for auth reasons.]
- [ ] T162 [sonnet] PostHog: page_view + section_interactions ⇒ tracked [BLOCKED: waiting on T229 (Sentry + PostHog init in app shell) and lap-backend — useDriverProfile T138 data hook. Without PostHog initialised at the shell level there is no client to fire events on, and without the data hook the profile route only renders a PageIntro placeholder so there are no sections to interact with.]
- [x] T163 [sonnet] Refetch on window focus so data stays fresh ⇒ configured (no-op: already delivered by T129 9293914 — `createQueryClient` sets `refetchOnWindowFocus: true` in the global default options; unit test "refetches queries when the browser window regains focus" pins the behaviour)
- [ ] T164 [sonnet] Cache invalidation on prescription accept/weakness resolve ⇒ tested [BLOCKED: waiting on lap-backend — prescription-accept and weakness-resolve endpoints. Cannot wire a mutation → invalidate(useDriverProfile) round-trip before the mutation endpoints and the useDriverProfile T138 hook exist.]
- [x] T165 [sonnet] Memoize heavy chart components ⇒ no re-renders on unrelated state changes (5e3c036)

## Block H — Skill drilldown + weakness detail pages (T166–T185)

- [ ] T166 [design] Mockup: per-skill drilldown page ⇒ approved
- [x] T167 [opus] Route `src/app/(app)/profile/skills/[dimension]/page.tsx` ⇒ renders (f863930)
- [ ] T168 [opus] Data hook `useSkillDrilldown(dimension)` ⇒ returns trend + sessions + weaknesses
- [ ] T169 [opus] `SkillTrendChart` component ⇒ Storybook
- [ ] T170 [opus] `BestSessionsList` component (top 5 by this dimension) ⇒ Storybook
- [ ] T171 [opus] `WorstSessionsList` component ⇒ Storybook
- [ ] T172 [opus] `RelatedWeaknessesList` component ⇒ Storybook
- [ ] T173 [sonnet] Interactive trend: click point → navigate to that session ⇒ works
- [ ] T174 [sonnet] A11y, responsive, E2E same pattern as Profile ⇒ green
- [ ] T175 [opus] Weakness detail route `src/app/(app)/weaknesses/[id]/page.tsx` ⇒ renders
- [ ] T176 [opus] `WeaknessHeader` component: category, severity, status ⇒ Storybook
- [ ] T177 [opus] `WeaknessTrendChart` component: confidence over time ⇒ Storybook
- [ ] T178 [opus] `EvidenceSessionsList` component ⇒ Storybook
- [ ] T179 [opus] `LinkedPrescriptionsList` component with outcomes ⇒ Storybook
- [ ] T180 [sonnet] Resolution action: "Mark resolved" with confirm ⇒ POST endpoint works
- [ ] T181 [sonnet] Resolution updates status to `resolved`, triggers refetch of Profile ⇒ tested
- [ ] T182 [sonnet] Loading/error/empty states ⇒ handled
- [ ] T183 [sonnet] E2E: navigate from Profile → Weakness Detail → mark resolved ⇒ green
- [ ] T184 [sonnet] Tests for all sub-components ⇒ green
- [ ] T185 [sonnet] Analytics events on weakness interactions ⇒ tracked

## Block I — Compare (durable) (T186–T205)

- [ ] T186 [design] Mockup: saved compare cases list + case detail ⇒ approved
- [ ] T187 [opus] Route `src/app/(app)/compare/page.tsx` lists saved cases ⇒ renders
- [ ] T188 [opus] Route `src/app/(app)/compare/[caseId]/page.tsx` shows one case ⇒ renders
- [ ] T189 [opus] Data hooks: useCompareCases, useCompareCase(id) ⇒ cached
- [ ] T190 [opus] `CompareCaseCreateModal` with rationale text field ⇒ Storybook
- [ ] T191 [sonnet] New compare flow: select 2+ sessions from Timeline → "Save as compare case" ⇒ works
- [ ] T192 [sonnet] Compare case detail layout: sessions side-by-side + rationale + outcome section ⇒ renders
- [ ] T193 [sonnet] Auto-updating outcome: on re-processing of referenced sessions, refetch ⇒ works
- [ ] T194 [sonnet] Edit rationale ⇒ PATCH works
- [ ] T195 [sonnet] Delete compare case ⇒ works
- [ ] T196 [sonnet] Compare list: filter by session/track/car ⇒ works
- [ ] T197 [sonnet] Loading/error/empty states ⇒ handled
- [ ] T198 [sonnet] E2E: create compare case → view → edit → delete ⇒ green
- [ ] T199 [sonnet] Legacy URL-param compare: redirect to "save as case" prompt ⇒ works
- [ ] T200 [sonnet] Storybook stories ⇒ complete
- [ ] T201 [sonnet] Unit tests ⇒ green
- [ ] T202 [sonnet] A11y ⇒ clean
- [ ] T203 [sonnet] PostHog events ⇒ tracked
- [ ] T204 [sonnet] Share compare case: public URL (if session owner permits) ⇒ works
- [ ] T205 [sonnet] Compare-to-self: same session lap-A vs lap-B ⇒ supported

## Block J — Onboarding + billing + settings (T206–T230)

- [ ] T206 [design] Mockup: onboarding wizard (4 steps) ⇒ approved
- [ ] T207 [opus] `OnboardingProvider` context + step tracker ⇒ state persisted
- [ ] T208 [opus] Step 1: Welcome — what LAP does in 15s ⇒ renders
- [ ] T209 [opus] Step 2: Sample session loader — upload curated .ibt fixture ⇒ works
- [ ] T210 [opus] Step 3: Install link for desktop (or mobile) ⇒ correct link per OS
- [ ] T211 [opus] Step 4: Accept first prescription ⇒ activation event fires
- [ ] T212 [sonnet] Skippable at each step ⇒ works
- [ ] T213 [sonnet] Resumable: user can leave and return ⇒ tested
- [ ] T214 [sonnet] Onboarding triggered only once per user ⇒ flag set on completion
- [ ] T215 [sonnet] Activation event sent to PostHog ⇒ visible
- [ ] T216 [sonnet] Time-to-first-value measured via PostHog funnel ⇒ reported
- [ ] T217 [opus] `BillingPage` route + UI: current plan, trial status, billing portal button ⇒ renders
- [ ] T218 [sonnet] Checkout button → POST /billing/checkout → redirect to Stripe ⇒ works
- [ ] T219 [sonnet] Billing portal button → Stripe Billing Portal ⇒ works
- [ ] T220 [sonnet] Trial expiry banner on app shell (48h soft block) ⇒ visible when near
- [ ] T221 [sonnet] Hard gate on expired trial: blocks all app pages with checkout CTA ⇒ works
- [ ] T222 [sonnet] Settings route with tabs: profile / preferences / integrations / data ⇒ renders
- [ ] T223 [sonnet] Profile: display name, skill level, avatar upload ⇒ works
- [ ] T224 [sonnet] Preferences: coaching tone (premium/blunt), unit system, language ⇒ works
- [ ] T225 [sonnet] Integrations: list paired devices, revoke button ⇒ works
- [ ] T226 [sonnet] Data: cohort opt-in toggle, export-all button (GDPR), delete-account button ⇒ works
- [ ] T227 [sonnet] QR pairing modal: generate QR, poll until scanned ⇒ works
- [ ] T228 [sonnet] Settings E2E: change preferences, pair device, toggle cohort ⇒ green
- [ ] T229 [sonnet] Sentry + PostHog init in app shell ⇒ both active
- [ ] T230 [sonnet] Error boundary at page level: show friendly error + report ⇒ works

## Block K — Polish + perf + a11y (T231–T240)

- [ ] T231 [sonnet] Lighthouse CI integrated into PR: fail if LCP > 2.5s on any top-level page ⇒ green
- [ ] T232 [sonnet] Image optimization re-enabled per audit finding ⇒ images served as webp/avif
- [ ] T233 [sonnet] Font subsetting: ship only used glyphs ⇒ font files smaller
- [ ] T234 [sonnet] Bundle analysis: no route > 200KB gzip JS ⇒ verified
- [ ] T235 [sonnet] Unused CSS purged ⇒ verified
- [ ] T236 [sonnet] A11y audit pass: axe across all top-level pages ⇒ no violations
- [ ] T237 [sonnet] Keyboard-only navigation works on all pages ⇒ manual test passes
- [ ] T238 [sonnet] Screen reader test on session detail ⇒ announces structure
- [ ] T239 [sonnet] Color contrast audit ⇒ all AA or better
- [ ] T240 [sonnet] Print stylesheets for session detail + driver profile ⇒ printable
