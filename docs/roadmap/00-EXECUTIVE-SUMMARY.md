# LAP — Executive Summary

**Date:** 2026-04-23 → 2026-10-31 (27 work weeks)
**Founder:** Solo, heavy AI-assisted, 50-60h/week, €400/mo budget.
**Runway:** ship-or-die.
**Goal:** 1000+ paying users at €15/month, public beta in 3 months, V1 in 5 months.

---

## The plan in 10 sentences

1. LAP becomes the **Garmin for drivers** — a Driver OS that turns every sim and real-life session into a personalized development plan.
2. The four apps unify behind one doctrine: **server = brain, clients = thin**. The webapp/backend owns all coaching intelligence; desktop and mobile render what the backend emits.
3. **Bundle v2 as single canonical session format** across all surfaces. UUIDv7 IDs. Pydantic v2 schemas generating TS + Swift types. No more per-page DTOs.
4. Ship the **Top 3 backend objects** (ActionPrescription, WeaknessEpisode, DriverProgressSnapshot) in Month 2, built on a **YAML coaching library** with **25 rules growing to 150 by Month 6**.
5. **Public beta launches 2026-07-23** with Driver Timeline + Driver Profile + Compare + Stripe live + mode-based desktop + reliable mobile.
6. **Sim↔real bridge ships at Month 4** as `TransferLink` entity with shape/intensity match algorithm. Non-negotiable doctrine, scoped to MVP UI in 6 months.
7. **V1 at Month 5 (2026-09-23)**: Android port + Apple Watch/WearOS companion + endurance event support + target event calendar + 100+ coaching rules.
8. **North Star = Weekly Paid Drivers** (WPD). Target 750 WPD / 1000 paying users / €10-15K MRR trajectory by 2026-10-31.
9. **No LLMs in coaching text.** Rule-based first, basic ML second. Trust differentiator against every "AI coach" competitor.
10. **Cuts that matter:** no social features, no full pit-call FSM, no cohort benchmarks until Month 4, no Android before Month 5, no LLM-generated coaching, no EventPerformancePrediction, no team-coach B2B product.

---

## What's in this roadmap folder

| File | Read when |
|---|---|
| `00-EXECUTIVE-SUMMARY.md` | You need the 2-minute version (you are here) |
| `01-STRATEGIC-DOCTRINE.md` | You're making a strategic trade-off and need the durable principles |
| `02-ARCHITECTURE-DECISIONS.md` | You need to implement a feature and wonder "which stack / format / ID / schema" — 16 ADRs with the decisions + rationale + alternatives rejected |
| `03-KPI-FRAMEWORK.md` | You want to know "am I on track?" — North Star, activation, retention, quality bars, per-app KPIs, measurement infrastructure |
| `04-ROADMAP-6MO.md` | You want the monthly + weekly view with critical path + parallelization lanes |
| `05-TASKS-BACKEND.md` | You're starting a backend task — 48 tasks with AI tool, hours, deps, acceptance criteria |
| `06-TASKS-WEBAPP.md` | Same, webapp — 31 tasks |
| `07-TASKS-DESKTOP.md` | Same, desktop — 27 tasks |
| `08-TASKS-MOBILE.md` | Same, mobile (iOS + Android + wearables) — 33 tasks |
| `09-TASKS-MARKETING.md` | Same, marketing — 21 tasks |
| `10-RISK-REGISTER.md` | You're worried — 10 risks with early signals + mitigations + rollback actions |
| `11-AI-PLAYBOOK.md` | You're about to ask Claude/Codex to do something and want the prompt pattern + which model + context management rules |

---

## First 5 things to do today

Right now, before closing this tab:

1. **Fix the desktop P0 that blocks CI.** `live_telemetry_processor` import break is merge-blocking everything. See task DT-001. 12-16 hours of Claude Opus + Sonnet work. **Today → end of Week 1.**
2. **Fix the mobile crash-on-init and silent-finalize bugs.** MO-001 + MO-002. 4-6 hours each. **This week.**
3. **Scaffold `lap-schemas` and `lap-backend`.** Parallel. BE-001 + BE-002. The hinge of everything downstream. **Week 2.**
4. **Pick Astro vs Next.js decision for marketing site extraction.** MK-001 / MK-002. 30 min decision, 10-30 hour execution. **Week 2-3.**
5. **Invite 5 trusted sim racers to be internal-alpha testers starting Month 2.** The closed beta at end of Month 2 and public at end of Month 3 are both risk-managed by this. Do this **this week** so onboarding is smooth.

---

## Commitments (read back to yourself every Monday)

- I will not ship features that break the "never lose a session" doctrine.
- I will not add client-side coaching logic after Month 1.
- I will not drop the €15/month price during the 6 months.
- I will not use LLMs to generate user-facing coaching text.
- I will take my 10 days off in August.
- I will hold a weekly review Friday 17:00 CET.
- I will not work >65h in a single week twice in a row.
- I will pivot if the Month 5 paying-user count is <300 of the 1000 target.

---

## The one line I'd tape to my monitor

> **Ship the loop: capture → weakness → prescription → next session → outcome → repeat.**
>
> Everything else is either serving the loop or delaying the ship.
