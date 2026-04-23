# Launch Playbook

**Target: Public beta 2026-07-10 to 2026-07-23** (earlier-if-ready window per G1=d). V1 release 2026-09-23 or earlier.

Soft launch philosophy per G2: YouTube + email + Twitter/Insta + free-trial-influencer-outreach + Reddit careful (no paid placement, no product promotion in comments). NO Product Hunt / HackerNews — more controlled.

---

## Phase 1 — Pre-launch (Day -21 to -7)

### Infrastructure readiness gate (Day -21)

Can only launch if ALL:
- [ ] Ops stream Tier 1-3 complete (O001-O071)
- [ ] Legal: ToS + Privacy + Cookie policies live (see `10-playbook-legal.md`)
- [ ] Stripe live-mode (not test) with first test charge refunded
- [ ] Email sequences drafted + imported to Resend
- [ ] Sprint 1 core flows green end-to-end (user can sign up, upload session, see weakness, accept prescription)
- [ ] Review loop metrics: CI green >90%, zero open PAUSE_FOR_HUMAN_REVIEW
- [ ] Figma mockups → real implementations for Driver Timeline, Profile, Coaching tab (at minimum)
- [ ] Mobile Android in Play Store internal test track (nice-to-have, not blocker)
- [ ] Desktop installer signed + downloadable from GitHub Release

### Content readiness gate (Day -14)

- [ ] Marketing site live at `lap-coach.racing` with all 11 core pages (home, how-it-works, pricing, demo, product/*, blog, about, privacy, terms, cookies, press)
- [ ] ≥10 coaching flagship articles published
- [ ] 2 pillar pages indexed (submitted to GSC)
- [ ] Launch blog post draft ready
- [ ] 5 Reddit-community "soft engagement" threads already established (you're known in r/iRacing etc., have karma)
- [ ] Twitter/Insta accounts created with 10 existing posts (backdated warm-up posts so you don't look new)
- [ ] YouTube channel created with ≥3 tutorial videos uploaded
- [ ] Influencer shortlist: 10 sim-racing YouTubers/streamers identified — DMs drafted for outreach

### Beta-user curation (Day -7)

- [ ] Waitlist reviewed, first 30 users identified as alpha cohort (mix: high karma sim racers, real-world track day enthusiasts, known competitive iRacing names if any on the list)
- [ ] Personal email drafted to each of the 30 with a personalized note (not a blast)
- [ ] Founder-discount coupon code generated: `FOUNDER2026` = 20% off × 12 months
- [ ] Bug-report channel set up (email `support@lap-coach.racing` + in-app feedback widget)
- [ ] Internal "war room" doc for launch-week observations

## Phase 2 — Soft launch (Day 0 to +7)

### Day 0 — Alpha-30 invitations

- [ ] 09:00 CET — Email the 30 alpha cohort personally. Subject: "Your LAP Coach access is ready"
- [ ] Monitor signup funnel in PostHog: aim for >50% conversion (personally-emailed) within 48h
- [ ] Post in Discord communities you're a member of (if any) — low-key "I'm launching a beta, DM if interested" format
- [ ] Personal LinkedIn post (founder's voice, no hype)
- [ ] Founder-log blog post: "LAP Coach alpha is live. Here's how it's going."

### Day 1-3 — First user feedback loop

- [ ] Monitor Sentry: any crash in first 48h = drop everything and fix
- [ ] Monitor PostHog: are users completing the activation funnel? (signup → first session → first insight → first prescription accept)
- [ ] Monitor Resend: are welcome emails arriving? Any bounces?
- [ ] Respond to every user message personally within 4 hours
- [ ] First bug-patch cycle: any reported issue that affects >1 user → fix same-day
- [ ] If a user gets stuck at activation step N, write a short docs update same-day

### Day 4-7 — Expand

- [ ] Day 4 — invite the next 30 waitlist members (70 total now)
- [ ] Day 5 — publish a founder-log post with "What 30 alpha users taught us in 4 days" (anonymized observations)
- [ ] Day 7 — invite entire remaining waitlist (assuming ≤200 signups)

## Phase 3 — Public beta (Day +8 to V1)

### Day +8 — Open sign-ups

- [ ] Homepage CTA becomes "Start 14-day trial" pointing to `app.lap-coach.racing/signup` — no more waitlist gate
- [ ] `marketing /loop` kicks into final-published-content mode (previously drafting for post-launch)
- [ ] Schedule 1 blog post + 1 YouTube video per week indefinitely

### Soft launch channels (per your G2 selections)

**YouTube** (primary):
- [ ] 90-second product demo → homepage embed + YouTube upload
- [ ] 3-minute "How LAP works" → YouTube + embed in `/how-it-works`
- [ ] 5 × 60-90 sec tutorials published weekly
- [ ] Target: 10 subscribers by end of Month 1 (low bar, build gradually)

**Email**:
- [ ] Weekly newsletter: new content + product updates + founder-log
- [ ] Waitlist-→-trial conversion campaigns continuing

**Twitter/X + Instagram**:
- [ ] 2-3 posts/week per platform — mix of: coaching library insights (quotable facts), product mini-demos (screen recordings), founder-log mini-threads
- [ ] Engagement >= posting: reply to every comment + relevant sim-racing tweets

**Reddit (CAREFUL)**:
- [ ] ONLY answer questions where LAP is directly relevant, and link only if the link genuinely helps
- [ ] Never post "I built LAP, check it out"
- [ ] Build comment karma in r/iRacing, r/simracing, r/CarRacing over time — become a known contributor, not a promoter
- [ ] If someone asks "what telemetry tool do you use", honest answer including alternatives, LAP one of them

**Influencer outreach** (free product):
- [ ] Identify 10 mid-tier sim-racing YouTubers (5K-50K subs — big enough for reach, small enough to respond)
- [ ] Personal DM with: "Built this, here's 12 months free, no strings, would love to hear what you think if you try it"
- [ ] Zero paid placements
- [ ] If 2-3 mention LAP positively, that's win

**Reddit forbidden**: paid product placement. Will get you banned on sight. Don't even risk it.

## Phase 4 — V1 release (~Day +60)

Only happens when:
- [ ] Core product loop (capture → insight → prescription → outcome) works for ≥90% of users
- [ ] Mobile Android in Play Store production (open beta or full release)
- [ ] Desktop installer stable
- [ ] Coaching library ≥100 rules with <5% false-positive rate
- [ ] Sim↔real bridge MVP has ≥50 TransferLink entities created and rated >70% "useful"

### V1 launch events

- [ ] V1 blog post: "LAP Coach V1 — everything that ships today"
- [ ] V1 email blast to all users (trial + paid + waitlisters who never converted)
- [ ] New YouTube demo showing new-in-V1 features
- [ ] Press kit update + outreach to 5 sim-racing journalists (Race Department, iRacing forums moderators, SimRacing.gp)
- [ ] Founder long-form post on LinkedIn: "6 months of LAP — what worked, what didn't, what's next"
- [ ] Update marketing hero copy to remove "beta" framing

## Incident playbook

During launch window, any of these = immediate action:
- Signup broken for >5 min → revert to previous webapp deploy, post apology in status page
- Payment flow broken → email affected users + temp-free-extended-trial as apology
- Session upload silently fails → blocker, halt marketing, fix before more signups
- Review loop pauses + can't unpause cleanly → manual investigation + potential roll-back
- Negative blog post / tweet goes viral criticizing → 24h silence rule, then founder-voice response

## Metrics to watch hourly on launch day

- Signups/hour
- Activation funnel conversion
- Sentry 5xx rate
- Stripe successful charges (post-trial conversion)
- Email delivery rate
- DNS / uptime

## Post-launch weekly cadence

- **Monday**: weekly metrics review (PostHog dashboard + sprint progress monitor)
- **Tuesday**: one-on-one with first 10 users who signed up (async or live)
- **Wednesday**: blog post published
- **Thursday**: YouTube video published
- **Friday**: founder-log + weekly review ritual (see `11-playbook-weekly.md`)
- **Sunday**: plan next week's content calendar

## Goal posts

30 days post-launch:
- 200 trial signups
- 40 paid conversions
- 10 YouTube subscribers
- 3 organic mentions by external sim racing content creators
- Zero known data-loss incidents

60 days post-launch:
- 500 trial signups (lifetime)
- 150 paid conversions
- 50 YouTube subscribers
- 1 major review blog post / video from a credible source

90 days post-launch (~V1+):
- 1000 paying users
- Monthly churn ≤ 5%
- NPS ≥ 40 via in-app survey
