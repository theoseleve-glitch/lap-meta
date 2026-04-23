# LAP 6-Month Development Roadmap

Date: 2026-04-23

Horizon: 2026-04-23 to 2026-10-31

Inputs:
- `full audit  (1).pdf`
- `C:\Users\Admin\Downloads\questionnaire.md`
- Local repo/docs scan across `Analysis/V2_claude_ai`, `Analysis/V2_claude_ai/lap-website`, `datalogger`, and `lap_mobile`

## 1. Strategic Decisions

### Product Identity

LAP should be built and marketed as:

> Garmin for racing drivers: a Driver OS that turns telemetry into a continuous driver development plan.

This is not a generic telemetry viewer. The analysis layer exists to serve coaching, progression, readiness, and next-session planning.

### 6-Month Success Definition

By 2026-10-31, LAP should feel like one ecosystem:

1. A sim racer can sign up, install the logger, record a session, sync it, receive a useful diagnosis, get a next-session plan, complete that next session, and see whether the prescription worked.
2. The webapp owns driver memory, weaknesses, prescriptions, outcomes, and progression.
3. Desktop and mobile are trusted capture/live-assistant clients that feed the same canonical session model.
4. The website explains the ecosystem clearly and sells the dream without promising fake AI coaching.
5. Stripe is live and the product can support paying B2C customers.

### Failure Definition

The main failure mode is not "too little code." The main failure mode is shipping four impressive but disconnected products.

If the products do not share canonical sessions, driver identity, source taxonomy, quality scoring, and coaching memory, the roadmap has failed even if every repo gained features.

### Frozen Product Split

| Product | Role | Must Own | Must Not Become |
|---|---|---|---|
| Website | Sell the dream and explain the ecosystem | Positioning, SEO, waitlist/signup/download funnels, launch narrative | An operational dashboard |
| Webapp/backend | Driver intelligence brain | Session memory, driver profile, WeaknessEpisode, ActionPrescription, ActionOutcome, TransferLink, progression, paid account | A pile of session pages with no memory |
| Desktop | Sim capture and live local assistant | Low-latency capture, overlays, modes, strategy prompts, local finalization, sync | Heavy cloud-dependent compute during gameplay |
| Mobile | Real-world capture companion and light live dashboard | Crash-safe capture, RaceBox/iPhone sensors, preflight checks, upload queue, quick trackside trust cues | Deep analysis brain |

### Primary Persona

Primary: sim racer who wants structured improvement.

Secondary: amateur real-life racer or karter.

Explicit anti-persona for this cycle: pro teams, expensive semi-pro categories, team-coach buyer workflows.

### Commercial Target

User target from questionnaire: 500-5000 users, 1000 paying users stretch, EUR 10k MRR minimum ambition.

Reality check: at EUR 12-20/month, EUR 10k MRR needs roughly 500-850 paying users. For a solo founder, this requires a strong public beta by month 3, aggressive content, and a very clear paid conversion loop.

## 2. North Star, KPIs, and Quality Bars

### North Star Metric

Primary north star:

`Completed Coaching Loops per active driver per month`

A completed coaching loop means:

1. Session is recorded.
2. Session is synced and cloud-visible.
3. LAP creates at least one WeaknessEpisode or updates an existing one.
4. LAP generates an ActionPrescription.
5. Driver records a later session against that prescription.
6. LAP writes an ActionOutcome showing improved, unchanged, or worse.

This proves LAP is more than session history.

### Per-App Primary KPIs

| Product | Primary KPI | 6-Month Target |
|---|---|---|
| Website | Visitor to signup/waitlist/logger-download conversion | 8-12% on targeted traffic |
| Webapp/backend | Completed coaching loops per active driver/month | 2+ loops for retained active users |
| Desktop | Sim capture -> finalize -> sync success rate | 98%+ for supported sim sessions |
| Mobile | Started real capture -> local safe session -> sync success rate | 95%+ beta, 98% release target |

### Activation

A new user is activated when they:

1. Create an account.
2. Connect/install a capture path.
3. Upload or sync a valid session.
4. See a driver-readable insight and a next-session action.

Target time-to-first-value:

| Scenario | Target |
|---|---|
| Demo/sample session | Under 5 minutes |
| Sim user with desktop logger | Under 30 minutes |
| Mobile real-life capture | Under 1 track session |

### Reliability Targets

| Area | Public Beta Target | Release Target |
|---|---:|---:|
| Upload-to-session-visible success | 95% | 99% |
| Upload-to-first-insight latency | p95 < 120s | p95 < 45s |
| Desktop session loss | < 1% | < 0.2% |
| Mobile session loss | < 2% beta | < 0.5% |
| Webapp paid/auth critical path availability | 99% | 99.5% |
| False-positive strong coaching recommendation | < 15% beta | < 8% |

### Engineering Health KPIs

Track weekly:

1. `main` CI green rate by repo: target 90% beta, 95% release.
2. P0 bug count open longer than 48h: target 0.
3. Canonical E2E smoke pass rate: target 100% before public beta.
4. Upload/sync failure rate by source: target visible in dashboard by month 2.
5. Schema drift incidents: target 0 after Month 1.

## 3. Recommended Tech Stack Decisions

### Backend

Decision: keep the current Python/Flask backend for 6 months. Do not migrate to FastAPI or Node during this cycle.

Reason:
- The bottleneck is product coherence and canonical intelligence, not framework choice.
- Migration would consume solo-founder capacity.
- Flask can support the required API, Celery, auth, Stripe, ingestion, and intelligence modules if boundaries are cleaned up.

Target internal structure:

```text
telemetry_tool/
  contracts/
  ingest/
  sessions/
  intelligence/
  coaching/
  bridge/
  strategy/
  billing/
  observability/
```

`lap_tool_virtualisation` should be absorbed into the main backend domain model, but heavy jobs should still run as separate Celery worker processes.

### Schema and Contracts

Decision: use Pydantic models as the source of truth, emit JSON Schema, and generate TypeScript types from schemas.

Rationale:
- Python backend already dominates ingestion/intelligence.
- JSON Schema is easy for desktop/mobile/web to validate.
- TypeScript generation removes duplicate frontend DTOs.
- Swift can consume generated schemas or hand-written Codable structs with schema tests.

Canonical contract artifacts:

```text
contracts/
  session_bundle_v2.schema.json
  session_summary.schema.json
  driver_profile.schema.json
  weakness_episode.schema.json
  action_prescription.schema.json
  action_outcome.schema.json
  transfer_link.schema.json
  strategy_event.schema.json
  data_quality.schema.json
```

### IDs

Decision: use UUIDv7 for canonical IDs.

Use UUIDv7 for:
- `driver_id`
- `session_id`
- `bundle_id`
- `weakness_episode_id`
- `action_prescription_id`
- `action_outcome_id`
- `transfer_link_id`
- `strategy_plan_id`
- `strategy_event_id`

Migration stance: hard cutover for new ingestion; historical sessions are reprocessed where possible and archived if not compatible.

### Data Model Doctrine

Every session must carry:

| Field | Required |
|---|---|
| `session_id` | Yes |
| `driver_id` | Yes |
| `source_type` | Yes: sim, kart, track_day, race_weekend, endurance, test, drill, qualifying, stint |
| `source_app` | Yes: desktop, mobile, import, web |
| `environment` | Yes: sim, real_kart, real_car, other |
| `vehicle` | Yes |
| `track_layout` | Yes, even if provisional |
| `session_objective` | Yes, can be "unknown" only during beta |
| `training_block_id` | Required for coaching-plan sessions; nullable otherwise |
| `event_id` | Nullable |
| `started_at`, `ended_at` | Yes |
| `data_quality_score` | Yes |
| `provenance` | Yes: app build, device id, sensor config, firmware where available |

### ML and LLM Policy

6-month policy:

1. User-facing coaching is deterministic/rule-based first.
2. Basic ML is allowed only after enough labeled data exists to validate it.
3. No LLM-generated coaching text in the release product.
4. AI can assist development, audits, documentation, UI exploration, and internal triage.
5. The coaching library should use structured templates, evidence, measurable targets, and confidence.

### AI Tool Allocation

| Work Type | Primary AI | Secondary AI | Notes |
|---|---|---|---|
| Architecture and roadmap docs | Codex / ChatGPT high reasoning | Claude Code review | Use AI for synthesis, but freeze decisions manually |
| Backend implementation | Codex | Copilot inline | Use tests and schema diffs as authority |
| Frontend implementation | Codex | Copilot inline | Avoid broad UI rewrites before contracts |
| Desktop Qt/QML refactor | Codex | Claude Code for second-pass risk audit | Keep changes small and test-gated |
| iOS Swift reliability work | Codex | Copilot inline | Needs Mac/Xcode validation |
| Design/marketing exploration | Figma AI / Figma Make | Claude design critique | Export final specs into repo docs |
| Large refactor review | Claude Code | Codex | Use as independent reviewer, not sole implementer |
| Test generation | Codex | Copilot | Prioritize contract, smoke, and reliability tests |

## 4. Dependency Map

### Hard Blockers

These block multiple downstream streams:

1. Canonical `SessionBundleV2` schema.
2. Unified ingestion pipeline replacing split `sessions_v2` and `sync_upload`.
3. Canonical ID and provenance model.
4. Data-quality scoring contract.
5. Backend-owned `next_actions` / `ActionPrescription`.
6. Crash-safe mobile session journal.
7. Desktop live processor import/runtime stability.
8. Stripe/account entitlement path for paid beta.
9. E2E smoke path: sim detect -> record -> finalize -> sync -> web review.

### Parallelizable Work

Can run while blockers are being implemented:

1. Website messaging cleanup and ecosystem explanation.
2. Coaching ontology/library drafting.
3. Desktop overlay curation and mode UX design.
4. Mobile trust-cue UI design.
5. Public beta landing/waitlist/content.
6. Observability dashboard and runbook cleanup.
7. Sample/demo session preparation.

### Explicit Deferrals

Do not build in the first 6 months unless everything above is stable:

1. Social network features.
2. Live multi-car streaming.
3. Advanced neural ML or LLM coaching.
4. Full B2B/team-coach product.
5. Deep peer percentile models without opt-in data-sharing.
6. Android and wearable release-quality apps. Prototype only if capacity exists after mobile reliability.

## 5. Milestone Overview

| Month | Dates | Theme | Exit Gate |
|---|---|---|---|
| Month 1 | Apr 23-May 22 | Stop fragmentation and fix P0 reliability | Canonical schema + smoke path skeleton + no known P0 runtime blockers |
| Month 2 | May 23-Jun 22 | Coaching memory MVP | WeaknessEpisode + ActionPrescription + backend `next_actions` visible in webapp |
| Month 3 | Jun 23-Jul 22 | Public beta and paid path | Stripe live, sim-first loop works for strangers, beta launch |
| Month 4 | Jul 23-Aug 22 | Sim-real bridge MVP and mode depth | TransferLink MVP + desktop modes + mobile field beta |
| Month 5 | Aug 23-Sep 22 | Release candidate hardening | 50 strangers unattended, reliability targets mostly met |
| Month 6 | Sep 23-Oct 31 | Full release and growth loop | Driver OS story coherent, paid product stable, KPI dashboard reviewed weekly |

## 6. Month 1 - Architecture Lock and P0 Stabilization

Objective: stop product drift, define the shared contracts, and fix the failures that would destroy trust.

### Month 1 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M1-01 | Ecosystem | BLOCKER | Create architecture doctrine doc | User accepted server=brain, clients=thin; needs one source of truth | `docs/ecosystem_architecture.md` | Codex | None | Reviewed against audit/questionnaire |
| M1-02 | Backend | BLOCKER | Create Pydantic contract package | Contract drift is top technical risk | `telemetry_tool/contracts/*` | Codex | M1-01 | Schema tests pass |
| M1-03 | Backend | BLOCKER | Define `SessionBundleV2` schema | Must be canonical across desktop, mobile, web | JSON Schema + examples | Codex | M1-02 | Golden fixture validation |
| M1-04 | Backend | BLOCKER | Define UUIDv7 ID policy | Needed before migrations and cross-app sync | ID helper + migration notes | Codex | M1-02 | Unit tests |
| M1-05 | Backend | BLOCKER | Define source/environment/session taxonomy | Sim-real bridge and timeline depend on it | Enum contract | Codex | M1-02 | Contract tests |
| M1-06 | Backend | BLOCKER | Define `DataQualityScore` contract | Incomplete telemetry must be usable but flagged | Quality model + reason codes | Codex | M1-02 | Unit tests with low/high quality fixtures |
| M1-07 | Webapp/backend | BLOCKER | Remove duplicate bundle type sources | Audit found duplicate bundle contracts | Single TS generated source | Codex | M1-02 | Typecheck/build |
| M1-08 | Webapp/backend | BLOCKER | Fix possible double `/api/v1` prefix in bundle hooks | Audit high-risk endpoint drift | Corrected API client usage | Codex | None | API hook tests |
| M1-09 | Webapp/backend | BLOCKER | Resolve duplicate session channels route | Audit found duplicate endpoint registration | One source of truth route | Codex | None | Integration route test |
| M1-10 | Webapp/backend | BLOCKER | Build unified ingestion design | `sessions_v2` and `sync_upload` must converge | Design + first migration path | Codex | M1-03 | Contract smoke |
| M1-11 | Desktop | BLOCKER | Fix or rebuild `live_telemetry_processor` import path | Runtime integrity is P0 | Processor booting reliably | Codex | None | `python -m pytest tests -q` |
| M1-12 | Desktop | BLOCKER | Fix QML bootstrap test instability | CI degradation should not be accepted | Passing bootstrap test | Codex | None | `python -m pytest tests/test_qml_bootstrap.py -q` |
| M1-13 | Desktop | BLOCKER | Keep evaluation gate green | Logger must be trusted ingestion source | Gate report | Codex | M1-11 | `python -m pytest tests/test_evaluation_gate.py -v` |
| M1-14 | Mobile | BLOCKER | Implement crash-safe active session journal design | "Never lose a session" is first trust requirement | Design + implementation plan | Codex | M1-03 | Unit test plan |
| M1-15 | Mobile | BLOCKER | Patch force unwraps and crash-on-init risks | Audit/user marked Sprint 1 | Safe initialization | Codex/Copilot | None | Xcode unit tests on Mac |
| M1-16 | Mobile | BLOCKER | Make finalize fail explicitly on missing/empty temp CSV | Silent success destroys trust | `corrupt_local` state | Codex | M1-14 | Unit tests |
| M1-17 | Mobile | BLOCKER | Implement deterministic upload queue model | Sync must resume after launch | Queue state machine | Codex | M1-14 | Unit tests |
| M1-18 | Website | PARALLEL | Align public positioning statements | Current marketing has sim/real ambiguity | Copy patch list | Figma/Claude/Codex | None | Content QA |
| M1-19 | Website | PARALLEL | Draft "How LAP works" ecosystem page | Website must explain 4-app system | Page outline + wireframe | Figma AI + Codex | M1-01 | Manual review |
| M1-20 | Ecosystem | BLOCKER | Define E2E smoke path | Needed before beta | Test plan: detect -> record -> finalize -> sync -> review | Codex | M1-03 | Smoke checklist exists |
| M1-21 | Ecosystem | PARALLEL | Create weekly KPI dashboard spec | Needed to avoid shipping blind | Metrics schema | Codex | None | KPI review template |

### Month 1 Exit Gate

Do not proceed to feature expansion until:

1. Canonical session schema exists.
2. Desktop can run the gate suite.
3. Mobile cannot silently "succeed" with missing session files.
4. Webapp duplicate routes/types/prefix issues are resolved.
5. E2E smoke path is specified even if not fully automated.

## 7. Month 2 - Coaching Memory MVP

Objective: make LAP remember a driver and prescribe what to do next.

### Month 2 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M2-01 | Backend | BLOCKER | Add `DriverProgressSnapshot` contract and DB table | Driver profile needs backend memory | Migration + model + API | Codex | M1-02 | Integration tests |
| M2-02 | Backend | BLOCKER | Add `WeaknessEpisode` contract and DB table | First core intelligence object | Migration + CRUD/update API | Codex | M1-02 | Unit + integration tests |
| M2-03 | Backend | BLOCKER | Add `ActionPrescription` contract and DB table | Replaces frontend drill heuristics | Migration + API | Codex | M2-02 | Integration tests |
| M2-04 | Backend | BLOCKER | Add `ActionOutcome` contract skeleton | Needed for closed loop | Migration + nullable outcome state | Codex | M2-03 | Unit tests |
| M2-05 | Backend | BLOCKER | Build deterministic prescription engine v1 | No LLM; rules + evidence + confidence | `next_actions` generator | Codex | M2-02 | Golden fixtures |
| M2-06 | Backend | PARALLEL | Draft coaching library taxonomy | Weaknesses judged against library | Technique/consistency/racecraft/etc. ontology | Codex + Claude review | M2-02 | Product review |
| M2-07 | Webapp | BLOCKER | Replace SessionDebrief heuristics with backend `next_actions` | Audit P1/P3 | UI consumes API payload | Codex | M2-05 | E2E test |
| M2-08 | Webapp | BLOCKER | Build Strava-like Driver Profile v1 | User requested profile first-class | Profile page with trend, weaknesses, plan | Codex/Figma | M2-01 | Playwright smoke |
| M2-09 | Webapp | PARALLEL | Build recurring weaknesses panel | Required coaching memory UX | Panel with severity, confidence, last seen | Codex | M2-02 | Component tests |
| M2-10 | Webapp | PARALLEL | Make compare cases durable | Compare should become learning artifact | Saved compare case model/UI | Codex | M1-03 | Integration tests |
| M2-11 | Backend | BLOCKER | Build canonical ingestion endpoint v1 | Unifies upload/sync path | One ingestion lifecycle | Codex | M1-10 | Upload integration test |
| M2-12 | Desktop | PARALLEL | Implement explicit mode architecture design | Practice/Sprint/Endurance/Review | Mode policy interface | Codex | M1-11 | Unit tests |
| M2-13 | Desktop | PARALLEL | Curate overlay catalog into race-minimal/core/advanced | Keep all, reorganize, suppress streamer | Presets + config | Codex/Figma | M2-12 | Manual QA |
| M2-14 | Desktop | BLOCKER | Emit Bundle v2 compatible metadata | Desktop must feed brain | Bundle writer update | Codex | M1-03 | Evaluation gate extension |
| M2-15 | Mobile | BLOCKER | Implement crash-safe journal | Session survives restart | Active session persistence | Codex | M1-14 | Xcode tests |
| M2-16 | Mobile | BLOCKER | Implement preflight capture gates | GPS/storage/battery/permissions/track | Preflight state UI/API | Codex/Figma | M1-15 | UI/unit tests |
| M2-17 | Mobile | BLOCKER | Emit Bundle v2 compatible upload metadata | Mobile must feed brain | Upload payload schema | Codex | M1-03 | Upload contract test |
| M2-18 | Website | PARALLEL | Ship ecosystem architecture page | Critical for conversion clarity | Public page with diagram | Figma + Codex | M1-19 | Content QA |
| M2-19 | Website/webapp | BLOCKER | Decide and implement paid trial model | User wants no permanent free tier | 1-month trial, Racer/World-Class paid | Codex | None | Stripe test mode |
| M2-20 | Webapp/backend | BLOCKER | Stripe live path in test/staging | Paid beta needs billing | Checkout/portal/webhook verified | Codex | M2-19 | Webhook tests |

### Month 2 Exit Gate

Required:

1. A synced valid session can produce backend-owned `next_actions`.
2. Driver Profile v1 shows real backend memory.
3. Desktop and mobile emit or map to Bundle v2.
4. Stripe path works in test/staging.
5. Website explains the ecosystem accurately.

## 8. Month 3 - Public Beta and Paid Path

Objective: get real users into the sim-first loop and start gathering data.

### Scope Discipline

World-class environment for Month 3: sim.

Supported capture goal:
- iRacing and ACC live logging should be the reliable baseline.
- Other sim titles can start as file/import support or adapter backlog unless already stable.
- Do not promise full live support for all titles until smoke-tested.

### Month 3 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M3-01 | Ecosystem | BLOCKER | Automate E2E sim smoke | Beta cannot rely on manual hope | Smoke script/checklist | Codex | M1-20, M2-14 | Smoke pass |
| M3-02 | Desktop | BLOCKER | Build install/update beta flow | Sim users need low-friction start | Installer + download docs | Codex | M1-13 | Fresh machine test |
| M3-03 | Desktop | BLOCKER | Implement sync to canonical ingestion | Desktop feeds webapp automatically | Sync path | Codex | M2-11, M2-14 | E2E smoke |
| M3-04 | Webapp | BLOCKER | Build onboarding path after signup | Activation depends on first session | Checklist + logger download + sample data | Codex/Figma | M2-20 | Playwright test |
| M3-05 | Webapp | BLOCKER | Build first useful insight panel | Time-to-first-value | Insight + action + evidence | Codex | M2-05 | E2E test |
| M3-06 | Webapp | BLOCKER | Build ActionPrescription completion state | Closed loop needs driver intent | Mark planned/done/skipped | Codex | M2-03 | Integration tests |
| M3-07 | Backend | BLOCKER | Build ActionOutcome evaluator v1 | Detect whether prescribed weakness improved | Outcome job | Codex | M2-04 | Golden fixtures |
| M3-08 | Webapp | PARALLEL | Add training plan page v1 | Driver OS needs plan surface | Rolling plan view | Codex/Figma | M3-06 | Component/E2E |
| M3-09 | Backend | PARALLEL | Add readiness state skeleton | Universal readiness later; start simple | `DriverReadinessState` v0 | Codex | M2-01 | Unit tests |
| M3-10 | Website | BLOCKER | Launch waitlist/signup/logger funnel | Public beta needs conversion path | Updated CTA flow | Codex/Figma | M2-18 | Analytics events |
| M3-11 | Website | PARALLEL | SEO content cluster for beginner sim racers | Primary persona includes beginners | 8-12 articles/pages | Codex + human review | M2-18 | Content QA |
| M3-12 | Webapp/backend | BLOCKER | Turn on Stripe live for limited beta | Paid B2C path | Live checkout | Codex | M2-20 | Real low-value payment test |
| M3-13 | Ecosystem | BLOCKER | Add beta telemetry/feedback collection | Need learn fast | Feedback form + issue categories | Codex | M3-04 | User feedback visible |
| M3-14 | Mobile | PARALLEL | Field-test iOS capture reliability | Secondary persona, not blocker for sim beta | Trackside beta report | Codex | M2-15 | Test session review |
| M3-15 | Marketing | PARALLEL | Create public beta launch assets | Need momentum | Demo video, screenshots, copy | Figma/Claude/Codex | M3-04 | Manual review |

### Month 3 Exit Gate

Public beta can launch when:

1. A stranger can complete signup -> desktop install -> record -> sync -> web review without you in the loop.
2. Stripe live checkout works.
3. At least one coaching loop can complete from two sessions.
4. Session loss and sync failures are visible, not hidden.
5. Website claims match actual product state.

## 9. Month 4 - Sim-Real Bridge MVP and Live Mode Depth

Objective: make the bridge real, while deepening live desktop and mobile capture trust.

### Bridge Definition for Month 4

Minimum viable bridge:

1. User can manually link a sim session and a real session.
2. LAP can auto-suggest links when track, vehicle class, and objective are similar.
3. LAP compares higher-level traits and exact metrics where channels overlap.
4. LAP shows a transfer summary: what transferred, what did not, and what action to take next.

No claim of perfect physics equivalence.

### Month 4 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M4-01 | Backend | BLOCKER | Add `TransferLink` contract and DB table | Sim-real bridge depends on explicit entity | Migration + model + API | Codex | M1-05 | Integration tests |
| M4-02 | Backend | BLOCKER | Add manual link endpoint | MVP starts manual/hybrid | Link/unlink API | Codex | M4-01 | Integration tests |
| M4-03 | Backend | PARALLEL | Add auto-suggest link heuristic | Track/car/objective similarity | Suggestion endpoint | Codex | M4-01 | Fixture tests |
| M4-04 | Backend | BLOCKER | Define transfer metrics v1 | Shape vs intensity needs math | Metrics spec + functions | Codex | M4-01 | Golden fixtures |
| M4-05 | Webapp | BLOCKER | Build Transfer Summary Card | Bridge must be visible | Timeline/profile card | Codex/Figma | M4-02, M4-04 | E2E test |
| M4-06 | Webapp | PARALLEL | Add bridge timeline filter | User wants summary card + timeline | Timeline UI | Codex | M4-05 | UI test |
| M4-07 | Webapp | PARALLEL | Feed bridge findings into WeaknessEpisode | Bridge must affect coaching memory | Weakness source attribution | Codex | M4-04, M2-02 | Integration test |
| M4-08 | Mobile | BLOCKER | Improve timestamp normalization | RaceBox/GPS/CoreMotion skew hurts fusion | Reconciled timestamp layer | Codex | M2-15 | Unit tests with skew fixtures |
| M4-09 | Mobile | PARALLEL | Expand RaceBox parser beyond NAV-PVT | User wants full UBX coverage | Parser roadmap + priority messages | Codex | M4-08 | Parser tests |
| M4-10 | Mobile | PARALLEL | Build trackside trust cues | User requested live dashboard + post visual | GPS quality, lap, speed, G-G, sync | Figma/Codex | M2-16 | Device QA |
| M4-11 | Desktop | BLOCKER | Implement Practice/Sprint/Endurance mode policy v1 | User wants full architecture in 6mo | Mode-specific overlay/coaching/strategy defaults | Codex | M2-12 | Unit/manual QA |
| M4-12 | Desktop | BLOCKER | Serialize strategy plan vs actual execution | Needed for training execution score | Strategy events in bundle | Codex | M2-14 | Bundle tests |
| M4-13 | Desktop | PARALLEL | Implement pit-call lifecycle v1 | User wants armed in 6mo | Armed/deferred/committed/served states | Codex | M4-11 | Unit tests |
| M4-14 | Backend/webapp | PARALLEL | Show strategy execution score | Turns desktop events into coaching outcome | Score + review panel | Codex | M4-12 | Integration test |
| M4-15 | Website | PARALLEL | Publish sim-real bridge explainer without overclaiming | Bridge is real but early | Landing section/page | Figma/Codex | M4-05 | Content QA |

### Month 4 Exit Gate

Required:

1. At least 10 manually linked sim-real pairs can be analyzed.
2. Transfer summary produces actionable coaching, not just charts.
3. Desktop mode architecture works for practice/sprint/endurance.
4. Mobile can complete a field beta session without data loss.

## 10. Month 5 - Release Candidate Hardening

Objective: turn beta into a release candidate that can support strangers and paid customers.

### Month 5 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M5-01 | Ecosystem | BLOCKER | Run 50-stranger unattended beta | User wants product working beyond founder support | Beta cohort report | Human + Codex analysis | M3 launch | KPI review |
| M5-02 | Backend | BLOCKER | Performance pass on upload/analysis pipeline | Paid users need speed | p95 report + fixes | Codex | M3-01 | Load/smoke tests |
| M5-03 | Backend | BLOCKER | Add observability for ingestion/coaching jobs | Need know failures before users complain | Metrics/log dashboard | Codex | M2-11 | Alert test |
| M5-04 | Webapp | BLOCKER | Harden account/billing/subscription flows | Revenue path | Account billing UI | Codex | M3-12 | Stripe webhook test |
| M5-05 | Webapp | BLOCKER | Polish Driver Profile and Training Plan | Core Driver OS value | Release-quality UX | Figma/Codex | M3-08 | User tests |
| M5-06 | Webapp | PARALLEL | Add readiness score v1 | User wants universal readiness | Score with confidence and caveats | Codex | M3-09 | Fixture tests |
| M5-07 | Backend | PARALLEL | Basic ML experiment offline only | User wants basic ML, but not before data | Internal notebook/model report | Codex | Real beta data | Offline validation |
| M5-08 | Desktop | BLOCKER | Installer/release pipeline hardening | Serious sim racers need trust | Signed/reproducible release checklist if possible | Codex | M3-02 | Fresh install QA |
| M5-09 | Desktop | BLOCKER | Degraded-state UX for telemetry/coaching/strategy/sync | User hoped to prevent failures; product must still explain them | Clear failure banners and recovery | Codex/Figma | M4-11 | Manual QA |
| M5-10 | Mobile | BLOCKER | Release-candidate iOS capture path | Secondary persona trust | TestFlight candidate | Codex | M4-08 | Device test matrix |
| M5-11 | Mobile | PARALLEL | Android feasibility prototype | User wants Android, but release is risky | Decision memo + prototype if feasible | Codex | M5-10 not blocked | Prototype only |
| M5-12 | Mobile | PARALLEL | Wearable steering/HR experiment | Interesting, not release-critical | Research prototype | Codex | None | Do not block release |
| M5-13 | Website | BLOCKER | Full launch site content pass | Release needs coherent story | Pricing, product, demo, docs | Figma/Codex/Claude review | M5-05 | Content QA |
| M5-14 | Growth | PARALLEL | Launch SEO/community/content cadence | Need users for MRR target | Weekly publishing plan | Codex | M3-10 | Traffic dashboard |

### Month 5 Exit Gate

Release candidate needs:

1. 50 strangers can use the product unattended.
2. Billing/account flows work.
3. Upload/sync/coaching errors are observable and recoverable.
4. Core sim loop reaches release quality.
5. Mobile is at least TestFlight trustworthy for real-world capture.

## 11. Month 6 - Full Release and Growth Loop

Objective: release the coherent Driver OS and scale the feedback/revenue loop.

### Month 6 Tasks

| ID | Product | Type | Task | Context | Output | AI | Dependency | Validation |
|---|---|---|---|---|---|---|---|---|
| M6-01 | Ecosystem | BLOCKER | Full release readiness review | Prevent launch with hidden gaps | Go/no-go checklist | Codex + Claude review | M5 exit | Signed checklist |
| M6-02 | Webapp/backend | BLOCKER | Lock coaching-loop analytics | North Star must be visible | Dashboard for loops/prescriptions/outcomes | Codex | M3-07 | Dashboard QA |
| M6-03 | Backend | BLOCKER | Data retention and privacy cleanup | Paid product needs trust | Policy + enforcement jobs | Codex | Billing/account | Tests |
| M6-04 | Webapp | BLOCKER | Final conversion/account UX polish | Paid B2C target | Checkout and onboarding polish | Figma/Codex | M5-04 | E2E |
| M6-05 | Desktop | BLOCKER | Release desktop logger v1 | Sim-first public release | Installer + release notes | Codex | M5-08 | Fresh install |
| M6-06 | Mobile | PARALLEL | Release iOS capture beta or v1 | Secondary persona | App/TestFlight release | Codex | M5-10 | Device QA |
| M6-07 | Website | BLOCKER | Launch public narrative | Driver OS, not fake AI | Launch pages/content | Figma/Codex | M5-13 | Content QA |
| M6-08 | Growth | BLOCKER | Paid acquisition/community experiment | Need revenue, not only product | 3-5 channel experiments | Codex for copy/data | M6-07 | CAC/conversion report |
| M6-09 | Ecosystem | PARALLEL | B2B open-door package | User wants B2B next, not core now | Racing-school pitch deck + demo flow | Figma/Codex | M6-07 | 5 outreach targets |
| M6-10 | Ecosystem | BLOCKER | October 31 strategy review | Decide continue/sell/personal tool | Investor/acquisition/internal memo | Codex + human | Metrics | Final review |

### Month 6 Exit Gate

The 6-month plan is successful if:

1. The flagship coaching loop works for sim users.
2. Desktop capture/live assistant is reliable enough for serious sim racers.
3. Mobile can support real-life capture beta without session-loss embarrassment.
4. Sim-real bridge is real at MVP level.
5. Website tells one coherent story.
6. Paid path is live.
7. Weekly metrics show whether LAP is becoming a business or a personal masterpiece.

## 12. Backlog by Product

### Website Backlog

Priority order:

1. Fix current-state positioning.
2. Explain the ecosystem architecture.
3. Build waitlist/signup/logger download conversion path.
4. Remove or soften claims around AI coaching until backend coaching is real.
5. Rewrite pricing around free trial, Racer, World-Class.
6. Launch beginner-focused SEO content.
7. Produce public beta demo video.
8. Extract marketing site into standalone app/repo after Month 2 if it does not slow beta.

Recommended extraction:

- Keep Next.js if reusing current React/Three/GSAP assets.
- Consider Astro only if you intentionally simplify to mostly static content.
- Do not let extraction block Month 1-3 product work.

### Webapp/Backend Backlog

Priority order:

1. Contract authority.
2. Unified ingestion.
3. Driver identity and canonical timeline.
4. WeaknessEpisode.
5. ActionPrescription.
6. ActionOutcome.
7. Driver Profile.
8. Durable compare cases.
9. Training plans.
10. TransferLink.
11. Readiness score.
12. Strategy execution review.
13. Basic ML after data exists.

Kill or hide from core IA:

1. Admin/race-control for normal users.
2. Jobs page for normal users.
3. Exports as a primary nav concept.
4. Dev-plans style internal pages.

### Desktop Backlog

Priority order:

1. Runtime import/test stability.
2. Evaluation gate green.
3. Bundle v2 metadata.
4. Sync to canonical ingestion.
5. Mode architecture: Practice, Sprint, Endurance, Review.
6. Overlay curation.
7. Live prompts: pit, save fuel, push, slow down/incident ahead, cold tire warming, repeated corner mistake.
8. Strategy plan vs actual events.
9. Degraded-state UX.
10. Release installer hardening.

### Mobile Backlog

Priority order:

1. Never lose a session.
2. Safe initialization and finalize failure states.
3. Deterministic upload queue.
4. Preflight gates.
5. Timestamp reconciliation.
6. Bundle v2 metadata.
7. Trackside trust UI.
8. RaceBox parser expansion.
9. Local quick review.
10. Android and wearable prototypes only after iOS reliability.

## 13. Coaching System v1 Specification

### Mandatory Insight Structure

Every user-facing coaching insight must include:

1. Observation.
2. Evidence.
3. Likely cause.
4. Recommended action.
5. Measurable target.
6. Confidence.
7. Review-later condition.

### WeaknessEpisode v1

Minimum fields:

```text
weakness_episode_id
driver_id
weakness_type
category
first_seen_at
last_seen_at
recurrence_count
severity
confidence
affected_environments
affected_tracks
affected_vehicles
evidence_session_ids
status
last_prescription_id
```

Initial categories:

1. Technique.
2. Consistency.
3. Setup sensitivity.
4. Confidence/adaptation.
5. Race management.
6. Execution.

Prioritization:

1. Most coachable.
2. Most recurring.
3. Biggest time loss.

### ActionPrescription v1

Minimum fields:

```text
action_prescription_id
driver_id
weakness_episode_id
title
why_it_matters
action_steps
session_objective
target_context
success_condition
expected_gain
confidence
due_next_session
status
```

### ActionOutcome v1

Minimum fields:

```text
action_outcome_id
action_prescription_id
evaluation_session_id
completed_status
metric_before
metric_after
improved
confidence_delta
notes
```

## 14. Sim-Real Bridge v1 Specification

### TransferLink v1

Minimum fields:

```text
transfer_link_id
driver_id
sim_session_id
real_session_id
link_type
confidence
track_similarity
vehicle_similarity
objective_similarity
created_by
```

### Transfer Metrics v1

Start with metrics that can work across imperfect data:

1. Line shape similarity where GPS path exists.
2. Speed trace shape similarity by normalized distance.
3. Braking zone timing and release-shape similarity where brake input exists.
4. G-G envelope and percentile comparison.
5. Steering smoothness where available.
6. Consistency band comparison.
7. Confidence/adaptation delta between sim and real.

Bridge output should answer:

1. What transfers?
2. What fails to transfer?
3. Is the driver shape correct but intensity wrong?
4. What should they train next?

## 15. Race Strategy v1 Specification

Race strategy is a secondary differentiator, not the core product loop.

### Required Persistent Events

Persist these into finalized bundles:

1. Strategy plan created.
2. Target pace set.
3. Fuel target set.
4. Tire/stint target set.
5. Pit window opened.
6. Pit call armed.
7. Pit call deferred.
8. Pit call committed.
9. Pit service completed.
10. Save fuel prompt issued.
11. Push prompt issued.
12. Slowdown/incident prompt issued.
13. Cold tire warning issued.
14. Repeated corner-loss prompt issued.
15. User annotation before or after race.

### Strategy Review Output

The webapp should show:

1. Plan vs actual.
2. Execution score.
3. Time/fuel/tire consequences.
4. Next-time suggestion.

## 16. Weekly Execution Ritual

Every week:

1. Run the canonical smoke path.
2. Review KPI dashboard.
3. List top 3 blockers.
4. Decide what gets cut.
5. Ship one user-visible improvement.
6. Update roadmap risk notes.

Pivot criteria:

1. Public beta users cannot complete activation without help.
2. Coaching recommendations are perceived as generic.
3. Desktop or mobile loses sessions.
4. Website traffic converts but users do not activate.
5. Paid conversion is weak because value is unclear.

## 17. Immediate Next 10 Actions

Do these in order:

1. Freeze this roadmap as the working plan.
2. Create `docs/ecosystem_architecture.md`.
3. Create backend `contracts` package.
4. Define `SessionBundleV2`.
5. Fix webapp contract drift: duplicate bundle types, double `/api/v1`, duplicate channels route.
6. Fix desktop live processor and QML bootstrap gate.
7. Fix mobile finalize/session-loss P0s.
8. Create E2E smoke path.
9. Draft coaching library categories.
10. Build backend `WeaknessEpisode` and `ActionPrescription` MVP.

## 18. Non-Compromises

Do not compromise on:

1. No hidden session loss.
2. No fake AI coaching claims.
3. No four-product fragmentation.
4. No user-facing coaching without evidence/confidence.
5. No broad feature sprawl before the flagship loop works.

1. The product model you should commit to
Website

Role: positioning, trust, ecosystem explanation, conversion, waitlist, and download routing.
It should never become operational product logic. Your own answers say this, and the audit says the current site under-explains the ecosystem and over-indexes on story over system clarity.

Webapp

Role: the system of record and the driver intelligence layer.
This is where the deep coaching belongs: driver profile, recurring weakness memory, intervention tracking, next-session plans, progression, sim↔real linking, event prep, performance/readiness models, and durable review artifacts. That matches both your answers and the audit’s recommended ownership.

Desktop app

Role: real-time, race-critical, low-latency execution.
It should own telemetry capture, overlays, live reminders, live strategy prompts, and immediate packaging/sync. It should not become the place where long-term driver evaluation lives.

Mobile app

Role: real-life capture companion + field logistics.
It should be trusted at trackside, offline-first, sync-safe, simple, and robust. Your own answers prioritize “never lose a session,” strict offline behavior, capture reliability, and quick local validation.

2. The one strategic sentence for the next 6 months

Build LAP as a sim-first driver-improvement system with a cloud-owned coaching brain, while shipping a credible sim↔real bridge and bulletproof capture clients.

That is the cleanest synthesis of:

your persona choice: sim racer first, amateur real-life racer second,
your product ambition: coaching and strategy, not generic tooling,
your architecture doctrine: server = brain,
and the audit’s warning that today LAP is still too fragmented and too client-heavy.
3. The actual 6-month strategy
Phase 1 — Month 1
Make the ecosystem reliable and contract-driven

This is the serialization point for everything else. The audit repeatedly says the ecosystem promise depends on a canonical pipeline, shared contracts, and moving business logic out of clients.

Goals
Define the canonical session bundle and shared schema layer.
Unify ingestion for desktop and mobile.
Remove obvious repo-boundary violations.
Stop the biggest trust-destroyers.
Must-do tasks

Web/backend

Choose and implement shared schema system: Pydantic models + JSON Schema + generated TS types.
Define canonical objects: SessionManifest, TelemetryChunk, Insight, DriverProfile, WeaknessEpisode, ActionPrescription, BridgeLink.
Make the API the final owner of:
session finalization
canonical identity
coaching insight generation
error schema for sync/upload failures

Desktop

Keep local capture/overlay stable.
Strip out anything that behaves like long-term intelligence.
Ensure packaging/sync uses the canonical contract.

Mobile

Make the first sprint “never lose a session.”
Ship crash-safe journal, deterministic upload queue, explicit corrupt-local states, safe stop UX, and force-unwrap removal. Those are already explicitly marked as non-negotiable in your questionnaire.

Website

Publish an explicit ecosystem architecture page.
Clean up messaging contradictions.
Stop promising AI coaching before the system is hardened. That is also directly aligned with your own answer.
AI allocation
Claude Code: contract design, cross-repo refactors, backend/domain modeling.
Copilot: repetitive typing, small repo-local cleanups, test scaffolding.
Codex: repo-wide audit passes, consistency checks, migration checklists.
Figma / design AI: website IA and ecosystem explanation visuals only after the architecture is frozen.
Phase 2 — Month 2
Close the first real product loop

This month is about one golden path:

discover → sign up → download client → record session → sync → review session in webapp → receive one clear next action

The audit calls the current first-time workflow fragmented.

Must-do tasks

Website

Persona-routed CTA system: sim racer vs real-life racer.
Dedicated “How LAP works” page with explicit app roles.
Proof block with screenshots of desktop/webapp/mobile.

Webapp

Build the first serious driver profile page.
Add first-class backend objects for:
recurring weakness
action prescription
action outcome
This is almost exactly what the audit recommends.

Desktop

End session → package → upload → cloud confirmation.
Show sync status clearly.

Mobile

Start / stop / validate / sync with local review.
Trackside trust cues: dashboard, local trace/map, clear quality/sync state.
Deliverable at end of Month 2

A user can complete a session and see:

what went wrong,
whether this weakness already existed,
what to do next session,
whether this is improving over time.

That is the first moment LAP starts feeling like a coaching product instead of a telemetry utility.

Phase 3 — Month 3
Public beta: sim-first coaching product

You already set a target of public beta in 3 months.

Must-do tasks

Webapp

Launch Coaching Memory MVP
recurring weakness timeline
prescribed actions
last action result
confidence/trend
Launch first version of the Improvement Plan
weekly focus
session objective
review cadence
next best drill / next best race goal

Desktop

Stabilize live coaching surface and strategy surface.
Ensure anything rendered live is consuming structured insight objects, not computing its own interpretation.

Website

Beta landing page with:
sim-first clarity
ecosystem map
explicit product maturity statement
waitlist / beta signup / logger download funnel
AI allocation
Claude Code: coaching-memory object model, progression logic, state machines.
Copilot: component plumbing, UI glue, tests.
Codex: product consistency audits between desktop/webapp/backend.
Phase 4 — Month 4
Build the first true driver-intelligence layer

This is where you start earning the Garmin/Runna comparison.

Must-do tasks

Webapp/backend

Create a Driver Evaluation Model v1:
consistency
control smoothness
brake release quality
line repeatability
setup sensitivity
strategy execution quality
Add readiness / confidence / trend states.
Add event prep mode for a target race/session.
Add predicted performance band for selected contexts.

This is still rules + heuristics + basic ML at most, which matches your questionnaire: basic ML in 6 months, avoid LLM-as-core-text layer.

Important constraint

Do not chase fancy predictive science too early. Your own questionnaire deprioritizes heavy ML, and the audit explicitly says advanced predictive models should wait until contracts and workflow closure are stable.

Phase 5 — Month 5
Ship the sim↔real bridge MVP and full release candidate

You said the bridge is real and non-negotiable, and your preferred minimum viable bridge is essentially the same metrics of analysis across environments.

Bridge MVP definition

Do not try to solve full transfer intelligence yet.

Ship:

manual/hybrid session linking
shared driver traits across environments
side-by-side comparable metrics
“shape vs intensity” commentary
bridge findings stored as inputs into coaching memory

That is also very close to the audit’s recommended MVP.

Full release candidate scope

By the end of Month 5, a serious user should be able to:

capture reliably in sim and real life
sync into one account
review sessions in one web timeline
receive recurring coaching themes
follow an improvement plan
see first bridge signals between sim and real

That is enough for the first serious release.

Phase 6 — Month 6
Optimize retention, expand supported surfaces, harden product economics
Must-do tasks
Improve driver profile and progression UX.
Add retention loops:
weekly coaching summary
“you improved this trait” notifications
event prep reminders
missed-goal nudges
Expand supported sims only if the ingest pipeline is stable.
Finalize pricing/plan enforcement and usage gating.
Do not do in Month 6
massive visual redesign
autonomous AI coach
complex neural models
broad partnerships
team-coach/B2B-first pivot

Those would dilute the core loop.

4. Recommended KPI system

Because your KPI section is not fully locked yet, I’d treat this as the proposed default operating system.

North Star Metric

Weekly Active Drivers completing the coaching loop

Definition:
user records or uploads a session → session is processed → user views review → user gets a next action / plan step.

Why this metric:
it rewards the exact product you want to build — not raw uploads, not pageviews, but completed learning loops.

Per-repo primary KPI
Website

Visitor → qualified action conversion

waitlist signup
demo request
logger download
beta signup
Webapp

Reviewed sessions that turn into an action

% processed sessions opened
% reviewed sessions with next action delivered
% users with at least one recurring weakness object
% users returning to check progression within 7 days
Desktop

Race-critical reliability

successful session capture rate
upload completion rate
session available in cloud within X minutes
live overlay crash-free session rate
Mobile

Never-lose-session reliability

session loss rate
corrupt_local rate
pending uploads >24h
session visible locally immediately after stop
session visible in cloud within 1h when network exists
Suggested target values by Month 6
Reliability
Desktop successful session capture: 99.5%+
Mobile session loss: <0.5%
Sync failure after retry window: <1%
Processing success: 98%+
Product loop
60%+ of processed sessions get opened
35%+ of opened sessions produce a saved next action
25%+ of active users complete at least 2 coaching loops per month
20%+ of active users return for progression review weekly
Conversion
Website visitor → qualified action: 3–8%
Signup → first session recorded: 25–40%
First session → first review opened: 60%+

These are hard but credible for an early serious niche product.

5. What gets delegated to the webapp

You asked this earlier, and after the questionnaire + audit, the answer is now very clean.

The webapp should own
driver identity
driver profile
canonical session timeline
recurring weakness memory
intervention history
next-session prescriptions
improvement plan
event prep mode
strategy review history
sim↔real bridge artifacts
progression/readiness/confidence/performance prediction
durable review pages and sharing/export surfaces
The webapp should not own
low-latency race prompts
live overlays
trackside capture-critical UX
anything that breaks when offline and therefore must be local-first

That division is exactly what your architecture doctrine and audit both point toward.

6. What to explicitly deprioritize

Your questionnaire already hints at some of this, and I agree strongly.

Deprioritize for 6 months
heavy ML / labeled-data ambitions
LLM-generated coaching as a core differentiator
a huge visual redesign before contracts stabilize
team-coach / pro / expensive semi-pro buyer as the main persona
multi-partner expansion in the first phase
7. The biggest execution truth

The audits are basically saying this:

your foundations are better than your product loop.

You already have meaningful capture and session tooling, but the real gap is:

remembering weaknesses,
connecting sessions over time,
prescribing what to do next,
proving improvement,
and linking sim to real in a structured way.

So the next 6 months should not be “add more features everywhere.”

They should be:

unify contracts
centralize intelligence
close the learning loop
only then expand breadth
8. My blunt conclusion

You are not building four equal apps.

You are building:

one intelligence product: the webapp/backend
two acquisition/execution surfaces: desktop and mobile
one narrative shell: the website

That is the mental model that will keep you from drowning.

This is a highly ambitious, beautifully ruthless set of answers. You’ve successfully cut the fat: you are building a "Garmin for drivers," you are centralizing the "brain" in the cloud, you are targeting the sim-racer first (with real-life as the secondary persona), and you are doing it solo via a massive AI-multiplier.

If you are putting in 50–60 hours a week and using Cursor/Claude to achieve a 10x-20x velocity, the biggest risk isn't writing the code—it's context switching and integration drift.

Here is your ruthless 6-month, repo-by-repo development roadmap to get LAP to a paid public launch.

The AI Stack for this Sprint
Architecture & Schema Design (The "Brain"): Use Claude 3.5 Sonnet / Claude 3.7 Sonnet in the web interface (using Projects with your codebase uploaded as context). It is unmatched for designing cross-repo JSON schemas and Python/TypeScript typing.

Heavy Coding & Refactoring: Cursor (with Claude Sonnet or GPT-4o). Use Composer/multi-file edit for the massive refactors (like stripping heuristics out of the frontends).

UI/UX Prototyping: v0 by Vercel or Claude Artifacts for generating the new Strava-like driver profile and marketing site pages before integrating them into your Next.js repos.

Mobile (Swift) & Desktop (Qt/QML) Debugging: Cursor + Claude. Claude is exceptionally good at finding Swift concurrency issues and QML binding bugs.

Month 1: Stop the Bleeding & Lay the Foundation
Theme: Fix the P0 bugs, split the monoliths, and stabilize the capture layer. You cannot build a brain if the sensory organs are dying.

Backend (lap_tool_virtualisation / lap_web API)

Task 1 [BLOCKING]: Define the canonical Bundle v2 JSON schema and ULID format for all sessions. (AI: Claude Web to generate the strict JSON/Pydantic schemas).

Task 2 [PARALLEL]: Merge sessions_v2 and sync_upload into a single, canonical ingestion pipeline.

Mobile (lap_mobile - iOS)

Task 3 [BLOCKING]: Fix the crash-on-init (LapCoachAppModel.live() force-unwraps and StorageService() try!). (AI: Cursor inline).

Task 4 [BLOCKING]: Fix the finalizeSession silent success bug. It MUST mark corrupt_local if the temp file is missing.

Task 5 [PARALLEL]: Change UX to require a long-press/explicit stop to prevent fullScreenCover dismissal from killing a session.

Desktop (lap-coach-logger - Qt/QML/Python)

Task 6 [BLOCKING]: Rip and rebuild the live_telemetry_processor import break. Restore CI green status. (AI: Cursor codebase scan).

Task 7 [PARALLEL]: Fix the QML bootstrap test failures and UI-coupled settings-save bugs.

Web & Marketing (lap-website)

Task 8 [PARALLEL]: Extract the marketing site out of the main Next.js app into a standalone Astro or lightweight Next.js repo. (AI: v0 for rapid scaffolding).

Task 9 [PARALLEL]: Clean up the /api/v1 double-prefixes and duplicate session-channels routes in the core webapp.

Month 2: The "Brain" Migration
Theme: Shift all intelligence from the clients to the server. The clients become dumb, fast rendering engines.

Backend (API & Workers)

Task 1 [BLOCKING]: Create the database models and API endpoints for the 3 core objects: DriverProgressSnapshot, WeaknessEpisode, and ActionPrescription. (AI: Claude Web for DB schema design).

Task 2 [BLOCKING]: Build the deterministic rules engine that generates the next_actions payload based on telemetry thresholds.

Webapp (lap-website - App Router)

Task 3 [BLOCKING]: Delete all local Next.js SessionDebrief heuristics. Wire the frontend to strictly consume the backend's next_actions and WeaknessEpisode payloads. (AI: Cursor Composer to rewrite the React hooks).

Task 4 [PARALLEL]: Build the V1 "Strava-like" Driver Profile page.

Desktop & Mobile

Task 5 [PARALLEL]: Strip complex track mapping, sector math, and local coaching heuristics from both mobile and desktop. Pass raw telemetry straight to the new unified backend ingestion endpoint.

Month 3: The Core Coaching Loop & Reliability
Theme: "Never lose a session" and closing the loop. You should be able to drive, upload, and instantly get an accurate ActionPrescription.

Mobile (lap_mobile)

Task 1 [BLOCKING]: Implement the crash-safe session journal. Persist active state every N seconds to disk.

Task 2 [BLOCKING]: Build the deterministic background upload queue worker that auto-resumes on app launch. (AI: Claude to architect the Swift background tasks).

Task 3 [PARALLEL]: Implement preflight readiness gating (GPS quality, Storage, Track Selection).

Backend & Webapp

Task 4 [PARALLEL]: Implement the overarching Driver Score model (Elo/Rating system) and percentile peer-benchmarking logic.

Task 5 [PARALLEL]: Build the "Durable Compare" flow. Stop using transient URL params; allow users to save a side-by-side comparison as a learning artifact.

Month 4: Live Assistant & The Sim ↔ Real Bridge
Theme: Making the desktop app a race engineer and building your ultimate moat (the bridge).

Desktop (lap-coach-logger)

Task 1 [BLOCKING]: Implement explicit runtime modes (Practice, Sprint, Endurance) with associated overlay layouts. (AI: Cursor for QML state machines).

Task 2 [PARALLEL]: Build the V1 pit-call lifecycle state machine (Armed -> Commit -> Served).

Task 3 [PARALLEL]: Serialize the "Strategy Plan vs. Actual Execution" into the finalized bundle to grade race execution.

Backend (The Bridge)

Task 4 [BLOCKING]: Build the TransferLink math. Create the algorithms that compare a Sim session's telemetry shape (e.g., trail braking curve) to a Real session, flagging where "shape matches but intensity diverges." (AI: Claude Data Analysis/Python for Pandas/Numpy algorithm generation).

Month 5: Premium Features & Marketing Engine
Theme: Packaging the intelligence so it looks like a €20/month product.

Webapp (lap-website)

Task 1 [BLOCKING]: Integrate Stripe. Set up the 12-20€/month tiers (with the 1-3 month free trial flow). (AI: Cursor to implement Stripe checkout and webhook listeners).

Task 2 [PARALLEL]: Build the "Next Session / Weekly Plan" generator UI based on user goals and target events (fetching iRacing calendars).

Task 3 [PARALLEL]: Finalize the premium coaching language (translating raw data into plain English advice).

Website (Marketing Repo)

Task 4 [PARALLEL]: Rewrite the copy to explicitly sell the "Driver OS / Garmin for Drivers" dream. (AI: Claude 3.5 Sonnet for copywriting).

Task 5 [PARALLEL]: Build the visual "How LAP Works" ecosystem architecture page. Open the Waitlist/Beta signup form.

Month 6: The Crucible (Smoke Tests & Launch)
Theme: Bug hunting, end-to-end reliability, and public release. No new features.

All Repositories (QA & Ops)

Task 1 [BLOCKING]: Write and pass the explicit E2E smoke path: Sim Detect → Record → Finalize → Sync → Web Review → Action Prescription. (AI: Cursor/Playwright for E2E web testing, XCTest for mobile).

Task 2 [BLOCKING]: Setup a staging environment to test Mobile -> API -> Web flows simultaneously.

Task 3 [PARALLEL]: Expand the RaceBox parser in the mobile app to full UBX class coverage to match desktop data fidelity.

Task 4 [PARALLEL]: Polish the track-side Mobile UX (live dashboard, quick post-session visualizations).

Task 5 [MILESTONE]: Launch the Public Beta. Onboard the first 500-5000 users. Support them manually if needed to ensure the coaching loop actually changes their behavior.
