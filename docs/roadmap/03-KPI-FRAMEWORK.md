# LAP — KPI Framework

You left the entire KPI block (H1-H7) + most of Block 17 (Q170-183) blank. Decisions follow. All targets are 6-month (2026-10-31) unless noted.

---

## 1. North Star Metric

**Weekly Paid Drivers (WPD)** — unique paying accounts that uploaded ≥1 session AND viewed ≥1 coaching surface (WeaknessEpisode, ActionPrescription, or DriverTimeline) in the last 7 days.

**Why not MAU or MRR?**
- MAU counts people who opened the app, not people getting value.
- MRR is an outcome, not a lever. WPD drives MRR.
- WPD captures the loop you actually care about: driver captures → driver learns → driver pays to keep learning.

**6-month target:** 750 WPD (out of 1000+ paying users target).
- Implies: 75% of paid users are weekly-active. High bar, but realistic for a tool with a weekly loop.

**Sub-metrics feeding WPD:**
- Upload cadence per user (sessions/week)
- Coaching surface view rate (visits/week)
- ActionPrescription acceptance rate (% of proposed that user accepts)

---

## 2. Activation

> **A user is activated when, within 7 days of signup, they:**
> 1. **Uploaded their first session** (either from desktop or mobile OR via manual web upload for sim log files)
> 2. **Viewed their first `WeaknessEpisode` or `ActionPrescription`** in the webapp
> 3. **Accepted at least one prescription** (clicked "Add to next session plan")

All three = activated. Drop any one and activation is missed.

**Target activation rate:** 55% of signups activate within 7 days.

**Why three criteria?** The single most predictive behavior for paid conversion in coaching-adjacent SaaS is not "used the product" but "committed to a next step". Without the Accept step we measure curiosity, not commitment.

---

## 3. Retention

| Cohort stage | Target |
|---|---|
| D7 retention (activated cohort) | 70% |
| D30 retention | 45% |
| M3 retention | 35% |
| M6 retention | 28% |
| Paid retention (after trial→paid conversion) | 85% M1, 70% M3 |

**Read this as:** of 100 users who activate, 45 are still weekly-active after 30 days. Of 100 who convert to paid, 85 are still paying at end of Month 1 of their subscription.

---

## 4. Quality bars (ship blockers)

No feature ships to beta or V1 if these are missed.

| Metric | Beta (M3) | V1 (M5) | 6mo (M6) |
|---|---|---|---|
| Upload success rate (started captures → cloud-visible sessions) | 95% | 98% | 99% |
| Session loss rate (captures that started and silently disappeared) | 0 per 1000 | 0 per 1000 | 0 per 1000 |
| Upload → insight latency (p95, upload complete → coaching panel loaded) | 90s | 60s | 45s |
| Upload → cloud visibility (session appears in list after upload) | 30s p95 | 15s p95 | 10s p95 |
| Synced within 5min (% of sessions) | 85% | 95% | 98% |
| Synced within 1hr | 95% | 99% | 99.5% |
| Synced within 24hr | 99% | 99.9% | 99.9% |
| Webapp LCP p75 | 2.5s | 2.0s | 1.8s |
| Webapp INP p75 | 200ms | 150ms | 100ms |
| Desktop CPU during session (overlays on) | <15% on 6-core Ryzen 5 baseline | same | same |
| Mobile battery drain / hour recording | <15% on iPhone 13+ | <12% | <10% |
| Coaching false-positive rate (library rules) | <10% (user-flagged "not actually a weakness") | <5% | <3% |
| Prescription efficacy (% of prescriptions where `ActionOutcome.success_condition_met` = true) | n/a (not enough cycles) | 40% | 55% |
| CI green rate | 95% | 98% | 99% |
| Prod 5xx rate | <0.1% | <0.05% | <0.01% |

---

## 5. Time-to-first-value

**Target:** 8 minutes from signup to seeing first useful insight.

**Breakdown:**
- Signup + email verify: 2 min
- First session upload (either test session we provide OR user uploads an existing iRacing `.ibt`): 3 min
- Backend processing + first insight render: <60s
- User reads first `WeaknessEpisode`: 2 min read

Failure modes and mitigations:
- First-signup user has no sessions → provide a "load sample session" option showing a real curated session so the user sees what the product does before their own data is ready.
- Desktop install too painful → web-based `.ibt` upload is the fast path for day-1 signups.

---

## 6. Per-app primary KPIs

| App | Primary KPI | Target M6 |
|---|---|---|
| **Marketing site** | Trial signup rate from landing | 3.5% of unique sessions |
| **Webapp** | WPD (North Star) | 750 |
| **Desktop** | % of paid users with ≥1 session captured via desktop in last 14 days | 60% |
| **Mobile** | % of paid users with ≥1 real-life session captured via mobile in last 28 days | 20% (given 500-5000 split you gave, real-life is secondary) |

**Marketing site secondary KPIs:**
- LCP p75 on homepage: <2.0s
- Time on product page p50: >90s (engaged)
- Email capture → trial conversion: 20%
- Homepage → pricing → trial funnel: 12% → 40% (=4.8% overall trial rate)

---

## 7. Coaching KPIs (proves the brain works)

These prove the webapp is more than "a session list":

| KPI | Target M6 |
|---|---|
| % of sessions with at least one `WeaknessEpisode` attached | 85% |
| % of users with an open `ActionPrescription` | 70% |
| Prescription acceptance rate (proposed → accepted) | 60% |
| Prescription efficacy rate | 55% |
| Weakness resolution rate (episodes marked `resolved` within 30 days of first detection) | 25% |
| Coaching library rule hit rate (avg rules fired per session) | 3-8 |
| Coaching library false-positive rate (user flags "not actually a weakness") | <5% |

---

## 8. Bridge KPIs (proves sim↔real is real)

| KPI | Target M6 |
|---|---|
| Total `TransferLink` entities created | 500 |
| Users with at least one transfer link | 20% of dual-persona users (sim + real captured) |
| Auto-suggested vs manual link ratio | 60/40 |
| User rating of transfer report "useful" | >70% thumbs-up |

---

## 9. Engineering health (the three we commit to)

From Q183:

1. **CI green rate on main branch ≥ 98%** across all repos. A branch-week report fires Slack alert if below.
2. **p95 upload success rate ≥ 98%** measured daily. Pages you (Slack/SMS) on <95% for >1 hour.
3. **Zero session-loss incidents per week.** If even one user reports lost data, incident mode.

---

## 10. What failure looks like

Explicit so we can recognize it without denial:

| Signal | Threshold | What it means |
|---|---|---|
| Activation rate <30% at M3 | Missed | Onboarding broken or wrong persona |
| D30 retention <25% at M3 | Missed | Product not actually coaching well |
| WPD/paying ratio <50% | Missed | Users pay but don't use — high churn coming |
| Prescription efficacy <25% at M5 | Missed | Coaching library isn't working; ship is fragile |
| <100 paying users at M6 | Critical miss | Go-to-market broken |
| <1000 paying users at M6 | Short of target | Acceptable miss if retention is strong |
| CI green rate <90% for 2 weeks | Critical engineering miss | Roadmap pause, reliability sprint |

---

## 11. What success looks like

- 1000+ paying users.
- 750 WPD.
- 55% prescription efficacy.
- 500 TransferLinks created.
- First B2B inbound conversation by Month 5.
- Coaching library with 100+ rules, <5% false-positive rate.
- Zero session-loss incidents reported.
- €12-15K MRR trajectory at Month 6 with 3-5% weekly user growth.

---

## 12. Measurement infrastructure

To make these KPIs real, the following instruments must be in place by end of Month 1:

1. **PostHog** for product analytics. Free tier covers 1M events/month. Track all activation criteria, funnel steps, feature usage.
2. **Sentry** for error tracking across all clients (web, desktop, mobile). ~€26/mo.
3. **A KPI dashboard page in the backend** (admin-only) that shows North Star + quality bars in near-real-time. Built in Month 1 Week 4.
4. **Weekly automated Slack report** every Monday 09:00 UTC with last-week's KPI deltas.
5. **Incident runbook** for session-loss events. Stub in Month 1, matured by Month 3.

Total observability cost: <€50/month.
