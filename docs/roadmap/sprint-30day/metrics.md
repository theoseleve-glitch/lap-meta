# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T23:40Z (Cycle #79)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 65 | 2 (T018/T019) | 1 (T013) | `512892a` (T068 TransferLink — 11th model) |
| lap-webapp | 81 | 5 (T157/T158/T161/T162/T164) | 0 | `59453d2` (T169 SkillTrendChart; 292) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 20 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 66 | 0 | 0 | `b100bb8` (T066 LocationSampleValidator plausibility filter) |
| lap-website (marketing) | 67 | 1 (T067) + implicit (T082/T084/T087) | 0 | `38a447c` (T088 /demo SEO meta) |
| datalogger (desktop) | 43 | 1 (T035) | 0 | `864e1c7` (T044 5 MiB chunk telemetry) |

## This cycle (Cycle #79)

- Verified GREEN: 5 (backend T068, webapp T169, mobile T066, website T088, datalogger T044)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Datalogger flake re-observed**: initial run 20 failed/1506 passed, re-run 19 failed/1507 passed. Stable set = 19; one test in overlay_browser/session_coordinator set is non-deterministic. Pattern known since c68.

## Cumulative (79 cycles)

- Total reviewed: 299 · Accepted+tagged: 295 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 79 notables — 11TH ORM + DEEP WEBAPP CHART + MOBILE VALIDATION + DATALOGGER CHUNKING

- **Backend T068 TransferLink ORM + migration** — 11th model. 50/50 (+2). orm.py delta + migration + tests 119 lines. TransferLink is new — likely relates to the coaching-session sharing pattern (share profile, driver X shows session to coach Y).
- **Webapp T169 SkillTrendChart component** — 268 ins (largest webapp diff yet). **+11 tests** (281→292) — largest single-commit test increase in webapp. Commit body mentions "data-session-id on each point marker to pave the way for" (likely T170 interaction wiring).
- **Mobile T066 LocationSampleValidator physical-bounds plausibility filter** — 251 ins. 3 files: LocationFieldViolation (18) + LocationSampleValidator (39) + 194 test lines. **Plausibility filtering** guards against sensor spikes (e.g., GPS jumps to Antarctica). Complements T065 mapper. 13 consecutive clean mobile accepts.
- **Website T088 /demo SEO meta tuning** — 40 ins. Target kw "sim racing telemetry demo" in title + description. 255 tests (+2). T087 implicitly gated (same video-chain).
- **Datalogger T044 chunk telemetry into 5 MiB parts** — 149 ins. Adds `chunk_size_bytes` to IngestClient (default 5 MiB per ADR-012). Files > threshold split into `<name>.part<i>of<N>` slices carried as separate `chunks[]` multipart parts. Completes the ingestion client for large bundles.
- Schemas idle 20 cycles.
- Disk 86% stable 55 cycles.

## Current issues (unchanged)

- Datalogger 19 stable failures + occasional 20th flake.
- Datalogger pyproject missing dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Webapp 5 [BLOCKED] on backend.
- Website T067 [BLOCKED]: Cloudflare OAuth.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Backend dependency pressure

Sprint-backend at T068 (11th ORM). 6 downstream blocks. Each subsequent ORM delays router phase by one cycle. If T069-T070 ship, that's likely the complete ADR-005 ORM set.

## Cron: next 23:55 UTC.
