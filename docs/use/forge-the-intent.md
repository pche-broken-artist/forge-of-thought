---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 9d823300fa60ea26
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
---

# Forge the intent

This page shows how you iterate the intent, the document in which a project keeps what the principal (the person whose thinking is being forged) holds, round by round with `/forge intent`. It is for the principal who has a brief, an open thread or a new thought and wants it worked into the intent. What the intent holds and why is explained in [The intent](../about/the-intent.md).

## When to use it

Use it in any of these cases:

- The project has no intent yet and the briefs are to be consolidated into the first one.
- A brief is pending or only partly mined.
- An open thread, a new word of yours or what the recipients sent back is to be worked in.

## The command

```
/forge intent [slug]
```

The slug names the project. It is the file `10-intent.md` that is iterated, together with the threads in `threads.md` beside it.

## What happens

1. Claude resolves the project and reads the briefs you say to mine, the decisions, the ledger, the intent as it stands and the open threads.
   You should now see Claude naming where the round starts.
2. The round starts where you are. Briefs are offered before threads.
   - A brief that is pending or partial is mined whole by whole, one brief at a time.
   - Otherwise the round starts from an open thread, a new word of yours or what the recipients sent back.

   You should now see one brief or one thread put forward as the matter of the round.
3. The round takes one theme at a time. Claude probes contradictions, gaps and unstated assumptions, and asks of an idea two separate questions: whether it is good and whether it is feasible. It offers options with their trade-offs, and it proposes research where a thread needs outside grounding. Research runs only on your word.
   You should now see your answers carried in the conversation and reflected back as structure, with nothing written yet.
4. The reality check comes last, before a lower layer is proposed. Claude runs it with you. Afterwards it offers `/challenge <persona> intent` as the independent check (see [Challenge the thinking](challenge-the-thinking.md)). It never runs that check on its own judgement.
   You should now see the joint reality check done and the independent one offered.
5. At the round's natural end Claude asks whether to write. You answer `write`. One write covers the whole round: the intent is rewritten for coherence, never appended to. Threads that were resolved move into positions or rejections. The Mined column of every brief touched is kept.
   You should now see the intent rewritten once and the files named.
6. Claude closes by naming what changed and what stays open. Where the intent is complete for now, it names the layers that can follow. Where you take no approval for the project, it offers the approval. This is a recommendation, never a gate.
   You should now see what changed, what stays open and what can follow.

The conversation runs by the methods described in [The working methods](../about/working-methods.md), among them one write per round.

## What you have afterwards

- `10-intent.md`, rewritten once for the round, in the project's language.
- `10-intent.history.md`, the companion that records the change.
- `threads.md`, the open threads of the project. They are part of the intent as its history is: the intent says what holds, the threads say what is being worked. The file is rewritten freely and has no version, no history and no ledger row of its own.
- Every thread names, right after its ID and in square brackets, the artefact it concerns, as `/forge` names it.
- Whatever remains unsettled is saved into its thread before the session ends.

The first intent is created as version 0.1 from the template, together with its history companion and `threads.md`.

The intent has these sections:

- Essence: what you want and why, as of today.
- Positions: what you currently hold.
- Facts: what is the case.
- Rejected directions: what was considered and dropped, with the reason.
- Candidate structure for the layer below: the recipients, the objective and the success criteria, staged as soon as you see them. It is optional.

## If something goes wrong

- A thread closes only on your word. If Claude has not closed one, nothing is wrong: the thread stays in `threads.md`.
- The intent does not solve. What it says would hold however the thing were realised. Where a matter is about how to realise it, the solution design takes it, and where the project has none, the item names it.
- Where a gap, a contradiction or a risk shows, Claude raises it as a question and does not fill it by assumption.

## A worked example

A project `<slug>` has one brief, never mined, and no intent yet.

1. You type `/forge intent <slug>`. Claude reads the brief and says the round starts with it, mined whole.
2. Claude takes the first theme, the purpose of the project. It reflects back what it understood as a short structure: one essence, two candidate positions, one open question.
3. You answer the question and modify one position. Claude carries both and goes on to the next theme, the recipients. Nothing is written.
4. Claude names a contradiction between two statements of the brief and asks which one holds. You say the second. The first goes to the rejected directions with its reason, and a third matter that you cannot yet decide is kept as a thread.
5. The themes are done. Claude runs the reality check with you, asks what of it is feasible and where the wheel already exists, and offers `/challenge <persona> intent`.
6. Claude asks whether to write. You answer `write`. The intent is created as version 0.1, with its history companion and `threads.md`.
7. Claude closes: the intent now holds the essence, positions and one rejection. One thread stays open. It does not block the layer below, so Claude names the layers that can follow and recommends going on to one of them. You may also stay with the intent for another round.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs, one write per round among them.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
