# LAP Marketing Website — 30-Day Sprint Queue

**Repo:** `lap-website/`.
**Stack:** Astro 5 (static-first), Tailwind, TypeScript strict, GSAP (motion), Cloudflare Pages (host), Resend (forms), Plausible/PostHog (analytics cookieless).
**Deploys to:** `lap.com` (webapp is on `app.lap.com`, separate).
**Total:** 220 tasks. Same /loop rules as sprint-backend.md.

---

## Block A — Project scaffold + deploy pipeline (T001–T020)

- [x] T001 [opus] Astro 5 init with TypeScript strict template ⇒ `pnpm dev` boots (lap-website@fbe7bd6)
- [x] T002 [sonnet] Tailwind integration + design tokens from old lap-website ⇒ styling renders (lap-website@fa5f6d8)
- [x] T003 [sonnet] Font setup (monospace Font Monument + sans Inter) with preload + swap ⇒ FOUT minimized (lap-website@06f4255)
- [ ] T004 [sonnet] Directory layout: `src/pages/`, `src/layouts/`, `src/components/`, `src/content/`, `public/` ⇒ organized
- [ ] T005 [sonnet] ESLint + Prettier + astro-check ⇒ `pnpm lint` green
- [ ] T006 [sonnet] Vitest + Playwright for tests ⇒ sample passes
- [ ] T007 [codex] GitHub Actions CI: build + typecheck + lint + test ⇒ workflow green
- [ ] T008 [codex] Cloudflare Pages project linked to repo ⇒ auto-deploy on push
- [ ] T009 [codex] Domain DNS: `lap.com` → Cloudflare Pages; `app.lap.com` → webapp ⇒ configured
- [ ] T010 [sonnet] Preview deploys per PR ⇒ preview URLs land in PR comments
- [ ] T011 [sonnet] Robots.txt + sitemap.xml auto-generated via Astro integration ⇒ verified
- [ ] T012 [sonnet] Default SEO layout: title + description + og + twitter + JSON-LD ⇒ all pages inherit
- [ ] T013 [sonnet] Canonical URLs + og:image per page ⇒ tested
- [ ] T014 [sonnet] PostHog client integration (cookieless initial-load) ⇒ pageviews ping
- [ ] T015 [sonnet] Plausible alternative or skip (pick one analytics, per GDPR preference) ⇒ decision noted
- [ ] T016 [sonnet] Sentry browser SDK integrated ⇒ errors captured
- [ ] T017 [sonnet] Lighthouse CI in GitHub Actions: LCP <1.8s threshold on homepage ⇒ gate
- [ ] T018 [sonnet] Visual regression via Chromatic or Percy ⇒ baseline set
- [ ] T019 [sonnet] 404 page designed + linked ⇒ renders
- [ ] T020 [sonnet] 500 page designed + linked ⇒ renders

## Block B — Homepage (T021–T040)

- [ ] T021 [design] Figma: new homepage hero + 4-5 scroll sections ⇒ approved
- [ ] T022 [opus] Hero component: positioning headline + subhead + dual CTA ⇒ Astro component
- [ ] T023 [opus] Headline options (A/B): "The Driver OS — Train. Race. Improve." / "Every lap, one step better." ⇒ default chosen
- [ ] T024 [opus] Subhead: one-sentence ecosystem pitch ⇒ copy locked
- [ ] T025 [opus] Primary CTA: "Start 14-day trial" → `/signup` (app.lap.com handoff) ⇒ wired
- [ ] T026 [opus] Secondary CTA: "See how it works" → `/how-it-works` ⇒ wired
- [ ] T027 [opus] Hero motion: subtle GSAP entrance, reduced-motion respected ⇒ smooth
- [ ] T028 [opus] Hero visual: product screenshot (Driver Profile page, mocked) ⇒ renders crisp
- [ ] T029 [opus] Section "After every session" — 3 tile grid (weakness detected / prescription / outcome tracked) ⇒ renders
- [ ] T030 [opus] Section "Sim and real, one driver profile" — bridge narrative ⇒ renders
- [ ] T031 [opus] Section "Built for serious sim racers" — persona fit bullets ⇒ renders
- [ ] T032 [opus] Section "Compare to tools you know" — MoTeC/Garage61 comparison ⇒ tight bullets
- [ ] T033 [opus] Section "Not for you if" — anti-persona disclosure ⇒ builds trust
- [ ] T034 [opus] Final CTA block: pricing snippet + trial CTA ⇒ renders
- [ ] T035 [opus] Social proof section (beta-user quotes — placeholders until real quotes exist) ⇒ scaffolded
- [ ] T036 [sonnet] Homepage performance audit: LCP <1.5s mobile 4G ⇒ achieved
- [ ] T037 [sonnet] Homepage JS total <100KB ⇒ verified
- [ ] T038 [sonnet] Homepage a11y: axe clean ⇒ pass
- [ ] T039 [sonnet] Homepage mobile layout: single column, readable at 360px ⇒ tested
- [ ] T040 [sonnet] E2E: homepage → CTA → signup ⇒ green

## Block C — "How LAP works" ecosystem page (T041–T055)

- [ ] T041 [design] Figma: ecosystem architecture diagram (desktop / mobile / webapp / bridge) ⇒ approved
- [ ] T042 [opus] Route `/how-it-works` shell ⇒ renders
- [ ] T043 [opus] Hero: "The whole driver improvement loop, in one place" ⇒ renders
- [ ] T044 [opus] Diagram component: annotated SVG showing data flow ⇒ accessible text alt
- [ ] T045 [opus] Section "1. Capture" — desktop + mobile capture explained ⇒ renders
- [ ] T046 [opus] Section "2. Brain" — backend intelligence layer (weaknesses, prescriptions, bridge) ⇒ renders
- [ ] T047 [opus] Section "3. Plan" — next-session plan generation ⇒ renders
- [ ] T048 [opus] Section "4. Improve" — outcome tracking loop ⇒ renders
- [ ] T049 [opus] "Where we are today vs year 2" honesty section ⇒ builds trust
- [ ] T050 [sonnet] Screenshots from real product surfaces (real Driver Profile UI) ⇒ embedded
- [ ] T051 [sonnet] Deep-links into product docs for interested devs ⇒ linked
- [ ] T052 [sonnet] CTA at end: "Try the 14-day trial" ⇒ wired
- [ ] T053 [sonnet] A11y + responsive ⇒ clean
- [ ] T054 [sonnet] SEO: target keyword "sim racing coaching platform how it works" ⇒ meta tuned
- [ ] T055 [sonnet] E2E: navigate → consume → CTA ⇒ green

## Block D — Pricing + trial CTA (T056–T070)

- [ ] T056 [design] Figma: pricing page (one tier, monthly + yearly) ⇒ approved
- [ ] T057 [opus] Route `/pricing` shell ⇒ renders
- [ ] T058 [opus] Tier card: €15/mo or €150/yr (save €30) + "14-day free trial" badge ⇒ Storybook
- [ ] T059 [opus] "What's included" checklist ⇒ 12 bullets
- [ ] T060 [opus] Founder-waitlist offer section: "Signed up before launch? €12/mo for 12 months" ⇒ rendered
- [ ] T061 [opus] FAQ section: 10 questions (cancel anytime, no card for trial, data export, etc.) ⇒ accordion
- [ ] T062 [opus] B2B teaser: "Running a racing academy? Talk to us." ⇒ inline CTA to `/for-schools`
- [ ] T063 [opus] Checkout CTA wires to `app.lap.com/signup?plan=monthly|yearly` ⇒ tested
- [ ] T064 [opus] Value-anchor comparison: "vs €80-150/hr human coach" ⇒ visible
- [ ] T065 [sonnet] Refund policy link ⇒ works
- [ ] T066 [sonnet] Contact sales link ⇒ email form or Calendly
- [ ] T067 [sonnet] Currency localization (EUR default, USD if US visitor detected) ⇒ optional
- [ ] T068 [sonnet] Performance + a11y ⇒ clean
- [ ] T069 [sonnet] SEO: target "sim racing coaching price" ⇒ meta
- [ ] T070 [sonnet] E2E: pricing → CTA → signup ⇒ green

## Block E — Demo + product tour page (T071–T090)

- [ ] T071 [design] Figma: demo page with interactive or video walkthrough ⇒ approved
- [ ] T072 [opus] Route `/demo` shell ⇒ renders
- [ ] T073 [opus] Choose format: embedded video (YouTube/Vimeo) OR inline screenshots ⇒ default video
- [ ] T074 [opus] 3-minute product walkthrough video embedded ⇒ lazy-loaded
- [ ] T075 [opus] Below-video: key screens in static cards ⇒ Storybook each
- [ ] T076 [opus] "Try it with a real session" option: upload `.ibt` or use sample ⇒ CTA to app.lap.com sample path
- [ ] T077 [opus] Sample session data: pre-seeded Sebring session viewable without signup (read-only) ⇒ linked
- [ ] T078 [opus] Call-outs on each screen explaining what it does ⇒ annotations
- [ ] T079 [opus] Transcript of video ⇒ linked (a11y + SEO)
- [ ] T080 [sonnet] Video controls: keyboard accessible ⇒ tested
- [ ] T081 [sonnet] Demo page LCP <2s (video lazy) ⇒ achieved
- [ ] T082 [sonnet] Demo mobile layout: video full-width ⇒ responsive
- [ ] T083 [sonnet] A11y ⇒ axe clean
- [ ] T084 [sonnet] Conversion tracking: demo_viewed event ⇒ PostHog
- [ ] T085 [sonnet] Post-demo CTA: "Start your trial" prominent ⇒ wired
- [ ] T086 [sonnet] Testimonial placement post-video ⇒ structured
- [ ] T087 [sonnet] Video captions + subtitles ⇒ uploaded
- [ ] T088 [sonnet] SEO: target "sim racing telemetry demo" ⇒ meta
- [ ] T089 [sonnet] Related links: how-it-works, pricing ⇒ placed
- [ ] T090 [sonnet] E2E: demo page → CTA → signup ⇒ green

## Block F — Waitlist + email capture (T091–T105)

- [ ] T091 [opus] Waitlist form component: email only, consent-compliant ⇒ submits
- [ ] T092 [opus] Backend for form: Cloudflare Worker → forwards to Resend "waitlist" audience ⇒ tested
- [ ] T093 [opus] Spam protection: Cloudflare Turnstile ⇒ tested
- [ ] T094 [opus] Double-opt-in email: "Confirm your email to join the LAP waitlist" ⇒ sent via Resend
- [ ] T095 [opus] Post-confirm redirect to a personal welcome page ⇒ renders
- [ ] T096 [opus] Waitlist welcome email drip (3 emails over 2 weeks) ⇒ scheduled
- [ ] T097 [sonnet] Waitlist email 1: what LAP is + when launch ⇒ copy written
- [ ] T098 [sonnet] Waitlist email 2: behind-the-scenes dev update + upcoming features ⇒ copy written
- [ ] T099 [sonnet] Waitlist email 3: beta access invitation + founder pricing ⇒ copy written
- [ ] T100 [sonnet] Unsubscribe link + handling ⇒ works
- [ ] T101 [sonnet] GDPR compliance: consent checkbox + privacy link ⇒ present
- [ ] T102 [sonnet] Waitlist count public (optional): "Join 247 sim racers waiting" ⇒ rendered if ≥100 signups
- [ ] T103 [sonnet] PostHog events: waitlist_submitted, waitlist_confirmed ⇒ tracked
- [ ] T104 [sonnet] Tests: form submission, email delivery, drip timing ⇒ green
- [ ] T105 [sonnet] Waitlist data export for founder to see list ⇒ works

## Block G — Product pages per pillar (T106–T130)

- [ ] T106 [design] Figma: product pages (/product, /product/desktop, /product/mobile, /product/bridge) ⇒ approved
- [ ] T107 [opus] `/product` overview ⇒ renders
- [ ] T108 [opus] `/product/desktop` page: sim capture + live coaching + strategy ⇒ renders
- [ ] T109 [opus] `/product/desktop` screenshots + video ⇒ embedded
- [ ] T110 [opus] `/product/desktop` download CTA → GitHub Releases ⇒ linked
- [ ] T111 [opus] `/product/desktop` supported sims list ⇒ bullet grid
- [ ] T112 [opus] `/product/desktop` system requirements ⇒ clear
- [ ] T113 [opus] `/product/mobile` page: real-life capture + Android ⇒ renders
- [ ] T114 [opus] `/product/mobile` Google Play badge ⇒ placed
- [ ] T115 [opus] `/product/mobile` RaceBox integration explained ⇒ clear
- [ ] T116 [opus] `/product/mobile` Wear OS companion ⇒ mentioned
- [ ] T117 [opus] `/product/bridge` page: sim↔real transfer narrative ⇒ renders
- [ ] T118 [opus] `/product/bridge` example transfer report screenshot ⇒ embedded
- [ ] T119 [opus] `/product/bridge` "how it works" algorithm teaser ⇒ renders
- [ ] T120 [opus] `/product/coaching` page: coaching library preview ⇒ renders
- [ ] T121 [opus] `/product/coaching` sample weaknesses + prescriptions ⇒ shown
- [ ] T122 [opus] `/product/driver-profile` page: progression narrative ⇒ renders
- [ ] T123 [opus] Cross-linking between product pages ⇒ consistent
- [ ] T124 [sonnet] Product pages shared layout ⇒ DRY
- [ ] T125 [sonnet] A11y + responsive across all product pages ⇒ clean
- [ ] T126 [sonnet] SEO per page: target keyword per pillar ⇒ meta tuned
- [ ] T127 [sonnet] Performance: LCP <2s per product page ⇒ achieved
- [ ] T128 [sonnet] Download page analytics: downloads_initiated event ⇒ tracked
- [ ] T129 [sonnet] Tests for download-button integrity ⇒ green
- [ ] T130 [sonnet] iOS page (coming-soon state) ⇒ renders with waitlist CTA

## Block H — SEO pillar pages (T131–T170) — 4 pillars × 10 tasks each

### Pillar 1: "Sim to Real-Life Racing Transfer" (T131–T140)
- [ ] T131 [opus] Keyword research + outline (3000+ words) ⇒ outline
- [ ] T132 [opus] Section 1: what transfers, what doesn't (with data) ⇒ draft
- [ ] T133 [opus] Section 2: shape vs intensity framework ⇒ draft
- [ ] T134 [opus] Section 3: track geometry analysis ⇒ draft
- [ ] T135 [opus] Section 4: case studies (Sebring, Silverstone, Nürburgring) ⇒ draft
- [ ] T136 [opus] Section 5: how to measure transfer yourself ⇒ draft
- [ ] T137 [opus] Editing pass: tighten prose, remove fluff ⇒ reviewed
- [ ] T138 [sonnet] Add internal links (to product pages, other pillar) ⇒ linked
- [ ] T139 [sonnet] Add FAQ section + schema.org markup ⇒ structured
- [ ] T140 [sonnet] Publish + indexing submission ⇒ in Google Search Console

### Pillar 2: "What is Trail Braking (and how to measure it)" (T141–T150)
- [ ] T141 [opus] Outline ⇒ done
- [ ] T142 [opus] Section 1: physics of trail braking ⇒ draft
- [ ] T143 [opus] Section 2: common mistakes + data signatures ⇒ draft
- [ ] T144 [opus] Section 3: how LAP detects it ⇒ draft
- [ ] T145 [opus] Section 4: drill progression to improve ⇒ draft
- [ ] T146 [opus] Section 5: examples from real telemetry ⇒ draft
- [ ] T147 [opus] Editing ⇒ done
- [ ] T148 [sonnet] Internal linking ⇒ done
- [ ] T149 [sonnet] FAQ + schema ⇒ done
- [ ] T150 [sonnet] Publish ⇒ indexed

### Pillar 3: "Best Sim Racing Telemetry Apps Compared (2026)" (T151–T160)
- [ ] T151 [opus] Outline: comparison of LAP, Garage61, RaceLab, MoTeC, Track Attack, STINT ⇒ done
- [ ] T152 [opus] Section 1: what each does well ⇒ draft
- [ ] T153 [opus] Section 2: what each lacks ⇒ draft
- [ ] T154 [opus] Section 3: pricing comparison ⇒ table
- [ ] T155 [opus] Section 4: choosing by persona (casual, competitive, team coach) ⇒ draft
- [ ] T156 [opus] Section 5: honest LAP limitations ⇒ trust-building
- [ ] T157 [opus] Editing ⇒ done
- [ ] T158 [sonnet] Internal linking ⇒ done
- [ ] T159 [sonnet] FAQ + schema ⇒ done
- [ ] T160 [sonnet] Publish ⇒ indexed

### Pillar 4: "How to Build a Driver Development Plan" (T161–T170)
- [ ] T161 [opus] Outline ⇒ done
- [ ] T162 [opus] Section 1: what a development plan is (vs aimless practice) ⇒ draft
- [ ] T163 [opus] Section 2: framework (diagnose → prescribe → execute → measure → adapt) ⇒ draft
- [ ] T164 [opus] Section 3: weekly / monthly / event-cycle cadences ⇒ draft
- [ ] T165 [opus] Section 4: how LAP automates this ⇒ draft
- [ ] T166 [opus] Section 5: DIY template for non-LAP users ⇒ draft
- [ ] T167 [opus] Editing ⇒ done
- [ ] T168 [sonnet] Internal linking ⇒ done
- [ ] T169 [sonnet] FAQ + schema ⇒ done
- [ ] T170 [sonnet] Publish ⇒ indexed

## Block I — Blog posts (T171–T200) — 10 posts × 3 tasks each

### Batch 1 (T171–T180): Coaching rule deep-dives
- [ ] T171 [opus] "Late Braking at T1: What Your Telemetry Is Saying" — draft ⇒ done
- [ ] T172 [opus] "Throttle Pickup: Smooth vs Aggressive" — draft ⇒ done
- [ ] T173 [opus] "Apex Speed: The Real Measure of Corner Commitment" — draft ⇒ done
- [ ] T174 [opus] "Consistency Over Raw Pace: Why Your Average Matters" — draft ⇒ done
- [ ] T175 [opus] "Tire Management in Endurance: Data Signals" — draft ⇒ done
- [ ] T176 [sonnet] Editing pass on batch 1 ⇒ done
- [ ] T177 [sonnet] Batch 1 internal linking ⇒ done
- [ ] T178 [sonnet] Batch 1 FAQ + schema ⇒ done
- [ ] T179 [sonnet] Batch 1 publish ⇒ all indexed
- [ ] T180 [sonnet] Batch 1 social media kit (5 tweets/post) ⇒ drafted

### Batch 2 (T181–T190): Founder / product stories
- [ ] T181 [opus] "Why I'm Building LAP (and Not Another MoTeC Clone)" — draft ⇒ done
- [ ] T182 [opus] "The Sim-to-Real Gap: A Honest Look" — draft ⇒ done
- [ ] T183 [opus] "Designing Coaching That Drivers Actually Follow" — draft ⇒ done
- [ ] T184 [opus] "Pre-launch Month in Numbers" — draft (monthly update) ⇒ done
- [ ] T185 [opus] "What We're NOT Building (and Why)" — draft ⇒ done
- [ ] T186 [sonnet] Editing pass on batch 2 ⇒ done
- [ ] T187 [sonnet] Batch 2 internal linking ⇒ done
- [ ] T188 [sonnet] Batch 2 FAQ + schema ⇒ done
- [ ] T189 [sonnet] Batch 2 publish ⇒ all indexed
- [ ] T190 [sonnet] Batch 2 social kit ⇒ drafted

### Blog infrastructure (T191–T200)
- [ ] T191 [opus] Blog listing page `/blog` ⇒ renders
- [ ] T192 [opus] Blog post layout with TOC + reading-time ⇒ Storybook
- [ ] T193 [opus] Author cards ⇒ rendered
- [ ] T194 [opus] Tags + categories ⇒ filterable
- [ ] T195 [opus] Related-posts component ⇒ renders
- [ ] T196 [opus] RSS feed `/blog/rss.xml` ⇒ valid
- [ ] T197 [opus] Newsletter embed in blog posts ⇒ captures emails
- [ ] T198 [sonnet] Blog post OG images auto-generated ⇒ works
- [ ] T199 [sonnet] Blog post a11y + responsive ⇒ clean
- [ ] T200 [sonnet] Blog post performance: LCP <2s ⇒ achieved

## Block J — B2B + launch + ops (T201–T220)

- [ ] T201 [opus] `/for-schools` landing: karting academies + racing schools ⇒ renders
- [ ] T202 [opus] B2B hero + value-prop + case-study placeholder ⇒ renders
- [ ] T203 [opus] B2B form: name, school, students-count, email, message ⇒ submits
- [ ] T204 [opus] B2B form → Resend → sales@lap.com inbox + confirmation email ⇒ tested
- [ ] T205 [opus] B2B pricing overview (anchor, not commit) ⇒ "from €X/seat/mo, contact us" 
- [ ] T206 [opus] B2B social proof slots ⇒ scaffolded
- [ ] T207 [sonnet] Press kit page `/press`: logo files, screenshots, founder bio, facts ⇒ renders
- [ ] T208 [sonnet] Press release template for launch ⇒ drafted
- [ ] T209 [opus] Public beta launch landing page (one-off, featured for launch week) ⇒ renders
- [ ] T210 [opus] V1 launch landing page ⇒ renders later
- [ ] T211 [opus] Launch-day blog post "Introducing LAP" ⇒ drafted + scheduled
- [ ] T212 [sonnet] Launch content: 5 Reddit posts for r/iRacing, r/simracing, r/CarRacing, r/TrackRacing, r/karting ⇒ drafted
- [ ] T213 [sonnet] Launch content: 3 Discord announcement drafts ⇒ ready
- [ ] T214 [sonnet] YouTube short 2-min demo script ⇒ drafted
- [ ] T215 [sonnet] Twitter thread launch: 8 tweets ⇒ drafted
- [ ] T216 [sonnet] LinkedIn launch post ⇒ drafted
- [ ] T217 [sonnet] Product Hunt launch page ⇒ drafted
- [ ] T218 [sonnet] Analytics events: signup_clicked, demo_viewed, pricing_viewed, waitlist_submitted, download_clicked ⇒ all firing
- [ ] T219 [sonnet] Conversion funnel dashboards in PostHog ⇒ configured
- [ ] T220 [sonnet] Final site audit: broken links, missing meta, a11y, performance ⇒ all green
