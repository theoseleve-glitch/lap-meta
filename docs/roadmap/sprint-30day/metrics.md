# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T12:25Z (Cycle #34)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 32 | 205 | 2 | 1 (T013) | 0 | `7b64848` (**18 idle cycles**) |
| lap-webapp | 47 | 193 | 0 | 0 | 0 | `38433aa` (T118 prescriptionsAcceptedBadge) |
| lap-schemas (subset) | 14 | — | 0 | 0 | 0 | `b6ce2ed` (idle 1 cycle) |
| lap-mobile-android | 33 | 207 | 0 | 0 | 0 | `291c7f3` (idle 10 cycles) |
| lap-website (marketing) | 33 | 187 | 0 | 0 | 1 (T017 inline) | `515a907` (T038 axe a11y + CI e2e job) |
| datalogger (desktop) | 11 | 229 | 0 | 0 | 0 | `cdfd017` (idle 1 cycle) |

## This cycle (Cycle #34)

- Verified GREEN: 2 (webapp T118, website T038)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Workflow-touch: website T038 adds a new `e2e` job to `.github/workflows/ci.yml` — no `workflow_dispatch`/`secrets.*` additions → guardrail condition NOT met → ACCEPT

## Cumulative (34 cycles)

- Total reviewed: 132 · Accepted+tagged: 130 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 34 notables

- **Website T038 adds full a11y gate**: homepage WCAG 2.1 A/AA cleaned (4 component color-contrast fixes: AfterEverySession, DriverProfilePreview, SocialProof), new `tests/e2e/a11y.spec.ts` using `@axe-core/playwright`, new CI e2e job (Playwright chromium) running on ubuntu-latest after `verify`. T034 FinalCta mirror triggered Playwright strict-mode issue in existing `tests/e2e/home.spec.ts` → assertions updated to handle 2 "Start 14-day trial" links. Second CI workflow edit in 3 cycles (T036 label rename, T038 new job). Both accepted under narrow guardrail rule.
- Webapp T118 prescriptionsAcceptedBadge derivation — 76 tests (+7). Pair with T117 newWeaknessesBadge.
- Mobile hits 10 idle cycles (first double-digit) — expected: all mobile work since T025 went into lap-schemas/kotlin/ subproject.
- Disk 86% stable 11 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 12:30 UTC.
