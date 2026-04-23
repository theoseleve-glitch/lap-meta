# LAP Webapp — Sprint 2 Queue

**Starts when:** Sprint 1 `sprint-webapp.md` drains.
**Covers:** M4 bridge UI + cohort + target event picker + M5 endurance UX + V1 polish + M6 B2B + perf + a11y + final bash.
**Total:** 150 tasks.

---

## Block A — Bridge UI (T001–T020)

- [ ] T001 [design] Figma: bridge tab on session detail + full TransferReport page ⇒ approved
- [ ] T002 [opus] Bridge tab added to `SessionDetailShell` tabs ⇒ routes via `?tab=bridge`
- [ ] T003 [opus] `BridgeSuggestCard` component: renders auto-suggested pair ⇒ Storybook
- [ ] T004 [opus] `ManualLinkButton` with session-picker modal ⇒ works
- [ ] T005 [opus] Session picker filters to compatible sessions (same master_track, comparable car class) ⇒ tested
- [ ] T006 [opus] Create-link mutation: POST /bridge/links with optimistic UI ⇒ tested
- [ ] T007 [opus] Bridge tab empty state: "No linked sessions yet" with CTA ⇒ rendered
- [ ] T008 [opus] Route `/app/bridge/reports/:linkId` TransferReport page shell ⇒ renders
- [ ] T009 [opus] `SessionHeaderPair` component: both sessions side-by-side (sim + real) ⇒ Storybook
- [ ] T010 [opus] `ShapeMatchScoreBadge` component: 0-1 score with color + tooltip ⇒ Storybook
- [ ] T011 [opus] `IntensityMatchScoreBadge` component ⇒ Storybook
- [ ] T012 [opus] `DivergencePointsList` component: corner-by-corner breakdown ⇒ Storybook
- [ ] T013 [opus] `DivergencePoint` mini-trace component: shows sim vs real per channel ⇒ tested
- [ ] T014 [opus] `TransferredSkillsList` / `NonTransferredSkillsList` components ⇒ Storybook
- [ ] T015 [sonnet] Rate useful/not-useful thumbs: POST /bridge/links/:id/rate ⇒ persists
- [ ] T016 [sonnet] Bridge summary card on Driver Profile: "3 active links" ⇒ rendered
- [ ] T017 [sonnet] Driver-level bridge timeline: `/app/bridge` lists all links ⇒ tested
- [ ] T018 [sonnet] Bridge filter: by track, by car, by date range ⇒ works
- [ ] T019 [sonnet] Delete link button with confirm ⇒ works
- [ ] T020 [sonnet] E2E: create link → view report → rate useful ⇒ green

## Block B — Cohort benchmarks UI (T021–T035)

- [ ] T021 [design] Figma: cohort percentile badges on Driver Profile + unlock states ⇒ approved
- [ ] T022 [opus] `PercentileBadge` component (0-100 with color scale) ⇒ Storybook
- [ ] T023 [opus] Driver Profile dimensions get percentile badges when cohort unlocked ⇒ tested
- [ ] T024 [opus] Cohort-locked state: "Unlocks at 20 drivers for your {car, track} combo — currently at {N}" ⇒ rendered
- [ ] T025 [opus] Privacy-first copy: "You see percentile. No one sees where they rank vs you." ⇒ tested
- [ ] T026 [opus] Cohort opt-in toggle in `/app/settings/data` ⇒ persists
- [ ] T027 [opus] Opt-in warning: "Your anonymized metrics will be used to build percentile benchmarks. You can opt out anytime." ⇒ rendered
- [ ] T028 [sonnet] Opt-out: when toggled off, data deletion confirmation ⇒ tested
- [ ] T029 [sonnet] Archetype badge: "Smooth Flow" / "Late Braker" / etc. with explanation ⇒ Storybook
- [ ] T030 [sonnet] Cohort context switcher: "Show me percentile for car X at track Y" ⇒ tested
- [ ] T031 [sonnet] Benchmark trend: percentile change over last 4 weeks ⇒ chart
- [ ] T032 [sonnet] A11y: badges have text alternatives ⇒ axe clean
- [ ] T033 [sonnet] Empty state (no data): "Upload sessions to unlock your benchmark" ⇒ rendered
- [ ] T034 [sonnet] Tests for each percentile state (locked, locked-close, unlocked) ⇒ green
- [ ] T035 [sonnet] E2E: opt in → see cohort message → opt out → badges hidden ⇒ green

## Block C — Target event picker (T036–T050)

- [ ] T036 [design] Figma: event browser + countdown card + readiness-for-event view ⇒ approved
- [ ] T037 [opus] `/app/events` route: list upcoming iRacing events + user's pinned events ⇒ renders
- [ ] T038 [opus] Event card: track, car, date, time-to-go, priority ⇒ Storybook
- [ ] T039 [opus] Pin/unpin event: POST/DELETE /driver/target-events ⇒ optimistic UI
- [ ] T040 [opus] Event filters: source (iRacing, real-life), series, class, date range ⇒ works
- [ ] T041 [opus] Event detail page: track info, suggested prep sessions, readiness snapshot ⇒ renders
- [ ] T042 [opus] Add-real-event form: user creates a track day entry ⇒ tested
- [ ] T043 [sonnet] `ReadinessForEventCard` on Driver Profile: shows score + top missing readiness factor ⇒ Storybook
- [ ] T044 [sonnet] Event countdown banner across app shell when event <7d away ⇒ visible
- [ ] T045 [sonnet] Event post-mortem: after event, prompt user for "how did it go?" ⇒ form
- [ ] T046 [sonnet] Post-event data populates RecentEvents list ⇒ history
- [ ] T047 [sonnet] Target-event-aware Timeline filter: "Show only sessions prepping for event X" ⇒ works
- [ ] T048 [sonnet] Email notifications: opt-in "Remind me 24h + 1h before event" ⇒ preference
- [ ] T049 [sonnet] A11y on event pages ⇒ axe clean
- [ ] T050 [sonnet] E2E: pin event → see countdown → readiness updates → post-mortem ⇒ green

## Block D — Endurance UX (T051–T065)

- [ ] T051 [design] Figma: endurance session detail with stint breakdown ⇒ approved
- [ ] T052 [opus] `EnduranceStintList` component: per-stint summary ⇒ Storybook
- [ ] T053 [opus] `LongRunPaceChart`: lap time over stint duration ⇒ Canvas or Recharts
- [ ] T054 [opus] `TirePreservationScore` gauge ⇒ Storybook
- [ ] T055 [opus] `PaceDecayScore` chart: slope highlighted ⇒ rendered
- [ ] T056 [opus] Endurance session detail page auto-detects endurance and adds stint tab ⇒ tested
- [ ] T057 [opus] Strategy-plan-vs-actual timeline component ⇒ Storybook
- [ ] T058 [opus] Stint comparison: lap-time trajectories side-by-side ⇒ tested
- [ ] T059 [sonnet] Endurance-specific coaching insights displayed ⇒ tested
- [ ] T060 [sonnet] Endurance event aggregate page: show all sessions within an event ⇒ renders
- [ ] T061 [sonnet] Endurance leaderboard (cohort, if unlocked): pace-decay percentile ⇒ tested
- [ ] T062 [sonnet] Driver handoff metadata display (read-only; multi-driver full UX deferred) ⇒ shown
- [ ] T063 [sonnet] Export endurance report as PDF ⇒ works
- [ ] T064 [sonnet] A11y + responsive ⇒ clean
- [ ] T065 [sonnet] E2E: upload endurance session → see stint breakdown → export PDF ⇒ green

## Block E — V1 release polish (T066–T080)

- [ ] T066 [sonnet] Release notes page `/app/whats-new` ⇒ MDX source
- [ ] T067 [opus] Copy pass on all `/app/*` pages: align tone with "Driver OS" positioning ⇒ reviewed
- [ ] T068 [sonnet] In-app changelog widget with badge on new features ⇒ works
- [ ] T069 [sonnet] First-session celebration modal ⇒ fires once, respects skip
- [ ] T070 [sonnet] First-prescription celebration ⇒ fires
- [ ] T071 [sonnet] First-week review email trigger ⇒ backend event fires
- [ ] T072 [sonnet] Empty states across all pages polished ⇒ consistent
- [ ] T073 [sonnet] Loading skeletons match final content shape ⇒ consistent
- [ ] T074 [sonnet] Error boundaries at route level with report button ⇒ works
- [ ] T075 [sonnet] Toast system unified ⇒ consistent
- [ ] T076 [sonnet] Keyboard shortcuts help modal (press `?`) ⇒ works
- [ ] T077 [sonnet] Command palette (Cmd/Ctrl+K) with route search ⇒ works
- [ ] T078 [sonnet] Theme switcher (light/dark/auto) ⇒ persists
- [ ] T079 [sonnet] Avatars + identicons for drivers ⇒ renders
- [ ] T080 [sonnet] V1 launch screenshot set for App Store / Play Store / marketing ⇒ captured

## Block F — B2B webapp (T081–T100)

- [ ] T081 [design] Figma: org admin dashboard + coach driver-list view ⇒ approved
- [ ] T082 [opus] `/app/orgs` list route ⇒ renders for org admins
- [ ] T083 [opus] Create org wizard ⇒ tested
- [ ] T084 [opus] Invite member form ⇒ tested
- [ ] T085 [opus] Member management table: role, status, last active, remove ⇒ tested
- [ ] T086 [opus] `/app/orgs/:id/coaches` coach dashboard: all driver progress at a glance ⇒ renders
- [ ] T087 [opus] Coach driver-detail view: same as driver's self-view but with coach notes + assign-prescription action ⇒ tested
- [ ] T088 [opus] Coach-assigned prescription mutation ⇒ tested
- [ ] T089 [opus] Coach note on session ⇒ tested
- [ ] T090 [sonnet] Org-level KPI dashboard ⇒ aggregate numbers
- [ ] T091 [sonnet] Org billing page: plan, seats, invoice history ⇒ Stripe portal integration
- [ ] T092 [sonnet] Seat-upgrade flow ⇒ Stripe checkout
- [ ] T093 [sonnet] Org settings page ⇒ brand logo upload
- [ ] T094 [sonnet] Role switcher for users who are admin in one org + driver in another ⇒ works
- [ ] T095 [sonnet] Audit log page for org admins ⇒ shows actions
- [ ] T096 [sonnet] Org-scoped URLs: `/app/orgs/:slug/*` when in org context ⇒ routing
- [ ] T097 [sonnet] Notifications for coaches: "new session from your driver X" ⇒ in-app
- [ ] T098 [sonnet] Coach-to-driver messaging (lightweight, not chat) ⇒ one-way notes
- [ ] T099 [sonnet] E2E: create org → invite coach → coach assigns prescription → driver sees ⇒ green
- [ ] T100 [sonnet] A11y: all B2B screens axe-clean ⇒ tested

## Block G — Performance + a11y + perf (T101–T120)

- [ ] T101 [sonnet] Lighthouse CI thresholds: LCP <2.0s, INP <100ms, CLS <0.1 on top-10 pages ⇒ all pass
- [ ] T102 [sonnet] Code-splitting audit: no initial chunk >100KB gzip ⇒ verified
- [ ] T103 [sonnet] Image strategy: all images use next/image with proper sizes ⇒ audited
- [ ] T104 [sonnet] Font loading strategy: preload + swap ⇒ FOUT minimized
- [ ] T105 [sonnet] Third-party script audit: defer/async where possible, remove unused ⇒ done
- [ ] T106 [sonnet] Tailwind JIT: verify no unused utilities in build ⇒ small CSS
- [ ] T107 [sonnet] Web Vitals tracking via PostHog ⇒ p75 per-page visible in dashboard
- [ ] T108 [sonnet] Route-level prefetching on hover (smart, budgeted) ⇒ works
- [ ] T109 [sonnet] Mobile viewport audit: all pages render <3s on slow-4G ⇒ tested
- [ ] T110 [sonnet] A11y pass 1: axe across all top-level pages ⇒ violations fixed
- [ ] T111 [sonnet] A11y pass 2: keyboard-only navigation ⇒ fully usable
- [ ] T112 [sonnet] A11y pass 3: screen reader (NVDA + VoiceOver) ⇒ announces correctly
- [ ] T113 [sonnet] A11y pass 4: color contrast AA+ everywhere ⇒ verified
- [ ] T114 [sonnet] A11y pass 5: focus rings consistent ⇒ visible
- [ ] T115 [sonnet] PWA manifest + service worker (offline read-only for recent sessions) ⇒ optional feature
- [ ] T116 [sonnet] Install prompt for PWA ⇒ tested
- [ ] T117 [sonnet] Dark mode: verify all custom colors have dark variants ⇒ reviewed
- [ ] T118 [sonnet] Reduce-motion preference respected on GSAP ⇒ tested
- [ ] T119 [sonnet] i18n-ready: strings extracted to `src/i18n/en.json` ⇒ no hardcoded
- [ ] T120 [sonnet] French translation stubs ⇒ file created

## Block H — Final bash (T121–T150)

- [ ] T121 [sonnet] Triage Sentry issues: top 10 by frequency ⇒ fixed
- [ ] T122 [sonnet] Triage PostHog low-engagement pages: identify drop-offs ⇒ 3 fixes
- [ ] T123 [sonnet] CSP hardening: tighter directives ⇒ tested, nothing breaks
- [ ] T124 [sonnet] Security headers audit via securityheaders.com ⇒ A+ grade
- [ ] T125 [sonnet] Cookie audit: only essential cookies without consent ⇒ compliant
- [ ] T126 [sonnet] Privacy policy page ⇒ written
- [ ] T127 [sonnet] Terms of service page ⇒ written
- [ ] T128 [sonnet] Cookie policy page ⇒ written
- [ ] T129 [sonnet] GDPR data-export request flow (from settings) ⇒ works
- [ ] T130 [sonnet] GDPR delete-account flow with confirmation ⇒ works
- [ ] T131 [sonnet] Unsubscribe links on email templates ⇒ work
- [ ] T132 [sonnet] 404 page with search ⇒ renders
- [ ] T133 [sonnet] 500 page with recovery action ⇒ renders
- [ ] T134 [sonnet] Maintenance page template ⇒ prepared
- [ ] T135 [sonnet] Sitemap.xml auto-generated ⇒ correct
- [ ] T136 [sonnet] Robots.txt correct for app subdomain (noindex auth'd pages) ⇒ verified
- [ ] T137 [sonnet] OG images per page type ⇒ 10 unique
- [ ] T138 [sonnet] Twitter card metadata ⇒ present
- [ ] T139 [sonnet] LinkedIn card metadata ⇒ present
- [ ] T140 [sonnet] Slack unfurl tested ⇒ renders
- [ ] T141 [sonnet] Dependency audit: `pnpm audit` clean ⇒ zero highs
- [ ] T142 [sonnet] Dependency updates: all deps within 1 minor version of latest ⇒ bumped
- [ ] T143 [sonnet] Storybook coverage audit: each exported component has a story ⇒ ≥90%
- [ ] T144 [sonnet] E2E coverage audit: each top-level user journey tested ⇒ 10+ flows
- [ ] T145 [sonnet] Visual regression tests (Chromatic): baseline set ⇒ running
- [ ] T146 [sonnet] Performance budget file ⇒ committed
- [ ] T147 [sonnet] Build-size monitoring via bundle-analyzer in CI ⇒ comment on PRs
- [ ] T148 [sonnet] Changelog.md updated with Sprint 2 entries ⇒ written
- [ ] T149 [sonnet] V1 smoke test run on 5 devices (Chrome, Safari, Firefox, Android, iOS) ⇒ all green
- [ ] T150 [sonnet] Final /app polish: typography pass, spacing pass, alignment ⇒ review passes
