#!/usr/bin/env python3
"""Docs lint, mechanical half of rule 8: broken relative links + orphan docs.

Scope (settled on the first lint run, 2026-07-08):
- Link check: every relative markdown link/image in COMPASS.md, README.md,
  CLAUDE.md, docs/ (including raw/), and .claude/skills/ must resolve.
- Orphan check: every file in docs/ (including raw/) and .claude/skills/
  must be linked from at least one other doc. Entry points (README.md,
  CLAUDE.md, COMPASS.md, this script) are roots, not orphan candidates.
- Fenced code blocks are excluded from the link scan (added 2026-07-09):
  verbatim sources carry template placeholders like [title](link) inside
  fences, which are examples, not links. Links outside fences still count
  for both checks, so a fence-only link target can newly orphan — rerun
  proves it hasn't.
Exit 0 = clean, exit 1 = findings printed.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Missing entry points are skipped so the script runs unchanged in forks
# (akaiv has no README.md).
SOURCES = [p for p in (
    [ROOT / "COMPASS.md", ROOT / "README.md", ROOT / "CLAUDE.md"]
    + sorted((ROOT / "docs").rglob("*.md"))
    + sorted((ROOT / ".claude" / "skills").rglob("*.md"))
) if p.exists()]

# Orphan candidates: everything under docs/ and .claude/skills/ (any file
# type — raw images are link targets too), plus COMPASS.md which README
# and CLAUDE.md must point at.
CANDIDATES = set(
    p for p in list((ROOT / "docs").rglob("*")) + list((ROOT / ".claude" / "skills").rglob("*"))
    if p.is_file()
) | {ROOT / "COMPASS.md"}

LINK = re.compile(r"!?\[[^\]]*\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")

FENCE = re.compile(r"^```.*?^```", re.M | re.S)

broken, linked = [], set()
for src in SOURCES:
    for target in LINK.findall(FENCE.sub("", src.read_text())):
        if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue  # external URL or in-page anchor
        resolved = (src.parent / target.split("#")[0]).resolve()
        if resolved.exists():
            linked.add(resolved)
        else:
            broken.append(f"{src.relative_to(ROOT)}: broken link -> {target}")

orphans = [
    f"{p.relative_to(ROOT)}: orphan — nothing links to it"
    for p in sorted(CANDIDATES - linked)
]

findings = broken + orphans
for line in findings:
    print(line)
print(f"{len(findings)} finding(s).")
sys.exit(1 if findings else 0)
