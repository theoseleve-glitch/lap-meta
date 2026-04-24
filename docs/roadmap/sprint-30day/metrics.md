# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T20:10Z (Cycle #65)

## Per-repo status

| Repo | `[x]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|
| lap-backend | 55 | 1 (T013) | `76d6046` (T058 User ORM + migration — first ORM model) |
| lap-webapp | 71 | 0 | `cc32108` (T152 ProfileSkeleton; 244) |
| lap-schemas (subset) | 35 | 0 | `0dda9cb` (idle 5 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 56 | 0 | `29fc1ee` (T056 OrphanTempFileReconciler) |
| lap-website (marketing) | 57 | 0 | `f4808c3` (T066 /pricing contact-sales mailto) |
| datalogger (desktop) | 35 | 0 | `f0f2855` (T036 CSV fallback integration test) |

## This cycle (Cycle #65)

- Verified GREEN: 5 (backend T058, webapp T152, mobile T056, website T066, datalogger T036)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (65 cycles)

- Total reviewed: 253 · Accepted+tagged: 249 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 65 notables — FIRST BACKEND ORM MODEL + MOBILE RECONCILER PAIR + DESKTOP T035 BLOCKED

- **Backend T058 User ORM model + alembic migration** — first ORM entity in the async stack assembled across c63-c65. `infra/orm.py` (27) + auto-generated migration `a486bfbde9e9_t058_add_users_table.py` (44) + tests/test_user_model.py (69) + alembic/env.py (+3) + pyproject (+1). Full matrix: ruff clean, mypy Success 7 files, pytest 24/24 (+2). Canonical ADR-005 user columns: id UUIDv7, clerk_user_id, email, created_at, subscription_status, is_admin.
- **Mobile T056 OrphanTempFileReconciler** — pair with c64 T055 JournalReconciler. One-way disk→DB lookup; T057 will cover the reverse. Filesystem abstracted behind TempFileInventory so unit tests drive 4 cases without disk. 3 consecutive clean mobile accepts (c63+c64+c65) — detekt pre-push gap effectively closed.
- **Desktop T036 CSV fallback integration test** — sprint-desktop skipped T035 by correctly marking it `[BLOCKED: backend ingestion endpoint not live — cannot validate manifest server-side]` and moved to T036. Own test file 31/31 (+1 file, +93 lines). Self-aware sprint-loop cross-repo gating. Full suite: 1470 passed (+2), 19 pre-existing failures (stable tech-debt).
- **Webapp T152 ProfileSkeleton** — 244 tests (+5 from 239). 5 unit tests + 1 Storybook variant. TDD red-green. ProfileSkeleton matches ProfileLayout grid so swapping skeleton↔content doesn't shift.
- **Website T066 /pricing contact-sales mailto** — 232 tests (+1). Pragmatic choice: mailto over Calendly (no OAuth, works everywhere). Subject-line pre-fill → single triageable inbound thread.
- **Datalogger env workaround** — c64's `uv pip install pydantic pyyaml uuid6` prepended to the verification matrix worked cleanly. 19 pre-existing failures stable.
- Schemas idle 5 cycles (35/35 parity stable).
- Disk 86% stable 41 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras — review loop pre-installs them each cycle until sprint-desktop fixes.
- Desktop T035 [BLOCKED]: needs backend ingestion endpoint (expected post-T080 routers).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.
- **Mobile detekt pre-push gap: DROPPED** from watchlist. c63+c64+c65 = 3 consecutive clean accepts with proactive named constants. Pattern confirmed closed.

## Cron: next 20:25 UTC.
