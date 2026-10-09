---
generated: 2026-10-09
made: derived
inputs-hash: 10701ea70e70e137
inputs:
  - projects/forge/10-intent.md
  - templates/artefact-definition.md
  - CLAUDE.md
---

# About elicitation

This page explains what elicitation is in the forge: how the
principal and Claude find an artefact together, what is kept apart
in that work, and the shape every kind of artefact's definition
keeps. It is for the user who works an artefact, the extender who
writes a definition of his own, and the evaluator who wants to know
why the shape is as it is. It was put together from the forge
intent's positions on elicitation, from the skeleton of a definition
in `templates/artefact-definition.md`, and from the Document chain
section of `CLAUDE.md`.

## What elicitation is

Elicitation is the process by which the principal and Claude find an
artefact together and form the knowledge it holds. It is not any
conversation of theirs, and in its meaning it is not a conversation
at all: the conversation is the medium. The interview is one
instrument of it; research and sources are others. How a given area
is found is the situation's: a question, a research step, a source.

Elicitation differs by artefact. The talk over a brief, over an
intent and over a requirements document are three different talks,
so every kind of artefact has a definition of its own that says how
it is found.

### Three things kept apart

- **The map**: what must be found for the artefact to be complete.
- **The process**: how the map is walked.
- **The template**: where the result lands.

The map stands before the template. A template can be filled and
still miss what the artefact is for: the map says what has to be
found, the template only where it lands.

### What is not elicitation

- Composing a recipe: that is configuration from known options, not
  the finding of knowledge.
- `/setup`.
- The walkthrough of a reviewer's findings: it has its shape already
  and nothing per artefact in it.

## The definition of an artefact

Every artefact of the chain has a definition: its state file under
`.claude/skills/forge/states/`, worked through `/forge <state>` and
paired with the artefact's template. The definition says what the
artefact is, how it is found, by questions, research and sources,
and owns its rules; the template says what comes out. The pair reads
as: how we get there, and what is to come out.

Which artefacts the forge has is the listing of that directory, one
definition each. They are listed nowhere else; the table of
artefacts in the README is rendered from the definitions. The rules
of a particular artefact live in its definition, and `CLAUDE.md`
keeps of each artefact only what it is, how it joins the chain, and
a pointer.

### The seven blocks

The elicitation of one kind of artefact is defined in seven blocks,
in reading order:

| Block | What it holds |
|---|---|
| Target | the artefact's file and its template |
| Inputs | what the finding starts from |
| Aim | what the elicitation achieves and when the artefact is complete: the one place where completion is stated |
| Partner | Claude's stance: what he does, what he does not do, who steers the finding and who the decisions |
| Map | what must be found |
| Instruments | only the mechanisms of the forge this artefact uses in a way of its own, cited and never described |
| Course | the ways in, the order, and what is offered when the Aim's completion is reached; it states no completion of its own |

Every definition carries all seven, so that the shape can be
checked. A block empty on purpose says so with the reason and is
never silently left out. Aim and Partner do not repeat each other:
Aim says what is true of the artefact at the end, Partner what
Claude does beyond that, citing the Aim.

What is shared mechanism stays outside the definition, cited and
never repeated there: the form of the conversation, one write per
round, versioning with history and ledger, creation from the
template, the language question, ending by naming the state. The
skeleton in `templates/artefact-definition.md` shows the blocks as
they stand on disk, with the shared mechanism cited in its opening
paragraph and a closing note on how the files are made: the first
artefact is created from its template as v0.1, with its history
companion and its row in the ledger.

The genre files of `/recipe` map onto the same shape without loss
(Genre and Skeleton to Target, Role to Partner, the elicitation
checklist to Map), but the seven blocks themselves are for the
artefacts of the chain.

### What a Map is

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation, and it is neither a list
of questions nor a list of criteria.

The Map is walked at the moments its definition names, as the
question whether each area has been consciously considered. At the
walk Claude says of each area how it stands: found, considered and
left open, considered and found not to apply, or not looked at. An
area may stay empty when it was considered and found not to apply.
The walk is said aloud and nothing is recorded.

## Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants, and Claude composes the
whole and returns it for his judgement. Authorship is his either
way: the author is the one who sends a thing into the world and
answers for it, and Claude is a tool.

- **Found together**, the rule holds as it stands: where Claude is
  unsure he asks and fills no gap by assumption.
- **Handed over**, Claude works the definition alone. Its Map says
  what must be found; he finds it from what he was given, from
  research and from the sources, within the bounds the principal
  sets. He says what he assumed and what he chose, with what it was
  chosen against, so that the principal judges decisions and not
  prose: in a short list returned with the proposal, and in the
  artefact in plain words at the place each stands, until the
  principal has judged it. Nothing is derived from the proposal and
  nothing is done on it before he has judged it. What a test can
  tell of work handed over is told by a test and not by his reading;
  his judgement is for what no test can tell.

Every definition is written so that it can be worked either way. The
reason: the principal's attention is the scarce thing, and whether a
matter deserves it is his to say, not the forge's.

## Why the definitions stand on their own

The definitions live in the state files of `/forge`, are used on
real work at once and mended there as the work shows; they are not
tried first in a separate place. Whatever goes wrong is restored
from git, and a trial would mean changing every definition twice. A
change of what a definition is to achieve goes through the forge
intent first. Self-contained definitions are also what would make a
later split of the engine a move of files rather than a rewrite.

## See also

- [About the document chain](the-document-chain.md): how the definitions make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a definition of one's own.
