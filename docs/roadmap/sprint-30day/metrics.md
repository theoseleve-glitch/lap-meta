# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T22:10Z (Cycle #73)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 61 | 2 (T018/T019) | 1 (T013) | `9eb760c` (T064 WeaknessEpisode — 7th model) |
| lap-webapp | 75 | 0 | 0 | `ebaef85` (idle 1 cycle) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 14 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 62 | 0 | 0 | `e9f505e` (T062 LocationPermissionManager) |
| lap-website (marketing) | 63 | 1 (T067) | 0 | `64ab068` (T081 demo LCP budget via assertMatrix) |
| datalogger (desktop) | 40 | 1 (T035) | 0 | `be38dbe` (T041 IngestClient typed surface; ADR-012) |

## This cycle (Cycle #73)

- Verified GREEN: 4 (backend T064, mobile T062 mid-cycle, website T081 mid-cycle, datalogger T041 mid-cycle via Phase-1 bisect)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Mid-cycle commits this cycle: 3** (mobile T062, website T081, datalogger T041) — highest count to date. Confirms the "re-fetch per repo before tagging" pattern.

## Cumulative (73 cycles)

- Total reviewed: 279 · Accepted+tagged: 275 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 73 notables — 7TH ORM + MOBILE PERMISSION LAYER + DEMO BUDGET GATE + DATALOGGER INGEST CLIENT

- **Backend T064 WeaknessEpisode ORM** — 7th model. `infra/orm.py` +38, migration 55, tests 152 — new record for backend test file size. 40/40 (+3). FK to Session. Captures ADR-005's coaching artifact pattern (one-to-many driver weaknesses per session).
- **Mobile T062 LocationPermissionManager** (mid-cycle) — Android fine+coarse+background permission flow. Clean 5-file separation: PermissionChecker interface, ContextPermissionChecker impl, LocationPermissionManager (58), LocationPermissionState (16 enum), tests 140 cases. 9 consecutive clean mobile accepts. Capture layer now has permission gating before sensor start.
- **Website T081 demo LCP budget** (mid-cycle) — migrates lighthouserc.json from single `assertions` to `assertMatrix` with per-URL budgets: /demo ≤2000ms LCP, / keeps 1500ms. 249 tests (+3). Budget gate lands BEFORE T074 video ships — forward-defensive: when the video lands, it must pass the contract already in place.
- **Datalogger T041 IngestClient typed surface** (mid-cycle, ADR-012) — creates `infra/` package + `IngestClient` skeleton for `POST /api/v1/sessions/ingest` endpoint. Frozen `IngestResult` dataclass with `session_id`, `ingest_job_id`, `status_stream`. **Backend ingestion contract surface emerging** (T035 unblock path now visible).
- **Systematic-debugging Phase-1 bisect caught sprint-desktop WIP pollution**: datalogger working tree had unresolved `<<<<<<< Updated upstream` merge markers in finalizer.py (lines 173, 338) — not from T041, but from sprint-desktop's half-merged T042+ WIP. Stashed ALL dirty state → verified T041 clean (1485 passed, 19 pre-existing failures) → popped. T041 accepted per ADR-017: stale WIP is not a revert trigger.
- Schemas idle 14 cycles.
- Disk 86% stable 49 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- **Datalogger working tree has unresolved merge markers in src/lap_coach_logger/writers/finalizer.py (lines 173 + 338)** — sprint-desktop WIP carrying bad merge state. NOT blocking review loop (stash+restore pattern works) but sprint-desktop should resolve before next WIP commit. Flag for user.
- Desktop T035 [BLOCKED]: backend ingestion endpoint — **unblock path now in sight** (T041 IngestClient, upcoming backend routers).
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function currency injection.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 22:25 UTC.
