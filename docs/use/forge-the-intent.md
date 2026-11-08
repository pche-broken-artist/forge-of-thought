---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: d9c629ec1c717b83
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

`/forge intent` iterates the intent, the file `10-intent.md` that holds what the principal wants and holds, round by round. This page is for the principal, the person whose thinking is being forged, who runs the command and decides the content. For what the intent holds and why it is rewritten for coherence, see [The intent](../about/the-intent.md).

## When to use it

Use it in any of these cases:

- The project has briefs and no intent yet.
- A brief is new or only partly mined.
- A thread is open and you want to work it.
- You have a new word to add.
- The recipients of an assignment sent something back.

## The command

```
/forge intent [slug]
```

The slug names the project. The command resolves the project, then reads the briefs you say to mine, the decisions record, the ledger (the state of the project, made when it is read) and the intent as it stands, together with its open threads.

## What happens

1. **Claude picks the way in.**
   - With no intent yet, it consolidates the briefs into the first one.
   - With a brief pending or partly mined, it mines that brief whole by whole, one brief at a time.
   - With an open thread, a new word of yours or what the recipients sent back, the round starts there.
   - Briefs are offered before threads.

   You should now see Claude name where the round starts.

2. **The round works one theme at a time.** Claude probes contradictions, gaps and unstated assumptions. It asks of an idea whether it is good and whether it is feasible, as two separate questions. It reflects a brain-dump back as structure before anything is written, and it offers options with trade-offs. Where a thread needs outside grounding it proposes research, which runs on your word. Claude composes the wording and you decide the substance. These are the [working methods](../about/working-methods.md) of the conversation.

   You should now see one theme in play, with your answers carried in the conversation and not written yet.

3. **The reality check comes last.** Once the themes are done, Claude and you check together what is feasible and where the wheel already exists. Then Claude offers `/challenge <persona> intent` as the independent check. It is offered once the joint check is done and never run on Claude's own judgement. How to run it is in [Challenge the thinking](challenge-the-thinking.md).

   You should now see the offer of the independent check.

4. **Claude reflects the round back and asks to write.** It restates what it understood, so that the write confirms and does not surprise. It writes once per round, on your word `write`, as one version for the whole round. The text is rewritten for coherence and not appended to.

   You should now see the restated round and the question whether to write.

5. **The write settles the round.**
   - Threads you have resolved move into positions or rejections and are closed.
   - The mining of every brief touched is recorded.
   - The history companion records the changes.
   - The ledger is remade.

   You should now see the intent written and the threads closed.

6. **The round ends.** Claude names what changed and what stays open. When no thread blocks the next layer, it names the layers that can follow. Where the project takes no approval it offers one instead. This is a recommendation and never a gate.

   You should now see what changed, what stays open and what can follow.

## The threads

The open threads are files in `threads/`, one file per thread. A thread is part of the intent: the intent says what holds, the threads say what is being worked, the working debate included until the thread is settled. The header of each thread file says three things:

- `concerns`: the artefact the thread concerns, named as `/forge` names it, several where several.
- `origin`: where the thread came from. This is you (the default), a document by path, or Claude's synthesis.
- `status`: `open` or `closed`.

The header and the text are freely rewritten while the thread is open. A thread closes only on your word. Closing sets `status: closed` and adds a `closed` record to the intent's history, saying when and by what. A closed file is immutable and stays as the archive. A thread is never moved, renamed or deleted. What returns is a new thread that cites the old one.

An unfinished conversation is saved into its thread before the session ends, so that nothing lives only in the conversation.

## What you have afterwards

- `10-intent.md` rewritten for coherence, in the sections of the template:
  - the essence, what you want and why, as of today;
  - the positions;
  - the facts;
  - the rejected directions, each with its reason;
  - optionally, the candidate structure for the layer below, such as the recipients, the objective and the success criteria.
- The history companion of the intent, with a record for each change.
- Threads closed where they were resolved, and the rest still open in `threads/`.
- The briefs touched, marked as mined.

## If something goes wrong

The definition names no error messages for this command. Its stopping conditions are these:

- A thread closes only on your word, so Claude leaves an unresolved one open.
- Nothing is written until you say `write`. If you want a write before the round is over, you may order it at any moment. It does not close the round unless you say so.

## A worked example

This is one generic round on a project `my-project` with one pending brief and one open thread.

```
/forge intent my-project
```

1. Claude reads the pending brief and the open thread. It offers the brief first and proposes to mine it whole by whole. You agree.
2. It takes the first theme, say who the recipients are. It asks whether the idea is good and, separately, whether it is feasible. You answer, and Claude reflects the answer back as a draft position.
3. The second theme resolves the open thread, which asked whether one capability is in the first version or later. You decide it is later. Claude proposes a rejection or a deferral, with your reason.
4. The reality check follows: Claude and you check what is feasible and what already exists elsewhere. Claude then offers `/challenge <persona> intent` and you decline for now.
5. Claude reflects the round: two new positions, one fact, one deferral, the brief mined and the thread resolved. It asks whether to write. You say `write`.
6. The intent is rewritten as one new version, the thread is closed and the history records each change. Claude reports that the first version of the recipients is settled, that one question about the objective stays open, and that the assignment can follow once it is answered.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
