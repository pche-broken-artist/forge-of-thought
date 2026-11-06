---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 6d8d23b7958ee700
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page shows how you iterate the solution design, the document
`40-solution-design.md` that says how the things wanted are realised,
with `/forge solution-design`. It is for the principal, the person
whose thinking is being forged, who works the design together with
Claude. What the design holds is explained in [The solution
design](../about/the-solution-design.md). Terms of the forge are
defined in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you want to say how what is wanted is realised, part by
part, with the choices each part rests on. Whether a design is worth
writing at all is yours to say. A project may stop at a layer above
it.

There are four ways in:

- No design exists yet.
- A layer above the design has moved. The pass then runs on what
  changed.
- The thing the design describes has changed below it. The design is
  then brought current.
- A wording needs a fix. It is made directly.

## The command

```
/forge solution-design my-project
```

The slug is optional where Claude can tell the project. Replace
`my-project` with the slug of your project.

## What happens

1. Claude resolves the project and reads the inputs. The inputs are
   the lowest layer the project has above the design (the
   assignment or the BRD, and whatever stands above that), the
   intent with its threads, the decisions and the ledger (the state
   of the project, made at read time). Where the thing already
   exists, Claude reads what realises it as it stands. You should now
   see Claude name what it has read and what the design says today.
2. Claude proposes the parts and the choices, and you judge them.
   How the design is composed is your choice: found together by
   questions, or handed over with a few sentences of what you want.
   Claude names the few real choices and does not dress every part
   as one. Where there was no real alternative it says so, and where
   a reason is not known it says that. You should now see each choice
   with what it was chosen against and what it costs.
3. Claude makes the coverage map. It lists the in-scope items of the
   layer above that no part realises, and the parts that realise no
   item. The map is a tool of the pass and is not part of the design.
   You should now see both lists, each possibly empty.
4. Claude ends by naming what changed and what stays open. When every
   in-scope item of the layer above is realised, knowingly left
   unanswered or open as a question, and no open question blocks
   realisation, it offers the approval. The offer is a
   recommendation, never a gate. You should now see that summary and,
   where it applies, the offer.
5. You say when to write. The design is written once at the end of
   the round, rewritten for coherence and never appended to. You
   should now see Claude name the file and sections it wrote.

What cannot be realised, or only at a price not worth paying, is not
settled in the design. Claude raises it as a thread, and the intent
decides what is wanted first.

Once the design stands, Claude offers `/challenge <persona>
solution-design`, an independent test of the choices. The persona
`architect` exists for it. It runs only on your word. The way to run
it is in [Challenge the thinking](challenge-the-thinking.md).

## What you have afterwards

- `40-solution-design.md`. A first design starts as version 0.1,
  made from the template, and carries `How the parts work together`,
  `Parts`, `Across the parts` and `Open` as sections. Empty sections
  and template comments are deleted. Each part names what it realises
  by the IDs of the layer above, never by their wording, and names
  where it is realised by path.
- `40-solution-design.history.md`, the companion that records each
  change and why.
- Threads in the intent for whatever could not be realised.

## If something goes wrong

- A layer above is missing or has moved: the design is made on the
  lowest layer the project has, and a pass on a moved layer runs on
  what changed.
- A part cannot be realised: it goes back to the intent as a thread
  and is not forced into the design.
- A reason for a choice is not known: Claude says so and the design
  carries it as open until you judge it.
- A choice Claude made and you have not judged: the design says so in
  plain words at that part until you have.

## A worked example

You have a project `my-project` with an intent and an assignment, and
no design yet.

1. You type `/forge solution-design my-project`.
2. Claude reads the assignment, the intent and its threads, and says
   that no design exists.
3. It proposes three parts and one real choice, a part built by a
   team and not by software, with what the choice was made against and
   what it costs. For a second part it says there was no real
   alternative.
4. The coverage map shows one in-scope requirement with no part. You
   decide that a fourth part realises it.
5. One item cannot be realised at a price worth paying. Claude raises
   it as a thread for the intent.
6. You say write. Claude creates `40-solution-design.md` as version
   0.1 with its history companion, names what stays open, and offers
   `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a
  solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge
  of the design.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
