# Sprint Metrics — live snapshot

## Last updated: 2026-04-24T10:25Z (Cycle #26)

## Per-repo status

| Repo | `[x]` | `[ ]` | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD |
|---|---|---|---|---|---|---|
| lap-backend (total sprint-backend.md) | 25 | 212 | 2 | 1 (T013) | 0 | `7b64848` (**10 idle cycles** — schemas-phase) |
| lap-webapp | 41 | 199 | 0 | 0 | 0 | `f1d0e5e` (T089 PrescriptionCard) |
| lap-schemas (T021–T055 subset in sprint-backend) | 8 | — | 0 | 0 | 0 | `124b8c4` (idle 1 cycle) |
| lap-mobile-android | 27 | 213 | 0 | 0 | 0 | `291c7f3` (idle 2 cycles) |
| lap-website (sprint-marketing) | 27 | 193 | 0 | 0 | 1 (T017 inline) | `152a1d3` (idle 1 cycle) |
| datalogger (sprint-desktop) | 5 | 235 | 0 | 0 | 0 | `6690165` (idle 1 cycle) |

## This cycle (Cycle #26)

- Verified GREEN: 1 (webapp T089)
- Reverted: 0 | SCOPE_FLAG: 0 new
- 5 of 6 repos idle at cycle-25-end baselines

## Cumulative (26 cycles)

- Total reviewed: 102 · Accepted+tagged: 100 (1 INFRA_FLAG c4, 1 SCOPE_FLAG c11-T017)
- Reverted: 1 · Pause triggers: 0

## Cycle 26 notables

- Webapp **T089 PrescriptionCard** (65 lines + 74-line test). test count climbed to 5 files / 32 tests (+10 from T088's 22). Coaching-domain component pair T088 (WeaknessEpisodeCard) + T089 (PrescriptionCard) now both live — shaping the "After every session" tiles the website section references.
- Backend 10 idle cycles: entering double-digits. Natural per ADR — backend T021-T045 run in lap-schemas, and T018/T019 are BLOCKED on docker.
- Disk usage: **86%** stable.
- First 100-commit milestone on reviewed+tagged (100 accepts, 1 revert, 1 INFRA_FLAG, 1 SCOPE_FLAG over 26 cycles).

## Current issues

- Datalogger 19 pre-existing failures (tech-debt; bisect-verified cycle 24).
- Backend T013 NEEDS_REWORK persistent.
- Backend T018/T019 Dockerfile + docker-compose BLOCKED (docker not installed).
- Website T017 SCOPE_FLAG (cycle 11 Lighthouse CI).
- Step 10 daily-email deferred: `ops/.last_daily_sent`=2026-04-23.

## Cron: next 10:30 UTC.
