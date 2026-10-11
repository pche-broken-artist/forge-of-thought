---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 943e9e9b6f5d67f1
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the artefact of the chain that says how the
things wanted are realised, as the solution stands today. This page
says what it is, who writes and reads it, what it is made from, what
it holds, when it is complete and why it is shaped as it is. It is
for anyone who meets the file `40-solution-design.md` in a project:
the one who iterates it with Claude, the one who builds from it, and
the one who judges whether it does its job. How it is iterated is
the page [Design the solution](../use/design-the-solution.md); every
term of the forge is in the [Glossary](../reference/glossary.md).

## What it is

The solution design is one layer of a project's chain, the file
`40-solution-design.md`. It describes the solution as it stands and
is kept current. Its body is the present state; its history stands
beside it in a companion file.

It is made of items under a short prose head on how the parts work
together. One ID prefix is its own: `SOL`, a part of the solution or
a matter that holds across parts. What is open is a `TBC` with its
owner.

The layer whose "what" the design answers is the layer above it,
most often the intent (the page [The intent](the-intent.md)). The
division between the two is by kind of content, never by who said
it. The intent says what the principal wants and why; the principal
is the person whose thinking is being forged. The design says how
it is realised. The test of a sentence: would it still hold if the
thing were realised in a wholly different way? If it would, it is
intent; if not, it is solution. A principle the principal sets for
the solution, what the realisation must respect whatever its shape,
is intent; the mechanism that honours it is solution. What the
principal wants a user to be able to do is intent; how a command
does it, what it is built of, its steps and the checks it runs, is
solution. An idea of the principal's about how to build something
is solution too.

Not every project has a solution design. A project takes the layers
it needs, and many end at the intent, where what is wanted needs no
solution written down. The design is worth writing where the way is
not obvious, where a choice has a price, or where two hands would
solve the same matter differently if it were not written down.
Whether it is written, the principal says. A layer a project does
not have is not missing: the state map and the checks say nothing
of it, and the ledger (the file that holds the project's state)
declares no end of the chain.

## Who writes and reads it

The principal writes it with Claude. How the two compose it is the
principal's choice: found together by elicitation, or handed over
with a few sentences of what he wants. Either way Claude proposes
the parts and the choices, and the principal judges them. Claude
names the few real choices and does not dress every part as one.
Where there was no real alternative it says so and invents none.
Where a reason is not known it says the reason is unknown. How sure
it is of a claim it says in words. A choice Claude made and the
principal has not yet judged says so in plain words at the item,
until he has judged it.

The design is read by whoever realises the solution, a person or an
agent, without the principal in the room. Nothing is built in the
forge: the design specifies.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first, and the design follows.

## Made from

The design is derived from the lowest layer the project has above
it: the intent alone, the assignment or the BRD. Whatever stands
above that layer is an input as well. The intent is read with the
project's threads, the file `threads.md`. The project's decisions
and its ledger are read too. Where the thing already exists, what
realises it is read as it stands. Research and sources enter as the
principal directs.

## What it holds

The design holds what cannot be read off the thing itself: why,
against what, at what price, and how the parts fit. It restates
nothing of the layer above, which it cites by ID. It copies nothing
of what realises it, which it names by path.

Its shape is owned by `templates/solution-design.md`. Under the
front-matter and the title stand these sections:

- How the parts work together: short prose on the few ideas the
  solution rests on, the main courses of events, and what is
  deliberately not designed.
- Parts: the `SOL` items, grouped under plain headings when clusters
  emerge.
- Across the parts: `SOL` items for what holds across parts, in the
  same shape.
- Open: the `TBC` items.

A `SOL` item says what the part is and what it answers for, then in
this order:

- `Realises:` the IDs of the layer above, never their wording.
- `Choice:` what was chosen, against what, and what it costs; or
  that there was no real alternative.
- `Where:` the path.

Where a part is realised in a file of its own, the item names the
file and the detail is the file's. Where it is only part of a file,
or no file exists yet, the item carries the detail.

A `TBC` carries its owner, what would close it, and whether it
blocks realisation.

The ground the design covers, whatever the order it is found in, is
the Map of its definition (the file
`.claude/skills/forge/states/solution-design.md`):

- what is to be realised, and what of it is knowingly left
  unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole;
- the parts, by whom where it is not software, and where each is
  realised;
- how the parts work together, and what holds across them;
- the choices, each against what it was chosen against, doing
  nothing or the least that would do among it, and what it costs;
- what is open or unproven, what would close it, and whether it
  blocks realisation;
- how it will be known to hold: by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

An area may stay empty when it was considered and found not to
apply. Empty sections and the template's comments are deleted on
write.

## Complete when

The design is complete for now when every item of the layer above
that is in scope is realised by a part, knowingly left unanswered,
or open as a `TBC`, and when no `TBC` that blocks realisation is
open. It is never finished: it is kept current, as the intent is.
When that completion is reached, Claude offers the approval, as a
recommendation and never a gate.

## How it is found

The design is found through its definition. There are four ways in:
no design yet, and whether one is worth writing is the principal's
to say; a layer above that moved, and the pass runs on what changed;
the thing changed below, and the design is brought current; a
wording fix, made directly.

With every pass Claude makes a coverage map: the in-scope items of
the layer above with no part, and the parts that realise no item.
That map is a tool of the pass, not part of the design. A pass ends
by naming what changed and what stays open.

Two instruments stand beside the pass, both on the principal's word
and never on Claude's own judgement. Research is proposed where a
choice needs outside grounding. A challenger is offered once the
design stands, as the independent test of the choices.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion
`40-solution-design.history.md` and its row in the ledger. A write
rewrites the design for coherence and never appends to it.

## Why

The intent and the design are divided because an intent that
carries the solution cannot be read as what is wanted, and because
nobody can be asked for a proposal of the whole solution over it.

The design holds why, against what, at what price and how the parts
fit because these are what cannot be read off the thing itself. The
reason it cites the layer above by ID rather than restating it is
not recorded.

From the artefacts of the chain the thing must be buildable without
a look at the finished product. The product is what is built, never
a source of its own design. How deep the chain must go for that is
the project's: the solution design gives the architecture, and a
technical specification the detail where the one who builds needs
it.

The design is read without the principal in the room. So it says in
words how sure a claim is, says where a reason is unknown, and marks
a choice the principal has not yet judged. The reason the few real
choices are named and the rest are not dressed as choices is not
recorded beyond that rule.

## A worked example

One `SOL` item of a generic project, in the shape the template
gives. The project is a placeholder; the IDs under `Realises:` point
to the positions of its intent.

```
### Reporting

- **SOL.0010 Nightly export.** A job that writes the day's orders to
  one file the finance team reads each morning. It answers for the
  file being complete for the day and present before the team
  starts. Realises: POS.0120, POS.0130. Choice: a scheduled job once
  a night, against an export on demand; it costs up to one day of
  delay for an order placed after the run. Where:
  `scripts/export-orders.py`.
```

The item says what the part is and what it answers for. It cites
the positions it realises by ID and does not repeat their wording.
It names the one real choice, what it was chosen against and what it
costs. It names the file where the part lives, and the detail of the
job is that file's, not the item's.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
