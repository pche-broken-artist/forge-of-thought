---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: b5d3756c41883885
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

The intent is the working document of a project: the consolidated
current state of what the principal (the person whose thinking is
being forged) holds, in one file, `10-intent.md`. This page says what
that file holds, why it is rewritten rather than appended to, where
the open matters live instead, and where solving goes. It is written
for whoever uses the forge or evaluates it; how the intent is
iterated in practice is the page [Forge the intent](../use/forge-the-intent.md).

## What it is

The intent is the trunk of a project's chain of documents, the
[artefact](../reference/glossary.md) every lower layer is derived
from. It chisels the briefs into what the principal holds: the
briefs are the principal's own raw input, and the intent is what
remains of them once they have been worked through with Claude.

It is the current state, not a log. Each round of work rewrites it
for coherence, so that the whole reads as one, and the changes of the
round are recorded in its history companion (the page
[Versioning and history](versioning-and-history.md)). Nothing is
appended; nothing is kept twice.

It exists because a conversation with Claude ends and its context is
lost. Anything of value must live in a file. The intent is the
document to read when returning to a project after weeks, instead of
excavating old conversations.

It does not solve. It says what the principal wants and why, and how
the things he wants are realised belongs to the solution design (the
page [The solution design](the-solution-design.md)). The test of a
sentence is this: would it still hold if the thing were realised in a
wholly different way? If it would, it is intent. If it would not, it
is solution. A principle the principal sets for the solution, which
the realisation must respect whatever its shape, is intent; the
mechanism that honours it is solution. What the principal wants a
user to be able to do, and what must be true when it is done, is
intent, a command he asks for by name among it. How the command does
it, what it is built of, its steps and the checks it runs, is
solution. The division is by kind of content, never by who said it:
an idea of the principal's about how to build something is solution
too.

## Who writes and reads it

The principal and Claude write it together. The principal owns the
substance; Claude composes the wording. Claude helps him reach the
aim of the document: it mines the briefs with him whole by whole,
probes contradictions, gaps and unstated assumptions, reflects a
brain-dump back as structure before it is written, offers options
with trade-offs, and runs the final reality check with him. An idea
is challenged on two questions kept apart, whether it is good and
whether it is feasible; that is a way of asking, and nothing is
recorded per idea. A thread closes only on the principal's word.

Its audience is the principal and Claude only, as its header says.
The layer below, where the project has one, is derived from it; the
intent itself is never handed to the recipients of an assignment.

## Made from

- The briefs the principal says to mine: `00-brief.md` and any
  `00-brief-<name>.md`, approved or not.
- `decisions.md`, the project's record of decisions.
- The ledger, the project's state report, made at read time.
- Sources, only as the principal directs.
- The intent as it stands, read together with the project's threads
  in `threads/`.

## What it holds

The file follows the template `templates/intent.md`. Its header
carries the version, the status and the project slug. Its body has
these areas, each of which may stay empty when it was considered and
found not to apply:

- **Essence**: a few sentences on what the principal wants and why,
  as of today.
- **Positions** (prefix `POS`): the statements the principal
  currently holds. A position says what he holds and why it holds,
  in as many words as it takes to be understood without loss of
  meaning, and names what it comes from, a brief or a source. It is
  dated once, with the day it took its present shape. A position
  without an ID does not exist: it carries its ID from birth, and
  the history records it by that ID.
- **Facts** (prefix `FCT`): what is the case, stated by the principal
  on his word or by a source cited to its file. Verification is never
  demanded. A fact is not a stance; making a source's fact the
  principal's own stance is a new position.
- **Rejected directions** (prefix `REJ`): what was considered and
  dropped, with the reason.
- **Candidate structure for the layer below**: an optional staging
  area for what the layer below will need as soon as the principal
  sees it, the recipients, the objective and the success criteria
  where that layer is an assignment, as positions with IDs. It is
  left out where the project takes no layer and deleted once the
  layer exists and leads.

Ideas are placed on a horizon where the principal sees one: a proof
of concept, the first version, a later one, or good but far away.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that goes into the history in the same step that writes the
position, while the whole context is at hand. Earlier steps of a
position are found by searching the history for its ID, and a
position cites no record of the history. A number stays in a
position only where it is the rule or a threshold, never as a
measurement. Text leaves a position only into the history, word for
word.

An item says what is to be achieved and why. What realises it is
named in the solution design where the project has one. Where the
project has none, the item names the file that realises it; where
the output is only part of a file or the file does not exist yet, the
item keeps the full information. Because another change may rewrite
that part, the detail would otherwise be lost. Where the item and
what realises it say different things, that is a finding, never
mended in silence.

The IDs of positions, facts, rejections and threads follow the ID
scheme of `CLAUDE.md`.

### The threads

What is being worked lives outside the intent's body, in threads
(prefix `THR`): one file per thread, `threads/THR.NNNN.md`, made from
`templates/thread.md`. The intent says what holds; the threads say
what is being worked. They are part of the intent as its history is.

A thread's header is its state:

- `concerns`: the artefact it concerns, named as the state map of
  `/forge` names it; several where several.
- `origin`: where it came from, the principal's word (the default),
  a document by path, or Claude's synthesis.
- `status`: `open` or `closed`.

A thread has no title and no further fields. Its first sentence is
its headline; its last dated paragraph is its state. It carries the
working debate for as long as it is unsettled: what was said, what
was tried, the plan of a change under way, the proposals that await a
decision. It is where an unfinished conversation is saved before a
session (one sitting with Claude) ends.

While open, a thread is freely rewritten, header included. It has no
version and no history of its own. A thread is never moved, renamed
or deleted. Closing it is `status: closed` and one `closed` record in
the intent's history, saying when and by what. The closed file is
immutable and is the archive. What returns later is a new thread
citing the old one. The intent's history records the birth and the
closing of a thread, not every saving of its debate. There is no list
file of threads; the ledger makes the list.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. At that point Claude names the layers that can
follow from it, or offers the approval where the principal takes
none: a recommendation, never a gate.

## How it is found

The intent is found by elicitation, the conversation in which Claude
draws out what the principal has not yet articulated (the page
[Elicitation](elicitation.md)). Briefs are mined one at a time,
whole by whole, and offered before threads. Within a round one theme
is worked at a time; the reality check comes last, before a lower
layer is proposed. Research is proposed where a thread needs outside
grounding and run on the principal's word. An independent reality
check by a challenger is offered once the joint one is done, never
run on Claude's own judgement. At the write, resolved threads move
into positions or rejections.

## Why

The intent replaced an append-only question-and-answer log. The log
was rejected because it left the current state of what was wanted
scattered across the brief, the log and the assignment, with no
single place answering "what do I want now". The intent is that one
place, which is why each round rewrites it for coherence instead of
appending.

The intent does not solve, because an intent that carries the
solution cannot be read as what is wanted, and nobody can be asked
for a proposal of the whole solution over it.

Facts have a prefix of their own, because without one a fact would
have passed for a position. A thread carries its origin so that a
hypothesis of Claude's stays visibly its own until the principal
takes it up; what Claude has worked out is never a fact, since a fact
is the principal's word or a source's.

Threads are files of their own, one per thread, so that two people on
different threads never conflict, so that Claude reads only the
threads it needs, and so that whatever drives the intent file need
not handle a block with an inner state of its own. A thread's header
is its state and changes on a branch too, the one header that does; a
thread is therefore not an artefact.

Rejected directions are kept, with their reasons, so that old ground
is not re-litigated and the reasoning is preserved for a later return
to the project.

The way to a position goes into the history rather than the
position, so that the position stays readable as what holds, and the
record is written while the whole context is still at hand.

## A worked example

A position of a generic project, as it would stand in the Positions
area of `10-intent.md`:

```
- **POS.0010** Every order confirmation reaches the customer within
  the hour it was placed. Reason: a customer who hears nothing calls
  the service desk, and the desk's load is the cost the project is
  meant to remove. From `00-brief.md`. Present shape 2026-03-14.
```

The sentence passes the test: it would still hold if the confirmation
were sent by mail, by text message or by a courier. How the
confirmation is sent is solution and belongs in the solution design.
If a round later changes the hour to the day, the old wording leaves
the position word for word into the history, and the record there
says what was said on the way.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
