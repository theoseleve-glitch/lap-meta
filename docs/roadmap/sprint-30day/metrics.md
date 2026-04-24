# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T13:10Z (Cycle #37)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 34 | 203 | 2 | 1 (T013) | 0 | `7b64848` (**21 idle cycles**) |
| lap-webapp | 49 | 191 | 0 | 0 | 0 | `1dfa795` (idle 1 cycle) |
| lap-schemas (subset) | 17 | — | 0 | 0 | 0 | `d6f89f0` (T037 ActionOutcome; pytest 48) |
| lap-mobile-android | 35 | 205 | 0 | 0 | 0 | `291c7f3` (idle 13 cycles) |
| lap-website (marketing) | 36 | 184 | 0 | 0 | 1 (T017 inline) | `374fb80` (T042 /how-it-works route shell — 4 pages) |
| datalogger (desktop) | 14 | 226 | 0 | 0 | 0 | `b76bdbd` (T014 pre-commit config + test) |

## This cycle (Cycle #37)

- Verified GREEN: 3 (schemas T037 Python-only, website T042, datalogger T014)
- Reverted: 0 | SCOPE_FLAG: 0 new
- P+K lockstep broken: Python T037 landed without Kotlin counterpart this cycle — sprint-mobile loop deferred

## Cumulative (37 cycles)

- Total reviewed: 145 · Accepted+tagged: 143 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 37 notables

- Website T042 lands **/how-it-works route shell** — second page on the site. Build output: 4 pages (up from 3). Wires T026 secondary CTA destination.
- Datalogger T014 adds **`.pre-commit-config.yaml`** (ruff + mypy + pytest hooks) + 59-line test validating config content. Not `pip install pre-commit` on review host (per Hard NEVER rule #1 on install-restrictions); the test validates YAML structure without executing hooks.
- Schemas T037 ActionOutcome (Python, 23 + 60 = 83 lines) — pytest 48. ADR object count: 17/35 (~49%).
- Backend 21 idle. Mobile 13 idle. Webapp 1 idle.
- Disk 86% stable 14 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 13:15 UTC.
