---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 3dc48407c55fb939
inputs:
  - CLAUDE.md#Document chain
  - templates/recipe.md
  - templates/recipe-readme.md#Instructions
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.0720
  - projects/forge/10-intent.md#POS.0730
  - projects/forge/10-intent.md#POS.0590
  - projects/forge/10-intent.md#POS.0770
  - projects/forge/10-intent.md#POS.0810
  - projects/forge/10-intent.md#POS.1000
  - projects/forge/10-intent.md#POS.1550
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0240
---

# Renders and recipes

A render is an output for one audience, generated from the documents
of a project and never edited by hand; a recipe is the file that says
how it is made. This page explains what the two are, how an output
travels from a recipe to a finished file, and why the forge keeps the
render out of reach of the hand. It is for anyone who uses the forge,
extends it or weighs it.

## What it is

A project's thinking lives in its chain: the versioned documents
(artefacts) that run from a brief through the intent to whatever
layers the project needs (see the [Glossary](../reference/glossary.md)
for each term). The chain is composed by the principal, that is, the
person whose thinking is being forged.

A render is an audience-specific output generated from the chain.
Examples are a presentation for a group, an architecture picture, an
executive summary and the repository README.

A render is never a source of truth.
The artefacts stay the source of truth.
A render assigns nothing and is not part of the chain.

What is iterated is the recipe, not the render.
A recipe lives in `recipes/<recipe>.md` and holds in one file:

- the inputs: the artefacts the render is generated from, one or
  several;
- the audience;
- the instructions: tone, what to emphasise, what to omit, length,
  register;
- the template: the literal skeleton of the render, with placeholders;
- optionally the format: the file the render is turned into.

A recipe is a tool, not a record of thinking.
It carries a version and no status, because a recipe is never approved
and stays at 0.x for life.
Being versioned, it keeps its history in a companion file beside it,
like every versioned document.

The boundary between chain and render is authorship, not audience.
A chain artefact is composed by the principal.
A render is generated from artefacts.
So an article the principal writes is a layer of the chain, and its
translation is a render.

The pages of the documentation are generated too, but they are not
renders.
They are made without any recipe (see
[The documentation](the-documentation.md)).

## How it works

### Generation from the recipe

`/render <recipe>` regenerates the output from its recipe, mechanically.
The render is undated and is overwritten freely.
Everything is Markdown, content only: a presentation is a `.md` file
that says what is on each slide.

Recipes are deliberately loose.
The template fixes the structure and what information appears where.
It never fixes the wording.
Each rendering derives the words again from the current inputs.
Where a wording carries weight (a title, a claim, a fixed line), the
recipe pins it as fixed text, and that text is regenerated verbatim
while everything else is derived freely.

A render may serve as an input of another render, such as a slide that
cites an architecture picture.
The citing recipe then declares that render among its inputs.

How to compose a recipe is said in
[Compose a recipe](../use/compose-a-recipe.md), and how to generate
one in [Render an output](../use/render-an-output.md).

### Provenance and staleness

Every render opens with its provenance.
The provenance cites the recipe and every input, each with its version.
Because the provenance tracks the dependency, a render whose recipe or
inputs have moved on since it was made is stale.
The exact block and the exact definition of stale are given in
[Render provenance](../reference/render-provenance.md).
The ledger (the state report of a project, made from its documents at
read time) mirrors the provenance in its Renders table.

### Who regenerates, and when

A render is regenerated in only two ways:

- by the principal's explicit `/render`;
- by `/release`.

Claude never regenerates a render on its own judgement.
It reports staleness and offers to regenerate.
Every `/release` regenerates the README and the release notes.
Every other render is as stale as the principal lets it be.
No check reports the staleness of a render.
The state map of the project, which `/forge` shows, does.

When a `/release` has regenerated renders, its summary reports what
materially changed in them.
The principal rules on that change before the release is committed.

### Several languages

A recipe may declare its output languages in `languages:`.
The first language is the primary.
The rest are translations of it.
`/render` generates the primary render and, in the same run, translates
it into every other language, scene for scene and line for line.
The result is one render per language, `renders/<recipe>.<lang>.md`.
Each has its own provenance, and a translation cites the primary render
it was made from.
A recipe with one language keeps `renders/<recipe>.md`.

### Two steps to a finished file

An output is made in two steps, each with its own command, divided by
cost.

1. `/render` generates the Markdown and, where the recipe names a
   format, the plain file beside it.
   The plain file of a deck or a document is made through pandoc.
   A screenplay is turned into a video, or into the events its player
   plays, through the screenplay script (see
   [The screenplay and its player](the-screenplay-and-its-player.md)).
   This step is deterministic and cheap, and is repeated freely.
2. `/publish` makes the designed file through a model and its document
   skills, into `published/`.
   It runs only on the principal's command, never by `/render`, never by
   `/release` and never on Claude's own judgement.
   Its provenance stands in a companion file beside it, and the ledger's
   Published table says whether each published file is `current` or
   `stale`.
   It takes the render as it lies on disk and never renders.
   Where the render is stale, it says so before the conversion, and the
   principal decides.
   How to run it is said in
   [Publish a designed file](../use/publish-a-designed-file.md).

A screenplay has no designed step.
A recipe that names no format ends at the Markdown.
The format and what each step needs stand in the recipe's `## Format`
section, and are never copied into the render.

The Markdown render stays the sole source of truth.
A plain or a published file is an output of second order: tracked in git
like any render, never edited by hand.

### README, release notes and genres

Every project has a README as a render of its own `recipes/readme.md`.
A thought project also has release notes, a render of
`recipes/release-notes.md`.
A library has a README only: a catalogue of what it holds.
Both recipes are scaffolded when the project is created, and every
`/release` of the project regenerates both.

A README presents the project to a person meeting its repository for
the first time.
It says what the thing is, what one gets, how to start, where it
stands and where the documentation is.
Every claim in it is derivable from the inputs.
It closes with a short section saying that it is a render that is never
edited by hand.

Release notes are a log of releases, not a story.
They have one section per release, newest first, with one sentence per
change from the reader's side.
What the reader must do is written with the change in its history
record and carried into the notes word for word.

A recipe may be composed through a genre interview, `/recipe <genre>`.
Each genre has one definition carrying its checklist of questions, and
a skeleton that extends the base recipe shape without replacing it.
The genres are `presentation`, `readme`, `release-notes` and
`screenplay`.

## Why

- **Never edited by hand.**
  A fix made in the render would not survive the next regeneration.
  So content fixes go into the recipe or the inputs, and the file is
  regenerated.
- **The recipe stays loose.**
  Fixing the text in the template would turn the recipe into the render
  and make the inputs meaningless.
- **Regeneration only on the principal's word or by a release.**
  Regeneration is stochastic: the same inputs never guarantee the same
  words.
  An unreviewed regeneration is therefore an unreviewed edit of a
  document that faces outward.
  Pinned wording and the release summary are two light defences, and
  neither is a gate.
- **Translations in the same run.**
  The quotes of a transcript, the beats and the captions are chosen
  once.
  A second generation would choose the quotes and the cut again
  differently, so the other languages are translated from the primary
  render instead.
- **Two steps divided by cost.**
  The expensive conversion through a model should run as seldom as
  possible.
- **`/publish` never renders.**
  A render is made by a model and is never the same twice.
  A fresh render would publish a text the principal has not read.
- **A README in every project.**
  Whoever finds the project should know what runs it.
- **Release notes as a log.**
  A reader wants to see plainly what was added, changed and removed.
- **No regeneration of only the stale renders at every save.**
  That was considered and rejected.
  On projects it saves nothing, because the input of the README (the
  ledger) moves at every operation.
  It would also add a staleness state that several commands must read
  alike.
- **No recipe per page of the documentation.**
  That was considered and rejected.
  Many pages would mean as many recipes to iterate by hand.
  A recipe is a tool the principal shapes, while a page is to come from
  the project's documents with no hand in between.
  The documentation map replaces the recipes, with one generated entry
  per page.

## A worked example

A generic recipe for an executive summary in two languages, in the shape
the recipe template defines. The slug, purpose and audience are
placeholders.

```markdown
---
project: example-project
purpose: executive summary
audience: the steering group
version: 0.3
languages: en, cs
---

# Recipe — executive summary

## Inputs
- 10-intent.md

## Instructions
Plain and direct. Lead with the objective, then the positions that
matter most to the steering group. Omit open threads. One page.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template none,
  model <name>.

## Template
# <Project title>: executive summary
## Objective
<two or three sentences>
## Key positions
- <position>: <one line>
```

From this recipe `/render` writes `renders/<recipe>.en.md` and, in the
same run, its translation `renders/<recipe>.cs.md`, each opening with
its provenance, and a plain `.docx` beside each.
Only on the principal's `/publish` does a designed file appear in
`published/`.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a render.
- [Publish a designed file](../use/publish-a-designed-file.md): the
  designed file.
- [The screenplay and its player](the-screenplay-and-its-player.md):
  the screenplay, its two formats and where a public one lands.
- [The work product](the-work-product.md): the output that is not a
  render.
- [Render provenance](../reference/render-provenance.md): the
  provenance block and the definition of stale.
- [The documentation](the-documentation.md): the pages, generated
  without a recipe.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
