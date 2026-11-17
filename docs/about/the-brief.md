---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 5d6e5a6da4fe8006
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0920
  - projects/forge/10-intent.md#REJ.0040
  - projects/forge/10-intent.md#REJ.0180
  - projects/forge/10-intent.md#REJ.0220
  - CLAUDE.md#Prime directives
---

# The brief

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from what was found around
the idea. The principal is the person whose thinking is forged. This
page explains what a brief is and why it is rough on purpose. It is
written for someone who uses the forge and for someone who weighs
it.

## What it is

A brief is an artefact (see [Glossary](../reference/glossary.md))
that puts an idea together. It is free-form. Any structure the
principal finds useful is allowed, such as headings or tables. The
text has no required content. It carries no IDs and follows none of
the conventions of the chain. Only a minimal header is fixed.

A brief holds thoughts to be processed, not decisions. A brief is
mined: its thoughts are worked into the intent (see
[The intent](the-intent.md)). Only the intent turns them into
positions, that is into decided items (see
[Glossary](../reference/glossary.md)). Nothing in a brief is yet a
position. A thought may be changed, reworked or dropped when it is
mined.

A brief is rough on purpose: neither perfect nor detailed. Its usual
shape is light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it
- the research that verifies or limits a topic, cited beside it
- what is still open

It is composed in a round or two and then mined.

A brief is not the record of what was found on the way to it. The
search around an idea is wide and gathers as many ideas as it can.
What goes into the brief and what stays out is the principal's
decision, made on what was found.

A project may have more than one brief. The founding brief is the
file `00-brief.md`. A later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as a
brief of its own (`00-brief-<name>.md`). It has the same header, the
same states and the same rules. A project has a single intent,
however many briefs it has.

## Who writes and reads it

The brief belongs to the principal. What is in it he approved,
whoever first said it.

Claude's part changes on the way. At the opening Claude is the
active one:

- it inspires
- it brings how the same thing is done elsewhere and how original
  the idea is
- it verifies what can be verified
- it proposes research and the intake of outside material

A proposal Claude makes, however large, serves the search and is not
the brief. Then the brief is written. Claude moves the principal to
say what he wants and why, and what he does not want. On the
principal's word it writes down what the talk arrived at, in words
that are understood. In the writing Claude may:

- translate
- mend the grammar
- word an idea of its own that the principal has accepted

What Claude has formulated it shows the principal before it is
written. Claude does not take the brief over. It does not decide
what goes in, and it does not work the brief into an intent.

A brief is read when it is mined. It is mined into the single intent
when the principal says so, approved or not. The command is
`/forge intent`. A position mined from a brief cites the brief as
its provenance. The version the brief was mined at is said by the
record of the mining, and drift is measured against that version.

The ledger shows how far each brief is mined. The ledger is the file
that shows what stands in a project (see
[Glossary](../reference/glossary.md)). Its Briefs table has one row
per brief. It reads the record of the mining, which stands in the
history of the intent. A history is the companion file
(`<file>.history.md`) beside a versioned document. The shape of the
mining record is on the page
[History companion](../reference/history-companion.md). How much of
a brief is mined is a judgement, recorded in the record of the
mining and in the provenance of the positions. It is never a metric.

A whole of thinking may die on the way. The brief then stays as it
stands, and the intent carries one rejected direction with the
reason. The trace survives either way.

## Made from

A brief is made from the principal's thought, however it arrives.
Around the thought, material is gathered while the brief is
composed:

- research notes, in `research/`
- sources, in `sources/`
- Claude's own proposals

The existing intent and the ledger are read only to know what
already stands. They never shape the text.

The file is made from the template `templates/brief.md`, which is
the minimal header and nothing else. A history companion
(`<file>.history.md`) is made with it.

## What it holds

The header is the only fixed part of the file. The template gives
it:

```yaml
---
project: <slug>
title: <working title>
author: <principal>
version: 0.1
status: draft
---
```

Below the header the text is free. A brief says what the idea is and
why. It may carry a mechanism where the mechanism is part of the
idea.

Nothing in a brief marks authorship. Two marks may stand in the
text, and they carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact
  with provenance.
- `(remark: …)` is short and stands where a reservation or an
  uncertainty must stay visible. It is named by what it is and not
  by who made it.

What merely inspired a thought carries no mark. It stays
discoverable through the research note. A suggestion or an
alternative the principal did not take is gone. It stays only where
he says so.

What stays out of the brief lives in `research/` where it is a
research note and in `sources/` where it is a source. Otherwise it
lives nowhere.

A summary the principal orders into a brief is stored as shown,
never re-narrated.

A brief is kept in the language it is written in. It is the one
exception among the artefacts. The other artefacts are written in
the language of the project, which its project file names (see
[Languages](languages.md)).

## Complete when

A brief is complete when the principal says so and approves it. It
is approved on his word alone.

A brief is versioned like every artefact. It is a draft until the
principal approves it, and the approved version is `1.0`. After that
it is changed as any artefact is. A brief is not locked and not
immutable. What it said at any version stands in its history and in
git.

Before the approval is offered, the Map of the brief's definition is
walked once. The definition is the file that says what a brief is
and how it is found (`.claude/skills/forge/states/brief.md`). Its
Map names what the search around the idea looks at. It does not say
what the brief must contain, and it prescribes no headings. The
areas are:

- the thought: what the principal wants, why, and what prompted it
- the boundaries: what the principal does not want, and what is out
  of scope
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or proof
  that the thing already exists
- the material: the sources and the research the thought rests on,
  gathered and registered, for the intent to cite
- what is still open: what was not decided or verified

The walk asks of each area whether it has been consciously
considered. An area may leave nothing in the brief. The walk asks
and does not mend. What is unresolved may stay in the brief as it
is, such as a tension or a boundary left vague. Resolving it is the
work of the intent.

Mining does not wait for the approval.

## How it is found

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came
- it is begun outside and finished with Claude in the forge
- it is born in the forge from the first word

The command `/forge brief [name]` serves the latter two. Composing a
brief is described on the page
[Write a brief](../use/write-a-brief.md).

Two commands serve the search around the idea:

- `/research <topic>`: what a research found is stored as a note in
  `research/` and indexed
- `/ingest [file]`: outside material is registered in `sources/` and
  indexed

Claude proposes each of them, and each runs on the principal's word.
Claude proposes a research step against a named need, such as an
uncertainty or a comparison. After the step Claude says what it
changed in the thought and what stays uncertain. The principal says
whether to go on. What the research did not find, or found not to
hold, stands in the research note like any other result. It enters
the brief where the principal takes it.

Claude holds the form of the brief. The talk may turn to taking the
idea apart and agreeing it piece by piece. Claude then says in one
sentence that this is the work of the intent and does not develop
it. It offers once to go on in the intent. The offer is a
recommendation, never a gate. The principal decides whether the
matter stays in the brief as one open line or is let go.

## Why

**Free form.** No structure is required. A required structure would
force premature tidiness. No structure is forbidden either. A
templated brief with chapters, such as a goal and a high-level idea,
was rejected on the same ground.

**Rough on purpose.** The exact working of a thought is left to the
intent: the chiselling, in the image the forge uses. A brief
polished until the intent has nothing left to do has gone too far. A
brief is where thoughts are thrown in before they are chosen among.
Not all of them survive, and the choosing belongs to the intent.

**Not the record of what was found.** The brief holds the
principal's choice. What he does not take needs no home of its own.
A research note has `research/` and a source has `sources/`. What
merely fell by in the conversation is gone with it. A second home
for what was found and not taken was rejected in each form proposed:

- a first draft of the intent beside a draft brief
- a record kind for notes
- a new artefact before the brief

**No mark of authorship.** What is in a brief the principal
approved, whoever first said it. A mark naming Claude before every
block that is not the principal's own was dropped. A mark that names
a model reads differently on every model the forge runs on. The two
marks that stay carry something other than authorship. A remark is
named by what it is and not by who made it. It therefore reads the
same whatever model the forge runs on.

**More than one brief.** A big new whole of thinking needs a place
where the thought can be worked on before it enters the intent, as a
branch does in git, without a new kind of document. A thread (see
[Glossary](../reference/glossary.md)) was wrong for it: a thread is
a question, not a body of work. A working space that holds positions
before they are merged into the intent was judged heavy for now.

**Not recorded.** Why a brief is kept in the language it is written
in: the reason is not recorded. Why the record of the mining stands
in the history of the intent: the reason is not recorded.

## A worked example

A brief of five lines. Its header stands above the text, as the
section What it holds shows.

```markdown
We want a new colleague to do real work within the first week.
Today it takes about a month, most of it spent waiting for access.
One checklist per role, kept by the receiving team (source: sources/onboarding-survey.md).
No new tool: what we have is enough (remark: not verified for contractors).
Still open: who keeps the checklists current.
```

What the lines are:

- lines 1 and 2: what the principal wants and why
- line 3: a thought, with the source that supports it
- line 4: a boundary, with a reservation kept visible
- line 5: what is still open

No line has an ID, and no line is a decision. When the brief is
mined, each thought may become a position, be reworked or be
dropped.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [History companion](../reference/history-companion.md): the shape
  of the mining record.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
