---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: e5f12fa35e9f2775
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
---

# Forge the intent

This page shows how you iterate the intent of a project with `/forge intent`, round by round. The intent is the file `10-intent.md`, where what the principal (the person whose thinking is being forged) holds is kept as positions, facts and rejected directions. It is written for the principal who sits down to work it. For what the intent holds and why it is rewritten for coherence, see [The intent](../about/the-intent.md).

## When to use it

Use it in any of these cases:

- The project has briefs and no intent yet. A brief is the principal's own text of what he wants, why and what not.
- A brief is new or only partly mined.
- A thread is open. A thread is one unresolved matter that is worked next.
- You have a new word to add.
- The recipients of an assignment sent something back.

## The command

```
/forge intent my-project
```

The slug is optional. Without it, Claude resolves the project from where you work. Replace `my-project` with the slug of your project.

## What happens

1. Claude reads the briefs you say to mine, the record of decisions, the ledger (the project's state table, remade by a script) and the intent as it stands, together with the open threads in `threads/`.
   You should now see Claude say where the round starts.
2. The round starts where the project stands.
   - With no intent yet, the briefs are consolidated into the first one.
   - With a brief pending or partly mined, Claude mines it whole by whole, one brief at a time.
   - With an open thread, a new word of yours or what the recipients sent back, the round starts there.

   Briefs are offered before threads.
   You should now see one starting point offered, with a brief ahead of a thread.
3. The round works one theme at a time. Claude asks questions and probes contradictions, gaps and unstated assumptions. It asks of an idea whether it is good and whether it is feasible, as two separate questions. It may offer options with their trade-offs and may propose research where a thread needs outside grounding; the research runs on your word.
   You should now see one theme in the conversation, not the whole intent at once.
4. The joint reality check comes last, before any layer below the intent is proposed. It asks what of the intent is feasible and where the wheel already exists.
   You should now see Claude go through what the intent found, and name any area that stays empty because it was considered and found not to apply.
5. Claude offers the independent reality check, `/challenge <persona> intent`. It is offered once, after the joint check, and never run on Claude's own judgement. Running it is described in [Challenge the thinking](challenge-the-thinking.md).
   You should now see the offer, and nothing run until you say so.
6. Answers are carried in the conversation, not written one by one. At the natural end of the round Claude reflects the whole round back: the new wording and the records that go with it. You answer `write`, and only then are the files written, once for the round. The way the conversation runs is described in [The working methods](../about/working-methods.md).
   You should now see Claude name the files and sections it wrote.
7. On the write, resolved threads move into positions or rejected directions and are closed. The mining of every brief touched is recorded, and the ledger is remade.
   You should now see the closed threads gone from the open ones and their substance standing in the intent.
8. The round ends by naming what changed and what stays open. When the intent is complete for now, that is, no open thread blocks the layer below, Claude names the layers that can follow. Where you take no layer below, it offers the approval of the intent instead. Either is a recommendation, never a gate.
   You should now see a short statement of what changed, what is open and what can follow.

## The threads

The open threads are files in `threads/`, one file per thread. Each file opens with a header that says three things:

- `concerns`: the artefact the thread concerns, named as `/forge` names it, several where several.
- `origin`: where the thread came from: the principal's word (the default), a document by its path, or Claude's own synthesis.
- `status`: `open` or `closed`.

A thread is freely rewritten while it is open, its header included. It has no version and no history of its own. It is never moved, renamed or deleted. Closing a thread sets `status: closed` and adds a record to the intent's history saying when and by what; the closed file stays as the archive. A matter that returns is a new thread that cites the old one. A thread closes only on your word.

Whatever stays unsettled when a conversation ends is saved into its thread before the working session closes. The ledger holds one line for it at most, never its substance.

## What you have afterwards

- `10-intent.md` rewritten for coherence: nothing twice, every position with its provenance.
- Its history companion, with one record per change and the mining records of the briefs touched.
- Resolved threads closed and the rest still open in `threads/`.
- The ledger remade.

The intent says what would hold however the thing were realised. How it is realised belongs to the solution design where the project has one, and to the item itself where it has none.

## If something goes wrong

- The intent is a conversation, not a script, so no message is printed for it. If a round stalls, ask Claude to save what is unsettled into its thread, and take the matter up in the next round.
- If Claude writes before you said `write`, or writes one answer at a time, stop it. One write per round, on your word, is the rule.
- If a theme is not yours to settle now, answer with the verdict `park`. It stays an open thread.

## A worked example

A project `my-project` has one brief and no intent.

1. You type `/forge intent my-project`. Claude finds the brief and offers to mine it first.
2. Claude takes the first theme, the reasons for the work. It asks what you want and why, and whether the idea is also feasible. You answer in your own words.
3. Claude takes the second theme, the recipients. You say you are not sure. Claude does not fill the gap; it notes that the matter is undecided.
4. Claude reflects the round back as a structure: an essence, two positions, one fact, one rejected direction with its reason, and one open thread about the recipients.
5. You say `write`. The intent is created as a first draft with its history, the open thread lands in `threads/`, and the brief is recorded as mined.
6. Claude names what changed and what stays open. It offers `/challenge <persona> intent` as the independent check. You decline it for now, so nothing runs.

In the next round you type the same command. The thread about the recipients is now the starting point, since no brief is left unmined. When you settle it, the thread moves into a position and is closed on the write.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
