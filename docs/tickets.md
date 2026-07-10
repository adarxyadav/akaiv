# Tickets

> No ticket, no work. One checkbox per unit. Unfamiliar territory → list the ticket's open unknowns under it before starting. Done tickets get a log line and leave this file.

## Version one — skeleton live at akaiv.in

Decisions settled with the user 2026-07-06: skeleton before explainer #1; plain HTML/CSS/JS, no framework, no build step; hosted on GitHub Pages with the custom domain.

Revised 2026-07-07: akaiv.in was already live on Vercel (project `akaiv-app`, a "coming soon" page from an earlier, unrelated project) — hosting switches to Vercel instead of GitHub Pages, reusing that project and its existing domain link. GitHub push still happens, for backup and code history, not for Pages hosting.

- [ ] The skeleton page — one HTML file: the name, one line on what akaiv is, made with care. Check: user opens it in a browser and confirms it carries care.
- [ ] Live at akaiv.in — deployed to the existing Vercel project (`akaiv-app`), repo pushed to GitHub for backup. Check: user loads https://akaiv.in on their own phone and sees the page.

**Unknowns (blind-spot pass):**
- ~~Where akaiv.in is registered~~ — settled 2026-07-06: GoDaddy; DNS records edited there when we point the domain.
- ~~Does a GitHub account exist yet~~ — settled 2026-07-06: yes, `adarxyadav`.
- What "care" means on a page this small — typography, spacing, light/dark — settled by looking at drafts, not by specifying upfront.

## Page #2 — new page, idea to pick

Arriving work 2026-07-09, routed via /ticket (the skill's first real run).

- [ ] Page #2 — user picks the idea, then it ships as one page linked from index.html. Check: the user opens the deployed page and confirms the mechanism is felt, not read — the builder doesn't call it done; rule 7 explainer + quiz before closing. 2026-07-10: local playtest passed; linked from index; explainer written, quiz mostly passed. Remaining: production deploy (awaiting user's go), user opens the deployed page once, one quiz retry (which project practice two-doors is theory for).

**Unknowns (blind-spot pass):**
- ~~Decision: which idea~~ — settled 2026-07-09: **recognition over recall**, the user picked the recommendation — a self-experiment the reader runs on their own memory (fail recall, then pass recognition on the same content, inside a minute); the mechanism our own quiz practice proved on its owner. Pool rested: the bet, Litt's bottleneck, two loads, facts vs decisions, fog or ticket, no silent exits.
- Decision (user, later): the interaction that carries the picked idea — 2026-07-09: one working draft built (`two-doors.html`: eight words for eight seconds → door one, recall typed from blank → door two, recognition among category-matched lures → scores side by side, lesson lands after), deviating from the three-sketch spread: this mechanism has one canonical experiment shape, alternates on demand at playtest. 2026-07-10: playtest run, mechanism felt — no alternate needed.
- Fact (dug): plain HTML/CSS/JS, no build step, Vercel project `akaiv-app` — a new page is one HTML file plus a link from index.html; deploy is push-and-done.
