---
generated: 2026-10-09
made: derived
inputs-hash: 72d31767ba2b2b45
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md
---

# About the solution design

This page explains what the solution design is, where it stands in
the chain, what it holds and why it is shaped as it is. It is for a
user who wonders whether his project needs one, for an extender who
wants to know its rules before touching them, and for an evaluator
who wants to see what the forge means by "solution". It was put
together from the definition of the solution design
(`.claude/skills/forge/states/solution-design.md`), its template
(`templates/solution-design.md`) and the positions of the forge's
own intent that give the reasons.

## What it is

The solution design is an artefact of the chain, the file
`40-solution-design.md` of a project. It says how the things wanted
are realised, as the solution stands today, and it is kept current:
its body is the present state, its history stands beside it in a
companion file, as with every versioned document of the forge.

It is read by whoever realises the solution, a person or an agent,
without the principal in the room. That reader is the measure of
the document: what he would need to ask the principal must stand in
the design.

Nothing is built in the design. It specifies; the building happens
elsewhere.

## Where it stands in the chain

The intent says what the principal wants and why, and it does not
solve. The test of a sentence is whether it would still hold if the
thing were realised in a wholly different way: if it would, it is
intent; if not, it is solution. A principle the principal sets for
the solution is intent; the mechanism that honours it is solution.
The division is by kind of content, never by who said it: an idea
of the principal's about how to build something is solution too.
The reason is that an intent which carries the solution cannot be
read as what is wanted, and nobody can be asked for a proposal of
the whole solution over it.

The solution design is derived from the lowest layer the project
has above it: the intent alone, the assignment, or a BRD, with
whatever stands above that as its input. It also reads the
project's decisions, its ledger and the intent's open threads, and
where the thing already exists, what realises it as it stands.

No layer below the intent is a condition of another. A project
takes the layers it needs, and many end at the intent, where what
is wanted needs no solution written down. A solution design is
worth writing where the way is not obvious, where a choice has a
price, or where two hands would solve the same matter differently
if it were not written down. Whether it is written, the principal
says; a project without one is not missing anything, and the state
map and the checks say nothing of it.

From the artefacts of the chain the thing must be buildable without
a look at the finished product: the product is what is built, never
a source of its own design. How deep the chain must go for that is
the project's. The solution design gives the architecture; a
technical specification is a layer below it, for the detail where
the one who builds needs it.

## What it holds

The design holds what cannot be read off the thing itself: why,
against what, at what price, and how the parts fit. Two rules keep
it from swelling:

- it restates nothing of the layer above, which it cites by ID;
- it copies nothing of what realises it, which it names by path.

Where a part is realised in a file of its own, the item names the
file and the detail is the file's. Where a part is only part of a
file, or no file exists yet, the item carries the detail.

What the design finds, in whatever order, covers these areas; an
area may stay empty when it was considered and found not to apply:

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

## The shape of the document

The template gives the document a short prose head and then items.
The head, "How the parts work together", carries the few ideas the
solution rests on, the main courses of events, and what is
deliberately not designed. Narrative stops there.

Under it come the parts, grouped under plain headings when clusters
emerge; then a section for what holds across the parts; then what
is open. A section that is empty is deleted, and so are the
template's comments. A write rewrites the document for coherence,
never appends to it.

### A part

A part is an item with the prefix SOL. It is either one part of the
solution or a matter that holds across parts. It says what the part
is and what it answers for, and then, in this order:

- **Realises:** the IDs of the layer above, never their wording;
- **Choice:** what was chosen, against what, and what it costs, or
  that there was no real alternative;
- **Where:** the path of what realises it.

The choice is written only where there was a real one. Claude names
the few real choices and does not dress every part as one: where
there was no alternative he says so and invents none, and where a
reason is not known he says it is unknown. A choice Claude made
that the principal has not yet judged says so in plain words at the
item, until he has judged it.

### An open matter

What is open is an item with the prefix TBC. It carries its owner,
what would close it, and whether it blocks realisation. Both
prefixes follow the ID scheme of `CLAUDE.md`: numbers are stable
and never reused.

## How it is worked

The design is iterated through `/forge solution-design`. How it is
composed is the principal's choice, artefact by artefact: found
together by elicitation, or handed over to Claude with a few
sentences of what is wanted. Either way Claude proposes the parts
and the choices and the principal judges them.

There are four ways into a pass:

- no design yet, and whether one is worth writing is the
  principal's to say;
- a layer above moved, and the pass runs on what changed;
- the thing changed below, and the design is brought current;
- a wording fix, made directly.

With every pass Claude makes a coverage map: the in-scope items of
the layer above that no part realises, and the parts that realise
no item. The map is a tool of the pass, not part of the design. The
pass ends by naming what changed and what stays open.

What the designing shows cannot be realised, or only at a price not
worth paying, is raised as a thread, and what is wanted is decided
in the intent first; the design follows the intent, never the other
way round.

Where a choice needs outside grounding, Claude proposes
`/research <topic>`, run on the principal's word. Once the design
stands, `/challenge <persona> solution-design` is offered as the
independent test of its choices; it is never run on Claude's own
judgement.

## When it is complete

The design is complete for now when every item of the layer above
that is in scope is realised by a part, knowingly left unanswered,
or open as a TBC, and when no TBC that blocks realisation is open.
At that point Claude offers the approval: a recommendation, never a
gate. The design is never finished, because the solution it
describes keeps changing and the document is kept current with it.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion
`40-solution-design.history.md` and its row in the ledger's
Documents table.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [About the intent](the-intent.md): the layer whose "what" this answers.
