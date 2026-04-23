#!/usr/bin/env python3
"""
Preformatted alert emails for LAP ops. Wraps send_email.py with templates.

Usage:
    python send_alert.py <alert_type> "<context>"

Alert types:
    loop-stopped              — a /loop died or Claude exited
    scope-blowup              — a commit exceeded 1500 LOC for one task
    secret-leak               — commit contained a detected secret (CRITICAL)
    contract-drift            — schema/API drift between repos
    strategy-decision-required — non-code decision needed from human
    pause-triggered           — review loop hit a pause condition
    human-review-required     — forced checkpoint (M3/W11 etc.)
    ci-broken                 — repo CI has been red for >6h
    budget-spike              — unexpected rate-limit/credit spike detected

Context is free-form text (who/what/where/when/proposed action).

Exit codes: same as send_email.py.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone

try:
    from send_email import send
except ImportError:
    # allow invocation from a different cwd
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from send_email import send  # type: ignore


ALERT_TEMPLATES: dict[str, tuple[str, str]] = {
    "loop-stopped": (
        "🔴 LAP ALERT — Loop stopped",
        "A sprint or review loop has stopped firing.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "1. Inspect the terminal for the stack trace / exit reason.\n"
        "2. Fix the root cause (dependency, permission, disk).\n"
        "3. Restart the loop with the same /loop command from LOOP-SETUP.md.\n\n"
        "Every hour the loop is down is ~4 tasks not shipping.",
    ),
    "scope-blowup": (
        "🟡 LAP ALERT — Scope blowup",
        "A commit exceeded 1500 LOC for a task scoped to ~1h.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "The commit was pushed (tests passed) but flagged with `[SCOPE_FLAG]`. "
        "Consider splitting the task into smaller units in the sprint file going forward.\n\n"
        "Read the diff: the agent may have made correct-but-overreaching design choices that deserve your eyes.",
    ),
    "secret-leak": (
        "🚨 LAP CRITICAL — Secret leaked",
        "A commit contained what the review loop detected as a secret (API key, token, password).\n\n"
        "## Context\n\n{ctx}\n\n"
        "## IMMEDIATE ACTION REQUIRED\n\n"
        "1. The commit has been reverted locally + on origin.\n"
        "2. BUT: the secret was in git history for <time>. If it was ever pushed to a public-leak crawler, it's compromised.\n"
        "3. ROTATE THE SECRET NOW on the issuing service (Stripe, Clerk, Resend, etc.).\n"
        "4. Audit usage of that secret for the last N hours.\n"
        "5. If the key had production scope, audit production logs too.\n\n"
        "This is the single highest-priority alert the system sends.",
    ),
    "contract-drift": (
        "🟡 LAP ALERT — Contract drift",
        "Data contracts have drifted between repos.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "Regenerate the affected consumer's types (TS / Swift / Kotlin) and commit. "
        "Next sprint cycle will depend on this being resolved.",
    ),
    "strategy-decision-required": (
        "🟢 LAP — Strategy decision required",
        "The loops have hit a decision that is not code-reviewable, not in the ADRs, not solvable by the docs.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "Decide. Then either:\n"
        "- Update an ADR in docs/roadmap/02-ARCHITECTURE-DECISIONS.md, OR\n"
        "- Post the decision into the blocked sprint task as a `[DECISION: <answer>]` note.\n\n"
        "The loops will self-unblock once the decision is written.",
    ),
    "pause-triggered": (
        "🟡 LAP ALERT — Review loop paused",
        "The review loop hit a pause trigger and stopped this cycle.\n\n"
        "## Context\n\n{ctx}\n\n"
        "The next cycle (in ~2h) will fire fresh. If the underlying condition persists, the loop will keep pausing and commits will stop landing on GitHub.\n\n"
        "## Common pause triggers\n\n"
        "- >3 commits failed review in one cycle (sprint loop prompt may be malfunctioning)\n"
        "- >1 cross-repo contract test failed in a row\n"
        "- Any secret-leak detected\n"
        "- Disk usage >90%\n"
        "- Unexpected upstream push (someone else committed)",
    ),
    "human-review-required": (
        "🔴 LAP — Human review checkpoint hit",
        "A forced human-review checkpoint has fired. The review loop is paused until you remove the marker.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "1. Open `docs/roadmap/sprint-30day/review-log.md`.\n"
        "2. Find the `PAUSE_FOR_HUMAN_REVIEW` entry.\n"
        "3. Review the specific diff / state that triggered it.\n"
        "4. Either approve (remove the PAUSE line, commit the log) or raise the concern as an ADR update.\n\n"
        "The loop WILL NOT resume until the PAUSE marker is removed.",
    ),
    "ci-broken": (
        "🟡 LAP ALERT — CI red for >6h",
        "A repo's CI has been red for more than 6 consecutive hours.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "The sprint loop may be producing code that passes local tests but fails CI. "
        "Investigate the CI logs on GitHub Actions and compare to local test behavior.",
    ),
    "budget-spike": (
        "🟡 LAP ALERT — Usage spike detected",
        "Rate-limit or token consumption looks abnormal vs baseline.\n\n"
        "## Context\n\n{ctx}\n\n"
        "## Required action\n\n"
        "Check Anthropic usage dashboard. If a loop is in a retry storm (same task failing + retrying forever), kill it and inspect.",
    ),
}


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2

    alert_type = sys.argv[1]
    context = sys.argv[2]

    if alert_type not in ALERT_TEMPLATES:
        print(f"ERROR: Unknown alert type '{alert_type}'.", file=sys.stderr)
        print(f"Known types: {', '.join(sorted(ALERT_TEMPLATES.keys()))}", file=sys.stderr)
        return 2

    subject, body_template = ALERT_TEMPLATES[alert_type]
    body = body_template.format(ctx=context)
    body += f"\n\n---\n\n*Timestamp: {datetime.now(timezone.utc).isoformat()}*"
    body += f"\n\n*Alert type: `{alert_type}`*"

    return send(subject, body)


if __name__ == "__main__":
    sys.exit(main())
