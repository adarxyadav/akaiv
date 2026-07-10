---
name: fork
description: Copy the Whetstone template into a new project — a fork, not a link.
disable-model-invocation: true
---

# Fork

Runs from the stone. The fork contract — what travels, what's replaced, the two sync rules — lives in Whetstone's COMPASS starter-template bullet; read it first and follow it exactly. This runbook carries only the mechanics:

1. **Copy the structure:** COMPASS.md, CLAUDE.md, docs/ (tickets, log, index), .claude/skills/ — with studies, tickets, and log emptied.
2. **In the copy's COMPASS:** replace "What this is" with the project stub (what it is, why it exists, a line naming it a Whetstone fork); keep the bet; write in the two sync rules; trim the doc map to the files that survived the copy.
3. **Log line one in the copy = the copy date** — it anchors the sync contract.
4. **`git init`,** first commit named as the fork.
5. **Run the copy's lint script** to zero findings.

Done when the copy lints clean and the human has read the stub and confirmed it says what they mean.
