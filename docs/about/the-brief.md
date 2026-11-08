---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 32dafd9822d0e32f
inputs:
  - .claude/skills/forge/states/brief.md
  - templates/brief.md
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0920
  - projects/forge/10-intent.md#POS.1610
  - projects/forge/10-intent.md#REJ.0040
  - projects/forge/10-intent.md#REJ.0180
  - projects/forge/10-intent.md#REJ.0220
  - CLAUDE.md#Prime directives
---

# The brief

A brief is the text in which the principal (the person whose
thinking is being forged) puts one whole of thinking together: what
he wants, why, and what he chose to take from the finding around
it. This page says what a brief is, who writes it, what it holds,
when it is complete and why it is rough on purpose. It is for a user
who is about to write one and for an evaluator who wants to know
what the first document of a project is and is not. How to compose
one is a page of its own: [Write a brief](../use/write-a-brief.md).

## What it is

A brief is the first artefact of a project and the start of its
chain. Its file is `00-brief.md`. A later whole of thinking, born
during the project's life, is a brief of its own, `00-brief-<name>.md`,
with the same header, the same states and the same rules.

The brief is free form. Below a minimal YAML header the principal
uses any structure he finds useful: prose, headings, tables, lists,
use cases. It has no required content and no IDs. None of the
conventions of the chain apply to its text. A templated brief with
fixed chapters (goal, high-level idea and so on) was considered and
rejected. The reason is that a required structure would force
premature tidiness. No structure is forbidden either. A summary the
principal orders into a brief is stored as shown, never re-narrated.

The brief holds thoughts to be processed, not decisions. Nothing in
it is yet a position. Its thoughts may be changed, reworked or
dropped when the brief is mined, and only the intent turns them into
positions. Where the brief is mined is the page
[The intent](the-intent.md).

A brief is rough on purpose, neither perfect nor detailed. The
chiselling belongs to the intent. A brief polished until the intent
has nothing left to do has gone too far. Its usual shape is light:

- the topics of the whole;
- a few sentences per topic on what the principal wants of it;
- the research that verifies or limits it, cited beside it;
- what is still open.

It is composed in a round or two and then mined. It is the place
where thoughts are thrown in before they are sifted. Not all of them
survive, and the sifting belongs to the intent.

A brief is not the record of the finding. The finding is wide:
research, sources, the principal's ideas and Claude's. It gathers as
many ideas as it can. What goes into the brief and what stays out is
the principal's decision, made on what was found. What stays out
lives in `research/` where it is a finding and in `sources/` where it
is a source, and otherwise nowhere. A second home for what the brief
does not take (an early draft of the intent beside the brief, a
record kind for notes, an artefact before the brief) was considered
and rejected. The reason is that the brief holds the principal's
choice, and what he does not take needs no home: what merely fell by
in the conversation is gone with it.

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it. Claude (the cognitive extension of the principal that
runs the forge) takes a part that changes on the way. At the opening
Claude is the active one: it inspires, brings how the same thing is
done elsewhere and how original the idea is, verifies what can be
verified, and proposes research and ingest. A proposal of Claude's,
however large, serves the finding and is not the brief. Then the
brief is written. Claude moves the principal to say what he wants,
why and what he does not want, and forms the record: on the
principal's word to write, Claude takes what the talk arrived at and
writes it down so that it is understood. It may translate, mend the
grammar and word an idea of its own that the principal has accepted.
What it has formulated it reflects back before it is written. What
Claude does not do is take the brief over: it does not decide what
goes in, and it does not chisel the brief into an intent.

Claude holds the form. A brief says what the idea is and why. It may
carry a mechanism where the mechanism is part of the idea. Once the
talk turns to taking the idea apart and agreeing it piece by piece
(definitions, blocks, wording), Claude says in one sentence that this
is the intent's work, does not develop it, and offers once to go on
in the intent. That offer is a recommendation, never a gate. The
principal decides whether the matter stays in the brief as one open
line or is let go. No walkthrough (the forge's way of working a list
of decisions one item per message) runs over the text of a brief.

What Claude thinks of the brief it says when asked. What does not
fit it says at once and unasked, in one sentence: a wrong
assumption, a contradiction, a risk. What goes into the brief and
what stays out is the principal's to say.

The brief is read by whoever mines it into the intent, and by the
ledger (the project's state report, made at read time), which reads
its header and the record of its mining.

### What marks nothing, and what marks something else

Nothing in a brief marks authorship. A mark such as an italic
*(Claude)* before every block that is not the principal's own was
tried and dropped. The reason is that a mark naming a model reads
differently on every model the forge runs on, and that what is in
the brief the principal approved anyway.

Two marks stay, because they carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact
  with provenance. What merely inspired the thought carries no mark
  and stays discoverable through the research note.
- `(remark: …)` stands, short, where a reservation or an uncertainty
  must stay visible. It is named by what it is and not by who made
  it, so that it reads the same whatever model the forge runs on.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

## Made from

The principal's thought, however it arrives. Around it, gathered
during the finding: research notes in `research/`, sources in
`sources/`, and Claude's own proposals. The existing intent and the
ledger are read only to know what already stands, never to shape the
text.

The file itself is created from the template `templates/brief.md`,
which holds the minimal YAML header and nothing else. Its history
companion `<file>.history.md` is created beside it from
`templates/history.md`.

## What it holds

The header carries `project`, `title`, `author`, `version` and
`status`. Only the header is fixed. Everything below it is the
principal's text in the form he chooses, as the section "What it is"
says.

The brief is kept in the language it is written in. Among the
artefacts of the chain, which otherwise follow the project's
language, the briefs (`00-brief*.md`) are the one exception. The
reason for the exception is not recorded. What the languages of a
project are and how they are set is the page
[Languages](languages.md).

## Complete when

The brief is complete when the principal says so and approves it. The
approval is his word, never a condition the forge imposes. Before the
approval is offered, the Map of the finding is walked once (see "How
it is found").

A brief is versioned like every artefact: a draft until the
principal approves it, `1.0` on approval, and changed after that as
any artefact is. It is not locked and not immutable. What it said at
any version stands in its history companion and in git.

Approval is not a condition of mining. A brief is mined into the
single intent when the principal says so, approved or not. A project
may have more than one brief, and each is mined under the same rules.
How far each brief is mined is recorded as a record in the intent's
history, with the brief's file as its subject. The record stands in
the intent's history and not in the brief's, because the mining
changes the intent and not the brief. Its version column says which
version of the intent mined it. The ledger's Briefs table shows one
row per brief and reads that record; until one exists the mining is
pending. "How much" was mined is a judgement recorded in the mining
record and in the provenance of the positions, never a metric.

A brief is the provenance of its whole. A position mined from it
cites it, with the version the mining record names, and drift is
measured against that version. A whole that dies on the way leaves
the brief as it stands and one rejected direction in the intent with
the reason, so that the trace survives either way.

## How it is found

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

`/forge brief [name]` is the door for the latter two. At any time the
principal may have Claude give the brief a structure: the text
gathered under headings in a logical order, what repeats pointed out,
the grammar mended. Claude adds nothing, drops nothing and rewords no
thought. It shows the structure before it is written, and the
headings are the principal's to rename. The step is the principal's
to ask for, never a condition of the approval.

Two instruments serve the finding. `/research <topic>` puts durable
findings into `research/`, indexed. `/ingest [file]` puts outside
material into `sources/`, registered and indexed. Both are proposed
by Claude and run on the principal's word. Claude proposes a research
step against a named need: an uncertainty, a comparison, an
inspiration. After it Claude says what it changed in the thought,
what stays uncertain and whether more research is likely to change
anything. Whether to go on is the principal's to say. What the
research did not find, or found not to hold, is a finding like any
other and stands in the research note. It enters the brief where the
principal takes it.

The definition of the brief carries a Map. The Map is of the
finding, not of the brief: it names what the finding looks at, and
what of it enters the brief is the principal's choice. It prescribes
neither headings nor the order of the conversation. It is walked
once, at the closing, before the approval is offered, with one
question: has each area been consciously considered? An area may
leave nothing in the brief. The walk asks and does not mend. A
tension, an alternative left undecided or a boundary left vague may
stay in the brief as it is, since resolving them is the intent's
work. The areas are:

- the thought: what the principal wants, why, and what prompted it;
- the boundaries: what the principal does not want, and what is out
  of scope;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or proof
  that the wheel exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  finding.

## Why

The brief is free form because a required structure would force
premature tidiness. The brief is rough because the chiselling, the
sifting and the turning of thoughts into positions belong to the
intent; a brief that does that work itself leaves the intent nothing
to do.

The brief is not the record of the finding because it holds the
principal's choice. A finding or a source has a home in `research/`
or `sources/`. Anything else the principal did not take needs none.

Nothing marks authorship because what is in the brief the principal
approved, whoever first said it, and because a mark naming a model
reads differently on every model the forge runs on. The two marks
that stay carry provenance and reservation, not authorship.

A project may have more than one brief because a big new whole needs
a place where the thought can be tempered before it enters the trunk,
much as a branch does in git, without a new document kind. A thread
was wrong for it, since a thread is a question and not a body of
work. A working space with positions before the merge was judged
heavy for now.

The mining is recorded in the intent's history and not in the
brief's because the mining changes the intent and not the brief.

The brief keeps the language it is written in. The reason for this
exception is not recorded.

## A worked example

A generic brief of five lines, in the shape the template defines.
The header is the template's, placeholders included; the text below
it is free form.

```
---
project: <slug>
title: <working title>
author: <principal>
version: 0.1
status: draft
---

We want one place where every team's on-call handover is written
the same way, because today each team keeps its own notes and the
next shift reads none of them. A one-page template seems enough;
what a handover must say at minimum is not yet decided (remark:
the night shift may need less). Out of scope: tooling and alerts.
```

The brief names what is wanted and why, keeps one open question
visible as a remark, states one boundary, and leaves the rest to the
intent.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
