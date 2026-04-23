# LAP — Strategic Doctrine (6 months: 2026-04-23 → 2026-10-31)

**Status:** ratified from the 198-question questionnaire dated 2026-04-23.
**Owner:** Solo founder + AI-assisted (Claude Code, Codex/Copilot, Figma, Claude Design).
**Runway:** ship-or-die. Public beta by end of Month 3 (2026-07-23). V1 by end of Month 5 (2026-09-23). Paid product by 2026-10-31.

---

## 1. Mission (one sentence)

> LAP is the Garmin-for-drivers: a cross-platform Driver OS that turns every sim and real-world session into a personalized development plan the driver can actually execute.

## 2. Product identity

**We sell:** cross-surface driver progression.
**We do not sell:** a logger. A viewer. A strategy widget. An AI coach. We sell the loop that makes drivers measurably better over months.

**Tagline options (pick one in Month 1):**
- "The Driver OS — train, race, improve."
- "Every lap, one step better."
- "Your driving, measured. Your progress, engineered."

## 3. Target persona

### Primary (100% of product decisions weighted to this persona)

**The Serious Sim Racer.**
- Races iRacing, ACC, ACE, rF2, AMS2, LMU, Rennsport, F1 games.
- 3-8 sessions per week.
- Already competitive within their split/class.
- Has tried Garage61 / RaceLab / MoTeC. Found them either too shallow (Garage61) or too pro-engineer (MoTeC).
- Wants to know *what to practice this week*, not *what a turn-by-turn lap report looks like*.
- Spends €30-80/month on sim hardware/sub already. €15/month is in-budget.

### Secondary (scoped, EU-only, capture-only)

**The Amateur Real-World Racer / Track-day Enthusiast.**
- RaceBox owner or phone-capture capable.
- Does 1-4 track days per year + regular karting.
- Treats LAP as the serious logger that replaces RaceChrono Pro + a spreadsheet.

### Anti-personas (explicitly refused)

- Professional racing team engineers → MoTeC exists.
- Pro drivers with dedicated coaches → we are not trying to replace Driver61.
- Expensive semi-pro category → wrong price point, wrong expectations.
- Casual "one session a month" phone users → wrong retention profile.

## 4. The seven principles of LAP

1. **Server owns the brain. Clients are thin.** Coaching insights, thresholds, weakness detection, next-session plans, benchmarks — all live in the backend. Desktop and mobile render what the backend emits; they do not decide.
2. **One canonical session format.** Bundle v2, everywhere, day one. Sim, real, mobile, desktop — same manifest, same schema, same checksums.
3. **Never lose a session.** Any capture that started must either finalize safely or be surfaced to the user as recoverable / corrupt. Silent success on missing files is a P0 bug.
4. **Deterministic before statistical. Statistical before generative.** Rule-based coaching first (built from a coaching library we own). Basic ML (regressions, percentiles) next. No LLM in coaching text — ever, in this 6-month plan.
5. **Offline-first on capture. Cloud-first on intelligence.** Desktop and mobile capture must work with zero network. Coaching views, progression, and benchmarks are cloud-only by design; they don't work offline, and we say so.
6. **The loop closes or the feature doesn't ship.** Every coaching insight ships with: observation → evidence → likely cause → prescribed action → measurable success condition → review-next-session. Incomplete insights are hidden.
7. **Sim ↔ Real is a data model, not a marketing claim.** `TransferLink` is a first-class entity. If we can't link sessions at the data layer, we don't claim the bridge publicly.

## 5. What LAP does / does not do in 6 months

### DOES

- Capture sim sessions (iRacing, ACC, AC, AMS2, rF2, LMU, Rennsport, F1 games).
- Capture real-life sessions (RaceBox + iPhone, Android by Month 5-6).
- Live overlays during sessions (desktop).
- Live lightweight coaching prompts (desktop + mobile).
- Live race strategy (sprint + endurance, armed pit-call, no full state machine yet).
- Finalize + sync sessions with integrity guarantees.
- Backend-generated `WeaknessEpisode`, `ActionPrescription`, `ActionOutcome`, `DriverProgressSnapshot`.
- Unified Driver Timeline across sim + real.
- Sim↔real `TransferLink` with side-by-side shape/intensity comparison.
- Next-session plans with measurable success conditions.
- Coaching library with 80-150 rules covering beginner → advanced.
- Auto-ingest iRacing weekly/special event calendars to suggest target events.

### DOES NOT

- Social features (leaderboards, friend-compare, sharing). Deferred to Q1 2027.
- Fully autonomous AI coaching text (LLM generation). Never in this plan.
- Multi-car live broadcast / streaming. Out of scope.
- MoTeC-grade engineering analysis surfaces (FFT, suspension travel analysis, etc.).
- Full pit-call lifecycle state machine (armed + confirmed + executed + deferred). We ship "armed" only.
- Driver swap / multi-driver endurance beyond bundle-level metadata.
- Android app in Month 1-4 (port starts Month 5).
- Full peer benchmarking (we have no cohort data yet — single-user mode for the first 3 months, cohort opens at Month 4+ once paying users exist).
- EventPerformancePrediction (lap-time ceiling prediction). Year 2.
- Fully autonomous race engineer.
- B2B dashboards for teams/schools (door open, no roadmap slot).

## 6. Strategic cuts (versus the audit)

The audit scoped ~18-26 person-months of work for a 4-5 person team. You have one person + AI. Cuts are mandatory.

| Audit recommendation | Action | Why |
|---|---|---|
| Full pit-call state machine | Cut to "armed" signal only | Full FSM is a quarter of work, low user payoff in 6mo |
| Android port early | Deferred to Month 5-6 | iOS parity matters first; Android split dilutes focus |
| Race-engineering-grade analysis | Deferred | Wrong persona |
| LLM coaching narrative | Rejected | Trust cost > benefit at this stage |
| Heavy ML / neural models | Rejected | Labeling cost > ROI in 6mo |
| Peer benchmarking at launch | Deferred to Month 4+ | No cohort data exists yet |
| Full endurance workflow (stint handoffs, driver swaps) | Deferred | Sprint/endurance *events* ship; dedicated endurance UX does not |
| EventPerformancePrediction | Deferred | Too risky/unreliable |
| Fully rebuilt desktop mode architecture | Partial | Ship 4 intent modes (Practice / Sprint / Endurance / Review); don't rewrite session FSM |

## 7. Bets

1. **Coaching library is a moat.** 80-150 rules written by us, curated, tested against real sessions. Basic ML augments. No generative AI. This is defensible because it's work Garage61/RaceLab haven't done.
2. **Cross-platform ecosystem is a moat.** One user, one identity, sim + real + mobile + desktop. Garage61 is sim-only. RaceChrono is real-only. Nobody bridges.
3. **Price moat.** €15/month single tier is 3-5x below per-sim coaching ($80-150/hr human coach) and 2x below Racing Republic equivalents. No free tier beyond trial reduces churn and signals seriousness.
4. **Public beta at Month 3 forces discipline.** A hard external deadline stops us from endlessly polishing.

## 8. Pricing & monetization

- **Pricing:** €15/month or €150/year (≈€12.50/month). Single tier.
- **Trial:** 14-day full-feature free trial (pick 14 over 30 — higher urgency, same conversion in practice for prosumer SaaS).
- **No free tier** beyond trial.
- **Stripe live:** Month 1, Week 3.
- **B2B (racing schools, karting academies):** door open, outbound starts only in Month 5. No roadmap feature work in 6mo beyond multi-seat billing which is a Month 6 item if inbound demand appears.
- **Existing pre-launch signups (waitlist):** grandfathered at €12/month for 12 months as a loyalty signal.

## 9. Launch moments

| Date | Event | What ships |
|---|---|---|
| 2026-05-22 (end M1) | **Internal alpha** | Backend contract layer + webapp Driver Timeline skeleton + desktop P0 fixes merged |
| 2026-06-22 (end M2) | **Closed private beta** (≤30 invited sim racers) | Coaching Memory MVP (top 3 backend objects), desktop mode system, mobile Sprint 1 shipped |
| 2026-07-23 (end M3) | **Public beta** | Stripe live, webapp Driver OS v1, marketing site standalone, sim↔real MVP |
| 2026-09-23 (end M5) | **V1 release** | Android app, Apple Watch/WearOS companion, coaching library v1 (100+ rules), endurance events support |
| 2026-10-31 (end M6) | **Paid target hit** | 1000+ paying users, €10k MRR trajectory, B2B outbound opened |

## 10. What we will not compromise on

From Q195 + derived from answers:

1. **Never lose a session** — any capture that started either finalizes correctly or is surfaced as recoverable. Silent failure is a merge-blocking bug.
2. **Server owns the brain** — no new client-side coaching logic shipped after Month 1. Any existing client logic migrates or gets deleted.
3. **€15/month core tier** — price does not move up during the 6 months, even if B2B demands different tier.
4. **No LLMs in user-facing coaching text** — the moment we generate coaching narrative with an LLM, we lose the trust differentiator against "AI coach" competitors.
5. **Grandfathered early users** — any change to pricing or feature availability preserves terms for pre-launch waitlist signups.
6. **Offline capture on desktop and mobile** — if a feature requires cloud to capture, we don't ship it in the capture client.

## 11. The one thing that scares us most (honest)

The bridge between sim and real becomes marketing-only because we never get enough real-world sessions in the data to validate `TransferLink` logic. Mitigation: Month 4 we force-run a "sim↔real labeled pairs" data collection push using our own real sessions (the Sebring/Silverstone/VLN/Red Bull Ring sim + real track day data already in `LapCoachLogger_sessions/`).
