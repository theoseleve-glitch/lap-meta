# Weekly Review Ritual

**When:** Friday 17:00-18:00 CET (per your A3 answer).
**Who:** You, alone. ChatGPT or Claude.ai as brainstorm partner.
**Why:** The only human-owned checkpoint that ties the 7 loops + 6 non-loop streams together into strategic course-correction.

---

## Pre-ritual (15 min)

Open in browser tabs:
- Latest 7 daily strategy emails (Gmail search: `from:onboarding@resend.dev`)
- `review-log.md` on lap-meta (last 7 days)
- `metrics.md` on lap-meta
- PostHog weekly dashboard
- GitHub activity: `github.com/theoseleve-glitch?tab=overview` (last 7 days)
- Anthropic + OpenAI usage dashboards
- Your founder-log draft (you write one per week)

## The ritual — 45 min structured

### 1. Numbers check (10 min)

Write these numbers into `docs/roadmap/weekly-reviews/YYYY-WW.md`:

```
Sprint progress (per repo):
- backend: N [x] this week, M total, K% complete
- webapp: ...
- desktop: ...
- mobile: ...
- marketing: ...

Non-loop progress:
- ChatGPT tasks completed: N (coaching articles, pillars, blog, emails, research)
- Codex tasks completed: N (which side-quests?)
- Figma screens completed: N
- Human tasks completed: N (which infra, which video, which labels)

Quality:
- CI green rate: N%
- Commits reverted: N
- SCOPE_FLAGs: N
- Coaching rule false-positive rate (if harness active): N%

Budget:
- Claude Max usage this week: N% of 5h windows hit 100%
- Codex token usage: $N or %
- SaaS spend: €N
- Total burn: €N

Product:
- Signups this week: N (post-launch only)
- Trial conversions: N
- Paying users: N (delta vs last week)
- Churn: N

Content:
- Coaching articles published this week: N
- Blog posts: N
- YouTube videos: N
- Newsletter sent: Y/N
```

### 2. What surprised me (10 min)

ChatGPT brainstorm prompt:
```
Here's my week in numbers: [paste above].
Here are the daily emails from this week: [paste 7 emails].
Here's the review log: [paste last week's cycles].

Surface 3 things that are NOT in the numbers — things that happened this week I should notice but haven't quantified yet. Be specific, not generic.
```

Write the 3 surprises into the weekly review file.

### 3. Strategic decisions queued (10 min)

For each `[DECISION REQUIRED]` marker in the daily emails that wasn't resolved during the week:
- Restate the decision
- List 2-3 options
- Pick one, write rationale in 2 sentences
- Update the affected ADR or sprint file with the decision

If 3+ decisions queued unresolved, that's a signal — your review cadence might need to shift to twice-weekly or you need to empower the loops with clearer ADRs.

### 4. Roadmap adjustment (10 min)

Ask yourself:
- Are we drifting from the 6-month goal? (1000 paid users by 2026-10-31)
- Is any risk from `10-RISK-REGISTER.md` triggering? (re-read the signals list)
- Is any pillar getting starved while another is over-fed? (look at time spent across streams)
- Are the loops actually shipping the right thing, or drifting? (sample 3 commits from each repo, quick diff read)

If an adjustment is warranted, write it as a diff to:
- `04-ROADMAP-6MO.md` (if roadmap timing)
- `01-STRATEGIC-DOCTRINE.md` (if doctrine)
- A specific sprint file (if task priorities)
- A new ADR (if an architectural decision changed)

Commit to lap-meta with message prefix `meta: weekly review YYYY-WW`.

### 5. Founder log (5 min)

Short personal reflection post, ~300 words. Publish to blog or keep private. Topics rotate:
- What I learned this week about sim racing users
- What went right (celebrate — solo founders forget to)
- What I'd do differently
- What's haunting me about the roadmap

Publish to `lap-coach.racing/blog/founder-log/[YYYY-WW].mdx` or keep in `docs/founder-log/` if still private.

## Monthly addition (last Friday of each month, add 30 min)

At weeks 4, 8, 12, 16, 20, 24:

### Month-end review (30 min extra)

- Compare this month's numbers to last month
- Review whether the next month's sprint files are realistic given current velocity
- Update the per-phase task costs in `03-KPI-FRAMEWORK.md` with observed reality
- Re-run the "how much of 6-month roadmap done" calculation (like we did on 2026-04-23)
- Decide if any big pivot is warranted
- If pivot: draft a new ADR, update doctrine, adjust sprints, notify loops via sprint file updates

## Quarterly checkpoint (Fridays at month 3 and month 6)

End of Month 3 = 2026-07-24 = public-beta-live week. This is **mandatory human-review checkpoint** per ADR and loop-review runbook.

Extend the ritual to 2 hours:
- Full product usage review (you use LAP as a user would for 30 min)
- Review all live customer support emails + resolve
- Re-validate persona fit with actual beta-user data
- Decide whether to open the cohort feature, B2B door, Apple Watch revival, etc.
- Write a public "3 months in" blog post

End of Month 6 = 2026-10-31 = retro + plan year 2.

## What this ritual prevents

Without this ritual:
- Loops ship correct code that builds the wrong product
- Strategic decisions accumulate unresolved in daily emails, eventually becoming a pile too big to handle
- You lose track of how much AI budget is being consumed vs value produced
- Drift from doctrine happens invisibly — you'd wake up at Month 5 with a product you didn't intend to build
- Customer insight goes unprocessed

With this ritual:
- 45-60 minutes/week prevents all of the above
- Documented weekly = you can always reconstruct "why did I decide X at week Y"
- Course corrections happen in time to matter, not post-mortem

## Anti-patterns

- **Skipping the ritual** because "nothing urgent this week" — the ritual's job is exactly catching non-urgent drift
- **Extending it beyond 60 min** unless month-end — protects you from turning review into avoidance of execution
- **Not committing the weekly review** — version-control makes it reconstructible later
- **Doing it Monday instead of Friday** — Friday catches the week you just lived; Monday has forgotten

## File structure

```
docs/
  roadmap/
    weekly-reviews/
      2026-W18.md  ← first review (May 1)
      2026-W19.md
      ...
      2026-W44.md  ← Month 6 checkpoint review
  founder-log/
    2026-W18.md
    ...
```

All committed to lap-meta, all pushed.
