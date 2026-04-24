# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T18:10Z (Cycle #57)

## Per-repo status

| Repo | `[x]` | HEAD |
|---|---|---|
| lap-backend | 49 | `772dc3d` (idle 9 cycles) |
| lap-webapp | 65 | `0d650c9` (idle 1 cycle) |
| lap-schemas (subset) | 32 | `7efa477` (T052 schema-sync-check CI job; pytest 72) |
| lap-mobile-android | 51 | `3856589` (T051 UploadQueueDao — 3rd DAO) |
| lap-website (marketing) | 51 | `a60b55c` (T060 founder-waitlist offer) |
| datalogger (desktop) | 29 | `07329a9` (T029 events.json contract) |

## This cycle (Cycle #57)

- Verified GREEN: 4 (schemas T052, mobile T051, website T060, datalogger T029)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **New workflow file**: `.github/workflows/schema-sync.yml` added in schemas T052 (push + pull_request triggers, no workflow_dispatch, no secrets.*) — guardrail condition NOT met → ACCEPT

## Cumulative (57 cycles)

- Total reviewed: 221 · Accepted+tagged: 219 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 57 notables

- **Schemas T052 schema-sync-check CI job**: 62-line new workflow file runs Python OpenAPI generate → TypeScript + Kotlin codegen → verify committed generated files match. Fires on push + pull_request. Uses `astral-sh/setup-uv@v5` + `actions/setup-node@v4` + `actions/setup-java@v4` — standard actions, no secrets, no workflow_dispatch. pytest 72 (+3 from T051's 69; contract test validates workflow structure). **Load-bearing cross-language sync enforcement now in CI**.
- **Mobile 3rd DAO**: T051 UploadQueueDao + LapDatabase.uploadQueueDao(). Methods: enqueue (upsert at finalize), dequeueNext (FIFO pick for T147 UploadBundleWorker), updateAttempt (records backoff state per T154 retry curve). FIFO via `ORDER BY session_id ASC` since UUIDv7 is time-ordered by construction.
- Website T060 founder-waitlist offer (35-line PricingFounderOffer.astro + mount + test). 202 tests (+7).
- Datalogger T029 locks events.json contract structure (sector/lap/flag) at SessionFinalizer. 17/17 tests (up from 14). +66 lines in test_finalizer_accepts_manifest.py only — pure test-add.
- Backend 9 idle, webapp 1 idle.
- Disk 86% stable 34 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 18:15 UTC.
