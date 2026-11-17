---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 2b940148cb713f5e
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
why it is neither an artefact nor a render. The kinds of document are
on [Documents and records](documents-and-records.md), and the render
is on [Renders and recipes](renders-and-recipes.md). The page is for
whoever works with the forge, extends it or evaluates it.

## What it is

A project may make outputs that are neither artefacts nor renders. A
work product is such an output: any result of Claude's work that the
principal (the person whose thinking is being forged) asked for.

A work product has this life in a project:

- It takes its inputs from the chain (the artefacts of the project,
  such as the intent) and from the resources (the sources and the
  research of the project).
- It adds work of its own.
- It is iterated.
- It is handed over as a result of the project.
- What it shows flows back into the intent.

The chain and the intent are each given in one line in the
[Glossary](../reference/glossary.md).

A work product is a document kind of its own, named `work`. It lives
in a group of its own, the directory `work/`. The table of document
kinds gives it this row:

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |

A work product is two files:

| File | Path | What it holds |
|---|---|---|
| the file | `work/<name>.<ext>`, named by the work alone | the content |
| the specification | `work/<name>.spec.md` | the way and the why |

The specification is a versioned document. Its history companion
(the append-only record of what changed in it, and why) lies beside
it as `work/<name>.spec.history.md`.

## How it works

The picture shows the two files and what surrounds them:

```
the chain and the resources
   |  cited by ID and path, never copied
   v
work/<name>.spec.md  ---- records ---->  work/<name>.spec.history.md
(the way and the why)                              |
   |  the file is made on the                      v
   |  principal's word                   the ledger's Work table
   v                                     (current, stale, by hand)
work/<name>.<ext>
(the content)
   |
   v
the principal works with the file freely;
a conclusion that is to hold goes into the intent first
```

### The specification

The specification holds the way and the why of the work. Its header
carries four fields: `version`, `status`, `project` and `file`. The
field `file` names the file the specification makes. Its sections
are these, in this order:

| Section | What it says |
|---|---|
| Task | what is asked, for whom, and what the file is to show |
| Inputs | the items and the files the work starts from: items by ID and files by path, as they stand, never copied |
| Method | how the work is done: the model, the steps, the structure of the file |
| Assumptions | what the work assumes, each assumption an item with the prefix `ASM` |
| Open | what is open, each matter an item with the prefix `TBC`, with an owner and what would close it |
| Making | how the file is made from the specification: by what means, in what format and language, and what of the specification the file carries |

These rules hold for the specification:

- A work product has no prefix of its own. Its items use the
  prefixes `ASM` and `TBC`.
- A new item takes the next free number of the project. The count
  runs after every specification the project already has.
- The sections Assumptions and Open are deleted where they are empty.
- The Making section is never copied into the file.
- The specification is written in the project's language, as the
  artefacts are. The file is written in whatever language the work
  needs, and the Making section says which.
- The specification is versioned by the house scheme (the forge's
  scheme of version numbers) and keeps its history companion. Its
  status is `draft`, `approved` or `superseded`.
- The specification can be approved.
- A new specification is created from the template
  `templates/work.md` at version 0.1, with its history companion
  created beside it from `templates/history.md`. The templates are
  listed on [Templates](../reference/templates.md).

### The file

The file holds the content, in whatever form the work needs. It is
made from the specification, and it is made again whenever the
specification changes.

The principal works with the file freely: that is what the file is
for. What the principal does in the file is treated by its kind:

- A conclusion that is to hold goes into the intent first, as a
  position (an item of the intent).
- A change of the way or the why made in the file is carried into
  the specification in the same round and written with it. Such a
  change is a change of the task, of the inputs, of the method or of
  what the work assumes.
- The states of the work and its wording belong to the file alone.
- A file touched by hand and not remade is said so by a record in
  the specification's history.

### The state in the ledger

The ledger is the single source of truth for the state of a project,
made at read time by a script. Its Work table carries one row per
work product. A row holds:

- the file
- the specification with its version
- the inputs with their versions
- when the file was made
- the state of the file

The state is one of three:

| State | What it means |
|---|---|
| `current` | the record of the making stands: the file was made from the specification |
| `stale` | the specification was written and no making followed |
| `by hand` | the principal has worked the file and does not want it remade; a `changed` record with `state: by hand` says so, written on the principal's word |

The ledger script makes the Work table from the records of the
specification's history. A work product gets its row from the first
record of its specification. A check of the forge named `light`
verifies the Work table against the directory, as it does the other
tables of the ledger.

### How a work product is composed

A work product is composed as any artefact is: by elicitation or
handed over (both ways of composing are in the
[Glossary](../reference/glossary.md)). Claude proposes, with its
assumptions and its choices listed. The principal judges.

One command, `/work <name> [slug]`, is the one way to a work product:
without a name it lists the work products of the project from the
ledger, and with a name it works the specification with the principal
and makes the file from it in the same round, on the principal's
word. How to run it is on
[Work a work product](../use/work-a-work-product.md).

## Why

**Why a kind of its own.** The neighbours of a work product stay what
they are, and a work product is none of them:

| Neighbour | What it is | Where a work product differs |
|---|---|---|
| a render | a view of the chain for an audience; it carries no content of its own and is never edited by hand | a work product adds work of its own, and the principal works with its file freely |
| a research note | an answer to one question about the world outside; it is immutable | a work product takes its inputs from the chain and the resources, and it is iterated |
| an artefact of the chain | the principal's thinking in items with IDs | the content of a work product is a file of any form, and a file of any form cannot carry items with IDs |

**Why the render was not stretched.** Stretching the render to cover
the work product was weighed and dropped. It would have cost the rule
that a render is never edited by hand.

**Why two files.** The reason is not recorded. What is recorded is
the division: the file holds the content in whatever form the work
needs, and the specification holds the way and the why. It is also
recorded that a file of any form cannot carry items with IDs, and
that the assumptions and the open matters stand as items in the
specification.

**Why the specification can be approved.** A work product is handed
over, and a sign-off means something there.

**Why one command and not two.** The specification and the file are
worked by one command, where a recipe and its render have two
(`/recipe` and `/render`). The making is a step of the round, and the
specification is iterated with the principal. A second command would
only separate what one conversation does. The price is a skill (the
file that defines the command) that does two things.

## A worked example

A generic specification, in a project with the placeholder slug
`example-project`. The work is a cost model, and the specification
lies at `work/cost-model.spec.md`:

```markdown
---
version: 0.1
status: draft
project: example-project
file: work/cost-model.xlsx
---

# Cost model — Work specification

<!-- Shape: templates/work.md -->

## Task
A cost model of the two options the intent weighs, for the people who
choose between them. The file is to show the yearly cost of each
option over five years and the year in which one overtakes the other.

## Inputs
- 10-intent.md: POS.NNNN
- sources/price-list.md

## Method
One sheet per option, one row per cost item, one column per year. A
summary sheet sets the two totals side by side.

## Assumptions
- **ASM.0010** The prices of the price list hold for all five years.

## Open
- **TBC.0010** (owner: the principal) Whether the cost of training
  belongs in the model. Closed by: the principal's decision.

## Making
A workbook in English, filled by a script from the method above. The
file carries the assumptions on its summary sheet and nothing else of
this specification.
```

What the example shows:

- The field `file` names the file the specification makes,
  `work/cost-model.xlsx`. The file is named by the work alone.
- The history companion lies beside the specification as
  `work/cost-model.spec.history.md`.
- The inputs are cited, never copied. `POS.NNNN` stands for the ID of
  an item of the intent, and the second line is a file by its path.
- The assumption and the open matter are items with IDs. The open
  matter names its owner and what would close it.
- The Making section names the means, the format, the language and
  what of the specification the file carries.

Once the file is made, the Work table of the ledger shows the work
product as `current`. A later write of the specification with no
making after it turns the state to `stale`.

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

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
