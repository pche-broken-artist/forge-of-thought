---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: f1d50a87e47a09db
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
current state of what the principal holds. The principal is the
person whose thinking is being forged, with final authority over
every word of content. This page is for a user who works an intent
and for an evaluator who wants to know what it is. It explains what
the intent holds, why it is rewritten every round instead of growing
as a log, and where the solving of a matter goes instead.

## What it is

The intent is the file `10-intent.md` of a project, and it is the
trunk of every chain of documents: the chain starts at a brief, and
below the intent a project takes only the layers it needs. Many
projects end at the intent.

The intent is not an append-only log. Every round rewrites it for
coherence, so that it says what holds today, everything coherent and
nothing twice. What changed and why is recorded in its history
companion, the append-only file `10-intent.history.md` beside it
(see [Versioning and history](versioning-and-history.md)). The past
of a position is found there by searching for the position's ID,
never in the intent itself.

An intent says what is wanted and why, and it does not solve. What
the principal wants, what he does not want, what is the case, what
is open and what he dropped belong to it. How the things he wants
are realised belongs to the solution design (see
[The solution design](the-solution-design.md)).

The test of a sentence is one question: would it still hold if the
thing were realised in a wholly different way? If it would, the
sentence is intent. If it would not, the sentence is solution. The
division is by kind of content, never by who said it. An idea of the
principal's about how to build something is solution too. A
principle the principal sets for the solution (what the realisation
must respect whatever its shape) is intent. The mechanism that
honours it is solution. What the principal wants a user to be able
to do, and what must be true when it is done, is intent. A command
he asks for by name is intent as well. How that command does it,
what it is built of, its steps and the checks it runs, is solution.

Where a project has no solution design, an item of the intent names
the file that realises it. Where the item and what realises it say
different things, that is a finding (a reviewer's result), never
mended in silence.

## Who writes and reads it

The principal and Claude write it together. Claude composes the
wording, and the principal gives the substance. A thread closes only
on the principal's word. The template marks the audience as the
principal and Claude only: the intent is a working document, not a
handover to recipients.

The text is in the project's language, the `language` of its
project file, English when none is given. The notation stays
English throughout: the ID prefixes, the status words and the
front-matter keys.

## Made from

- The briefs the principal says to mine: `00-brief.md` and any later
  `00-brief-<name>.md`, approved or not.
- The project's decisions, `decisions.md`.
- The ledger, the single source of truth for a project's state,
  made by a script at read time.
- Sources, only as the principal directs.
- The conversation itself, reflected back as structure before it is
  written.

The first intent is created from `templates/intent.md` as version
0.1, with its history companion and an empty `threads/` folder.

## What it holds

The intent carries these sections, as `templates/intent.md` gives
them:

- **Essence**: a few sentences of what the principal wants and why,
  as of today.
- **Positions** (prefix `POS`): what the principal holds or wants.
- **Facts** (prefix `FCT`): what is the case.
- **Rejected directions** (prefix `REJ`): what was considered and
  dropped, with the reason.
- **Candidate structure for the layer below**: an optional staging
  area for what the next layer will need (the recipients, the
  objective, the success criteria) as soon as the principal sees it.
  It is left out where the project takes no layer, and deleted once
  that layer exists and leads.

The open matters carry the prefix `THR` and live outside the file,
as threads (below).

### A position

A position says what the principal holds and why he holds it. It
takes as many words as it needs to be understood without loss of
meaning. It names what it comes from, a brief or a source. It
carries one date: the day the position took its present shape.

A position does not carry the way to it. Why it was changed, what
was said on the way, trials, measurements, settled findings and the
research that turned it are written into the history, in the same
step that writes the position. A number stays in a position only
where the number is the rule or a threshold, never as a measurement.
A position without an ID does not exist: it carries its ID from
birth.

### A fact

A fact is what is the case. It is stated either by the principal on
his own word or by a source, cited to its file. Verification is
never demanded. When the principal makes a source's fact his own
stance, that is a new position. What Claude has worked out is never
a fact, because a fact is the principal's word or a source's.

### A rejected direction

A rejected direction records what was considered and dropped, and
why. It keeps old ground from being argued again. It also preserves
the reasoning for anyone who returns to the project later. A matter
the principal deferred is not dropped and is not a rejection.

### Threads

What is being worked lives in threads, one file per thread, in the
project's `threads/` folder beside the intent, named
`threads/THR.NNNN.md` from `templates/thread.md`. The intent says
what holds, and the threads say what is being worked. A thread says
what is open and where it came from. It carries the working debate
for as long as it is unsettled: what was said, what was tried, the
plan of a change under way and the proposals that await a decision.
An unfinished conversation is saved into its thread.

A thread's header is its state:

- `concerns`: the artefact it concerns, as `/forge` names it, or
  several, comma-separated.
- `origin`: the principal's word (the default), a document by path,
  or Claude's synthesis.
- `status`: `open` or `closed`.

A thread has no title and no further fields. Its first sentence is
its headline, and its last dated paragraph is its state. No list of
threads is kept by hand: the ledger script makes it.

While a thread is open, it is rewritten freely, the header too. It
has no version and no history of its own. A thread is never moved,
renamed or deleted. Closing a thread sets `status: closed` and adds
a `closed` record to the intent's history that says when and by
what. The closed file is immutable and is the archive. What holds
goes into the intent, as a position or a rejection. A matter that
returns becomes a new thread citing the old one.

### A worked example

A generic position in the shape the template gives, with its reason
and its provenance:

```markdown
## Positions
- **POS.0010** Every report goes out in one shared format, so that
  a reader who knows one report can read any other without
  learning a new layout. From `00-brief.md`. Present shape
  YYYY-MM-DD.
```

The sentence passes the test: it would still hold however the format
were produced. A sentence such as "a script fills the format from a
spreadsheet" would fail it, and would belong in the solution design.

An open thread beside it, in the shape of `templates/thread.md`:

```markdown
---
id: THR.0010
concerns: intent
origin: Claude's synthesis
status: open
---

Which readers the shared report format must serve first is not yet
settled. ... Opened YYYY-MM-DD.
```

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, the whole
passes through a final reality check: what of it is feasible, and
where the wheel already exists. When completion is reached, Claude
names the layers that can follow, or offers the approval where the
principal takes no layer. That is a recommendation, never a gate.

## How it is found

The intent is found in a working conversation between the principal
and Claude, through `/forge intent` (see
[Forge the intent](../use/forge-the-intent.md); the way of drawing
out what the principal holds is [Elicitation](elicitation.md)). The
briefs are mined one whole brief at a time, briefs before threads.
Within a round one theme is taken at a time. Claude probes
contradictions, gaps and unstated assumptions. It asks of each idea
two separate questions: whether it is good and whether it is
feasible. Ideas are placed on a horizon where the principal sees
one: a proof of concept, the first version, a later one, or good but
far away.

At the write, resolved threads move into positions or rejections.
One write closes the round as one version, with its changes recorded
in the history.

## Why

- **Why a file at all.** Chat context dies, and anything of value
  must live in a file. The intent is the document to read when
  returning to a project after weeks, instead of digging through old
  conversations.
- **Why not a log.** An append-only question-and-answer log was
  tried and rejected. It left the current state scattered across the
  brief, the log and the assignment, with no single place answering
  "what do I want now".
- **Why the way to a position goes into the history.** It is written
  in the same step that writes the position, while the whole context
  is at hand.
- **Why threads are files.** Two people working on different threads
  never conflict. Claude reads only the threads it needs.
- **Why a fact has a prefix of its own.** Without one, a fact would
  pass for a position.
- **Why a thread carries its origin.** A hypothesis of Claude's then
  stays visibly Claude's until the principal takes it up.
- **Why the intent does not solve.** An intent that carries the
  solution cannot be read as what is wanted. Nobody can then be
  asked for a proposal of the whole solution over it.

For every term of the forge in one line, see the
[Glossary](../reference/glossary.md).

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
