---
generated: 2026-10-10
made: derived
inputs-hash: bedc6d820dc77f2b
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md
---

# About the solution design

This page explains what the solution design is, what it holds, how
it is shaped and why the forge has it. It is for anyone who uses the
forge and wonders whether a project needs one, for anyone who
extends the forge and wants to know where the rules of this layer
live, and for anyone evaluating whether the chain of a project can
carry a thing all the way to being built. It was put together from
the definition of the solution design
(`.claude/skills/forge/states/solution-design.md`), its template
(`templates/solution-design.md`) and the positions of the forge's
own intent that give the reasons.

## What it is

The solution design is an artefact of the chain, the file
`40-solution-design.md` in a project. It says how the things wanted
are realised, as the solution stands today, and it is kept current:
its body is the present state, its history stands beside it in a
companion file, as with every versioned document of the forge.

It is read by whoever realises the solution, a person or an agent,
without the principal in the room. That reader is the measure of the
document: what he could not work out from the thing itself has to
stand here.

## Where it sits in the chain

The solution design is derived from the lowest layer the project has
above it: the intent alone, the assignment, or a business
requirements document where the project has one. Whatever stands
above that layer is its input as well, together with the project's
decisions and ledger. The intent is read with the project's open
threads.

No layer below the intent is a condition of another. A project takes
the layers it needs, and many end at the intent, where what is
wanted needs no solution written down. A layer a project does not
have is not missing: the state map and the checks say nothing of it,
and the ledger declares no end of the chain. The number in the file
name orders the files and prescribes no sequence.

The division between the intent and the solution design is by kind
of content, never by who said it. The intent says what the principal
wants and why; it does not solve. The test of a sentence: would it
still hold if the thing were realised in a wholly different way? If
it would, it is intent; if not, it is solution. A principle the
realisation must respect whatever its shape is intent; the mechanism
that honours it is solution. What the user is to be able to do, and
what must be true when it is done, is intent; how it is done, what
it is built of, its steps and their order, is solution. An idea of
the principal's about how to build something is solution too. The
reason for the division: an intent that carries the solution cannot
be read as what is wanted, and nobody can be asked for a proposal of
the whole solution over it.

## When it is worth writing

Whether a project writes a solution design is the principal's to
say. It is worth writing where the way is not obvious, where a
choice has a price, or where two hands would solve the same matter
differently if it were not written down.

From the artefacts of the chain the thing must be buildable without
a look at the finished product: the product is what is built, never
a source of its own design. How deep the chain must go for that is
the project's. The solution design gives the architecture; a
technical specification, a layer below, gives the detail where the
one who builds needs it.

## What it holds and what it does not

The solution design holds what cannot be read off the thing itself:
why, against what, at what price, and how the parts fit.

It restates nothing of the layer above, which it cites by ID. It
copies nothing of what realises it, which it names by path. Where a
part is realised in a file of its own, the item names the file and
the detail is the file's; where a part is only part of a file, or no
file exists yet, the item carries the detail.

It is complete for now when every in-scope item of the layer above
is realised by a part, knowingly left unanswered, or open as a TBC,
and when no TBC that blocks realisation is open. It is never
finished: as the solution moves, the design moves with it.

## The shape of the document

The document opens with a short prose head on how the parts work
together: the few ideas the solution rests on, the main courses of
events, and what is deliberately not designed. Below it come the
parts as items, grouped under plain headings when clusters emerge;
then, where there are any, the items for what holds across parts;
then what is open.

### A SOL item

A SOL is a part of the solution, or a matter that holds across
parts. It says what the part is and what it answers for, then, in
this order:

- **Realises:** the IDs of the items of the layer above that this
  part answers, never their wording.
- **Choice:** what was chosen, against what, and what it costs; or
  that there was no real alternative. The alternatives weighed
  include doing nothing, or the least that would do.
- **Where:** the path of what realises it.

A choice Claude made and the principal has not yet judged says so in
plain words at the item, until he has judged it.

### A TBC item

A TBC is what is open or unproven. It carries its owner, what would
close it, and whether it blocks realisation.

Both kinds of item take their IDs from the forge's ID scheme: stable,
never renumbered.

## How it is found

How the design is composed is the principal's choice: found together
by elicitation, or handed over to Claude with a few sentences of
what is wanted. Either way Claude proposes the parts and the choices
and the principal judges them.

Claude names the few real choices and does not dress every part as
one: where there was no real alternative he says so and invents
none, and where a reason is not known he says it is unknown. How
sure he is of a claim he says in words. Where the designing shows
that something cannot be realised, or only at a price not worth
paying, he raises it as a thread, and what is wanted is decided in
the intent first. Nothing is built in the design: it specifies.

Before a design is returned or a write is offered, a map of what a
design can hold is walked; an area may stay empty when it was
considered and found not to apply. The areas are: what is to be
realised and what is knowingly left unanswered; the ground, meaning
what already exists and is kept or replaced, what stands around it,
and what the principal has fixed in advance; the approach as a whole;
the parts and where each is realised; how the parts work together
and what holds across them; the real choices, each with what it was
chosen against and what it costs; what is open or unproven; how it
will be known to hold, by what the thing is compared with the
design; the way there, where the solution replaces something that
runs; and what is deliberately not designed and left to the file or
to the one who realises.

With every pass Claude makes a coverage map: the in-scope items of
the layer above with no part, and the parts that realise no item.
The map is a tool of the pass, not part of the design. A pass ends
by naming what changed and what stays open; when the design is
complete for now, Claude offers the approval as a recommendation,
never a gate.

Research may be proposed where a choice needs outside grounding, and
a challenge of the design offered once it stands; both run on the
principal's word, never on Claude's own judgement.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [About the intent](the-intent.md): the layer whose "what" this answers.
