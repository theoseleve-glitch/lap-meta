# LAP — Risk Register

Top 10 ways this plan dies. Each with a trigger signal, mitigation, and the rollback action if mitigation fails.

---

## R-01 — Contract registry becomes the single point of failure

**Probability:** High.
**Impact:** Catastrophic — blocks all downstream work.

**What could happen:** `lap-schemas` Pydantic changes break TS or Swift codegen silently. Webapp or mobile ships with stale types. Backend rejects valid clients.

**Early signals:**
- CI fails with "generated types out of sync" more than once a week
- A single merge in Week 3 of M1 ripples into >10 downstream PRs

**Mitigation:**
- Dedicated CI job blocks PRs that mutate Pydantic without regenerated TS+Swift artifacts checked in.
- Breaking changes require semver bump in `lap-schemas` package version.
- Weekly "schema health" check: are all four consumers on the same major version?

**Rollback:** fall back to manually maintained TS types in `lap-webapp` + Swift types in `lap-mobile`; accept 2 weeks of duplicated work while the codegen gets fixed. Never block product velocity on codegen issues.

---

## R-02 — Coaching library false-positive rate > 10%

**Probability:** Medium.
**Impact:** High — kills product trust. Users churn fast when the coach is wrong.

**What could happen:** Rules misfire. "You're braking late at T1" triggers on a corner where the driver is actually doing the correct late-apex line. User loses trust.

**Early signals:**
- Beta users flag insights as "not actually a weakness" at >10% rate (instrument this with a thumbs-down button in the coaching card)
- Specific rules dominate false-positive complaints

**Mitigation:**
- Every new rule tested against ≥3 archived sessions before shipping
- Confidence gating: rules only fire at full strength after N corroborating sessions
- User-flagged false positives auto-disable the rule at the user level, flag for review
- Monthly "rule audit" — top 10 highest-false-positive rules get rewritten or removed

**Rollback:** disable a rule globally via a feature flag without a deploy. Coaching library is data-driven, not code-driven.

---

## R-03 — Ship-or-die runway is real; MRR target is missed

**Probability:** Medium-High.
**Impact:** Existential.

**What could happen:** 1000 paying users target (€10K+ MRR) is missed. Revenue covers €400/mo cost but doesn't sustain you as a full-time founder.

**Early signals:**
- At M3 (public beta), trial-to-paid conversion <10% after 4 weeks
- At M4, paying users <150 (25% of the 1000 target milestone at 40% of the time)
- CAC (even at €0 paid ads) runs >€20 effective when you count the waitlist-acquisition marketing time

**Mitigation:**
- Weekly conversion dashboard, alert on drop
- Willingness to push pricing down to €10/mo if elasticity data supports it
- B2B door opens earlier (M4 instead of M5) if B2C undershoots
- Paid ad experiments at M5 (€500 budget) to test scale of acquisition

**Rollback:**
- If at M5 you have <300 paying users, activate "Plan B": pause major feature work, focus on conversion optimization + content marketing push + one B2B close.
- If at M6 you have <500 paying users, acknowledge commercial miss and shift horizon (personal tool / acquisition / continue bootstrapping on reduced scope).

---

## R-04 — Solo burnout in Months 3-4

**Probability:** Medium-High.
**Impact:** High — all progress stops if you stop.

**What could happen:** 50-60h/week sustained for 6 months with ship-or-die pressure + public beta launch pressure + August break disruption = burnout around weeks 12-16.

**Early signals:**
- Commit velocity drops below 70% of M1-M2 average
- Sleep <6h 3+ nights/week
- Skipping meals, neglecting exercise
- Feature momentum stalls even when code is flowing
- Emotional response: "I hate this project" thoughts more than once a week

**Mitigation:**
- Hard weekly cap: no more than 55h/week averaged over 4 weeks
- One fully off day per week, non-negotiable (not negotiable with yourself)
- Defer weakest-ROI tasks before adding hours
- The August 10-day break is a feature, not a bug — protect it
- Monthly "am I OK?" self-check written to a private journal

**Rollback:**
- If burnout hits: immediately descope to must-ship-only. Cancel planned features. Ship V0.5 if needed.
- The 6-month plan has optional items (WearOS, paid ads, B2B scaffold, 150-rule target) — delete them, not sleep.

---

## R-05 — Beta launch reveals fundamental UX wrong

**Probability:** Medium.
**Impact:** High — could force 1-2 month replan.

**What could happen:** At M3 beta, users don't convert because the Driver OS interface doesn't match how they think. Coaching insights are shown but ignored. Prescriptions are proposed but not accepted.

**Early signals:**
- Activation rate <30% at 2 weeks into beta
- Time-to-first-insight >20 minutes (vs 8min target)
- Prescription acceptance rate <30%
- User interviews surface confusion about what to do next

**Mitigation:**
- Alpha test (M1 internal) with 3 trusted sim racers before public beta
- User interview budget: 5 users/week during beta, 30 min each
- Hot-swap prompts via feature flags to A/B test messaging
- The `next_actions` API makes UI decisions server-side, so frontend changes are cheap

**Rollback:** if UX is fundamentally off, pause feature work for 2 weeks, redesign onboarding + Coaching view based on user interviews. Accept the slip to public-beta Month 4. Do NOT launch publicly with a broken UX.

---

## R-06 — Sim↔real bridge fails to produce useful reports

**Probability:** Medium.
**Impact:** Medium-High — the bridge is a key differentiator.

**What could happen:** Shape/intensity match algorithm produces reports that are technically correct but not actionable. Users rate transfer reports "not useful" at >50%.

**Early signals:**
- Transfer reports at M4 consistently flag divergences that users say "yeah, I know, that's because real-life is different"
- `TransferLink` auto-suggest picks wrong pairs
- Users stop engaging with bridge reports after trying once

**Mitigation:**
- Month 4 Week 1: use your own archived sim+real sessions as ground-truth test set
- Involve 3-5 real-world sim-racer users as bridge co-designers during M3
- Bridge report structure is modular — fixable section by section

**Rollback:** if at M4 end the bridge is weak, reposition: "sim vs real comparison" instead of "transfer coaching". Rename TransferReport to ComparisonReport. Drop the "what transfers" claim. Keep the data model as a longitudinal tracking feature, defer the coaching-on-bridge to Year 2.

---

## R-07 — Mobile reliability sprint underdelivers

**Probability:** Medium.
**Impact:** High — "never lose a session" is non-negotiable per doctrine.

**What could happen:** Capture journal, upload queue, or finalize integrity has a corner-case bug that causes session loss in the wild. Users report it. Trust breaks.

**Early signals:**
- Sentry captures crashes during capture
- Beta users report "I did a session but it's not there"
- Upload failure rate >5% sustained

**Mitigation:**
- Dedicated test suite for every failure scenario listed in Q107 (file missing, partial, corrupt, unsynced, inaccurate timestamps, wrong track map, wrong lap segmentation)
- Failure-injection CI tests: force-kill app mid-recording, disconnect network mid-upload, run out of storage, battery < 5%
- User-visible recovery UI as last line of defense: even if all else fails, the raw telemetry file sits on disk and the user can recover via webapp upload

**Rollback:** if at M2 end mobile reliability still has known issues, delay mobile public beta by 4-6 weeks. Desktop is primary capture surface anyway. Mobile can launch with iOS 17 at M3 internally, public at M4.

---

## R-08 — Android + WearOS in one month blows up

**Probability:** High for scope slip.
**Impact:** Low-Medium — Android is secondary persona at this stage.

**What could happen:** Android scaffold takes longer than expected. WearOS port is blocked on WearOS+Android integration. V1 release at M5 ships without Android or Watch.

**Early signals:**
- M5 Week 1: Android capture pipeline not working end-to-end
- M5 Week 2: RaceBox BLE on Android has platform-specific bugs

**Mitigation:**
- M5 Week 1 includes a "kill Android" checkpoint: if scaffold takes >5 days, defer Android to M6
- WearOS has a hard dependency on Android; Apple Watch is the priority
- Android is an acquisition channel enhancer, not a revenue driver in 6 months

**Rollback:** Slip Android to M6 or Q1 2027. Launch V1 at M5 with iOS-only mobile + Apple Watch. Android in beta for users who need it. Reframe V1 positioning: "LAP V1 — available on iOS, Android coming soon."

---

## R-09 — Stripe / payments break in production

**Probability:** Low.
**Impact:** Critical while it's happening.

**What could happen:** Webhook misfires, subscription state diverges from reality, user charged incorrectly.

**Early signals:**
- Sentry errors in `/api/v1/billing/webhooks`
- Daily automated job detects users with `subscription_status: active` in Stripe but `inactive` locally
- A paying user reports "I can't access despite paying"

**Mitigation:**
- Stripe test-mode full happy path + failure path tested before M3 prod cutover
- Automated daily reconciliation job compares Stripe subscription list to local DB
- Webhook signature validation + replay tolerance
- Manual admin tool to force-sync a single user's subscription

**Rollback:** Stripe has dashboard-visible subscriptions. Worst case: refund affected users manually, grant free month, communicate transparently.

---

## R-10 — Competitor ships the same feature before we do

**Probability:** Low-Medium.
**Impact:** Medium.

**What could happen:** Garage61 adds rule-based coaching. RaceLab adds progression tracking. Racing Republic undercuts pricing.

**Early signals:**
- Monitored via monthly competitor check (set calendar reminder)
- Reddit / Discord chatter about competitor feature drops

**Mitigation:**
- Moat is the ecosystem, not any single feature
- Price moat: €15 is already cheap vs 1:1 coaching
- Coaching library as data asset is defensible — takes time to replicate

**Rollback:** differentiate on what we have that they don't (cross-platform + sim↔real bridge). Don't try to match feature-for-feature. Stay doctrinal.

---

## Weekly review criteria (Q194)

Every Friday, 17:00 CET, self-review against these questions. If >1 fires red, schedule a pivot discussion (with yourself or a trusted peer).

1. **Velocity:** commits, PRs merged, hours worked — trending up or down vs last week?
2. **KPIs:** upload success, activation rate, WPD — on trajectory to targets?
3. **Ship health:** CI green? Sentry errors? User reports?
4. **Sleep / mood:** are you OK?
5. **Risk register:** did any early signal above fire this week?

## Forced-pivot triggers (Q195 non-compromises)

If any of these happen, stop feature work for 1 week minimum:
- Session-loss incident reported by any user
- CI green rate <85% for 5 days
- Mobile crash-free users <97% for 5 days
- Stripe broken >2 hours in production
- 3+ paying-user churns in a week citing product issues
- You work >65 hours in a single week twice in a row

## The one thing I'm most worried about (Q196)

Based on the doctrine + roadmap: **the sim↔real bridge is non-negotiable per Q132, but has the least validated signal of everything in the plan.** The shape/intensity math in ADR-005 §5.5 is my best guess at what "transfer" means. If it's wrong, the moat collapses.

**Pre-flight:** before committing to bridge UI in M4, run the algorithm in M3 on your 10-15 archived real+sim same-track sessions. If the output isn't something you, as the domain expert, nod at — we have a problem and the M4 plan adjusts.
