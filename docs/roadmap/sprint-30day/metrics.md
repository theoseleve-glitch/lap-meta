# Sprint Metrics — live snapshot

## Last updated: 2026-04-26T01:42Z (Cycle #189 — IDLE 35th consecutive + backend hold 119; M1 wrap-up signal — CHANGELOG + README onboarding)

## Per-repo status (HEAD as of c154 push)

| Repo | HEAD (post-push) | Last reviewed sha | Notes |
|---|---|---|---|
| lap-backend | 07604cb (T240) | f005d57 (T122 pre-cascade) | **HELD 119 commits** awaiting T104 schemas cascade resolution; **forced-checkpoint = 12 commits** (billing T155-T165 + crypto T204); T180-T240 full M1 surface incl coaching chain + hardening + ops + project docs (61 normal incl T204) |
| lap-webapp | 1ac2574 (T236) | 1ac2574 (T236) | idle since c151 |
| lap-schemas | a837d89 (Billing wire) | a837d89 | 3 consecutive clean schemas commits since T104 BLOCKED |
| lap-mobile-android | 64a88e4 (T183) | 64a88e4 (T183) | T183 OfflineCapturePolicy reviewed in c154 |
| lap-website | 1e34d87 (T152) | 1e34d87 (T152) | Pillar 3 §2 accepted; lint baseline flag (10 files) unchanged |
| datalogger | b23fbdf (T151) | b23fbdf (T151) | T150+T151 reviewed in c154; 19-stable-failure baseline holds; 20-flake 4th recurrence |

## Cumulative (180 cycles)

- Total reviewed: ~754+ sprint commits across 6 repos (26-cycle idle streak — no new reviews since c154)
- Reverts (cumulative): **7** (~0.78% rate over 180 cycles)
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
- **c158**: IDLE 4th consecutive; backend hold +2 to 39 (T159 + T160).
- **c159**: IDLE 5th consecutive; backend hold +1 to 40 (T161 admin /billing/sync endpoint).
- **c160**: IDLE 6th consecutive; backend hold +2 to 42; 160-cycle milestone.
- **c161**: IDLE 7th consecutive; backend hold +2 to 44 (T164 + T165 e2e billing test).
- **c162**: IDLE 8th consecutive; backend hold +1 to 45 (T166 Sentry SDK init); billing batch T155-T165 closed.
- **c163**: IDLE 9th consecutive; backend hold +2 to 47 (T167+T168 Sentry).
- **c164**: IDLE 10th consecutive; backend hold +1 to 48 (T169 PostHog SDK init).
- **c165**: IDLE 11th consecutive; backend hold +2 to 50 (T170+T171 PostHog events); half-century milestone.
- **c166**: IDLE 12th consecutive; backend hold +2 to 52 (T172+T173 PostHog events).
- **c167**: IDLE 13th consecutive; backend hold +1 to 53 (T174 PostHog identify on first-login).
- **c168**: IDLE 14th consecutive; backend hold +1 to 54 (T175 Prometheus /metrics endpoint).
- **c169**: IDLE 15th consecutive; backend hold +2 to 56 (T176+T177 Prometheus domain metrics).
- **c170**: IDLE 16th consecutive; backend hold +1 to 57 (T178 admin /api/v1/admin/kpis); 170-cycle mark.
- **c171**: IDLE 17th consecutive; backend hold +1 to 58 (T179 weekly Slack KPI cron).
- **c172**: IDLE 18th consecutive; backend hold +4 to 62 (T180 audit cron + T181-T183 coaching engine kernel start); surface shift to coaching rules engine.
- **c173**: IDLE 19th consecutive; backend hold +5 to 67 (T184-T188 engine kernel complete + first rule).
- **c174**: IDLE 20th consecutive; backend hold +5 to 72 (T189-T193 braking rules to 6 total).
- **c175**: IDLE 21st consecutive; backend hold +4 to 76; braking pillar 10 rules complete.
- **c176**: IDLE 22nd consecutive; backend hold +3 to 79; braking-pillar arc T180-T200 closed (21 commits).
- **c177**: IDLE 23rd consecutive; backend hold +2 to 81 (T201 admin simulate + T202 public listing).
- **c178**: IDLE 24th consecutive; backend hold +3 to 84 (T203 + **T204 signed-bundle crypto forced-checkpoint** + T205); checkpoint surface 11→12 commits.
- **c179**: IDLE 25th consecutive; backend hold +2 to 86 (T206 flag aggregation + T207 persist run_rules output).
- **c180**: IDLE 26th consecutive; backend hold +2 to 88 (T208+T209 WeaknessEpisode lifecycle); 180-cycle mark.
- **c181**: IDLE 27th consecutive; backend hold +2 to 90 (T210 dedup counter + T211 Prescription skeleton).
- **c182**: IDLE 28th consecutive; backend hold +4 to 94 (T212-T215 Prescription kernel).
- **c183**: IDLE 29th consecutive; backend hold +4 to 98 (T216-T219 Prescription close + ActionOutcome opens).
- **c184**: IDLE 30th consecutive; backend hold +3 to 101 (T220-T222); first triple-digit hold.
- **c185**: IDLE 31st consecutive; backend hold to 105 (T223-T227 polish + e2e test + openapi/swagger).
- **c186**: IDLE 32nd consecutive; backend hold to 110 (T228-T231 hardening: redoc + schemathesis + k6).
- **c187**: IDLE 33rd consecutive; backend hold to 114 (T232-T235 SLO+dep+sec+backups).
- **c188**: IDLE 34th consecutive; backend hold to 117 (T236 restore-test + T237 flags + T238 v1/v2 versioning).
- **c189 (this cycle)**: IDLE 35th consecutive; backend hold to 119 (T239 CHANGELOG with M1 entries + T240 README onboarding with mermaid arch diagram). **M1 wrap-up signal** — sprint loop adding project documentation suggests Milestone 1 closing on backend.

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
