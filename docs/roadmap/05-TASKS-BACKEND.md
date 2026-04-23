# LAP — Backend Task Backlog

**Repo:** `lap-backend` (new, absorbs `lap_tool_virtualisation` + old Flask API)
**Stack:** Python 3.12, FastAPI 0.115+, Pydantic v2, SQLAlchemy 2.0 + Alembic, Celery 5.4 + Redis, Postgres 16 (Neon), Clerk (auth), Stripe, PostHog, Sentry.
**Task format:** `BE-NNN` — AI tools in brackets. Hours are solo+AI estimates.

---

## Month 1 — Foundation

### BE-001 🔴 Scaffold FastAPI project structure
- **Month/week:** M1/W2
- **Deps:** none (entry point)
- **Parallel with:** BE-002 (schemas)
- **AI:** claude-opus (architecture design) + codex (boilerplate)
- **Hours:** 6-8
- **Context:** Create `lap-backend/` with domain-driven layout per CLAUDE.md. Top-level: `app/`, `domain/`, `infra/`, `coaching/`, `tests/`. `app/` has routers. `domain/` has pure business logic. `infra/` has DB + external adapters.
- **Acceptance:**
  - `uv sync` succeeds
  - `uvicorn app.main:app --reload` starts
  - Health check `/healthz` returns 200
  - CI runs ruff + mypy --strict on `domain/` and `app/`

### BE-002 🔴 Publish `lap-schemas` package with Pydantic v2 models
- **Month/week:** M1/W2
- **Deps:** none (entry point)
- **Parallel with:** BE-001
- **AI:** claude-opus (model design from ADR-005, ADR-006) + codex (boilerplate)
- **Hours:** 10-14
- **Context:** Standalone `lap-schemas/` package in the monorepo. Publishes `SessionManifest`, `SessionRecord`, `TelemetrySample`, `DataQuality`, `SensorConfigSnapshot`, and the 7 backend object shapes. Uses Pydantic v2 with strict validation. Exports are versioned — `lap_schemas.v1.session.SessionManifest`.
- **Acceptance:**
  - Every field from ADR-005 and ADR-006 modeled with correct types
  - `pytest tests/schemas/` green
  - `python -m lap_schemas.generate_openapi > openapi.json` produces valid OpenAPI 3.1

### BE-003 🔴 TypeScript codegen pipeline from OpenAPI
- **Month/week:** M1/W2
- **Deps:** BE-002
- **Parallel with:** BE-004
- **AI:** codex (pipeline script)
- **Hours:** 3-4
- **Context:** Use `openapi-typescript@7` to generate TS types into `lap-schemas/typescript/src/generated/`. Publish as a private npm package (or internal workspace) consumed by `lap-webapp` and `lap-website`.
- **Acceptance:**
  - `pnpm --filter lap-schemas generate:ts` produces `.d.ts` files
  - Types are importable as `import type { SessionManifest } from '@lap/schemas'`

### BE-004 🔴 Swift codegen pipeline from OpenAPI
- **Month/week:** M1/W2
- **Deps:** BE-002
- **Parallel with:** BE-003
- **AI:** codex
- **Hours:** 4-6
- **Context:** Use `openapi-generator-cli` Swift5 template. Output into `lap-mobile/LapCoachMobileApp/Generated/`.
- **Acceptance:**
  - `make swift-codegen` produces Swift structs
  - `xcodebuild` compiles the generated code

### BE-005 🔴 Database schema + first migration
- **Month/week:** M1/W2
- **Deps:** BE-002
- **Parallel with:** BE-006
- **AI:** claude-opus (schema design) + codex (Alembic migration)
- **Hours:** 8-10
- **Context:** Tables: `users`, `driver_profiles`, `sessions`, `session_records`, `telemetry_chunks` (references only, actual data in object storage), `weakness_episodes`, `action_prescriptions`, `action_outcomes`, `driver_progress_snapshots`, `transfer_links`, `driver_benchmark_profiles`, `driver_readiness_states`. All use UUIDv7 PKs. Foreign keys + indexes explicit. Row-level security (RLS) policies in Postgres.
- **Acceptance:**
  - `alembic upgrade head` from blank DB works
  - `alembic downgrade base` cleans up
  - RLS enforced: user A cannot SELECT from user B's sessions even with direct DB access

### BE-006 🔴 Clerk auth middleware for FastAPI
- **Month/week:** M1/W3
- **Deps:** BE-001
- **AI:** claude-sonnet (integration)
- **Hours:** 4-6
- **Context:** Clerk provides JWTs in `Authorization: Bearer`. Middleware validates against Clerk's JWKS, extracts `user_id`, fetches or creates a LAP `User` row on first call, attaches to request state.
- **Acceptance:**
  - `/api/v1/me` returns current user
  - Unauthenticated requests to protected routes return 401
  - First-time Clerk users get a LAP user row auto-provisioned

### BE-007 🔴 `POST /api/v1/sessions/ingest` endpoint
- **Month/week:** M1/W3
- **Deps:** BE-002, BE-005, BE-006
- **AI:** claude-opus (contract design) + claude-sonnet (implementation)
- **Hours:** 12-16
- **Context:** Per ADR-012. Accepts multipart/form-data: a `manifest` field (JSON matching `SessionManifest`) + `chunks[]` (telemetry files). Validates manifest. Persists to object storage (Cloudflare R2 or S3). Creates `Session` + `SessionRecord` rows. Dispatches Celery job. Returns 202 with `session_id`, `ingest_job_id`, SSE stream URL.
- **Acceptance:**
  - Happy path: returns 202 with valid IDs within 2s
  - Idempotency: same `Idempotency-Key` returns same response
  - Invalid manifest: 422 with clear field errors
  - Huge payload (500MB telemetry): streaming works, no memory spike

### BE-008 🔴 Celery worker setup + `process_session_ingest` skeleton
- **Month/week:** M1/W3
- **Deps:** BE-007
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Celery 5.4 with Redis broker + result backend. First job `process_session_ingest(session_id)`: for now just reads the manifest, validates, computes checksums, marks session `ready`. Real processing comes in BE-015+.
- **Acceptance:**
  - Celery worker boots with `celery -A app.infra.celery worker`
  - Job completes in <5s for a small session
  - Failure modes: Celery retry policy with exponential backoff, surfaced to SSE stream

### BE-009 🔴 SSE job status endpoint
- **Month/week:** M1/W3
- **Deps:** BE-008
- **Parallel with:** BE-010
- **AI:** claude-sonnet
- **Hours:** 4-5
- **Context:** `GET /api/v1/jobs/:id/events` returns SSE stream. Events: `queued`, `processing`, `stage:N`, `completed`, `failed`. Clients can subscribe to see ingestion progress.
- **Acceptance:**
  - SSE stream stays alive 30 min
  - Reconnection via `Last-Event-ID` works
  - Events are newline-delimited JSON

### BE-010 🟡 Stripe subscription infrastructure
- **Month/week:** M1/W3
- **Deps:** BE-006
- **Parallel with:** BE-009
- **AI:** claude-opus (flow) + claude-sonnet (implementation)
- **Hours:** 10-12
- **Context:** Stripe test mode. Create `/api/v1/billing/checkout` → returns Stripe Checkout session URL for €15/mo or €150/yr. Webhook at `/api/v1/billing/webhooks` handles `customer.subscription.*`, `invoice.*`. Sync subscription state to `users.subscription_status`. 14-day trial by default.
- **Acceptance:**
  - Dev-mode: user can click pay → reach Stripe Checkout → subscribe → return → `/api/v1/me` shows `subscription_status: trialing`
  - Webhook signature validated
  - Grandfather coupon for waitlist: `WAITLIST_FOUNDER` gives 20% off for 12 months

### BE-011 🔴 Bulk migration: existing sessions → UUIDv7 + Bundle v2
- **Month/week:** M1/W4
- **Deps:** BE-007
- **AI:** claude-opus (safety planning) + claude-sonnet (migration script)
- **Hours:** 10-14
- **Context:** One-time script that reads existing sessions (old IDs, old bundle format), assigns UUIDv7, re-finalizes into Bundle v2 shape, uploads to object storage, updates DB. Keeps old ID → new ID alias table for URL backward-compat (deprecate at M6).
- **Acceptance:**
  - Dry-run mode first
  - All existing sessions migrated without data loss
  - Old URLs `/sessions/:old_id` redirect to `/sessions/:new_id`
  - Rollback script exists

### BE-012 🔴 Observability: Sentry + PostHog backend SDK
- **Month/week:** M1/W4
- **Deps:** BE-001
- **Parallel with:** most M1/W4 tasks
- **AI:** codex
- **Hours:** 3-4
- **Context:** Sentry for exceptions + performance. PostHog for product analytics server-side (ingest events, activation tracking).
- **Acceptance:**
  - Unhandled exception in FastAPI appears in Sentry within 1 min
  - Custom event `session_ingested` appears in PostHog

### BE-013 🟡 Admin KPI dashboard skeleton
- **Month/week:** M1/W4
- **Deps:** BE-006, BE-012
- **AI:** claude-sonnet + claude-design
- **Hours:** 8-10
- **Context:** `/admin/kpis` auth-gated page. Shows WPD, activation rate, upload success rate, active incidents. Server-rendered HTML with htmx for live updates.
- **Acceptance:**
  - Accessible only to `is_admin=true` users
  - Numbers update within 5 min of events
  - Includes "Recent failed ingestions" table

### BE-014 🟡 Weekly KPI Slack report
- **Month/week:** M1/W4
- **Deps:** BE-013
- **AI:** codex
- **Hours:** 3-4
- **Context:** Cron every Monday 09:00 UTC: compute last-week KPIs, post to Slack channel `#lap-kpi`. Diff vs prior week highlighted.

---

## Month 2 — Intelligence

### BE-015 🔴 Session processing pipeline — parse + persist core
- **Month/week:** M2/W5
- **Deps:** BE-007, BE-011
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Celery job chain: `parse_bundle` → `validate_checksums` → `compute_lap_splits` (using track catalog) → `extract_session_metrics` → `compute_data_quality` → persist. No coaching yet.
- **Acceptance:**
  - Real iRacing `.ibt` archived session processes end-to-end in <30s
  - Real RaceBox session from archive processes in <30s
  - Failures retried 3x with backoff, then marked `failed` with user-facing reason

### BE-016 🔴 Track catalog + sector detection
- **Month/week:** M2/W5
- **Deps:** BE-005
- **Parallel with:** BE-015
- **AI:** claude-opus (catalog design) + claude-sonnet (algorithms)
- **Hours:** 10-14
- **Context:** Seed catalog with 30 tracks (iRacing exports + OSM). `TrackLayout` has start/finish coords, sector splits, official corner names, sim↔real master mapping. Algorithm: given a GPS trace, detect lap crossings vs start/finish line.
- **Acceptance:**
  - 30 tracks seeded
  - Lap detection accuracy >99% on archived Sebring sessions (manual validation)
  - Sim↔real mapping: Spa-iRacing and Spa-real map to same `master_track_id`

### BE-017 🔴 Coaching library rules engine — loader + runner
- **Month/week:** M2/W5
- **Deps:** BE-002
- **Parallel with:** BE-015, BE-016
- **AI:** claude-opus (engine design) + claude-sonnet (implementation)
- **Hours:** 16-20
- **Context:** Load YAML rules from `coaching/library/rules/**/*.yaml`. Compile condition strings into callable predicates. Rules engine runs over a processed session and emits `CoachingInsight` records. Includes versioning — rules have `id + version`, insights reference which rule+version generated them.
- **Acceptance:**
  - `python -m coaching.engine.run --session-id X` outputs insights
  - Rules can reference session features (`apex_speed`, `brake_pressure_peak`, etc.) via a stable feature namespace
  - Misconfigured rule fails fast at load time (not at runtime)

### BE-018 🔴 First 10 coaching rules (braking category)
- **Month/week:** M2/W5-6
- **Deps:** BE-017
- **AI:** claude-opus (authoring) + claude-sonnet (tests)
- **Hours:** 16-20
- **Context:** Author 10 YAML rules covering late braking, early braking, abrupt release, insufficient trail brake, inconsistent brake pressure, brake lock-up patterns, released-too-early, brake-balance complaints, cold-brake first-lap, and over-braking mid-corner. Each rule unit-tested against 3+ archived sessions.
- **Acceptance:**
  - 10 rules in `coaching/library/rules/braking/`
  - Each has explanation templates at beginner/intermediate/advanced levels
  - Each has a drill template linked
  - `pytest coaching/tests/braking/` green on archive sessions

### BE-019 🔴 `WeaknessEpisode` lifecycle (open / update / resolve)
- **Month/week:** M2/W6
- **Deps:** BE-017
- **AI:** claude-opus
- **Hours:** 12-16
- **Context:** Per ADR-005 §5.2. Aggregator job: takes session's `CoachingInsight` records, matches to existing open episodes or opens new. Confidence decay job runs nightly. Resolution logic: if a weakness's success condition was met across the last N sessions, mark resolved.
- **Acceptance:**
  - Session A → opens 3 WeaknessEpisodes
  - Session B (7 days later) with same weaknesses → confidence rises, no duplicate episodes
  - Session C with different weaknesses → existing episodes decay

### BE-020 🔴 `ActionPrescription` generator
- **Month/week:** M2/W6
- **Deps:** BE-019
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** When WeaknessEpisode opens/escalates to medium/high severity → emit ActionPrescription. Draws drill template from library rule. Sets `success_condition` from rule template.
- **Acceptance:**
  - Each new episode of severity ≥ medium creates exactly one Prescription
  - Prescriptions have measurable `success_condition`
  - Duplicate prescriptions for same weakness are prevented

### BE-021 🔴 `ActionOutcome` background checker
- **Month/week:** M2/W7
- **Deps:** BE-020
- **AI:** claude-sonnet
- **Hours:** 8-10
- **Context:** After each new session ingests, check: are there any `ActionPrescription` for this driver marked `accepted` whose `measurement_window` includes this session? If yes, evaluate `success_condition` against the new session's metrics, persist `ActionOutcome`, update Prescription status.
- **Acceptance:**
  - Prescription → accept → next session shows `in_progress`
  - Next session meets target → `completed` + outcome recorded
  - Next session misses target → stays `in_progress` until `valid_until` or window exhausted

### BE-022 🔴 `DriverProgressSnapshot` scorer
- **Month/week:** M2/W7
- **Deps:** BE-015
- **Parallel with:** BE-021
- **AI:** claude-opus
- **Hours:** 12-14
- **Context:** Per session + rolling 30-day snapshot. Score each of the 10 dimensions using weighted session metrics. Confidence based on sample count + recency. Trend over 14 days.
- **Acceptance:**
  - After N sessions, `GET /api/v1/driver/progress` returns current snapshot
  - Confidence is 0 after 30 days without evidence
  - Trend tags sensibly (up/flat/down/volatile)

### BE-023 🔴 `GET /api/v1/sessions/:id/next_actions` endpoint (frontend migration target)
- **Month/week:** M2/W8
- **Deps:** BE-019, BE-020
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Per Q82. Returns: `{ weakness_episodes_new, weakness_episodes_escalated, prescriptions_new, prescriptions_progressing }` for a session. Replaces the frontend SessionDebrief heuristic block.
- **Acceptance:**
  - Webapp SessionDebrief fetches this instead of generating text locally
  - Payload is stable (schema in `lap-schemas`)

### BE-024 🟡 Public API for Driver Timeline
- **Month/week:** M2/W8
- **Deps:** BE-015, BE-019
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** `GET /api/v1/driver/timeline?cursor=...&limit=20` returns paginated feed of sessions with their WeaknessEpisode/Prescription badges.

### BE-025 🔴 Audit P0 cleanup: duplicate routes + `/api/v1` double-prefix
- **Month/week:** M1/W1 (sooner the better)
- **Deps:** none
- **AI:** codex
- **Hours:** 2-4
- **Context:** Resolve `/sessions/:id/channels` duplicate route in old Flask codebase. Fix `/api/v1` double-prefix in bundle hooks. These land before BE-001 if possible so the old API doesn't rot during migration.

---

## Month 3 — Public Beta Backend Support

### BE-026 🔴 `GET /api/v1/driver/profile` aggregate endpoint
- **Month/week:** M3/W9
- **Deps:** BE-022
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Returns current DriverProgressSnapshot + top 5 open WeaknessEpisodes + open Prescriptions + Readiness summary. One round-trip for Driver Profile page.

### BE-027 🔴 Durable Compare API
- **Month/week:** M3/W10
- **Deps:** BE-015
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Per Q85. `POST /api/v1/compare_cases` creates a saved compare case (session IDs + rationale). `GET /api/v1/compare_cases/:id` returns the case + auto-updating outcome block that re-evaluates if referenced sessions change (reprocessed, for instance).

### BE-028 🔴 Session detail endpoint + full telemetry download
- **Month/week:** M3/W9
- **Deps:** BE-015
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Replace the old Flask `GET /sessions/:id` with a clean endpoint returning the canonical `SessionRecord`. Separate endpoint for raw telemetry download (signed URL to object storage).

### BE-029 🟡 Weekly readiness state job
- **Month/week:** M3/W10
- **Deps:** BE-022
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** `DriverReadinessState` computed once a week + on target-event changes. Inputs: volume, quality, recency, consistency, unresolved weakness count, familiarity, event pressure, recovery.

### BE-030 🔴 Stripe production cutover
- **Month/week:** M3/W11
- **Deps:** BE-010
- **AI:** claude-opus (checklist) + codex
- **Hours:** 6-8
- **Context:** Switch from test keys to live. Verify webhook signature validation. Grandfather coupon live. Trial → paid flow verified end-to-end.
- **Acceptance:**
  - Real €15 charge processed in test run (refunded)
  - Webhook events in production logs

### BE-031 🔴 Load testing + rate limiting
- **Month/week:** M3/W12
- **Deps:** BE-007, BE-015
- **AI:** codex
- **Hours:** 4-6
- **Context:** k6 or Locust script: 100 concurrent sessions uploading, 1000 concurrent API requests. Add rate limits: 100 req/min/user on read, 10 ingestions/hr/user.

### BE-032 🟡 E2E smoke test for critical path
- **Month/week:** M3/W12
- **Deps:** BE-031
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Automated test: sim session → upload → insights generated → appears in user timeline. Runs in CI nightly against staging.

---

## Month 4 — Sim↔Real Bridge

### BE-033 🔴 `TransferLink` entity + CRUD API
- **Month/week:** M4/W13
- **Deps:** BE-005, BE-015
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Per ADR-005 §5.5. Endpoints: `POST /api/v1/bridge/links`, `GET /api/v1/bridge/links/:id`, `GET /api/v1/driver/:id/bridge/links`.

### BE-034 🔴 Shape + intensity match algorithms
- **Month/week:** M4/W13
- **Deps:** BE-033
- **AI:** claude-opus (algorithm design, cite sources)
- **Hours:** 16-20
- **Context:** For two sessions, for each channel of interest (brake, throttle, steering): compute shape-match score via normalized cross-correlation (or DTW) on lap-aligned segments. Intensity match via ratios of peak/integral values. Identify divergence points per corner.
- **Acceptance:**
  - On identical sim sessions: shape=1.0, intensity=1.0
  - On sim vs real same track: shape >0.6, intensity may diverge
  - Divergence points flag corners where the driver behaves differently

### BE-035 🔴 Auto-suggest linked sessions
- **Month/week:** M4/W14
- **Deps:** BE-033
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** `GET /api/v1/bridge/suggest_links?session_id=X` returns candidate pairs: sessions from the same `master_track_id` + comparable car class, within 60 days, different `source` (sim/real).

### BE-036 🔴 Transfer diagnostics report generator
- **Month/week:** M4/W14
- **Deps:** BE-034
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Combines shape + intensity + divergence points into a structured `TransferReport` that the webapp renders. Generates a `CoachingInsight` capturing the transfer-relevant takeaways.

### BE-037 🟡 Cohort opt-in + benchmark skeleton
- **Month/week:** M4/W15-16
- **Deps:** BE-022
- **AI:** claude-opus
- **Hours:** 10-14
- **Context:** Per ADR-008. User setting `cohort_opt_in`. Nightly job: if ≥20 opt-in drivers per `{track, car_class}` → compute percentiles, populate `DriverBenchmarkProfile`. Until 20 drivers, leaves profile null and UI shows "Cohort unlocks at 20 drivers."

### BE-038 🟡 Coaching library expansion (target: 60-80 rules)
- **Month/week:** M4 entire
- **Deps:** BE-017
- **AI:** claude-opus (authoring, 15-20 rules/week)
- **Hours:** 20-30
- **Context:** Add racecraft, tire management, minimum speed, throttle pickup, consistency categories.

### BE-039 🟡 Endurance event tagging
- **Month/week:** M4/W16
- **Deps:** BE-015
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Session manifest gains `endurance_event_id`. Sessions grouped under endurance event aggregate laps by stint. No UX change yet — just data model.

### BE-040 🟡 iRacing calendar fetcher
- **Month/week:** M4/W16
- **Deps:** BE-005
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Weekly cron pulls iRacing schedule (public JSON). Stores as `TargetEvent` rows users can pin.

---

## Month 5 — V1 Release Backend Support

### BE-041 🔴 Strategy plan vs actual serialization into Bundle v2
- **Month/week:** M5/W17
- **Deps:** BE-015
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** Per Q102. Bundle v2 extends to include a `strategy_section`: pre-race plan, actual pit events, execution delta. Post-race analysis compares plan vs actual.

### BE-042 🔴 Endurance long-run consistency scoring
- **Month/week:** M5/W18-19
- **Deps:** BE-022, BE-039
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** New scoring path for endurance sessions: emphasizes long-run pace decay, stint-over-stint consistency, tire preservation.

### BE-043 🔴 Target-event-aware plan generation
- **Month/week:** M5/W19
- **Deps:** BE-020, BE-040
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** If user has pinned a `TargetEvent`, `ActionPrescription` generation weights toward prescriptions whose `expected_context` matches the target event's track/car. Rank most-impactful for that event first.

### BE-044 🟡 Coaching library to 100+ rules
- **Month/week:** M5 entire
- **Deps:** BE-017
- **AI:** claude-opus (authoring)
- **Hours:** 25-35

---

## Month 6 — Scale

### BE-045 🟡 Cohort benchmarks live
- **Month/week:** M6/W21
- **Deps:** BE-037
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Flip the feature flag after validating ≥20 opt-in users per top tracks. Monitor for data leakage (no driver can query another's).

### BE-046 🟡 B2B multi-seat billing scaffold
- **Month/week:** M6/W22-23
- **Deps:** BE-010
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Open if there's real B2B inbound. Adds `Organization`, multi-user seats, admin-invitable. Minimal UX — most of this stays dormant until first real B2B customer closes.

### BE-047 🟡 Coaching library to 150 rules
- **Month/week:** M6 entire
- **Hours:** 20-30

### BE-048 🟡 API v2 versioning prep
- **Month/week:** M6/W24
- **Deps:** BE-007
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Framework for `/api/v2/` alongside v1. Used for any breaking changes post-M6.

---

## Summary

| Month | Backend hours (rough) | Key deliverable |
|---|---|---|
| M1 | 90-110 | FastAPI + schemas + ingestion live |
| M2 | 130-160 | 3 core intelligence objects + rules engine + 25+ rules |
| M3 | 45-55 | Beta APIs + Stripe prod + load tests |
| M4 | 80-100 | Bridge end-to-end + cohort prep + 60+ rules |
| M5 | 60-80 | Endurance + events + 100+ rules |
| M6 | 50-70 | Cohort live + B2B scaffold + 150 rules |
| **Total** | **~500 hours** | |

At 30h/week backend allocation = ~17 weeks of backend. Realistic for solo+AI with the other repos split across.
