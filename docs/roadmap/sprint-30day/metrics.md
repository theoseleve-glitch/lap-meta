# Sprint Metrics — live snapshot

## Last updated: 2026-04-26T15:25Z (Cycle #134 — 5 accepts + 1 revert + 1 cross-repo cascade hold)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | `[ ]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 117 | 4 | 2 (T013, **T104 new**) | 0 | 117 | `f005d57` (T122 SessionRecord persistence) |
| lap-webapp | 116 | 0 | 1 (**T233 new**) | 0 | 123 | `612b18f` (revert T233) |
| lap-schemas | — | 0 | — | 0 | — | `cab48ad` (revert T104) |
| lap-mobile-android | 165 | 0 | 0 | 0 | 75 | `fda018b` (T168 force-kill resume) |
| lap-website (marketing) | 110 | 0 | 0 | 0 | 110 | `bc6465a` (T136 pillar 1 §6) |
| datalogger (desktop) | 128 | 2 | 0 | 0 | 110 | `98104d2` (T129 streamer toggle) |

## Cumulative (133 cycles)

- Total reviewed: ~672 (+364 this cycle, post-resume)
- Accepted+tagged this cycle: 364 (354 sprint + 10 already-pushed prior to cycle)
- Reverted this cycle: **2** (lap-webapp T233 next/font spread, lap-schemas T104 missing test update)
- Reverted total: **5** (1.0% revert rate over 504 sprint reviews)
- Pause triggers: 0 active (c81 resolved at user RESUME 2026-04-26T13:00Z)
- INFRA_FLAG this cycle: 1 (datalogger pyproject missing ruff/mypy/pytest dev extras → 145 ruff + 425 mypy latent errors revealed; not new drift, latent-since-c1)

## Cycle 133 notables — RESUME + 364-COMMIT BACKLOG CLEARED + 2 NEW REVERTS

- **Pause lifted at 2026-04-26T13:00Z** by user after a two-layer ADR-005 audit: ORM (lap-backend) found 2 missing FKs fixed at T112 (`a831422`); Pydantic (lap-schemas) audit found 0 CRITICAL + 7 MINOR (full report `loop-report-c50-consumer-drift.md`); ADR-005 amended with 3 missing nested-type subsections (SessionContext, CohortDef, TargetEvent).
- **lap-backend** — 64 sprint commits T071-T122 + T112 manual fix. 401 pytest pass, ruff/mypy clean, app.main importable. Includes T112 missing-FK fix + T117 sample stream + T118 sector splits + T119 metric extraction + T120 quality scorer + T121 timestamp alignment + T122 SessionRecord persistence.
- **lap-webapp REVERT T233** — 39 sprint commits accepted; **T233 "font subsetting" reverted in `612b18f`** because `pnpm build` failed with "Unexpected spread" in next/font/google macros. Sprint loop's local verify (typecheck + lint + test) didn't catch it because the spread constraint only fires during `next build`. T234 (200KB JS budget) preserved — separate file. 595 tests pass post-revert. Block H largely landed: T217 BillingPage, T220 TrialExpiryBanner, T221 TrialHardGate, T222 Settings shell, T229 Sentry+PostHog, T230 ErrorBoundary, T231 LCP CI, T232 image optim, T234 JS budget.
- **lap-schemas REVERT T104** — 6 schema commits accepted (T098-T103); **T104 "expand SessionIngestAccepted" reverted in `cab48ad`** because adding 3 required fields (`session_id`, `ingest_job_id`, `status_stream_url`) without updating `tests/test_session_ingest.py` left pytest red. T104 marked NEEDS_REWORK in sprint-backend.md (the parent backend task this schema commit supports).
- **lap-mobile-android** — 108 sprint commits T069-T167. Gradle matrix all green (detekt + ktlintCheck + assembleDebug + testDebugUnitTest). T168 force-kill relaunch resume scenario locks attempt-count carry-over.
- **lap-website** — 53 sprint commits T091-T136. 707 tests pass + 18-page build green. Pillar content + pricing journey + e2e.
- **datalogger** — 94 sprint commits, 19 stable test baseline (2287 pass + 1 skip), INFRA_FLAG: dev-extras absent in pyproject (ruff/mypy/pytest not installed by `uv sync`). Latent ruff (145) and mypy (425) errors revealed but not attributable to specific cycle-133 commit (existed pre-c81). Recommend: add `[project.optional-dependencies.dev]` block to datalogger pyproject + re-evaluate ruff/mypy state after sprint loops can self-verify.

## Review loop state after c133

- **Loop is ACTIVE.** Next cron fire processes any new mid-cycle commits (sprint loops fired during this cycle's verification — backend, schemas, website, datalogger HEADs advanced during pytest runs).
- Mid-cycle HEAD drift this cycle: backend `f005d57→e16cfa0`, schemas `cab48ad→6b15072`, website `bc6465a→9cabdfa`, datalogger `98104d2→9f450ab`. Webapp + mobile stayed at the verified HEAD.

## Current issues

- **NEW**: webapp T233 NEEDS_REWORK (next/font spread).
- **NEW**: backend T104 (schemas-side) NEEDS_REWORK (test not updated with required fields).
- **NEW**: datalogger latent ruff (145) + mypy (425) errors — root cause: dev tools not in pyproject.
- Datalogger 19 stable failures (overlay_browser/overlay_window_manager/sync_queue) + occasional 20th flake.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Backend T013 NEEDS_REWORK persistent (env schema ruff/SIM300).
- Backend T018/T019 BLOCKED on docker.
- Step 10 daily-email deferred.

## Cron: ACTIVE (15-min interval). Next fire processes mid-cycle commits.

## Cycle 134 delta

- backend: T123 verified red at e16cfa0 (cross-repo cascade from c133 schemas T104 revert; 31 tests fail). NOT pushed. Origin held at f005d57 (also red against current schemas master). T104 sprint marker strengthened in sprint-backend.md L140.
- webapp: T233 reworked at e0f6494 (sprint loop used inline literals per c133 hint). 602 tests + build green. Tagged + pushed.
- schemas: T104 reapplied at 39e3b7c with same test bug; reverted in dc6cad2. T123 (6b15072 SessionDetail) tagged + pushed.
- mobile: T169 (23ee7ab BackoffSchedule retry) tagged + pushed.
- website: T137 + T138 (pillar 1 cross-links) tagged + pushed. 722 tests.
- datalogger: idle.
- Cumulative reverts: **6** (1.1% over 134 cycles).
- **Cross-repo cascade** active and blocking: lap-backend ingest path will stay red until lap-schemas T104 re-lands with proper test + lap-backend pytest verified green in same iteration.
