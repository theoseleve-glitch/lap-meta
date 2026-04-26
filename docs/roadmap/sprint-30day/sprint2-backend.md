# LAP Backend — Sprint 2 Queue (post-Sprint-1 remainder of 6-month roadmap)

**Starts when:** Sprint 1 `sprint-backend.md` drains (~Day 10-12 at current pace).
**Covers:** M3 APIs + M4 bridge + cohort + endurance + target events + strategy plan/actual + coaching library 25→75 rules + B2B + v2 prep.
**Total:** 200 tasks. Same /loop rules as Sprint 1 (see `LOOP-SETUP.md`).
**Transition:** change Terminal 1's /loop prompt to reference `sprint2-backend.md` instead of `sprint-backend.md`.

---

## Block A — M3 API completion (T001–T015)

- [x] T001 [sonnet] `GET /api/v1/driver/timeline?cursor=&limit=20` paginated endpoint returning SessionRecord[] with badges ⇒ tested — sha: afcd3af (lap-schemas: 234890d)
- [x] T002 [sonnet] Timeline cursor format (base64 of `{sha256(user_id+last_seen_at)}`) ⇒ opaque + stable — sha: 6f9bbc3
- [x] T003 [sonnet] Timeline filters: source, track, car, date range ⇒ composable — sha: d183302
- [x] T004 [sonnet] `GET /api/v1/driver/profile` single-shot aggregate (progress snapshot + top-5 weaknesses + active prescriptions + readiness) ⇒ <200ms p95 — sha: 717fa07 (lap-schemas: 071be32)
- [x] T005 [opus] Durable Compare API: `POST /api/v1/compare_cases`, `GET /api/v1/compare_cases/:id`, `DELETE` ⇒ CRUD tested — sha: ea19755 (lap-schemas: a5c60ff)
- [x] T006 [sonnet] Compare case refetch: when referenced sessions reprocessed, outcome section updates ⇒ cache invalidation works — sha: 52746b1 (lap-schemas: 94217a5)
- [x] T007 [sonnet] `GET /api/v1/driver/weaknesses/:id` weakness detail with history + evidence + linked prescriptions ⇒ tested — sha: c63c325 (lap-schemas: a78e56e)
- [x] T008 [sonnet] `POST /api/v1/prescriptions/:id/accept` / `/skip` / `/flag-wrong` ⇒ state transitions tested — sha: 60dbf23
- [x] T009 [sonnet] `GET /api/v1/driver/skills/:dimension` drilldown endpoint (trend + best/worst sessions + related weaknesses) ⇒ tested — sha: d7e8643 (lap-schemas: 3ada902)
- [x] T010 [sonnet] `GET /api/v1/sessions/:id/coaching` aggregated coaching view for a single session ⇒ tested — sha: 5963ca3 (lap-schemas: 1e353d5)
- [x] T011 [sonnet] `POST /api/v1/insights/:id/flag` user-flagged false positive → decrements rule confidence ⇒ tested — sha: 5199e03
- [x] T012 [sonnet] Rule false-positive aggregation job (nightly) ⇒ surfaces high-FP rules to admin — sha: a4bca1a
- [x] T013 [sonnet] `GET /api/v1/admin/rules/health` admin endpoint listing rules with FP rate ⇒ 200 — sha: 0c25e0f
- [x] T014 [sonnet] Rate-limit enforcement: 100 req/min/user read, 10 ingest/hr ⇒ 429 on overflow — sha: 465c95d
- [x] T015 [sonnet] API contract tests: schemathesis against OpenAPI ⇒ zero drift — sha: dfd0c0d

## Block B — Bridge entity + CRUD (T016–T030)

- [x] T016 [opus] `TransferLink` Pydantic model per ADR-005 §5.5 ⇒ validates, round-trip JSON — sha: ee5a979 (lap-schemas)
- [x] T017 [opus] `DivergencePoint` Pydantic model ⇒ validates — sha: fe5ac42 (lap-schemas)
- [x] T018 [opus] ORM `TransferLinkEntity` + migration (driver_id, session_pair, shape_match, intensity_match, divergence_points, created_by) ⇒ applied — sha: 512892a (already shipped as T068 in sprint 1; verified migration applies + round-trip test green)
- [x] T019 [opus] `POST /api/v1/bridge/links` create link (manual or auto) ⇒ tested — sha: eb15c68 (lap-schemas: 627d3b6)
- [x] T020 [opus] `GET /api/v1/bridge/links/:id` full report ⇒ tested — sha: 256a2ca
- [x] T021 [opus] `GET /api/v1/driver/:id/bridge/links` paginated driver timeline of links ⇒ tested — sha: d4ae4e5 (lap-schemas: 355f337)
- [x] T022 [opus] `DELETE /api/v1/bridge/links/:id` revoke ⇒ tested — sha: 404c582
- [x] T023 [opus] `POST /api/v1/bridge/links/:id/rate` thumbs-up/down usefulness feedback ⇒ stored — sha: 7a575fa (lap-schemas: 26c2485)
- [x] T024 [opus] Bridge RLS: drivers can only see their own links ⇒ integration test proves — sha: c607358
- [x] T025 [sonnet] Bridge storage: divergence_points stored as JSONB array, indexed by track_distance_m ⇒ efficient — sha: 8dc92ee
- [ ] T026 [sonnet] Link validation: both sessions must be same master_track_id + comparable car class ⇒ enforced
- [ ] T027 [sonnet] Link dedup: same pair can't be linked twice ⇒ 409 on conflict
- [ ] T028 [sonnet] Backend generates `CoachingInsight` when a link is created (transfer findings) ⇒ persisted
- [ ] T029 [sonnet] Link lifecycle: marked `stale` if a referenced session is deleted ⇒ tested
- [ ] T030 [sonnet] Bulk link operations: batch create for migration/import ⇒ tested

## Block C — Bridge algorithms (T031–T050)

- [ ] T031 [opus] Lap-aligned segmenter: given two sessions + corner set, returns paired lap segments ⇒ unit-tested with fixture
- [ ] T032 [opus] Channel extraction: brake, throttle, steering, speed, g_lat, g_lon ⇒ consistent DataFrame shape
- [ ] T033 [opus] Normalization: each channel resampled to 500 points per corner via cubic spline ⇒ stable
- [ ] T034 [opus] Shape match algorithm: normalized cross-correlation per channel ⇒ returns 0-1 score
- [ ] T035 [opus] Shape match validation: on identical sim-vs-sim sessions returns 1.0 ⇒ tested
- [ ] T036 [opus] Shape match: on sim-vs-real same track gives >0.6, <0.95 ⇒ validated with archived pair
- [ ] T037 [opus] Intensity match algorithm: peak + integral ratios per channel ⇒ returns 0-1 score
- [ ] T038 [opus] Intensity match validation: identical sessions = 1.0, scaled sessions = 0.8 ⇒ tested
- [ ] T039 [opus] Divergence detection: scan per-corner for shape ≥0.9 but intensity ≤0.6 → "same shape, different intensity" divergence ⇒ tested
- [ ] T040 [opus] Divergence detection: scan for shape ≤0.5 → "different technique" divergence ⇒ tested
- [ ] T041 [opus] Divergence point serialization: corner tag + metric + sim_value + real_value + divergence_type ⇒ persisted
- [ ] T042 [opus] Transferred-skills extraction: skills (dimensions) where both shape + intensity ≥0.85 ⇒ listed
- [ ] T043 [opus] Non-transferred-skills extraction: dimensions where shape <0.7 OR intensity <0.5 ⇒ listed
- [ ] T044 [opus] Bridge algorithm performance: process a pair in <5s ⇒ benchmarked
- [ ] T045 [opus] Bridge algorithm deterministic: same input = same output ⇒ test
- [ ] T046 [sonnet] `GET /api/v1/bridge/suggest_links?session_id=X` returns candidate pairs by track + car class + 60-day window ⇒ tested
- [ ] T047 [sonnet] Suggest ordering: most-similar-track first, then recency ⇒ tested
- [ ] T048 [sonnet] Suggest cache: 1h TTL per session ⇒ tested
- [ ] T049 [sonnet] Algorithm fallback: if channel missing in one session, flag "partial-comparison" and exclude that channel ⇒ tested
- [ ] T050 [sonnet] Algorithm tests against archived Sebring-sim + Sebring-real pair in LapCoachLogger_sessions/ ⇒ produces sensible output

## Block D — Cohort benchmarks (T051–T065)

- [ ] T051 [opus] `DriverBenchmarkProfile` Pydantic + ORM entity ⇒ migration
- [ ] T052 [opus] `cohort_opt_in` field on DriverProfile + privacy enforcement ⇒ only opt-in drivers' data flows to cohort
- [ ] T053 [opus] `PATCH /api/v1/driver/profile` to toggle cohort_opt_in ⇒ updates
- [ ] T054 [opus] Anonymized metric store: `cohort_metrics` table with `{car_id, track_id, metric, value, session_time}`, NO driver_id ⇒ schema
- [ ] T055 [opus] Cohort ingestion job: after each session, if opt-in, append metric rows ⇒ nightly or per-session
- [ ] T056 [opus] Cohort minimum: compute percentile only if ≥20 distinct cohort members per {car_id, track_id, metric} ⇒ enforced
- [ ] T057 [opus] Percentile compute: per-dimension, per-(car+track) ⇒ nightly aggregation
- [ ] T058 [opus] `GET /api/v1/driver/benchmark` returns driver's percentile profile (null if cohort not unlocked) ⇒ tested
- [ ] T059 [sonnet] Cohort size query endpoint: "how many drivers have this car+track combo?" ⇒ for UI messaging
- [ ] T060 [sonnet] Archetype assignment: given percentiles, tag as `late_braker`, `smooth_flow`, etc. ⇒ rule-based
- [ ] T061 [sonnet] Cohort privacy audit: test that querying another driver's percentile is impossible ⇒ proven
- [ ] T062 [sonnet] Cohort data deletion: when driver opts out, purge their metric rows ⇒ tested
- [ ] T063 [sonnet] Cohort refresh: percentiles recomputed weekly ⇒ cron
- [ ] T064 [sonnet] Admin endpoint: `/api/v1/admin/cohort/status` shows size per cohort context ⇒ auth-gated
- [ ] T065 [sonnet] Cohort unlock notifications: when a driver's cohort crosses 20 threshold, send event → triggers benchmark population ⇒ tested

## Block E — Endurance + long-run scoring (T066–T080)

- [ ] T066 [opus] `endurance_event_id` field on SessionManifest ⇒ schema updated
- [ ] T067 [opus] `EnduranceEvent` entity (id, event_name, total_duration, stint_count, driver_ids) ⇒ migration
- [ ] T068 [opus] Stint detection: in long sessions, split into stints by pit-event markers ⇒ tested
- [ ] T069 [opus] Stint record: per-stint laps, tire age, fuel used, lap-time decay ⇒ persisted
- [ ] T070 [opus] Long-run consistency score: stddev of lap time over last N laps of each stint ⇒ tested
- [ ] T071 [opus] Pace-decay score: slope of lap time over stint duration ⇒ tested
- [ ] T072 [opus] Tire preservation score: tire-life proxy from fuel + pace decay ⇒ rule-based
- [ ] T073 [opus] Endurance-weighted DriverProgressSnapshot (adds long-run dimensions) ⇒ tested
- [ ] T074 [opus] Coaching rules specific to endurance (stint management, tire) ⇒ 5+ rules authored
- [ ] T075 [sonnet] `GET /api/v1/endurance/events/:id` summary endpoint ⇒ tested
- [ ] T076 [sonnet] `GET /api/v1/driver/endurance/history` list ⇒ tested
- [ ] T077 [sonnet] Endurance-specific insights emitted: "your pace decay in hour 2 is 0.8s/lap — coolant management issue" ⇒ fires
- [ ] T078 [sonnet] Long-run benchmarks (cohort, if opt-in): percentile of pace decay ⇒ available
- [ ] T079 [sonnet] Endurance test: 90-min archive session scored correctly ⇒ validated
- [ ] T080 [sonnet] Endurance edge cases: single-stint session, variable stint length ⇒ tested

## Block F — Target events + calendar (T081–T095)

- [ ] T081 [opus] `TargetEvent` entity (id, driver_id, source, event_name, track, car, date, priority) ⇒ migration
- [ ] T082 [opus] `POST /api/v1/driver/target-events` pin a target ⇒ tested
- [ ] T083 [opus] `DELETE /api/v1/driver/target-events/:id` unpin ⇒ tested
- [ ] T084 [opus] `GET /api/v1/driver/target-events` list ⇒ tested
- [ ] T085 [opus] iRacing calendar scraper: weekly fetch official series + special events ⇒ data stored
- [ ] T086 [opus] Calendar parser: extract track, car class, start-end dates ⇒ tested
- [ ] T087 [opus] Calendar refresh cron: Mondays 08:00 UTC ⇒ runs
- [ ] T088 [opus] Real-life events (manual curation): user can add a track day ⇒ form endpoint
- [ ] T089 [opus] Target-aware readiness: DriverReadinessState recomputed when event pinned/unpinned ⇒ tested
- [ ] T090 [opus] Target-aware plan generation: ActionPrescription priority weighted by match to target ⇒ tested
- [ ] T091 [opus] Target preparation milestones: "3 sessions until event" triggers specific prescriptions ⇒ rule
- [ ] T092 [sonnet] Event suggestion: recommend events matching driver's history ⇒ algorithm
- [ ] T093 [sonnet] Event countdown endpoint for UI ⇒ tested
- [ ] T094 [sonnet] Event notification (via email) 24h and 1h before ⇒ scheduled via Celery
- [ ] T095 [sonnet] Event post-mortem: after event, compare predicted readiness to actual performance ⇒ feedback loop

## Block G — Strategy plan vs actual (T096–T110)

- [ ] T096 [opus] `StrategyPlan` entity (id, session_id, planned_stints, planned_fuel, planned_pit_laps) ⇒ migration
- [ ] T097 [opus] `StrategyEvent` entity (id, session_id, kind [plan, armed, pit, stint_end, fcy, sc], at_lap, details) ⇒ migration
- [ ] T098 [opus] `POST /api/v1/sessions/:id/strategy/plan` set pre-race plan ⇒ tested
- [ ] T099 [opus] `POST /api/v1/sessions/:id/strategy/events` append runtime event ⇒ tested
- [ ] T100 [opus] `GET /api/v1/sessions/:id/strategy/timeline` combined plan+actual timeline ⇒ tested
- [ ] T101 [opus] Plan-vs-actual divergence scoring: pit-lap delta, fuel delta, stint duration delta ⇒ computed
- [ ] T102 [opus] Strategy execution score (0-100) per session ⇒ persisted
- [ ] T103 [opus] Bundle v2 extension: strategy_section in manifest ⇒ tested round-trip
- [ ] T104 [sonnet] Strategy insights: coaching emitted when execution <70 (e.g., "missed pit window by 3 laps") ⇒ rule
- [ ] T105 [sonnet] Plan-vs-actual visualization data endpoint for webapp ⇒ tested
- [ ] T106 [sonnet] Strategy history endpoint ⇒ lists recent sessions with execution scores
- [ ] T107 [sonnet] Strategy templates: user can save "my Le Mans strategy" for reuse ⇒ CRUD
- [ ] T108 [sonnet] FCY/SC event integration: strategy recalcs accounting for caution laps ⇒ tested
- [ ] T109 [sonnet] Strategy simulation API: "what if I pitted 2 laps later?" ⇒ returns alt outcome
- [ ] T110 [sonnet] Strategy tests vs archived endurance sessions ⇒ sensible outputs

## Block H — Coaching library expansion (T111–T160) — 50 new rules

**Goal: go from ~10 rules (Sprint 1) to 60 total. Each task = 1 rule authored + tested against ≥3 archive sessions.**

### Throttle pickup (T111–T120)
- [ ] T111 [opus] Rule `th.early_throttle.snap_oversteer` (early throttle causes rear slip) ⇒ YAML + tests
- [ ] T112 [opus] Rule `th.late_throttle.exit_speed_loss` (late throttle loses exit momentum) ⇒ YAML + tests
- [ ] T113 [opus] Rule `th.abrupt_pickup.traction_break` (binary on-off vs modulated) ⇒ YAML + tests
- [ ] T114 [opus] Rule `th.partial_throttle.mid_corner` (coasting instead of committing) ⇒ YAML + tests
- [ ] T115 [opus] Rule `th.throttle_lift.mid_corner` (involuntary lift) ⇒ YAML + tests
- [ ] T116 [opus] Rule `th.staircase_pattern.uneven_modulation` ⇒ YAML + tests
- [ ] T117 [opus] Rule `th.early_full.before_apex` ⇒ YAML + tests
- [ ] T118 [opus] Rule `th.full_throttle_underuse.straights` ⇒ YAML + tests
- [ ] T119 [opus] Rule `th.throttle_consistency.lap_variance` ⇒ YAML + tests
- [ ] T120 [opus] Rule `th.exit_commit.confidence_deficit` ⇒ YAML + tests

### Minimum speed / cornering (T121–T130)
- [ ] T121 [opus] Rule `cs.min_speed.too_low_late_apex` ⇒ YAML + tests
- [ ] T122 [opus] Rule `cs.min_speed.too_high_wide_line` ⇒ YAML + tests
- [ ] T123 [opus] Rule `cs.apex_miss.early_turn` ⇒ YAML + tests
- [ ] T124 [opus] Rule `cs.apex_miss.late_turn` ⇒ YAML + tests
- [ ] T125 [opus] Rule `cs.line_variance.inconsistent_apex` ⇒ YAML + tests
- [ ] T126 [opus] Rule `cs.rotation_lack.understeer_mid` ⇒ YAML + tests
- [ ] T127 [opus] Rule `cs.rotation_excess.overrotation_exit` ⇒ YAML + tests
- [ ] T128 [opus] Rule `cs.trail_brake_insufficient.rotation_missing` ⇒ YAML + tests
- [ ] T129 [opus] Rule `cs.steering_smoothness.saw_pattern` ⇒ YAML + tests
- [ ] T130 [opus] Rule `cs.corner_speed.cohort_deficit` (requires cohort) ⇒ YAML + tests

### Consistency / racecraft (T131–T140)
- [ ] T131 [opus] Rule `co.lap_time_variance.high_spread` ⇒ YAML + tests
- [ ] T132 [opus] Rule `co.lap_time_trend.fade_over_run` ⇒ YAML + tests
- [ ] T133 [opus] Rule `co.sector_consistency.t1_volatile` ⇒ YAML + tests
- [ ] T134 [opus] Rule `co.braking_point_drift.over_run` ⇒ YAML + tests
- [ ] T135 [opus] Rule `rc.passing_attempts.abort_rate` ⇒ YAML + tests
- [ ] T136 [opus] Rule `rc.defensive_line.too_often` ⇒ YAML + tests
- [ ] T137 [opus] Rule `rc.blue_flag_compliance.slow_lift` ⇒ YAML + tests
- [ ] T138 [opus] Rule `rc.restart_acceleration.poor_launch` ⇒ YAML + tests
- [ ] T139 [opus] Rule `rc.pit_exit_safety.slow_merge` ⇒ YAML + tests
- [ ] T140 [opus] Rule `rc.overtake_position.inside_inefficient` ⇒ YAML + tests

### Tire + fuel management (T141–T150)
- [ ] T141 [opus] Rule `tm.tire_temp_overheat.aggressive_early` ⇒ YAML + tests
- [ ] T142 [opus] Rule `tm.tire_wear.unbalanced_front_rear` ⇒ YAML + tests
- [ ] T143 [opus] Rule `tm.stint_pace_decay.tire_degradation` ⇒ YAML + tests
- [ ] T144 [opus] Rule `tm.lockup_pattern.flat_spot_risk` ⇒ YAML + tests
- [ ] T145 [opus] Rule `fm.fuel_burn_excess.vs_target` ⇒ YAML + tests
- [ ] T146 [opus] Rule `fm.lift_and_coast.too_rare` ⇒ YAML + tests
- [ ] T147 [opus] Rule `fm.fuel_saving.ineffective_pattern` ⇒ YAML + tests
- [ ] T148 [opus] Rule `fm.pit_window.late_entry_risk` ⇒ YAML + tests
- [ ] T149 [opus] Rule `tm.cold_tire_mistakes.first_3_laps` ⇒ YAML + tests
- [ ] T150 [opus] Rule `tm.warm_up_pace.too_aggressive` ⇒ YAML + tests

### Adaptation + conditions (T151–T160)
- [ ] T151 [opus] Rule `ad.grip_change.slow_to_adapt` ⇒ YAML + tests
- [ ] T152 [opus] Rule `ad.setup_change.regression` ⇒ YAML + tests
- [ ] T153 [opus] Rule `ad.weather_transition.wet_line_wrong` ⇒ YAML + tests
- [ ] T154 [opus] Rule `ad.rain_start.tire_commitment_late` ⇒ YAML + tests
- [ ] T155 [opus] Rule `ad.traffic_loss.defensive_excess` ⇒ YAML + tests
- [ ] T156 [opus] Rule `ad.new_track.learning_rate_slow` ⇒ YAML + tests
- [ ] T157 [opus] Rule `ad.car_change.transfer_gap` ⇒ YAML + tests
- [ ] T158 [opus] Rule `ad.qualifying_vs_race.pace_delta` ⇒ YAML + tests
- [ ] T159 [opus] Rule `ad.pressure_response.error_rate_spike` ⇒ YAML + tests
- [ ] T160 [opus] Rule `ad.night_driving.pace_drop` ⇒ YAML + tests

## Block I — B2B + multi-seat (T161–T180)

- [ ] T161 [opus] `Organization` entity + migration (id, name, plan, admin_user_id, seats_limit) ⇒ applied
- [ ] T162 [opus] `OrganizationMember` entity (org_id, user_id, role [admin, coach, driver]) ⇒ migration
- [ ] T163 [opus] `POST /api/v1/orgs` create org ⇒ tested
- [ ] T164 [opus] `POST /api/v1/orgs/:id/invites` invite user by email ⇒ tested
- [ ] T165 [opus] `POST /api/v1/orgs/:id/invites/:token/accept` user redeems invite ⇒ tested
- [ ] T166 [opus] `DELETE /api/v1/orgs/:id/members/:user_id` admin removes member ⇒ tested
- [ ] T167 [opus] Org RLS: members see only their org's drivers; admins can see all members ⇒ tested
- [ ] T168 [opus] Stripe: multi-seat subscription product + proration on member add/remove ⇒ tested
- [ ] T169 [opus] Coach role: can view drivers' profiles but not edit billing ⇒ tested
- [ ] T170 [opus] Seat cap enforcement: invite rejected if at limit ⇒ 402 response
- [ ] T171 [sonnet] Coach dashboard endpoint: aggregate view of org drivers' progress ⇒ tested
- [ ] T172 [sonnet] Coach assign prescriptions manually: `POST /api/v1/coach/prescriptions` ⇒ tested
- [ ] T173 [sonnet] Coach notes on driver sessions: `POST /api/v1/sessions/:id/coach-notes` ⇒ tested
- [ ] T174 [sonnet] Org-level metrics: average WPD, best gains by dimension ⇒ aggregate endpoint
- [ ] T175 [sonnet] Org branding (uploadable logo, custom domain later) ⇒ metadata field
- [ ] T176 [sonnet] Org deletion: cascading cleanup (members unlinked but data preserved) ⇒ tested
- [ ] T177 [sonnet] B2B pricing tiers: 5-seat / 15-seat / unlimited ⇒ Stripe products created
- [ ] T178 [sonnet] Trial for orgs: 30-day free on initial signup ⇒ Stripe configured
- [ ] T179 [sonnet] Org invoice PDF: sent monthly ⇒ via Stripe
- [ ] T180 [sonnet] Integration test: org creation → invite → accept → coach assigns → driver sees ⇒ green

## Block J — Security + v2 prep + polish (T181–T200)

- [ ] T181 [opus] Security audit: all endpoints checked for missing auth, IDOR, privilege escalation ⇒ report
- [ ] T182 [opus] Rate limit tuning based on real traffic: differentiate read/write/ingest ⇒ deployed
- [ ] T183 [opus] Secret rotation runbook: Stripe, Clerk, Resend, R2 — steps documented ⇒ committed
- [ ] T184 [opus] CORS review: tighten allowed origins for prod ⇒ tested
- [ ] T185 [sonnet] Backup restore test: restore from yesterday's pg_dump to staging ⇒ runs
- [ ] T186 [sonnet] Disaster-recovery plan doc: RTO, RPO, failover steps ⇒ written
- [ ] T187 [sonnet] Structured error codes: `ErrorCode` enum used consistently ⇒ migrated
- [ ] T188 [sonnet] API v2 scaffold: `/api/v2/` router empty, v1 still primary ⇒ compiles
- [ ] T189 [sonnet] Deprecation policy doc: how v1 endpoints sunset ⇒ written
- [ ] T190 [sonnet] Performance: N+1 query audit across all endpoints ⇒ fixed
- [ ] T191 [sonnet] Performance: add query plans for top-10 slowest ⇒ indexed
- [ ] T192 [sonnet] Observability: Prometheus custom histograms for business metrics ⇒ scraping
- [ ] T193 [sonnet] Alerting: PagerDuty/webhook for `5xx rate >0.5%` sustained ⇒ wired
- [ ] T194 [sonnet] GDPR export endpoint: `POST /api/v1/me/export` delivers user data zip ⇒ tested
- [ ] T195 [sonnet] GDPR delete endpoint: `DELETE /api/v1/me` cascading delete ⇒ tested
- [ ] T196 [sonnet] Data retention policy: anonymize sessions >2 years old for opted-out users ⇒ cron
- [ ] T197 [sonnet] Admin audit log: all admin actions logged with user_id + action + timestamp ⇒ tested
- [ ] T198 [sonnet] Changelog.md updated with Sprint 2 entries ⇒ written
- [ ] T199 [sonnet] OpenAPI docs published at `/api/v1/docs` with auth protection toggled off for docs-only ⇒ accessible
- [ ] T200 [sonnet] Load test pass 2: 500 concurrent users, target <300ms p95 on all endpoints ⇒ passes
