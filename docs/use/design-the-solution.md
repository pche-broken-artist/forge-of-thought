---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 12d2aba03b30ca1b
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page is for the principal, the person whose thinking is being forged, who wants to write or keep current the solution design of a project: the document that says how the things wanted are realised. The command `/forge solution-design` iterates it together with Claude. What a solution design holds is explained in [The solution design](../about/the-solution-design.md); terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Whether a solution design is worth writing at all is yours to say. Claude does not insist on one.

The command fits in four situations:

- No design exists yet and you want one.
- A layer above the design has moved (the intent, the assignment or the BRD), and the design must follow.
- The thing that realises the design has changed below, and the design must be brought current.
- A wording needs fixing. This one is made directly.

## The command

```
/forge solution-design [slug]
```

The slug names the project. Without it, Claude resolves the project itself. The design is the file `40-solution-design.md` of the project.

## What happens

1. Claude reads the lowest layer the project has above the design, the intent, the decisions, the ledger (the state record made from the documents) and the threads of the intent. Where the thing already exists, it reads what realises it as it stands. You should now see Claude say what it has read and whether a design stands already.

2. Claude proposes the parts of the solution and the few real choices among them. You judge them. Where there was no real alternative, Claude says so and invents none. Where a reason is not known, it says that it is unknown. You may also hand the design over: Claude then works from what you give it and returns a proposal. You should now see a proposal of parts and choices that you can accept, change or reject.

3. Claude makes the coverage map. It lists the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design. You should now see both lists, each possibly empty.

4. Claude walks the areas a design may find: what is to be realised, what already exists, the approach, the parts, how they work together, the choices, what is open, how it will be known to hold, the way there, and what is deliberately not designed. An area may stay empty when it was considered and does not apply. You should now see the design rewritten for coherence, not appended to.

5. What cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. What is wanted is decided in the intent first, and the design follows. You should now see a thread proposed in place of a workaround in the design.

6. Claude names what changed and what stays open. When every in-scope item of the layer above is realised by a part, knowingly left unanswered or open as an open question, and no open question that blocks realisation remains, Claude recommends approval. The recommendation is not a gate. You should now see the closing summary and, when the design is complete for now, the offer.

7. Once the design stands, Claude offers an independent test of its choices: `/challenge <persona> solution-design`, where the persona `architect` exists for it. It runs only on your word. See [Challenge the thinking](challenge-the-thinking.md).

## What you have afterwards

- `40-solution-design.md`: the design, with a history companion `40-solution-design.history.md` beside it. The first design is version 0.1.
- Threads in the intent for whatever could not be realised.
- A design that is current, not finished: it is never finished.

## If something goes wrong

- If the design shows that something wanted cannot be realised, that is not an error. It becomes a thread of the intent, and the intent changes first.
- If the coverage map shows an item without a part, the design is not yet complete for now. Either a part is added, the item is knowingly left unanswered, or it is recorded as an open question.
- If you do not want a design, say so. Nothing requires one.

## A worked example

A project `my-slug` has an intent and an assignment and no design.

1. You type `/forge solution-design my-slug`.
2. Claude reads the intent, the assignment and the threads, and says no design exists yet.
3. It proposes three parts and one real choice, and says plainly that the other two parts had no alternative. You accept two parts and modify the choice.
4. The coverage map shows one requirement of the assignment with no part. You decide to leave it knowingly unanswered.
5. While designing, Claude finds that one wanted thing cannot be realised at a reasonable price. It proposes a thread for the intent instead of bending the design.
6. Claude names what changed, lists the open question that remains, and offers the independent test once the design stands.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
