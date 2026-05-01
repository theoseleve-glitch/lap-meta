# Cycle 216 Forced-Checkpoint Adjudication

**Trigger**: Review-loop cycle 216 (`2bc76e9`, 2026-04-27 19:16Z) PAUSED on 15 sprint commits matching `loop-review.md:344-345` — *"any change to `lap-backend/app/auth/*` or `lap-backend/app/billing/*`; any diff touching cryptographic code, token handling, or payment flow."*

**Audit performed**: 2026-04-28 by 3 parallel specialist sub-agents (security-auditor on mobile-auth, security-architect on schemas RBAC + billing, pii-detector on telemetry opt-out).

---

## TL;DR

**Verdict: lift the cycle-216 PAUSE on all 15 commits.** No CRITICAL or HIGH findings. The forced-checkpoint surface is structurally well-formed: token-storage substrate is uniform (Tink AES256-GCM, Keystore-rooted MasterKey), zero token-leakage to logs/analytics, RBAC role taxonomy disambiguates `OrgInviteRole` ⊂ `OrgRole` so privilege-escalation-via-invite is structurally impossible, billing tier expansion is a closed-set additive change with no client-side pricing leakage, and the telemetry opt-out commit is a correct addition over already-shipped T222/T223 telemetry (not a new privacy regression).

Two MED-severity follow-ups are pre-launch concerns but **not c216-rework gates**:
1. T164 email case-fold mismatch (`Alice@x.com` invite ≠ `alice@x.com` user → 403 at accept-time).
2. T224 telemetry — `TelemetryOptOutToggle` is unmounted dead code; SDK auto-context (device-id, IP, OS) is not gated by the decorator; default-ON without consent banner is GDPR-questionable.

Three non-blocking schema-side cleanups (drop invitation `token` from response when email-send lands; Kotlin codegen sweep before mobile org-aware UI; ADR for token-write atomicity pattern that repeats across 4 auth use cases).

**Net**: 8 ACCEPT + 6 ACCEPT_WITH_NOTE (LOW) + 1 ACCEPT_WITH_NOTE (LOW with one MED gap, T224). Zero NEEDS_REWORK / REVERT. *(T164's MED severity resolved during adjudication — see `4d36b0b`.)*

---

## Background — what triggered c216

Cycle 216 ended a 60-cycle review-idle drought (c155–c215). All 5 review repos resumed simultaneously with 301 unreviewed sprint commits queued. **15** of those 301 hit the runbook's forced-checkpoint criteria (`loop-review.md:344-345`):

| Surface | Repo | Tasks | Count |
|---|---|---|---|
| Auth (token-handling) | lap-mobile-android | T176, T177, T184, T185, T186, T187, T188, T189, T190 | 9 |
| RBAC (authorization model) | lap-schemas | T163, T164, T165, T167 | 4 |
| Payment (billing tier) | lap-schemas | T177 | 1 |
| Privacy (telemetry opt-out) | lap-mobile-android | T224 | 1 |

The remaining 286 unreviewed commits do **not** require human adjudication and can be processed by the autonomous review loop on resume.

---

## Surface 1 — Mobile auth (9 commits)

| SHA | Task | Verdict | Severity | Finding | Action |
|---|---|---|---|---|---|
| `8d816e8` | T176 Apple-sign-in via Clerk | ACCEPT_WITH_NOTE | LOW | Apple JWS verification delegated to Clerk/backend (`AppleCredentialExchanger`) — correct for v1. T176 landed Apr 27, AFTER T190 (Apr 25), so `AuthFlowsIntegrationTest` does not yet cover Apple-flow composition. | Lift; extend integration test next auth touch. |
| `d09c710` | T177 Magic-link | ACCEPT_WITH_NOTE | LOW | Token format intentionally opaque to kernel (good). Same chronological gap as T176 — landed after T190. | Lift; same follow-up. |
| `a13876d` | T184 DeepLinkRouter (`lap://pair`) | ACCEPT | NONE | Filter scoped tight (scheme=lap, host=pair only). `lap://settings` routes to `Unknown` — no scheme overload. `autoVerify="false"` correct on non-https. | Lift. |
| `bb29430` | T185 App Links autoVerify | ACCEPT | NONE | `autoVerify="true"` on https only with `pathPrefix=/pair`. assetlinks fingerprint requirement (debug + release + Play App Signing) documented at `AppLinksConfig.kt:21-27`. | Lift; **must** confirm `assetlinks.json` hosted before any release build (silent chooser-fallback on missing fingerprints). |
| `0f10d2d` | T186 SessionExpired modal | ACCEPT | NONE | Local-data preservation enforced **structurally** at `SessionExpiredPolicy.kt:67-72` — constructor takes only `SecureTokenStorage`, physically can't drop DB. User-initiated-logout flag distinguishes from T175. | Lift. |
| `9dbd03a` | T187 AccountRepository | ACCEPT | NONE | `AccountId("active")` placeholder is process-local; storage is per-app per-user-profile (Android sandbox), no cross-install leakage. `isNotBlank` invariant defends against partial-write/restored-backup. | Lift. |
| `6981acf` | T188 BiometricLockPolicy | ACCEPT | NONE | Toggle uses regular SharedPreferences with `apply()`; biometric template lives in OS Keystore (never in app); default-OFF is documented v1 stance. `unlockedThisProcess` re-prompt-on-process-death only is acknowledged trade. | Lift. |
| `871bd99` | T189 SyncMeProfileUseCase | ACCEPT | NONE | Cache-untouched-on-Unauthorized correct (clearing belongs in T186's `HandleSessionExpired`). InMemory v1 cache → stale-on-account-switch concern moot (process-local, restart drops). `@Synchronized` adequate for read-mostly workload. | Lift. |
| `65c00e8` | T190 AuthFlows integration tests | ACCEPT | NONE | Cross-kernel composition tests share ONE storage fake across pair / logout / expired / refresh-rotation / re-pair / invalid / blip — the substrate-drift class. Instrumented test exercises real Tink AES256-GCM + Keystore via `EncryptedTokenStorageInstrumentedTest`. | Lift; run `./gradlew app:connectedDevDebugAndroidTest` once CI has a device. |

### Token-handling substrate (verified clean)

- `SecureTokenKeys.ACCESS_TOKEN = "auth.access_token"` and `REFRESH_TOKEN = "auth.refresh_token"` defined **once** at `app/src/main/kotlin/com/lap/mobile/auth/SecureTokenStorage.kt:47-48`. All 9 commits + T173/T174/T175/T179 read/write via these constants.
- Backed by `EncryptedPreferencesTokenStorage` (Tink AES256-SIV keys / AES256-GCM values, MasterKey from Android Keystore — TEE/StrongBox where available), `commit()` for synchronous durability on token writes.
- **Zero** `Sentry.capture*`, `posthog.capture`, `Timber.[ed]`, `Log.[wedi]`, `println`, `track`, or `breadcrumb` calls anywhere under `app/src/main/kotlin/com/lap/mobile/auth/`, `account/`, or `deeplink/`.
- Atomicity preserved across all 4 token-writing paths (T174 silent-refresh, T179 pair, T177 magic-link verify, T176 Apple exchange): both halves written before `Authenticated` returned; pre-existing tokens preserved on every non-Success path.
- **Production wiring landed**: only `bb29430` (T185 manifest filter) and `a13876d` (T184 manifest filter) ship runtime-active surface. `6981acf` (T188) lands `AuthModule.bindBiometricLockPreference` as the only active DI addition. Everything else is kernel-only with explicit `[PENDING: device-required]` HTTP impls — no `@Binds` for `AppleAuthProvider`, `AppleCredentialExchanger`, `MagicLinkSender`, `MagicLinkVerifier`, or `MeProfileFetcher` (verified at `AuthModule.kt`).

### Top-3 device-only invariants (gating any release build)

1. **EncryptedSharedPreferences round-trip survives process death + restart on real Android Keystore.** Verify (a) MasterKey instantiates on a TEE-equipped device without falling back to software keystore, (b) `commit()` write of refresh token survives `Process.killProcess` and reads back identically, (c) `clear(ACCESS_TOKEN)` leaves `REFRESH_TOKEN` intact through Tink's deterministic key encryption — the substrate T174's silent-refresh + T175's logout both depend on. Test: `./gradlew app:connectedDevDebugAndroidTest -Pandroid.testInstrumentationRunnerArguments.class=com.lap.mobile.auth.EncryptedTokenStorageInstrumentedTest` on a Pixel-tier device with StrongBox.
2. **App Links autoVerify against the actually-hosted `assetlinks.json`.** Until `https://app.lap-coach.racing/.well-known/assetlinks.json` serves the JSON documented at `AppLinksConfig.kt:21-39` containing all THREE SHA256 fingerprints (debug + release upload + Play App Signing), the OS falls back to chooser silently. Verify: `adb shell pm get-app-links com.lap.mobile`. The Play App Signing fingerprint is the one that breaks if forgotten — Play resigns the APK with its own key.
3. **BiometricPrompt callback timing for `unlockedThisProcess`.** The kernel is JVM-pure but real-world correctness depends on the Android shell flipping the flag exclusively on `onAuthenticationSucceeded` (not `onAuthenticationError` cancellation, not `onAuthenticationFailed` for partial bio-match). Verify capability-detection (`BiometricManager.canAuthenticate()`) greys the toggle on no-sensor emulator without removing it.

---

## Surface 2 — Schemas RBAC + billing (5 commits)

| SHA | Task | Surface | Verdict | Severity | Finding | Action |
|---|---|---|---|---|---|---|
| `e31ce52` | T163 Organization + OrganizationCreate | RBAC | ACCEPT_WITH_NOTE | LOW | `seats_limit` is caller-asserted (no max-cap, no plan-tier coupling). Caller could create a `free` org with `seats_limit=10000`; safety lives in backend, not schema. | Lift; track plan↔seats coupling as schema-layer enrichment. |
| `b152fcf` | T164 OrganizationInvitation + OrgInviteRole | RBAC | ACCEPT | NONE (was MED) | ~~Email regex did no case-fold; backend case-sensitive equality at accept-time → 403.~~ **Fixed in `4d36b0b` (2026-04-28) — `@field_validator(mode='before')` on `OrganizationInvitationCreate.email` strips + lowercases at the boundary; 3 new tests in `tests/test_organization.py`; openapi.json unchanged.** | Lift. |
| `51ecbdd` | T165 OrganizationMembership | RBAC | ACCEPT | LOW | `OrganizationMembership.role: OrgInviteRole` correctly excludes `admin` — solid disambiguation. `frozen=True` makes wire payload immutable. | Lift. |
| `2c391c6` | T167 OrgRole + OrganizationMemberEntry + List | RBAC | ACCEPT | NONE | `OrgRole` ⊃ `OrgInviteRole` cleanly typed. List response is the only place `admin` flows on the wire — privilege-escalation surface is structurally absent in invite/membership shapes. | Lift. |
| `b311dd8` | T177 BillingPlan B2B tiers | Payment | ACCEPT_WITH_NOTE | LOW | Closed Literal expansion is forward-compatible for Python consumers; **breaking change for Kotlin/Swift exhaustive `when`** if/when codegen runs. No price/amount fields leaked to client. | Lift; ensure Kotlin/Swift parity regen lands before mobile B2B work. |

### RBAC implementability

The schema layer carries the right structural safeties for FastAPI consumers:
- `extra="forbid"` on every model (`organization.py:49,57,86,94,101,118,142,151`) blocks request-body smuggling — a mobile client **cannot** inject `admin_user_id` or `role=admin` into `OrganizationCreate`.
- `OrganizationInvitationCreate.role: OrgInviteRole = Literal["coach", "driver"]` (`organization.py:97`) is **the single most important RBAC invariant in this batch** — it makes admin-elevation-via-invite structurally impossible at the schema boundary, not at the router. Backend `app/routers/organizations.py:344` flows `body.role` straight into the DB row trusting that constraint.
- All FK fields explicitly typed `UUID7`. `frozen=True` on response models locks wire-payload immutability.

Gaps requiring backend code (cannot live in schema):
- **Default-deny for `seats_limit`** — current `Field(ge=1)` requires caller to specify; plan-tier-to-seats translation lives in backend Stripe glue.
- **Invitation lifecycle** — `accepted_at` / `revoked_at` are server-side fields on `OrgInvitationRow`; schema response is "pending invitation" only. Correct.
- **Cross-org leakage prevention** is purely backend-enforced — schema models have explicit `org_id: UUID7` foreign keys but cannot stop a backend router from returning org-B data; backend at `organizations.py:516-531,575-588` does correctly enforce caller-membership checks with status-parity 403s.

### Billing tier risk

- Forward-compatible at the wire level — adding three new variants to a `Literal` is a strict superset; existing Python consumers keep working, mypy flags exhaustive matches.
- **No pricing/amount fields exposed.** Schema is purely a `plan_id` symbol that backend translates to a Stripe `price_id` server-side (`billing.py:1-17` docstring is explicit) — no client-asserted-pricing bypass.
- Trial/proration **not** piggybacked here. T178 (30-day trial) and T168 (proration) are separate backend commits that read `BillingPlan` rather than mutating its shape.
- **Risk window**: Kotlin/Swift exhaustive-`when` breakage on next codegen. Currently no Kotlin `BillingPlan` exists (org/billing surface not yet codegen'd to Kotlin).

### Python-Kotlin parity

**Zero Kotlin parity for any of the 5 commits.** Kotlin generated sources end at `TransferLink.kt` / `WeaknessEpisode.kt` etc. — no `Organization*`, `OrgRole`, `OrgInviteRole`, `OrganizationMembership`, `OrganizationMemberEntry`, `BillingPlan` files. **Sustainable for ~3-5 cycles** because (a) mobile Android does not yet have org-management UI in scope (these are coach/admin web flows; mobile is driver-side), (b) datalogger doesn't touch billing or RBAC. Risk window opens when **driver-side mobile starts reading "which org am I in"** to scope coach feedback / session sharing — Kotlin needs `OrgRole` and likely `OrganizationMembership` (read-only) within 1-2 cycles after that.

---

## Surface 3 — Telemetry opt-out (1 commit)

| SHA | Task | Verdict | Severity | Finding | Action |
|---|---|---|---|---|---|
| `af26a35` | T224 Telemetry opt-out toggle + decorators | ACCEPT_WITH_NOTE | LOW (with one MED gap) | Decorator pattern is sound, runtime-immediate, well-tested. **`TelemetryOptOutToggle` Compose leaf is unmounted (no Settings screen imports it) — ships as dead code.** SDK auto-context (device-id, IP, OS) is not gated by decorator. Default-ON without consent banner is GDPR-questionable for EU. | Lift; bundle pre-launch follow-ups (see below). |

### What's correct in T224

- `OptOutAwareSentryReporter` and `OptOutAwareAnalyticsReporter` gate every interface method on a per-call `isOptedOut()` check — runtime flips immediate, locked by 11 JVM tests.
- All Sentry/PostHog SDK direct calls are confined to `SentrySdkReporter.kt:27/31/35` and `PostHogAnalyticsReporter.kt:27/29` — no other call site bypasses the wrapper interface.
- Timber → ReleaseLoggingTree → SentryReporter chain (`Logging.kt:32`) **is** properly wrapped via the injected `OptOutAwareSentryReporter`.
- SharedPreferences (non-encrypted) for opt-out flag is correct (UX flag, not credential; Android per-app sandbox is the trust boundary).

### What's transmitted today (PII assessment)

Three explicit emission paths exist in app code:
- `LapApplication.onCreate` → `app_started` (no properties).
- `SessionCoordinator.start:138-141` → `session_started` with `{session_id: <uuid>}`.
- `SessionCoordinator.stop:186-192` → `session_finalized` with `{session_id, sample_count}`.
- `UploadBundleWorker.kt:41` → `upload_completed`.

**No** email, displayName, userId/account_id, IP coordinates, GPS, lap data, telemetry samples, or device hardware ID in app-level emissions — only locally-generated `session_id` UUIDs and counts.

**However, SDK auto-context is sent regardless of decorator:**
- PostHog auto-attaches `$device_id` (install UUID), `$ip` (server-side), `$app_version`, `$os_version`, `$device_manufacturer`, `$device_model`, `$lib`, `$lib_version`, `$timezone` to every event.
- Sentry auto-attaches OS, device-class, locale, app-state, plus default breadcrumbs (network/lifecycle).

The toggle's *"anonymous"* wording is defensible in a US/CCPA frame (no user-supplied identifier sent) but the SDK auto-context sends a fingerprintable device-class + IP, which under EU DPA interpretation is personal data.

### Coverage gaps in T224

1. **Unmounted toggle UI** — `TelemetryOptOutToggle.kt` is defined but no Settings screen imports it. Grep on `TelemetryOptOutToggle` returns only the file itself. The decorator works, but a user has no way to flip it. (MED — dead code at point of release.)
2. **SDK init is unconditional** — `SentryAndroid.init` and `PostHogAndroid.setup` run whenever DSN/api-key valid, regardless of opt-out state. Native crash handler, ANR detector, app-lifecycle telemetry, install/session beacons still flow when user is "opted out at the decorator level". T224 does **not** call `Sentry.close()`, set `options.isEnabled=false`, or `PostHog.optOut()`.
3. **First-launch race** — `track(APP_STARTED)` fires unconditionally in `onCreate` before the user can possibly toggle anything; PostHog's install event queues during `setup()`. A user who opens the app once will always have one `app_started` + one `$identify` of install_id reach PostHog, even if they immediately uninstall.
4. **Sentry `configureSentryOptions`** (`SentryConfig.kt:52-65`) sets only DSN/environment/release/debug/sampleRate — auto-instrumentation (ANR, native crashes, app-lifecycle/network breadcrumbs, screen tracking) is left at SDK defaults.

### GDPR/CCPA stance

LAP's marketing is EU-targeted (per ADR-019:768 the "GDPR persistence" watch). **Default-ON without first-launch consent prompt is non-compliant under GDPR Art. 6/7 strict interpretation** (consent must be affirmative opt-in for non-essential analytics; legitimate-interest is contestable for product analytics). Under CCPA, default-ON with discoverable opt-out is acceptable, but the toggle being **dead-code (unmounted)** breaks even that bar.

---

## Cross-cutting follow-ups

### Pre-launch blocking (must land before public store release)

| ID | Action | Surface | Owner |
|---|---|---|---|
| FU-1 | Mount `TelemetryOptOutToggle` into Settings/Privacy screen | mobile T224+ | sprint-mobile |
| FU-2 | Add `Sentry.close()` / `options.isEnabled=false` re-init + `PostHog.optOut()` on opt-out flip — gate SDK auto-context, not just our wrapper | mobile T224 | sprint-mobile |
| FU-3 | Write **ADR-020: Mobile telemetry default policy** (default-OFF + onboarding consent **OR** default-ON + first-launch consent banner) | docs | manual |
| FU-4 | Disable Sentry default PII context (`isSendDefaultPii=false`, narrowed breadcrumbs) in `SentryConfig.configureSentryOptions` | mobile T224 follow-up | sprint-mobile |
| FU-5 | Verify `https://app.lap-coach.racing/.well-known/assetlinks.json` is hosted with debug + release + Play App Signing fingerprints before T185 ships in any release build | mobile T185 | manual + ops |
| ~~FU-6~~ | ~~Lowercase-normalize email on `OrganizationInvitationCreate.email`~~ — **DONE in `4d36b0b` 2026-04-28** | schemas T164 | ✅ closed |
| FU-7 | Update privacy policy text on `lap-coach.racing/privacy` to match actual mobile data flow (post FU-1..FU-4 lock-in) | marketing | sprint-marketing |

### Non-blocking (cleanup, scheduled before mobile org-aware UI)

| ID | Action | Surface |
|---|---|---|
| FU-8 | Drop `token` field from `OrganizationInvitation` response model when email-send pipeline lands (admin currently sees the link to share manually — acceptable today, not when email-delivery exists) | schemas T164 |
| FU-9 | Kotlin codegen sweep for `Organization*` / `OrgRole` / `OrgInviteRole` / `OrganizationMembership` / `OrganizationMemberEntry` / `BillingPlan` before mobile starts consuming org/billing surface | schemas codegen |
| FU-10 | Write **ADR-021: Auth use-case token-write atomicity** — codify pattern that repeats verbatim across `PairingRedeemUseCase.kt:103-104`, `MagicLinkUseCase.kt:155-156`, `AppleSignInUseCase.kt:167-168`, `TokenAuthenticator.kt:55-56` (write both halves inside `Success` only; preserve pre-existing on non-Success), with named exception for `HandleSessionExpired.onExpired() { storage.clearAll() }` | docs |
| FU-11 | Extend `AuthFlowsIntegrationTest.kt` to cover MagicLink + AppleSignIn substrate-drift scenarios (currently only PairingRedeem is composed through shared storage; T176/T177 landed chronologically AFTER T190) | mobile auth tests |
| FU-12 | Schema-layer enrichment ticket for `seats_limit` ↔ plan-tier coupling (today caller-asserted; safety lives in backend) | schemas T163 |

---

## Resume protocol

Per `loop-review.md:340` — *"post a PAUSE_FOR_HUMAN_REVIEW entry and stop the loop until the user manually resumes."*

Per cycle 216 commit body — *"To resume: delete `🛑 PAUSE_FOR_HUMAN_REVIEW ACTIVE` from review-log.md (~L6286) and `⚠️ PAUSE_FOR_HUMAN_REVIEW ACTIVE` from metrics.md (~L5)."*

**Recommended resume actions** (in order):

1. Open `docs/roadmap/sprint-30day/review-log.md`, find the `🛑 PAUSE_FOR_HUMAN_REVIEW ACTIVE` marker (~L6286), delete those lines, replace with one-line entry: `c216 PAUSE LIFTED 2026-04-28 — 15 forced-checkpoint commits adjudicated (see c216-forced-checkpoint-adjudication.md). 0 reverts. 7 follow-ups tracked.`
2. Open `docs/roadmap/sprint-30day/metrics.md`, find the `⚠️ PAUSE_FOR_HUMAN_REVIEW ACTIVE` marker (~L5), delete it.
3. File the 7 pre-launch follow-ups (FU-1 through FU-7) into the appropriate sprint files (sprint-mobile.md / sprint2-mobile.md for FU-1/2/4/5; sprint-schemas-equivalent or sprint2-backend.md for FU-6; ADR work as manual tasks).
4. File the 5 non-blocking cleanups (FU-8 through FU-12) as low-priority backlog entries.
5. Re-arm the review loop with a fresh `/loop` prompt — it will pick up from the next unreviewed sprint commit, NOT re-review the 15 c216 commits (review-log entry above prevents re-trigger).

The loop will, on next fire, resume processing the **286 remaining unreviewed sprint commits** that did NOT match forced-checkpoint criteria — these are the bulk of the 60-cycle drought backlog and can be cleared autonomously per the standard runbook.

---

## Audit provenance

- **Sub-agents**: 3 parallel specialists dispatched 2026-04-28 — security-auditor (mobile-auth), security-architect (schemas RBAC + billing), pii-detector (T224).
- **Commit range**: cycle 216 PAUSE meta = `2bc76e9` (Telemetry root, 2026-04-27 19:16Z).
- **Forced-checkpoint criteria reference**: `docs/roadmap/sprint-30day/loop-review.md:344-345`.
- **Repos audited**: `lap-mobile-android` (10 commits), `lap-schemas` (5 commits).
- **Method**: per-commit `git show <sha>` diff read + landed-file spot-check at HEAD + cross-reference with sprint task descriptions + targeted greps for known-pitfall patterns (token leakage, SDK auto-context, `extra='allow'`, role-write surface, etc.).
- **Coverage gaps disclosed**: `[PENDING: device-required]` paths cannot be validated by JVM-only audit (instrumented tests + assetlinks.json hosting + BiometricPrompt callbacks); they remain on the device-CI gate (FU-5 + invariant #1 + invariant #3 above).
