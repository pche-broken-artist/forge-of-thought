---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 2c3eb364178d12ca
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

The intent is the document that says what the principal holds today:
what he wants, why, what is the case and what he dropped. The
principal is the person whose thinking is being forged. This page
explains what the intent holds, why it is rewritten every round
instead of growing as a log, and why solving goes elsewhere. It is
for a user who works an intent and for an evaluator who wants to
know what the document is.

## What it is

The intent is the file `10-intent.md` of a project. It is the
consolidated current state of what the principal holds. It is the
trunk of the chain of documents: every project has one after its
brief, and many projects end at it.

The intent is not a log. Each round rewrites it for coherence, so
that everything in it fits together and nothing is said twice. The
changes of a round are recorded in a history companion beside it
(see [Versioning and history](versioning-and-history.md)). The
intent is versioned like every artefact of the chain.

The intent says what is wanted and why, and it does not solve. The
test of a sentence is this question: would it still hold if the
thing were realised in a wholly different way? If it would, the
sentence is intent. If not, it is solution, and it belongs in
[The solution design](the-solution-design.md).

- A principle the principal sets for the solution is intent.
  It says what the realisation must respect, whatever its shape.
- The mechanism that honours that principle is solution.
- What the principal wants a user to be able to do, and what must
  be true when it is done, is intent.
  A command he asks for by name counts here too.
- How the command does it is solution.
  Its parts, its steps, their order and the checks it runs belong
  there.

The division is by the kind of content, never by who said it. An
idea of the principal's about how to build something is solution
too.

## Who writes and reads it

The principal and Claude write it together. The principal supplies
the substance. Claude composes the wording. Claude is the AI
assistant that works with the principal. The template marks its
audience as the principal and Claude only.

The intent is the document to read when returning to a project after
weeks. It replaces the excavation of old conversations.

## Made from

The intent is made from these inputs:

- the briefs the principal says to mine, approved or not;
- the project's decisions, `decisions.md`;
- the ledger (the state of the project, made by a script when it is
  read);
- sources, only as the principal directs;
- the conversation of the round.

The first intent is created from the template `templates/intent.md`
as version 0.1. Its history companion and an empty `threads/`
directory are made with it.

## What it holds

The intent holds four kinds of item, each with an ID of its own
prefix:

- **POS** (a position): what the principal holds or wants.
- **FCT** (a fact): what is the case.
- **REJ** (a rejected direction): what was considered and dropped,
  with the reason.
- **THR** (a thread): an open matter.
  A thread lives in a file of its own, not in the intent.

The template sets the sections in this order:

- Essence: what the principal wants and why, as of today.
- Positions.
- Facts.
- Rejected directions.
- Candidate structure for the layer below.
  This section is optional.
  It holds what the next layer will need as soon as the principal
  sees it, such as the recipients, the objective and the success
  criteria.
  It is left out where the project takes no layer below, and deleted
  once that layer exists and leads.

### A position

A position says what the principal holds and why it holds. It uses
as many words as it takes to be understood without loss of meaning.
It names what it comes from: a brief or a source. It is dated once,
with the day it took its present shape.

The way to a position does not belong in it. Why it changed, what
was said on the way, trials, measurements, counts, settled findings,
what others do and which research turned it all go into the history.
They are written there in the same step that writes the position,
while the whole context is at hand. Earlier steps of a position are
found by searching the history for its ID. A number stays in a
position only where it is the rule or a threshold, never as a
measurement.

A position carries its ID from its birth. A position without an ID
does not exist.

### A fact

A fact is what is the case. It is stated by the principal on his
word, or by a source cited to its file. Verification is never
demanded. When the principal makes a source's fact his own stance,
that is a new position. What Claude has worked out is never a fact,
because a fact is the principal's word or a source's.

### A rejected direction

A rejected direction records what was dropped and why. It prevents
old ground from being argued again. It keeps the reasoning for a
later return to the project.

### A thread

A thread is one open matter of the intent. It is a file,
`threads/THR.NNNN.md`, made from the template `templates/thread.md`.
The threads are part of the intent, as its history is. The intent
says what holds; the threads say what is being worked.

A thread's header is its state:

- `concerns`: the artefact it concerns, as the forge command names
  it; several where several.
- `origin`: the principal's word (the default), a document by path,
  or Claude's synthesis.
- `status`: `open` or `closed`.

The origin keeps a hypothesis of Claude's visibly Claude's until the
principal takes it up.

The body's first sentence is its headline. Its last dated paragraph
is its state. While a thread is open, it carries the working debate:
what was said, what was tried, the plan of a change under way and the
proposals that await a decision. It is where an unfinished
conversation is saved.

An open thread is rewritten freely, the header too. A thread has no
version and no history of its own. It is never moved, renamed or
deleted. Closing it sets `status: closed` and adds a record to the
intent's history saying when it closed and by what. The closed file
is immutable and is the archive. What holds goes into the intent as
a position or a rejection. A matter that returns is a new thread that
cites the old one.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, the whole is
passed through a final reality check.

## How it is found

The intent is found in a working conversation with Claude. The
briefs are mined one at a time, whole by whole. Contradictions, gaps
and unstated assumptions are probed. Ideas are placed on a horizon
where the principal sees one: a proof of concept, the first version,
a later one, or good but far away. How this conversation runs is
explained in [Elicitation](elicitation.md). How you start a round is
in [Forge the intent](../use/forge-the-intent.md).

## Why

**Why a file at all.** Chat context dies, and anything of value must
live in a file.

**Why one rewritten document and not a log.** An append-only log of
questions and answers was tried and dropped. It left the current
state scattered across the brief, the log and the assignment. No
single place answered "what do I want now". The intent is that place.

**Why the way to a position is kept out of it.** The reason is not
recorded.

**Why threads are files.** Two people working on different threads
never conflict. Claude reads only the threads it needs. The tool that
merges files need not handle blocks with an inner state.

**Why the intent does not solve.** An intent that carries the
solution cannot be read as what is wanted. Nobody can be asked for a
proposal of the whole solution over it.

**Why a fact has its own prefix.** Without one, a fact would pass
for a position.

## A worked example

A generic position with its reason, in the shape of the template:

```markdown
- **POS.0010** Every team sees the same weekly status of its open
  requests, so that nobody has to ask another team where a request
  stands. Reason: questions about status take up the start of every
  planning meeting today. From the brief. Dated 2026-01-15.
```

The sentence would hold however the status were produced: by a
report, a board or a mail. That is why it is intent. A sentence
naming the tool that produces the status would be solution.

A generic thread file beside it:

```markdown
---
id: THR.0010
concerns: intent
origin: the principal
status: open
---

Which requests count as open for the weekly status. Opened
2026-01-15.

2026-01-20: proposals await the principal's decision.
```

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
