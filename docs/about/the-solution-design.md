---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 54b1a17b2c5ae529
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the artefact of the chain that says how the
things wanted are realised. This page explains what it holds, who
writes and reads it, when it is complete and why it restates nothing
of the layer above it. It is written for anyone who uses the forge,
extends it or weighs it up.

## What it is

The solution design is a document of the chain, the file
`40-solution-design.md` of a project. It says how the things wanted
are realised, part by part, with the choices the parts rest on. It
describes the solution as it stands today and is kept current. Its
body is the present state. Its history stands beside it in a
companion file, `40-solution-design.history.md`.

It answers the "what" of the layer above it. The layer above says
what the principal (the person whose thinking is forged) wants and
why; the solution design says how that is realised. Nothing is built
in it: the design specifies.

A project does not need one. Many projects end at the intent, where
what is wanted needs no solution written down. A layer a project
does not have is not missing: `/forge` and the checks say nothing of
it.

## Who writes and reads it

- **Written by** the principal with Claude. How it is composed is the
  principal's choice: found together in conversation, or handed over
  to Claude with a few sentences of what he wants. Either way Claude
  proposes the parts and the choices, and the principal judges them.
- **Read by** whoever realises the solution, a person or an agent (an
  automated worker such as a model run), without the principal in the
  room.

## Made from

The solution design is derived from the lowest layer the project has
above it. That layer may be one of these:

- the intent alone;
- the assignment;
- the BRD.

Whatever stands above that layer is an input too. Beside them it
reads the project's decisions, its ledger (the state of the project,
made from its documents when it is read) and, with the intent, the
project's open threads. Where the thing already exists, what realises
it is read as it stands. Research and sources are read as the
principal directs.

Whether a solution design is written at all is the principal's to
say. It is worth writing in these cases:

- where the way is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it were
  not written down.

## What it holds

It holds what cannot be read off the thing itself:

- why the solution is as it is;
- what each choice was made against;
- at what price;
- how the parts fit together.

It restates nothing of the layer above. It cites that layer by ID.
It copies nothing of what realises it. It names that by path.

The file has a short prose head and then items:

- **How the parts work together:** short prose on the few ideas the
  solution rests on, the main courses of events, and what is
  deliberately not designed.
- **Parts:** one SOL item per part, grouped under plain headings when
  clusters emerge.
- **Across the parts:** SOL items for what holds across parts, in the
  same shape.
- **Open:** TBC items, the questions still to be confirmed.

Empty sections are deleted.

### The shape of a SOL item

A SOL item is a part of the solution, or a matter that holds across
parts. It first says what the part is and what it answers for. Then
it gives three fields in this order:

- `Realises:` the IDs of the items of the layer above that the part
  realises, never their wording.
- `Choice:` what was chosen, against what, and what it costs; or that
  there was no real alternative.
- `Where:` the path where the part is realised.

Where a part is realised in a file of its own, the item names the
file and the detail stays in that file. Where the part is only part
of a file, or no file exists yet, the item carries the detail. A
choice Claude made that the principal has not yet judged says so in
plain words at the item, until he has judged it.

### The shape of a TBC item

A TBC item is an open question. It carries three things:

- its owner;
- what would close it;
- whether it blocks realisation.

### A worked example

A generic item, in the shape the template gives, not taken from any
project:

```
### Intake
- **SOL.0010 Order intake.** Receives an order and hands it on
  for checking; answers for every order being recorded once.
  Realises: REQ.0010, REQ.0020. Choice: a queue, chosen against a
  direct call, at the cost of one more component to run.
  Where: `src/intake/`.

## Open
- **TBC.0010** (owner: <who>) Which retry limit the queue uses.
  Closed by: a measurement of peak load. Blocks realisation: no.
```

## Complete when

The solution design is complete for now when two things hold:

- every item of the layer above that is in scope is realised by a
  part, knowingly left unanswered, or open as a TBC;
- no TBC that blocks realisation is open.

It is never finished. When completion is reached, Claude offers the
approval as a recommendation, never as a gate.

## How it is found

It is iterated through `/forge solution-design`. Claude reads the
inputs and the design as it stands. A pass starts in one of these
situations:

- there is no design yet, and the principal says whether one is
  worth writing;
- a layer above moved, and the pass runs on what changed;
- the thing changed below, and the design is brought current;
- a wording needs fixing, and it is fixed directly.

With every pass Claude makes a coverage map. It lists the in-scope
items of the layer above that have no part, and the parts that
realise no item. The coverage map is a tool of the pass, not part of
the design.

Along the way Claude walks the areas a design must consider:

- what is to be realised, and what is knowingly left unanswered;
- the ground: what exists and is kept or replaced, what stands
  around it, what the principal has fixed in advance;
- the approach as a whole;
- the parts, and by whom each is done where it is not software;
- how the parts work together;
- the real choices, each with what it was chosen against and what it
  costs;
- what is open or unproven, and whether it blocks realisation;
- how it will be known that the thing matches the design;
- the way there, where the solution replaces something that runs;
- what is deliberately left to the file or to the one who realises.

An area may stay empty when it was considered and found not to
apply. Claude names the few real choices and does not dress every
part as one. Where there was no real alternative, it says so and
invents none. Where a reason is not known, it says so.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first. Where a choice needs outside grounding,
Claude may propose `/research`. Once the design stands, Claude may
offer `/challenge` on it as an independent test of the choices. Both
run only on the principal's word.

A write rewrites the design for coherence and never appends.

## Why

The intent and the solution design are kept apart by kind of
content. An intent that carries the solution cannot be read as what
is wanted. Nobody can then be asked for a proposal of the whole
solution over it. The test of a sentence is whether it would still
hold if the thing were realised in a wholly different way. If it
would, it belongs to the intent; if not, it belongs to the solution
design.

The thing must be buildable from the artefacts of the chain without
a look at the finished product. The product is what is built and is
never a source of its own design. This is why the design holds the
why, the alternatives, the price and the fit: these cannot be read
off the thing itself.

The solution design gives the architecture. A further, more detailed
specification can give the detail where the one who builds needs it.

Why the design cites the layer above by ID rather than restating it,
and names what realises a part by path rather than copying it: the
reason is not recorded.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
