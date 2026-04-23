# Sprint Metrics — live snapshot

## Last updated: 2026-04-23T23:20Z (Cycle #11)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 12 | 228 | 0 | **1** (T013 reverted) | 0 | `3312b5e` (revert of T013 on top) |
| lap-webapp | 11 | 229 | 0 | 0 | 0 | `52e1cce` (3 consecutive idle cycles) |
| lap-schemas | 0 | — | 0 | 0 | 0 | `a50d39a` |
| lap-mobile-android | 14 | 226 | 0 | 0 | 0 | `8577f35` (T014 R8 rules + minified release) |
| lap-website | 14 | 3 BLOCKED | 3 | 0 | **1** (T017 SCOPE_FLAG) | `317d62c` (T017 Lighthouse CI) |
| datalogger | 2 | 238 | 0 | 0 | 0 | `eb97496` (7th quiet cycle) |

## This cycle (Cycle #11)

- Verified GREEN: 2 (mobile T014, website T017)
- **REVERTED: 1** (backend T013 — first revert of the loop's history)
- **SCOPE_FLAG: 1** (website T017 = 2267 insertions > 1500 non-scaffold threshold)
- scope-blowup alert: dedup-suppressed for 2026-04-23 (already fired cycle 3/4)

### Backend T013 revert details

`tests/test_env_example.py` had two ruff violations:
- `E501 Line too long (89 > 88)` line 5: the `REQUIRED_KEYS = frozenset({...})` line
- `SIM300 Yoda condition` line 23: `REQUIRED_KEYS <= _keys_in_env_example()` should be `_keys_in_env_example() >= REQUIRED_KEYS`

Both are in code the sprint loop just added. Sprint loop's own acceptance said "pre-commit green" but evidently didn't run ruff with the same config the review loop uses. Original T013 committed at `3ada05d` (pushed), reverted in `3312b5e` (pushed). sprint-backend.md T013 → `[NEEDS_REWORK]` with reason. Next backend sprint iteration re-picks T013.

### Website T017 SCOPE_FLAG

T017 landed 5 files / 2267 insertions. Lighthouse CI config + workflow. Above 1500 non-scaffold threshold. SCOPE_FLAG annotation on sprint-marketing.md T017 line. Push stands (flag is not a revert). User decides at next weekly review whether to split.

## Cumulative (11 cycles)

- Total reviewed: 50 (c11: backend T013 REVERTED, mobile T014 + website T017 accepted; backend baseline didn't advance due to revert)
- Accepted+tagged: 48 (1 INFRA_FLAG c4)
- **Reverted: 1** (first ever — cycle 11 backend T013)
- NEEDS_REWORK events: 3 cumulative (c4×2 cleared c5; c11×1 active)
- SCOPE_FLAG active: 1 (website T017)
- Pause triggers: 0 (1 revert is well below the >3 threshold)

## Cycle 11 notables

- **First mandatory revert of loop history**. Previously 10 cycles without a revert; T013 hit the matrix.
- Website T017 very large (2267 lines) — Lighthouse CI with lhci config + ubuntu workflow includes substantial generated config.
- Webapp 3 idle cycles / Datalogger 7 quiet cycles (both likely stalled terminals).

## Current issues

- **Backend sprint loop: `ruff check .` gap** — sprint loop's local acceptance doesn't match review-loop config. User may want to add ruff to sprint-loop's pre-commit hook OR update sprint-backend.md T003 acceptance to explicitly run `ruff check .` before commit.
- lap-website T008-T010 BLOCKED on Cloudflare OAuth (carried).
- Webapp 3 idle cycles, Datalogger 7 quiet cycles.

## Cron: next fire 23:37 UTC.
