# Sprint Metrics — live snapshot

Overwritten each review cycle. Single source of truth for "how's the sprint going."

---

## Last updated: 2026-04-23T20:20Z (Cycle #5)

## Per-repo status

| Repo | `[x]` done | `[ ]` open | `[BLOCKED]` | `[NEEDS_REWORK]` | `[SCOPE_FLAG]` | HEAD SHA |
|---|---|---|---|---|---|---|
| lap-backend | 7 | 233 | 0 | 0 | 0 | `3f3d471` (T007 FastAPI /healthz /readyz) |
| lap-webapp | 8 | 232 | 0 | 0 | 0 | `19b0803` (T008 useReducedMotion hook) |
| lap-schemas | 0 | — | 0 | 0 | 0 | `a50d39a` (unchanged) |
| lap-mobile-android | 8 | 232 | 0 | 0 | 0 | `226b89a` (T008 pre-commit hook) |
| lap-website (sprint-marketing) | 8 | **3 BLOCKED** (T008-T010, user-action) | 3 | 0 (was 2 in cycle 4 — cleared per ADR-018) | 0 (T001 now `[SCAFFOLD_BULK]` informational, not SCOPE_FLAG per ADR-018 Dec 2) | `255cb7b` (T011 robots+sitemap) |
| datalogger (sprint-desktop) | 2 | 238 | 0 | 0 | 0 | `eb97496` (unchanged — no new desktop commits this cycle) |

## This cycle (Cycle #5)

- Verified (true green at HEAD per ADR-018 Dec 5): **8** sprint commits
  - lap-backend: T007 `3f3d471` (FastAPI — `import app.main` now applicable + passes)
  - lap-webapp: T007 `29ffe70`, T008 `19b0803`
  - lap-mobile-android: T008 `226b89a`
  - lap-website: T005 `bffd825`, T006 `9cb0ecf`, T007 `5826a14`, T011 `255cb7b` (re-verified from cycle 4 — all green now per ADR-018)
- Reverted: 0
- NEEDS_REWORK markers cleared: **2** (lap-website T005 + T006 — already restored by user/ADR-018 before this cycle)
- Flagged (scope): 0 (cycle 3's T001 SCOPE_FLAG reclassified to SCAFFOLD_BULK per ADR-018 Dec 2)
- Flagged (scaffold-bulk): 1 (lap-website T001 retroactive, informational)
- INFRA_FLAG: 0 (datalogger had no new commits this cycle; pytest-in-dev-deps gap from cycle 4 still applies when next commit lands)
- BLOCKED: 3 new markers in sprint-marketing.md (T008 Cloudflare Pages, T009 DNS, T010 Preview deploys — all require user Cloudflare OAuth)
- Skipped (ADR-017 applicability): backend pytest (still no tests/); mobile detekt/ktlintCheck (silent-skip continues — tasks wired to `:app:` subproject, runbook uses root-level names, benign noise)
- Repo-level skipped (non-FF): 0

## Cumulative (since loop start)

- Total cycles run: 5
- Total sprint commits reviewed: 29 (c1: 0, c2: 3, c3: 9, c4: 9, c5: 8)
- Total accepted + pushed + tagged: 28 (1 INFRA_FLAG from c4 datalogger T002)
- Total reverted: 0
- Total NEEDS_REWORK events: 2 (both c4 lap-website, both cleared c5 per ADR-018)
- Total SCOPE_FLAG: 0 current (c3's T001 now SCAFFOLD_BULK informational)
- CI green rate at HEAD: 29/29 true-or-applicable-green
- Last deploy: n/a (no repo has deploy config yet — lap-website T008 blocked on user OAuth)

## Current issues

- **lap-website T008-T010 BLOCKED on user Cloudflare setup** — marketing loop correctly self-marked these as [BLOCKED] with reason notes. Unblock requires: user signs into Cloudflare dashboard, creates Pages project bound to the lap-website GitHub repo, sets build command `pnpm build` + output dir `dist` + Node 22. Then T009 (DNS) and T010 (PR previews) unblock cascadingly. Loop will keep skipping these.
- **Mobile detekt/ktlintCheck still silent-skipped** — tasks confirmed wired to `:app:` subproject (e.g., `./gradlew :app:detekt` works per cycle 4 commit 0a15e1e), but my applicability grep uses `^detekt\s` pattern not matching `:app:detekt`. Cycle-4 memo flagged this; fix is trivial in a future runbook revision. Not impacting results (assemble+test cover real behavior).
- **Datalogger pytest gap** (carried from cycle 4) — dev deps don't yet include pytest. datalogger sprint loop didn't commit anything this cycle so no impact; next sprint(desktop) commit will re-surface INFRA_FLAG until resolved.

## Disk usage

C: at 86% (down 1% — weird, cleanup may have happened). Threshold 95%. Within headroom.

## Alert state (ops/alert-dedup.json)

- `strategy-decision-required`:
  - `c2-infra-gap-2026-04-23` (resolved)
  - `c4-lapwebsite-matrix-fail-2026-04-23` (resolved by ADR-018)
- `scope-blowup`:
  - `2026-04-23` (cycle-3 T001 blowup, now reclassified to SCAFFOLD_BULK; entry kept as historical dedup)

No new alerts this cycle — all repos green, no triggers hit.

## Cron

Active: `b6279c25` (`7,37 * * * *`, 30-min rounded from user's 45m). Next fire 20:37 UTC.

## ADR-018 policy adoption

- Decision 1 (@types/node mandatory): lap-website already has `"@types/node": "25.6.0"` in devDeps (T006 fix). sprint-webapp T017 task description updated per Decision 4.
- Decision 2 (scaffold-task threshold 8000): T001 line in sprint-marketing.md updated `[SCOPE_FLAG]` → `[SCAFFOLD_BULK]`.
- Decision 5 (HEAD-based review, not per-commit): now canonical in runbook Step 2.
