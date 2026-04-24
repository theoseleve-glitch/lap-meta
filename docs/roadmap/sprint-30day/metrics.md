# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T16:10Z (Cycle #49)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 43 | 194 | 2 | 1 (T013) | 0 | `772dc3d` (idle 1 cycle) |
| lap-webapp | 59 | 181 | 0 | 0 | 0 | `cb5285e` (idle 1 cycle) |
| lap-schemas (subset) | 26 | — | 0 | 0 | 0 | `4f84bc8` (T046 TS codegen scaffold; pytest 69) |
| lap-mobile-android | 45 | 195 | 0 | 0 | 0 | `233e538` (T045 InsightCacheEntity + MIGRATION_3_4) |
| lap-website (marketing) | 45 | 175 | 0 | 0 | 1 (T017 inline) | `ca94b17` (T052 final CTA + T053 a11y responsive clean) |
| datalogger (desktop) | 22 | 218 | 0 | 0 | 0 | `b78fdb5` (idle 1 cycle) |

## This cycle (Cycle #49)

- Verified GREEN: 4 (schemas T046, mobile T045, website T052 + T053)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (49 cycles)

- Total reviewed: 190 · Accepted+tagged: 188 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 49 notables

- **TS codegen side of schemas activated**: T046 scaffolds `typescript/package.json` + `openapi-typescript@7` + 384-line package-lock.json. Sits alongside Python + Kotlin subdirs. When T043's `generate_openapi.py` runs, its output feeds this TS codegen pipeline → webapp generated types. Three-language schema layer now all scaffolded.
- **Mobile T045 third Room migration** (v3→v4): InsightCacheEntity for offline caching of backend-authored CoachingInsights (dashboard renders with no network). Payload is kotlinx-serialized JSON via LapSchemasJson. Full gradle matrix BUILD SUCCESSFUL.
- Website **T052 final CTA wired** + **T053 a11y + responsive clean** — both captured, tests 169/169 (+1 from T049's 168), build 4 pages. e2e a11y spec updated (+41/-8), mobile-layout spec extended (+64/-0).
- Schemas subset Python stays 25; Kotlin side grew on mobile (not counted in subset). TS side now scaffolded.
- Backend 1 idle, webapp 1 idle, datalogger 1 idle after yesterday's burst.
- Disk 86% stable 26 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 16:15 UTC.
