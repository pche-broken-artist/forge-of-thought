---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: c724a9ff6f23c060
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own,
such as a model, an analysis or a worked task. This page explains
what a work product is, why it is kept as two files, and why it is
neither an artefact of the chain nor a render. It is for anyone who
uses a project, extends the forge or weighs whether the forge fits
their work.

## What it is

A project may make outputs that are neither artefacts nor renders.
Such an output is a result of Claude's work that the principal asked
for. The principal is the person whose thinking is being forged, and
the final authority on all content. The output takes whatever form
the work needs.

A work product has a life of its own in the project:

- It takes its inputs from the chain and the resources (the
  project's sources and research notes).
- It adds work of its own to them.
- It is iterated, like an artefact.
- It is handed over as a result of the project.
- What it shows flows back into the intent.

It is a kind of document of its own, called **work**, in a group of
its own. Its files live in the directory `work/`. In the table of
document kinds it reads as follows.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |

The other kinds a project holds are described in
[Documents and records](documents-and-records.md). Every term used
here has its one line in the [Glossary](../reference/glossary.md).

## How it works

### Two files

A work product is two files side by side in `work/`:

- `work/<name>.<ext>`: the file. It holds the content and is named by
  the work alone.
- `work/<name>.spec.md`: the specification. It holds the way and the
  why.

The specification says these things, each in a section of its own:

- **Task**: what is asked, for whom, and what the file is to show.
- **Inputs**: the items and files the work starts from. Items are
  cited by their ID and files by their path. They are cited as they
  stand and never copied.
- **Method**: how the work is done, such as the model, the steps and
  the structure of the file.
- **Assumptions**: each one an item with the prefix `ASM`.
- **Open**: what is still open, each one an item with the prefix
  `TBC`, with an owner and with what would close it.
- **Making**: how the file is made from the specification, by what
  means, in what format and language, and what of the specification
  the file carries.

Nothing of the Making section is copied into the file. The
specification has no ID prefix of its own. Its skeleton is the
template `templates/work.md`, listed in
[Templates](../reference/templates.md).

### Languages

The specification is written in the project's language, as the
artefacts are. The file is written in whatever language the work
needs. The Making section of the specification says which.

### Versions and approval

The specification is versioned by the house scheme of the forge, and
a new one starts as version `0.1`. It keeps its history in a
companion file beside it, `work/<name>.spec.history.md`. The
specification can be approved. The file is made from the
specification again whenever the specification changes.

### Working the file by hand

The principal works with the file freely. That is what the file is
for. Three rules keep the file and the specification in step:

- A conclusion that is to hold goes into a position of the intent
  first, and from there down the chain.
- A change of the way or the why made in the file (its task, its
  inputs, its method or what it assumes) is carried into the
  specification in the same round and written with it.
- A file touched by hand and not made again is said so by a record
  in the specification's history.

The states of the work and its wording belong to the file alone.

### The state in the ledger

The ledger is the single source of truth for a project's state. It
is made by a script at read time from the project's documents. Its
Work table is made from the records of each specification's history.
It carries one row per work product:

- the file;
- the specification with its version;
- the inputs with their versions;
- when the file was made;
- its state.

The state is one of three:

- `current`: the latest record is the making of the file.
- `stale`: the specification was written and the file was not made
  after it.
- `by hand`: the principal has worked the file and does not want it
  made again. A record says so, on his word.

### The command

One command, `/work <name> [slug]`, works the specification with the
principal and makes the file from it in the same round on his word.
How to run it is on
[Work a work product](../use/work-a-work-product.md).

A work product is composed as any artefact is. It may be found
together with the principal by questions, or handed over to Claude
with a few sentences of what he wants. Either way Claude proposes,
with its assumptions and choices listed, and the principal judges.

## Why

### Why two files

The file is the content, and the principal works with it freely in
whatever form the work needs. The specification holds the way and the
why, and the file is made from it. Why the way and the why are kept
in a file of their own, apart from the content, is not recorded
beyond that division.

The specification is versioned and can be approved. The reason is
that a work product is handed over, and a sign-off means something
there.

### Why it is not a render

A render is a view of the chain for an audience. It carries no
content of its own. It is never edited by hand. A work product
carries content of its own, and the principal edits its file freely.
The render and its recipe are described in
[Renders and recipes](renders-and-recipes.md).

Stretching the render to cover work products was weighed and
dropped. It would have cost the rule that a render is never edited
by hand.

### Why it is not a research note

A research note answers one question about the world outside the
project. It is immutable once written. A work product is iterated and
remade.

### Why it is not an artefact of the chain

An artefact of the chain is the principal's thinking, written as
items with IDs. A file of any form, such as a model or a table of
figures, cannot carry that.

### Why one command and not two

A render has two commands: `/recipe` to compose its recipe and
`/render` to make the render. A work product has one. The making is a
step of the same round in which the specification is iterated with
the principal. A second command would only separate what one
conversation does. The price is a command that does two things.

## A worked example

A generic specification, as the template shapes it. The placeholders
stand where a real project puts its own names and IDs.

```markdown
---
version: 0.2
status: draft
project: <slug>
file: work/cost-model.xlsx
---

# Cost model — Work specification

## Task
A cost model of the proposed rollout for the steering group,
showing the cost per year under the two options of the intent.

## Inputs
- 10-intent.md: POS.NNNN
- sources/<file>

## Method
One sheet per option, one row per cost item, a summary sheet that
compares the totals per year.

## Assumptions
- **ASM.0010** Prices are those of the current year, without
  inflation.

## Open
- **TBC.0010** (owner: <who>) The licence price for the second
  option. Closed by: the vendor's offer registered as a source.

## Making
A spreadsheet made by Claude from this specification, in the
language of the steering group; the file carries the sheets and the
figures, nothing of this section.
```

Beside it stand `work/cost-model.xlsx` (the file) and
`work/cost-model.spec.history.md` (the history companion). When the
principal changes figures in the spreadsheet by hand and wants to
keep them, a record in the history says so, and the ledger's Work
table shows the file as `by hand`.

## See also

- [Work a work product](../use/work-a-work-product.md): working one
  with `/work`.
- [Renders and recipes](renders-and-recipes.md): the render, which a
  work product is not.
- [Documents and records](documents-and-records.md): the kinds of
  document a project holds.
- [Templates](../reference/templates.md): the specification's
  skeleton.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
