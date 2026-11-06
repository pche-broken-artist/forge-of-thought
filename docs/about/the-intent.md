---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 50dbc77205ae64e8
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

The intent is the artefact of the chain that says what the principal
(the person whose thinking is being forged) wants and why, as it
stands today. This page is for the user who works an intent with
Claude and for the evaluator who wants to know what the file is, what
belongs in it and what is kept out of it on purpose. It explains; how
an intent is iterated is the page [Forge the
intent](../use/forge-the-intent.md), and every term used here is in
the [Glossary](../reference/glossary.md).

## What it is

The intent is the file `10-intent.md` of a project, the trunk of its
chain: a chain starts at a brief, the intent chisels the briefs into
what the principal holds, and every layer below is derived from it.

It is the consolidated current state of what the principal holds. It
is not a log. Every round rewrites it for coherence and never appends
to it; what changed, and why, is recorded in its history companion
beside it (see [Versioning and history](versioning-and-history.md)).

It exists because the context of a conversation dies and anything of
value must live in a file. It is the document to read when returning
to a project after weeks, instead of excavating old conversations.

An intent says what is wanted and why, and it does not solve. The
test of a sentence is this: would it still hold if the thing were
realised in a wholly different way? If it would, the sentence is
intent. If it would not, it is solution and belongs in [The solution
design](the-solution-design.md). A principle the principal sets for
the solution, which the realisation must respect whatever its shape,
is intent; the mechanism that honours it is solution. What the
principal wants a user to be able to do, and what must be true when
it is done, is intent; how it is done, what it is built of, its steps
and the checks it runs, is solution. The division is by kind of
content, never by who said it: an idea of the principal's about how
to build something is solution too.

## Who writes and reads it

The principal writes it with Claude. The principal owns the
substance; Claude composes the wording. A thread closes only on the
principal's word.

Its audience is the principal and Claude only: it is a working
document, never handed to anyone. Claude reads it, together with the
project's threads, at the start of every round, and the layer below
is derived from it.

## Made from

- The briefs the principal says to mine: `00-brief.md` and any
  `00-brief-<name>.md`, approved or not.
- The project's decisions and its ledger (the project's state
  report, made by a script at read time).
- Sources, only as the principal directs.
- The conversation itself: what the principal says, and what Claude
  draws out by questions.
- Research, where a thread needs outside grounding and the principal
  asks for it.

## What it holds

The shape of the file is the template `templates/intent.md`. Its
sections, in order:

- **Essence**: a few sentences on what the principal wants and why,
  as of today.
- **Positions** (prefix `POS`): statements the principal currently
  holds.
- **Facts** (prefix `FCT`): what is the case.
- **Rejected directions** (prefix `REJ`): what was considered and
  dropped, and why.
- **Candidate structure for the layer below**: an optional staging
  area for what the next layer will need as soon as the principal
  sees it, such as the recipients, the objective and the success
  criteria of an assignment. It is left out where the project takes
  no layer and deleted once the layer exists.

Beside the file, in the directory `threads/`, live the threads
(prefix `THR`): what is open and being worked.

### A position

A position says what the principal holds and why he holds it, in as
many words as it takes to be understood without loss of meaning. It
names what it comes from, a brief or a source. It is dated once: one
date, the day it took its present shape. A position without an ID
does not exist; it carries its ID from birth.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that is written into the history in the same step that writes the
position, while the whole context is at hand. Earlier steps are found
by searching the history for the position's ID; the position itself
cites no record of the history. A number stays in a position only
where it is a rule or a threshold, never as a measurement. Text
leaves a position only into the history, word for word.

A position says what is to be achieved and why. What realises it is
named in the solution design where the project has one. Where the
project has no solution design, the position names the file that
realises it, and where that is only part of a file, or the file does
not exist yet, the position keeps the full information, so that a
rewrite of that part cannot lose the detail. Where the position and
what realises it say different things, that is a finding (a
reviewer's result), never mended in silence.

Ideas are placed on a horizon where the principal sees one: a proof
of concept, the first version, a later one, or good but far away.
What he deferred is not dropped.

### A fact

A fact is what is the case: stated by the principal on his word, or
stated by a source and cited to its file. Verification is never
demanded. What Claude has worked out is never a fact, since a fact
is the principal's word or a source's. When the principal makes a
source's fact his own stance, that is a new position.

### A rejected direction

A rejected direction records what was dropped and the reason it was
dropped. It prevents old ground from being re-litigated and keeps the
reasoning for a later return to the project.

### A thread

A thread is one open matter of the intent: what is undecided, what it
would take to decide it, and whether it blocks the layer below. The
intent says what holds; the threads say what is being worked. A
thread carries the working debate for as long as it is unsettled:
what was said, what was tried, the plan of a change under way, the
proposals that await a decision. It is where an unfinished
conversation is saved before a session ends.

Each thread is a file of its own, `threads/THR.NNNN.md`, made from
`templates/thread.md`. Its header is its state and carries three
fields:

- `concerns`: the artefact it concerns, as `/forge` names it; several
  where several.
- `origin`: where it came from. The principal's word, which is the
  default; a document, by its path; or Claude's synthesis.
- `status`: `open` or `closed`.

The first sentence of a thread is its headline; its last dated
paragraph is its state. A thread has no title and no further fields.
It has no version and no history of its own. While open it is freely
rewritten, header included. A thread is never moved, renamed or
deleted. Closing a thread is `status: closed` in its header and a
`closed` record in the intent's history that says when and by what.
A closed thread is immutable and is its own archive. What returns
later is a new thread citing the old one. There is no list of threads
in a file; the list is made by the ledger script.

The threads are part of the intent as its history is. The intent's
history records the birth and the closing of a thread, not every
saving of its debate.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished.

Before a lower layer is derived from it, the whole is passed through
a final reality check: what of it is feasible, and where the wheel
already exists. When that completion is reached, Claude names the
layers that can follow from the intent, or offers the approval where
the principal takes none: a recommendation, never a gate.

## How it is found

The intent is found by elicitation; the method is the page
[Elicitation](elicitation.md). In short: Claude mines the briefs
with the principal whole by whole, probes contradictions, gaps and
unstated assumptions, and challenges an idea on two questions kept
apart, whether it is good and whether it is feasible. It reflects a
brain-dump back as structure before anything is written, offers
options with trade-offs and proposes research where a thread needs
outside grounding. Within a round one theme is worked at a time, and
the round is written once, at its end, on the principal's word. On
the write, resolved threads move into positions or rejections. The
text is in the project's language. The command that runs a round is
`/forge intent`, described in [Forge the
intent](../use/forge-the-intent.md).

## Why

The intent is one consolidated file because the alternative was
tried and rejected: an append-only log of questions and answers left
the current state of what was wanted scattered across the brief, the
log and the assignment, with no single place answering "what do I
want now".

The intent does not solve because an intent that carries the solution
cannot be read as what is wanted, and nobody can be asked for a
proposal of the whole solution over it.

The way to a position goes into the history, not into the position,
so that the position stays what the principal holds, readable without
loss of meaning, and the record is written while the whole context is
still at hand.

Facts have a prefix of their own because, without one, a fact would
have passed for a position.

A thread carries its origin so that a hypothesis of Claude's stays
visibly Claude's until the principal takes it up.

Threads are files of their own, one per thread, for three reasons:
two people working on different threads never conflict; Claude reads
only the threads it needs; and whatever reads the intent need not
handle blocks that carry a state of their own.

## A worked example

A position of a generic project, in the shape the template defines.
The slug and the content are placeholders.

```
## Positions
- **POS.0010** Every order the shop receives is confirmed to the
  customer within the hour, whatever channel it arrived by. Reason:
  a customer who hears nothing calls, and a call costs the team more
  than the order earned (`00-brief.md`). Present shape 2026-03-14.
```

The position says what is wanted and why, names the brief it comes
from, and is dated once. It would still hold if the confirmation were
sent by mail, by text message or by a phone call, so it is intent;
which channel is used, and by what system, belongs in the solution
design. How the shop came to the one-hour rule, and what was said on
the way, is in the record of the history that wrote the position, not
here.

The thread that was open while the rule was found would have stood
beside it as `threads/THR.0010.md`, its header `concerns: intent`,
`origin: the principal`, `status: open`, and would now be closed,
immutable, with a `closed` record in the intent's history.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
