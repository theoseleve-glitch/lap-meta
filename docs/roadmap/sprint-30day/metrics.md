# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T18:40Z (Cycle #59)

## Per-repo status

| Repo | `[x]` | HEAD |
|---|---|---|
| lap-backend | 50 | `772dc3d` (idle 11 cycles) |
| lap-webapp | 66 | `625d2a8` (T147 ProfileLayout responsive tests; 220) |
| lap-schemas (subset) | 33 | `774094e` (T053 post-commit Pydantic drift warning; pytest 74) |
| lap-mobile-android | 52 | `6d6887e` (T052 InsightCacheDao — 4th DAO) |
| lap-website (marketing) | 52 | `ffae773` (T061 /pricing FAQ 10 Qs) |
| datalogger (desktop) | 30 | `9bb1227` (T030 SessionFinalizer step 6 — sha256 checksums) |

## This cycle (Cycle #59)

- Verified GREEN: 5 (webapp T147, schemas T053, mobile T052, website T061, datalogger T030)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (59 cycles)

- Total reviewed: 227 · Accepted+tagged: 225 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 59 notables

- **Mobile 4th DAO** (InsightCacheDao) — upsertBatch (one HTTP roundtrip → many inserts in single transaction) + listForSession (dashboard offline list per T195). 4/7 entities covered; 3 remain (PrescriptionCache, TrackCache, RuleBundle).
- **Schemas T053 post-commit Pydantic drift warning** — adds `.githooks/post-commit` (33 lines) + 65-line contract test. Dev-local warning when Pydantic schema changes aren't matched by codegen updates. Complements T052 CI enforcement with a faster local signal.
- Datalogger T030 **sha256 manifest checksums** (step 6 in SessionFinalizer pipeline). finalizer.py +29 / -2 + test file +78 lines = 20/20 tests. Checksums now computed for written outputs; integrity verifiable at ingestion.
- Website T061 /pricing FAQ — 10 questions native `<details>/<summary>` (117-line PricingFaq.astro). 211 tests (+9).
- Webapp T147 ProfileLayout responsive-stacking tests (+29 test lines + 9/-3 src) — 220 tests (+3).
- Backend 11 idle.
- Disk 86% stable 36 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 18:45 UTC.
