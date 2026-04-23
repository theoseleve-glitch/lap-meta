# LAP — 6-Month Development Roadmap (Nov 2026 → Apr 2027)

**Owner**: Théo • **Team size**: 1 FTE + heavy AI assist (Claude Code Max 20x, Codex, Copilot, Claude Design, Figma) • **Budget**: €400/mo infra+tooling
**Horizon**: Public beta by end of M3 • Full paid release end of M5 • Post-launch iteration M6
**Target**: 1000 paying users, €10k MRR by end of M6
**North-star product identity**: **Driver OS — Garmin for racing drivers**, cross-surface driver progression as the moat

---

## 0. Strategic Compass

### Product doctrine (frozen for 6 months)
1. **Server is the brain. Clients are thin.** All coaching intelligence, progression, weakness lifecycle, readiness, and bridge diagnostics live in `lap_backend`. Clients render insight objects, never invent them. Exception: desktop can compute <100ms local overlays from raw telemetry (speed, gear, brake bias) — but never "you're losing X in Y" coaching.
2. **One canonical driver, many environments.** A driver is a single identity with multiple personas (sim/kart/car) and multiple vehicles/tracks/championships. Sim and real sessions live in the same timeline.
3. **One bundle format, one session API.** Bundle v2 is canonical. `sessions_v2` and `sync_upload` unify into a single ingestion pipeline.
4. **No LLM in user-facing coaching text.** Premium, understandable, measured language comes from a human-written coaching library indexed by weakness type, severity, driver level.
5. **Offline-first on mobile and desktop is strict.** Never lose a session. Always recover. Always resume upload.
6. **Ship > craft when in tension.** This is a ship-or-die runway. Every optional polish defers until after the M5 full release.

### Success criteria (M6 end)
- 500+ paying users minimum (target 1000)
- €5k+ MRR minimum (target €10k)
- Zero known session-loss defects on mobile or desktop
- Cross-surface driver timeline renders sim + real in one feed
- A new sim-racer can go from signup → uploaded session → actionable coaching plan in under 15 minutes unattended
- TransferLink exists as a real data object with at least one non-trivial diagnostic shipped

### Failure criteria (actively avoid)
- Four disconnected apps without shared identity or data flow
- Coaching text generated inconsistently across surfaces
- Mobile or desktop losing a track session
- Stripe not live by M5
- Sim↔real bridge parked to 2027

### Explicit non-goals (frozen — reject even if users ask)
1. No social features (leaderboards, friend feeds, public sharing) in M1–M6.
2. No live multi-car telemetry streaming to web.
3. No LLM-generated coaching prose anywhere user-visible.
4. No team/B2B admin features beyond "same account, multiple drivers" stub.
5. No dataset-labeling ML — only heuristics + simple statistical baselines per driver.
6. No real-time collaboration (multiple users editing same session).
7. No native Mac desktop build (Windows only for logger).
8. No Chinese / Japanese / Korean i18n.
9. No self-hosted/on-prem deployment.
10. No community-contributed coaching content.

---

## 1. Decisions locked (delegated to me — reject now or never)

| Area | Decision | Why |
|---|---|---|
| Backend framework | Migrate Flask → **FastAPI** | Async-native for streaming ingestion; Pydantic v2 is the schema; AI tooling is excellent on FastAPI; type-safe. |
| Worker queue | **Celery + Redis** (keep) | Already in use; no reason to churn. |
| Schema registry | **Pydantic v2 → codegen** | TS types via `pydantic2ts`, JSON Schema via `.model_json_schema()`, one Python source of truth. |
| Canonical ID | **UUIDv7** | Time-ordered, indexable, well-supported in Postgres 16, Python `uuid-utils`, Swift UUID, TS `uuid` v10. |
| `lap_tool_virtualisation` | **Absorb** into `lap_backend/processing/` | Solo dev; less coordination overhead; Celery workers still run independently. |
| Marketing site | **Extract** to `lap_marketing` (Astro) | Decoupled deploy, static+MDX, way faster SEO iteration. |
| Bundle format | **Bundle v2 canonical** across all clients | Hard cutover; old sessions reprocessed server-side. |
| Database | **Postgres 16** (confirm current) | JSONB for flexible telemetry fields, time-series extension optional later. |
| Auth | **Supabase Auth** (keep — you already use Supabase MCP) | Magic link for web → client handoff. |
| Mobile platforms | **iOS (M1-6) + Android (M4 kickoff)** | Android launches M6 in beta. |
| Companion | **Apple Watch companion M6** | Steering feel via wrist IMU + HR. Stretch goal. |
| Sim titles (M6) | iRacing, ACC, AC, AMS2, rF2, LMU, Rennsport, F1 | Priority: iRacing > ACC > LMU > rest. F1 and AC are last. |
| Real-life hardware | **RaceBox Mini + RaceBox Micro full UBX** | Parser expands in M2. |
| Pricing | Free 14-day trial → **Racer €14.99/mo** → **World-Class €24.99/mo** | Kill Demo tier. |
| LLM usage | **None in user-visible text**. Internal only (code review, test generation). | Hard rule. |

---

## 2. Architecture Blueprint

### Repo topology (end state, end of M2)

```
lap_backend/                  (FastAPI monolith, Celery workers, Postgres, Redis)
├── api/                      HTTP layer (FastAPI routers)
├── contracts/                Pydantic models — single source of truth
├── ingestion/                Upload, bundle validation, canonical transform
├── processing/               (absorbs lap_tool_virtualisation) — Celery tasks, detectors, feature extraction
├── coaching/                 WeaknessEpisode engine, ActionPrescription generator, coaching library
├── progression/              DriverProgressSnapshot, benchmarks, readiness scoring
├── bridge/                   TransferLink, sim↔real diagnostics
├── billing/                  Stripe integration
├── auth/                     Supabase Auth bridge
├── db/                       Alembic migrations, SQLModel repositories
├── tests/
└── ops/                      Deploy scripts, monitoring

lap_webapp/                   (Next.js 14 app router — consumer-only, no marketing)
├── app/                      (Keep /(app)/* routes; delete /(marketing)/*)
├── components/
├── lib/
│   ├── api/                  Generated TS types from backend + typed fetchers
│   └── hooks/
├── tests/

lap_desktop/                  (Qt/QML, Python)
├── capture/                  Adapter framework, finalization
├── live/                     Live overlays, local-compute detectors
├── modes/                    NEW — Practice/Sprint/Endurance policy layer
├── bundle/                   Bundle v2 writer
├── sync/                     Upload to backend
└── ui/                       QML shell

lap_mobile/                   (iOS Swift, Android Kotlin M4+)
├── ios/LapCoachMobile/
├── android/LapCoachMobile/   (M4 kickoff)
└── shared-schema/            Generated Swift+Kotlin from Pydantic JSON Schema

lap_marketing/                (Astro — extracted M1)
├── pages/
├── content/
└── components/
```

### Data flow (happy path)

```
[Desktop/Mobile capture] 
    ↓ Bundle v2 (JSON manifest + Parquet telemetry + checksums)
[Backend ingestion API] 
    ↓ Validate → Store canonical → Enqueue processing
[Celery processing] 
    ↓ Detectors → Features → WeaknessEpisode candidates
[Coaching engine] 
    ↓ Rules + driver baseline → ActionPrescription
[Progression engine] 
    ↓ DriverProgressSnapshot update
[Webapp renders] insights + timeline + plan
```

### Live coaching path (desktop)
```
Desktop local detector (cheap, <100ms) 
    → Raw signal detected
Backend low-latency endpoint (WebSocket or SSE)
    → Enriched insight (coaching text from library, severity, prescription)
Desktop overlay renders
```

Round-trip target: <500ms for non-critical, desktop-local-only for <100ms prompts.

---

## 3. Canonical Data Contracts (Pydantic v2)

These ship in Month 1. They are the foundation — every other piece of work depends on them.

### `Session`
```python
class Session(BaseModel):
    id: UUID                              # UUIDv7
    driver_id: UUID
    source: SourceType                    # enum: IRACING | ACC | AC | AMS2 | RF2 | LMU | RENNSPORT | F1 | KART | CAR_TRACK | UNKNOWN
    environment: EnvironmentType          # enum: SIM | REAL
    vehicle_ref: VehicleRef               # normalized via backend-owned catalog
    track_ref: TrackRef
    session_type: SessionType             # PRACTICE | QUALI | SPRINT | ENDURANCE | TEST | DRILL
    objective: Optional[str]              # free-text or linked ActionPrescription id
    started_at: datetime
    ended_at: datetime
    lap_count: int
    best_lap_ms: Optional[int]
    data_quality: DataQualityScore
    provenance: Provenance                # device, firmware, sensor config, app build
    bundle_ref: BundleRef                 # storage pointer + checksum
    status: SessionStatus                 # INGESTED | PROCESSING | COACHED | FAILED
    linked_session_id: Optional[UUID]     # for TransferLink (sim↔real manual or auto)
```

### `WeaknessEpisode`
```python
class WeaknessEpisode(BaseModel):
    id: UUID
    driver_id: UUID
    category: WeaknessCategory            # TECHNIQUE | CONSISTENCY | SETUP_SENSITIVITY | CONFIDENCE | RACE_MANAGEMENT | EXECUTION
    subtype: str                          # e.g. "late_apex_turn_in", "brake_release_choppy"
    first_seen_at: datetime
    last_seen_at: datetime
    recurrence_count: int
    severity: float                       # 0..1
    confidence: float                     # 0..1, decays without reinforcement
    environments: list[EnvironmentType]   # SIM, REAL, or both
    affected_tracks: list[UUID]
    affected_vehicles: list[UUID]
    status: EpisodeStatus                 # OPEN | RESOLVING | RESOLVED | DORMANT
    evidence_sessions: list[UUID]         # session ids that reinforced this
    last_prescription_id: Optional[UUID]
```

### `ActionPrescription`
```python
class ActionPrescription(BaseModel):
    id: UUID
    driver_id: UUID
    weakness_episode_id: UUID
    title: str                            # coaching-library-referenced, NOT LLM-generated
    rationale: str                        # same: from library
    drill_type: DrillType                 # BRAKING | THROTTLE | CONSISTENCY | TIRE | TRAFFIC | FUEL | WET | QUALI | CORNER_FOCUS
    target_context: TargetContext         # which track/car/session_type this applies to
    success_condition: MeasurableTarget   # e.g. "reduce sector 2 variance to <0.15s across 5 laps"
    expected_gain_ms: Optional[int]
    due_by_session: Optional[int]         # session ordinal or next-N
    priority: int                         # 0..100 (most-coachable first, not biggest-time-loss)
    created_at: datetime
    status: PrescriptionStatus            # ASSIGNED | IN_PROGRESS | COMPLETED | EXPIRED
```

### `ActionOutcome`
```python
class ActionOutcome(BaseModel):
    id: UUID
    prescription_id: UUID
    session_id: UUID                      # the session in which we measured
    completed: bool
    measured_result: MeasuredResult       # actual value of the success_condition metric
    improvement_observed: bool
    confidence_delta: float               # how much this bumps confidence in resolution
    notes: Optional[str]
```

### `TransferLink`
```python
class TransferLink(BaseModel):
    id: UUID
    driver_id: UUID
    sim_session_id: UUID
    real_session_id: UUID
    link_type: Literal["MANUAL", "AUTO_SUGGESTED"]
    track_analog_confidence: float        # how similar the tracks are in the catalog
    vehicle_analog_confidence: float
    diagnostics: TransferDiagnostics      # shape_match vs intensity_match per channel
    created_at: datetime
```

### `DriverProgressSnapshot`
```python
class DriverProgressSnapshot(BaseModel):
    id: UUID
    driver_id: UUID
    computed_at: datetime
    environment: EnvironmentType          # SIM-only, REAL-only, or COMBINED snapshot
    dimensions: dict[Dimension, DimensionScore]  # braking, throttle, min_speed, line_consistency, tire_mgmt, racecraft, consistency, strategy_exec, setup_sensitivity, adaptation
    overall_score: float                  # LAP Elo-style aggregate
    iracing_ir_estimate: Optional[float]  # if SIM environment
    readiness: DriverReadinessState
    open_weakness_count: int
    resolved_weakness_count_30d: int
    trend_7d: float
    trend_30d: float
```

### `DriverReadinessState`
```python
class DriverReadinessState(BaseModel):
    driver_id: UUID
    computed_at: datetime
    readiness_score: float                # 0..100
    inputs: ReadinessInputs               # volume, quality, recency, consistency, unresolved_weaknesses, familiarity, event_pressure
    limiting_factor: str                  # human-readable
    recommendation: Optional[str]         # "practice X before event Y"
```

### `CoachingInsight` (runtime output — what clients render)
```python
class CoachingInsight(BaseModel):
    id: UUID
    session_id: UUID
    driver_id: UUID
    observation: str                      # "late apex turn 4 over 6 of 10 laps"
    evidence: Evidence                    # telemetry span refs + chart preset
    likely_cause: str                     # from coaching library
    action: str                           # from library, level-appropriate
    measurable_target: MeasurableTarget
    confidence: float
    review_later_at: Optional[datetime]
    severity: Severity                    # INFO | LOW | MED | HIGH
    display_level: DriverLevel            # BEGINNER | INTERMEDIATE | ADVANCED — text variant picked accordingly
```

These seven, plus `Session`, are the spine.

---

## 4. AI Tool Assignment (legend used in task tables)

| Code | Tool | Use for |
|---|---|---|
| **CC** | Claude Code (Max 20x) | Multi-file refactors, architectural work, backend features, desktop QML+Python work, anything requiring strong reasoning across a repo |
| **CCS** | Claude Code Sonnet | Faster iteration on scoped tasks, test generation, single-feature implementation with clear spec |
| **COD** | Codex | Boilerplate, single-file edits, test scaffolding, simple bug fixes, generating many similar files |
| **CPT** | Copilot | Inline autocomplete during your hands-on coding, not standalone task assignment |
| **CD** | Claude Design / Figma AI | UI mockups, design system specs, component states, visual iteration |
| **CR** | Claude Chrome / Cowork | Research (competitor features, sim title specs, iRacing event calendars), coordination, cross-doc synthesis |
| **HUM** | You, manually | Architectural decisions, pricing, copy, product taste calls, schema design sign-off |

Rule of thumb: **CC for anything touching 3+ files or affecting contracts. COD for anything touching 1 file with clear spec. CCS when CC is busy or task is scoped tightly. HUM for anything that requires taste.**

---

## 5. Month-by-Month Roadmap

### Legend
- `→` = blocks downstream task
- `∥` = parallel-safe with other tasks in same block
- `P0` = stop-the-world severity
- `P1` = critical path for milestone
- `P2` = important but can slip 1–2 weeks
- Effort estimates assume you at 50+h/week with heavy AI assist

---

## MONTH 1 — Foundations (Nov 1 → Nov 30, 2026)

**Theme**: Kill the critical defects. Define the contracts. Set up the new backend skeleton. Start mobile reliability sprint. Extract marketing.

**Milestone**: End of M1 — all P0 defects closed, canonical Pydantic contracts defined and frozen, FastAPI skeleton serving a subset of v1 endpoints behind a feature flag, mobile capture journal shipping in internal build.

### Week 1 (Nov 1–7) — STOP-THE-WORLD War Room

All tasks in Week 1 are parallel across repos. Goal: close every P0 on the audit's defect list.

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 1.1 | P0 Fix `LapCoachAppModel.live()` force-unwrap (AppViewModel.swift:18-25) | mobile | 0.5d | CC | nothing | Replace `try!` with proper error handling surfaced in UI as startup-error screen. |
| 1.2 | P0 Fix `try! StorageService()` crash-on-init | mobile | 0.5d | CC | 1.1 | Convert to async init with failure UI. |
| 1.3 | P0 `finalizeSession` integrity contract (StorageService.swift:56-69) | mobile | 1d | CC | 1.2 | Must fail loudly and mark `corrupt_local` if tmp file missing/empty. Add tests. |
| 1.4 | P0 Prevent accidental stop via `fullScreenCover` dismissal (ContentView.swift:11-20) | mobile | 0.5d | COD | ∥ | Require explicit stop intent; confirm dialog + hold-to-stop. |
| 1.5 | P0 RaceBox mode: block recording state until first sample received | mobile | 0.5d | COD | ∥ | Guard in SessionManager.swift:63-75. |
| 1.6 | P0 Audit `live_telemetry_processor` missing imports — list the missing modules | desktop | 0.5d | CC | → 1.7 | Deliverable: a doc listing exactly what `LiveCoachTracker`, `LiveDashboardTracker`, `LiveInputDiagnostics` need to expose. |
| 1.7 | P0 **Decision**: rip out `live_telemetry_processor` reference, replace with stub emitting from backend (Month 2+) | desktop | 1d | CC | 1.6 | Desktop goes dumb on live coaching until M3; overlays still render local detectors (brake/throttle/speed/gear). Commit to this. |
| 1.8 | P0 Fix QML bootstrap test collection failure | desktop | 1d | CC | ∥ | Unblocks CI. |
| 1.9 | P0 Fix `/api/v1` double-prefix in bundle query hooks | webapp | 0.5d | COD | ∥ | |
| 1.10 | P0 Resolve duplicate `/sessions/:id/channels` route (data_v2.py vs data_v2_channels.py) | webapp + backend | 0.5d | CC | ∥ | Pick data_v2_channels.py as canonical; delete duplicate; register only once. |
| 1.11 | P0 Delete duplicate `src/types/bundles.ts` (keep `src/lib/api/bundles/types.ts`) | webapp | 0.5d | COD | ∥ | |
| 1.12 | P0 Repair stale E2E specs (sessions.spec.ts, compare.spec.ts) | webapp | 1d | CCS | 1.10 | Update mocks to current routes; make CI green. |
| 1.13 | Baseline all-repo CI green report | all | 0.5d | HUM+COD | after 1.1–1.12 | Merge all P0 fixes; CI must be green end of week. |

**End of Week 1 gate**: all repos CI green, no session-loss defect in mobile, desktop starts without import error.

### Week 2 (Nov 8–14) — Contract definition + backend skeleton

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 1.14 | **HUM** Freeze the 8 Pydantic contracts (Section 3 of this doc) — review field-by-field and sign off | backend | 1d | HUM+CC | → 1.16, 1.22 | This is the single most important decision of the quarter. Do it carefully. |
| 1.15 | Set up `lap_backend` FastAPI skeleton (separate from current Flask, coexist) | backend | 1d | CC | ∥ | FastAPI + SQLModel + Alembic + Pydantic v2 + pytest. |
| 1.16 | Implement `contracts/` module with all 8 Pydantic models + validators | backend | 2d | CC | 1.14 | Must include `.model_json_schema()` export. |
| 1.17 | Set up `pydantic2ts` codegen → `lap_webapp/src/lib/api/generated/` | backend + webapp | 1d | CC | 1.16 | CI step that regenerates on every backend PR. |
| 1.18 | Set up JSON Schema export → `lap_mobile/shared-schema/` and `lap_desktop/shared-schema/` | backend | 0.5d | COD | 1.16 | Shell script + CI. |
| 1.19 | Migration tooling: Alembic setup with baseline from current schema | backend | 1d | CC | 1.15 | |
| 1.20 | Read-only FastAPI endpoint `/v2/sessions/{id}` returning new Session contract (coexists with legacy) | backend | 1d | CC | 1.16, 1.19 | Feature flag. Serves as proof of life. |
| 1.21 | Mobile: capture journal architecture design doc | mobile | 1d | CC+HUM | → 1.28 | Append-only WAL in SQLite; heartbeat every 2s; reconciliation on launch. |

### Week 3 (Nov 15–21) — Mobile Sprint 1 start + marketing extraction

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 1.22 | Extract marketing to `lap_marketing` (Astro) — fresh repo | marketing | 2d | CC | ∥ | Move `src/app/(marketing)/*`, `src/data/*` marketing content, `public/`. Set up Vercel deploy. |
| 1.23 | Redirect primary domain strategy: lap.app → marketing, app.lap.app → webapp | marketing + webapp | 0.5d | HUM | 1.22 | DNS + Vercel config. |
| 1.24 | Delete `src/app/(marketing)/*` from `lap_webapp` | webapp | 0.5d | COD | 1.22, 1.23 | |
| 1.25 | Webapp nav revamp: remove marketing links, push user to coaching-first IA | webapp | 1d | CCS | 1.24 | |
| 1.26 | Mobile: capture journal implementation — WAL writes, heartbeat | mobile | 3d | CC | 1.21 | |
| 1.27 | Mobile: startup reconciliation — detect interrupted sessions, offer recovery | mobile | 2d | CC | 1.26 | |
| 1.28 | Mobile: finalize integrity contract with explicit `corrupt_local` status | mobile | 1d | CC | 1.3 | |
| 1.29 | Mobile: persistent recording-state UI strip | mobile | 1d | COD+CD | 1.26 | "Recording locally / Finalizing / Upload pending" visible always. |
| 1.30 | Desktop: rip remaining `live_telemetry_processor` references, stub with backend-future interface | desktop | 2d | CC | 1.7 | Leaves `LiveTelemetryProcessor` as interface; implementation returns empty until M3. |
| 1.31 | Desktop: fix UI-coupled settings-save bugs (debounce, error isolation) | desktop | 1d | CCS | ∥ | |

### Week 4 (Nov 22–30) — Bundle v2 canonical + mobile upload queue design

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 1.32 | Bundle v2 schema formalization (manifest.json + parquet + checksums) | backend + desktop + mobile | 2d | CC+HUM | → all ingestion | Write the bundle spec doc. Include: manifest schema, checksum alg (SHA-256), parquet column spec, provenance fields. |
| 1.33 | Backend ingestion endpoint `/v2/sessions/upload` with Bundle v2 validation | backend | 2d | CC | 1.32 | Returns session UUID, triggers Celery processing job. |
| 1.34 | Backend: migrate one Celery task from Flask (session processing) to FastAPI+Celery | backend | 2d | CC | 1.33 | Validates the new architecture works end-to-end. |
| 1.35 | Mobile: upload queue table design (SQLite) — attempt_count, next_retry_at, last_http_code, idempotency_key | mobile | 1d | CC | → 2.X | |
| 1.36 | Mobile: automated retry worker on app launch + connectivity regain | mobile | 2d | CC | 1.35 | Background URLSession with delegate wiring. |
| 1.37 | Webapp: generate TS types from new `/v2` contracts; use in a single page as pilot | webapp | 1d | CC | 1.17 | Pick one low-stakes page — drivers/progression — as pilot. |
| 1.38 | Contract smoke test suite: backend emits model → webapp consumes → roundtrip | backend + webapp | 1d | CCS | 1.37 | CI gate. |
| 1.39 | **M1 retrospective + roadmap adjustment** | all | 0.5d | HUM | end | Decide if M2 scope holds. |

### M1 KPI checkpoints
- All P0 defects closed: **PASS/FAIL** (binary)
- CI green across all 5 repos: **target 100%**
- Mobile internal build has never lost a test session across 20 recording attempts
- At least 1 webapp page consuming backend-generated TS types
- Bundle v2 manifest validates via Pydantic
- Marketing site live at new domain, webapp still accessible at app.*

---

## MONTH 2 — Contract Rollout + Mobile Reliability Locks (Dec 1 → Dec 31, 2026)

**Theme**: Everything consumes the new contracts. Mobile ships reliability. Desktop modes architected. Backend coaching engine foundations.

**Milestone**: End of M2 — new Session API is the default for `lap_webapp`, mobile ships v2 to TestFlight, desktop has mode system architecture (no behavior yet), backend coaching engine can produce a WeaknessEpisode from a processed session.

### Week 5 (Dec 1–7)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 2.1 | Backend: migrate all session-read endpoints to `/v2` with contracts | backend | 3d | CC | 1.33 | `/v2/sessions`, `/v2/sessions/{id}`, `/v2/sessions/{id}/channels`, `/v2/sessions/compare`. Legacy `/v1` stays but marked deprecated. |
| 2.2 | Backend: session serializer module — single source of truth for public session shape | backend | 1d | CC | 2.1 | Enforces "no raw dict returns" rule from audit. |
| 2.3 | Backend: unify `sessions_v2` and `sync_upload` ingestion paths into one | backend | 2d | CC | 1.33 | Both endpoints call the same internal pipeline. |
| 2.4 | Webapp: migrate Sessions list + detail to new contracts | webapp | 3d | CC | 2.1 | Delete page-local interfaces as you go. |
| 2.5 | Webapp: migrate Compare flow to new contracts + dedupe DTO helpers | webapp | 2d | CCS | 2.1, 2.4 | |
| 2.6 | Webapp: migrate Drivers/progression page to new contracts | webapp | 2d | CCS | 2.1 | |
| 2.7 | Mobile: bundle v2 writer — replaces CSV+metadata flow | mobile | 3d | CC | 1.32 | Parquet via Apache Arrow Swift, manifest.json, checksums. |
| 2.8 | Mobile: upload queue integration — send Bundle v2 to `/v2/sessions/upload` | mobile | 2d | CC | 1.36, 2.7, 2.3 | |

### Week 6 (Dec 8–14)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 2.9 | Mobile: timestamp normalization — canonical timebase, raw source timestamps preserved as metadata | mobile | 2d | CC | ∥ | Decision: primary = device monotonic clock for sample ordering, GPS timestamp for absolute time reference, RaceBox timestamp preserved as raw. |
| 2.10 | Mobile: preflight readiness gating (track selected, GPS quality, storage, battery) | mobile | 2d | CC+CD | ∥ | Hard blocks: track, GPS. Warnings: storage, battery. |
| 2.11 | Mobile: explicit "local saved" vs "cloud confirmed" state badges on session list + detail | mobile | 1d | CD+COD | 2.8 | |
| 2.12 | Mobile: TestFlight release v0.5 — "never lose a session" | mobile | 1d | HUM | 2.8, 2.9, 2.10, 2.11 | First real external testers. |
| 2.13 | Desktop: mode system architecture design doc (Practice/Sprint/Endurance/Review) | desktop | 1d | CC+HUM | → 2.14 | Contract: ModePolicy object defines overlay defaults, coaching cadence, strategy assumptions, pit behavior per mode. |
| 2.14 | Desktop: implement ModePolicy module + mode selection UI | desktop | 3d | CC | 2.13 | Mode persists per session type. No behavior bindings yet — just the plumbing. |
| 2.15 | Desktop: bundle v2 writer to replace current finalizer output | desktop | 3d | CC | 1.32 | Shared with mobile format. |

### Week 7 (Dec 15–21)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 2.16 | Backend: coaching library — structured data source for coaching text | backend | 3d | CC+HUM | → 2.19 | YAML/JSON keyed by (weakness_subtype × driver_level). You write ~30 entries manually as MVP; AI drafts another 50 for your review. Includes `observation_template`, `likely_cause`, `action`, `drill_ref`. |
| 2.17 | Backend: detector framework in `processing/` module (braking, apex, throttle, consistency baseline) | backend | 3d | CC | 2.3 | Port existing detectors, but they produce `DetectorEvent` objects, not raw text. |
| 2.18 | Backend: WeaknessEpisode engine — takes detector events over session, matches to library, creates/updates episodes | backend | 3d | CC | 2.16, 2.17 | Confidence decay formula: `c_new = c_old * 0.85 + reinforcement * 0.15`. Recurrence increments if same subtype + same driver + within 30 days. |
| 2.19 | Backend: ActionPrescription generator v0 — rule-based, deterministic | backend | 2d | CC | 2.18 | Input: WeaknessEpisode, driver readiness. Output: drill from library matching severity + level. |
| 2.20 | Backend: `/v2/drivers/{id}/weaknesses` endpoint returning open episodes | backend | 1d | CCS | 2.18 | |
| 2.21 | Backend: `/v2/sessions/{id}/next_actions` endpoint returning prescriptions | backend | 1d | CCS | 2.19 | |
| 2.22 | Webapp: replace SessionDebrief frontend heuristic with backend `next_actions` call | webapp | 1d | CC | 2.21 | This is a direct kill of audit finding #1. |

### Week 8 (Dec 22–31) — Holiday-safe week

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 2.23 | Backend: RaceBox full UBX parser port from mobile → backend side-processing | backend | 2d | CC | ∥ | Mobile keeps parsing raw bytes locally but full UBX class decode moves server-side. |
| 2.24 | Mobile: RaceBox parser expanded to all needed UBX classes (NAV-PVT + NAV-POSLLH + ESF-MEAS + NAV-STATUS) | mobile | 3d | CC | ∥ | |
| 2.25 | Marketing: ecosystem "How LAP works" page + content rewrite | marketing | 3d | CD+CC | ∥ | Single-page explainer showing desktop+mobile+webapp+bridge. Include diagram. |
| 2.26 | Marketing: homepage positioning rewrite — "Driver OS / Garmin for drivers" narrative | marketing | 2d | CC+HUM | ∥ | Kill positioning contradictions identified in audit. |
| 2.27 | Webapp: delete `admin/race-control`, `jobs`, `exports` pages (audit kill-list) | webapp | 1d | COD | ∥ | |
| 2.28 | **M2 retrospective** | all | 0.5d | HUM | end | |

### M2 KPIs
- 100% of webapp session-related pages consume backend v2 contracts; zero page-local DTOs remain for core flows
- Mobile: 0 session losses across internal beta (target 30+ sessions captured)
- Mobile TestFlight shipped
- Backend produces at least 1 WeaknessEpisode per test session with correct category
- Desktop starts in a mode and mode persists
- At least 1 webapp user story end-to-end: open session → see backend next_action prescription

---

## MONTH 3 — Coaching Memory MVP + PUBLIC BETA (Jan 1 → Jan 31, 2027)

**Theme**: Ship the coaching layer to real users. Launch public beta.

**Milestone**: End of M3 — public beta is live, Stripe is live, at least 50 signups with at least 10 completed upload→insight flows.

### Week 9 (Jan 1–7)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 3.1 | Backend: DriverProgressSnapshot computation — runs after each processed session | backend | 3d | CC | 2.18 | 10 dimensions per doctrine (all real, no placeholder). Stores snapshot with `computed_at`. |
| 3.2 | Backend: `/v2/drivers/{id}/progression` endpoint — timeline of snapshots | backend | 1d | CCS | 3.1 | |
| 3.3 | Backend: ActionOutcome measurement — after next session with same context, evaluate success_condition | backend | 2d | CC | 2.19, 3.1 | Closes the loop. |
| 3.4 | Webapp: Driver Profile page — first-class route `/app/driver` (Strava-like) | webapp | 4d | CC+CD | 3.1, 3.2 | Sections: Overall score, dimensions radar, readiness, open weaknesses, recent prescriptions, progression chart, recent sessions. |
| 3.5 | Webapp: Recurring Weaknesses panel on Driver Profile | webapp | 2d | CC | 2.20, 3.4 | Shows open WeaknessEpisodes with confidence, recurrence count, last seen, severity. |
| 3.6 | Webapp: Next Actions panel — shows active prescriptions with due-by context | webapp | 2d | CC | 2.21, 3.4 | |

### Week 10 (Jan 8–14)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 3.7 | Desktop: live coaching via backend insights — WebSocket/SSE from `/v2/live/coaching` | desktop + backend | 3d | CC | 2.19, 1.30 | Desktop sends live telemetry samples → backend detectors → enriched CoachingInsight → desktop overlay renders. Round-trip <500ms target. |
| 3.8 | Desktop: local-only fast overlays remain (brake/throttle/speed/gear) — <100ms latency | desktop | 1d | COD | ∥ | No coaching text in these. |
| 3.9 | Desktop: mode-specific behavior bindings — Practice overlay default, Sprint overlay default, Endurance overlay default | desktop | 2d | CCS | 2.14 | Practice: coaching-heavy, Sprint: strategy-heavy, Endurance: strategy + stint mgmt. |
| 3.10 | Desktop: pit-call lifecycle state machine — **armed state only** (M6 commit: you only need armed in 6mo) | desktop | 2d | CC | 3.9 | States: idle → monitor → armed. Commit/served/deferred deferred to post-M6. |
| 3.11 | Desktop: degraded-state UX — banners when backend coaching unavailable | desktop | 1d | CD+COD | 3.7 | |
| 3.12 | Backend: DriverReadinessState computation | backend | 2d | CC | 3.1 | Inputs per doctrine: volume, quality, recency, consistency, unresolved weaknesses, familiarity. Formula: weighted sum 0..100. |
| 3.13 | Backend: Stripe integration — checkout session, subscription webhooks, plan entitlements | backend | 3d | CC | ∥ | Two plans: Racer €14.99, World-Class €24.99. 14-day trial. |

### Week 11 (Jan 15–21) — BETA LAUNCH WEEK

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 3.14 | Webapp: pricing page + Stripe checkout integration | webapp | 2d | CC | 3.13 | |
| 3.15 | Webapp: account/billing settings page | webapp | 2d | CCS | 3.13, 3.14 | |
| 3.16 | Webapp: entitlement gating across features | webapp | 2d | CC | 3.13 | Free trial users get full access for 14 days. |
| 3.17 | Marketing: public beta landing + waitlist → beta invite flow | marketing | 2d | CC+CD | ∥ | |
| 3.18 | Marketing: pricing page | marketing | 1d | CD | 3.14 | |
| 3.19 | Marketing: "How LAP works" ecosystem diagram polished | marketing | 1d | CD+HUM | 2.25 | |
| 3.20 | Onboarding flow: signup → persona selection → download desktop logger → first session walkthrough | webapp + desktop | 3d | CC+CD | 3.14 | Deep-link handoff from web to desktop auth. |
| 3.21 | End-to-end smoke test: new user signup → download → first session → see coaching insight | all | 1d | HUM+CC | all above | GATE for beta launch. Must pass unattended. |
| 3.22 | **PUBLIC BETA LAUNCH** — Jan 20 ± 2 days | all | HUM | 3.21 | Announce on relevant sim-racing forums, r/simracing, Discord, your contacts at racing schools. |

### Week 12 (Jan 22–31)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 3.23 | Beta feedback triage — daily review, priority defect log | all | 0.5d/day | HUM | after 3.22 | First 10 days of beta. |
| 3.24 | Mobile: submit to App Store (public release, post-TestFlight) | mobile | 2d | CC+HUM | 2.12 + beta feedback | |
| 3.25 | Backend: observability — Sentry for errors, basic Prometheus metrics (upload success rate, processing latency, coaching generation success rate) | backend | 2d | CC | ∥ | |
| 3.26 | Backend: iRacing session calendar fetcher — Celery beat job, populates `event_calendar` table | backend | 2d | CC | ∥ | Weekly/seasonal calendars. Used for event-prep plan generation. |
| 3.27 | Webapp: "Upcoming events" section on Driver Profile | webapp | 1d | CCS | 3.26 | |
| 3.28 | **M3 retrospective** | all | 0.5d | HUM | | |

### M3 KPIs
- Public beta live: binary
- **≥50 signups** in first 10 days post-launch
- **≥10 beta users** complete upload → receive coaching insight unattended
- Stripe checkout flow converts at least 1 trial → paid
- D7 activation (upload → see insight): **≥40%** of signups
- Zero mobile session losses reported in beta
- Upload → insight latency p95: **<5 min**
- At least 3 WeaknessEpisodes generated per test user
- App Store approval: binary

---

## MONTH 4 — Sim↔Real Bridge + Strategy (Feb 1 → Feb 28, 2027)

**Theme**: Ship the differentiator. Bridge sim and real. Add strategy execution tracking. Start Android.

**Milestone**: End of M4 — TransferLink objects exist, unified driver timeline shows sim + real in one feed, saved comparisons are durable artifacts, Android alpha in internal testing.

### Week 13 (Feb 1–7)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 4.1 | Backend: Track catalog with sim↔real analogs (manual curated + physics similarity score) | backend | 3d | CC+HUM | → 4.2 | You manually seed the top 20 real tracks with their sim analogs (e.g., Barcelona real ↔ Barcelona iRacing ↔ Barcelona ACC). Physics score: turn count + sector lengths + elevation similarity. |
| 4.2 | Backend: Vehicle catalog with sim↔real analogs | backend | 2d | CC+HUM | → 4.3 | Same approach. |
| 4.3 | Backend: TransferLink engine — auto-suggest links based on track+vehicle analog confidence ≥0.7 | backend | 3d | CC | 4.1, 4.2 | `/v2/drivers/{id}/bridge/suggestions` returns candidate sim↔real pairs. |
| 4.4 | Backend: TransferDiagnostics — shape vs intensity math per channel (brake, throttle, steering, speed) | backend | 3d | CC | 4.3 | Shape = normalized curve correlation. Intensity = absolute magnitude delta. Output: per-channel `shape_match: 0..1`, `intensity_delta: float`. |
| 4.5 | Webapp: Bridge page — `/app/bridge` — shows suggested links + manual link action | webapp | 3d | CD+CC | 4.3 | |

### Week 14 (Feb 8–14)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 4.6 | Webapp: Transfer diagnostics view — per-link detailed breakdown | webapp | 3d | CC | 4.4, 4.5 | Per-corner shape match %, intensity delta chart, textual summary from library. |
| 4.7 | Webapp: Unified Driver Timeline on Profile page — chronological sim + real + bridge pairs | webapp | 3d | CC+CD | 3.4, 4.3 | Visual distinction between sim cards and real cards. Bridge pairs shown connected. |
| 4.8 | Backend: saved comparison artifacts — `ComparisonCase` object (persistent, named, with rationale + outcome) | backend | 2d | CC | ∥ | Replaces URL-param ephemeral compare. |
| 4.9 | Webapp: saved comparisons UI — "Save this compare", list of saved cases, attach to WeaknessEpisode | webapp | 2d | CC | 4.8 | |
| 4.10 | Backend: strategy plan persistence — `StrategyPlan` object stored as part of bundle | backend + desktop | 2d | CC | ∥ | Pre-race plan snapshot, live recalc events, actual pit events. |
| 4.11 | Desktop: strategy plan capture — record pre-race plan, live adjustments, pit events | desktop | 3d | CC | 4.10 | |

### Week 15 (Feb 15–21)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 4.12 | Webapp: Plan vs Actual review page for race sessions | webapp | 3d | CC+CD | 4.10, 4.11 | Side-by-side: planned stints vs executed stints, pit windows plan vs actual, delta analysis. |
| 4.13 | Desktop: Endurance mode — stint block UI, long-run consistency overlay, variance buffer display | desktop | 3d | CC+CD | 2.14, 3.9 | |
| 4.14 | Desktop: Sprint mode polish — race-critical overlays only, reduce streamer widget default exposure | desktop | 2d | CD+COD | 3.9 | Move streamer widgets to "advanced/streaming" category behind toggle. |
| 4.15 | Mobile: Android port kickoff — Kotlin project setup, shared-schema consumption | mobile (android) | 4d | CC | ∥ | |
| 4.16 | Mobile: Android capture MVP — phone GPS/IMU mode | mobile (android) | 3d | CC | 4.15 | No RaceBox yet; GPS+IMU only for alpha. |

### Week 16 (Feb 22–28)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 4.17 | Backend: EventPerformancePrediction v0 — per driver, for upcoming target event | backend | 3d | CC | 3.26, 3.1 | Bounded prediction: expected pace band, consistency band. Inputs: DriverProgressSnapshot + event track/vehicle familiarity. Rule-based, not ML. |
| 4.18 | Webapp: "Target Event" feature — user selects upcoming event, sees prediction + readiness + tailored plan | webapp | 3d | CC+CD | 4.17 | |
| 4.19 | Backend: benchmark per car-track — driver's historical bests vs their own baseline | backend | 2d | CC | ∥ | No cross-user data (per your answer). Just self-benchmark. |
| 4.20 | Marketing: case study content — first 3 beta users with measurable improvement | marketing | 2d | HUM+CC | ∥ | Interview + data pull. |
| 4.21 | Marketing: sim title integration page | marketing | 1d | CD+CC | ∥ | |
| 4.22 | Desktop: adapter additions — AMS2, rF2, LMU (you already have iRacing, ACC; AC and Rennsport land M5; F1 last) | desktop | 4d | CC | ∥ | Priority: AMS2 > LMU > rF2. |
| 4.23 | **M4 retrospective** | all | 0.5d | HUM | | |

### M4 KPIs
- ≥3 beta users have created at least 1 TransferLink pair (manual or accepted auto-suggest)
- Bridge page loads transfer diagnostics for a test pair in <3s
- Unified Driver Timeline shows sim + real in same feed
- Saved comparison cases: at least 5 created across beta users
- Paid users: **≥20**
- MRR: **≥€300**
- Android alpha: binary (yes/no shipped internally)
- New adapters landed: AMS2, LMU, rF2 (3 of 3)

---

## MONTH 5 — FULL RELEASE (Mar 1 → Mar 31, 2027)

**Theme**: Polish, launch, monetize. All coaching objects shipping. Full sim title coverage. Full release public.

**Milestone**: End of M5 — full paid release live, Stripe production-grade, all 7 canonical backend objects visible in UI, ≥100 paid users.

### Week 17 (Mar 1–7)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 5.1 | Backend: DriverBenchmarkProfile — self-percentile over time per dimension | backend | 3d | CC | 3.1 | No cross-user. Own-trend percentile bands. |
| 5.2 | Webapp: Benchmark view on Driver Profile | webapp | 2d | CC+CD | 5.1 | |
| 5.3 | Backend: coaching library expansion — grow from 30 → 200 entries covering all WeaknessCategory × subtype × level | backend | 4d | CC+HUM | ∥ | You sign off on quality; CC drafts and you edit. |
| 5.4 | Webapp: coaching text level auto-selection based on driver experience (platform tenure + completed prescriptions) | webapp + backend | 2d | CC | 5.3 | |
| 5.5 | Desktop: adapter additions — AC, Rennsport | desktop | 3d | CC | ∥ | |

### Week 18 (Mar 8–14)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 5.6 | Webapp: Development Plan view — user-targeted multi-week training plan | webapp | 3d | CC+CD | 3.1, 4.17 | Composed of ActionPrescriptions scheduled over days/sessions. |
| 5.7 | Backend: plan generator — given driver readiness + open weaknesses + target event, produce scheduled plan | backend | 3d | CC | 3.12, 4.17 | Deterministic rules engine. |
| 5.8 | Webapp: prescription completion tracking UI | webapp | 2d | CCS | 3.3 | User marks drill as done → outcome evaluation on next session. |
| 5.9 | Desktop: adapter — F1 game (last) | desktop | 2d | CC | ∥ | |
| 5.10 | Mobile iOS: final pre-release polish, App Store screenshots, release notes | mobile | 2d | HUM+CD | ∥ | |
| 5.11 | Mobile Android: beta release via Play Internal Testing | mobile (android) | 1d | HUM | 4.16 | |

### Week 19 (Mar 15–21) — FULL RELEASE WEEK

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 5.12 | Full E2E regression: every persona's first-week journey | all | 2d | HUM+CC | all | Sim-only, real-only, dual. Every platform. |
| 5.13 | Performance audit: webapp LCP/TTI, backend p95 endpoints, mobile startup | all | 1d | CC | ∥ | |
| 5.14 | Marketing: launch announcement content — homepage refresh, blog post, social | marketing | 2d | CC+CD | ∥ | |
| 5.15 | Marketing: affiliate/referral tracking setup (Plausible goals, Stripe referral codes) | marketing + backend | 1d | CC | ∥ | |
| 5.16 | Marketing: partnerships outreach — racing schools (Almeida Racing Academy), sim racing Discords, content creators | marketing | 2d | HUM | ∥ | Open-door B2B angle. |
| 5.17 | Observability: dashboards for every KPI in Section 7 | backend | 2d | CC | ∥ | Grafana or equivalent. |
| 5.18 | **FULL PUBLIC RELEASE** — Mar 17 ± 3 days | all | HUM | 5.12 | Announce broadly. Close public beta branding. |

### Week 20 (Mar 22–31)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 5.19 | Post-release defect triage, daily | all | 0.5d/day | HUM | | |
| 5.20 | Onboarding optimization based on activation funnel data | webapp + marketing | 2d | CC | 5.17, 5.18 | Iterate on signup → first insight friction. |
| 5.21 | Support: set up docs, FAQ, Intercom or Crisp widget | marketing + webapp | 1d | CC+HUM | ∥ | |
| 5.22 | Pricing experimentation: A/B test free trial length (7d vs 14d vs 30d) | backend + marketing | 1d | CC | 5.17 | |
| 5.23 | **M5 retrospective** | all | 0.5d | HUM | | |

### M5 KPIs
- **Full release live**: binary
- **Paid users: ≥100**
- **MRR: ≥€1500**
- D7 retention: ≥30%
- D30 retention: ≥15%
- All 8 sim titles have adapters shipping and tested
- Time-to-first-value (signup → first insight): ≤15 min median
- Mobile session loss rate: <0.5%
- Upload success rate p95: ≥99%

---

## MONTH 6 — Iterate + Door-Opening (Apr 1 → Apr 30, 2027)

**Theme**: Learn from real users, sharpen what works, prepare the next chapter. Apple Watch companion. Android public. B2B open-door.

**Milestone**: End of M6 — ≥500 paid users, ≥€5k MRR, data-driven product improvements shipped, racing school pilot conversation started.

### Week 21 (Apr 1–7)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 6.1 | Data-driven week: pull every KPI dashboard, rank top 3 bottlenecks | all | 1d | HUM+CR | | |
| 6.2 | Ship fix for bottleneck #1 (TBD based on data) | all | 3d | CC | 6.1 | |
| 6.3 | Ship fix for bottleneck #2 | all | 2d | CC | 6.1 | |
| 6.4 | Ship fix for bottleneck #3 | all | 2d | CC | 6.1 | |

### Week 22 (Apr 8–14)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 6.5 | Apple Watch companion MVP — HR + wrist IMU (steering proxy) | mobile | 5d | CC+CD | 5.10 | Streams to iPhone app during session. |
| 6.6 | Android public release on Play Store | mobile | 2d | HUM+CC | 5.11 | Following feedback loop from internal testing. |
| 6.7 | Backend: HR + wrist IMU ingestion + "driver effort" auxiliary metric | backend | 2d | CC | 6.5 | Optional channel; doesn't block core analysis. |

### Week 23 (Apr 15–21)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 6.8 | B2B pilot kit: pitch deck, case studies, partnership proposal template | marketing | 3d | CC+CD+HUM | ∥ | For racing schools and academies. Open-door mode. |
| 6.9 | B2B outreach: first 5 conversations with racing school decision-makers | marketing | 3d | HUM | 6.8 | |
| 6.10 | Coaching library: expand to cover endurance-specific weaknesses + stint management + tire preservation patterns | backend | 3d | CC+HUM | 5.3 | |
| 6.11 | Webapp: coach-target feature — users set their own coaching targets for coach-target comparison baseline | webapp + backend | 2d | CC | ∥ | Per your answer to Q88. |

### Week 24 (Apr 22–30)

| # | Task | Repo | Effort | AI | Blocks | Notes |
|---|---|---|---|---|---|---|
| 6.12 | Prediction feedback loop — compare EventPerformancePrediction to actual outcomes, calibrate | backend | 2d | CC | 4.17 | Store calibration data; don't retrain anything, just measure. |
| 6.13 | Webapp: Predicted vs Actual event review | webapp | 2d | CC+CD | 6.12 | |
| 6.14 | Content marketing: weekly SEO content schedule (published, not just drafted) | marketing | 2d | CC+HUM | ∥ | Beginner content per Q39 answer (racing line, wet line, terminology). |
| 6.15 | Final M6 retrospective + M7-M12 strategy kickoff doc | all | 1d | HUM+CR | | Hand off to next planning cycle. |

### M6 KPIs (end of roadmap)
- **Paid users: ≥500** (stretch 1000)
- **MRR: ≥€5k** (stretch €10k)
- D30 retention: ≥20%
- Apple Watch companion: live in App Store
- Android: live on Play Store
- ≥3 B2B conversations with racing schools
- ≥20 WeaknessEpisodes auto-resolved by ActionOutcomes (closed coaching loop working)
- ≥10 TransferLink pairs analyzed across user base
- NPS: ≥40 (or equivalent satisfaction proxy)
- Prediction calibration data captured for ≥30 events

---

## 6. Cross-Cutting Task Streams (parallel to monthly work)

### Continuous — every month
- **Tests**: every new feature PR requires tests. Floor: backend 70% line coverage, webapp critical paths E2E green.
- **Documentation**: internal architecture docs updated on every contract change. User-facing docs grow with feature releases.
- **Observability**: new metrics added as new features ship. Never ship a feature without a KPI attached.
- **Security**: Supabase RLS audited monthly. Stripe PCI compliance verified.
- **Backup**: Postgres nightly backup + 30-day retention by M2.

### Quarterly
- **Retention cohort analysis** end of M3 and M6
- **Pricing A/B tests** launched M5 Week 20
- **User interviews**: start M3 Week 11, target 5 interviews/month (Q44 — yes, you'll invest to make it go)

---

## 7. KPI Dashboard

### Product KPIs (weekly review)

| KPI | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| Signups | — | internal | 50+ | 150 | 500 | 1500 |
| Paid users | 0 | 0 | 3 | 20 | 100 | 500 |
| MRR (€) | 0 | 0 | ~50 | 300 | 1500 | 5000 |
| D7 activation | — | — | 40% | 45% | 50% | 55% |
| D30 retention | — | — | — | 20% | 15% | 20% |
| Upload success p95 | — | 95% | 98% | 99% | 99% | 99.5% |
| Time-to-first-insight (median) | — | — | 30min | 20min | 15min | 10min |
| WeaknessEpisodes generated/user/week | — | — | 2 | 3 | 4 | 5 |
| Prescription efficacy (% improvement on next matching session) | — | — | baseline | 25% | 35% | 45% |
| TransferLinks created/user | — | — | — | 0.5 | 1.0 | 1.5 |

### Engineering health KPIs (weekly review)

| KPI | Target | Hard ceiling/floor |
|---|---|---|
| CI green rate | 100% | <95% = pause feature work |
| Backend p95 endpoint latency | <300ms | >1s = incident |
| Mobile session-loss rate | 0% | >0.5% = stop-the-world |
| Production error rate | <0.5% | >2% = incident |
| Test coverage (backend) | 70%+ | <60% = block PR |
| Time from PR open → main merge | <24h | >72h = process review |

### Reliability KPIs (continuous)
- Mobile: 0 session losses across 30+ captures between releases
- Desktop: 0 crashes during race session across beta users for 2 consecutive weeks
- Backend: uptime 99.5% minimum

---

## 8. Weekly Cadence

### Monday (1h) — Week planning
- Review last week's KPIs vs targets
- Check M-level milestone trajectory
- Decide the week's P1 deliverable (ONE thing that must ship this week)
- Any P0 defects? Triage first

### Wednesday (30min) — Mid-week check
- Is the P1 on track? If no, cut scope now, not Friday.

### Friday (1h) — Shipping day + retro
- What shipped?
- What slipped? Why?
- Any contract/architecture decisions to sign off before Monday?
- Update roadmap doc

### Pivot triggers (force a roadmap rewrite)
- MRR at M3 end <€100 → revisit pricing / persona
- Paid conversion <2% of activations at M5 → pause feature work, dig into conversion
- Mobile session loss rate >1% at any point → stop-the-world, everything pauses until fixed
- Any P0 defect that can't be fixed within 48h → call in outside help

---

## 9. Risk Register

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Solo dev burnout | Catastrophic | Medium-High | 10 off-days in August pre-booked; hard weekly hour ceiling; one "off" weekend per month minimum |
| Backend migration drags past M2 | High | Medium | Feature flag approach; v1 and v2 coexist; don't flip users until v2 is verified |
| Coaching library quality (you writing 200 entries by hand) | High | High | Accept that draft quality from AI is starting point; commit to 1 dedicated library-writing day per week in M2-M5 |
| TransferLink diagnostics produce garbage | High for positioning | Medium | Ship with strong confidence gating; hide low-confidence links from UI; manual-link always available as fallback |
| Sim adapter maintenance burden | Medium | High | Adapters kept minimal; clear deprecation policy if a title breaks after an update |
| Stripe/billing bug costs money | Medium | Low | Extensive test mode use; Stripe webhooks idempotent; nightly reconciliation report |
| Apple Watch companion slips | Low | Medium | Explicitly stretch goal; fine if it lands M7 |
| Android port quality gap | Medium | Medium | Ship Android as beta only through M6 end; don't over-promise feature parity |
| Ship-or-die runway pressure causes scope explosion | High | High | **Weekly Friday scope review is non-negotiable**; the 10 explicit non-goals (§0) must stay dead |
| Claude Code / Codex credit burn exceeds budget | Low | Medium | €400/mo cap. Monitor weekly. If burn rate too high, shift tasks to CCS or cheaper tiers. |
| Live coaching WebSocket latency > target | Medium | Medium | Fall back to polling at 2s interval; accept degraded UX rather than kill feature |
| Coaching library "premium tone" inconsistency | Medium | High | Write tone guide first (M2); have Claude draft, you edit 100%; no shipping draft-quality text to users |

---

## 10. Explicit Kill List (audit work NOT being done — defer or delete)

From the audits, the following are **explicitly deferred past M6**:

1. **Fully autonomous AI coach** — deferred indefinitely per your answers
2. **LLM-generated coaching prose** — deferred indefinitely (doctrine)
3. **ML-based weakness detection with labeled datasets** — deferred per your "dataset label work" concern
4. **Social features** (leaderboards, friends, sharing) — deferred per audits + your answers
5. **Live multi-car telemetry streaming to web** — deferred
6. **Team/B2B admin UI** — beyond stub, deferred to M7+ per Q91
7. **Cross-user data compute** — explicitly no per Q90
8. **Strategy pit-call commit/served/deferred states** — only `armed` ships in M3 per Q97; rest is M7+
9. **Endurance-specific driver swap workflow** — audit mentions; deferred
10. **Visual redesign of webapp beyond coaching-first IA** — deferred until M6 data justifies
11. **Mac desktop build** — Windows-only for M6
12. **Self-hosted/enterprise deployment** — indefinite defer
13. **Mandarin/Japanese/Korean i18n** — indefinite defer
14. **Predictive ML event models** — deferred; EventPerformancePrediction is rule-based only in M6
15. **Real-time collaboration on session** — deferred
16. **User-generated coaching content / community library** — deferred

---

## 11. First 7 Days — Your Actual Monday

If you start this roadmap Nov 1, here's your literal first-7-days checklist:

**Day 1 (Mon)**
- [ ] Read this whole doc, flag any decision you reject
- [ ] Open 5 Claude Code sessions in parallel: 1 per repo
- [ ] Mobile: Fix force-unwraps (tasks 1.1, 1.2) — CC
- [ ] Webapp: Fix `/api/v1` double-prefix (1.9) — COD
- [ ] Desktop: Audit `live_telemetry_processor` imports (1.6) — CC

**Day 2 (Tue)**
- [ ] Mobile: `finalizeSession` integrity contract (1.3) — CC
- [ ] Mobile: `fullScreenCover` stop bug (1.4) — COD
- [ ] Desktop: Decide and execute rip of `live_telemetry_processor` (1.7) — CC
- [ ] Webapp: Delete duplicate bundle types (1.11), fix duplicate channels route (1.10) — CC+COD

**Day 3 (Wed)**
- [ ] Desktop: QML bootstrap test fix (1.8) — CC
- [ ] Mobile: RaceBox recording-state guard (1.5) — COD
- [ ] Webapp: Update stale E2E specs (1.12) — CCS
- [ ] Start drafting Pydantic contracts for §3 of this doc (1.14) — HUM+CC

**Day 4 (Thu)**
- [ ] Continue Pydantic contract drafting — you must sign off personally (1.14)
- [ ] Set up `lap_backend` FastAPI skeleton (1.15) — CC

**Day 5 (Fri)**
- [ ] Merge and verify all Week 1 P0 fixes (1.13)
- [ ] CI green check across all 5 repos
- [ ] **Week 1 retro**: what slipped? Adjust Week 2 scope

**Weekend: rest**. You cannot ship 24 weeks if you burn week 1.

**Day 6-7 (Mon-Tue of Week 2)** — transitions into the Week 2 task block above.

---

## 12. Appendix — Key Architectural Diagrams (you should draw these for real)

### A. Data flow: Session upload → coaching insight rendered

```
Mobile/Desktop → [Bundle v2] → FastAPI /v2/sessions/upload → 
    Validation → Canonical transform → Store → 
    Celery enqueue: processing.run_session(session_id) →
    Detectors emit events → Coaching engine matches library →
    WeaknessEpisode upsert + ActionPrescription generation →
    DriverProgressSnapshot recompute →
    Webhook → webapp subscribes → renders
```

### B. Coaching library structure (YAML per entry)

```yaml
- id: brake_release_choppy
  category: TECHNIQUE
  subtype: brake_release_choppy
  detector_ref: choppy_brake_release_detector_v1
  confidence_floor: 0.6
  variants:
    beginner:
      observation: "You're releasing the brake in sharp steps instead of smoothly."
      likely_cause: "Gripping the pedal too hard or lifting in bursts."
      action: "Practice slow, gradual pressure release. Think: 'pour the brake out, don't dump it.'"
      drill_ref: brake_release_smoothing_drill_01
    intermediate:
      observation: "Brake release curve shows visible steps across 6 of 10 laps (see trace)."
      likely_cause: "Possible pedal load modulation issue, or residual tension at peak brake."
      action: "Target a continuous release curve over 0.4s from peak to off."
      drill_ref: trail_brake_continuity_drill_02
    advanced:
      observation: "Release gradient variance 18% vs optimal (see Turn 3 overlay)."
      likely_cause: "Inconsistent trail-off into apex, possibly compensating for late turn-in."
      action: "Benchmark against your best Turn 3 trace; target <8% variance over 5 laps."
      drill_ref: trail_brake_consistency_elite_03
  measurable_target:
    metric: brake_release_gradient_variance
    beginner_threshold: 0.15
    intermediate_threshold: 0.10
    advanced_threshold: 0.08
    window: 5_laps
```

### C. Repo deploy topology

```
lap_marketing    → Vercel (edge, static)      → lap.app
lap_webapp       → Vercel                     → app.lap.app
lap_backend      → Fly.io or Railway (Docker) → api.lap.app
  + Celery workers (same host or separate)
  + Postgres (managed, e.g. Neon or Supabase)
  + Redis (managed, e.g. Upstash)
lap_desktop      → GitHub Releases + auto-updater (Sparkle/winsparkle equivalent)
lap_mobile iOS   → App Store
lap_mobile Android → Play Store
```

---

## 13. How to use this doc

1. **Read it once end-to-end, flag rejections** — you have veto on any locked decision (§1). Reject now, before execution.
2. **Pin §11 (First 7 Days) somewhere visible** — that's literally Monday morning.
3. **Every Friday, update the doc** — retrospective notes, slipped tasks moved, scope adjustments.
4. **Every month end, write a 1-page "what actually happened" addendum** — compare to the monthly milestone gate.
5. **When in doubt about scope, check §10 (Kill List)** — the non-goals are there to protect you.
6. **When in doubt about AI tool choice, check §4** — CC for architectural, COD for single-file, HUM for taste.
7. **When things are on fire, §9 (Risk Register) has your mitigation scripts** — pre-decided, don't re-decide under pressure.

---

**Last revision**: 2026-04-23 (initial draft)
**Next scheduled revision**: End of Week 1 (2026-11-07) — post-P0-fixes retrospective
