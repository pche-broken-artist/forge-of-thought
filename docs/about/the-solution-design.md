---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 579f4ff8e358babf
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the artefact of the chain that says how the
things wanted are realised. This page says what it is, who writes
and reads it, what it is made from, what it holds, when it is
complete and why it is shaped as it is, for anyone who works with a
project of the forge: the one whose project needs a design, the one
who extends the forge and the one who judges it. How a design is
iterated step by step is the page [Design the
solution](../use/design-the-solution.md).

## What it is

The solution design is one [artefact of the
chain](../reference/glossary.md): a document of the versioned line
that runs from the brief through the intent to the layers a project
takes below it. Its file is `40-solution-design.md`. Its history
stands beside it in an append-only companion,
`40-solution-design.history.md`.

It describes the solution as it stands today and is kept current,
as the intent is. The body is the present state. The companion is
the record of how it got there.

It gives the architecture. A technical specification gives the
detail where the one who builds needs it. Nothing is built in the
design: the design specifies.

Not every project has one. A project takes the layers it needs
below the intent, and many end at the intent, where what is wanted
needs no solution written down. A design is worth writing in three
cases:

- where the way is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it
  were not written down.

Whether a design is written is the principal's to say. The
principal is the one whose thinking is forged, the final authority
on all content. A layer a project does not have is not missing:
the state map of `/forge` and the checks say nothing of it, and
the ledger, the project's single source of truth for state,
declares no end of the chain.

## Who writes and reads it

The design is composed by the principal with Claude. How it is
composed is the principal's choice, artefact by artefact: found
together by elicitation, or handed over with a few sentences of what
he wants. Either way Claude proposes the parts and the choices and
the principal judges them.

Claude names the few real choices and does not dress every part as
one. Where there was no real alternative it says so and invents
none. Where a reason is not known it says it is unknown. How sure it
is of a claim it says in words. A choice Claude made and the
principal has not yet judged says so in plain words at the item,
until he has judged it.

The design is read by whoever realises the solution, a person or an
agent, without the principal in the room. The front-matter of the
file names that audience.

## Made from

The design is derived from the lowest layer the project has above
it. That layer is one of three:

- the intent alone;
- the assignment, where the project has one;
- the BRD, where the project has one.

Whatever stands above that layer is its input as well. Beside the
layer above, the design is made from:

- `decisions.md`, the record of the principal's decisions with
  their reasons;
- the ledger;
- `threads.md`, the project's open threads, read together with the
  [intent](the-intent.md);
- what realises the thing, read as it stands, where the thing
  already exists;
- research and sources, as the principal directs.

The shape of the file is the template `templates/solution-design.md`.

## What it holds

The design holds what cannot be read off the thing itself: why,
against what, at what price, and how the parts fit. It is made of
items under a short prose head.

The prose head, "How the parts work together", carries the few
ideas the solution rests on, the main courses of events, and what
is deliberately not designed. The items follow in three sections:

- "Parts": one SOL item per part of the solution, grouped under
  plain headings when clusters emerge;
- "Across the parts": SOL items for what holds across parts, in the
  same shape;
- "Open": one TBC item per open question.

A SOL is a part of the solution, or a matter that holds across
parts. It says what the part is and what it answers for, then three
fields in this order:

- `Realises:` the IDs of the items of the layer above, never their
  wording;
- `Choice:` what was chosen, against what, and what it costs, or
  that there was no real alternative;
- `Where:` the path of what realises the part.

A TBC carries three things: its owner, what would close it, and
whether it blocks realisation.

The design restates nothing of the layer above. It cites the layer
above by ID. It copies nothing of what realises it. It names what
realises a part by path. Where a part is realised in a file of its
own, the item names the file and the detail is in that file. Where
a part is only part of a file, or no file exists yet, the item
carries the detail.

What the design is to cover is its Map, the areas Claude walks
before a design is returned or a write is offered. An area may stay
empty when it was considered and found not to apply. The areas:

- what is to be realised: the items of the layer above the design
  answers, and what of them it knowingly leaves unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole: the few ideas the solution rests on;
- the parts: what is built or done, by whom where it is not
  software, and where each is realised;
- how the parts work together, and what holds across them;
- the choices: for each real one, what it was chosen against, doing
  nothing or the least that would do among it, and what it costs;
- what is open or unproven: what would close it, and whether it
  blocks realisation;
- how it will be known to hold: by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

A check keeps the design true against what realises it.

### A worked example

One SOL item and one TBC item of a project with the placeholder
slug `<slug>`, in the shape the template gives. The project's
intent asks for a shop that always knows the state of every order.

```
## Parts

### Orders
- **SOL.0010 The order store.** One table that holds every order the
  shop has taken and the state each is in; it answers for the state
  of an order being known at any moment. Realises: POS.0210,
  POS.0220. Choice: a table in the database the shop already runs,
  against a service of its own, which would cost a second thing to
  deploy and watch; the one database is enough while one team runs
  the shop. Where: `src/orders/store.py`.

## Open
- **TBC.0010** (owner: the principal) Whether fulfilled orders are
  kept, and for how long. Closed by: the retention the principal
  sets. Blocks realisation: no.
```

The item cites the two positions of the intent it realises by their
IDs and repeats none of their wording. It names the one file where
the store is realised, and the detail of the table is that file's
to carry. The choice says what it was chosen against and what the
alternative would have cost. The open question has an owner, a way
to close it, and does not stop the building.

## Complete when

The design is complete for now when two things hold:

- every item of the layer above that is in scope is realised by a
  part, knowingly left unanswered, or open as a TBC;
- no TBC that blocks realisation is open.

It is never finished. Because it describes the solution as it
stands, it changes whenever the solution does. When the completion
is reached, Claude offers the approval as a recommendation, never as
a gate.

## How it is found

The design is iterated through `/forge solution-design`; the steps
are the page [Design the solution](../use/design-the-solution.md).
There are four ways into a pass:

- no design yet, and whether one is worth writing is the
  principal's to say;
- a layer above moved, and the pass runs on what changed;
- the thing changed below, and the design is brought current;
- a wording fix, made directly.

With every pass Claude makes a coverage map: the in-scope items of
the layer above with no part, and the parts that realise no item.
The coverage map is a tool of the pass and no part of the design.

Two instruments serve the pass. `/research <topic>` is proposed
where a choice needs outside grounding and runs on the principal's
word. `/challenge <persona> solution-design` is the independent
test of the choices, offered once the design stands and never run
on Claude's own judgement.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion and its row in the ledger's
Documents table. SOL and TBC follow the ID scheme of the forge. A
write rewrites the design for coherence and never appends; empty
sections and all template comments are deleted. Each pass ends by
naming what changed and what stays open.

## Why

The intent says what the principal wants and why, and it does not
solve. How the things wanted are realised belongs to the solution
design. The test of a sentence is whether it would still hold if
the thing were realised in a wholly different way. If it would, it
is intent. If not, it is solution. A principle the principal sets
for the solution is intent; the mechanism that honours it is
solution. What the principal wants a user to be able to do, and
what must be true when it is done, is intent; how it is done, what
it is built of, its steps and the checks it runs, is solution. The
division is by kind of content, never by who said it: an idea of
the principal's about how to build something is solution too.
Because an intent that carries the solution cannot be read as what
is wanted, and nobody can be asked for a proposal of the whole
solution over it.

The design cites the layer above by ID and restates none of its
wording. The division above keeps what is wanted in one layer and
how it is realised in another. A reason beyond that division for
citing rather than restating is not recorded.

The design holds what cannot be read off the thing itself. What
can be read off the thing is read there, so that the design names
the file and copies none of its detail. Because from the artefacts
of the chain the thing must be buildable without a look at the
finished product: the product is what is built, never a source of
its own design. How deep the chain must go for that is the
project's: the design gives the architecture, a technical
specification the detail where the one who builds needs it.

The design is read by whoever realises the solution, without the
principal in the room. So that such a reader can act on it, every
real choice carries what it was chosen against and what it costs,
every open question carries its owner and whether it blocks the
building, and a choice the principal has not judged says so at the
item. The reason for keeping the design current, beyond that it
describes the solution as it stands, is not recorded.

A design is optional. Because many projects end at the intent,
where what is wanted needs no solution written down, and a layer a
project does not have is not missing. It is worth writing where the
way is not obvious, where a choice has a price, or where two hands
would solve the same matter differently if it were not written
down.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
