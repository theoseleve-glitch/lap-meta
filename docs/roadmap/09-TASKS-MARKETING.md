# LAP — Marketing Site Task Backlog

**Repo:** `lap-website` (slimmed to marketing only per ADR-002)
**Stack:** Astro 5 (static-first, lightweight, great for marketing) OR Next.js 14 kept if migration cost too high. Recommendation: migrate to Astro — ships 10× less JS, better Lighthouse scores, cheaper Cloudflare Pages hosting. Accept the 2-week migration cost.
**Task format:** `MK-NNN`.

---

## Month 1 — Extraction + Skeleton

### MK-001 🔴 Extraction from monolith
- **Month/week:** M1/W1-2
- **Deps:** WA-001
- **AI:** claude-opus (plan) + codex (mechanical moves)
- **Hours:** 10-14
- **Context:** Create `lap-website` as standalone. Move:
  - `lap-website/src/app/(marketing)/**` → new site
  - `lap-website/src/components/rooms/**` (marketing components) → new site
  - `lap-website/src/components/site/**` (SiteHeader, MobileDrawer, etc.) → new site
  - `lap-website/public/**` assets → new site
  - JSON-LD, sitemap generators → new site
- **Acceptance:**
  - Marketing site builds and deploys standalone
  - Webapp routes remain functional on `app.lap-coach.racing`
  - Marketing remains on `lap-coach.racing`

### MK-002 🔴 Astro migration (OR: skip if Next.js decided to stay)
- **Month/week:** M1/W3
- **Deps:** MK-001
- **AI:** claude-opus (migration strategy) + claude-sonnet (component conversion)
- **Hours:** 20-30
- **Context:** Convert React components to Astro components where they don't need interactivity. Keep GSAP-heavy rooms as Astro islands using `client:load`. Preserve i18n via Astro's built-in i18n. Preserve SEO metadata + JSON-LD via Astro integrations.
- **Decision checkpoint:** if this runs >5 days, abandon migration and stay on Next.js. Not worth derailing M1.
- **Acceptance:**
  - Homepage LCP <2.0s on mobile 4G
  - Total JS bundle <150KB (down from ~800KB currently)
  - No regressions vs current visual

### MK-003 🔴 Deploy to Cloudflare Pages
- **Month/week:** M1/W3
- **Deps:** MK-002 (or MK-001 if skipped)
- **AI:** codex
- **Hours:** 3-4
- **Context:** Cloudflare Pages with custom domain, auto-deploy from main branch. Preview deploys for PRs.

### MK-004 🔴 Build guardrails re-enabled
- **Month/week:** M1/W3
- **Deps:** MK-003
- **AI:** codex
- **Hours:** 2-3
- **Context:** Per audit Q's about disabled TS/lint checks in `next.config.mjs`. Re-enable on marketing site (smaller surface, safer).

---

## Month 2 — Content + Positioning

### MK-005 🔴 Positioning + copy rewrite
- **Month/week:** M2/W6
- **Deps:** MK-003
- **AI:** claude-opus (copy)
- **Hours:** 10-14
- **Context:** Align all public statements (Q54+ audit concerns):
  - Homepage hero: "The Driver OS — every lap, one step better." (placeholder, iterate)
  - Single positioning line about sim-first availability
  - Remove any AI-coach claims (Q130)
  - Align `SimFirst.tsx`, JSON-LD, `route-map.ts`, `claim-registry.ts`, logger page
- **Acceptance:**
  - Every public claim traceable to a shippable feature
  - No contradictions between pages

### MK-006 🔴 "How LAP works" ecosystem page
- **Month/week:** M2/W8
- **Deps:** MK-005
- **AI:** claude-design + claude-opus (copy)
- **Hours:** 10-14
- **Context:** Per Q125. Dedicated `/how-it-works` page with diagram + explanation:
  - Desktop logger captures sim sessions
  - Mobile captures real-life sessions
  - Webapp is the brain — coaching, progression, bridge
  - Website is the storefront
- **Acceptance:**
  - Diagram is visually clear (you specifically asked for example image in Q125)
  - Page explains ecosystem in <2 min read

### MK-007 🔴 Logger page surfaced in navigation
- **Month/week:** M2/W6
- **Deps:** MK-005
- **AI:** claude-sonnet
- **Hours:** 2-3
- **Context:** Per audit. Logger page orphaned in current nav. Add to header nav as "Desktop app" (or "Logger"). Add to route-map.

### MK-008 🔴 Pricing page
- **Month/week:** M2/W7
- **Deps:** MK-005
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** One tier: €15/mo or €150/yr (save €30). 14-day trial CTA. Waitlist users get €12/mo for 12 months.

### MK-009 🔴 Waitlist capture form + email sequence
- **Month/week:** M2/W6
- **Deps:** MK-005
- **AI:** claude-sonnet + codex
- **Hours:** 6-8
- **Context:** Waitlist form → stores email + persona tag → welcome email + weekly "what's shipping" email drip. Use Resend or Loops (~€20/mo).

### MK-010 🟡 Demo page — concrete preview
- **Month/week:** M2/W7
- **Deps:** MK-005
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** Audit said demo page is thin. Replace with embedded video or interactive walkthrough of actual Driver Profile / Coaching / Bridge surfaces. No fake mockups.

---

## Month 3 — Public Beta Launch

### MK-011 🔴 Launch landing page variant
- **Month/week:** M3/W12
- **Deps:** MK-006
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** Public beta day landing page: "LAP public beta now live" hero + trial CTA. Featured on homepage for 2 weeks post-launch.

### MK-012 🔴 Launch content (blog, Reddit, social)
- **Month/week:** M3/W12
- **Deps:** MK-011
- **AI:** claude-opus (long-form)
- **Hours:** 10-14
- **Context:** Launch-day content:
  - Blog post "Introducing LAP" (2000 words, product story, target personas)
  - r/iRacing + r/simracing + r/CarRacing announcement
  - Discord announcement in Garage61 community (where allowed)
  - YouTube short demo video (2 min)
- **Acceptance:** all scheduled for 2026-07-23 09:00 CET

### MK-013 🟡 Press kit
- **Month/week:** M3/W11
- **AI:** claude-opus
- **Hours:** 4-6
- **Context:** `/press` page with logo files, screenshots, founder quote, facts sheet. Email to 5 sim-racing journalists/YouTubers.

---

## Month 4 — Content + SEO

### MK-014 🟡 First 2 pillar pages for SEO
- **Month/week:** M4/W13-14
- **AI:** claude-opus (long-form SEO)
- **Hours:** 10-14
- **Context:** Pillar pages (3000+ words, optimized for intent):
  - "How to transfer from sim racing to real-life racing" (targets bridge moat)
  - "What is trail braking and how to measure it" (targets coaching library rule visibility)

### MK-015 🟡 4 blog posts on coaching rules
- **Month/week:** M4/W15-16
- **AI:** claude-opus
- **Hours:** 12-16
- **Context:** Each post deep-dives one rule from the coaching library, showing example sessions, evidence, drill. Serves dual purpose: SEO content + social proof of coaching library depth.

---

## Month 5 — V1 Launch Moment

### MK-016 🔴 V1 launch landing + press push
- **Month/week:** M5/W20
- **Deps:** MK-006
- **AI:** claude-opus + claude-design
- **Hours:** 10-14
- **Context:** V1 release 2026-09-23. New hero. Featured in press kit refresh. Blog post "LAP V1 — Driver OS is here". Reddit/Discord round 2.

### MK-017 🟡 Android/Watch launch copy
- **Month/week:** M5/W20
- **Deps:** AN-006, WR-001
- **AI:** claude-opus
- **Hours:** 4-6
- **Context:** Update product/logger page to mention Android availability + Apple Watch companion.

---

## Month 6 — SEO Push + B2B

### MK-018 🟡 2 more pillar pages
- **Month/week:** M6/W21-22
- **AI:** claude-opus
- **Hours:** 10-14
- **Context:** "Best sim racing telemetry apps compared (2026)" + "How to build a driver development plan" — both target high-intent keywords.

### MK-019 🟡 4 more blog posts
- **Month/week:** M6/W23-25
- **AI:** claude-opus
- **Hours:** 12-16

### MK-020 🟡 `/for-schools` B2B landing
- **Month/week:** M6/W22
- **Deps:** WA-029
- **AI:** claude-design + claude-opus (copy)
- **Hours:** 6-8
- **Context:** Landing for racing schools / karting academies. "Per-student LAP for academies" framing. Lead form → outbound sales.

### MK-021 🟡 Paid ad landing pages (optional)
- **Month/week:** M6/W23
- **AI:** claude-design
- **Hours:** 4-6
- **Context:** 2-3 targeted landing pages for paid acquisition if organic undershoots 1000 users by mid-M6.

---

## Summary

| Month | Marketing hours | Key deliverable |
|---|---|---|
| M1 | 35-50 | Extraction + (maybe) Astro migration + deploy |
| M2 | 40-55 | Positioning + How-it-works + pricing + waitlist |
| M3 | 20-30 | Public beta launch content |
| M4 | 20-30 | SEO pillar + coaching blog posts |
| M5 | 15-25 | V1 launch moment |
| M6 | 30-45 | SEO push + B2B landing + paid ads if needed |
| **Total** | **~180 hours** | |

Marketing is the smallest bucket by design — heavy lift is homepage + 2 core pages, rest is writing that AI can draft and you edit.
