---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 8fc3eb1fe9eee8b8
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
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0240
---

# Renders and recipes

A render is an output of a project made for one audience and
generated from the documents of the chain: a pitch, an architecture
picture, an executive summary, the README of the repository. This
page explains what a render is, what the recipe it is made from is,
how the two relate to the chain and why an output is generated from a
recipe and never edited by hand. It is for anyone who uses the forge,
extends it or judges it; the terms of the forge are gathered in the
[Glossary](../reference/glossary.md).

## What it is

A render is never a source of truth. The artefacts of the chain, the
intent and the layers below it, stay the only source of truth. A
render assigns nothing and is not part of the chain.

What is iterated is the render's **recipe**, one versioned file
`recipes/<recipe>.md`. The recipe holds the inputs (one artefact or
several), the audience, the instructions and the literal template of
the output. `/render <recipe>` regenerates the output from it. The
render itself is never edited by hand. A fix to a render goes into
the recipe or into the inputs, and the render is regenerated. How a
recipe is composed is the matter of [Compose a
recipe](../use/compose-a-recipe.md); how an output is generated is
the matter of [Render an output](../use/render-an-output.md).

The boundary between the chain and a render is authorship, not
audience. A chain artefact is composed by the principal, the person
whose thinking is being forged, with Claude proposing. A render is
generated from artefacts. An article the principal writes is a layer
of the chain; its translation is a render.

A recipe is a tool, not a record of thinking. It carries a version in
its front-matter and no status. It stays at 0.x unless the principal
names an integer. When he names one, 1.0 or 2.0, the recipe takes it
and the count goes on from there, 2.1, 2.2. Claude never proposes
that integer. The integer is the principal's own mark and not an
approval, and nothing guards or reads it. The date of a recipe is
computed from its history; a render cites the version. Being
versioned, a recipe keeps its history in a companion beside it, as
every versioned kind does. The companion records what changed in the
recipe at its own grain; the substantive turns of the thinking live
in the intent.

Everything a render is made of is Markdown, content only. A
presentation is a Markdown file saying what is on each slide, with
mermaid for pictures.

## How it works

### Provenance and staleness

Every render opens with its provenance: the recipe and every input,
each with its version. A render is stale when a version it cites
differs from the version the file has today. The provenance block
and the definition of stale are the matter of [Render
provenance](../reference/render-provenance.md). The ledger, the
project's state report made at read time, mirrors the provenance in
its Renders table.

A render is regenerated only by `/release` or by the principal's
explicit `/render`. Claude never regenerates a render on its own
judgement: it reports staleness and offers. No check reports the
staleness of a render; the state map of the project shows it.

A render may be an input of another render, such as a deck slide
citing an architecture picture. The citing recipe must declare the
other render among its Inputs, so that provenance and staleness
track the dependency.

### Several languages

A recipe may declare several languages in `languages:`, the first
primary and the rest its translations. `/render` generates the
primary render and, in the same run, translates it into every other
language scene for scene and line for line. There is one render per
language, `renders/<recipe>.<lang>.md`, each with its own provenance
and its own row in the ledger's Renders table; the translation cites
the primary render it was made from. A recipe with one language keeps
`renders/<recipe>.md`. A render may therefore be in any language, or
languages, its recipe declares.

### Two steps, divided by cost

An output is made in two steps, each with its own command.

- `/render` generates the Markdown and, where the recipe names a
  format, the plain file beside it: a `.pptx` from a deck render or a
  `.docx` from a document render, made through pandoc. This step is
  deterministic, cheap and repeated freely.
- `/publish` makes the designed file through a model and its document
  skills, into `published/`. This step runs only on the principal's
  command, never by `/render`, by `/release` or on Claude's own
  judgement. It makes a file and sends nothing anywhere. Beside the
  designed file stands a companion that carries its provenance; the
  ledger's Published table says what each published file was made
  from and whether it is `current` or `stale`. The designed file is
  the matter of [Publish a designed
  file](../use/publish-a-designed-file.md).

`/publish` takes the render as it lies on disk and never renders. A
stale render is named before the conversion, and the word is the
principal's. A recipe that names no format ends at the Markdown. The
format and what each step needs stand in the recipe's `## Format`
section and are never copied into the render.

A screenplay is the exception among the formats. Its render is
turned into a video or into the events its player plays by a script
alone, and it has no designed file. Its recipe's `output:` may send
the public file into the engine's `docs/videos/`, the one public
folder. The screenplay, its two formats and where a public one lands
are the matter of [The screenplay and its
player](the-screenplay-and-its-player.md).

A plain file and a published file are tracked in git like any render
output and are never edited by hand. The Markdown render stays the
source of truth. All other format conversion stays outside the forge.

### The principal's own files

The forge owns in `renders/` and `published/` only the files its
recipes name: the render and its translations, the plain file, the
designed file and its companion. Any other file there is the
principal's own, made by hand from the forge's files:

- a copy under a new name that he edits;
- a PDF saved from Word or PowerPoint;
- an HTML of a diagram.

Such a file is kept in git beside the forge's files. It has no
companion, no row in the ledger and no check. The forge never reads,
overwrites or raises it. The forge's own file stays untouched by
hand: what is to change is copied first.

### The README and the release notes

Every project has a README as a render of its own `recipes/readme.md`,
with its output in the project root. A thought project also has
release notes, a render of `recipes/release-notes.md`. The two recipes
are genres of `/recipe`, scaffolded by `/new-project`, and every
`/release` of the project regenerates both after its check. The
engine's own README and release notes are made by the same mechanism.

A README presents the project to a human meeting its repository for
the first time: a recipient, a colleague, the principal after weeks
away. It stands alone, so that no claim requires opening the chain.
It carries what the thing is, what one gets, how to start, where it
stands and where the documentation is; the rest belongs to the ledger
and to the documentation. Every claim in it is derivable from the
inputs. Every README closes with a short section on itself and one
fixed sentence that says what engine the project runs under; the
engine's own README is the one exception, since it is the destination
that sentence points to. A library has a README only, a catalogue of
what it holds and how to use it.

Release notes are a log of releases, not a story. There is one
section per release, newest first, with fixed groups in a fixed order
and one sentence per change from the reader's side with a pointer. At
a major release the minors since the previous major are folded into
it. The sections are derived at the release from the records of the
history log since the previous release. One thing is never derived:
what the reader must do is written with the change, in the `Action`
field of its record, and the render carries it into *Action required*
word for word. A thought project's release notes are made the same
way from the histories of all its chain artefacts but the brief.

### Composition by genre

A recipe may be composed through a genre interview, `/recipe
<genre>`, with the genre's skeleton `templates/recipe-<genre>.md`
extending the base recipe shape, never replacing it. The genres today
are `presentation`, `readme`, `release-notes`, `screenplay` and
`user-stories-export`.

### Where a render lands

By default a render lands at `renders/<recipe>.md`. A recipe's
`output:` overrides this with a path read relative to the project
root; a leading slash means the engine root. This is how the forge's
own project sends the engine's README, release notes and CONTRIBUTING
into the engine root, which is why a release of the engine lands in
two commits. The forge's own project is the matter of [Projects and
the engine](projects-and-the-engine.md).

### What is not a render

A page of the documentation is not a render. A recipe per page was
considered and dropped. Pages are generated from a map, one generated
entry per page, with no hand in between; the pages are the matter of
[The documentation](the-documentation.md). The security policy and
the code of conduct are no render either; they are the matter of [The
security policy and the code of
conduct](the-security-policy-and-the-code-of-conduct.md).

## Why

A render is never edited by hand because it is a second-order output.
The artefacts hold what the principal thinks; the recipe holds how
that is to be shown to one audience; the render is what falls out of
the two. An edit to the render would be lost at the next regeneration
and would make the render disagree with its inputs. So a fix goes
into the recipe or into the inputs, and the render is regenerated.

A recipe fixes the structure and what information appears where,
never the wording. Each rendering re-derives the words from the
current inputs. Fixing the text in the template would turn the recipe
into the render and make the inputs meaningless.

Regeneration is stochastic: the same inputs never guarantee the same
words. An unreviewed regeneration is therefore an unreviewed edit of
an outward-facing document. This is why a render is regenerated only
by a release or on the principal's word, and why regenerated renders
pass under his eyes. Two light defences follow from it, neither of
them a gate. A recipe may pin load-bearing wording as fixed text,
which regenerates verbatim while everything else re-derives freely.
A `/release` that regenerated renders reports in its summary what
materially changed in them, so that the principal rules on the delta
before the release commit without reading a full diff.

A recipe carries no status because approval has a meaning only where
someone receives the document, and a recipe is received by nobody. It
is iterated continuously. The integer the principal may name means
nothing beyond his own mark.

The translations of a recipe are made in the same run as the primary
render because the quotes of a transcript, the beats and the captions
are chosen once. A second generation would choose them again
differently, and the translation would no longer be the same cut.

The two steps of an output are divided by cost so that the expensive
conversion runs as seldom as possible. `/publish` never renders
because a render is made by a model and is never the same twice; a
second one would publish a text the principal has not read. The word
is `publish` by the principal's choice, and it agrees with the rule
that only the principal publishes.

The principal's own files are left alone by the forge so that he can
work with the forge's outputs freely, while the forge's own file stays
what its recipe made. The reason the forge recorded for allowing them
beside its own files, beyond this, is not recorded in the inputs of
this page.

Every project has a README because a visitor meeting the repository
should understand it without opening the chain, and the README is
regenerated at every release so that it never drifts from the chain.
A library has a README only because release notes are derived from
the history of an intent, which a library does not have; its history
is git. Release notes are a log, not a story, because a reader wants
to see plainly what was added, changed and removed.

Regenerating only the stale renders at every save was considered and
rejected. It would have saved perhaps a third of the engine's saves
and nothing on projects, whose README input, the ledger, moves at
every operation; and it would have added a staleness state that the
save, the state map and the checks must all read alike. The
two-command shape of save and release saves everything and adds
nothing.

A recipe per page of the documentation was dropped because eighty
pages would mean eighty recipes to iterate by hand. A recipe is a
tool the principal shapes, while a page is to come from the project's
documents with no hand in between; the documentation map replaces the
recipes, one generated entry per page.

## A worked example

The shape of a recipe, with placeholders, for a project with the
placeholder slug `example-project`. The front-matter carries the
project, the purpose, the audience and the version; `output:` and
`languages:` are optional. The sections are Inputs, Instructions,
Format and Template; a recipe without a Format section ends at the
Markdown.

```markdown
---
project: example-project
purpose: executive summary
audience: the steering group
version: 0.3
# output: <path>
# languages: <en, cs>
---

# Recipe — executive summary

## Inputs
- 10-intent.md
- 20-assignment.md

## Instructions
<!-- Audience, tone, what to emphasise, what to omit, target
length, register. Everything the renderer must know beyond the
template. -->

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference
  <path | none>, page size <A4 | Letter>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must
  know>.

## Template
<!-- The literal skeleton of the render, with placeholders. Always
Markdown. -->
```

`/render executive-summary` writes `renders/executive-summary.md`,
opening with the provenance that cites this recipe at 0.3 and the two
inputs at their versions, and beside it the plain file
`renders/executive-summary.docx`. When the intent moves to a new
version, the render is stale; Claude reports it and offers, and the
render is regenerated on the principal's word or at the next
release. `/publish executive-summary` makes the designed file
`published/executive-summary.docx`, with its companion beside it,
only when the principal asks for it.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing a recipe.
- [Render an output](../use/render-an-output.md): generating a render.
- [Publish a designed file](../use/publish-a-designed-file.md): the designed file.
- [The screenplay and its player](the-screenplay-and-its-player.md): the screenplay, its two formats and where a public one lands.
- [The work product](the-work-product.md): the output that is not a render.
- [Projects and the engine](projects-and-the-engine.md): the forge's own project, whose root renders land in the engine.
- [Render provenance](../reference/render-provenance.md): the provenance block and the definition of stale.
- [The documentation](the-documentation.md): the pages, generated without a recipe.
- [The security policy and the code of conduct](the-security-policy-and-the-code-of-conduct.md): the two fixed files of the root, which are no render either.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
