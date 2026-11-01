---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 96f14567aebbf469
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page explains what that process
is, how it is laid down for every kind of artefact in a definition
of seven blocks, and why the forge keeps the finding apart from the
form the result takes. It is for anyone who works an artefact with
Claude, anyone who writes a definition of a new kind of artefact,
and anyone judging whether the forge does what it claims.

## What it is

Elicitation is not any conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is the medium. The interview, in which Claude draws out
by questions what the principal has not yet put into words, is one
instrument. Research and sources are others.

Three things are kept apart:

- the map: what must be found for the artefact to be complete;
- the process: how the map is walked;
- the template: where the result lands.

Elicitation differs by artefact. The talk over a brief, the talk
over an intent and the talk over a BRD are three different talks.
Every kind of artefact therefore has a definition of its own. The
definition is a state file of the forge, worked through
`/forge <state>`, and it stands beside the artefact's template as a
pair: the definition says how the artefact is found, by questions,
research and sources, and owns its rules; the template says what
comes out. Which artefacts the forge has is the listing of the
directory of definitions, one definition each. How the definitions
join the artefacts into one chain is explained in
[The document chain](the-document-chain.md).

Some things that look like elicitation are not:

- composing a recipe, which is configuration from known options and
  not the finding of knowledge;
- `/setup`, the first run after cloning the engine;
- the walkthrough of a reviewer's findings (a walkthrough is the
  forge's way of working a list of items one per message, each
  closed with a verdict), which has its shape already and nothing
  per artefact in it.

How an artefact is composed is the principal's choice, made artefact
by artefact. He may find it with Claude by elicitation. He may hand
it over with a few sentences of what he wants, and Claude composes
the whole and returns it for his judgement. Authorship is his either
way: the author is the one who sends a thing into the world and
answers for it, and Claude is a tool.

## How it works

### The seven blocks of a definition

The elicitation of one kind of artefact is defined in seven blocks,
in reading order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what the elicitation achieves and when the artefact is
  complete. This is the one place where completion is stated.
- **Partner**: Claude's stance. What it does, what it does not do,
  who steers the finding and who makes the decisions.
- **Map**: what must be found.
- **Instruments**: only the mechanisms of the forge this artefact
  uses in a way of its own, cited and never described.
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached. The Course states no completion of
  its own.

Every definition carries all seven. A block that is empty on purpose
says so with the reason and is never silently left out. Aim and
Partner do not repeat each other: the Aim says what is true of the
artefact at the end, the Partner what Claude does beyond that,
citing the Aim.

What every artefact shares stays outside the definition and is cited
there, never repeated: the form of the conversation, one write per
round, versioning with history and the ledger (the project's state
report, made at read time), creation from the template, the
language of the artefact, and ending by naming the state. The rules
of a particular artefact live in its own definition. The skeleton of
a definition is `templates/artefact-definition.md`; how a new
definition is written and brought into the forge is the matter of
[Add an artefact](../extend/add-an-artefact.md).

### What a Map is

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation. It is neither a list of
questions nor a list of criteria.

The Map is walked at the moments its definition names. The walk asks
of each area whether it has been consciously considered. An area may
stay empty when it was considered and found not to apply. At the
walk Claude says of each area how it stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

The walk is said aloud and nothing is recorded. How an area is found
depends on the situation: a question, a research step, a source.

### Found together or handed over

Every definition is written so that it can be worked either way.

Found together, the rule holds as it stands: where Claude is unsure
it asks and fills no gap by assumption.

Handed over, Claude works the definition alone. The Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose,
with what each choice was chosen against, in two places: as a short
list of what the principal might have decided otherwise, returned
with the proposal, and in the artefact itself, in plain words at the
place each stands, until the principal has judged it. Work handed
over keeps the bounds the principal sets and comes back as a
proposal. Nothing is derived from it and nothing is done on it
before he has judged it. What a test can tell of work handed over is
told by a test and not by his reading; his judgement is for what no
test can tell.

### How sure a claim is

Whatever Claude brings as knowledge says in plain words whether it is
verified and on what, unverified, or a hypothesis. A claim never
gains certainty by being written into an artefact. Certainty is said
in words, not marks: no mark of certainty is introduced. This is
Claude's conduct and therefore holds in every layer of the chain and
in the conversation, not in one artefact alone.

## Why

The map stands before the template because a template can be filled
and still miss what the artefact is for. The map says what has to be
found; the template says only where it lands.

Every definition carries all seven blocks so that the shape can be
checked.

The Aim is the one place where completion is stated, and the Course
states no completion of its own, so that completion is never said
twice.

Composing a recipe is not elicitation because it is configuration
from known options and not the finding of knowledge. The walkthrough
of a reviewer's findings is not elicitation because it has its shape
already and nothing per artefact in it.

The principal may hand an artefact over because his attention is the
scarce thing, and whether a matter deserves it is his to say, not the
forge's.

The reason why the walk of a Map is said aloud and nothing recorded
is not recorded.

## A worked example

The example is invented and taken from no project. Suppose a kind of
artefact called a charter, the written ground of a working group,
with a definition whose Map names five areas in the charter's own
words: the purpose the group serves, who belongs to it, how often it
meets, what it may not decide, and what ends it.

The principal and Claude have talked for a while about the group.
The definition's Course names this moment for a walk of the Map.
Claude says of each area how it stands:

- The purpose the group serves: found. The principal has said it in
  two sentences, and Claude has reflected them back.
- Who belongs to it: considered and left open. Two roles are named;
  whether a third joins waits on the principal's word.
- How often it meets: considered and found not to apply. The group
  meets when a matter arises, so the area stays empty on purpose.
- What it may not decide: found, from a source the principal brought
  in, cited where it stands.
- What ends it: not looked at.

The walk is said and nothing is written. The conversation then turns
to the one area not yet looked at. Where the charter's sections go
and what headings they carry is the template's business, not the
Map's: the Map said what had to be found, and the template says where
each thing lands when the principal says to write.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
