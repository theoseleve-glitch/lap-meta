# Human Stream — Irreducible Tasks

**Resource:** You (no AI can do these for you).
**Your time:** 5-10h/week scattered throughout.
**Target:** ~100 completions over 30 days.

---

## Block A — Daily operations (H001-H030)

Recurring almost daily. Not every day every task, but the cluster.

### Morning ritual (~15 min/day)

- [ ] H001 Day 1 — morning email triage + review-log scan
- [ ] H002-H030 (same pattern, one per day for 30 days) — format: read daily email, check review-log.md, clear any `PAUSE_FOR_HUMAN_REVIEW` markers, note any strategy decisions surfaced

## Block B — Account & infrastructure setup (H031-H070)

Front-loaded in Days 1-5. One-time signups.

**Day 1-2 (critical path):**
- [ ] H031 Stripe account (test mode first — https://dashboard.stripe.com/register)
- [ ] H032 Create Stripe products: LAP Monthly (€15), LAP Yearly (€150), Founder Waitlist (€12/mo × 12mo coupon)
- [ ] H033 Stripe test webhook secret + publishable key → note in password manager
- [ ] H034 Clerk account (https://clerk.com/) + create "LAP Coach" application (production + dev environment)
- [ ] H035 Clerk allowed origins configured for `lap-coach.racing` + `app.lap-coach.racing` + `localhost:*`
- [ ] H036 Clerk publishable + secret keys → password manager
- [ ] H037 Neon account (https://neon.tech) + create `lap-backend` project with dev branch + prod branch
- [ ] H038 Neon database URLs → password manager (2 URLs: dev + prod)
- [ ] H039 Upstash account (https://upstash.com) + create Redis for dev and prod
- [ ] H040 Cloudflare R2 bucket `lap-telemetry-dev` + `lap-telemetry-prod` + API token scoped to those buckets
- [ ] H041 Resend account (https://resend.com) + verify domain `lap-coach.racing` via DNS
- [ ] H042 Resend API key → password manager
- [ ] H043 Sentry project (https://sentry.io) `lap-backend`, `lap-webapp`, `lap-website`, `lap-desktop`, `lap-mobile`, `lap-labs` — 6 separate DSNs
- [ ] H044 PostHog project (https://posthog.com) — 1 project, 5+ client distinctions via event `source` tag
- [ ] H045 PostHog API key + host URL → password manager

**Day 2-3 (DNS + domain):**
- [ ] H046 Cloudflare DNS: `lap-coach.racing` → A-record to CF Pages (when pages project created)
- [ ] H047 Cloudflare DNS: `app.lap-coach.racing` → A-record to webapp Worker or Pages
- [ ] H048 Cloudflare DNS: `api.lap-coach.racing` → backend host (Fly.io or Railway)
- [ ] H049 Cloudflare DNS: `docs.lap-coach.racing` → CF Pages separate project (optional — could be subpath of main site)
- [ ] H050 Cloudflare DNS: `status.lap-coach.racing` → UptimeRobot / BetterUptime status page
- [ ] H051 MX records for `@lap-coach.racing` via Google Workspace or Resend forwarding
- [ ] H052 SPF + DKIM for Resend verified
- [ ] H053 DMARC policy set (`p=quarantine` first, tighten later)

**Day 3-5 (business side):**
- [ ] H054 File SIRET / micro-entreprise registration (url: https://www.autoentrepreneur.urssaf.fr/) — needs national ID + address
- [ ] H055 Get SIRET number + URSSAF account — store in password manager, update `00-OVERVIEW.md` "Business Entity" field
- [ ] H056 Open business bank account (Qonto / Shine / N26 Business — EU micro-entreprise friendly)
- [ ] H057 Link Stripe payouts to business bank account
- [ ] H058 Google Workspace: `hello@lap-coach.racing`, `theo@lap-coach.racing`, `support@lap-coach.racing` (€6/mo/user × 1-2)
- [ ] H059 Or cheaper: use Cloudflare Email Routing + Resend send-from-domain (free)
- [ ] H060 LinkedIn business page for LAP Coach (when ready to publicize)
- [ ] H061 Google Play Developer Console account ($25 one-time) — wait until mobile close to launch (Month 5)
- [ ] H062 Apple Developer account ($99/yr) — defer until Mac arrives
- [ ] H063 Product Hunt account (if using)
- [ ] H064 Twitter/X account `@lap_coach` or similar — deferred to soft-launch per your answer D1
- [ ] H065 YouTube channel — deferred until launch kit ready
- [ ] H066 Discord server — deferred until beta community exists
- [ ] H067 Reddit account + earn karma in r/iRacing, r/simracing, r/CarRacing by commenting (NO product placement — risks ban per your note)
- [ ] H068 Document every API key in a single password manager (1Password / Bitwarden) with clear naming
- [ ] H069 Enable 2FA on every account above
- [ ] H070 Backup: export all secrets to an encrypted file + store offline (second device or USB) — disaster recovery

## Block C — Design & brand (H071-H085)

- [ ] H071 Review existing Figma logo — confirm final, or commit to iterate
- [ ] H072 Decide brand split: is it "LAP" or "LAP Coach" officially? (Figma frames + all copy)
- [ ] H073 Validate brand name with 5 sim-racer acquaintances (quick informal, not structured customer dev)
- [ ] H074 Photograph yourself for founder headshot (or commission — budget €100-300 if professional)
- [ ] H075 Generate social preview images for launch kit (the ones where brand matters)
- [ ] H076 Record YouTube channel intro (10-20s brand identity)
- [ ] H077 Record 90-second product demo for homepage (OBS + DaVinci Resolve, free tools)
- [ ] H078 Record 3-min walkthrough (how LAP works, full flow)
- [ ] H079 Record RaceBox pairing tutorial (2 min)
- [ ] H080 Record "first session upload" tutorial
- [ ] H081 Record 5 × 15-second social clips from demo material
- [ ] H082 Schedule: record all videos in 1-2 evening session days, edit over another evening
- [ ] H083 Upload to YouTube as unlisted first (for launch-day switch to public)
- [ ] H084 Write YouTube video descriptions with timestamps + links
- [ ] H085 Create playlist structure: "Getting Started", "Coaching Deep-Dive", "Behind the Scenes"

## Block D — Coaching library validation labeling (H086-H100)

After Codex delivers the validation harness (K030), you label rule firings.

- [ ] H086 Harness live — spend 1h familiarizing with labeling UI
- [ ] H087 Day 1 labeling: 20 firings across 5 rules
- [ ] H088 Day 2 labeling: 20 more
- [ ] H089 Day 3 labeling: 20 more — start noticing patterns per rule
- [ ] H090 Pattern audit: identify any rule where your FP rate feels >10%, flag for backend /loop to re-tune
- [ ] H091-H100 — continue 20/day × 10 days = ~200 labeled firings minimum (aim for 500+ by end of sprint)

## Block E — Strategy + decisions (H101-H115)

Triggered by daily email flags.

- [ ] H101 Respond to first strategy-decision email (if any comes in)
- [ ] H102-H115 — queued per strategy email that arrives; format: read, decide, write decision into the affected sprint file as `[DECISION: <answer>]` comment, notify the loop

## Block F — Writing (yours, not AI) (H116-H125)

Places where your voice matters more than AI efficiency.

- [ ] H116 Personal "Why I'm building LAP" blog post (1500w, your voice, post on marketing site)
- [ ] H117 Personal LinkedIn post announcing LAP Coach concept
- [ ] H118 Founder letter for waitlist (post-signup email 1 — your voice)
- [ ] H119 Public beta launch announcement — your post on social (Twitter/Insta thread)
- [ ] H120 V1 release announcement — your post
- [ ] H121 Respond to first 10 user emails personally (not templates)
- [ ] H122 First 10 user interviews post-beta (see customer dev playbook)
- [ ] H123 Weekly founder-log short (~300w per week × 4 weeks) — builds an audience
- [ ] H124 Product Hunt or HN launch comment thread — respond personally to all top comments
- [ ] H125 Write "6 months of LAP" retrospective at end of sprint

## Block G — Pricing & beta decisions (H126-H130)

- [ ] H126 Validate €15/mo pricing with at least 3 user interviews (post-beta)
- [ ] H127 Decide when to open public beta (based on Phase 1 velocity + infra readiness)
- [ ] H128 Decide waitlist invitation batch sizes (30 first, 100 next, open after)
- [ ] H129 Set paid-ad budget (if any) for first month post-launch
- [ ] H130 First-100-users retro: what did we learn about pricing?

---

## Daily rhythm (human side)

**~1h/day** average, clustered as:

- Morning 15min: email + review-log triage
- 15min mid-day: labeling if harness running
- 15min evening: social engagement, strategy decisions if surfaced

Plus block time:
- 1 full day for Ops/Accounts setup (Day 1 or 2)
- Video recording days (2 × 4h sessions)
- Customer dev days (post-beta, ~5h × 6 days for 30 interviews)

Target: 100 human tasks completed across 30 days.
