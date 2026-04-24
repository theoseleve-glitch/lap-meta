# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T13:25Z (Cycle #38)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 35 | 202 | 2 | 1 (T013) | 0 | `7b64848` (**22 idle cycles**) |
| lap-webapp | 50 | 190 | 0 | 0 | 0 | `8dac3bc` (T123 DateRangeFilter) |
| lap-schemas (subset) | 18 | — | 0 | 0 | 0 | `be89964` (T038 DivergencePoint + T036 CoachingInsight Kotlin; pytest 51) |
| lap-mobile-android | 36 | 204 | 0 | 0 | 0 | `291c7f3` (idle 14 cycles) |
| lap-website (marketing) | 36 | 184 | 0 | 0 | 1 (T017 inline) | `374fb80` (idle 1 cycle) |
| datalogger (desktop) | 14 | 226 | 0 | 0 | 0 | `b76bdbd` (idle 1 cycle) |

## This cycle (Cycle #38)

- Verified GREEN: 3 (webapp T123, schemas T036 Kotlin + T038 Python concurrent-capture)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Concurrent-commit capture**: schemas T038 DivergencePoint landed post-snapshot, detected via push `d6f89f0..be89964` range, matrix-verified green (pytest 51 +3), tagged

## Cumulative (38 cycles)

- Total reviewed: 148 · Accepted+tagged: 146 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 38 notables

- **Kotlin-first pattern observed**: schemas T036 `CoachingInsight consumer stub` landed in Kotlin WITHOUT a corresponding Python Pydantic source. Commit body explicitly documents the inversion: "No Pydantic source exists yet; stub derived from the 6-month roadmap doc — the two nested types (Evidence, MeasurableTarget) are deferred until canonical Python lands. severity RFC3339 strings until T038." Valid sprint work; sprint-mobile is getting ahead on mobile-consumer-only shapes. Will require reconciliation when Python T045+ lands CoachingInsight.
- Schemas subset now 18/35 (~51%). Schemas Python 51 pytest (+3 from T038 DivergencePoint; 3 tests).
- Webapp T123 DateRangeFilter (68 + 112 = 180 lines implementation + test) — 96 tests (+11). Big test-count jump for a UI primitive.
- Backend 22 idle, mobile 14 idle, webapp 0 idle now after T123 landed, website 1 idle, datalogger 1 idle.
- Disk 86% stable 15 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- **Kotlin-ahead-of-Python for CoachingInsight** — minor: tracked, will reconcile at T045.
- Step 10 daily-email deferred.

## Cron: next 13:30 UTC.
