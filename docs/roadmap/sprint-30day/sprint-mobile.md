# LAP Mobile — 30-Day Sprint Queue (Android-first)

**Repo:** `lap-mobile-android/`.
**Why Android first:** No Mac available → iOS frozen → Android is the active mobile lane. Android also covers Wear OS (companion per Q120). iOS resumes when Mac arrives (see `sprint-mobile-ios-future.md`).
**Stack:** Kotlin 2.0, Jetpack Compose, Gradle 8.10+, Hilt, Room, WorkManager, Retrofit, Kotlinx Serialization, Kotlin BLE (`nordic-android`), FusedLocationProviderClient, SensorManager, Clerk Android SDK.
**Total:** 240 tasks. Same /loop rules as sprint-backend.md. **Build verification:** `./gradlew app:assembleDebug && ./gradlew app:testDebugUnitTest` must be green per coding task.

---

## Block A — Project scaffold (T001–T025)

- [x] T001 [opus] Gradle project init: `./gradlew init` with Kotlin+Compose template, package `com.lap.mobile` ⇒ `gradlew assembleDebug` works — 999f2f3
- [x] T002 [sonnet] Gradle version catalog `gradle/libs.versions.toml` with Kotlin 2.0, Compose BOM 2025.01, AGP 8.7 ⇒ builds — 1341404
- [x] T003 [sonnet] Enable Compose Compiler, set min SDK 26 (Android 8), target SDK 34 ⇒ builds — f300508
- [x] T004 [sonnet] KSP enabled for Hilt + Room ⇒ builds — d9e8e75
- [x] T005 [codex] `.editorconfig`, `detekt.yml`, `.gitattributes` ⇒ checked-in — 2a7a118
- [x] T006 [codex] Detekt + ktlint Gradle tasks: `./gradlew detekt ktlintCheck` ⇒ green on empty project — 0a15e1e
- [x] T007 [codex] GitHub Actions `ci.yml`: assembleDebug, lint, test on push ⇒ workflow green — b1dceb8 [PENDING: green-on-push validation requires remote GHA run; each step verified locally]
- [x] T008 [sonnet] Pre-commit hook: ktlintFormat + assembleDebug ⇒ blocks bad commits — 226b89a
- [x] T009 [sonnet] Hilt setup: `@HiltAndroidApp` on `LapApplication`, AppComponent wired ⇒ app launches — 1426ca2 [PENDING: app-launch-on-device]
- [x] T010 [sonnet] Navigation-compose dep + NavHost scaffold in MainActivity ⇒ default route renders — 690db9f [PENDING: default-route-renders-on-device]
- [x] T011 [sonnet] Material 3 theme: light + dark color schemes, Typography, Shapes ⇒ screens themed — 098f8bd [PENDING: visual-check-on-device]
- [x] T012 [sonnet] App icon + launcher icon set (temporary placeholders) ⇒ installed on device — 40e013e [PENDING: install-on-device]
- [x] T013 [sonnet] Strings.xml: default English strings, values-fr/ stubbed ⇒ localizable — 584a231
- [x] T014 [sonnet] ProGuard/R8 rules file with defaults + Hilt+Room+Retrofit keep rules ⇒ release build works — 8577f35
- [x] T015 [sonnet] Signing configs: debug default, release placeholder reading from `keystore.properties` ⇒ compiles both — 2208d57
- [x] T016 [sonnet] Flavor setup: `dev`, `staging`, `prod` with different API endpoints ⇒ all three build — d706c03
- [x] T017 [sonnet] BuildConfig fields: API_BASE_URL, CLERK_PUBLISHABLE_KEY, SENTRY_DSN, POSTHOG_KEY ⇒ populated per flavor — 3529361
- [x] T018 [sonnet] Package layout: `capture/`, `ingest/`, `coaching/`, `ui/`, `data/`, `di/`, `core/` ⇒ packages exist with `.gitkeep` — 5caa77e
- [x] T019 [sonnet] Logging: Timber integrated, tree config per build type ⇒ logs appear — dc887af [PENDING: logs-visible-on-device]
- [x] T020 [sonnet] Coroutines: default dispatchers provider for testing (`DispatcherProvider`) ⇒ injectable — ea2eb5e
- [ ] T021 [sonnet] Serialization: `kotlinx-serialization-json` dep + `SerializersModule` with polymorphic tags ⇒ serializes test class
- [ ] T022 [sonnet] Error model: `sealed class DomainError` + `Result<T, E>` alias ⇒ unit tests round-trip
- [ ] T023 [sonnet] DI module: `@Module @InstallIn(SingletonComponent::class)` for app-level providers ⇒ Hilt compiles
- [ ] T024 [sonnet] Navigation routes enum: `Routes.Login`, `Routes.SessionList`, `Routes.Dashboard`, etc. ⇒ all defined
- [ ] T025 [sonnet] First integration test: launch app, land on login/list ⇒ green via `androidTest`

## Block B — Schema integration (T026–T040)

- [ ] T026 [sonnet] Install `@lap/schemas` Kotlin types as local module (`lap-schemas/kotlin/`) ⇒ Gradle includes
- [ ] T027 [sonnet] Reference `SessionManifest` Kotlin type (generated or hand-typed stub until codegen ready) ⇒ imports
- [ ] T028 [sonnet] `TelemetrySample` Kotlin data class ⇒ compiles
- [ ] T029 [sonnet] `SourceTag` enum ⇒ compiles
- [ ] T030 [sonnet] `EnvironmentTag` enum ⇒ compiles
- [ ] T031 [sonnet] `DataQuality` data class ⇒ compiles
- [ ] T032 [sonnet] `SensorConfigSnapshot` data class ⇒ compiles
- [ ] T033 [sonnet] `LapRecord` data class ⇒ compiles
- [ ] T034 [sonnet] `WeaknessEpisode` data class (consumer-side) ⇒ compiles
- [ ] T035 [sonnet] `ActionPrescription` data class ⇒ compiles
- [ ] T036 [sonnet] `CoachingInsight` data class ⇒ compiles
- [ ] T037 [sonnet] `DriverProgressSnapshot` data class ⇒ compiles
- [ ] T038 [sonnet] All schema types serializable via kotlinx-serialization ⇒ round-trip tests green
- [ ] T039 [sonnet] UUID7 type alias (`typealias UUID7 = String` with validation) ⇒ unit-tested
- [ ] T040 [sonnet] Replace any hand-rolled duplicate types ⇒ diff clean

## Block C — Room database + journal (T041–T060)

- [ ] T041 [opus] Room setup: `LapDatabase` abstract class, `TypeConverters` for UUID7/Instant ⇒ compiles
- [ ] T042 [opus] Entity `SessionEntity` (id, state, started_at, ended_at, source, track_id, car_id, sample_count, file_uri) ⇒ migration applied
- [ ] T043 [opus] Entity `SessionJournalEntity` (session_id, last_heartbeat_at, file_offset, status) ⇒ migration
- [ ] T044 [opus] Entity `UploadQueueEntity` (session_id, state, attempt_count, next_retry_at, last_http_code, last_error, chunks_sent, chunks_total, idempotency_key) ⇒ migration
- [ ] T045 [opus] Entity `InsightCacheEntity` (session-level CoachingInsights cached for offline view) ⇒ migration
- [ ] T046 [opus] Entity `PrescriptionCacheEntity` ⇒ migration
- [ ] T047 [opus] Entity `TrackCacheEntity` (offline sector splits) ⇒ migration
- [ ] T048 [opus] Entity `RuleBundleEntity` (compiled coaching-rules bundle + fetched_at) ⇒ migration
- [ ] T049 [sonnet] DAO `SessionDao`: insert, update, list by status, observe as Flow ⇒ tested
- [ ] T050 [sonnet] DAO `JournalDao`: upsertHeartbeat, listStale ⇒ tested
- [ ] T051 [sonnet] DAO `UploadQueueDao`: enqueue, dequeueNext, updateAttempt ⇒ tested
- [ ] T052 [sonnet] DAO `InsightCacheDao`: upsertBatch, listForSession ⇒ tested
- [ ] T053 [opus] Migration strategy: `fallbackToDestructiveMigration` in dev flavor, strict migrations in prod ⇒ documented
- [ ] T054 [opus] Journal writer service: heartbeat every 5s during recording, writes via DAO ⇒ tested with fake clock
- [ ] T055 [opus] Journal startup reconciliation: find stale journal rows (heartbeat > 60s gap) ⇒ tested
- [ ] T056 [opus] Reconciliation: find orphan temp files ⇒ tested
- [ ] T057 [opus] Reconciliation: find sessions in `recording`/`finalizing` → offer recovery ⇒ tested
- [ ] T058 [sonnet] Recovery modal composable: renders stale session list with actions ⇒ Compose preview
- [ ] T059 [sonnet] Recovery → Finalize-from-journal path ⇒ works for test fixture
- [ ] T060 [sonnet] Journal retention: rows >7 days auto-clean after user confirms ⇒ tested

## Block D — Location + motion capture (T061–T085)

- [ ] T061 [opus] `LocationCaptureService`: FusedLocationProviderClient at high-accuracy, 10Hz ⇒ samples stream
- [ ] T062 [opus] Permission manager: request location (fine+coarse, foreground + background) ⇒ tested flows
- [ ] T063 [opus] Foreground service: `CaptureForegroundService` with persistent notification during recording ⇒ survives backgrounding
- [ ] T064 [opus] Notification channel + lock-screen visible notification ⇒ user-aware
- [ ] T065 [opus] `LocationSample` mapped to `TelemetrySample` shape with `t_source_clock="gnss"` ⇒ tested
- [ ] T066 [opus] Horizontal accuracy, speed, bearing fields populated ⇒ validated
- [ ] T067 [sonnet] Location error handling: loss of fix surfaced via UiState ⇒ tested
- [ ] T068 [sonnet] `MotionCaptureService`: SensorManager accelerometer + gyroscope at 50Hz ⇒ samples stream
- [ ] T069 [sonnet] Motion samples mapped to TelemetrySample with `t_source_clock="device_monotonic"` (using `SensorEvent.timestamp` in nanos) ⇒ tested
- [ ] T070 [sonnet] Low-pass filter option on accelerometer (configurable) ⇒ tested
- [ ] T071 [opus] `CaptureOrchestrator`: combines location + motion + BLE into single `Flow<TelemetrySample>` ⇒ tested
- [ ] T072 [opus] Per-sample source tagging, no on-device fusion (server aligns per ADR-007) ⇒ tested
- [ ] T073 [sonnet] Battery-aware throttling: if battery <20%, reduce motion rate to 25Hz ⇒ tested
- [ ] T074 [sonnet] Thermal-aware throttling: if device thermal = SEVERE, pause non-critical sensors ⇒ tested
- [ ] T075 [sonnet] Recording state machine: IDLE → ARMED → RECORDING → FINALIZING → COMPLETED/FAILED ⇒ unit-tested
- [ ] T076 [sonnet] `SessionCoordinator` wiring: orchestrator + journal + state machine ⇒ integration test green
- [ ] T077 [sonnet] Recording start: preflight check (Block E) must pass before ARMED→RECORDING ⇒ enforced
- [ ] T078 [sonnet] Recording stop: emit SessionEndEvent, transition to FINALIZING ⇒ tested
- [ ] T079 [sonnet] Crash-safe buffer: writes sample batches to disk every 500 samples or 10s ⇒ tested
- [ ] T080 [sonnet] Buffer file format: newline-delimited JSON or length-prefixed binary ⇒ documented
- [ ] T081 [sonnet] Power management: acquire WakeLock (PARTIAL_WAKE_LOCK) during recording ⇒ released on stop
- [ ] T082 [sonnet] Sample count reported via Flow for UI ⇒ rendered
- [ ] T083 [sonnet] Instrumented test: start recording for 60s, verify >3000 samples captured ⇒ green
- [ ] T084 [sonnet] Instrumented test: kill app during recording → restart → journal recovery ⇒ green
- [ ] T085 [sonnet] Instrumented test: airplane mode during recording → capture continues locally ⇒ green

## Block E — Preflight readiness gate (T086–T100)

- [ ] T086 [opus] `PreflightService` interface + impl ⇒ compiles
- [ ] T087 [opus] Check: location permission granted (fine + background for Android 10+) ⇒ hard-block otherwise
- [ ] T088 [opus] Check: notification permission (Android 13+) for foreground service ⇒ hard-block
- [ ] T089 [opus] Check: bluetooth permission + BT adapter enabled (if RaceBox mode) ⇒ hard-block
- [ ] T090 [opus] Check: track selected ⇒ hard-block
- [ ] T091 [opus] Check: GPS fix quality (accuracy ≤20m, 6+ sats) ⇒ hard-block with "wait" override
- [ ] T092 [opus] Check: RaceBox BLE connected if mode ⇒ hard-block
- [ ] T093 [opus] Check: storage ≥500MB free ⇒ hard-block
- [ ] T094 [opus] Check: battery ≥15% ⇒ soft-warn, override allowed
- [ ] T095 [opus] Check: device thermal state ≤ MODERATE ⇒ soft-warn
- [ ] T096 [sonnet] Compose `PreflightScreen` with live-updating checklist ⇒ Preview
- [ ] T097 [sonnet] Start button disabled until all hard-blocks cleared ⇒ tested
- [ ] T098 [sonnet] Per-item help text + "Fix it" CTA (deep-link to settings when permission missing) ⇒ works
- [ ] T099 [sonnet] Preflight value refresh: every 2s while screen open ⇒ tested
- [ ] T100 [sonnet] Preflight unit tests: each check isolated ⇒ green

## Block F — RaceBox BLE (T101–T130)

- [ ] T101 [opus] Nordic Android BLE library integrated ⇒ scan stubs work
- [ ] T102 [opus] `RaceBoxBleService`: scan by service UUID ⇒ surfaces advertisers
- [ ] T103 [opus] BLE connection state: DISCONNECTED / SCANNING / CONNECTING / CONNECTED / LOST ⇒ Flow<State>
- [ ] T104 [opus] UART service + characteristic discovery ⇒ tested with mock
- [ ] T105 [opus] Packet stream: BLE notifications flow into byte stream ⇒ tested
- [ ] T106 [opus] UBX framer: reassembles fragmented frames, validates sync + checksum ⇒ tested with captured log
- [ ] T107 [opus] UBX class parser: NAV-PVT (position, velocity, time) ⇒ unit-tested with real fixture
- [ ] T108 [opus] UBX class parser: NAV-STATUS ⇒ tested
- [ ] T109 [opus] UBX class parser: NAV-PVAT (with attitude) ⇒ tested
- [ ] T110 [opus] UBX class parser: NAV-RELPOSNED ⇒ tested
- [ ] T111 [opus] UBX class parser: ESF-RAW (IMU) ⇒ tested
- [ ] T112 [opus] UBX class parser: ESF-ALG ⇒ tested
- [ ] T113 [opus] UBX class parser: ESF-MEAS ⇒ tested
- [ ] T114 [opus] UBX class parser: ESF-STATUS ⇒ tested
- [ ] T115 [opus] UBX class parser: SEC-UNIQID (populates provenance device_id) ⇒ tested
- [ ] T116 [opus] UBX class parser: MON-VER (populates firmware in provenance) ⇒ tested
- [ ] T117 [opus] RaceBox sample → `TelemetrySample` with `t_source_clock="racebox_gnss"` ⇒ tested
- [ ] T118 [sonnet] Horizontal accuracy from NAV-PVT hAcc populated ⇒ non-null
- [ ] T119 [sonnet] RaceBox status reconnect: on disconnect, attempt reconnect 3x ⇒ tested
- [ ] T120 [sonnet] RaceBox disconnect mid-session: journal marks gap, capture continues with phone GPS fallback ⇒ tested
- [ ] T121 [sonnet] BLE permission flow: request + settings deep-link ⇒ works
- [ ] T122 [sonnet] BLE scan timeout: 30s then stop + surface error ⇒ tested
- [ ] T123 [sonnet] BLE scan results UI: list advertisers with signal strength ⇒ Compose preview
- [ ] T124 [sonnet] Device pairing: tap advertiser → connect → save as "last used RaceBox" ⇒ persisted
- [ ] T125 [sonnet] Auto-reconnect on session start: uses last-used device ⇒ tested
- [ ] T126 [sonnet] BLE service lifecycle: bound to CaptureForegroundService ⇒ survives backgrounding
- [ ] T127 [sonnet] Packet fuzz test: random byte streams don't crash parser ⇒ green
- [ ] T128 [sonnet] Parser benchmark: 1000 samples/sec sustained, no backlog ⇒ green
- [ ] T129 [sonnet] BLE integration test (emulator + mock peripheral) ⇒ green
- [ ] T130 [sonnet] UX: "RaceBox connected" indicator in dashboard header ⇒ visible

## Block G — Bundle v2 writer (T131–T145)

- [ ] T131 [opus] `BundleV2Writer` class: emits manifest.json + telemetry + laps + events + checksums ⇒ compiles
- [ ] T132 [opus] Manifest writer: populates all `SessionManifest` fields ⇒ round-trip JSON test
- [ ] T133 [opus] Telemetry writer: CSV-v2 format with both source + canonical timestamps ⇒ valid
- [ ] T134 [opus] Telemetry writer: Parquet via Apache Arrow (if dep feasible) else CSV only ⇒ at least CSV works
- [ ] T135 [opus] Laps writer: JSON of LapRecord shape ⇒ valid
- [ ] T136 [opus] Events writer: session events (start, lap cross, flags, stop) ⇒ valid
- [ ] T137 [opus] Checksum writer: SHA-256 per file in manifest ⇒ matches on re-read
- [ ] T138 [opus] Atomic rename: temp → final via File.renameTo ⇒ tested (no partial bundles)
- [ ] T139 [opus] SensorConfigSnapshot populated (location rate, motion rate, BLE state, device model, os) ⇒ populated
- [ ] T140 [opus] DataQuality populated (score, gaps, sample rate stability, warnings) ⇒ computed
- [ ] T141 [sonnet] Integration test: write → read-back → validate round-trip ⇒ green
- [ ] T142 [sonnet] Integration test: incomplete write → retry → no corruption ⇒ green
- [ ] T143 [sonnet] Bundle finalize: called at session stop, blocks until complete ⇒ tested
- [ ] T144 [sonnet] Bundle finalize integrity check: all files present, sha matches, non-empty ⇒ enforced
- [ ] T145 [sonnet] Bundle size logged to journal + UI ⇒ visible

## Block H — WorkManager upload queue (T146–T170)

- [ ] T146 [opus] WorkManager setup + Hilt integration ⇒ `HiltWorkerFactory` registered
- [ ] T147 [opus] `UploadBundleWorker` (CoroutineWorker): reads next queue row, uploads ⇒ tested
- [ ] T148 [opus] Retrofit + OkHttp: `IngestApi` with `POST /api/v1/sessions/ingest` ⇒ compiles
- [ ] T149 [opus] Auth interceptor: attaches Clerk JWT, 401 triggers token refresh ⇒ tested
- [ ] T150 [opus] Idempotency-Key header: session UUIDv7, persisted ⇒ identical on retry
- [ ] T151 [opus] Multipart upload: manifest + chunks[] streamed ⇒ tested with fixture
- [ ] T152 [opus] Resume cursor: chunks_sent persisted, resumes from partial ⇒ tested
- [ ] T153 [opus] Upload progress: emits per-chunk progress via Flow ⇒ UI renders
- [ ] T154 [sonnet] Exponential backoff: 1s/2s/4s/8s/16s/30s/60s with jitter ⇒ tested
- [ ] T155 [sonnet] Max attempts: 10 before `failed_permanent` ⇒ tested
- [ ] T156 [sonnet] Network constraint: UNMETERED default, user can override to ALLOW_METERED ⇒ setting persists
- [ ] T157 [sonnet] WiFi-only toggle in Settings ⇒ respected
- [ ] T158 [sonnet] Battery constraint: defer if battery low (unless user forces) ⇒ tested
- [ ] T159 [sonnet] Worker bounded to UNIQUE by session_id (no duplicate uploads) ⇒ tested
- [ ] T160 [sonnet] Queue ordering: FIFO by `enqueued_at`, failed_permanent skipped ⇒ tested
- [ ] T161 [sonnet] Manual retry: user-initiated resets attempt_count, re-enqueues ⇒ works
- [ ] T162 [sonnet] Abandon upload: user deletes local session (confirm), removes from queue ⇒ works
- [ ] T163 [sonnet] Queue visibility UI: "Uploads" screen listing active + failed ⇒ Compose preview
- [ ] T164 [sonnet] Per-session upload state UI: Local / Uploading %/ Cloud-confirmed / Failed ⇒ badges
- [ ] T165 [sonnet] Connectivity observer: NetworkCallback triggers queue kick ⇒ tested
- [ ] T166 [sonnet] Auth-restore trigger: on login, kicks queue ⇒ tested
- [ ] T167 [sonnet] Test: airplane mode during upload → resumes on reconnect ⇒ green
- [ ] T168 [sonnet] Test: force-kill during chunk upload → relaunch resumes ⇒ green
- [ ] T169 [sonnet] Test: 502 response → retries at backoff → eventually succeeds ⇒ green
- [ ] T170 [sonnet] Test: 422 response → `failed_permanent` immediately (no retry on client error) ⇒ green

## Block I — Clerk auth + QR pairing (T171–T190)

- [ ] T171 [opus] Clerk Android SDK dep + `@HiltEntryPoint` integration ⇒ compiles
- [ ] T172 [opus] Login screen: email + password (+ Google) ⇒ Compose preview
- [ ] T173 [opus] Session token storage: Android Keystore + EncryptedSharedPreferences ⇒ secure
- [ ] T174 [opus] Token refresh: silent on 401, via OkHttp Authenticator ⇒ tested
- [ ] T175 [opus] Logout: clears keystore, kills WorkManager uploads, resets DB ⇒ tested
- [ ] T176 [sonnet] Apple sign-in via Clerk (required by App Store eventually — Android optional) ⇒ noted, deferred
- [ ] T177 [sonnet] Magic-link sign-in flow ⇒ works
- [ ] T178 [opus] QR scanner: CameraX + ML Kit barcode ⇒ scans
- [ ] T179 [opus] Pairing flow: scan QR in webapp → POST /auth/pairing/redeem → store refresh ⇒ works
- [ ] T180 [sonnet] Manual code entry fallback ⇒ works
- [ ] T181 [sonnet] Paired-device indicator in Settings ⇒ visible
- [ ] T182 [sonnet] Unpair (revoke this device): POST /auth/devices/:id/revoke ⇒ tested
- [ ] T183 [sonnet] Offline capture permitted without auth for current session (auth check at upload) ⇒ tested
- [ ] T184 [sonnet] Deep-link from webapp: `lap://pair?token=...` ⇒ routes correctly
- [ ] T185 [sonnet] Deep-link domain: App Links verification on `app.lap-coach.racing/pair` ⇒ configured
- [ ] T186 [sonnet] Session expired UX: sign-in-again modal, preserves local data ⇒ works
- [ ] T187 [sonnet] Multi-account scaffold (single-account active in v1) ⇒ not user-facing
- [ ] T188 [sonnet] Biometric lock option (Settings → Security) ⇒ works
- [ ] T189 [sonnet] User profile sync: on login, fetch /me and populate local cache ⇒ tested
- [ ] T190 [sonnet] Unit + instrumented tests for auth flows ⇒ green

## Block J — Dashboard UI (T191–T210)

- [ ] T191 [design] Compose mockup: live dashboard with speed gauge, lap timing, trackmap ⇒ Figma reviewed
- [ ] T192 [opus] `DashboardScreen` composable + `DashboardViewModel` ⇒ compiles
- [ ] T193 [opus] Speed gauge: large, glanceable, color-coded ⇒ Compose preview
- [ ] T194 [opus] Lap counter + current lap time ⇒ renders
- [ ] T195 [opus] Track map: Canvas-based breadcrumb of GPS trail ⇒ performant at 10Hz updates
- [ ] T196 [opus] Speed-over-distance trace (last lap) ⇒ renders
- [ ] T197 [opus] G-G diagram (lat accel vs lon accel) ⇒ Canvas-rendered
- [ ] T198 [opus] GPS fix-quality indicator (green/yellow/red dot) ⇒ reflects state
- [ ] T199 [opus] Sample rate indicator (Hz) ⇒ visible
- [ ] T200 [opus] BLE/RaceBox connection indicator ⇒ reflects state
- [ ] T201 [opus] Battery indicator with warning at <20% ⇒ visible
- [ ] T202 [opus] Recording-state strip (persistent across dashboard) ⇒ visible
- [ ] T203 [sonnet] Stop button: 0.5s hold + confirm ⇒ tested
- [ ] T204 [sonnet] Back gesture during recording: confirm dialog ⇒ tested
- [ ] T205 [sonnet] Screen wakelock during recording ⇒ works
- [ ] T206 [sonnet] Orientation: landscape forced during recording ⇒ tested
- [ ] T207 [sonnet] Voice announcements: TTS "Lap 3 — 1:42.3" ⇒ optional in Settings
- [ ] T208 [sonnet] Contrast-high theme for outdoor sunlight ⇒ toggle works
- [ ] T209 [sonnet] Accessibility: contentDescription on all critical controls ⇒ TalkBack works
- [ ] T210 [sonnet] Dashboard integration test: start recording, view dashboard, stop ⇒ green

## Block K — Rules engine, observability, tests, release (T211–T240)

- [ ] T211 [opus] Port rules-engine-lite interface from desktop spec ⇒ Kotlin interface
- [ ] T212 [opus] Rules bundle fetcher: downloads compiled JSON from backend at login ⇒ tested
- [ ] T213 [opus] Rules bundle cache: Room-backed, TTL 7 days, signature-verified ⇒ tested
- [ ] T214 [opus] Rules engine runtime: evaluates rule conditions against session features ⇒ unit-tested
- [ ] T215 [opus] Rules engine hook into SessionCoordinator: runs per lap-end event ⇒ tested
- [ ] T216 [sonnet] Subset: load only rules tagged `applicable_to: mobile_real_life` to reduce bundle size ⇒ tested
- [ ] T217 [sonnet] Coaching prompt composable: bottom-sheet card during recording ⇒ preview
- [ ] T218 [sonnet] Coaching prompt audio cue (TTS) optional ⇒ configurable
- [ ] T219 [sonnet] Coaching prompt dismissal + flag-as-wrong ⇒ persists
- [ ] T220 [sonnet] Coaching prompt throttle: max 1 per 30s ⇒ tested
- [ ] T221 [sonnet] User skill-level setting drives explanation variant ⇒ tested
- [ ] T222 [sonnet] Sentry Android SDK: init + breadcrumbs ⇒ 500 captured
- [ ] T223 [sonnet] PostHog Android SDK: events `app_started`, `session_started`, `session_finalized`, `upload_completed` ⇒ visible
- [ ] T224 [sonnet] Telemetry opt-out in Settings ⇒ respected
- [ ] T225 [sonnet] App startup smoke tests (JUnit) ⇒ green
- [ ] T226 [sonnet] ViewModel unit tests: SessionListVM, DashboardVM ⇒ green
- [ ] T227 [sonnet] Repository unit tests: SessionRepo, UploadRepo ⇒ green
- [ ] T228 [sonnet] Instrumented test: full capture-to-upload flow with mock backend ⇒ green
- [ ] T229 [sonnet] Instrumented test: preflight hard-block scenarios ⇒ green
- [ ] T230 [sonnet] Instrumented test: permission denial handling ⇒ green
- [ ] T231 [sonnet] Instrumented test: BLE disconnect mid-session ⇒ green
- [ ] T232 [sonnet] Benchmark test: memory + CPU during 30-min recording ⇒ within budget
- [ ] T233 [sonnet] App icon final design ⇒ replaced
- [ ] T234 [sonnet] Google Play Store metadata drafted (description, screenshots, category) ⇒ ready
- [ ] T235 [sonnet] Play Store internal test track build ⇒ uploaded
- [ ] T236 [sonnet] Play Store closed beta track ⇒ configured
- [ ] T237 [sonnet] Crashlytics / Sentry crash-free-users target ≥98% ⇒ baseline measured
- [ ] T238 [sonnet] ProGuard R8 release build: size + startup verified ⇒ within targets
- [ ] T239 [sonnet] CHANGELOG.md populated with M1 entries ⇒ written
- [ ] T240 [sonnet] Smoke test on clean Android device: install, sign up, first session, upload ⇒ green

---

## Notes

- **Wear OS companion** (per Q120): scoped for M5/W19 in main roadmap, not in this 30-day sprint.
- **iOS parity**: see `sprint-mobile-ios-future.md`, resume when Mac available.
- **Performance target**: ≤12% battery/hour recording, ≤300MB memory, p95 upload success ≥98%.
