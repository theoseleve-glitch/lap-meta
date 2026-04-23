# ChatGPT Stream — Prose, Research, Editorial

**Resource:** ChatGPT (unlimited basic LLM per your plan).
**Your time:** 15-20h/week. Mostly sessions of 45-90 min.
**Format:** `- [ ] C###` — tick when done; ChatGPT session outputs go to file paths specified.
**Target:** ~300 meaningful completions over 30 days. Mostly articles + polished content.

Output destinations:
- Coaching library articles → `lap-website/src/content/coaching/[rule-id].mdx`
- Blog posts → `lap-website/src/content/blog/[slug].mdx`
- Pillar pages → `lap-website/src/content/pillars/[slug].mdx`
- Docs → `lap-website/src/content/docs/[section]/[slug].mdx`
- Emails → `lap-website/src/content/emails/[campaign]/[name].mjml`
- Research notes → `docs/research/[YYYY-MM-DD]-[topic].md`

---

## Block A — Coaching Library Flagship Articles (C001-C030)

30 × 2000-word articles covering the most important driver-technique archetypes. Each is a standalone SEO asset + product moat. Target 8-10/week for weeks 1-3.

Structure template (save to `docs/research/coaching-flagship-template.md` first):
- Hook (1 paragraph)
- What the weakness is (250w)
- Why it happens — physics + psychology (400w)
- Detection signals in telemetry (300w)
- How to fix: drill progression beginner → advanced (500w)
- Sim-to-real transfer notes (300w)
- Related weaknesses + progression (200w)
- Reference to related library rules

- [ ] C001 Flagship: "Late Braking and the Apex Speed You're Leaving Behind"
- [ ] C002 Flagship: "Trail Braking: Why Release Curve Matters More Than Pressure"
- [ ] C003 Flagship: "Early Throttle vs Clean Throttle: The Exit Commitment Problem"
- [ ] C004 Flagship: "Minimum Corner Speed — The Hidden Tax of Overslowing"
- [ ] C005 Flagship: "The V Shape vs The U Shape: Braking and Throttle Integration"
- [ ] C006 Flagship: "Steering Smoothness: Why Saw-Tooth Patterns Cost You 0.3s/Lap"
- [ ] C007 Flagship: "Lap-Time Consistency: Why Your Average Matters More Than Your Best"
- [ ] C008 Flagship: "Tire Temperature: The First-3-Lap Problem"
- [ ] C009 Flagship: "Tire Wear Management in 20-Minute Races"
- [ ] C010 Flagship: "Reading Understeer vs Oversteer in Your Inputs"
- [ ] C011 Flagship: "Fuel Management: Lift-and-Coast Done Right"
- [ ] C012 Flagship: "The Sim-to-Real Gap: What Transfers and What Doesn't"
- [ ] C013 Flagship: "Racecraft: The Overtake You Should Have Abandoned"
- [ ] C014 Flagship: "Defensive Line: When It Costs You More Than It Saves"
- [ ] C015 Flagship: "Cold Laps: The Six Ways Your Times Lie About You"
- [ ] C016 Flagship: "Grip Transitions: Adapting When the Track Changes Under You"
- [ ] C017 Flagship: "Race-Pace Decay: Why Hour 2 Is Slower Than Hour 1"
- [ ] C018 Flagship: "Setup Sensitivity: When the Problem Isn't Your Driving"
- [ ] C019 Flagship: "Pressure and Error Rate: Racing Under Stress"
- [ ] C020 Flagship: "Wet Line: Physics + Confidence Calibration"
- [ ] C021 Flagship: "Qualifying vs Race Pace: Why Your Delta Is a Diagnostic"
- [ ] C022 Flagship: "Brake Balance: When Entry Feels Wrong and Why"
- [ ] C023 Flagship: "Throttle Modulation: The Staircase That Kills Momentum"
- [ ] C024 Flagship: "Apex Clipping: Kerb Usage as a Skill"
- [ ] C025 Flagship: "Traffic Management: Losing 0.8s/Lap to Blue Flags"
- [ ] C026 Flagship: "Restart Acceleration: The 20-Second Advantage Nobody Practices"
- [ ] C027 Flagship: "Pit Entry / Pit Exit: Where Races Are Actually Lost"
- [ ] C028 Flagship: "Endurance-Stint Discipline: The Tire Reserve Problem"
- [ ] C029 Flagship: "Night Driving: Why Your Pace Drops and What to Do"
- [ ] C030 Flagship: "Setup Change Regression: When Faster Is Slower"

## Block B — Coaching Library Standard Articles (C031-C180)

150 × 1200-word articles, one per coaching rule in the backend library. Generated in batches of 10/week (~20 sessions × 90min).

Template structure:
- Hook (150w)
- Technical definition (200w)
- Telemetry signature (200w)
- Drill/fix (350w)
- Common mistakes (200w)
- Related rules (100w)

**Batch 1 — Braking (C031-C050) — 20 articles covering braking-category rules from `coaching/library/rules/braking/*.yaml`:**

- [ ] C031 "Threshold Braking: Finding the Edge"
- [ ] C032 "Brake Release Modulation"
- [ ] C033 "ABS vs Non-ABS Technique"
- [ ] C034 "Brake Point Consistency"
- [ ] C035 "Deep Braking Under Load Transfer"
- [ ] C036 "Brake Lockup Recovery"
- [ ] C037 "Trail Brake Into Fast Corners"
- [ ] C038 "Trail Brake Into Slow Corners"
- [ ] C039 "Shallow Brake on Compression"
- [ ] C040 "Downshift Brake Integration"
- [ ] C041 "Heel-Toe Technique (Real-Life)"
- [ ] C042 "Sequential vs H-Pattern Braking Rhythm"
- [ ] C043 "Brake Pressure Ramp-Up Speed"
- [ ] C044 "Engine Braking Use in GT Cars"
- [ ] C045 "Brake Bias Shift Mid-Corner"
- [ ] C046 "Pedal Modulation on Wet"
- [ ] C047 "Cold Brake Warmup Laps"
- [ ] C048 "Brake Fade Management Long Stints"
- [ ] C049 "Panic Braking Muscle Memory"
- [ ] C050 "Brake Late Into Slipstream"

**Batch 2 — Throttle (C051-C070) — 20 articles:**

- [ ] C051 "Throttle Ramp-Up Linearity"
- [ ] C052 "Partial Throttle Cornering"
- [ ] C053 "Throttle Steering (Front-Wheel Drive)"
- [ ] C054 "Throttle Steering (Rear-Wheel Drive)"
- [ ] C055 "Throttle Off Compression Bump"
- [ ] C056 "Power-On Understeer Diagnosis"
- [ ] C057 "Throttle Stab Anti-Pattern"
- [ ] C058 "Mid-Corner Throttle Lift"
- [ ] C059 "Exit Commitment Progressive"
- [ ] C060 "Throttle Application at Track-Out"
- [ ] C061 "Traction Control Reliance"
- [ ] C062 "Throttle Bypass on Short Shift"
- [ ] C063 "Torque Management LMP vs GT"
- [ ] C064 "Throttle Roll-On Wet Conditions"
- [ ] C065 "Launch Throttle Modulation"
- [ ] C066 "Downhill Throttle Control"
- [ ] C067 "Uphill Throttle Rhythm"
- [ ] C068 "Full-Throttle Awareness (Fuel Save Mode)"
- [ ] C069 "Throttle Stab on Kerb Release"
- [ ] C070 "Neutral Throttle Through Chicanes"

**Batch 3 — Line & Minimum Speed (C071-C090) — 20 articles:**

- [ ] C071 "Late Apex vs Early Apex Decisions"
- [ ] C072 "Geometric vs Racing Line"
- [ ] C073 "Double Apex Management"
- [ ] C074 "Line Compromise for Exit Speed"
- [ ] C075 "Overslowing Entry Waste"
- [ ] C076 "Track-Out Width Utilization"
- [ ] C077 "Understeer Through Line Widening"
- [ ] C078 "Line Variance Per Lap"
- [ ] C079 "Banked Corner Entry"
- [ ] C080 "Off-Camber Line Choice"
- [ ] C081 "Long Right-Hander Rhythm"
- [ ] C082 "Chicane Sequence Line"
- [ ] C083 "Slow Chicane vs Fast Chicane"
- [ ] C084 "Heavy Braking Zone Approach"
- [ ] C085 "Full-Speed Kink Technique"
- [ ] C086 "Corner Entry Speed Deficit"
- [ ] C087 "Minimum-Speed Percentile Analysis"
- [ ] C088 "Apex Miss Pattern (Early)"
- [ ] C089 "Apex Miss Pattern (Late)"
- [ ] C090 "Line Adjustment for Degraded Tires"

**Batch 4 — Consistency & Racecraft (C091-C115) — 25 articles:**

- [ ] C091 "Lap-Time Variance Diagnosis"
- [ ] C092 "Sector Time Analysis"
- [ ] C093 "Mistake Recovery Speed"
- [ ] C094 "Attention Fatigue Over Run"
- [ ] C095 "Focus Maintenance 60+ Minutes"
- [ ] C096 "Visual Scan Pattern"
- [ ] C097 "Mirror Usage Pattern"
- [ ] C098 "Overtake Setup Corner Selection"
- [ ] C099 "Dive-Bomb Anti-Pattern"
- [ ] C100 "Late-Braking Overtake Assessment"
- [ ] C101 "Side-by-Side Corner Discipline"
- [ ] C102 "Defensive Blocking vs Chopping"
- [ ] C103 "Slipstream Usage on Straights"
- [ ] C104 "Draft Exit Timing"
- [ ] C105 "Closing Gaps Without Running Wide"
- [ ] C106 "Pit Exit Merge Safety"
- [ ] C107 "Safety Car Pace Prep"
- [ ] C108 "FCY/VSC Discipline"
- [ ] C109 "Race Start Launch"
- [ ] C110 "Restart Craft Lap 1"
- [ ] C111 "Blue Flag Response"
- [ ] C112 "Lapping Traffic Clean"
- [ ] C113 "Being Lapped Clean"
- [ ] C114 "First-Lap Position Strategy"
- [ ] C115 "Last-Lap Risk Management"

**Batch 5 — Tire + Fuel (C116-C135) — 20 articles:**

- [ ] C116 "Tire Temperature Window"
- [ ] C117 "Pressure Drop Over Stint"
- [ ] C118 "Compound Selection Logic"
- [ ] C119 "Flat-Spot Recovery"
- [ ] C120 "Tire Sidewall Abuse Signal"
- [ ] C121 "Graining Recognition"
- [ ] C122 "Blistering Recognition"
- [ ] C123 "Overheating Prevention"
- [ ] C124 "Fuel Burn Rate Targets"
- [ ] C125 "Lift-and-Coast Geometry"
- [ ] C126 "Short-Shift for Fuel"
- [ ] C127 "Save Mode Pace Target"
- [ ] C128 "Push Mode Usage"
- [ ] C129 "Fuel Window Optimization"
- [ ] C130 "Splash-and-Dash Strategy"
- [ ] C131 "Undercut Pit Strategy"
- [ ] C132 "Overcut Pit Strategy"
- [ ] C133 "Stint Length Optimization"
- [ ] C134 "Tire Offset Per Corner"
- [ ] C135 "Tire Warmup Lap Technique"

**Batch 6 — Adaptation + Miscellaneous (C136-C180) — 45 articles covering remaining rule categories:**

- [ ] C136 "Grip Level Awareness"
- [ ] C137 "Track-State Adaptation (Green → Rubbered)"
- [ ] C138 "Setup Feedback Loop"
- [ ] C139 "Ride Height Effect on Entry"
- [ ] C140 "Damper Settings Diagnosis"
- [ ] C141 "Anti-Roll Bar Felt Effect"
- [ ] C142 "Aero Balance Cornering"
- [ ] C143 "Differential Settings (Race)"
- [ ] C144 "Differential Settings (Qualifying)"
- [ ] C145 "Brake Bias Per Corner Type"
- [ ] C146 "Traction Control Setting Choice"
- [ ] C147 "ABS Intensity Tuning"
- [ ] C148 "Wet-to-Dry Transition"
- [ ] C149 "Dry-to-Wet Transition"
- [ ] C150 "Rain Intensity Recognition"
- [ ] C151 "Evening Session Vision"
- [ ] C152 "Low-Light Track-Marker Recognition"
- [ ] C153 "Temperature Drop Effect Stint 3+"
- [ ] C154 "Hot-Weather Pace Preservation"
- [ ] C155 "Wind-Affected Corner Lines"
- [ ] C156 "Altitude Effect on Power"
- [ ] C157 "New Track Learning Curve"
- [ ] C158 "New Car Learning Curve"
- [ ] C159 "Car Class Transition Skills"
- [ ] C160 "Transitioning Sim Platforms"
- [ ] C161 "Physical Simulator Hardware Calibration"
- [ ] C162 "Pedal Force Consistency"
- [ ] C163 "Wheel FFB Tuning Learn"
- [ ] C164 "Seat Position and Feel"
- [ ] C165 "Driving Posture Endurance"
- [ ] C166 "Hydration and Pace"
- [ ] C167 "Pre-Race Mental Routine"
- [ ] C168 "Post-Mistake Reset Protocol"
- [ ] C169 "Fear and Corner Commitment"
- [ ] C170 "Confidence Calibration After Spin"
- [ ] C171 "Real-World Safety Margin"
- [ ] C172 "Karting Crossover Skills"
- [ ] C173 "Track Day Preparation Plan"
- [ ] C174 "Data-Study Habit: Self-Review"
- [ ] C175 "Video-Study Habit"
- [ ] C176 "Peer-Benchmark Reading"
- [ ] C177 "Coach-vs-Data Reconciliation"
- [ ] C178 "Improvement Plateau Diagnosis"
- [ ] C179 "Over-Training Recognition"
- [ ] C180 "Regression After Break"

## Block C — SEO Pillar Pages Polish (C181-C200)

The marketing /loop drafts pillar pages. Your job with ChatGPT is to EDIT each to editorial quality. 4 pillars × 5 tasks each.

**Pillar 1 — Sim-to-Real Transfer:**
- [ ] C181 Edit pass 1: tighten prose, remove SEO padding
- [ ] C182 Fact-check every physics claim; add citations
- [ ] C183 Add 3 concrete examples from archived session data
- [ ] C184 Internal linking pass: link to 8 related coaching articles
- [ ] C185 Final read + schema.org structured data

**Pillar 2 — Trail Braking:**
- [ ] C186 Edit pass 1
- [ ] C187 Fact-check + citations
- [ ] C188 Concrete examples
- [ ] C189 Internal linking
- [ ] C190 Final polish

**Pillar 3 — Telemetry Apps Compared:**
- [ ] C191 Edit pass 1 — tone/fairness toward competitors
- [ ] C192 Update pricing comparison table (verify numbers)
- [ ] C193 Add "honest LAP limitations" section
- [ ] C194 Internal linking
- [ ] C195 Final polish + pricing sensitivity disclosure

**Pillar 4 — Driver Development Plan:**
- [ ] C196 Edit pass 1
- [ ] C197 Framework diagram description (for Figma)
- [ ] C198 Case study sketches (real-looking fictional)
- [ ] C199 Internal linking
- [ ] C200 Final polish

## Block D — Marketing Loop Output Polish (C201-C240)

ChatGPT edits every blog post / content piece the marketing /loop ships. 40 items, 1 per loop output.

- [ ] C201 Blog post polish: TBD (whatever lap-website /loop ships next)
- [ ] C202-C240: same pattern, queued as they arrive

## Block E — Email Sequences (C241-C260)

MJML / markdown drafts for transactional and lifecycle emails.

**Welcome/onboarding drip:**
- [ ] C241 Email 1: "You're in" (immediate, post-waitlist signup)
- [ ] C242 Email 2: "What LAP actually is" (Day 2)
- [ ] C243 Email 3: "Your first session: 3 ways to import" (Day 4)
- [ ] C244 Email 4: "How to read your first weakness report" (Day 7)
- [ ] C245 Email 5: "Accept your first prescription" (Day 9)
- [ ] C246 Email 6: "The 30-day improvement arc" (Day 14)
- [ ] C247 Email 7: "What's after your trial" (Day 12 of trial = Day 12 post-signup)

**Trial-to-paid:**
- [ ] C248 Trial Day 10: "3 days left" urgency email
- [ ] C249 Trial Day 13: "last day" + upgrade link
- [ ] C250 Trial expired: "come back any time" (no guilt)

**Re-engagement (paid user inactive 14d):**
- [ ] C251 "Missing you" + top weakness summary email
- [ ] C252 "Quick session idea" email

**Cancelled-paid recovery:**
- [ ] C253 "What went wrong" short feedback ask
- [ ] C254 "Come back with a discount" 30-day-out

**Ambassador/referral:**
- [ ] C255 "Invite a racer friend" post 30-day paid milestone

**Beta invite:**
- [ ] C256 Beta invite email with founder pricing code
- [ ] C257 Beta reminder email (unread after 5d)

**V1 launch announcement:**
- [ ] C258 Launch email to waitlist
- [ ] C259 Launch email to free trial users
- [ ] C260 Launch email to post-trial lapsed

## Block F — Docs Site Content (C261-C280)

- [ ] C261 "Getting Started: Desktop capture" help article
- [ ] C262 "Getting Started: Mobile capture" help article
- [ ] C263 "Getting Started: iRacing integration" walkthrough
- [ ] C264 "Getting Started: ACC integration" walkthrough
- [ ] C265 "Getting Started: AC Competizione integration"
- [ ] C266 "Getting Started: RaceBox pairing"
- [ ] C267 "Reading Your Driver Profile" help
- [ ] C268 "Understanding Weakness Episodes" help
- [ ] C269 "Accepting and Following Prescriptions" help
- [ ] C270 "Sim-to-Real Bridge: How It Works" help
- [ ] C271 "Data Quality: What Affects Your Session Score" help
- [ ] C272 "Troubleshooting: Session won't upload"
- [ ] C273 "Troubleshooting: RaceBox not connecting"
- [ ] C274 "Troubleshooting: Overlays not showing in iRacing"
- [ ] C275 "Troubleshooting: Android battery drain"
- [ ] C276 "FAQ: Cancel anytime"
- [ ] C277 "FAQ: Data ownership + GDPR export"
- [ ] C278 "FAQ: Refund policy"
- [ ] C279 "FAQ: Supported sims"
- [ ] C280 "FAQ: Hardware requirements"

## Block G — Research Dossier (C281-C300)

Weekly research memos to `docs/research/`. 4 weeks × ~5 memos each.

**Week 1:**
- [ ] C281 Competitor deep-dive: Garage61 current feature set, pricing, gaps
- [ ] C282 Competitor: RaceLab
- [ ] C283 Competitor: Racing Republic
- [ ] C284 Keyword research: top 50 priority keywords for LAP
- [ ] C285 Racing theory extraction from owned books: first 40 insights

**Week 2:**
- [ ] C286 Competitor: MoTeC + pro tools
- [ ] C287 Competitor: Track Attack / Skip Barber digital tools
- [ ] C288 Keyword research: long-tail opportunities for coaching library
- [ ] C289 Racing theory extraction: next 40 insights
- [ ] C290 SERP analysis: what content ranks #1-3 for target queries?

**Week 3:**
- [ ] C291 Market sizing: sim-racing subscription tools TAM
- [ ] C292 Keyword research: brand + navigational queries
- [ ] C293 Racing theory extraction: next 40 insights
- [ ] C294 Sim racer community analysis (Discord servers, YouTubers, streamers)
- [ ] C295 Pricing model analysis (competitors + adjacent industries)

**Week 4:**
- [ ] C296 Launch-readiness checklist against research
- [ ] C297 Post-launch competitive response prediction
- [ ] C298 Racing theory extraction: final 50 insights (total: 170 insights feeding coaching library)
- [ ] C299 Year-2 roadmap research (B2B racing academies, esports teams)
- [ ] C300 Consolidated research dossier 1.0 → commit to lap-meta

---

## Recommended daily rhythm (ChatGPT side)

- 09:00-10:30 — 1 coaching article (flagship or 2 standards)
- 15:00-15:30 — research memo continuation (15 min focused) OR email draft
- 17:00-18:00 — editorial polish pass on marketing /loop output from the day

Target: 180 articles + pillars + emails + docs + research = ~300 items over 30 days. At 10 items/day, doable with unlimited ChatGPT.
