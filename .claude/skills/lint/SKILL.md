---
name: lint
description: Rule 8 sweep — the mechanical lint script plus a judgment pass over the docs, findings flagged for the human's ruling.
disable-model-invocation: true
---

# Lint

Two halves, split by who can be certain.

1. **Mechanical half.** Run the project's lint script (tools/lint-docs.py here): broken links and orphans, flagged with certainty. Fix the findings; rerun to zero.
2. **Judgment half.** Read every non-raw doc against the current compass. Flag contradictions, superseded claims, and pointers to things that moved — each flag carrying a proposed verdict, because a stale sentence still reads fine and only judgment catches it. The human rules on every flag; fixes apply after the ruling.
3. **One-owner spot check.** For facts edited since the last sweep: grep the old value — extra hits are escaped copies, re-linked to the owner.
4. **Log line,** and the script run once more, clean, after the fixes land.

Done when the script exits clean and every judgment flag carries the human's ruling.
