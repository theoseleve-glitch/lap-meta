# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T10:10Z (Cycle #25)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 18 | 212 | 2 | 1 (T013) | 0 | `7b64848` (**9 idle cycles**) |
| lap-webapp | 41 | 199 | 0 | 0 | 0 | `2df91cc` (idle 1 cycle) |
| lap-schemas (T021–T055 tracked in sprint-backend) | 8 | — | 0 | 0 | 0 | `124b8c4` (T028 Python + T027 Kotlin stub — pytest 21, gradle BUILD SUCCESSFUL) |
| lap-mobile-android | 27 | 213 | 0 | 0 | 0 | `291c7f3` (idle 1 cycle) |
| lap-website (sprint-marketing) | 27 | 193 | 0 | 0 | 1 (T017 inline) | `152a1d3` (T032 compare-to-tools-you-know) |
| datalogger (sprint-desktop) | 5 | 235 | 0 | 0 | 0 | `6690165` (T005 InputDiagnosticsProcessor — own 5/5 pass) |

## This cycle (Cycle #25)

- Verified GREEN: 4 (schemas T028 + sprint(mobile) T027 Kotlin stub, website T032, datalogger T005)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Concurrent-commit capture: `124b8c4 sprint(mobile): T027 SessionManifest Kotlin stub` landed between snapshot and push — detected post-push, matrix-verified, tagged

## Cumulative (25 cycles)

- Total reviewed: 101 · Accepted+tagged: 99 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 25 notables

- **Schemas Python ↔ Kotlin in lock-step**: T028 lands `TelemetrySample` on Python side (21 pytest, +3), T027 Kotlin stub lands `SessionManifest.kt` (51 lines) on Kotlin side — two parallel sprint loops (sprint-backend, sprint-mobile) writing to `lap-schemas/python/` and `lap-schemas/kotlin/` respectively. Mobile Gradle `:schemas:build` BUILD SUCCESSFUL with the new Kotlin stub → **cross-repo binding healthy**.
- **Data contract surface grew**: Python Pydantic models (SessionManifest, DataQuality, TelemetrySample, SensorConfigSnapshot, SourceTag, EnvironmentTag, UUID7) now = 7 of the 35 ADR-006/ADR-007 objects. Kotlin mirror = 1 (SessionManifest stub).
- Datalogger Terminal 3 steady: T003 → T004 → T005 across cycles 22, 24, 25 (T005 added InputDiagnosticsProcessor 70-line module, 5 TDD tests).
- Website T032 "compare to tools you know" section — 90 tests (+8 from T031's 82). Persona framing aligned with STRATEGIC-DOCTRINE.md §3.
- Disk usage: **86%** stable.

## Current issues

- **Datalogger pre-existing-failures tech-debt**: 19 failing tests (4 sync_queue + 15 overlay/workspaces/ghost). Predates T003. See cycle 24 bisect detail.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 Dockerfile + docker-compose BLOCKED (docker not installed).
- Website T017 SCOPE_FLAG (Lighthouse CI 2267 lines — cycle 11).
- Step 10 daily-email not fired: `ops/.last_daily_sent`=2026-04-23 stale; out of user-prompt scope.

## Cron: next 10:15 UTC (15-min /loop cadence).
