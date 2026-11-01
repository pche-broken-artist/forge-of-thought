---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 3b2b5855a67deeff
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

A brief is the principal's own text of one whole of thinking: what he
wants and why. The principal is the person whose thinking is being
forged, and the final authority on its content. This page explains
what a brief is, who writes it, what it holds and why it is rough on
purpose. It is for anyone who uses the forge and for anyone weighing
whether its way of starting a project is sound.

## What it is

A brief is the first artefact of every chain, that is, the first
versioned document a project's thinking travels through. It puts an
idea together. It holds what the principal wants, why he wants it,
and what he chose to take from the finding around it.

A brief is free form. Only a minimal header is fixed. Below it the
principal may use any structure he finds useful: prose, headings,
tables, lists or use cases. A brief has no required content and no
IDs, and none of the conventions of the chain apply to it.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position. Its thoughts may be changed, reworked or dropped
when it is mined, that is, when its thoughts are worked into
[The intent](the-intent.md). Only the intent turns them into
positions.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling is the intent's work: a brief is the raw piece, and the
intent is where it is shaped. A brief polished until the intent has
nothing left to do has gone too far. It is where thoughts are thrown
in before they are sifted. Not all of them survive, and the sifting
happens in the intent.

## Who writes and reads it

The brief belongs to the principal. Whatever stands in it he
approved, whoever first said it.

Claude (the AI assistant the forge runs on) helps compose it. At the
opening Claude is the active one. It brings how the same thing is
done elsewhere, verifies what can be verified, and proposes research
and the intake of outside material. Then, on the principal's word to
write, Claude writes down what the talk arrived at so that it is
understood. It may translate, mend the grammar and word an idea of
its own that the principal has accepted. It reflects back what it
has formulated before it is written. Claude does not decide what
goes in, and it does not chisel the brief into an intent.

The brief is read when it is mined into the intent. Positions mined
from it cite it as their provenance. The ledger (the table of a
project's state, built from its documents when it is read) has a
Briefs table with one row per brief.

## Made from

A brief is made from the principal's thought, however it arrives.
Around it, the finding gathers more:

- research notes, kept in `research/`;
- sources, the outside material kept in `sources/`;
- Claude's own proposals.

The finding is wide and gathers as many ideas as it can. The brief
is not the record of the finding. What goes in and what stays out is
the principal's decision, made on what was found. What stays out
lives in `research/` or `sources/` where it is a finding or a source.
Otherwise it lives nowhere.

A brief can arrive in one of three ways:

- finished from outside, and stored as it came;
- begun outside, and finished with Claude in the forge;
- born in the forge from the first word.

All three are equally legitimate. The forge does not distinguish
them.

## What it holds

The file is `00-brief.md` for the founding brief. A later whole of
thinking is a file of its own, `00-brief-<name>.md`. Each brief has
a history companion beside it, `<file>.history.md`, as every
versioned document has.

The fixed header is the one the template `templates/brief.md` gives:

- `project`: the slug of the project;
- `title`: a working title;
- `author`: the principal's handle;
- `version`: the version number;
- `status`: `draft`, `approved` or `superseded`.

Its usual shape is light:

- the topics of the whole;
- for each topic, a few sentences of what the principal wants of it;
- beside each, the research that verifies or limits it;
- what is still open.

Nothing in a brief marks who wrote what. Two marks may stand,
because they carry something other than authorship:

- `(source: <path>)`: stands where the identity of a source
  supports, limits or contradicts the thought. At mining it becomes
  a fact with its provenance.
- `(remark: …)`: a short note that stands where a reservation or an
  uncertainty must stay visible. It is named by what it is, not by
  who made it.

What merely inspired a thought carries no mark. It stays
discoverable through its research note. A suggestion or an
alternative the principal did not take is gone, unless he says it
stays.

A brief is kept in the language it is written in. It is the one
artefact that does not follow the language of its project. The
reason is not recorded here; [Languages](languages.md) covers the
languages of the forge.

### A worked example

A generic brief, its header as the template gives it and five lines
of text:

```
---
project: <slug>
title: <working title>
author: <principal>
version: 0.1
status: draft
---

We want new team members to be productive in their first week.
Today the knowledge sits in people's heads and in scattered notes.
What we want: one starting path, owned by the team, kept current.
What we do not want: a heavy portal nobody maintains.
Open: who keeps it current (remark: unclear whether anyone has time).
```

It has no headings, no IDs and no polish. Sorting it into positions
is left to the intent.

## Complete when

A brief is complete when the principal says so and approves it.
Before the approval is offered, Claude walks the Map of the brief's
definition once. The Map lists the areas the finding looks at. The
walk asks whether each area was consciously considered, and an area
may leave nothing in the brief.

A brief is versioned like every artefact. It is a draft until the
principal approves it, which makes it version 1.0. After that it is
changed as any artefact is. It is not locked and not immutable: what
it said at any version stands in its history and in git.

A brief may be mined into the intent when the principal says so,
approved or not.

## How it is found

A project may have more than one brief. The founding brief is
`00-brief.md`. A later whole of thinking that would otherwise land in
the intent as a batch of unproven positions is born as
`00-brief-<name>.md`. It has the same header, the same states and the
same rules.

Every brief is mined into the single intent of the project, when the
principal says so. How far each brief is mined is recorded in the
intent's history. The record is kept there because mining changes
the intent, not the brief. The ledger reads that record and shows it
in its Briefs table. "How much" is a judgement recorded in the
mining record and in the provenance of the positions, never a
metric.

A whole that dies on the way leaves its brief as it stands. The
intent then records one rejected direction with the reason, so the
trace survives either way.

How you compose a brief is shown in [Write a brief](../use/write-a-brief.md).
The terms used here are in the [Glossary](../reference/glossary.md).

## Why

- **No required structure.** A required structure would force
  premature tidiness. A templated brief with chapters (goal,
  high-level idea and so on) was rejected for that reason. No
  structure is forbidden either.
- **No second home for what the brief leaves out.** A draft intent
  beside a draft brief, a separate notes record and a new artefact
  before the brief were all rejected. The brief holds the
  principal's choice, and what he does not take needs no home. A
  finding or a source already has `research/` and `sources/`. What
  merely fell by in the conversation is gone with it.
- **No marks of authorship.** Whatever is in the brief the principal
  approved, whoever first said it. A mark that names a model also
  reads differently on every model the forge runs on. The two marks
  that stay are named by what they are so that they read the same on
  any model.
- **More than one brief.** A big new whole needs a place where the
  thought can be tempered before it enters the intent, without a new
  kind of document. It works much like a branch in git. A thread
  (one open matter of the intent) was wrong for it, because a thread
  is a question and not a body of work.
- **Rough on purpose.** The chiselling belongs to the intent. A brief
  that does the intent's work leaves the intent nothing to do.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
