---
name: close
description: Retire a finished ticket by running its named check — explainer and quiz included when the work was substantial. Use when a ticket's work is done.
---

# Close

A ticket leaves the queue only through its own check.

1. **Run the named check, as written.** The ticket's check line is the contract; read the result plainly — passed, failed, or blocked.
2. **Substantial work → explainer, then quiz.** Drive /explain-diff for the explainer, then quiz conversationally: the reader passes when they could defend the change themselves. A miss that survives a plain-words recap and a concrete retry is a lesson — write it where it executes (the rule, the doc, the skill) and log that you did.
3. **On a pass:** the ticket leaves the tickets file, and a closing log line records what closed — plus the quiz's sticking point, when one emerged.
4. **Short of a pass:** the ticket stays, with one line under it naming what blocked.

Done when the tickets file and the log agree: the ticket is gone and the log says why — or it remains and names its blocker.
