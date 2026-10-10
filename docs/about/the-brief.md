---
generated: 2026-10-10
made: derived
inputs-hash: e50a39c7b04b29c4
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md
---

# About the brief

This page explains what a brief is in the forge, why it has the shape
it has and what is deliberately kept out of it. It is for the user who
is about to write one and for the evaluator who wants to know what a
brief is and is not. It was put together from the brief's definition
(`.claude/skills/forge/states/brief.md`), the brief's skeleton
(`templates/brief.md`) and the positions and rejected directions of
the forge's own intent (`projects/forge/10-intent.md`); the language
rule comes from `CLAUDE.md`, prime directive 6.

## What a brief is

A brief is the principal's text of one whole of thinking: what he
wants and why, together with what he chose to take from the finding
around it. The finding is wide: research notes, sources, his own ideas
and Claude's. The brief is not its record. What goes in and what stays
out is the principal's decision, made on what was found.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position: its thoughts may be changed, reworked or dropped
when the brief is mined, and only the intent turns them into
positions. It is where thoughts are thrown in before they are sifted;
not all of them survive, and the sifting is the intent's.

A brief says what the idea is and why. It may carry a mechanism where
the mechanism is part of the idea. Once the talk turns to taking the
idea apart and agreeing it piece by piece (definitions, blocks,
wording), that is the intent's work, and the brief is left as it is.

## Why it is free form

Below its header a brief is free form: any structure the principal
finds useful (prose, headings, tables, use cases), no required
content, no IDs and none of the conventions of the chain. No
structure is required because a required one would force premature
tidiness, and none is forbidden. A templated brief with fixed chapters
(goal, high-level idea and so on) was considered and rejected for this
reason. A summary the principal orders into a brief is stored as
shown, never re-narrated.

The only fixed part is a minimal YAML header, which carries the
project, a working title, the date, the author, the version, the
status and the last change. It is the same kind of header every
artefact carries, because a brief is versioned like every artefact.

## Why it is rough

A brief is rough on purpose, neither perfect nor detailed. The
chiselling is the intent's: a brief polished until the intent has
nothing left to do has gone too far. Its usual shape is light: the
topics of the whole, each with a few sentences of what the principal
wants of it, the research that verifies or limits it cited beside it,
and what is still open. It is composed in a round or two and then
mined.

A tension, an alternative left undecided or a boundary left vague may
stay in the brief as it is, since resolving them is the intent's work.
Before the brief is approved, the areas the finding looks at are
walked once, to ask whether each has been consciously considered: the
thought and what prompted it; the boundaries; the world around it
(what exists that does the same or the opposite); the material the
thought rests on; and what is still open. An area may leave nothing in
the brief. The walk asks and does not mend.

## What stays out, and where it goes

The brief is not the record of the finding. What the principal does
not take needs no home of its own: a finding lives in `research/` and
a source in `sources/`, where the intent can cite them; what merely
fell by in the conversation is gone with it. A second home for what
the finding yields and the brief does not take (an early intent draft
beside the brief, a "notes" record, a new artefact before the brief)
was considered and rejected: the brief holds the principal's choice,
and the rest is either a finding, a source or nothing.

## Marks in a brief

Nothing in a brief marks authorship: what is in it the principal
approved, whoever first said it. A mark such as an italic model name
before every block that was not the principal's own was tried and
dropped, because a mark that names a model reads differently on every
model the forge runs on.

Two marks stay, because they carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact with
  provenance. What merely inspired the thought carries no mark and
  stays discoverable through the research note.
- `(remark: …)` stands where a reservation or an uncertainty must stay
  visible, named by what it is and not by who made it, so that it
  reads the same whatever model the forge runs on.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

## Where a brief comes from

Three origins are equally legitimate, and the forge does not
distinguish them: the brief arrives finished from outside and is
stored as it came; it is begun outside and finished with Claude in the
forge; or it is born in the forge from the first word. In every case
the brief is the principal's. Claude may translate, mend the grammar
and word an idea of his own that the principal has accepted, but he
does not decide what goes in and does not chisel the brief into an
intent.

## More than one brief

A project may have more than one brief. The founding brief is
`00-brief.md`. Every later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as
`00-brief-<name>.md`, with the same header, the same states and the
same rules. The reason is that a big new whole needs a place where
the thought can be tempered before it enters the trunk, much like a
branch, without inventing a new document kind. A thread was judged
wrong for it, because a thread is a question, not a body of work.

A brief is mined into the single intent when the principal says so,
approved or not. The positions mined from it cite the brief and its
version as their provenance, and drift is measured against that
version. A whole that dies on the way leaves the brief as it stands
and one rejected direction in the intent with the reason, so the trace
survives either way. The ledger carries one row per brief and notes
how far each is mined; how much is a judgement, never a metric.

## Versioning and status

A brief is versioned like every artefact: a draft until the principal
approves it, 1.0 on his explicit word, and changed after that as any
artefact is. It is complete when the principal says so. It is neither
locked nor immutable: what it said at any version stands in its
history and in git, and an approved brief can still be changed; a new
whole is a new brief.

## Language

Among the artefacts of the chain the brief is the one exception to the
rule that artefacts are written in the project's language: a brief is
kept in whatever language it is written in.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [About the intent](the-intent.md): where the brief is mined.
