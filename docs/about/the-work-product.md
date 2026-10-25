---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 5d25554652e42494
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project made with work of its own,
such as a model, an analysis or a worked task, in whatever form the
work needs. This page explains what a work product is, why it is
kept as two files, and why it is neither an artefact of the chain
nor a render. It is written for anyone who uses the forge, extends
it or evaluates it.

## What it is

A project mostly holds the documents of its chain and the renders
made from them. Some results fit neither. The principal (the person
whose thinking is being forged, with final say on all content) may
ask Claude for a result that needs work of its own: a model, an
analysis, a worked task. Such a result is a work product.

A work product:

- takes its inputs from the chain and from the project's resources
  (its sources and research);
- adds work of its own;
- is iterated over several rounds;
- is handed over as a result of the project;
- feeds what it shows back into the intent.

It is a document kind of its own, **work**, in a group of its own.
The kinds of document a project holds are described in
[Documents and records](documents-and-records.md). In the forge's
table of document kinds the row reads:

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |

## How it works

### Two files in `work/`

A work product lives in the project's `work/` directory as two
files:

- `work/<name>.<ext>`: the file. It holds the content and is named
  by the work alone.
- `work/<name>.spec.md`: the specification beside it. It holds the
  way and the why.

The specification says:

- what the task is;
- which items and files the work starts from, cited by ID and path
  and never copied;
- the method;
- the assumptions, as items with the prefix `ASM`;
- what is still open, as items with the prefix `TBC`, each with an
  owner;
- how the file is made from it, in its section `## Making`.

A work specification has no ID prefix of its own. Nothing of
`## Making` is copied into the file. The skeleton of the
specification is `templates/work.md`, listed in
[Templates](../reference/templates.md).

### Language

The specification is written in the project's language, as the
artefacts of the chain are. The file is written in whatever language
the work needs. The specification's `## Making` section says which.

### Versions and history

The specification is versioned by the house scheme: `0.1`, `0.2`
and so on for drafts, an integer for an approved version. Its
history (the record of what changed and why) lives in an
append-only companion beside it, `work/<name>.spec.history.md`. The
specification can be approved. The file is made from the
specification again whenever the specification changes.

### Working with the file

The principal works with the file freely. Three things follow from
that:

- A conclusion that is to hold goes into the intent first, as a
  position.
- A change of the way or the why made in the file is carried into
  the specification in the same round and written with it. The way
  and the why are the task, the inputs, the method and what is
  assumed. The states of the work and its wording belong to the
  file alone.
- A file touched by hand and not remade is said to be so by a
  record in the specification's history.

### The Work table of the ledger

The ledger is the project's single source of truth for state, made
from the documents by a script whenever it is read. Its Work table
is made by that script from the records of each specification's
history. It carries one row per work product:

- the file;
- the specification with its version;
- the inputs with their versions;
- when the file was made;
- its state.

The state is one of three:

- `current`: the last record is the making of the file;
- `stale`: the specification was written and the file has not been
  made since;
- `by hand`: the principal has worked the file and does not want it
  remade, recorded on his word.

### One command

One command serves a work product, `/work`. Bare, it lists the
project's work products; with a name, it works the specification
with the principal and makes the file from it in the same round, on
his word. How to run it is the page
[Work a work product](../use/work-a-work-product.md).

A work product is composed as any artefact is. The principal may
find it together with Claude by questions, or hand it over with a
few sentences of what he wants. Claude then proposes, with its
assumptions and choices listed, and the principal judges.

## Why

**Why two files.** The file is what the work produces, in any form.
The specification keeps the way and the why beside it, so the file
can be made again from it. The specification is versioned and
approvable because a work product is handed over, and a sign-off
means something there. Why the file is named by the work alone is
not recorded.

**Why the principal may work the file freely.** That is what the
file is for. What must last is carried elsewhere: a conclusion into
the intent, a change of the way or the why into the specification.

**Why it is not a render.** A render is a view of the chain for an
audience. It carries no content of its own and is never edited by
hand. A work product has content of its own, and the principal
works with it. Renders are described in
[Renders and recipes](renders-and-recipes.md).

**Why the render was not stretched to cover it.** Stretching the
render to cover work products was weighed and dropped. It would
have cost the rule that a render is never edited by hand.

**Why it is not a research note.** A research note answers one
question about the world outside the project and is immutable once
written. A work product is iterated.

**Why it is not an artefact of the chain.** An artefact of the chain
is the principal's thinking in items with IDs. A file of any form
cannot carry that.

**Why one command and not two.** The making of the file is a step
of the round, and the specification is iterated with the principal.
A second command would only separate what one conversation does.
The price is a command that does two things.

## A worked example

A generic specification, following the skeleton. The slug, the name
and the content are placeholders taken from no project.

```markdown
---
version: 0.2
status: draft
project: <slug>
file: work/cost-model.xlsx
---

# Cost model — Work specification

## Task
A cost model of the proposed change for the steering group,
showing the cost per year under two volumes.

## Inputs
- 10-intent.md: POS.NNNN
- sources/<file>

## Method
One sheet per volume, one row per cost item, the totals per year
at the foot of each sheet.

## Assumptions
- **ASM.0010** Prices stay at today's level over the period.

## Open
- **TBC.0010** (owner: <who>) The volume of the second year.
  Closed by: the forecast of the next quarter.

## Making
A spreadsheet in the language of the steering group, made from the
method above; none of this specification is copied into it.
```

Beside it lie `work/cost-model.xlsx`, the file, and
`work/cost-model.spec.history.md`, the history. If the principal
edits the spreadsheet and keeps his edits, a record in the history
marks the file `by hand`, and the ledger's Work table shows that
state.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
