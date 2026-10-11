---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 8740bd8268f286d1
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
---

# Design the solution

This page shows how you iterate the solution design, the document that says how the things wanted are realised, with `/forge solution-design`. It is for the principal (whoever's thinking is being forged) who runs a project and wants the design written or kept current. What a solution design holds, and why, is on [The solution design](../about/the-solution-design.md); terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the things wanted are settled and you want to say how they are realised. Whether a design is worth writing at all is yours to say: a project may stop at the layer above and never have one.

There are four ways in:

- There is no design yet. Claude creates the first one.
- A layer above has moved. The pass runs on what changed.
- The thing that realises the design has changed. The design is brought current.
- A wording needs fixing. It is made directly.

## The command

```
/forge solution-design [slug]
```

The slug names the project; leave it out and Claude resolves the project itself. The target is `40-solution-design.md`.

## What happens

1. Claude reads the lowest layer the project has above the design, the intent, whatever stands above that, the decisions record, the ledger (the project's single record of state) and the project's open threads. Where the thing already exists, it reads what realises it as it stands. It also reads the design, if there is one.

   You should now see Claude say what it has read and which of the four ways in applies.

2. You choose how the design is composed: found together with Claude by questions, or handed over with a few sentences of what you want. Either way Claude proposes the parts and the choices, and you judge them.

   You should now see proposed parts, each saying what it is and what it answers for.

3. Claude names the few real choices and does not dress every part as one. Where there was no real alternative it says so, and where a reason is not known it says it is unknown. A choice you have not yet judged is marked as such in the design, in plain words, until you have.

   You should now see each real choice with what it was chosen against and what it costs.

4. Claude makes the coverage map. The map lists the in-scope items of the layer above that no part realises, and the parts that realise no item. It is a tool of the pass and is not part of the design.

   You should now see both lists, each possibly empty.

5. What cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. What is wanted is decided in the intent first, never in the design.

   You should now see each such matter named as a thread to take up in the intent.

6. Claude reflects back what it will write and asks whether to write. On your word it writes once for the whole round. The design is rewritten for coherence, never appended to. A first design starts as a draft, with its history companion and its row in the ledger.

   You should now see the new file, or the new version of it, and a statement of what changed and what stays open.

7. When every in-scope item of the layer above is realised by a part, knowingly left unanswered or open, and no open question blocks realisation, Claude offers the approval. It is a recommendation, never a gate.

8. Once the design stands, Claude offers an independent challenge of its choices. It never runs one on its own judgement.

   You should now see the offer of `/challenge <persona> solution-design`.

## What you have afterwards

- `40-solution-design.md`, current for now. It is never finished.
- Its history companion, `40-solution-design.history.md`, and its row in the ledger.
- Items that say what each part is and what it answers for. Each item then gives, in order, the items above it that it realises, its choice, and where it lives, as the template shows. The detail of a part lives in its own file where it has one.
- Threads in the intent for whatever could not be realised.

## Challenge the design

`/challenge <persona> solution-design` tests the choices from outside. The persona `architect` exists for the solution design. The run is described on [Challenge the thinking](challenge-the-thinking.md).

## If something goes wrong

- The coverage map shows an in-scope item with no part. Add a part, leave the item knowingly unanswered, or leave it open as an open question that records its owner, what would close it and whether it blocks realisation.
- The coverage map shows a part that realises no item. Either the part does not belong, or something wanted has not been said above; in the second case it is a matter for the intent.
- A part cannot be realised, or only at a price not worth paying. Take it back to the intent as a thread.
- A reason for a choice is not known. The design says it is unknown; Claude does not invent one.

## A worked example

A project called `<slug>` has an intent with three in-scope items: customers receive a receipt, receipts are kept for a year, and staff can look one up. There is no design yet.

You run:

```
/forge solution-design <slug>
```

Claude reads the intent, the decisions record, the ledger and the threads, and says there is no design yet. You hand it a few sentences: receipts are made by the existing till software, and a small store is to be added.

Claude proposes two parts. The first is the receipt maker, which realises the first item, with no real alternative since the till already makes receipts. The second is the receipt store, which realises the second and third items. Its choice is a file store against a database, chosen because it is the least that would do, at the cost of slow lookup when the store grows. This choice is marked as not yet judged by you.

The coverage map shows every in-scope item with a part and every part realising an item. In the intent, though, the retention period turns out to be unaffordable on the chosen store at the expected volume. Claude does not change what is wanted. It names a thread for the intent and leaves a blocking open question in the design.

You say `write`. Claude writes the first design as a draft with its history companion and ledger row, and names what changed and what stays open. It then offers `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a solution design holds and why it restates nothing above it.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
