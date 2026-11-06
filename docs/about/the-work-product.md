---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 3b50535b4e4e4e9f
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own:
a model, an analysis, a worked task, in whatever form the work needs.
This page explains what a work product is, why it is two files, and
why it is neither an artefact of the chain nor a render. It is for the
user who asks for one, the extender who meets the kind in the rules,
and the evaluator who wants to know where its state is recorded.

## What it is

A work product is any result of Claude's work that the principal (the
person whose thinking is being forged) asked for. It takes its inputs
from the chain, the versioned documents of the project, and from the
resources, the sources and research notes the project holds. It adds
work of its own. It is iterated. It is handed over as a result of the
project. What it shows flows back into the intent.

It is a document kind of its own, `work`, in a group of its own, the
directory `work/`. In the table of document kinds ([Documents and
records](documents-and-records.md)) it stands in one row:

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |

A work product is two files:

- the file, `work/<name>.<ext>`: it holds the content and is named by
  the work alone, in whatever format the work needs;
- the specification, `work/<name>.spec.md`: it holds the way and the
  why.

The specification carries no prefix of its own. What it holds is:

- the task: what is asked, for whom, and what the file is to show;
- the inputs: items cited by ID and files cited by path, as they
  stand, never copied;
- the method: how the work is done, the model, the steps, the
  structure of the file;
- the assumptions, as ASM items;
- what is open, as TBC items, each with an owner and what would
  close it;
- the making: how the file is made from the specification, by what
  means, in what format and language, and what of the specification
  the file carries.

The skeleton of the specification is `templates/work.md` ([Templates](../reference/templates.md)).

## How it works

The specification is versioned by the house scheme, drafts as `0.x`
and signed-off versions as integers. Its history lives in a companion
beside it, `work/<name>.spec.history.md`, one record per change. The
specification can be approved, because a work product is handed over
and a sign-off means something there. The file is made from the
specification again whenever the specification changes.

The specification is written in the project's language, as the
artefacts are. The file is written in whatever language the work
needs, and the specification's `## Making` section says which.

The specification is composed as any artefact is: by elicitation, or
handed over with a few sentences of what the principal wants. Handed
over, Claude proposes the specification with its assumptions and its
choices listed, and the principal judges. One command, `/work <name>`,
works the specification with the principal and makes the file from it
in the same round on his word ([Work a work
product](../use/work-a-work-product.md)). The first specification is
created from `templates/work.md` as version 0.1, with its history
companion beside it. Nothing of the specification is copied into the
file.

The principal works with the file freely; that is what the file is
for. Three rules keep the two files and the intent in step:

- a conclusion that is to hold goes intent-first into a position of
  the intent, and from there down the chain;
- a change of the way or the why made in the file (its task, its
  inputs, its method, what it assumes) is carried into the
  specification in the same round and written with it; the state of
  the work and its wording stay the file's alone;
- a file touched by hand and not remade is said so by a record in
  the specification's history.

The ledger (the project's state report, built by a script at read
time and never kept in git) carries a Work table with one row per
work product. The row is made from the records of the specification's
history, never written by hand. It shows the file, the specification
with its version, the inputs with their versions, when the file was
made, and the state of the file:

- `current`: the last record is the making of the file;
- `stale`: the specification was written and no making followed;
- `by hand`: a record says the principal has worked the file and does
  not want it remade, on his word.

The check `light` verifies the Work table against the directory, as it
does the other tables of the ledger.

## Why

The work product is a kind of its own because its neighbours stay what
they are, and none of them can carry it:

- a render is a view of the chain for an audience; it carries no
  content of its own and is never edited by hand ([Renders and
  recipes](renders-and-recipes.md));
- a research note answers one question about the world outside, and
  it is immutable;
- an artefact of the chain is the principal's thinking in items with
  IDs, which a file of any form cannot carry.

Stretching the render to cover the work product was weighed and
dropped. It would have cost the rule that a render is never edited by
hand.

The specification is approvable because a work product is handed over,
and a sign-off means something there.

The work product has one command for the specification and the file,
rather than two as a recipe and a render have. The making is a step of
the round, and the specification is iterated with the principal, so a
second command would only separate what one conversation does. The
price is a skill that does two things.

The Work table is made from the records of the specification's history
because nobody writes a row of the ledger: what only the ledger would
know lives in records, and the ledger is remade from them.

## A worked example

A principal of a project with the placeholder slug `<slug>` asks for a
capacity model: how many units of a thing are needed per period, over
the horizon the intent sets. The work product is two files in `work/`:

- `work/capacity-model.xlsx`, the file: the model itself, in the form
  the work needs, a spreadsheet;
- `work/capacity-model.spec.md`, the specification: the way and the
  why, with `work/capacity-model.spec.history.md` beside it.

The specification, in the shape `templates/work.md` gives, at its
first version:

```
---
version: 0.1
status: draft
project: <slug>
file: work/capacity-model.xlsx
---

# Capacity model — Work specification

## Task
A model of how many units are needed per period over the horizon
the intent sets, for the principal, to show where the need
exceeds what is available.

## Inputs
- 10-intent.md: POS.NNNN
- sources/<demand-figures>.md

## Method
One sheet per period; the need per period computed from the demand
figures of the source by the rule the position states; a summary
sheet with the periods where the need exceeds what is available.

## Assumptions
- **ASM.0010** The demand figures of the source hold for the whole
  horizon.

## Open
- **TBC.0010** (owner: the principal) What is available per period.
  Closed by: a figure per period in the intent.

## Making
A spreadsheet made by Claude from this specification, one sheet per
period and a summary, in the project's language; the task and the
method are not copied into it.
```

The ASM and TBC numbers are the project's next free ones, after every
specification the project already has. When the principal says
`write`, the file is made from the specification in the same round,
a record of the making is appended to the history companion, and the
ledger's Work table shows the row with the state `current`. If the
principal later changes the specification and no making follows, the
row says `stale`. If he works the spreadsheet by hand and does not
want it remade, he says so, a record is appended, and the row says
`by hand`.

## See also

- [Work a work product](../use/work-a-work-product.md): working one with `/work`.
- [Renders and recipes](renders-and-recipes.md): the render, which a work product is not.
- [Documents and records](documents-and-records.md): the kinds of document a project holds.
- [Templates](../reference/templates.md): the specification's skeleton.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
