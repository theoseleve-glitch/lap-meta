# Legal Playbook — DIY Drafts

Per your G3=a: DIY with ChatGPT drafts, accept the risk.

This file contains structural drafts of the legal artifacts LAP needs before public beta. **These are starting points, not lawyer-reviewed documents.** Use ChatGPT to refine, localize (French + English versions), and regenerate when product scope changes. Commit polished versions to `lap-website/src/content/legal/` and publish at:
- `lap-coach.racing/legal/terms`
- `lap-coach.racing/legal/privacy`
- `lap-coach.racing/legal/cookies`
- `lap-coach.racing/legal/refund-policy`
- `lap-coach.racing/legal/dpa` (for B2B — post-beta)

Jurisdiction: **France (micro-entreprise, GDPR)** per your B2 answer.

---

## L-01 — Terms of Service (skeleton)

Generate via: ChatGPT prompt "draft a Terms of Service for a French micro-entreprise SaaS named LAP Coach at lap-coach.racing providing telemetry coaching software, with the following specific terms: [list below]. Target French + English versions, GDPR aware, B2C-first with B2B openable."

**Required specific clauses:**

1. **Service definition** — "LAP Coach provides software tools for capturing, analyzing, and coaching on motorsport telemetry data from simulated and real-world driving sessions. LAP Coach does not provide real-time safety-critical advice for actual vehicle operation."
2. **Safety disclaimer** — "Users acknowledge that on-track and on-road driving is inherently dangerous. LAP Coach outputs are informational only. Users remain solely responsible for their driving decisions. LAP Coach is not liable for any damage, injury, or loss arising from use of its outputs."
3. **Free trial** — "LAP Coach offers a 14-day free trial. Trial users may access all Service features without entering payment information until the trial ends. At trial expiration, the account enters a read-only state pending subscription."
4. **Pricing + auto-renewal** — "Subscriptions renew automatically at the end of each billing cycle unless cancelled in-account. Cancellation takes effect at the end of the current billing period. No refunds for partial periods except as required by applicable consumer-protection law."
5. **French consumer-protection right** — "Consumers in France may exercise their 14-day cooling-off right for distance-selling contracts (Code de la consommation L221-18), provided the Service has not been 'substantially performed' within this window. Users who upload their first session waive this right under L221-28 for the digital-content portion of the Service."
6. **Data ownership** — "Users retain ownership of all telemetry data they upload. LAP Coach retains a limited license to process this data to provide the Service and (if opt-in) to contribute anonymized metrics to peer benchmarks."
7. **Account termination** — "Users may cancel any time. LAP Coach may terminate for violations with 30-day notice unless immediate termination is required for security or legal reasons."
8. **Prohibited uses** — "Reverse engineering, automated scraping of competitor data, harassment, impersonation of another driver, use of LAP Coach outputs to make safety-critical decisions on public roads without professional validation."
9. **Intellectual property** — "The LAP Coach brand, coaching library content, software, and marketing materials are property of Theo Seleve (sole trader / micro-entrepreneur) until an incorporated entity acquires them. User-contributed setups / notes / tags remain user property."
10. **Limitation of liability** — "LAP Coach's aggregate liability is limited to the total subscription fees paid by the user in the 12 months preceding the claim. This does not apply to damages that cannot be limited under French or EU law (personal injury caused by our gross negligence, etc.)."
11. **Warranty disclaimer** — "Service provided 'as is' with no implied warranty of merchantability or fitness for a particular purpose, except as required by mandatory consumer-protection law."
12. **Governing law** — "French law. Disputes in French courts with jurisdiction at defendant's domicile. Consumer users retain rights to bring disputes in their country of residence."
13. **Changes to terms** — "Material changes with 30-day email notice. Continued use after effective date = acceptance."
14. **Contact** — `hello@lap-coach.racing` or postal address (your SIRET-registered address).

---

## L-02 — Privacy Policy (skeleton)

ChatGPT prompt: "Draft a GDPR-compliant Privacy Policy for LAP Coach French micro-entreprise. Include the following specifics: [list below]. Target French + English versions."

**Required specifics:**

1. **Data controller** — Theo Seleve (micro-entrepreneur, SIRET pending as of 2026-04-23), `theo@lap-coach.racing`. Will transition to incorporated entity if/when formed.
2. **Data collected:**
   - Account: email, display name, clerk_user_id, subscription status
   - Session telemetry: GPS, IMU, vehicle inputs, sim/real metadata, timestamps
   - Usage analytics: pages viewed, features used, session durations (cookieless first-party)
   - Device info: app version, OS version, device model, browser
   - Support correspondence
3. **Legal bases (GDPR Art. 6):**
   - Contract (Art. 6(1)(b)) — processing necessary to provide the subscribed Service
   - Consent (Art. 6(1)(a)) — for optional features like cohort benchmarking, newsletter subscription, analytics cookies
   - Legitimate interests (Art. 6(1)(f)) — for security, fraud prevention, service improvement
4. **Data sharing (sub-processors):**
   - Clerk (US, SCCs) — auth
   - Stripe (US, SCCs) — payments
   - Neon (AWS EU) — database
   - Cloudflare R2 (EU, as configured) — object storage
   - Resend (US, SCCs) — transactional email
   - Sentry (US, SCCs) — error tracking (opt-out in settings)
   - PostHog EU — product analytics (EU region selected in ops)
5. **International transfers** — adequate safeguards (SCCs for US transfers)
6. **Retention** — "Account data retained while account active + 30 days after deletion request. Session telemetry retained 2 years post-deletion unless opted-out (for cohort benchmarks, anonymized). Payment records retained 10 years (French tax law)."
7. **User rights (GDPR)** — access, rectification, deletion ("right to be forgotten"), portability, restriction, objection, withdraw consent. Request via `privacy@lap-coach.racing` — respond within 30 days.
8. **Cohort opt-in** — "Peer benchmarks (Driver Cohort feature) require opt-in. Data anonymized before cohort computation. No cross-user identification possible."
9. **Cookie notice** — "Essential cookies only (session, CSRF, trial banner state) load without consent. Analytics cookies load only after user consent via cookie banner."
10. **Children** — "Service not directed at users under 16. We do not knowingly collect data from minors."
11. **Automated decisions** — "Coaching prescriptions are algorithmic but not 'automated decisions with legal or significant effect' under GDPR Art. 22. Users can always decline any prescription."
12. **Data breach notice** — "In event of breach, notify CNIL within 72h per GDPR Art. 33 and affected users within 72h per Art. 34."
13. **DPO** — "No formal DPO required at our scale. Founder is data protection lead."
14. **Complaints** — "Right to lodge complaint with CNIL (French data protection authority) at cnil.fr."

---

## L-03 — Cookie Policy

ChatGPT prompt: "Draft a cookie policy for lap-coach.racing listing the following cookies + categories: [list below]. Consent model: opt-in for non-essential, pre-set for essential."

**Cookie inventory:**

| Cookie | Category | Purpose | Duration |
|---|---|---|---|
| `__Host-clerk-session` | Essential | Auth session | 7 days |
| `csrf-token` | Essential | CSRF protection | Session |
| `cookie-consent` | Essential | Remembers consent choice | 12 months |
| `_posthog` | Analytics | Product analytics (opt-in) | 12 months |
| Sentry session cookie | Analytics | Error tracking (opt-in) | 30 min |
| `trial-banner-dismissed` | Functional | UI state | 30 days |

No advertising cookies. No third-party tracking. Cookie banner blocks analytics until consent.

---

## L-04 — Refund Policy

Short and clear:

- **14-day trial** — no charge, no refund needed
- **Monthly plan** — "No refunds for partial months. Cancel any time, keep access until end of current billing period."
- **Yearly plan** — "Full refund within first 30 days. Pro-rata refund after 30 days if cancelling for a specific written reason (e.g., inability to use, undelivered feature)."
- **France consumer rights** — "French consumers retain all rights under Code de la consommation. Distance-selling right of withdrawal (14 days) applies unless the user has started using paid features, per L221-28."
- **How to request** — `billing@lap-coach.racing`, processed within 14 days via Stripe.

---

## L-05 — Data Processing Agreement (B2B only, deferred)

Only needed when first B2B customer closes. Template content:

- Subject matter: processing telemetry data of B2B customer's drivers
- Duration: matches subscription term
- Nature: collection, storage, analysis, coaching output generation
- Categories: drivers' personal data (name, email, driving metrics)
- Sub-processors: same list as Privacy Policy
- Security: specifics per SaaS norms (TLS in transit, encryption at rest, access logs, least-privilege)
- Breach notice: 48h
- Deletion: 30 days post-termination
- Audit right: 1× annually with 30-day notice
- Liability: subject to main agreement caps

Defer until first B2B inbound conversation (Month 5+).

---

## L-06 — Copyright notices

- Every page footer: "© 2026 Theo Seleve / LAP Coach. All rights reserved."
- Coaching library articles: `CC BY-SA 4.0` OR "all rights reserved" — pick one and stick with it. CC-BY-SA encourages shares + backlinks but means competitors could host your content. **Recommended: all rights reserved for now; revisit at scale.**
- Blog posts: all rights reserved
- Open-source code (if any): MIT or Apache 2.0 for any client SDKs released

---

## L-07 — Trademarks

- "LAP Coach" as a word mark — filed in France (INPI) is advisable but not urgent. Budget ~€250 INPI filing fee + ~€400 if you use a trademark attorney. Defer to Month 5+ when product has revenue justifying.
- "LAP" alone is likely too generic to register (laps in racing, lap dances, etc.). Stick with "LAP Coach" for trademark protection.

---

## L-08 — Insurance

- **Professional liability insurance** — French professional liability (responsabilité civile professionnelle) is NOT mandatory for micro-entrepreneur software services, but recommended once you have paying users. Quote: ~€200-500/year via companies like Hiscox, Allianz Pro. Defer until revenue justifies.
- **Cyber liability** — covers data breach response costs. Consider at 500+ paying users. ~€400-1000/year.

---

## L-09 — What's NOT in this playbook

- Full pro-grade ToS with indemnification clauses → lawyer review €500-1500 when you have customer demanding it
- B2B master services agreement templates → lawyer review when first B2B prospect materializes
- European Accessibility Act compliance (coming June 2025, applies to digital services) → review when scale warrants
- CCPA (California) compliance → only if US customers grow to meaningful % of user base
- Privacy Shield replacement / SCCs updates → monitor CNIL guidance

---

## Implementation tasks

- [ ] L-T001 Generate ToS v1 via ChatGPT with prompt above
- [ ] L-T002 Review personally, adjust to accurately reflect what Service actually does
- [ ] L-T003 Publish to `lap-website/src/content/legal/terms.mdx` + route `/legal/terms`
- [ ] L-T004 Same for Privacy Policy (L-02)
- [ ] L-T005 Same for Cookie Policy (L-03)
- [ ] L-T006 Same for Refund Policy (L-04)
- [ ] L-T007 Add footer links to all legal pages
- [ ] L-T008 Add cookie banner (only appears if user hasn't consented) — lap-website sprint has this in T014 (PostHog)
- [ ] L-T009 Add GDPR export + deletion endpoints to backend (sprint covers)
- [ ] L-T010 Internal doc: data-processor contract with each sub-processor confirmed
- [ ] L-T011 Pre-launch: post all legal pages, verify linked from signup flow
- [ ] L-T012 Post-launch: budget €500-1000 for one-pass lawyer review when first paying customer triggers concern

Never publish to production without:
- L-T001-L-T007 complete
- All pages accessible from signup flow
- Links work, no 404s
- Timestamp at bottom ("Last updated: YYYY-MM-DD")

---

## Risk acceptance

Per your G3=a: DIY drafts. Accept that:
- A hostile consumer lawyer could find weaknesses in DIY ToS
- A French consumer dispute could go to DGCCRF (consumer protection) — you'd defend with good-faith compliance
- First regulatory question you receive, immediately budget €500-1000 for lawyer response

The alternative (€1500-3000 full legal package before first user) is valid but not urgent pre-revenue. This is the trade you made, documented.
