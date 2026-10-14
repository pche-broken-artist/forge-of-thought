---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 6fcbc1e6cf6e6a91
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
wants and why, in whatever form he finds useful. The principal is
the person whose thinking is forged. This page says what a brief is,
who writes and reads it, what it holds, when it is complete, how it
comes about and why it is rough on purpose. It is written for the
user of the forge and for anyone evaluating how the forge works. How
to compose one is said in [Write a brief](../use/write-a-brief.md).

## What it is

A brief is the first [artefact](../reference/glossary.md) of a
project: the document the chain starts from. It is the principal's
text of one whole of thinking, with what he chose to take from the
exploration around it. The exploration is wide. It gathers research,
sources, the principal's ideas and Claude's. The brief is not its
record: what goes in and what stays out is the principal's decision,
made on what was found.

The brief is free-form. Any structure the principal finds useful may
stand in it: prose, headings, tables, lists, use cases. It has no
required content and no IDs. Only a minimal header at its top is
fixed. A templated brief with chapters (goal, high-level idea and so
on) was rejected. The reason is that a required structure would
force premature tidiness; none is required, and none is forbidden.

The brief is rough on purpose, neither perfect nor detailed. The
precise work of turning its thoughts into positions belongs to the
intent (the owners call this the chiselling). A brief polished until
the intent has nothing left to do has gone too far. Its usual shape
is light: the topics of the whole, each with a few sentences of what
the principal wants of it, the research that verifies or limits it
cited beside it, and what is still open. It is composed in a round
or two and then worked into the intent.

Nothing in a brief is yet a position. Its thoughts are to be
processed, not decisions: they may be changed, reworked or dropped
when the brief is worked into the intent, and only the intent turns
them into positions. The brief is where thoughts are thrown in
before they are sifted. Not all of them survive, and the sifting is
the intent's work. Where the brief is worked into the intent is
said in [The intent](the-intent.md).

A brief lives as `00-brief.md`, the founding brief of a project, or
as `00-brief-<name>.md`, a later whole of thinking born during the
project's life. A project may have more than one brief. Every later
whole of thinking that would otherwise land in the intent as a batch
of unproven positions is born as a brief of its own, under the same
header, the same states and the same rules.

A brief is kept in the language it is written in. Among the
artefacts of the chain this is the one exception to the rule that
the artefacts follow the project's language. Why a brief keeps its
language is said in [Languages](languages.md).

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it. Claude is its partner, and Claude's part changes on
the way. At the opening Claude is the active one: it inspires,
brings how the same thing is done elsewhere and how original the
idea is, verifies what can be verified, and proposes research and
the intake of outside material. A proposal of Claude's, however
large, serves the exploration and is not the brief. Then the brief
is written. Claude moves the principal to say what he wants, why
and what he does not want, and Claude forms the record: on the
principal's word to write, it takes what the talk arrived at and
writes it down so that it is understood. Claude may translate, mend
the grammar and word an idea of its own that the principal has
accepted. What it has formulated it reflects back before it is
written. What Claude does not do is take the brief over: it does
not decide what goes in, and it does not chisel the brief into an
intent.

Claude holds the form. A brief says what the idea is and why. It
may carry a mechanism where the mechanism is part of the idea. Once
the talk turns to taking the idea apart and agreeing it piece by
piece (definitions, blocks, wording), Claude says in one sentence
that this is the intent's work, does not develop it, and offers
once to go on in the intent. That offer is a recommendation, never
a gate. The principal decides whether the matter stays in the brief
as one open line or is let go. No walkthrough (the item-by-item
review of a list, each item closed with a verdict) runs over the
text of a brief.

What Claude thinks of the brief it says when asked. What does not
fit it says at once and unasked, in one sentence: a wrong
assumption, a contradiction, a risk. What goes into the brief and
what stays out is the principal's to say.

The intent reads the brief. A position mined from a brief cites the
brief and its version as its provenance, and drift is measured
against that version. The brief is in this sense the provenance of
its whole.

## Made from

A brief is made from the principal's thought, however it arrives.
Around it, gathered while the brief is composed, stand:

- research notes, in `research/`;
- sources, in `sources/`;
- Claude's own proposals.

The existing intent and the ledger (the project's one file of
state) are read only to know what already stands, never to shape
the text.

What the exploration yields and the brief does not take has no
second home. A finding of research lives in `research/`. A source
lives in `sources/`. What merely fell by in the conversation is gone
with it. A second home for such material (an early draft of the
intent beside a draft brief, a record kind for notes, or a new
artefact before the brief) was rejected. The reason is that the
brief holds the principal's choice, and what he does not take needs
no home.

## What it holds

At the top stands the fixed header, in YAML. It names the project,
a working title, the date, the author, the version, the status and
the last change. The last change is derived from the records of the
newest version in the brief's history companion, never written by
hand. Below the header the text is free-form.

A brief carries no IDs and no conventions of the chain. Nothing in
it marks authorship. Marks of authorship, such as a model's name in
italics before every block that is not the principal's own, were
rejected. The reason is twofold: what is in the brief the principal
approved, whoever first said it; and a mark that names a model reads
differently on every model the forge runs on.

Two marks stay. Because each carries something other than
authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought; at mining it becomes a fact
  with provenance. What merely inspired the thought carries no mark
  and stays discoverable through the research note.
- `(remark: …)` stands, short, where a reservation or an
  uncertainty must stay visible, named by what it is and not by who
  made it. So that it reads the same whatever model the forge runs
  on.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays.

A summary or a structured proposal the principal orders into the
brief is stored as shown, never re-narrated.

At any time the principal may have Claude give the brief a
structure: the text gathered under headings in a logical order,
what repeats pointed out, the grammar mended. Claude adds nothing,
drops nothing and rewords no thought. It shows the structure before
it is written, and the headings are the principal's to rename. The
step is the principal's to ask for, never a condition of the
approval.

The brief is versioned like every artefact. It is a draft until the
principal approves it, which makes it version 1.0, and it is
changed after that as any artefact is. It keeps its history in a
companion file beside it, and it has one row in the Briefs table of
the ledger, which tracks how far the brief has been mined. How far
is a judgement, recorded in the row's note and in the provenance of
the positions, never a metric.

## Complete when

The brief is complete when the principal says so and approves it.
Before the approval is offered, the Map of its definition is walked
once. The Map is of the exploration, not of the brief: it names
what the exploration looks at, and what of it enters the brief is
the principal's choice. The walk asks one thing of each area: has
it been consciously considered? An area may leave nothing in the
brief. The walk asks and does not mend. A tension, an alternative
left undecided or a boundary left vague may stay in the brief as it
is, since resolving them is the intent's work. The areas are:

- the thought: what the principal wants, why, and what prompted
  it;
- the boundaries: what the principal does not want, and what is
  out of scope;
- the world around it: what exists that does the same or the
  opposite, and what of it is inspiration, counter-example or
  proof that the wheel exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  exploration.

Approval is on the principal's explicit word, never implied. An
approved brief is not locked and not immutable: it is changed like
any artefact, and what it said at any version stands in its history
and in git.

A brief is mined into the single intent when the principal says so,
approved or not. A whole that dies on the way leaves the brief as it
stands and one rejected direction in the intent with the reason, so
that the trace survives either way.

## How it is found

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

`/forge brief [name]` is the door for the latter two. Its
definition is `.claude/skills/forge/states/brief.md`, and the shape
of the result is `templates/brief.md`.

Two instruments serve the exploration. `/research <topic>` stores
durable findings in `research/`, indexed. `/ingest [file]` stores
outside material in `sources/`, registered and indexed. Both are
proposed by Claude and run on the principal's word. Claude proposes
a research step against a named need: an uncertainty, a comparison,
an inspiration. After it, Claude says what it changed in the
thought, what stays uncertain and whether more research is likely
to change anything. Whether to go on is the principal's to say.
What the research did not find, or found not to hold, is a finding
like any other and stands in the research note. It enters the brief
where the principal takes it.

## Why

A brief exists so that the idea is put together before it is taken
apart. Its roughness is deliberate. Because the chiselling of
thoughts into positions is the intent's work, a brief that already
does that work leaves the intent nothing to do and has gone too far.
Because a required structure would force premature tidiness, no
structure is required.

The brief is not the record of the exploration. Because it holds
the principal's choice, what he did not take needs no home of its
own: research and sources have their directories, and the rest is
gone.

Nothing in it marks authorship. Because what is in it the principal
approved, whoever first said it, and because a mark naming a model
reads differently on every model the forge runs on.

A project may have more than one brief. Because a big new whole
needs a place where the thought can be tempered before it enters
the trunk of the intent, like a branch in git, without a new
document kind. An open thread was wrong for it: a thread is a
question, not a body of work. A working space holding positions
before they merge into the intent was judged heavy for now.

A brief keeps its language. The reason is not recorded in the
inputs of this page; see [Languages](languages.md).

## A worked example

Below the fixed header, a brief may be as short as this. The text
is generic and taken from no project.

```
# Onboarding of new colleagues, rethought

A new colleague should be productive in the first week, not the first month.
Today the knowledge sits with three people and leaves with them.
The idea: one written path per role, owned by the team that hires, reviewed each quarter.
Elsewhere this is a checklist (source: research/2026-01-15-onboarding-practice.md); the path is wanted, not the checklist.
Open: who owns the path when a role spans two teams (remark: unverified whether such a role exists today).
```

Five lines, no IDs, one source mark where a source limits the
thought, one remark where an uncertainty must stay visible. The
sifting of these lines into positions is the intent's work.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
