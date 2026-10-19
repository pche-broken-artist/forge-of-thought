---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: f4575e375268a679
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0920
  - projects/forge/10-intent.md#REJ.0040
  - projects/forge/10-intent.md#REJ.0180
  - projects/forge/10-intent.md#REJ.0220
  - CLAUDE.md#Prime directives
---

# The brief

A brief is the principal's own text of one whole of thinking: what
he wants, why, and what he does not want. The principal is the person
whose thinking is being forged, and the final authority on what the
documents say. This page explains what a brief is, who writes it,
what it holds and why it is rough on purpose. It is for a user who is
about to write one and for an evaluator who wants to know why the
chain starts this way. How to compose one is on
[Write a brief](../use/write-a-brief.md).

## What it is

A brief is the first artefact of a project's chain. An artefact is a
versioned document of the chain, composed by the principal with
Claude. The brief puts an idea together: what the principal wants and
why, with what he chose to take from the work of finding around it.

A brief holds thoughts to be processed, not decisions. Its thoughts
may be changed, reworked or dropped when the brief is mined. Mining
means taking the brief's thoughts into the
[intent](the-intent.md), the project's working document of what the
principal currently holds. Only the intent turns a thought into a
position.

The brief is rough on purpose, neither perfect nor detailed. The
chiselling (the working of each thought into an exact, agreed form)
belongs to the intent. A brief polished until the intent has nothing
left to do has gone too far. The brief is where thoughts are thrown
in before they are sifted, and not all of them survive.

A brief is not the record of the finding. The finding is the wide
search around the idea: research, sources, the principal's ideas and
Claude's. The finding gathers as many ideas as it can. What goes into
the brief and what stays out is the principal's decision, made on
what was found.

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it.

Claude helps compose it. At the opening Claude is the active one: it
inspires, brings how the same thing is done elsewhere and how
original the idea is, verifies what can be verified, and proposes
research and the intake of sources. A proposal of Claude's, however
large, serves the finding and is not the brief.

When the brief is written, Claude forms the record. On the
principal's word to write, it writes down what the talk arrived at so
that it is understood. It may translate, mend the grammar and word an
idea of its own that the principal has accepted. What it has
formulated it shows back to the principal before it is written.
Claude does not decide what goes in. Claude does not chisel the brief
into an intent.

The brief is read when it is mined into the intent. A position mined
from it cites the brief as its provenance.

## Made from

The principal's thought, however it arrives, is the brief's material.
Around it, during the finding, stand:

- research notes in `research/`
- sources in `sources/`
- Claude's own proposals

The existing intent and the ledger are read only to know what already
stands, never to shape the text. The ledger is the project's single
record of state.

## What it holds

A brief opens with a minimal YAML header, the only fixed part. The
header comes from `templates/brief.md` and has these fields:

- `project`: the project's slug
- `title`: a working title
- `author`: the principal
- `version`: the version of the brief, starting at `0.1`
- `status`: `draft` until the principal approves it

Below the header the brief is free form. It may carry any headings,
tables, lists, prose or use cases the principal finds useful. It has
no required content, no IDs and no conventions of the chain.

Its usual shape is light:

- the topics of the whole
- for each topic, a few sentences of what the principal wants of it
- beside each, the research that verifies or limits it
- what is still open

A brief says what the idea is and why. It may carry a mechanism where
the mechanism is part of the idea.

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)`: stands where the identity of a source supports,
  limits or contradicts the thought; at mining it becomes a fact with
  its provenance.
- `(remark: …)`: a short note where a reservation or an uncertainty
  must stay visible, named by what it is and not by who made it.

What merely inspired a thought carries no mark. It stays discoverable
through its research note. A suggestion or an alternative the
principal did not take is gone, unless he says it stays.

A brief is kept in the language it is written in. Every other
artefact of the chain is in the project's language. The briefs are
the one exception among the artefacts. The reason for the exception
is not recorded. How the forge's languages fit together is on
[Languages](languages.md).

### A worked example

A generic brief with a five-line body, for a placeholder project
`my-project`:

```markdown
---
project: my-project
title: A shared calendar for the team
author: <principal>
version: 0.1
status: draft
---

I want one calendar the whole team can see, because meetings clash.
It should show who is away; nothing about tasks or time tracking.
Tools for this exist (source: sources/calendar-survey.md).
(remark: unsure whether guests from outside should see it)
Open: which existing calendar it replaces.
```

The body has no headings and no IDs. One thought cites a source, one
reservation stays visible as a remark, and one question is left open
for the intent.

## Complete when

The brief is complete when the principal says so and approves it.
Before the approval is offered, Claude checks once whether each area
of the finding has been considered:

- the thought: what the principal wants, why, and what prompted it
- the boundaries: what he does not want, and what is out of scope
- the world around it: what exists that does the same or the
  opposite
- the material: the sources and research the thought rests on
- what is still open: what was not decided or verified

An area may leave nothing in the brief. The check asks and does not
mend. A tension, an undecided alternative or a vague boundary may
stay in the brief as it is, because resolving it is the intent's
work.

A brief is approved only on the principal's explicit word. It is
versioned like every artefact: a draft until approved, then `1.0`,
and changed after that as any artefact is. It is not locked and not
immutable. What it said at any version stands in its history and in
git.

## How it is found

A brief has three origins, all equally legitimate, and the forge does
not tell them apart:

- It arrives finished from outside and is stored as it came.
- It is begun outside and finished with Claude.
- It is born with Claude from the first word.

For the last two, the brief is worked through `/forge brief`. Claude
moves the principal to say what he wants, why and what he does not
want. A summary or a structured proposal the principal asks to record
is stored as shown, never retold.

When the talk turns to taking the idea apart and agreeing it piece by
piece, Claude says in one sentence that this is the intent's work. It
offers once to go on in the intent, as a recommendation and never as
a gate. No walkthrough (the forge's way of working a list of items
with the principal one item at a time) runs over the text of a
brief.

A project may have more than one brief. The founding brief is
`00-brief.md`. A later whole of thinking that would otherwise land in
the intent as a batch of unproven positions is born as
`00-brief-<name>.md`, with the same header, the same states and the
same rules.

A brief is mined into the single intent when the principal says so,
approved or not. How far each brief is mined is recorded in the
intent's history, in the record of the mining. The record stands
there because mining changes the intent and not the brief. Positions
mined from a brief cite it, and the version they were mined at is
the one the mining record names. The ledger shows one row per brief.
How much of a brief is mined is a judgement, recorded in the mining
record and in the provenance of the positions, never a metric. A
whole that dies on the way leaves the brief as it stands and one
rejected direction in the intent with the reason. The trace survives
either way.

## Why

No structure is required of a brief. A required structure would
force premature tidiness. A templated brief with fixed chapters (a
goal, a high-level idea and so on) was rejected for this reason. None
is forbidden either.

The brief is rough because the chiselling belongs to the intent. The
brief is where thoughts are gathered; the intent is where they are
sifted and made exact.

What the finding yields and the brief does not take has no second
home. A draft intent beside a draft brief, a separate kind of notes
and a new artefact before the brief were all rejected. The brief
holds the principal's choice. A finding or a source already has
`research/` and `sources/`. What merely fell by in the conversation
is gone with it.

Nothing marks authorship because what is in the brief the principal
approved, whoever first said it. A mark naming a model was also
rejected because it reads differently on every model the forge runs
on. A remark is named by what it is for the same reason: so that it
reads the same whatever model the forge runs on.

A later brief exists because a big new whole needs a place where the
thought can be tempered before it enters the intent, much like a git
branch, without a new kind of document. An open thread was the wrong
place for it, because a thread is a question and not a body of work.
A working space with positions before the merge was judged too heavy
for now.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
