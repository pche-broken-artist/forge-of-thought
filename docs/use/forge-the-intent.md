---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 29aaa0563d4a0a53
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

`/forge intent [slug]` iterates the intent, the file `10-intent.md`, one round at a time. This page is for the principal, the person whose thinking is being forged, who wants to bring briefs, open threads or new thoughts into the intent. A round is one working conversation with Claude that ends in one write.

## When to use it

Use it in any of these cases:

- You have no intent yet and want the briefs consolidated into the first one.
- A brief is pending or only partly mined.
- A thread is open and you want to work on it.
- You have a new word of your own to bring in.
- The recipients of an assignment have sent something back.

## The command

```
/forge intent <slug>
```

The slug names the project. Where it is left out, Claude resolves the project itself.

## What happens

1. Claude resolves the project and reads the briefs you say to mine, the decisions, the ledger and the intent as it stands, together with the project's threads.

   You should now see Claude start from the way in that fits: a first intent, a brief to mine, or a thread or word to take up.

2. The round starts where you are. Briefs are offered before threads. A brief is mined whole by whole, one brief at a time. A thread, a new word of yours or what the recipients sent back starts a round of its own.

   You should now see one brief or one thread offered as the start of the round.

3. The round runs one theme at a time. Claude probes contradictions, gaps and unstated assumptions. It asks two questions about an idea and keeps them apart: whether the idea is good, and whether it is feasible. It offers options with trade-offs and may propose research where a thread needs outside grounding. Research runs only on your word.

   You should now see answers carried in the conversation, not written one by one. They are written at the end, as step 5 says.

4. The reality check comes last, before a lower layer is proposed. Claude runs it with you, and you can then ask for the independent one with `/challenge <persona> intent`. Claude only offers it and never runs it on its own judgement. How it runs is on [Challenge the thinking](challenge-the-thinking.md).

   You should now see what of the intent is feasible, and where the wheel already exists.

5. Claude reflects the round back as structure and asks whether to write. You confirm with `write`. The intent is rewritten for coherence, never appended to, and the whole round is one version with its changes recorded in the history. Resolved threads move into positions or rejections and are closed. The mining of each brief you touched is recorded.

   You should now see Claude name the file and the section it wrote.

6. The round ends by naming what changed and what stays open. Where the intent is complete for now, Claude names the layers that can follow from it. Where you take no approval for the intent, it offers the approval instead. Both are a recommendation, never a gate.

   You should now see a short statement of what changed, what stays open and what can follow.

## The threads

The open matters of the intent are files in `threads/`, one file per thread. Each file's header says what it concerns, where it came from and whether it is open:

```
---
id: THR.NNNN
concerns: intent
origin: the principal
status: open
---
```

- `concerns` is the artefact the thread concerns, named as `/forge` names it. It lists several where several apply.
- `origin` is your word, a document by its path, or Claude's own synthesis.
- `status` is `open` or `closed`.

The first sentence of a thread is its headline. Its last dated paragraph is its state. A thread is freely rewritten while it is open, and its debate stays in it until it is settled. A thread closes only on your word. Closing sets `status: closed` and adds a `closed` record to the intent's history. A closed thread is never changed, moved or deleted, and it stays as the archive. A matter that returns is a new thread that cites the old one.

An unfinished conversation is saved into its thread before the session ends. A session is one run of Claude from start to end.

## What you have afterwards

- A rewritten `10-intent.md` with its essence, positions, facts and rejected directions, and a new version.
- A history companion, `10-intent.history.md`, with one record per change and the mining record of each brief touched.
- Threads that were settled, closed, and open threads that hold the state of what is unfinished.
- A remade ledger. The ledger is the state of the project, made at read time from the documents.

## If something goes wrong

The inputs record no stop conditions and no messages for this job. The one rule that applies: whatever remains unsettled is saved into its thread before the session ends, so nothing lives only in the conversation.

## A worked example

A generic round on a project with the placeholder slug `my-idea`, started from an open thread.

```
/forge intent my-idea
```

Claude reads the intent and the threads and offers the one open thread, which asks whether the idea needs a first version for a pilot team. It leaves the other themes for later. You answer, Claude probes one gap in the answer, and you settle it. A second theme follows in the same way. Nothing is written yet.

Claude then reflects the round back: one new position, one fact, and one direction dropped with its reason. You say `write`. Claude rewrites the intent, bumps its version, records the changes in the history, and closes the thread, whose matter is now a position and a rejection. It ends by saying what changed, that one thread still stays open, and that the intent is ready for the independent check with `/challenge <persona> intent`.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
