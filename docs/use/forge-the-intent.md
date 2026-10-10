---
generated: 2026-10-10
made: mirrored
inputs-hash: b3576d4e9ea67bae
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - CLAUDE.md
---

# Forge the intent

This page is for the person who holds the thinking in a project and
wants to work the intent, `10-intent.md`, with Claude. It says how a
round of `/forge intent [slug]` runs, what you do in it and what
ends up in the files.

## Start a round

Run `/forge intent` with the project's slug if you have more than one.
Claude resolves the project, then reads the briefs you say to mine,
the decisions, the ledger, the intent as it stands and the project's
open threads. A round starts in one of these ways:

- **No intent yet.** The briefs are consolidated into the first
  intent.
- **A brief pending or partial.** It is mined whole by whole, one
  brief at a time.
- **An open thread, a new word of yours, or what the recipients sent
  back.** The round starts from there.

Briefs are offered before threads.

## What happens in the round

- One theme at a time. Claude helps you reach the intent's aim: it
  probes contradictions, gaps and unstated assumptions, offers
  options with their trade-offs, and proposes research where a thread
  needs outside grounding. You decide the substance, and a thread
  closes only on your word.
- Your answers are carried in the conversation and reflected back as
  structure. Nothing is written answer by answer.
- The reality check comes last, before a lower layer is proposed. It
  asks what of the intent is feasible and where the wheel already
  exists.

## Write, once per round

When the round reaches its natural end, Claude asks whether to write.
On your word, `write`, it first reflects the whole round back, then
writes once: one version for the round, its changes recorded in the
history beside the intent. The text is rewritten for coherence, never
appended. When Claude says something is written, it names the file
and section.

On the write:

- Resolved threads move into positions or into rejected directions,
  with the reason.
- The Mined column of every brief touched is kept.
- Whatever stays unsettled is saved into its thread before the
  session ends.

## Where things live

The intent holds what you hold: positions, facts, rejected directions
and, where the project takes a layer below, a staging area of what
that layer will need. The open threads live in `threads.md`, one file
for the project, beside the intent. Each thread names, in square
brackets after its number, the document it concerns. The threads are
freely rewritten: they have no version, no history and no ledger row
of their own. A first intent is made from the templates as version
0.1, with its history and its threads file.

## End of the round

Claude names what changed and what stays open. When no thread blocks
the next layer, it names the layers that can follow, or offers the
approval where you take none. This is a recommendation, never a gate.

## The independent reality check

Once the joint reality check is done, Claude offers
`/challenge <persona> intent` as the independent one. It is run only
when you say so, never on Claude's own judgement.

## See also

- [About the intent](../about/the-intent.md): what the intent holds and why it is rewritten for coherence.
- [About the working methods](../about/working-methods.md): the named ways the conversation runs, one write per round among them.
- [Challenge the thinking](challenge-the-thinking.md): running the independent reality check.
