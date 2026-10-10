---
generated: 2026-10-10
made: mirrored
inputs-hash: 42dc610bd05c8c62
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - CLAUDE.md
---

# Design the solution

This page is for the person who wants to write down how the things
wanted are realised, or to bring an existing design up to date. It
says how to run the pass and what you see at the end of it.

## Start

Run `/forge solution-design [slug]`, with the slug of your project.
The command iterates `40-solution-design.md`. The design is derived
from the lowest layer the project has above it: the assignment or the
BRD, or the intent alone where there is nothing between. Claude also
reads the decisions, the ledger and the project's threads. Where the
thing already exists, Claude reads what realises it as it stands.

Whether a design is worth writing is yours to say. A project that has
no use for one simply does not have it, and nothing is missing.

## The ways in

- **No design yet.** The first design is created from the template as
  version 0.1, with its history companion and its row in the ledger.
- **A layer above has moved.** The pass runs on what changed.
- **The thing changed below.** The design is brought current with it.
- **A wording fix.** It is made directly.

You may compose the design together with Claude, or hand it over with
a few sentences of what you want. Either way Claude proposes the parts
and the choices, and you judge them. Claude names the few real
choices and does not dress every part as one. Where there was no real
alternative he says so, and where a reason is not known he says that
it is unknown. A choice Claude made that you have not judged yet is
marked as such in the design until you have.

## The coverage map

At every pass Claude makes a coverage map. It lists the in-scope
items of the layer above that have no part, and the parts that
realise no item. The map is a tool of the pass and is not part of the
design. The design is complete for now when every in-scope item is
realised by a part, knowingly left unanswered, or open as a question
with an owner, and when no open question blocks realisation. It is
never finished.

## What cannot be realised

Designing may show that something wanted cannot be realised, or only
at a price not worth paying. Claude raises it as a thread, and what is
wanted is decided in the intent first. The design does not settle it.

## What you see

The design is one file with the ideas it rests on, the parts, what
holds across the parts, and what is still open. Each part says what it
realises, what was chosen against what and at what cost, and where it
lives; the shape of a part is on the page about the solution design.
A write rewrites the design for coherence rather than appending to
it. The pass ends with Claude naming what changed and what stays
open. When the design is complete for now, he offers approval as a
recommendation, never as a gate.

## Test it

Once the design stands, Claude offers `/challenge <persona>
solution-design`, an independent test of its choices. The persona
`architect` exists for this. It runs only on your word.

## See also

- [About the solution design](../about/the-solution-design.md): what a solution design holds and why it restates nothing above it.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
