# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T02:50Z (Cycle #18)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 17 | 223 | 0 | 1 (T013) | 0 | `7b64848` (**2 idle cycles**) |
| lap-webapp | 16 | 224 | 3 (T010, T019, T020) | 0 | 0 (T017+T018 reclassified to SCAFFOLD_BULK) | `d9a0343` (T034 ApiError) |
| lap-schemas | 2 | 238 | 0 | 0 | 0 | `fcc4848` (T022 UUID7) |
| lap-mobile-android | 21 | 219 | 0 | 0 | 0 | `d4b1b78` (T021 kotlinx-serialization) |
| lap-website | 21 | 5 BLOCKED | 5 | 0 | 1 (T017 Lighthouse — may still qualify for ADR-018 reclassification, user decision) | `0c170b3` (T026 secondary CTA) |
| datalogger | 2 | 238 | 0 | 0 | 0 | `eb97496` (**14th quiet cycle**) |

## This cycle (Cycle #18)

- Verified GREEN: 4 (webapp T034, schemas T022 first matrix-running cycle, mobile T021, website T026)
- Backend idle 2nd cycle.
- Reverted: 0 | SCOPE_FLAG: 0 new
- **ADR-018 Dec 2 expanded** by user: webapp T017 + T018 reclassified SCOPE_FLAG → SCAFFOLD_BULK (Tier B test-harness 8000, Tier C Storybook 15000).

### Schemas matrix actually ran this cycle
T022 added pyproject.toml + src/lap_schemas/v1/ids.py + tests/test_ids.py. Matrix invocation:
- Path quirk: my script ran `uv run pytest python/tests/` from inside `python/` dir, which resolved to `python/python/tests/` and failed with "file not found". **Script path bug**, not code defect. Re-ran with `cd python && uv run pytest -q` (uses testpaths config) → **3 passed in 0.14s**. TRUE VERDICT: GREEN.
- ruff/mypy/codegen still silent-skipped per ADR-017 (no [tool.ruff]/[tool.mypy]/Makefile codegen-check yet).

## Cumulative (18 cycles)

- Total reviewed: 76 · Accepted+tagged: 74 (1 INFRA_FLAG c4)
- Reverted: 1 (T013)
- **Active SCOPE_FLAGs: 1** (down from 3 — website T017 only; webapp T017+T018 now SCAFFOLD_BULK)
- Pause triggers: 0

## Cycle 18 notables

- **Webapp jumped T019→T034** due to T010-T033 being schema-dependent BLOCKED or schema-migration tasks. T034 ApiError is a self-contained typed-error work. Sprint loop correctly finding independent tasks.
- Schemas matrix started running with T022 (first applicable pytest — 3/3 green).
- Backend idle 2nd consecutive cycle (no new sprint commits past T020 Makefile).
- Datalogger 14 quiet cycles.

## Current issues

- Backend 2-cycle idle (not stalled historically; may be finishing something).
- Datalogger still appears stopped.
- Backend T013 NEEDS_REWORK persistent.
- Runbook-matrix path invocation for schemas needs cleanup: my bash script had a `cd python && pytest python/tests/` double-path bug. Future cycles should `cd python && pytest` (relies on testpaths config) OR run from repo root with `pytest python/tests/`.

## Cron: next 03:07 UTC.
