---
generated: 2026-10-10
made: derived
inputs-hash: 9d3216ac34ba4336
inputs:
  - CLAUDE.md
  - templates/recipe.md
  - templates/recipe-readme.md
  - projects/forge/10-intent.md
---

# About renders and recipes

This page explains what a render is, what a recipe is, where the
line between the chain and a render runs, and why a render is
regenerated only on the principal's word. It is for anyone who uses
the forge, extends it or wants to understand how it treats its
outputs. It was put together from `CLAUDE.md` (Document chain,
Renders, and Documentation), the recipe skeleton
`templates/recipe.md`, the readme skeleton
`templates/recipe-readme.md` and the positions and rejected
directions of the forge intent `projects/forge/10-intent.md`.

## What a render is

A render is an audience-specific output generated from the chain:
a pitch for a group, an architecture picture, an executive summary,
the repository README. It is generated, never composed, and it is
never a source of truth. A render assigns nothing and is not part
of the chain: the artefacts of the chain remain the sole source of
truth, and a render only restates them for one audience.

A render is never edited by hand. When something in a render is
wrong, the fix goes into one of two places: the recipe it is made
from, or the inputs the recipe reads. Then the render is
regenerated. The same holds for the README of the engine and of
every project: a change of process is complete only once the intent
is updated and the README re-rendered.

A render may itself be an input of another render. A deck slide can
cite an architecture picture, for instance, provided the citing
recipe declares that render among its inputs, so that provenance
and staleness track the dependency.

## What a recipe is

The thing that is iterated is the recipe, one versioned file per
render under `recipes/<recipe>.md`. A recipe carries everything a
render is made from, in the sections the recipe skeleton gives:

- **Inputs**: the documents the render is generated from, by path.
  More than one input is legitimate, an intent and an assignment
  together for instance.
- **Instructions**: the audience, the tone, what to emphasise, what
  to omit, the register, everything the renderer must know beyond
  the template.
- **Format**: optional. Which file is made beside the Markdown and
  what each of the two steps below needs for it. A recipe without
  this section ends at the Markdown.
- **Template**: the literal skeleton of the render, with
  placeholders, always Markdown.

The front-matter of a recipe names the project, the purpose, the
audience, a version and an `updated` date; it may name an `output`
path that overrides the default `renders/<recipe>.md`.

Recipes are tools, not records of thinking. They carry a version and
an updated date, enough for a render to cite, and no status: a
recipe is never approved and stays at 0.x for life. Being versioned,
a recipe keeps its history in a companion file beside it, like every
versioned document of the forge; the companion records what changed
in the recipe at its own grain, while the substantive turns live in
the intent.

Recipes are deliberately loose. The template fixes the structure and
what information appears where, never the wording: a presentation
recipe says what belongs on a slide, not its phrasing. Each
rendering re-derives the words from the current inputs. Fixing the
whole text in the template would turn the recipe into the render and
make the inputs meaningless. There is one deliberate exception to
this looseness, pinned wording, explained below.

A recipe may be composed through a genre interview, `/recipe
<genre>`, which starts from a genre's own skeleton
(`templates/recipe-<genre>.md`). A genre skeleton extends the base
recipe shape and never replaces it. The first genre was
`presentation`, a slide-by-slide deck whose render is turned into a
PowerPoint file; the README and the release notes are genres too.

## The boundary between chain and render

The boundary between a chain artefact and a render is authorship,
not audience. A chain artefact is composed by the principal: Claude
proposes, the principal composes. A render is generated from
artefacts. So an article the principal writes is a layer of the
chain, and its translation is a render. That one test decides where
a new document belongs, whoever is meant to read it.

## Provenance and staleness

Every render opens with its provenance, citing the recipe and every
input with their versions; the ledger's Renders table mirrors that
provenance. Because the versions are named, staleness is visible: a
render whose recipe or input has moved on since it was made is
stale, and the `/forge` map shows it. The exact shape of the
provenance block and the precise definition of stale are the
reference page's (see below).

Staleness is never a finding of a check, the README and the release
notes included: the release regenerates those two anyway, so such a
finding would be void at every release and noise everywhere else.
Claude reports staleness and offers to regenerate; it never
regenerates on its own judgement.

## Why a render is regenerated only on the principal's word

Regeneration is stochastic. A render is made by a model, and the
same inputs never guarantee the same words, so an unreviewed
regeneration is an unreviewed edit of an outward-facing document.
Hence a render is regenerated only by `/release` or by the
principal's explicit `/render`. The README and the release notes are
regenerated by every release; every other render is as stale as the
principal lets it be.

Three light defences follow from this, none of them a gate:

- **Pinned wording.** A recipe may pin load-bearing wording as fixed
  text: a title, a claim, a fixed line. What is pinned regenerates
  verbatim; everything else re-derives freely.
- **The delta at a release.** A release that regenerated renders
  reports in its summary what materially changed in them, so the
  principal rules on the delta before the release commit without
  reading a full diff.
- **The scan for instance facts.** A subagent sees the session's
  whole context and may take it for the files on disk. So every
  agent that writes an outward-facing file is told in its definition
  that instance facts are not material and that its inputs are read
  from disk, and the generated files are scanned mechanically for
  instance facts before they are kept.

The alternative of regenerating stale renders at every save was
rejected: on a project the README's input, the ledger, moves at
every operation, so almost every save would render; and it would add
a staleness state that the save, the state map and the checks must
all read alike. With the renders at the release only, the README on
the main line is current at every release and stale in between
visibly, never silently.

## Everything is Markdown, made in two steps

Everything the forge produces is Markdown, renders included: a
presentation is a Markdown file saying what is on each slide, with
mermaid for pictures. The forge ends at content, but it carries its
delivery-format tools at its edge. An output is made in two steps,
each with its own command, divided by cost so that the expensive
conversion runs as seldom as possible:

1. `/render` generates the Markdown and, where the recipe names a
   format, the plain file beside it through pandoc
   (`renders/<recipe>.docx` or `.pptx`). Deterministic, cheap,
   repeated freely.
2. `/publish` makes the designed file through a model and its
   document skills, into `published/`. Expensive, and only on the
   principal's command: never by `/render`, never by `/release`,
   never on Claude's own judgement. It makes a file and sends it
   nowhere.

`/publish` takes the render as it lies on disk and never renders
first: a second render would publish a text the principal has not
read. A stale render is named before the conversion, and the word is
the principal's. The conversions are two scripts, `scripts/md2pptx.py`
and `scripts/md2docx.py`; what each needs installed and how a
template or a reference document is named is their own headers'. A
plain or a published file is tracked in git like any render output
and never edited by hand: the Markdown render stays the source of
truth. The ledger's Published table says what each published file
was made from and whether it is current or stale.

## The README and the release notes

Every project has a README as a render of its own
`recipes/readme.md`, with its output in the project root so that the
host shows it as the front page. A thought project also has release
notes from `recipes/release-notes.md`. The engine has both in the
same way, by the same mechanism, and every release of the project
regenerates both after its check. A library has a README only, a
catalogue of what it holds, since release notes are derived from the
history of an intent, which a library does not have. Both recipes
are scaffolded by `/new-project`.

What a README carries is the readme skeleton's, the one owner. The
README presents the project to a human meeting its repository for
the first time and stands alone: no claim requires opening the
chain. Its chapters are what the thing is, what one gets, how to
start, where it stands, and where the documentation is; the rest is
the ledger's and the documentation's. Every claim is derivable from
the inputs; nothing is invented, and anything superseded in the
inputs must not survive. The README is cut to what orients and
points, and it is English only; a translation is a render.

Release notes are a log of releases, not a story: one section per
release, newest first, with fixed groups in a fixed order and one
sentence per change from the user's side. The sections are derived
at the release from the records of the history log since the
previous release. One thing is never derived: what the reader must
do is written with the change in its history record and carried into
the notes word for word.

## A page of the documentation is not a render

The pages under `docs/` look like renders, generated and never edited
by hand, but no recipe stands behind them and `/render` is untouched.
A recipe per page was considered and dropped: eighty pages would mean
eighty recipes to iterate by hand, and a recipe is a tool the
principal shapes, while a page is to come from the project's
documents with no hand in between. A map with one generated entry
per page replaces the recipes, and a command of its own, `/document`,
makes the pages. A release never regenerates the documentation; it
reports the age of the index and offers `/document`. What the pages
have in common with renders is the review: they pass under the
principal's eyes as every regenerated render does.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a render.
- [Publish a designed file](../use/publish-a-designed-file.md): the designed file.
- [Render provenance](../reference/render-provenance.md): the provenance block and the definition of stale.
- [About the documentation](the-documentation.md): the pages, generated without a recipe.
