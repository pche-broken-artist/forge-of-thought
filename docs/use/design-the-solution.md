---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - CLAUDE.md
---

# Design the solution

This page is for the person who wants to write or keep current the
solution design of a project: the document that says how the things
wanted are realised. It tells what `/forge solution-design` does, when
to run it and what you see.

## Whether to write one

A solution design is not required. Whether one is worth writing is
yours to say. A project may end at its intent or take the layers it
needs; a layer it does not have is not missing.

## Run it

```
/forge solution-design [slug]
```

The command iterates `40-solution-design.md` in the project. It
works from the lowest layer the project has above the design: the
intent alone, or the assignment or the BRD where there is one, and
whatever stands above that. It also reads the project's decisions, its
ledger and its threads. Where the thing already exists, it reads what
realises it as it stands. Research and sources are used as you direct.

The design is derived from that layer. It cites the items above by ID
and restates none of them. It copies nothing of what realises it and
names it by path.

## The ways in

- **No design yet.** The first design is created from the template as
  version 0.1, with its history companion and its row in the ledger.
- **A layer above has moved.** The pass runs on what changed.
- **The thing changed below.** The design is brought current.
- **A wording fix.** It is made directly.

## How you work with Claude

You may compose the design together with Claude by questions, or hand
it over with a few sentences of what you want. Either way Claude
proposes the parts and the choices, and you judge them. It names the
few real choices and does not dress every part as one: where there
was no real alternative it says so, and where a reason is not known it
says that. A choice you have not yet judged is marked as such at its
item in plain words.

Nothing is built here. The design specifies.

## The coverage map

At every pass Claude makes the coverage map, and shows it to you:

- the in-scope items of the layer above that have no part;
- the parts that realise no item.

The map is a tool of the pass and is not part of the design. An item
with no part is either given one, knowingly left unanswered, or
opened as a question.

## What cannot be realised

If the designing shows that something cannot be realised, or only at
a price not worth paying, Claude does not bend the design around it.
It raises it as a thread. What is wanted is decided in the intent
first, and the design follows.

## What you get

The design has three kinds of content: how the parts work together,
the parts, and what is open. Each part is one item that says what it
is and what it answers for, which items above it it realises, the
choice it rests on, and where it lives. A question that is not yet
answered is kept as an open item with its owner, what would close it
and whether it blocks realisation. Empty sections and template
comments are deleted, and each write rewrites the design for
coherence rather than appending to it. What a part is and why the
design is shaped so is on
[About the solution design](../about/the-solution-design.md).

The design is complete for now when every in-scope item of the layer
above is realised by a part, knowingly left unanswered, or open, and
no open question that blocks realisation remains. It is never
finished.

## At the end of a pass

Claude names what changed and what stays open. When the design is
complete for now, it offers the approval as a recommendation, never a
gate.

## Test the design

Once the design stands, `/challenge <persona> solution-design` tests
its choices independently. The persona `architect` exists for it.
Claude offers the challenge and does not run it on its own judgement;
it runs when you call it. See
[Challenge the thinking](challenge-the-thinking.md).

If a choice needs outside grounding, `/research <topic>` is proposed
and run on your word.

## See also

- [About the solution design](../about/the-solution-design.md): what a solution design holds and why it restates nothing above it.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
