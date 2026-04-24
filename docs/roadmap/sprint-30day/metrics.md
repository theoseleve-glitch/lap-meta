# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T00:20Z (Cycle #13)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 14 | 226 | 0 | 1 (T013) | 0 | `edeb53d` (T015 CORS — aligned to new domain) |
| lap-webapp | 11 | 229 | 0 | 0 | 0 | `52e1cce` (5 idle cycles) |
| lap-schemas | 0 | — | 0 | 0 | 0 | `a50d39a` |
| lap-mobile-android | 16 | 224 | 0 | 0 | 0 | `d706c03` (T016 flavors dev/staging/prod) |
| lap-website | 16 | 4 BLOCKED | 4 | 0 | 1 (T017) | `6add4af` (T020 500 page) |
| datalogger | 2 | 238 | 0 | 0 | 0 | `eb97496` (9th quiet cycle) |

## This cycle (Cycle #13)

- Verified GREEN: 3 (backend T015 CORS — 10 pytest; mobile T016 flavors; website T020 — 3 pages)
- Reverted: 0 | NEEDS_REWORK: 0 new | SCOPE_FLAG: 0 new

**Cross-repo coherence improvement**: backend T015 CORS middleware explicitly pins origin to `https://app.lap-coach.racing` — now aligned with website T013's `lap.com → lap-coach.racing` migration. Domain coherence improved.

## Cumulative (13 cycles)

- Total reviewed: 56 · Accepted+tagged: 54 (1 INFRA_FLAG c4)
- Reverted: 1 (backend T013)
- Pause triggers: 0

## Cycle 13 notables

- **UTC date rolled** to 2026-04-24 at start of this cycle. Tags now `reviewed/20260424/...`.
- Backend pytest count now 10 (was 8 at T014). Growing test coverage each cycle.
- Mobile flavors setup triples gradle task count (121 for assembleDebug vs 41 typical) — matrix latency +~30%. Still well under timeout.
- Website builds 3 pages now (/, /404, /500).
- Webapp 5 consecutive idle cycles. Datalogger 9 consecutive quiet cycles.

## Current issues

- Backend T013 still NEEDS_REWORK (carried).
- Website T017 SCOPE_FLAG (carried).
- Webapp Terminal 2 + datalogger Terminal 3 both appear stopped.
- lap-website T008-T010 + T018 BLOCKED on user.
- **Daily email next eligible**: 08:07 UTC cycle (current 00:18 UTC → ~16 cycles from now).

## Cron: next fire 00:37 UTC.
