---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/forge/states/intent.md
  - templates/intent.md
  - templates/threads.md
  - projects/forge/10-intent.md
---

# About the intent

This page explains what the intent of a project is, what it holds and
why it is shaped the way it is. It is for someone who uses the forge
and for someone weighing whether it suits them. It was put together
from the intent's definition (`.claude/skills/forge/states/intent.md`),
the templates `templates/intent.md` and `templates/threads.md`, and the
forge's own intent (`projects/forge/10-intent.md`), whose positions
give the reasons.

## A working document, not a log

The intent, `10-intent.md`, is the working document of a project: the
consolidated current state of what the principal holds. It is
rewritten for coherence every round and never appended to; what
changed in a round is recorded in its history beside it, not in the
body.

The reason is that chat context dies and anything of value must live
in a file. The intent is the document to read when returning to a
project after weeks, instead of digging through old conversations.

An earlier design kept the answers as an append-only question and
answer log. It was rejected because it left the current state of the
intent scattered across the brief, the log and the assignment, with no
single place answering "what do I want now". The intent replaced it.

## What it is for

The intent chisels the briefs into what the principal holds. From the
briefs, the sources and the conversation it keeps:

- what matters, as **positions** (prefix POS);
- what is the case, as **facts** (prefix FCT);
- what was dropped, as **rejected directions** with the reason
  (prefix REJ);
- what is undecided, as **threads** (prefix THR), kept in
  `threads.md` beside it.

Ideas are placed on a horizon where the principal sees one: a proof
of concept, the first version, a later one, or good but far away.
Everything is coherent, nothing is said twice, every position has its
provenance, and the whole passes a final reality check before a lower
layer is derived from it.

The template gives the document an Essence (what the principal wants
and why, as of today), then Positions, Facts and Rejected directions,
and an optional staging area for what the layer below will need, such
as the recipients, the objective and the success criteria, once the
principal sees them.

## What a position carries, and what goes into the history

A position says what the principal holds and why, in as many words as
it takes to be understood without loss of meaning, and names what it
comes from: a brief or a source. It carries its ID from birth and is
dated once, on the day it took its present shape.

What does not belong in a position is the way to it: why it was
changed, what was said on the way, trials, measurements, counts,
settled findings, what others do, which research turned it. All of
that is written into the history in the same step that writes the
position, while the whole context is at hand. Earlier steps of a
position are found by searching the history for its ID; the position
itself cites no record of the history. A number stays in a position
only where it is the rule or a threshold, never as a measurement.
Text leaves a position only into the history, word for word.

So the body reads as the current state, and nothing of how it was
reached is lost.

## Why a fact has a prefix of its own

A fact is what is the case: stated by the principal on his word, or
by a source cited to its file. Verification is never demanded. A
position, by contrast, is what the principal holds or wants. Without a
prefix of its own, a fact would pass for a position. When the
principal makes a source's fact his own stance, that is a new
position.

What Claude has worked out is never a fact, since a fact is the
principal's word or a source's.

## Threads, and why each names its artefact

The threads live in `threads.md`, one file for the project. The
intent says what holds; the threads say what is being worked. A
thread says what is open and where it came from, and carries the
working debate for as long as it is unsettled: what was said, what was
tried, the plan of a change under way, the proposals awaiting a
decision. It is where an unfinished conversation is saved before a
session ends.

A thread carries its origin: the principal's word (the default,
unmarked), a document by path, or Claude's synthesis. This keeps a
hypothesis of Claude's visibly his until the principal takes it up.

Every thread names, right after its ID and in square brackets, the
artefact it concerns, as `/forge` names it, or several where it
concerns several. One file holds the threads of every artefact of the
project, and the name is what tells which artefact an open matter
belongs to.

The threads file is part of the intent as its history is: freely
rewritten, with no version, no history of its own and no row in the
ledger. The intent's history records the birth and the closing of a
thread, not every saving of its debate. A settled thread leaves the
file and is kept whole: what holds goes into the intent, and the
record of its closing carries the thread's last wording word for
word. A thread closes only on the principal's word.

## An intent does not solve

An intent says what the principal wants and why. What he wants, what
he does not want, what is the case, what is open and what he dropped
belong to it; how the things he wants are realised belongs to the
solution design.

The test of a sentence: would it still hold if the thing were realised
in a wholly different way? If it would, it is intent; if not, it is
solution. A principle the principal sets for the solution, which the
realisation must respect whatever its shape, is intent; the mechanism
that honours it is solution. What he wants the user to be able to do,
and what must be true when it is done, is intent, including a command
he asks for by name; how the command does it, what it is built of, its
steps and the checks it runs, is solution. The division is by kind of
content, never by who said it: an idea of the principal's about how to
build something is solution too.

The reason: an intent that carries the solution cannot be read as what
is wanted, and nobody can be asked for a proposal of the whole
solution over it.

An item says what is to be achieved and why. What realises it is named
in the solution design where the project has one, and in the item
where it has none.

## Complete for now, never finished

The intent is complete for now when no thread blocks the next layer.
It is never finished. At that point Claude names the layers that can
follow from it, or offers the approval where the principal takes no
further layer: a recommendation, never a gate.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating it.
- [About versioning and history](versioning-and-history.md): the history companion a position's past lives in.
- [About the solution design](the-solution-design.md): where the solution goes instead.
