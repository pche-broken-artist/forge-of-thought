---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: e062aa0d511e0d97
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page shows how you iterate the solution design of a project with `/forge solution-design`. The solution design is the document `40-solution-design.md` that says how the things wanted are realised, part by part, with the choices they rest on. It is written for you, the principal (the person whose thinking is being forged), and for whoever later realises the solution, a person or an agent. What the document holds is described in [The solution design](../about/the-solution-design.md); terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Whether a solution design is worth writing at all is yours to say. A project may stop at a higher layer and never have one.

Once you want one, there are four ways in:

- There is no design yet.
- A layer above the design has moved, and the pass runs on what changed.
- The thing that realises the solution has changed, and the design is brought current.
- A wording needs fixing, and it is fixed directly.

## The command

```
/forge solution-design [slug]
```

The slug names the project. Leave it out and Claude resolves the project itself.

## What happens

1. Claude resolves the project and reads what the design is made from: the lowest layer the project has above the design (the intent alone, the assignment, the BRD or the user stories), whatever stands above that, the decisions, the ledger (the state of the project, made when it is read) and the threads of the intent (its open matters). Where the thing already exists, Claude reads what realises it as it stands. You should now see Claude restate what it has read and where the design stands.

2. Claude proposes the parts and the choices, and you judge them. You may compose the design together with Claude by questions, or hand it over with a few sentences of what you want. Either way Claude names the few real choices. Where there was no real alternative it says so, and where a reason is not known it says that too. A choice you have not yet judged is marked as Claude's at the place where it stands. You should now see each proposal with its reason and a recommendation.

3. Claude makes the coverage map. It lists the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design. You should now see the two lists, each possibly empty.

4. If the design shows that something wanted cannot be realised, or only at a price not worth paying, Claude raises it as a thread. What is wanted is then decided in the intent first. You should now see the thread named, and the design left without a pretence that it is solved.

5. Claude writes once, at the end of the round, on your word. A write rewrites the design for coherence and does not append. A first design starts as version 0.1, with a history companion beside it. You should now see `40-solution-design.md` and `40-solution-design.history.md` in the project.

6. Claude ends by naming what changed and what stays open. When the design is complete for now, it offers approval as a recommendation, never as a gate. You should now see that closing statement.

## What you have afterwards

- `40-solution-design.md`, made from the template: how the parts work together, the parts, what holds across them, and what is open. Empty sections are deleted.
- Its history companion, with one record per change.
- A list of what stays open, each with its owner and whether it blocks realisation.

The design is complete for now when every in-scope item of the layer above is realised by a part, knowingly left unanswered, or open as a question to be confirmed, and when no open question that blocks realisation remains. It is never finished.

Once the design stands, Claude offers `/challenge <persona> solution-design`, an independent test of the choices by a reviewing subagent (an isolated agent that sees nothing of the conversation). The persona `architect` exists for this. The challenge never runs on Claude's own judgement. How it runs is in [Challenge the thinking](challenge-the-thinking.md).

## If something goes wrong

- A reason for a choice is not known: Claude says so at the item and does not invent one.
- The design shows that something wanted cannot be realised: it goes back to the intent as a thread, and you decide there.
- An in-scope item has no part: the coverage map shows it. The item is realised, knowingly left unanswered, or opened as a question.
- Further failures are not recorded for this command.

## A worked example

The project `my-project` has an intent and an assignment, and no BRD. You have never written a design.

You type:

```
/forge solution-design my-project
```

Claude reads the assignment and the intent with its threads, and proposes three parts. Two of them have no real alternative, and Claude says so. The third rests on a real choice, which Claude marks as its own until you judge it. The coverage map shows one requirement with no part. You decide to leave it knowingly unanswered. You say `write`. Claude creates `40-solution-design.md` as version 0.1 with its history companion, names what stays open, and offers `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
