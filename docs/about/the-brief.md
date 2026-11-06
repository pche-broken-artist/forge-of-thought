---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 6d01f4538219a75d
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
wants and why, with what he chose to take from the finding around it.
The principal is the person whose thinking is forged. This page says
what a brief is, who writes and reads it, what it holds, when it is
complete and why it is rough on purpose. It is for the user who wants
to know what the first document of a project is and for the evaluator
who wants to know why it has so little structure. How to compose one
is the page [Write a brief](../use/write-a-brief.md).

## What it is

A brief is the first artefact of a project's chain, the document the
chain starts at. An artefact is a document of the chain, composed by
the principal with Claude and versioned. The founding brief is the
file `00-brief.md`. A later brief is `00-brief-<name>.md`, one per
later whole of thinking.

A brief is free form. Any structure the principal finds useful may
stand in it: prose, headings, tables, lists, use cases. It has no
required content and no IDs. The only fixed part is a minimal YAML
header. The conventions of the chain do not apply to its text.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position. Its thoughts may be changed, reworked or dropped
when they are mined. Only [the intent](the-intent.md) turns them
into positions.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling belongs to the intent. A brief polished until the intent
has nothing left to do has gone too far. It is the place where
thoughts are thrown in before they are sifted: not all of them
survive, and the sifting is the work of the intent.

A brief is not the record of the finding. The finding around it is
wide: research, sources, the principal's ideas and Claude's. The
brief carries what the principal chose to take from it. What he left
out lives in `research/` and `sources/` where it is a finding or a
source, and otherwise nowhere.

A brief is versioned as every artefact is. It is a draft until the
principal approves it, then 1.0, and it is changed after that as any
artefact is. It is not locked and not immutable. What it said at any
version stands in its history and in git.

A brief is kept in the language it is written in. This is the one
exception among the artefacts, which otherwise follow the language of
the project. The reason for the exception is not recorded in the
inputs of this page; what the forge does with languages is the page
[Languages](languages.md).

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it. Claude is his cognitive extension: it proposes,
verifies, draws out and writes down, and it decides nothing about
what goes in.

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact with
  provenance. What merely inspired the thought carries no mark and
  stays discoverable through the research note.
- `(remark: …)` stands where a reservation or an uncertainty must
  stay visible. It is named by what it is and not by who made it.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

The brief is read by Claude when it is mined into the intent through
`/forge intent`. The ledger reads its header. The ledger is the
project's single source of truth for state, made at read time from
the documents. Its Briefs table shows one row per brief and how far
each is mined, from the record of the mining in the intent's history.

## Made from

A brief is made from the principal's thought, however it arrives.
Around it, gathered during the elicitation, stand research notes in
`research/`, sources in `sources/` and Claude's own proposals. A
proposal of Claude's, however large, serves the finding and is not
the brief. The existing intent and the ledger are read only to know
what already stands, never to shape the text.

The file is created from `templates/brief.md`. The template is the
minimal YAML header and nothing else. Beside it a history companion
`<file>.history.md` is created from `templates/history.md`. The
history is an append-only record of what changed in the brief and
why; the body of the brief is the current state, the companion the
record.

## What it holds

The header holds the project's slug, a working title, the author,
the version and the status. The status is `draft` until the brief is
approved.

Below the header the text is the principal's. Its usual shape is
light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it;
- the research that verifies or limits each topic, cited beside it;
- what is still open.

A brief says what the idea is and why. It may carry a mechanism where
the mechanism is part of the idea. A summary or a structured proposal
the principal orders into a brief is stored as shown, never
re-narrated.

## Complete when

A brief is complete when the principal says so and approves it.
Approval is his explicit word, never a by-product of another step.
Before the approval is offered, the Map of the brief's definition is
walked once. The definition is the file that says what the artefact
is and how it is found; its Map names the areas the finding looks at:

- the thought: what the principal wants, why, and what prompted it;
- the boundaries: what he does not want, and what is out of scope;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or proof
  that the wheel exists;
- the material: the sources and research the thought rests on,
  registered so that the intent can cite them;
- what is still open: what was not decided or verified.

The walk asks whether each area has been consciously considered. An
area may leave nothing in the brief. The walk asks and does not mend:
a tension, an alternative left undecided or a boundary left vague may
stay as it is, because resolving them is the intent's work.

A brief is mined into the single intent when the principal says so,
approved or not. Positions mined from it cite the brief with the
version they were mined at. A whole that dies on the way leaves the
brief as it stands and one rejected direction in the intent with the
reason, so that the trace survives either way. How much of a brief is
mined is a judgement recorded in the mining record of the intent's
history and in the provenance of the positions, never a metric.

## How it is found

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

`/forge brief [name]` is the door for the latter two. At the opening
Claude is the active one: it inspires, brings how the same thing is
done elsewhere and how original the idea is, verifies what can be
verified, and proposes research (`/research`) and the registration of
outside material (`/ingest`). Both run on the principal's word. After
a research step Claude says what it changed in the thought, what
stays uncertain and whether more research is likely to change
anything.

Then the brief is written. Claude moves the principal to say what he
wants, why and what he does not want, and forms the record: on the
principal's word to write, it takes what the talk arrived at and
writes it down so that it is understood. It may translate, mend the
grammar and word an idea of its own that the principal has accepted.
What it has formulated it reflects back before it is written. It does
not take the brief over: it does not decide what goes in, and it does
not chisel the brief into an intent.

Claude holds the form. Once the talk turns to taking the idea apart
and agreeing it piece by piece, Claude says in one sentence that this
is the intent's work and offers once to go on in the intent. That is
a recommendation, never a gate. The principal decides whether the
matter stays in the brief as one open line or is let go. No
walkthrough runs over the text of a brief; a walkthrough is the
forge's way of working a list of decisions one item per message.

At any time the principal may have Claude give the brief a structure:
the text gathered under headings in a logical order, what repeats
pointed out, the grammar mended. Claude adds nothing, drops nothing
and rewords no thought. The step is the principal's to ask for and
never a condition of the approval.

What Claude thinks of the brief it says when asked. What does not fit
it says at once and unasked, in one sentence: a wrong assumption, a
contradiction, a risk.

## Why

No structure is required, because a required one would force
premature tidiness. None is forbidden either. A templated brief with
chapters, such as goal and high-level idea, was considered and
rejected for the same reason.

The brief is rough because the chiselling belongs to the intent. A
brief that is composed in a round or two and then mined leaves the
intent the work the intent is for.

The brief is not the record of the finding because what the principal
does not take needs no home. A finding or a source already has
`research/` and `sources/`. What merely fell by in the conversation
is gone with it. A second home for the rest, such as a draft intent
beside a draft brief, a notes record or a new artefact before the
brief, was considered and rejected.

Nothing marks authorship because a mark that names a model reads
differently on every model the forge runs on. Marks such as
*(Claude)* before every block that was not the principal's own were
dropped for this reason. What carried something other than authorship
stays as `(source: <path>)` and `(remark: …)`, so that the brief
reads the same whatever model the forge runs on.

A project may have more than one brief because a big new whole needs
a place where the thought can be tempered before it enters the trunk
of the chain, like a branch in git, without a new document kind. A
thread was wrong for it, since a thread is a question and not a body
of work. A working space with positions before the merge was judged
heavy for now. Every later whole that would otherwise land in the
intent as a batch of unproven positions is therefore born as a brief
under the same rules.

The brief is never locked because what it said at any version stands
in its history and in git.

## A worked example

Below the header the template gives, a brief may be as short as this.
The project and the source are placeholders.

```
Every team keeps its own calendar and we lose a morning a week
finding each other.

I want one calendar every team reads and writes, where the teams
already work, not another tool to log into.

Two products do this already (source: sources/calendar-survey.md);
one of them is free (remark: the free one may not survive the year).

Not wanted: a calendar that also books rooms.

Open: who owns the calendar once it exists.
```

Nothing in it is a position yet. The source mark becomes a fact with
provenance when the brief is mined. The remark keeps a doubt visible
without saying who had it. The open line is the kind of matter the
intent resolves.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
