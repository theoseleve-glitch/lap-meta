# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T10:40Z (Cycle #27)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total sprint-backend.md) | 26 | 211 | 2 | 1 (T013) | 0 | `7b64848` (**11 idle cycles**) |
| lap-webapp | 42 | 198 | 0 | 0 | 0 | `dc2fc0a` (T090 OutcomeBadge) |
| lap-schemas (T021–T055 subset) | 9 | — | 0 | 0 | 0 | `e3277f1` (T029 SessionRecord + T028 Kotlin stub; pytest 24) |
| lap-mobile-android | 28 | 212 | 0 | 0 | 0 | `291c7f3` (idle 3 cycles) |
| lap-website (sprint-marketing) | 28 | 192 | 0 | 0 | 1 (T017 inline) | `a35e7e0` (T033 not-for-you-if anti-persona) |
| datalogger (sprint-desktop) | 6 | 234 | 0 | 0 | 0 | `64893ec` (T006 LiveTelemetryProcessor composition) |

## This cycle (Cycle #27)

- Verified GREEN: 5 (webapp T090, schemas T029 + T028-kt stub, website T033, datalogger T006)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (27 cycles)

- Total reviewed: 107 · Accepted+tagged: 105 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 27 notables

- **Datalogger T006 is first REFACTOR commit** (net -24 lines: 153 ins / 177 del in live_telemetry_processor.py). Unlike T003/T004/T005 which only added new files, T006 modifies existing code. Regression-tested by running `test_signal_plumbing.py` (existing downstream consumer of live_telemetry_processor) → 32/32 pass. T006's own 5 composition tests pass. No regressions.
- **Coaching tile component set complete**: webapp T088 (WeaknessEpisodeCard) + T089 (PrescriptionCard) + T090 (OutcomeBadge) — all 3 tiles of the "After every session" section now have typed React components. 5 test files / 40 tests pass (+8 from T089's 32).
- **Schemas Python ↔ Kotlin lockstep continues**: T029 SessionRecord (Python, 24 pytest) + T028 TelemetrySample Kotlin stub both land. Mobile `:schemas:build` BUILD SUCCESSFUL.
- Website T033 anti-persona "not for you if" disclosure — 98 tests (+8 from T032's 90). Persona filtering doctrine landed.
- Disk usage: **86%** stable for 4 cycles.

## Current issues

- Datalogger 19 pre-existing test failures (tech-debt; see cycle 24 bisect).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 Dockerfile + docker-compose BLOCKED.
- Website T017 SCOPE_FLAG (cycle 11 Lighthouse CI).
- Step 10 daily-email: deferred, out of user-prompt scope.

## Cron: next 10:45 UTC.
