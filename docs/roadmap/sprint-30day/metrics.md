# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T18:55Z (Cycle #60)

## Per-repo status

| Repo | `[x]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|
| lap-backend | 51 | 1 (T013) | `772dc3d` (idle 12 cycles) |
| lap-webapp | 67 | 0 | `2c5ed02` (T148 skill-radar click-drilldown; 227) |
| lap-schemas (subset) | 34 | 0 | `6b8e80d` (T054 regen workflow README; pytest 74) |
| lap-mobile-android | 52 | **2** (T013 + T053 new) | `ff0fc60` (**REVERT of T053**) |
| lap-website (marketing) | 53 | 0 | `b50ef92` (T062 /pricing B2B teaser) |
| datalogger (desktop) | 31 | 0 | `dff270c` (T031 atomic temp→final rename lock) |

## This cycle (Cycle #60)

- Verified GREEN: 4 (webapp T148, schemas T054, website T062, datalogger T031)
- **Reverted: 1** — mobile T053 MigrationPolicy (ff0fc60 reverts f9ab816)
- SCOPE_FLAG: 0 new

## Cumulative (60 cycles)

- Total reviewed: 232 · Accepted+tagged: 229 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: **2** (cycle 4 datalogger early-state, cycle 60 mobile T053)
- Pause triggers: 0

## Cycle 60 notables — REVERT EVENT

- **Mobile T053 REVERTED** — `builder.addMigrations(*migrations.toTypedArray())` at MigrationPolicy.kt:31:30 tripped detekt's `SpreadOperator` rule (1 weighted issue → analysis fails build). Real lint error on applicable-rule per runbook → Step 3 revert. 
  - Revert commit: `ff0fc60`, pushed to origin alongside original `f9ab816`.
  - `sprint-mobile.md` T053 marked `[NEEDS_REWORK]` with failure reason + proposed fix direction: `@Suppress("SpreadOperator")` annotation or rewrite migrations addition as a loop.
  - After revert: detekt BUILD SUCCESSFUL at `ff0fc60` (confirmed clean).
  - Sprint-mobile loop will re-pick T053 in next iteration. Infinite revert-recreate risk mitigated by the sprint-loop presumably adapting approach.
- **First revert since cycle 4** (cycle 60 is the 2nd revert in 60 cycles — revert rate still 0.86%).

- Other 4 accepts:
  - Webapp T148 skill-radar click-drilldown → Routes.tsx +7 + test; 227 tests (+7).
  - Schemas T054 regen workflow in README (91/16 +/-).
  - Website T062 /pricing B2B teaser — 217 tests (+6).
  - Datalogger T031 atomic temp→final rename contract lock — 23/23 tests (+3).

- Backend 12 idle. Mobile back to T052 at `ff0fc60`.
- Disk 86% stable 37 cycles.

## Current issues

- **Mobile T053 NEEDS_REWORK** (new; detekt SpreadOperator).
- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 19:00 UTC.
