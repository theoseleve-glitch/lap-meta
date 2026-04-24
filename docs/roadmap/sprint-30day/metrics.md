# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T12:55Z (Cycle #36)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 33 | 204 | 2 | 1 (T013) | 0 | `7b64848` (**20 idle cycles**) |
| lap-webapp | 49 | 191 | 0 | 0 | 0 | `1dfa795` (T120 FilterChipGroup primitive) |
| lap-schemas (subset) | 16 | — | 0 | 0 | 0 | `ef37165` (T036 ActionPrescription + T035 Kotlin; pytest 45) |
| lap-mobile-android | 35 | 205 | 0 | 0 | 0 | `291c7f3` (idle 12 cycles) |
| lap-website (marketing) | 35 | 185 | 0 | 0 | 1 (T017 inline) | `d94f7a8` (T040 signup e2e flow) |
| datalogger (desktop) | 13 | 227 | 0 | 0 | 0 | `323fe7f` (T013 pyproject pinning contract) |

## This cycle (Cycle #36)

- Verified GREEN: 5 (webapp T120, schemas T036 Python + T035 Kotlin, website T040, datalogger T013)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (36 cycles)

- Total reviewed: 142 · Accepted+tagged: 140 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 36 notables

- **Backend hits 20-cycle idle milestone** — since T020 Makefile, all backend-scope work (T021+) has been landing in lap-schemas (Python subdir). Expected per ADR.
- **Mobile 12-cycle idle milestone** — all mobile-scope work since T025 androidTest lives in lap-schemas/kotlin/ subproject. Mobile-android repo itself is a passive consumer of `:schemas:build`.
- Schemas Python+Kotlin 8 of 10 recent cycles paired (T036 ActionPrescription 99-line test + T035 SuccessCondition Kotlin 19 + 66). Schemas subset [x]=16 = half of ADR-006/007's 35-object target.
- Webapp T120 FilterChipGroup primitive (48 + 97 lines) — first non-badge, non-entry UI primitive for timeline filtering. 85 tests (+6).
- Website T040 signup e2e flow — pure-add Playwright spec (55 lines). Matches T038 a11y + T039 mobile layout scope.
- Datalogger T013 **contract-test for pyproject pinning** — unique shape: asserts pyproject.toml has 3.12 pin + uv.lock invariants (55 lines, 5 tests). Locks the Python version constraint as tested state. Pure-add (no actual lock file changes).
- Disk 86% stable 13 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 13:00 UTC.
