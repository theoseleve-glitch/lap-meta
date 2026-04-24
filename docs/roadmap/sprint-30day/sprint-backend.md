# LAP Backend — 30-Day Sprint Queue

**Repo:** `lap-backend` (new per ADR-002).
**Stack:** Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 + Alembic, Celery, Postgres 16, Redis.
**Loop interval:** 1 hour. Each task is scoped to exactly 1 hour of AI-assisted work.
**Total:** 240 tasks (8/day × 30 days worth of focused execution).

## Rules for /loop

1. Read this file. Find the next unchecked `[ ]` task in order.
2. If the task has `Dep:` and that dep is unchecked, skip to the next independent task.
3. Complete the task fully: code + tests + commit. Do NOT start what you can't finish in ~1 hour.
4. Mark `[x]` with the git SHA appended like ` — sha: abc1234`.
5. If blocked, change `[ ]` to `[BLOCKED]` and append a one-line reason.
6. Commit format: `sprint(backend): T### <short>`. No `--no-verify`.
7. Push only if CI green. Reference ADRs in `docs/roadmap/02-ARCHITECTURE-DECISIONS.md`.

---

## Block A — Project scaffold (T001–T020)

- [x] T001 [opus] Scaffold `lap-backend/` with `pyproject.toml` (uv), Python 3.12, MIT license ⇒ `uv sync` succeeds — sha: 4969e7c
- [x] T002 [sonnet] Add `.gitignore`, `.python-version`, `README.md` stub, `docs/` folder ⇒ repo clean — sha: 1069ac3
- [x] T003 [sonnet] Configure ruff (rules: E,F,I,N,UP,B,C4,SIM,RET,ARG,PTH) in `pyproject.toml` ⇒ `ruff check .` green — sha: 15c52ff
- [x] T004 [sonnet] Configure mypy strict mode for `app/` and `domain/` ⇒ `mypy` green on empty dirs — sha: 2bbca58
- [x] T005 [codex] GitHub Actions: `.github/workflows/ci.yml` runs ruff+mypy+pytest on push ⇒ workflow valid — sha: 05776ea
- [x] T006 [codex] Pre-commit: `.pre-commit-config.yaml` with ruff, mypy, trailing-whitespace ⇒ `pre-commit run --all-files` green — sha: 0360564
- [x] T007 [opus] Create `app/main.py` with FastAPI() + `/healthz` + `/readyz` endpoints ⇒ uvicorn starts, curl returns 200 — sha: 3f3d471
- [x] T008 [sonnet] Setup `structlog` for JSON logging, wire into FastAPI middleware ⇒ request logs are JSON — sha: 602d05b
- [x] T009 [sonnet] Add pytest + pytest-asyncio + httpx in dev deps, `tests/` dir with conftest.py ⇒ `pytest` finds 0 tests green — sha: 20484aa
- [x] T010 [codex] First test: `test_healthz_returns_200` in `tests/test_health.py` ⇒ test green — sha: 699bc51
- [x] T011 [sonnet] Domain layout: create `app/`, `domain/`, `infra/`, `coaching/` top-level packages with `__init__.py` ⇒ importable — sha: fbef621
- [x] T012 [sonnet] Config via `pydantic-settings`: `Config` class in `app/config.py` reading env vars ⇒ unit-tested — sha: 14180aa
- [NEEDS_REWORK] T013 [sonnet] Env schema: `.env.example` with DATABASE_URL, REDIS_URL, CLERK_SECRET, STRIPE_SECRET ⇒ committed — sha: 3ada05d — failed review cycle 11: `ruff check .` exit 1 with 2 errors in tests/test_env_example.py (E501 line 5 89>88 chars on REQUIRED_KEYS frozenset; SIM300 line 23 yoda condition on `REQUIRED_KEYS <= _keys_in_env_example()`), reverted in 3312b5e. Re-do: line-wrap + rewrite as `_keys_in_env_example() >= REQUIRED_KEYS`.
- [x] T014 [sonnet] Dependency injection: `app/deps.py` with `get_config`, `get_db`, `get_current_user` stubs ⇒ imports work — sha: 6018966
- [x] T015 [sonnet] Add CORS middleware configured for `app.lap-coach.racing` origins only ⇒ preflight test green — sha: edeb53d
- [x] T016 [sonnet] Add request-id middleware, propagate to logs + response header ⇒ header present in tests — sha: 5d31465
- [x] T017 [sonnet] Add rate-limit middleware skeleton (SlowAPI or custom) — no enforcement yet ⇒ decorator works — sha: ef85842
- [BLOCKED] T018 [codex] Dockerfile for backend (multi-stage, python:3.12-slim base) ⇒ `docker build` succeeds — BLOCKED: docker not installed in Windows sandbox; acceptance requires local docker runtime to verify build succeeds
- [BLOCKED] T019 [codex] docker-compose.yml with postgres+redis+backend services for local dev ⇒ `docker compose up` works — BLOCKED: docker compose not available in Windows sandbox; same root cause as T018
- [x] T020 [sonnet] Makefile targets: `make dev`, `make test`, `make lint`, `make migrate` ⇒ all run — sha: 7b64848

## Block B — `lap-schemas` foundation (T021–T045)

- [ ] T021 [opus] Create `lap-schemas/` package with `python/src/lap_schemas/v1/__init__.py` ⇒ importable
- [ ] T022 [opus] Define `UUID7` type alias + validator using `uuid6` library ⇒ unit test generates valid v7
- [ ] T023 [opus] Define `EnvironmentTag` enum (sim_practice, sim_race, real_track_day, real_race, real_karting, drill, test) ⇒ enum values frozen
- [ ] T024 [opus] Define `SourceTag` literal (iracing, acc, ac, ams2, rf2, lmu, rennsport, f1_game, real) ⇒ typed
- [ ] T025 [opus] Pydantic model `SensorConfigSnapshot` per ADR-006 ⇒ validates, 3 unit tests
- [ ] T026 [opus] Pydantic model `DataQuality` per ADR-006 ⇒ validates, 3 unit tests
- [ ] T027 [opus] Pydantic model `SessionManifest` per ADR-006 ⇒ validates, round-trip JSON test
- [ ] T028 [opus] Pydantic model `TelemetrySample` per ADR-007 (dual timestamps) ⇒ validates
- [ ] T029 [opus] Pydantic model `SessionRecord` (canonical post-ingestion shape) ⇒ validates
- [ ] T030 [opus] Pydantic model `LapRecord` (lap splits, sector times, flags) ⇒ validates
- [ ] T031 [opus] Pydantic model `SkillDimension` per ADR-005 §5.1 ⇒ validates
- [ ] T032 [opus] Pydantic model `DriverProgressSnapshot` per ADR-005 §5.1 ⇒ validates, example fixture
- [ ] T033 [opus] Pydantic enum `WeaknessCategory` per ADR-005 §5.2 ⇒ frozen
- [ ] T034 [opus] Pydantic model `WeaknessEpisode` per ADR-005 §5.2 ⇒ validates
- [ ] T035 [opus] Pydantic model `SuccessCondition` per ADR-005 §5.3 ⇒ validates
- [ ] T036 [opus] Pydantic model `ActionPrescription` per ADR-005 §5.3 ⇒ validates
- [ ] T037 [opus] Pydantic model `ActionOutcome` per ADR-005 §5.4 ⇒ validates
- [ ] T038 [opus] Pydantic model `DivergencePoint` per ADR-005 §5.5 ⇒ validates
- [ ] T039 [opus] Pydantic model `TransferLink` per ADR-005 §5.5 ⇒ validates
- [ ] T040 [opus] Pydantic model `CohortDef` + `DriverBenchmarkProfile` per ADR-005 §5.6 ⇒ validates
- [ ] T041 [opus] Pydantic model `TargetEvent` + `DriverReadinessState` per ADR-005 §5.7 ⇒ validates
- [ ] T042 [opus] Pydantic model `CoachingInsight` (session-level, pre-episode aggregation) ⇒ validates
- [ ] T043 [sonnet] OpenAPI generator script: `python -m lap_schemas.generate_openapi` outputs `openapi.json` ⇒ valid OpenAPI 3.1
- [ ] T044 [sonnet] Package `lap-schemas` publishable locally: `pip install -e lap-schemas/python` ⇒ imports work
- [ ] T045 [codex] Add `lap-backend` dependency on `lap-schemas` in pyproject.toml ⇒ import works in backend

## Block C — TS & Swift codegen (T046–T055)

- [ ] T046 [sonnet] TS codegen: `lap-schemas/typescript/` with `openapi-typescript@7` setup ⇒ runs
- [ ] T047 [sonnet] TS codegen script: `pnpm generate:ts` produces `generated/schema.d.ts` ⇒ file exists
- [ ] T048 [sonnet] TS codegen: wrap into `@lap/schemas` npm package (private workspace) ⇒ importable
- [ ] T049 [sonnet] Swift codegen: `openapi-generator-cli` config for Swift5 ⇒ produces `.swift` files
- [ ] T050 [sonnet] Swift codegen script: `make swift-codegen` ⇒ output in `lap-mobile/Generated/`
- [ ] T051 [sonnet] Kotlin codegen (for Android later): `openapi-generator-cli` config for kotlin ⇒ produces `.kt`
- [ ] T052 [codex] CI rule: job `schema-sync-check` fails if `.d.ts` or `.swift` files are stale vs openapi.json ⇒ green when synced
- [ ] T053 [codex] Git hook: post-commit warns if Pydantic model changed without regen ⇒ warns correctly
- [ ] T054 [sonnet] Docs: `lap-schemas/README.md` explaining regen workflow ⇒ written
- [ ] T055 [sonnet] Version strategy: `lap-schemas` follows calver `YYYY.MM.N`, bump on breaking change ⇒ documented

## Block D — Database + SQLAlchemy (T056–T080)

- [ ] T056 [opus] SQLAlchemy 2.0 setup: `infra/db.py` with async engine + session factory ⇒ connection works
- [ ] T057 [sonnet] Alembic init: `alembic.ini` + `alembic/env.py` configured for async ⇒ `alembic upgrade head` works on empty DB
- [ ] T058 [opus] ORM model `User` (id UUIDv7, clerk_user_id, email, created_at, subscription_status, is_admin) ⇒ migration applied
- [ ] T059 [opus] ORM model `DriverProfile` (id, user_id, display_name, skill_level, cohort_opt_in) ⇒ migration applied
- [ ] T060 [opus] ORM model `Session` (id, driver_id, manifest jsonb, created_at, status) ⇒ migration applied
- [ ] T061 [opus] ORM model `SessionRecord` (id, session_id, processed payload jsonb) ⇒ migration applied
- [ ] T062 [opus] ORM model `TelemetryArtifact` (id, session_id, s3_key, sha256, size_bytes) ⇒ migration applied
- [ ] T063 [opus] ORM model `Lap` (id, session_id, lap_number, time_ms, sector_times, valid) ⇒ migration applied
- [ ] T064 [opus] ORM model `WeaknessEpisode` matching Pydantic shape ⇒ migration applied
- [ ] T065 [opus] ORM model `ActionPrescription` matching Pydantic shape ⇒ migration applied
- [ ] T066 [opus] ORM model `ActionOutcome` matching Pydantic shape ⇒ migration applied
- [ ] T067 [opus] ORM model `DriverProgressSnapshot` ⇒ migration applied
- [ ] T068 [opus] ORM model `TransferLink` ⇒ migration applied
- [ ] T069 [opus] ORM model `DriverBenchmarkProfile` ⇒ migration applied
- [ ] T070 [opus] ORM model `DriverReadinessState` ⇒ migration applied
- [ ] T071 [opus] ORM model `TrackLayout`, `CarModel`, `TrackEquivalence`, `CarEquivalence` ⇒ migrations applied
- [ ] T072 [opus] ORM model `CoachingInsight` (per-session outputs) ⇒ migration applied
- [ ] T073 [opus] ORM model `UploadQueueItem` (mirrors mobile's SQLite schema, for audit trail) ⇒ migration applied
- [ ] T074 [opus] RLS policy: users can only SELECT their own sessions ⇒ integration test proves isolation
- [ ] T075 [opus] RLS policy: same for weakness_episodes, prescriptions, outcomes, snapshots, transfer_links ⇒ tests
- [ ] T076 [sonnet] Repo layer: `SessionRepo` with `get`, `list_by_driver`, `create`, `update_status` ⇒ unit-tested
- [ ] T077 [sonnet] Repo layer: `DriverRepo` with `get`, `create`, `update_settings` ⇒ unit-tested
- [ ] T078 [sonnet] Repo layer: `WeaknessRepo` with `open`, `update_confidence`, `resolve` ⇒ unit-tested
- [ ] T079 [sonnet] Repo layer: `PrescriptionRepo` + `OutcomeRepo` ⇒ unit-tested
- [ ] T080 [sonnet] DB session dependency: `get_db()` yields async session ⇒ FastAPI routes can use Depends(get_db)

## Block E — Auth (Clerk) (T081–T095)

- [ ] T081 [opus] Clerk integration: `infra/clerk.py` with JWKS fetch + cache ⇒ JWKS loads
- [ ] T082 [sonnet] Auth middleware: validate JWT from `Authorization: Bearer <>` header ⇒ 401 on invalid
- [ ] T083 [sonnet] Dependency `get_current_user` → returns User row, auto-provision on first call ⇒ tested
- [ ] T084 [sonnet] Endpoint `GET /api/v1/me` returning current user ⇒ 200 with payload
- [ ] T085 [sonnet] Endpoint `PATCH /api/v1/me` for profile updates ⇒ updates DB
- [ ] T086 [sonnet] Clerk webhook receiver: `POST /api/v1/auth/webhooks` handling user.created, user.deleted ⇒ syncs DB
- [ ] T087 [sonnet] Clerk webhook: validate Svix signature ⇒ rejects tampered
- [ ] T088 [sonnet] Admin guard: `require_admin` dependency checks `is_admin=true` ⇒ 403 for non-admin
- [ ] T089 [sonnet] Magic QR pairing endpoint: `POST /api/v1/auth/pairing/create` returns short-lived token ⇒ token in response
- [ ] T090 [sonnet] Magic QR redeem: `POST /api/v1/auth/pairing/redeem` exchanges token for refresh ⇒ refresh in response
- [ ] T091 [sonnet] Pairing token TTL: 5 minutes, single-use, stored in Redis ⇒ integration test
- [ ] T092 [sonnet] Device session table + endpoint `GET /api/v1/auth/devices` lists paired devices ⇒ 200
- [ ] T093 [sonnet] Device revoke: `DELETE /api/v1/auth/devices/:id` revokes ⇒ future requests 401
- [ ] T094 [sonnet] Rate-limit auth endpoints (10 req/min/IP) ⇒ 429 after threshold
- [ ] T095 [sonnet] Integration test: full happy path signup→me→pair→upload with auth ⇒ green

## Block F — Ingestion pipeline (T096–T125)

- [ ] T096 [opus] Ingestion endpoint: `POST /api/v1/sessions/ingest` accepts multipart ⇒ smoke test green
- [ ] T097 [opus] Parse `manifest` form field as `SessionManifest`, 422 on invalid ⇒ tested
- [ ] T098 [opus] Validate idempotency-key header present, 400 if missing ⇒ tested
- [ ] T099 [opus] Idempotency cache: Redis-backed, 24h TTL, returns prior response on key hit ⇒ tested
- [ ] T100 [opus] Stream chunks to object storage (local fs first, R2/S3 later) ⇒ file persists
- [ ] T101 [opus] Compute sha256 per chunk during streaming ⇒ matches manifest
- [ ] T102 [opus] Create `Session` row with `status=uploaded` + `TelemetryArtifact` rows ⇒ DB rows present
- [ ] T103 [opus] Dispatch Celery task `process_session_ingest(session_id)` ⇒ task queued
- [ ] T104 [opus] Return 202 with `{session_id, ingest_job_id, status_stream_url}` ⇒ response shape matches
- [ ] T105 [sonnet] Cloudflare R2 client integration: `infra/storage.py` with put/get/sign-url ⇒ integration test
- [ ] T106 [sonnet] Swap local fs → R2 in ingestion endpoint ⇒ works with R2 creds
- [ ] T107 [sonnet] Celery worker setup: `celery -A app.infra.celery worker -l info` ⇒ starts clean
- [ ] T108 [sonnet] Celery Redis broker + result backend wired ⇒ task completes visible
- [ ] T109 [sonnet] Celery `process_session_ingest` skeleton: read manifest, mark `processing`, log ⇒ status updates
- [ ] T110 [sonnet] Celery task retry policy: exponential backoff, max 3 attempts ⇒ tested with failing task
- [ ] T111 [sonnet] Celery failure handler: on final failure, mark session `failed` with reason ⇒ visible in UI
- [ ] T112 [opus] SSE endpoint `GET /api/v1/jobs/:id/events` ⇒ stream stays alive
- [ ] T113 [sonnet] SSE events: queued, processing, stage:<N>, completed, failed ⇒ events received in order
- [ ] T114 [sonnet] SSE Last-Event-ID reconnection support ⇒ resumes from cursor
- [ ] T115 [opus] Bundle parser: unpack the Bundle v2 format into normalized sample stream ⇒ tested with fixture
- [ ] T116 [opus] Checksum validator: verify each chunk's sha256 matches manifest ⇒ tested
- [ ] T117 [opus] Lap detection: given samples + `TrackLayout`, emit `Lap` rows ⇒ matches archived session laps
- [ ] T118 [opus] Sector splits: compute sector times from track layout checkpoints ⇒ validated against known sessions
- [ ] T119 [opus] Session metric extraction: best lap, avg lap, consistency, peak speed ⇒ persisted
- [ ] T120 [opus] DataQuality scorer: compute from sample completeness, gaps, rate stability ⇒ score 0-100
- [ ] T121 [opus] Canonical timestamp alignment per ADR-007 ⇒ dual timestamps present on every sample
- [ ] T122 [sonnet] Persist `SessionRecord` after processing ⇒ row present
- [ ] T123 [sonnet] Update `Session.status=ready` when done ⇒ visible via GET /sessions/:id
- [ ] T124 [sonnet] Processing pipeline integration test with archived Sebring session ⇒ end-to-end green
- [ ] T125 [sonnet] Processing pipeline integration test with archived RaceBox session ⇒ end-to-end green

## Block G — Track + car catalog (T126–T145)

- [ ] T126 [opus] Track catalog seed: `coaching/catalog/tracks/sebring.yaml` with checkpoints ⇒ parses
- [ ] T127 [opus] Same for Silverstone ⇒ parses
- [ ] T128 [opus] Same for Nürburgring VLN (Gesamtstrecke) ⇒ parses
- [ ] T129 [opus] Same for Red Bull Ring ⇒ parses
- [ ] T130 [opus] Same for Laguna Seca ⇒ parses
- [ ] T131 [opus] Same for Lime Rock Park ⇒ parses
- [ ] T132 [opus] Same for Ledenon ⇒ parses
- [ ] T133 [opus] Same for Charlotte Motor Speedway ⇒ parses
- [ ] T134 [opus] Same for Spa-Francorchamps ⇒ parses
- [ ] T135 [opus] Same for Monza ⇒ parses
- [ ] T136 [sonnet] Track catalog loader: read YAMLs at startup into memory ⇒ accessible via `get_track_catalog()`
- [ ] T137 [opus] Sim↔real track equivalence table seeded (10 pairs) ⇒ lookup works
- [ ] T138 [opus] Car catalog seed: `coaching/catalog/cars/*.yaml` with 15 common GT3s + karting classes ⇒ parses
- [ ] T139 [opus] Car equivalence table (sim-to-real car class mapping) ⇒ lookup works
- [ ] T140 [sonnet] Endpoint `GET /api/v1/catalog/tracks` paginated list ⇒ returns 10+ tracks
- [ ] T141 [sonnet] Endpoint `GET /api/v1/catalog/tracks/:id` detail ⇒ returns checkpoints
- [ ] T142 [sonnet] Endpoint `GET /api/v1/catalog/cars` list ⇒ returns cars
- [ ] T143 [sonnet] Endpoint `GET /api/v1/catalog/cars/:id` detail ⇒ returns car specs
- [ ] T144 [sonnet] Unit tests: track catalog load, lookup by sim/track name ⇒ green
- [ ] T145 [sonnet] Unit tests: sim↔real equivalence returns correct master_id ⇒ green

## Block H — Stripe integration (T146–T165)

- [ ] T146 [sonnet] Stripe SDK setup, test keys in env ⇒ `stripe.api_key` loads
- [ ] T147 [sonnet] Create products in Stripe dashboard: LAP Monthly (€15), LAP Yearly (€150), Waitlist Founder (€12) ⇒ IDs in config
- [ ] T148 [sonnet] Endpoint `POST /api/v1/billing/checkout` creates Checkout session → returns URL ⇒ test mode works
- [ ] T149 [sonnet] Checkout session metadata includes `user_id`, trial=14 days ⇒ inspected on Stripe side
- [ ] T150 [sonnet] Success URL + cancel URL configured ⇒ redirects work
- [ ] T151 [sonnet] Endpoint `POST /api/v1/billing/webhooks` validates Stripe signature ⇒ test with Stripe CLI green
- [ ] T152 [sonnet] Webhook handler: `customer.subscription.created` → sets user.subscription_status=trialing ⇒ DB updated
- [ ] T153 [sonnet] Webhook handler: `customer.subscription.updated` → sync status ⇒ reflects in DB
- [ ] T154 [sonnet] Webhook handler: `customer.subscription.deleted` → status=canceled ⇒ access gated
- [ ] T155 [sonnet] Webhook handler: `invoice.payment_failed` → status=past_due ⇒ notification queued
- [ ] T156 [sonnet] Webhook handler: `invoice.payment_succeeded` → status=active ⇒ DB updated
- [ ] T157 [sonnet] Endpoint `GET /api/v1/billing/portal` returns Stripe Billing Portal URL ⇒ redirects work
- [ ] T158 [sonnet] Waitlist founder coupon: `WAITLIST_FOUNDER` → 20% off 12 months ⇒ created in Stripe
- [ ] T159 [sonnet] Apply coupon via checkout metadata when user is on waitlist ⇒ discount shows on Stripe
- [ ] T160 [sonnet] Daily reconciliation job: compare Stripe subs to DB, log drift ⇒ runs clean
- [ ] T161 [sonnet] Admin endpoint: `POST /api/v1/admin/billing/sync/:user_id` force-syncs from Stripe ⇒ works
- [ ] T162 [sonnet] Subscription gate dependency `require_active_subscription` ⇒ 402 for inactive
- [ ] T163 [sonnet] Grace period logic: trial expired → 48h soft block with banner, then hard block ⇒ tested
- [ ] T164 [sonnet] Refund endpoint stub (admin only): `POST /api/v1/admin/billing/refund` ⇒ works in test mode
- [ ] T165 [sonnet] Integration test: checkout → webhook → user.status → gated endpoint ⇒ end-to-end green

## Block I — Observability (T166–T180)

- [ ] T166 [sonnet] Sentry SDK: init in `app/main.py`, DSN from env ⇒ 500 error captured
- [ ] T167 [sonnet] Sentry: sample traces at 10% ⇒ verified in Sentry dashboard
- [ ] T168 [sonnet] Sentry: release tagging from `pyproject.toml` version ⇒ tagged correctly
- [ ] T169 [sonnet] PostHog Python SDK: init in config ⇒ ready
- [ ] T170 [sonnet] PostHog: emit `session_ingested` event ⇒ visible in PostHog
- [ ] T171 [sonnet] PostHog: emit `prescription_created` event ⇒ visible
- [ ] T172 [sonnet] PostHog: emit `prescription_accepted` event ⇒ visible
- [ ] T173 [sonnet] PostHog: emit `weakness_resolved` event ⇒ visible
- [ ] T174 [sonnet] PostHog: user.identify on first-login ⇒ users show up
- [ ] T175 [sonnet] Prometheus metrics endpoint `/metrics` ⇒ Prometheus can scrape
- [ ] T176 [sonnet] Custom metrics: sessions_ingested_total, ingest_duration_seconds histogram ⇒ metrics present
- [ ] T177 [sonnet] Custom metrics: prescriptions_created_total, weakness_episodes_open_total gauge ⇒ present
- [ ] T178 [sonnet] Admin KPI endpoint `GET /api/v1/admin/kpis` returns current WPD, activation, upload success ⇒ 200
- [ ] T179 [sonnet] Cron job: Slack weekly KPI report Monday 09:00 UTC ⇒ posts to channel
- [ ] T180 [sonnet] Cron job: daily session-loss audit — any session in `recording` >24h → alert ⇒ alert on fixture

## Block J — Coaching rules engine (T181–T210)

- [ ] T181 [opus] Rules engine: YAML schema design (JSON Schema for rule file) ⇒ documented in ADR-013
- [ ] T182 [opus] Rules loader: read `coaching/library/rules/**/*.yaml` at startup ⇒ catches malformed rules at load
- [ ] T183 [opus] Rules compiler: convert YAML condition strings to callable predicates ⇒ unit-tested
- [ ] T184 [opus] Feature namespace: enumerate available session features (apex_speed, brake_peak, etc.) ⇒ documented
- [ ] T185 [opus] Rules runner: given a processed session, evaluate all rules, emit `CoachingInsight[]` ⇒ works on fixture
- [ ] T186 [opus] Rule versioning: rules have `id + version`, insights reference the version ⇒ tracked
- [ ] T187 [opus] Rule confidence gating: only fire at full strength after N corroborating sessions ⇒ tested
- [ ] T188 [opus] Rule `br.late_braking.apex_speed_loss` authored with 3 explanation variants ⇒ YAML parses, unit test green
- [ ] T189 [opus] Rule `br.early_braking.entry_speed_loss` authored ⇒ YAML parses, test green
- [ ] T190 [opus] Rule `br.abrupt_release.load_transfer_mismatch` authored ⇒ test green
- [ ] T191 [opus] Rule `br.inconsistent_pressure.sector_variance` authored ⇒ test green
- [ ] T192 [opus] Rule `br.lockup.pattern_detection` authored ⇒ test green
- [ ] T193 [opus] Rule `br.cold_brakes.first_lap_deficit` authored ⇒ test green
- [ ] T194 [opus] Rule `br.over_braking.mid_corner` authored ⇒ test green
- [ ] T195 [opus] Rule `br.balance_shift.rear_locking_entry` authored ⇒ test green
- [ ] T196 [opus] Rule `br.trail_brake.release_too_early` authored ⇒ test green
- [ ] T197 [opus] Rule `br.threshold_braking.not_reached` authored ⇒ test green
- [ ] T198 [sonnet] Tests: all 10 braking rules against archived Sebring session ⇒ at least 3 fire correctly
- [ ] T199 [sonnet] Tests: all 10 against Silverstone ⇒ meaningful insights
- [ ] T200 [sonnet] Tests: all 10 against Red Bull Ring ⇒ meaningful insights
- [ ] T201 [sonnet] Rules engine API: `POST /api/v1/admin/coaching/rules/simulate` ⇒ admin can test-run
- [ ] T202 [sonnet] Rules engine API: `GET /api/v1/coaching/rules` lists active rules ⇒ public read-only
- [ ] T203 [opus] Rules compilation: compile YAML to portable JSON for client engines ⇒ output spec'd
- [ ] T204 [opus] Rules bundle endpoint: `GET /api/v1/coaching/rules/bundle?version=latest` → signed JSON ⇒ desktop/mobile can fetch
- [ ] T205 [opus] False-positive flagging: `POST /api/v1/coaching/insights/:id/flag` for user feedback ⇒ persists
- [ ] T206 [sonnet] Flag aggregation job: tag rules with >10% false-positive rate ⇒ surfaced in admin
- [ ] T207 [opus] CoachingInsight persistence after rule runs ⇒ linked to session + rule version
- [ ] T208 [opus] WeaknessEpisode opener: on CoachingInsights, match to existing or open new ⇒ deduplicates correctly
- [ ] T209 [opus] WeaknessEpisode confidence decay job (nightly) ⇒ decays correctly
- [ ] T210 [opus] WeaknessEpisode recurrence counter ⇒ increments on re-observation

## Block K — Prescription + Outcome lifecycle (T211–T225)

- [ ] T211 [opus] Prescription generator: when episode opens/escalates, create Prescription ⇒ tested
- [ ] T212 [opus] Prescription draws drill template from library rule ⇒ linked correctly
- [ ] T213 [opus] Prescription `success_condition` populated from rule template ⇒ machine-checkable
- [ ] T214 [opus] Prescription dedup: same weakness open → no duplicate prescription ⇒ tested
- [ ] T215 [sonnet] Endpoint `POST /api/v1/prescriptions/:id/accept` ⇒ status=accepted
- [ ] T216 [sonnet] Endpoint `POST /api/v1/prescriptions/:id/skip` ⇒ status=skipped
- [ ] T217 [sonnet] Endpoint `GET /api/v1/driver/:id/prescriptions?status=open` ⇒ returns
- [ ] T218 [opus] Outcome checker: after each session, evaluate open prescriptions' success_conditions ⇒ tested
- [ ] T219 [opus] Outcome persistence: create ActionOutcome row + update prescription status ⇒ tested
- [ ] T220 [opus] Confidence change propagation: outcome updates episode confidence ⇒ tested
- [ ] T221 [opus] Efficacy score computation: per-user, per-prescription, per-rule ⇒ populated
- [ ] T222 [sonnet] Endpoint `GET /api/v1/driver/:id/outcomes?window=30d` ⇒ returns
- [ ] T223 [sonnet] Prescription expiry cron: `valid_until` expired → status=expired ⇒ runs nightly
- [ ] T224 [sonnet] Endpoint `GET /api/v1/sessions/:id/next_actions` (per WA-009) ⇒ returns array
- [ ] T225 [sonnet] Integration test: full loop session→insight→episode→prescription→next session→outcome ⇒ green

## Block L — Polish + tests (T226–T240)

- [ ] T226 [sonnet] Openapi.json exposed at `/api/v1/openapi.json` ⇒ valid
- [ ] T227 [sonnet] Swagger UI exposed at `/api/v1/docs` ⇒ renders
- [ ] T228 [sonnet] ReDoc exposed at `/api/v1/redoc` ⇒ renders
- [ ] T229 [sonnet] Contract test: OpenAPI matches runtime endpoints ⇒ schemathesis green
- [ ] T230 [sonnet] Load test: k6 script hits /sessions/ingest at 50 rps ⇒ <500ms p95
- [ ] T231 [sonnet] Load test: /driver/profile at 500 rps ⇒ <200ms p95
- [ ] T232 [sonnet] Error budget doc: SLO targets per endpoint ⇒ committed
- [ ] T233 [sonnet] Dependabot + renovate setup ⇒ PRs generated
- [ ] T234 [sonnet] Security scan: `pip-audit` + `bandit` run in CI ⇒ no high-severity findings
- [ ] T235 [sonnet] Backup job: daily pg_dump to R2 ⇒ file present
- [ ] T236 [sonnet] Restore-from-backup script tested in staging ⇒ green
- [ ] T237 [sonnet] Feature flags: `app/flags.py` with env-backed flags for gradual rollouts ⇒ used on one endpoint
- [ ] T238 [sonnet] API versioning: `v1` prefix locked, `v2` scaffold folder present ⇒ structure in place
- [ ] T239 [sonnet] Changelog: `CHANGELOG.md` with Keep-a-Changelog format ⇒ has M1 entries
- [ ] T240 [sonnet] README complete: dev setup, deployment, architecture diagram link ⇒ a new dev could onboard in 1h
