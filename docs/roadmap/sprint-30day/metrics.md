# Sprint Metrics — live snapshot

## Last updated: 2026-04-25T18:49Z (Cycle #158 — IDLE 4th consecutive + backend hold 39 + billing-surface forced-checkpoint pending)

## Per-repo status (HEAD as of c154 push)

| Repo | HEAD (post-push) | Last reviewed sha | Notes |
|---|---|---|---|
| lap-backend | c5e67f1 (T160) | f005d57 (T122 pre-cascade) | **HELD 39 commits** awaiting T104 schemas cascade resolution; T155-T160 billing surface (6 commits, forced-checkpoint will trigger on unblock) |
| lap-webapp | 1ac2574 (T236) | 1ac2574 (T236) | idle since c151 |
| lap-schemas | a837d89 (Billing wire) | a837d89 | 3 consecutive clean schemas commits since T104 BLOCKED |
| lap-mobile-android | 64a88e4 (T183) | 64a88e4 (T183) | T183 OfflineCapturePolicy reviewed in c154 |
| lap-website | 1e34d87 (T152) | 1e34d87 (T152) | Pillar 3 §2 accepted; lint baseline flag (10 files) unchanged |
| datalogger | b23fbdf (T151) | b23fbdf (T151) | T150+T151 reviewed in c154; 19-stable-failure baseline holds; 20-flake 4th recurrence |

## Cumulative (154 cycles)

- Total reviewed: ~754+ sprint commits across 6 repos
- Reverts (cumulative): **7** (~0.9% rate over 154 cycles)
  - c133: lap-webapp T233 (next/font spread macros — reworked c134 with inline literals at e0f6494)
  - c133/c134/c136: lap-schemas T104 — 3 reapplies all reverted (test fixture not updated alongside required-field additions); ESCALATED TO BLOCKED at c136 — awaiting human resolution
- Pause-trigger alerts fired: **2**
  - c124 corrective `human-review-required` (deferred c81 alert — Resend `1dd7a636-6ed8-45b8-b8d1-f5be3d576d72`)
  - c136 systematic-malfunction `pause-triggered` after T104 3rd revert (Resend `50090743-0584-49b4-a72d-7da1b4c8905b`)
- Active cross-repo cascades: **1** (T104 → backend held 30 commits)
- Forced-checkpoint pauses lifted: **1** (c81 → c133 ADR-005 review)
- 20-failure datalogger flake recurrences: **4** (c139, c149, c151, c154) — overlay_browser timing tech-debt; baseline 19 between

## Cycle 153 notables — 4 accepts, 0 reverts

- **lap-mobile-android T182**: UnpairDeviceUseCase (server revoke + local logout). bd241f6, 309 insertions. Initial gradle test BUILD FAILED in 5s (transient cache artifact); --rerun-tasks gave BUILD SUCCESSFUL in 46s. Not a regression. Pipe-masking pattern (`tail -N` swallowing exit code) recurred — flagged for runbook addendum.
- **lap-website T151**: telemetry-apps-comparison pillar outline (Pillar 3 planning). 2d1560a, 474 insertions in `docs/pillar-articles/`. 20 pages built. **LINT-BASELINE-FLAG**: 10 baseline prettier issues (8 test fixtures + 2 blog astro pages) all unrelated to T151 — pre-existing tech-debt; recommended chore task `prettier --write` cleanup.
- **datalogger T148 + T149**: strategy push/manage UI (6280ee1, 436 ins) + safety-car detection/strategy recalc (9b1b00c, 235+1 ins). Stable 19/2501/1-skip baseline. **FLAG**: 1 `# type: ignore[arg-type]` (specific error code, **kwargs unpack workaround) accepted not reverted per Step 4.
- **lap-schemas Billing**: a837d89 already-tagged from prior session, no new push.
- **lap-backend**: held +4 (T148-T151 sprint commits accumulated). Cascade resolution still pending.

## Recent cycle history (c134-c153 summary)

- **c134-c136**: T104 saga — 3 reapplies, 3 reverts; ESCALATED BLOCKED at c136 with explicit resolution paths documented in sprint-backend.md. Pause-alert fired.
- **c137-c145**: Long quiet stretch — sprint loops re-converging post-pause; user-paused at intervals; "reviewed go on" signal at c145 unblocked the resumed loop.
- **c146-c148**: Gradle false-positive resolved (chained-task BUILD FAILED → strict per-task && gating). Pipe-masking bug noted for datalogger.
- **c149-c150**: lap-schemas resumes clean wire commits (TrackCatalog, CarCatalog, Billing) demonstrating the loop CAN land schemas changes when test+model land together. 150-cycle milestone.
- **c151-c152**: 20-flake 3rd recurrence on datalogger; mobile T181; backend hold 25→26.
- **c153**: 4 accepts (mobile T182 + website T151 + datalogger T148+T149); backend hold +4 to 30.
- **c154**: 4 accepts (mobile T183 + website T152 + datalogger T150+T151); backend hold +1 to 31; 20-flake 4th recurrence; `set -o pipefail` mitigation worked.
- **c155**: IDLE; backend hold +2 to 33 (T153+T154 webhook handlers).
- **c156**: IDLE 2nd consecutive; backend hold +1 to 34 (T155 invoice.payment_failed handler).
- **c157**: IDLE 3rd consecutive; backend hold +3 to 37 (T156-T158 billing/Stripe webhook + portal + promo).
- **c158 (this cycle)**: IDLE 4th consecutive; backend hold +2 to 39 (T159 WAITLIST_FOUNDER promo at checkout + T160 daily Stripe<->DB reconciliation). Billing surface = T155-T160 (6 commits).

## Review loop state

- **Loop is ACTIVE** (cron 15-min interval; `/loop` self-paced).
- **Backend hold is the dominant work item**: T104 cascade blocks 30 backend sprint commits. Resolution requires human-authored schemas commit landing model+test in one shot (or making the 3 new fields `Optional[str]=None` with field-level defaults).
- **Webapp idle** through c151-c153 — the T237+ work appears not yet sprint-loop-generated.

## Current issues

- **BLOCKED (cross-repo cascade)**: lap-backend held 30 commits pending lap-schemas T104 (`SessionIngestAccepted` required fields without paired test update). Awaiting human action.
- **Lint baseline (lap-website)**: 10 prettier-formatting files pre-date T151. Recommend `chore: prettier --write` cleanup task.
- **Datalogger pytest baseline**: 19 stable failures (overlay_browser/overlay_window_manager/sync_queue) — long-standing tech-debt, not new drift.
- **Pipe-masking gating bug**: `cmd 2>&1 | tail -N` swallows exit code, masks failures. Runbook should mandate `set -o pipefail` + `${PIPESTATUS[0]}` checks for verification chains.
- **Datalogger pyproject dev-extras absent**: ruff/mypy/pytest not installed by `uv sync`. Latent 145 ruff + 425 mypy errors invisible to sprint loop. Recommend `[project.optional-dependencies.dev]` block.

## Cron: ACTIVE (15-min interval). Next fire processes any new mid-cycle commits.
