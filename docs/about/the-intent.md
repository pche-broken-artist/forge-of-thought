---
generated: 2026-10-09
made: derived
inputs-hash: cf8c41caf5b14e9d
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - projects/forge/10-intent.md
---

# About the intent

This page explains what the intent is, what it holds and why it is
shaped the way it is. It is for the person whose thinking is being
forged and for anyone judging whether the forge does what it claims.
It was put together from the intent's definition
(`.claude/skills/forge/states/intent.md`), its template
(`templates/intent.md`), the threads template (`templates/threads.md`)
and the design positions of the forge's own intent
(`projects/forge/10-intent.md`).

## What the intent is

The intent, `10-intent.md`, is the working document of a project: the
consolidated current state of what the principal holds. It is the
trunk of the chain. The briefs are chiselled into it; from the briefs,
the sources and the conversation it keeps what matters as positions,
what is the case as facts, what is undecided as threads, and what was
dropped as rejections with the reason.

It is not an append-only log. Every round rewrites it for coherence,
and what changed is recorded in its history companion, never in the
body. The reason is that chat context dies: anything of value must
live in a file. The intent is the document to read when returning to
a project after weeks, instead of excavating old conversations.

An append-only question-and-answer log was considered and rejected,
because it left the current state of what was wanted scattered across
the brief, the log and the assignment, with no single place answering
"what do I want now". The intent is that single place.

## What a position carries

A position (prefix `POS`) is a statement the principal currently
holds: what he holds and why it holds, in as many words as it takes to
be understood without loss of meaning. It names what it comes from, a
brief or a source, and it is dated once, with the day it took its
present shape. A position without an ID does not exist: it carries its
ID from birth.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that is written into the history in the same step that writes the
position, while the whole context is still at hand. Earlier steps of a
position are found by searching the history for its ID; the position
itself cites no record of the history. A number stays in a position
only where it is the rule or a threshold, never as a measurement.
Text leaves a position only into the history, word for word.

A position says what is to be achieved and why. What realises it is
named in the solution design where the project has one. Where a
project has no solution design, the position names the file, and
where the output is only part of a file or the file does not exist
yet, it keeps the full information, since another change may rewrite
that part and the detail would be lost. Where a position and what
realises it say different things, that is a finding, never mended in
silence.

## Why a fact has a prefix of its own

A fact (prefix `FCT`) is what is the case: stated by the principal on
his word, or by a source cited to its file. Verification is never
demanded. A position is what the principal holds or wants; making a
source's fact his own stance is a new position, not a change to the
fact.

Without a prefix of its own, a fact would have passed for a position.
What Claude has worked out is never a fact, since a fact is the
principal's word or a source's.

## Rejected directions

A rejected direction (prefix `REJ`) is what was considered and
dropped, with the reason. It is kept so that old ground is not
re-litigated and the reasoning is there for a later return to the
project. Deferred is not dropped: an idea placed later on the horizon
stays a position, with a word saying where the principal sees it,
whether a proof of concept, the first version, later, or good but far
away.

## Threads, in a file beside the intent

The open threads (prefix `THR`) live in `threads.md`, one file for
the project, beside the intent. The intent says what holds, the
threads what is being worked. A thread says what is open and where it
came from, and carries the working debate for as long as it is
unsettled: what was said, what was tried, the plan of a change under
way, the proposals that await a decision. It is where an unfinished
conversation is saved before a session ends.

Every thread names, right after its ID and in square brackets, the
artefact it concerns, as `/forge` names it, several where it concerns
several. That is how a thread is found from the artefact it blocks:
the intent is complete for now when no thread blocks the next layer,
and a thread that names its artefact says which layer it stands in
front of.

A thread also carries its origin: the principal's word, which is the
default and needs no mark, a document by path, or Claude's synthesis.
The reason is that a hypothesis of Claude's stays visibly his until
the principal takes it up.

The threads file is part of the intent as its history is: freely
rewritten, with no version, no history and no ledger row of its own.
A settled thread leaves the file and is kept whole: what holds goes
into the intent, and the record of its closing in the intent's
history carries the thread's last wording word for word. A thread
closes only on the principal's word.

## The staging area for the layer below

The template ends with an optional section, "Candidate structure for
the layer below". The recipients, the objective and the success
criteria are found in the intent as soon as the principal sees them,
as positions with IDs like everything else, so that the layer below
takes them over instead of finding them first. The section is left
out where the project takes no layer, and deleted once the layer
exists and leads.

## What the intent does not do: it does not solve

An intent says what the principal wants and why. What he wants, what
he does not want, what is the case, what is open and what he dropped
belong to it; how the things he wants are realised belongs to the
solution design.

The test of a sentence: would it still hold if the thing were realised
in a wholly different way? If it would, it is intent; if not, it is
solution. A principle the principal sets for the solution, what the
realisation must respect whatever its shape, is intent; the mechanism
that honours it is solution. What the principal wants the user to be
able to do, and what must be true when it is done, is intent, a
command he asks for by name among it; how the command does it, what
it is built of, its steps and the checks it runs, is solution. The
division is by kind of content, never by who said it: an idea of the
principal's about how to build something is solution too.

The reason is that an intent that carries the solution cannot be read
as what is wanted, and nobody can be asked for a proposal of the whole
solution over it.

## Complete for now, never finished

The intent is complete for now when no thread blocks the next layer.
Before a lower layer is derived, the whole is passed through a final
reality check: what of it is feasible, and where the wheel already
exists. It is never finished: many iterations are the normal mode,
and a change may come from below, when solving shows that what is
wanted must change, in which case the intent changes first.

## How the files are made

The first intent is created from `templates/intent.md` as version
0.1, with its history companion `10-intent.history.md` and the threads
file `threads.md` from `templates/threads.md`. The shape of the intent
is the template's: an Essence of a few sentences saying what the
principal wants and why as of today, then Positions, Facts, Rejected
directions, and the optional Candidate structure for the layer below.
The text is in the project's language, and the Mined column of every
brief touched is kept in the ledger on each write.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [About versioning and history](versioning-and-history.md): the
  history companion a position's past lives in.
- [About the solution design](the-solution-design.md): where the
  solution goes instead.
