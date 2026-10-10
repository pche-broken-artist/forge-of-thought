---
generated: 2026-10-10
made: derived
inputs-hash: a1942f5623705b52
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - projects/forge/10-intent.md
---

# About the intent

This page explains what the intent is, what it holds and why it is
built the way it is. It is for the person who runs a project through
the forge and for anyone evaluating what the forge produces. It was
put together from the intent's definition
(`.claude/skills/forge/states/intent.md`), its template
(`templates/intent.md`), the template of the threads file
(`templates/threads.md`) and the design positions of the forge's
own intent (`projects/forge/10-intent.md`); the reasons given here
are the ones those files give.

## What the intent is

The intent, `10-intent.md`, is the working document of a project:
the consolidated current state of what the principal holds. It is
not an append-only log. Every round rewrites it for coherence, and
what changed is recorded in its history companion beside it, never
in the body.

The reason is simple: chat context dies, and anything of value must
live in a file. The intent is the document to read when returning
to a project after weeks, instead of excavating old conversations.
An earlier design, an append-only log of questions and answers, was
dropped because it left the current state scattered across the
brief, the log and the assignment, with no single place answering
"what do I want now". The intent is that place.

The intent chisels the briefs into what the principal holds. From
the briefs, the sources and the conversation it keeps what matters
as positions, what is the case as facts, what is undecided as
threads and what was dropped as rejections, each with its reason.
Ideas are placed on a horizon where the principal sees one: a proof
of concept, the first version, a later one, or good but far away.
Everything is coherent, nothing is said twice, every position has
its provenance, and the whole passes through a reality check before
a lower layer is derived from it.

## What it holds

The intent has four kinds of item, each with a prefix of its own,
and an essence in prose at the top: three to ten sentences of what
the principal wants and why, as of today.

### Positions

A position (prefix POS) is what the principal currently holds or
wants. It says what he holds and why it holds, in as many words as
it takes to be understood without loss of meaning, and it names
what it comes from: a brief or a source. It is dated once, with the
day it took its present shape.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
findings settled, what others do, which research turned it. All of
that goes into the history in the same step that writes the
position, while the whole context is still at hand. Earlier steps
are found by searching the history for the position's ID; the
position itself cites no record of the history. A number stays in a
position only where it is the rule or a threshold, never as a
measurement. Text leaves a position only into the history, word for
word. A position without an ID does not exist: it carries its ID
from birth, and the history records it by that ID.

A position says what is to be achieved and why. What realises it is
named in the solution design where the project has one. Where the
project has no solution design, the position names the file that
realises it; and where the output is only part of a file, or the
file does not exist yet, the position keeps the full information,
since another change may rewrite that part and the detail would be
lost. Where a position and what realises it say different things,
that is a finding, never mended in silence.

### Facts

A fact (prefix FCT) is what is the case: stated by the principal on
his word, or by a source cited to its file. Verification is never
demanded. A fact is not a stance. Making a source's fact the
principal's own stance is a new position.

Facts have a prefix of their own because without one a fact would
have passed for a position. What the forge's assistant has worked
out is never a fact, since a fact is the principal's word or a
source's.

### Rejected directions

A rejected direction (prefix REJ) is what was considered and
dropped, with the reason. It prevents re-litigating old ground and
preserves the reasoning for a future return to the project. What
was deferred to a later horizon is not a rejection: deferred is
still wanted, only not now.

### Threads

The open threads of a project live in a file of their own beside
the intent, `threads.md`, one file per project. The intent says
what holds; the threads say what is being worked. A thread (prefix
THR) says what is open and where it came from, and carries the
working debate for as long as it is unsettled: what was said, what
was tried, the plan of a change under way, the proposals that await
a decision. It is where an unfinished conversation is saved before
a session ends.

Every thread names, right after its ID and in square brackets, the
artefact it concerns, as `/forge` names it; several where it
concerns several. A thread also carries its origin: the principal's
word, which is the default and needs no mark; a document by path;
or the assistant's synthesis. The origin is marked so that a
hypothesis of the assistant's stays visibly his until the principal
takes it up.

A thread closes only on the principal's word. A settled thread
leaves the file and is kept whole: what holds goes into the intent
as a position or a rejection, and the record of its closing in the
intent's history carries the thread's last wording word for word.
The threads file is part of the intent as the history is: freely
rewritten, with no version, no history and no ledger row of its
own. The intent's history records the birth and the closing of a
thread, not every saving of its debate.

### The staging area for the layer below

The template ends with an optional section, "Candidate structure
for the layer below". It holds what the layer below will need as
soon as the principal sees it: the recipients, the objective and
the success criteria where that layer is an assignment, written as
positions with IDs like everything else. The layer then takes them
over instead of finding them first. The section is left out where
the project takes no layer, and deleted once the layer exists and
leads.

## What the intent does not do: solve

An intent says what the principal wants and why, and it does not
solve. What he wants, what he does not want, what is the case, what
is open and what he dropped belong to it; how the things he wants
are realised belongs to the solution design.

The test of a sentence: would it still hold if the thing were
realised in a wholly different way? If it would, it is intent; if
not, it is solution. A principle the principal sets for the
solution, something the realisation must respect whatever its
shape, is intent; the mechanism that honours it is solution. What
the principal wants the user to be able to do, and what must be
true when it is done, is intent, a command he asks for by name
among it. How the command does it, what it is built of, its steps
and their order and the checks it runs, is solution. The division
is by kind of content, never by who said it: the principal's own
idea about how to build something is solution too.

The reason: an intent that carries the solution cannot be read as
what is wanted, and nobody can be asked for a proposal of the whole
solution over it.

## When it is complete

The intent is complete for now when no thread blocks the next
layer. It is never finished. At the end of a round the forge names
what changed and what stays open; when the intent is complete for
now, it names the layers that can follow from it, or offers the
approval where the principal takes none. That is a recommendation,
never a gate.

## How the files are made

The first intent is created from `templates/intent.md` as version
0.1, with its history companion `10-intent.history.md` from
`templates/history.md` and the threads file `threads.md` from
`templates/threads.md`. The text is in the project's language. The
assistant composes the wording, the principal the substance.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [About versioning and history](versioning-and-history.md): the
  history companion a position's past lives in.
- [About the solution design](the-solution-design.md): where the
  solution goes instead.
