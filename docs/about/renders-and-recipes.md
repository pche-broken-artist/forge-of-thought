---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 394bc59a646a2a4b
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

A render is an output made for one audience, generated from the
documents of a project and never edited by hand. This page says what
a render is, what its recipe is, how an output is made from the two
and why the forge keeps them apart from the chain. It is for anyone
who works with a project of the forge, extends it or wants to
understand why an output is regenerated rather than corrected: the
principal (the person whose thinking is being forged), a colleague
who receives a render, and a reader who only evaluates the forge.

## What it is

A render is an audience-specific output generated from the chain
(the versioned documents of a project, from its brief and intent
downward). A pitch for a group, an architecture picture, an executive
summary and the README of the repository are renders.

A render is never a source of truth. The artefacts of the chain
remain the sole source of truth. A render assigns nothing and is not
part of the chain.

A render is never edited by hand. What is iterated is its recipe. A
recipe is one versioned file, `recipes/<recipe>.md`, holding in one
place:

- the inputs: one artefact of the chain or several, by path
- the audience
- the instructions: tone, what to emphasise, what to omit, register
- the literal output template, with placeholders
- optionally a format section, saying what file is made beyond the
  Markdown and what each step needs

The command `/render <recipe>` regenerates the render from its
recipe. Where the render lands, how the generation is isolated and
what provenance it opens with are defined in
`.claude/skills/render/SKILL.md`. How to compose a recipe is on
[Compose a recipe](../use/compose-a-recipe.md); how to regenerate a
render is on [Render an output](../use/render-an-output.md).

The boundary between the chain and a render is authorship, not
audience. A chain artefact is composed by the principal: Claude (the
model that runs the forge) proposes, the principal composes. A render
is generated from artefacts. An article the principal writes is a
layer of the chain; its translation is a render.

A recipe is a tool, not a record of thinking. It carries a version
and an `updated` date in its front-matter, enough for a render to
cite, and no status field. A recipe is never approved and stays at a
0.x version for life. Being versioned, a recipe keeps its history in
a companion file beside it, `recipes/<recipe>.history.md`, like every
versioned kind of document.

Two things look like renders and are not. A page of the
documentation is generated from the project's documents without a
recipe: see [The documentation](the-documentation.md). A work product
is an output made with work of its own and is neither artefact nor
render: see [The work product](the-work-product.md).

## How it works

### Provenance and staleness

Every render opens with its provenance: the recipe and every input,
each cited with its version. The ledger (the file `ledger.md`, the
single source of truth for a project's state) mirrors the provenance
in its Renders table.

A render is stale when a cited version differs from the one its
recipe or an input now has. What the provenance block holds and how
stale is defined exactly is on
[Render provenance](../reference/render-provenance.md).

No check reports the staleness of a render. The state map of the
project, shown by `/forge`, shows it. Claude never regenerates a
render on its own judgement: it reports staleness and offers. A
render is regenerated only by the principal's explicit `/render` or
by `/release`. A release regenerates the README and the release notes
of the project. Every other render is as stale as the principal lets
it be.

A recipe may pin load-bearing wording as fixed text: a title, a
claim, a fixed line. What is pinned regenerates verbatim. Everything
else re-derives freely from the current inputs. A release that
regenerated renders reports in its summary what materially changed in
them, so that the principal rules on the difference before the
release commit without reading a full diff.

### Several languages

A recipe may declare several languages in `languages:`. The first
is primary; the rest are its translations. `/render` generates the
primary render and, in the same run, translates it into every other
language, scene for scene and line for line, so that every language
carries the same cut.

There is one render per language, `renders/<recipe>.<lang>.md`,
each with its own provenance and its own row in the ledger's Renders
table. A translation cites the primary render it was made from. A
format file follows the name of its render. A recipe with one
language keeps `renders/<recipe>.md`. A render may be in any
language, or languages, its recipe declares.

### Two steps, divided by cost

Everything the forge produces is Markdown, renders included. A
presentation is a `.md` file saying what is on each slide, with
mermaid for pictures. The forge ends at content, but carries its
delivery-format tools at its edge. An output is made in two steps,
each with its own command.

The first step is `/render`. It generates the Markdown and, where the
recipe names a format, the plain file beside it: a `.docx` or a
`.pptx` through pandoc, in `renders/`. For a screenplay the same step
makes a video or the events of its player through
`scripts/md2video.py` instead. This step is deterministic and cheap
and is repeated freely.

The second step is `/publish`. It makes the designed file through a
model and its document skills, into `published/`. It runs only on
the principal's command, never by `/render`, never by `/release` and
never on Claude's own judgement. It makes a file and sends nothing
anywhere. `/publish` takes the render as it lies on disk and never
renders: a stale render is named before the conversion, and the word
is the principal's. The ledger's Published table says what each
published file was made from and whether it is `current` or `stale`.
See [Publish a designed file](../use/publish-a-designed-file.md).

A screenplay has no designed step and no published file. What a
screenplay is, its two formats and where a public one lands is on
[The screenplay and its player](the-screenplay-and-its-player.md).

The format and what each step needs stand in the recipe's `## Format`
section and are never copied into the render. A recipe that names no
format ends at the Markdown. The conversions are three scripts,
`scripts/md2pptx.py`, `scripts/md2docx.py` and `scripts/md2video.py`.
What each needs installed, how a template or a reference document is
named, where the output lands and what becomes of a diagram is said
by each script's own header. A plain or a published file is tracked
in git like any render output and never edited by hand: the Markdown
render stays the source of truth.

### The README and the release notes

Every project has a README as a render of its own
`recipes/readme.md`, with its output in the project root. A thought
project also has release notes from `recipes/release-notes.md`. The
engine's own README and release notes are made by the same mechanism.
Every `/release` of the project regenerates both after its check.

The README presents the project to a human meeting its repository
for the first time: a recipient, a colleague, the principal after
weeks away. It stands alone, so that no claim requires opening the
chain. It carries what the thing is, what one gets, how to start,
where it stands and where the documentation is. Every claim is
derivable from the inputs; nothing is invented, and anything
superseded in the inputs does not survive. Content fixes go into the
recipe or the inputs, and the file is regenerated. A process change
is complete only once the intent is updated and the README
re-rendered.

The release notes are a log of releases, not a story: one section
per release, newest first, with fixed groups in a fixed order and one
sentence per change from the reader's side. The sections are derived
at the release from the records of the history log since the previous
release. One thing is never derived: what the reader must do after a
change is written with the change, in the `Action` field of its
history record, and the render carries it into its "Action required"
part word for word.

A library has a README only: a catalogue of what it holds and how to
use it, from its ledger and indexes. Release notes are derived from
the history of an intent, which a library does not have; its history
is git.

### Genres

A recipe may be composed through a genre interview, `/recipe <genre>`,
with one definition per genre carrying the elicitation checklist and
the genre's skeleton, `templates/recipe-<genre>.md`, extending the
base recipe shape and never replacing it. The genres today are
`presentation`, `readme`, `release-notes` and `screenplay`. The
readme and the release-notes recipes of a new project are scaffolded
by `/new-project`.

A render may cite another render as a picture source, such as a deck
slide citing an architecture picture, when the citing recipe declares
that render among its inputs. Provenance and staleness then track the
dependency.

## Why

A render is never edited by hand because it is generated: a hand
edit would be lost at the next regeneration, and the artefacts, not
the render, are the source of truth. A fix therefore goes into the
recipe or into the inputs, and the file is regenerated.

The recipe is kept loose on purpose. The template fixes the structure
and what information appears where, never the wording. A presentation
recipe says what belongs on a slide, not its phrasing or its placement
on a picture. Each rendering re-derives the words from the current
inputs. Fixing the text in the template would turn the recipe into
the render and make the inputs meaningless.

A regenerated render passes under the principal's eyes because
regeneration is stochastic: the same inputs never guarantee the same
words. An unreviewed regeneration is therefore an unreviewed edit of
an outward-facing document. For the same reason `/publish` never
renders: a second render would publish a text the principal has not
read.

A recipe with several languages translates in one run, from the
primary render, because the quotes of a transcript, the beats and the
captions are chosen once. A second generation would choose them again
differently, and the languages would not carry the same cut.

The two steps are divided by cost so that the expensive conversion
runs as seldom as possible. The plain file is cheap and deterministic
and may be remade at every render. The designed file costs a model
run and is made only when the principal asks for it. The word
"publish" was the principal's choice; it agrees with the rule that
only the principal publishes.

Regenerating only stale renders at every save was considered and
rejected. It would have saved little on the engine and nothing on
projects, whose README input, the ledger, moves at every operation,
and it would have added a staleness state that several commands must
all read alike. The present shape, a cheap save without a render and
a release that regenerates the README and the release notes, saves
everything and adds nothing.

Making the documentation out of renders, one recipe per page, was
considered and rejected. Many pages would mean as many recipes to
iterate by hand. A recipe is a tool the principal shapes, while a
page is to come from the project's documents with no hand in between.
The documentation map replaces the recipes, with one generated entry
per page.

Every README closes with one fixed sentence, part of the readme
genre, so that whoever finds the project knows what runs it. The
engine's own README is the one exception, because that sentence
exists to point a visitor to the engine and the engine's README is
that destination.

## A worked example

A generic recipe for a short summary of a project's intent, for a
recipient who has not read the chain, has this shape. The slug and
the paths are placeholders.

```markdown
---
project: <slug>
purpose: a one-page summary of the intent for the recipients
audience: the recipients of the assignment
version: 0.3
updated: 2026-10-14
last_change: <derived from the records of the newest version in recipes/summary.history.md>
languages: en, fr
---

# Recipe - a one-page summary of the intent

## Inputs
- 10-intent.md
- 20-assignment.md

## Instructions
- One page. Plain, direct. No history of how a position was reached.
- The title is pinned: "What we are asking for".
- Omit every rejected direction; carry every position in scope.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template none.

## Template
# What we are asking for

## Why
<two or three sentences from the intent's purpose>

## What
<one line per position in scope, grouped as the intent groups them>

## What we expect back
<one line per deliverable of the assignment>
```

`/render summary` would make `renders/summary.en.md` from the two
inputs and, in the same run, `renders/summary.fr.md` translated from
it, each opening with its own provenance and each with a plain
`.docx` beside it. If the intent then moves to a newer version, both
renders are stale until the principal asks for `/render summary`
again. `/publish summary` would make the designed file from the
render as it lies on disk, only when the principal says so.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a render.
- [Publish a designed file](../use/publish-a-designed-file.md): the designed file.
- [The screenplay and its player](the-screenplay-and-its-player.md): the screenplay, its two formats and where a public one lands.
- [The work product](the-work-product.md): the output that is not a render.
- [Render provenance](../reference/render-provenance.md): the provenance block and the definition of stale.
- [The documentation](the-documentation.md): the pages, generated without a recipe.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
