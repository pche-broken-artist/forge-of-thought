---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 7d28bfb3f94f10c5
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the document of the chain that says how the
things wanted are realised. This page is for anyone who uses,
extends or evaluates the forge. It explains what a solution design
holds, who it is for, when one is worth writing and why it restates
nothing of the layer above it.

## What it is

The solution design is an artefact of the chain, the file
`40-solution-design.md` of a project. An artefact is one versioned
document of the chain of documents a thought travels. The solution
design says how the things wanted are realised, as the solution
stands today. It is kept current: its body is the present state, and
its history stands beside it in a companion file.

It answers the "what" of the layer above it. The intent says what the
principal wants and why, and it does not solve. The principal is the
person whose thinking is being forged. How the things he wants are
realised belongs to the solution design (see
[The intent](the-intent.md)).

A simple test divides the two. Would a sentence still hold if the
thing were realised in a wholly different way? If it would, it is
intent. If not, it is solution. The division is by kind of content,
never by who said it. An idea of the principal's about how to build
something is solution too.

Nothing is built in the solution design. It specifies.

## Who writes and reads it

The principal and Claude write it. How it is composed is the
principal's choice: found together by questions, or handed over to
Claude with a few sentences of what he wants. Either way Claude
proposes the parts and the choices, and the principal judges them.

Claude names the few real choices and does not dress every part as
one. Where there was no real alternative, it says so and invents
none. Where a reason is not known, it says so. A choice Claude made
that the principal has not judged yet says so in plain words at the
item, until he has judged it.

It is read by whoever realises the solution, a person or an agent.
That reader works without the principal in the room.

## Made from

The solution design is derived from the lowest layer the project has
above it. That is one of these:

- the intent alone;
- the assignment;
- the BRD.

Whatever stands above that layer is its input too. Beside them it
reads:

- the decisions of the project;
- the ledger, the state of the project made at read time;
- the threads of the intent, that is, its open matters;
- what already realises the thing, where the thing exists;
- research and sources, as the principal directs.

No layer below the intent is a condition of another. A project takes
the layers it needs, and many end at the intent, where what is
wanted needs no solution written down. A project without a solution
design is not missing one.

## What it holds

It holds what cannot be read off the thing itself:

- why;
- against what;
- at what price;
- how the parts fit.

It restates nothing of the layer above: it cites those items by
their IDs. It copies nothing of what realises it: it names those
files by path.

The document has a short prose head and items under it, in these
sections:

- **How the parts work together:** the few ideas the solution rests
  on, the main courses of events, and what is deliberately not
  designed.
- **Parts:** one item per part, grouped under plain headings when
  clusters emerge.
- **Across the parts:** items for what holds across parts, in the
  same shape.
- **Open:** the questions still to be confirmed.

A section with nothing in it is deleted.

### The shape of a part

One prefix is the solution design's own: SOL. A SOL item is a part
of the solution, or a matter that holds across parts. It says what
the part is and what it answers for. Then, in this order:

- `Realises:` the IDs of the layer above that the part answers,
  never their wording;
- `Choice:` what was chosen, against what, and what it costs, or
  that there was no real alternative;
- `Where:` the path where the part is realised.

Where a part is realised in a file of its own, the item names the
file. The detail is then the file's. Where the part is only part of
a file, or no file exists yet, the item carries the detail itself.

### The shape of an open question

What is open is a TBC item, that is, a question to be confirmed. It
carries:

- its owner;
- what would close it;
- whether it blocks realisation.

### A worked example

A generic part, in the shape the template gives:

```markdown
### Reporting
- **SOL.0010 Weekly export.** A scheduled job that writes the week's
  figures to one file for the team that reviews them.
  Realises: POS.NNNN, POS.NNNN. Choice: a file over a live
  dashboard, at the cost of figures a week old. Where:
  `<path>`.
```

And an open question beside it:

```markdown
## Open
- **TBC.0010** (owner: <who>) Which day the week closes on.
  Closed by: <what>. Blocks realisation: no.
```

## Complete when

It is complete for now when every item of the layer above that is in
scope is one of these:

- realised by a part;
- knowingly left unanswered;
- open as a TBC.

No TBC that blocks realisation may be open. A solution design is
never finished. When it is complete for now, Claude offers the
approval as a recommendation, never as a gate.

## How it is found

The design is iterated through its definition, by
`/forge solution-design` (see
[Design the solution](../use/design-the-solution.md)). Before the
design is returned or a write is offered, Claude walks over what the
design must find, in any order:

- what is to be realised, and what of it is knowingly left
  unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole;
- the parts, by whom where they are not software, and where each is
  realised;
- how the parts work together, and what holds across them;
- the choices: for each real one, what it was chosen against (doing
  nothing or the least that would do among them) and what it costs;
- what is open or unproven, what would close it, and whether it
  blocks realisation;
- how it will be known to hold, by comparing the thing with the
  design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

An area may stay empty when it was considered and found not to apply.

With every pass Claude makes a coverage map. It lists the in-scope
items of the layer above with no part, and the parts that realise no
item. The coverage map is a tool of the pass, not part of the design.

The ways into a pass are these:

- no design yet: whether one is worth writing is the principal's to
  say;
- a layer above moved: the pass runs on what changed;
- the thing changed below: the design is brought current;
- a wording fix: made directly.

Where a choice needs outside grounding, Claude proposes a research,
run on the principal's word. Once the design stands, Claude offers a
challenge of its choices by an isolated reviewer, never run on its
own judgement.

Where the designing shows that something cannot be realised, or only
at a price not worth paying, Claude raises it as a thread. What is
wanted is then decided in the intent first.

The first design is created from `templates/solution-design.md` as
version 0.1, with its history companion. A write rewrites the
document for coherence, never appends.

## Why

The solution design is a document of its own because an intent that
carries the solution cannot be read as what is wanted. Nobody could
then be asked for a proposal of the whole solution over it.

It is worth writing only in some cases:

- where the way is not obvious;
- where a choice has a price;
- where two hands would solve the same matter differently if it were
  not written down.

Whether it is written is the principal's to say.

The thing must be buildable from the artefacts of the chain without
a look at the finished product. The product is what is built, never
a source of its own design. How deep the chain must go for that is
the project's to say. The solution design gives the architecture. A
technical specification gives the detail, where the one who builds
needs it.

Why the design holds only what cannot be read off the thing, and
cites the layer above instead of restating it, is not recorded
beyond this.

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
