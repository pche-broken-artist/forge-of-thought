---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: e1c0c091b0897e29
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
documents of a project's chain. Examples are a pitch, an architecture
picture, an executive summary or the repository README. This page
explains what a render and its recipe are, how an output gets from the
chain to a finished file, and why a render is never edited by hand. It
is for anyone who uses the forge, extends it or wants to judge how it
works.

## What it is

The chain is the series of versioned documents a project's thinking
travels through. These documents are the artefacts: the brief, the
intent and any layers below it. The principal (the person whose
thinking is being forged) composes them with Claude. The artefacts are
the one source of truth.

A render is generated from one or more artefacts for a given audience.
It is never a source of truth. It assigns nothing and is not part of
the chain.

The thing a person works on is the render's **recipe**, a file at
`recipes/<recipe>.md`. One recipe holds everything a render is made
from:

- Inputs: the artefacts the render is generated from, one or several.
- Audience and instructions: tone, emphasis, what to leave out, length.
- Format: optional, the file formats the output is turned into.
- Template: the literal skeleton of the render, with placeholders.

The recipe is versioned like other versioned documents of the forge.
Its history is kept in a companion file beside it. A recipe is a tool,
not a record of thinking. It is never approved, so it carries no
status and stays at a 0.x version for life.

### Where the boundary lies

The boundary between an artefact and a render is authorship, not
audience. An artefact is composed by the principal: Claude proposes and
the principal decides. A render is generated from artefacts. So an
article the principal writes is a layer of the chain, and its
translation is a render.

### What is a render and what is not

Every project has a README, and every thought project also has release
notes. Both are renders of the project's own recipes,
`recipes/readme.md` and `recipes/release-notes.md`, written to the
project root. The engine has its own README and release notes made the
same way. A library (a project that only holds shared material) has a
README only. Its README is a catalogue of what it holds. A library has
no release notes because release notes are derived from the history of
an intent, and a library has no intent.

Two kinds of output are not renders:

- A page of the documentation is generated from a documentation map,
  with no recipe in between. See [The documentation](the-documentation.md).
- A work product is an output with work of its own. See
  [The work product](the-work-product.md).

## How it works

### Generation

`/render <recipe>` regenerates the render from its recipe. The output
lands at `renders/<recipe>.md` unless the recipe's `output:` names
another place. A render is overwritten freely and carries no date in
its name.

Every render opens with its provenance. The provenance cites the
recipe and every input, each with its version. A render is stale when
the recipe or an input has moved past the version it cites. The ledger
(the state report of a project, built from its documents) shows each
render in its Renders table. The exact provenance block and the
definition of stale are in [Render provenance](../reference/render-provenance.md).
How you run a generation is in [Render an output](../use/render-an-output.md).

A render may use another render as an input, for example a slide that
shows an architecture picture. The citing recipe must then declare that
render among its inputs. This way provenance and staleness follow the
dependency.

### What a recipe fixes and what it does not

A recipe is deliberately loose. Its template fixes the structure and
what information appears where, never the wording. A presentation
recipe says what belongs on a slide, not how it is phrased. Each
generation derives the words again from the current inputs.

Where a wording must not move, the recipe pins it as fixed text. A
pinned title, claim or line regenerates word for word. Everything else
is derived again freely.

### When a render is regenerated

A render is regenerated in two cases only:

- The principal asks for it with `/render`.
- A release regenerates it.

Claude never regenerates a render on its own judgement. It reports that
a render is stale and offers to regenerate it. Every release regenerates
the README and the release notes. Every other render stays as stale as
the principal lets it be. The state map of `/forge` shows staleness. No
check reports it.

When a release has regenerated renders, its summary says what
materially changed in them. The principal then rules on that change
before the release commit, without reading a full diff.

### Several languages

A recipe may declare its output languages in `languages:`. The first
language is the primary one and the rest are its translations. `/render`
generates the primary render. In the same run it translates that render
into every other language, scene for scene and line for line. Each
language gets its own render, `renders/<recipe>.<lang>.md`. Each has its
own provenance and its own row in the ledger. A translation cites the
primary render it was made from. A recipe with one language keeps
`renders/<recipe>.md`.

### Two steps to a file

Everything the forge produces is Markdown, renders included. A
presentation is a Markdown file saying what is on each slide. Where the
recipe's `## Format` section names a format, the output is made in two
steps, each with its own command:

1. `/render` writes the Markdown and, beside it, the plain file. A
   deck becomes a `.pptx` and other renders a `.docx`, through pandoc.
   This step is deterministic and cheap, and it may be repeated freely.
2. `/publish` makes the designed file through a model and its document
   skills, into `published/`. It runs only on the principal's command.
   It never runs as part of `/render`, of a release, or on Claude's
   own judgement. It makes a file and sends nothing anywhere.

The provenance of a designed file stands in a companion beside it,
`published/<recipe>.md`. The ledger's Published table says what each
designed file was made from and whether it is current or stale.

`/publish` takes the render as it lies on disk and never renders.
Because a render is made by a model, a second render would never be the
same. Publishing one would publish a text the principal has not read.
Where the render is stale, `/publish` says so before the conversion and
the principal decides.

A screenplay is the exception. Its render becomes a video or the events
its player plays, through a script alone. It has no designed step. See
[The screenplay and its player](the-screenplay-and-its-player.md).

A recipe without a `## Format` section ends at the Markdown. The
Markdown render stays the source of truth in every case. A plain or a
designed file is a second-order output: regenerated at will and never
edited by hand. How you make one is in
[Publish a designed file](../use/publish-a-designed-file.md).

### Composing a recipe by genre

A recipe may be composed through a genre interview, `/recipe <genre>`.
Each genre has one definition with the questions to ask. It also has a
template that extends the base shape of a recipe and never replaces it.
The genres are `presentation`, `readme`, `release-notes` and
`screenplay`. How you compose one is in
[Compose a recipe](../use/compose-a-recipe.md).

The readme genre fixes what a README carries:

- what the project is;
- what one gets from it;
- how to start;
- where it stands;
- where the documentation is.

A README stands alone. Every claim in it comes from the inputs, and
anything superseded in the inputs does not survive. It closes with a
short section saying it is a render, regenerated at every release and
never edited by hand.

## Why

**Why a render is never edited by hand.** A render is never edited by
hand because the artefacts must stay the one source of truth. A fix to
a render goes into its recipe or its inputs, and the render is
regenerated. A change to the forge itself is complete only once its
intent is updated and its README regenerated.

**Why the recipe fixes structure, not words.** Fixed text in the
template would turn the recipe into the render. The inputs would then
mean nothing.

**Why regeneration waits for the principal's word.** Regeneration is
stochastic: the same inputs never guarantee the same words. A
regeneration nobody reviews is therefore an unreviewed edit of a
document others read. The pinned wording and the release summary are
the two defences. Neither one blocks the work.

**Why translations come from the primary render.** The quotes of a
transcript, the beats and the captions are chosen once. A second
generation would choose them again, and differently. Translating the
primary keeps the same cut in every language.

**Why two steps.** The steps are divided by cost. The expensive
conversion through a model then runs as seldom as possible.

**Why release notes are a log.** A reader wants to see plainly what was
added, changed and removed in each release.

**Why a render is not regenerated at every save.** The forge considered
having `/save` regenerate only the renders whose recipe or input had
moved, and rejected it. On a project the README's input is the ledger,
which changes with every operation, so little would be saved. It would
also add a staleness state that `/save`, `/forge` and the checks would
all have to read alike.

**Why the documentation has no recipes.** One recipe per page was
considered and dropped. Every page would need a recipe iterated by
hand, but a recipe is a tool the principal shapes. A page is to come
from the project's documents with no hand in between. A documentation
map, with one generated entry per page, takes the place of the
recipes.

## A worked example

A generic recipe for an executive summary in two languages, made into
a Word file. The project slug is a placeholder.

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
- 20-assignment.md

## Instructions
Plain and direct. One page. Lead with the objective, then the three
largest risks. Leave out anything already marked out of scope.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template none,
  model <name>.

## Template
# <Project title>: executive summary

## Objective
<the objective, in two sentences>

## Risks
- <risk>
```

`/render` makes `renders/<recipe>.en.md` and translates it into
`renders/<recipe>.cs.md`, with the plain Word file beside each. Each
render opens with provenance citing recipe version 0.3 and both inputs
with their versions. A new version of the intent makes both renders
stale until the principal asks for them again.

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

Generated on 2026-10-25 for version 6.1 from the files the front-matter
names; never edited by hand.
