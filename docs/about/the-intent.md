---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: a8047e179e5ed6d1
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/thread.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.1680
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#REJ.0010
---

# The intent

The intent is the document that holds what the principal (whoever's
thinking is being forged) currently wants and why, consolidated into
one coherent state and rewritten every round. This page says what
the intent holds, why it is rewritten rather than appended to, where
the open matters live and where the solving goes instead. It is for
the user who works an intent with Claude and for the evaluator who
wants to know what the document is and why it has the shape it has.

## What it is

The intent is the working document of a project, the file
`10-intent.md`: the consolidated current state of what the principal
holds. It is not a log. Each round rewrites it for coherence, and
what changed is recorded in the history companion beside it (see
[Versioning and history](versioning-and-history.md)). It is the
document to read when returning to a project after weeks, instead of
excavating old conversations.

The intent works the briefs down to what the principal holds. The
owners' image for this is chiselling: from the briefs, the sources
and the conversation it keeps what matters as positions, what is the
case as facts, what is undecided as threads and what was dropped as
rejections with the reason. Everything in it is coherent, nothing
stands twice, and every position carries its provenance.

An intent says what is wanted and why. It does not solve. The test of
a sentence is whether it would still hold if the thing were realised
in a wholly different way. If it would, the sentence is intent. If it
would not, it is solution, and it belongs in
[The solution design](the-solution-design.md). A principle the
principal sets for the solution, what the realisation must respect
whatever its shape, is intent. The mechanism that honours it is
solution. What the principal wants the user to be able to do, and
what must be true when it is done, is intent; a command he asks for
by name is among it. How the command does it, what it is built of,
its steps and their order and the checks it runs, is solution. The
division is by kind of content, never by who said it: an idea of the
principal's about how to build something is solution too.

## Who writes and reads it

The principal writes the intent with Claude. The principal supplies
the substance and decides; Claude composes the wording and proposes.
A thread closes only on the principal's word. The template names
its audience as the principal and Claude only: the intent is not
handed to anyone.

It is read at the start of every round, together with the project's
threads. The layer below, where the project takes one, is derived
from it. Its history is read by whoever needs the way to a position.
The ledger (the project's state report, remade by a script after
every write) reads the mining of the briefs from the records of the
history and makes the list of threads from the thread files. An
independent reality check of the intent is run through `/challenge`
on the principal's word, once the joint reality check is done, and
never on Claude's own judgement.

## Made from

- The briefs the principal says to mine: `00-brief.md` and any
  `00-brief-<name>.md`, approved or not.
- `decisions.md` and the ledger.
- Sources, only as the principal directs.
- The conversation: the principal's answers, a new word of his, and
  what the recipients of a lower layer sent back.
- The intent as it stands, read with the project's threads in
  `threads/`.

The first intent is created from `templates/intent.md` as version
0.1, with its history companion `10-intent.history.md` made from
`templates/history.md` and an empty `threads/` beside it.

## What it holds

The shape is the template's: an Essence, Positions, Facts, Rejected
directions and, where the project takes a layer below, a Candidate
structure for that layer. The threads stand beside the intent in
files of their own. The items carry the prefixes `POS`, `FCT`, `REJ`
and `THR`; how they are numbered is the ID scheme of `CLAUDE.md`.
An area of the intent may stay empty when it was considered and
found not to apply.

**Essence.** Three to ten sentences: what the principal wants and
why, as of today.

**Positions (`POS`).** A position says what the principal holds and
why it holds, in as many words as it takes to be understood without
loss of meaning. It names what it comes from, a brief or a source.
It is dated once: one date, the day the position took its present
shape. It carries its ID from birth; a position without an ID does
not exist. Ideas are placed on a horizon where the principal sees
one: a proof of concept, the first version, a later one, or good but
far away. Making a source's fact the principal's own stance is a new
position.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that is written into the history in the same step that writes the
position, while the whole context is at hand. A number stays in a
position only where it is the rule or a threshold, never as a
measurement. Text leaves a position only into the history, word for
word. A position cites no record of the history; the earlier steps
are found by searching the history for the position's ID.

An item says what is to be achieved and why. What realises it is
named in the solution design where the project has one. Where the
project has none, the item names the file that realises it. Where
that output is only part of a file, or the file does not exist yet,
the item keeps the full information. Because another change may
rewrite that part, and the detail would be lost. Where the item and
what realises it say different things, that is a finding (the result
of a reviewer), never mended in silence.

**Facts (`FCT`).** A fact is what is the case: stated by the
principal on his word, or by a source cited to its file. A source's
fact cites the file; the principal's needs none. Verification is
never demanded. What Claude has worked out is never a fact.

**Rejected directions (`REJ`).** What was considered and dropped,
and why.

**Candidate structure for the layer below.** An optional staging
area: what the layer below will need as soon as the principal sees
it, such as the recipients, the objective and the success criteria
where that layer is an assignment, as positions with IDs like
everything else. It is left out where the project takes no layer and
deleted once the layer exists and leads.

**Threads (`THR`).** The threads are files, `threads/THR.NNNN.md`,
one per thread, made from `templates/thread.md`. They are part of the
intent as its history is: the intent says what holds, the threads
what is being worked, the working debate included until a thread is
settled. A thread says what is open and where it came from. For as
long as it is unsettled it carries what was said, what was tried,
the plan of a change under way and the proposals that await a
decision. It is where an unfinished conversation is saved before a
session ends. Its first sentence is its headline, its last dated
paragraph its state.

A thread's header is its state, in three fields:

- `concerns`: the artefact it concerns, as `/forge` names it;
  several where several;
- `origin`: where it came from: the principal's word, a document by
  path, or Claude's synthesis; the principal's word is the default;
- `status`: `open` or `closed`.

A thread is freely rewritten while open, the header too. It has no
version and no history of its own. It is never moved, renamed or
deleted. Closing is `status: closed` and a `closed` record in the
intent's history that says when and by what. The closed file is
immutable and is the archive. What returns is a new thread citing
the old one. On a write, a resolved thread moves into a position or
a rejection, and the intent's history records the birth and the
closing of a thread, not every saving of its debate. There is no
list file of threads: the ledger makes the list from the files.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, or the intent
is approved, the Map of its definition (the list of areas the intent
finds: the essence, the weight of every idea, the ground, the
horizon, what is open, the briefs as wholes, what the layer below
will need, and reality) is walked, and the whole is passed through a
final reality check. When completion is reached, Claude names the
layers that can follow from the intent, or offers the approval where
the project takes no layer. That is a recommendation, never a gate.

## How it is found

The intent is found by elicitation, the questioning that draws out
what the principal has not yet articulated (see
[Elicitation](elicitation.md)); the command that runs a round is
described in [Forge the intent](../use/forge-the-intent.md). Claude
mines the briefs with the principal whole by whole, one brief at a
time, and offers the briefs before the threads. It probes
contradictions, gaps and unstated assumptions. It challenges an idea
on two questions kept apart, whether it is good and whether it is
feasible; that is a way of asking, and nothing is recorded per idea.
It reflects a brain-dump back as structure before anything is
written, offers options with trade-offs, and proposes research where
a thread needs outside grounding, run on the principal's word. A
source enters only as the principal directs. Within a round one
theme is worked at a time, and the reality check comes last.

The round ends in one write. The write rewrites the intent for
coherence and never appends. Resolved threads move into positions or
rejections, and the record of what was mined from every brief
touched is kept in the history. Whatever remains unsettled is saved
into its thread before the session ends, and the ledger is remade.
Claude ends by naming what changed and what stays open.

## Why

The intent exists as one file because chat context dies, and
anything of value must live in a file. An append-only log of
questions and answers was the earlier shape. It was rejected because
it left the current state of the intent scattered across the brief,
the log and the assignment, with no single place answering "what do
I want now". The consolidated, rewritten intent is that one place,
and its history keeps what the log would have kept.

Rejected directions are kept so that old ground is not re-litigated
and the reasoning is preserved for a future return to the project.

Facts have a prefix of their own because, without one, a fact would
have passed for a position.

A thread carries its origin so that a hypothesis of Claude's stays
visibly its own until the principal takes it up.

Threads are files of their own, not a block of the intent, for three
reasons the owners give. Two people on different threads never
conflict. Claude reads only the threads it needs. No merge need
handle a block with an inner state. A thread is not an artefact, and
its header is its state.

The intent does not solve because an intent that carries the
solution cannot be read as what is wanted, and because nobody can be
asked for a proposal of the whole solution over it.

## A worked example

A position of a project, written as the template shapes it:

```markdown
- **POS.0010** Every customer request is kept in one place, so that
  anyone can find a request without asking who took it. Requests
  are lost today whenever the colleague who took them is away, and
  one place for them is wanted before any tool is chosen. From
  `00-brief.md`. 2026-02-10.
```

The position says what is wanted (one place for every request) and
why (requests are lost when their taker is away). It names its
provenance, the brief, and carries one date. It says nothing of
which tool, which steps or how many requests were lost last month:
the count would be a measurement, and the tool would be solution.
The sentence passes the test of an intent. It would still hold if
the one place were a ticket system or a shared mailbox. "The
requests go into a ticket system with three queues" would not hold
under a different realisation, so it belongs in the solution design.

An open matter of the same project, say whether requests from
partners count as customer requests, would not stand in the intent.
It would be a thread, one file in `threads/`, with `concerns:
intent`, `origin: the principal` and `status: open` in its header,
the debate in its body and its last dated paragraph as its state.
Once the principal decides, the thread is closed, its file stays as
the archive, and what he decided goes into the position or into a
rejected direction.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
