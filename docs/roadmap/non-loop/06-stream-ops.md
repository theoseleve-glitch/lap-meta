# Ops Stream — Infrastructure & Accounts Checklist

**Resource:** Your time + ChatGPT for config help + Codex for automation scripts.
**Nature:** Mostly one-time setup, front-loaded in Days 1-5.

Checklist format: each item has `[ ]` → `[x]` state. Mark date completed.

---

## Tier 1 — Day 1-2 critical path (do before other loops need these)

These block downstream work. All under your €50/mo starting budget via free tiers.

### Domain + DNS (you own `lap-coach.racing` on Cloudflare)

- [ ] O001 Verify DNS zone is active in Cloudflare dashboard
- [ ] O002 Set nameservers at registrar (if not Cloudflare as registrar — probably already set if domain bought through CF)
- [ ] O003 Enable CF proxy (orange cloud) on apex — HTTPS + CDN auto-applied
- [ ] O004 Add CAA record: `lap-coach.racing CAA 0 issue "letsencrypt.org"` + `"google.com"`
- [ ] O005 MX records:
   - Option A (Google Workspace, €6/mo): `lap-coach.racing MX 1 smtp.google.com`
   - Option B (Cloudflare Email Routing, FREE): enable in CF dashboard, routes to personal email
   - **Recommended: Option B until revenue justifies Workspace**
- [ ] O006 SPF record (TXT): `v=spf1 include:_spf.resend.com include:spf.improvmx.com -all` (adjust based on sender services)
- [ ] O007 DKIM: enable once Resend is configured (H041) — CF DNS entries added via Resend dashboard
- [ ] O008 DMARC: TXT `_dmarc.lap-coach.racing v=DMARC1; p=quarantine; rua=mailto:dmarc@lap-coach.racing; pct=25`

### Postgres (Neon)

- [ ] O009 Create Neon project `lap-backend`
- [ ] O010 Create branches: `main` (prod), `dev` (local dev)
- [ ] O011 Enable autoscaling on prod branch, 0.25 CU min (cheapest)
- [ ] O012 Copy connection strings:
   - `NEON_DATABASE_URL_PROD=postgresql://...`
   - `NEON_DATABASE_URL_DEV=postgresql://...`
- [ ] O013 Store in password manager + `.env` files for lap-backend
- [ ] O014 Test: `psql $NEON_DATABASE_URL_PROD -c 'select 1'`

### Redis (Upstash)

- [ ] O015 Create Upstash Redis instance `lap-backend-prod`, region = eu-west-2 (EU compliance) or us-east-1 (closer to Cloudflare Workers)
- [ ] O016 Enable TLS
- [ ] O017 Get REST URL + token → env
- [ ] O018 Create second instance for dev

### Object storage (Cloudflare R2)

- [ ] O019 Create R2 buckets: `lap-telemetry-prod`, `lap-telemetry-dev`
- [ ] O020 Create API token scoped to R2 read+write on those 2 buckets only
- [ ] O021 S3-compatible endpoint + access key + secret key → env
- [ ] O022 Test: upload a file via `aws s3 --endpoint-url=... cp ...`
- [ ] O023 Set lifecycle rule on dev bucket: auto-delete objects >7 days (keeps dev cheap)

### Auth (Clerk)

- [ ] O024 Create Clerk application "LAP Coach"
- [ ] O025 Configure: email + password, Google OAuth, Apple OAuth (deferred)
- [ ] O026 Development instance + Production instance keys
- [ ] O027 Allowed redirect URIs: `http://localhost:3000/*`, `https://app.lap-coach.racing/*`
- [ ] O028 Webhook secret for user.created/user.deleted/session.created
- [ ] O029 Add user metadata schema: `skill_level` (beginner/intermediate/advanced), `cohort_opt_in` (bool), `plan_type` (null/monthly/yearly/b2b)

### Payments (Stripe)

- [ ] O030 Create Stripe account (test mode)
- [ ] O031 Create products + prices:
   - `LAP Monthly` price €15/mo recurring
   - `LAP Yearly` price €150/yr recurring
   - `Founder Waitlist` coupon 20% off 12 months (stackable on both plans)
- [ ] O032 Create webhook endpoint target `/api/v1/billing/webhooks` + signing secret
- [ ] O033 Copy test + live keys → env (don't go live until M3 launch)
- [ ] O034 Enable Stripe Tax (EU VAT MOSS — configure your SIRET when available)
- [ ] O035 Enable Billing Portal (self-serve cancel/update)

## Tier 2 — Day 3-5 observability

### Error tracking (Sentry)

- [ ] O036 Create Sentry org "lap"
- [ ] O037 Create 6 projects: `lap-backend`, `lap-webapp`, `lap-website`, `lap-desktop`, `lap-mobile-android`, `lap-labs`
- [ ] O038 Each project: DSN + auth token → env
- [ ] O039 Release tracking via GitHub Actions (or manual `sentry-cli releases new`)
- [ ] O040 Set up alert rules: >10 errors/hour on any project → email

### Analytics (PostHog)

- [ ] O041 Create PostHog project "LAP Coach"
- [ ] O042 EU region instance (GDPR compliance)
- [ ] O043 Personal API key for server-side + public client key
- [ ] O044 Enable session recordings (10% sample on production, 100% on staging)
- [ ] O045 Feature flags enabled (will use for gradual rollouts)

### Uptime monitoring

- [ ] O046 BetterUptime or UptimeRobot free tier
- [ ] O047 Monitors: `lap-coach.racing` (marketing), `app.lap-coach.racing` (webapp), `api.lap-coach.racing/healthz` (backend), Android Play Store listing URL
- [ ] O048 Status page published at `status.lap-coach.racing` (optional public page)
- [ ] O049 Alerts route to `ops@lap-coach.racing` + phone SMS (if free tier includes)

## Tier 3 — Week 2 deploy infrastructure

### Marketing site (Cloudflare Pages)

- [ ] O050 Create Cloudflare Pages project, link to `theoseleve-glitch/lap-website` repo
- [ ] O051 Build settings: `pnpm install && pnpm build`, output `dist`, Node 22
- [ ] O052 Custom domain: `lap-coach.racing` + `www.lap-coach.racing`
- [ ] O053 Preview URL template for PRs: auto-enabled
- [ ] O054 Environment variables (Production): `PUBLIC_POSTHOG_KEY`, `PUBLIC_POSTHOG_HOST`, `RESEND_API_KEY`, `SENTRY_DSN`
- [ ] O055 Analytics tab + Web Vitals enabled

### Webapp (Cloudflare Workers via OpenNext)

- [ ] O056 When lap-webapp sprint reaches deploy task, create Worker project
- [ ] O057 Custom domain: `app.lap-coach.racing`
- [ ] O058 Environment variables: DB, Redis, Clerk, Stripe, R2, Sentry, PostHog
- [ ] O059 KV namespace for session cache
- [ ] O060 Durable Objects if needed (SSE fan-out)

### Backend (Fly.io or Railway)

- [ ] O061 Fly.io account + CLI installed (`fly auth signup`)
- [ ] O062 Create app `lap-backend-staging` + `lap-backend-prod`
- [ ] O063 Dockerfile tested locally (`fly launch --no-deploy` generates)
- [ ] O064 Secrets set: `NEON_DATABASE_URL`, `REDIS_URL`, `CLERK_SECRET_KEY`, `STRIPE_SECRET_KEY`, `R2_*`, `SENTRY_DSN`, `POSTHOG_KEY`
- [ ] O065 Custom domain: `api.lap-coach.racing`
- [ ] O066 Health check at `/healthz` configured
- [ ] O067 Auto-scale config: min 1, max 3 machines (staging 0-1)

### CI/CD

- [ ] O068 GitHub Actions per repo — sprint tasks handle most; verify they actually run
- [ ] O069 Branch protection on `master` (optional early; enable if collaborators join): require PR, require CI green
- [ ] O070 Dependabot: enable for all repos, weekly schedule
- [ ] O071 Renovate: alternative to Dependabot, more flexible grouping (optional)

## Tier 4 — Ongoing (monthly review)

- [ ] O072 Monthly: review Stripe balance + bank reconciliation
- [ ] O073 Monthly: rotate any API keys approaching 90-day age
- [ ] O074 Monthly: review Sentry error volume + dismiss old issues
- [ ] O075 Monthly: review PostHog session recordings for user-friction patterns
- [ ] O076 Monthly: check Neon database size + scale plan if approaching limit
- [ ] O077 Monthly: check R2 storage + lifecycle rules effective
- [ ] O078 Monthly: Cloudflare cache hit rate + tune if low

## Tier 5 — Pre-launch checklist (complete before public beta)

- [ ] O079 All custom domains have HTTPS, HSTS preload submitted
- [ ] O080 Privacy policy + ToS + Cookie policy live at `/privacy`, `/terms`, `/cookies` (see legal playbook)
- [ ] O081 Sentry alerts quieted (not paging you on low-sev)
- [ ] O082 Backup tested: restore Neon dev-branch to fresh Postgres → verify data integrity
- [ ] O083 Incident response plan written (in `ops/incident-response.md`)
- [ ] O084 Status page cached response for common incidents

---

## Total SaaS cost projection

At launch (pre-revenue):
- Cloudflare: free (Pages + Workers + R2 below free tier)
- Neon: free (0.5 GB + 100 compute hours/mo)
- Upstash: free (10K commands/day)
- Resend: free (100 emails/day)
- Sentry: free (5K errors/mo)
- PostHog: free (1M events/mo)
- BetterUptime: free (10 monitors)
- Clerk: free (10K MAU)
- Stripe: free + 2.9% + €0.25/transaction on revenue
- **Total: €0/mo** until first user

At 100 paying users:
- Still mostly free tiers
- Clerk: potentially first paid tier if MAU exceeds 10K (unlikely at 100 paid)
- Neon: might exceed free compute hours, $0-20
- **Total: ~€5-30/mo + Stripe fees**

At 1000 paying users (€12-15k MRR):
- Clerk Pro €25/mo base
- Neon Launch tier $19/mo
- Upstash pro $10/mo  
- Sentry Team $26/mo
- PostHog Scale (may still be free depending on events)
- Resend pro $20/mo (for higher sending limits)
- BetterUptime Pro $29/mo
- **Total: ~€130-200/mo** — well within your B1 budget tier (b)

You're massively over-provisioned with your budget for the first 100 users. Don't optimize too early — free tiers work.
