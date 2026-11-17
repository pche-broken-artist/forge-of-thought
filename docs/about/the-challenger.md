---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: c4670437f13c6be2
inputs:
  - .claude/skills/challenger-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0420
  - projects/forge/10-intent.md#POS.0440
  - projects/forge/10-intent.md#POS.0450
  - projects/forge/10-intent.md#POS.0790
---

# The challenger

The challenger is the reviewer that attacks the substance of the
thinking in a project, through a persona chosen for the run. This
page says what a challenger attacks, how it works, what it returns
and why it may be wrong. It is for whoever runs a persona, adds one
or weighs what such a review is worth. Every term of the forge used
here stands in one line in the [Glossary](../reference/glossary.md).

## What it is

A challenger reviews the thinking, not the documents that carry it.
It writes as an equal of the principal (the person whose thinking is
being forged). Its report is headed a peer review.

It works through a persona. A persona is one isolated agent (a
separate run of Claude in a context of its own, which reads every
file it cites from disk in that run). Each persona has a register
(the role in whose voice it speaks) and is defined by the blind spots
it exists to find. What a persona goes after is said in the Lens
section of its own file. The personas the forge has are listed in
[Challenger personas](../reference/challenger-personas.md).

What all personas share is one contract. The contract is the same
whatever the persona: the subject, the way of working and the shape
of the report. This page describes that contract.

A new persona is created on the principal's decision, when it is
first needed, and only where its blind spots genuinely differ from
those of the personas that exist. Personas that would say the same
things in different words are noise. How one is added is described in
[Add a challenger persona](../extend/add-a-challenger-persona.md).

### What it attacks

The subject of a challenger is the substance of its target. The
quality of the documents is not its subject. Formal review of a
document (ambiguity, structure, traceability, measurability of
wording) belongs to the lenses of the critic (the reviewer of the
documents). The challenger does not duplicate it. Where the thinking
is sound and the document is sloppy, the challenger says nothing.

The target is one of these:

- an artefact of the chain (the documents of a project in their
  order: the briefs, the intent and the layers below it)
- any file of the project, named by its path and read with the chain
  around it
- a work product, read with its specification
- the whole chain, when no target is named. Each challenge then names
  the artefact or the file it concerns.

A file may give a persona nothing to work on. Its report then says so
and carries nothing else.

A persona is run with the command `/challenge`. Typed bare, the
command lists the personas and recommends one that fits the subject
of the project. Running one is described in
[Challenge the thinking](../use/challenge-the-thinking.md).

## How it works

### What it reads

The persona reads the whole chain above and around its target, and
modifies nothing:

- the briefs
- the intent (the document that says what is wanted)
- the threads (matters opened to be decided)
- the decisions
- the sources, where the project has them
- every layer below the intent that exists, such as an assignment, a
  BRD or a solution design
- the earlier reports in `challenges/`

All of this is context. The challenges aim at the target.

### How it challenges

- It reads for what is not there as much as for what is. Silence in
  the intent is its richest material.
- It grounds itself outside the documents where a claim hinges on how
  the world actually works: how comparable organisations solve the
  matter, what the known failure rates and patterns are. It uses web
  search for that, not for padding. On a purely technical trade-off
  it lets the mechanism lead, not an analyst's framework.
- It never fabricates. A precise "I don't know the current figure"
  beats an invented statistic or a citation that does not exist. Any
  number, benchmark or citation that it reconstructs from memory and
  has not verified is flagged as such.
- It corrects a flawed assumption in the material before it builds on
  it. A challenge stacked on the material's own error is worthless.
- It is concrete. "Consider stakeholder alignment" is worthless. "The
  owners of X and Y both lose scope under this and neither is named
  anywhere in the intent" is a challenge.
- It returns three to seven challenges. Sharp and few beats thorough
  and long. Where it has nothing serious to say about something, it
  says nothing about it.
- It marks every challenge with a severity (dealbreaker, major or
  minor) and orders the challenges by it. A fatal flaw is never
  buried in a flat list beside cosmetic ones.
- It gives every challenge an epistemic status: consensus, active
  debate, emerging practice or its own judgement.
- It is direct: no flattery, no hedging, no softening. Where the
  thinking is strong, it says so in one line and moves on. The
  principal needs signal, not encouragement.
- It never proposes an edit, a wording or a structure for a document.
  It challenges the thinking. The principal decides what to do about
  it.
- It may be wrong. Where a challenge rests on facts it cannot verify
  from the artefacts, it says what it assumes and asks.

### What it produces

The persona returns one report, in English, in its final message. It
writes no file. The report holds:

- a header: the date, the project, the target, every file read (with
  its version where it has one) and the persona with its register
- an overall read: what the initiative is really about as written,
  and an honest assessment of whether it is aimed at the right thing
- the challenges, in the order of their severity
- what is strong: brief, and only what genuinely is
- the questions it cannot answer from the documents: things the
  principal knows and the challenger does not. These often invalidate
  or sharpen a challenge.

Each challenge holds:

- a headline of one line
- its severity
- the challenge itself
- why it matters
- what would change the challenger's mind, falsifiable and concrete
- its epistemic status

### What happens to the report

The persona gives a challenge no ID and files nothing. The command
files the report in the `challenges/` directory of the project, the
name of the file completed by `scripts/forge-report.py`, and gives
each challenge its ID. Claude then offers a walkthrough (the
challenges put to the principal one by one, each for a verdict).

Every challenge is either mended or explicitly rejected, with the
reason recorded as a decision. Rejecting and parking are legitimate
outcomes. Silently ignoring a challenge is not.

```
the target, read with the chain around it
        |
        v
one persona, isolated:
three to seven challenges, ordered by severity
        |
        v
the report, filed in challenges/ by the command,
each challenge given its ID
        |
        v
the walkthrough: the principal judges each challenge
        |
        +--  accepted: mended wherever it needs to be
        +--  rejected: the reason recorded as a decision
        +--  parked
```

## Why

### Why a challenger may be wrong

A challenger works from the documents. The principal knows things it
does not, and such a thing can invalidate a challenge or sharpen it.
The questions at the end of the report name what the challenger could
not answer for itself.

Isolation is also not independence. The author, the critic and the
challengers share one model family. What that family systematically
cannot see, none of them will find. Agreement between the reviewers
is therefore never treated as validation. It only means that the
artefact is consistent under one set of priors. The calibration point
lies outside: review by humans or by a different model family,
invited at the principal's discretion.

### Why it is best run before the next layer

An artefact is best challenged before the next layer is first derived
from it: the intent before the first assignment, a BRD before the
solution design. Accepted challenges are then still cheap to absorb.
Whether a challenger runs again later, after a draft or before
approval, is left to the judgement of whoever runs the process. No
rule prescribes it.

### Why a rejected challenge is a legitimate outcome

Two things recorded about the challenger make a rejection an ordinary
outcome of a review, not a failure of it.

The challenger may be wrong. It says so itself, wherever a challenge
rests on something it assumes.

A challenge decides nothing. It may inspire. Nothing enters the
intent because a reviewer wrote it, only because the principal
composed it.

What the forge asks of a rejection is that it is explicit and that
its reason is recorded.

### Why an accepted challenge is mended where it needs to be

An accepted challenge is mended wherever it needs to be. One that
mends nothing was not accepted.

A challenge of a layer below the intent is mended in that layer and
changes nothing above it. The exception is a challenge which shows
that what is wanted cannot be realised, or only at a price not worth
paying. A thread is then opened in the intent, citing the challenge,
and what is wanted is decided there. Why the mend otherwise stays in
its own layer: the reason is not recorded.

A mend is not always an addition. An accepted challenge may change
the intent by subtraction as readily as by addition. In either case
the principal composes the wording, and the challenger proposes none.

## A worked example

A project with the placeholder slug `my-project` has an intent in
draft. The intent merges two intake processes into one. No layer
below the intent exists yet, so this is the cheap moment for a
challenge. The principal runs one persona on the intent.

The persona reads the brief, the intent, the threads and the
decisions. It returns four challenges, the gravest first. The first
one holds:

- Headline: the owners of the two intake processes both lose scope,
  and neither is named anywhere in the intent.
- Severity: major.
- Challenge: the intent says what is merged and by when. It is silent
  on who gives up what, and on who owns the merged process.
- Why it matters: the merge depends on both owners, and an owner who
  is not named has agreed to nothing on record.
- What would change my mind: a recorded decision that both owners
  have agreed to the merge, or an owner of the merged process named
  in the intent.
- Epistemic status: my judgement.

Among the questions it cannot answer from the documents, the persona
asks whether the two owners have been consulted.

Claude files the report and offers the walkthrough. The challenge can
end in two ways, and both are in order:

- The principal knows that the two owners proposed the merge
  themselves. The challenge rested on a fact the documents did not
  hold. The principal rejects it, and the reason is recorded as a
  decision. The intent stays as it is.
- The owners have not been asked. The principal accepts the challenge
  and composes the mend in the intent: an owner of the merged process
  is named, or one of the two processes is taken out of the merge.
  The persona proposed neither wording. No layer has been derived
  yet, and nothing below the intent has to follow.

## See also

- [Challenge the thinking](../use/challenge-the-thinking.md): running
  a persona.
- [Challenger personas](../reference/challenger-personas.md): the
  personas and what each hunts.
- [Add a challenger persona](../extend/add-a-challenger-persona.md):
  adding a persona of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
