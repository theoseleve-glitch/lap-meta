# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T15:45Z (Cycle #47)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total) | 41 | 196 | 2 | 1 (T013) | 0 | `7b64848` (**31 idle cycles**) |
| lap-webapp | 57 | 183 | 0 | 0 | 0 | `ed63d1c` (T137 profile route shell) |
| lap-schemas (subset) | 25 | — | 0 | 0 | 0 | `8cac625` (T044 pip install-e + v1 re-exports; pytest 69) |
| lap-mobile-android | 43 | 197 | 0 | 0 | 0 | `77b661e` (T043 SessionJournalEntity + MIGRATION_1_2) |
| lap-website (marketing) | 43 | 177 | 0 | 0 | 1 (T017 inline) | `2343382` (T049 /how-it-works honesty section) |
| datalogger (desktop) | 21 | 219 | 0 | 0 | 0 | `ff57d65` (T021 lap_schemas.v1 as dep) |

## This cycle (Cycle #47)

- Verified GREEN: 5 (webapp T137, schemas T044 + ride-along 8cac625 re-exports, mobile T043, website T049, datalogger T021)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **First cross-repo Python dep**: datalogger T021 wires `lap_schemas.v1` via pip install-e enabled by schemas T044 + v1 re-exports

## Cumulative (47 cycles)

- Total reviewed: 182 · Accepted+tagged: 180 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 47 notables

- **Cross-repo Python dependency landing** (first time): datalogger → lap-schemas.v1 runtime binding. Enabled by two coordinated commits: schemas T044 (`make lap-schemas pip install -e able` — editable install support + `v1` re-export namespace) + datalogger T021 (adds `lap-schemas` to pyproject.toml + requirements.txt + contract test). Parallel to the mobile-kotlin side which has been consuming :schemas via gradle since cycle 24.
- **First Room Migration lands**: mobile T043 adds SessionJournalEntity + manual `MIGRATION_1_2` from Room v1 → v2. Includes `MigrationsTest.kt` (18 lines) that validates migration logic. FK cascade to sessions.id. Full gradle matrix green with Room KSP re-exercised.
- Webapp T137 profile route shell (17 + 15 lines) — 141 tests (+2). Second app route after /timeline.
- Website T049 "honesty section" (today vs Year 2) — 107-line HowItWorksHonesty.astro; 168 tests (+7). Meta-narrative addressing roadmap transparency.
- **Schemas ride-along commit** `8cac625 schemas(v1): re-export SessionManifest, LapRecord, TelemetrySample` — NOT `sprint(` prefix so non-reviewable per Step 1.4, but pushable via fast-forward (Hard NEVER #2 only protects hotfix/manual/meta/revert). Same pattern as cycle 24's `feat(kotlin):` Kotlin scaffold.
- Backend 31 idle, webapp 0 idle, schemas 0 idle, mobile 0 idle, website 0 idle, datalogger 0 idle — **every repo active this cycle except backend** (which is structurally quiet).
- Disk 86% stable 24 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 15:50 UTC.
