---
project: <slug>
purpose: readme
audience: humans arriving at the project's repository
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/readme.history.md>
output: README.md
---

# Recipe — readme

<!-- Readme-genre recipe, iterated via /recipe readme; the output
path is the project root, so the host shows it as the front page. The
rules: CLAUDE.md, Document chain, Renders. -->

## Inputs
<!-- What the README is generated from. A thought project: the ledger
(state), the brief (what was asked), the intent (essence and
positions), the layers below it once they exist, and the
documentation index docs/README.md where the project has one. A
library: the ledger and the two resource indexes. -->
- ledger.md
- 00-brief.md
- 10-intent.md

## Instructions
- The README presents the project to a human meeting its repository
  for the first time — a recipient, a colleague, the principal after
  weeks away. It stands alone: no claim requires opening the chain.
  This skeleton is the one owner of what a README carries: what the
  thing is, what one gets, how to start, where it stands and where
  the documentation is; the rest is the ledger's and the
  documentation's (the engine's own README has a recipe of its own).
- Every claim is derivable from the inputs; invent nothing, omit
  rather than embellish. Anything superseded in the inputs must not
  survive.
- Tone: plain, direct. Language: <English>. A table for the chain's
  state, prose only where the subject is being explained.
- Title: `# <Project title> <intent version>` — the title from the
  brief or intent, the current intent version (no status annotation).
- <Which subject matters most for this audience; what must not
  appear; how much of the essence to carry; whether recipients or
  the principal are the primary reader.>
- Close with a short section "About this README": a render of
  `recipes/readme.md`, regenerated at every release, never edited by
  hand; fixes go into the recipe or the inputs. Then the fixed
  sentence, verbatim: "Reading this repository needs nothing beyond a
  Markdown viewer. Maintaining and evolving it needs **Forge of
  Thought** — the engine this project is run under:
  https://github.com/pche-broken-artist/forge-of-thought."
- Keep the visible dated footer `_Last updated: <render date>_`.

## Pinned facts (not rendered)
<!-- Optional. Facts of the project that no file of the project
owns yet - prerequisites, how a tool is installed, the public home
of the repository. The README does not print them; the
documentation's planner reads them here as an owner
(`.claude/agents/docs-planner.md`). One bullet each; dropped the day
a file owns the fact. Omit the section when the project has none. -->
- <fact>

## Template
# <Project title> <intent version>

*<one-line subtitle: what the project is about>*

## What this project is
<two to four paragraphs from the brief and the intent's essence: the
problem, the direction, who receives the assignment>

## What you get
<the artefacts the project hands over and to whom, from the intent and
the layers below it; one short paragraph or a few bullets>

## How to start
<where a reader begins: the brief for the ask, the intent for what
holds, the assignment or a lower layer for what is handed over; one
line each>

## Where it stands
<table: artefact | version | status | date — from the ledger's
Documents table; one line on briefs and their mining state>

## Documentation
<one line pointing to docs/README.md with the version it was made for;
omit the section when the project has no docs/>

## About this README
<the fixed closing per the instruction>

_Last updated: <render date>_
