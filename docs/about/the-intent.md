---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 70f88e448384d14f
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
principal is the person whose thinking is being forged. This page is
for anyone who uses the intent and for anyone who evaluates the
forge, and it explains what the intent holds, why it is rewritten
every round and where the solution goes instead.

## What it is

The intent is the file `10-intent.md` of a project, the trunk of its
chain of documents. It is the consolidated current state of what the
principal holds. It is not a log. Each round of work rewrites it for
coherence, and the changes go into its history companion beside it
(see [Versioning and history](versioning-and-history.md)).

An intent says what is wanted and why, and it does not solve. How
the things wanted are realised belongs to the solution design (see
[The solution design](the-solution-design.md)).

The test of a sentence is one question: would it still hold if the
thing were realised in a wholly different way? If it would, the
sentence is intent. If it would not, it is solution.

The division is by the kind of content, never by who said it. An
idea of the principal's about how to build something is solution
too. A principle the principal sets for the solution is intent; the
mechanism that honours it is solution. A command the principal asks
for by name is intent; how the command does its work is solution.

## Who writes and reads it

The principal and Claude write it together. Claude composes the
wording; the principal owns the substance. A thread closes only on
the principal's word. The intent's audience is the principal and
Claude only: it is a working document, not a handover to anyone
else.

## Made from

- the briefs the principal says to mine (a brief is the principal's
  own text of what he wants)
- the record of the principal's decisions, `decisions.md`
- the ledger (the file that holds the project's state)
- sources, only as the principal directs
- the conversation of each round

The first intent consolidates the briefs. Later rounds start from a
brief not yet mined, from an open thread, from a new word of the
principal's or from what the recipients sent back.

## What it holds

The intent has the sections its template gives:

- **Essence**: a few sentences on what the principal wants and why,
  as of today.
- **Positions** (prefix `POS`): what the principal holds or wants,
  each with its reason and its provenance.
- **Facts** (prefix `FCT`): what is the case, on the principal's word
  or on a source cited to its file.
- **Rejected directions** (prefix `REJ`): what was considered and
  dropped, and why.
- **Candidate structure for the layer below**: optional; what the
  next layer will need as soon as the principal sees it, as positions
  with IDs.

A position says what the principal holds and why, in as many words
as it takes to be understood without loss of meaning. It names what
it comes from, such as a brief or a source. It carries one date: the
day it took its present shape. The way to it does not belong in it.
Why it changed, what was said, trials and research that turned it go
into the history, written in the same step as the position.

A fact is what is the case. Verification is never demanded. What
Claude has worked out is never a fact, since a fact is the
principal's word or a source's. Making a source's fact the
principal's own stance is a new position.

A rejected direction keeps the reason it was dropped. Ideas the
principal has deferred are not dropped. Where he sees a horizon, an
idea is placed on it: a proof of concept, the first version, a later
one, or good but far away.

### Threads

What is still being worked lives in threads (prefix `THR`), one file
per thread in `threads/` beside the intent. The intent says what
holds; the threads say what is being worked. A thread carries the
working debate while it is unsettled: what was said, what was tried,
the plan of a change under way and the proposals that await a
decision. It is where an unfinished conversation is saved.

A thread's header is its state:

- `concerns`: the artefact it concerns, several where several
- `origin`: the principal's word (the default), a document by path,
  or Claude's synthesis
- `status`: `open` or `closed`

A thread is rewritten freely while it is open, its header too. It has
no version and no history of its own. It is never moved, renamed or
deleted. Closing a thread sets `status: closed`, and a record in the
intent's history says when and by what. The closed file is immutable
and is the archive. A matter that returns becomes a new thread citing
the old one.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, the whole
passes through a final reality check. When it is complete for now,
Claude names the layers that can follow, or offers the approval where
the project takes no layer below. That is a recommendation, never a
gate. The reason it is never finished is not recorded.

## How it is found

The intent is found by conversation with the principal (see
[Elicitation](elicitation.md)), and it is iterated through its
definition (see [Forge the intent](../use/forge-the-intent.md)).
Claude mines the briefs one at a time, probes contradictions, gaps
and unstated assumptions, and asks of an idea whether it is good and
whether it is feasible, as two separate questions. Research is
proposed where a thread needs outside grounding. At the end of a
round, resolved threads become positions or rejected directions, and
the round is written once.

## Why

The intent exists because chat context dies. Anything of value must
live in a file. The intent is the document to read when returning to
a project after weeks, instead of digging through old conversations.

It is rewritten rather than appended to. An earlier design used an
append-only log of questions and answers, and it was rejected. The
reason: it left the current state scattered across the brief, the log
and the assignment, with no single place that answered "what do I
want now".

Threads are files of their own. Because each thread is a separate
file, two people working on different threads never conflict. Claude
also reads only the threads it needs.

A thread carries its origin so that a hypothesis of Claude's stays
visibly Claude's until the principal takes it up. Facts have a prefix
of their own because without it a fact would pass for a position.

The intent does not solve. The reason: an intent that carries the
solution cannot be read as what is wanted, and nobody can be asked
for a proposal of the whole solution over it.

## A worked example

A generic position with its reason, in the shape the template gives:

```
- **POS.0010** The weekly report reaches the team before the Monday
  meeting. Reason: the week's decisions are taken at that meeting,
  and a report that arrives later decides nothing. From
  `00-brief.md`. Present shape <date>.
```

The test holds: the sentence stays true whether the report is
e-mailed, printed or shown on a screen. A sentence such as "a
script sends the report by e-mail on Sunday night" would not survive
a different realisation, so it is solution and belongs in the
solution design.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
