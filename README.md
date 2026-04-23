# lap-meta

Meta-repository for the LAP project. Contains the 6-month roadmap, 30-day sprint queues, ops/email scripts, and review-loop state.

## Contents

```
docs/
  roadmap/
    00-EXECUTIVE-SUMMARY.md       — 2-minute overview of the plan
    01-STRATEGIC-DOCTRINE.md      — mission, persona, what we build/cut
    02-ARCHITECTURE-DECISIONS.md  — 16 ADRs (backend stack, contracts, auth, etc.)
    03-KPI-FRAMEWORK.md           — North Star, activation, retention, quality bars
    04-ROADMAP-6MO.md             — month-by-month critical path
    05-TASKS-BACKEND.md           — 48 backend tasks covering all 6 months
    06-TASKS-WEBAPP.md            — 31 webapp tasks
    07-TASKS-DESKTOP.md           — 27 desktop tasks
    08-TASKS-MOBILE.md            — 33 mobile tasks (iOS + Android + wearables)
    09-TASKS-MARKETING.md         — 21 marketing tasks
    10-RISK-REGISTER.md           — top 10 risks + mitigations + rollback
    11-AI-PLAYBOOK.md             — which AI for which task type
    sprint-30day/
      LOOP-SETUP.md               — terminal commands for /loop agents
      sprint-backend.md           — Sprint 1: 240 backend tasks (M1-early-M2)
      sprint-webapp.md            — Sprint 1: 240 webapp tasks (M1-M3)
      sprint-desktop.md           — Sprint 1: 240 desktop tasks (M1-M5)
      sprint-mobile.md            — Sprint 1: 240 Android tasks
      sprint-mobile-ios-future.md — frozen iOS sprint (resumes with Mac)
      sprint2-*.md                — Sprint 2 queues for remaining 6mo work
      sprint-marketing.md         — entire marketing scope
      loop-review.md              — runbook for the autonomous review loop
      review-log.md               — append-only cycle log
      metrics.md                  — live snapshot
ops/
  send_email.py                   — Resend-backed email sender
  send_alert.py                   — 9 preformatted alert types
  README.md                       — email system setup + operation
  .env.example                    — RESEND_API_KEY template
```

## Sub-repositories (not in this repo — they have their own)

- `lap-backend` → github.com/theoseleve-glitch/lap-backend
- `lap-webapp` → github.com/theoseleve-glitch/lap-webapp
- `lap-schemas` → github.com/theoseleve-glitch/lap-schemas
- `lap-mobile-android` → github.com/theoseleve-glitch/lap-mobile-android
- `lap-website` → github.com/theoseleve-glitch/lap-website (marketing)
- `datalogger` → github.com/theoseleve-glitch/lap-coach-logger (desktop)
- `lap_mobile` (iOS, frozen pending Mac)

## Purpose

This repo is edited by the autonomous **review loop** (Terminal 5) every 2h — it commits `review-log.md`, `metrics.md`, and `ops/.last_daily_sent` updates here. It's also edited by you when you decide strategy items raised in the daily emails.

Never merge product code into this repo. Product code goes in its respective sub-repo.
