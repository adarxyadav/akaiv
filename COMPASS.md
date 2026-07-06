# Compass — akaiv

*One page: what this is and how we work. Read first, every session.*

## What this is

**akaiv** — a public personal site at [akaiv.in](https://akaiv.in). Each page is an interactive explainer: one idea, taught so a reader with zero context can feel it through interaction, not just read about it. The first page teaches why the check stays outside the doer's reach — whoever does the work doesn't decide it's done.

**Why it exists:** it is the first project forked from Whetstone — where the judgment sharpened there gets spent on a real internet thing, public from day one, with its owner's name on it. Building it is also how its owner learns to code: small verified steps, an explainer and a quiz on every substantial change.

**The bet behind it:** AI made building cheap, so average became the default — anyone can ship software now, and most of it reads like it. What's scarce isn't code anymore, it's judgment: knowing what great looks like, and writing it down precisely enough that humans *and agents* can act on it. And it stays scarce for a mechanical reason: models learn what can be verified, and taste has no verifier yet.

*akaiv is a Whetstone fork, copied 2026-07-06 (the log's first line is the copy date). Two rules keep the fork alive: a lesson that generalizes beyond akaiv gets filed back to Whetstone as a ticket, not buried here; and every so often, diff Whetstone's COMPASS against the copy date and pull what applies.*

## How we work

**Before building**

1. **Everything starts as a ticket** in [docs/tickets.md](docs/tickets.md). No ticket, no work.
2. **Find your unknowns.** New territory → blind-spot pass; write the open questions under the ticket before starting.
3. **Study before borrowing.** Anything we learn from gets a `docs/<name>-study.md`: what it is, what's worth stealing, what it changed for us. The source itself is saved verbatim to `docs/raw/` — read, never edited. Studies link the related studies and the rules they produced.

**While building**

4. **Small verified steps.** Build the smallest thing that works; run it before calling it done. The ticket names its check *before* work starts, and the check stays outside the doer's reach — whoever does the work doesn't edit what counts as done. Agents automate what can be verified, so the check is what makes work delegable. For doc-scale work the check is rule 7's quiz.
5. **Log every change.** One line in [docs/log.md](docs/log.md): `date — what — why`. Work came out different from the ticket? Add `deviated:` and why.
6. **File answers back.** A substantial answer worked out in a session — a comparison, a synthesis, a discovered connection — becomes a doc, not chat history. Explorations compound like studies do.

**Before closing**

7. **Explain, then quiz on big work.** When the agent builds something substantial, it writes a short explainer — background first, intuition before details, changes walked through as prose — then quizzes you; the ticket closes only when you pass. We understand to participate in the next loop, not just to verify this one; the quiz is the speed regulator.
8. **Leave the docs clean.** Fix or delete anything stale, contradictory, or orphaned. Short beats complete — a stale complete page is worse than a fresh short one. Every so often, raise a lint ticket: contradictions, superseded claims, orphan pages, missing links.

## Doc map

The doc map below is the index; when it outgrows a glance (~10+ docs), split it into `docs/index.md`.

- `COMPASS.md` — this page
- `docs/tickets.md` — work queue, open work only; finished work moves to the log
- `docs/log.md` — history, append-only
- `docs/<name>-study.md` — one per system studied. So far: none
- `docs/raw/` — studied sources, saved verbatim; read, never edited (created with the first study)
- `.claude/skills/` — the toolbox. So far: [/explain-diff](.claude/skills/explain-diff/SKILL.md) (inherited from Whetstone)
