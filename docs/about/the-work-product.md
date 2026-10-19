---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 35b8fad7480ece93
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own,
such as a model, an analysis or a worked task, in whatever form the
work needs. This page explains what it is, why it is two files, and
why it is neither an artefact of the chain nor a render. It is for
anyone who uses the forge, extends it or weighs it.

## What it is

A project may make outputs that are neither artefacts nor renders.
Such an output is any result of Claude's work that the principal
(the person whose thinking is forged) asked for. It takes its inputs
from the chain and from the resources of the project. It adds work of
its own. It is iterated, it is handed over as a result of the
project, and what it shows flows back into the intent.

The work product is a document kind of its own, **work**, in a group
of its own. Its row among the kinds of document reads:

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |

A work product lives in the project's `work/` directory as two
files:

- `work/<name>.<ext>`: the file. It holds the content and is named
  by the work alone.
- `work/<name>.spec.md`: the specification beside it. It holds the
  way and the why.

The specification says these things:

- the task: what is asked, for whom, and what the file is to show;
- the inputs: the items and files the work starts from, cited by ID
  and path and never copied;
- the method: how the work is done, the model, the steps and the
  structure of the file;
- the assumptions, as `ASM` items;
- what is open, as `TBC` items, each with an owner and what would
  close it;
- the making: how the file is made from the specification, by what
  means, in what format and language.

A work product has no ID prefix of its own.

## How it works

The specification is versioned by the house scheme of version
numbers. It keeps its history in a companion beside it,
`work/<name>.spec.history.md`, as every versioned document does. It
can be approved: its `status` is `draft`, `approved` or
`superseded`. The file is made again from the specification whenever
the specification changes. Nothing of the `## Making` section is
copied into the file.

The two files differ in language. The specification is written in
the project's language, as the artefacts are. The file is in
whatever language the work needs. The `## Making` section of the
specification says which.

The principal works with the file freely. That is what the file is
for. Three things follow from it:

- A conclusion that is to hold goes into the intent first, as a
  position, and from there down the chain.
- A change to the way or the why made in the file (its task, its
  inputs, its method or what it assumes) is carried into the
  specification in the same round and written with it. The states
  of the work and its wording belong to the file alone.
- A file worked by hand and not remade is recorded as such in the
  history of the specification.

A work product is composed as any artefact is. It is found together
with the principal by questions, or handed over to Claude with a few
sentences of what he wants. Claude proposes, with its assumptions
and choices listed, and the principal judges.

One command, `/work`, is the way to a work product: bare, it lists
the project's work products, and with a name it works the
specification and makes the file from it in the same round, on the
principal's word.

The state of every work product is shown in the Work table of the
ledger (the file that holds the state of a project, made by a script
when it is read). The table is made from the records in the
specification's history. It carries one row per work product:

- the file;
- the specification, with its version;
- the inputs, with their versions;
- when the file was made;
- its state.

The state is one of three:

- `current`: the latest record is the making of the file.
- `stale`: the specification was written and the file was not made
  again after it.
- `by hand`: the principal has worked the file and does not want it
  remade. A record in the specification's history says so, on his
  word.

The check `light` verifies the Work table against the `work/`
directory, as it does the other tables of the ledger.

## Why

**Why two files.** The file holds the content, and the principal
works with it freely. The specification holds the way and the why,
and the file is made again from it whenever it changes. Why the way
and the why are kept in a file of their own rather than in the file
itself is not stated further: the reason is not recorded.

**Why the specification is versioned and approvable.** A work
product is handed over, and a sign-off means something there.

**Why it is not a render.** A render is a view of the chain for an
audience. It carries no content of its own and is never edited by
hand. A work product carries content of its own, and the principal
works with its file.

**Why it is not a research note.** A research note answers one
question about the world outside the project and is immutable. A
work product is iterated.

**Why it is not an artefact of the chain.** An artefact of the chain
is the principal's thinking in items with IDs. A file of any form
cannot carry that.

**Why the render was not stretched to cover it.** Stretching the
render to cover the work product was weighed and dropped. It would
have cost the rule that a render is never edited by hand.

**Why one command and not two.** The forge has two commands for a
render, `/recipe` for the recipe and `/render` for the output. For a
work product it has one. The making is a step of the same round, and
the specification is iterated with the principal, so a second
command would only separate what one conversation does. The price is
a command that does two things.

## A worked example

A generic specification, in the shape of the template the forge
gives for it. The project slug and the name of the work are
placeholders.

```markdown
---
version: 0.1
status: draft
project: <slug>
file: work/cost-model.xlsx
---

# Cost model — Work specification

## Task
A cost model of the proposed change for the people who decide the
budget; the file is to show the cost per year under each option.

## Inputs
- 10-intent.md: POS.NNNN
- sources/<file>

## Method
One sheet per option, the same rows on each; the totals on a sheet
of their own.

## Assumptions
- **ASM.0010** The prices of the current year hold for the first
  year.

## Open
- **TBC.0010** (owner: <who>) The number of licences. Closed by: the
  count from the team that holds them.

## Making
A spreadsheet in the project's language, made from the method above;
nothing of this specification is copied into it.
```

Beside it stand the file `work/cost-model.xlsx` and the history
companion `work/cost-model.spec.history.md`.

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

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
