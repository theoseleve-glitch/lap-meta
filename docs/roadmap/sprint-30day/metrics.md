# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T22:25Z (Cycle #74)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 61 | 2 (T018/T019) | 1 (T013) | `9eb760c` (idle 1 cycle) |
| lap-webapp | 76 | **2 new** (T157, T158 on backend driver profile) | 0 | `9b170fa` (T159 chart a11y descriptions; 270) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 15 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 62 | 0 | 0 | `e9f505e` (idle 1 cycle) |
| lap-website (marketing) | 63 | 1 (T067) | 0 | `64ab068` (idle 1 cycle) |
| datalogger (desktop) | 40 | 1 (T035) | 0 | `be38dbe` (idle 1 cycle; **merge-marker WIP pollution still present**) |

## This cycle (Cycle #74)

- Verified GREEN: 1 (webapp T159)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **New BLOCKS**: webapp T157 + T158 self-gated on backend driver profile endpoint (T138 useDriverProfile hook). Both with detailed unblock reasoning including cross-task references (T138 data hook, T167 drilldown page, T231 Lighthouse CI integration).

## Cumulative (74 cycles)

- Total reviewed: 280 · Accepted+tagged: 276 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 74 notables — WEBAPP A11Y + TWO NEW SELF-AWARE BLOCKS

- **Webapp T159 chart text descriptions** — accessibility pass: each profile chart now has aria-describedby wired. SkillRadarChart `<desc>` with strongest/weakest dimensions. DriverScoreCard, ReadinessGauge, RecentSessionsSparkline get sr-only `<p>` summaries (trend range, event context, best/slowest lap). 270 tests (+7 from 263).
- **Webapp T157 + T158 both self-BLOCKED**: both cite backend driver profile endpoint (→ T138 useDriverProfile data hook) as the dep. T157 e2e additionally references T167 (drilldown page target, unbuilt). T158 LCP gating additionally references T231 (Lighthouse CI integration in Block K — proper scope for the gate). **3rd and 4th concurrent blocks on backend** (alongside desktop T035 backend ingestion). Active blocks total = 6 (T018/T019 docker, T013 webapp, T035 datalogger, T067 website, T157 + T158 webapp).
- Self-aware sprint behavior now at **6 documented instances** across 4 sprint loops:
  1. desktop T035 (backend ingestion) — c65
  2. website T067 (Cloudflare + edge) — c67
  3. webapp T155 no-op (T145 covered) — c69
  4. website T071 design-gate skip — c71
  5. webapp T157 (backend + T167) — c74
  6. webapp T158 (backend + T231) — c74
- 5 other repos idle. Schemas idle 15 cycles.
- Disk 86% stable 50 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- **Datalogger working tree still has unresolved merge markers in finalizer.py (lines 173, 338)** — sprint-desktop should resolve before next WIP commit. 2nd cycle in a row flagged.
- Desktop T035 [BLOCKED]: backend ingestion endpoint (datalogger T041 IngestClient client-side ready).
- Webapp T157 + T158 [BLOCKED]: backend driver profile endpoint (T138 useDriverProfile).
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function currency injection.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Backend dependency pressure

With T157+T158 webapp + T035 desktop all blocked on backend endpoints, sprint-backend's upcoming router work (T065-T080) has **3 downstream waiters**. When routers land, the unblocks will cascade.

## Cron: next 22:40 UTC.
