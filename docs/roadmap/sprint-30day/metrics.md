# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T09:45Z (Cycle #22)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 17 | 214 | 2 | 1 (T013) | 0 | `7b64848` (**6 idle cycles** — schemas-phase natural) |
| lap-webapp | 39 | 201 | 0 | 0 | 0 | `7b95523` (T058 prune unused CSS) |
| lap-schemas (T021–T055 tracked in sprint-backend) | 6 | — | 0 | 0 | 0 | `8199e8d` (T026 DataQuality — pytest 15) |
| lap-mobile-android | 25 | 215 | 0 | 0 | 0 | `b7b6681` (T025 androidTest launch smoke) |
| lap-website (sprint-marketing) | 25 | 195 | 0 | 0 | 1 (T017) | `8d34fee` (idle, 2 cycles) |
| datalogger (sprint-desktop) | 3 | 237 | 0 | 0 | 0 | `f3c1cc7` (T003 — ends 17-cycle quiet streak) |

## This cycle (Cycle #22)

- Verified GREEN: 4 (webapp T058, schemas T026, mobile T025, datalogger T003)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Datalogger **T003 ends Terminal-3 quiet streak** at 17 cycles

## Cumulative (22 cycles)

- Total reviewed: 91 · Accepted+tagged: 89 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c_)
- Reverted: 1 · Pause triggers: 0

## Cycle 22 notables

- **Mobile `detekt` + `ktlintCheck` now APPLICABLE** per Gradle task list (previously flagged as not-applicable per cycle-2 memory) — sprint-mobile block landed detekt/ktlint config between then and now. Both pass BUILD SUCCESSFUL at HEAD.
- **Datalogger 4 pre-existing `test_sync_queue` failures detected** (tests from the cycle-1 manual integration commit `304c0a9`). Verified fail at both current HEAD `f3c1cc7` and prior baseline `eb97496` — predates T003, not regression. Flagged as tech-debt; not a cycle-22 revert trigger.
- Schemas pytest **15 passed** (+3 from T025's 12). Steady coverage growth per new Pydantic model.
- Disk usage: **86%** (down 3pp from cycle 21's 89%; 95% pause threshold healthy).
- Webapp `[x]` count 39 at cycle 22 vs. 18 reported cycle 21 — prior metrics rows under-counted; current count authoritative via `grep -cE '^- \[x\] T[0-9]' sprint-webapp.md`.

## Current issues

- **Datalogger sync_queue tech-debt** — 4 failing tests (`test_ensure_sync_metadata_persists_required_fields`, `test_queue_session_is_deduplicated_by_session_and_bundle_hash`, `test_process_queue_skips_when_sync_feature_disabled`, `test_process_queue_drops_entry_after_max_retry_attempts`). Pre-existing since cycle-1 bulk integration. Needs dedicated fix task.
- Datalogger user-WIP working tree (30+ files) causes additional 15 flaky overlay/session_coordinator test failures when left in-tree; clean-HEAD pytest shows only the 4 pre-existing failures.
- Backend T013 NEEDS_REWORK persistent.
- Website T017 SCOPE_FLAG persistent.

## Cron: next 10:00 UTC (15-min /loop cadence). Daily email eligible (ops/.last_daily_sent=2026-04-23, today=2026-04-24) — NOT sent this cycle (out of user-prompt scope Step 10).
