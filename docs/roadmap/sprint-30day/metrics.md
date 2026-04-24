# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T15:10Z (Cycle #45)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 40 | 197 | 2 | 1 (T013) | 0 | `7b64848` (**29 idle cycles**) |
| lap-webapp | 56 | 184 | 0 | 0 | 0 | `9293914` (idle 1 cycle) |
| lap-schemas (subset) | 24 | — | 0 | 0 | 0 | `afed51d` (T043 OpenAPI generator script; pytest 66) |
| lap-mobile-android | 42 | 198 | 0 | 0 | 0 | `435a9de` (idle 1 cycle) |
| lap-website (marketing) | 42 | 178 | 0 | 0 | 1 (T017 inline) | `add0c59` (T048 Improve section step 04) |
| datalogger (desktop) | 20 | 220 | 0 | 0 | 0 | `bb2a36f` (T020 pip-pin leak regression guard) |

## This cycle (Cycle #45)

- Verified GREEN: 3 (schemas T043 OpenAPI generator, website T048, datalogger T020)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (45 cycles)

- Total reviewed: 175 · Accepted+tagged: 173 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 45 notables

- **Codegen infrastructure landing**: schemas T043 adds `generate_openapi.py` (81 lines) + test (50 lines). First codegen primitive — OpenAPI spec emission from Pydantic models. Future cycles could wire this to webapp `src/generated/` and mobile Kotlin generated classes. Sits idle until consumers invoke it.
- **Datalogger [x]=20 milestone** (from [x]=2 baseline at cycle 1 → [x]=20 at cycle 45; 18 accepted over 44 cycles).
- Website `/how-it-works` page now has 4 step sections: Capture (T045) + Brain (T046) + Plan (T047) + Improve (T048). 161 tests (+7). Full 4-step coaching-loop narrative assembled.
- Datalogger T020 removes a stray `=1.26` pip pin from an old requirement + 2-test regression guard. Pure-add (no actual pip-pin changes in the commit — just the guard). Another contract-test in the growing desktop shelf.
- Schemas Python pytest 66 (+3 from T043's generator tests).
- Backend 29 idle. Webapp + mobile 1 idle each.
- Disk 86% stable 22 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 15:15 UTC.
