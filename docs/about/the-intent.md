---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: f9475fbfbd75be21
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#REJ.0010
---

# The intent

The intent is the consolidated current state of what the principal
holds: the one document of a project that answers "what do I want
now". The principal is the person whose thinking is being forged.
This page says what the intent is, what it holds, when it is
complete and why it is kept the way it is. It is written for the
person who works a project with Claude and for the person who
evaluates how the forge keeps thinking. How a round on the intent is
run is the how-to [Forge the intent](../use/forge-the-intent.md).

## What it is

The intent is an artefact of the chain, the file `10-intent.md` in
the project folder. It is the working document: the briefs, the
documents a chain starts from, are chiselled into it, that is, their
substance is sorted into what the principal holds, what is the case,
what is undecided and what was dropped. It is the trunk of the
chain: every layer below it is derived from it.

The intent is not a log. Every round rewrites it for coherence, so
that the body always reads as one current state. What changed, and
why, is recorded in its history companion, `10-intent.history.md`,
beside it; the history is explained in
[Versioning and history](versioning-and-history.md). The intent
carries a version, a date and a status, as every artefact does.

The intent says what the principal wants and why. It does not
solve. The test of a sentence is this: would it still hold if the
thing were realised in a wholly different way? If it would, the
sentence is intent. If it would not, the sentence is solution and
belongs in the solution design, explained in
[The solution design](the-solution-design.md). A principle the
principal sets for the solution, something the realisation must
respect whatever its shape, is intent; the mechanism that honours it
is solution. What the principal wants a user to be able to do, and
what must be true when it is done, is intent, a command asked for by
name among it; how the command does it, what it is built of, its
steps and the checks it runs, is solution. The division is by kind
of content, never by who said it: an idea of the principal's about
how to build something is solution too.

## Who writes and reads it

The principal and Claude write it together. Claude composes the
wording; the principal supplies the substance. A thread closes only
on the principal's word. The intent's audience is the principal and
Claude only: it is never handed to anyone else as it stands.

It is the document to read when returning to a project after weeks,
instead of excavating old conversations. It is also the input of
whatever layer the project takes below it: that layer takes over
what the intent has staged for it instead of finding it first.

## Made from

A round on the intent reads:

- the briefs the principal says to mine: `00-brief.md` and any
  `00-brief-<name>.md`, approved or not;
- `decisions.md`, the project's decisions;
- the ledger, the project's single source of truth for state;
- sources, only as the principal directs;
- the intent as it stands, together with the project's threads in
  `threads.md`.

The first intent is created from the template `templates/intent.md`
as version 0.1, with its history companion `10-intent.history.md`
from `templates/history.md` and the threads file `threads.md` from
`templates/threads.md`. The text is in the project's language.

## What it holds

The template gives the intent five sections. Each item in it carries
a stable ID with one of the prefixes of the intent: POS, FCT, REJ,
and THR for the threads beside it. The ID scheme is explained in the
[Glossary](../reference/glossary.md).

**Essence.** A few sentences: what the principal wants and why, as of
today.

**Positions (POS).** A position is what the principal holds or wants,
and why he holds it, in as many words as it takes to be understood
without loss of meaning. It names what it comes from, a brief or a
source. It is dated once: one date, the day the position took its
present shape. A position without an ID does not exist: it carries
its ID from birth, and the history records it by that ID.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that is written into the history in the same step that writes the
position. Earlier steps of a position are found by searching the
history for its ID; a position cites no record of the history. A
number stays in a position only where it is the rule or a threshold,
never as a measurement. Text leaves a position only into the
history, word for word.

A position says what is to be achieved and why. What realises it, a
file among it, is named in the solution design where the project
has one. Where the project has no solution design, the position
names the file itself. Where the output is only part of a file, or
the file does not exist yet, the position keeps the full
information. Where the position and what realises it say different
things, that is a finding, never mended in silence.

Ideas are placed on a horizon where the principal sees one:

- a proof of concept;
- the first version;
- a later version;
- good but far away.

**Facts (FCT).** A fact is what is the case, as the principal states
it on his word or as a source states it. A source's fact cites its
file; the principal's needs no citation. Verification is never
demanded. A fact is not a stance: making a source's fact the
principal's own stance is a new position. What Claude has worked out
is never a fact.

**Rejected directions (REJ).** What was considered and dropped, and
why.

**Candidate structure for the layer below.** An optional staging
area: what the layer below will need as soon as the principal sees
it, such as the recipients, the objective and the success criteria
where that layer is an assignment. These are positions with IDs like
everything else. The section is left out where the project takes no
layer below, and deleted once the layer exists and leads.

**Threads (THR), in `threads.md`.** The threads live in a file of
their own beside the intent, one file for the project. The intent
says what holds; the threads say what is being worked. A thread
names, right after its ID and in square brackets, the artefact it
concerns, as the state map names it; several where it concerns
several. A thread says what is open and where it came from. Its
origin is one of three:

- the principal's word, the default, which needs no mark;
- a document, cited by path;
- Claude's synthesis.

A thread carries the working debate for as long as it is unsettled:
what was said, what was tried, the plan of a change under way, the
proposals that await a decision. It is where an unfinished
conversation is saved before a session ends. A settled thread leaves
the file and is kept whole: what holds goes into the intent as a
position or a rejection, and the record of its closing in the
intent's history carries the thread's last wording word for word.
The threads file is part of the intent as the history is: freely
rewritten, with no version, no history and no row in the ledger of
its own. The intent's history records the birth and the closing of a
thread, not every saving of its debate.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, the whole is
coherent, nothing stands twice, every position carries its
provenance, and the whole has passed through a final reality check.
At that point Claude names the layers that can follow from the
intent, or offers the approval where the principal takes no layer:
a recommendation, never a gate.

## How it is found

The intent is found by elicitation, by questions, research and
sources; the method is explained in [Elicitation](elicitation.md).
A round starts in one of three ways:

- there is no intent yet, and the briefs are consolidated into the
  first one;
- a brief is pending or partial, and it is mined whole by whole, one
  brief at a time;
- an open thread, a new word of the principal's or what the
  recipients sent back, and the round starts there.

Briefs are offered before threads. Within a round, one theme is
worked at a time; the reality check comes last, before a lower layer
is proposed. Claude probes contradictions, gaps and unstated
assumptions. It challenges an idea on two questions kept apart,
whether it is good and whether it is feasible; this is a way of
asking, and nothing is recorded per idea. It reflects a brain-dump
back as structure before anything is written, offers options with
their trade-offs, and proposes research where a thread needs outside
grounding. Research runs on the principal's word. An independent
reality check by a challenger persona is offered once the joint one
is done, never run on Claude's own judgement.

At the round's end, before a lower layer is proposed or the intent
is approved, its Map is walked: a list of what the intent finds, in
whatever order it was found. An area may stay empty when it was
considered and found not to apply. The areas are:

- the essence: what the principal wants and why, as of today;
- the weight of every idea: what he holds and why, what he dropped
  and why, what he deferred, which is not dropped;
- the ground: what is the case, and on whose word or which source;
- the horizon: what is a proof of concept, the first version, later,
  or good but far away;
- what is open: what is undecided, what it would take to decide it,
  and which of it blocks the layer below;
- the briefs as wholes: whether the substance of each is in the
  intent, was dropped, or was knowingly left behind;
- what the layer below will need: the recipients, the objective and
  the success criteria, as soon as he sees them;
- reality: what of it is feasible, and where the wheel already
  exists.

The round ends with one write, on the principal's confirmation. On
the write, resolved threads move into positions or rejections, and
the Mined column of every brief touched is kept in the ledger. The
round closes by naming what changed and what stays open.

## Why

The intent exists because chat context dies. Anything of value must
live in a file, and the intent is that file for what the principal
holds.

It is rewritten, not appended, because an append-only log was tried
and rejected. A question-and-answer log left the current state of
the intent scattered across the brief, the log and the assignment,
with no single place answering "what do I want now".

It does not solve, because an intent that carries the solution
cannot be read as what is wanted. Over such an intent nobody can be
asked for a proposal of the whole solution.

The way to a position goes into the history in the same step as the
position, because that is the moment the whole context is at hand;
later it would be lost. A position keeps the full information where
its output is only part of a file, because another change may
rewrite that part and the detail would be lost with it.

A fact has a prefix of its own, because without one a fact would
have passed for a position. A thread carries its origin, so that a
hypothesis of Claude's stays visibly its own until the principal
takes it up. Rejected directions are kept, so that old ground is not
re-litigated and the reasoning is preserved for a later return to
the project.

Why the threads live in a file of their own rather than in the
intent's body, and why the intent is said to be never finished, are
not recorded in the inputs of this page.

## A worked example

A generic position, in the shape the template gives. It carries its
ID, what the principal holds, the reason he holds it, and where it
comes from:

```
## Positions
- **POS.0010** A new colleague is onboarded from one checklist, kept
  in the team handbook, and from nothing else. Reason: with two
  lists nobody knows which one is current, and a step missing from
  one of them is noticed only when it has been missed. From
  `00-brief.md`. 2026-10-14.
```

The sentence passes the test of the intent: it would still hold if
the checklist were a wiki page, a printed sheet or a form in a tool.
Which tool holds the checklist, and how a step is ticked off, is
solution. If the principal later moved the checklist into a shared
tool, the position would be rewritten in place, and its earlier
wording would go word for word into the history under the same ID.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
