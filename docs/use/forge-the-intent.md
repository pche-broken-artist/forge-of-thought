---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: b0c60837525df537
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

This page shows how you iterate the intent of a project with
`/forge intent`, one round at a time. It is for the principal, the
person whose thinking is being forged, who supplies the ideas and the
decisions while Claude keeps the structure and proposes.

## When to use it

Use it in any of these cases:

- The project has briefs that are not yet mined into the intent, or
  only partly.
- A thread of the intent is open and you want to work on it.
- You have a new word to add to the intent.
- The recipients of an assignment have sent something back, and it
  changes what you hold.

The intent is never finished. It is complete for now when no open
thread blocks the layer below. What the intent holds and why it is
rewritten for coherence is explained in
[The intent](../about/the-intent.md).

## The command

```
/forge intent [slug]
```

The slug names the project. The file iterated is `10-intent.md`.

## What happens

1. Claude resolves the project, then reads the briefs you point to,
   the decisions, the ledger (the state of the project, made when it
   is read) and the intent as it stands, together with the open
   threads in `threads/`.

   You should now see Claude say where the round starts.

2. The round starts at one of these places:
   - There is no intent yet: the briefs are consolidated into the
     first one.
   - A brief is pending or only partly mined: it is mined whole by
     whole, one brief at a time.
   - There is an open thread, a new word of yours or something the
     recipients sent back: the round starts there.

   Briefs are offered before threads.

   You should now see one brief, thread or word taken up.

3. The conversation runs one theme at a time. Claude probes
   contradictions, gaps and unstated assumptions, and it asks two
   questions apart about an idea: whether it is good and whether it is
   feasible. It reflects a brain-dump back as structure before
   anything is written, offers options with trade-offs, and proposes
   research where a thread needs outside grounding. It composes the
   wording; you decide the substance.

   You should now see answers reflected back, not written.

4. Your answers are carried in the conversation. Nothing is written
   one answer at a time. At the natural end of the round Claude asks
   whether to write.

   You should now see the question whether to write.

5. You say `write`. Claude first reflects the whole round back: the
   new wording and the records of change. You confirm, and only then
   is the file written, once for the whole round, as one version.

   You should now see the intent rewritten for coherence, not
   appended to, and a history record for each change.

6. Threads that were resolved move into positions or rejections, and
   they are closed. A thread closes only on your word. A brief that
   was touched has its mined record kept.

   You should now see the resolved threads closed and the ledger
   remade.

7. The reality check comes last, before a lower layer is proposed.
   The joint check is done with Claude. Then
   `/challenge <persona> intent` is offered as the independent
   check. It is never run on Claude's own judgement. How to run it is
   in [Challenge the thinking](challenge-the-thinking.md).

   You should now see the independent check offered, and run only if
   you say so.

8. The round ends with Claude naming what changed and what stays
   open. When no thread blocks the layer below, it names the layers
   that can follow from the intent. Where the project takes no
   approval, it offers the approval instead. Either is a
   recommendation, never a gate.

   You should now see a closing summary of changes and open matters.

## The threads

Each open matter of the intent is a file in `threads/`, one file per
thread. The header of the file says:

- `concerns`: the artefact the thread concerns, named as `/forge`
  names it; several, comma-separated, where several.
- `origin`: where it came from, which is the principal (the default),
  a document by path, or Claude's synthesis.
- `status`: `open` or `closed`.

The body is the thread itself. Its first sentence is its headline and
its last dated paragraph is its state. A thread is freely rewritten
while it is open, header included. Once it is closed it is immutable
and stays as the archive. What comes back later is a new thread that
cites the old one.

If a conversation is unfinished when the session ends, it is saved
into its thread first, so that nothing lives only in the
conversation.

## What you have afterwards

- `10-intent.md` rewritten for coherence, in one new version.
- Its history, with one record per change.
- Threads that were resolved, closed, and the open ones saved with
  their state.
- The mined record of each brief the round touched.
- The ledger remade.

The working methods behind the round (one write per round, the
walkthrough, reflecting back) are described in
[The working methods](../about/working-methods.md). Any term of the
forge is in the [Glossary](../reference/glossary.md).

## If something goes wrong

- A thread stays open until you say it is closed. Claude does not
  close one on its own.
- The independent check is not run unless you ask for it.
- If a correction lands on text written moments ago, it belongs to
  the same round and is carried like any answer. It does not make a
  version of its own.
- If the session must end while a matter is unsettled, say so. Claude
  saves it into its thread before the end.

## A worked example

A project `my-project` has one brief that has not been mined, and one
open thread.

```
/forge intent my-project
```

Claude reads the brief and the thread and offers the brief first. It
takes the first theme, says what it understood as a short list of
positions and asks one question about a gap it found. You answer. It
reflects the answer back and moves to the next theme. When the themes
are done, Claude says the round seems complete and asks whether to
write.

You say `write`. Claude shows the new wording of the positions, the
facts and one rejected direction with its reason, and the history
records. You confirm, and the intent is written as one version. The
open thread is now resolved into a position, so it is closed. Claude
offers the independent check with a persona, you decline for now, and
the round closes with the line: one brief mined, one thread closed,
one thread still open, and the assignment named as the layer that can
follow.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
