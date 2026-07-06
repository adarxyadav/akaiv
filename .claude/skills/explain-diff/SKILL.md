---
name: explain-diff
description: Use when the user wants a change — diff, branch, PR, or doc revision — explained in depth, or when COMPASS rule 7 calls for an explainer before the quiz on substantial work. Writes a markdown explainer file.
---

# Explain Diff

Produce a markdown explainer that teaches the reader the change well enough that they could defend it themselves.

Sections:

- **Background**: What already exists that the change touches. Explore the surrounding code and docs before writing anything. Layer it in two passes: first a from-zero primer for a newcomer (flag it as skippable for readers who already know the system), then the specific context this change sits in.
- **Intuition**: Why the change is shaped the way it is — state the goal before any mechanics, and keep to the essence rather than the full detail. Ground it in a small worked example with made-up data.
- **Walkthrough**: A literate diff — narrate the changes as prose in conceptual order (cause before effect, never alphabetical file order), embedding snippets where the story needs them.
- **Quiz**: Five questions, listed with no answers shown. Pitch them so only someone who grasped the substance can pass, while a reader who understood the change but skipped incidental details still passes — no trick questions. The quiz itself runs conversationally afterward per rule 7: the agent asks, grades, and probes follow-ups; the ticket closes only on a pass. If the reader stalls or feels overwhelmed: first recap the change as its one or two core ideas in plain words, then re-ask one question at a time as multiple choice with plausible distractors. Frame every question around concrete events and artifacts ("what future event would weaken X?"), never around wording or rhetoric ("what is this word doing?") — the first lands, the second doesn't.

Format:

- One markdown file outside the repo: `/tmp/YYYY-MM-DD-explainer-<slug>.md`. The date prefix keeps explainers time-sorted; they live outside the repo because they are derived and re-derivable — never version them.
- Write like Martin Kleppmann at his clearest: plain classic prose, each section flowing into the next.
- Diagrams: choose one small family of reusable shapes and use it throughout the explainer — mermaid blocks or markdown tables, each carrying example data. No ASCII art. Offer a companion HTML artifact only when the change genuinely benefits from an interactive figure; never default to one.
- Final self-check: every code snippet is fenced with a language tag, every diagram carries example data, and each quiz question meets the calibration above.
