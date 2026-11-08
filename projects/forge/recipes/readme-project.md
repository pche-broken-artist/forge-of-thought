---
project: forge
purpose: readme
audience: humans arriving at the repository of the forge's own project
version: 0.1
output: README.md
---

# Recipe — readme (the project's own)

<!-- A recipe: CLAUDE.md, Document chain, Renders (what it is) and
Versioning & status (how it is versioned). Readme genre; the file is
named readme-project because recipes/readme.md of this project
renders the engine's README (POS.1980, SOL.0930). -->

## Inputs
- ledger.md
- 10-intent.md

## Instructions
- This README stands on the repository `forge`, the forge's own
  project of Forge of Thought, and says in the first sentence that
  whoever wants to use the forge needs the engine,
  https://github.com/pche-broken-artist/forge-of-thought, not this
  repository (POS.1980).
- Then what this repository is: Forge of Thought run through its own
  process; the briefs, the intent with its positions and rejected
  directions, the solution design, the threads, the decisions, the
  research, the reviews and the challenges, and the recipes whose
  renders are the engine's README, release notes and CONTRIBUTING.
- Who clones it and how: whoever develops the engine, beside it as
  `projects/forge`, with `/import-project
  https://github.com/pche-broken-artist/forge.git`; a release of the
  engine then lands in two commits, one here and one in the engine.
- Where to say something: the engine's Discussions and Issues, its
  CONTRIBUTING and SECURITY, by link; this repository has none of
  its own.
- Where it stands: the Documents table of the ledger (file, version,
  status, date) and one line with the count of open threads.
- Every claim derivable from the inputs; invent nothing. Tone plain
  and direct. Language: English.
- Title: `# Forge of Thought, the forge's own project <intent
  version>`. Nothing from any other project; no instance facts.
- Close with "About this README": a render of
  `recipes/readme-project.md`, regenerated at every release, never
  edited by hand; then the fixed sentence of the readme genre,
  verbatim, and the dated footer.

## Template
# Forge of Thought, the forge's own project <intent version>

*<one line: the thinking behind the engine, kept as a project of the engine's own process>*

<the first sentence: the engine is what you install, with the link>

## What this repository is
<two paragraphs>

## Who clones it, and how
<one paragraph with the command>

## Where it stands
<table from the ledger's Documents table; the line on open threads>

## Where to say something
<the three links into the engine>

## About this README
<the fixed closing>

_Last updated: <render date>_
