# Cycle 216 Forced-Checkpoint — Follow-up Backlog

**Source**: `c216-forced-checkpoint-adjudication.md` (audit 2026-04-28).
**Lifted**: 2026-05-01 (cycle 239 + 1, manual).
**Total items**: 12 originally; 1 closed during adjudication; 11 outstanding.

Each item is tracked here for full context. Loop-executable items are mirrored as `[ ]` tasks in the appropriate sprint file (sprint2-mobile.md / sprint-marketing.md). Manual items (ADRs, ops, launch checklist) live here only.

---

## ✅ Closed during adjudication

| ID | Action | Status |
|---|---|---|
| FU-6 | Lowercase-normalize email on `OrganizationInvitationCreate.email` | **DONE** in `lap-schemas@4d36b0b` (2026-04-28). `@field_validator(mode='before')` strips + lowercases at the boundary; 3 new tests; openapi.json unchanged. |

---

## Pre-launch blocking (must land before public store release)

These five gate the EU-compliant T224 telemetry story plus the App Links runtime contract. None blocks the c216 PAUSE lift; all block public release.

### FU-3 — ADR-020: Mobile telemetry default policy (manual)

Write the ADR that locks consent semantics for the mobile app. **Decision agreed during adjudication** (2026-04-28):
- **Default-OFF** (`DEFAULT_OPTED_OUT = true`).
- **First-launch consent banner** (industry-standard pattern), modal before onboarding.
- **SDK init gated**: `LapApplication.initSentryIfConfigured` and `PostHogAndroid.setup` only run after Yes is recorded.
- **Consent record**: choice + ISO-8601 UTC timestamp + ADR-020 version persisted to the same SharedPreferences as the toggle. GDPR Art. 7(1) demands proof — record the timestamp.

The ADR itself documents the decision; T093 (sprint2-mobile) implements the banner.

### FU-1 / FU-2 / FU-4 — see sprint2-mobile.md T091, T092, T093

Filed as loop-executable tasks (mount toggle, gate SDK init + invoke `Sentry.close()` / `PostHog.optOut()` on flip + disable `isSendDefaultPii` + first-launch consent banner per ADR-020).

### FU-5 — Host `assetlinks.json` with all three SHA256 fingerprints (ops)

`https://app.lap-coach.racing/.well-known/assetlinks.json` must serve the JSON documented at `lap-mobile-android/app/src/main/kotlin/com/lap/mobile/deeplink/AppLinksConfig.kt:21-39`:

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.lap.mobile",
      "sha256_cert_fingerprints": [
        "<DEBUG_KEYSTORE_FINGERPRINT>",
        "<RELEASE_UPLOAD_KEYSTORE_FINGERPRINT>",
        "<PLAY_APP_SIGNING_FINGERPRINT>"
      ]
    }
  }
]
```

**The Play App Signing fingerprint is the one that breaks if forgotten** — Play resigns the APK with its own key. Verify on device with `adb shell pm get-app-links com.lap.mobile` ("verified" = success; "ask" = chooser fallback).

### FU-7 — sprint-marketing.md T221

Privacy policy text on `lap-coach.racing/privacy` must match actual mobile data flow post-FU-1..FU-4 lock-in.

---

## Non-blocking (cleanup; scheduled before mobile org-aware UI)

### FU-8 — Drop `token` from `OrganizationInvitation` response when email-send lands (schemas)

Today, the response model exposes `token: str` so an admin viewing pending invites sees the link to share manually. When the email-delivery pipeline lands (server-only fan-out), drop the field from the response — admins should not retain a relay path that bypasses the mailbox.

File on schemas backlog. No T# yet (depends on which sprint surfaces email send).

### FU-9 — Kotlin codegen sweep before mobile org-aware UI (schemas codegen)

Currently zero Kotlin parity for `Organization*` / `OrgRole` / `OrgInviteRole` / `OrganizationMembership` / `OrganizationMemberEntry` / `BillingPlan`. Sustainable today (mobile is driver-side; doesn't yet read org membership). Risk window opens when driver-side mobile starts reading "which org am I in" — sweep needs to land within 1-2 cycles of that surface starting.

### FU-10 — ADR-021: Auth use-case token-write atomicity (manual ADR)

Codify the pattern repeated verbatim across `PairingRedeemUseCase.kt:103-104`, `MagicLinkUseCase.kt:155-156`, `AppleSignInUseCase.kt:167-168`, `TokenAuthenticator.kt:55-56`:

> Auth use cases write tokens atomically inside the `Success` branch only; non-`Success` branches preserve pre-existing tokens by omission.

Named exception: `HandleSessionExpired.onExpired() { storage.clearAll() }` (T186).

The ADR should also call for a parameterised cross-kernel composition test — currently `AuthFlowsIntegrationTest` only exercises the pair flow through shared storage. FU-11 implements that test extension.

### FU-11 — sprint2-mobile.md T094

Extend `AuthFlowsIntegrationTest.kt` with `magic_link_verify_through_shared_storage` and `apple_sign_in_through_shared_storage` cases — currently T176/T177 (Apple, magic-link) landed AFTER T190 chronologically so their cross-kernel composition isn't covered.

### FU-12 — Schema-layer enrichment for `seats_limit` ↔ plan-tier coupling (schemas)

Today `OrganizationCreate.seats_limit: int = Field(ge=1)` is caller-asserted with no max-cap or plan-tier coupling. Backend currently translates `plan_id` → Stripe price → seat allowance server-side, which is the right boundary today. If a future "self-service org create" flow exposes seat-cap to the client, the schema should constrain seats by tier (e.g., `Annotated[int, AfterValidator(_constrain_to_plan)]`).

File on schemas backlog. Low priority; only matters if seats_limit ever becomes client-asserted with consequences.

---

## Cross-references

- Adjudication doc: `docs/roadmap/sprint-30day/c216-forced-checkpoint-adjudication.md`
- Cycle 216 PAUSE meta commit: `2bc76e9` (Telemetry root, 2026-04-27)
- Forced-checkpoint criterion: `loop-review.md:344-345`
- T164 fix: `lap-schemas@4d36b0b` (2026-04-28)
