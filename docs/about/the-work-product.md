---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: b18f5a251f02b2b4
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own:
a model, an analysis, a worked task, in whatever form the work needs.
This page explains what a work product is, why it is kept as two
files, and why it is neither an artefact of the chain nor a render.
It is written for anyone who uses the forge, extends it or weighs
whether it fits their way of working.

## What it is

A work product is any result of Claude's work that the principal
asked for. The principal is the person whose thinking is being
forged, and who has the final say on every document.

A work product has these traits:

- It takes its inputs from the chain and from the project's
  resources (its sources and research).
- It adds work of its own to those inputs.
- It is iterated, like any document the principal works on.
- It is handed over as a result of the project.
- What it shows flows back into the intent.

It is a kind of document of its own, called **work**, and it lives in
a folder of its own, `work/`. The forge's table of document kinds
describes it as "an output of the project made with work of its own:
the file holds the content, the specification beside it the way and
the why". Claude writes it and the principal judges it. The
specification is versioned. The file is remade from the
specification, and the principal works with the file freely. The
other kinds a project holds are described on
[Documents and records](documents-and-records.md).

## How it works

### Two files

A work product is two files side by side in `work/`:

- `work/<name>.<ext>`: the file, which holds the content. It is
  named by the work alone, and its extension is whatever the work
  needs.
- `work/<name>.spec.md`: the specification, which holds the way and
  the why.

The specification says:

- what the task is: what is asked, for whom, and what the file is to
  show;
- which items and files the work starts from, cited by ID and by
  path and never copied;
- the method: how the work is done, and the structure of the file;
- what is assumed, as assumption items (`ASM`);
- what is still open, as open items (`TBC`), each with an owner and
  what would close it;
- how the file is made from the specification, in its `## Making`
  section.

Nothing of the `## Making` section is copied into the file. The
specification has no ID prefix of its own. Its skeleton is the
template `templates/work.md`, listed on [Templates](../reference/templates.md).

### Language

The specification is written in the project's language, as the
artefacts of the chain are. The file is written in whatever language
the work needs. The `## Making` section says which.

### Versions and sign-off

The specification is versioned by the forge's house scheme: `0.1`,
`0.2` and so on for drafts, integers for approved versions. It keeps
its history in a companion file beside it,
`work/<name>.spec.history.md`, one record per change. The
specification can be approved. Because a work product is handed over,
a sign-off means something there. Whenever the specification changes,
the file is made from it again.

### Working with the file

The principal works with the file freely, since that is what it is
for. Three rules keep the two files honest:

- A conclusion that is to hold goes into the intent first, as a
  position of the principal.
- A change to the way or the why made in the file (its task, its
  inputs, its method or what it assumes) is carried into the
  specification in the same round and written with it.
- A file the principal has touched by hand and does not want remade
  is said so by a record in the specification's history.

The wording and the states of the work itself belong to the file
alone.

### The Work table

The ledger is the project's one record of state, made by a script at
read time from the documents. Its Work table carries one row per work
product, made by the ledger script from the records of the
specification's history. Each row shows:

- the file;
- the specification, with its version;
- the inputs, with their versions;
- when the file was made;
- its state.

The state is one of three:

| State | Meaning |
|---|---|
| `current` | the last record is the making of the file |
| `stale` | the specification was written and the file was not made again after it |
| `by hand` | the principal has worked the file and does not want it remade, recorded on his word |

### The command

One command, `/work`, serves both files: it works the specification
with the principal and makes the file from it in the same round. How
to run it is on [Work a work product](../use/work-a-work-product.md).

## Why

### Why two files

The file holds the content in whatever form the work needs. A file of
any form cannot carry the principal's thinking as items with IDs, and
it cannot carry its own way and why. The specification carries them,
so the task, the inputs, the method and the assumptions stay visible
and can be versioned and approved while the principal works the file
freely.

### Why it is not a render

A render is a view of the chain for an audience. It carries no
content of its own and is never edited by hand; it is remade from its
recipe instead. A work product adds work of its own, and the
principal works its file freely. The render is described on
[Renders and recipes](renders-and-recipes.md).

Stretching the render to cover work products was weighed and
dropped. It would have cost the rule that a render is never edited by
hand.

### Why it is not a research note

A research note answers one question about the world outside the
project, and it is immutable once written. A work product is iterated
and worked on.

### Why it is not an artefact of the chain

An artefact of the chain is the principal's thinking written as items
with stable IDs. The file of a work product may have any form, and a
file of any form cannot carry such items.

### Why one command for both files

The making of the file is a step of the round in which the
specification is iterated with the principal. A second command would
only separate what one conversation does. The price is a command that
does two things. The forge chose this against the pair `/recipe` and
`/render`, which split the same kind of work into two commands.

## A worked example

A generic specification, in the shape the template gives. The project
slug, the name and the items are placeholders.

```markdown
---
version: 0.1
status: draft
project: example-project
file: work/cost-model.xlsx
---

# Cost model — Work specification

## Task
A cost model of the proposed change, for the steering group, showing
the yearly running cost of each option.

## Inputs
- 10-intent.md: POS.0100, POS.0110
- sources/vendor-offer.md

## Method
One sheet per option, one row per cost item, a summary sheet that
compares the options over three years.

## Assumptions
- **ASM.0010** Prices stay as the vendor offer states them for the
  three years.

## Open
- **TBC.0010** (owner: finance) The internal hourly rate to use.
  Closed by: the rate confirmed by finance.

## Making
Made by Claude as a spreadsheet in English from the Method above; the
file carries the figures and the sheets, none of this specification.
```

Beside it would stand `work/cost-model.xlsx`, the file, and
`work/cost-model.spec.history.md`, the history companion.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
