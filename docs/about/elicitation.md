---
generated: 2026-10-10
made: derived
inputs-hash: fcbbec0e858a3405
inputs:
  - projects/forge/10-intent.md
  - templates/artefact-definition.md
  - CLAUDE.md
---

# About elicitation

This page explains what elicitation is in the forge: how an artefact
of the chain is found, what every artefact's definition consists of,
and why the shape is the way it is. It is for anyone who works with
the forge, extends it with an artefact of their own, or evaluates how
it is built. It was put together from the forge's intent, from the
skeleton of an artefact definition (`templates/artefact-definition.md`)
and from the engine's `CLAUDE.md`.

## What elicitation is

Elicitation is the process by which the principal and Claude find an
artefact together and form the knowledge it holds. It is not any
conversation between them, and in its meaning it is not a
conversation at all: the conversation is the medium. The interview,
in which Claude draws out by questions what the principal has not yet
articulated, one question per message, is one instrument; research
and sources are others. How a given piece of knowledge is found
depends on the situation: a question, a research step, a source.

Elicitation differs by artefact. The talk over a brief, over an
intent and over an assignment are three different talks, which is why
every kind of artefact has a definition of its own.

## Three things kept apart

Three things are deliberately separated:

- the **map**: what must be found for the artefact to be complete;
- the **process**: how the map is walked;
- the **template**: where the result lands.

The map stands before the template. The reason: a template can be
filled and still miss what the artefact is for. The map says what has
to be found; the template says only where it lands. Filling every
section of a skeleton is not the same as having found what the
artefact exists to hold.

## The definition and its seven blocks

Every artefact of the chain has a definition: a state file under
`.claude/skills/forge/states/`, worked through `/forge <state>` and
paired with the artefact's template. The definition says what the
artefact is, how it is found (by questions, research and sources) and
owns its rules; the template says what comes out. The two are a pair:
how we get there, and what is to come out.

Which artefacts the forge has is simply the listing of that
directory, one definition each. They are listed nowhere else; the
table of artefacts in the README is rendered from the definitions.

A definition is written in seven blocks, in reading order:

| Block | What it holds |
|---|---|
| Target | the artefact's file and its template |
| Inputs | what the finding starts from |
| Aim | what the elicitation achieves and when the artefact is complete: the one place where completion is stated |
| Partner | Claude's stance: what he does, what he does not do, who steers the finding and who the decisions |
| Map | what must be found (below) |
| Instruments | only the mechanisms of the forge this artefact uses in a way of its own, cited and never described |
| Course | the ways in, the order, and what is offered when the Aim's completion is reached; it states no completion of its own |

Every definition carries all seven, so that the shape can be checked.
A block that is empty on purpose says so with the reason; it is never
silently left out. Aim and Partner do not repeat each other: the Aim
says what is true of the artefact at the end, the Partner what Claude
does beyond that, citing the Aim. When the Aim's completion is
reached, the Course offers a next step as a recommendation, never a
gate.

What is shared across all artefacts stays outside the definition and
is cited, never repeated there: the form of the conversation, one
write per round, versioning with history and ledger, creation from
the template, the language question, and ending by naming what
changed and what stays open. The skeleton on disk,
`templates/artefact-definition.md`, shows the seven blocks as they
stand and opens with exactly those citations.

The rules of a particular artefact live in its own definition, not in
`CLAUDE.md`. `CLAUDE.md` keeps of each artefact only what it is, how
it joins the chain, and a pointer.

## What a Map is

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation, and it is neither a list
of questions nor a list of criteria.

The Map is walked at the moments its definition names, as the
question whether each area has been consciously considered. An area
may stay empty when it was considered and found not to apply. At the
walk Claude says of each area how it stands: found; considered and
left open; considered and found not to apply; or not looked at. This
is said aloud and nothing is recorded.

## What is not elicitation

Three things look like it and are not:

- **Composing a recipe.** A recipe is configuration from known
  options, not the finding of knowledge. (The genre files of
  `/recipe` do map onto the shape of a definition without loss, but
  the seven blocks themselves are for the artefacts of the chain.)
- **`/setup`.** Preparing an instance is not finding an artefact.
- **A walkthrough of a reviewer's findings.** It has its shape
  already and nothing per artefact in it.

## Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He either finds it with Claude by elicitation, or he
hands it over with a few sentences of what he wants and Claude
composes the whole and returns it for his judgement.

Found together, Claude asks where he is unsure and fills no gap by
assumption. Handed over, Claude works the definition alone: its Map
says what must be found, and he finds it from what he was given, from
research and from the sources, within the bounds the principal sets.
What he returns is a proposal, with a short list of what he assumed
and what he chose, each choice with what it was chosen against, and
the same said in plain words in the artefact where it stands, until
the principal has judged it. Nothing is derived from the proposal and
nothing is done on it before that judgement.

Authorship is the principal's either way. The author is the one who
sends a thing into the world and answers for it; Claude is a tool.

## See also

- [About the document chain](the-document-chain.md): how the
  definitions make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
