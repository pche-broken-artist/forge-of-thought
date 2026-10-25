---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 89cc5172c8eb8269
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page is for you when you want to write or bring up to date the solution design of a project, the document that says how the things wanted are realised. You do it with `/forge solution-design`, working with Claude in a conversation. You are the principal, that is, the person whose thinking is being forged, and you judge every part and every choice. What the document holds is described in [The solution design](../about/the-solution-design.md).

## When to use it

Whether a solution design is worth writing for your project is yours to say. Claude does not insist on one.

The command serves four ways in:

- No design exists yet. The first one is created.
- A layer above the design has moved. The pass works on what changed.
- The thing that realises the design has changed below. The design is brought current.
- A wording needs fixing. It is fixed directly.

## The command

```
/forge solution-design my-project
```

The slug is optional. Without it, Claude resolves the project itself. The command iterates `40-solution-design.md`.

## What happens

1. Claude resolves the project and reads what it needs: the lowest layer the project has above the design (the assignment or the business requirements document, or the intent alone), whatever stands above that, the intent's open threads, the record of decisions and the ledger (the state of the project, made when it is read). Where the thing already exists, Claude reads what realises it as it stands. You should now see Claude say which project and which design it is working on.

2. Claude walks the ground of the design: what is to be realised, what already exists and is kept or replaced, the few ideas the solution rests on, the parts and where each is realised, how the parts work together, the real choices, what is open, how it will be known to hold, the way there where the solution replaces something that runs, and what is deliberately left undesigned. An area may stay empty when it was considered and does not apply. You should now see Claude propose parts and choices for you to judge.

3. Claude names the few real choices and does not dress every part as one. Where there was no real alternative it says so. Where a reason is not known it says that it is unknown, and it says in words how sure it is of a claim. A choice Claude made and you have not yet judged is marked as such in the design until you have judged it. You should now see each real choice with what it was chosen against and what it costs.

4. With every pass Claude makes the coverage map: the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design. You should now see both lists.

5. What the designing shows cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. What is wanted is decided in the intent first. You should now see a thread raised, not a change quietly made to the design.

6. Claude ends by naming what changed and what stays open. When every in-scope item above is realised, knowingly left unanswered or open, and no open matter that blocks realisation remains, Claude recommends approving the design. The recommendation is not a gate. You should now see the closing summary and, where it applies, the recommendation.

7. The design is written once at the end of the round, when you say so. A write rewrites the document for coherence and does not append to it. The first design is created as version 0.1 with a history companion beside it. You should now see the file written and named.

When the design stands, Claude offers `/challenge <persona> solution-design`, an independent test of its choices by an isolated reviewer. The persona `architect` exists for this. Claude never runs it on its own judgement. See [Challenge the thinking](challenge-the-thinking.md).

## What you have afterwards

- `40-solution-design.md`, which says how the things wanted are realised as the solution stands today.
- `40-solution-design.history.md`, which records what changed and why.
- Where the pass found something unrealisable, a thread in the intent.

The design restates nothing of the layer above and cites its items by ID. It copies nothing of what realises it and names that by path.

## A worked example

You have a project `my-project` with an intent and an assignment, and no design.

```
/forge solution-design my-project
```

Claude reads the assignment, the intent and its threads. It proposes three parts and one real choice: a part could be done by hand or by a script, and Claude recommends the script and states what that costs. The coverage map shows one requirement with no part and one part that serves no requirement. You decide the requirement is out of scope for now, and you drop the part. While designing, Claude finds that one wanted behaviour cannot be realised without a price you would not pay, so it raises a thread in the intent instead of bending the design. You say `write`. Claude writes version 0.1 of the design and its history, names what stays open, and offers `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
