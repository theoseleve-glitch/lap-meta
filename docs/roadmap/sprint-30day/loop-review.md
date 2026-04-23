# LAP — Autonomous Review + Deploy Loop Runbook

**Fires every 2h** from Telemetry root. One agent, all 5 repos. Plays the role that would otherwise be human review + CI + deploy.

**Critical read before running:** you are removing yourself from the quality gate. This loop catches objective failures (broken builds, failing tests, lint, type errors, secret leaks, scope blowups, forbidden patterns). It **cannot catch**: product-level wrongness, UX errors, wrong interpretation of an ADR, subtle security bugs, bad architecture choices. Acceptable pre-launch (zero paying users). You MUST reinsert yourself as human reviewer at or before the **Month 3 / Week 11 checkpoint** (2026-07-01) before anything ships to real paying users.

---

## What this loop does each cycle (runs every 2h)

For each of the 5 repos (`lap-backend`, `lap-webapp`, `lap-schemas`, `lap-mobile-android`, `datalogger`):

### Step 1 — Sync state

1. `cd` into repo.
2. `git fetch origin && git pull --ff-only` (do not force-merge; if non-fast-forward, flag and skip this repo this cycle).
3. Identify commits since the last review-log entry for this repo (parse `review-log.md`).
4. List only commits whose author email is `theos.eleve@gmail.com` AND commit message starts with `sprint(`. These are AI-authored sprint commits that require review. Skip others (manual commits, merges).

### Step 2 — Verify each commit

For each unreviewed commit, in order:

**Build + type + lint + test — language-specific matrix:**

| Repo | Command sequence (must all exit 0) |
|---|---|
| `lap-backend` | `uv sync` → `ruff check .` → `mypy app/ domain/` → `pytest -q` → `python -c "import app.main"` |
| `lap-webapp` | `pnpm install --frozen-lockfile` → `pnpm typecheck` → `pnpm lint` → `pnpm test` → `pnpm build` |
| `lap-schemas` | `uv sync` → `ruff check python/` → `mypy python/` → `pytest python/tests/` → `make codegen-check` (if Makefile has it) |
| `lap-mobile-android` | `./gradlew detekt` → `./gradlew ktlintCheck` → `./gradlew app:assembleDebug` → `./gradlew app:testDebugUnitTest` |
| `datalogger` | `pytest -q` → `ruff check src/` → `mypy src/` |

If any command fails: **go to Step 3 (revert path)**. If all pass: **go to Step 4 (accept path)**.

### Step 3 — Revert path

1. `git revert --no-edit <sha>` — creates a new revert commit. Do NOT use `git reset`.
2. Append to the offending task in `sprint-<repo>.md`: change the `[x] T### ... — sha: <sha>` to `[NEEDS_REWORK] T### ... — failed review: <reason>, reverted in <revert-sha>`. Reason must cite the first failing check (e.g., "pytest failed: test_health::test_returns_200").
3. Push both the original commit and the revert to origin (keeps history honest).
4. Log the event in `review-log.md`.
5. Do NOT attempt to fix the bad commit. The next sprint-loop iteration will re-pick the task and redo it.

### Step 4 — Accept path

1. Apply additional guardrails before pushing:
   - **Diff-size check:** `git show --stat <sha>` — if total insertions+deletions > 1500 lines for a single task, this is probable scope creep. FLAG (do not auto-revert) by appending `[SCOPE_FLAG] T### ... — diff=<N> lines, reviewer-triggered` next to the `[x]` mark. Push anyway. User must decide at next weekly review.
   - **Forbidden patterns scan:** `git show <sha>` | grep for: `--no-verify`, `# type: ignore`, `@pytest.mark.skip` without a `reason=`, `print(` in production code (not in tests/scripts), `TODO` added (not removed), `any` type added in TS/Python. Each hit is a FLAG (not revert), logged.
   - **Secret scan:** run `git log -p <sha>` | grep for patterns: `sk_live_`, `sk_test_` (unless in `.env.example`), `AIzaSy`, `ghp_`, `gho_`, `xoxb-`, `Bearer ey`, email passwords, private keys. Any hit → REVERT via Step 3 as "secret-leak".
   - **File-path guardrails:** any commit modifying `.github/workflows/*.yml` with addition of `workflow_dispatch` + `secrets.*` must also have been preceded by an explicit task requiring that change. If not, FLAG.

2. Tag the commit: `git tag reviewed/<YYYYMMDD>/<repo>/<short-sha> <sha>` so review history is discoverable.
3. `git push origin HEAD` and `git push origin --tags`.
4. Log success to `review-log.md`.

### Step 5 — Cross-repo coherence check (after per-repo steps)

Once all 5 repos processed this cycle, run:

1. **Schema drift check:** if `lap-schemas/python/` changed in this cycle, verify `lap-webapp/src/generated/` and `lap-mobile-android/app/.../generated/` regenerated and committed. If not, open a GitHub issue titled `schema-drift: lap-schemas updated, <repo> not regenerated` in the affected repo.
2. **Endpoint drift check:** if `lap-backend/app/routers/` changed, verify webapp e2e tests still reference valid paths. Run `pnpm test:contracts` (if it exists) in webapp.
3. **Contract test:** if both backend and webapp have new commits, run cross-repo smoke: spin up backend via `docker compose up -d postgres redis backend`, run webapp e2e against it. If fail → FLAG (not revert, since attribution is ambiguous).

### Step 6 — Deploy path (conditional, only if infra exists)

For each repo where Step 4 succeeded AND a deploy config exists in the repo root:

| Repo | Deploy trigger file | Deploy action | Target |
|---|---|---|---|
| `lap-backend` | `fly.toml` or `railway.json` | `fly deploy --remote-only` / `railway up` | staging env (`lap-backend-staging`) |
| `lap-webapp` | `wrangler.toml` or `.vercel/` | auto via git push (Cloudflare Pages watches origin) | preview URL (auto) |
| `lap-schemas` | n/a | `uv publish` to private PyPI if version bumped | internal registry |
| `lap-mobile-android` | `fastlane/Fastfile` or `.github/workflows/internal-track.yml` | `./gradlew publishInternalTrack` or workflow dispatch | Google Play internal track |
| `datalogger` | `inno-setup/*.iss` + `.github/workflows/release.yml` | workflow dispatch | GitHub Release draft |

**If no deploy config file exists yet → skip deploy for that repo this cycle. Log "deploy skipped: no config".**

**Never deploy to production in this loop.** Only staging / preview / internal / draft. Production deploy remains human-gated until explicit roadmap milestone.

### Step 7 — Post-deploy smoke (if any repo was deployed)

1. `curl https://<staging-url>/healthz` — expect 200 within 60s.
2. `curl https://<staging-url>/api/v1/me` with a test token — expect 401 (auth required) or 200 (if test token).
3. For webapp preview URL: Playwright smoke test `tests/smoke/login-and-list.spec.ts`.
4. If any smoke fails → rollback:
   - Backend: `fly releases` → `fly deploy --image <previous-image>` 
   - Webapp: no rollback needed on preview (next push overwrites)
   - Log the smoke failure as FLAG, do NOT revert the commit (smoke infra may be the fault, not the code).

### Step 8 — Update metrics

Rewrite `metrics.md` (overwrite, not append) with current counts from all 5 sprint files:

```
- Date: <YYYY-MM-DD>
- Sprint backend: [x]=N  [BLOCKED]=N  [NEEDS_REWORK]=N  [SCOPE_FLAG]=N  [ ]=N
- Sprint webapp:  ...
- Sprint desktop: ...
- Sprint mobile:  ...
- CI green rate (this cycle): N/N verified
- Commits reverted this cycle: N
- Scope flags this cycle: N
- Cross-repo issues: N
- Last deploy: <repo> @ <sha> @ <time>
```

### Step 9 — Log cycle

Append to `review-log.md`:

```
## <ISO-8601 timestamp> — Cycle #<N>

### lap-backend
- 3 new commits reviewed
- abc1234: ✓ all checks → pushed + tagged reviewed/20260423/lap-backend/abc1234
- def5678: ✗ pytest failed (test_ingest::test_idempotency) → REVERTED in 9abcdef, task T098 → [NEEDS_REWORK]
- 0011223: ✓ all checks, SCOPE_FLAG diff=1823 lines → pushed with flag

### lap-webapp
- 2 new commits reviewed
- ...

### Deploys
- lap-webapp → Cloudflare preview https://lap-webapp-abc.pages.dev (smoke: ✓)
- Others: skipped (no deploy config)

### Cross-repo
- No schema drift detected.
- Contract test: PASS

### Metrics delta
- 4 commits verified, 1 reverted, 1 flagged.
```

### Step 10 — Daily strategy email (at most once per calendar day, 08:00 UTC window)

Read `ops/.last_daily_sent` (create if missing). If the file's content is already today's date (UTC, `YYYY-MM-DD`), **skip Step 10**. Otherwise, if the current cycle is at or after 08:00 UTC, compose and send the daily strategy email.

**Gather inputs:**
1. `review-log.md` — all entries since the last daily send (covers the past 24h).
2. `metrics.md` — current snapshot.
3. Each `sprint-*.md` — list `[x]` added in the past 24h, all `[NEEDS_REWORK]`, all `[BLOCKED]`, all `[SCOPE_FLAG]`.
4. Recent `git log --since=24h` across all 5 repos — commit SHAs + subjects.

**Compose the email body** in this exact structure. Keep each section tight; use bullet points.

```markdown
# LAP Daily — <YYYY-MM-DD> — <one-line executive summary>

## KPIs (last 24h)
- Tasks shipped: <N> [x] (backend: <N>, webapp: <N>, desktop: <N>, mobile: <N>)
- Commits reverted: <N>
- Scope flags: <N>
- CI green rate: <N>%
- Sprint drain ETA: <N> days at current pace

## Work shipped (bullet list)
### lap-backend
- T0XX: <short description> (sha: <7-char>)
- ...
### lap-webapp
- ...
### lap-desktop
- ...
### lap-mobile
- ...

## Strategy decisions requiring HUMAN INPUT
Only list items that are:
  - NOT code-reviewable (the loops handle those)
  - NOT answered by an existing ADR or docs/roadmap file
  - Will block work within 48h OR have compounding consequences
Be brutally selective. Examples of what qualifies:
  - "Claude/Stripe/Clerk requires an account choice I can't make"
  - "Two valid interpretations of an ADR produce different behavior"
  - "Coaching library rule X disagrees with ADR-013 — which wins?"
If nothing qualifies: write "None — all work is self-contained."

## Issues flagged for awareness (NOT urgent, NOT blocking)
- SCOPE_FLAG on <repo>/<task>: diff <N> lines — agent over-engineered but tests passed
- Forbidden-pattern hit: <description>
- (Keep short; group similar ones)

## Blockers
- <repo> <task> blocked on <reason>. ETA to unblock: <estimate>.

## Next 24h outlook
- Expected shipments: <list task ranges per repo>
- Risks: <any loop showing systemic issues>
- Questions the loops will probably hit: <preemptive list>

---
Generated by review loop cycle #<N>.
```

**Send:**
```bash
python ops/send_email.py "LAP Daily — <YYYY-MM-DD> — <summary>" "<body>"
```

**On success:** write today's UTC date (`YYYY-MM-DD`) to `ops/.last_daily_sent` (overwrite), commit this change with `meta: daily email sent <date>`.

**On failure:** log the error in `review-log.md` but do NOT retry same cycle; will retry next cycle naturally.

### Step 11 — Alert emails (fired inline during earlier steps)

Alerts are fired immediately, not batched. The pattern is:

```bash
python ops/send_alert.py <alert-type> "<context with sha, file, repo, proposed fix>"
```

**When to fire each alert type:**

| Trigger | Alert type | Fired in step |
|---|---|---|
| Commit's test suite fails → reverted | skip (daily email covers it) | 3 |
| Commit exceeds 1500 LOC | `scope-blowup` | 4 |
| Forbidden-pattern scan hit | skip (daily email covers it) | 4 |
| Secret detected in commit | `secret-leak` (CRITICAL, immediate) | 4 |
| Schema drift after lap-schemas change | `contract-drift` | 5 |
| Contract test FAIL between backend+webapp | `contract-drift` | 5 |
| Deploy succeeded but smoke failed | `loop-stopped` (with "deploy smoke" context) | 7 |
| Any entry in Pause Triggers fires | `pause-triggered` | "Pause triggers" section |
| Forced human-review checkpoint hits | `human-review-required` | "Forced checkpoints" section |
| CI has been red on a repo >6h | `ci-broken` | 9 (end of cycle check) |
| Strategy decision blocking a task for >4h | `strategy-decision-required` | 8 (metrics scan) |

**Always include:** repo name, SHA (if applicable), task ID, specific failure message, and a one-line proposed action in the context string.

**Context string format:**
```
<repo> <sha> task=<T###> — <what happened> — Proposed: <what user should do>
```

Example:
```bash
python ops/send_alert.py secret-leak "lap-backend abc1234 task=T011 — detected 'sk_live_' in app/billing/stripe.py line 42 — REVERTED in def5678. Proposed: ROTATE Stripe key immediately at dashboard.stripe.com/apikeys."
```

---

## Hard NEVER rules

1. **Never revert a commit whose author email is NOT `theos.eleve@gmail.com`.** Those are manual commits — human intent.
2. **Never revert a commit whose message starts with `hotfix:`, `manual:`, `meta:`, or `revert:`.** Revert chains are human business.
3. **Never push to a branch other than the repo's default (`master`).** No rebase. No force-push.
4. **Never deploy to production.** Staging / preview / internal / draft only.
5. **Never edit `docs/roadmap/02-ARCHITECTURE-DECISIONS.md` or `01-STRATEGIC-DOCTRINE.md`.** These are load-bearing decisions.
6. **Never touch another repo's sprint file except via the `[NEEDS_REWORK]` or `[SCOPE_FLAG]` markers.** Don't mass-rewrite.
7. **Never run `rm -rf`, `git reset --hard`, `git clean -fd`, or `git push --force`.** If you need to undo, use `git revert`.
8. **Never create new GitHub repos, new remotes, or new branches.** Structure is fixed.
9. **Never upload anything to PyPI / npm / Play Store / App Store production channels.** Staging and internal tracks only.
10. **Never delete the `review-log.md` or `metrics.md` files.** Append / overwrite only the content.

## Pause triggers — exit the cycle and do nothing else until human intervenes

If any of these happen, **stop the current cycle, write a PAUSE entry in `review-log.md`, and let the /loop fire the next cycle fresh**:

- More than 3 commits in a single cycle fail review (= sprint loop is malfunctioning systematically).
- More than 1 cross-repo contract test fails in a row.
- Any secret-leak detected (even if reverted — user must rotate).
- Any smoke test failure on a production URL (if accidentally pointed at prod).
- `git fetch` returns an unexpected ref (someone else pushed).
- Disk usage >95% on local machine.

## Self-governance

The review loop cannot review its own commits. When you commit a change to `review-log.md` or `metrics.md`, use commit message prefix `meta: review loop cycle <N>` — the rule #2 above prevents self-review.

## Forced human-review checkpoints

At the following moments, post a PAUSE_FOR_HUMAN_REVIEW entry and stop the loop until the user manually resumes:

- Backend `ADR-005` objects all land (post-backend T070): user reviews data model + DB schema.
- Webapp Driver OS pages complete (post-webapp T165): user reviews UX at staging.
- Any change to `lap-backend/app/auth/*` or `lap-backend/app/billing/*`.
- Any diff touching cryptographic code, token handling, or payment flow.
- Before **Month 3 / Week 11** (2026-07-01): mandatory full-state review by human.

When a forced checkpoint hits: also fire `python ops/send_alert.py human-review-required "<context>"` so the user is emailed, not just logged.

## Notification discipline

The email system can spam. Guardrails:

1. **One `scope-blowup` alert per day max** — if multiple commits flag scope in one cycle, aggregate into one alert with a list.
2. **One `pause-triggered` alert per unique cause per day** — if the same pause fires in consecutive cycles, suppress duplicates; the daily email summarizes.
3. **`secret-leak` is NEVER deduplicated** — always sent.
4. **`human-review-required` is NEVER deduplicated** — always sent.
5. **`strategy-decision-required` fires once per unique decision** — identify by a hash of the context string; don't re-send for the same question on subsequent cycles.

Track dedup state in `ops/alert-dedup.json` — a simple dict of `{alert_type: {hash: last_sent_iso}}`.
