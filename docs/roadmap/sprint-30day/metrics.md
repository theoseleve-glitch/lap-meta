# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T22:55Z (Cycle #76)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 63 | 2 (T018/T019) | 1 (T013) | `4622063` (T066 ActionOutcome — 9th model) |
| lap-webapp | 79 | **5 new** (T157, T158, T161, T162, T164 all on backend) | 0 | `5e3c036` (T165 memoize charts; 277) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 17 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 64 | 0 | 0 | `9e89acb` (T064 lock-screen notification + service category) |
| lap-website (marketing) | 65 | 1 (T067) + implicit (T082, T084 video-gate) | 0 | `6fe6390` (T085 /demo post-demo CTA) |
| datalogger (desktop) | 41 | 1 (T035) | 0 | `5a979d8` (T042 IngestClient.upload; **merge markers resolved by fix c351c75**) |

## This cycle (Cycle #76)

- Verified GREEN: 5 (backend T066, webapp T165, mobile T064, website T085, datalogger T042)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Meta fix commit** noted but not reviewed: datalogger c351c75 `fix: resolve stash-pop conflict markers (P0 — 13 src files)` — resolves the finalizer.py + 12 other files' merge markers I flagged across c73-c75. Runbook Step 1 skips non-`sprint(` commits; this is correct — fix commits are user/meta territory, not review-loop scope. **3rd-cycle flag cleared**.
- **Datalogger test flakiness** confirmed: HEAD oscillates 19↔20 failures across runs. Stable set = 19 (baseline since c22). T042 own-file 5/5.

## Cumulative (76 cycles)

- Total reviewed: 289 · Accepted+tagged: 285 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 76 notables — 9TH ORM + MOBILE LOCK-SCREEN NOTIFICATION + WEBAPP PERF + DATALOGGER INGEST UPLOAD + FIX CLEARS MERGE POLLUTION

- **Backend T066 ActionOutcome ORM + migration** — 9th model. 46/46 (+3). orm.py +22 + migration 47 + tests 167. Completes the coaching feedback loop: ActionPrescription (T065) → ActionOutcome (T066) captures whether the prescription worked.
- **Mobile T064 lock-screen visible notification + service category** — 56 lines. Updates CaptureForegroundService + CaptureNotification to set `VISIBILITY_PUBLIC` + `CATEGORY_SERVICE` so users see the "recording session" status on lock screen (transparency requirement, Android 14+ FGS). 11 consecutive clean mobile accepts.
- **Webapp T165 memoize heavy profile charts** — 44 lines. 4 charts (SkillRadarChart, DriverScoreCard, ReadinessGauge, RecentSessionsSparkline) wrapped in React.memo so parent re-renders from unrelated state (filter, modal, theme) skip chart render. 277 tests (+4).
- **Website T085 /demo post-demo trial CTA** — 31 lines. Mounts shared T034 FinalCta on /demo. Zero new components — reuses existing signup contract (href, rel=noopener, copy "Start 14-day"). 251 tests (+2).
- **Datalogger T042 IngestClient.upload returns ingest_job_id** — 288 lines. Happy-path POST to ADR-012 endpoint: reads manifest.json, builds multipart/form-data body (manifest field + every bundle file). First functional ingest implementation.
- **Datalogger fix c351c75** resolved merge-marker pollution (30+ zones in 13 files) with explicit per-zone audit. Runbook correctly skipped it (non-`sprint(` prefix). **3 new self-aware behaviors from webapp** this cycle (T161, T162, T164 BLOCKED + T163 no-op).
- Self-aware sprint behavior count: **10 events across 4 loops**:
  1. desktop T035 — c65
  2. website T067 — c67
  3. webapp T155 no-op — c69
  4. website T071 design-gate — c71
  5. webapp T157 — c74
  6. webapp T158 — c74
  7. webapp T161 (backend share endpoint) — c76
  8. webapp T162 (T229 + backend data hook) — c76
  9. webapp T163 no-op (T129 covers) — c76
  10. webapp T164 (backend mutations) — c76
- Schemas idle 17 cycles.
- Disk 86% stable 52 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22). **Flake (20th failure) observed again** — flips across runs. Stable baseline = 19.
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- ~~Datalogger finalizer.py merge markers~~ **RESOLVED** in fix c351c75 (3 cycles flagged).
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- **Webapp 5 BLOCKED tasks on backend**: T157, T158, T161, T162, T164 — all waiting on backend endpoints (driver profile, share, mutations).
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- Step 10 daily-email deferred.

## Backend dependency pressure

**6 concurrent downstream blocks on backend endpoints** (was 3 at c74):
- desktop T035 (ingestion)
- webapp T157 (profile page e2e)
- webapp T158 (profile LCP)
- webapp T161 (share endpoint)
- webapp T162 (PostHog + data hook)
- webapp T164 (mutation endpoints)

Sprint-backend is at T066 ORM. Expect router phase (T067+?) to unblock cascade.

## Cron: next 23:10 UTC.
