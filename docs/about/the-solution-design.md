---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 48a291ef4e362274
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
rests on. This page says what the document holds, who it is for,
what it is made from, when it counts as complete and why it restates
nothing of the layer above it. It is for anyone who works with a
project of the forge, extends it or judges how well it keeps its own
rules.

## What it is

The solution design is one artefact of the chain, the file
`40-solution-design.md` of a project. The chain is the series of
versioned documents a project's thinking travels through, from the
brief through [The intent](the-intent.md) and downward. The design
answers the question the layers above it leave open: how.

The design describes the solution as it stands today. It is kept
current. Its body is the present state and its history stands beside
it in a companion file. It is never finished.

The design is one of the layers a project may take below the intent.
No layer below the intent is a condition of another. Many projects
end at the intent, where what is wanted needs no solution written
down. A project that has no design is not missing one: the state map
of the project and the checks say nothing of it, and the ledger (the
project's state report, made at read time) declares no end of the
chain.

The design is worth writing in three cases:

- where the way to realise what is wanted is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it were
  not written down.

Whether a project writes one is for the principal to say. The
principal is the person whose thinking is being forged.

## Who writes and reads it

The design is composed by the principal with Claude. How it is
composed is the principal's choice, artefact by artefact: found
together by questions, or handed over with a few sentences of what he
wants. Either way Claude proposes the parts and the choices, and the
principal judges them.

Claude names the few real choices and does not dress every part as
one. Where there was no real alternative, it says so and invents
none. Where a reason is not known, it says the reason is unknown.
How sure it is of a claim, it says in words. A choice Claude made and
the principal has not yet judged says so in plain words at the item,
until he has judged it.

The design is read by whoever realises the solution, a person or an
agent, without the principal in the room. It is written so that the
thing can be built from it without a look at any finished product.

Nothing is built in the design. The design specifies.

## Made from

The design is derived from the lowest layer the project has above
it: the intent alone, the assignment, or the BRD. Whatever stands
above that layer is an input too. The intent is read together with
the project's threads, the open matters kept in `threads/`.

Beside the layers above, the design reads the project's decisions
and its ledger. Where the thing already exists, what realises it is
read as it stands. Research and sources enter as the principal
directs.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion `40-solution-design.history.md`
made from `templates/history.md`. A write rewrites the document for
coherence and never appends to it. Empty sections and the template's
comments are deleted on the write.

## What it holds

The design holds what cannot be read off the thing itself:

- why a part is as it is;
- against what it was chosen;
- at what price;
- how the parts fit.

It restates nothing of the layer above, which it cites by ID. It
copies nothing of what realises it, which it names by path.

The document is made of items under a short prose head. The head,
"How the parts work together", carries the few ideas the solution
rests on, the main courses of events and what is deliberately not
designed. The items follow in three sections of the template: the
parts, what holds across the parts, and what is open.

### The shape of a SOL item

One prefix is the design's own: `SOL`, a part of the solution or a
matter that holds across parts. An item says what the part is and
what it answers for, then three fields in this order:

- `Realises:` the IDs of the layer above, never their wording;
- `Choice:` what was chosen, against what, and what it costs, or
  that there was no real alternative;
- `Where:` the path to what realises the part.

Where a part is realised in a file of its own, the item names the
file and the detail is the file's. Where the part is only part of a
file, or no file exists yet, the item carries the detail. Where a
part is done by people rather than software, the item says by whom.

Items are grouped under plain headings when clusters emerge. IDs
follow the scheme of the whole forge: stable, never renumbered,
numbered in tens.

### The shape of a TBC

What is open is a `TBC`, an open question. A TBC carries three
things: its owner, what would close it, and whether it blocks
realisation.

## Complete when

The design is complete for now when two conditions hold. Every item
of the layer above that is in scope is realised by a part, knowingly
left unanswered, or open as a TBC. No TBC that blocks realisation is
open.

When the completion is reached, Claude offers the approval. The offer
is a recommendation, never a gate. Even approved, the design stays
current with the solution and is never finished.

## How it is found

The design is iterated through its definition; the job is
[Design the solution](../use/design-the-solution.md). There are four
ways in:

- no design yet, and whether one is worth writing is the
  principal's to say;
- a layer above moved, and the pass runs on what changed;
- the thing changed below, and the design is brought current;
- a wording fix, made directly.

The definition carries a map of what the design finds, whatever the
order it is found in: what is to be realised and what is knowingly
left unanswered; the ground, that is what exists already, what stands
around it and what the principal has fixed in advance; the approach
as a whole; the parts; how the parts work together; the choices; what
is open or unproven; how it will be known to hold; the way there,
where the solution replaces something that runs; and what is
deliberately not designed. The map is walked before the design is
returned or a write is offered. An area may stay empty when it was
considered and found not to apply.

With every pass Claude makes a coverage map: the in-scope items of
the layer above that no part realises, and the parts that realise no
item. The coverage map is a tool of the pass, not part of the design.
A pass ends by naming what changed and what stays open.

Two instruments stand beside the pass. Research is proposed where a
choice needs outside grounding and runs on the principal's word. A
challenge of the design, the independent test of its choices by an
isolated reviewer, is offered once the design stands and never run on
Claude's own judgement.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first, and the design follows.

## Why

The chain divides what is wanted from how it is realised by kind of
content, never by who said it. The test of a sentence: would it
still hold if the thing were realised in a wholly different way? If
it would, it belongs to the intent. If not, it belongs to the design.
A principle the principal sets for the solution is intent; the
mechanism that honours it is solution. An idea of the principal's
about how to build something is solution too. The reason recorded is
this: an intent that carries the solution cannot be read as what is
wanted, and nobody can be asked for a proposal of the whole solution
over it. Why the design cites the layer above by ID rather than
restating it is not recorded beyond this division.

The design holds only what cannot be read off the thing itself,
because the thing itself is read where it stands. This is why a part
realised in a file of its own is named by path and its detail stays
in the file.

From the artefacts of the chain the thing must be buildable without
a look at the finished product. The product is what is built, never
a source of its own design. How deep the chain must go for that is
the project's to say: the design gives the architecture, and a
technical specification gives the detail where the one who builds
needs it.

The design is worth writing where the way is not obvious, where a
choice has a price, or where two hands would solve the same matter
differently if it were not written down. The reason it is kept
current rather than closed at approval is not recorded.

Every term of the forge used here is in one line in the
[Glossary](../reference/glossary.md).

## A worked example

A generic item of the parts section, taken from no project, with the
layer above an intent:

```markdown
### Reminders
- **SOL.0010 Weekly reminder.** Sends one reminder to every member
  whose return is overdue; answers for the reminder reaching the
  member and for no member getting it twice in one week.
  Realises: POS.0120, POS.0130. Choice: one scheduled run a week,
  against a mail at the moment each return falls overdue; the run
  keeps the mail to one per member and costs up to six days of
  delay. Where: `src/reminders/weekly.py`.
- **SOL.0020 Member list.** Reads the members and their returns from
  the register the library already keeps. Realises: POS.0120.
  Choice: no real alternative, the register is the only record of
  the members. Where: `src/reminders/members.py`.
```

A generic item of the open section:

```markdown
## Open
- **TBC.0010** (owner: the principal) Whether a member may switch
  the reminder off. Closed by: a position in the intent. Blocks
  realisation: no.
```

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
