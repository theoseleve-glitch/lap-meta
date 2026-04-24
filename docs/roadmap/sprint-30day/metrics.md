# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T16:55Z (Cycle #52)

## Per-repo status

| Repo | `[x]` | HEAD |
|---|---|---|
| lap-backend | 45 | `772dc3d` (idle 4 cycles) |
| lap-webapp | 61 | `7a5bb70` (T142 ActivePrescriptionsList) |
| lap-schemas (subset) | 28 | `33111e6` (T048 @lap/schemas TS entry points; pytest 69) |
| lap-mobile-android | 47 | `94e76a3` (T047 TrackCacheEntity + MIGRATION_5_6) |
| lap-website (marketing) | 47 | `f63417e` (T055 /how-it-works e2e journey) |
| datalogger (desktop) | 25 | `8c91bf2` (T025 SessionFinalizer step 1 — accept SessionManifest) |

## This cycle (Cycle #52)

- Verified GREEN: 5 (webapp T142, schemas T048, mobile T047, website T055, datalogger T025)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (52 cycles)

- Total reviewed: 202 · Accepted+tagged: 200 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0
- **200-accept cumulative milestone**

## Cycle 52 notables

- **Mobile Room v6**: T047 TrackCacheEntity + MIGRATION_5_6. 5th consecutive Room migration. 6 entity tables total now (Session, Journal, UploadQueue, InsightCache, PrescriptionCache, TrackCache). TrackCache payload is opaque JSON blob (no Track Pydantic yet — deferred coupling).
- **Datalogger T025 SessionFinalizer** starts accepting `lap_schemas.v1.SessionManifest` at the writer boundary (31 ins / 2 del in finalizer.py + 156-line test). Cross-repo type now flowing through the actual data pipeline, not just imports.
- **Schemas T048** wires @lap/schemas TS package entry points (exports/types fields in typescript/package.json +9 lines). TS codegen pipeline: scaffold (T046) → emit script (T047) → package entry points (T048).
- Webapp T142 ActivePrescriptionsList (47 + 63 + index = 150 lines). 179 tests (+8).
- Website T055 /how-it-works e2e journey (navigate → consume → CTA, 28-line Playwright spec extension). 171 unit tests (e2e counted separately).
- Backend 4 idle.
- Disk 86% stable 29 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 17:00 UTC.
