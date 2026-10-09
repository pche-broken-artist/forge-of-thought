---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md
---

# About the solution design

This page explains what the solution design is, why the forge has it
and where it sits in the chain. It is for a user deciding whether a
project needs one, for someone extending the forge, and for an
evaluator who wants to know what the artefact is for. It was put
together from the solution design's definition
(`.claude/skills/forge/states/solution-design.md`), its template
(`templates/solution-design.md`) and the positions of the forge's own
intent that give its reasons and its place in the chain.

## What it is

The solution design is the artefact that says how the things wanted
are realised. It describes the solution as it stands today and is kept
current, as the intent is: its body is the present state, and its
history stands beside it in a companion file. It is never finished,
only complete for now.

It is read by whoever realises the solution, a person or an agent,
without the principal in the room. That reader is the reason for what
it holds. The design holds what cannot be read off the thing itself:

- why a part is as it is,
- what it was chosen against,
- at what price,
- and how the parts fit together.

It restates nothing of the layer above, which it cites by ID, and it
copies nothing of what realises it, which it names by path.

## Why it is separate from the intent

The intent says what the principal wants and why, and it does not
solve. The test of a sentence is whether it would still hold if the
thing were realised in a wholly different way. If it would, it is
intent; if not, it is solution. A principle the principal sets for the
solution belongs to the intent; the mechanism that honours it belongs
to the solution. The division is by kind of content, never by who said
it: an idea of the principal's about how to build something is
solution too.

The reason: an intent that carries the solution cannot be read as what
is wanted, and nobody can be asked for a proposal of the whole solution
over it. So how things are realised goes into its own artefact, and
the intent stays the statement of what is wanted.

## Where it sits in the chain

The solution design is the file `40-solution-design.md` of a project.
It is derived from the lowest layer the project has above it: the
intent alone, the assignment, or a BRD. Whatever stands above that
layer is its input as well.

No layer below the intent is a condition of another. A project takes
the layers it needs, and many end at the intent, where what is wanted
needs no solution written down. A project without a solution design is
not missing anything: `/forge` and the checks say nothing of it, and
the ledger declares no end of the chain. The number in the file name
orders the files and prescribes no sequence.

## When it is worth writing

A solution design is worth writing where:

- the way is not obvious,
- a choice has a price,
- two hands would solve the same matter differently if it were not
  written down.

Whether it is worth writing in a given project is the principal's to
say.

## How deep the chain must go

From the artefacts of the chain, the thing must be buildable without a
look at the finished product. The product is what is built, never a
source of its own design. How deep the chain must go for that is the
project's choice. The solution design gives the architecture; where
the one who builds needs the detail, a technical specification is a
layer below it, taken where the project needs it.

## What it is made of

The design opens with a short prose head on how the parts work
together: the few ideas the solution rests on, the main courses of
events, and what is deliberately not designed. Below it come the
parts, grouped under plain headings, then the matters that hold across
parts, then what is open.

A part of the solution, or a matter that holds across parts, is a SOL
item. It says what the part is and what it answers for, then, in this
order:

| Field | What it holds |
|---|---|
| Realises | The IDs of the items of the layer above, never their wording. |
| Choice | What was chosen, against what, and what it costs; or that there was no real alternative. |
| Where | The path of what realises the part. |

Two rules govern what an item carries:

- Where a part is realised in a file of its own, the item names the
  file and the detail is the file's. Where it is only part of a file,
  or no file exists yet, the item carries the detail.
- A choice Claude made and the principal has not judged says so in
  plain words at the item, until he has judged it.

What is open is a TBC item. It carries its owner, what would close it,
and whether it blocks realisation.

## When it is complete

The design is complete for now when every in-scope item of the layer
above is realised by a part, knowingly left unanswered, or open as a
TBC, and when no TBC that blocks realisation is open. With every pass
Claude maps the in-scope items with no part and the parts that realise
no item; that map is a tool of the pass, not part of the design. When
the design is complete for now, Claude offers the approval as a
recommendation, never as a gate.

## How Claude works on it

How the design is composed is the principal's choice. Either way
Claude proposes the parts and the choices, and the principal judges
them. Claude names the few real choices and does not dress every part
as one: where there was no real alternative he says so and invents
none, and where a reason is not known he says it is unknown. He says
in words how sure he is of a claim.

If the designing shows that something wanted cannot be realised, or
only at a price not worth paying, Claude raises it as a thread, and
what is wanted is decided in the intent first. Nothing is built in the
design: it specifies.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [About the intent](the-intent.md): the layer whose "what" this
  answers.
