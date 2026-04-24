# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T15:25Z (Cycle #46)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 40 | 197 | 2 | 1 (T013) | 0 | `7b64848` (**30 idle cycles**) |
| lap-webapp | 56 | 184 | 0 | 0 | 0 | `a500e17` (T130 sessionDetailPath route helper) |
| lap-schemas (subset) | 24 | — | 0 | 0 | 0 | `afed51d` (idle 1 cycle) |
| lap-mobile-android | 42 | 198 | 0 | 0 | 0 | `428000f` (T042 SessionEntity + @Database v1 activation) |
| lap-website (marketing) | 42 | 178 | 0 | 0 | 1 (T017 inline) | `add0c59` (idle 1 cycle) |
| datalogger (desktop) | 20 | 220 | 0 | 0 | 0 | `bb2a36f` (idle 1 cycle) |

## This cycle (Cycle #46)

- Verified GREEN: 2 (webapp T130, mobile T042)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (46 cycles)

- Total reviewed: 177 · Accepted+tagged: 175 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0
- **Backend 30 idle cycles milestone** (from cycle 2 T020 Makefile → cycle 46 still at 7b64848)

## Cycle 46 notables

- **Mobile T042 activates Room persistence**: First `@Entity` lands (`SessionEntity` with id/state/started_at/ended_at/source/track_id/car_id/sample_count/file_uri), `@Database v1` active, KSP annotation processor green. SourceTag now has a dedicated converter (wireValue round-trip) so ingest-rejected values can't reach local storage. UUID7 identity converter removed per Room/KSP constraint. Subsequent entity additions will bump via Migrations per T053 policy. Full gradle matrix BUILD SUCCESSFUL with `:app:testDebugUnitTest` green.
- Webapp T130 sessionDetailPath helper (6 lines ts + 24 test). 139 tests (+5). Unlocks T131+ for clickable timeline entries.
- Backend 30 idle, webapp 0 idle, schemas 1 idle, mobile 0 idle, website 1 idle, datalogger 1 idle.
- Disk 86% stable 23 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 15:30 UTC.
