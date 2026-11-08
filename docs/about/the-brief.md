---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: e464440a3eb494d0
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

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from the finding around it.
The principal is the one whose thinking is being forged. This page
says what a brief is, who writes and reads it, what it holds, when it
is complete and why it is rough on purpose. It is for the user who
starts a project and for the evaluator who wants to know what the
first artefact of the chain is and is not. How to compose one is
[Write a brief](../use/write-a-brief.md); every term of the forge is
in the [Glossary](../reference/glossary.md).

## What it is

The brief is the first artefact of a project's chain, the file
`00-brief.md`. An artefact is a document of the chain, one of the
versioned documents a project's thinking travels through. A later
whole of thinking, born during the project's life, is a brief of its
own, `00-brief-<name>.md`. It carries the same header, the same
states and the same rules.

A brief is free form. Below a minimal YAML header the principal may
use any structure he finds useful: prose, headings, tables, lists,
use cases. No content is required. No IDs appear in it, and none of
the conventions of the chain. A summary the principal orders into a
brief is stored as shown, never re-narrated.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position. Its thoughts may be changed, reworked or dropped
when they are mined, and only the intent turns them into positions.
The intent is the working document in which the principal's thinking
is consolidated: [The intent](the-intent.md).

A brief is rough on purpose, neither perfect nor detailed. The
chiselling belongs to the intent. A brief polished until the intent
has nothing left to do has gone too far. Its usual shape is light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it;
- the research that verifies or limits a topic, cited beside it;
- what is still open.

A brief is composed in a round or two and then mined. It is the place
where thoughts are thrown in before they are sifted: not all of them
survive, and the sifting belongs to the intent.

A brief is not the record of the finding. The finding is wide, made
of research, sources, the principal's ideas and Claude's, and it
gathers as many ideas as it can. What goes into the brief and what
stays out is the principal's decision, made on what was found. What
stays out lives in `research/` or `sources/` where it is a finding or
a source, and otherwise nowhere.

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it. Claude forms the record: on the principal's word to
write, it takes what the talk arrived at and writes it down so that
it is understood. Claude may translate, mend the grammar and word an
idea of its own that the principal has accepted. What Claude does not
do is take the brief over: it does not decide what goes in, and it
does not chisel the brief into an intent.

Three origins of a brief are equally legitimate, and the forge does
not distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

`/forge brief [name]` is the door for the latter two.

The brief is read when it is mined into the single intent through
`/forge intent`. A position mined from it cites the brief as its
provenance, with the version it was mined at. The ledger reads the
brief's header and the record of the mining in the intent's history.
The ledger is the project's single source of truth for state, made
at read time by a script. Its Briefs table shows one row per brief
and how far each is mined, pending until a mining record exists.

## Made from

A brief is made from the principal's thought, however it arrives.
Around it, gathered during the elicitation, stand research notes in
`research/`, sources in `sources/` and Claude's own proposals. The
existing intent and the ledger are read only to know what already
stands, never to shape the text.

A new brief is created from `templates/brief.md`, which is the
minimal YAML header and nothing else, with its history companion
`<file>.history.md` from `templates/history.md`. A brief is versioned
as every artefact is, and its history lives in that companion.

## What it holds

Only the header is fixed. It carries the project's slug, a working
title, the author, the version and the status. The text below it is
free form.

A brief says what the idea is and why. It may carry a mechanism where
the mechanism is part of the idea.

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact
  with provenance. What merely inspired the thought carries no mark
  and stays discoverable through the research note.
- a short `(remark: …)` stands where a reservation or an uncertainty
  must stay visible. It is named by what it is, not by who made it.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

A brief is kept in whatever language it is written in. It is the one
exception among the artefacts, which otherwise follow the project's
language. Why a brief keeps its language is said in
[Languages](languages.md); the reason is not recorded here.

## Complete when

A brief is complete when the principal says so and approves it. The
Map of its definition is walked before the approval is offered. The
Map is of the finding, not of the brief: it names what the finding
looks at, and what of it enters the brief is the principal's choice.
It is walked once, at the closing, and asks one question of each
area: has it been consciously considered? The areas are:

- the thought: what the principal wants, why, and what prompted it;
- the boundaries: what he does not want, and what is out of scope;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or proof
  that the wheel exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  finding.

An area may leave nothing in the brief. The walk asks and does not
mend: a tension, an alternative left undecided or a boundary left
vague may stay in the brief as it is. Resolving them is the intent's
work.

A brief is a draft until the principal approves it, 1.0, and is
changed after that as any artefact is. An approved brief is not
locked and not immutable: what it said at any version stands in its
history and in git. A new whole is a new brief.

A brief is mined into the single intent when the principal says so,
approved or not. How far each brief is mined is recorded in the
intent's history, since the mining changes the intent and not the
brief. "How much" is a judgement recorded there and in the provenance
of the positions, never a metric. A whole that dies on the way leaves
the brief as it stands and one rejected direction in the intent with
the reason, so that the trace survives either way.

## How it is found

Claude's part changes on the way. At the opening Claude is the active
one: it inspires, brings how the same thing is done elsewhere and how
original the idea is, verifies what can be verified, and proposes
research and ingest. A proposal of Claude's, however large, serves the
finding and is not the brief.

Then the brief is written. Claude moves the principal to say what he
wants, why and what he does not want. What Claude has formulated it
reflects back before it is written. What does not fit, such as a
wrong assumption, a contradiction or a risk, Claude says at once and
unasked, in one sentence. What Claude thinks of the brief it says
when asked. What goes into the brief and what stays out is the
principal's to say.

Claude holds the form. Once the talk turns to taking the idea apart
and agreeing it piece by piece, in definitions, blocks or wording,
Claude says in one sentence that this is the intent's work, does not
develop it, and offers once to go on in the intent. That offer is a
recommendation, never a gate. The principal decides whether the
matter stays in the brief as one open line or is let go. No
walkthrough runs over the text of a brief. A walkthrough is the
forge's way of working a list of items one per message, each closed
with a verdict.

Two instruments serve the finding. `/research <topic>` puts durable
findings into `research/`, indexed. `/ingest [file]` puts outside
material into `sources/`, registered and indexed. Both are steps of
the elicitation, proposed by Claude and run on the principal's word.
Claude proposes a research step against a named need: an
uncertainty, a comparison, an inspiration. After it Claude says what
it changed in the thought, what stays uncertain and whether more
research is likely to change anything. Whether to go on is the
principal's to say. What the research did not find, or found not to
hold, is a finding like any other and stands in the research note. It
enters the brief where the principal takes it.

## Why

No structure is required, because a required one would force
premature tidiness. None is forbidden. A templated brief with
chapters, such as goal and high-level idea, was rejected for that
reason.

A brief is rough on purpose, because the chiselling belongs to the
intent. A brief polished until the intent has nothing left to do has
gone too far.

A brief is not the record of the finding, because the brief holds the
principal's choice, and what he does not take needs no home. A
finding or a source has `research/` and `sources/`. What merely fell
by in the conversation is gone with it. A second home for what the
finding yields and the brief does not take, such as a draft intent
beside a draft brief, a notes record or a new artefact before the
brief, was rejected for that reason.

Nothing in a brief marks authorship, because a mark that names a
model reads differently on every model the forge runs on. A mark in
italics before every block that is not the principal's own was
dropped for that reason. A remark is named by what it is and not by
who made it, so that it reads the same whatever model the forge runs
on.

A project may have more than one brief, because a big new whole needs
a place where the thought can be tempered before it enters the trunk,
in the way a git branch does, without a new document kind. A thread
of the intent was wrong for it, since a thread is a question and not
a body of work. A working space with positions before the merge was
judged heavy for now.

A brief is the provenance of its whole, so that drift can be measured
against the version it was mined at.

## A worked example

A generic brief, as it might stand after one round. Only the header
is fixed.

```
---
project: <slug>
title: Fewer standing meetings
author: <handle>
version: 0.1
status: draft
---

We spend too many hours in standing meetings, and most decisions are made elsewhere anyway.
I want fewer and shorter meetings, each with a written agenda, and the decisions written down the same day.
Not wanted: a new tool. The calendar we have is enough.
The survey (source: sources/meeting-survey.md) says the engineers see it the same way. (remark: the survey was small.)
Still open: who owns the agenda, and whether the weekly review stays.
```

The `(source: …)` mark will become a fact with provenance when the
brief is mined. The `(remark: …)` keeps an uncertainty visible without
saying who raised it. The open line stays open: settling it is the
intent's work.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
