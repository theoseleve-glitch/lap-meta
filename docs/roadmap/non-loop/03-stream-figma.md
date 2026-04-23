# Figma Stream — Design Forge

**Resource:** Figma Pro × 8 seats + Claude Design (AI-native).
**Your time:** 10-12h/week.
**Starting point:** You have a LAP / LAP COACH logo already in Figma.
**Output:** Figma file URLs posted into the sprint file tasks they unblock (e.g., `webapp T111 — fig: https://figma.com/...`).

---

## Team / file structure (set up day 1)

Create a Figma Team "LAP Coach" and initialize files:

- [ ] F001 `00 — Brand & Identity` — logo variants, colorway, typography, motion principles, spacing grid, iconography
- [ ] F002 `01 — Design System Core` — tokens, components, states, variants, effects (shadow/blur/glow)
- [ ] F003 `02 — Webapp Driver OS` — all `/app/*` screens (Timeline, Profile, Compare, Bridge, Weakness, Skill Drilldown, Settings, Onboarding)
- [ ] F004 `03 — Marketing Site` — homepage, how-it-works, pricing, demo, product pages, blog, pillar pages
- [ ] F005 `04 — Mobile Android` — preflight, dashboard, session list, session detail, pairing, settings
- [ ] F006 `05 — Desktop Overlays` — coaching card, mode indicators, strategy widget, pit-armed state, session review
- [ ] F007 `06 — App Store Assets` — Play Store feature graphic, screenshots, icon variants, social media OG images
- [ ] F008 `07 — Email Templates` — welcome, onboarding drip, trial-to-paid, win-back, launch
- [ ] F009 `08 — Launch Kit` — Product Hunt graphics (if used), Twitter/Insta posts, YouTube thumbnails, press kit

## Block A — Brand & Identity (F010-F025)

Given: logo exists in Figma. Expand into a full identity system.

- [ ] F010 Extract logo variants: wordmark, icon-only, horizontal lockup, stacked lockup
- [ ] F011 Logo safe areas + minimum sizes (print, web, favicon, app icon contexts)
- [ ] F012 Dark-mode + light-mode logo variants
- [ ] F013 Favicon + apple-touch-icon + android-icon (512×512 + adaptive)
- [ ] F014 Color palette: primary, secondary, accent, semantic (success/warning/error/info), grayscale
- [ ] F015 Color accessibility audit: WCAG AA on every pair used in UI
- [ ] F016 Typography scale: hero, display, H1-H4, body, small, mono — font choices + fallback stack
- [ ] F017 Grid system: 4px base, 8pt scale, container max-widths (1280, 1440, 1600)
- [ ] F018 Motion principles: easing curves, duration scale (150/250/400/600ms), reduced-motion alternatives
- [ ] F019 Shadow scale + depth system
- [ ] F020 Icon library: 60 core icons (sim racing specific — steering wheel, brake pedal, fuel, tire, track shapes, flag, helmet, stopwatch, clipboard, trophy, etc.)
- [ ] F021 Illustration style guide: if using, define vector style + illustrative tone
- [ ] F022 Photography direction: what actual photos look like (if used)
- [ ] F023 Brand voice + tone doc (text, written once, referenced everywhere): confident, measured, data-forward, not bro
- [ ] F024 Competitor visual comparison board: how LAP stands out vs Garage61, RaceLab, Racing Republic, RaceChrono
- [ ] F025 Logo file exports: SVG, PNG @1x/2x/3x, PDF for all variants

## Block B — Design System Core (F026-F040)

- [ ] F026 Buttons: primary, secondary, ghost, destructive, icon-only — all states (default, hover, active, focus, disabled, loading)
- [ ] F027 Input fields: text, textarea, number, select, checkbox, radio, toggle, file upload, search — with validation states
- [ ] F028 Cards: base card, stat card, session card, weakness card, prescription card, outcome card — all variants
- [ ] F029 Navigation: primary nav, secondary/tab nav, breadcrumb, pagination, sidebar
- [ ] F030 Modals, drawers, popovers, tooltips — with z-index scale
- [ ] F031 Empty states: no sessions, no weaknesses, no cohort yet, cohort locked, no target event
- [ ] F032 Loading skeletons: every card shape
- [ ] F033 Error states: 404, 500, rate-limited, offline, trial expired
- [ ] F034 Alert / toast / banner system
- [ ] F035 Data viz primitives: sparkline, bar, line, scatter, radar, gauge, heatmap, violin
- [ ] F036 Table component: sortable, filterable, paginated, expandable rows
- [ ] F037 Form patterns: single-column, two-column, sectioned, stepper
- [ ] F038 Timeline component (generic — adapts to driver timeline, session timeline, strategy timeline)
- [ ] F039 Badge / tag / chip system
- [ ] F040 Complete component library auto-published to Storybook (handoff spec)

## Block C — Webapp Driver OS mockups (F041-F060)

One screen per task, each unblocking a corresponding sprint-webapp.md `[design]` task.

- [ ] F041 Driver Timeline — desktop, unblocks webapp T111
- [ ] F042 Driver Timeline — mobile viewport, unblocks T133
- [ ] F043 Driver Profile — desktop, unblocks T136
- [ ] F044 Driver Profile — mobile viewport
- [ ] F045 Skill radar chart state variants
- [ ] F046 Weakness Detail page — unblocks T175
- [ ] F047 Skill Drilldown page — unblocks T166
- [ ] F048 Session Detail Shell — already exists; freshen, unblocks T007
- [ ] F049 Session Coaching Tab — unblocks T086-T110
- [ ] F050 Compare Case creation modal — unblocks T186
- [ ] F051 Compare Case Detail — unblocks T188
- [ ] F052 Onboarding wizard 4 steps — unblocks T206-T215
- [ ] F053 Settings layout + tabs
- [ ] F054 Paired device management screen
- [ ] F055 Billing / Paywall screens — unblocks T217-T221
- [ ] F056 Trial-expired hard-gate screen — unblocks T221
- [ ] F057 Bridge Tab on session detail — unblocks T022 (Sprint 2)
- [ ] F058 Transfer Report full-page — unblocks T023 (Sprint 2)
- [ ] F059 Cohort percentile badges — unblocks T021 (Sprint 2)
- [ ] F060 Target Event picker + countdown — unblocks T036-T050 (Sprint 2)

## Block D — Marketing site mockups (F061-F075)

Unblocking marketing sprint `[design]` tasks.

- [ ] F061 Homepage hero + 4-5 scroll sections — unblocks marketing T021
- [ ] F062 "How LAP works" ecosystem page + diagram — unblocks T041
- [ ] F063 Pricing page — unblocks T056
- [ ] F064 Demo page — unblocks T071
- [ ] F065 Product page — overview — unblocks T106
- [ ] F066 Product → desktop page
- [ ] F067 Product → mobile page
- [ ] F068 Product → bridge page
- [ ] F069 Product → coaching library page (lists all 150 rules)
- [ ] F070 Pillar page template (for 4 SEO pillars)
- [ ] F071 Blog post template
- [ ] F072 Coaching article template (for the 180 articles)
- [ ] F073 For-schools / B2B landing
- [ ] F074 404 + 500 + maintenance pages
- [ ] F075 Press kit page layout

## Block E — Mobile Android (F076-F085)

- [ ] F076 Preflight screen (permissions + readiness gates) — unblocks mobile T091
- [ ] F077 Dashboard — recording state (landscape) — unblocks T126
- [ ] F078 Dashboard — battery-saver state
- [ ] F079 Session list + upload state badges — unblocks T092
- [ ] F080 Session detail (compact, real-life focused) — unblocks T145
- [ ] F081 QR pairing flow — unblocks T170
- [ ] F082 Settings + paired devices
- [ ] F083 First-launch wizard
- [ ] F084 Coaching prompt bottom-sheet during recording — unblocks T152
- [ ] F085 Wear OS companion UI sketches (5 tiles/screens) — unblocks Sprint 2 mobile T041-T053

## Block F — Desktop overlays (F086-F092)

Existing desktop has ~40 overlay widgets. Refinement pass.

- [ ] F086 Coaching card design refresh (race mode) — unblocks desktop T094
- [ ] F087 Coaching card design refresh (practice mode verbose)
- [ ] F088 Strategy widget w/ pit-armed state — unblocks T141
- [ ] F089 Mode switcher UI + indicator
- [ ] F090 Race-minimal preset layout (all widgets arranged for full-screen 1080p/1440p/4K)
- [ ] F091 Practice preset layout
- [ ] F092 Endurance preset layout (incl. stint timer, long-run reference)

## Block G — App Store + launch assets (F093-F100)

- [ ] F093 Play Store feature graphic (1024×500)
- [ ] F094 Play Store screenshots: 8 screens showing Driver Profile, Coaching, Timeline, Bridge report, Settings (tablet + phone)
- [ ] F095 Play Store icon (512×512 adaptive + legacy)
- [ ] F096 Apple Watch screenshots (placeholder for when Mac arrives)
- [ ] F097 Social media OG images per marketing page (1200×630)
- [ ] F098 YouTube thumbnails for demo videos (1280×720) — 5 templates
- [ ] F099 Twitter/Insta post templates (square + portrait) — 10 variants
- [ ] F100 Press kit visual assets (logo sheet, founder headshot slot, product screenshots ready-to-download)

---

## Workflow: Figma → sprint task URLs

For each design task, the flow is:
1. You open Figma, design the screen with Claude Design's help
2. You finalize the Figma file frame for that screen
3. You go to the corresponding sprint file task (e.g., `sprint-webapp.md` T111)
4. Append to the task line: `— fig: https://figma.com/file/XXX?node-id=YYY`
5. Commit sprint file change to lap-meta
6. Next time the sprint /loop picks up that task, it reads the Figma URL and uses `figma-use` MCP to implement

This is what transforms the `[design]` sprint task from "placeholder rendering" to "pixel-accurate implementation".

## Daily rhythm (Figma side)

- 08:30-10:30 — 1 Figma session per day (2h focused) — typically 2-3 screens completed
- Batch similar work: all webapp screens one day, marketing pages another, etc.
- Claude Design generates first draft, you iterate
- Every 5 screens: commit the Figma file + post URLs to sprint tasks

Target over 30 days: 100 Figma tasks = ~3-4 screens/day average with unblocking effect on 30+ sprint `[design]` tasks.
