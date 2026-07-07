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

## Explainer #1 — the check stays outside the doer's reach

One idea: whoever does the work doesn't grade it. Reader has zero context; the page makes them feel the mechanism through interaction, then a one-paragraph lesson lands. One page, linked from index.html.

- [ ] Explainer #1 — user picks the interaction concept, then it ships as one page. Check: the user plays it and calls it done — the builder doesn't; rule 7 quiz before closing. 2026-07-06: all three sketches built as working drafts; user locked **same-eyes.html** (worker whose self-check shares its blind spot) — the-bar and own-cut deleted. Remaining: user playtest, rule 7 explainer + quiz.

**Unknowns (blind-spot pass):**
- Which interaction makes the mechanism *felt* — settled by the user picking among sketches, not specified upfront.
- Does the lesson survive a reader with zero context — only the user's playtest answers this.
