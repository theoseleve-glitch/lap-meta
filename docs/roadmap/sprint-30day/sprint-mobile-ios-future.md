# LAP Mobile — 30-Day Sprint Queue

**Repo:** `lap_mobile/` (iOS Swift). Android scaffold (M5) tracked separately once this sprint is done.
**Stack:** Swift 6, iOS 17+, SwiftUI, CoreLocation, CoreMotion, CoreBluetooth, GRDB (SQLite), XcodeGen.
**Total:** 240 tasks. Same /loop rules as sprint-backend.md.

⚠️ **Mac required** for building. If /loop runs on a non-Mac host, tasks that need `xcodebuild` will error — mark them `[BLOCKED: needs-mac]` and continue to the next.

---

## Block A — P0 defect elimination (T001–T020)

- [ ] T001 [opus] Audit all `try!` in the codebase ⇒ list in commit body, count = X
- [ ] T002 [sonnet] Replace `LapCoachAppModel.live()` force-unwrap with guarded config load ⇒ unit-tested
- [ ] T003 [sonnet] Replace `StorageService() try!` with `Result<StorageService, InitError>` ⇒ tested
- [ ] T004 [sonnet] Config error screen: shown when API URL missing, CTA to contact support ⇒ SwiftUI view
- [ ] T005 [sonnet] Storage recovery screen: shown when storage init fails ⇒ SwiftUI view
- [ ] T006 [sonnet] Remove remaining `try!` in non-critical paths (logging, analytics) ⇒ count = 0
- [ ] T007 [opus] `finalizeSession` integrity check step 1: validate temp file exists ⇒ tested
- [ ] T008 [opus] `finalizeSession` integrity check step 2: validate non-empty ⇒ tested
- [ ] T009 [opus] `finalizeSession` integrity check step 3: validate CSV header present ⇒ tested
- [ ] T010 [opus] `finalizeSession` integrity check step 4: validate sample count > 0 ⇒ tested
- [ ] T011 [opus] `finalizeSession` integrity check step 5: compute sha256, store in metadata ⇒ tested
- [ ] T012 [opus] `finalizeSession` on failure: mark status `corrupt_local`, do not auto-delete ⇒ tested
- [ ] T013 [sonnet] Corrupt-local session UI: list item with recovery CTA ⇒ rendered
- [ ] T014 [sonnet] Corrupt-local recovery: user can export raw file, retry finalize, or delete ⇒ all three work
- [ ] T015 [opus] `fullScreenCover` dismissal no longer triggers stop ⇒ tested
- [ ] T016 [opus] Explicit Stop button in dashboard header ⇒ rendered
- [ ] T017 [opus] Stop button requires 0.5s hold ⇒ tested (UIGestureRecognizer)
- [ ] T018 [opus] Swipe-to-dismiss disabled during recording ⇒ tested
- [ ] T019 [sonnet] Back gesture during recording shows confirm dialog ⇒ tested
- [ ] T020 [sonnet] Stop intent event logged to journal before actually stopping ⇒ tested

## Block B — Capture journal (T021–T035)

- [ ] T021 [opus] GRDB (SQLite) setup: package added, database init in `AppStart` ⇒ connects
- [ ] T022 [opus] Schema v2: `session_journal` table (session_id, started_at, source, track_id, file_offset, sample_count, last_heartbeat) ⇒ migration applies
- [ ] T023 [opus] Migration runner: applies all migrations on boot ⇒ tested
- [ ] T024 [opus] Journal write on session start: row inserted ⇒ tested
- [ ] T025 [opus] Journal heartbeat: every 5s during recording → update `last_heartbeat` + `sample_count` + `file_offset` ⇒ tested
- [ ] T026 [opus] Journal write on session stop ⇒ row closed
- [ ] T027 [opus] Startup reconciliation step 1: find stale journal rows (no heartbeat > 60s) ⇒ listed
- [ ] T028 [opus] Startup reconciliation step 2: find orphan temp files ⇒ listed
- [ ] T029 [opus] Startup reconciliation step 3: find DB sessions stuck in `recording` or `finalizing` ⇒ listed
- [ ] T030 [opus] Startup reconciliation step 4: offer recovery UI for each finding ⇒ modal shown
- [ ] T031 [sonnet] Recovery modal: "Session from 2h ago not finalized. Recover / Discard / Export raw" ⇒ rendered
- [ ] T032 [sonnet] Recovery → Finalize-from-journal path ⇒ re-runs finalize on existing temp file
- [ ] T033 [sonnet] Journal entries older than 7 days auto-clean after user confirms loss ⇒ tested
- [ ] T034 [sonnet] Journal integrity: corrupt journal row handling ⇒ isolated, doesn't block app
- [ ] T035 [sonnet] Tests: journal round-trip, reconciliation happy path, reconciliation with orphan temp ⇒ green

## Block C — Schema integration (T036–T050)

- [ ] T036 [sonnet] Install `@lap/schemas` Swift package ⇒ imports work
- [ ] T037 [sonnet] Replace local `SessionMetadata` struct with `SessionManifest` from schemas ⇒ compiles
- [ ] T038 [sonnet] Replace local `Sample` struct with `TelemetrySample` from schemas ⇒ compiles
- [ ] T039 [sonnet] Replace local `SourceMode` enum with `SourceTag` ⇒ compiles
- [ ] T040 [sonnet] Audit all local duplicates: delete if possible ⇒ ≥3 removals
- [ ] T041 [opus] SampleModel: carry `t_source_ns` + `t_source_clock` per ADR-007 ⇒ tested
- [ ] T042 [opus] Stop doing server-side analysis on device: remove lap/statistics engine in `DataModels/SampleModel.swift` that computes summaries beyond basic display ⇒ diff clean
- [ ] T043 [opus] Remove local track-mapping / sector math (`LapTimingEngine`) beyond local-dashboard needs ⇒ tested
- [ ] T044 [opus] Remove local start/finish line detection (server does it) ⇒ diff clean
- [ ] T045 [sonnet] Session list uses `SessionManifest` shape from server ⇒ refactored
- [ ] T046 [sonnet] Session detail uses server-computed lap list, not local ⇒ refactored
- [ ] T047 [sonnet] Deep review pushed to webapp: "View full analysis in webapp" CTA instead of on-device ⇒ implemented
- [ ] T048 [sonnet] Provenance fields populated: device_model, os_version, app_build, sensor_config ⇒ tested
- [ ] T049 [sonnet] Cache track catalog from backend (for offline sector split rendering only) ⇒ works
- [ ] T050 [sonnet] Tests updated for new shapes ⇒ green

## Block D — Preflight readiness gate (T051–T065)

- [ ] T051 [opus] `PreflightService` in `Services/PreflightService.swift`: checks permissions, sensors, storage, battery ⇒ compiles
- [ ] T052 [opus] Check 1: location permission granted (always/in-use per config) ⇒ hard-block otherwise
- [ ] T053 [opus] Check 2: motion permission granted ⇒ hard-block otherwise
- [ ] T054 [opus] Check 3: bluetooth permission if RaceBox mode ⇒ hard-block
- [ ] T055 [opus] Check 4: track selected ⇒ hard-block
- [ ] T056 [opus] Check 5: GPS quality (accuracy ≤20m, 6+ sats) ⇒ hard-block with "wait" override
- [ ] T057 [opus] Check 6: RaceBox BLE connected if RaceBox mode ⇒ hard-block
- [ ] T058 [opus] Check 7: storage ≥500MB available ⇒ hard-block
- [ ] T059 [opus] Check 8: battery ≥15% ⇒ soft-warn, allow override
- [ ] T060 [sonnet] Preflight UI: modal with checklist, each item with status icon ⇒ rendered
- [ ] T061 [sonnet] Preflight UI: Start button disabled until all hard-blocks cleared ⇒ tested
- [ ] T062 [sonnet] Preflight UI: explanation per item (e.g., "GPS needs clear sky") ⇒ helpful
- [ ] T063 [sonnet] Preflight live refresh: values update every 2s while modal open ⇒ tested
- [ ] T064 [sonnet] Preflight persistence: user-accepted warnings remembered for session ⇒ tested
- [ ] T065 [sonnet] Tests: preflight hard-block / all pass / warn paths ⇒ green

## Block E — Bundle v2 writer (T066–T080)

- [ ] T066 [opus] `BundleV2Writer` class: emits manifest.json + telemetry + laps + events + checksums ⇒ compiles
- [ ] T067 [opus] Manifest writer: populates all `SessionManifest` fields ⇒ round-trips
- [ ] T068 [opus] Telemetry writer: CSV v2 format (with source+canonical timestamps) ⇒ valid
- [ ] T069 [opus] Telemetry writer: Parquet via ArrowSwift if feasible, else CSV fallback ⇒ one works
- [ ] T070 [opus] Laps writer: LapRecord JSON or Parquet ⇒ valid
- [ ] T071 [opus] Events writer: JSON of session events (lap crossings, flags) ⇒ valid
- [ ] T072 [opus] Checksum writer: sha256 per file in manifest ⇒ matches on re-read
- [ ] T073 [opus] Temp → final atomic rename preserved ⇒ tested
- [ ] T074 [opus] SensorConfigSnapshot populated (motion rate, location rate, BLE status) ⇒ populated
- [ ] T075 [opus] DataQuality populated (score, gaps count, sample rate stability) ⇒ populated
- [ ] T076 [sonnet] Integration test: write → read-back → validate against @lap/schemas ⇒ green
- [ ] T077 [sonnet] Integration test: bundle parses on backend (mock server) ⇒ green
- [ ] T078 [sonnet] Backward compat: old CSVs marked `bundle_format: v1`, new are `v2` ⇒ tagged
- [ ] T079 [sonnet] Bundle size accounting: report size in logs + UI ⇒ visible
- [ ] T080 [sonnet] Tests ⇒ green

## Block F — Durable upload queue (T081–T100)

- [ ] T081 [opus] `UploadQueue` SQLite table: session_id, state, attempt_count, next_retry_at, last_http_code, last_error, chunks_sent, chunks_total, idempotency_key ⇒ migration applied
- [ ] T082 [opus] `UploadWorker` singleton: starts on AppDelegate.applicationDidFinishLaunching ⇒ boots
- [ ] T083 [opus] `UploadWorker` starts on connectivity regain via NWPathMonitor ⇒ tested with airplane mode toggle
- [ ] T084 [opus] `UploadWorker` starts on Clerk token restore ⇒ tested
- [ ] T085 [opus] `UploadWorker` dequeue logic: pick next non-failed-permanent row ⇒ correct order
- [ ] T086 [opus] Idempotency-Key generation: UUIDv7 persisted at session creation ⇒ consistent across retries
- [ ] T087 [opus] Exponential backoff: 1s, 2s, 4s, 8s, 16s, 30s (cap at 5 min) with ±20% jitter ⇒ tested
- [ ] T088 [opus] Max 10 attempts before `failed_permanent` ⇒ tested
- [ ] T089 [opus] Resume: chunk cursor stored in queue row, resumes from `chunks_sent` ⇒ tested
- [ ] T090 [opus] Chunk upload: background URLSession for resume across app kills ⇒ tested
- [ ] T091 [opus] Background URLSession delegate wired in AppDelegate ⇒ completion callback fires after relaunch
- [ ] T092 [sonnet] Queue state visible in UI: "N sessions queued — uploading 1 of 5" ⇒ banner
- [ ] T093 [sonnet] Per-session upload state: Local / Uploading / Cloud-confirmed / Failed ⇒ badges visible
- [ ] T094 [sonnet] Manual retry: failed-permanent session has "Retry" button ⇒ resets state, re-queues
- [ ] T095 [sonnet] Abandon upload: user can delete local session (with confirm) ⇒ works
- [ ] T096 [sonnet] Queue visibility UI: "Uploads" tab in settings showing active + failed ⇒ renders
- [ ] T097 [sonnet] Test: airplane mode during upload → queue persists → reconnect → resumes ⇒ green
- [ ] T098 [sonnet] Test: force-kill during chunk upload → relaunch → resumes ⇒ green
- [ ] T099 [sonnet] Test: 502 from server → retry at backoff → eventually succeeds ⇒ green
- [ ] T100 [sonnet] Test: 422 from server → marks `failed_permanent` immediately (no retry on client error) ⇒ green

## Block G — Timestamp + RaceBox parser (T101–T125)

- [ ] T101 [opus] Separate source timestamps for motion samples: `CACurrentMediaTime()` nanoseconds ⇒ tested
- [ ] T102 [opus] Separate source timestamps for location samples: `CLLocation.timestamp.timeIntervalSince1970 * 1e9` ⇒ tested
- [ ] T103 [opus] Separate source timestamps for RaceBox samples: parsed from UBX NAV-PVT iTOW ⇒ tested
- [ ] T104 [opus] Attach `t_source_clock` enum to every emitted sample ⇒ tagged
- [ ] T105 [opus] Remove on-device timestamp fusion (server does canonical alignment) ⇒ diff clean
- [ ] T106 [sonnet] Tests: each adapter tags timestamps correctly ⇒ green
- [ ] T107 [opus] RaceBox parser: UBX frame segmenter handles fragmentation ⇒ existing tests still green
- [ ] T108 [opus] UBX class support: NAV-PVT (existing) ⇒ still works
- [ ] T109 [opus] UBX class support: NAV-STATUS (fix status) ⇒ decoded
- [ ] T110 [opus] UBX class support: NAV-PVAT (position+velocity+attitude+time) ⇒ decoded
- [ ] T111 [opus] UBX class support: NAV-RELPOSNED (RTK relative positioning if RaceBox Pro) ⇒ decoded
- [ ] T112 [opus] UBX class support: ESF-RAW (IMU raw from RaceBox IMU models) ⇒ decoded
- [ ] T113 [opus] UBX class support: ESF-ALG (IMU alignment) ⇒ decoded
- [ ] T114 [opus] UBX class support: ESF-MEAS (IMU measurements) ⇒ decoded
- [ ] T115 [opus] UBX class support: ESF-STATUS (IMU sensor status) ⇒ decoded
- [ ] T116 [opus] UBX class support: SEC-UNIQID (device unique ID) ⇒ decoded → populates provenance
- [ ] T117 [opus] UBX class support: MON-VER (firmware version) ⇒ decoded → populates provenance
- [ ] T118 [sonnet] Parser unit tests with captured UBX logs from actual RaceBox ⇒ all classes tested
- [ ] T119 [sonnet] Parser fuzz tests: random byte streams don't crash ⇒ green
- [ ] T120 [sonnet] RaceBox horizontalAccuracy field populated from NAV-PVT hAcc ⇒ tested
- [ ] T121 [sonnet] RaceBox IMU fields (if ESF-RAW arrives) replace phone-IMU for that stream ⇒ tested
- [ ] T122 [sonnet] RaceBox provenance fields attached to every session ⇒ populated
- [ ] T123 [sonnet] RaceBox connection-status UI widget ⇒ visible
- [ ] T124 [sonnet] RaceBox disconnection mid-session: graceful (journal marks gap) ⇒ tested
- [ ] T125 [sonnet] RaceBox auto-reconnect: scan + re-connect during session ⇒ works

## Block H — Dashboard + trackside UX (T126–T145)

- [ ] T126 [design] Figma: live dashboard layout with trust cues ⇒ approved
- [ ] T127 [sonnet] Dashboard header: persistent recording state strip per Q122 ⇒ visible
- [ ] T128 [sonnet] Dashboard: speed gauge (large, glanceable) ⇒ rendered
- [ ] T129 [sonnet] Dashboard: lap counter + current lap time ⇒ rendered
- [ ] T130 [sonnet] Dashboard: live trackmap with breadcrumb trail ⇒ rendered
- [ ] T131 [sonnet] Dashboard: speed-over-distance trace ⇒ rendered
- [ ] T132 [sonnet] Dashboard: g-g diagram (lat vs lon g) ⇒ rendered
- [ ] T133 [sonnet] Dashboard: GPS fix quality indicator (green/yellow/red) ⇒ color-coded
- [ ] T134 [sonnet] Dashboard: sample rate indicator (Hz) ⇒ visible
- [ ] T135 [sonnet] Dashboard: BLE connection status (if RaceBox) ⇒ visible
- [ ] T136 [sonnet] Dashboard: session-so-far summary panel ⇒ rendered
- [ ] T137 [sonnet] Glanceability: contrast-high color palette for outdoor sun readability ⇒ tested
- [ ] T138 [sonnet] Glanceability: font size responsive to phone size ⇒ tested
- [ ] T139 [sonnet] Glanceability: critical info (speed, lap time) at top ⇒ visible
- [ ] T140 [sonnet] Battery-saver mode: auto-throttles non-critical UI updates when <20% ⇒ works
- [ ] T141 [sonnet] Screen-lock during recording (prevent auto-sleep) ⇒ UIApplication.idleTimerDisabled
- [ ] T142 [sonnet] Orientation: landscape primary during recording ⇒ locked
- [ ] T143 [sonnet] Orientation: portrait for list/settings ⇒ works
- [ ] T144 [sonnet] Voice announcements (optional): "Lap 3 — 1:42.3" ⇒ configurable
- [ ] T145 [sonnet] Session detail on mobile: basic metrics + "Full analysis in webapp" CTA ⇒ tight

## Block I — Rules engine lite on mobile (T146–T165)

- [ ] T146 [opus] Port rules engine interface from desktop (`RulesEngineLite`) ⇒ Swift interface
- [ ] T147 [opus] Rules loader: fetches compiled bundle from backend at login ⇒ works
- [ ] T148 [opus] Rules cache: persisted in app docs, TTL 7 days ⇒ tested
- [ ] T149 [opus] Rules engine runs in background queue, not main thread ⇒ tested
- [ ] T150 [opus] Rules engine evaluation on lap-end events ⇒ tested
- [ ] T151 [opus] Subset of rules applicable to real-life capture (smaller set than desktop) ⇒ documented
- [ ] T152 [sonnet] Coaching prompt UI: bottom-sheet or overlay card during recording ⇒ rendered
- [ ] T153 [sonnet] Coaching prompt audio cue option ⇒ configurable
- [ ] T154 [sonnet] Coaching prompt dismissal ⇒ works
- [ ] T155 [sonnet] Coaching prompt flag-as-wrong ⇒ POST to backend, persists
- [ ] T156 [sonnet] Coaching prompt throttle: max 1 per 30s ⇒ tested
- [ ] T157 [sonnet] Coaching prompt audio: uses AVSpeechSynthesizer ⇒ works
- [ ] T158 [sonnet] Coaching prompts respect user skill level from Settings ⇒ variant chosen
- [ ] T159 [sonnet] Coaching integration with dashboard: card slot reserved ⇒ visible
- [ ] T160 [sonnet] Test: rules engine fires correct insight on archive session playback ⇒ green
- [ ] T161 [sonnet] Test: offline fallback uses cached rules ⇒ green
- [ ] T162 [sonnet] Test: rule update propagates on next app-open ⇒ green
- [ ] T163 [sonnet] Test: background queue doesn't block UI ⇒ tested (Instruments)
- [ ] T164 [sonnet] Test: battery impact of rules engine ⇒ negligible
- [ ] T165 [sonnet] Coaching prompt screenshots for QA review ⇒ archived

## Block J — QR pairing + Clerk (T166–T180)

- [ ] T166 [opus] Clerk iOS SDK integrated ⇒ imports work
- [ ] T167 [opus] Login flow: email + password (+ Google sign-in) ⇒ works against Clerk test env
- [ ] T168 [opus] Token storage: refresh token in iOS Keychain ⇒ secure, restored on launch
- [ ] T169 [opus] Token refresh: silent refresh in AppDelegate ⇒ works
- [ ] T170 [opus] QR scanner: AVFoundation-based scanner in "Pair device" flow ⇒ scans
- [ ] T171 [opus] Pairing flow: scan QR → POST /auth/pairing/redeem → receive refresh token ⇒ works
- [ ] T172 [sonnet] Pairing "forgot to scan" fallback: user enters code manually ⇒ works
- [ ] T173 [sonnet] Paired-device indicator in settings ⇒ visible
- [ ] T174 [sonnet] Unpair (logout) ⇒ clears keychain
- [ ] T175 [sonnet] Offline capture allowed without network: auth check on upload, not on capture ⇒ tested
- [ ] T176 [sonnet] Multi-account scaffold (single account only in v1) ⇒ not user-facing
- [ ] T177 [sonnet] Magic-link sign-in option ⇒ works
- [ ] T178 [sonnet] Apple sign-in (required by App Store if third-party OAuth) ⇒ wired
- [ ] T179 [sonnet] Session timeout: 7-day refresh rotates ⇒ tested
- [ ] T180 [sonnet] Logout clears journal, uploads paused ⇒ tested

## Block K — Observability + tests + polish (T181–T240)

- [ ] T181 [sonnet] Sentry iOS SDK integrated ⇒ crash captured
- [ ] T182 [sonnet] Sentry breadcrumbs: journal heartbeats, permission changes, BLE state ⇒ present
- [ ] T183 [sonnet] PostHog iOS SDK integrated ⇒ ready
- [ ] T184 [sonnet] PostHog events: `app_started`, `session_started`, `session_finalized`, `upload_completed` ⇒ visible
- [ ] T185 [sonnet] PostHog identify on login ⇒ user IDs match
- [ ] T186 [sonnet] Telemetry opt-out in Settings ⇒ respected
- [ ] T187 [sonnet] Unit tests: capture journal ⇒ green
- [ ] T188 [sonnet] Unit tests: upload queue ⇒ green
- [ ] T189 [sonnet] Unit tests: preflight service ⇒ green
- [ ] T190 [sonnet] Unit tests: BundleV2Writer ⇒ green
- [ ] T191 [sonnet] Unit tests: RaceBox parser all UBX classes ⇒ green
- [ ] T192 [sonnet] Unit tests: timestamp normalization ⇒ green
- [ ] T193 [sonnet] Unit tests: rules engine lite ⇒ green
- [ ] T194 [sonnet] Integration test: full capture→finalize→upload ⇒ green
- [ ] T195 [sonnet] Integration test: airplane mode during upload ⇒ resumes
- [ ] T196 [sonnet] Integration test: force-kill during recording ⇒ recovers via journal
- [ ] T197 [sonnet] Integration test: RaceBox connect mid-session ⇒ samples switch sources
- [ ] T198 [sonnet] UI test: login → start session → stop → see in list ⇒ green
- [ ] T199 [sonnet] UI test: preflight hard-block scenarios ⇒ green
- [ ] T200 [sonnet] UI test: pair device via QR ⇒ green
- [ ] T201 [sonnet] Perf: battery drain ≤ 15%/hr recording on iPhone 13 ⇒ measured via Energy Log
- [ ] T202 [sonnet] Perf: memory stable over 2h session ⇒ tested
- [ ] T203 [sonnet] Perf: app launch <2s on iPhone 13+ ⇒ tested
- [ ] T204 [sonnet] Accessibility: VoiceOver labels on all controls ⇒ audit passes
- [ ] T205 [sonnet] Accessibility: Dynamic Type supported ⇒ tested
- [ ] T206 [sonnet] Accessibility: color contrast AA+ ⇒ verified
- [ ] T207 [sonnet] Localization: English strings extracted to .strings ⇒ done
- [ ] T208 [sonnet] Localization: French strings stubbed ⇒ done
- [ ] T209 [sonnet] App icon + launch screen finalized ⇒ designed
- [ ] T210 [sonnet] Screenshots for App Store ⇒ captured
- [ ] T211 [sonnet] Privacy manifest (required iOS 17+) ⇒ populated
- [ ] T212 [sonnet] App Store metadata: description, keywords, category ⇒ drafted
- [ ] T213 [sonnet] TestFlight internal distribution ready ⇒ works
- [ ] T214 [sonnet] TestFlight external beta group created ⇒ ready for invites
- [ ] T215 [sonnet] In-app update prompt (for TestFlight external) ⇒ works
- [ ] T216 [sonnet] Crash-free-users target ≥98% ⇒ measured baseline
- [ ] T217 [sonnet] Network error handling: specific messages per error class ⇒ copy reviewed
- [ ] T218 [sonnet] Empty-state illustrations for session list, uploads, pairing ⇒ designed
- [ ] T219 [sonnet] Loading-state skeletons throughout ⇒ consistent
- [ ] T220 [sonnet] Error-state retry buttons ⇒ consistent
- [ ] T221 [sonnet] Settings: clear storage option ⇒ works
- [ ] T222 [sonnet] Settings: export diagnostics bundle ⇒ works
- [ ] T223 [sonnet] Settings: about (version, build, credits) ⇒ renders
- [ ] T224 [sonnet] Settings: support (mail link) ⇒ opens mailto
- [ ] T225 [sonnet] Settings: data export (GDPR) ⇒ triggers backend job + notify when ready
- [ ] T226 [sonnet] Settings: delete account ⇒ confirm → triggers backend delete
- [ ] T227 [sonnet] Offline banner: "offline — uploads paused" ⇒ visible
- [ ] T228 [sonnet] Connection-restored toast: "syncing 3 sessions" ⇒ visible
- [ ] T229 [sonnet] Haptic feedback: start / stop / success events ⇒ subtle
- [ ] T230 [sonnet] Dark mode / light mode support ⇒ tested
- [ ] T231 [sonnet] iPad layout (basic support, not optimized) ⇒ works
- [ ] T232 [sonnet] Documentation: README refreshed ⇒ current
- [ ] T233 [sonnet] Documentation: CONTRIBUTING for Swift contributors ⇒ written
- [ ] T234 [sonnet] Build pipeline: GitHub Actions macOS runner builds IPA ⇒ green
- [ ] T235 [sonnet] Code signing: Apple Dev Program cert configured ⇒ builds valid
- [ ] T236 [sonnet] Version number source: single xcconfig file ⇒ consistent
- [ ] T237 [sonnet] Changelog: CHANGELOG.md refreshed with M1 entries ⇒ written
- [ ] T238 [sonnet] Release checklist document ⇒ committed
- [ ] T239 [sonnet] Smoke test on clean iPhone: install, sign up, first session, upload ⇒ green
- [ ] T240 [sonnet] First TestFlight build submitted ⇒ accepted by App Store review
