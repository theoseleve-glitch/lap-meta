# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T09:55Z (Cycle #24)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend | 18 | 213 | 2 | 1 (T013) | 0 | `7b64848` (**8 idle cycles** — schemas-phase natural) |
| lap-webapp | 40 | 200 | 0 | 0 | 0 | `2df91cc` (T088 WeaknessEpisodeCard) |
| lap-schemas (T021–T055 tracked in sprint-backend) | 7 | — | 0 | 0 | 0 | `1e20418` (T027 SessionManifest → pytest 18; + feat(kotlin) scaffold) |
| lap-mobile-android | 26 | 214 | 0 | 0 | 0 | `291c7f3` (T026 include :schemas gradle module) |
| lap-website (sprint-marketing) | 26 | 194 | 0 | 0 | 1 (T017 inline) | `21b7ee1` (T031 "built for serious sim racers" section) |
| datalogger (sprint-desktop) | 4 | 236 | 0 | 0 | 0 | `fa8ec3e` (T004 DashboardLiveProcessor — own tests 6/6) |

## This cycle (Cycle #24)

- Verified GREEN: 5 (webapp T088, schemas T027, mobile T026, website T031, datalogger T004)
- Reverted: 0 | SCOPE_FLAG: 0 new
- Rode-along non-reviewable: 1 (lap-schemas `1e20418` feat(kotlin): scaffold — not `sprint(` prefix so out of review scope per Step 1.4, but HEAD-matrix green covers it)

## Cumulative (24 cycles)

- Total reviewed: 97 · Accepted+tagged: 95 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 24 notables

- **Cross-repo wiring landed**: lap-schemas `1e20418 feat(kotlin):` scaffold + lap-mobile-android T026 `include(":schemas")` both land this cycle. Mobile Gradle build BUILD SUCCESSFUL with the new `:schemas` subproject included → **contract-drift is logically-consistent at HEAD** even though codegen hasn't populated yet.
- **Datalogger tech-debt FLAG expanded**: cycle 22 flagged "4 pre-existing sync_queue failures". Cycle 24's clean-tree full-suite bisect at T003 vs T004 reveals **15 pre-existing failures, not 4** — the earlier count missed `test_desktop_workspaces` (2), `test_ghost_widget` (1), `test_overlay_browser_frontend` (8) because cycle 22's clean test used a file-list invocation that silently swallowed collection failures. Same 15 failures at both T003 (f3c1cc7) and T004 (fa8ec3e) clean trees → T004 is innocent.
- Cycle 22 narrative self-correction: "overlay tests PASS cleanly" was wrong; they fail clean at T003 too.
- Disk usage: **86%** (unchanged — stable 3 cycles).
- Schemas pytest climbed to 18 (+3 from T027).
- Webapp: 4 test files / 22 tests pass (+10 from T088's `WeaknessEpisodeCard.test.tsx` 70-line spec).
- Website: 13 test files / 82 tests pass (+7 from T031's "built for serious sim racers" section).

## Current issues

- **Datalogger pre-existing-failures tech-debt (expanded)**: 15 failing tests in test_desktop_workspaces (2), test_ghost_widget (1), test_overlay_browser_frontend (8), test_overlay_window_manager (4). Plus 4 in test_sync_queue.py (from cycle 22). All predate cycle-1 manual integration commit `304c0a9` or are consequences of it. Not blocking per-commit review; needs a dedicated tech-debt sprint pass.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 Dockerfile + docker-compose BLOCKED (docker not installed in Windows sandbox).
- Website T017 SCOPE_FLAG (Lighthouse CI, 2267 lines — cycle 11 alert).
- `ops/.last_daily_sent`=2026-04-23 stale (today=2026-04-24); Step 10 not in user's /loop prompt scope so not fired here — daily summary won't auto-send until user changes prompt or runs manually.

## Cron: next 10:00 UTC (15-min /loop cadence).
