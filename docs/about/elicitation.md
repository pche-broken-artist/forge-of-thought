---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: d9c3b30d9707fc70
inputs:
  - projects/forge/10-intent.md#Elicitation
  - templates/artefact-definition.md
  - CLAUDE.md#Document chain
---

# Elicitation

Elicitation is the process by which the principal (the person whose
thinking is being forged) and Claude find an artefact together and
form the knowledge it holds. This page explains what that process
is, how every kind of artefact carries a definition of its own
elicitation, and why the forge keeps the definition apart from the
template. It is for the user who wants to know what happens when an
artefact is forged, for the extender who will write a definition of
a new kind, and for the evaluator who asks what the forge means by
"finding" rather than "writing".

## What it is

Elicitation is not any conversation between the principal and
Claude. In its meaning it is not a conversation at all. The
conversation is the medium. The interview, in which Claude draws out
by questions what the principal has not yet articulated, is one
instrument. Research and sources are others.

Three things are kept apart:

- the map: what must be found for the artefact to be complete;
- the process: how the map is walked;
- the template: where the result lands.

The map stands before the template. Because a template can be
filled and still miss what the artefact is for: the map says what
has to be found, the template only where it lands.

Elicitation differs by artefact. The talk over a brief, the talk
over an intent and the talk over a BRD are three different talks.
So every kind of artefact has a definition of its own elicitation.
The definition is the state file of that kind in
`.claude/skills/forge/states/`, worked through `/forge <state>` and
paired with the artefact's template: the definition says how the
artefact is found, by questions, research and sources, and owns its
rules; the template says what comes out. Which artefacts the forge
has is the listing of that directory, one definition each; they are
listed nowhere else, and the table of artefacts in the README is
rendered from the definitions. How the definitions make a chain,
from a brief through the intent to the layers a project needs, is
the matter of [The document chain](the-document-chain.md).

Three things that look like elicitation are not:

- composing a recipe, which is configuration from known options and
  not the finding of knowledge;
- `/setup`, the preparation of an instance;
- the walkthrough of a reviewer's findings (a walkthrough is the
  method by which a list of items is worked one item at a time, each
  closed with the principal's verdict), which has its shape already
  and nothing per artefact in it.

## How it works

### The seven blocks of a definition

The elicitation of one kind of artefact is defined in seven blocks,
in reading order:

- **Target**: the artefact's file and its template;
- **Inputs**: what the finding starts from;
- **Aim**: what the elicitation achieves and when the artefact is
  complete, the one place where completion is stated;
- **Partner**: Claude's stance, that is what it does, what it does
  not do, who steers the finding and who makes the decisions;
- **Map**: what must be found;
- **Instruments**: only the mechanisms of the forge this artefact
  uses in a way of its own, cited and never described;
- **Course**: the ways in, the order, and what is offered when the
  Aim's completion is reached; it states no completion of its own.

Every definition carries all seven. A block that is empty on purpose
says so with the reason and is never silently left out. Aim and
Partner do not repeat each other: Aim says what is true of the
artefact at the end, Partner what Claude does beyond that, citing
the Aim.

What is shared by every artefact stays outside the definition and is
cited there, never repeated: the form of the conversation, one write
per round, versioning with history and ledger (the ledger is the
project's state report, made at read time), creation from the
template, the language question, and ending by naming the state.

The skeleton of a definition is `templates/artefact-definition.md`.
It opens with a one-line description of what the artefact is, then a
paragraph that cites the shared mechanism, then the seven blocks. It
closes with how the files are made: the first artefact of the kind
is created from its template as version 0.1, with its history
companion beside it; a write rewrites the artefact for coherence and
never appends; empty sections and template comments are deleted. A
new definition is born through `/new-artefact`; how an extender
writes one is the matter of [Add an artefact](../extend/add-an-artefact.md).

The genre files of `/recipe` map onto the same shape without loss:
Genre and Skeleton onto Target, Role onto Partner, the elicitation
checklist onto Map. The seven blocks themselves are for the
artefacts of the chain.

### What a Map is

A Map is a map of what must be found, not a questionnaire. It names,
in the artefact's own vocabulary, what the finding looks at or
consciously verifies. It prescribes neither the headings of the
document nor the order of the conversation. It is neither a list of
questions nor a list of criteria. Why a Map takes this form rather
than a questionnaire is not recorded beyond the reason given for
the map above: a template can be filled and still miss what the
artefact is for.

The Map is walked at the moments its definition names, as the
question whether each area has been consciously considered. An area
may stay empty when it was considered and found not to apply. At the
walk Claude says of each area how it stands, in one of four states:

- found;
- considered and left open;
- considered and found not to apply;
- not looked at.

The walk is said aloud and nothing is recorded. How an area is found
is the situation's to decide: a question, a research step, a source.

### Claude's conduct in the finding

Whatever Claude brings as knowledge says in plain words whether it
is verified and on what, unverified, or a hypothesis. A claim never
gains certainty by being written into an artefact. This is said in
words, not marks: no mark of certainty is introduced. The rule is
Claude's conduct, so it holds in every layer of the chain and in the
conversation alike.

### Found together or handed over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants and Claude composes the
whole and returns it for his judgement.

Authorship is his either way. The author is the one who sends a
thing into the world and answers for it, and Claude is a tool.

Found together, the rule holds as it stands: where Claude is unsure
it asks and fills no gap by assumption.

Handed over, Claude works the definition alone. Its Map says what
must be found; Claude finds it from what it was given, from research
and from the sources. It says what it assumed and what it chose,
with what each choice was chosen against, so that the principal
judges decisions and not prose. This is said twice: in what Claude
returns, as a short list of what the principal might have decided
otherwise, and in the artefact itself, in plain words at the place
each choice stands, until the principal has judged it. Work handed
over keeps the bounds he sets and comes back as a proposal: nothing
is derived from it and nothing is done on it before he has judged
it. What a test can tell of work handed over is told by a test and
not by his reading; his judgement is for what no test can tell.

Every definition is written so that it can be worked either way.

### How a definition lives

A definition is not tried before it is used. It lives in its state
file, is used on real work at once and is mended there as the work
shows. A change of what a definition is to achieve goes through the
forge's own intent first.

## Why

The map stands before the template. Because a template can be
filled and still miss what the artefact is for.

Every definition carries all seven blocks, an empty block saying so
with its reason. So that the shape can be checked.

Elicitation is defined per kind of artefact. Because the talk over
one kind is a different talk from the talk over another; one
definition for all would describe none of them.

The principal chooses, artefact by artefact, whether to find it
together or hand it over. Because his attention is the scarce thing,
and whether a matter deserves it is his to say, not the forge's.

A definition is used on real work at once rather than tried first.
Because whatever goes wrong is restored from git, and a trial would
mean changing every definition twice, in the intent and in its
file, and moving it over afterwards.

Composing a recipe is not elicitation. Because it is configuration
from known options, not the finding of knowledge. The walkthrough of
findings is not elicitation. Because it has its shape already and
nothing per artefact in it. Why `/setup` is set apart is not
recorded.

## A worked example

The example is invented: an artefact called the pilot, a layer a
project might add below its assignment to say how the assigned thing
is first tried in the small. No project of the forge has it. It
shows the shape only.

Its definition, in the seven blocks, might read:

- **Target.** `40-pilot.md`. Shape of the result:
  `templates/pilot.md`.
- **Inputs.** The intent and the assignment as they stand.
- **Aim.** A pilot that the recipients can run without the
  principal in the room; complete when what is tried, who tries it
  and what ends the trial are each either found or consciously
  left open.
- **Partner.** Claude proposes the boundary of the trial and
  challenges a trial that would prove nothing; the principal decides
  what is tried. Beyond the Aim, Claude never decides what the trial
  is for.
- **Map.** What the pilot finds, whatever the order; where it lands
  is the template's. Walked before every write; an area may stay
  empty when it was considered and found not to apply.
  - what is tried, and what of the assignment it stands for
  - who takes part
  - what is measured, and what counts as enough
  - what ends the pilot
  - what happens to the thing after the pilot
- **Instruments.** Research, for what others have measured in a
  trial of this kind, cited by its own definition.
- **Course.** Resolve the project and read the inputs and the pilot
  as it stands. The ways in: from a thread of the intent that asks
  for a trial, or from the assignment's deliverables. End by naming
  what changed and what stays open; when the Aim's completion is
  reached, offer the next layer: a recommendation, never a gate.

Now the Map is walked, before a write, with the slug `<slug>`
standing for the project. Claude says aloud:

> What is tried: found, it is the first of the assignment's
> deliverables, from your answer earlier in this round. Who takes
> part: considered and left open, you named the team but not who in
> it. What is measured: found, from the success criterion of the
> assignment, and a research note gave the usual figure, verified
> on one source. What ends the pilot: considered and found not to
> apply, you said the pilot runs until the next layer replaces it.
> What happens after: not looked at.

Nothing of this is recorded. The one area not looked at is the next
question; the one left open stays open until the principal names a
person; the one found not to apply stays empty in the written
artefact. When the principal says to write, the result lands in
`40-pilot.md` in the shape `templates/pilot.md` gives, and the
history companion beside it records the change.

## See also

- [The document chain](the-document-chain.md): how the definitions make the chain a star.
- [Add an artefact](../extend/add-an-artefact.md): writing a definition of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
