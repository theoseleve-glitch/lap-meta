# LAP — 6-Month Roadmap (2026-04-23 → 2026-10-31)

**Today:** 2026-04-23.
**Paid target hit:** 2026-10-31 (1000+ paying users, €10K+ MRR trajectory).
**Calendar:** 27 work weeks. August has 10 days off (you flagged in Q33) — Month 4 adjusts.

**Format:** monthly themes, weekly milestones, critical-path arrows, parallel-lane notation.

---

## Legend

- `[BLOCK]` — must complete before downstream tasks start
- `[PAR: X]` — can run in parallel with X
- `[AI: claude-opus]` — recommended AI tool (see `11-AI-PLAYBOOK.md`)
- `🔴 P0` — merge-blocking, ship-blocking if missed
- `🟡 P1` — high priority, slip buffer ≤1 week
- `🟢 P2` — nice-to-have within month

---

## Overview (the map before the details)

```
M1 FOUNDATION          M2 INTELLIGENCE       M3 PUBLIC BETA        M4 BRIDGE             M5 V1 RELEASE         M6 SCALE
Apr 23 → May 22        May 23 → Jun 22       Jun 23 → Jul 23       Jul 24 → Aug 23       Aug 24 → Sep 23       Sep 24 → Oct 31

Backend: FastAPI       Backend: 3 objects    Backend: bridge API   Backend: cohort prep  Backend: calendar     Backend: cohort ON
   +schemas+Bundle v2  Webapp: next_actions  Webapp: Driver OS     Webapp: TransferLink  Webapp: events        Webapp: B2B scaffold
Desktop: P0 fixes      Desktop: live proc    Marketing: standalone UI                    Mobile: Android α     Mobile: WearOS+Watch
Mobile: never-lose     Mobile: upload queue  Stripe live           Desktop: mode system  Desktop: pit-armed    Marketing: SEO push
Marketing: prep        Private beta (30)     ▲ PUBLIC BETA LIVE   Coaching library 60+  ▲ V1 RELEASE         ▲ 1000 PAID TARGET
                                                                                                              1000 WPD
    ▲ internal alpha   ▲ closed beta         ▲ paid trials start  ▲ transfer reports    ▲ android beta        B2B door opens
```

---

## Month 1 — FOUNDATION HARDENING (Apr 23 → May 22)

**Theme:** Nothing new ships. P0 defects die. Contracts get locked. Everything downstream depends on M1 being clean.

**Milestones:**
- 🔴 **M1.1** Schema registry (`lap-schemas`) published with top 10 Pydantic models + TS/Swift codegen working.
- 🔴 **M1.2** FastAPI backend skeleton up, auth wired (Clerk), `/sessions/ingest` endpoint accepting Bundle v2 payloads.
- 🔴 **M1.3** All audit P0 defects fixed (see task list).
- 🔴 **M1.4** Marketing site extracted to standalone Astro repo, skeleton deployed.
- 🟡 **M1.5** Stripe integration prototyped (checkout flow dev-mode).
- 🟡 **M1.6** Observability in place (PostHog + Sentry across all clients).

### Week 1 (Apr 23 → Apr 29) — Damage control

Goal: unblock everything.

| Day | Task | AI | Parallel? |
|---|---|---|---|
| Mon-Tue | 🔴 Desktop P0: fix `live_telemetry_processor` import break (rip-and-rebuild per Q103) | claude-opus (architecture) + claude-sonnet (implementation) | BLOCK for all desktop work |
| Mon-Tue | 🔴 Desktop P0: fix `qml_bootstrap` test collection | claude-sonnet | PAR with above |
| Wed | 🔴 Mobile P0: remove `try!` force-unwraps in `LapCoachAppModel.live()` and `StorageService` | claude-sonnet | BLOCK for mobile work |
| Wed-Thu | 🔴 Mobile P0: `finalizeSession` integrity check (fail if temp missing) | claude-sonnet | PAR |
| Thu-Fri | 🔴 Mobile P0: prevent fullScreenCover accidental stop | claude-sonnet | PAR |
| Fri | Repo reorg: create `lap-backend`, `lap-schemas`, rename `lap-website/src/app/app` → future `lap-webapp` | codex (mechanical moves) | BLOCK M1.1 |
| Fri | 🟡 Webapp P0: fix `/api/v1` double-prefix in bundle hooks | codex | PAR |
| Fri | 🟡 Webapp P0: resolve `/sessions/:id/channels` duplicate route | codex | PAR |

**End-of-week-1 gate:** CI green on all four repos. No merge goes through without green CI.

### Week 2 (Apr 30 → May 6) — Contracts

Goal: `lap-schemas` live with the models every other repo will consume.

| Task | AI | Notes |
|---|---|---|
| 🔴 Define Pydantic v2 models for `SessionManifest`, `SessionRecord`, `TelemetrySample`, `DataQuality`, `SensorConfigSnapshot` | claude-opus | BLOCK all ingestion work. See ADR-006. |
| 🔴 Add the 7 backend object skeletons (fields shapes from ADR-005, empty methods) | claude-opus | PAR with above |
| 🔴 OpenAPI 3.1 generation pipeline | claude-sonnet | PAR |
| 🔴 TypeScript codegen pipeline (`openapi-typescript`) | claude-sonnet | PAR |
| 🔴 Swift codegen pipeline (`openapi-generator`) | claude-sonnet | PAR |
| 🔴 CI rule: "PR mutating Pydantic schemas must include regenerated TS + Swift" | codex | PAR |
| 🟡 Decide ORM: SQLAlchemy 2.0 + Alembic. Scaffold base models. | claude-opus | PAR |
| 🟡 Decide DB: Postgres 16 on Neon (serverless Postgres, generous free tier, scales). | — | decision only |

**End-of-week-2 gate:** Someone runs `pnpm --filter lap-schemas generate` and TS + Swift files appear. Any Pydantic change fails CI in dependent repos until regenerated.

### Week 3 (May 7 → May 13) — FastAPI skeleton + Stripe prototype

| Task | AI | Notes |
|---|---|---|
| 🔴 FastAPI app structure: `lap-backend/app/` with routers per domain (sessions, driver, coaching, bridge, admin) | claude-opus | BLOCK for ingestion |
| 🔴 Clerk auth middleware for FastAPI | claude-sonnet | BLOCK for any authenticated endpoint |
| 🔴 `POST /api/v1/sessions/ingest` (ADR-012) accepting Bundle v2 | claude-opus | blocks all clients' upload integration |
| 🔴 Celery worker setup, first job: `process_session_ingest` (skeleton, no processing yet) | claude-sonnet | PAR with ingest endpoint |
| 🔴 UUIDv7 generation + DB migration for existing tables | claude-sonnet | PAR |
| 🟡 Stripe checkout dev-mode: test-account subscription creation | claude-sonnet | PAR |
| 🟡 Stripe webhook handler skeleton (`/api/v1/billing/webhooks`) | claude-sonnet | PAR |
| 🟡 Marketing site: create standalone Astro repo, import existing `src/components/rooms/*` | claude-opus | PAR — big PR, can't overlap with above for focus |

**End-of-week-3 gate:** A session payload can be POSTed to the new backend, authenticated, accepted, and queued for processing (even if processing is a no-op).

### Week 4 (May 14 → May 22) — Observability + migration

| Task | AI | Notes |
|---|---|---|
| 🔴 PostHog client integration (web, desktop, mobile) + event taxonomy | claude-sonnet | BLOCK for KPI measurement |
| 🔴 Sentry integration (web, desktop, mobile, backend) | claude-sonnet | PAR |
| 🔴 Bundle v2 writer in desktop (replace existing finalizer) | claude-opus | BLOCK desktop ingestion |
| 🔴 Bundle v2 writer in mobile (replace existing chunk upload) | claude-opus | PAR with desktop |
| 🔴 Ingestion pipeline: parse Bundle v2, validate, persist `SessionRecord` + raw artifacts | claude-opus | BLOCK all downstream |
| 🔴 Migrate existing sessions: bulk UUIDv7 assignment, re-finalize into Bundle v2 format | claude-opus | BLOCK hard cutover |
| 🟡 Admin KPI dashboard skeleton (backend-rendered, auth-gated) | claude-sonnet | PAR |
| 🟡 Weekly Slack KPI report cron (even if numbers are 0s right now) | codex | PAR |
| 🟢 Marketing site: deploy first landing page to Vercel/Cloudflare | claude-design + codex | PAR |

**End-of-Month-1 gate (internal alpha 2026-05-22):**
- All four repos compile, CI green
- Schema registry publishes TS + Swift
- FastAPI backend accepts + persists a Bundle v2 session
- Desktop writes Bundle v2
- Mobile writes Bundle v2
- Old sessions migrated
- All known P0 defects fixed
- Observability wired

---

## Month 2 — INTELLIGENCE BACKEND (May 23 → Jun 22)

**Theme:** The brain starts existing. Ship the top 3 backend objects and a first coaching library.

**Milestones:**
- 🔴 **M2.1** `WeaknessEpisode`, `ActionPrescription`, `ActionOutcome` live end-to-end (detection → UI).
- 🔴 **M2.2** `DriverProgressSnapshot` generated per session + per week.
- 🔴 **M2.3** Coaching library v0 (25-35 YAML rules, braking + throttle + consistency).
- 🔴 **M2.4** Desktop `live_telemetry_processor` rebuilt with rules engine.
- 🔴 **M2.5** Mobile "never lose a session" sprint complete.
- 🟡 **M2.6** Frontend `next_actions` payload replaces SessionDebrief heuristics.
- 🟡 **M2.7** Closed private beta (≤30 invited sim racers) by 2026-06-22.

### Week 5-6 (May 23 → Jun 5) — The three objects

| Task | AI | Deps |
|---|---|---|
| 🔴 `WeaknessEpisode` full implementation: detection engine reads finalized session → emits episodes, confidence decay job, recurrence counter | claude-opus | M1.4 complete |
| 🔴 `ActionPrescription` generator: fired when WeaknessEpisode opens/escalates, links to drill templates | claude-opus | `WeaknessEpisode` |
| 🔴 `ActionOutcome` checker: background job compares next-session data to `SuccessCondition` | claude-sonnet | PAR with above |
| 🔴 Rules engine: YAML loader, compiler, runner. Load rules from `lap-backend/coaching/library/rules/*.yaml` | claude-opus | BLOCK everything coaching |
| 🔴 First 10 rules: all braking-category. Tested against archived Sebring/Silverstone sessions. | claude-opus (rule authoring) + claude-sonnet (tests) | PAR |
| 🟡 `DriverProgressSnapshot` scorer: per-dimension scoring from session metrics, confidence from sample count | claude-opus | PAR |

### Week 7 (Jun 6 → Jun 12) — Desktop rules + mobile reliability

| Task | AI | Notes |
|---|---|---|
| 🔴 Desktop: `live_telemetry_processor` rewrite using rules engine (ADR-009). Fetch rules at session-start, execute locally. | claude-opus | BLOCK any live coaching claim |
| 🔴 Desktop: rules cache (7-day TTL, survives offline) | claude-sonnet | PAR |
| 🔴 Mobile: capture journal with heartbeat every 5s, persisted to SQLite | claude-sonnet | BLOCK "never lose" |
| 🔴 Mobile: startup reconciliation: on launch, find stale recording/finalizing states, orphan temp files, offer recovery | claude-opus | PAR |
| 🔴 Mobile: durable upload queue table (session_id, attempt_count, next_retry_at, last_http_code). Worker on bootstrap + connectivity regain. | claude-opus | PAR |
| 🔴 Mobile: preflight readiness gate before Start (track, GPS, storage, battery per Q112) | claude-sonnet | PAR |

### Week 8 (Jun 13 → Jun 22) — Frontend migration + beta prep

| Task | AI | Notes |
|---|---|---|
| 🔴 Webapp: replace SessionDebrief heuristics with `GET /api/v1/sessions/:id/next_actions` | claude-opus | BLOCK coaching claim |
| 🔴 Webapp: new "Coaching" surface on session detail: list WeaknessEpisodes, Prescriptions | claude-opus | PAR |
| 🔴 Coaching library: expand to 25-35 rules covering braking + throttle + consistency dimensions | claude-opus (authoring) | PAR |
| 🟡 Invite 30 beta users from waitlist. Send onboarding email with desktop+mobile install links | — | final day |
| 🟡 Beta feedback channel: Discord server + in-app feedback widget | codex | PAR |

**End-of-Month-2 gate (closed beta 2026-06-22):**
- 30 sim racers can sign up, install desktop, capture a session, see WeaknessEpisodes + Prescriptions, and get an ActionOutcome on the next session.
- Mobile app does not lose sessions and resumes uploads on launch.
- Coaching library fires at least 3-8 rules per session.

---

## Month 3 — PUBLIC BETA LAUNCH (Jun 23 → Jul 23)

**Theme:** Driver OS UX ships. Public launch. Stripe live. Marketing narrative finalized.

**Milestones:**
- 🔴 **M3.1** Webapp Driver Timeline live (unified sim+real chronological feed).
- 🔴 **M3.2** Driver Profile page (Strava-style, per Q84).
- 🔴 **M3.3** Durable Compare (saved cases with rationale, per Q85).
- 🔴 **M3.4** Marketing site live on production domain with "How LAP works" page.
- 🔴 **M3.5** Stripe live in production. Trial→paid flow working.
- 🔴 **M3.6** Desktop mode system (Practice/Sprint/Endurance/Review) shipped.
- 🔴 **M3.7** Public beta announced. Waitlist invited en masse.

### Week 9 (Jun 23 → Jun 29) — Driver Timeline + Driver Profile

| Task | AI | Notes |
|---|---|---|
| 🔴 Webapp: `DriverTimelinePage` — chronological feed of sessions with WeaknessEpisode/Prescription badges | claude-opus (UX) + claude-design (visual) | BLOCK beta |
| 🔴 Webapp: `DriverProfilePage` — top-level progression dashboard, skill dimensions, current open weaknesses, readiness score | claude-opus + claude-design | PAR |
| 🔴 Backend: `GET /api/v1/driver/timeline` paginated endpoint | claude-sonnet | BLOCK Timeline page |
| 🔴 Backend: `GET /api/v1/driver/profile` aggregate endpoint | claude-sonnet | BLOCK Profile page |
| 🟡 Webapp kill-list: delete `/app/jobs`, `/app/exports`, `/app/admin/race-control` pages (Q92) | codex | PAR |

### Week 10 (Jun 30 → Jul 6) — Compare + Coaching surfaces

| Task | AI | Notes |
|---|---|---|
| 🔴 Webapp: durable Compare — persist compare cases with user-added rationale + auto-updating outcome sections | claude-opus | PAR |
| 🔴 Webapp: per-dimension drilldown pages (braking, throttle, etc.) showing trend + evidence sessions | claude-opus + claude-design | PAR |
| 🔴 Webapp: onboarding flow — signup → load sample session → first insight → first prescription | claude-design (key UX) | BLOCK time-to-first-value KPI |
| 🟡 Desktop: review page — small post-session summary with "See details in webapp" CTA (Q95) | claude-sonnet | PAR |

### Week 11 (Jul 7 → Jul 13) — Desktop mode system + Stripe prod

| Task | AI | Notes |
|---|---|---|
| 🔴 Desktop: mode engine (Practice/Sprint/Endurance/Review). Binds to overlay defaults, coaching cadence, strategy assumptions (Q96) | claude-opus | BLOCK desktop public |
| 🔴 Desktop: overlay catalog reorg. Race-minimal default preset. Streamer widgets moved to "Advanced" category (Q98) | claude-sonnet + claude-design | PAR |
| 🔴 Stripe production: live keys, webhook validation, subscription state sync to user DB | claude-opus | BLOCK launch |
| 🔴 Stripe production: grandfather waitlist users at €12/mo × 12mo via coupon | codex | PAR |
| 🟡 Pricing page on marketing site: €15/mo + €150/yr, 14-day trial CTA | claude-design | PAR |

### Week 12 (Jul 14 → Jul 23) — Launch week

| Task | AI | Notes |
|---|---|---|
| 🔴 Marketing site "How LAP works" ecosystem architecture page with diagram (Q125) | claude-design | BLOCK launch |
| 🔴 Marketing site copy pass: align claims to reality (no "AI coach" claims per Q130), 14-day trial CTA consistent | claude-opus | PAR |
| 🔴 Load test: backend handles 100 concurrent session uploads, 1000 concurrent API requests | codex + claude-sonnet | BLOCK launch |
| 🔴 E2E smoke test: Sim Detect → Record → Finalize → Sync → Web Review (Q191) | claude-sonnet | BLOCK launch |
| 🔴 Beta → public: invite entire waitlist. Content calendar for launch week (blog post, Reddit, Discord announcements) | claude-opus (copy) | 2026-07-23 |
| 🔴 Launch day: public beta lives, Stripe trials open, press kit released | — | 2026-07-23 |

**End-of-Month-3 gate (public beta 2026-07-23):**
- Anyone can sign up, start 14-day trial, pay at end.
- Driver Timeline + Driver Profile + Coaching surfaces feel like a product.
- Desktop with mode system is the default installer.
- Mobile is stable on iOS (not yet Android).
- Coaching library has 40+ rules.

**Targets by end of M3:** 200 paying trials started, 50 converted, 50 active WPD.

---

## Month 4 — DESKTOP COHERENCE + SIM↔REAL BRIDGE MVP (Jul 24 → Aug 23)

**Theme:** the sim↔real promise stops being marketing. Desktop matures. Scope-adjusted for your 10 days off in August.

**Working days in Month 4:** ~22 (31 calendar - 10 off - weekends).

**Milestones:**
- 🔴 **M4.1** `TransferLink` entity live. Manual + auto-suggest linking.
- 🔴 **M4.2** Transfer diagnostics report (shape vs intensity divergence per ADR-005).
- 🔴 **M4.3** Pit-armed state on desktop strategy (not full FSM per Q97).
- 🔴 **M4.4** Coaching library to 60-80 rules.
- 🟡 **M4.5** Cohort data collection starts if ≥20 opt-in users exist.
- 🟡 **M4.6** Endurance session tagging (not full endurance UX).

### Week 13 (Jul 24 → Jul 30)

| Task | AI | Notes |
|---|---|---|
| 🔴 Backend: `TransferLink` full implementation. Shape-match algorithm (DTW or normalized cross-correlation on input signals), intensity metric (peak-value ratios) | claude-opus | BLOCK bridge |
| 🔴 Backend: `/api/v1/bridge/suggest_links` endpoint — for a given session, suggest candidate sim↔real pairs by track + car class | claude-sonnet | PAR |
| 🔴 Track equivalence table: seed with 20 common sim↔real tracks (ADR-014) | claude-opus (curation) | BLOCK auto-suggest |

### Week 14 (Jul 31 → Aug 6)

| Task | AI | Notes |
|---|---|---|
| 🔴 Webapp: Bridge view in session detail — "Link to sim equivalent" / "Link to real-life equivalent" | claude-opus | PAR |
| 🔴 Webapp: Transfer Report page — shape match score, intensity match score, divergence points, transferred/non-transferred skills | claude-opus + claude-design | BLOCK bridge KPI |
| 🔴 Desktop: pit-call "armed" signal in live strategy + overlay affordance (Q97) | claude-sonnet | PAR |
| 🟡 Coaching library: expand to 50 rules (add racecraft, tire management, minimum speed dimensions) | claude-opus | PAR |

### Week 15 (Aug 7 → Aug 13) — 5 work days (first week of 10-day break included partially)

Reduced scope. Keep shipping 1-2 critical items only.

| Task | AI | Notes |
|---|---|---|
| 🔴 Backend: cohort opt-in mechanism in Driver Profile settings (ADR-008) | claude-sonnet | PAR |
| 🔴 Bugfix + stability week. Triage beta feedback. | — | PAR |

### Week 16 (Aug 14 → Aug 23) — 8 work days after break

| Task | AI | Notes |
|---|---|---|
| 🔴 Coaching library: 60-80 rules total by end of month | claude-opus | |
| 🟡 Desktop: plan-vs-actual strategy serialized into finalized bundle (Q102) | claude-opus | PAR |
| 🟡 Endurance tagging: session metadata supports endurance event type. No dedicated UX yet. | claude-sonnet | PAR |
| 🟡 iRacing calendar fetcher prototype (Q157) | claude-sonnet | PAR |

**End-of-Month-4 gate:**
- A user with a sim session at Spa and a real-life track day at Spa can link them and see a transfer report.
- Auto-suggest proposes the link without being asked.
- Pit-armed renders during sprint/endurance overlays.

**Targets by end of M4:** 400 paid trials, 150 converted, 100 WPD, 50+ TransferLinks created.

---

## Month 5 — MOBILE + ANDROID + V1 RELEASE (Aug 24 → Sep 23)

**Theme:** Mobile story closes. Android shows up. V1 ships — the "it's actually done" moment.

**Milestones:**
- 🔴 **M5.1** Android app beta (feature parity with iOS on capture + sync + light coaching).
- 🔴 **M5.2** Apple Watch / WearOS companion app (steering telemetry from wrist motion + heart rate).
- 🔴 **M5.3** Endurance event support (stint-level metadata, long-run consistency tracking).
- 🔴 **M5.4** iRacing special-event calendar integration.
- 🔴 **M5.5** Coaching library at 100+ rules.
- 🔴 **M5.6** V1 release — marketing push.

### Week 17 (Aug 24 → Aug 30)

| Task | AI | Notes |
|---|---|---|
| 🔴 Android scaffold: Kotlin + Jetpack Compose. Port `lap-mobile` capture architecture. | claude-opus (architecture) + claude-sonnet (implementation) | BLOCK Android beta |
| 🔴 Shared Android ingestion contract via generated Kotlin types from `lap-schemas` | claude-sonnet | PAR |
| 🔴 Android: BLE UART for RaceBox (Kotlin coroutine BLE) | claude-sonnet | BLOCK Android RaceBox |

### Week 18 (Aug 31 → Sep 6)

| Task | AI | Notes |
|---|---|---|
| 🔴 Android: capture + finalize + upload queue parity with iOS | claude-opus | |
| 🔴 Android: CoreLocation → FusedLocationProvider, CoreMotion → SensorManager | claude-sonnet | PAR |
| 🟡 Apple Watch companion: heart rate sampling + wrist motion streaming to phone | claude-sonnet | PAR |

### Week 19 (Sep 7 → Sep 13)

| Task | AI | Notes |
|---|---|---|
| 🔴 WearOS companion (Q120): heart rate + wrist motion. Shared BLE protocol with Apple Watch. | claude-sonnet | PAR |
| 🔴 Endurance event support backend: stint-level timing, long-run consistency dimension weighted higher | claude-opus | |
| 🔴 iRacing calendar integration: weekly fetch of iRacing schedule, user can pin target events | claude-opus | |

### Week 20 (Sep 14 → Sep 23)

| Task | AI | Notes |
|---|---|---|
| 🔴 V1 feature freeze at 2026-09-16. Bugfix + polish only. | — | |
| 🔴 Coaching library audit: verify 100+ rules passing unit tests against archive | claude-opus | |
| 🔴 V1 marketing push: release notes, changelog page, updated homepage copy, press outreach | claude-opus | |
| 🔴 V1 launch 2026-09-23 | — | |

**Targets by end of M5:** 700 paid trials lifetime, 400 converted, 300 WPD.

---

## Month 6 — SCALE, COHORT, B2B DOOR (Sep 24 → Oct 31)

**Theme:** consolidate, grow, open B2B conversations.

**Milestones:**
- 🔴 **M6.1** Cohort benchmarks live if ≥20 opt-in users (they should exist by now).
- 🔴 **M6.2** 1000+ paying users hit.
- 🔴 **M6.3** B2B outbound: reach out to 10 racing schools / karting academies.
- 🟡 **M6.4** SEO content push (4 pillar pages, 8 blog posts).
- 🟡 **M6.5** Coaching library to 150 rules.

### Week 21-24 (Sep 24 → Oct 22) — Scale + cohort

| Task | AI | Notes |
|---|---|---|
| 🔴 Turn on `DriverBenchmarkProfile` generation, validate ≥20 opt-in users exist per track+car context | claude-opus | |
| 🔴 Webapp: percentile views on Driver Profile | claude-design | PAR |
| 🟡 B2B outbound: landing page `/for-schools`, outreach email template, list of 10 target academies | claude-opus (outreach copy) | PAR |
| 🟡 SEO: 4 pillar pages ("What is trail braking", "iRacing to real-life transfer", "Best telemetry apps compared", "Driver improvement plan") | claude-opus (long-form) | PAR |
| 🟡 8 blog posts on coaching rules, beta user stories | claude-opus | PAR |

### Week 25-27 (Oct 23 → Oct 31) — Final push

| Task | AI | Notes |
|---|---|---|
| 🔴 Hit 1000 paying users. Daily funnel analysis. Paid ads if needed (budget ≤€500). | — | |
| 🟡 Coaching library to 150 rules | claude-opus | |
| 🟡 Q4 planning doc — what's next for Nov-Dec | claude-opus | |

**End-of-Month-6 gate (2026-10-31):**
- 1000+ paying users, €12-15K MRR trajectory
- 750+ WPD
- 500+ TransferLinks created
- 55%+ prescription efficacy
- First B2B conversation in progress
- Coaching library at 150 rules

---

## Critical path (end-to-end dependency chain)

```
W1: P0 fixes across all repos
     ↓
W2: lap-schemas publishes contracts  ← BLOCKS EVERYTHING DOWNSTREAM
     ↓
W3: FastAPI ingest endpoint live
     ↓
W4: Bundle v2 writers on desktop + mobile, migration done
     ↓
W5-6: WeaknessEpisode + ActionPrescription + ActionOutcome in backend
     ↓
W7: Desktop rules engine (needs coaching library seeded)
W7: Mobile never-lose-a-session (parallel, different repo)
     ↓
W8: Frontend next_actions migration (needs WeaknessEpisode)
     ↓
W9-11: Driver Timeline + Profile + Compare + Mode system (parallel across webapp + desktop)
     ↓
W12: PUBLIC BETA LAUNCH ← single biggest risk point
     ↓
W13-16: TransferLink end-to-end (needs Driver Profile as destination for insights)
     ↓
W17-20: Android + Watch + V1 (parallel with W21+)
     ↓
W21-27: Scale
```

## Parallelization lanes

You're solo. AI assistance lets you parallelize conceptually even when you're not physically multitasking. Here's the lane plan:

**Lane A (YOU primary):** Architecture + critical-path coding. Anything requiring judgment.
**Lane B (AI + YOU supervising):** Coaching library rule authoring. Review each rule. ~1-2 hours/day.
**Lane C (AI mostly):** Boilerplate (Pydantic models, React skeletons, tests). You review PRs.
**Lane D (AI + quick review):** Documentation, marketing copy, blog posts.

Rough time split per week:
- 60% Lane A (30-36h)
- 15% Lane B (8-9h)
- 15% Lane C (8-9h)
- 10% Lane D (5-6h)

## Sprint-end gates (weekly ritual)

Every Friday 17:00 CET, you:
1. Check CI green on all repos
2. Check PostHog: are KPIs moving toward targets?
3. Check Sentry: any new error classes?
4. Review next week's task list, adjust for slippage
5. If slipped >2 days on a `[BLOCK]` task — pivot meeting (with yourself or a trusted peer). Consider descoping, not pushing.

## Forced-pivot triggers (go/no-go criteria)

If any of these fire, pause feature work and address:
- CI green <90% for 3 consecutive days
- Session-loss incident reported by a beta/paid user
- Beta activation rate <25% after 2 weeks of collection
- Desktop crash rate >1% of sessions
- Mobile upload success rate <95% sustained for a week
- Stripe/billing broken for >2 hours in production
- 3+ paying users churn in a single week citing "broken feature"

Pivot = stop feature work, fix root cause, resume only after green.
