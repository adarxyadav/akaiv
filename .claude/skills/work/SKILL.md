---
name: work
description: Execute one ticket with small verified steps. Use when asked to build, fix, or carry out work a ticket describes.
---

# Work

Run one ticket from the project's tickets file, smallest verified step first.

1. **Load the ticket.** Work that has no ticket gets one first — run /ticket, then return here. Read the named check: you will run it, and you leave it unedited — whoever does the work doesn't touch what counts as done. A ticket with no check goes back through /ticket step 3 before any building.
2. **Build small, run it.** The smallest thing that works, run before it's called done. Questions surfacing mid-build sort the usual way: facts you dig up yourself, decisions go to the human one at a time with a recommendation.
3. **Run the check.** A machine-owned check (suite, script, deployed page) runs now, exactly as the ticket words it. A human-owned check (quiz, read-and-confirm) gets queued: state precisely what the human must do.
4. **Log it.** One line in the project log: date — what — why. Work came out different from the ticket? Add `deviated:` and why.

Done when the check has run — or sits queued on the human's side — and the log line exists. The ticket stays in the file: retiring it is /close's job, after its check passes.
