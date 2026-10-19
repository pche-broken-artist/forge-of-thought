---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 6b63206aefeac43e
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged, with final authority over every word) and
Claude find an artefact together and form the knowledge it holds. An
artefact is one document of the chain, such as a brief, an intent or
an assignment. This page explains what elicitation is and what it is
not. It also explains the definition that every kind of artefact has
and the Map inside it. It is written for anyone who uses the forge,
extends it or weighs it up.

## What it is

Elicitation is not any conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is only the medium it runs in. Several instruments do
the finding:

- the interview: Claude draws out by questions what the principal
  has not yet put into words, one question per message;
- research: a look at current practice on a topic;
- sources: external inputs, such as transcripts or documents.

Elicitation keeps three things apart:

- the map: what must be found for the artefact to be complete;
- the process: how that map is walked;
- the template: the skeleton where the result lands.

Elicitation differs from artefact to artefact. The talk over a brief,
the talk over an intent and the talk over an assignment are three
different talks. For this reason every kind of artefact has a
definition of its own. A definition is a file in
`.claude/skills/forge/states/`, worked through `/forge <state>`.

Three things look like elicitation and are not:

- composing a render recipe: it is configuration from known options,
  not the finding of knowledge;
- `/setup`, the first run that prepares an instance (one
  installation of the forge);
- the walkthrough of a reviewer's findings: a walkthrough is the way
  a list of items is worked with the principal one item per message,
  each closed with a verdict, and it has its shape already, with
  nothing in it that depends on the artefact.

## How it works

### A definition paired with a template

Every artefact of the chain has a definition, paired with the
artefact's template. The definition says what the artefact is and how
it is found, by questions, research and sources. It also holds the
rules of that artefact. The template says what comes out. Together
they answer two questions: how we get there, and what is to come out.
Which artefacts the forge has is simply the list of definitions in
that directory, one each. How the definitions shape the chain is
explained in [The document chain](the-document-chain.md).

### The seven blocks

Every definition carries the same seven blocks, in this reading
order:

- **Target**: the artefact's file and its template.
- **Inputs**: what the finding starts from.
- **Aim**: what is true of the artefact at the end, and when it is
  complete; this is the one place where completion is stated.
- **Partner**: what Claude does beyond the Aim and what it does not
  do, who steers the finding and who makes the decisions.
- **Map**: what must be found.
- **Instruments**: only the mechanisms of the forge that this
  artefact uses in a way of its own, cited and never described.
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached.

All seven blocks are always present. A block that is empty on
purpose says so, with the reason. It is never silently left out.

Aim and Partner do not repeat each other. Aim says what is true of
the artefact at the end. Partner says what Claude does beyond that,
and cites the Aim. Course states no completion of its own. What it
offers at completion is a recommendation, never a gate.

Some mechanism is shared by every artefact. It stays outside the
definition and is only cited there:

- the form of the conversation;
- one write per round of conversation;
- versioning with its history;
- creation of the file from its template;
- the language the artefact is written in;
- ending by naming what changed and what stays open.

A skeleton for a new definition stands in
`templates/artefact-definition.md`. Writing one of your own is the
subject of [Add an artefact](../extend/add-an-artefact.md).

### The Map

A Map is a map of what must be found. It is not a questionnaire. It
names, in the artefact's own words, the areas the finding looks at
or consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation. It is neither a list of
questions nor a list of criteria.

A Map is walked at the moments its definition names. The walk asks,
of each area, whether it has been consciously considered. At the walk
Claude says how each area stands:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

An area may stay empty when it was considered and found not to
apply. The walk is said aloud, and nothing of it is recorded. How an
area is found depends on the situation: a question, a step of
research or a source.

### Found together or handed over

How an artefact is composed is the principal's choice, artefact by
artefact. He can find it with Claude by elicitation. He can also hand
it over with a few sentences of what he wants. Then Claude composes
the whole and returns it for his judgement.

Found together, Claude asks where it is unsure and fills no gap by
assumption. Handed over, Claude works the definition alone. The Map
says what must be found, and Claude finds it from what it was given,
from research and from the sources. It says what it assumed and what
it chose, each choice with what it was chosen against. It says this
in a short list when it returns the work. It also says it in plain
words in the artefact, at the place each choice stands, until the
principal has judged it. Work handed over keeps the bounds the
principal sets and comes back as a proposal. Nothing is derived from
it, and nothing is done on it, before he has judged it.

Authorship is the principal's either way. Every definition is
written so that it can be worked either way.

## Why

- The map stands before the template. The reason is that a template
  can be filled and still miss what the artefact is for. The map
  says what has to be found; the template only says where it lands.
- Each kind of artefact has its own definition. The reason is that
  elicitation differs by artefact: the talk over each layer is a
  different talk.
- Composing a recipe is not elicitation. The reason is that it is
  configuration from known options, not the finding of knowledge.
- The walkthrough of findings is not elicitation. The reason is that
  it has its shape already and nothing in it depends on the artefact.
- Every definition carries all seven blocks. The purpose is that the
  shape can be checked.
- Authorship stays with the principal even when he hands the work
  over. The reason is that the author is the one who sends a thing
  into the world and answers for it, and Claude is a tool.
- The principal chooses, artefact by artefact, whether to find it
  together or hand it over. The reason is that his attention is the
  scarce thing, and whether a matter deserves it is for him to say,
  not for the forge.
- Claude names what it assumed and chose, with what each choice was
  chosen against. The purpose is that the principal judges decisions
  and not prose.
- Why the shared mechanism is cited rather than described in each
  definition: the reason is not recorded.

## A worked example

Take an invented kind of artefact, a "risk register", that some
forge might add. Its definition would carry a Map such as this one,
in the artefact's own words:

```
**Map.** What the risk register finds, whatever the order; where it
lands is the template's. Walked before each write; an area may stay
empty when it was considered and found not to apply.
- the risks the intent already implies
- who carries each risk
- what would show that a risk has happened
- the risks consciously accepted, with why
```

None of these lines is a question, and none fixes a heading of the
register. Each names something the finding has to have looked at.

Before a write, Claude walks the Map aloud and says how each area
stands:

| Area | How it stands |
|---|---|
| the risks the intent already implies | found |
| who carries each risk | considered and left open |
| what would show that a risk has happened | not looked at |
| the risks consciously accepted, with why | considered and found not to apply |

The walk shows at once what is still missing: the signs that a risk
has happened were never looked at. Claude raises that area next, by
a question, a step of research or a source. Nothing of the walk is
written into the register or anywhere else.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
