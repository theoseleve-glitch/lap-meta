# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T20:55Z (Cycle #68)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 57 | 2 (T018/T019 docker) | 1 (T013) | `3de44d4` (T060 Session ORM — 3rd model) |
| lap-webapp | 73 | 0 | 0 | `78eb856` (T154 ProfileEmptyState; 255) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 9 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 58 | 0 | 0 | `8fc1087` (T058 RecoverySessionModal — first Compose UI) |
| lap-website (marketing) | 59 | 1 (T067 currency-l10n) | 0 | `bf5abc9` (T069 /pricing SEO meta) |
| datalogger (desktop) | 37 | 1 (T035 backend ingestion) | 0 | `7e2cde5` (T038 v1→v2 bundle shim) |

## This cycle (Cycle #68)

- Verified GREEN: 5 (backend T060, webapp T154, mobile T058, website T069, datalogger T038)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (68 cycles)

- Total reviewed: 263 · Accepted+tagged: 259 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 68 notables — THIRD ORM MODEL + FIRST MOBILE UI COMPOSABLE + DATALOGGER FLAKE CAUGHT BY BISECT

- **Backend T060 Session ORM + migration** — 3rd model in the async stack. Completes the c65-c68 data layer core: User (T058) + DriverProfile (T059, FK User) + Session (T060, FK DriverProfile). `infra/orm.py` +23 + alembic migration 42 + tests 81. Full matrix: ruff clean, mypy 7 files, pytest 28/28 (+2).
- **Mobile T058 RecoverySessionModal Compose composable** — **first UI surface in sprint-mobile**. Launch-time AlertDialog rendering reconciler output (T055/T057), per-row Finalize/Discard + "Later" dismiss. Stateless — caller owns list and callbacks. T059 will wire the actual Finalize-from-journal path. Reconcilers + Room + UI modal now vertically integrated. 5 consecutive clean mobile accepts (c63/64/65/67/68).
- **Webapp T154 ProfileEmptyState** — 255 tests (+5). Empty branch when T138 data hook returns null. Completes profile UI state machine: Layout + Skeleton + Error + Empty = 4 branches.
- **Website T069 /pricing SEO meta** — 234 tests (+2). Before: "Pricing — LAP". After: keyword "sim racing coaching price" in title + meta + og/twitter. 36-line diff, mostly BaseLayout prop threading.
- **Datalogger T038 v1→v2 bundle shim (reprocess path)** — 218 lines (bundle_v1_compat.py 112 + test 106). Own tests 6/6 pass. Full suite 1478 passed (+6), 19 pre-existing failures stable.
  - **Phase-1 bisect caught a flake**: initial run reported 20 failed / 1477 passed (+1 failure over baseline). Checkout parent a146064 (T037), same 19 known failures only. Re-ran HEAD → 19 failures again. The extra failure was transient (likely overlay_browser timing). Per systematic-debugging: flakes that don't reproduce on re-run are not revert triggers. Green after bisect.
- Schemas idle 9 cycles.
- Disk 86% stable 44 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22); occasional +1 flake in overlay tests (non-deterministic).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function currency injection.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 21:10 UTC.
