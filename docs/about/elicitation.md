---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 1d397696b812b693
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact of the chain
together and form the knowledge it holds. This page says what
elicitation is, what a definition is and how it shapes the finding,
and why the forge keeps it in this shape. It is for the user who
works an artefact with Claude, for the extender who writes the
definition of a new kind of artefact, and for the evaluator who
wants to know what the forge means by finding an artefact rather
than writing one.

## What it is

Elicitation is not any conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is the medium. The interview, in which Claude draws out
by questions what the principal has not yet put into words, is one
instrument. Research and sources are other instruments.

Three things are kept apart:

- the map: what must be found for the artefact to be complete;
- the process: how the map is walked;
- the template: where the result lands.

Elicitation differs by artefact. The talk over a brief, the talk over
an intent and the talk over a business requirements document are
three different talks. So every kind of artefact has a definition of
its own.

Three things resemble elicitation and are not elicitation:

- composing a recipe: it is configuration from known options, not
  the finding of knowledge;
- `/setup`: the reason is not recorded;
- the walkthrough of a reviewer's findings (the settling of a list of
  findings one item at a time): it has its shape already, and nothing
  in it is particular to an artefact.

### What a definition is

Every artefact of the chain has a definition: its state file
`.claude/skills/forge/states/<state>.md`. The definition is the one
thing `/forge <state>` works by. It stands beside the artefact's
template as a pair: the definition says how the result is reached,
the template says what comes out. The definition says what the
artefact is and how it is found, by questions, research and sources.
It owns the artefact's rules. The file `CLAUDE.md` keeps of each
artefact only what it is, how it joins the chain, and a pointer to
its definition.

Which artefacts the forge has is the listing of the directory of
definitions, one definition each. They are listed nowhere else. The
table of artefacts in the README is rendered from the definitions.
How the definitions give the chain its shape is said in
[The document chain](the-document-chain.md).

## How it works

### The seven blocks

The elicitation of one kind of artefact is defined in seven blocks,
in reading order:

- Target: the artefact's file and its template;
- Inputs: what the finding starts from;
- Aim: what the elicitation achieves and when the artefact is
  complete; it is the one place where completion is stated;
- Partner: Claude's stance, that is, what it does, what it does not
  do, who steers the finding and who makes the decisions;
- Map: what must be found;
- Instruments: only the mechanisms of the forge this artefact uses
  in a way of its own, cited and never described;
- Course: the ways in, the order, and what is offered when the Aim's
  completion is reached; it states no completion of its own.

Every definition carries all seven blocks. A block that is empty on
purpose says so, with the reason. It is never silently left out. Aim
and Partner do not repeat each other: Aim says what is true of the
artefact at the end, Partner says what Claude does beyond that,
citing the Aim.

What every artefact shares stays outside the definition. It is cited
there and never repeated: the form of the conversation, one write
per round, versioning with history and ledger (the ledger is the
project's single source of truth for state), creation from the
template, the language question, and ending by naming the state.

The skeleton of a definition is `templates/artefact-definition.md`.
A definition is born through `/new-artefact`; how one is written is
said in [Add an artefact](../extend/add-an-artefact.md). The
skeleton also fixes how the artefact's files are made. The first
artefact is created from its template as version 0.1. Its history
companion is created beside it from `templates/history.md`, and the
artefact gets its row in the ledger's Documents table. Its items
follow the ID scheme of `CLAUDE.md`. A write rewrites the artefact
for coherence and never appends. Empty sections and all template
comments are deleted.

A definition is used on real work as soon as it exists, and it is
mended there as the work shows. A change of what a definition is to
achieve goes through the intent first.

### The Map

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

This is said aloud, and nothing is recorded. How an area is found is
decided by the situation: a question, a research step, a source.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants. Every definition is
written so that it can be worked either way.

Found together, Claude asks where it is unsure and fills no gap by
assumption.

Handed over, Claude works the definition alone. The Map says what
must be found. Claude finds it from what it was given, from research
and from the sources. It returns the artefact as a proposal, within
the bounds the principal set. With the proposal comes a short list
of what Claude assumed and what it chose, each choice with what it
was chosen against. The same is said in plain words in the artefact
at the place where each choice stands, until the principal has
judged it. So the principal judges decisions, not prose. Nothing is
derived from the proposal and nothing is done on it before he has
judged it. What a test can tell of work handed over is told by a
test, not by his reading; his judgement is for what no test can
tell.

Authorship is the principal's either way.

### Recipes and the shape

The genre files of `/recipe` map onto the seven blocks without loss:
Genre and Skeleton onto Target, Role onto Partner, the elicitation
checklist onto Map. The seven blocks themselves are for the artefacts
of the chain. Composing a recipe remains outside elicitation, as said
above.

## Why

The map stands before the template. Because a template can be filled
and still miss what the artefact is for: the map says what has to be
found, the template says only where it lands.

Every kind of artefact has a definition of its own. Because the talks
differ: the brief, the intent and a business requirements document
are not found by one talk.

Every definition carries all seven blocks, an empty one with its
reason. So that the shape can be checked.

Composing a recipe is not elicitation. Because it is configuration
from known options and not the finding of knowledge. The walkthrough
of a reviewer's findings is not elicitation. Because it has its shape
already, and nothing in it is particular to an artefact. Why `/setup`
is not elicitation is not recorded.

Why the walk of a Map is said aloud and never recorded is not
recorded.

Authorship is the principal's, found together or handed over. Because
the author is the one who sends a thing into the world and answers
for it, and Claude is a tool.

The choice between finding together and handing over is the
principal's, artefact by artefact. Because his attention is the
scarce thing, and whether a matter deserves it is his to say, not
the forge's.

A definition is used on real work at once and mended there. Because
whatever goes wrong is restored from git, and a trial would mean
changing every definition twice, in the intent and in its file, and
moving it over afterwards.

## A worked example

The example is invented and belongs to no project. Suppose the forge
had an artefact called the reading guide: a document that tells a
newcomer to a project what to read and in what order. Its definition
would carry the seven blocks; the Map block might read:

```
**Map.** What the reading guide finds, whatever the order; where it
lands is the template's. Walked before every write; an area may stay
empty when it was considered and found not to apply.
- the newcomer: who arrives, and what they already know
- the order: which documents come first, which may wait
- the time: how much reading the guide asks for
- what is left out on purpose
- the words a newcomer will not know
```

The Map names five areas in the reading guide's own words. It does
not say that the guide has five sections, and it does not say that
the newcomer is talked about first. The guide's headings are its
template's; the order of the talk is the conversation's.

Found together, the principal and Claude talk over the guide for a
while. When the principal says to write, the definition names that
moment as a walk of the Map. Claude says aloud how each area stands:

- the newcomer: found; two kinds of reader were named and the guide
  speaks to both;
- the order: found;
- the time: considered and left open; the principal has not said how
  much reading the guide may ask for;
- what is left out: considered and found not to apply; the project
  has three documents and the guide points to all of them;
- the words: not looked at.

Nothing of this is written down. The principal hears it and decides
where to go: a question on the time, a glance at the words, or the
write as it stands. The area that stays empty stays empty with its
reason said, not silently.

Handed over, the same Map is walked by Claude alone. The principal
gives a few sentences: the guide is for a colleague who joins the
project next month. Claude finds the five areas from those sentences,
from the project's documents and from what research says about
reading guides. It returns the guide as a proposal, with a short
list beside it: it assumed the colleague knows the forge already; it
chose to put the intent before the brief, against the order in which
the two were written; it left the time open, because the sentences
did not say it. The same three remarks stand in plain words in the
guide where each applies. The principal judges those three decisions
and not the prose around them. Nothing is derived from the guide
until he has.

## See also

- [The document chain](the-document-chain.md): how the definitions
  make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a
  definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
