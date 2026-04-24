# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T21:55Z (Cycle #72)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 60 | 2 (T018/T019) | 1 (T013) | `40eeed0` (T063 Lap ORM — 6th model) |
| lap-webapp | 75 | 0 | 0 | `ebaef85` (T156 ProfilePage Storybook 3 states; 263) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 13 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 61 | 0 | 0 | `d2f4e52` (T061 LocationCaptureService 10Hz — first hardware) |
| lap-website (marketing) | 62 | 1 (T067) | 0 | `002d38f` (T073 /demo video format lock) |
| datalogger (desktop) | 39 | 1 (T035) | 0 | `c59dc8e` (T040 canonical SessionManifest adapter) |

## This cycle (Cycle #72)

- Verified GREEN: 5 (backend T063, webapp T156, mobile T061 mid-cycle, website T073, datalogger T040)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (72 cycles)

- Total reviewed: 275 · Accepted+tagged: 271 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 72 notables — SIXTH ORM MODEL + FIRST MOBILE HARDWARE SURFACE + WEBAPP STORYBOOK

- **Backend T063 Lap ORM + migration** — **6th model**, biggest backend test file yet (144 lines of tests). 37/37 (+4). FK to Session. `infra/orm.py` +20 Lap.
- **Mobile T061 LocationCaptureService 10Hz FusedLocationProvider** — **first hardware sensor integration** on mobile. Clean layer separation: LocationDataSource (interface, 13) + FusedLocationDataSource (impl 67) + LocationCaptureConfig (23) + LocationAccuracyMode (enum 14) + LocationCaptureService (orchestrator 19). 341 lines total. 8 consecutive clean mobile accepts.
- **Webapp T156 ProfilePage Storybook stories** — full-page surface at Profile/ProfilePage with 3 data stories (Loaded, Loading, Empty). 263 tests (+8 from 255). Completes the profile data-state coverage: Layout + Skeleton + Error + Empty + all three composed into full-page stories.
- **Website T073 demo format — video (default)** — 246 tests (+7). Locks walkthrough format decision, reserves 16:9 video footprint so T074 iframe is zero-CLS drop-in. Block E progressing.
- **Datalogger T040 canonical SessionManifest adapter** — `write_bundle_v2_from_manifest` replaces inline kwargs-hand-wiring in finalizer. 246 lines refactor. Full suite: 1479 passed (+2), 19 pre-existing stable.
- Schemas idle 13 cycles.
- Disk 86% stable 48 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function currency injection.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 22:10 UTC.
