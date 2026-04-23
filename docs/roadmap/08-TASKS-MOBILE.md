# LAP — Mobile Task Backlog

**Repos:** `lap-mobile` (iOS Swift, existing), `lap-mobile-android` (new M5), `lap-mobile-wearables` (Watch + WearOS companion, M5).
**Stack iOS:** Swift 6, iOS 17+ target, SwiftUI, CoreLocation, CoreMotion, CoreBluetooth, SQLite (GRDB), XcodeGen.
**Stack Android:** Kotlin 2.0, Jetpack Compose, FusedLocationProvider, SensorManager, Android BLE Kotlin coroutines.
**Stack Wearables:** WatchKit (Apple Watch), WearOS Compose (Android wearable).
**Task format:** `MO-NNN` (iOS + shared), `AN-NNN` (Android), `WR-NNN` (wearables).

---

## Month 1 — P0 + Foundation

### MO-001 🔴 Remove `try!` force-unwraps (crash-on-init)
- **Month/week:** M1/W1
- **Deps:** none
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Per Q113 + audit P0. `LapCoachAppModel.live()` force-unwraps API URL. `StorageService()` uses `try!`. Replace with graceful failure paths:
  - Missing API URL → show config error screen with "contact support" CTA
  - Storage init failure → attempt recovery, if fails show corrupt-state screen with "reinstall" option
- **Acceptance:**
  - `grep -rn "try!" LapCoachMobileApp/` returns 0 results
  - App boot with deliberately corrupted storage shows recovery UI, doesn't crash

### MO-002 🔴 `finalizeSession` integrity check
- **Month/week:** M1/W1
- **Deps:** none
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Per Q109 + audit P0. Current `finalizeSession` silently succeeds when temp CSV is missing. Add checks:
  - Temp file exists
  - Non-empty
  - Header present
  - Sample count > 0
  - Move succeeds
  - Sample hash computed
  - If any check fails → persist with `upload_state: corrupt_local` and surface in UI with recovery options

### MO-003 🔴 Prevent `fullScreenCover` accidental stop
- **Month/week:** M1/W1
- **Deps:** none
- **AI:** claude-sonnet
- **Hours:** 3-4
- **Context:** Per Q114 + audit. Dashboard dismissal should not stop session. Require explicit Stop action:
  - Swipe-to-dismiss disabled during recording
  - Back gesture → confirm dialog "Stop recording?"
  - Stop button requires 0.5s hold (prevents accidental tap in cockpit)

### MO-004 🔴 Capture journal with heartbeat
- **Month/week:** M1/W2
- **Deps:** MO-001
- **AI:** claude-opus
- **Hours:** 10-14
- **Context:** Persist active session state to SQLite every 5 seconds during recording: `session_id`, `started_at`, `sample_count`, `last_heartbeat_at`, `source`, `track_id`, `file_offset`. On app launch, find stale entries and offer recovery.
- **Acceptance:**
  - Force-quit app during recording → on relaunch, user sees "Recover session?" with telemetry-so-far visible
  - Heartbeat gap >60s marks session `suspicious` but still recoverable
  - Entries older than 7 days auto-cleaned after user confirms loss

### MO-005 🔴 Startup reconciliation
- **Month/week:** M1/W2
- **Deps:** MO-004
- **AI:** claude-opus
- **Hours:** 6-8
- **Context:** On app launch:
  1. Scan journal for active sessions
  2. Scan temp files for orphans
  3. Scan DB for sessions in `recording` or `finalizing` state
  4. Reconcile: which are recoverable? which are lost? which were finalized but never uploaded?
  5. Surface result as "Recovery" card on session list, not automatic deletion.

### MO-006 🔴 Install `@lap/schemas` Swift types
- **Month/week:** M1/W2
- **Deps:** BE-004
- **AI:** claude-sonnet
- **Hours:** 3-4
- **Context:** Generated Swift types for `SessionManifest`, `TelemetrySample`. Replace local struct duplicates.

### MO-007 🔴 Bundle v2 writer
- **Month/week:** M1/W4
- **Deps:** MO-006
- **AI:** claude-opus
- **Hours:** 10-14
- **Context:** Mobile currently writes CSV + chunk JSON. Rewrite to produce Bundle v2: manifest JSON + telemetry parquet (via ArrowSwift or similar) OR fallback to CSV with explicit `bundle_format: v2_csv_fallback` flag. Compute SHA-256 checksums.
- **Acceptance:**
  - Finalized bundle parses on server via `SessionManifest.model_validate()`
  - Checksums match server-side validation

### MO-008 🔴 Preflight readiness gate
- **Month/week:** M1/W3
- **Deps:** MO-001
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Per Q112. Before Start button enabled, verify:
  - Track selected (hard block)
  - GPS quality OK (hard block unless explicitly overridden)
  - Storage >500MB available (hard block)
  - Battery >15% (warning, can override)
  - Permissions granted: location always + motion + bluetooth if RaceBox mode (hard block)
  - RaceBox connected if RaceBox mode (hard block)
- **Acceptance:**
  - Start button grayed with hover-reason until blocks cleared
  - Preflight surface shown as modal when any block present

### MO-009 🔴 Durable upload queue table + worker
- **Month/week:** M2/W7
- **Deps:** MO-007, BE-007
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Per Q106 + audit. SQLite table `upload_queue` with: `session_id`, `state`, `attempt_count`, `next_retry_at`, `last_http_code`, `last_error`, `chunks_sent`, `chunks_total`, `idempotency_key`. Worker:
  - Starts on app launch
  - Starts on connectivity regain (`NWPathMonitor`)
  - Starts on auth restore
  - Exponential backoff + jitter
  - Resumable via chunk cursor
  - Max 10 attempts, then `failed_permanent` with user-visible recovery UI
- **Acceptance:**
  - Kill network during upload → resumes on reconnect without user interaction
  - Force-quit mid-upload → resumes on relaunch
  - Backend receives same `Idempotency-Key` on retry, returns prior response

### MO-010 🔴 Background URLSession delegate wiring
- **Month/week:** M2/W7
- **Deps:** MO-009
- **AI:** claude-opus
- **Hours:** 6-8
- **Context:** Per audit. Current code has background URLSession configured but no delegate wiring. Implement `URLSessionDataDelegate` in `AppDelegate` so uploads complete even when app is backgrounded or relaunched.

### MO-011 🟡 Sentry + PostHog integration
- **Month/week:** M1/W4
- **Deps:** MO-001
- **AI:** codex
- **Hours:** 3-4

---

## Month 2 — Reliability Sprint

### MO-012 🔴 Timestamp normalization (per ADR-007)
- **Month/week:** M2/W5
- **Deps:** MO-006
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Every sample carries `t_source_ns` + `t_source_clock`. Canonical alignment happens server-side. Client stops fusing pre-upload. RaceBox samples report `t_source_clock: racebox_gnss`, CoreMotion as `coremotion`, CLLocation as `gnss`.

### MO-013 🔴 RaceBox parser full UBX class coverage
- **Month/week:** M2/W6
- **Deps:** MO-012
- **AI:** claude-opus (protocol knowledge) + claude-sonnet (implementation)
- **Hours:** 10-14
- **Context:** Per Q118. Expand parser beyond NAV-PVT to: NAV-STATUS, NAV-PVAT (attitude), NAV-RELPOSNED (relative positioning), UBX-ESF-RAW (IMU raw from RaceBox IMU). Test against captured RaceBox logs.

### MO-014 🔴 Strip local track mapping and sector math
- **Month/week:** M2/W7
- **Deps:** MO-006
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Per Q117. Remove on-device start/finish detection + sector logic. Clients send raw GPS; server does track-aware lap segmentation. Keep a cached sector-splits file for offline live dashboard display only.

### MO-015 🔴 Explicit "local saved" vs "cloud confirmed" badges
- **Month/week:** M2/W8
- **Deps:** MO-009
- **AI:** claude-design + claude-sonnet
- **Hours:** 4-6
- **Context:** Per audit. Session list shows two pills: "Local" (always), "Cloud" (when confirmed by server). Users know what's safe.

### MO-016 🔴 Persistent recording-state strip
- **Month/week:** M1/W4
- **Deps:** MO-004
- **AI:** claude-design
- **Hours:** 4-6
- **Context:** During recording, a sticky banner: "Recording — 24 min — 18 laps — GPS good". During finalize: "Finalizing…". During upload: "Uploading — 42%". Survives navigation.

### MO-017 🟡 Historical review on mobile (local only)
- **Month/week:** M2/W8
- **Deps:** MO-006
- **AI:** claude-design
- **Hours:** 8-10
- **Context:** Per Q119. Mobile can show: session list, summary metrics, lap list, simple trace. Deep analysis requires webapp handoff link.

### MO-018 🟡 Live dashboard polish
- **Month/week:** M2/W8
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** Per Q122. Live trackmap, lap time, speed trace, GPS line, g-g diagram. Trackside trust cues: GPS fix indicator, sample rate indicator, BLE connection status.

---

## Month 3 — Pairing + Coaching Surface

### MO-019 🔴 QR pairing with webapp
- **Month/week:** M3/W11
- **Deps:** WA-020, BE-006
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** User scans QR in webapp with phone camera → exchanges token for refresh token → app paired. Uses Clerk mobile SDK for token storage in keychain.

### MO-020 🔴 Rules engine client on mobile (lightweight)
- **Month/week:** M3/W10-11
- **Deps:** DT-010
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Port the rules engine logic from desktop to Swift. Or use the compiled rules as a portable DSL + run via an evaluator. Smaller rule subset than desktop (mobile focuses on real-life capture, fewer sim-specific rules).

### MO-021 🔴 Coaching prompts during real-life sessions
- **Month/week:** M3/W12
- **Deps:** MO-020
- **AI:** claude-design + claude-sonnet
- **Hours:** 6-8
- **Context:** Glanceable notifications / on-dashboard prompts driven by rules engine. Audio cue option (voice coach for hands-busy).

---

## Month 4 — Bridge Support + Stabilization

### MO-022 🟡 Bridge tab on mobile session detail
- **Month/week:** M4/W14
- **Deps:** WA-022
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** If session has a TransferLink, show minimal card "Sim equivalent: [session]" with CTA "View transfer report in webapp".

### MO-023 🟡 Stability + battery pass
- **Month/week:** M4/W15-16
- **AI:** claude-sonnet (profiling)
- **Hours:** 10-14
- **Context:** Instruments profiling, Energy Log analysis. Target: <12% battery/hour recording on iPhone 13+. Adaptive sensor throttling when battery <20%.

---

## Month 5 — Android + Wearables

### AN-001 🔴 Android project scaffold
- **Month/week:** M5/W17
- **Deps:** MO-004, MO-007, MO-009 (proven iOS patterns to port)
- **AI:** claude-opus (architecture) + claude-sonnet (implementation)
- **Hours:** 14-18
- **Context:** Kotlin 2.0, Jetpack Compose, Gradle version catalog. Mirror package structure from iOS. Use `KotlinxSerialization` with `@lap/schemas` Kotlin codegen (or hand-written + CI-enforced parity).

### AN-002 🔴 Android capture pipeline
- **Month/week:** M5/W17
- **Deps:** AN-001
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** `LocationManager` (FusedLocationProvider), `SensorManager` for IMU. Journal via Room (SQLite). Foreground service for recording (required on Android for continuous location).

### AN-003 🔴 Android RaceBox BLE
- **Month/week:** M5/W17-18
- **Deps:** AN-001
- **AI:** claude-sonnet
- **Hours:** 10-14
- **Context:** Kotlin BLE via `android.bluetooth.le` + coroutines. Port UBX parser from Swift.

### AN-004 🔴 Android upload queue
- **Month/week:** M5/W18
- **Deps:** AN-002
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** WorkManager for background uploads. Same idempotency contract as iOS.

### AN-005 🔴 Android UI parity (capture-only, no deep review)
- **Month/week:** M5/W18
- **Deps:** AN-002
- **AI:** claude-design
- **Hours:** 14-18
- **Context:** Compose UI: login, session list, capture dashboard, preflight, track picker. No deep review (per Q119 mobile stays capture-only for review).

### AN-006 🔴 Android beta release
- **Month/week:** M5/W20
- **AI:** codex
- **Hours:** 4-6
- **Context:** Google Play internal test track. Open beta by end of M5.

### WR-001 🔴 Apple Watch companion app
- **Month/week:** M5/W18
- **Deps:** MO-001
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Per Q120. WatchKit app that:
  - Samples heart rate via HealthKit
  - Streams wrist motion (a proxy for steering) via CoreMotion
  - Bluetooth-pairs with iPhone LAP app
  - Pushes samples to phone in real-time during recording
- **Acceptance:**
  - Watch and phone both show "Recording" state synced
  - Heart-rate samples arrive in phone's bundle
  - Battery drain on watch <10%/hr

### WR-002 🟡 WearOS companion
- **Month/week:** M5/W19
- **Deps:** AN-001, WR-001
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Parity with Apple Watch on WearOS. Compose for Wear. Wear Health Services for heart rate.

### MO-024 🔴 iOS V1 release
- **Month/week:** M5/W20
- **AI:** codex
- **Hours:** 4-6
- **Context:** App Store submission. TestFlight → Production.

---

## Month 6 — Stabilization + Cross-Platform Parity

### MO-025 🟡 Crash rate stabilization
- **Month/week:** M6/W21-22
- **AI:** claude-sonnet (Sentry analysis) + claude-opus (fixes)
- **Hours:** 15-25
- **Context:** Review Sentry issues ordered by frequency. Target: <0.5% crash-free users.

### AN-007 🟡 Android polish + Play Store submission
- **Month/week:** M6/W22
- **AI:** codex
- **Hours:** 4-6

### MO-026 🟡 Bug bash ongoing
- **Month/week:** M6 throughout
- **Hours:** 20-30

---

## Summary

| Month | Mobile hours | Key deliverable |
|---|---|---|
| M1 | 55-70 | P0 crash fixes + capture journal + Bundle v2 |
| M2 | 70-90 | Upload queue + timestamp normalization + RaceBox full + dashboard polish |
| M3 | 25-35 | QR pairing + mobile rules engine |
| M4 | 20-30 | Bridge cards + battery/stability |
| M5 | 115-150 | **Android scaffold + capture + upload + UI parity + Apple Watch + WearOS** |
| M6 | 40-60 | Stabilization + store submissions |
| **Total** | **~350 hours** | |

M5 is mobile-heavy by design (Android + wearables in one month is aggressive — consider slipping WearOS to M6 if Android port runs hot).
