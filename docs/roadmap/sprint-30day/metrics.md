# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T19:25Z (Cycle #62)

## Per-repo status

| Repo | `[x]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|
| lap-backend | 52 | 1 (T013) | `772dc3d` (idle 14 cycles) |
| lap-webapp | 68 | 0 | `a9c6043` (idle 1 cycle) |
| lap-schemas (subset) | 35 | 0 | `0dda9cb` (idle 1 cycle; Python parity 35/35 ✓) |
| lap-mobile-android | 53 | **2** (T013 + T054 new) | `d38d17b` (**REVERT** of T054) |
| lap-website (marketing) | 54 | 0 | `fff0d89` (idle 1 cycle) |
| datalogger (desktop) | 32 | 0 | `b248656` (idle 1 cycle) |

## This cycle (Cycle #62)

- Verified GREEN: 0
- **Reverted: 1** — mobile T054 JournalWriter (d38d17b reverts 7f34d84)
- 5 repos idle at cycle-61-end baselines

## Cumulative (62 cycles)

- Total reviewed: 238 · Accepted+tagged: 234 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: **3** (cycle 4 datalogger, cycle 60 mobile T053, cycle 62 mobile T054)
- Pause triggers: 0

## Cycle 62 notables — REVERT EVENT (mobile 2nd consecutive revert)

- **Mobile T054 REVERTED** — `JournalWriter.kt:32:66` tripped detekt's `MagicNumber` rule on literal `5` (heartbeat interval). 1 weighted issue → detekt analysis fails build. Runbook Step 3 revert.
  - Revert commit: `d38d17b`. Push pair: `a4c1bd2..d38d17b`.
  - sprint-mobile.md T054 marked `[NEEDS_REWORK]` with fix direction: extract `5L` to `private const val HEARTBEAT_INTERVAL_SECONDS = 5L`.
  - detekt BUILD SUCCESSFUL at revert HEAD (from cache — prior commit state).
- **Mobile now 2 reverts in 3 consecutive cycles** (c60 T053 SpreadOperator + c62 T054 MagicNumber). Both caught by detekt default rules. Pattern noted: sprint-mobile is shipping Kotlin that doesn't run local detekt pre-push.
- Sprint-file-ahead-of-code: sprint-mobile.md had T054 marked `[x]` at commit time; now back to `[NEEDS_REWORK]`.

## Cumulative revert rate

- **1.26% revert rate** over 62 cycles (3/238). Still well below typical code-review thresholds.

## Current issues

- **Mobile T054 NEEDS_REWORK** (new, detekt MagicNumber).
- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.
- **Pattern note**: sprint-mobile's 2 consecutive reverts for default-detekt-rule trips suggests detekt isn't in sprint-mobile's pre-push loop. Worth flagging to user at next opportunity.

## Cron: next 19:30 UTC.
