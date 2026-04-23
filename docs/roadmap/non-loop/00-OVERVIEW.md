# LAP — Non-Loop Roadmap

Everything in the 6-month plan that the 7 autonomous loops (4 sprint + review + marketing + codex) don't produce. Mirror structure to sprint files: per-resource queue files + cross-cutting playbooks.

**Created 2026-04-23** after the Sprint 1 loops were humming and we confirmed the real budget cost per task (~0.7% of 5h window, 3.5× cheaper than initial estimates) was leaving massive headroom for non-loop work.

---

## Your decisions that shape this batch

From 2026-04-23 answer block:

| Axis | Decision |
|---|---|
| Coaching content scope | **30 flagship (2000w) + 150 standard (1200w) = ~240k words** |
| Non-loop daily budget | **6-8h/day** alongside running loops |
| Weekly review | **Friday 17:00 CET** |
| SaaS monthly budget | **<€50 → €50-150 scaling with user count** |
| Business entity | **Micro-entreprise (SIRET pending)** |
| Domain | **`lap-coach.racing` on Cloudflare** |
| Logo | **Exists in Figma** |
| Brand | **LAP / LAP COACH (with variants)** |
| Community accounts | **None exist yet — build as part of launch prep** |
| Customer interviews | **Deferred to post-beta** (won't happen before product-grade state) |
| SEO tools | **None paid — AI-driven research** |
| IDE | **VS Code** |
| Codex commit policy | **Mix — small direct to master, large via PR** |
| V2 prototypes | **All 4: setup recommender, pace predictor, cohort viz, training-plan engine** |
| Codex repo | **New `lap-labs` experiments repo** |
| Launch date | **Earlier if Phase 1 velocity holds (2026-07-10 possible)** |
| Launch channels | **YouTube, email, Twitter/Insta, free-trial influencer outreach, Reddit careful in soft-launch only (no paid product placement)** |
| Legal path | **DIY with ChatGPT drafts** (€0, accept risk) |

## Allocation envelope

Assuming 6-8h/day × 30 days = 180-240h. Distributed:

| Stream | Your time (h/week) | AI/tool resource |
|---|---|---|
| ChatGPT content + research | 15-20h | ChatGPT unlimited |
| Figma design forge | 10-12h | Figma Pro + Claude Design |
| Codex side-quests (briefing + review) | 4-6h | Codex CLI (autonomous when running) |
| Copilot live work | 5-7h | Copilot Agent (300 premium/mo) |
| Ops + legal one-time setups | 6-10h total (front-loaded) | Your hands + ChatGPT drafts |
| Human-only tasks (interviews, video, decisions) | 5-10h | You |
| Weekly review + strategy | 2h Fri | You + ChatGPT brainstorm |

Total: ~45-65h/week. Aligns with stated 6-8h/day × 6-7 day week.

## Files in this folder

```
00-OVERVIEW.md                ← this file
01-stream-chatgpt.md          ← ~300 tasks: 180 coaching articles + research + docs + emails + launch content
02-stream-codex.md            ← ~80 side-quest tasks including 4 V2 spikes + harness + monitor
03-stream-figma.md            ← ~80 design tasks: system + sprint [design] mockups + marketing
04-stream-copilot.md          ← prompt library for 300-req/mo premium deep-dives
05-stream-human.md            ← ~100 irreducible human tasks w/ weekly schedule
06-stream-ops.md              ← ~40 account/infra setup items + domain config
07-playbook-customer-dev.md   ← post-beta scripts (deferred, ready when you are)
08-playbook-content.md        ← editorial calendar + voice + SEO + racing-book list
09-playbook-launch.md         ← day-by-day orchestration for public beta + V1
10-playbook-legal.md          ← DIY drafts: ToS, Privacy, Cookie, Refund, DPA
11-playbook-weekly.md         ← Friday 17:00 CET ritual + monthly cadence
```

**Total: ~570 non-loop items** spread across streams running in parallel with the 1,700 autonomous-loop tasks.

## How to use these files

**Daily:**
- 1-2 ChatGPT sessions on highest-priority items from `01-stream-chatgpt.md`
- 1 Figma block from `03-stream-figma.md`
- Check Codex progress + brief next task from `02-stream-codex.md`
- Human tasks from `05-stream-human.md` (recordings, labeling, account signups)
- Use Copilot premium prompts from `04-stream-copilot.md` when you hit a scenario they match

**Weekly Friday 17:00 CET:**
- Ritual from `11-playbook-weekly.md`

**Milestone:**
- Public beta launch: `09-playbook-launch.md`
- Pre-launch legal: `10-playbook-legal.md`
- Post-beta: `07-playbook-customer-dev.md`

## Critical scope implications from your answers

### The 240k-word content moat

30 flagship articles + 150 standard articles at ChatGPT-polished editorial quality is the biggest single bet in the non-loop work. It's your SEO moat, your product moat (users consume content without subscribing → top-of-funnel), and your persuasion moat (no competitor has this depth of indexed driving-technique content). Over 30 days at ChatGPT unlimited, feasible at ~8k words/day.

### Four V2 spikes in parallel

Codex runs four experimental prototypes in `lap-labs` simultaneously: setup recommender, pace predictor, cohort viz, training-plan engine. None ship to production in the 6-month window — they're validation that the V2 roadmap is possible. Acceptable risk because Codex sessions don't block the critical path.

### Social-accounts blindspot

No Discord / YouTube / Twitter / Reddit presence today. This is structured as "build just-in-time for soft launch" in `09-playbook-launch.md`. Until then, launch-content tasks in `01-stream-chatgpt.md` draft the assets so when accounts exist, content is ready to ship.

### Customer dev deferred

Because customer interviews won't happen until product is beta-ready, `07-playbook-customer-dev.md` is designed for post-beta activation. Zero customer-dev tasks land before 2026-07-10.

### DIY legal means iteration risk

`10-playbook-legal.md` has ChatGPT-drafted ToS/Privacy/Cookie/DPA/Refund that are defensible but not lawyer-reviewed. Risk: a GDPR-specific edge case slips through. Mitigation: budget 1 lawyer review (€500-1000) as an optional post-beta task when first paying customer triggers a formal contract need.

### The "earlier launch" option

Your A2="c or more" (6-8h+) plus Phase 1 cost observations (0.7%/task) means aggressive interval tuning is feasible. If Phase 1 velocity holds through Week 2, public beta can shift earlier than 2026-07-23 to as early as 2026-07-10. That buys 13 extra days of beta-user feedback before V1.
