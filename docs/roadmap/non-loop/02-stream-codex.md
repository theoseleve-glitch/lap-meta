# Codex Stream — Autonomous Side-Quest Coding

**Resource:** Codex CLI (OpenAI coding agent, ~½ Claude Max tokens, manual invocation).
**Repo:** `lap-labs/` (new, separate from production repos) + ad-hoc across existing repos for critical-path acceleration.
**Your time:** 4-6h/week briefing + reviewing (sessions run autonomously).
**Commit policy (per F1=c):** Small tasks (<500 LOC diff) direct to master. Large tasks via PR with your review before merge.

Output destinations:
- V2 prototypes → `lap-labs/` new repo
- Coaching library validation harness → `lap-labs/coaching-harness/`
- Sprint progress monitor → `lap-labs/sprint-monitor/`
- Critical-path acceleration → into the respective sprint repo directly

---

## Setup (K000-K005) — do first

- [ ] K000 Create `lap-labs` repo: `mkdir C:/Users/Admin/Documents/Telemetry/lap-labs && cd lap-labs && git init && git add . && gh repo create theoseleve-glitch/lap-labs --private --source=. --remote=origin`
- [ ] K001 Add `CLAUDE.md` + `README.md` explaining it's an experiments / side-quest repo, not production
- [ ] K002 Workspace structure: `coaching-harness/`, `sprint-monitor/`, `v2-spikes/setup-recommender/`, `v2-spikes/pace-predictor/`, `v2-spikes/cohort-viz/`, `v2-spikes/training-plan/`
- [ ] K003 Each sub-project has its own `pyproject.toml` or `package.json` — polyglot workspace
- [ ] K004 Add `.gitignore` covering Python/Node/Streamlit secrets
- [ ] K005 First commit + push to GitHub

## Block A — Coaching Library Validation Harness (K010-K030)

**Single most important Codex output.** Closes R-02 from the risk register (coaching rule false-positive rate). Codex owns it end-to-end.

- [ ] K010 [Codex session 1, ~3h] Bootstrap Streamlit app in `lap-labs/coaching-harness/`. Streamlit + pandas + pyarrow + pyyaml deps. Basic "hello world" page.
- [ ] K011 [~1h] Session loader: enumerate `C:/Users/Admin/Documents/Telemetry/LapCoachLogger_sessions/` bundles, parse each session.json + laps
- [ ] K012 [~1h] Rule loader: read all YAML files from `lap-backend/coaching/library/rules/**/*.yaml`, compile conditions
- [ ] K013 [~2h] Rule execution engine: run each rule over each session, collect firings with timestamp + corner + evidence
- [ ] K014 [~2h] Trace visualization: for each firing, render matplotlib / plotly chart of brake/throttle/steering/speed in the corner where fired
- [ ] K015 [~2h] Labeling UI: 3-button interface (Correct / Incorrect / Ambiguous) + optional notes field per firing
- [ ] K016 [~1h] Persistence: labels stored in `lap-labs/coaching-harness/labels.jsonl` append-only
- [ ] K017 [~1h] Dashboard: per-rule FP rate, FN rate (requires separate "known weakness" fixture set), overall coverage
- [ ] K018 [~2h] Export: CSV of labels → `lap-backend/coaching/library/tuning/labels.csv` for backend to consume
- [ ] K019 [~1h] Filtering: filter labelings by rule, corner, severity, confidence, driver (single-driver for now)
- [ ] K020 [~1h] Batch mode: label N-at-a-time, keyboard shortcuts (Y=correct, N=incorrect, A=ambiguous, →=next)
- [ ] K021 [~1h] Screenshot generation: export labeled firing as PNG for potential blog content
- [ ] K022 [~2h] Rule threshold auto-tuner: given labeled data, suggest threshold changes that reduce FP < 5% without sacrificing TP > 80%
- [ ] K023 [~1h] Output the auto-tuned thresholds as YAML patches to feed back into rule library
- [ ] K024 [~1h] Tests: unit tests for loader + execution + labeling flow
- [ ] K025 [~1h] README + getting-started doc for the harness
- [ ] K026 [~1h] Deploy to local dev: `streamlit run app.py` + instructions for Windows launcher bat
- [ ] K027 [~1h] Import/export label sets — lets you back up labels and merge across versions
- [ ] K028 [~1h] Rule-diff mode: compare rule v1 vs v2 output on same session (A/B rule iteration)
- [ ] K029 [~1h] Weekly summary report generator: "this week labeled N firings, X rules improved, Y new false-positives flagged"
- [ ] K030 [review] Codex completes, you spend 1 hour familiarizing + start labeling 30 min/day

## Block B — Sprint Progress Monitor (K031-K045)

Codex builds a small internal dashboard reading all sprint files + review log + git state.

- [ ] K031 [Codex session, ~2h] Python CLI `sprint-monitor` in `lap-labs/sprint-monitor/`
- [ ] K032 [~1h] Parse all sprint-*.md files, count [x] / [ ] / [BLOCKED] / [NEEDS_REWORK] / [SCOPE_FLAG] / [SCAFFOLD_BULK]
- [ ] K033 [~1h] Parse review-log.md for cycle timestamps + outcomes
- [ ] K034 [~1h] Git log per repo: commits per day, lines changed per day, per-author
- [ ] K035 [~1h] Compute velocity: commits/day per repo, [x]/day per sprint, trending
- [ ] K036 [~1h] Burn-down: projected drain date per sprint given current velocity
- [ ] K037 [~1h] Slack webhook: weekly Monday 09:00 CET post to #lap-progress channel (or email via Resend)
- [ ] K038 [~1h] Terminal TUI view: live-refreshing sprint board
- [ ] K039 [~1h] HTML report generator: static report to `lap-labs/sprint-monitor/report-latest.html`
- [ ] K040 [~1h] Budget consumption tracker: parse email.log and compute approximate Claude Max budget usage / day
- [ ] K041 [~1h] Phase detection heuristic: when avg task wall-clock rises > 15min sustained for 3 days, auto-alert to slow loops
- [ ] K042 [~1h] Forecast: project end-date for each sprint given velocity + remaining tasks
- [ ] K043 [~1h] Tests + error handling
- [ ] K044 [~1h] Docs
- [ ] K045 [review] Deploy as cron (Task Scheduler on Windows) firing every Monday 09:00 CET

## Block C — V2 Spike: Car Setup Recommender (K046-K055)

Exploration only. No production deploy. Validates whether a setup recommender is feasible with existing data.

- [ ] K046 [Codex session, ~3h] Bootstrap `lap-labs/v2-spikes/setup-recommender/` — Python + pandas + scikit-learn
- [ ] K047 [~2h] Load archived sessions with setup metadata (iRacing exports include setup in session.json). Build dataset of {setup_params, lap_time_delta, driving_style_signature}
- [ ] K048 [~2h] Feature engineering: extract driving-style signature from telemetry (aggressive/smooth, late/early braker, etc.)
- [ ] K049 [~3h] Train baseline model: given style + target track + car, predict setup adjustments
- [ ] K050 [~2h] Validation on held-out sessions: compare predicted setup to actually-used setup
- [ ] K051 [~1h] Visualize: which setup params have largest predicted impact per driver style
- [ ] K052 [~2h] Simple CLI: `setup-recommender --session LapCoachLogger_sessions/X --target-track spa` → prints recommended setup deltas
- [ ] K053 [~1h] Write-up: `lap-labs/v2-spikes/setup-recommender/FINDINGS.md` — what worked, what didn't, year-2 recommendation
- [ ] K054 [~1h] Tests
- [ ] K055 [review] Codex delivers, you read findings + decide if it belongs in year-2 roadmap

## Block D — V2 Spike: Pace / Lap-Time Predictor (K056-K065)

Statistical (not LLM) prediction of expected lap pace given driver history + track + car + conditions.

- [ ] K056 [Codex session, ~3h] Bootstrap `lap-labs/v2-spikes/pace-predictor/`
- [ ] K057 [~2h] Dataset: all archived sessions with {driver_features, track, car, session_type, weather} → lap_time vector
- [ ] K058 [~2h] Baseline model: gradient boosting on tabular features
- [ ] K059 [~2h] Confidence intervals: predicted best-lap ± σ, race-pace ± σ, consistency band
- [ ] K060 [~1h] Compare predicted vs actual on held-out sessions
- [ ] K061 [~1h] Visualization: "expected pace envelope" for a driver at a track
- [ ] K062 [~1h] CLI: `pace-predictor --driver me --track nurburgring-vln --car gt3` → pace band
- [ ] K063 [~1h] Write-up FINDINGS.md
- [ ] K064 [~1h] Tests
- [ ] K065 [review] Deliverable reviewed, year-2 decision recorded

## Block E — V2 Spike: Cohort Data Visualization (K066-K074)

Once cohort benchmarking is live in the backend, visualize the distributions for product-team exploration.

- [ ] K066 [Codex session, ~2h] Bootstrap `lap-labs/v2-spikes/cohort-viz/` — Streamlit + plotly
- [ ] K067 [~2h] Mock cohort data (or real if backend produces it by then): per-track, per-car percentile distributions
- [ ] K068 [~2h] Violin plots per dimension (braking, throttle, etc.) with driver markers
- [ ] K069 [~1h] Archetype clustering: k-means on dimension scores, label clusters
- [ ] K070 [~2h] Interactive filter: car, track, session count min, date range
- [ ] K071 [~1h] Driver similarity: given a driver, find N most-similar based on dimension profile
- [ ] K072 [~1h] Export: PNG of any chart for marketing/blog use
- [ ] K073 [~1h] Write-up FINDINGS.md: what this could look like in-product
- [ ] K074 [review]

## Block F — V2 Spike: Training Plan Engine (K075-K083)

Runna-style multi-week plan generator given driver goals + current state.

- [ ] K075 [Codex session, ~3h] Bootstrap `lap-labs/v2-spikes/training-plan/`
- [ ] K076 [~2h] Plan template schema: {duration_weeks, focus_areas, weekly_sessions_count, progression_rules}
- [ ] K077 [~3h] Rule-based plan generator: given driver state (weaknesses, target event, time available), output weekly schedule
- [ ] K078 [~2h] Session-level prescription: per training session, what drill + target track + expected duration + success condition
- [ ] K079 [~1h] Adaptation logic: if a week's measured improvement < target, adjust next week's intensity or shift focus
- [ ] K080 [~1h] Visualization: 12-week plan as calendar + progression chart
- [ ] K081 [~1h] CLI: `training-plan --driver me --target iracing-24h-nurburgring --weeks 12` → outputs schedule
- [ ] K082 [~1h] Write-up FINDINGS.md
- [ ] K083 [review]

## Block G — Critical-Path Acceleration (K084-K090+)

Ad-hoc Codex sessions fired when a sprint task blocks 5+ downstream tasks. Fire each session only when the daily email / review log flags a specific blocker.

Common patterns (pre-written briefs):

- [ ] K084 Backend T045 (TS codegen pipeline) acceleration — one 4h Codex session cuts 2-3 days of /loop time if T045 is stuck
- [ ] K085 Webapp T031 (typed API client generation) acceleration
- [ ] K086 Mobile T042 (SessionEntity + Room migration) acceleration
- [ ] K087 Bridge algorithm implementation (backend T034 shape match) — complex, Codex can iterate faster than /loop
- [ ] K088 Coaching rule YAML authoring — Codex can batch-write 20 rules in one 4h session if backend /loop falls behind
- [ ] K089 Integration test writing — Codex can backfill missing test coverage across any repo
- [ ] K090 Performance optimization passes (JIT profiling + hot path improvements) — Codex is good at focused optimizations

These fire on-demand, not on a schedule. When the daily email shows a blocker on 5+ downstream tasks, assess whether a 4h Codex session unblocks it.

---

## Daily/weekly rhythm (Codex side)

- **Daily 14:30-15:00** — check Codex progress on any running session, brief next if needed
- **Weekly Monday morning** — review last week's Codex output, decide which V2 spike/side-quest to fire next
- **When daily email flags a critical blocker** — decide within 2h whether to fire Codex acceleration

Sessions typically 2-4 hours. You can run at most 2 concurrent Codex sessions without overwhelming context/review capacity.

Target over 30 days: all 4 V2 spikes completed with FINDINGS.md, harness live + labeled ≥500 rule firings, sprint monitor deployed, 2-4 critical-path accelerations.
