# LAP Desktop — 30-Day Sprint Queue

**Repo:** `datalogger/` (= `lap-coach-logger`).
**Stack:** Python 3.12, PyQt6 / QML 6, pyirsdk, ACC shared-mem, Pydantic v2, PyInstaller, Inno Setup.
**Total:** 240 tasks. Same /loop rules as sprint-backend.md.

---

## Block A — P0 fixes + CI unblock (T001–T020)

- [x] T001 [opus] Audit `live_telemetry_processor.py` imports, list every missing module reference ⇒ doc comment (4cd3623)
- [x] T002 [opus] Define `LiveProcessor` ABC in `core/live_processor.py` with slots (on_sample, on_lap_end, on_session_end) ⇒ ABC importable (eb97496)
- [x] T003 [opus] Rebuild `CoachingLiveProcessor` using existing `live_detectors.py` primitives ⇒ no external missing imports (f3c1cc7)
- [x] T004 [opus] Rebuild `DashboardLiveProcessor` exposing normalized snapshots ⇒ consumable by VM (fa8ec3e)
- [x] T005 [opus] Rebuild `InputDiagnosticsProcessor` for input telemetry surfacing ⇒ compiles (6690165)
- [x] T006 [sonnet] Update `live_telemetry_processor.py` to compose the three Processors via the ABC ⇒ no missing imports (64893ec)
- [x] T007 [sonnet] Feature flag `LIVE_COACHING_ENABLED` to disable live coaching if needed ⇒ env-driven (c36b134)
- [x] T008 [sonnet] Smoke test: run main with sim-disconnected → app boots without crash ⇒ green (b6754ee)
- [x] T009 [sonnet] Smoke test: run main with iRacing mock → live processor runs ⇒ green (8343002)
- [x] T010 [sonnet] Fix `tests/test_qml_bootstrap.py` TypeError (property collision) ⇒ collection green (ed9b004)
- [x] T011 [sonnet] Add regression test: import all VM classes via bootstrap ⇒ green (cdfd017)
- [x] T012 [sonnet] Add regression test: import all processor classes ⇒ green (934bcd5)
- [x] T013 [codex] `pyproject.toml`: upgrade to Python 3.12, pin deps ⇒ `uv sync` clean (323fe7f)
- [x] T014 [codex] `.pre-commit-config.yaml`: ruff + mypy + pytest on staged ⇒ installed (b76bdbd)
- [x] T015 [codex] GitHub Action: `pytest -q` blocks merge ⇒ workflow green (a2d40a2)
- [x] T016 [codex] GitHub Action: ruff + mypy block merge ⇒ workflow green (b49d989)
- [x] T017 [sonnet] Migrate `session_state.py` to typed enum + state machine lib (transitions) ⇒ tests green (76d39dc)
- [x] T018 [sonnet] Migrate `SessionCoordinator` to use `logging.getLogger(__name__)` throughout ⇒ consistent (7fa3933)
- [x] T019 [sonnet] Remove `launch_stderr.log` + `launch_stdout.log` committed noise files ⇒ .gitignore updated (e02fc36)
- [x] T020 [sonnet] Clean up `=1.26` weird root file (looks like a pip pin leak) ⇒ gone (bb2a36f)

## Block B — Contract + schema integration (T021–T040)

- [x] T021 [sonnet] Install `@lap/schemas` Python package as dep ⇒ `from lap_schemas.v1 import SessionManifest` works (ff57d65)
- [x] T022 [sonnet] Replace local `SessionMetadata` dataclass with `SessionManifest` ⇒ compiles (b78fdb5)
- [x] T023 [sonnet] Replace local `BundleSchema` with shared types ⇒ compiles (4f26585)
- [x] T024 [sonnet] Audit all duplicate Pydantic models in desktop, remove ⇒ ≥5 removals (a1de554)
- [x] T025 [opus] `SessionFinalizer` rewrite step 1: accept `SessionManifest` instead of ad-hoc dict ⇒ tests green (8c91bf2)
- [x] T026 [opus] `SessionFinalizer` step 2: write manifest.json in Bundle v2 format ⇒ format matches spec (a7d327f)
- [x] T027 [opus] `SessionFinalizer` step 3: write telemetry as parquet (pyarrow) or CSV fallback ⇒ file present (7a37169)
- [x] T028 [opus] `SessionFinalizer` step 4: write laps.parquet with LapRecord shape ⇒ round-trip valid (c4cd898)
- [x] T029 [opus] `SessionFinalizer` step 5: write events.json (sector/lap/flag events) ⇒ valid JSON (07329a9)
- [x] T030 [opus] `SessionFinalizer` step 6: compute sha256 per file, write manifest checksums ⇒ match on re-read (9bb1227)
- [x] T031 [opus] `SessionFinalizer` step 7: atomic temp→final rename retained ⇒ no partial bundles (dff270c)
- [x] T032 [sonnet] `SessionFinalizer` step 8: write `SensorConfigSnapshot` with adapter info ⇒ populated (b248656)
- [x] T033 [sonnet] `SessionFinalizer` step 9: write `DataQuality` score with all sub-metrics ⇒ populated (22de27d)
- [x] T034 [sonnet] `SessionFinalizer` step 10: timestamps include both t_source_ns + t_canonical_ns per ADR-007 ⇒ tested (3fdc300)
- [BLOCKED: backend ingestion endpoint not live — cannot validate manifest server-side] T035 [sonnet] Integration test: finalize an archived Sebring session → manifest validates server-side ⇒ green
- [x] T036 [sonnet] Integration test: finalize with CSV fallback (no pyarrow) ⇒ works (f0f2855)
- [x] T037 [sonnet] Integration test: interrupted finalize doesn't corrupt prior bundles ⇒ green (a146064)
- [x] T038 [sonnet] Backward compat shim: read old v1 bundles, re-serialize as v2 on demand ⇒ reprocess path works (7e2cde5)
- [x] T039 [sonnet] Update `bundle_schema.py` to emit v2-only ⇒ v1 writer removed (ea4b34a)
- [x] T040 [sonnet] Update `writers/*` to use canonical field names ⇒ consistency (c59dc8e)

## Block C — Upload client to new ingest endpoint (T041–T055)

- [x] T041 [opus] Replace current upload module with new `IngestClient` in `infra/ingest.py` ⇒ typed (be38dbe)
- [x] T042 [opus] `IngestClient.upload(manifest, artifacts)` returns `ingest_job_id` ⇒ tested against mock server (5a979d8)
- [x] T043 [opus] `Idempotency-Key` = session UUIDv7, added to headers ⇒ tested (a6a40c7)
- [x] T044 [opus] Chunk streaming: upload telemetry file in 5MB chunks ⇒ works (864e1c7)
- [x] T045 [opus] Resume-on-interrupt: chunk cursor persisted, resumes from last ⇒ tested (a241f86)
- [x] T046 [sonnet] SSE consumer: poll `/jobs/:id/events` for progress ⇒ emits Qt signal (4c12d18)
- [x] T047 [sonnet] Progress dial on Finalize/Upload screen reflects SSE ⇒ visible (df3d548)
- [x] T048 [sonnet] Network failure handling: retry with exponential backoff ⇒ works (4ffb380)
- [x] T049 [sonnet] Auth token refresh: Clerk token refresh on 401 ⇒ silent (a1456f5)
- [x] T050 [sonnet] Auth token storage: OS keychain via `keyring` library ⇒ secure (53b81f5)
- [x] T051 [sonnet] Pairing flow: scan QR (camera or manual entry) → redeem → store tokens ⇒ works (d26edf9)
- [x] T052 [sonnet] "Not paired" empty state in UI with CTA to open webapp for pairing QR ⇒ visible (bf98715)
- [x] T053 [sonnet] Multi-account support: not needed in M1, scaffolded for later ⇒ single-account works (f07154d)
- [x] T054 [sonnet] Unit test: IngestClient happy path, 4xx, 5xx, network error ⇒ all paths (2e2c0e0)
- [x] T055 [sonnet] Integration test: end-to-end capture → finalize → upload → server confirms ⇒ green (0289e38)

## Block D — Observability (T056–T065)

- [x] T056 [sonnet] Sentry Python SDK integrated in bootstrap ⇒ 500 error reports (d524fc1)
- [x] T057 [sonnet] Sentry Qt integration: capture QML errors ⇒ QML throws appear in Sentry (e87fee7)
- [x] T058 [sonnet] Sentry release tagging from version.py ⇒ tagged (b97fc67)
- [x] T059 [sonnet] PostHog Python SDK integrated ⇒ ready (e610084)
- [x] T060 [sonnet] PostHog event: `desktop_app_started` ⇒ visible (44c9e57)
- [x] T061 [sonnet] PostHog event: `session_captured` with sim/track/car props ⇒ visible (c22bea7)
- [x] T062 [sonnet] PostHog event: `overlay_toggled` with widget id ⇒ visible (bb1a132)
- [x] T063 [sonnet] PostHog event: `mode_switched` (after mode engine ships) ⇒ stub in place (357348b)
- [x] T064 [sonnet] PostHog event: `coaching_insight_viewed` ⇒ stub (ab058b1)
- [x] T065 [sonnet] Opt-out flag in Settings for telemetry collection ⇒ respected (cff051c)

## Block E — Session review placeholder cleanup (T066–T075)

- [x] T066 [sonnet] Audit review page for "to be wired later" placeholders ⇒ list in commit msg (2b4c389)
- [BLOCKED: backend reprocess endpoint not live] T067 [sonnet] Wire Re-process button → backend `/sessions/:id/reprocess` ⇒ works
- [x] T068 [sonnet] Wire Open Folder button (already works) → ensure cross-platform ⇒ tested (84a8142)
- [x] T069 [sonnet] Wire Delete button with confirm ⇒ works (aa900e0)
- [x] T070 [sonnet] Hide Export button on desktop (push user to webapp per Q95) ⇒ replaced with "View in webapp" link (29c18a5)
- [x] T071 [sonnet] Review page: show only compact summary (laps, best, consistency, DQ) ⇒ tight UI (fa625f6)
- [x] T072 [sonnet] Review page: "See full analysis in webapp" primary CTA ⇒ prominent (56095d3)
- [x] T073 [sonnet] Review page: remove deep-analysis tabs (telemetry, setup, engineering) ⇒ simpler (2c7ff6e)
- [x] T074 [sonnet] Fix field contract mismatch: `quality_grade`, `best_lap_formatted` come from loader ⇒ correct (c16fb27)
- [x] T075 [sonnet] Integration test: review page loads for archived session without errors ⇒ green (e541074)

## Block F — Rules engine client (T076–T105)

- [x] T076 [opus] Rules engine client: `coaching/rules_engine.py` loads compiled JSON bundle ⇒ parses (fdd08ec)
- [x] T077 [opus] Compiled rule bundle loader: fetch from server at login, cache to disk ⇒ works (241d19f)
- [x] T078 [opus] Cache TTL 7 days, signature-verified ⇒ tested (a2d5250)
- [x] T079 [opus] Rules engine: evaluate a rule's condition against a session-feature dict ⇒ unit-tested (d2e867c)
- [x] T080 [opus] Rules engine: run all rules over an in-progress session window ⇒ emits insights (4a7cddc)
- [x] T081 [opus] Performance: <1ms overhead per sample ⇒ benchmark passes (59d51ab)
- [x] T082 [opus] Thread safety: rules run on sample thread, insights queued to VM thread ⇒ tested (635bf9b)
- [x] T083 [sonnet] Rules engine integration: `LiveTelemetryProcessor` invokes it per lap-end ⇒ tested (64171cf)
- [x] T084 [sonnet] Test harness: inject a fake session, verify insights match expected ⇒ green (54ce8c0)
- [x] T085 [sonnet] Test: late-braking detection with fixture matching rule br.late_braking ⇒ fires (72cf11b)
- [x] T086 [sonnet] Test: early-release detection ⇒ fires (4b6e191)
- [x] T087 [sonnet] Test: apex-speed-loss detection ⇒ fires (0c052eb)
- [x] T088 [sonnet] Test: rule false-positive gating (only fires with N corroborating laps) ⇒ tested (c79dc58)
- [x] T089 [sonnet] Offline fallback: if cache expired and offline, use last-known rules + banner ⇒ tested (1f3adf0)
- [x] T090 [sonnet] Rule update check on app start: if server has newer bundle, fetch ⇒ works (dac917c)
- [x] T091 [opus] Overlay VM: `CoachingCardViewModel` consumes insight stream ⇒ QML binds (7b375c1)
- [x] T092 [opus] Overlay VM: insights queue with cooldown (no spam) ⇒ tested (d236f9a)
- [x] T093 [opus] Overlay VM: explanation variant selected by user skill level ⇒ tested (fd63841)
- [x] T094 [sonnet] QML: CoachingCard widget renders one insight at a time ⇒ visually validated (3721f9c)
- [x] T095 [sonnet] QML: CoachingCard fade in/out animation ⇒ smooth (5b44f32)
- [x] T096 [sonnet] Coaching card audio cue option (voice) ⇒ configurable (1f0b08e)
- [x] T097 [sonnet] Coaching card "dismiss" button ⇒ works (3ce9600)
- [x] T098 [sonnet] Coaching card "flag as wrong" button → POST to backend ⇒ works (93cb05a)
- [x] T099 [sonnet] Bundle serializer includes live-generated insights (tagged client-side) ⇒ tested (7ddd00a)
- [x] T100 [sonnet] Rules engine unit coverage ≥ 80% ⇒ report (9492d10) [94%]
- [x] T101 [sonnet] Rules engine load test: 1000 samples/sec sustained ⇒ no backup (9a2f8ec)
- [x] T102 [sonnet] Rules engine memory: <100MB residue during 2h session ⇒ profiled (1023098)
- [x] T103 [sonnet] Coaching view integration: disable if feature flag off ⇒ tested (e2e1f19)
- [x] T104 [sonnet] Coaching view fallback text: "insights available post-session in webapp" ⇒ correct copy (00b5c24)
- [x] T105 [sonnet] Bundle upload includes flag showing which rules fired ⇒ server can audit (34f3c75)

## Block G — Mode engine (T106–T135)

- [x] T106 [opus] `Mode` ABC in `core/modes/base.py` ⇒ compiles (6210310)
- [x] T107 [opus] `PracticeMode` subclass: verbose coaching, minimal strategy ⇒ tests (229cc0e)
- [x] T108 [opus] `SprintMode` subclass: race coaching, simplified strategy ⇒ tests (d4c603a)
- [x] T109 [opus] `EnduranceMode` subclass: long-run focus, stint awareness ⇒ tests (369d585)
- [x] T110 [opus] `ReviewMode` subclass: no live coaching, readiness guidance ⇒ tests (64f2135)
- [x] T111 [opus] `ModeEngine`: runtime mode selection + transition rules ⇒ unit-tested (da1dfdb)
- [x] T112 [opus] Mode binds overlay preset: each mode has its widget set ⇒ switching works (9237c73)
- [x] T113 [opus] Mode binds coaching cadence: verbosity per mode ⇒ tested (15d33e6)
- [x] T114 [opus] Mode binds strategy assumptions: safety margins per mode ⇒ tested (c25a1a7)
- [x] T115 [opus] Mode tagging: finalized session carries `environment_tag` ⇒ correct (f6e309a)
- [x] T116 [opus] Mode switch UI: dropdown in main toolbar ⇒ visible (9d53efc)
- [x] T117 [sonnet] Mode switch persists across app restarts ⇒ tested (ee9e589)
- [x] T118 [sonnet] Mode auto-detect from sim hint: iRacing Race session → SprintMode default ⇒ optional (4e26be3)
- [x] T119 [sonnet] Mode switch during recording: allowed but logged, mid-session tag split ⇒ handled (b9fdebf)
- [x] T120 [sonnet] Mode E2E test: switch Practice→Sprint, verify overlay changes ⇒ green (2c6ca65)
- [x] T121 [opus] Overlay preset system refactor: preset = list of widget ids + positions ⇒ tested (0af7799)
- [x] T122 [opus] "Race-minimal" preset: 8-10 core widgets (lap delta, fuel, tires, coach, position, flags, sector color, gap) ⇒ defined (ff8fabc)
- [x] T123 [opus] "Practice" preset: 12 widgets (adds inputs, g-g, live trace) ⇒ defined (db7442d)
- [x] T124 [opus] "Endurance" preset: 10 widgets (adds stint timer, tire life, long-run pace) ⇒ defined (ef0f5a6)
- [x] T125 [opus] "Streamer" preset: separate from above, 15 widgets ⇒ defined (c72a7e5)
- [x] T126 [sonnet] Default preset on first install: race-minimal ⇒ tested (10c676a)
- [x] T127 [sonnet] Preset picker in Settings ⇒ works (a106de1)
- [x] T128 [sonnet] Widget categorization in QML: "Race", "Practice", "Endurance", "Streamer", "Advanced" ⇒ tagged (fb1e813)
- [x] T129 [sonnet] Streamer widgets grouped behind "Show advanced" toggle ⇒ hidden by default (98104d2)
- [x] T130 [sonnet] Widget search in overlay manager ⇒ works (9f450ab)
- [x] T131 [sonnet] Widget preview thumbnail in manager ⇒ visible (d0c243f)
- [x] T132 [sonnet] Export preset JSON ⇒ works (0246bff)
- [x] T133 [sonnet] Import preset JSON ⇒ works (83cd3e3)
- [x] T134 [sonnet] Preset versioning ⇒ tracked (37799fe)
- [x] T135 [sonnet] E2E: install → default preset → switch to Practice mode → preset changes ⇒ green (6c3c975)

## Block H — Strategy + pit-armed (T136–T155)

- [x] T136 [opus] Refactor `core/race_strategy.py`: move logic out of OverlayViewModel ⇒ domain service (ff147d5)
- [x] T137 [opus] Strategy service: pre-race calculation API ⇒ tested (9d3e8f6)
- [x] T138 [opus] Strategy service: live recalculation API ⇒ tested (e3c2cce)
- [x] T139 [opus] Strategy service: `armed` state field ⇒ tested (f194a65)
- [x] T140 [opus] Pit-armed computation: when fuel window or tire life reaches threshold ⇒ tested (9138a1e)
- [x] T141 [sonnet] Pit-armed UI: overlay color change + pit indicator ⇒ visible (9e4f77f)
- [x] T142 [sonnet] Pit-armed audio cue ⇒ optional (c0cc85a)
- [x] T143 [sonnet] Manual arm override: user can arm/disarm ⇒ works (93d8e08)
- [x] T144 [sonnet] Strategy plan serialized into bundle per Q102 ⇒ tested (cbf7cbe)
- [x] T145 [sonnet] Actual pit events captured (sim events or user-annotated) ⇒ stored (703dac8)
- [x] T146 [sonnet] Plan-vs-actual summary in bundle ⇒ computable (27decd4)
- [x] T147 [sonnet] Strategy view in desktop review: compact summary ⇒ UI visible (f29475d)
- [x] T148 [sonnet] Strategy guidance: push/manage label based on fuel + tire ⇒ displayed (6280ee1)
- [x] T149 [opus] Divergence alerts: safety car detection (from iRacing SDK) + strategy recalc ⇒ tested (9b1b00c)
- [x] T150 [opus] Divergence alerts: FCY detection + strategy recalc ⇒ tested (1c1cb4b)
- [x] T151 [sonnet] Driver decision prompts: pit, save fuel, push, cool tires ⇒ shown (b23fbdf)
- [x] T152 [sonnet] Corner-specific prompts: "losing X at T1 — brake later" (from rules engine) ⇒ shown (31f4dc2)
- [x] T153 [sonnet] Minimal-click acknowledgment: button press on wheel-compatible input ⇒ works (f76605e)
- [x] T154 [sonnet] Test: strategy recalc with sim data ⇒ correct pit window (aa6d9fe)
- [x] T155 [sonnet] Test: armed triggers at right fuel threshold ⇒ green (27ddd81)

## Block I — Overlay polish + degraded state (T156–T175)

- [x] T156 [sonnet] Audit all 40+ widgets: each has degraded-state rendering (stale/missing data) ⇒ list complete (f977afb)
- [x] T157 [sonnet] Widget lap-delta: degraded = grayed with "—" ⇒ rendered (62d53ae)
- [x] T158 [sonnet] Widget fuel: degraded = grayed ⇒ rendered (9110c8a)
- [x] T159 [sonnet] Widget tire: degraded state ⇒ rendered (4b0a94b)
- [x] T160 [sonnet] Widget coaching card: "insights not available" banner ⇒ rendered (c4b2c63)
- [x] T161 [sonnet] Widget input: degraded = "sensor stale" ⇒ rendered (fba215b)
- [x] T162 [sonnet] Widget g-g: degraded state ⇒ rendered (2f550ac)
- [x] T163 [sonnet] Widget live trace: degraded state ⇒ rendered (35a5cef)
- [x] T164 [sonnet] Widget sector colors: degraded state ⇒ rendered (de36086)
- [ ] T165 [sonnet] Widget flags: degraded state ⇒ rendered
- [ ] T166 [sonnet] Widget position: degraded state ⇒ rendered
- [ ] T167 [sonnet] Widget gap: degraded state ⇒ rendered
- [ ] T168 [sonnet] Widget stint-timer (endurance): degraded ⇒ rendered
- [ ] T169 [sonnet] Widget tire-life: degraded ⇒ rendered
- [ ] T170 [sonnet] Widget long-run-pace: degraded ⇒ rendered
- [ ] T171 [sonnet] Global degraded banner: "coaching disabled — check backend" ⇒ visible when off
- [ ] T172 [sonnet] Global degraded banner: "offline — local only" ⇒ visible when no network
- [ ] T173 [sonnet] Settings persistence: debounce saves (save every 2s max) ⇒ tested
- [ ] T174 [sonnet] Settings persistence: rollback if save fails ⇒ user sees error
- [ ] T175 [sonnet] Settings persistence: repeated saves don't corrupt config.json ⇒ tested

## Block J — Packaging + release (T176–T200)

- [ ] T176 [sonnet] PyInstaller spec file updated for new dependencies ⇒ builds
- [ ] T177 [sonnet] PyInstaller produces single-folder distribution ⇒ folder valid
- [ ] T178 [sonnet] Inno Setup script updated for new executable ⇒ installer builds
- [ ] T179 [sonnet] Inno Setup: code signing with your cert (or self-signed for alpha) ⇒ signed
- [ ] T180 [sonnet] Inno Setup: custom install dir, desktop shortcut, start-menu entry ⇒ tested
- [ ] T181 [sonnet] Inno Setup: uninstaller cleans all files + registry entries ⇒ tested
- [ ] T182 [sonnet] Version string from single source (pyproject.toml → compile-time) ⇒ consistent
- [ ] T183 [sonnet] Release checklist: auto-generated from git log between tags ⇒ script works
- [ ] T184 [sonnet] RELEASE_CHECKLIST.md versioned ⇒ in-sync with code
- [ ] T185 [sonnet] Auto-update mechanism: check for newer version on app start ⇒ check runs
- [ ] T186 [sonnet] Auto-update: download to temp, verify signature, apply on next launch ⇒ tested
- [ ] T187 [sonnet] Auto-update: opt-out in Settings ⇒ respected
- [ ] T188 [sonnet] Auto-update: rollback if new version crashes ⇒ bail-out logic
- [ ] T189 [sonnet] Crash dump capture: minidump on crash, offer to upload ⇒ works
- [ ] T190 [sonnet] First-launch wizard: welcome, sim detection, pairing QR prompt ⇒ renders
- [ ] T191 [sonnet] First-launch: download rules bundle for offline coaching ⇒ works
- [ ] T192 [sonnet] First-launch: download track catalog for offline sector splits ⇒ works
- [ ] T193 [sonnet] License.txt packaged ⇒ visible in installer
- [ ] T194 [sonnet] Privacy.txt packaged ⇒ visible
- [ ] T195 [sonnet] Build matrix in CI: Windows 10 + 11 builds ⇒ green
- [ ] T196 [sonnet] Smoke test installer on clean Windows VM ⇒ runs
- [ ] T197 [sonnet] Uninstaller leaves no orphan files ⇒ verified
- [ ] T198 [sonnet] Documentation in docs/ folder updated for new architecture ⇒ current
- [ ] T199 [sonnet] README.md refreshed: install link, pair phone, first session ⇒ reviewed
- [ ] T200 [sonnet] CHANGELOG.md has M1 + M2 entries ⇒ written

## Block K — Tests + perf + misc (T201–T240)

- [ ] T201 [sonnet] Integration test: full Practice session from sim-start → finalize ⇒ green
- [ ] T202 [sonnet] Integration test: full Sprint session ⇒ green
- [ ] T203 [sonnet] Integration test: Endurance 30-min simulated session ⇒ green
- [ ] T204 [sonnet] Integration test: iRacing adapter happy path ⇒ green
- [ ] T205 [sonnet] Integration test: iRacing adapter sim-disconnect mid-session ⇒ finalize correctly
- [ ] T206 [sonnet] Integration test: ACC adapter happy path ⇒ green
- [ ] T207 [sonnet] Integration test: ACC adapter no-game ⇒ graceful
- [ ] T208 [sonnet] Integration test: offline mode (no network) captures + queues upload ⇒ green
- [ ] T209 [sonnet] Integration test: freeze detection trips on stalled sim ⇒ correct
- [ ] T210 [sonnet] Integration test: stale temp files cleaned on startup ⇒ green
- [ ] T211 [sonnet] Perf profile: overlay rendering at full load → CPU <15% on Ryzen 5 baseline ⇒ tested
- [ ] T212 [sonnet] Perf profile: rules engine overhead <1ms/sample ⇒ tested
- [ ] T213 [sonnet] Perf profile: memory stable over 2h session ⇒ tested
- [ ] T214 [sonnet] Perf profile: app start <3s on SSD ⇒ tested
- [ ] T215 [sonnet] UI polish: icon pack consistent ⇒ visual review passes
- [ ] T216 [sonnet] UI polish: font rendering at all supported DPIs (100%/125%/150%/200%) ⇒ looks right
- [ ] T217 [sonnet] UI polish: dark theme consistency ⇒ no artifacts
- [ ] T218 [sonnet] UI polish: high-contrast mode available ⇒ toggle works
- [ ] T219 [sonnet] Translation scaffold: English only v1, stubs for FR+ ⇒ strings extracted
- [ ] T220 [sonnet] Accessibility: keyboard-only navigation for main UI ⇒ usable
- [ ] T221 [sonnet] Accessibility: screen reader support (NVDA on Windows) tested ⇒ works
- [ ] T222 [sonnet] Settings schema migration: v1 → v2 config.json ⇒ works
- [ ] T223 [sonnet] Config backup on migration ⇒ backup file present
- [ ] T224 [sonnet] Telemetry opt-in flow during first-run ⇒ explicit
- [ ] T225 [sonnet] Analytics: session-finalization success rate metric ⇒ computed
- [ ] T226 [sonnet] Analytics: feature usage per widget ⇒ PostHog events
- [ ] T227 [sonnet] Documentation: OVERLAY_PLATFORM.md refreshed ⇒ current
- [ ] T228 [sonnet] Documentation: SESSION_LIFECYCLE.md ⇒ written
- [ ] T229 [sonnet] Documentation: COACHING_RULES.md explaining client-side execution ⇒ written
- [ ] T230 [sonnet] Documentation: TROUBLESHOOTING.md expanded ⇒ covers common issues
- [ ] T231 [sonnet] Log rotation: rotate logs at 10MB, keep last 7 ⇒ works
- [ ] T232 [sonnet] Log levels configurable via Settings ⇒ works
- [ ] T233 [sonnet] Diagnostic bundle export: zip logs + config + session list for support ⇒ works
- [ ] T234 [sonnet] Support email link in Help menu ⇒ opens mailto
- [ ] T235 [sonnet] "About" dialog shows version, build, dependencies ⇒ renders
- [ ] T236 [sonnet] Shortcut: Ctrl+Shift+R opens Restart with clean config for testing ⇒ works
- [ ] T237 [sonnet] Shortcut: F1 opens help ⇒ works
- [ ] T238 [sonnet] Shortcut: Ctrl+L clears log view ⇒ works
- [ ] T239 [sonnet] Splash screen during boot with progress ⇒ visible
- [ ] T240 [sonnet] Final smoke test on clean Win11 install: all features work ⇒ ship-ready
