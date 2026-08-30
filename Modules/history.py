#!/usr/bin/env python3
"""Write HISTORY.md from the git log. Safe to re-run.

    python3 Modules/history.py

WHY GENERATE IT RATHER THAN KEEP ONE BY HAND
A hand-written changelog is a second record of the same events, and the two
diverge the first time somebody is in a hurry. The commit messages in this repo
already carry the reasoning -- what broke, what was measured, why a decision went
the way it did -- so the history is written by writing good commits, and this
just renders them.

Which means: if a commit message here is terse, the history is poorer for it.
That is the intended pressure.
"""
import subprocess, pathlib, re, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "HISTORY.md"
SEP  = "\x1e"

log = subprocess.run(
    ["git", "-C", str(ROOT), "log", "--reverse", f"--format=%H{SEP}%h{SEP}%ad{SEP}%an{SEP}%s{SEP}%b{SEP}"],
    capture_output=True, text=True, check=True).stdout

commits = []
for chunk in log.split(SEP + "\n"):
    parts = chunk.strip("\n").split(SEP)
    if len(parts) < 6:
        continue
    full, short, date, author, subject, body = parts[:6]
    # the trailers are machinery, not history
    body = "\n".join(l for l in body.splitlines()
                     if not re.match(r"^(Co-Authored-By|Claude-Session|Signed-off-by):", l)).strip()
    stat = subprocess.run(["git", "-C", str(ROOT), "show", "--stat", "--format=", full],
                          capture_output=True, text=True).stdout.strip().splitlines()
    summary = stat[-1].strip() if stat else ""
    commits.append(dict(short=short, date=date, author=author, subject=subject,
                        body=body, files=len(stat) - 1 if stat else 0, summary=summary))

lines = [
    "# History",
    "",
    "Every commit, oldest first, with the reasoning that came with it.",
    "",
    "**Generated** by `python3 Modules/history.py` from the git log — not maintained by hand, so",
    "it cannot drift from what actually happened. The reasoning lives in the commit messages;",
    "this only renders them. A terse commit makes a poorer history, which is the point.",
    "",
    f"{len(commits)} commits.",
    "",
    "---",
    "",
]
for i, c in enumerate(commits, 1):
    lines.append(f"## {i}. {c['subject']}")
    lines.append("")
    lines.append(f"`{c['short']}` · {c['date']} · {c['author']} · "
                 f"{c['files']} file{'s' if c['files'] != 1 else ''} changed")
    lines.append("")
    if c["body"]:
        lines.append(c["body"])
        lines.append("")
    lines.append("---")
    lines.append("")

OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)} — {len(commits)} commits, {OUT.stat().st_size // 1024} KB")
