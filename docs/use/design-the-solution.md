---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: ee1188da70682285
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page shows how you iterate a project's solution design, the document that says how the things wanted are realised, with `/forge solution-design`. It is for the principal, the person whose thinking is forged, who has a project and wants its design written or brought current. What a solution design holds is on [The solution design](../about/the-solution-design.md); the terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the project has a layer above the design (an assignment, or a BRD) and you want the design written or kept current. Whether a design is worth writing at all is yours to say. Claude does not insist on one.

There are four ways in:

- No design yet: the first one is written.
- A layer above has moved: the pass runs on what changed.
- The thing that realises the design has changed below: the design is brought current.
- A wording fix: it is made directly.

## The command

```
/forge solution-design [slug]
```

The slug names the project. Without it Claude resolves the project as the other `/forge` commands do.

## What happens

1. Claude reads the lowest layer the project has above the design, and whatever stands above that. It also reads the decisions, the ledger and the project's threads. Where the thing already exists, it reads what realises it as it stands. Research and sources are read as you direct.

   You should now see Claude say what it has read and which way in applies.

2. Claude proposes the parts and the real choices, and you judge them. How the design is composed is your choice: found together with you by questions, or handed over with a few sentences of what you want. Either way Claude names only the few real choices, says plainly where there was no alternative, and says where a reason is not known.

   You should now see proposed parts and choices, each with what it was chosen against and what it costs.

3. Claude makes the coverage map. It lists the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design.

   You should now see those two lists, so that nothing wanted is left out in silence.

4. Whatever the designing shows cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. What is wanted is decided in the intent first, and the design follows.

   You should now see each such matter named as a thread for the intent, not settled inside the design.

5. Claude ends by naming what changed and what stays open. It writes once, on your word, and rewrites the design for coherence instead of appending to it. When the design is complete for now, it offers approval as a recommendation, never as a gate.

   You should now see the design file and its history updated.

## What you have afterwards

- `40-solution-design.md`, kept current. A first design starts as a draft, version 0.1, made from the solution-design template, with its history companion and its row in the ledger's Documents table.
- A design that is complete for now when every in-scope item of the layer above is realised by a part, knowingly left unanswered, or open as a to-be-confirmed question, and when no open question blocks realisation. It is never finished.

Once the design stands, Claude offers an independent test of its choices:

```
/challenge architect solution-design
```

The persona `architect` exists for this. It is offered, never run on Claude's own judgement. See [Challenge the thinking](challenge-the-thinking.md).

## If something goes wrong

- A choice Claude made that you have not judged is marked as such in plain words at its item until you judge it.
- A reason nobody knows is written as unknown, never invented.
- An open question that blocks realisation keeps the design from being complete. It names its owner and what would close it.

## A worked example

A project, here called `<slug>`, has an assignment and no design yet.

1. You type `/forge solution-design <slug>`.
2. Claude reads the assignment, the intent and its threads. It proposes three parts and one real choice, for which it names the alternative it set aside and the cost. For the other two it says there was no real alternative.
3. The coverage map shows one requirement of the assignment with no part. You say it is left knowingly unanswered. Claude records that in the design.
4. While designing the second part, Claude finds that a requirement cannot be realised at an acceptable price. It raises a thread for the intent and does not change the requirement itself.
5. You say `write`. Claude creates `40-solution-design.md` as a draft with its history companion and ledger row, names what stays open, and offers `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
