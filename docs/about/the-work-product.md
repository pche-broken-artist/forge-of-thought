---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 04f2a2d12ed58eab
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own:
a model, an analysis, a worked task, in whatever form the work
needs. This page explains what a work product is, why it is kept as
two files, and why it is neither an artefact of the chain nor a
render. It is for anyone who uses the forge, extends it or weighs
it.

## What it is

A project may be asked for results that are neither its artefacts
nor its renders. An artefact is a document of the chain that holds
the principal's thinking (the principal is the person whose
thinking the project forges). A render is an output generated from
the chain for one audience. A work product is any result of
Claude's work that the principal asked for. It does the following:

- it takes its inputs from the chain and from the project's
  resources;
- it adds work of its own;
- it is iterated, like any document of the project;
- it is handed over as a result of the project;
- what it shows flows back into the intent, the trunk artefact that
  holds the principal's positions.

Work is a document kind of its own, called `work`, and it lives in
the project's folder `work/`. The kinds of document a project holds
are set out in [Documents and records](documents-and-records.md).
Every term used here is also in the [Glossary](../reference/glossary.md).

## How it works

### Two files

A work product is two files, side by side in `work/`:

- `work/<name>.<ext>`: the file. It holds the content and is named
  by the work alone.
- `work/<name>.spec.md`: the specification. It holds the way and
  the why.

The specification has the following sections, in this order:

- Task: what is asked, for whom, and what the file is to show.
- Inputs: the items it starts from, cited by ID, and the files,
  cited by path. They are cited as they stand and never copied.
- Method: how the work is done, such as the model, the steps and
  the structure of the file.
- Assumptions: each one an item with the prefix `ASM`.
- Open: each open matter an item with the prefix `TBC`, with an
  owner and what would close it.
- Making: how the file is made from the specification. It says by
  what means, in what format and in what language.

A work product has no ID prefix of its own. Nothing of the
`## Making` section is copied into the file. The skeleton of the
specification is `templates/work.md`, listed in
[Templates](../reference/templates.md).

### Languages

The specification is written in the project's language, as the
artefacts are. The file is written in whatever language the work
needs. The `## Making` section says which.

### Versions and approval

The specification is versioned by the house scheme. Drafts are 0.1,
0.2 and so on, and an integer version is approved. Its history is
kept in a companion file beside it, `work/<name>.spec.history.md`.
The specification can be approved. The file is made from the
specification again whenever the specification changes.

### Working with the file

The principal works with the file freely. That is what the file is
for. Three rules keep the two files true to each other:

- A conclusion that is to hold goes into the intent first, as a
  position.
- A change of the way or the why made in the file is carried into
  the specification in the same round and written with it. This
  covers the task, the inputs, the method and what the work
  assumes.
- A file touched by hand and not remade is recorded as such in the
  specification's history.

The states of the work and its wording belong to the file alone.

### The Work table

The ledger is the project's single report of state, built from the
documents each time it is read. Its Work table carries one row per
work product, made from the records of the specification's history.
The row holds:

- the file;
- the specification with its version;
- the inputs with their versions;
- when the file was made;
- the state of the file.

The state is one of three:

- `current`: the last record is the making of the file.
- `stale`: the specification was written and the file was not made
  again after it.
- `by hand`: the principal has worked the file and does not want it
  remade, recorded on his word.

### One command

One command, `/work`, works a work product: it works the
specification with the principal and makes the file from it in the
same round. How to run it is in
[Work a work product](../use/work-a-work-product.md).

A work product is composed as any artefact is. It is found together
with the principal by questions, or handed over to Claude with a few
sentences of what he wants. Claude proposes, with its assumptions
and choices listed, and the principal judges.

## Why

### Why it is not a render

A render is a view of the chain for an audience. It carries no
content of its own. It is never edited by hand. A work product
carries content of its own, and the principal works its file
freely. More on the render is in
[Renders and recipes](renders-and-recipes.md).

Stretching the render to cover work products was weighed and
dropped. The reason is that it would have cost the rule that a
render is never edited by hand.

### Why it is not a research note

A research note answers one question about the world outside the
project. It is immutable. A work product is iterated and worked by
hand.

### Why it is not an artefact of the chain

An artefact of the chain is the principal's thinking, written as
items with IDs. A file of any form, such as a spreadsheet or a
diagram, cannot carry that.

### Why the specification can be approved

A work product is handed over. A sign-off means something there.

### Why one command and not two

The making of the file is a step of the same round, and the
specification is iterated with the principal. A second command
would only separate what one conversation does. The price is one
command that does two things.

### Why two files

The inputs say what each file holds: the content in one, the way and
the why in the other. Why these are kept in two files rather than
one is not recorded beyond that.

## A worked example

A generic specification, in the shape of the template, for a
placeholder project `<slug>` and a work product named
`capacity-model`:

```markdown
---
version: 0.1
status: draft
project: <slug>
file: work/capacity-model.xlsx
---

# Capacity model — Work specification

## Task
Estimate the capacity the team needs next year, for the principal,
as a table per quarter.

## Inputs
- 10-intent.md: POS.NNNN
- sources/<file>

## Method
One sheet per quarter, demand against capacity, one summary sheet.

## Assumptions
- **ASM.0010** A working year has the same number of days in every
  quarter.

## Open
- **TBC.0010** (owner: <who>) The planned demand of the fourth
  quarter. Closed by: the demand plan.

## Making
A spreadsheet in the language of the team, made from the Method;
nothing of this specification is copied into it.
```

Beside it stand the file `work/capacity-model.xlsx` and the history
companion `work/capacity-model.spec.history.md`.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
