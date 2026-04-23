#!/usr/bin/env python3
"""
Core email sender for LAP ops. Uses Resend API (https://resend.com).

Usage:
    python send_email.py "<subject>" "<body_markdown>"

Env (loaded from ./ops/.env automatically if present):
    RESEND_API_KEY   — required. Get from https://resend.com/api-keys
    EMAIL_TO         — default: theos.eleve@gmail.com
    EMAIL_FROM       — default: LAP Ops <onboarding@resend.dev>

Exit codes:
    0  — sent successfully
    1  — API error
    2  — usage / config error
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path


def _load_dotenv() -> None:
    """Load KEY=VALUE pairs from ops/.env into os.environ (non-destructive)."""
    env_file = Path(__file__).parent / ".env"
    if not env_file.exists():
        return
    for raw in env_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _md_to_html(md: str) -> str:
    """Tiny markdown → HTML converter. Good enough for log-style emails."""
    import html as html_mod
    import re

    out_lines: list[str] = []
    in_list = False
    in_code = False
    for line in md.splitlines():
        # fenced code
        if line.startswith("```"):
            if in_code:
                out_lines.append("</pre>")
                in_code = False
            else:
                out_lines.append('<pre style="background:#0e1116;color:#c9d1d9;padding:12px;border-radius:6px;overflow:auto;font-size:12px">')
                in_code = True
            continue
        if in_code:
            out_lines.append(html_mod.escape(line))
            continue

        stripped = line.rstrip()
        if stripped.startswith("# "):
            out_lines.append(f"<h1 style='margin:16px 0 8px;font-size:20px'>{html_mod.escape(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            out_lines.append(f"<h2 style='margin:14px 0 6px;font-size:17px;border-bottom:1px solid #30363d;padding-bottom:4px'>{html_mod.escape(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            out_lines.append(f"<h3 style='margin:10px 0 4px;font-size:14px;color:#8b949e'>{html_mod.escape(stripped[4:])}</h3>")
        elif stripped.startswith(("- ", "* ")):
            if not in_list:
                out_lines.append('<ul style="margin:4px 0;padding-left:20px">')
                in_list = True
            item = html_mod.escape(stripped[2:])
            # simple inline code `x`
            item = re.sub(r"`([^`]+)`", r"<code style='background:#1c2128;padding:1px 5px;border-radius:3px'>\1</code>", item)
            # bold **x**
            item = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", item)
            out_lines.append(f"<li>{item}</li>")
        else:
            if in_list:
                out_lines.append("</ul>")
                in_list = False
            if not stripped:
                out_lines.append("<br>")
            else:
                text = html_mod.escape(stripped)
                text = re.sub(r"`([^`]+)`", r"<code style='background:#1c2128;padding:1px 5px;border-radius:3px'>\1</code>", text)
                text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
                out_lines.append(f"<p style='margin:4px 0'>{text}</p>")
    if in_list:
        out_lines.append("</ul>")
    if in_code:
        out_lines.append("</pre>")
    body_html = "\n".join(out_lines)
    return (
        '<div style="font-family:ui-sans-serif,-apple-system,Segoe UI,Roboto,sans-serif;'
        "color:#c9d1d9;background:#0d1117;padding:24px;max-width:760px;margin:0 auto;"
        'border:1px solid #30363d;border-radius:8px;font-size:14px;line-height:1.5">'
        f"{body_html}"
        "</div>"
    )


def send(subject: str, body_md: str) -> int:
    _load_dotenv()

    api_key = os.environ.get("RESEND_API_KEY")
    email_to = os.environ.get("EMAIL_TO", "theos.eleve@gmail.com")
    email_from = os.environ.get("EMAIL_FROM", "LAP Ops <onboarding@resend.dev>")

    if not api_key:
        print("ERROR: RESEND_API_KEY not set. Create ops/.env from .env.example.", file=sys.stderr)
        return 2
    if not subject or not body_md:
        print("ERROR: subject and body are required.", file=sys.stderr)
        return 2

    payload = {
        "from": email_from,
        "to": [email_to],
        "subject": subject,
        "html": _md_to_html(body_md),
        "text": body_md,
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "lap-ops/1.0 (python-urllib)",
            "Accept": "application/json",
        },
        method="POST",
    )

    log_path = Path(__file__).parent / "email.log"

    def _log(line: str) -> None:
        try:
            with log_path.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:  # noqa: BLE001
            pass

    def _say(msg: str) -> None:
        """ASCII-safe stdout/stderr write that won't crash on Windows cp1252."""
        try:
            print(msg)
        except UnicodeEncodeError:
            sys.stdout.buffer.write((msg + "\n").encode("utf-8", errors="replace"))

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            response = json.loads(resp.read().decode("utf-8"))
            rid = response.get("id", "<unknown>")
            ts = datetime.now(timezone.utc).isoformat()
            _log(f"{ts} OK {rid} | {subject}")
            _say(f"[OK] Email sent. Resend ID: {rid}")
            return 0
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        ts = datetime.now(timezone.utc).isoformat()
        _log(f"{ts} ERR http{e.code} | {subject} | {body[:200]}")
        _say(f"[ERR] HTTPError {e.code}: {body}")
        return 1
    except urllib.error.URLError as e:
        ts = datetime.now(timezone.utc).isoformat()
        _log(f"{ts} ERR url | {subject} | {e.reason}")
        _say(f"[ERR] URLError: {e.reason}")
        return 1
    except Exception as e:  # noqa: BLE001
        ts = datetime.now(timezone.utc).isoformat()
        _log(f"{ts} ERR exc | {subject} | {type(e).__name__}: {e}")
        _say(f"[ERR] Unexpected: {type(e).__name__}: {e}")
        return 1


def _main() -> int:
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    return send(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    sys.exit(_main())
