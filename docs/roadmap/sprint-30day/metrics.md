# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T11:10Z (Cycle #29)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 28 | 209 | 2 | 1 (T013) | 0 | `7b64848` (**13 idle cycles**) |
| lap-webapp | 43 | 197 | 0 | 0 | 0 | `75f5e3b` (idle 1 cycle) |
| lap-schemas (subset) | 11 | — | 0 | 0 | 0 | `3ffbbc9` (T031 SkillDimension + T030 Kotlin rewire; pytest 30) |
| lap-mobile-android | 30 | 210 | 0 | 0 | 0 | `291c7f3` (idle 5 cycles) |
| lap-website (marketing) | 30 | 190 | 0 | 0 | 1 (T017 inline) | `6f733b1` (idle 1 cycle; [x] count grew no-code) |
| datalogger (desktop) | 8 | 232 | 0 | 0 | 0 | `b6754ee` (T008 smoke-sim-disconnected) |

## This cycle (Cycle #29)

- Verified GREEN: 3 (schemas T031 Python + T030 Kotlin refactor, datalogger T008)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Website [x] count advanced +1 with no code commit → sprint-marketing bookkept a no-code task (decision/copy review)

## Cumulative (29 cycles)

- Total reviewed: 115 · Accepted+tagged: 113 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 29 notables

- **Second consecutive Kotlin refactor cycle**: T029 (SourceTag) in cycle 28, T030 (EnvironmentTag) in cycle 29. Both times used `:schemas:test --rerun-tasks` to force execution past Gradle UP-TO-DATE cache.
- **Datalogger T008 smoke test lands** — first user-journey test (boot with sim disconnected, 4 TDD cases) after 5 processor builds. Counter to the 19 pre-existing failures, new desktop tests continue green.
- Schemas Python pytest 30 (+3). Kotlin side: EnvironmentTag enum + SourceTag enum + SessionManifest rewire lockstep with Python.
- Mobile 5 idle cycles. Webapp 1 idle. Backend 13 idle.
- Disk 86% stable 6 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 11:15 UTC.
