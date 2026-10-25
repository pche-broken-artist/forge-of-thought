---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 8b6c14ed35c3280a
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. An artefact is a document of the chain,
such as a brief or an intent. This page explains what elicitation is
and what it is not. It also explains the definition, which is the
file that says how one kind of artefact is found. It is written for
anyone who uses the forge, extends it with a kind of artefact of
their own, or evaluates how it works.

## What it is

Elicitation is the finding of an artefact's content by the principal
and Claude together. It is not any conversation of theirs.

The conversation is only the medium. The instruments of the finding
are several:

- the interview: Claude draws out by questions what the principal
  has not yet put into words;
- research;
- sources, that is, external inputs registered in the project.

Three things are kept apart:

- the Map: what must be found for the artefact to be complete;
- the process: how the Map is walked;
- the template: the skeleton where the result lands.

Elicitation differs by artefact. The talk over a brief, the talk
over an intent and the talk over a business requirements document
are three different talks. For that reason every kind of artefact
has a definition of its own.

Some work of the forge is not elicitation:

- composing a recipe (the file that says how a render is made);
- `/setup`, which prepares a new installation;
- the walkthrough of a reviewer's findings, that is, going through
  them with the principal one item at a time.

## How it works

### The definition

Every artefact of the chain has a definition. A definition is a
state file, `.claude/skills/forge/states/<state>.md`, worked through
`/forge <state>`. It is paired with the artefact's template:

- the definition says what the artefact is and how it is found, by
  questions, research and sources, and it owns the artefact's rules;
- the template says what comes out.

Which artefacts the forge has is the listing of the directory of
definitions, one definition each. They are listed nowhere else. How
the definitions shape the chain as a whole is described in
[The document chain](the-document-chain.md).

### The seven blocks

A definition has seven blocks, in this reading order:

| Block | What it holds |
|---|---|
| Target | the artefact's file and its template |
| Inputs | what the finding starts from |
| Aim | what the elicitation achieves and when the artefact is complete |
| Partner | Claude's stance: what it does, what it does not do, who steers the finding and who takes the decisions |
| Map | what must be found |
| Instruments | only the mechanisms of the forge this artefact uses in a way of its own, cited and never described |
| Course | the ways in, the order, and what is offered when the Aim's completion is reached |

The Aim is the one place where completion is stated. The Course
states no completion of its own. The Aim and the Partner do not
repeat each other. The Aim says what is true of the artefact at the
end. The Partner says what Claude does beyond that, citing the Aim.

Every definition carries all seven blocks. A block that is empty on
purpose says so, with its reason. It is never silently left out.

Some mechanism is shared by every definition and lives outside it.
A definition cites it and never repeats it:

- the form of the conversation;
- one write per round;
- versioning with history;
- creation of the file from its template;
- the question of the language;
- ending by naming the state.

The skeleton of a definition is `templates/artefact-definition.md`.
How to write a definition of one's own is described in
[Add an artefact](../extend/add-an-artefact.md).

The genre files of `/recipe` map onto this shape without loss. Genre
and skeleton map to Target, role to Partner, and the elicitation
checklist to Map. The seven blocks themselves are for the artefacts
of the chain.

### The Map

A Map is a map of what must be found. It is not a questionnaire.

It names, in the artefact's own vocabulary, what the finding looks
at or consciously verifies. It prescribes neither the headings of
the document nor the order of the conversation. It is neither a list
of questions nor a list of criteria. How an area is found depends on
the situation: a question, a research step or a source.

A Map is walked at the moments its definition names. The walk asks
whether each area has been consciously considered. At the walk
Claude says of each area how it stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

An area may stay empty when it was considered and found not to
apply. The walk is said aloud, and nothing of it is recorded.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. There are two ways:

- found together: the principal finds it with Claude by elicitation;
- handed over: the principal gives a few sentences of what he wants,
  and Claude composes the whole and returns it for his judgement.

Found together, the forge's rule holds as it stands. Where Claude is
unsure, it asks, and it fills no gap by assumption.

Handed over, Claude works the definition alone. The Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose,
with what each choice was chosen against. This is said in two
places: in a short list returned with the work, and in plain words
in the artefact where each choice stands, until the principal has
judged it. Work handed over keeps the bounds the principal sets. It
comes back as a proposal. Nothing is derived from it and nothing is
done on it before he has judged it. What a test can tell of work
handed over is told by a test, not by his reading.

Every definition is written so that it can be worked either way.
Authorship is the principal's in both.

## Why

The Map stands before the template because a template can be filled
and still miss what the artefact is for. The Map says what has to be
found. The template says only where it lands.

A recipe is not elicitation because composing it is configuration
from known options. It is not the finding of knowledge. The
walkthrough of findings is not elicitation because it has its shape
already and nothing in it depends on the artefact. Why `/setup` is
not elicitation is not recorded.

Every definition carries all seven blocks so that the shape can be
checked. The reason a Map is not a questionnaire is not recorded
beyond the reason above for putting the Map before the template.

Authorship stays with the principal because the author is the one
who sends a thing into the world and answers for it. Claude is a
tool. The principal chooses between finding together and handing
over because his attention is the scarce thing. Whether a matter
deserves it is his to say, not the forge's.

## A worked example

The artefact below is invented for this example: a "lessons
learned" document of no real project. Its definition might give a
Map like this:

- what happened, in the participants' own terms;
- what went well and should be kept;
- what went badly and why it went badly;
- what is changed next time, and who owns each change.

The definition names the moment of the walk, say before the first
write. At that moment Claude goes through the areas aloud:

- what happened: found;
- what went well: found;
- what went badly: considered and left open, because the cause of
  one failure is still unknown;
- what is changed next time: not looked at.

Nothing of this is written into the document. The principal now sees
that one area was never looked at and one stays open. He decides
whether to look further or to write as things stand. The headings of
the document come from its template, not from the Map. The order in
which the areas were talked about was free.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
