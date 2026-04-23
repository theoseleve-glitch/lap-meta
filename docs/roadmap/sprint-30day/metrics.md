# Sprint Metrics — live snapshot

## Last updated: 2026-04-23T23:50Z (Cycle #12)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 13 | 227 | 0 | 1 (T013) | 0 | `6018966` (T014 DI stubs) |
| lap-webapp | 11 | 229 | 0 | 0 | 0 | `52e1cce` (**4 idle cycles**) |
| lap-schemas | 0 | — | 0 | 0 | 0 | `a50d39a` |
| lap-mobile-android | 15 | 225 | 0 | 0 | 0 | `2208d57` (T015 keystore.properties) |
| lap-website | 15 | 4 BLOCKED (T008-T010, T018) | 4 | 0 | 1 (T017) | `3e57701` (T019 404 page) |
| datalogger | 2 | 238 | 0 | 0 | 0 | `eb97496` (**8th quiet cycle**) |

## This cycle (Cycle #12)

- Verified GREEN: 3 (backend T014 — 8 pytest tests now; mobile T015 keystore; website T019 404 — build now emits 2 pages)
- Reverted: 0 | NEEDS_REWORK: 0 new (T013 still open)
- SCOPE_FLAG: 0 new (T017 still open)

## Cumulative (12 cycles)

- Total reviewed: 53 · Accepted+tagged: 51 (1 INFRA_FLAG c4)
- **Reverted: 1** (backend T013, cycle 11, NEEDS_REWORK awaiting sprint-loop redo)
- Pause triggers: 0

## Current issues

- **Backend T013 still NEEDS_REWORK** — sprint loop moved past it (T014 green now). Will re-pick when user or sprint-loop rule changes process [NEEDS_REWORK] tasks. Not time-sensitive; T013 is env.example schema, can be re-done anytime.
- **Webapp 4 consecutive idle cycles** — Terminal 2 very likely stalled.
- **Datalogger 8 consecutive quiet cycles** — Terminal 3 almost certainly stopped.
- lap-website T008-T010 + T018 BLOCKED on user (Cloudflare/Chromatic-Percy OAuth).

## Cross-repo observation

Website T013 migrated site URL `lap.com → lap-coach.racing`. Backend/webapp/mobile still reference old domain in code — but no current sprint task requires webapp-backend URL coherence. Not a contract-drift fail per runbook Step 5, just a migration-in-progress artifact.

## Cron: next fire 00:07 UTC (first cycle of 2026-04-24).
