# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T18:25Z (Cycle #58)

## Per-repo status

| Repo | `[x]` | HEAD |
|---|---|---|
| lap-backend | 49 | `772dc3d` (idle 10 cycles) |
| lap-webapp | 65 | `5dbd53a` (T146 ProfileLayout composition; 217 tests) |
| lap-schemas (subset) | 32 | `7efa477` (idle 1 cycle; pytest 72) |
| lap-mobile-android | 51 | `3856589` (idle 1 cycle) |
| lap-website (marketing) | 51 | `a60b55c` (idle 1 cycle) |
| datalogger (desktop) | 29 | `07329a9` (idle 1 cycle) |

## This cycle (Cycle #58)

- Verified GREEN: 1 (webapp T146)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (58 cycles)

- Total reviewed: 222 · Accepted+tagged: 220 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 58 notables

- **Webapp ProfileLayout** (T146 ProfileLayout.tsx 47 + test 63 + index = 182 lines). **217 tests** (+8). Composes the profile route shell — now that all profile components exist (T137 shell, T139 DriverScoreCard, T140 SkillRadarChart, T141 OpenWeaknessesList, T142 ActivePrescriptionsList, T143 ReadinessGauge, T144 RecentSessionsSparkline, T145 ArchetypeBadge), T146 arranges them.
- Backend 10 idle cycles.
- Disk 86% stable 35 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 18:30 UTC.
