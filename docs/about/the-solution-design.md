---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: eb8b9a8f3cb2cad2
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
writes and reads it, what it is made from and why it restates
nothing of the layer above it. It is for the user who asks whether a
project needs one, for the extender who meets its shape, and for the
evaluator who asks what the design rests on.

## What it is

The solution design is one artefact of the
[chain](../reference/glossary.md), the row of versioned documents a
project's thinking travels. Its file is `40-solution-design.md`, a
layer below [the intent](the-intent.md). It describes the solution
as it stands today and is kept current, as the intent is: its body
is the present state, and its history stands beside it in a
companion file. It is never finished.

Not every project has one. A project takes the layers it needs, and
many end at the intent, where what is wanted needs no solution
written down. A solution design is worth writing in three cases:

- where the way is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it were
  not written down.

Whether it is written, the principal says. The principal is the
person whose thinking is forged. A layer a project does not have is
not missing: the state map (`/forge`) and the checks say nothing of
it, and the ledger declares no end of the chain. The ledger is the
project's state report, made at read time from its documents.

The design gives the architecture. Where the one who builds needs
more detail, a technical specification gives it. How deep the chain
must go for that is for the project to decide.

## Who writes and reads it

The principal and Claude compose it. How it is composed is the
principal's choice, artefact by artefact: found together by
questions, or handed over with a few sentences of what he wants.
Either way Claude proposes the parts and the choices, and the
principal judges them. Claude names the few real choices and does
not dress every part as one: where there was no real alternative it
says so and invents none, and where a reason is not known it says
the reason is unknown. How sure it is of a claim, it says in words.
A choice Claude made and the principal has not yet judged says so in
plain words at the item, until he has judged it.

The design is read by whoever realises the solution, a person or an
agent, without the principal in the room. Nothing is built in the
forge: the design specifies.

## Made from

The design is derived from the lowest layer the project has above
it, and whatever stands above that layer is its input too. The
lowest layer may be:

- the intent alone;
- the assignment;
- the BRD;
- [the user stories](the-user-stories.md), which a design cites and
  never the reverse.

Beside the layer above, the design reads the project's decisions and
the ledger. The intent is read with the project's threads, the open
matters of the intent, one file each. Where the thing already
exists, what realises it is read as it stands. Research and sources
enter as the principal directs.

From the artefacts of the chain the thing must be buildable without
a look at the finished product: the product is what is built, never
a source of its own design.

## What it holds

The design opens with a short prose head on how the parts work
together: the few ideas the solution rests on, the main courses of
events, and what is deliberately not designed. Below the head it is
made of items.

The sections of the file, as the template gives them, are:

- Parts: one SOL item per part of the solution, grouped under plain
  headings when clusters emerge;
- Across the parts: SOL items for what holds across parts, in the
  same shape;
- Open: one TBC item per open matter.

A SOL item is a part of the solution, or a matter that holds across
parts. It says what the part is and what it answers for, then three
fields in this order:

- `Realises:` the IDs of the items of the layer above, never their
  wording;
- `Choice:` what was chosen, against what, and what it costs; or
  that there was no real alternative;
- `Where:` the path of what realises the part.

Where a part is realised in a file of its own, the item names the
file, and the detail belongs to the file. Where the part is only part
of a file, or no file exists yet, the item carries the detail.

A TBC item carries its owner, what would close it, and whether it
blocks realisation.

The design restates nothing of the layer above, which it cites by
ID. It copies nothing of what realises it, which it names by path.
What it holds is what cannot be read off the thing itself: why,
against what, at what price, and how the parts fit.

The line between the intent and the design runs by kind of content,
never by who said it. The test of a sentence: would it still hold if
the thing were realised in a wholly different way? If it would, it
is intent. If it would not, it is solution. A principle the
principal sets for the solution is intent; the mechanism that
honours it is solution. What the principal wants the user to be able
to do is intent, a command he asks for by name among it. How the
command does it, what it is built of, its steps and the checks it
runs, is solution. An idea of the principal's about how to build
something is solution too.

The areas the design covers, whatever the order it finds them, are:

- what is to be realised, and what of it is knowingly left
  unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole;
- the parts, by whom where a part is not software, and where each is
  realised;
- how the parts work together, and what holds across them;
- the choices: what each was chosen against, doing nothing or the
  least that would do among it, and what it costs;
- what is open or unproven, what would close it, and whether it
  blocks realisation;
- how it will be known to hold, by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

An area may stay empty when it was considered and found not to
apply.

## Complete when

The design is complete for now when two things hold:

- every item of the layer above that is in scope is realised by a
  part, knowingly left unanswered, or open as a TBC;
- no TBC that blocks realisation is open.

Complete for now is not finished: the design is kept current for as
long as the solution stands. When completion is reached, Claude
offers the approval as a recommendation, never as a gate.

## How it is found

The design is iterated through `/forge solution-design`; how a pass
runs is the page [Design the solution](../use/design-the-solution.md).
There are four ways in:

- no design yet, and whether one is worth writing is for the
  principal to say;
- a layer above has moved, and the pass runs on what changed;
- the thing has changed below, and the design is brought current;
- a wording fix, made directly.

With every pass Claude makes a coverage map: the in-scope items of
the layer above that no part realises, and the parts that realise no
item. The coverage map is a tool of the pass, not part of the
design. Two instruments stand beside it. Research is proposed where
a choice needs outside grounding and runs on the principal's word. A
challenge of the design, the independent test of its choices by an
isolated reviewer, is offered once the design stands and is never
run on Claude's own judgement.

What the designing shows cannot be realised, or only at a price not
worth paying, Claude raises as a thread. What is wanted is then
decided in the intent first, and the design follows.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion from `templates/history.md`.
SOL and TBC follow the ID scheme of the forge. A write rewrites the
design for coherence and never appends; empty sections and the
template's comments are deleted.

## Why

The intent says what the principal wants and why; it does not solve.
How the things he wants are realised belongs to the solution design.
The reason is recorded: an intent that carries the solution cannot
be read as what is wanted, and nobody can be asked for a proposal of
the whole solution over it.

The design cites the layer above by ID rather than restating it. The
reason for citing instead of restating is not recorded.

The design holds why, against what, at what price, and how the parts
fit, because these are what cannot be read off the thing itself.
Everything that can be read off the thing is left to the file, and
the item names the file by path. The reason for naming rather than
copying is not recorded.

The design is read without the principal in the room. The reason is
not recorded.

A design is worth writing only where the way is not obvious, where a
choice has a price, or where two hands would solve the same matter
differently. Where none of these holds, what is wanted needs no
solution written down, and the project ends at the intent.

## A worked example

A generic item of a design, in the shape the template gives. The
project is invented; the IDs in `Realises:` are those of its own
intent.

```
### Storage
- **SOL.0010 Nightly export.** A scheduled job that writes the
  day's records to one file per day and answers for nothing being
  lost between two runs. Realises: POS.0120, POS.0130. Choice: a
  nightly batch, against a change feed, at the cost of a day's
  delay; the feed would need a service the project does not run.
  Where: `jobs/export.md`.
- **SOL.0020 File naming.** One file per day, named by its date.
  Realises: POS.0130. Choice: no real alternative. Where:
  `jobs/export.md`.
```

The first item records a real choice, with what it was chosen
against and what it costs. The second says there was no real
alternative and invents none. Both cite the intent by ID and never
restate its wording, and both name the file that carries the detail.

An open matter of the same design:

```
## Open
- **TBC.0010** (owner: the principal) Which time zone dates the
  file. Closed by: a decision in the intent. Blocks realisation:
  no.
```

## See also

- [Design the solution](../use/design-the-solution.md): iterating
  it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [The user stories](the-user-stories.md): the stories, which a
  design cites and never the reverse.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
