---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 1476477632f980d5
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page says what that process is,
what a definition is and why every kind of artefact has one. It is
for anyone who works an artefact with Claude, for anyone who wants
to write a definition of a new kind of artefact, and for anyone who
wants to judge whether the shape holds.

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

The map stands before the template. A template can be filled and
still miss what the artefact is for: the map says what has to be
found, the template only where it lands.

Elicitation differs by artefact. The talk over a brief, over an
intent and over a layer below them are three different talks. So
every kind of artefact has a definition of its own: a file that
says how that kind is found. The artefacts of the chain, and where
each definition lives, are described in
[The document chain](the-document-chain.md).

Three things are not elicitation:

- composing a recipe, the instruction for a generated output, which
  is configuration from known options and not the finding of
  knowledge;
- `/setup`, the first run after the engine is cloned; the reason is
  not recorded;
- the walkthrough of a reviewer's findings, that is the working of
  a list of findings one at a time to the principal's verdict, which
  has its shape already and nothing per artefact in it.

## How it works

### The definition and its template

Every artefact of the chain has a definition: its state file under
`.claude/skills/forge/states/`, one file per kind of artefact,
worked through `/forge <state>`. The definition says what the
artefact is, how it is found, by questions, research and sources,
and owns the rules of that artefact. It stands beside the artefact's
template as a pair: the definition says how the principal and
Claude get there, the template says what is to come out. Which
artefacts the forge has is the listing of that directory, one
definition each. They are listed nowhere else, and the table of
artefacts in the README is rendered from the definitions.

The rules of a particular artefact live in its definition, not in
the engine's core instructions. The core keeps of each artefact what
it is, how it joins the chain and a pointer to the definition.

### The seven blocks

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

Every definition carries all seven blocks. A block empty on purpose
says so with the reason. It is never silently left out.

Aim and Partner do not repeat each other. Aim says what is true of
the artefact at the end. Partner says what Claude does beyond that,
citing the Aim.

Shared mechanism stays outside the definition, cited and never
repeated there: the form of the conversation, one write per round,
versioning with its history companion and the ledger (the file that
holds a project's state), creation from the template, the language
question, and ending by naming the state.

The skeleton of a definition, `templates/artefact-definition.md`,
shows the blocks as they stand on disk. It opens with one paragraph
that names the artefact and cites the shared mechanism. It closes
with how the files are made: the first artefact of the kind is
created from its template as version 0.1, with its history companion
beside it and its row in the ledger, and a write rewrites the
artefact for coherence and never appends. How to write a definition
of a new kind is in [Add an artefact](../extend/add-an-artefact.md).

The genre files of `/recipe` map onto the same shape without loss:
Genre and Skeleton to Target, Role to Partner, the elicitation
checklist to Map. The seven blocks themselves are for the artefacts
of the chain.

### The Map

A Map is a map of what must be found, not a questionnaire. It
names, in the artefact's own vocabulary, what the finding looks at
or consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation. It is neither a list of
questions nor a list of criteria.

The Map is walked at the moments its definition names. The walk is
the question whether each area has been consciously considered. An
area may stay empty when it was considered and found not to apply.
At the walk Claude says of each area how it stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

The walk is said aloud, and nothing is recorded. How an area is
found depends on the situation: a question, a research step, a
source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants, and Claude composes the
whole and returns it for his judgement.

Found together, the rule holds as it stands: where Claude is unsure
it asks and fills no gap by assumption.

Handed over, Claude works the definition alone. Its Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose,
with what each choice was chosen against, so that the principal
judges decisions and not prose. This stands in two places: in what
Claude returns, as a short list of what the principal might have
decided otherwise, and in the artefact itself, in plain words at the
place each choice stands, until the principal has judged it. Work
handed over keeps the bounds the principal sets and comes back as a
proposal. Nothing is derived from it and nothing is done on it
before he has judged it. What a test can tell of work handed over is
told by a test and not by his reading; his judgement is for what no
test can tell.

Authorship is the principal's either way. The author is the one who
sends a thing into the world and answers for it. Claude is a tool.
Every definition is written so that it can be worked either way.

## Why

The map stands before the template because a template can be filled
and still miss what the artefact is for. The map says what has to be
found; the template only says where it lands.

Every kind of artefact has a definition of its own because the talk
over one kind of artefact is not the talk over another.

Every definition carries all seven blocks so that the shape can be
checked.

Completion is stated in the Aim alone, and the Course states none of
its own, so that there is one place to look for when an artefact is
complete.

The definition is worked by `/forge` and stands beside the template
as a pair: how the principal and Claude get there, and what is to
come out.

The principal chooses, artefact by artefact, whether to find it
together or to hand it over, because his attention is the scarce
thing, and whether a matter deserves it is his to say, not the
forge's.

Why composing a recipe is not elicitation: it is configuration from
known options, not the finding of knowledge. Why the walkthrough of
findings is not: it has its shape already and nothing per artefact
in it. Why `/setup` is not: the reason is not recorded.

## A worked example

The example is invented. Suppose the forge had a kind of artefact
called the itinerary: the plan of one journey. Its definition would
carry the seven blocks, in the shape the skeleton gives:

- **Target.** `30-itinerary.md`. Shape of the result:
  `templates/itinerary.md`.
- **Inputs.** The intent of the project, and any source that names a
  place, a date or a companion.
- **Aim.** An itinerary from which the traveller can set out without
  the principal in the room: every leg has a place and a day, and
  what is left open is said to be open. Complete when no leg is
  undated.
- **Partner.** Claude proposes the order of the legs and asks for
  what the inputs do not give; the principal decides where to go and
  what to skip.
- **Map.** What the itinerary finds, whatever the order; where it
  lands is the template's. Walked before every write; an area may
  stay empty when it was considered and found not to apply.
  - the destinations and the order they are visited in
  - the days each leg takes
  - who travels
  - what the journey must not cost more than
  - what is deliberately left open for the road
- **Instruments.** Empty on purpose: the itinerary uses no mechanism
  of the forge in a way of its own.
- **Course.** Resolve the project and read the inputs and the
  itinerary as it stands. The ways in: a first itinerary from the
  intent, or a changed leg. End by naming what changed and what
  stays open; when the Aim's completion is reached, offer a render
  for the companions: a recommendation, never a gate.

Now the Map is walked, before a write. Claude says aloud, area by
area, how each stands:

- The destinations and their order: found. Three places, in the
  order the principal gave them.
- The days each leg takes: considered and left open. The second leg
  has no length yet; the principal said he would decide it after a
  source arrives.
- Who travels: found, from the intent.
- What the journey must not cost more than: considered and found
  not to apply. The principal said the journey has no budget, and
  the area stays empty.
- What is deliberately left open for the road: not looked at.

Nothing of this walk is recorded. What it changes is the next
question: Claude asks about the one area not looked at, and the
write that follows the round carries what was found. The headings of
the written itinerary are the template's, not the Map's, and the
conversation ran in whatever order the principal's answers took.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
