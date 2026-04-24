# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T23:10Z (Cycle #77)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 64 | 2 (T018/T019) | 1 (T013) | `3eb2f5d` (T067 DriverProgressSnapshot — **10th model**) |
| lap-webapp | 80 | 5 (T157/T158/T161/T162/T164) | 0 | `f863930` (T167 skill drilldown route shell — first dynamic route) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 18 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 65 | 0 | 0 | `590d4ca` (T065 LocationSample→TelemetrySample mapper with gnss clock) |
| lap-website (marketing) | 66 | 1 (T067) + implicit (T082/T084) | 0 | `7f2e426` (T086 /demo testimonials placement) |
| datalogger (desktop) | 42 | 1 (T035) | 0 | `a6a40c7` (T043 Idempotency-Key header — ADR-012) |

## This cycle (Cycle #77)

- Verified GREEN: 5 (backend T067, webapp T167 mid-cycle, mobile T065 mid-cycle, website T086, datalogger T043)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (77 cycles)

- Total reviewed: 294 · Accepted+tagged: 290 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 77 notables — 10TH ORM MODEL (MILESTONE) + DYNAMIC WEBAPP ROUTE + GNSS MAPPER + IDEMPOTENCY HEADER

- **Backend T067 DriverProgressSnapshot ORM + migration** — **10th ORM model** 🎯. 48/48 (+2). orm.py +49 (largest ORM class yet — snapshot captures aggregate state: SkillProfile, Weaknesses, Prescriptions at a point-in-time). Migration 57. Tests 145. The snapshot pattern enables webapp's driver profile endpoint (T138 hook) — this is likely the last ORM before routers.
- **Webapp T167 skill drilldown route shell** (mid-cycle) — **first dynamic route** in webapp (Next.js 14 `[dimension]` catch-all). URL-decodes slug, kebab→human label. 53 ins. 281 tests (+4). Ships the UI surface that T157 e2e was blocked on (T157 still needs backend data to fully wire).
- **Mobile T065 LocationSample→TelemetrySample mapper with gnss source clock** (mid-cycle) — 178 ins. Converts captured location samples to domain's TelemetrySample with gnss timestamp as source-clock (not Android system clock — avoids skew). 12 consecutive clean mobile accepts. Capture→domain transformation layer begins.
- **Website T086 /demo testimonials placement** — 34 ins. Mounts shared T035 SocialProof between walkthrough (T073) and CTA (T085). Zero new components; doctrine-aligned "no testimonials until beta" message anchored single-place.
- **Datalogger T043 Idempotency-Key header** — 90 ins. Adds ADR-012 `Idempotency-Key: <session_id (UUID7)>` to `IngestClient.upload`. Backend will deduplicate retries at HTTP layer. 1503 passed (+2), 19 stable failures.
- Schemas idle 18 cycles.
- Disk 86% stable 53 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22, occasional 20th flake).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Webapp 5 [BLOCKED]: T157, T158, T161, T162, T164 — all on backend endpoints.
- Website T067 [BLOCKED]: Cloudflare OAuth.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Backend dependency pressure (unchanged: 6 blocks)

Sprint-backend at T067 (10th ORM). Router phase is likely next — will unblock 6 downstream.

## Cron: next 23:25 UTC.
