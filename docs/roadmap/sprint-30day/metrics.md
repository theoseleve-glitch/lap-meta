# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T20:40Z (Cycle #67)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 56 | 2 (T018/T019 docker) | 1 (T013) | `31fb7b4` (T059 DriverProfile ORM) |
| lap-webapp | 72 | 0 | 0 | `fc7d610` (T153 ProfileError + retry; 250) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 8 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 57 | 0 | 0 | `03d180f` (T057 CrashedSessionReconciler) |
| lap-website (marketing) | 58 | 1 (T067 currency-l10n defer) | 0 | `3549ebd` (T068 /pricing a11y + responsive) |
| datalogger (desktop) | 36 | 1 (T035 backend ingestion) | 0 | `a146064` (T037 interrupted finalize) |

## This cycle (Cycle #67)

- Verified GREEN: 5 (backend T059, webapp T153, mobile T057, website T068, datalogger T037)
- Reverted: 0 | SCOPE_FLAG: 0 new | BLOCKED (new, self-reported by sprint loops): 1 (website T067)

## Cumulative (67 cycles)

- Total reviewed: 258 · Accepted+tagged: 254 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 67 notables — SECOND ORM MODEL + 2ND SELF-AWARE BLOCK

- **Backend T059 DriverProfile ORM + migration** — pairs with c65 T058 User. `infra/orm.py` +18 lines (DriverProfile class), new migration `3d41041193b9_t059_add_driver_profiles.py` 42, tests 79. Full matrix: ruff clean, mypy 7 files, pytest 26/26 (+2). Foreign key to User — first relational shape in the schema.
- **Webapp T153 ProfileError state with retry** — 250 tests (+6). Error boundary with retry CTA. UI error/loading trifecta now complete: ProfileSkeleton (T152) + ProfileError (T153) + ProfileLayout (T146).
- **Mobile T057 CrashedSessionReconciler (recording/finalizing → recovery)** — 179 lines. Direction opposite T056 (DB row without file, not file without DB row). State literal hoisting pattern consistent with c64/c65 — detekt clean from start. Commit body references T075 SessionState typed enum as the future consolidation. 4 consecutive clean mobile accepts (c63+c64+c65+c67, c66 idle).
- **Website T068 /pricing a11y + responsive clean** — 69 lines. Extends T038/T053 e2e gates to cover /pricing with WCAG 2.1 A/AA axe scan + mobile-layout spec. 232 tests (no new vitest cases — a11y lives in Playwright e2e which isn't run inline).
- **Website T067 SELF-BLOCKED** (currency localization) — sprint-marketing wrote a substantial `[BLOCKED: ...]` reason citing 4 failure modes (static build can't geo-detect, Cloudflare OAuth gate, JS bundle budget, USD maintenance) and the unblock path (T008 Cloudflare Pages + edge function injecting `request.cf.country`). Doctrine-aware reasoning (§8 EUR canonical, §3 EU personas). **2nd self-aware block** this sprint (desktop T035 in c65 was the 1st).
- **Datalogger T037 interrupted finalize integration** — extends test_finalizer_accepts_manifest.py (+77 lines / 33 cases on that file, +2 from c65). Full suite: 1472 passed (+2), 19 pre-existing failures stable.
- Schemas idle 8 cycles.
- Disk 86% stable 43 cycles.

## Current issues (unchanged from c65-c66)

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function currency injection.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 20:55 UTC.
