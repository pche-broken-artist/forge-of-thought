---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 87ab6d6ea3ccca00
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - .claude/agents/challenger-architect.md
---

# Design the solution

This page shows how you iterate the solution design of a project with `/forge solution-design`. The solution design is the document `40-solution-design.md`, which says how the things wanted are realised. What it holds is described in [The solution design](../about/the-solution-design.md). Terms of the forge are explained in the [Glossary](../reference/glossary.md). In this page the principal is the person whose thinking is being forged, and Claude is the assistant that works with the principal.

## When to use it

Use it when a project needs its solution design made or brought current. Whether a design is worth writing at all is yours to say. Nothing forces it.

There are four ways in:

- No design exists yet: the first one is made.
- A layer above the design has moved: the pass runs on what changed.
- The thing the design describes has changed below it: the design is brought current.
- A wording fix is needed: it is made directly.

## The command

```
/forge solution-design [slug]
```

The slug names the project. Leave it out and Claude resolves the project itself.

## What happens

1. Claude resolves the project and reads what the design is made from. That is the lowest layer the project has above the design (the intent alone, the assignment, the BRD or the user stories), whatever stands above that, the decisions, the ledger (the state of the project, made when it is read) and the project's threads. Where the thing already exists, Claude reads what realises it as it stands. You should now see Claude say which layer it takes as the ground of the design.

2. Claude puts forward the parts of the solution and the choices they rest on, and you judge them. You may compose the design together with Claude, or hand it over with a few sentences of what you want. Either way Claude proposes and you decide. Claude names the few real choices and does not dress every part as one. Where there was no real alternative it says so, and where a reason is not known it says that. You should now see a draft of the parts, each with what it answers for.

3. Claude makes the coverage map. It lists the in-scope items of the layer above that no part realises, and the parts that realise no item. The map is a tool of the pass and is not part of the design. You should now see the two lists, each possibly empty.

4. Claude walks what the design must find before it returns the design or offers a write. It considers these areas, and one may stay empty when it was considered and found not to apply:
   - what is to be realised, and what is knowingly left unanswered;
   - the ground: what exists, what stands around it and what you fixed in advance;
   - the approach as a whole;
   - the parts and where each is realised;
   - how the parts work together;
   - the choices, with what each was chosen against and what it costs;
   - what is open or unproven;
   - how it will be known to hold;
   - the way there, where the solution replaces something that runs;
   - what is deliberately not designed.

   You should now see these areas covered in the draft, or named as not applying.

5. Claude names what changed and what stays open. When the design is complete for now, it offers the approval as a recommendation, never as a gate. A design is complete for now when every in-scope item of the layer above is realised by a part, knowingly left unanswered, or open as a to-be-confirmed question, and no open question that blocks realisation remains. It is never finished. You should now see a closing summary and, if the design is complete, the offer to approve.

6. The write happens once, at the end of the round, on your word. You should now see the file written.

Where the design holds a choice Claude made and you have not judged, the design says so in plain words at that part until you have judged it.

## What you have afterwards

- `40-solution-design.md`, rewritten for coherence as a whole and not appended to. Each part names what it realises, the choice it rests on and where it is realised. Empty sections and template comments are removed.
- `40-solution-design.history.md`, the companion that records the change and the reason. A first design starts as version 0.1.
- A list of what stays open.

## If something goes wrong

- The designing shows that something wanted cannot be realised, or only at a price not worth paying. Claude raises it as a thread. What is wanted is then decided in the intent first, and the design follows. It is not bent to fit.
- A question blocks realisation and cannot be closed in this pass. It stays in the design as an open question that names its owner and what would close it, and the design is not called complete.

## Challenge the design

Once the design stands, Claude offers `/challenge <persona> solution-design`. It runs only on your word. The persona `architect` exists for it and reviews a solution design. How a challenge runs is described in [Challenge the thinking](challenge-the-thinking.md), and the personas of today are listed in [Challenger personas](../reference/challenger-personas.md).

## A worked example

A project, here called `<slug>`, has an intent and an assignment, and no design yet.

```
/forge solution-design <slug>
```

Claude takes the assignment as the lowest layer above the design and reads it with the intent and the threads. It proposes three parts and names one real choice among them, with what it was chosen against and what it costs. For the other two it says there was no real alternative. The coverage map shows one assignment item with no part. You decide to leave it knowingly unanswered, and the design says so. Claude names what stays open, you confirm the write, and `40-solution-design.md` appears as version 0.1 with its history. Claude then offers `/challenge architect solution-design`, and you take it up or leave it.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Challenger personas](../reference/challenger-personas.md): the personas of today, the architect among them.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
