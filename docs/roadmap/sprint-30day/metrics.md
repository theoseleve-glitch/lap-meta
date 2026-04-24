# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T16:00Z (Cycle #48)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 42 | 195 | 2 | 1 (T013) | 0 | `772dc3d` (T045 depend on lap-schemas — **first backend commit since cycle 2**, 31-cycle idle streak ended) |
| lap-webapp | 58 | 182 | 0 | 0 | 0 | `cb5285e` (T139 DriverScoreCard component) |
| lap-schemas (subset) | 25 | — | 0 | 0 | 0 | `8cac625` (idle 1 cycle; pytest 69) |
| lap-mobile-android | 44 | 196 | 0 | 0 | 0 | `6bc18a7` (T044 UploadQueueEntity + MIGRATION_2_3) |
| lap-website (marketing) | 43 | 177 | 0 | 0 | 1 (T017 inline) | `2343382` (idle 1 cycle) |
| datalogger (desktop) | 22 | 218 | 0 | 0 | 0 | `b78fdb5` (T022 shared SessionManifest from lap-schemas) |

## This cycle (Cycle #48)

- Verified GREEN: 4 (backend T045, webapp T139, mobile T044, datalogger T022)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Backend 31-cycle idle streak ENDS** (cycle 2 T020 Makefile → cycle 48 T045 depend on lap-schemas)
- **Backend full matrix green** for first time: ruff clean, mypy Success (7 source files), pytest 18 passed, uv sync resolved 44 packages, uv.lock regenerated
- **Datalogger uses shared SessionManifest**: T022 completes the cycle-47 T021 dep wiring by actually replacing local type with shared v1 type — the cross-repo dep is now load-bearing

## Cumulative (48 cycles)

- Total reviewed: 186 · Accepted+tagged: 184 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 48 notables

- **Backend activation event**: After 31 idle cycles (cycle 2 → cycle 47), lap-backend sprint T045 lands `depend on lap-schemas` — adds lap-schemas to pyproject.toml + 10-line test_schemas_import.py + 29-line uv.lock refresh. Backend now mirrors datalogger T021's cross-repo wiring pattern. Backend matrix: uv sync OK, ruff "All checks passed", mypy "Success: no issues found in 7 source files", pytest 18 passed.
- **Cross-repo dep parity achieved across ALL Python consumers**: schemas source-of-truth → datalogger (T021) → backend (T045). Plus Kotlin `:schemas` → mobile-android (since cycle 24). Schema contract layer is now the true single source of truth, with declared dependencies in consumers.
- Mobile T044 second Room migration (v2→v3) — UploadQueueEntity for T147 chunked upload worker + T154 backoff curve. 55+56 = 111 lines. Full gradle matrix green.
- Datalogger T022 replaces local `SessionManifest` with `lap_schemas.v1.SessionManifest` — bundle_schema.py + finalizer.py refactored, 23 tests pass (bundle_schema_uses_shared_manifest + session_bundle + lap_schemas_available).
- Webapp T139 DriverScoreCard (100 + 73 + index = 234 ins) — 154 tests (+13 from T137's 141). Substantial profile-route component.
- Backend 0 idle, webapp 0 idle, schemas 1 idle, mobile 0 idle, website 1 idle, datalogger 0 idle — most active cycle yet.
- Disk 86% stable 25 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 16:05 UTC.
