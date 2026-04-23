# LAP Ops

Email notification system for the autonomous loop fleet. Sends:
- **Daily strategy email** (08:00 UTC every day) — KPIs, work done, strategy decisions needing human input, flagged issues, blockers, outlook.
- **Alert emails** (ad-hoc) — fired inline by the review loop when something broke or needs fast human input.

Both go to `theos.eleve@gmail.com` via **Resend** (free tier, 100 emails/day — we send ~5).

---

## One-time setup (5 minutes)

1. Go to https://resend.com → sign up (free, no card).
2. Dashboard → API Keys → **Create API key** → give it "Full access" → copy the key (starts with `re_…`).
3. In this folder:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env`, paste your key:
   ```
   RESEND_API_KEY=re_YourActualKeyHere
   ```
5. Test:
   ```bash
   python send_alert.py strategy-decision-required "Test alert from setup."
   ```
6. Check `theos.eleve@gmail.com` inbox (and spam folder on first send). You should see the email within 30 seconds. Mark as "not spam" if Gmail put it there, so future emails land in inbox.

If the test works, you're done. The review loop will use these scripts automatically from now on.

---

## Files

| File | Purpose |
|---|---|
| `send_email.py` | Core email sender. Takes `subject` + `body_md` args, POSTs to Resend. |
| `send_alert.py` | Preformatted alerts. 9 alert types, each with a template. |
| `.env.example` | Template. Copy to `.env`. |
| `.env` | YOUR secrets. Gitignored. Never commit. |
| `email.log` | Append-only log of sent emails (local only, for audit). |

---

## Usage

### From the review loop (automatic)

The review loop reads `docs/roadmap/sprint-30day/loop-review.md` each cycle and calls these scripts:

- **Daily strategy email** — Step 10 in the runbook. Composed by Claude inline with full context from logs + metrics + sprint files. Sent via `python ops/send_email.py "subject" "body"`.

- **Alerts** — Fired from Steps 3/4/5/7/11 whenever a pause/revert/flag condition hits. Sent via `python ops/send_alert.py <type> "<context>"`.

### Manual (you, occasionally)

Send an ad-hoc email:
```bash
python ops/send_email.py "Test" "Hello world"
```

Send an alert manually:
```bash
python ops/send_alert.py loop-stopped "Backend terminal exited because pnpm install failed. See: ..."
```

List available alert types:
```bash
python ops/send_alert.py
```

---

## Alert catalog

| Type | Severity | When fired |
|---|---|---|
| `loop-stopped` | 🔴 high | A /loop died / Claude exited |
| `scope-blowup` | 🟡 med | A single-task commit exceeded 1500 LOC |
| `secret-leak` | 🚨 critical | API key / token detected in a commit |
| `contract-drift` | 🟡 med | Schema drift between repos |
| `strategy-decision-required` | 🟢 low-med | Non-code decision needed |
| `pause-triggered` | 🟡 med | Review loop paused this cycle |
| `human-review-required` | 🔴 high | Forced checkpoint (e.g. M3/W11) |
| `ci-broken` | 🟡 med | CI red >6h |
| `budget-spike` | 🟡 med | Token usage abnormal |

---

## Rate limits (Resend free tier)

- 100 emails / day
- 3000 emails / month
- 1 custom domain (optional, we don't need one — Resend's `onboarding@resend.dev` works as sender)

Expected actual volume: 1 daily email + ≤5 alerts/day = well under 10. 10x headroom.

---

## What to do if emails stop arriving

1. Check `ops/email.log` — did the scripts think they sent?
2. If log shows success but no email → check Gmail spam folder. Mark as not-spam.
3. Resend dashboard → Logs → look for bounces / rejections.
4. If API key was accidentally committed → rotate at resend.com/api-keys, update `.env`.
5. If you hit 100/day limit → extremely unlikely, but you can upgrade to paid or switch provider (the scripts are single-file, easy to swap).
