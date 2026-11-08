---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: fa4fdf95c82beb23
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page explains what that process is,
how every kind of artefact defines its own, and why the parts are
kept apart as they are. It is for the user who works an artefact with
Claude, for the extender who writes a definition, and for the
evaluator who wants to know what "found together" means here.

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
still miss what the artefact is for. The map says what has to be
found; the template only says where it lands.

Elicitation differs by artefact. The talk over a brief, the talk over
an intent and the talk over a business requirements document are
three different talks. So every kind of artefact has a definition of
its own, and the definition is paired with the artefact's template:
how we get there, and what is to come out.

Three things are not elicitation:

- composing a recipe, because that is configuration from known
  options and not the finding of knowledge;
- `/setup`, the first run after cloning the engine; the reason is not
  recorded;
- the walkthrough of a reviewer's findings (the method by which a
  list of items is worked one item per message, each closed with a
  verdict), because it has its shape already and nothing per
  artefact in it.

## How it works

### The definition

Every artefact of [the document chain](the-document-chain.md) has a
definition. The definition is a state file,
`.claude/skills/forge/states/<state>.md`, and it is worked through
`/forge <state>`. It says what the artefact is, how it is found, by
questions, research and sources, and it owns the artefact's rules.
The template says what comes out. Which artefacts the forge has is
the listing of that directory, one definition each; they are listed
nowhere else, and the table of artefacts in the README is rendered
from the definitions. A chain starts at a brief and its trunk is the
intent. Below the intent a project takes the layers it needs, and no
layer is a condition of another.

The definition is written in seven blocks, in reading order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what the elicitation achieves and when the artefact is
  complete. This is the one place where completion is stated.
- **Partner**: Claude's stance: what it does, what it does not do,
  who steers the finding and who makes the decisions.
- **Map**: what must be found.
- **Instruments**: only the mechanisms of the forge this artefact
  uses in a way of its own, cited and never described.
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached. The Course states no completion of its
  own.

Every definition carries all seven blocks. A block empty on purpose
says so with the reason; it is never silently left out. Aim and
Partner do not repeat each other: Aim says what is true of the
artefact at the end, Partner what Claude does beyond that, citing the
Aim.

What every artefact shares stays outside the definition and is
cited there, never repeated:

- the form of the conversation;
- one write per round;
- versioning with history and ledger (the ledger is the file that
  states the project's state, made at read time);
- creation from the template;
- the language question;
- ending by naming the state.

The skeleton of a definition, `templates/artefact-definition.md`,
shows the same shape. Its Course opens by resolving the project and
reading the inputs and the artefact as it stands. It ends by naming
what changed and what stays open; when the Aim's completion is
reached, something is offered as a recommendation, never as a gate.
The skeleton also says how the files are made: the first artefact is
created from its template as version 0.1, with a history companion
beside it; a write rewrites the artefact for coherence and never
appends; empty sections and all template comments are deleted. How
to write a definition of one's own is the page
[Add an artefact](../extend/add-an-artefact.md).

The genre files of `/recipe` map onto the same shape without loss:
Genre and Skeleton to Target, Role to Partner, the elicitation
checklist to Map. The seven blocks themselves are for the artefacts
of the chain.

### The Map

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
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

The walk is said aloud and nothing is recorded. How an area is found
depends on the situation: a question, a research step, a source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants, and Claude composes the
whole and returns it for his judgement. Authorship is his either way:
the author is the one who sends a thing into the world and answers
for it, and Claude is a tool.

Found together, the rule holds as it stands: where Claude is unsure
it asks and fills no gap by assumption.

Handed over, Claude works the definition alone. The Map says what
must be found; Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose, with
what each choice was chosen against, so that the principal judges
decisions and not prose. This is said twice: as a short list of what
the principal might have decided otherwise, and in the artefact in
plain words at the place each stands, until the principal has judged
it. Work handed over keeps the bounds the principal sets and comes
back as a proposal: nothing is derived from it and nothing is done on
it before he has judged it. What a test can tell of work handed over
is told by a test and not by his reading; his judgement is for what
no test can tell. Every definition is written so that it can be
worked either way.

### How sure a claim is

Whatever Claude brings as knowledge says in plain words whether it is
verified and on what, unverified, or a hypothesis. A claim never
gains certainty by being written into an artefact. Words, not marks:
no mark of certainty is introduced. The rule is Claude's conduct, so
it holds in every layer of the chain and in the conversation, not in
one artefact alone.

## Why

The map stands before the template because a template can be filled
and still miss what the artefact is for.

Every kind of artefact has a definition of its own because the
elicitation differs by artefact: the talks over a brief, over an
intent and over a business requirements document are three different
talks.

Every definition carries all seven blocks so that the shape can be
checked.

Composing a recipe is not elicitation because it is configuration
from known options, not the finding of knowledge. The walkthrough of
findings is not elicitation because it has its shape already and
nothing per artefact in it. Why `/setup` is not elicitation is not
recorded.

The principal chooses, artefact by artefact, whether to find an
artefact together or to hand it over, because his attention is the
scarce thing, and whether a matter deserves it is his to say, not the
forge's.

The definitions are used on real work at once and mended there as the
work shows, rather than tried first. Whatever goes wrong is restored
from git, and a trial would mean changing every definition twice, in
the intent and in its file, and moving it over afterwards. A change
of what a definition is to achieve goes through the intent first.

## A worked example

The example is invented and belongs to no project. Suppose a project
has a layer below the intent called a risk register, defined by its
own definition and paired with its template. Its Map names five
areas, in the register's own words:

- the risks the recipients must know of;
- for each risk, the harm it does if it comes about;
- for each risk, who watches it;
- what is being done about each risk now;
- the risks that were weighed and set aside, with the reason.

The Map says nothing about the headings of the register or the order
in which these areas come up. In the conversation the principal
starts with the harm he fears most; Claude asks what else could go
wrong; a source, an earlier incident report the principal registered,
supplies two more risks, each cited with its provenance.

At the moment the definition names for the walk, Claude says of each
area how it stands:

- the risks: found;
- the harm of each: found;
- who watches each: considered and left open, because two risks have
  no owner yet;
- what is being done now: not looked at;
- the risks set aside: considered and found not to apply, because
  nothing was weighed and dropped in this round.

Nothing of this is recorded. The principal decides to look at what is
being done now before the write, and the round goes on. When he says
to write, the result lands where the template says, and the history
companion receives one record per change.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
