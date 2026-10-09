---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md
  - CLAUDE.md
---

# About the brief

This page explains what a brief is in Forge of Thought, how it
behaves and why it is shaped the way it is. It is for anyone who uses
the forge and for anyone weighing whether it suits them. It was put
together from the brief's definition
(`.claude/skills/forge/states/brief.md`), its template
(`templates/brief.md`), the design positions and rejected directions
of the forge's own intent (`projects/forge/10-intent.md`) and the
language rule of `CLAUDE.md`.

## What a brief is

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from the finding around it.
The principal is whoever's thinking is being forged. Every chain of
documents starts at a brief, and the brief is what the intent is
later mined from.

The brief holds thoughts to be processed, not decisions. Nothing in
it is yet a position: its thoughts may be changed, reworked or
dropped when it is mined, and only the intent turns them into
positions. It is where thoughts are thrown in before they are
sifted; not all of them survive, and the sifting is the intent's.

## Free form, on purpose

A brief has a minimal header and nothing else fixed. The header
carries the project, a working title, the date, the author, the
version, the status and the last change. Below it the text is free:
prose, headings, tables, lists, use cases, whatever structure serves
the thought. It has no required content, no IDs and none of the
conventions of the chain.

No structure is required because a required one would force
premature tidiness, and none is forbidden. A templated brief with
fixed chapters (goal, high-level idea and so on) was considered and
rejected for that reason. A summary the principal orders into a brief
is stored as shown, never re-narrated.

At any time the principal may ask Claude to give the brief a
structure: the text gathered under headings in a logical order, what
repeats pointed out, the grammar mended. Nothing is added, dropped or
reworded, the structure is shown before it is written, and it is
never a condition of approval.

## Rough on purpose

A brief is neither perfect nor detailed. The chiselling is the
intent's work, and a brief polished until the intent has nothing
left to do has gone too far. Its usual shape is light: the topics of
the whole, each with a few sentences of what the principal wants of
it, the research that verifies or limits it cited beside it, and what
is still open. It is composed in a round or two and then mined.

A brief may carry a mechanism where the mechanism is part of the
idea. Once the talk turns to taking the idea apart and agreeing it
piece by piece (definitions, blocks, wording), that is the intent's
work. Claude says so in one sentence and offers once to go on in the
intent, as a recommendation and never a gate; the principal decides
whether the matter stays in the brief as one open line or is let go.
No walkthrough runs over the text of a brief.

## Not the record of the finding

Around a brief there is a finding: research, sources, the
principal's ideas and Claude's. The finding is wide and gathers as
many ideas as it can. The brief is not its record. What goes into the
brief and what stays out is the principal's decision, made on what
was found.

What stays out lives in `research/` or `sources/` where it is a
finding or a source, and otherwise nowhere. A second home for it was
considered and rejected: an early draft intent beside the draft
brief, a separate kind of notes record, or a new artefact before the
brief. The reason is that the brief holds the principal's choice, and
what he does not take needs no home; what merely came up in the
conversation is gone with it.

The definition names what the finding looks at, so that each area is
consciously considered before the brief is approved: the thought
itself and what prompted it, its boundaries, the world around it
(what already does the same or the opposite), the material it rests
on, and what is still open. An area may leave nothing in the brief,
and the brief has no required content.

## Whose it is, and the marks it carries

The brief is the principal's: what is in it he approved, whoever
first said it. Claude inspires, verifies, proposes research and
writes down what the talk arrived at so that it is understood, but
he does not decide what goes in and does not chisel the brief into
an intent.

For that reason nothing in a brief marks authorship. Marking every
block that was not the principal's own with the name of the model
was tried and dropped: authorship is settled by the principal's
approval, and a mark that names a model reads differently on every
model the forge runs on.

Two marks stay, because they carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact with
  provenance. What merely inspired the thought carries no mark and
  stays discoverable through the research note.
- `(remark: …)` is short and stands where a reservation or an
  uncertainty must stay visible. It is named by what it is, not by who
  made it, so that it reads the same whatever model the forge runs on.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

## Three origins

Three origins are equally legitimate, and the forge does not
distinguish between them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

## More than one brief

A project may have more than one brief. The founding brief is
`00-brief.md`. Every later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as
`00-brief-<name>.md`, with the same header, the same states and the
same rules.

The reason is that a big new whole needs a place where the thought
can be tempered before it enters the trunk, much as a git branch
does, without a new kind of document. An open thread was the wrong
place for it, because a thread is a question and not a body of work;
a working document with positions before a merge was judged too
heavy for now.

A brief is mined into the single intent when the principal says so,
approved or not. Positions mined from it cite the brief and its
version as provenance, and drift is measured against that version.
The ledger's Briefs table carries one row per brief and records how
far each is mined, as a judgement in its note and in the provenance
of the positions, never as a metric. A whole that dies on the way
leaves the brief as it stands and one rejected direction in the
intent with the reason, so the trace survives either way.

## Versioned, never locked

A brief is versioned like every artefact: a draft until the
principal approves it, then 1.0, and changed after that as any
artefact is. Its history lives in a companion file beside it. It is
approved only on the principal's explicit word, when he says it is
complete. It is not locked and not immutable: what it said at any
version stands in its history and in git.

## Language

The artefacts of the chain are written in the project's language,
but the briefs are the one exception: a brief is kept in whatever
language it is written in.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [About the intent](the-intent.md): where the brief is mined.
