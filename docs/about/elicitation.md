---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 3667820f131500f1
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page explains what elicitation is,
what the definition of an artefact is and how its Map is walked. It
serves whoever works with the forge, extends it by an artefact or
judges how it is built.

## What it is

An artefact is a document of the chain. A chain starts at a brief,
its trunk is the intent, and below the intent a project takes the
layers it needs ([The document chain](the-document-chain.md)).
Elicitation is how one such artefact is found.

Elicitation is not any conversation of the principal and Claude. In
its meaning it is not a conversation at all:

- The conversation is the medium.
- The interview (Claude asking the principal questions) is one
  instrument.
- Research and sources are other instruments.

Three things are kept apart:

- The map: what must be found for the artefact to be complete.
- The process: how the map is walked.
- The template: where the result lands.

The map stands before the template. The map says what has to be
found, the template only where it lands.

Elicitation differs by artefact. The talk over a brief, the talk over
an intent and the talk over a BRD (one of the layers below the
intent) are three different talks. Every kind of artefact has a
definition of its own.

A definition is the file that says what the artefact is and how it is
found. It owns the rules of its artefact. It stands beside the
artefact's template as a pair: the definition says how the artefact
is reached, the template what is to come out. The definitions are the
files `.claude/skills/forge/states/<state>.md`, one for each kind of
artefact, and the command `/forge <state>` works by them. Which
artefacts the forge has is the listing of that directory. They are
listed nowhere else.

Three things are not elicitation:

- Composing a recipe. A recipe is the versioned file a render is
  made from, and a render is an output generated from the chain for
  one audience ([Glossary](../reference/glossary.md)).
- The command `/setup`.
- The walkthrough of a reviewer's findings. A walkthrough is the
  working through of a list of items on which the principal gives
  the verdicts.

## How it works

### The seven blocks of a definition

A definition has seven blocks, in reading order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what is true of the artefact at the end, and when the
  artefact is complete. The Aim is the one place where completion is
  stated.
- **Partner**: Claude's stance. The block says what Claude does
  beyond the Aim, what Claude does not do, who steers the finding and
  who steers the decisions.
- **Map**: what must be found, whatever the order.
- **Instruments**: the mechanisms of the forge that this artefact
  uses in a way of its own. They are cited and never described.
- **Course**: the ways in, the order, and what is offered when the
  completion of the Aim is reached. The Course states no completion
  of its own. It ends by naming what changed and what stays open.
  What it offers is a recommendation, never a gate.

Every definition carries all seven blocks. A block that is empty on
purpose says so with the reason. It is never silently left out.

Aim and Partner do not repeat each other. The Aim says what is true
of the artefact at the end. Partner says what Claude does beyond
that, and cites the Aim.

What every artefact shares stands outside the definition. A
definition cites the shared mechanism and never repeats it:

- the form of the conversation
- one write per round of the conversation
- versioning with a history
- the language
- how the files are made from the template

The seven blocks are for the artefacts of the chain. A new kind of
artefact gets its definition through the command `/new-artefact`,
from the template `templates/artefact-definition.md`, which holds
the seven blocks unfilled
([Add an artefact](../extend/add-an-artefact.md)).

### The Map

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It does not prescribe the headings of the
document. It does not prescribe the order of the conversation. It is
neither a list of questions nor a list of criteria. Where a found
thing lands is said by the template.

A Map is walked at the moments its definition names. The walk is the
question whether each area has been consciously considered. At the
walk Claude says of each area how it stands:

- found
- considered and left open
- considered and found not to apply
- not looked at

An area may stay empty when it was considered and found not to apply.
The walk is said aloud and nothing is recorded. How an area is found
depends on the situation: by a question, by a research step or by a
source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact:

- Found together: the principal finds the artefact with Claude by
  elicitation. Where Claude is unsure, it asks and fills no gap by
  assumption.
- Handed over: the principal hands the artefact over with a few
  sentences of what is wanted. Claude composes the whole and returns
  it for the principal's judgement.

Handed over, Claude works the definition alone. The Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose, with
what each choice was chosen against. It says so in two places: in a
short list of what the principal might have decided otherwise, and
in the artefact, in plain words at the place where each stands, until
the principal has judged it.

Work handed over keeps the bounds the principal sets and comes back
as a proposal. Nothing is derived from it and nothing is done on it
before the principal has judged it. What a test can tell of such work
is told by a test and not by the principal's reading. The principal's
judgement is for what no test can tell.

The principal is the author either way. Every definition is written
so that it can be worked either way.

## Why

The map stands before the template. The reason is that a template can
be filled and still miss what the artefact is for.

Every kind of artefact has a definition of its own. The reason is
that elicitation differs by artefact: the talks are different talks.

Every definition carries all seven blocks. The reason is that the
shape can then be checked.

Composing a recipe is not elicitation. The reason is that it is
configuration from known options and not the finding of knowledge.

The walkthrough of a reviewer's findings is not elicitation. The
reason is that it has its shape already and holds nothing that
differs by artefact.

Why `/setup` is not elicitation: the reason is not recorded.

Why a Map is not a questionnaire, and why nothing of its walk is
recorded: the reason is not recorded.

The principal chooses, artefact by artefact, between finding together
and handing over. The reason is that the principal's attention is the
scarce thing. Whether a matter deserves that attention is for the
principal to say, not for the forge.

The principal is the author either way. The reason is that the author
is the one who sends a thing into the world and answers for it.
Claude is a tool.

Claude says what it assumed and what it chose in work handed over.
The purpose is that the principal judges decisions and not prose.

## A worked example

The example takes an invented artefact (a rollout plan) in the file
`60-rollout-plan.md`. Its definition carries this Map:

```
**Map.** What the rollout plan finds, whatever the order; where it
lands is the template's. Walked before a write is proposed; an area
may stay empty when it was considered and found not to apply.
- the groups the rollout reaches
- the order of the steps
- what each step depends on
- the way back from a step
- the training the groups need
```

The Map names areas in the words of a rollout plan. It holds no
question: "the way back from a step" is an area, and how the
principal is asked about it is left to the conversation.

Before a write is proposed, the Map is walked. Claude says of each
area how it stands:

| Area | How it stands |
|---|---|
| the groups the rollout reaches | found |
| the order of the steps | found |
| what each step depends on | considered and left open |
| the way back from a step | not looked at |
| the training the groups need | considered and found not to apply |

The areas were found in no prescribed order and by different means:
the groups by the principal's answers, the order of the steps from a
source.

One area is not looked at yet. How it is found depends on the
situation: Claude may ask the principal one question, take a research
step or read a source.

One area is considered and left open. Whether the plan is complete
with that area open is said by the Aim of the definition, the one
place where completion is stated.

The area on training stays empty: it was considered and found not to
apply.

The walk is said in the conversation and written nowhere. Where each
found thing lands in `60-rollout-plan.md` is said by the template
`templates/rollout-plan.md`, not by the Map.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
