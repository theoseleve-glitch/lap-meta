# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T11:40Z (Cycle #31)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 29 | 208 | 2 | 1 (T013) | 0 | `7b64848` (**15 idle cycles**) |
| lap-webapp | 45 | 195 | 0 | 0 | 0 | `f03f703` (T116 groupByWeek utility) |
| lap-schemas (subset) | 12 | — | 0 | 0 | 0 | `8af8655` (T032 DriverProgressSnapshot + T031 DataQuality Kotlin; pytest 33) |
| lap-mobile-android | 31 | 209 | 0 | 0 | 0 | `291c7f3` (idle 7 cycles) |
| lap-website (marketing) | 31 | 189 | 0 | 0 | 1 (T017 inline) | `b0c103b` (T036 LCP 1.5s mobile 4G) |
| datalogger (desktop) | 9 | 231 | 0 | 0 | 0 | `8343002` (T009 iRacing mock smoke test) |

## This cycle (Cycle #31)

- Verified GREEN: 5 (webapp T116, schemas T032 Python + T031 Kotlin, website T036, datalogger T009)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Workflow-touch observed: website T036 edits `.github/workflows/ci.yml` — label-only rename, no `workflow_dispatch`/`secrets.*` additions → guardrail condition NOT met → ACCEPT

## Cumulative (31 cycles)

- Total reviewed: 122 · Accepted+tagged: 120 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 31 notables

- **Website T036 tightens LCP gate 1.8s → 1.5s on mobile 4G profile**. Changes `preset: desktop` → default mobile, adds 4 TDD budget contract tests. Touches `.github/workflows/ci.yml` (job label rename only — not a secrets/dispatch addition) + lighthouserc.json + CLAUDE.md convention sync. ACCEPTED as legitimate sprint-marketing T036 material.
- Webapp T116 `groupByWeek` utility (74-line function + 73-line test) — pure utility landing before TimelineEntry consumer rendering.
- Schemas Python T032 DriverProgressSnapshot (37 + 87 lines) + Kotlin T031 DataQuality data class (51 lines) — 4th consecutive Python+Kotlin lockstep cycle.
- Datalogger T009 second smoke test (iRacing mock live processor, 86 lines, 3 TDD cases). Smoke test series grows: T008 (disconnected) + T009 (iRacing mock) = 2 of N boot scenarios.
- Disk 86% stable 8 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 11:45 UTC.
