---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 01fd59ae57223699
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

This page shows how you iterate the intent, the file `10-intent.md`
that holds what the principal wants and why, with the command `/forge
intent`, one round at a time. It is for the principal, the person
whose thinking is being forged. Claude is the machine that works with
the principal.

## When to use it

Use it when the intent needs to grow or change. A round can start
from any of these:

- There is no intent yet, and the briefs are to be consolidated into
  the first one.
- A brief is pending or only partly mined.
- A thread is open. A thread is one matter set aside to be taken up
  later.
- You have a new word to add.
- The recipients of an assignment have sent something back.

For what the intent holds and why it is rewritten for coherence, see
[The intent](../about/the-intent.md).

## The command

```
/forge intent [slug]
```

`slug` names the project. Leave it out where Claude can resolve the
project without it.

## What happens

1. Claude resolves the project and reads the inputs: the briefs you
   say to mine, the decisions record, the ledger (the state of the
   project, made from its documents when it is read) and the intent
   as it stands. It reads the open threads with the intent. They are
   files in `threads/`, one per thread.

   You should now see Claude say where the round starts.

2. The round starts from one of the ways in above. Briefs are offered
   before threads. A brief is mined whole by whole, one brief at a
   time.

   You should now see one brief, or one thread, taken up first.

3. Claude works one theme at a time. It probes contradictions, gaps
   and unstated assumptions. It asks of an idea whether it is good
   and whether it is feasible, as two questions kept apart. It offers
   options with their trade-offs. Where a thread needs outside
   grounding, it proposes research and runs it on your word.

   You should now see one theme in the conversation, not several.

4. The answers are carried in the conversation. Nothing is written
   while the round runs. The conversation is described in
   [The working methods](../about/working-methods.md).

   You should now see your answers reflected back as structure.

5. The reality check comes last. Claude and you go through what is
   feasible and where the wheel already exists. Then Claude offers
   `/challenge <persona> intent` as the independent reality check. It
   never runs it on its own judgement. How that check is run is on
   [Challenge the thinking](challenge-the-thinking.md).

   You should now see the offer of the independent check.

6. At the round's natural end Claude reflects the round back and asks
   whether to write. You answer `write`. Claude then writes once for
   the whole round. Resolved threads move into positions or rejections
   and are closed. The mining record of every brief touched is kept.
   A position written or rewritten carries one date and no trial,
   count or plan. The way to it goes into the record of the change.

   You should now see the intent file changed, with one version for
   the whole round.

7. Whatever stays unsettled is saved into its thread before the
   session ends. A session is one run of the conversation with
   Claude. Claude then remakes the ledger.

   You should now see the unfinished matter in a thread file.

8. The round ends with Claude naming what changed and what stays
   open. When no thread blocks the next layer, it names the layers
   that can follow from the intent. Where the principal takes no
   further layer, it offers the approval instead. This is a
   recommendation, never a gate.

   You should now see a closing summary of the round.

## The threads

Each thread file carries a header that says:

- what it concerns
- where it came from
- whose it is
- when it is taken up
- what waits on it, where something does
- whether it is open or closed

How a thread is born, kept and closed is described in
[Set a matter aside as a thread](set-a-matter-aside.md). A thread
closes only on your word.

## What you have afterwards

- `10-intent.md` rewritten once for the round, with its record
  appended beside it.
- Resolved threads closed, their outcome standing as a position or a
  rejection.
- Open threads saved as files, ready for the next round.
- A closing summary of what changed and what stays open.

The intent says what holds however the thing were realised. How it is
realised belongs to the solution design, not to the intent.

## A worked example

A project `demo-project` has a brief that was never mined and one open
thread about who the recipients are.

1. You type `/forge intent demo-project`.
2. Claude offers the brief first. You mine it with Claude, theme by
   theme: the aim, what is dropped, what is deferred.
3. Claude reflects back what it understood as positions, facts and one
   rejection with its reason. You correct one position. Claude carries
   the correction and does not write it yet.
4. Claude turns to the open thread. You settle it in conversation, and
   it becomes a position.
5. Claude runs the reality check with you and offers `/challenge
   <persona> intent`. You decline it for now.
6. Claude asks whether to write. You answer `write`. The intent is
   rewritten once, the thread is closed, and the mining of the brief
   is recorded.
7. Claude names what changed, names what stays open, and names the
   layers that can follow, or offers the approval.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why
  it is rewritten for coherence.
- [Set a matter aside as a thread](set-a-matter-aside.md): how a
  thread is born, taken up and closed with `/thread`.
- [The working methods](../about/working-methods.md): the named ways
  the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the
  independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
