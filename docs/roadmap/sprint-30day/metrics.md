# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T23:55Z (Cycle #80)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 66 | 2 (T018/T019) | 1 (T013) | `32999fb` (T069 DriverBenchmarkProfile — 12th model) |
| lap-webapp | 82 | 5 (T157/T158/T161/T162/T164) | 0 | `8cd9d3e` (T170 BestSessionsList; 302) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 21 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 67 | 0 | 0 | `dacf4d7` (T067 LocationFixMonitor loss-of-fix UiState) |
| lap-website (marketing) | 68 | 1 (T067) + implicit (T082/T084/T087) | 0 | `0b6d1ca` (T089 /demo related links) |
| datalogger (desktop) | 44 | 1 (T035) | 0 | `a241f86` (T045 completion cursor persistence) |

## This cycle (Cycle #80)

- Verified GREEN: 5 (backend T069, webapp T170, mobile T067, website T089, datalogger T045)
- Reverted: 0 | SCOPE_FLAG: 0 new

## Cumulative (80 cycles)

- Total reviewed: 304 · Accepted+tagged: 300 🎯 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0
- **Milestone**: 300 cumulative accepts reached (295 → 300 this cycle). 80 review cycles. 97.4% first-pass rate.

## Cycle 80 notables — 12TH ORM + BESTSESSIONS LIST + FIX MONITOR + RELATED LINKS + CURSOR RESUMPTION

- **Backend T069 DriverBenchmarkProfile ORM + migration** — 12th model. 52/52 (+2). orm.py +21, migration 45, tests 104. Benchmark profile likely holds cohort-relative metrics (driver X vs cohort Y).
- **Webapp T170 BestSessionsList component** — 260 ins / **+10 tests** (292→302). Best-of surfacing on profile. data-session-id wired from T169 paves the drill-through.
- **Mobile T067 LocationFixMonitor surfaces loss-of-fix via UiState** — 254 ins. LocationFixMonitor 49 + LocationFixState 23 + test 182. 7th layer of mobile capture stack. Surfaces GPS loss-of-fix to UI so user knows they're not in a dead zone unconsciously. **14 consecutive clean mobile accepts**.
- **Website T089 /demo related links** — 55 ins. Small footer inside /demo with caption-styled links to /how-it-works + /pricing. Post-FinalCta fallback path for users who skipped primary CTA. 258 tests (+3).
- **Datalogger T045 persist completion cursor** — 225 ins. Writes `.ingest_cursor.json` with 202-response fields on success. Subsequent upload calls read cursor, match manifest's session_id → return cached `IngestResult` without re-POSTing. Resumability + idempotency.
- Schemas idle 21 cycles.
- Disk 86% stable 56 cycles.

## Current issues

- Datalogger 19 stable failures + occasional 20th flake (known since c22/c68).
- Datalogger pyproject missing dev extras.
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Webapp 5 [BLOCKED] on backend: T157, T158, T161, T162, T164.
- Website T067 [BLOCKED]: Cloudflare OAuth.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Cron: next 00:10 UTC.
