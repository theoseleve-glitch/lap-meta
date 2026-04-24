# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T10:55Z (Cycle #28)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 27 | 210 | 2 | 1 (T013) | 0 | `7b64848` (**12 idle cycles**) |
| lap-webapp | 43 | 197 | 0 | 0 | 0 | `75f5e3b` (T112 timeline route shell) |
| lap-schemas (subset) | 10 | — | 0 | 0 | 0 | `2b17115` (T030 LapRecord + T029 Kotlin rewire; pytest 27) |
| lap-mobile-android | 29 | 211 | 0 | 0 | 0 | `291c7f3` (idle 4 cycles) |
| lap-website (marketing) | 29 | 191 | 0 | 0 | 1 (T017 inline) | `6f733b1` (T034 final-cta + trial) |
| datalogger (desktop) | 7 | 233 | 0 | 0 | 0 | `c36b134` (T007 LIVE_COACHING_ENABLED flag) |

## This cycle (Cycle #28)

- Verified GREEN: 5 (webapp T112, schemas T030 Python + T029 Kotlin, website T034, datalogger T007)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (28 cycles)

- Total reviewed: 112 · Accepted+tagged: 110 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 28 notables

- **Kotlin T029 refactor verified with forced rerun**: `./gradlew :schemas:test --rerun-tasks` BUILD SUCCESSFUL explicitly executed `:schemas:test` (not just UP-TO-DATE). Refactor commits need forced rerun or the cache may hide stale pass results.
- **Datalogger T007 = second modification commit** (coaching_live_processor.py +26/-2). Feature flag LIVE_COACHING_ENABLED gates T003's processor. 15 tests pass (new feature-flag file + existing native_bridge_contracts).
- Webapp T112 jumped from T090 to T112 — sprint-webapp loop skipped T091-T111 this window. New Next.js route `/timeline` shell.
- Schemas Python 27 pytest (+3 from T029's 24). Kotlin side: T029 rewired SessionManifest to use SourceTag enum + added SourceTagTest.
- Website T034 final-cta pricing/trial snippet — 107 tests (+9).
- Disk 86% stable 5 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 11:00 UTC.
