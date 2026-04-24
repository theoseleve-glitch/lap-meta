# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T17:55Z (Cycle #56)

## Per-repo status

| Repo | `[x]` | HEAD |
|---|---|---|
| lap-backend | 48 | `772dc3d` (idle 8 cycles) |
| lap-webapp | 64 | `0d650c9` (T145 ArchetypeBadge; 209 tests) |
| lap-schemas (subset) | 31 | `4916bc0` (T051 Kotlin codegen + chore exclude generated/; pytest 69) |
| lap-mobile-android | 50 | `dd36dcf` (T050 JournalDao — 2nd DAO; mobile [x]=50 milestone) |
| lap-website (marketing) | 50 | `4f3aa37` (T059 /pricing "What's included" checklist) |
| datalogger (desktop) | 28 | `c4cd898` (T028 SessionFinalizer step 4 — laps.parquet write) |

## This cycle (Cycle #56)

- Verified GREEN: 5 (webapp T145, schemas T051, mobile T050, website T059, datalogger T028)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Non-sprint ride-along accepted: schemas `4916bc0 chore(kotlin): exclude generated/ pending BigDecimal serializer`

## Cumulative (56 cycles)

- Total reviewed: 217 · Accepted+tagged: 215 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 56 notables

- **Mobile 2nd DAO** (JournalDao). DAO layer 2/7 entities covered.
- **Mobile [x]=50 milestone** (50/240 = 20.8%).
- **Schemas Kotlin codegen config** at parity with Swift + TS. Only Python source-of-truth; three codegen targets ready.
- Webapp T145 ArchetypeBadge — 209 tests (+9).
- Website T059 pricing "What's included" checklist — 195 tests (+9).
- Datalogger T028 SessionFinalizer now writes laps.parquet with round-trip validation. 4-step pipeline complete: accept manifest → write v2 manifest.json → parquet primary/CSV fallback → write laps.parquet.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 18:00 UTC.
