---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - CLAUDE.md
---

# Forge the intent

This page is for the person who runs a project in the forge and wants
to work the intent: it says what `/forge intent [slug]` does, how a
round of it goes and what you see at the end. Without a slug the
command works the project you are in.

## What the command works on

`/forge intent` iterates `10-intent.md`, the document in which your
briefs are chiselled into what you hold: positions, facts, rejected
directions and, beside it, the open threads. It is where you and
Claude find out what you want and why, and it is never finished; it
is complete for now when no open thread blocks the layer below.

## How a round starts

Claude reads the briefs, the decisions, the ledger, the intent as it
stands and the threads. Then the round starts in one of these ways:

- **No intent yet.** The briefs are consolidated into the first
  intent.
- **A brief pending or only partly mined.** The brief is mined whole
  by whole, one brief at a time, with you.
- **An open thread, a new word of yours, or what the recipients sent
  back.** The round starts from there.

Briefs are offered before threads.

## How a round goes

- **One theme at a time.** Claude works the theme with you, probes
  contradictions, gaps and unstated assumptions, and asks whether an
  idea is good and whether it is feasible, as two separate questions.
  Where a thread needs grounding from outside, Claude proposes
  `/research`, which runs on your word.
- **The reality check comes last,** before a lower layer is proposed.
  Claude does it with you first. Then `/challenge <persona> intent`
  is offered as the independent reality check; it is never run on
  Claude's own judgement. How to run it: see Challenge the thinking.
- **Answers are carried in the conversation.** Nothing is written
  answer by answer. At the natural end of the round Claude asks
  whether to write, and you say `write`. Before writing, Claude
  reflects the round back to you, so that the write confirms and does
  not surprise.
- **One write per round.** The intent is rewritten for coherence, not
  appended to, with one version bump for the whole round and its
  changes recorded in the history companion. Resolved threads move
  into positions or rejections, and the Mined column of every brief
  touched is kept in the ledger.
- **Anything unsettled is saved into its thread** before the session
  ends, so that it is not left only in the conversation.

## The threads file

The open threads live in `threads.md`, beside the intent. A thread is
what is being worked: the working debate stays in it until it is
settled, while the intent says only what holds. The file is freely
rewritten and has no version, no history of its own and no row in the
ledger. Every thread names, in square brackets right after its
identifier, the artefact it concerns, for example `[intent]`; several
where it concerns several. A new project gets the file from the
template at the first intent.

## How a round ends

Claude names what changed and what stays open. When the intent has
reached its completion for now, Claude names the layers that can
follow from it, or, where you take no approval, offers the approval.
This is a recommendation, never a gate: you decide whether to go on.

## See also

- [About the intent](../about/the-intent.md): what the intent holds
  and why it is rewritten for coherence.
- [About the working methods](../about/working-methods.md): the named
  ways the conversation runs, one write per round among them.
- [Challenge the thinking](challenge-the-thinking.md): running the
  independent reality check.
