# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T22:40Z (Cycle #75)

## Per-repo status

| Repo | `[x]` | `[BLOCKED]` | `[NEEDS_REWORK]` | HEAD |
|---|---|---|---|---|
| lap-backend | 62 | 2 (T018/T019) | 1 (T013) | `dd601a7` (T065 ActionPrescription — 8th model) |
| lap-webapp | 77 | 2 (T157/T158) | 0 | `bd51979` (T160 print styles; 273) |
| lap-schemas (subset) | 35 | 0 | 0 | `0dda9cb` (idle 16 cycles; Python parity 35/35 ✓) |
| lap-mobile-android | 63 | 0 | 0 | `94b81b6` (T063 CaptureForegroundService + notification) |
| lap-website (marketing) | 64 | 1 (T067) + implicit (T082 video-gate) | 0 | `6102080` (T083 /demo axe clean) |
| datalogger (desktop) | 40 | 1 (T035) | 0 | `be38dbe` (idle 2; **merge-marker pollution still**) |

## This cycle (Cycle #75)

- Verified GREEN: 4 (backend T065, webapp T160, mobile T063, website T083)
- Reverted: 0 | SCOPE_FLAG: 0 new
- **Flake caught on website build**: first `pnpm build` re-run failed with ESM AsyncLoaderHooks error (node internal), re-re-run succeeded. Not T083-caused; systematic-debugging accept path.

## Cumulative (75 cycles)

- Total reviewed: 284 · Accepted+tagged: 280 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 3 · Pause triggers: 0

## Cycle 75 notables — 8TH ORM + MOBILE FOREGROUND SERVICE + WEBAPP PRINT STYLES + WEBSITE A11Y

- **Backend T065 ActionPrescription ORM + migration** — 8th model. Largest backend test file to date (193 lines). 43/43 (+3). ADR-005 coaching pattern: one Session spawns WeaknessEpisodes (T064) + ActionPrescriptions (T065). Aggregate shape now covers the full driver-coaching artifact pipeline.
- **Mobile T063 CaptureForegroundService with persistent notification** — 243 lines. AndroidManifest +15, CaptureForegroundService 80, CaptureForegroundCommand 28, CaptureNotification 19, strings.xml +5, test 52. **First Android Service class** — capture will run in foreground for multi-hour sessions. 10 consecutive clean mobile accepts.
- **Webapp T160 print styles on profile layout** — 28 lines (small diff). Tailwind `print:` variants: `print:bg-white print:text-black` on root, `print:break-inside-avoid` on hero + 3-col row, `print:grid-cols-3` locks layout for print. 273 tests (+3). Niche but enables coach review on paper.
- **Website T083 /demo axe clean** — 22 lines. Extends existing WCAG 2.1 A/AA axe e2e to /demo. Commit body notes T072 shell + T073 placeholder were already clean at ship — no fixes needed, just asserting the gate. 249 tests (same count, Playwright e2e adds no vitest).
- **T082 implicitly gated on T074 video** (documented in T081's commit body from c73). Sprint-marketing jumped T082 → T083 since T082 can't test what isn't shipped yet.
- Schemas idle 16 cycles. Datalogger idle 2.
- Disk 86% stable 51 cycles.

## Current issues

- Datalogger 19 pre-existing failures (tech-debt since c22).
- Datalogger pyproject doesn't declare pydantic/pyyaml/uuid6 as dev extras.
- **Datalogger finalizer.py merge markers persist** (3rd cycle flagged).
- Desktop T035 [BLOCKED]: backend ingestion endpoint.
- Webapp T157 + T158 [BLOCKED]: backend driver profile endpoint.
- Website T067 [BLOCKED]: Cloudflare Pages OAuth + edge-function.
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 BLOCKED on docker.
- Website T017 SCOPE_FLAG.
- **Website build flake observed (ESM loader)** — 1 occurrence, re-run green. Watch.
- Step 10 daily-email deferred.

## Cron: next 22:55 UTC.
