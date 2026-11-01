---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: fb47548c09f33e67
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. An artefact is one document of the
chain, such as a brief or an intent. This page explains what
elicitation is and what it is not. It also explains the definition
that every kind of artefact has, block by block. It is for anyone
who works with the forge, extends it or weighs it.

## What it is

Elicitation is not any conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is the medium it runs in. Elicitation itself uses
several instruments:

- the interview: questions that draw out what the principal has not
  yet put into words;
- research: a question looked up outside the conversation;
- sources: external inputs, such as a transcript or a document,
  stored as they arrived.

Three things are kept apart:

- the map: what must be found for the artefact to be complete;
- the process: how the map is walked;
- the template: the skeleton where the result lands.

Elicitation differs by artefact. The talk over a brief, the talk
over an intent and the talk over a business requirements document
are three different talks. Every kind of artefact therefore has a
definition of its own.

Some work looks like elicitation and is not:

- composing a recipe (the instructions a render is made from): it
  is configuration from known options, not the finding of knowledge;
- `/setup`, the first run that prepares an instance (one
  installation of the forge);
- the walkthrough of a reviewer's findings: it already has its
  shape, and nothing in it differs by artefact.

A walkthrough is the way a list of items is put to the principal,
one item per message, each with a verdict.

## How it works

### A definition and its template

Every artefact of the chain has a definition. The definition is a
file of the engine, `.claude/skills/forge/states/<state>.md`. It is
worked through the command `/forge <state>`. Each definition stands
beside the artefact's template as a pair:

- the definition says how the artefact is reached: what it is, how
  it is found by questions, research and sources, and the rules that
  belong to it;
- the template says what is to come out.

Which artefacts the forge has is the listing of the directory of
definitions, one definition each. They are listed nowhere else. How
the definitions shape the chain is explained in
[The document chain](the-document-chain.md).

### The seven blocks

A definition is written in seven blocks, in this reading order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what the elicitation achieves, and when the artefact is
  complete. This is the one place where completion is stated.
- **Partner**: Claude's stance. It says what Claude does and does
  not do, who steers the finding and who makes the decisions.
- **Map**: what must be found.
- **Instruments**: the mechanisms of the forge that this artefact
  uses in a way of its own. They are cited, never described.
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached. The Course states no completion of
  its own.

Every definition carries all seven blocks. A block that is empty on
purpose says so, with the reason. It is never silently left out.

Aim and Partner do not repeat each other. The Aim says what is true
of the artefact at the end. The Partner says what Claude does beyond
that, and cites the Aim.

Some mechanism is shared by every artefact. It stays outside the
definition, cited and never repeated:

- the form of the conversation;
- one write per round: what is agreed in a working conversation is
  written once, at its end, on the principal's word;
- versioning with a history;
- creation of the first version from the template;
- the language the artefact is written in;
- ending by naming what changed and what stays open.

The definition is the place for the rules of its own artefact. What
a brief carries, for example, belongs to the brief's definition.

### What a Map is

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own words, what the finding looks at or
consciously verifies. It is neither a list of questions nor a list
of criteria. It prescribes neither the headings of the document nor
the order of the conversation.

A Map is walked at the moments its definition names. The walk asks
of each area whether it has been consciously considered. At the walk
Claude says of each area how it stands:

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
by artefact. He may find it with Claude by elicitation. He may also
hand it over with a few sentences of what he wants. Claude then
composes the whole and returns it for his judgement.

Found together, Claude asks where it is unsure and fills no gap by
assumption.

Handed over, Claude works the definition alone. The Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose, and
what each choice was chosen against. It says this in two places:

- in a short list returned with the work, of what the principal
  might have decided otherwise;
- in the artefact, in plain words, at the place each assumption or
  choice stands, until the principal has judged it.

Work handed over keeps the bounds the principal sets and comes back
as a proposal. Nothing is derived from it and nothing is done on it
before he has judged it. Every definition is written so that it can
be worked either way.

Authorship is the principal's either way.

Writing a definition for a new kind of artefact is described in
[Add an artefact](../extend/add-an-artefact.md). Every term used here
is given in one line in the [Glossary](../reference/glossary.md).

## Why

- **The map stands before the template.** A template can be filled
  and still miss what the artefact is for. The map says what has to
  be found. The template says only where it lands.
- **Every definition carries all seven blocks.** This is so that the
  shape can be checked.
- **A recipe is not elicited.** Composing a recipe is configuration
  from known options, not the finding of knowledge.
- **The walkthrough of findings is not elicitation.** It has its
  shape already, and nothing in it differs by artefact.
- **Authorship stays with the principal when work is handed over.**
  The author is the one who sends a thing into the world and answers
  for it. Claude is a tool.
- **Handing over is the principal's choice.** His attention is the
  scarce thing. Whether a matter deserves it is for him to say, not
  for the forge.
- **Choices are named in a handed-over artefact.** This is so that
  the principal judges decisions and not prose.
- **Why a definition has exactly these seven blocks, why shared
  mechanism stays outside the definitions, and why the Map walk is
  said aloud and not recorded:** the reason is not recorded.

## A worked example

Take an invented kind of artefact, a "field plan", that says how a
team will visit a site. This artefact is not part of the forge. It
only shows the shape.

Its definition would carry the seven blocks. Its Map might name
these areas, in the artefact's own words:

- the purpose of the visit;
- who goes and who decides on the spot;
- what must be seen or measured;
- the risks on site;
- what happens with the results.

The Map does not say that the plan has a heading "Risks". It does
not say that risks are discussed third. It does not list questions.

At the moment the definition names, Claude walks the Map aloud:

| Area | How it stands |
|---|---|
| the purpose of the visit | found |
| who goes and who decides on the spot | found |
| what must be seen or measured | considered and left open |
| the risks on site | considered and found not to apply |
| what happens with the results | not looked at |

The principal now sees that the measurements are still open and that
nobody has yet thought about the results. The next questions go
there. The walk is said in the conversation and is not written into
any file. Where the answers land in the field plan is for its
template to say.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
