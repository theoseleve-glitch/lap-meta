# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T19:10Z (Cycle #61)

## Per-repo status

| Repo | `[x]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|
| lap-backend | 52 | 1 (T013) | `772dc3d` (idle 13 cycles) |
| lap-webapp | 68 | 0 | `a9c6043` (T149 weaknessDetailPath helper; 232) |
| lap-schemas (subset) | 35 | 0 | `0dda9cb` (T055 calver versioning docs; pytest 74) |
| lap-mobile-android | 53 | 0 | `a4c1bd2` (T053 **rework** — forEach, not spread) |
| lap-website (marketing) | 54 | 0 | `fff0d89` (T063 /pricing plan-CTA e2e wiring) |
| datalogger (desktop) | 32 | 0 | `b248656` (T032 SensorConfigSnapshot persistence contract) |

## This cycle (Cycle #61)

- Verified GREEN: 5 (webapp T149, schemas T055, mobile T053-rework, website T063, datalogger T032)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **T053 recovery event**: sprint-mobile re-picked T053 after c60 revert, replaced `*migrations.toTypedArray()` with `migrations.forEach { addMigrations(it) }` — detekt now passes. Mobile NR back to 0.

## Cumulative (61 cycles)

- Total reviewed: 237 · Accepted+tagged: 234 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 2 · Pause triggers: 0
- **Schemas subset at 35/35 (100%)** — ADR-006/007 object surface FULL Python parity

## Cycle 61 notables — T053 REWORK LANDED

- **Sprint-loop self-correction cycle completed in exactly 1 fire** (c60 revert → c61 rework): sprint-mobile read the `[NEEDS_REWORK]` note + reverted-in sha, implemented the rewrite per recommendation (`forEach` not spread), re-submitted. Full gradle matrix BUILD SUCCESSFUL (163 tasks). Review loop's NEEDS_REWORK annotation carried sufficient diagnostic context for single-round recovery.
- **Matrix vs working-tree confusion re-validated**: Initial mobile T053-rework matrix failed on `JournalWriterTest.kt:152:84` ktlint violation. Investigation showed JournalWriterTest.kt is UNTRACKED WIP from sprint-mobile's T054 preparation, not part of T053 commit. Stashed WIP → matrix passed cleanly. ACCEPT. Same pattern as cycle 22/24 datalogger. Lesson reinforced: when matrix fails, verify file belongs to reviewed commit before reverting.
- **Schemas subset milestone**: T055 pushes ADR-006/007 count to 35/35 (100%). Python side of schema contracts FULLY landed. Kotlin side still catching up; Swift + TS generated targets.
- Webapp T149 weaknessDetailPath helper (routes.ts +7 + test +24). 232 tests (+5).
- Website T063 /pricing plan-CTA e2e wiring verification (28-line Playwright extension). 217 unit tests.
- Datalogger T032 SensorConfigSnapshot persistence contract (+66 test lines). 26/26 tests (+3).
- Schemas T055 calver versioning docs (94-line VERSIONING.md + README update).
- Disk 86% stable 38 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 19:15 UTC.
