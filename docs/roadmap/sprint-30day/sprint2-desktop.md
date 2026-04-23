# LAP Desktop — Sprint 2 Queue

**Starts when:** Sprint 1 `sprint-desktop.md` drains.
**Covers:** M5 endurance refinement + target event display + auto-update + M6 perf + bug bash + release polish.
**Total:** 80 tasks (lighter because Sprint 1 covered most of desktop's 6mo scope).

---

## Block A — Endurance mode refinement (T001–T015)

- [ ] T001 [opus] Endurance overlay preset: stint timer, fuel runway, tire life, long-run pace reference ⇒ defined
- [ ] T002 [opus] Stint timer widget: elapsed stint time + projected end ⇒ Qt widget
- [ ] T003 [opus] Fuel runway widget: laps remaining on current fuel ⇒ tested
- [ ] T004 [opus] Tire life widget: estimate per compound + wear curve ⇒ tested
- [ ] T005 [opus] Long-run pace reference: rolling avg of last N laps vs target ⇒ rendered
- [ ] T006 [opus] Driver handoff metadata UI (read-only for v1): upcoming driver, ETA ⇒ displayed
- [ ] T007 [sonnet] Endurance-specific coaching prompts: "pace decay 0.3s/lap — check tire temps" ⇒ rule fires
- [ ] T008 [sonnet] Endurance mode binds strategy cadence: less aggressive, more conservative margins ⇒ tested
- [ ] T009 [sonnet] Endurance session split detection: auto-splits stints at pit events ⇒ tested
- [ ] T010 [sonnet] Stint summary overlay: post-stint popup "stint completed: 14 laps, avg 1:52.3" ⇒ shown
- [ ] T011 [sonnet] Pace-decay alert: if slope >threshold, coach card ⇒ fires
- [ ] T012 [sonnet] Endurance-specific bundle section in finalizer ⇒ tested
- [ ] T013 [sonnet] Tests: simulated 90-min session in endurance mode ⇒ all widgets update correctly
- [ ] T014 [sonnet] Documentation: `docs/ENDURANCE_MODE.md` ⇒ written
- [ ] T015 [sonnet] Preset export/import works for endurance ⇒ tested

## Block B — Target event integration (T016–T025)

- [ ] T016 [opus] Session-start UI fetches pinned target event from backend ⇒ tested
- [ ] T017 [opus] Display "Training for: iRacing Nürburgring 24h — in 12 days" header ⇒ rendered
- [ ] T018 [opus] Recommended focus: fetch top open ActionPrescription scoped to target-event's track/car ⇒ shown as banner
- [ ] T019 [sonnet] Session-start preset suggestion: "Use Endurance mode for this" based on target ⇒ offered
- [ ] T020 [sonnet] Event-context tag auto-applied to session manifest ⇒ tested
- [ ] T021 [sonnet] Event countdown in live overlay (compact) ⇒ optional widget
- [ ] T022 [sonnet] Post-event feedback form on next app-open ⇒ prompts user
- [ ] T023 [sonnet] Target-event history page in Settings ⇒ renders
- [ ] T024 [sonnet] Tests ⇒ green
- [ ] T025 [sonnet] E2E: pin event in webapp → open desktop → training-for header shows ⇒ green

## Block C — Auto-update mechanism (T026–T040)

- [ ] T026 [opus] Auto-update architecture design ⇒ ADR written
- [ ] T027 [opus] Version-check endpoint: `GET https://releases.lap-coach.racing/latest.json` returns semver + download-url + signature ⇒ mocked
- [ ] T028 [opus] Client version-check on app start + periodically ⇒ runs
- [ ] T029 [opus] Update-available notification in UI ⇒ rendered
- [ ] T030 [opus] Download to temp dir with progress ⇒ works
- [ ] T031 [opus] Signature verification via embedded public key ⇒ rejects tampered
- [ ] T032 [opus] Apply-on-next-launch: stage new binary, swap on restart ⇒ tested
- [ ] T033 [opus] Rollback: if new version crashes on first run, revert to prior ⇒ tested
- [ ] T034 [sonnet] Auto-update opt-out toggle in Settings ⇒ respected
- [ ] T035 [sonnet] Update channels: stable + beta ⇒ user can switch
- [ ] T036 [sonnet] Release notes fetched alongside update ⇒ shown post-install
- [ ] T037 [sonnet] Update failures: surfaced via UI + Sentry ⇒ tested
- [ ] T038 [sonnet] Bandwidth consideration: schedule large downloads only on WiFi ⇒ optional
- [ ] T039 [sonnet] Tests: simulated update flow end-to-end ⇒ green
- [ ] T040 [sonnet] GitHub Actions release workflow: tag → builds → uploads → updates latest.json ⇒ CI green

## Block D — Performance pass (T041–T060)

- [ ] T041 [sonnet] Profile overlay rendering with 10 widgets under max telemetry rate ⇒ baseline captured
- [ ] T042 [sonnet] Reduce overlay VM update frequency where not needed ⇒ CPU drops
- [ ] T043 [sonnet] Cache computed values in coaching card rendering ⇒ fewer re-renders
- [ ] T044 [sonnet] Profile rules engine per-sample overhead: target <0.5ms ⇒ achieved
- [ ] T045 [sonnet] Profile session write throughput: can it handle 100 Hz IMU + 10 Hz GPS? ⇒ tested
- [ ] T046 [sonnet] Profile memory during 2-hour session: target <500MB residue ⇒ achieved
- [ ] T047 [sonnet] App startup target <3s on SSD with cold cache ⇒ achieved
- [ ] T048 [sonnet] QML shader compilation: warm cache on first launch ⇒ done
- [ ] T049 [sonnet] Python GIL audit: any blocking work on main thread ⇒ moved off
- [ ] T050 [sonnet] File I/O: finalizer writes parallelized where safe ⇒ faster
- [ ] T051 [sonnet] Bundle upload: chunks streamed, not loaded whole in memory ⇒ low-mem
- [ ] T052 [sonnet] Config save debounce: max 1 write per 5s ⇒ tested
- [ ] T053 [sonnet] Overlay preset switching target <200ms ⇒ achieved
- [ ] T054 [sonnet] Live-page data refresh rate caps at 30Hz UI / 100Hz data ⇒ tested
- [ ] T055 [sonnet] Background tasks: sync uploads, log rotation, rules bundle refresh ⇒ isolated
- [ ] T056 [sonnet] Race scenario test: iRacing at 60fps + all overlays + coaching ⇒ sim fps unaffected
- [ ] T057 [sonnet] Resource quotas: CPU <15%, RAM <500MB during idle ⇒ checked
- [ ] T058 [sonnet] Profile on lower-end hardware: Ryzen 5 baseline ⇒ acceptable
- [ ] T059 [sonnet] Telemetry sample drop detection: alert user if drops >1% ⇒ UI surface
- [ ] T060 [sonnet] Final performance report committed to docs ⇒ written

## Block E — Bug bash + release (T061–T080)

- [ ] T061 [sonnet] Sentry triage: top 10 recurring issues ⇒ fixed
- [ ] T062 [sonnet] User-reported bugs from closed beta: triaged ⇒ addressed
- [ ] T063 [sonnet] Edge case: iRacing crashed during recording → coordinator handles ⇒ tested
- [ ] T064 [sonnet] Edge case: ACC crashed → graceful ⇒ tested
- [ ] T065 [sonnet] Edge case: Windows sleep mid-recording → resumes or finalizes ⇒ tested
- [ ] T066 [sonnet] Edge case: disk full during finalize → clear error, preserve partial ⇒ tested
- [ ] T067 [sonnet] Edge case: network drops mid-upload → queue resumes on reconnect ⇒ tested
- [ ] T068 [sonnet] Edge case: Clerk auth expired during session → continues offline, re-auths on finalize ⇒ tested
- [ ] T069 [sonnet] Edge case: time zone change mid-session ⇒ canonical timebase preserved
- [ ] T070 [sonnet] Edge case: summer-time DST during session ⇒ no glitch
- [ ] T071 [sonnet] Installer signing: EV cert applied (or self-signed with clear warning) ⇒ done
- [ ] T072 [sonnet] Installer tested on Win 10 + Win 11 fresh install ⇒ both work
- [ ] T073 [sonnet] Uninstaller cleans registry + files fully ⇒ verified
- [ ] T074 [sonnet] Migration: v1→v2 config.json path ⇒ tested
- [ ] T075 [sonnet] Migration: v1→v2 bundle format ⇒ tested
- [ ] T076 [sonnet] Release checklist automation via GitHub Actions ⇒ script
- [ ] T077 [sonnet] Release notes template ⇒ committed
- [ ] T078 [sonnet] V1 GitHub Release draft created with installer attached ⇒ ready
- [ ] T079 [sonnet] Changelog.md Sprint 2 entries ⇒ written
- [ ] T080 [sonnet] Final README polish with install + first-session flow ⇒ reviewed
