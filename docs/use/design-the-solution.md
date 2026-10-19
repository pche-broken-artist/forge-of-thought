---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 507bc8b134c0d890
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page shows how you iterate a project's solution design, the document that says how the things wanted are realised, with `/forge solution-design`. It is for the principal, the person whose thinking is being forged, who runs the command and judges what Claude proposes. What a solution design holds is explained in [The solution design](../about/the-solution-design.md). Terms of the forge are listed in the [Glossary](../reference/glossary.md).

## When to use it

Use it when one of these is the case:

- The project has no design yet. Whether one is worth writing is yours to say; a project may stop at a higher layer.
- A layer above the design has moved, and the design must follow what changed.
- The thing the design describes has changed below it, and the design must be brought current.
- A wording needs fixing. Claude makes such a fix directly.

## The command

```
/forge solution-design my-project
```

The slug is optional where Claude can tell which project you mean. The command iterates `40-solution-design.md` of that project.

## What happens

1. Claude resolves the project and reads what the design is built from. That is the lowest layer the project has above the design (the intent alone, the assignment or the business requirements document, and whatever stands above that), the project's decisions, its open threads and the design as it stands. Where the thing already exists, Claude reads what realises it as it stands. You should now see Claude say which layers it read and whether a design exists.
2. Claude proposes the parts of the solution and the choices they rest on, and you judge them. How the design is composed is your choice: found together with Claude by questions, or handed over with a few sentences of what you want, in which case Claude returns a proposal with the list of what it assumed and chose. You should now see parts proposed one at a time, each with what it answers for.
3. Claude names the few real choices and does not dress every part as one. Where there was no real alternative it says so. Where a reason is not known it says it is unknown. Claude also says in words how sure it is of a claim. You should now see, for each real choice, what it was chosen against and what it costs.
4. Claude makes the coverage map. It lists the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design. You should now see both lists, each possibly empty.
5. What the designing shows cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. What is wanted is decided in the intent first, and the design follows. You should now see each such matter named as a thread, not worked around in the design.
6. At the end of the round Claude asks whether to write, and writes on your word. A write rewrites the design for coherence and never appends. You should now see Claude name what changed and what stays open.
7. Once the design stands, Claude offers `/challenge <persona> solution-design`. The persona `architect` exists for this test of the choices. It never runs on Claude's own judgement; it runs when you ask. The command is described in [Challenge the thinking](challenge-the-thinking.md). You should now see the offer, which you may decline.

## What you have afterwards

- `40-solution-design.md`, created as a first draft on the first pass and rewritten on later ones. It has these sections: how the parts work together, the parts, what holds across the parts, and what is open.
- Its history companion, `40-solution-design.history.md`, which records what changed and why.
- Each part of the design names the items of the layer above that it realises (by their IDs, never their wording), the choice made, and where the part lives (a path).
- Where a part is realised in a file of its own, the design names the file and the detail stays in the file. Where a part has no file yet, the design carries the detail.
- A choice Claude made and you have not judged is marked as such in plain words, until you have judged it.
- Each open question carries its owner, what would close it and whether it blocks realisation.

The design is complete for now when every in-scope item of the layer above is realised by a part, knowingly left unanswered, or open as a question, and when no open question that blocks realisation remains. It is never finished. When that point is reached, Claude offers approval as a recommendation, never as a gate.

## If something goes wrong

- A part cannot be realised, or only at a price not worth paying. Claude raises it as a thread of the intent. You decide what is wanted in the intent first, and the design is then brought current.
- The coverage map shows an item with no part. Either a part is added, the item is knowingly left unanswered and the design says so, or it stays open as a question with an owner.
- The map shows a part that realises no item. Either the part goes, or the layer above lacks something, and that goes back to the intent.
- A reason for a choice is not known. The design says it is unknown; it does not invent one.

## A worked example

The project `my-project` has an intent and an assignment, and no solution design.

1. You type `/forge solution-design my-project`.
2. Claude reads the assignment, the intent and its threads, and says no design exists. You say you want one.
3. Claude proposes three parts: an intake form, a review queue and a weekly report. For each it names the items of the assignment it answers. For the review queue it names a real choice: a shared board against a mailbox, chosen for visibility, at the price of one more tool to maintain. For the report it says there was no real alternative.
4. The coverage map shows one requirement with no part and no part without a requirement. You decide the requirement stays open, and Claude records it as an open question that does not block realisation.
5. Claude notes that one requirement cannot be met within the stated limit. It raises this as a thread of the intent, and you take it up there.
6. Claude asks whether to write. You say `write`, and Claude creates `40-solution-design.md` and its history companion, then names what changed and what stays open.
7. Claude offers `/challenge architect solution-design`. You run it when you want the choices tested.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
