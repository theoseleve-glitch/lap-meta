# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T11:55Z (Cycle #32)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 30 | 207 | 2 | 1 (T013) | 0 | `7b64848` (**16 idle cycles**) |
| lap-webapp | 46 | 194 | 0 | 0 | 0 | `6b34ca9` (T117 newWeaknessesBadge derivation) |
| lap-schemas (subset) | 13 | — | 0 | 0 | 0 | `2e9717c` (T033 WeaknessCategory + T032 SensorConfigSnapshot Kotlin; pytest 36) |
| lap-mobile-android | 32 | 208 | 0 | 0 | 0 | `291c7f3` (idle 8 cycles) |
| lap-website (marketing) | 32 | 188 | 0 | 0 | 1 (T017 inline) | `6250dc6` (T037 homepage JS budget lock <100 kB) |
| datalogger (desktop) | 10 | 230 | 0 | 0 | 0 | `ed9b004` (T010 QML property-collision regression guard) |

## This cycle (Cycle #32)

- Verified GREEN: 5 (webapp T117, schemas T033 Python + T032 Kotlin, website T037, datalogger T010)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Datalogger reaches **10 [x]** milestone (first repo to double-digit [x] on T-numbered tasks from [x]=2 baseline 30 cycles ago)

## Cumulative (32 cycles)

- Total reviewed: 127 · Accepted+tagged: 125 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 32 notables

- **Website T037 homepage JS budget contract** (~64-line test parses `dist/index.html`, gzips chunks, asserts sum <100_000 bytes). Scaffold budget for keeping bundle lean; no CI workflow touched this time — the test lives in vitest suite.
- **Datalogger T010 regression guard** for a VM property-collision TypeError. Pure-add test file (64 lines, 2 tests). Smoke + regression test pattern emerging in sprint-desktop's testing strategy.
- 5th consecutive Python+Kotlin lockstep cycle: T033 WeaknessCategory enum (Python) + T032 SensorConfigSnapshot data class (Kotlin, 47-line test).
- Webapp T117 newWeaknessesBadge derivation — 69 tests (+7).
- Disk 86% stable 9 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 12:00 UTC.
