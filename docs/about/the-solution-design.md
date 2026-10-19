---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: c720acbede4a4879
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the document of a project that says how the
things wanted are realised. This page explains what it holds, who
reads it, what it is made from and why it restates nothing of the
layer above it. It is for anyone who uses the forge, extends it or
weighs whether it fits their work.

## What it is

The solution design is an artefact of the chain, the file
`40-solution-design.md` of a project. An artefact is a versioned
document of the chain; the chain is the sequence of documents a
thought travels, from a brief through the intent to the layers below
it (see the [Glossary](../reference/glossary.md)). The
[intent](the-intent.md) says what the principal wants and why. The
principal is the person whose thinking is forged, with the final
word on all content. The solution design answers that "what" with a
"how".

It describes the solution as it stands today and is kept current.
Its body is the present state. Its history stands beside it in a
companion file, `40-solution-design.history.md`. It is never
finished: it changes when the layer above changes and when the thing
it describes changes.

A project does not need one. A project takes the layers it needs,
and many end at the intent, where what is wanted needs no solution
written down. A layer a project does not have is not missing: the
state map and the checks say nothing of it. Whether a solution
design is written at all, the principal says.

## Who writes and reads it

The principal and Claude write it together, or the principal hands
it over and Claude works it alone and returns a proposal. Either
way, Claude proposes the parts and the choices, and the principal
judges them. A choice Claude made that the principal has not yet
judged says so in plain words at its item until he has judged it.

It is read by whoever realises the solution, a person or an agent,
without the principal in the room. Its template names that reader as
its audience.

Nothing is built in it. The design specifies; others build.

## Made from

It is derived from the lowest layer the project has above it. That
is one of these:

- the intent alone
- the assignment
- the BRD

Whatever stands above that layer is its input too. Beside these it
reads the project's decisions and state, and the intent's open
threads. Where the thing already exists, what realises it is read as
it stands. Research and sources come in as the principal directs.

## What it holds

It holds what cannot be read off the thing itself:

- why
- against what
- at what price
- how the parts fit

It opens with a short prose head on how the parts work together: the
few ideas the solution rests on, the main courses of events, and
what is deliberately not designed. Under it stand items, each with a
stable ID.

A **SOL** item is a part of the solution, or a matter that holds
across parts. It says what the part is and what it answers for. Then
it gives, in this order:

- `Realises:` the IDs of the items of the layer above that it
  realises, never their wording
- `Choice:` what was chosen, against what, and what it costs, or
  that there was no real alternative
- `Where:` the path of what realises it

Where a part is realised in a file of its own, the item names the
file and the detail belongs to the file. Where the part is only part
of a file, or no file exists yet, the item carries the detail.

Only the real choices are dressed as choices. Where there was no
real alternative, the item says so and invents none. Where a reason
is not known, the item says it is unknown.

A **TBC** item is a matter still open. It carries its owner, what
would close it, and whether it blocks realisation.

The template groups the items under these headings:

- "How the parts work together" (the prose head)
- "Parts" (SOL items, grouped under plain headings when clusters
  emerge)
- "Across the parts" (SOL items for what holds across parts)
- "Open" (TBC items)

A section with nothing in it is deleted, and so is every comment of
the template.

## Complete when

The design is complete for now when two things hold. Every item of
the layer above that is in scope is realised by a part, knowingly
left unanswered, or open as a TBC. No TBC that blocks realisation is
open.

When that is reached, Claude offers the approval as a
recommendation, never as a gate. The design stays never finished
after it.

## How it is found

The design is found in conversation over the layer above, through
its definition, the file that says how an artefact is found and
owns its rules (`.claude/skills/forge/states/solution-design.md`).
What the person does to iterate it is on the page
[Design the solution](../use/design-the-solution.md).

A pass begins in one of four situations:

- there is no design yet, and whether one is worth writing is the
  principal's decision
- a layer above has moved, and the pass works on what changed
- the thing below has changed, and the design is brought current
- a wording needs fixing, and it is fixed directly

With every pass Claude draws up a coverage map. It lists the in-scope
items of the layer above that no part realises, and the parts that
realise no item. The coverage map is a tool of the pass, not part of
the design.

The definition's Map names what the design looks for, in any order:

- what is to be realised, and what of it is knowingly left
  unanswered
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance
- the approach as a whole
- the parts, by whom where a part is not software, and where each is
  realised
- how the parts work together, and what holds across them
- the real choices, each with what it was chosen against (doing
  nothing or the least that would do among it) and what it costs
- what is open or unproven, what would close it, and whether it
  blocks realisation
- how it will be known to hold, by comparing the thing with the
  design
- the way there, where the solution replaces something that runs
- what is deliberately not designed and left to the file or to the
  one who realises

An area may stay empty when it was considered and found not to
apply.

Where designing shows that something cannot be realised, or only at
a price not worth paying, Claude raises it as an open thread. What
is wanted is then decided in the intent first, and the design
follows.

## Why

The intent and the solution design are kept apart because an intent
that carries the solution cannot be read as what is wanted. Nobody
could then be asked for a proposal of the whole solution over it.
The test of a sentence is whether it would still hold if the thing
were realised in a wholly different way. If it would, it is intent.
If not, it is solution. The division is by kind of content, never by
who said it: an idea of the principal's about how to build something
is solution too.

The design is worth writing where the way is not obvious, where a
choice has a price, or where two hands would solve the same matter
differently if it were not written down.

It holds what cannot be read off the thing itself because the thing
must be buildable from the artefacts of the chain without a look at
the finished product. The product is what is built, never a source
of its own design. For the same reason the design names what
realises a part by its path and copies nothing of it.

It cites the items of the layer above by their IDs and never
restates them. The reason for not restating them is not recorded.

How deep the chain must go for the thing to be buildable belongs to
the project. The solution design gives the architecture. A technical
specification gives the detail where the one who builds needs it.

## A worked example

One generic SOL item, in the shape the template defines. It comes
from no project, and its IDs are placeholders as the template has
them.

```markdown
### Intake
- **SOL.NNNN Upload form.** A web form through which a member sends
  a document for review; it answers for getting the document in
  without an e-mail. Realises: POS.NNNN, POS.NNNN. Choice: a form
  on the existing site, chosen against a shared folder, which needs
  no build but loses who sent what; costs one page to maintain.
  Where: `site/upload.html`.
```

The item names its part and what it answers for. It cites the
intent's items by ID only. It states the one real choice with what
it was chosen against and its price. It points to the file that
realises it, which holds the detail.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
