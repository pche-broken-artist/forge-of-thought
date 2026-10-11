---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 4413e1ef7479c5af
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

The intent is the working document of a project: the consolidated
current state of what the principal (the person whose thinking is
being forged) holds, in one file, `10-intent.md`. This page says
what the intent holds, why it is rewritten rather than appended to,
and where the solving goes instead. It is written for the user of
the forge and for an evaluator who wants to understand the trunk of
every project before reading one.

## What it is

The intent chisels the briefs into what the principal holds: in
plain terms, it consolidates what he wrote and said into one
coherent statement of what he wants and why. It is the trunk of the
chain: every project starts at a brief and continues into an intent,
and whatever layers the project takes below it are derived from it.

It is a current state, not a log. Each round it is rewritten for
coherence, and what changed is recorded in its history companion
(the append-only file beside it, `10-intent.history.md`, that keeps
one record per change). Everything in it is coherent, nothing stands
twice, and every position names where it comes from.

It says what is wanted and why, and it does not solve. What it says
would still hold however the thing were realised. How the thing is
realised belongs to the solution design (see
[The solution design](the-solution-design.md)).

## Who writes and reads it

The principal and Claude write it together, and they are its only
audience. The principal owns the substance: what is held, what is
dropped, when a thread is settled. Claude owns the wording: it mines
the briefs with him, probes contradictions, gaps and unstated
assumptions, reflects a brain-dump back as structure before anything
is written, offers options with their trade-offs, and runs the final
reality check with him. A thread closes only on the principal's
word.

The intent is also the document to read when returning to a project
after weeks: it answers "what do I want now" without excavating old
conversations.

## Made from

- The briefs the principal says to mine: `00-brief.md` and any
  later `00-brief-<name>.md`, approved or not.
- `decisions.md`, the project's record of decisions.
- The ledger, the project's single file of state.
- Sources, only as the principal directs. What someone said in a
  source is never silently promoted to the principal's own position.
- The intent as it already stands, read together with the project's
  threads in `threads.md`.
- The conversation itself: what the principal says in the round.

The first intent is created from `templates/intent.md` as version
0.1, with its history companion from `templates/history.md` and its
threads file from `templates/threads.md`. Its text is in the
project's language.

## What it holds

The template gives the intent five sections. The items of four of
them carry stable IDs with a prefix each: POS, FCT, REJ in the intent
itself, THR in the threads file beside it. Naming the prefixes is as
far as this page goes; how the numbers are given is the ID scheme's.

### Essence

A few sentences of narrative: what the principal wants and why, as
of today.

### Positions (POS)

A position is a statement the principal currently holds or wants. It
says what he holds and why it holds, in as many words as it takes to
be understood without loss of meaning. It names what it comes from,
a brief or a source. It is dated once: one date, the day it took its
present shape. A position without an ID does not exist: it carries
its ID from birth, and the history records it by that ID.

What does not belong in a position is the way to it:

- why it was changed;
- what was said on the way;
- trials, measurements, counts;
- findings settled;
- what others do;
- which research turned it.

All of that goes into the history in the same step that writes the
position, while the whole context is at hand. Earlier steps of a
position are found by searching the history for its ID, and a
position cites no record of the history. A number stays in a
position only where it is the rule or a threshold, never as a
measurement. Text leaves a position only into the history, word for
word. How the companion keeps that past is
[Versioning and history](versioning-and-history.md).

A position says what is to be achieved and why. What realises it,
a file among it, is named in the solution design where the project
has one, and the realisation is the file's. Where the project has no
solution design, the position names the file. Where the output is
only part of a file, or the file does not exist yet, the position
keeps the full information, since another change may rewrite that
part and the detail would be lost. Where a position and what
realises it say different things, that is a finding, never mended in
silence.

Ideas are placed on a horizon where the principal sees one: a proof
of concept, the first version, a later one, or good but far away.

### Facts (FCT)

A fact is what is the case. It is stated by the principal on his
word, which needs no citation, or by a source, cited to its file.
Verification is never demanded. A fact is not a stance: making a
source's fact the principal's own stance is a new position. What
Claude has worked out is never a fact, since a fact is the
principal's word or a source's.

### Rejected directions (REJ)

What was considered and dropped, with the reason it was dropped.
The section prevents re-litigating old ground and preserves the
reasoning for a later return to the project.

### Threads (THR), in `threads.md` beside it

The threads live in a file of their own beside the intent, one for
the project. The intent says what holds; the threads say what is
being worked. A thread says what is open and where it came from, and
carries the working debate for as long as it is unsettled: what was
said, what was tried, the plan of a change under way, the proposals
that await a decision. It is where an unfinished conversation is
saved before a session ends.

Every thread names, right after its ID and in square brackets, the
artefact it concerns, as the state map of `/forge` names it, and
several where it concerns several. The reason for naming the
artefact is not recorded.

A thread carries its origin: the principal's word, which is the
default and needs no mark; a document, by path; or Claude's
synthesis.

A settled thread leaves the file and is kept whole: what holds goes
into the intent as a position or a rejection, and the record of its
closing in the intent's history carries the thread's last wording
word for word. The threads file is part of the intent as the history
is: freely rewritten, with no version, no history and no row in the
ledger of its own. The intent's history records the birth and the
closing of a thread, not every saving of its debate.

### Candidate structure for the layer below

An optional staging area: what the layer below will need as soon as
the principal sees it. Where that layer is an assignment, these are
the recipients, the objective and the success criteria, written as
positions with IDs like everything else. It is left out where the
project takes no layer, and deleted once the layer exists and leads.

## Complete when

The intent is complete for now when no thread blocks the next layer.
It is never finished. Before a lower layer is derived, the whole is
passed through a final reality check. When completion is reached,
Claude names the layers that can follow from it, or offers the
approval where the principal takes none: a recommendation, never a
gate.

## How it is found

The intent is found by elicitation, round by round, through
`/forge intent`; the method is [Elicitation](elicitation.md), the
job is [Forge the intent](../use/forge-the-intent.md). A round
starts from a brief not yet mined, from an open thread, from a new
word of the principal's or from what the recipients sent back, and
works one theme at a time. At its end the definition's Map is
walked: eight areas, each of which may stay empty when it was
considered and found not to apply.

- The essence: what the principal wants and why, as of today.
- The weight of every idea: what he holds and why, what he dropped
  and why, what he deferred, which is not dropped.
- The ground: what is the case, and on whose word or which source.
- The horizon: a proof of concept, the first version, later, or
  good but far away.
- What is open: what is undecided, what it would take to decide it,
  and which of it blocks the layer below.
- The briefs as wholes: whether the substance of each is in the
  intent, was dropped, or was knowingly left behind.
- What the layer below will need: recipients, objective and success
  criteria, as soon as he sees them.
- Reality: what of it is feasible, and where the wheel already
  exists.

Two instruments serve it. `/research <topic>` is proposed where a
thread needs outside grounding and runs on the principal's word.
`/challenge <persona> intent` is the independent reality check,
offered once the joint one is done and never run on Claude's own
judgement. Claude challenges an idea on two questions kept apart,
whether it is good and whether it is feasible: a way of asking,
nothing recorded per idea.

On the write, resolved threads move into positions or rejections,
and the Mined column of every brief touched is kept current.

## Why

The intent exists because chat context dies and anything of value
must live in a file. The alternative was tried: an append-only
question-and-answer log beside the brief. It was rejected because it
left the current state of what was wanted scattered across the
brief, the log and the assignment, with no single place answering
"what do I want now". The intent replaced it, and that is why it is
rewritten for coherence each round and never appended to: a log
records a trail, the intent records a state.

The way to a position goes into the history rather than the position
because the position is the current state and the history is the
record. It is written in the same step, while the whole context is
at hand, so that nothing of the way is lost when the position is
later reworded.

A fact has a prefix of its own because, without one, a fact would
have passed for a position. The two differ in kind: a fact is what
is the case, on the principal's word or a source's; a position is
what he holds or wants.

A thread carries its origin so that a hypothesis of Claude's stays
visibly its own until the principal takes it up.

The staging area for the layer below exists so that the layer takes
the recipients, the objective and the success criteria over instead
of finding them first.

The intent does not solve because an intent that carries the
solution cannot be read as what is wanted, and nobody can be asked
for a proposal of the whole solution over it. The test of a
sentence: would it still hold if the thing were realised in a wholly
different way? If it would, it is intent. If not, it is solution. A
principle the principal sets for the solution, what the realisation
must respect whatever its shape, is intent; the mechanism that
honours it is solution. What the principal wants the user to be able
to do, and what must be true when it is done, is intent, a command
he asks for by name among it; how the command does it, its steps,
their order and the checks it runs, is solution. The division is by
kind of content, never by who said it: an idea of the principal's
about how to build something is solution too.

## A worked example

A generic project: a team wants one handbook for new colleagues.
One position of its intent, in the shape the template gives, might
read as follows.

- **POS.0010** The handbook is one file that a new colleague reads
  before the first day, and it is rewritten whenever a rule
  changes, never appended to. Reason: a colleague who opens it must
  find the rules as they hold today, not the trail of how they came
  to hold. From the brief.

What stays out of the position goes into the history record written
in the same step: that an appended changelog was kept for two months
and nobody read it, that a wiki was weighed and dropped for its cost,
and what was said in the round that settled it. The position is
dated once, on the day it took this shape. Were the team to decide
how the file is published and who edits it, that would be solution,
not intent: the position above would hold whichever way it was
realised.

Every term of the forge used here is listed in one line in the
[Glossary](../reference/glossary.md).

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [Elicitation](elicitation.md): how the intent is found, the Map
  walked at the round's end.
- [Versioning and history](versioning-and-history.md): the history
  companion a position's past lives in.
- [The solution design](the-solution-design.md): where the solution
  goes instead.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
