# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T19:55Z (Cycle #64)

## Per-repo status

| Repo | `[x]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|
| lap-backend | 54 | 1 (T013) | `10b3e92` (T057 Alembic async init — 2nd backend commit in sequence) |
| lap-webapp | 70 | 0 | `3a094ab` (T151 targetEventPickerPath; 239) |
| lap-schemas (subset) | 35 | 0 | `0dda9cb` (idle 3 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 55 | 0 | `d3f131f` (T055 JournalReconciler — proactive named constants) |
| lap-website (marketing) | 56 | 0 | `fb04a89` (T065 /refund-policy + /pricing link) |
| datalogger (desktop) | 34 | 0 | `3fdc300` (T034 canonical_time helper ADR-007) |

## This cycle (Cycle #64)

- Verified GREEN: 5 (backend T057, webapp T151, mobile T055, website T065, datalogger T034)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (64 cycles)

- Total reviewed: 248 · Accepted+tagged: 244 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 64 notables — BACKEND API INFRA PAIR + MOBILE LEARNING CONFIRMED

- **Backend T057 Alembic async init** — 2nd consecutive backend commit after the c63 phase-transition. alembic.ini (149) + alembic/env.py (96) + script template (28) + test_alembic.py (28) + pyproject dep + uv.lock delta. Full matrix: ruff clean, mypy "Success: no issues found in 7 source files" (+1 from c63), pytest 22/22 (+2). Backend is now stood up for schema migrations — the pairing T056 engine + T057 migrations is the canonical FastAPI-async stack foundation.
- **Mobile T055 JournalReconciler** — **proactive learning from c62 MagicNumber revert**. Commit body explicitly references: "both named constants satisfy detekt MagicNumber from the start. All test literals hoisted to file-scope private const vals too." Sprint-mobile has internalized the detekt rule the review loop kept tripping. Extracted FakeJournalDao into its own file to share with JournalWriterTest. Full gradle matrix green on stashed tree (WIP pollution: `.claude/` only).
- **Webapp T151 targetEventPickerPath** — routes.ts +4 + test +11. 239 tests (+2). Wires Block G ProfileLayout ReadinessGauge click-target to /profile/readiness via helper, not string template.
- **Website T065 /refund-policy** — 186-line diff: new page + nav link from /pricing. 231 tests (+7). Tight copy covering EU 14-day + grandfathered waitlist lock.
- **Datalogger T034 canonical_time** — ADR-007 timestamp shaping (`t_source_ns` + `t_canonical_ns`). Own-file 6/6 tests pass. Full-suite reports 19 pre-existing failures (tech-debt since c22, reproduces at parent T033 per Phase-1 investigation) + missing transitive deps (pydantic/pyyaml/uuid6 were pruned from .venv by `uv sync` — review-loop infra issue, not code).
- Schemas idle 3 cycles (35/35 parity stable).
- Disk 86% stable 40 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger transitive deps (pydantic/pyyaml/uuid6) get pruned by `uv sync` — pyproject should declare them as dev extras, OR review loop must `uv pip install` them each cycle.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.
- Sprint-mobile detekt pre-push gap: c60+c62 but **c63 + c64 now clean without review-loop intervention** (T054 rework + T055 both proactively use named constants). Trend reversing — pattern may have closed. Drop from watchlist if c65 also clean.

## Cron: next 20:00 UTC.
