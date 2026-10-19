---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 6c9fd56c3223cb26
inputs:
  - .claude/skills/challenger-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0420
  - projects/forge/10-intent.md#POS.0440
  - projects/forge/10-intent.md#POS.0450
  - projects/forge/10-intent.md#POS.0790
---

# The challenger

A challenger is an isolated reviewer that attacks the substance of
the thinking in a project, never the quality of its documents. This
page explains what a challenger does, how it works, what it produces
and why it is run the way it is. It is written for anyone who uses
the forge, extends it with a persona of their own, or weighs whether
its review can be trusted.

## What it is

A challenger reviews the thinking of the principal (the person whose
thinking is being forged, and who decides everything about it). It
works through a persona. A persona is one challenger with a register
of its own and the blind spots it exists to find. Each persona is
its own agent, defined by what it goes after; what every persona
shares is one contract, written once. The personas and what each
hunts are listed in
[Challenger personas](../reference/challenger-personas.md).

The challenger runs as a subagent (a separate run of Claude with a
context of its own). It never sees the working conversation. It
reviews as a peer: its report is a peer review, and it is not there
to agree with the principal.

Its subject is substance. Whether the wording is ambiguous, the
structure sound or an item traceable is not its concern. Those
questions belong to the critic lenses. Where the thinking is sound
and only the document is sloppy, the challenger says nothing.

Its target is one of three things:

- an artefact of the chain (one versioned document, such as the
  intent);
- any file of the project, named by its path, read with the chain
  around it, and a work product read with its specification;
- the whole chain, when no target is named.

Whatever the target, the challenger reads the whole chain above and
around it as context. That context covers the briefs, the intent,
the threads, the decisions, the sources where they exist, every
layer below the intent that exists, and earlier challenges. It reads
and never modifies. The challenges aim at the target only. Where a
file named as the target gives the persona nothing to work on, the
report says so and carries nothing else.

## How it works

The challenger works by a fixed set of rules, the same for every
persona:

- It reads for what is not there as much as for what is. Silence in
  the intent is its richest material.
- It grounds itself externally where a claim hinges on how the world
  actually works. It may search the web for how comparable
  organisations solve the problem and for known failure patterns,
  and it says whether a point is consensus, active debate, emerging
  practice or its own judgement.
- It never fabricates. A precise "I don't know the current figure"
  stands in place of an invented statistic. Any number, benchmark or
  citation reconstructed from memory is flagged as such.
- It corrects a flawed assumption in the material before building on
  it.
- It is concrete. A vague prompt to consider something is not a
  challenge; a named gap is.
- It returns three to seven challenges. Where it has nothing serious
  to say about something, it says nothing.
- It marks each challenge as a dealbreaker, major or minor, and
  orders them by that severity. A fatal flaw is never buried among
  cosmetic points.
- It is direct. Where the thinking is strong, it says so in one line
  and moves on.
- It never proposes edits, wording or structure. It challenges the
  thinking, and the principal decides what to do about it.
- It may be wrong. Where a challenge rests on facts it cannot verify
  from the documents, it says what it assumes and asks.

## What it produces

The challenger returns one report and writes no file. The report
opens with an overall read of what the work is about and whether it
is aimed at the right thing. Each challenge then carries:

- a severity (dealbreaker, major or minor);
- the challenge itself;
- why it matters;
- what would change the challenger's mind, stated so that it can be
  proved false;
- an epistemic status (consensus, active debate, emerging practice
  or the challenger's own judgement).

The report closes with what is genuinely strong and with the
questions the challenger cannot answer from the documents. Those
questions often sharpen or overturn a challenge. The reason is that
the principal knows things the challenger does not.

The `/challenge` command files the report in the project's
`challenges/` directory, under a dated name, and gives each challenge
its ID. It then offers a walkthrough (the challenges put to the
principal one per message, each closed with a verdict). How to run a
persona is described in
[Challenge the thinking](../use/challenge-the-thinking.md).

## Why

**Why it is best run before the next layer.** An artefact is best
challenged before the next layer is first derived from it, such as
the intent before the first assignment. At that point accepted
challenges are still cheap to absorb. Whether to run it again later,
after a draft or before approval, is left to the judgement of
whoever runs the process. No rule prescribes it.

**Why a rejected challenge is healthy.** Every challenge is either
fixed or explicitly rejected with a recorded reason. Rejecting and
parking are legitimate outcomes; silently ignoring is not. The
challenger may be wrong, and it says so itself. Its agreement with
other reviewers proves nothing either. The author, the critic and
the challengers share one model family, and what that family
systematically cannot see, none of them will find. Agreement only
means the artefact is consistent under one set of priors. So a
challenge is an input to the principal's judgement, not a verdict on
it. The calibration point lies outside: review by humans or by a
different model family, invited at the principal's discretion.

**Why an accepted challenge is mended where it needs to be.** An
accepted challenge is mended wherever it needs to be, and one that
mends nothing was not accepted. A challenge of a layer below the
intent is mended in that layer and changes nothing above it. The
exception is a challenge that shows what is wanted cannot be
realised, or only at a price not worth paying. Then a thread is
opened in the intent, citing the challenge, and what is wanted is
decided there. A challenge may inspire, but nothing enters the
intent because a reviewer wrote it. It enters only because the
principal composed it. An accepted challenge may change the intent
by taking something away as readily as by adding something.

## A worked example

A project `example-project` has an intent and no assignment yet. The
principal runs one persona against the intent before the first
assignment is derived, because changes are still cheap there.

The challenger reads the brief, the intent, the threads and the
decisions. It returns four challenges:

- A dealbreaker: the intent assumes that the teams it concerns will
  adopt the change, and no item names who loses by it. What would
  change its mind: a named owner who has agreed.
- A major challenge: the stated objective treats a symptom, and the
  cause is nowhere in the intent. Its epistemic status is its own
  judgement.
- Two minor challenges, one resting on a failure rate it flags as
  reconstructed from memory.

It adds one question it cannot answer from the documents: whether a
budget limit exists that the intent does not mention.

In the walkthrough the principal answers the question. The budget
limit exists, which settles one minor challenge. He rejects it with
that reason recorded. He accepts the dealbreaker, and it is mended in
the intent by a new position on ownership. He parks the major
challenge for a later round. Nothing is silently dropped.

## See also

- [Challenge the thinking](../use/challenge-the-thinking.md): running
  a persona.
- [Challenger personas](../reference/challenger-personas.md): the
  personas and what each hunts.
- [Add a challenger persona](../extend/add-a-challenger-persona.md):
  adding a persona of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
