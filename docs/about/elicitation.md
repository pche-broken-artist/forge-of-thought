---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: ca15146eacc88b36
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page explains what elicitation is,
what a definition is and why the two are shaped as they are. It is
for anyone who uses the forge, extends it with an artefact of their
own, or evaluates how it works.

## What it is

An artefact is a document of the chain, such as a brief or an
intent; the [Glossary](../reference/glossary.md) gives every term of
the forge in one line. Elicitation is how such a document is found.
It is not any conversation between the principal and Claude. In its
meaning it is not a conversation at all.

- The conversation is the medium.
- The interview (questions asked one at a time to draw out what the
  principal has not yet put into words) is one instrument.
- Research and sources are other instruments.

Three things are kept apart in elicitation:

- the Map: what must be found for the artefact to be complete;
- the process: how the Map is walked;
- the template: where the result lands.

Elicitation differs by artefact. The talk over a brief and the talk
over an intent are different talks. For that reason every kind of
artefact has a definition of its own.

Some work in the forge looks like elicitation and is not:

- Composing a recipe (the file that says how a render is made). It
  is configuration from known options, not the finding of knowledge.
- `/setup`. The reason it is not counted as elicitation is not
  recorded.
- The walkthrough of a reviewer's findings (a list of items worked
  with the principal one item per message, each closed by his
  verdict). It has its shape already and nothing in it differs by
  artefact.

## How it works

### The definition

Every artefact of the chain has a definition. A definition is a
file, `.claude/skills/forge/states/<state>.md`, and it is worked
through the command `/forge <state>`. It stands beside the
artefact's template as a pair:

- the definition says how the artefact is reached: what it is, how
  it is found by questions, research and sources, and the rules that
  belong to it;
- the template says what is to come out.

Which artefacts the forge has is the listing of that directory, one
definition each. They are listed nowhere else. How the definitions
together make the chain is explained in
[The document chain](the-document-chain.md). How to write a
definition of one's own is in [Add an artefact](../extend/add-an-artefact.md).

### The seven blocks

Every definition carries seven blocks, in this reading order:

- **Target:** the artefact's file and its template.
- **Inputs:** what the finding starts from.
- **Aim:** what the elicitation achieves and when the artefact is
  complete. This is the one place where completion is stated.
- **Partner:** Claude's stance. It says what Claude does and does
  not do beyond the Aim, who steers the finding and who makes the
  decisions.
- **Map:** what must be found.
- **Instruments:** only the mechanisms of the forge that this
  artefact uses in a way of its own. They are cited, never
  described.
- **Course:** the ways in, the order, and what is offered when the
  Aim's completion is reached. It states no completion of its own.

All seven are always present. A block that is empty on purpose says
so, with the reason. It is never silently left out.

Aim and Partner do not repeat each other. The Aim says what is true
of the artefact at the end. The Partner says what Claude does beyond
that, and cites the Aim.

Some mechanism is shared by every artefact and stays outside the
definition. A definition cites it and never repeats it:

- the form of the conversation;
- one write per round of work;
- versioning with history;
- creation from the template;
- the language of the artefact;
- ending by naming the state.

### The Map

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies.

- It does not prescribe the headings of the document.
- It does not prescribe the order of the conversation.
- It is not a list of questions.
- It is not a list of criteria.

The Map is walked at the moments its definition names. At a walk the
question is whether each area has been consciously considered. Claude
says of each area how it stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

The walk is said aloud and nothing of it is recorded. An area may
stay empty when it was considered and found not to apply. How an
area is found depends on the situation: a question, a research step
or a source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact.

- **Found together.** He finds it with Claude by elicitation. Where
  Claude is unsure, it asks and fills no gap by assumption.
- **Handed over.** He hands it over with a few sentences of what he
  wants. Claude then works the definition alone: the Map says what
  must be found, and Claude finds it from what it was given, from
  research and from the sources, within the bounds the principal
  sets.

Work handed over comes back as a proposal. With it comes a short
list of what Claude assumed and what it chose, each choice with what
it was chosen against. The same is said in plain words in the
artefact, at the place each stands, until the principal has judged
it. Nothing is derived from the proposal and nothing is done on it
before his judgement.

Every definition is written so that it can be worked either way.
Either way, authorship is the principal's.

## Why

- **The Map stands before the template.** A template can be filled
  and still miss what the artefact is for. The Map says what has to
  be found; the template only says where it lands.
- **A Map is not a questionnaire.** It names areas to consider, so
  that a question, a research step or a source can each serve. The
  inputs give no further reason for keeping it free of headings and
  order.
- **Every definition carries all seven blocks.** This is so that the
  shape can be checked.
- **Recipes are not elicitation.** Composing a recipe chooses from
  known options. It does not find knowledge.
- **The walkthrough of findings is not elicitation.** It already has
  its shape, and nothing in it is particular to one artefact.
- **Authorship stays with the principal.** The author is the one who
  sends a thing into the world and answers for it. Claude is a tool.
- **The principal chooses between finding together and handing
  over.** His attention is the scarce thing. Whether a matter deserves
  it is his to say, not the forge's.
- **A handed-over artefact lists its assumptions and choices.** This
  is so that the principal judges decisions and not prose.

## A worked example

The artefact below is invented for this page and belongs to no
project: a retrospective, `60-retrospective.md`, that records what a
piece of work taught. Its definition, in the seven blocks:

```
**Target.** `60-retrospective.md`. Shape of the result:
`templates/retrospective.md`.

**Inputs.** The intent and the sources about the work looked back on.

**Aim.** A retrospective that says what was expected, what happened
and what changes next; complete when every area of the Map has been
considered.

**Partner.** Claude proposes wording and points to gaps; the principal
decides what the work taught.

**Map.** What the retrospective finds, whatever the order; where it
lands is the template's. Walked before each write.
- what was expected
- what happened
- where the two differed, and why
- what changes next

**Instruments.** None of its own: this block is empty on purpose,
because the shared mechanism is enough.

**Course.** Read the inputs and the retrospective as it stands. The
way in: what happened. End by naming what changed and what stays open.
```

Before a write, Claude walks the Map aloud:

```
what was expected            found
what happened                found
where the two differed, why  considered and left open
what changes next            not looked at
```

The walk shows that "what changes next" has not been looked at yet,
although the template's sections may already hold text. Claude
raises it. The principal answers, or says the area does not apply,
in which case it stays empty as considered and found not to apply.
Nothing of the walk itself is written into the artefact.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
