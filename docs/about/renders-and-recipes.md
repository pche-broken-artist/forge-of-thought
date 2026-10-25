---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 20757fca98be1968
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

A render is an output made for one audience and generated from the
documents of a project, and a recipe is the file it is generated
from. This page explains what the two are, how an output gets from
the recipe to a finished file, and why a render is never edited by
hand. It is written for the user who makes renders, the extender who
adds a kind of recipe, and the evaluator who wants to understand the
idea.

## What it is

A project of the forge keeps its thinking in the chain. The chain is
the row of versioned documents the principal (the person whose
thinking is being forged) composes with Claude: a brief, an intent,
and the layers below it that the project needs. These documents are
the source of truth.

A render is an output generated from that chain for a particular
audience. Examples:

- a pitch for a group;
- an architecture picture;
- an executive summary;
- the repository README.

A render is never edited by hand. What is worked on instead is its
recipe, `recipes/<recipe>.md`. A recipe holds four things in one
file:

- the inputs (one artefact of the chain, or several);
- the audience;
- the instructions;
- the literal template of the output.

The command `/render <recipe>` regenerates the render from its
recipe. See [Glossary](../reference/glossary.md) for the other terms
of the forge in one line each.

A render assigns nothing and is not part of the chain. The artefacts
stay the source of truth. The boundary between the chain and a
render is authorship, not audience. A chain artefact is composed by
the principal: Claude proposes, the principal composes. A render is
generated from artefacts. So an article the principal writes is a
layer of the chain, and its translation is a render.

A recipe is a tool, not a record of thinking. It carries a version
in its front-matter and no status field. A recipe is never approved,
so its version stays below 1.0 for life. Like every versioned
document, it keeps its history in a companion file beside it.

Not every generated file is a render. The pages of the documentation
are generated from the project's documents through the documentation
map, with no recipe in between (see
[The documentation](the-documentation.md)). A work product is
another kind of output with its own way of being made (see
[The work product](the-work-product.md)).

## How it works

### The recipe

A recipe is deliberately loose. Its template fixes the structure and
what information appears where. It does not fix the wording. A
presentation recipe, for example, says what belongs on a slide, not
the phrasing or where it stands on a picture. Each rendering derives
the words again from the current inputs.

A recipe may still pin load-bearing wording as fixed text, such as a
title, a claim or a fixed line. What is pinned regenerates word for
word. Everything else is derived again freely.

A render may use another render as an input, such as a deck slide
that shows an architecture picture. The citing recipe must declare
that render among its inputs.

### Composing a recipe by genre

A recipe may be composed through a genre interview, `/recipe
<genre>`. Each genre has a definition with the questions to ask and a
skeleton, `templates/recipe-<genre>.md`. The skeleton extends the
base recipe shape and never replaces it. The genres are
`presentation`, `readme`, `release-notes` and `screenplay`. How you
compose one step by step is in
[Compose a recipe](../use/compose-a-recipe.md).

### Provenance and staleness

Every render opens with its provenance. The provenance cites the
recipe and every input, each with its version. A render goes stale
when the current version of something it cites differs from the
version it cites. The ledger (the state report of a project, made
from its documents when it is read) carries a Renders table that
mirrors the provenance. The exact block and the definition of stale
are in [Render provenance](../reference/render-provenance.md).

A render is regenerated in two cases only:

- on the principal's explicit `/render`;
- by a `/release`, which regenerates the README and the release
  notes.

Claude never regenerates a render on its own judgement. It reports
that a render is stale and offers to regenerate it. Every render
other than the README and the release notes stays as stale as the
principal lets it be. No check reports the staleness of a render;
the state map of the project shows it.

When a `/release` regenerates renders, its summary reports what
materially changed in them. The principal then rules on that change
before the release is committed, without reading a full diff. How to
run a render is in [Render an output](../use/render-an-output.md).

### Several languages

A recipe may declare several output languages in `languages:`. The
first is the primary language and the rest are its translations.
`/render` generates the primary render. In the same run it
translates it into every other language, scene for scene and line
for line. The result is one render per language,
`renders/<recipe>.<lang>.md`. Each has its own provenance and its own
row in the ledger, and a translation cites the primary render it was
made from. A recipe with one language keeps `renders/<recipe>.md`.

### Two steps to a finished file

Everything the forge produces is Markdown, renders included. A
presentation is a `.md` file that says what is on each slide. The
forge carries a few tools at its edge that turn a Markdown render
into a delivery format. An output is made in two steps, each with its
own command.

1. `/render` generates the Markdown. Where the recipe names a
   format, it also makes the plain file beside it. A deck becomes a
   `.pptx` and a document a `.docx`, through pandoc. A screenplay
   becomes a video or the events its player plays, through
   `scripts/md2video.py`. This step is deterministic and cheap, and
   it may be repeated freely.
2. `/publish` makes the designed file through a model and its
   document skills, into `published/`. It runs only on the
   principal's command. It never runs from `/render`, from `/release`
   or on Claude's own judgement. It makes a file and sends nothing
   anywhere. The ledger's Published table says what each published
   file was made from and whether it is `current` or `stale`.

A screenplay has no designed step: its video or player is made by the
script alone. What a screenplay is, its two formats and where a
public one lands are in
[The screenplay and its player](the-screenplay-and-its-player.md).
How the designed file is made is in
[Publish a designed file](../use/publish-a-designed-file.md).

The format and what each step needs stand in the recipe's
`## Format` section. They are never copied into the render. A recipe
without that section ends at the Markdown. The plain file and the
published file are tracked in git like any render and never edited
by hand. The Markdown render stays the source of truth.

### The README and the release notes

Every project has a README, and every thought project also has
release notes. Both are renders of the project's own recipes,
`recipes/readme.md` and `recipes/release-notes.md`, written into the
project root. The engine's own README and release notes are made the
same way. Every `/release` of a project regenerates both. A library
(a project that holds shared material and no chain) has a README
only, a catalogue of what it holds. Both recipes are genres of
`/recipe`, and `/new-project` creates them.

The readme skeleton owns what a README carries:

- what the thing is;
- what one gets;
- how to start;
- where it stands;
- where the documentation is.

A README stands alone: no claim in it requires opening the chain.
Every claim in it comes from the inputs, and nothing superseded in
the inputs survives in it.

The release notes are a log of releases, not a story. There is one
section per release, newest first, with one sentence per change from
the reader's side. The sections are derived at the release from the
history records of the chain. What the reader must do after a change
is never derived: it is written with the change in its history
record and carried into the release notes word for word.

## Why

**Why a render is never edited by hand.** A render is generated from
the artefacts, which stay the one source of truth. A change made by
hand in a render would live nowhere in the chain. Fixes therefore go
into the recipe or the inputs, and the render is regenerated.

**Why the recipe fixes structure and not wording.** Each rendering
derives the words from the current inputs. Fixing the text in the
template would turn the recipe into the render. The inputs would then
mean nothing.

**Why a render is regenerated only on the principal's word or by a
release.** Regeneration is stochastic: the same inputs never
guarantee the same words. An unreviewed regeneration is therefore an
unreviewed edit of a document that faces outward. Pinned wording and
the release summary of what changed are two light defences. Neither
is a gate.

**Why translations are made from the primary render in the same
run.** In a screenplay the quotes of a transcript, the beats and the
captions are chosen once. A second generation would choose them, and
the cut, again differently. Translating the primary render keeps the
same cut in every language.

**Why two steps divided by cost.** The expensive conversion should
run as seldom as possible. The cheap step can run at every render;
the designed step runs only when the principal asks.

**Why `/publish` never renders.** A render is made by a model and is
never the same twice. A fresh render at publish time would publish a
text the principal has not read. `/publish` therefore takes the
render as it lies on disk. A stale render is named before the
conversion, and the principal decides.

**Why a project's README is a render too.** The forge runs every
project the way it runs itself: the recipe is iterated, the render
is regenerated and never edited by hand. A process change of the
engine is complete only once its intent is updated and the README
regenerated.

**What was rejected.**

- Regenerating at every save only the renders whose recipe or input
  moved, with a mark for a render skipped on the principal's word.
  It would save perhaps a third of the engine's saves and nothing on
  projects, whose README input (the ledger) moves at every operation.
  It would also add a staleness state that three commands must all
  read alike. Two commands, one to save and one to release, save
  everything and add nothing.
- A recipe per page of the documentation. Eighty pages would mean
  eighty recipes to iterate by hand. A recipe is a tool the principal
  shapes, while a page is to come from the project's documents with
  no hand in between. The documentation map replaces the recipes,
  with one generated entry per page.

### A worked example

A recipe of the base shape, plainly generic, looks like this:

```markdown
---
project: <slug>
purpose: executive summary
audience: the steering group
version: 0.1
# languages: en, cs
---

# Recipe — executive summary

## Inputs
- 10-intent.md

## Instructions
<audience, tone, what to emphasise, what to omit, target length,
register>

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template
  none, model <name>.

## Template
# <title>
<the literal skeleton of the render, with placeholders>
```

`/render` reads the inputs and the instructions, fills the template
and writes `renders/<recipe>.md` with its provenance at the top. The
`## Format` section names `docx`, so the same run makes the plain
`.docx` beside it. If the `languages:` line were active, the run
would write one render per language instead. Only the principal's
`/publish` would make the designed file in `published/`.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
