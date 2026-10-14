---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: bb4815183181e6b0
inputs:
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/40-solution-design.md#SOL.0640
  - templates/work.md
  - CLAUDE.md#Document kinds
---

# The work product

A work product is an output of a project that is made with work of
its own: a model, an analysis, a worked task, in whatever form the
work needs. This page says what a work product is, why it is two
files, and why it is neither an artefact of the chain nor a render.
It is for the user who asks for one, the extender who wants to know
where the kind sits among the others, and the evaluator who wants to
know what keeps it honest.

## What it is

A project may make outputs that are neither artefacts nor renders.
Such an output is any result of Claude's work that the principal
(the person whose thinking is being forged) asked for. It takes its
inputs from the chain and from the resources of the project, the
sources and the research notes. It adds work of its own. It is
iterated. It is handed over as a result of the project. What it
shows flows back into the intent.

The forge gives it a document kind of its own, **work**, in a group
of its own, the directory `work/`. Among the [kinds of document a
project holds](documents-and-records.md) the row reads: written by
Claude, judged by the principal; versioned, the specification; the
file remade from the specification, and the principal works with it
freely.

A work product is two files:

- the file, `work/<name>.<ext>`: it holds the content and is named
  by the work alone
- the specification, `work/<name>.spec.md`: it holds the way and the
  why

The specification carries no ID prefix of its own. The reason is
not recorded.

The specification is written in the project's language, as the
artefacts are. The file is written in whatever language the work
needs. Which language that is, the specification's `## Making`
section says.

## How it works

The specification holds, section by section, what the work rests
on. Its skeleton is the work template among the
[templates](../reference/templates.md) of the forge:

- `Task`: what is asked, for whom, and what the file is to show
- `Inputs`: the items the work starts from, cited by ID, and the
  files, cited by path, as they stand and never copied
- `Method`: how the work is done, such as the model, the steps and
  the structure of the file
- `Assumptions`: what is taken as given, as ASM items
- `Open`: what is still open, as TBC items, each with an owner and
  what would close it
- `Making`: how the file is made from the specification, by what
  means, in what format and language, and what of the specification
  the file carries

Nothing of the `## Making` section is copied into the file.

The specification is versioned by the house scheme (drafts as 0.x,
an integer once approved). Its history lives in a companion beside
it, `work/<name>.spec.history.md`, one record per change. The
specification can be approved. Whenever the specification changes,
the file is made from it again.

A work product is composed as any artefact is. The principal may
find it together with Claude by questions, or hand it over with a
few sentences of what he wants. Handed over, Claude proposes the
specification with its assumptions and choices listed, and the
principal judges.

One command, `/work <name>`, is the single door to a work product:
it works the specification with the principal and makes the file
from it in the same round, on the principal's word; how a run goes
is on [Work a work product](../use/work-a-work-product.md). The
first specification is created from the template as version 0.1,
with its history companion and its row in the ledger (the project's
single source of truth for state).

The ledger's Work table carries one row per work product: the file,
the specification with its version, the inputs with their versions,
when the file was made, and the state of the file. The state is one
of three:

- `current`: set when the file is made
- `stale`: set by a write of the specification that no making has
  followed
- `by hand`: set on the principal's word when he has worked the file
  and does not want it remade

The check named `light` verifies the Work table against the
directory, as it does the other tables of the ledger.

The principal works with the file freely; that is what the file is
for. What he finds there goes to the place it belongs:

- a conclusion that is to hold goes into the intent first, as a
  position
- a change of the structure goes into the specification
- a file touched by hand and not remade is said so in the Work
  table, as `by hand`

## Why

A work product is two files because the content and the reasoning
behind it behave differently. The file is the result, in whatever
form the work needs, and the principal works with it freely. The
specification is the way and the why, and it is what is iterated,
versioned and judged. An artefact of the chain is the principal's
thinking in items with IDs. A file of any form cannot carry that.
So the thinking about the file stands beside it, in a document that
can.

The specification is approvable because a work product is handed
over. A sign-off means something there.

A work product is not a [render](renders-and-recipes.md). A render
is a view of the chain for an audience. It carries no content of
its own. It is never edited by hand. A work product adds work of
its own, and the principal works with its file by hand. Stretching
the render to cover work products was weighed and dropped. It would
have cost the rule that a render is never edited by hand.

A work product is not a research note. A research note answers one
question about the world outside the project, and it is immutable.
A work product is iterated.

A work product is not an artefact of the chain. The chain holds the
principal's thinking in items with stable IDs. A model or an
analysis is made from that thinking, and what it shows flows back
into the intent, but the file itself is not a layer of the chain.

One command serves both files, against two commands as the recipe
and the render have. The making is a step of the round, and the
specification is iterated with the principal in that round. A
second command would only separate what one conversation does. The
price is a skill that does two things.

## A worked example

A generic specification, as the template shapes it, for a work
product named `capacity-model` in a project with the placeholder
slug `my-project`. The file beside it would be
`work/capacity-model.xlsx`.

```
---
version: 0.1
date: 2026-10-14
status: draft
last_change: <derived from the records of the newest version in work/capacity-model.spec.history.md>
project: my-project
file: work/capacity-model.xlsx
---

# Capacity model — Work specification

## Task
A model of the team's capacity over the next four quarters, for
the principal, showing where the plan of the intent exceeds what
the teams can deliver.

## Inputs
- 10-intent.md: POS.NNNN
- sources/headcount-plan.md

## Method
One sheet per quarter; one row per team; demand taken from the
plan, supply from the headcount source; the gap computed per row.

## Assumptions
- **ASM.0010** A full-time person yields four productive days a
  week.

## Open
- **TBC.0010** (owner: the principal) Whether contractors count
  as supply. Closed by: the principal's word.

## Making
A spreadsheet, made by Claude from this specification, in English;
the file carries the sheets and the rows, none of the text of this
specification.
```

The history companion `work/capacity-model.spec.history.md` stands
beside it, and the ledger's Work table carries one row: the file,
the specification at 0.1, the inputs with their versions, the date
of the making, and the state `current`.

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

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
