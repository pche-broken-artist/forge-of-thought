---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 6e2bd5ac36c1088f
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.1390
  - projects/forge/10-intent.md#REJ.0010
---

# The intent

The intent is the working document of a project: one file
(`10-intent.md`) that holds the consolidated current state of what
the principal (the person whose thinking is being forged) wants and
holds. This page says what the intent holds, why it is rewritten in
every round and never kept as a log, and where solving goes instead.
It is for anyone who works on an intent and for anyone who wants to
judge what kind of document it is.

## What it is

The intent is a current state, not an append-only log. It is
rewritten for coherence in every round. A round is one stretch of
work on the intent that ends in one write. What changed in a round
is recorded in the history companion, which is a file beside the
intent (see [Versioning and history](versioning-and-history.md)).
The body shows what holds now.

The intent says what the principal wants and why. It does not solve.
How the things wanted are realised belongs to the solution design,
which is a document of its own (see
[The solution design](the-solution-design.md)).

The intent is the document to read when returning to a project
after weeks, in place of digging through old conversations.

## Who writes and reads it

The principal and Claude write the intent together. Claude composes
the wording. The principal decides the substance. The text is in the
project's language.

The header of the file names its audience: the principal and Claude
only. The principal reads the intent to see what holds today. Claude
reads it as it stands at the start of a round, together with the
project's threads (the matters still being worked, see
[Threads](threads.md)). A lower layer (a further document below the
intent, an assignment for example) is derived from it.

## Made from

The file is made from the template `templates/intent.md`. Its
history companion (`10-intent.history.md`) and an empty `threads/`
directory are made beside it.

Its content comes from:

- the briefs the principal says to work through: `00-brief.md` and
  any `00-brief-<name>.md`, approved or not (for what a brief is,
  see the [Glossary](../reference/glossary.md));
- the decisions file of the project (`decisions.md`);
- the ledger (the file that shows the state of the project, remade
  by a script after every write);
- sources (outside documents, each cited by its file), only as the
  principal directs;
- the conversation of the round.

## What it holds

### The sections

The header carries the version, the status (`draft`, `approved` or
`superseded`), the project and the audience. The body has five
sections, in this order:

- Essence: three to ten sentences on what the principal wants and
  why, as of today.
- Positions (prefix `POS`): the statements the principal currently
  holds.
- Facts (prefix `FCT`): what is the case.
- Rejected directions (prefix `REJ`): what was considered and
  dropped, and why.
- Candidate structure for the layer below: an optional staging area
  for what the layer below will need, filled as soon as the
  principal sees it. Where that layer is an assignment, it holds the
  recipients, the objective and the success criteria. They are
  written as positions with IDs, like everything else. The section
  is left out where the project takes no layer below. It is deleted
  once the layer exists and leads.

Everything in the intent is coherent, and nothing stands in it
twice. What the principal deferred is not dropped. Where the
principal sees a horizon, an idea is placed on it: a proof of
concept, the first version, a later one, or good but far away.

### A position

A position says what the principal holds and why it holds. It is as
long as it must be to be understood without loss of meaning. It
names what it comes from: a brief or a source. It is dated once. The
one date is the day the position took its present shape. A position
carries its ID from its birth, and the history records it by that
ID.

The way to a position does not belong in the position:

- why it was changed;
- what was said on the way;
- trials, measurements and counts;
- findings that were settled;
- what others do;
- which research turned it.

All of that is written into the history, in the same step that
writes the position. A record of the history may carry what was said
and how the change was reached. The earlier steps of a position are
found by searching the history for its ID. The position itself cites
no record of the history. A number stays in a position only where it
is the rule or a threshold, never as a measurement. Text leaves a
position only into the history, word for word.

### A fact and a rejected direction

A fact is what is the case. It is stated by the principal on the
principal's own word, or by a source cited to its file. Verification
is never demanded. A position is what the principal holds or wants.
When the principal takes a fact of a source as the principal's own
stance, that is a new position. What Claude has worked out is never
a fact.

A rejected direction says what was considered and dropped, with the
reason.

### What is being worked

What is being worked lives in threads (prefix `THR`), which are
files of their own beside the intent and are read with it: the
intent says what holds, the threads say what is being worked (see
[Threads](threads.md)).

### What it leaves to the solution

What the principal wants, what the principal does not want, what is
the case, what is open and what was dropped belong to the intent.
How the things wanted are realised belongs to the solution design.

The test of a sentence is one question: would it still hold if the
thing were realised in a wholly different way? If it would, it is
intent. If it would not, it is solution.

- A principle the principal sets for the solution (what the
  realisation must respect whatever its shape) is intent. The
  mechanism that honours the principle is solution.
- What the principal wants the user of the thing to be able to do,
  and what must be true when it is done, is intent. A command the
  principal asks for by name is intent too. How the command does it
  (what it is built of, its steps and their order, the checks it
  runs) is solution.
- The division is by kind of content, never by who said it. The
  principal's own idea about how to build something is solution too.

An item of the intent says what is to be achieved and why. What
realises it is named in the solution design where the project has
one. Where the project has none, the item names the file that
realises it. Where the output is only part of a file, or the file
does not exist yet, the item keeps the full information.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished.

Before a lower layer is derived, the whole intent passes a final
reality check: what of it is feasible, and what already exists and
need not be invented. Claude runs this check with the principal. An
independent reality check (`/challenge <persona> intent`) is offered
once the joint one is done. It never runs on Claude's own judgement.

When the intent is complete for now, Claude names the layers that
can follow from it. Where the principal takes no layer, Claude
offers the approval of the intent. Either is a recommendation, never
a gate.

## How it is found

The intent is found in conversation between the principal and
Claude, by elicitation (see [Elicitation](elicitation.md)). Its
definition (the file that says what the intent is, what it holds and
how it is elicited) is `.claude/skills/forge/states/intent.md`. The
steps of a round are on
[Forge the intent](../use/forge-the-intent.md).

Claude helps the principal in these ways:

- It works through the briefs with the principal, one brief at a
  time, each as a whole.
- It probes contradictions, gaps and unstated assumptions.
- It challenges an idea on two questions kept apart: whether the
  idea is good, and whether it is feasible. This is a way of asking.
  Nothing is recorded per idea.
- It reflects a brain-dump back as structure before anything is
  written.
- It offers options with their trade-offs.
- It proposes research (`/research <topic>`) where a thread needs
  outside grounding. The research runs on the principal's word.
- It runs the final reality check with the principal.

Where a round starts depends on where the project stands:

- With no intent yet, the briefs are consolidated into the first
  one.
- With a brief not yet worked through, or worked through only in
  part, that brief comes first. Briefs are offered before threads.
- Otherwise the round starts at an open thread, at a new word of the
  principal or at what the recipients sent back.

Within a round one theme is worked at a time. The reality check
comes last.

What the intent finds is listed in the Map of its definition, in
whatever order the conversation takes:

- the essence: what the principal wants and why, as of today;
- the weight of every idea: what is held and why, what was dropped
  and why, and what was deferred;
- the ground: what is the case, and on whose word or which source;
- the horizon, where the principal sees one: what is a proof of
  concept, the first version, later, or good but far away;
- what is open: what is undecided, what it would take to decide it,
  and which of it blocks the layer below;
- the briefs as wholes: whether the substance of each is in the
  intent, was dropped, or was knowingly left behind;
- what the layer below will need: the recipients, the objective and
  the success criteria, as soon as the principal sees them;
- reality: what of it is feasible, and what already exists.

The Map of the definition is walked at the end of a round, before a
lower layer is proposed or the intent is approved. An area may stay
empty when it was considered and found not to apply. The round ends
with Claude naming what changed and what stays open.

## Why

The intent exists as a file for one reason: the context of a
conversation dies, and anything of value must live in a file.

The intent is a current state and not a log of questions and
answers. The reason: such a log, kept beside the brief, leaves the
current state of the intent scattered across the brief, the log and
the assignment. No single place then says what the principal wants
now.

The intent is rewritten in every round for coherence: everything in
it agrees, and nothing stands twice.

The way to a position is written into the history in the same step
as the position. The reason: the whole context is at hand at that
moment. Why the way is kept out of the position itself: the reason
is not recorded.

Facts have a prefix of their own. Without it, a fact would pass for
a position.

Rejected directions are kept with their reasons. They prevent old
ground from being argued again, and they preserve the reasoning for
a later return to the project.

The intent does not solve. The reason: an intent that carries the
solution cannot be read as what is wanted, and nobody can be asked
for a proposal of the whole solution over it.

An item keeps the full information where the output is only part of
a file or the file does not exist yet. The reason: another change
may rewrite that part, and the detail would be lost.

The candidate structure is staged in the intent for the layer below.
That layer then takes it over and does not have to find it first.

## A worked example

A project about the first week of a new colleague holds this
position:

```
- **POS.0010** A new colleague can find out alone, within the first
  week, whom to ask about what. Reason: the questions come when
  nobody is at hand, and a newcomer who has to wait stops asking.
  From the brief `00-brief.md`. Present shape 2026-03-02.
```

The position says what the principal holds, gives the reason, names
the brief it comes from and carries one date.

Three other sentences came up in the same round. Each goes to its
own place:

| Sentence | Where it goes | Why |
|---|---|---|
| "Whatever form the answer takes, it can be read without a login." | The intent, as a position | It is a principle the realisation must respect whatever its shape. |
| "The answer is one page with a table of names and topics." | The solution design | It would not hold if the thing were realised in a wholly different way. |
| "Two rounds of introductions were tried, and three of five newcomers still did not know whom to ask." | The history, in the record of the position | It is a trial and a count: the way to the position, not what is held. |

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Threads](threads.md): what a thread is, what it holds and why
  threads are files of their own.
- [Elicitation](elicitation.md): how the intent is found.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
