# LAP — Desktop Task Backlog

**Repo:** `lap-coach-logger` (existing, already on Windows, Qt/QML + Python)
**Stack:** Python 3.12, PyQt6 / QML 6, pyirsdk for iRacing, ACC shared-memory, Pydantic v2 for session bundles, PyInstaller for distribution, Inno Setup for installer.
**Task format:** `DT-NNN`.

---

## Month 1 — P0 + Contract Integration

### DT-001 🔴 Fix `live_telemetry_processor` import break (rip-and-rebuild)
- **Month/week:** M1/W1
- **Deps:** none
- **AI:** claude-opus (architecture) + claude-sonnet (implementation)
- **Hours:** 12-16
- **Context:** Per Q103 + audit P0. `live_telemetry_processor.py` imports `live_coach`, `live_dashboard`, `live_input_diagnostics` modules that don't exist. Rip and rebuild:
  - Delete references to missing modules
  - Define a `LiveProcessor` interface with slots: `on_sample`, `on_lap_end`, `on_session_end`
  - Implement `CoachingLiveProcessor` that just emits detector events (existing `live_detectors.py` primitives)
  - Implement `DashboardLiveProcessor` that exposes normalized snapshots for VM
  - Gate by feature flag so we can disable if something's broken live
- **Acceptance:**
  - `pytest tests/` green (previously blocked)
  - App boots cleanly with sim active, sees live overlays update

### DT-002 🔴 Fix `qml_bootstrap` test collection
- **Month/week:** M1/W1
- **Deps:** DT-001 (may share root cause)
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** `TypeError: 'property' object is not callable` at collection. Likely a Python 3.12 + PyQt6 property mismatch. Fix + add a smoke test that confirms QML can load all VM classes.

### DT-003 🟡 CI green gate — merge-blocking
- **Month/week:** M1/W1
- **Deps:** DT-001, DT-002
- **AI:** codex
- **Hours:** 2-3
- **Context:** Add GitHub Action that blocks merge if `pytest -q` or `mypy` fail. Precommit hook too.

### DT-004 🔴 Install `@lap/schemas` Python types
- **Month/week:** M1/W2
- **Deps:** BE-002
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Desktop app imports `SessionManifest`, `SessionRecord`, `TelemetrySample` from the shared package instead of local Pydantic duplicates.

### DT-005 🔴 Bundle v2 writer (replace existing `SessionFinalizer`)
- **Month/week:** M1/W4
- **Deps:** DT-004
- **AI:** claude-opus
- **Hours:** 12-14
- **Context:** Current `SessionFinalizer` writes a v1-ish bundle. Rewrite to emit canonical Bundle v2 per ADR-006. Includes: manifest JSON, telemetry parquet, laps parquet, events JSON, channels metadata, quality report, checksums. Atomic temp → final rename preserved.
- **Acceptance:**
  - New bundles pass `lap_schemas.v1.session.SessionManifest.model_validate()` server-side
  - Old sessions can be reprocessed via admin flow

### DT-006 🔴 Upload client to new `/api/v1/sessions/ingest`
- **Month/week:** M1/W4
- **Deps:** DT-005, BE-007
- **AI:** claude-sonnet
- **Hours:** 8-10
- **Context:** Replace current upload path with new typed client. Streams chunks. Honors `Idempotency-Key` (generated UUIDv7 per session). Resumable if network drops (chunk-level retry).

### DT-007 🟡 Remove placeholder review actions
- **Month/week:** M1/W3
- **Deps:** none
- **AI:** codex
- **Hours:** 2-3
- **Context:** Per audit: review page has "to be wired later" buttons. Either wire them (Reprocess, Export) or hide them. Per Q95 desktop review stays small, so hide Export (→ webapp) and wire Reprocess (→ backend endpoint).

### DT-008 🔴 Sentry integration
- **Month/week:** M1/W4
- **Deps:** DT-001
- **AI:** codex
- **Hours:** 2-3
- **Context:** `sentry_sdk` with Qt integration. Captures Python exceptions, uploads crash dumps.

### DT-009 🔴 PostHog integration
- **Month/week:** M1/W4
- **Deps:** DT-001
- **AI:** codex
- **Hours:** 2-3
- **Context:** `posthog-python`. Track events: `app_started`, `session_captured`, `overlay_toggled`, `mode_switched`.

---

## Month 2 — Rules Engine + Live Coaching Rewrite

### DT-010 🔴 Rules engine client (per ADR-009)
- **Month/week:** M2/W7
- **Deps:** BE-017, DT-001
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Client-side rules engine that loads compiled rules from server at session start (or from 7-day cache). Executes during live session. Emits coaching events consumed by overlay VM.
- **Acceptance:**
  - Matches server behavior on shared test fixtures (identical insights produced)
  - <1ms overhead per sample
  - Graceful degradation: if cache expired and offline, falls back to last-known rules

### DT-011 🔴 Rules cache
- **Month/week:** M2/W7
- **Deps:** DT-010
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Fetch compiled rules bundle at login. Cache to disk. TTL 7 days. Force-refresh on app update.

### DT-012 🔴 Overlay VM integration — coaching cards from rules
- **Month/week:** M2/W7-8
- **Deps:** DT-010
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** `OverlayViewModel` consumes `CoachingInsight` stream from engine, renders cards with explanation templates (beginner/intermediate/advanced per user level from settings).

### DT-013 🟡 Submit finalized bundles with live insights included
- **Month/week:** M2/W8
- **Deps:** DT-005, DT-010
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** Live-generated insights serialized into bundle. Server can use them (tagged as client-generated, lower trust) or overwrite with server-side authoritative insights.

---

## Month 3 — Mode System

### DT-014 🔴 Mode engine (Practice / Sprint / Endurance / Review)
- **Month/week:** M3/W11
- **Deps:** DT-001
- **AI:** claude-opus
- **Hours:** 14-18
- **Context:** Per Q96 — full architecture in 6 months. Explicit `Mode` abstraction. Each mode binds to:
  - Overlay preset (different widget set)
  - Coaching cadence (Practice: verbose, Race: minimal; Review: none)
  - Strategy assumptions (safety margins, fuel buffers)
  - Session tagging (auto-tag `environment_tag` on finalize)
- **Acceptance:**
  - Mode switch changes overlay stack within 1 frame
  - Coaching cadence visibly differs between modes
  - Session recorded in Practice mode gets `environment_tag: sim_practice` server-side

### DT-015 🔴 Overlay catalog reorganization
- **Month/week:** M3/W11
- **Deps:** DT-014
- **AI:** claude-sonnet + claude-design
- **Hours:** 10-12
- **Context:** Per Q98. Keep all widgets. Move streamer-oriented widgets to "Advanced / Streamer" category behind a toggle. Race-minimal default preset: 8-10 core widgets only (lap delta, fuel, tires, coaching card, position, flag status, sector color, gap to leader).
- **Acceptance:**
  - New install shows race-minimal preset by default
  - Streamer widgets still available but not visible unless user enables

### DT-016 🟡 Degraded-state UX
- **Month/week:** M3/W12
- **Deps:** DT-010
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** Per Q99. If processor/coaching/strategy/telemetry/sync fails, visible banner + safe fallback. No silent degradation. Q99 said "prevent via data reconstruction" — we still need UX for when reconstruction fails.

### DT-017 🟡 Review page: small summary + "open in webapp" CTA
- **Month/week:** M3/W11
- **Deps:** DT-005
- **AI:** claude-design
- **Hours:** 4-6
- **Context:** Per Q95. After session ends, desktop shows compact debrief card: key metrics, 1-2 top insights. Primary button: "See full analysis in webapp".

---

## Month 4 — Strategy + Pit-Armed

### DT-018 🔴 Pit-call "armed" signal
- **Month/week:** M4/W13
- **Deps:** DT-014
- **AI:** claude-sonnet
- **Hours:** 8-10
- **Context:** Per Q97. Single state: "armed" vs "not armed". Strategy widget shows armed when fuel/tire model suggests a pit window. User can manually arm. Arming changes overlay color/sound. No full state machine (deferred).

### DT-019 🔴 Live driver decision prompts
- **Month/week:** M4/W13-14
- **Deps:** DT-014, DT-010
- **AI:** claude-opus
- **Hours:** 10-12
- **Context:** Per Q100. Prompts for: pit, save fuel, push, cool tires, focus corner X (recurring mistake), traffic, target pace hold, accident ahead. Each prompt sourced from a rule + live context. Minimal-click acknowledgment.

### DT-020 🔴 Strategy plan vs actual serialization
- **Month/week:** M4/W14
- **Deps:** BE-041
- **AI:** claude-sonnet
- **Hours:** 6-8
- **Context:** Per Q102. Pre-race plan + actual pit events + execution delta serialized into bundle. Visible in webapp review.

### DT-021 🟡 Plan-vs-actual review on desktop
- **Month/week:** M4/W14
- **Deps:** DT-020
- **AI:** claude-design
- **Hours:** 6-8
- **Context:** Desktop review page shows "you planned X, actual was Y" summary. Full view still on webapp.

---

## Month 5 — V1 Polish + Endurance

### DT-022 🔴 Endurance mode refinement
- **Month/week:** M5/W18
- **Deps:** DT-014
- **AI:** claude-opus
- **Hours:** 8-10
- **Context:** Endurance overlay preset: stint timer, fuel runway, tire life estimate, driver handoff affordance (metadata only — no multi-user UX), long-run pace reference.

### DT-023 🔴 Target event display in session-start UI
- **Month/week:** M5/W19
- **Deps:** BE-040
- **AI:** claude-sonnet
- **Hours:** 4-6
- **Context:** If user pinned a target event in webapp, desktop session-start shows "training for: \[Event\]" + recommended focus (from most impactful open WeaknessEpisode).

### DT-024 🔴 V1 installer polish
- **Month/week:** M5/W20
- **AI:** codex
- **Hours:** 4-6
- **Context:** Inno Setup: code signing, auto-update mechanism check, clean uninstall.

### DT-025 🟡 Auto-update mechanism
- **Month/week:** M5/W20
- **AI:** claude-opus
- **Hours:** 10-14
- **Context:** On app start, check for new version; if yes, download + apply on next launch. Signed updates only.

---

## Month 6 — Stabilization

### DT-026 🟡 Performance pass
- **Month/week:** M6/W22
- **AI:** claude-sonnet
- **Hours:** 8-10
- **Context:** Profile overlay rendering, telemetry processor, rules engine. Target: CPU <15% on 6-core baseline with full overlay set.

### DT-027 🟡 Bug bash
- **Month/week:** M6 throughout
- **Hours:** 15-25

---

## Summary

| Month | Desktop hours | Key deliverable |
|---|---|---|
| M1 | 50-65 | P0 fixes + Bundle v2 + ingest integration |
| M2 | 30-40 | Rules engine client + live coaching rewrite |
| M3 | 35-45 | Mode system + overlay reorg |
| M4 | 30-40 | Pit-armed + decision prompts + plan/actual |
| M5 | 25-35 | Endurance + V1 installer |
| M6 | 25-35 | Performance + bugs |
| **Total** | **~200 hours** | |
