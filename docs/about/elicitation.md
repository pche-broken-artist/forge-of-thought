---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 5669d4a5591aa5e0
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. An artefact is a document of the chain,
such as a brief, an intent or a BRD. This page explains what
elicitation is, what a definition of an artefact is, and why the two
are shaped as they are. It is written for anyone who uses the forge,
extends it with an artefact of their own, or weighs whether it is
sound.

## What it is

Elicitation is not every conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is only the medium in which it happens.

Elicitation works through several instruments:

- the interview: questions that draw out what the principal has not
  yet put into words;
- research;
- sources: external inputs such as transcripts, offers, documents or
  standards, kept unchanged in the project's `sources/`.

Elicitation differs by artefact. The talk over a brief, the talk over
an intent and the talk over a BRD are three different talks. That is
why every kind of artefact has a definition of its own.

Some work looks like elicitation and is not:

- composing a recipe (the file that says how a render is made): this
  is configuration chosen from known options, not the finding of
  knowledge;
- `/setup`, the first run that prepares an instance (one installation
  of the forge): the reason it is not counted as elicitation is not
  recorded;
- a walkthrough of a reviewer's findings (a walkthrough is a list of
  items put to the principal for his decision): it has its own shape
  already and nothing in it differs per artefact.

## How it works

### Three things kept apart

Elicitation keeps three things separate:

- the map: what must be found for the artefact to be complete;
- the process: how the map is walked;
- the template: the skeleton where the result lands.

The map comes before the template. A template only says where a
result lands. The map says what has to be found.

### The definition

Every artefact of the chain has a definition. A definition is the
state file of that artefact in `.claude/skills/forge/states/`, and it
is worked through `/forge <state>`. Each definition is paired with
the artefact's template. The definition says how the artefact is
reached. The template says what is to come out. The listing of the
definitions is the listing of the artefacts the forge has: they are
listed nowhere else. How the definitions together shape the chain is
explained on [The document chain](the-document-chain.md).

A definition has seven blocks, in this reading order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what the elicitation achieves and when the artefact is
  complete. This is the one place where completion is stated.
- **Partner**: Claude's stance. It says what Claude does beyond the
  Aim and what it does not do, who steers the finding and who makes
  the decisions.
- **Map**: what must be found.
- **Instruments**: only those mechanisms of the forge that this
  artefact uses in a way of its own. They are cited, never described.
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached. The Course states no completion of
  its own.

Every definition carries all seven blocks. A block left empty on
purpose says so, with the reason. It is never silently left out.

Aim and Partner do not repeat each other. The Aim says what is true
of the artefact at the end. The Partner says what Claude does beyond
that, and it cites the Aim.

Some mechanism is shared by every artefact. It stays outside the
definition and is cited there, never repeated:

- the form of the conversation;
- one write per round;
- versioning with a history companion, and the ledger (the record of
  the project's state);
- creation of the artefact from its template;
- the language the artefact is written in;
- ending by naming the state.

The rules of a particular artefact live in its definition. The
project's core instructions (`CLAUDE.md`) keep of each artefact only
what it is, how it joins the chain, and a pointer to the definition.
How to write a definition for a new kind of artefact is shown on
[Add an artefact](../extend/add-an-artefact.md). The skeleton of a
definition is `templates/artefact-definition.md`. Other terms of the
forge are in the [Glossary](../reference/glossary.md).

### The Map

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own words, what the finding looks at or
consciously verifies.

A Map prescribes neither the headings of the document nor the order
of the conversation. It is not a list of questions. It is not a list
of criteria.

A Map is walked at the moments its definition names. The walk asks
of each area whether it has been consciously considered. At the walk
Claude says how each area stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

The walk is said aloud, and nothing of it is recorded. An area may
stay empty when it was considered and found not to apply. How an
area is found depends on the situation: a question, a research step
or a source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. There are two ways.

- **Found together.** The principal finds the artefact with Claude
  by elicitation. Where Claude is unsure, it asks. It fills no gap by
  assumption.
- **Handed over.** The principal hands the artefact over with a few
  sentences of what he wants. Claude works the definition alone. The
  Map says what must be found, and Claude finds it from what it was
  given, from research and from the sources. It returns the whole as
  a proposal, within the bounds the principal set.

Work handed over comes back with a short list of what Claude assumed
and what it chose. Each choice names what it was chosen against. The
same is said in plain words in the artefact, at the place where each
choice stands, until the principal has judged it. Nothing is derived
from the proposal and nothing is done on it before his judgement.
What a test can tell is told by a test. His judgement is for what no
test can tell.

Authorship is the principal's either way. Every definition is
written so that it can be worked in both ways.

## Why

- **The map stands before the template** because a template can be
  filled and still miss what the artefact is for.
- **Every kind of artefact has its own definition** because the talk
  differs by artefact: what must be found for a brief is not what
  must be found for an intent.
- **Every definition carries all seven blocks** so that the shape can
  be checked.
- **Shared mechanism is cited, not repeated.** The reason is not
  recorded.
- **A Map is not a questionnaire.** The reason is not recorded.
- **Handed-over choices are listed** so that the principal judges
  decisions and not prose.
- **Authorship stays with the principal** because the author is the
  one who sends a thing into the world and answers for it. Claude is
  a tool.
- **The choice of found together or handed over is the principal's**
  because his attention is the scarce thing. Whether a matter
  deserves it is his to say, not the forge's.

## A worked example

Take an invented artefact, a "meeting charter" that says why a
recurring meeting exists. It is not an artefact of the forge. It only
shows the shape. Its definition's Map might name these areas, in the
artefact's own words:

- the purpose the meeting serves;
- who must attend and who may;
- the decisions the meeting is allowed to take;
- what ends the meeting series.

The Map does not say which heading each area becomes. That belongs to
the charter's template. The Map does not say which area is talked
about first.

Suppose the definition names the walk at the moment the principal
asks to write. Claude then says aloud how each area stands:

| Area | How it stands |
|---|---|
| the purpose the meeting serves | found |
| who must attend and who may | considered and left open |
| the decisions the meeting is allowed to take | considered and found not to apply: the meeting only informs |
| what ends the meeting series | not looked at |

Nothing of this table is written into any file. The principal now
sees that one area was never looked at. It can be taken up with a
question, a source or a research step.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
