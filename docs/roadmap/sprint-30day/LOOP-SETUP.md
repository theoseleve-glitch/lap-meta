# /loop setup — 4 terminals, 1 task/hour, 30 days

**Updated 2026-04-23** — architecture scaffolded, paths confirmed, iOS frozen, Android primary.

## What's running where

| Terminal | Path | Repo | Sprint file | Platform |
|---|---|---|---|---|
| 1 — BACKEND | `C:/Users/Admin/Documents/Telemetry/lap-backend` | Python FastAPI | `sprint-backend.md` then `sprint2-backend.md` | ✓ Windows |
| 2 — WEBAPP | `C:/Users/Admin/Documents/Telemetry/lap-webapp` | Next.js | `sprint-webapp.md` then `sprint2-webapp.md` | ✓ Windows |
| 3 — DESKTOP | `C:/Users/Admin/Documents/Telemetry/datalogger` | Python / Qt QML | `sprint-desktop.md` then `sprint2-desktop.md` | ✓ Windows |
| 4 — MOBILE | `C:/Users/Admin/Documents/Telemetry/lap-mobile-android` | Kotlin / Compose | `sprint-mobile.md` then `sprint2-mobile.md` | ✓ Windows |
| 5 — REVIEW + DEPLOY | `C:/Users/Admin/Documents/Telemetry` | all 6 repos | `loop-review.md` runbook | ✓ Windows |
| 6 — MARKETING | `C:/Users/Admin/Documents/Telemetry/lap-website` | Astro static | `sprint-marketing.md` | ✓ Windows |

**`lap_mobile/` (iOS)** is frozen until Mac available. `sprint-mobile-ios-future.md` preserves its 240 iOS tasks for resumption.

## Email notifications (configured 2026-04-23)

All alerts + daily strategy digest are sent from `ops/send_email.py` via Resend API key `auto-prompt` to `theos.eleve@gmail.com`.

- `ops/.env` — contains live API key. **Gitignored, never committed.**
- `ops/email.log` — append-only audit of every send.
- `ops/send_email.py` — core sender (markdown → HTML, fallback-safe on Windows cp1252).
- `ops/send_alert.py` — 9 preformatted alert types (secret-leak, loop-stopped, scope-blowup, etc.).

The review loop (Terminal 5) handles:
- **Daily strategy digest** — first cycle after 08:00 UTC each day, composed from review-log + metrics + sprint state + git log.
- **Inline alerts** — fired immediately when a pause/revert/scope/leak condition hits, with dedup state in `ops/alert-dedup.json`.

Test email system manually:
```bash
cd C:/Users/Admin/Documents/Telemetry
python ops/send_alert.py strategy-decision-required "test alert"
```
Expect `[OK] Email sent. Resend ID: <uuid>` + email in Gmail inbox within 30s.

## Budget

Your €200/month Claude subscription ≈ €3,200 API-equivalent. 4 concurrent /loop threads at 1h interval = ~96 agent calls/day × 30 days = ~2,880 calls/month. Well within capacity. No throttling needed.

---

## Start order (important)

Backend schemas block everything downstream. Start Terminal 1 first.

```
Day 1, morning     → Start TERMINAL 1 (backend). Runs T001-T045 over first ~45 hours.
Day 2, evening     → Once T045 ("Swift codegen pipeline" / codegen working) is [x], start TERMINALS 2, 3, 4.
Day 3+             → All 4 running concurrently.
```

You can technically start all 4 immediately — terminals 2/3/4 will just pile up `[BLOCKED]` markers until their backend prereqs clear. Cleaner to wait.

---

## Terminal 1 — BACKEND

**Start command:**
```bash
cd C:/Users/Admin/Documents/Telemetry/lap-backend
claude
```

**Paste this prompt once Claude starts:**
```
/loop 1h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/sprint-backend.md. Find the next `[ ]` task in order (skip any whose Dep: references still-unchecked tasks — they unblock later). Invoke superpowers:using-superpowers. For implementation tasks, invoke superpowers:test-driven-development. Complete the task fully: write code, write tests, run `pytest -q` until green, commit. Commit format: `sprint(backend): T### <short>`. No --no-verify. Reference C:/Users/Admin/Documents/Telemetry/docs/roadmap/02-ARCHITECTURE-DECISIONS.md for any architecture choice. Reference ./CLAUDE.md for project conventions. Invoke superpowers:verification-before-completion before claiming done. After commit succeeds, edit the sprint file: change `[ ]` to `[x]` for that task and append ` — sha: <short-sha>`. If genuinely blocked after one honest attempt, change `[ ]` to `[BLOCKED: <reason>]`, move on. Never pause to ask the user. Never exit the loop. Keep diffs minimal — do not refactor beyond the task scope.
```

---

## Terminal 2 — WEBAPP

**Start command:**
```bash
cd C:/Users/Admin/Documents/Telemetry/lap-webapp
claude
```

**Paste this prompt once Claude starts:**
```
/loop 1h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/sprint-webapp.md. Find the next `[ ]` task in order (skip blocked-by-dep). Invoke superpowers:using-superpowers then superpowers:test-driven-development. Complete fully: code + `pnpm typecheck && pnpm lint && pnpm test` green + commit. Commit: `sprint(webapp): T### <short>`. No --no-verify. Reference C:/Users/Admin/Documents/Telemetry/docs/roadmap/02-ARCHITECTURE-DECISIONS.md and ./CLAUDE.md. Invoke superpowers:verification-before-completion before claim-done. Mark `[x]` with sha in sprint file. If blocked because a backend task is not yet done, mark `[BLOCKED: waiting on lap-backend T###]` and move on. Never ask the user. Never exit the loop. Minimal diffs — stay in scope.
```

---

## Terminal 3 — DESKTOP

**Start command:**
```bash
cd C:/Users/Admin/Documents/Telemetry/datalogger
claude
```

**Paste this prompt once Claude starts:**
```
/loop 1h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/sprint-desktop.md. Find the next `[ ]` task in order (skip blocked-by-dep). Invoke superpowers:using-superpowers. For P0 fixes use superpowers:systematic-debugging, else superpowers:test-driven-development. Complete fully: code + `pytest -q` green + commit. Commit: `sprint(desktop): T### <short>`. No --no-verify. Reference C:/Users/Admin/Documents/Telemetry/docs/roadmap/02-ARCHITECTURE-DECISIONS.md and ./CLAUDE.md. Invoke superpowers:verification-before-completion before claim-done. Mark `[x]` with sha. If blocked, `[BLOCKED: <reason>]`. If a task requires the backend ingestion endpoint and backend isn't live yet, skip it. Never ask the user. Never exit. Minimal diffs — no scope creep.
```

---

## Terminal 4 — MOBILE (Android)

**Start command:**
```bash
cd C:/Users/Admin/Documents/Telemetry/lap-mobile-android
claude
```

**Paste this prompt once Claude starts:**
```
/loop 1h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/sprint-mobile.md. This is the Android-first sprint (Kotlin + Compose + Gradle). iOS is frozen. Find the next `[ ]` task in order (skip blocked-by-dep). Invoke superpowers:using-superpowers then superpowers:test-driven-development. Complete fully: code + `./gradlew app:assembleDebug && ./gradlew app:testDebugUnitTest` green + commit. Commit: `sprint(mobile): T### <short>`. No --no-verify. Reference C:/Users/Admin/Documents/Telemetry/docs/roadmap/02-ARCHITECTURE-DECISIONS.md (especially ADR-007 dual timestamps, ADR-012 ingestion) and ./CLAUDE.md. Invoke superpowers:verification-before-completion before claim-done. Mark `[x]` with sha. If blocked, `[BLOCKED: <reason>]`. If a task requires an Android device (instrumented tests) and none connected, run unit tests only and mark the instrumented part `[PENDING: device-required]`. Never ask the user. Never exit the loop. Minimal diffs.
```

---

## Daily review ritual (10 min, every morning)

1. **Progress check:** `grep -c "\[x\]" sprint-*.md` in each repo. Target: 6-8 new [x] per repo per 24h.
2. **CI check:** each repo's GitHub Actions status.
3. **[BLOCKED] triage:** for each blocked task, decide — unblock (change to `[ ]`), defer (leave), or delete.
4. **Bad-commit scan:** `git log --since=1.day -n 20` in each repo. Spot-read any diff that smells wrong.
5. **Credit burn:** check Anthropic usage dashboard. Expected ~€15/day, stable.

## Stop / pause / resume

- **Pause a loop:** Ctrl+C in the terminal. Progress saved in sprint file's `[x]`.
- **Resume:** re-paste the same /loop command. Picks up at next `[ ]`.
- **Skip manually:** edit sprint file, change `[ ]` to `[SKIP: reason]`. Loop ignores non-`[ ]`.
- **Restart one task:** change `[x]` back to `[ ]`.
- **Emergency stop all 4:** close all 4 terminal windows.

## Forced pauses (kill loops, handle yourself)

- **P0 production bug** reported by a user.
- **3 consecutive bad commits** from the same loop (wrong scope, broken tests pushed).
- **Approaching release/merge-to-main** — no automated commits during release week.
- **[BLOCKED] count >20% of completed** — something systemic is wrong, pause and diagnose.

## Files in this folder

```
LOOP-SETUP.md                         ← this file
sprint-backend.md                     ← Sprint 1: 240 backend tasks (drains ~Day 10)
sprint-webapp.md                      ← Sprint 1: 240 webapp tasks
sprint-desktop.md                     ← Sprint 1: 240 desktop tasks
sprint-mobile.md                      ← Sprint 1: 240 Android tasks
sprint-mobile-ios-future.md           ← 240 iOS tasks (FROZEN until Mac)
sprint2-backend.md                    ← Sprint 2: 200 backend tasks (M3 APIs + bridge + cohort + endurance + events + 50 rules + B2B)
sprint2-webapp.md                     ← Sprint 2: 150 webapp tasks (bridge UI + cohort UI + endurance UX + V1 polish + B2B + perf + a11y)
sprint2-desktop.md                    ← Sprint 2: 80 desktop tasks (endurance refinement + auto-update + perf + bug bash)
sprint2-mobile.md                     ← Sprint 2: 90 mobile tasks (stabilization + Play Store + Wear OS)
sprint-marketing.md                   ← 220 marketing tasks (new pillar, never in any prior sprint)
loop-review.md                        ← runbook for Terminal 5 (review + deploy)
review-log.md                         ← append-only log, maintained by review loop
metrics.md                            ← live snapshot, overwritten by review loop
```

Totals: Sprint 1 = 960 tasks (4 × 240). Sprint 2 = 520 tasks (200 + 150 + 80 + 90). Marketing = 220 tasks. **Grand total = 1,700 tasks** covering ~100% of the 6-month roadmap.

---

## Terminal 5 — REVIEW + DEPLOY (autonomous quality gate)

You opted out of daily human review. This 5th loop plays the review + CI + deploy role that would normally be manual. It runs every 2 hours, picks up all new commits across all 5 repos made by Terminals 1-4, runs the full test matrix, and decides: push to GitHub (if green), revert (if broken), or flag (if oversized / suspicious).

**Critical acceptance:** this is AI reviewing AI. It catches objective failures (tests/lint/types/build/secrets/scope-blowups). It does NOT catch product-level wrongness. You must reinsert yourself as human reviewer before **2026-07-01** (M3/W11, public beta staging date).

### Start command

```bash
cd C:/Users/Admin/Documents/Telemetry
claude --dangerously-skip-permissions
```

### Paste this prompt once Claude starts

```
/loop 2h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/loop-review.md in full and execute exactly one cycle per the runbook. Invoke superpowers:using-superpowers then superpowers:systematic-debugging when investigating test failures. Respect the Hard NEVER rules section without exception. For each of the 5 repos (lap-backend, lap-webapp, lap-schemas, lap-mobile-android, datalogger) in order: sync, identify unreviewed sprint commits since last review-log entry, run the per-repo verification matrix, then take the revert path on any failure or the accept path on green. After all repos processed, run Step 5 cross-repo coherence, Step 6 conditional deploy (staging/preview only, never production), Step 7 post-deploy smoke, Step 8 rewrite metrics.md, Step 9 append to review-log.md. Commit review-log + metrics changes with message prefix `meta: review loop cycle <N>` and push to origin. If a Pause Trigger fires, write a PAUSE entry and exit this iteration (next iteration fires fresh). Never ask the user. Never exit the /loop itself. If a forced human-review checkpoint hits, write PAUSE_FOR_HUMAN_REVIEW to review-log.md and do not proceed until user manually removes the PAUSE marker.
```

### Why 2h instead of 1h

- Sprint loops produce ~4 commits per hour across 4 repos. Reviewing 8 commits per cycle keeps per-cycle work bounded (~15-30 min wall-clock for 8 verifications in parallel).
- 2h interval means you get a deploy-to-staging cadence of 2h. Fast enough for a preview loop, not so fast that infra churns.
- You can bump to 1h later if you want tighter feedback, but 2h is the safe starting value.

### First cycle expected behavior

The first time the review loop fires, it reads `review-log.md`'s "Initial state" section, sees the baseline commits (`4969e7c`, `9429e8b`, etc.) as "already-reviewed", and starts fresh from whatever commits landed since then. You should NOT see the initial T001 commits get re-reviewed or reverted.

### When the review loop should itself be audited

Every time the 4 sprint loops collectively ship ~50 commits (roughly every 2-3 days at current pace), YOU should spot-check `review-log.md` for:

- Are any commits getting reverted repeatedly? → a task's acceptance criterion may be wrong, fix the sprint file manually.
- Are SCOPE_FLAGs piling up? → a sprint loop is going rogue, consider tightening the prompt.
- Is CI green rate <80% on any repo? → something systemic is wrong.
- Are any `PAUSE_FOR_HUMAN_REVIEW` entries unhandled? → that's YOUR job, the loops won't proceed past them.

Budget 5 minutes every 2-3 days for this meta-review. It replaces the daily 15-min review with a less-frequent but mandatory one.

### Starting order (full picture)

```
Day 1, Hour 0       → Launch Terminal 1 (backend). Let it scaffold contracts alone.
Day 2, Hour ~45     → Once lap-backend T045 is [x], launch Terminals 2, 3, 4.
Day 2, Hour ~50     → Once Terminals 2/3/4 each have ≥2 commits, launch Terminal 5 (review).
Day 3+              → All 5 running in steady state. Your only job: triage
                      PAUSE_FOR_HUMAN_REVIEW flags and weekly meta-reviews.
```

### If you find you can't resist checking daily

That's fine — the review loop doesn't forbid human intervention. It just doesn't require it. Adding human review on top strictly improves quality. Removing human review entirely is the deliberate trade you made today.

---

## Terminal 6 — MARKETING (NEW — launch alongside the others)

Unlike Sprint 2 terminals (which wait for Sprint 1 to drain), the marketing terminal runs **immediately**. Marketing has zero prior sprint work and no backend dependencies for the first ~100 tasks. Start it now.

### Start command

```bash
cd C:/Users/Admin/Documents/Telemetry/lap-website
claude --dangerously-skip-permissions
```

### Paste this prompt once Claude starts

```
/loop 1h Read C:/Users/Admin/Documents/Telemetry/docs/roadmap/sprint-30day/sprint-marketing.md. Find the next `[ ]` task in order (skip blocked-by-dep). Invoke superpowers:using-superpowers then superpowers:test-driven-development for code, or superpowers:writing-skills for long-form content. Complete fully: code + `pnpm build && pnpm typecheck && pnpm test` green + commit. Commit: `sprint(marketing): T### <short>`. No --no-verify. Reference C:/Users/Admin/Documents/Telemetry/docs/roadmap/02-ARCHITECTURE-DECISIONS.md, 01-STRATEGIC-DOCTRINE.md for positioning, and ./CLAUDE.md. Invoke superpowers:verification-before-completion before claim-done. Mark `[x]` with sha. If blocked, `[BLOCKED: <reason>]`. All public-facing copy must align with 01-STRATEGIC-DOCTRINE.md — no "AI coach now" claims (roadmap forbids LLMs in coaching per ADR). Never ask the user. Never exit. Minimal diffs. When writing long-form content (blog, pillar pages), the target is human-quality professional prose, not SEO keyword soup.
```

---

## Sprint 1 → Sprint 2 transition

Around Day 10-12, Sprint 1 queues will drain. `metrics.md` will show `[ ] open` close to 0 on a repo. When that happens:

### For the affected terminal:

1. Ctrl+C the old /loop prompt.
2. Re-paste the same /loop command but **change the filename**:
   - `sprint-backend.md` → `sprint2-backend.md`
   - `sprint-webapp.md` → `sprint2-webapp.md`
   - `sprint-desktop.md` → `sprint2-desktop.md`
   - `sprint-mobile.md` → `sprint2-mobile.md`

No other change needed. Same terminal, same /loop cadence, new task queue.

### Expected drain order (at current velocity)

```
Day 10-12   → sprint-backend drains  → switch to sprint2-backend
Day 11-13   → sprint-webapp drains   → switch to sprint2-webapp
Day 14-16   → sprint-desktop drains  → switch to sprint2-desktop
Day 16-20   → sprint-mobile drains   → switch to sprint2-mobile
Day 22-30   → Sprint 2 queues drain  → full 6-month plan complete
Day 25-32   → sprint-marketing drains → marketing site live
```

If a Sprint 2 queue also drains before end of month, that means you're running faster than expected — the 6-month plan is done early and you can start planning the 7-12 month roadmap.

## Total coverage

With Sprint 1 + Sprint 2 + Marketing executed:

| Pillar | Sprint 1 | Sprint 2 | Coverage of 6mo plan |
|---|---|---|---|
| Backend | 240 tasks (M1-M2) | 200 tasks (M3-M6 + bridge + cohort + rules) | ~95% |
| Webapp | 240 tasks (M1-M3) | 150 tasks (M4-M6) | ~95% |
| Desktop | 240 tasks (M1-M5) | 80 tasks (M5-M6 polish) | ~100% |
| Mobile (Android) | 240 tasks (M1-M5 scaffolding) | 90 tasks (Play Store + Wear OS) | ~90% (iOS still frozen) |
| Marketing | 0 | 220 tasks (full 6mo scope) | ~95% |
| **Net** | | | **~95% of 6-month roadmap** |

The remaining ~5% is things like Apple Watch (needs Mac), second rounds of iteration based on real paying-user feedback, and paid ad experiments that require a marketing budget decision.
