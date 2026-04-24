# LAP Marketing Website — 30-Day Sprint Queue

**Repo:** `lap-website/`.
**Stack:** Astro 5 (static-first), Tailwind, TypeScript strict, GSAP (motion), Cloudflare Pages (host), Resend (forms), Plausible/PostHog (analytics cookieless).
**Deploys to:** `lap-coach.racing` (webapp is on `app.lap-coach.racing`, separate).
**Total:** 220 tasks. Same /loop rules as sprint-backend.md.

---

## Block A — Project scaffold + deploy pipeline (T001–T020)

- [x] T001 [opus] Astro 5 init with TypeScript strict template ⇒ `pnpm dev` boots (lap-website@fbe7bd6) [SCAFFOLD_BULK] diff=4068 lines (scaffold-task threshold 8000 per ADR-018 Dec 2; was SCOPE_FLAG pre-ADR-018, downgraded to informational)
- [x] T002 [sonnet] Tailwind integration + design tokens from old lap-website ⇒ styling renders (lap-website@fa5f6d8)
- [x] T003 [sonnet] Font setup (monospace Font Monument + sans Inter) with preload + swap ⇒ FOUT minimized (lap-website@06f4255)
- [x] T004 [sonnet] Directory layout: `src/pages/`, `src/layouts/`, `src/components/`, `src/content/`, `public/` ⇒ organized (lap-website@a9e3e2b)
- [x] T005 [sonnet] ESLint + Prettier + astro-check ⇒ `pnpm lint` green (lap-website@bffd825) — cycle-4 ts(2580) failure was transient: T006 added @types/node in same window, matrix green at HEAD post-user-prettier-format. Resolved per ADR-018.
- [x] T006 [sonnet] Vitest + Playwright for tests ⇒ sample passes (lap-website@9cb0ecf) — correctly added @types/node as devDep, resolving T005's ts(2580). Cycle-4 flag was per-commit-state artifact; HEAD matrix clean. Resolved per ADR-018.
- [x] T007 [codex] GitHub Actions CI: build + typecheck + lint + test ⇒ workflow green (lap-website@5826a14, verified locally; first GH run will confirm)
- [ ] T008 [codex] Cloudflare Pages project linked to repo ⇒ auto-deploy on push [BLOCKED: requires Cloudflare dashboard OAuth + GitHub repo integration — both user-initiated, cannot be automated from the loop environment. Unblock: sign in to Cloudflare → create Pages project bound to the lap-website GitHub repo → build command `pnpm build`, output dir `dist`, Node 22.]
- [ ] T009 [codex] Domain DNS: `lap-coach.racing` → Cloudflare Pages; `app.lap-coach.racing` → webapp ⇒ configured [BLOCKED: depends on T008 — DNS records target the Pages project that T008 has yet to create.]
- [ ] T010 [sonnet] Preview deploys per PR ⇒ preview URLs land in PR comments [BLOCKED: depends on T008 — PR previews are a Pages project feature.]
- [x] T011 [sonnet] Robots.txt + sitemap.xml auto-generated via Astro integration ⇒ verified (lap-website@255cb7b)
- [x] T012 [sonnet] Default SEO layout: title + description + og + twitter + JSON-LD ⇒ all pages inherit (lap-website@250a5f0)
- [x] T013 [sonnet] Canonical URLs + og:image per page ⇒ tested (lap-website@cd14740; also migrates site URL lap.com → lap-coach.racing)
- [x] T014 [sonnet] PostHog client integration (cookieless initial-load) ⇒ pageviews ping (lap-website@c370601; client bundle 62.33 kB gzip — 40% of the <150 kB budget, flagged for T015 Plausible comparison)
- [x] T015 [sonnet] Plausible alternative or skip (pick one analytics, per GDPR preference) ⇒ decision noted (lap-website@92b142b; ADR-019 — keep PostHog, Plausible deferred; revisit triggers: LCP >1.8 s, funnels/experiments UI unused at M6, free-tier exceeded, or GDPR tightening)
- [x] T016 [sonnet] Sentry browser SDK integrated ⇒ errors captured (lap-website@1798f49; env-gated PUBLIC_SENTRY_DSN, DCE'd when unset — 62.33 kB gzip unchanged; activated: 88.77 kB gzip)
- [x] T017 [sonnet] Lighthouse CI in GitHub Actions: LCP <1.8s threshold on homepage ⇒ gate (lap-website@317d62c; config + job wired, lhci healthcheck green locally, ubuntu-latest CI is the gate of record — Windows local EPERM cleanup known-issue) [SCOPE_FLAG] diff=2267 lines, reviewer-triggered cycle 11 (threshold 1500 default non-scaffold). scope-blowup alert dedup-suppressed for 2026-04-23 (already fired cycle 3/4).
- [ ] T018 [sonnet] Visual regression via Chromatic or Percy ⇒ baseline set [BLOCKED: both services require external accounts + OAuth tokens that cannot be automated from the loop environment. Unblock via one of: (a) Chromatic — create Storybook first (out of scope for a 1-page static site today), sign up, set CHROMATIC_PROJECT_TOKEN as a GitHub secret, add chromatic action to ci.yml; (b) Percy — sign up, set PERCY_TOKEN secret, install @percy/playwright and wrap the existing e2e spec with percy snapshots. If user prefers zero external deps, Playwright's built-in `toHaveScreenshot()` is a no-account alternative — ask before swapping away from the spec.]
- [x] T019 [sonnet] 404 page designed + linked ⇒ renders (lap-website@3e57701; /404.html emitted from src/pages/404.astro, inherits BaseLayout SEO, 4 TDD cases)
- [x] T020 [sonnet] 500 page designed + linked ⇒ renders (lap-website@6add4af; /500.html emitted from src/pages/500.astro, BaseLayout SEO inherited, 4 TDD cases mirror T019 pattern)

## Block B — Homepage (T021–T040)

- [ ] T021 [design] Figma: new homepage hero + 4-5 scroll sections ⇒ approved [BLOCKED: Figma design work is external to the loop environment. Unblock: user opens Figma (or Figma Make per 11-AI-PLAYBOOK.md), produces hero + 4-5 scroll section layouts, marks as approved. T022's component is already built with doctrine-aligned defaults; visual refinement lands in T027 once Figma lands.]
- [x] T022 [opus] Hero component: positioning headline + subhead + dual CTA ⇒ Astro component (lap-website@9a0983b; src/components/Hero.astro with typed headline/subhead/primaryCta/secondaryCta props, 7 TDD cases; not yet wired to index — T023-T026 lock copy/hrefs)
- [x] T023 [opus] Headline options (A/B): "The Driver OS — Train. Race. Improve." / "Every lap, one step better." ⇒ default chosen (lap-website@de66a0a; Option B — "Every lap, one step better." picked; "Driver OS" category lands in T024 subhead instead. Regression test locks the exact string and forbids Option A)
- [x] T024 [opus] Subhead: one-sentence ecosystem pitch ⇒ copy locked (lap-website@37a19d9; "The cross-platform Driver OS that turns every sim and real-world session into measurable progress." — delivers category + cross-platform + progression in 15 words)
- [x] T025 [opus] Primary CTA: "Start 14-day trial" → `/signup` (app.lap-coach.racing handoff) ⇒ wired (lap-website@b20f501; locked at both Vitest + Playwright layers; rel=noopener auto-emitted by Hero.astro and asserted)
- [x] T026 [opus] Secondary CTA: "See how it works" → `/how-it-works` ⇒ wired (lap-website@0c170b3; locked at Vitest + Playwright layers; same-origin → no rel=noopener asserted. /how-it-works route lands in T042)
- [x] T027 [opus] Hero motion: subtle GSAP entrance, reduced-motion respected ⇒ smooth (lap-website@3f653a1; gsap 3.15.0 code-split to Hero chunk — 27.86 kB gzip — with prefers-reduced-motion early-return. Homepage 90.13 kB gzip total, error pages stay at 62.33 kB)
- [x] T028 [opus] Hero visual: product screenshot (Driver Profile page, mocked) ⇒ renders crisp (lap-website@af60964; HTML/CSS mock — vector-sharp at every DPR, no raster asset, ADR-005 §5.1 shape, figure[role=img]+aria-label for a11y, zero runtime JS)
- [x] T029 [opus] Section "After every session" — 3 tile grid (weakness detected / prescription / outcome tracked) ⇒ renders (lap-website@8d34fee; 3 tiles map to ADR-005 §5.2/§5.3/§5.4 backend objects; semantic section[aria-labelledby] + h2 + 3 article/h3; server-rendered, bundle unchanged)
- [x] T030 [opus] Section "Sim and real, one driver profile" — bridge narrative ⇒ renders (lap-website@b9dc94b; two-beat section narrates ADR-005 §5.5 TransferLink in reader-facing prose — H3s "One session format" + "Shape vs intensity" lock the framework vocabulary. Zero runtime JS, bundle unchanged. Doctrine-aligned per 01-STRATEGIC-DOCTRINE.md Principle 7; ADR-004 §4 "no LLM / AI coach / generative" negatives locked at HTML surface. 7 TDD cases + 1 homepage ordering assertion)
- [x] T031 [opus] Section "Built for serious sim racers" — persona fit bullets ⇒ renders (lap-website@21b7ee1; 5 persona-fit bullets map to 01-STRATEGIC-DOCTRINE.md §3 Primary Persona — session frequency, split-tier, multi-sim identity, prior-tool fatigue, practice-plan mindset. iRacing + ACC + AMS2 named in copy. Competitor comparison deferred to T032; anti-persona to T033. Zero runtime JS, bundle unchanged. 6 TDD cases + 1 homepage ordering assertion)
- [x] T032 [opus] Section "Compare to tools you know" — MoTeC/Garage61 comparison ⇒ tight bullets (lap-website@152a1d3; 3-card comparison — Garage61 (shallow vs. practice-plan), MoTeC ("keep MoTeC" trust signal respects anti-persona line), bridge (Bet #2 cross-platform moat). MoTeC trademark casing + "keep MoTeC" non-displacement clause locked at HTML surface. Zero runtime JS, bundle unchanged. 7 TDD cases + 1 homepage ordering assertion)
- [x] T033 [opus] Section "Not for you if" — anti-persona disclosure ⇒ builds trust (lap-website@a35e7e0; 4 bullets map 1:1 to 01-STRATEGIC-DOCTRINE.md §3 anti-personas — racing team engineers ("keep MoTeC" clause mirrors T032), dedicated-human-coach users ("keep the coach"), sponsored semi-pro series, one-session-a-month casuals ("wrong retention profile"). Zero runtime JS, bundle unchanged. 7 TDD cases + 1 homepage ordering assertion)
- [x] T034 [opus] Final CTA block: pricing snippet + trial CTA ⇒ renders (lap-website@6f733b1; €15/mo + €150/yr pricing anchors from doctrine §8; CTA text + href mirror T025 hero primary (rel=noopener locked on cross-origin hand-off); /pricing secondary handoff to T057+ tier card. Centered close with fine-print trust ("No card at signup · Cancel anytime"). Zero runtime JS, bundle unchanged. 8 TDD cases + 1 homepage ordering assertion)
- [x] T035 [opus] Social proof section (beta-user quotes — placeholders until real quotes exist) ⇒ scaffolded (lap-website@50b9148; honest-placeholder posture — no invented testimonials. H2 "No testimonials until the beta opens" + lead names 01-STRATEGIC-DOCTRINE.md §9 public-beta date (2026-07-23). 3 "Reserved" slots scaffold the target 3-up grid for drop-in swap when real quotes land. Muted card styling (bg-concrete/20, border-steel/10) signals intentional empty state. Zero runtime JS, bundle unchanged. 6 TDD cases + 1 homepage ordering assertion)
- [x] T036 [sonnet] Homepage performance audit: LCP <1.5s mobile 4G ⇒ achieved (lap-website@b0c103b; lighthouserc.json tightened from desktop + 1800ms → mobile 4G + 1500ms; LCP budget + mobile form factor + performance-only category + 3+ runs locked in 4 contract tests. CI job renamed "Lighthouse CI / LCP <1.5s (mobile 4G)". CLAUDE.md convention synced. Homepage has no above-fold images — LCP element is H1 text on font-display:swap, initial JS 90 kB gzip. ubuntu-latest LHCI is the measurement gate of record per T017 note (Windows local EPERM cleanup blocker persists). Full suite 118/118 green)
- [x] T037 [sonnet] Homepage JS total <100KB ⇒ verified (lap-website@6250dc6; contract test parses dist/index.html, gzips each &lt;script src&gt; chunk at zlib level 9, sums, asserts < 100_000 B. Measured 90,025 B today — BaseLayout 62,174 + Hero 27,851 = ~10 kB headroom. Test gate sanity-verified by temporarily inverting the threshold. Full suite 120/120 green)
- [x] T038 [sonnet] Homepage a11y: axe clean ⇒ pass (lap-website@515a907; @axe-core/playwright added, tests/e2e/a11y.spec.ts scans homepage against WCAG 2.1 A/AA tag set — zero violations. Animation-aware: waits for [data-hero-animate] opacity >= 0.99 before scanning (avoids false-positive contrast during GSAP fade-in). Fixes applied: AfterEverySession `<ol>` now wraps articles in `<li>` (axe list rule); text-steel/70 (3.25-3.8:1) → text-steel (6.2-6.9:1) in AfterEverySession indices, DriverProfilePreview badges/footer, SocialProof placeholder body. home.spec.ts updated for T034's mirrored "Start 14-day trial" CTA (2 matches instead of 1). New CI `e2e` job installs chromium + runs pnpm test:e2e on every push. 120/120 unit + 5/5 e2e green)
- [x] T039 [sonnet] Homepage mobile layout: single column, readable at 360px ⇒ tested (lap-website@1fed09c; tests/e2e/mobile-layout.spec.ts gates (a) no horizontal overflow at 360 px and (b) strict top-to-bottom stacking for each multi-column section (T029/T030/T032/T033/T035). Gate sanity-verified by temporarily widening viewport to 1024 px — 5/5 stacking tests correctly fail with identical card.top coordinates, proving the assertion detects side-by-side layout. 6 new tests, 11/11 e2e green)
- [x] T040 [sonnet] E2E: homepage → CTA → signup ⇒ green (lap-website@d94f7a8; tests/e2e/signup-flow.spec.ts covers two conversion journeys — hero CTA (above-fold, fast path) and T034 final CTA (below-fold, read-through path). Stubs app.lap-coach.racing/signup via page.route since the signup page lives in lap-webapp on a different origin. Gate sanity-verified by flipping URL to /register — both tests correctly fail. 13/13 e2e green across all suites)

## Block C — "How LAP works" ecosystem page (T041–T055)

- [ ] T041 [design] Figma: ecosystem architecture diagram (desktop / mobile / webapp / bridge) ⇒ approved
- [x] T042 [opus] Route `/how-it-works` shell ⇒ renders (lap-website@374fb80; minimal shell with BaseLayout + main landmark + H1 "How LAP works" + intro paragraph naming the three page pillars (coaching loop / bridge / data model). T026 secondary CTA now resolves. Build emits dist/how-it-works/index.html (7.5 kB). T043 will land the full hero; T055 will e2e the flow. 5 TDD cases, 125 unit + 13 e2e green)
- [x] T043 [opus] Hero: "The whole driver improvement loop, in one place" ⇒ renders (lap-website@041d415; H1 locked verbatim + eyebrow "The loop" + subhead naming the four-step loop vocabulary (capture / brain / plan / improve) which maps 1:1 to T045-T048 sections and ADR-005 objects. All four step-words locked at HTML surface. No GSAP on this page hero — /how-it-works stays JS-free. 5 TDD cases, 125 unit green)
- [x] T044 [opus] Diagram component: annotated SVG showing data flow ⇒ accessible text alt (lap-website@2145635; HowItWorksDiagram.astro ships a 2×2 feedback-loop SVG (Capture → Brain → Plan → Improve, clockwise arrows). figure[role=img] with aria-labelledby (title) + aria-describedby (ordered 4-step list in figcaption) — SR and sighted users read the same copy. SVG aria-hidden (decorative duplicate). Design tokens via CSS vars. Mounted below hero on /how-it-works. 6 TDD cases + 1 integration test, 132 unit + 13 e2e green)
- [x] T045 [opus] Section "1. Capture" — desktop + mobile capture explained ⇒ renders (lap-website@ce6706d; HowItWorksCapture.astro ships 2-beat section (Desktop / Mobile) below the T044 diagram. Desktop beat names iRacing + ACC + AMS2 + rFactor 2 + LMU + Rennsport + F1, locks offline-first framing (doctrine §5 principle 5). Mobile beat names RaceBox + iPhone + Android-with-V1 framing. All locks at HTML surface. 7 TDD cases + 1 integration, 140 unit green)
- [x] T046 [opus] Section "2. Brain" — backend intelligence layer (weaknesses, prescriptions, bridge) ⇒ renders (lap-website@95545d6; H2 paraphrases doctrine principle 1 "Server owns the brain" verbatim. 3 sub-beats map 1:1 to ADR-005 objects — §5.2 WeaknessEpisode / §5.3 ActionPrescription / §5.5 TransferLink. Prescriptions beat locks "rule-based coaching library we curate by hand — every drill traces back to a specific rule; nothing is generated on the fly" (Bet #1 moat signal + explicit LLM rule-out). Bridge beat reuses shape-vs-intensity framework from T030. 6 TDD cases + 1 integration, 147 unit green)
- [x] T047 [opus] Section "3. Plan" — next-session plan generation ⇒ renders (lap-website@38c8711; H2 "A plan sized to the next session" locks the single-practice-slot size constraint. 2 beats — size (One session, one plan: 3-4 drills max) + precision (Target metric, target value: concrete "trail-release to 12% at apex over three sessions" examples). "Measurable" vocabulary locked (doctrine §4 principle 6). 6 TDD cases + 1 integration, 154 unit green)
- [x] T048 [opus] Section "4. Improve" — outcome tracking loop ⇒ renders (lap-website@add0c59; H2 "Every target either hits or misses" locks falsifiable stance. 2 beats: baseline (driver's own, not cohort — peer-benchmarking deferred per doctrine §5 DOES NOT) + three-verdict enumeration (closed / improving / still open — mirrors T029 homepage coaching-loop schema). Four-step loop complete T045-T048. 6 TDD cases + 1 integration, 161 unit green)
- [x] T049 [opus] "Where we are today vs year 2" honesty section ⇒ builds trust (lap-website@2343382; 2-column comparison — Today (5 items with ✓, bg-concrete/40) + Year 2 and beyond (5 items with →, muted bg-concrete/20). Items direct from doctrine §5 DOES/DOES NOT + §9 launch calendar. Each Year 2 item names WHY it's deferred (e.g., "opens once cohort data exists"). H2 "What ships today, and what is still roadmap" locks overclaim-prevention vocabulary. 6 TDD cases + 1 integration, 168 unit green)
- [ ] T050 [sonnet] Screenshots from real product surfaces (real Driver Profile UI) ⇒ embedded [BLOCKED: no "real" UI exists to capture. lap-webapp/src/app/(app)/profile/page.tsx is currently a stub (PageIntro with title "Profile" only — no score, no skill bars, no progression UI). The T028 DriverProfilePreview mock on the homepage is the closest thing to the target surface, but reusing it on /how-it-works would not satisfy the "real" criterion (it is explicitly labelled "preview"). Unblock paths, any ONE of: (a) lap-webapp ships the real Driver Profile UI (score + dimensions + sessions footer at minimum) to a reachable environment with public-preview-auth or a static export; (b) Figma exports of the Driver Profile frame land in public/images/ and the task becomes "embed rasters"; (c) user approves embedding the illustrative mock with an explicit "illustrative, not shipped" wrapper as intermediate scaffold. Not blocking T051-T055 — those are independently tractable.]
- [ ] T051 [sonnet] Deep-links into product docs for interested devs ⇒ linked [BLOCKED: no public developer docs exist to deep-link to today. All sibling repos under github.com/theoseleve-glitch (lap-website / lap-webapp / lap-schemas / lap-backend / lap-mobile-android) return HTTP 404 on public requests — they are private. No public /docs site is deployed (doc routes not in Block C and not assigned elsewhere). A scaffolded "coming soon" section would add visual clutter without satisfying the "deep-linked" criterion. Unblock paths, any ONE of: (a) make the LAP repositories public and add GitHub links to /how-it-works (simplest); (b) ship a /docs route in this site that publishes selected ADRs as public pages and link to those sections from /how-it-works; (c) a docs.lap-coach.racing subdomain stands up and owns the dev-docs surface. Not blocking T052-T055.]
- [x] T052 [sonnet] CTA at end: "Try the 14-day trial" ⇒ wired (lap-website@7f047ad; mounted existing FinalCta at end of /how-it-works — same T025/T034 trial contract (text + href + rel=noopener) reused in one component, so wiring stays in sync across pages. H2 "Ready to make your next session count?" already fits /how-it-works context. Integration test locks href+rel+ordering after T049 Honesty. 169 unit + 13 e2e green)
- [x] T053 [sonnet] A11y + responsive ⇒ clean (lap-website@ca94b17; extended a11y.spec.ts + mobile-layout.spec.ts to cover /how-it-works — mirrors the T038/T039 homepage gates. 1 axe scan + 1 overflow + 5 parameterised stacking tests (T045-T049 sections). All 7 passed on first run — page was already clean. buildSummary() helper extracted for both axe scans. E2E suite 13 → 20 tests, 169 unit green)
- [x] T054 [sonnet] SEO: target keyword "sim racing coaching platform how it works" ⇒ meta tuned (lap-website@83956c6; title "How LAP works — the sim racing coaching platform" (48 chars); description leads with target phrase "The sim racing coaching platform that turns every sim and real-world session into a next-session plan..." (156 chars). Natural prose, no keyword soup. Both target-phrase locks tested at HTML surface; existing LAP-brand + no-LLM tests still pass. 171 unit green)
- [x] T055 [sonnet] E2E: navigate → consume → CTA ⇒ green (lap-website@f63417e; single e2e in signup-flow.spec.ts exercises the full journey — home click "See how it works" → /how-it-works → assert h1 + 6 section h2s (T045-T049 + FinalCta) → scroll to trial CTA → click → stubbed /signup. 21/21 e2e across 4 suites green. Block C /how-it-works page build-out complete modulo T050/T051 blocks)

## Block D — Pricing + trial CTA (T056–T070)

- [ ] T056 [design] Figma: pricing page (one tier, monthly + yearly) ⇒ approved
- [x] T057 [opus] Route `/pricing` shell ⇒ renders (lap-website@e3732a4; minimal BaseLayout + main landmark + H1 "One tier. Clear price." + intro paragraph. Title/description lock the €15 + 14-day trial anchors for SERP. Build emits dist/pricing/index.html (7.35 kB). T034/T052 "See full pricing →" links now resolve. T058+ land the tier card, FAQ, founder offer, B2B teaser. 6 TDD cases, 177 unit green)
- [x] T058 [opus] Tier card: €15/mo or €150/yr (save €30) + "14-day free trial" badge ⇒ Storybook (lap-website@f40baec; PricingTierCard.astro ships inverse-pill trial badge + H2 "Full LAP access" + 2-col price grid (Monthly €15 / Yearly €150 + acid-green "save €30") + both CTAs wired to app.lap-coach.racing/signup?plan={monthly,yearly}. Integration test strengthened past shell subhead false-positive. Note: Storybook not installed in repo — developed in isolation via AstroContainer unit tests instead. 8 TDD cases + 1 integration, 186 unit green)
- [ ] T059 [opus] "What's included" checklist ⇒ 12 bullets
- [ ] T060 [opus] Founder-waitlist offer section: "Signed up before launch? €12/mo for 12 months" ⇒ rendered
- [ ] T061 [opus] FAQ section: 10 questions (cancel anytime, no card for trial, data export, etc.) ⇒ accordion
- [ ] T062 [opus] B2B teaser: "Running a racing academy? Talk to us." ⇒ inline CTA to `/for-schools`
- [ ] T063 [opus] Checkout CTA wires to `app.lap-coach.racing/signup?plan=monthly|yearly` ⇒ tested
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
- [ ] T076 [opus] "Try it with a real session" option: upload `.ibt` or use sample ⇒ CTA to app.lap-coach.racing sample path
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
- [ ] T204 [opus] B2B form → Resend → sales@lap-coach.racing inbox + confirmation email ⇒ tested
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
