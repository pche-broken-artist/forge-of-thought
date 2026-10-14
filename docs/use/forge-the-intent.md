---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: b9044ad893bbad4b
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
---

# Forge the intent

`/forge intent` is the command that iterates the intent, the file `10-intent.md` that holds what the principal currently wants and why. The principal is the person whose thinking is being forged. This page is for the principal who wants to work the intent round by round. For what the intent holds, see [The intent](../about/the-intent.md).

## When to use it

- You have a brief that has not yet been mined into the intent, or only in part.
- A thread is open and you want to settle it.
- You have a new word of your own about what you want.
- The recipients of an assignment sent something back, and you want it to change the intent.

## The command

```
/forge intent [slug]
```

The slug names the project. Where there is only one project, it can be left out.

## What happens

Claude resolves the project, then reads the briefs, the decisions file, the ledger (the file that holds the state of the project), the intent as it stands and the open threads. It then picks the way in.

1. **The way in is chosen.**
   - There is no intent yet: the briefs are consolidated into the first one.
   - A brief is pending or only partly mined: it is mined whole by whole, one brief at a time.
   - There is an open thread, a new word of yours or something the recipients sent back: the round starts there.

   Briefs are offered before threads.

   You should now see Claude name the way in and the first theme.

2. **One theme at a time.** Claude works a single theme with you. It probes contradictions, gaps and unstated assumptions. It asks of an idea whether it is good and, separately, whether it is feasible. It offers options with their trade-offs, and it proposes research where a thread needs grounding from outside. The wording is Claude's to propose, but the substance is yours, and a thread closes only on your word. How the conversation runs is described in [The working methods](../about/working-methods.md).

   You should now see one theme closed in the conversation, not yet in the file.

3. **The reality check comes last.** Once the themes are done, Claude runs the reality check with you, before any lower layer is proposed. It asks what of the intent is feasible and where the wheel already exists.

   You should now see the joint reality check done, and Claude offer the independent one: `/challenge <persona> intent`. A challenger is a reviewer run as a subagent, a helper that never sees your conversation. It runs only on your word. How to run it is in [Challenge the thinking](challenge-the-thinking.md).

4. **Claude reflects the round back.** Your answers are carried in the conversation, not written one by one. At the round's natural end Claude restates what it understood and asks whether to write.

   You should now see the round restated as structure, with the new wording, before anything is written.

5. **You say `write`.** The file is written once for the whole round. The intent is rewritten for coherence, never appended to. Resolved threads move into positions or into rejected directions, with the reason for each rejection. The Mined column of every brief touched is kept in the ledger. The change is recorded in the history companion of the intent, `10-intent.history.md`.

   You should now see Claude name the files and sections it wrote.

6. **The round ends.** Claude names what changed and what stays open. When no thread blocks the next layer, it names the layers that can follow from the intent. Where the project takes no approval, it offers the approval instead. This is a recommendation, never a gate.

   You should now see a short statement of what changed, what is open, and what can follow.

## What you have afterwards

- `10-intent.md`, rewritten for coherence, in the project's language. It has these sections:
  - Essence: what you want and why, as of today.
  - Positions: what you currently hold.
  - Facts: what is the case.
  - Rejected directions: what was dropped, and why.
  - Candidate structure for the layer below: an optional staging area for what the next layer will need.
- `10-intent.history.md`, with a record of each change.
- `threads.md`, the open threads of the project, one file for the whole project. Each thread names, in square brackets, the artefact it concerns. It has no version of its own. Whatever stays unsettled is saved into its thread before the session ends.

The first time, the intent is created from its template as a draft, with its history companion and the threads file.

## If something goes wrong

- A thread that you have not closed is never closed by Claude. It stays open in `threads.md`.
- If the conversation ends before a write, whatever is unsettled is saved into its thread. Whatever lived only in the conversation is not in any file.
- The intent says what would hold however the thing were realised. How it is realised belongs to the solution design, the layer below. If a theme turns into a how, Claude brings it back.
- The intent is complete for now when no thread blocks the next layer. It is never finished.

## A worked example

This is one round with a generic project, `my-project`, started from an open thread.

```
/forge intent my-project
```

Claude reads the brief, the intent and `threads.md`. No brief is waiting, so it offers the open thread "Who receives the assignment?" as the theme.

You talk it through. At first you say the recipients are the platform team. After a question about the second team that runs the same process, you change it to both teams. Claude asks whether this is good and whether it is feasible, and you answer both.

Claude proposes a short round-up: one position (both teams receive the assignment) and one rejected direction (a single recipient, dropped because the second team runs the same process). Claude then runs the reality check with you and offers `/challenge <persona> intent`. You decline for now.

Claude reflects the round back as the new wording and asks whether to write. You say `write`.

Claude rewrites the intent, moves the thread into the position and the rejection, records the change in the history, and says what stays open: two other threads. Neither blocks the next layer, so it names the layer that can follow.

## See also

- [The intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [The working methods](../about/working-methods.md): the named ways the conversation runs.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
