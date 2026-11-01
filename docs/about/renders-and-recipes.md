---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: deff35c37f47a520
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
  - projects/forge/10-intent.md#POS.1910
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0240
---

# Renders and recipes

A render is an audience-specific output generated from the documents
of a project's chain, and a recipe is the file that says how it is
made. This page explains why an output is generated from a recipe and
never edited by hand, where the line between the chain and a render
runs, how a recipe is versioned, how an output grows from Markdown
into a plain file and a designed file, and which files in `renders/`
and `published/` belong to the forge and which to the principal (the
person whose thinking is being forged). It is written for the user
who wants an output, for the extender who adds a recipe or a genre,
and for the evaluator who asks why the forge is built this way.

## What it is

A render is an output made for one audience from the chain: a pitch
for a group, an architecture picture, an executive summary, the
README of the repository. It is generated, never composed, and it is
never edited by hand. It assigns nothing and is not part of the
chain. The artefacts of the chain stay the only source of truth.

What is iterated is the render's recipe, a file `recipes/<recipe>.md`
in the project. One recipe holds the inputs (one artefact or several),
the audience, the instructions and the literal template of the
output. A recipe is a tool, not a record of thinking. It carries a
version in its front-matter and no status. The way to make one is
[Compose a recipe](../use/compose-a-recipe.md); the way to make the
output from it is [Render an output](../use/render-an-output.md).

The boundary between the chain and a render is authorship, not
audience. A chain artefact is composed by the principal, with Claude
proposing. A render is generated from artefacts. An article the
principal writes is a layer of the chain; its translation is a
render.

Every render opens with its provenance: the recipe and every input it
was made from, each with its version. The shape of that block and the
exact definition of a stale render are given in
[Render provenance](../reference/render-provenance.md). In short, a
render is stale when a version it cites is no longer the version its
document carries. The ledger (the state report of a project, made at
read time from its documents) mirrors the provenance in its Renders
table. Its Published table says what each designed file was made from
and whether it is `current` or `stale`.

The pages of the documentation look like renders and are not. They
are generated without a recipe, from a map of the project's
documents; the page [The documentation](the-documentation.md)
explains them, and the reason stands under Why below.

## How it works

### The recipe

A recipe has four sections and a front-matter. The front-matter names
the project, the purpose, the audience and the version. Two optional
keys change where and how the output lands:

- `output:` sends the render somewhere other than the default
  `renders/<recipe>.md`, read relative to the project root; a leading
  slash means the engine root.
- `languages:` lists the output languages, the first primary, the
  rest its translations.

The sections are these:

- Inputs: the artefacts the render is generated from, by path, one per
  line; more than one is legitimate.
- Instructions: the audience, the tone, what to emphasise, what to
  omit, the length, the register; everything the renderer must know
  beyond the template.
- Format: optional; a recipe without it ends at the Markdown. It names
  the format and what each of the two steps below needs. It is never
  copied into the render.
- Template: the literal skeleton of the render, with placeholders,
  always Markdown.

A recipe is deliberately loose. The template fixes the structure and
says what information appears where, never the wording. A recipe for
a presentation says what belongs on a slide, not how it is phrased or
where it sits on the picture. Each rendering re-derives the words
from the current inputs. One exception is allowed on purpose: a
recipe may pin load-bearing wording as fixed text, such as a title, a
claim or a fixed line, and what is pinned regenerates verbatim while
everything else re-derives freely.

A render may serve as an input of another render, for instance a deck
slide citing an architecture picture. The citing recipe has to
declare it among its Inputs. Then the provenance and the staleness of
the deck follow the picture.

### Genres

A recipe may be composed through a genre interview, `/recipe <genre>`.
One definition per genre carries the questions of the interview, and
the genre's skeleton (`templates/recipe-<genre>.md`) extends the base
shape of a recipe, never replaces it. The genres today are
`presentation`, `readme`, `release-notes` and `screenplay`.

### Versioning a recipe

A recipe is versioned by the house scheme and keeps its history in a
companion beside it, like every versioned document. It stays 0.x and
is iterated continuously. Only the principal names an integer, 1.0 or
2.0; the recipe takes it and the count goes on from there, 2.1, 2.2.
Claude never proposes the integer. The number means nothing beyond
the principal's own mark, and nothing guards or reads it. A recipe's
date is computed from its history, and a render cites the recipe's
version.

### Regeneration

`/render <recipe>` regenerates the output from the recipe. The render
is undated and overwritten freely. A render is regenerated in two
cases only: by the principal's explicit `/render`, or by `/release`,
which regenerates the README and the release notes of the project at
every release. Claude never regenerates a render on its own judgement.
It reports the staleness and offers. Every other render is as stale as
the principal lets it be. No check reports the staleness of any render;
the state map of the project shows it.

A regenerated render passes under the principal's eyes. A release that
regenerated renders reports in its summary what materially changed in
them, so that the principal rules on the difference before the release
commit without reading a full diff.

### Several languages in one run

Where a recipe declares `languages:`, `/render` generates the primary
render and, in the same run, translates it into every other language,
scene for scene and line for line. The result is one render per
language, `renders/<recipe>.<lang>.md`, each with its own provenance
and its own row in the ledger's Renders table. The translation cites
the primary render it was made from, and a format file follows the
name. A recipe with one language keeps `renders/<recipe>.md`.

### Two steps, divided by cost

Everything the forge produces is Markdown, renders included: a
presentation is a `.md` that says what is on each slide, with mermaid
for the pictures. The forge still ends at content, but it carries its
delivery-format tools at its edge. An output is made in two steps,
each with its own command.

The first step is `/render`. It generates the Markdown and, where the
recipe names a format, the plain file beside it through the script the
format names: a `.pptx` from a deck render, a `.docx` from a document
render, a video or the events of a player from a screenplay render.
This step is deterministic, cheap and repeated freely.

The second step is `/publish`. It makes the designed file through a
model and its document skills, into `published/`. It is expensive and
runs only on the principal's command, never by `/render`, never by
`/release`, never on Claude's own judgement. It makes a file and sends
nothing anywhere. It takes the render as it lies on disk and never
renders; a stale render is named before the conversion and the word
is the principal's. The provenance of the designed file stands in a
companion `published/<recipe>.md` beside it, and the ledger's
Published table reads it. The page
[Publish a designed file](../use/publish-a-designed-file.md) shows the
step.

A screenplay has no designed step: its video or its player events are
made by a script alone, and its `output:` may send a public file into
the engine's `docs/videos/`, the one public folder. The page
[The screenplay and its player](the-screenplay-and-its-player.md)
explains it.

A plain or a published file is tracked in git like any render output
and is never edited by hand. The Markdown render stays the source of
truth. All other format conversion stays outside the forge.

### README and release notes

Every project has a README as a render of its own `recipes/readme.md`,
with the project root as its output. A thought project also has
release notes from `recipes/release-notes.md`. This is the same
mechanism as the engine's own README and release notes, and every
`/release` of the project regenerates both after its check. A library
has a README only: a catalogue of what it holds and how to use it,
from its ledger and its indexes. Both recipes are genres of `/recipe`
and are scaffolded by `/new-project`.

What a README carries is said in one place, the readme skeleton: what
the thing is, what one gets, how to start, where it stands and where
the documentation is. The rest belongs to the ledger and to the
documentation. The README stands alone, so that no claim requires
opening the chain. Every claim in it is derivable from the inputs;
nothing is invented, and anything superseded in the inputs must not
survive. Content fixes go into the recipe or the inputs, and the file
is regenerated.

Release notes are a log of releases, not a story. There is one section
per release, newest first, with fixed groups in a fixed order inside
it and one sentence per change from the reader's side with a pointer.
The sections are derived at the release from the records of the
history log since the previous release. One thing is never derived:
what the reader must do after a change is written with the change, in
the `Action` field of its history record, and the release notes carry
it word for word. At a major release the minors since the previous
major are folded into it.

### The principal's own files

The forge owns in `renders/` and `published/` only the files its
recipes name: the render and its translations, the plain file, the
designed file and its companion. Any other file there is the
principal's own, made by hand from the forge's files: a copy under a
new name that he edits, a PDF saved from Word or PowerPoint, an HTML
of a diagram. Such a file is kept in git beside the forge's files. It
has no companion, no row in the ledger and no check, and the forge
never reads, overwrites or raises it. The forge's own file stays
untouched by hand: what is to change is copied first.

## Why

A render is never edited by hand because the artefacts of the chain
are the only source of truth. A hand edit of a render would be a
second place where content lives, and the next regeneration would
overwrite it. Content fixes go into the recipe or the inputs instead.

A recipe fixes structure and never wording because each rendering is
to re-derive the words from the current inputs. Fixing the text in
the template would turn the recipe into the render and make the
inputs meaningless.

A render is regenerated only on the principal's word or by a release
because regeneration is stochastic. The same inputs never guarantee
the same words, so an unreviewed regeneration is an unreviewed edit of
an outward-facing document. The pinned wording and the release's
summary of what changed are two light defences; neither is a gate,
because only the principal publishes and nothing blocks him.

A recipe carries no status because approval has a meaning only where
someone receives the document, and a recipe is received by nobody. For
the same reason the integer a principal gives a recipe is his own mark
and not an approval: nothing guards or reads it.

The translations of a render are made in the same run as the primary
because the quotes of a transcript, the beats and the captions are
chosen once. A second generation would choose them again differently,
and the translation would no longer be the same cut.

The output is made in two steps divided by cost so that the expensive
conversion runs as seldom as possible. The plain file is cheap and
deterministic and may be remade at every render; the designed file
costs a model's run and is made only when the principal asks for it.
`/publish` never renders because a render made by a model is never the
same twice: a second one would publish a text the principal has not
read.

A render is not regenerated at a save, even when stale, and no
"stale-only" rendering runs at a save. The forge rejected that shape:
it would spare only a part of the engine's saves and nothing on
projects, whose README input, the ledger, moves at every operation,
and it would add a staleness state that several commands must all
read alike. The two commands, save and release, do everything the
shape would do and add nothing.

The README and the release notes are regenerated at every release
because a process change is complete only once the intent is updated
and the README re-rendered, and because a reader wants to see plainly
what was added, changed and removed. A library has no release notes
because release notes are derived from the history of an intent,
which a library does not have; its history is git.

The pages of the documentation are not renders, although they look
like them. A recipe per page was considered and dropped: eighty pages
would mean eighty recipes to iterate by hand, and a recipe is a tool
the principal shapes, while a page is to come from the project's
documents with no hand in between. A generated map replaces the
recipes, one entry per page.

The principal's own files may stand in `renders/` and `published/`
beside the forge's files so that a copy he edits, a PDF he saves or a
diagram he exports has a place in the project and in git. The reason
why such a file has no companion, no row and no check is not
recorded. The rule that the forge's file is copied first follows from
the rule above it: the forge's render is never edited by hand.

## A worked example

The shape of a recipe, as the recipe skeleton defines it, filled for
a generic project `my-project` whose steering group wants an
executive summary as a Word document. Nothing here is taken from a
real project.

```markdown
---
project: my-project
purpose: executive summary
audience: the steering group
version: 0.3
---

# Recipe — executive summary

## Inputs
- 10-intent.md
- 20-assignment.md

## Instructions
- One page for readers who decide on budget and have not read the
  chain. Plain, direct, no internal vocabulary.
- Open with the problem and the direction, then what is handed over
  and to whom, then what is still open.
- Omit the rejected directions and the threads.
- Pin the title verbatim: "Executive summary: <project title>".

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template
  none, model <name>, the house colours on headings.

## Template
# Executive summary: <project title>

## The problem and the direction
<two short paragraphs from the intent's essence>

## What is handed over
<a few bullets from the assignment's deliverables, each with its
recipient>

## What is still open
<one bullet per open question of the assignment, with its owner>
```

After `/render executive-summary` the project holds
`renders/executive-summary.md`, opening with its provenance, and the
plain file `renders/executive-summary.docx` beside it. After the
principal's `/publish executive-summary` it also holds
`published/executive-summary.docx` and the companion
`published/executive-summary.md` that says what the designed file was
made from. Had the front-matter carried `languages: en, de`, the run
of `/render` would have left `renders/executive-summary.en.md` and
`renders/executive-summary.de.md` instead of one render, each with its
own provenance.

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

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
