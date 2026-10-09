---
generated: 2026-10-09
made: derived
inputs:
  - projects/forge/10-intent.md
  - templates/artefact-definition.md
  - CLAUDE.md
---

# About elicitation

This page explains what elicitation is in Forge of Thought, how the
definition of every kind of artefact is shaped around it, and why. It
is for anyone who uses the forge, wants to extend it with an artefact
of their own, or is weighing whether it suits them. It was put
together from the forge's own intent (its positions on elicitation),
the skeleton `templates/artefact-definition.md` and the Document chain
section of `CLAUDE.md`.

## What elicitation is

Elicitation is the process by which the principal (whoever's thinking
is being forged) and Claude find an artefact together and form the
knowledge it holds. It is not any conversation the two of them have,
and in its meaning it is not a conversation at all:

- the conversation is the medium;
- the interview is one instrument;
- research and sources are others.

Elicitation differs by artefact. The talk over a brief, over an
intent and over a BRD are three different talks, and so every kind of
artefact has a definition of its own.

## Three things kept apart

Elicitation keeps three things separate:

- **the map:** what must be found for the artefact to be complete;
- **the process:** how the map is walked;
- **the template:** where the result lands.

The map stands before the template. What must be found is settled
first; the headings of the document come after.

## The definition of an artefact

Every artefact of the chain has a definition: a state file
`.claude/skills/forge/states/<state>.md`, worked through
`/forge <state>` and paired with the artefact's template. The
definition says how we get there; the template says what is to come
out. The definition says what the artefact is, how it is found (by
questions, research and sources) and owns the artefact's rules.

The definitions are also the one list of artefacts the forge has.
Which artefacts exist is the listing of that directory, one definition
each; they are listed nowhere else, and the table of artefacts in the
README is rendered from them.

### The seven blocks

Every definition has the same seven blocks, in reading order:

| Block | What it holds |
|---|---|
| Target | the artefact's file and its template |
| Inputs | what the finding starts from |
| Aim | what the elicitation achieves and when the artefact is complete; the one place where completion is stated |
| Partner | Claude's stance: what he does, what he does not do, who steers the finding and who makes the decisions |
| Map | what must be found |
| Instruments | only the mechanisms of the forge this artefact uses in a way of its own, cited and never described |
| Course | the ways in, the order, and what is offered when the Aim's completion is reached; it states no completion of its own |

Every definition carries all seven so that the shape can be checked.
A block left empty on purpose says so, with the reason, and is never
silently left out. Aim and Partner do not repeat each other: Aim says
what is true of the artefact at the end, Partner what Claude does
beyond that.

What is shared by all artefacts stays outside the definitions and is
cited, never repeated: the form of the conversation, one write per
round, versioning with history and ledger, creation from the
template, the language, and ending by naming the state. The skeleton
for a new definition shows this on disk: it opens by citing those
shared rules, then lays out the seven blocks, and ends with how the
artefact's files are made from its template.

### The Map

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation, and it is neither a list
of questions nor a list of criteria.

The Map is walked at the moments its definition names, as the
question whether each area has been consciously considered. At the
walk Claude says of each area how it stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

This is said aloud and nothing is recorded. An area may stay empty
when it was considered and found not to apply. How an area is found
depends on the situation: a question, a research step, a source.

## What is not elicitation

- **Composing a recipe.** That is configuration from known options,
  not the finding of knowledge. The genre files of `/recipe` map onto
  the same shape without loss, but the seven blocks are for the
  artefacts of the chain.
- **`/setup`.**
- **The walkthrough of a reviewer's findings.** It has its shape
  already and nothing per artefact in it.

## Found together or handed over

How an artefact is composed is the principal's choice, artefact by
artefact:

- **Found together.** He finds it with Claude by elicitation. Where
  Claude is unsure he asks and fills no gap by assumption.
- **Handed over.** He gives a few sentences of what he wants, and
  Claude works the definition alone: its Map says what must be found,
  and Claude finds it from what he was given, from research and from
  the sources, within the bounds he sets. Claude returns a proposal
  with a short list of what he assumed and what he chose, each choice
  with what it was chosen against, and says the same in plain words in
  the artefact where it stands, until the principal has judged it.
  Nothing is derived from the proposal and nothing is done on it
  before his judgement.

Either way authorship is the principal's: the author is the one who
sends a thing into the world and answers for it, and Claude is a
tool. Every definition is written so that it can be worked either
way. The reason: the principal's attention is the scarce thing, and
whether a matter deserves it is his to say, not the forge's.

## See also

- [About the document chain](the-document-chain.md): how the definitions make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a definition of one's own.
