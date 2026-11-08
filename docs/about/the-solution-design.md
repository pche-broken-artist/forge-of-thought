---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 8e9294a5bced24bf
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the artefact of the chain that says how the
things wanted are realised, part by part, with the choices each part
rests on. This page explains what the design holds, where it is
derived from, when it is complete and why it restates nothing of the
layer above it. It is for the user who writes one with Claude, the
extender who touches its definition or template, and the evaluator
who wants to know what such a document is good for. Every term of the
forge is in the [Glossary](../reference/glossary.md); how a design is
iterated is on [Design the solution](../use/design-the-solution.md).

## What it is

The solution design is a versioned artefact of the chain, the file
`40-solution-design.md` of a project. It describes the solution as
it stands today and is kept current. Its body is the present state;
its history stands beside it in a companion file.

It is made of items under a short prose head on how the parts work
together. One ID prefix is its own: `SOL`, a part of the solution or
a matter that holds across parts. What is open is a `TBC`, an open
question with an owner.

A project is not obliged to have a design. Below the intent a project
takes the layers it needs, and many end at the intent, where what is
wanted needs no solution written down. A design is worth writing in
three situations:

- where the way to realise what is wanted is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it were
  not written down.

Whether a design is written, the principal (the person whose thinking
is being forged) says. A layer a project does not have is not
missing: the state map of `/forge` and the checks say nothing of it,
and the ledger (the single source of truth for a project's state,
made at read time) declares no end of the chain.

The design gives the architecture. Where the one who builds needs
more detail, a technical specification gives it; how deep a project's
chain must go for that is the project's own matter.

## Who writes and reads it

The design is composed by the principal with Claude. How it is
composed is the principal's choice, artefact by artefact: found
together by elicitation, or handed over to Claude with a few
sentences of what is wanted. Either way Claude proposes the parts and
the choices, and the principal judges them.

Claude names the few real choices and does not dress every part as
one. Where there was no real alternative it says so and invents none.
Where a reason is not known it says the reason is unknown. How sure it
is of a claim it says in words. A choice Claude made and the principal
has not yet judged says so in plain words at the item, until he has
judged it.

The design is read by whoever realises the solution, a person or an
agent, without the principal in the room. The reason for this
audience is not recorded.

Nothing is built in the design: the design specifies.

## Made from

The design is derived from the lowest layer the project has above
it. That layer is one of four:

- the intent alone;
- the assignment;
- the BRD;
- the user stories.

Whatever stands above that layer is an input as well. The intent is
read together with the project's threads, the open matters kept one
file each in `threads/`. The decisions file and the ledger are read
too. Where the thing already exists, what realises it is read as it
stands. Research and sources enter as the principal directs.

No layer below the intent is a condition of another. The number in
the file name orders the files and prescribes no sequence.

The design cites the layer above it and never the reverse: an item of
the design names the stories, business requirements or positions it
realises, and no story cites a part of the design. What the user
stories are is on [The user stories](the-user-stories.md); what the
intent is, the layer whose "what" the design answers, is on
[The intent](the-intent.md).

## What it holds

The design holds what cannot be read off the thing itself:

- why a part is as it is;
- against what it was chosen;
- at what price;
- how the parts fit.

It restates nothing of the layer above, which it cites by ID. It
copies nothing of what realises it, which it names by path. The
reason it cites rather than restates is not recorded.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion `40-solution-design.history.md`
made from `templates/history.md`. The template gives it this
structure:

- a header with `version`, `status`, `project` and the audience,
  whoever realises the solution;
- **How the parts work together**: short prose on the few ideas the
  solution rests on, the main courses of events, and what is
  deliberately not designed;
- **Parts**: the `SOL` items, grouped under plain headings when
  clusters emerge;
- **Across the parts**: `SOL` items for what holds across parts, in
  the same shape;
- **Open**: the `TBC` items.

A write rewrites the design for coherence and never appends. Empty
sections and every comment of the template are deleted.

### The shape of a SOL item

A `SOL` item is a part of the solution, or a matter that holds across
parts. It says what the part is and what it answers for, then three
fields in this order:

- `Realises:` the IDs of the layer above, never their wording;
- `Choice:` what was chosen, against what, and what it costs, or that
  there was no real alternative;
- `Where:` the path where the part is realised.

Where a part is realised in a file of its own, the item names the
file and the detail is left to the file. Where the part is only part
of a file, or no file exists yet, the item carries the detail. This
follows from a rule of the chain: from the artefacts of the chain the
thing must be buildable without a look at the finished product,
because the product is what is built and never a source of its own
design.

### The shape of a TBC

A `TBC` is an open or unproven matter. It carries its owner, what
would close it, and whether it blocks realisation.

### A worked example

A generic item, in the shape the template gives, taken from no
project:

```
### Storage
- **SOL.0010 The record store.** Keeps every record of a run as one
  file, named by date and topic, so that a run can be read back
  without the tool that made it.
  Realises: POS.0120, POS.0340. Choice: plain files in one folder,
  against a database; costs a slower search over many runs.
  Where: `scripts/store.py`.
```

And a generic open matter:

```
## Open
- **TBC.0010** (owner: the principal) Whether old records are
  archived or deleted. Closed by: a decision on how long a run must
  stay readable. Blocks realisation: no.
```

## Complete when

The design is complete for now when two things hold:

- every item of the layer above that is in scope is realised by a
  part, knowingly left unanswered, or open as a `TBC`;
- no `TBC` that blocks realisation is open.

It is never finished. It describes the solution as it stands and
moves with it, as the intent does.

When the completion is reached, Claude offers the approval as a
recommendation, never as a gate.

## How it is found

The design is found through `/forge solution-design`, the command
that iterates an artefact through its definition. How a session of it
runs is on [Design the solution](../use/design-the-solution.md); what
follows is what the definition asks the conversation to cover.

There are four ways into a pass:

- no design yet, and whether one is worth writing is the principal's
  to say;
- a layer above moved, and the pass runs on what changed;
- the thing changed below, and the design is brought current;
- a wording fix, made directly.

Whatever the order, the design's definition walks ten areas before
the design is returned or a write is offered; an area may stay empty
when it was considered and found not to apply:

- what is to be realised: the items of the layer above, and what of
  them the design knowingly leaves unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole: the few ideas the solution rests on;
- the parts: what is built or done, by whom where it is not software,
  and where each is realised;
- how the parts work together, and what holds across them;
- the choices: for each real one, what it was chosen against, doing
  nothing or the least that would do among the alternatives, and
  what it costs;
- what is open or unproven: what would close it, and whether it
  blocks realisation;
- how it will be known to hold: by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

With every pass Claude makes a coverage map: the in-scope items of
the layer above that no part realises, and the parts that realise no
item. The coverage map is a tool of the pass, not part of the design.
A pass ends by naming what changed and what stays open.

Two instruments stand beside the conversation. `/research <topic>` is
proposed where a choice needs outside grounding and runs on the
principal's word. `/challenge <persona> solution-design` is the
independent test of the choices, offered once the design stands and
never run on Claude's own judgement.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first; the design follows.

## Why

An intent says what the principal wants and why, and it does not
solve. What he wants, what he does not want, what is the case, what
is open and what he dropped belong to the intent. How the things he
wants are realised belongs to the solution design.

The reason is recorded: an intent that carries the solution cannot be
read as what is wanted, and nobody can be asked for a proposal of the
whole solution over it.

The division is by kind of content, never by who said it. An idea of
the principal's about how to build something is solution too. Three
pairs show the line:

- a principle the principal sets for the solution, what the
  realisation must respect whatever its shape, is intent; the
  mechanism that honours it is solution;
- what the principal wants the user to be able to do, and what must
  be true when it is done, is intent, a command he asks for by name
  among it; how the command does it, what it is built of, its steps
  and their order and the checks it runs, is solution;
- what is wanted is in the intent; how it is realised is in the
  design.

The test of a sentence decides where it belongs: would it still hold
if the thing were realised in a wholly different way? If it would, it
is intent. If not, it is solution.

Why the design is kept current rather than frozen at a version, and
why it is written for a reader without the principal in the room, the
inputs do not say: the reasons are not recorded.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [The user stories](the-user-stories.md): the stories, which a
  design cites and never the reverse.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
