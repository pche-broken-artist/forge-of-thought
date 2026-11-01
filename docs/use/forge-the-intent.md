---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 2e5f8220fecf5f48
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

`/forge intent` is the command that iterates the intent of a project, round by round, with Claude. This page is for the principal (the person whose thinking is being forged) who wants to bring a brief, an open thread or a new thought into the intent, and to know what happens in a round and what is written when.

## When to use it

Use it in any of these cases:

- The project has no intent yet and has one or more briefs. The briefs are consolidated into the first intent.
- A brief is pending or only partly mined. It is mined whole by whole, one brief at a time.
- A thread is open, you have a new word, or the recipients of an assignment sent something back. The round starts there.

Briefs are offered before threads. What the intent holds, and why it is rewritten for coherence, is explained in [The intent](../about/the-intent.md).

## The command

```
/forge intent [slug]
```

Without a slug, Claude resolves the project as `/forge` does for any state. The intent is the file `10-intent.md` of that project.

## What happens

1. Claude reads the briefs you say to mine, the decisions, the ledger (the state of the project, made from the documents when it is read), the intent as it stands and the project's `threads/`.

   You should now see Claude naming where the round starts: a brief, a thread, or your new word.

2. The round works one theme at a time. Claude probes contradictions, gaps and unstated assumptions, and asks of an idea two separate questions: is it good, and is it feasible. Nothing is recorded per idea from that asking. It offers options with their trade-offs, and proposes research where a thread needs outside grounding. Research runs only on your word.

   You should now see one theme in front of you, not the whole intent at once.

3. Your answers are carried in the conversation. Nothing is written yet. The way the conversation runs is described in [The working methods](../about/working-methods.md).

   You should now see Claude reflecting the answers back as structure.

4. The reality check comes last in the round, before any lower layer is proposed. Claude runs it with you. The independent check, a challenger run against the intent, is offered afterwards (see "The independent check" below).

   You should now see the joint check done, and the independent one offered.

5. At the natural end of the round Claude asks whether to write. You answer `write`. Claude first reflects the round back, showing the new wording and the records, and writes once the reflection is confirmed. The write rewrites the intent for coherence and never merely appends. One version is made for the whole round.

   You should now see the intent changed, with its history companion carrying the records of the round.

6. On the write, resolved threads move into positions or into rejected directions, and are closed. For every brief the round touched, the record of how far it is mined is kept. Claude then remakes the ledger.

   You should now see closed threads, and the ledger up to date.

7. The round ends with Claude naming what changed and what stays open. When the intent is complete for now (no thread blocks the next layer), it names the layers that can follow. Where the project takes no approval of the intent, it offers it instead. That is a recommendation, never a gate.

   You should now see a short statement of what changed, what is open and what can follow.

## Threads

Each open thread is a file in `threads/`, one file per thread. Its header says three things:

- `concerns`: the artefact the thread concerns, named as `/forge` names it. It lists several where several apply.
- `origin`: where the thread came from. This is the principal (the default), a document by path, or Claude's synthesis.
- `status`: `open` or `closed`.

While a thread is open it is freely rewritten, header included. Its first sentence is its headline and its last dated paragraph is its state. A closed thread is not edited, moved or deleted. A closed thread is the archive. If the matter returns, a new thread is opened that cites the old one. Closing happens only on your word.

An unfinished conversation is saved into its thread before the session (one run of Claude with you) ends, so that nothing lives only in the conversation.

## The independent check

The reality check Claude runs with you is joint. `/challenge <persona> intent` is the independent one: a reviewer who sees nothing of the conversation. Claude offers it once the joint check is done and never runs it on its own judgement. How to run it is described in [Challenge the thinking](challenge-the-thinking.md).

## What you have afterwards

- A new version of `10-intent.md`, with the round's records in `10-intent.history.md`.
- Resolved threads closed, the open ones saved in `threads/`.
- The ledger remade.
- A statement of what changed and what stays open.

## If something goes wrong

- A conversation ends before you say `write`: what was agreed lives only in the conversation. Ask Claude to save the unsettled matter into its thread first. A write you order mid-round does not close the round unless you say so.
- A correction lands on text written moments ago: it belongs to the same round and is carried like any other answer, not written as a version of its own.
- A thread seems done but you have not said so: it stays open, because a thread closes only on your word.

The inputs name no other stop conditions or messages for this command.

## A worked example

A project `my-project` has a brief and no intent yet.

```
/forge intent my-project
```

Claude reads the brief and says it will mine it whole. It takes the first theme, the reason the work exists, and asks what you want and why. You answer. Claude reflects your answer back as an essence and two candidate positions, and asks one question on whether the second is good and whether it is feasible. You say the second is good but far away, and that a third idea is dropped because it duplicates existing work. Claude carries both answers and moves to the next theme. One question stays unanswered.

At the end Claude runs the reality check with you, then asks whether to write. You say `write`. Claude shows the intent as it would read: an essence, the positions, a rejected direction with its reason, and one open thread for the unanswered question. You confirm, and the first intent is written as version 0.1 with its history. Claude names what changed, names the open thread as what stays open, and offers `/challenge <persona> intent` as the independent check.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
