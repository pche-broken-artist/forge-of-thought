---
generated: 2026-10-09
made: derived
inputs-hash: 3c16b1d4cd131aa1
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md
---

# About the brief

This page explains what a brief is in Forge of Thought, how it is
shaped and why it is shaped that way. It is for a person who is
about to write one, or who wants to judge whether the forge's idea
of a brief holds. It was put together from the brief's definition
(`.claude/skills/forge/states/brief.md`), its template
(`templates/brief.md`) and the positions and rejected directions of
the forge's own intent (`projects/forge/10-intent.md`), with the
reasons those files give. How a brief is composed, step by step, is
the page [Write a brief](../use/write-a-brief.md).

## What a brief is

A brief is the principal's text of one whole of thinking: what he
wants and why, together with what he chose to take from the finding
around it. The finding is wide: research notes, sources, the
principal's own ideas and the ones Claude brought while the idea
was being explored. The brief is the principal's selection from all
of that, made on what was found.

A brief holds thoughts to be processed, not decisions. Nothing in
it is yet a position: its thoughts may be changed, reworked or
dropped when they are mined, and only the intent turns them into
positions. It is where thoughts are thrown in before they are
sifted; not all of them survive, and the sifting belongs to the
intent.

Every project starts at a brief: `00-brief.md` is the founding
brief, and the intent is mined from it.

## Free form, no required content

The brief is free form. Any structure the principal finds useful
is allowed: prose, headings, tables, lists, use cases. There is no
required content, no IDs and none of the conventions of the chain.
Only a minimal YAML header is fixed: project, working title, date,
author, version, status and last change, as `templates/brief.md`
gives it; everything below the header is the principal's own text.

The reason is that a required structure would force premature
tidiness. A templated brief with chapters such as goal and
high-level idea was considered and rejected for exactly that: no
structure is required, and none is forbidden. A summary the
principal orders into a brief is stored as shown, never re-told in
Claude's words.

The usual shape is light: the topics of the whole, each with a few
sentences of what the principal wants of it, the research that
verifies or limits it cited beside it, and what is still open. It
is composed in a round or two and then mined.

## Rough on purpose

A brief is rough on purpose, neither perfect nor detailed. The
chiselling, the taking apart and agreeing piece by piece, is the
intent's work. A brief polished until the intent has nothing left
to do has gone too far.

This is why Claude holds the form. A brief says what the idea is
and why, and may carry a mechanism where the mechanism is part of
the idea. Once the talk turns to definitions, blocks and wording,
Claude says in one sentence that this is the intent's work, does
not develop it, and offers once to go on in the intent. That is a
recommendation, not a gate: the principal decides whether the point
stays in the brief as one open line or is let go. No walkthrough
runs over the text of a brief, and no IDs enter it. A tension, an
alternative left undecided or a boundary left vague may stay in the
brief as it is, since resolving them is the intent's work.

## Not the record of the finding

The brief is not the record of everything that was found. What
goes in and what stays out is the principal's decision. What stays
out has only two homes: `research/` where it is a finding, and
`sources/` where it is a source. Everything else is nowhere.

A second home for what the finding yields and the brief does not
take was considered, as a draft intent beside the draft brief or as
a kind of notes record, and rejected: the brief holds the
principal's choice, a finding or a source already has its
directory, and what merely fell by in the conversation is gone
with it.

## No marks of authorship

Nothing in a brief marks authorship. What is in it the principal
approved, whoever first said it. Claude may translate, mend the
grammar and word an idea of his own that the principal has
accepted; once accepted, it is the principal's text. A mark such as
an italic model name before every block that was not the
principal's own was tried and dropped, because a mark that names a
model reads differently on every model the forge runs on.

Two marks stay, because they carry something other than
authorship:

- `(source: <path>)` stands where the identity of a source
  supports, limits or contradicts the thought. At mining it becomes
  a fact with provenance. What merely inspired the thought carries
  no mark and stays discoverable through the research note.
- `(remark: …)` stands, short, where a reservation or an
  uncertainty must stay visible. It is named by what it is, not by
  who made it, so that it reads the same whatever model the forge
  runs on.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

## Three origins, equally legitimate

A brief may arrive in three ways, and the forge does not
distinguish them:

- it arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

`/forge brief` is the door for the latter two. In all three the
brief is the principal's: Claude inspires, verifies, proposes
research and draws out what the principal wants, why and what he
does not want, but he does not decide what goes in and does not
chisel the brief into an intent.

## More than one brief

A project may have more than one brief. The founding one is
`00-brief.md`; every later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as
`00-brief-<name>.md`, with the same header, the same states and
the same rules. The reason is that a big new whole needs a place
where the thought can be tempered before it enters the trunk,
somewhat like a branch in git, without a new document kind. A
thread was judged wrong for it, because a thread is a question and
not a body of work.

Each brief is mined into the single intent when the principal says
so, approved or not. Positions cite the brief and its version as
their provenance, and drift is measured against that version. A
whole that dies on the way leaves the brief as it stands and one
rejected direction in the intent with the reason, so the trace
survives either way. The ledger's Briefs table carries one row per
brief and says how far each is mined; how much is a judgement
recorded in its note, never a metric. Where the brief is mined and
what becomes of its thoughts is the page
[About the intent](the-intent.md).

## Versioned, approved, never locked

A brief is versioned like every artefact: a draft until the
principal approves it, then 1.0, and changed after that as any
artefact is, with its history kept in the companion beside it. The
brief is complete when the principal says so and approves it; the
areas of the finding are walked once before the approval is
offered, asking whether each was consciously considered, and an
area may leave nothing in the brief.

A brief is not locked and not immutable: what it said at any
version stands in its history and in git. An approved brief is
changed like any artefact, and a new whole is a new brief.

## Language

The briefs are the one exception to the rule that the artefacts of
the chain are written in the project's language: a brief is kept
in whatever language it is written in.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [About the intent](the-intent.md): where the brief is mined.
