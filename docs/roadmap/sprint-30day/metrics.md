# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T14:10Z (Cycle #41)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 37 | 200 | 2 | 1 (T013) | 0 | `7b64848` (**25 idle cycles**) |
| lap-webapp | 53 | 187 | 0 | 0 | 0 | `455a6b4` (idle 1 cycle) |
| lap-schemas (subset) | 21 | — | 0 | 0 | 0 | `5bb57e8` (T040 CohortDef + DriverBenchmarkProfile + T039 UUID7 Kotlin; pytest 57) |
| lap-mobile-android | 39 | 201 | 0 | 0 | 0 | `291c7f3` (idle 17 cycles) |
| lap-website (marketing) | 39 | 181 | 0 | 0 | 1 (T017 inline) | `ce6706d` (T045 Capture section step 01) |
| datalogger (desktop) | 16 | 224 | 0 | 0 | 0 | `b49d989` (idle 1 cycle) |

## This cycle (Cycle #41)

- Verified GREEN: 3 (schemas T040 Python + T039 Kotlin UUID7, website T045)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (41 cycles)

- Total reviewed: 160 · Accepted+tagged: 158 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 41 notables

- Schemas subset **21/35 (~60%)** ADR objects. Python 57 tests.
- Schemas T040 landed both `CohortDef` and `DriverBenchmarkProfile` in one commit (41 + 53 = 94 lines) — first multi-object Python commit.
- Kotlin T039 UUID7 typealias + `validateUuid7()` helper (adds type-safe ID wrapper + 54-line IdsTest.kt). Touches SessionManifest.kt to use the new typealias.
- Website T045 /how-it-works Capture step 01 section (56-line Astro component + mount). 140 tests (+8). Diagram from T044 is being progressively annotated with step-by-step component sections.
- Backend 25 idle, mobile 17 idle, webapp 1 idle, datalogger 1 idle.
- Disk 86% stable 18 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Kotlin-ahead-of-Python CoachingInsight (cycle 38).
- Step 10 daily-email deferred.

## Cron: next 14:15 UTC.
