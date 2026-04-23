# Content Playbook

Reference doc for running the content side of LAP. Editorial calendar, voice guide, SEO approach, racing-theory book list for grounding the coaching library.

---

## Voice + tone

From doctrine Q149 + marketing tone decisions:

**What we are:** confident, measured, data-forward, respectful of the driver's time.
**What we're not:** bro, hypey, "unlock your potential", fake-technical, AI-generated slop, condescending.

### Writing rules

1. Open with the specific, not the universal. "Your apex speed at Spa T1 is 3 km/h short" beats "Master every corner."
2. Use numbers where available. "Trail-brake release curve steeper than 200 kPa/100ms" beats "be smoother."
3. Credit the reader's intelligence. Skip 101-explanations for material a competitive sim racer knows. Put them in a separate "Beginner primer" link.
4. Be honest about what we don't know. "Sim-to-real tire grip coefficient relationship is still being validated" beats "Transfers perfectly."
5. No "unlock". No "game-changer". No "AI coach". Don't promise "you'll" anything specific.
6. Active voice. Short sentences. Mix rhythm. Don't write to 9th-grade level — write to competitive-adult level.

### Skill-level-aware variants

The coaching library has 3 explanation levels. Honor them in the articles:

- **Beginner** — no telemetry jargon, lots of analogies, every technical term linked to a primer
- **Intermediate** — telemetry references with parenthetical explanation, light physics
- **Advanced** — full jargon, physics equations where they clarify, references to data traces

Blog + pillar pages default to **Intermediate** unless tagged specifically.

## Editorial calendar

### Month 1 (Days 1-30): Foundation Content

**Week 1:**
- Days 1-3: Setup (content pipelines, first pillar outline)
- Days 4-7: 2 flagship coaching articles/day (C001-C008 delivered)

**Week 2:**
- 1 pillar page final edit (C181-C185) + 2 flagship/day (C009-C020)

**Week 3:**
- 2 pillars edited (C186-C195) + 10 standard coaching articles (C031-C040)

**Week 4:**
- 2 pillars edited (C196-C200) + 20 standard coaching articles (C041-C060)

### Month 2 (Days 31-60): Coaching Library Push

Daily: 3 standard coaching articles. Total: 90 articles (C061-C150).

### Month 3 (Days 61-90): Library Completion + Docs

Week 1-2: 30 more standard articles (C151-C180) finishing the coaching library.
Week 3-4: Docs site content (C261-C280).

### Month 4+: Launch content + blog cadence

- 2 original blog posts/week
- 1 founder-log post/week (yours, H123)
- Weekly research memo

## SEO approach (no paid tools, AI-driven)

### Keyword strategy

**Pillar-page keywords** (high-volume, competitive, long content wins):
1. "sim to real racing transfer" — 2000-word pillar
2. "what is trail braking" — 2000-word pillar
3. "best sim racing telemetry apps" — 2000-word pillar (comparison)
4. "how to build a driver development plan" — 2000-word pillar (Runna-style appeal)

**Coaching library keywords** (long-tail, low competition, content moat wins):
- "[driving technique] + detection in telemetry" × 180 articles
- Exact rule IDs as searchable tags
- Corner-specific searches ("Eau Rouge apex speed", "T1 Spa trail brake") covered by corner-tagged content

**Brand keywords**:
- "LAP Coach", "LAP telemetry", "LAP sim racing"
- Claim these via About page + structured data

### On-page SEO per article

Every article must have:
- Title (55-60 chars) with primary keyword
- Meta description (150-155 chars) that's not keyword-stuffed
- H1 = title (or close variant)
- H2 section headers answering common related queries
- Schema.org/Article or FAQPage structured data (JSON-LD)
- Internal links: 3+ to related coaching articles + pillar pages
- External links: 1-2 authoritative sources (Wikipedia, university physics pages, manufacturer docs) for credibility
- Alt text on every image
- Publish date + updated date visible
- Author byline (Theo)
- Related-posts section at bottom

### Off-page / distribution (launch-timed)

- Submit sitemap to Google Search Console + Bing Webmaster
- Earn backlinks naturally via Reddit / forum helpful-answer engagement (no self-promotion — only link when directly asked or the link genuinely helps the conversation)
- Reach out to 5 sim-racing YouTubers with early trial + coaching article tailored to their community

### Measurement

Quarterly:
- Google Search Console: impressions + clicks per article
- PostHog: article → trial-signup funnel
- Identify top-5 performing articles → commission follow-ups or translations

## Racing-theory book library

Per your request E2, here's a curated list of books + papers ranked by utility for the coaching library. Mix of owned + to-acquire.

### Core recommendations (own these)

1. **Ross Bentley — Speed Secrets** (original + Speed Secrets 2, 3, 4, Inner Speed Secrets) — the foundational modern racing-theory text in English. Every coaching library article should reference these where applicable.
2. **Carl Lopez — Going Faster!** (Skip Barber series) — the best single-book intro to racing line, braking, throttle, weight transfer for the non-expert.
3. **Jackie Stewart — Principles of Performance Driving** — now out of print in most editions but findable. Perspective from a 3× F1 champ.
4. **Paul Van Valkenburgh — Race Car Engineering & Mechanics** — for the physics that underpin many coaching rules (tire grip, weight transfer, aero).
5. **Brian Beckman — Physics of Racing papers** (free online at `phors.locost7.info/contents.htm`) — compact, mathematically precise, excellent for grounding threshold calculations.

### Strong add-ons

6. **Alan Johnson — Driving in Competition** — older but clear on mental discipline and strategy.
7. **Mark Donohue — The Unfair Advantage** — memoir with insights into setup theory.
8. **William F. Milliken, Douglas L. Milliken — Race Car Vehicle Dynamics** — engineering-grade reference. Most comprehensive single text on vehicle dynamics; heavy, for selective citation.
9. **Peter Wright — Ferrari Formula 1: Under the Skin** — understanding F1-level engineering gives context for LAP's coaching ambition.
10. **Carroll Smith — Tune to Win / Drive to Win / Engineer to Win** — the "-to Win" series, especially *Tune to Win* for tire + setup + data relationships.

### Specialist picks

11. **Bob Bondurant — High Performance Driving** — fundamentals, good for the "beginner" explanation variants.
12. **Trevor Hartman — Vehicle Dynamics and Racing Simulation** — connects sim-racing physics to real-world.
13. **Formula 1 team telemetry post-race analyses** (Williams, Sauber, Autosport articles) — for language and format models of "how pros talk about laps."
14. **iRacing user-generated guides** — Matt Malone's series, Dave Cam's series. NOT for authority, but for understanding what the competitive community knows.

### Free online resources

- SAE papers on vehicle dynamics (via `sae.org`, some free, many paywalled via university)
- Optimum Lap (free tool) blog posts on lap-time theory
- MoTeC Academy free lessons
- iRacing Fanatec/Simucube blog posts on setup → driver-input relationships

### Your reading plan

- **Weeks 1-2**: Speed Secrets 1 + Going Faster! + Physics of Racing papers → extract 80 insights (H/W allocation)
- **Weeks 3-4**: Tune to Win + Race Car Vehicle Dynamics (selective) → extract 40 more insights
- **Month 2**: Milliken (deep dives for specific coaching rules)
- **Month 3**: Specialist books as needed per rule authoring

ChatGPT handles extraction: "Read this chapter, extract the 10 insights most applicable to building a rule-based coaching library for amateur sim racers."

## Content publishing cadence

Per A2 (publishing cadence not explicitly answered, but clear from scope):

- **Coaching articles (flagship + standard)**: Staged publish, 5-10/week. Don't dump 180 in one week — SEO prefers cadence. Target: finished library live by end of Month 4.
- **Blog posts**: 2/week
- **Pillar pages**: 1 every 2 weeks (they're big)
- **Founder-log**: 1/week (yours)
- **Newsletter**: weekly digest of new content + product updates

## SEO tech stack (free)

- Google Search Console (GSC) — primary truth source
- Bing Webmaster Tools
- Google Analytics 4 or PostHog (you'll use PostHog per ops stream)
- Schema Markup Validator
- Mobile-Friendly Test
- PageSpeed Insights / Lighthouse

Skip: Ahrefs / SEMrush / Moz unless you add later. ChatGPT can answer most "is this keyword worth targeting" questions adequately.

## Never publish without

- Proofreading pass (ChatGPT: "proofread for typos, passive voice overuse, and factual contradictions")
- Fact-check pass (ChatGPT with P-11 prompt from Copilot playbook)
- Internal linking (3+ related pieces)
- OG image (Figma or automated generation)
- Schema.org JSON-LD
- Canonical URL tag

## Crisis content

If a negative review or public criticism surfaces:
- Don't react publicly in the first 24 hours
- Respond as yourself (not the brand) on the platform where it surfaced
- Acknowledge the point, don't defend
- If legitimate criticism, add a follow-up blog post addressing it directly

Founders who engage critics honestly tend to gain more trust than founders who ignore or deflect.
