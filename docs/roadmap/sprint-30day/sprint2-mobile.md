# LAP Mobile — Sprint 2 Queue (Android)

**Starts when:** Sprint 1 `sprint-mobile.md` drains.
**Covers:** Android crash stabilization + Play Store submission + Wear OS companion + battery/polish. Apple Watch deferred (Mac required).
**Total:** 90 tasks.

---

## Block A — Stabilization + crash triage (T001–T020)

- [ ] T001 [sonnet] Sentry dashboard audit: top-10 Android crashes from closed beta ⇒ list in commit
- [ ] T002 [sonnet] Fix crash: NPE in SessionCoordinator on rapid start/stop ⇒ resolved
- [ ] T003 [sonnet] Fix crash: BLE reconnect race on RaceBox disconnect-during-recording ⇒ resolved
- [ ] T004 [sonnet] Fix crash: LocationCaptureService not tearing down foreground notification on force-stop ⇒ resolved
- [ ] T005 [sonnet] Fix ANR: main-thread IO in journal writer ⇒ moved to coroutine
- [ ] T006 [sonnet] Fix ANR: synchronous network call during preflight ⇒ async
- [ ] T007 [sonnet] Fix leak: Room cursor not closed in UploadQueueDao.dequeueNext ⇒ resolved
- [ ] T008 [sonnet] Fix leak: Hilt scoped service holding Activity reference ⇒ resolved
- [ ] T009 [sonnet] Fix: foreground notification dismissible on Android 13+ ⇒ ongoing flag
- [ ] T010 [sonnet] Fix: dark-mode colors in preflight screen ⇒ corrected
- [ ] T011 [sonnet] Fix: landscape orientation breaks dashboard on some devices ⇒ tested on Pixel + Samsung + OnePlus
- [ ] T012 [sonnet] Fix: Deep-link from lap.com/pair opens but doesn't handle token correctly ⇒ resolved
- [ ] T013 [sonnet] Fix: RaceBox BLE cold-boot scan takes >30s on some devices ⇒ timeout + user cue
- [ ] T014 [sonnet] Fix: upload progress not updating when app is backgrounded ⇒ WorkManager status → notification
- [ ] T015 [sonnet] Fix: language picker doesn't persist across app restart ⇒ resolved
- [ ] T016 [sonnet] Fix: time-zone changes mid-session don't corrupt canonical timebase ⇒ tested
- [ ] T017 [sonnet] Fix: splash screen flash on Android 12+ ⇒ SplashScreen API
- [ ] T018 [sonnet] Fix: status bar color matches theme ⇒ edge-to-edge
- [ ] T019 [sonnet] Fix: accessibility announcement on recording start/stop ⇒ TalkBack correct
- [ ] T020 [sonnet] Crash-free users metric target ≥98.5% after this block ⇒ measured

## Block B — Play Store submission (T021–T040)

- [ ] T021 [design] Play Store listing assets: feature graphic, phone screenshots, tablet screenshots ⇒ ready
- [ ] T022 [design] App icon final (adaptive icon + round + legacy) ⇒ exported
- [ ] T023 [sonnet] Store listing copy: title, short description, long description ⇒ written
- [ ] T024 [sonnet] Localized listings: English + French ⇒ both written
- [ ] T025 [sonnet] Privacy policy URL + link in Play Store console ⇒ set
- [ ] T026 [sonnet] Data safety form: location-always + Bluetooth + motion disclosed ⇒ filled
- [ ] T027 [sonnet] Content rating questionnaire ⇒ completed → Everyone
- [ ] T028 [sonnet] Target audience: 18+ ⇒ selected
- [ ] T029 [sonnet] Ads declaration: none ⇒ selected
- [ ] T030 [sonnet] In-app purchase declaration: no (billing via Stripe web only) ⇒ noted
- [ ] T031 [sonnet] Signing key: Play App Signing enabled ⇒ configured
- [ ] T032 [sonnet] ProGuard final rules pass: keep reflection used by Room + Hilt + Kotlinx Serialization ⇒ release build works
- [ ] T033 [sonnet] Release build size target <25 MB ⇒ achieved
- [ ] T034 [sonnet] Internal test track upload: 3 internal testers invited ⇒ received app
- [ ] T035 [sonnet] Closed beta track upload: 20 beta users invited ⇒ received
- [ ] T036 [sonnet] Open beta track: public opt-in enabled ⇒ discoverable
- [ ] T037 [sonnet] App Review process: submit, respond to any reviewer questions ⇒ approved
- [ ] T038 [sonnet] Production release: staged rollout 5% → 20% → 100% ⇒ monitoring each
- [ ] T039 [sonnet] Play Console: reviews + crash reports monitored daily ⇒ dashboard set
- [ ] T040 [sonnet] Play Store SEO: keywords optimized ⇒ listing visible for "sim racing telemetry android"

## Block C — Wear OS companion (T041–T070)

- [ ] T041 [opus] Wear OS sub-module scaffold (`wear/`) with Wear-specific manifest ⇒ compiles
- [ ] T042 [opus] Minimum Wear OS version 4+ ⇒ configured
- [ ] T043 [opus] Wear app paired with phone app via Wearable Data Layer ⇒ connects
- [ ] T044 [opus] Data Layer message protocol: session start/stop events from phone → wear ⇒ tested
- [ ] T045 [opus] Heart-rate sensor via Health Services client ⇒ samples stream
- [ ] T046 [opus] Heart-rate data flows back to phone in real-time ⇒ received
- [ ] T047 [opus] Accelerometer on wrist (steering proxy) ⇒ samples stream
- [ ] T048 [opus] Wrist motion data to phone ⇒ received
- [ ] T049 [opus] Bundle-v2 writer includes wear-sourced samples ⇒ tested
- [ ] T050 [opus] Wear sample tagged `source_device="wear"` in provenance ⇒ tracked
- [ ] T051 [opus] Wear UI: current status (recording/idle), HR, session time ⇒ Compose for Wear
- [ ] T052 [opus] Wear complications: "LAP: Recording" on watch face ⇒ renders
- [ ] T053 [opus] Wear tile: quick-start session ⇒ works
- [ ] T054 [sonnet] Wear battery optimization: reduce sample rate when phone screen off ⇒ tested
- [ ] T055 [sonnet] Wear standalone fallback: if phone disconnected, wear keeps HR + wrist locally ⇒ tested
- [ ] T056 [sonnet] Wear reconnect on phone regain ⇒ syncs buffered samples ⇒ tested
- [ ] T057 [sonnet] Wear permission: body sensors + activity recognition ⇒ requested correctly
- [ ] T058 [sonnet] Wear app icon + branding ⇒ exported
- [ ] T059 [sonnet] Wear localization (en + fr) ⇒ stubbed
- [ ] T060 [sonnet] Wear a11y: large-font + TalkBack ⇒ works
- [ ] T061 [sonnet] Wear integration test: heart-rate flows to bundle end-to-end ⇒ green
- [ ] T062 [sonnet] Wear integration test: wrist motion flows ⇒ green
- [ ] T063 [sonnet] Wear Play Store listing: separate listing ⇒ drafted
- [ ] T064 [sonnet] Wear Play Store internal test ⇒ 3 testers
- [ ] T065 [sonnet] Wear production rollout: staged same as phone ⇒ monitored
- [ ] T066 [sonnet] Documentation: pairing flow for users ⇒ help article written
- [ ] T067 [sonnet] Onboarding: prompt user to install Wear companion ⇒ surfaces
- [ ] T068 [sonnet] Wear crash reporting via Sentry ⇒ wired
- [ ] T069 [sonnet] Benchmark: wear-added battery drain <5% additional per hour ⇒ measured
- [ ] T070 [sonnet] Apple Watch deferred note in user-facing help ⇒ "coming when macOS support lands"

## Block D — Battery + polish (T071–T090)

- [ ] T071 [sonnet] Battery profiler: 1h recording + BLE + upload ⇒ target ≤12%/hr
- [ ] T072 [sonnet] Battery profiler: 4h recording on endurance ⇒ target ≤12%/hr sustained
- [ ] T073 [sonnet] Adaptive sensor rates based on battery: <20% drops motion to 25Hz ⇒ tested
- [ ] T074 [sonnet] Doze mode compatibility: recording continues in doze ⇒ verified
- [ ] T075 [sonnet] Background restrictions: foreground service unaffected ⇒ verified on OEMs (Samsung, Xiaomi, OnePlus)
- [ ] T076 [sonnet] Thermal-throttling: if device overheats, reduce processing load ⇒ tested
- [ ] T077 [sonnet] OEM auto-kill whitelist instructions in help ⇒ written for top OEMs
- [ ] T078 [sonnet] Memory target: <300MB during recording ⇒ achieved
- [ ] T079 [sonnet] APK size <25MB release ⇒ achieved
- [ ] T080 [sonnet] Startup time <2s on mid-range device ⇒ achieved
- [ ] T081 [sonnet] Baseline profiler (App Startup optimization) ⇒ configured
- [ ] T082 [sonnet] R8 full mode enabled in release ⇒ tested
- [ ] T083 [sonnet] Final a11y audit: TalkBack full journey ⇒ passes
- [ ] T084 [sonnet] Final localization pass: all strings translated ⇒ 100%
- [ ] T085 [sonnet] Changelog updated ⇒ committed
- [ ] T086 [sonnet] Final smoke test on 5 devices ⇒ all green
- [ ] T087 [sonnet] Crash-free users target ≥99% post-V1 ⇒ measured
- [ ] T088 [sonnet] Documentation: Android setup guide ⇒ written
- [ ] T089 [sonnet] Documentation: RaceBox pairing guide ⇒ written
- [ ] T090 [sonnet] Documentation: Wear companion guide ⇒ written
