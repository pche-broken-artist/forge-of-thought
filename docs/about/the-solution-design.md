---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 1a617078fe2f541f
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.1420
---

# The solution design

The solution design is the document of a project that says how the
things wanted are realised. This page explains what it holds, what it
is made from, who writes and reads it, and why it solves where the
intent does not and restates nothing of the layer above it. It is for
whoever uses the forge, extends it or evaluates it.

## What it is

The solution design is an
[artefact of the chain](../reference/glossary.md): the file
`40-solution-design.md` of a project. It says how the things wanted
are realised, as the solution stands today. What is wanted stands
above it: in the [intent](the-intent.md), and in the layers a project
has between the intent and the design.

The design is kept current, as the intent is. Its body is the present
state, and its history stands beside it in
`40-solution-design.history.md`. Nothing is built in the design: it
specifies.

Not every project has a solution design. No layer below the intent is
a condition of another. A project takes the layers it needs, and many
projects end at the intent, where what is wanted needs no solution
written down. A design is worth writing where one of these holds:

- the way is not obvious;
- a choice has a price;
- two hands would solve the same matter differently if it were not
  written down.

Whether a design is worth writing is for the principal to say (the
principal is the person whose thinking is being forged). A layer a
project does not have is not missing. The command `/forge` and the
checks say nothing of it, and the ledger (the file that holds the
state of the project) declares no end of the chain. The number in the
file name orders the files and prescribes no sequence.

## Who writes and reads it

Claude proposes the parts and the choices, and the principal judges
them. That holds however the design is composed, and how it is
composed is the principal's choice. In proposing, Claude keeps to
this:

- It names the few real choices and does not dress every part as one.
- Where there was no real alternative, it says so and invents none.
- Where a reason is not known, it says that the reason is unknown.
- It says in words how sure it is of a claim.

A choice that Claude made and the principal has not yet judged says so
in plain words at its item, until the principal has judged it.

The design is read by whoever realises the solution (a person or an
agent), without the principal in the room. Why the design is written
for this reader: the reason is not recorded.

## Made from

The design is derived from the lowest layer the project has above it.
That layer is one of these:

- the intent alone;
- the [assignment](../reference/glossary.md);
- the [BRD](../reference/glossary.md);
- the [user stories](the-user-stories.md).

Whatever stands above that layer is an input as well. Beside the
layers, these are read:

- the decisions of the project (`decisions.md`) and its ledger;
- the [threads](../reference/glossary.md) of the project (`threads/`),
  together with the intent;
- what realises the thing, as it stands, where the thing already
  exists;
- research and sources, as the principal directs.

The shape of the file comes from the template
`templates/solution-design.md` (a template is the skeleton a new file
is made from).

## What it holds

The design holds what is designed, whole enough that the thing can be
built from it without a look at what realises it. It says what each
part does, why, against what it was chosen and at what price, and how
the parts fit. It restates nothing of the layer above: it cites that
layer by ID. It names what realises a part by path.

```text
the lowest layer the project has above the design
(the intent alone, the assignment, the BRD or the user stories)
        |
        |  the design cites it by ID and never restates it
        v
40-solution-design.md
(what is designed, whole enough to build from)
        |
        |  the design names them by path
        v
the files that realise the parts
(may repeat the design, are never its only place)
```

The file is a header and four sections:

- the header: the version, the status (`draft`, `approved` or
  `superseded`), the project and the audience;
- "How the parts work together": short prose on the few ideas the
  solution rests on, the main courses of events and what is
  deliberately not designed;
- "Parts": the items of the design, grouped under plain headings when
  clusters emerge;
- "Across the parts": items of the same shape for what holds across
  parts, left out when empty;
- "Open": what is open, left out when empty.

The design is made of two kinds of item.

A SOL item is a part of the solution, or a matter that holds across
parts. SOL is the one prefix that belongs to the design alone. The
item says what the part is and what it answers for, and then, in this
order:

- `Realises:` the IDs of the items of the layer above, never their
  wording;
- `Choice:` what was chosen, against what, and what it costs, or that
  there was no real alternative;
- `Where:` the path of the file that realises the part.

A SOL item carries the detail of its part, whatever file realises it.
A file that realises a part may repeat what the design says. It is
never the only place where that stands.

A TBC item is what is open. It carries its owner, what would close it
and whether it blocks realisation.

## Complete when

The design is complete for now when two things hold:

- every item of the layer above that is in scope is realised by a
  part, knowingly left unanswered, or open as a TBC;
- no TBC that blocks realisation is open.

It is never finished. When this completion is reached, Claude offers
the approval. The offer is a recommendation, never a gate.

## How it is found

The design is found through its definition, worked through the
command `/forge`. A definition is the file that says what an artefact
is to achieve and how it is found. This one is
`.claude/skills/forge/states/solution-design.md`. How a pass is run is
on the page [Design the solution](../use/design-the-solution.md).

A pass over the design starts from one of these situations:

- there is no design yet, and the principal says whether one is worth
  writing;
- a layer above has moved, and the pass runs on what changed;
- the thing itself has changed, and the design is brought current;
- a wording needs a fix, which is made directly.

The definition names the areas the design finds, in whatever order
the conversation takes them:

- what is to be realised: the items of the layer above that the
  design answers, and what of them it knowingly leaves unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole: the few ideas the solution rests on;
- the parts: what is built or done, by whom where it is not software,
  and where each is realised;
- how the parts work together, and what holds across them;
- the choices: for each real one, what it was chosen against (doing
  nothing, or the least that would do, among the alternatives) and
  what it costs;
- what is open or unproven: what would close it, and whether it
  blocks realisation;
- how it will be known to hold: by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed.

Every area is walked before the design is returned or a write is
offered. An area may stay empty when it was considered and found not
to apply.

With every pass Claude makes a coverage map: the items in scope of
the layer above that have no part, and the parts that realise no
item. The coverage map is a tool of the pass, not part of the design.
A pass ends by naming what changed and what stays open.

Two commands stand beside a pass:

- `/research <topic>`: proposed where a choice needs outside
  grounding, and run on the principal's word;
- `/challenge <persona> solution-design`: the independent test of the
  choices, offered once the design stands, and never run on Claude's
  own judgement.

The designing may show that something wanted cannot be realised, or
only at a price not worth paying. Claude raises that as a thread, and
what is wanted is decided in the intent first.

## Why

### Why the intent does not solve and the design does

An intent says what the principal wants and why, and it does not
solve. These belong to the intent:

- what the principal wants;
- what the principal does not want;
- what is the case;
- what is open;
- what the principal dropped.

How the things wanted are realised belongs to the solution design.
The reason: an intent that carries the solution cannot be read as
what is wanted, and nobody can be asked for a proposal of the whole
solution over it.

One test says where a sentence belongs: would it still hold if the
thing were realised in a wholly different way? If it would, it is
intent. If it would not, it is solution. Two pairs show the line:

| Intent | Solution |
|---|---|
| A principle the principal sets for the solution: what the realisation must respect whatever its shape. | The mechanism that honours the principle. |
| What the principal wants the people who use the thing to be able to do, and what must be true when it is done. A command the principal asks for by name is among it. | How the command does it: what it is built of, its steps and their order, and the checks it runs. |

The division is by kind of content, never by who said it. An idea of
the principal about how to build something is solution too.

### Why the design is whole enough to build from

The thing must be buildable from the artefacts of the chain without a
look at the finished product. The product is what is built, never a
source of its own design. For that reason what is designed stands in
the solution design, and a file that realises a part is never its
only place.

### Why it restates nothing above it

What is wanted stands in the layer above, and how it is realised
stands in the design: that is the division described above. An item
points to what it realises by ID and does not repeat its wording. The
reason for citing by ID in place of the wording is not recorded.

## A worked example

A generic item of a design, in the shape the template gives. `NNNN`
stands for the number of an ID, here of two positions of an intent.

```markdown
### Intake
- **SOL.0010 The intake form.** The one way a request arrives, and
  the place where it counts as received. The form asks for the
  requester, the matter in one sentence and the date an answer is
  needed by; it refuses a request without that date. Realises:
  POS.NNNN, POS.NNNN. Choice: one form for every kind of request,
  against one form per kind; the price is fields that some requests
  leave empty. Where: `intake/form.md`.
```

Read part by part:

- The name and the first sentences say what the part is and what it
  answers for, with the detail of the part. The fields and the
  refusal stand in the item. The form can be built from the item
  without a look at `intake/form.md`.
- `Realises:` gives two IDs of the layer above and none of their
  wording. The wording stays in the layer above.
- `Choice:` gives what was chosen, what it was chosen against and its
  price. Had there been no real alternative, the item would say so
  here and invent none.
- `Where:` gives the path of the file that realises the part. That
  file may repeat the item. It is never the only place of what the
  item says.

The test of a sentence sorts what belongs to this item and what does
not. "Every request is answered by the date it names" would still
hold if requests arrived in a wholly different way. It is intent and
stands in the layer above. "The form refuses a request without that
date" would not hold then. It is solution and stands in the item.

What is open stands beside the parts as a TBC:

```markdown
## Open
- **TBC.0010** (owner: the principal) Whether a request may also
  arrive by e-mail. Closed by: the principal's decision on the
  channels. Blocks realisation: no.
```

## See also

- [Design the solution](../use/design-the-solution.md): iterating it.
- [The intent](the-intent.md): the layer whose "what" this answers.
- [The user stories](the-user-stories.md): the stories, which a
  design cites and never the reverse.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
