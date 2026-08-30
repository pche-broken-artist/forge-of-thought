---
project: <slug>
purpose: readme
audience: humans arriving at the project's repository
version: 0.1
updated: YYYY-MM-DD
output: README.md
---

# Recipe — readme

<!-- Readme-genre recipe, scaffolded by /new-project and iterated via
/recipe readme. A recipe is the iterated thing; its render is
generated output. Never polish README.md by hand: change this recipe,
run /render readme — and every /save that touches the project
regenerates it. Recipes are tools: bare version + updated date in
front-matter, no status, no Version History — history lives in git.
The output path is the project root, so the host shows it as the
repository's front page. -->

## Inputs
<!-- What the README is generated from. A thought project: the ledger
(state), the brief (what was asked), the intent (essence and
positions), the assignment once it exists. A library: the ledger and
the two material indexes. -->
- ledger.md
- 00-brief.md
- 10-intent.md

## Instructions
- The README presents the project to a human meeting its repository
  for the first time — a recipient, a colleague, the principal after
  weeks away. It stands alone: no claim requires opening the chain.
- Every claim is derivable from the inputs; invent nothing, omit
  rather than embellish. Anything superseded in the inputs must not
  survive.
- Tone: plain, direct, UK English. Tables for enumerable facts (chain
  state, renders, what is waiting), prose only where the subject is
  being explained.
- Title: `# <Project title> <intent version>` — the title from the
  brief or intent, the current intent version (no status annotation).
- <Which subject matters most for this audience; what must not
  appear; how much of the essence to carry; whether recipients or
  the principal are the primary reader.>
- Close with a short section "About this README": a render of
  `recipes/readme.md`, regenerated on every save, never edited by
  hand; fixes go into the recipe or the inputs. Then the fixed
  sentence, verbatim: "Reading this repository needs nothing beyond a
  Markdown viewer. Maintaining and evolving it needs **Forge of
  Thought** — the engine this project is run under:
  https://github.com/pche-broken-artist/forge-of-thought."
- Keep the visible dated footer `_Last updated: <render date>_`.

## Template
# <Project title> <intent version>

*<one-line subtitle: what the project is about>*

## What this project is
<two to four paragraphs from the brief and the intent's essence: the
problem, the direction, who receives the assignment>

## Where it stands
<table: artefact | version | status | date — from the ledger's
Documents table; one line on briefs and their mining state>

## Renders
<table from the ledger's Renders table: render | audience | generated>

## Waiting on the principal
<bullets from the ledger; omit the section when empty>

## Layout
<short fenced tree of this project's directories, what lives where;
then one line "Depends on: <libraries from the ledger's Dependencies
table>" — omitted when the table is empty>

## About this README
<the fixed closing per the instruction>

_Last updated: <render date>_
