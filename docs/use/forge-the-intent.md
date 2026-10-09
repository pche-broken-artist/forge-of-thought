---
generated: 2026-10-09
made: mirrored
inputs-hash: f0f2fb8f6967d9fa
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - CLAUDE.md
---

# Forge the intent

This page is for the person who wants to build or extend the intent of a project: `/forge intent [slug]` iterates `10-intent.md`, the document that holds what you want, what is the case, what is open and what you dropped. It says how a round runs and what you see at its end.

## Start a round

Run `/forge intent`, with the project's slug if more than one project is in play. Claude reads the briefs you say to mine, the project's decisions and ledger, and the intent as it stands together with the open threads. Sources are read only as you direct.

A round starts in one of these ways:

- **No intent yet.** The briefs are consolidated into the first one.
- **A brief pending or partly mined.** It is mined whole by whole, one brief at a time.
- **An open thread, a new word of yours, or what the recipients sent back.** The round starts from there.

Briefs are offered before threads.

## What happens in the round

- Claude works one theme at a time. It probes contradictions, gaps and unstated assumptions, and asks of an idea whether it is good and whether it is feasible, as two separate questions.
- Ideas are placed on a horizon where you see one: a proof of concept, the first version, a later one, or good but far away.
- Claude may propose research where a thread needs outside grounding. It runs only on your word.
- The reality check comes last, before a lower layer is proposed.
- Your answers are carried in the conversation, not written one by one. When the round reaches its natural end, Claude reflects the round back to you first, then asks whether to write. The word to write is `write`.

The intent is composed by you: Claude shapes structure and wording, you decide the substance, and a thread closes only on your word.

## What the write does

One write per round, one version bump for the whole round, its changes recorded in the history companion beside the intent.

- The intent is rewritten for coherence, never appended to.
- Threads you resolved move into positions or into rejected directions, which keep the reason they were dropped.
- The Mined column of every brief touched is kept in the ledger, so you can see which briefs have been mined.
- The first intent is created from the template as version 0.1, together with its history companion and the threads file.

The open threads live in `threads.md`, beside the intent. They are part of the intent as its history is: the intent says what holds, the threads say what is being worked. The file is freely rewritten and has no version, no history and no ledger row of its own. Every thread names, in square brackets right after its ID, the artefact it concerns. Anything still unsettled when the session ends is saved into its thread.

## How the round ends

Claude names what changed and what stays open. When no thread blocks the next layer, it names the layers that can follow from the intent. Where the project takes no approval, it offers the approval instead. This is a recommendation, never a gate.

## The independent reality check

Once the joint reality check is done, Claude offers `/challenge <persona> intent` as the independent one. It never runs on Claude's own judgement; you start it. How it runs is on [Challenge the thinking](challenge-the-thinking.md).

## See also

- [About the intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [About the working methods](../about/working-methods.md): the named ways the conversation runs, one write per round among them.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
