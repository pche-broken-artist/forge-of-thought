---
generated: 2026-10-09
made: derived
inputs-hash: 22fede0190f9c9e9
inputs:
  - CLAUDE.md
  - templates/recipe.md
  - projects/forge/10-intent.md
---

# About renders and recipes

This page explains what a render is, what a recipe is, where the
line between the chain and its outputs runs, and why the forge
treats a regenerated output with care. It is for the user who wants
an output of a project, the extender who adds to the rendering
machinery and the evaluator who wants to understand how the forge
keeps its outputs honest. It was put together from `CLAUDE.md`
(Document chain, Renders), the recipe skeleton `templates/recipe.md`
and the positions and rejected directions of the forge intent in
`projects/forge/10-intent.md`.

## What a render is

A render is an audience-specific output generated from the chain: a
pitch for a group, an architecture picture, an executive summary,
the README of the repository. It is made from the artefacts, it
assigns nothing and it is not part of the chain. The artefacts stay
the sole source of truth; a render is never one.

A render is never edited by hand. A fix to its content goes into the
recipe or into the inputs, and the output is regenerated from them.
The render file in `renders/<recipe>.md` is overwritten freely and
carries no date of its own; what it carries is its provenance (below).

## What a recipe is

The thing that is iterated is the recipe, one versioned file at
`recipes/<recipe>.md`. It holds in one place everything the renderer
needs:

- **Inputs**: the artefacts the render is generated from, by path,
  one per line. More than one input is legitimate, an intent and an
  assignment together, for example.
- **Instructions**: audience, tone, what to emphasise, what to omit,
  target length and register; everything the renderer must know
  beyond the template.
- **Format**: optional. Which file is made beyond the Markdown and
  what each of the two steps needs for it (below). A recipe without
  this section ends at the Markdown.
- **Template**: the literal skeleton of the output, with
  placeholders, always Markdown.

The front-matter of a recipe carries the project, the purpose, the
audience, a version and an `updated` date, and may name an `output:`
path that overrides the default place of the render. Recipes are
tools, not records of thinking: a recipe is never approved, carries
no status and stays at 0.x for life. Being versioned, it keeps its
history in a companion beside it like every versioned document; the
companion records what changed in the recipe, while the substantive
turns of the thinking live in the intent.

Recipes are deliberately loose. The template fixes the structure and
says what information appears where, never the wording: a
presentation recipe says what belongs on a slide, not its phrasing.
Each rendering re-derives the words from the current inputs. If the
text were fixed in the template, the recipe would become the render
and the inputs would mean nothing.

A recipe may be composed through a genre interview: `/recipe <genre>`
walks a checklist for one genre, and the genre's skeleton extends
the base recipe shape without replacing it. The first genre is the
presentation, a slide-by-slide deck whose render is turned into a
PowerPoint file. Composing a recipe is the subject of
[Compose a recipe](../use/compose-a-recipe.md).

## The boundary: authorship, not audience

What separates a layer of the chain from a render is who makes it.
A chain artefact is composed by the principal, with Claude
proposing and the principal composing. A render is generated from
artefacts. An article the principal writes is a layer of the chain;
its translation is a render. Audience does not decide it: a document
for outsiders can be a layer, and a document for the principal
himself can be a render.

## Provenance and staleness

Every render opens with its provenance: the recipe and every input
it was made from, each with its version. The ledger's Renders table
mirrors that provenance. Because the versions are cited, it can be
seen when a render has fallen behind: a render whose recipe or
inputs have moved on since the versions it cites is stale. The exact
shape of the block and the definition of stale are in
[Render provenance](../reference/render-provenance.md).

A render may itself be an input of another render, a deck slide
citing an architecture picture, for instance, provided the citing
recipe declares it among its Inputs. The declaration is what lets
provenance and staleness follow the dependency.

## Why regeneration is guarded

Regeneration is stochastic: the same inputs never guarantee the same
words. An unreviewed regeneration is therefore an unreviewed edit of
an outward-facing document. For that reason a render is regenerated
only on the principal's explicit `/render` or by a release; Claude
never regenerates on his own judgement, he reports staleness and
offers. Every other render is as stale as the principal lets it be,
and no check reports the staleness of a render; the state map of
`/forge` shows it.

Two light defences stand against drift, neither of them a gate. A
recipe pins load-bearing wording as fixed text, a title, a claim, a
fixed line, which then regenerates verbatim while everything else
re-derives freely. And a release that regenerated renders reports in
its summary what materially changed in them, so the principal rules
on the delta before the release commit without reading a full diff.

Rendering only what is stale at every save was considered and
rejected: it would have saved little on the engine and nothing on
projects, whose README input moves at every operation, and it would
have added a staleness state that several commands must all read
alike. Two commands, a save that renders nothing and a release that
renders the README and the release notes, were kept instead.

## Everything is Markdown, made in two steps

Everything the forge produces is Markdown, renders included: a
presentation is a `.md` saying what is on each slide, with mermaid
for pictures. The forge ends at content, but it carries its
delivery-format tools at its edge, and an output is made in two
steps, each with its own command, divided by cost so that the
expensive conversion runs as seldom as possible.

- `/render` generates the Markdown and, where the recipe names a
  format, the plain file beside it through pandoc
  (`renders/<recipe>.docx` or `.pptx`): deterministic, cheap,
  repeated freely. See [Render an output](../use/render-an-output.md).
- `/publish` makes the designed file through a model and its
  document skills, into `published/`: expensive, only on the
  principal's command, never by `/render`, by a release or on
  Claude's own judgement. It takes the render as it lies on disk and
  never renders first, because a second render would be a text the
  principal has not read; a stale render is named before the
  conversion and the word is his. It makes a file and sends nothing
  anywhere. See
  [Publish a designed file](../use/publish-a-designed-file.md).

What each step needs, the format, a reference document or a template
and the model, stands in the recipe's Format section; the render
carries content only and the instructions for the model stay in the
recipe. The conversions are the scripts `scripts/md2pptx.py` and
`scripts/md2docx.py`. A plain or a published file is tracked in git
like any render output and is never edited by hand: the Markdown
render stays the source of truth, and the generated file is an output
of second order. The ledger's Published table says what each
published file was made from and whether it is current or stale.

## The README and the release notes

Every project has a README as a render of its own `recipes/readme.md`,
with the output in the project root, and a thought project has
release notes from `recipes/release-notes.md` as well; the engine's
own README and release notes are made the same way. Every release of
the project regenerates both after its check, and the regenerated
outputs pass under the principal's eyes like any other. A library has
a README only, a catalogue of what it holds, because release notes
are derived from the history of an intent, which a library does not
have. Both recipes are genres of `/recipe` and are scaffolded when a
project is created.

The README is never edited by hand: a content fix goes into the
recipe or the inputs and the file is regenerated, and a process
change of the engine is complete only once its intent is updated and
the README re-rendered. The release notes are a log of releases, not
a story: one section per release, newest first, derived from the
history records since the previous release, with what the reader
must do carried over word for word from the records.

## What is not a render

A page of the documentation is not a render: no recipe stands behind
it and `/render` is untouched. A recipe per page was considered and
dropped, because eighty pages would mean eighty recipes to iterate by
hand, and a recipe is a tool the principal shapes, while a page is to
come from the project's documents with no hand in between. A
generated map replaces the recipes, one entry per page. How the pages
are made is the subject of
[About the documentation](the-documentation.md).

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a
  render.
- [Publish a designed file](../use/publish-a-designed-file.md): the
  designed file.
- [Render provenance](../reference/render-provenance.md): the
  provenance block and the definition of stale.
- [About the documentation](the-documentation.md): the pages,
  generated without a recipe.
