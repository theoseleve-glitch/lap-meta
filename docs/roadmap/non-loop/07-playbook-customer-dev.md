# Customer Development Playbook

**Status: Deferred to Month 3+** per your answer D2 ("no plan for this yet and I guess it will be the case only when a beta that is product-grade enough to show to the world is ready"). This file is ready when you are.

Don't touch until public beta is live and ~10 users are using the product. Premature interviews waste your time and their time.

---

## Trigger conditions — when to start

Start when ALL of these are true:
1. Public beta is live (per `09-playbook-launch.md`)
2. ≥10 users have each uploaded ≥3 sessions
3. Review loop is clean-running (no ongoing PAUSE_FOR_HUMAN_REVIEW flags)
4. You have ~10 hours/week to commit to interviews + analysis for 2-3 weeks

Earliest realistic trigger: **2026-07-24** (1 week after earliest launch).

## What you're trying to learn

Five questions, in order of priority:

1. **Is the persona right?** Are the users you're attracting the "serious sim racer" persona from `01-STRATEGIC-DOCTRINE.md`? If not, who are they actually?
2. **Is the coaching library useful?** Do users understand + act on prescriptions? Or do they read and ignore?
3. **Does the bridge resonate?** Do sim-focused users care about real-life transfer (and vice versa), or is it a "nice-to-have" nobody actually uses?
4. **Is the price right?** €15/mo felt right from the outside. Does it match perceived value after 2 weeks of use?
5. **What's the biggest surprise?** What are users doing with LAP that you didn't expect? (Often the best product insights)

## Interview target: 30 users

Not more, not less. Diminishing returns beyond 30; noise above 10.

### Segmentation

Aim for a balanced mix:
- 10 iRacing users (primary persona)
- 5 ACC users
- 5 users of other sims (AC / AMS2 / rF2 / LMU / F1)
- 5 real-life track day users (secondary persona)
- 5 users who tried LAP and churned in trial (most valuable for diagnostic)

### Recruitment channels (since no Discord/Twitter today)

Options for reaching beta users who've signed up:
- In-app prompt post-first-session: "Help shape LAP — 15min call, free month as thanks"
- Email blast to trial users Day 7: "What's working, what's not?" + Calendly link
- Post-churn email: "Can I learn why? 10 min, free extended trial"

Do NOT cold-message sim racing communities — respect the no-product-placement rule.

## Interview guide (~20 min, recorded)

Get consent to record at the start. Use Zoom / Google Meet / Whereby (pick one). OpenAI Whisper for free transcription.

### Opening (2 min)
- "Thanks for doing this. No sales pitch — I genuinely want to learn how LAP is fitting (or not fitting) into your racing."
- "Can I record? Transcript stays with me, no sharing."

### Background (3 min)
- "How long have you been sim racing / track days?"
- "What sims / tracks do you race?"
- "What's the most competitive thing you've done in the last 6 months?"
- "Have you used any telemetry tools before? Which?"

### Discovery (5 min)
- "Walk me through the last time you used LAP. What did you open?"
- "What were you trying to figure out?"
- "Did you find it?"
- "What did you do with what you found?"

### Specific signal questions (5 min)
- "Tell me about a prescription you accepted. Did you follow it? What happened?"
- "Have you looked at the bridge / sim-vs-real compare? What did you think?"
- "Is there a feature you wish existed that doesn't?"
- "Is there a feature that exists that confuses you or annoys you?"

### Pricing (3 min)
- "Setting aside what LAP actually costs — at what monthly price would you think it's too cheap and you'd suspect quality?"
- "At what price would you think it's too expensive and you wouldn't consider it?"
- "At what price would you think it's on the expensive side but you'd still seriously consider it?"
- "At what price would you think it's a great deal?"
- (This is the Van Westendorp PSM — 4 questions, generates pricing range)

### Closing (2 min)
- "Anything I didn't ask that you want to bring up?"
- "Can I email you in 3 months to ask how things are going?"
- "Thank you — here's your free month code [code]"

## Analysis framework

After each interview:
1. Upload recording to OpenAI Whisper (free, local) → transcript file
2. ChatGPT: "Extract themes, pain points, and quotable lines from this transcript: [paste]"
3. Save output to `docs/research/customer-dev/interview-N-[user-id].md`
4. Tag themes (persona-fit, coaching-utility, bridge-utility, pricing, feature-request, ux-issue, surprise)

After 10 interviews done:
1. ChatGPT: "I have 10 interview summaries attached. Identify the top 5 themes, the most-common pain points, and any surprising findings. Compare to our strategic doctrine: [paste 01-STRATEGIC-DOCTRINE.md]."
2. Decide: any pivot needed?

After 30 interviews done:
1. Write a "What 30 users taught us" retrospective doc
2. Update `01-STRATEGIC-DOCTRINE.md` with any corrections
3. Update pricing (or confirm €15 is right) based on PSM aggregate

## Anti-patterns (don't)

- Don't pitch during the interview. It biases their answers.
- Don't ask "would you pay X?" — hypothetical, terrible signal. Use Van Westendorp.
- Don't interview churned users together with active users in the same analysis pass — keep them separate.
- Don't ignore contradictions. If 3 users say "the coaching library is the only reason I pay" and 3 say "coaching is confusing", that's a real split worth investigating.
- Don't batch all 30 at once. Do 5, analyze, do 5 more, iterate the guide.

## Pricing sensitivity specifically

Van Westendorp PSM gives 4 price points per respondent:
- Too Cheap (TC) — quality-worrying low
- Cheap (C) — deal territory
- Expensive (E) — upper consideration
- Too Expensive (TE) — out of consideration

Plot:
- X-axis: price
- Y-axis: cumulative % of respondents
- 4 curves intersect to give:
  - **Optimum Price Point (OPP)**: where TC% = TE%
  - **Indifference Price Point (IPP)**: where C% = E%
  - **Range of Acceptable Pricing**: between intersection of TC&E and C&TE

Run this analysis in a Jupyter notebook after 30 interviews. If IPP is ~€18 and your current price is €15, you can raise. If IPP is ~€12, consider dropping or bundling.

## Scheduled tasks (post-beta)

- [ ] CD001 Configure in-app interview prompt (post-first-session) — loop-assigned webapp task when this playbook activates
- [ ] CD002 Configure email trigger at trial Day 7
- [ ] CD003 Configure churn trigger email
- [ ] CD004 Set up Calendly or Cal.com with 20-min interview slots
- [ ] CD005 Write interview discussion guide (v2 from this doc)
- [ ] CD006 Write consent language
- [ ] CD007 Set up Whisper transcription pipeline
- [ ] CD008-CD037 — 30 interview tasks (1 line per interview, track completion)
- [ ] CD038 First 10-interview synthesis
- [ ] CD039 Second 10-interview synthesis
- [ ] CD040 Final 30-interview retrospective + doctrine updates
- [ ] CD041 PSM pricing analysis
- [ ] CD042 Publish "What 30 users taught us" blog post (anonymized)

## Compensation budget

Per interview: 1 month free extended trial (€15 value) = no cash outlay. If needed, can add a €20 Amazon gift card per interview (€600 total for 30) but not required.

---

**Again: don't activate this playbook until public beta is running with ≥10 engaged users.**
