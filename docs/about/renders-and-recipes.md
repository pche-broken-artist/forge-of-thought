---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 64f4e10f34425c0e
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
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0240
---

# Renders and recipes

A render is an output made for one audience and generated from a
project's chain of documents; it is never a source of truth and never
edited by hand. This page explains what a render and its recipe are,
how an output is made in two steps, and why the thing that is
iterated is the recipe and not the output. It is written for the
user who makes renders, the extender who adds genres and the
evaluator who wants to understand the boundary between the chain and
what is generated from it.

## What it is

A render is an audience-specific output generated from the chain:
a pitch for a group, an architecture picture, an executive summary,
the repository README. The chain is the project's line of versioned
documents, the brief, the intent and the layers below it. A render
assigns nothing and is not part of the chain. The documents of the
chain stay the sole source of truth.

A recipe is what is iterated. It lives in `recipes/<recipe>.md` and
holds four things in one versioned file:

- the inputs: one document of the chain or several, by path;
- the audience;
- the instructions;
- the literal output template.

A recipe is composed in conversation with the principal (the person
whose thinking is forged). It is versioned by the house scheme and
carries `version` and `updated` in its front-matter, enough for a
render to cite. It carries no status field and stays 0.x for life.
Because a recipe is a tool and not a record of thinking, it is never
approved. Being versioned, it keeps its history in a companion beside
it, `recipes/<recipe>.history.md`. The companion records what changed
in the recipe at the recipe's own grain; the substantive turns of the
project live in the intent.

The boundary between the chain and a render is authorship, not
audience. A document of the chain is composed by the principal:
Claude proposes, the principal composes. A render is generated from
documents. An article the principal writes is a layer of the chain;
its translation is a render.

A page of the documentation is not a render. It comes from the
project's documents with no recipe in between; how that works is
[The documentation](the-documentation.md). Every term of the forge
is defined in one line in the [Glossary](../reference/glossary.md).

## How it works

### The shape of a recipe

The skeleton `templates/recipe.md` owns the shape. The front-matter
names the project, the purpose, the audience, the version, the date
of the last update and `last_change`, which is derived from the
records of the newest version in the companion. An optional `output`
key overrides where the render lands. The body has four sections:

- `## Inputs`: the documents the render is generated from, one path
  per line; more than one input is legitimate, such as the intent
  and the assignment together;
- `## Instructions`: the audience, the tone, what to emphasise, what
  to omit, the target length, the register, everything the renderer
  must know beyond the template;
- `## Format`: optional; what file is made beyond the Markdown and
  what each step needs; a recipe without this section ends at the
  Markdown;
- `## Template`: the literal skeleton of the render with
  placeholders, always Markdown.

A recipe may be composed through a genre interview, `/recipe
<genre>`, with the genre's skeleton `templates/recipe-<genre>.md`.
One definition per genre carries the elicitation checklist. The
genre's skeleton extends the base recipe shape and never replaces
it. The first genre is `presentation`: a slide-by-slide deck whose
render is turned into a PowerPoint file. How a recipe is composed is
[Compose a recipe](../use/compose-a-recipe.md).

### The template is loose

The template fixes the structure and what information appears where.
It does not fix the wording. A presentation recipe says what belongs
on a slide, not its phrasing or its placement on a picture. Each
rendering re-derives the words from the current inputs.

One exception holds. A recipe may pin load-bearing wording as fixed
text: a title, a claim, a fixed line. What is pinned regenerates
verbatim; everything else re-derives freely.

### Generating the render

`/render <recipe>` regenerates the output from the recipe
mechanically. The output is undated and overwritten freely. Where it
lands, how the generation is isolated and what the render opens with
are defined in the render command; the job is
[Render an output](../use/render-an-output.md).

Every render opens with its provenance: it cites the recipe and
every input with their versions. A render whose recipe or input has
moved past the cited version is stale. The provenance block and the
exact definition of stale are
[Render provenance](../reference/render-provenance.md). The
project's ledger (the one file that holds the project's state)
mirrors the provenance in its Renders table.

A render may itself be an input of another render. A deck slide may
cite an architecture picture as `render: <file>`. The citing recipe
must declare that render among its Inputs. So that provenance and
staleness track the dependency, the declaration is not optional.

### When a render is regenerated

A render is regenerated only by `/release` or by the principal's
explicit `/render`. Claude never regenerates on its own judgement; it
reports staleness and offers. The README and the release notes are
regenerated by every `/release`. Every other render is as stale as
the principal lets it be. No check reports the staleness of any
render, those two included; the state map shown by `/forge` shows
it.

A `/release` that regenerated renders reports in its summary what
materially changed in them. So the principal rules on the delta
before the release commit without reading a full diff.

### Two steps, two commands

Everything the forge produces is Markdown, renders included. A
presentation is a `.md` file saying what is on each slide, with
mermaid for pictures. An output in a delivery format is made in two
steps, each with its own command.

1. `/render` generates the Markdown. Where the recipe's `## Format`
   section names a format, it also makes the plain file beside the
   render through pandoc, `renders/<recipe>.docx` or
   `renders/<recipe>.pptx`. This step is deterministic, cheap and
   repeated freely.
2. `/publish` makes the designed file through a model and its
   document skills, into `published/`. This step is expensive. It
   runs only on the principal's command, never by `/render`, never
   by `/release` and never on Claude's own judgement. It makes a
   file and sends nothing anywhere. It takes the render as it lies
   on disk and never renders; a stale render is named before the
   conversion and the word is the principal's. The job is
   [Publish a designed file](../use/publish-a-designed-file.md).

The format and what each step needs stand in the recipe's
`## Format` section and are never copied into the render. The
conversions are two scripts, `scripts/md2pptx.py` and
`scripts/md2docx.py`; what each needs installed and where its output
lands is said in its own header. A plain or a published file is
tracked in git like any render output and is never edited by hand.
The Markdown render stays the source of truth; the generated file is
an output of second order, regenerated at will. The ledger's
Published table says what each published file was made from and
whether it is `current` or `stale`.

### The README and the release notes

Every project has a README as a render of its own
`recipes/readme.md`, with the output in the project root. A thought
project also has release notes from `recipes/release-notes.md`. This
is the same mechanism as the engine's own README and release notes.
Both recipes are genres of `/recipe`, scaffolded by `/new-project`
and expected by `/check`. Every `/release` of the project regenerates
both after its check. A library has a README only, a catalogue of
what it holds and how to use it, from its ledger and indexes.

The readme skeleton, `templates/recipe-readme.md`, is the one owner
of what a README carries:

- what the thing is;
- what one gets;
- how to start;
- where it stands;
- where the documentation is.

The rest belongs to the ledger and the documentation. The README
presents the project to a human meeting its repository for the first
time: a recipient, a colleague, the principal after weeks away. It
stands alone; no claim requires opening the chain. Every claim is
derivable from the inputs, nothing is invented, and anything
superseded in the inputs does not survive. The title is the
project's title from the brief or the intent followed by the current
intent version. The README closes with a short section "About this
README", saying that it is a render of `recipes/readme.md`,
regenerated at every release and never edited by hand, with fixes
going into the recipe or the inputs. After it stands one fixed
sentence, part of the readme genre, that names the engine the
project is run under; the engine's own README is the one exception.
A visible dated footer closes the file.

The release notes are a log of releases, not a story. They have one
section per release, newest first, the version being the intent's.
Inside a section stand fixed groups in a fixed order, one sentence
per change from the user's side with a pointer. At a major release
the minors since the previous major are folded into it. The sections
are derived at the release from the records of the history log since
the previous release. One thing is never derived: what the reader
must do is written with the change, in the `Action` field of its
record, and the render carries it into Action required word for
word. A thought project's release notes work the same way from the
histories of all its chain documents but the brief.

## Why

**The recipe is iterated, never the render.** Content fixes go into
the recipe or into the inputs, and the file is regenerated. The
reason is that the documents of the chain remain the sole source of
truth; a render that was edited by hand would hold words no input
supports. For the engine's own README the rule reads: a process
change is complete only once the intent is updated and the README
re-rendered.

**The template fixes structure, not wording.** Fixing the text in
the template would turn the recipe into the render and make the
inputs meaningless.

**Regenerated renders pass under the principal's eyes.**
Regeneration is stochastic. The same inputs never guarantee the same
words. So an unreviewed regeneration is an unreviewed edit of an
outward-facing document. Two light defences follow, neither of them a
gate: a recipe pins load-bearing wording as fixed text, and a release
reports what materially changed in the renders it regenerated. For
the same reason a render is regenerated only on the principal's word
or by a release, and Claude only reports staleness and offers.

**Two steps, divided by cost.** The expensive conversion through a
model should run as seldom as possible, so the cheap and
deterministic step is separated from it and repeated freely.
`/publish` never renders. Because a render is made by a model and is
never the same twice, a second one would publish a text the
principal has not read. The word is `publish` by the principal's
choice; it agrees with the rule that only the principal publishes.

**Everything is Markdown.** The forge ends at content. It carries its
delivery-format tools at its edge, one for a deck and one for a
document, and all other format conversion stays outside the forge,
as git is kept outside for persistence.

**Release notes are a log, not a story.** A reader wants to see
plainly what was added, changed and removed.

**Every README closes with a fixed sentence.** So that whoever finds
the project knows what runs it. The engine's README is the
destination the sentence points to, which is why it alone omits the
sentence.

**A library has a README only.** Release notes are derived from the
history of an intent, which a library does not have; its history is
git.

**The genre is named "presentation", not "deck".** The reason given
is legibility across a company at rollout.

**Rejected: rendering only what is stale at every save.** One command
regenerating only a render whose recipe or input moved in that save,
with a skipped mark in the ledger, was dropped. It would save perhaps
a third of the engine's saves and nothing on projects, whose README
input, the ledger, moves at every operation. It would also add a
staleness state that the save, the state map and the checks must all
read alike. The two-command shape of save and release saves
everything and adds nothing.

**Rejected: a recipe per page of the documentation.** Eighty pages
would mean eighty recipes to iterate by hand. A recipe is a tool the
principal shapes, while a page is to come from the project's
documents with no hand in between. The documentation map replaces
the recipes, with one generated entry per page.

## A worked example

A generic recipe for an executive summary of a thought project,
with the shape the skeleton defines. The slug is a placeholder.

```markdown
---
project: <slug>
purpose: executive summary
audience: the steering group of the project
version: 0.2
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/executive-summary.history.md>
---

# Recipe — executive summary

## Inputs
- 10-intent.md
- 20-assignment.md

## Instructions
- The reader decides on funding and has ten minutes. Lead with what
  is wanted and what it costs; leave out how the work is organised.
- One page. Plain register, no jargon of the forge.
- The title is pinned: "<Project title>: what we ask and why".
  Everything else is re-derived from the inputs at every render.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: template
  none, model <name>, house colours as in the template.

## Template
# <Project title>: what we ask and why

## What is wanted
<the objective of the intent in three sentences>

## What is asked of whom
<one line per deliverable of the assignment, with its recipient>

## What is deliberately out of scope
<the out-of-scope items of the assignment, one per line>

## Open questions
<the open questions of the assignment, each with its owner>
```

The render of this recipe lands in `renders/executive-summary.md`,
opens with a provenance block citing the recipe at 0.2 and the two
inputs at their versions, and gets `renders/executive-summary.docx`
beside it because the recipe names a format. When the intent moves
to a new version, the render is stale until the principal says
`/render executive-summary`; a release does not regenerate it, only
the README and the release notes. The designed file in `published/`
is made only when the principal says `/publish executive-summary`.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a render.
- [Publish a designed file](../use/publish-a-designed-file.md): the designed file.
- [Render provenance](../reference/render-provenance.md): the provenance block and the definition of stale.
- [The documentation](the-documentation.md): the pages, generated without a recipe.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
