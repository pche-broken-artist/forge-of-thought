---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 19fb58c2d0632ff9
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
wants and why, with what he chose to take from the finding around
it. This page says what a brief is, who writes it, what it holds and
why it is rough on purpose. It is for the user who is about to write
one and for the evaluator who wants to know what the first artefact
of a chain is and is not. How a brief is composed, step by step, is
the page [Write a brief](../use/write-a-brief.md).

## What it is

The principal is the person whose thinking is being forged; he
supplies the ideas and the decisions, and Claude, the machine that
works with him, owns the structure and the process. The brief is the
first artefact of a project's chain, and the trunk of the chain, the
intent, is mined from it (see [The intent](the-intent.md)).

A brief is free form. Any structure the principal finds useful is
allowed: prose, headings, tables, use cases, lists. It has no
required content, no IDs and none of the conventions of the chain.
Only a minimal YAML header is fixed; the text below it is the
principal's. A templated brief with chapters (goal, high-level idea
and so on) was considered and rejected.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position. Its thoughts may be changed, reworked or dropped
when mined, and only the intent turns them into positions.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling is the intent's work. A brief polished until the intent
has nothing left to do has gone too far. It is where thoughts are
thrown in before they are sifted: not all of them survive, and the
sifting is the intent's.

The brief is not the record of the finding. The finding is wide: it
gathers research, sources, the principal's ideas and Claude's, as
many as it can. What goes into the brief and what stays out is the
principal's decision, made on what was found. What stays out lives
in `research/` where it is a finding and in `sources/` where it is a
source. Otherwise it lives nowhere.

A brief is versioned like every artefact: a draft until the principal
approves it as 1.0, and changed after that as any artefact is. It is
not locked and not immutable. What it said at any version stands in
its history companion and in git. A brief is the provenance of its
whole: a position mined from it cites it with its version, and drift
is measured against that version.

A project may have more than one brief. The founding brief is
`00-brief.md`. Every later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as
`00-brief-<name>.md`, with the same header, the same states and the
same rules. A brief is mined into the single intent when the
principal says so, approved or not. A whole that dies on the way
leaves the brief as it stands and one rejected direction in the
intent with the reason, so that the trace survives either way. The
ledger (the project's single file of state) carries one row per
brief in its Briefs table. How far a brief is mined is a judgement
recorded in that row's note and in the provenance of the positions,
never a metric.

A brief is kept in whatever language it is written in. The artefacts
of the chain are otherwise written in the project's one output
language, and the brief is the one exception among them (see
[Languages](languages.md)).

Three origins of a brief are equally legitimate, and the forge does
not distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it. Claude's part changes on the way. At the opening
Claude is the active one: it inspires, brings how the same thing is
done elsewhere and how original the idea is, verifies what can be
verified, and proposes research and ingest. A proposal of its own,
however large, serves the finding and is not the brief. Then the
brief is written. Claude moves the principal to say what he wants,
why, and what he does not want, and it forms the record: on the
principal's word to write, it takes what the talk arrived at and
writes it down so that it is understood. It may translate, mend the
grammar and word an idea of its own that the principal has accepted.
What it has formulated it reflects back before it is written. What
Claude does not do is take the brief over: it does not decide what
goes in, and it does not chisel the brief into an intent.

Claude holds the form. A brief says what the idea is and why; it may
carry a mechanism where the mechanism is part of the idea. Once the
talk turns to taking the idea apart and agreeing it piece by piece
(definitions, blocks, wording), Claude says in one sentence that this
is the intent's work, does not develop it, and offers once to go on
in the intent. That offer is a recommendation, never a gate. The
principal decides whether the matter stays in the brief as one open
line or is let go. No walkthrough (the one-item-per-message way of
deciding a list) runs over the text of a brief.

What Claude thinks of the brief it says when asked. What does not
fit it says at once and unasked, in one sentence: a wrong
assumption, a contradiction, a risk. What goes into the brief and
what stays out is the principal's to say.

The brief is read when it is mined into the intent, and the intent
cites it with its version from then on.

## Made from

The brief is made from the principal's thought, however it arrives.
Around it, gathered during the elicitation, stand research notes in
`research/`, sources in `sources/` and Claude's own proposals. The
existing intent and ledger are read only to know what already
stands, never to shape the text.

A new brief is created from the template `templates/brief.md`, which
holds the minimal YAML header and nothing else. The header carries
the keys `project`, `title`, `date`, `author`, `version`, `status`
and `last_change`. The version starts at 0.1 and the status at
`draft`. `last_change` is derived from the records of the newest
version in the history companion, `00-brief.history.md`, which is
created beside the brief. The brief gets its row in the ledger's
Briefs table at creation, with mining pending.

## What it holds

The usual shape of a brief is light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it;
- beside each topic, the research that verifies or limits it, cited;
- what is still open.

A brief is composed in a round or two and then mined.

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)` stands where the identity of a source supports,
  limits or contradicts the thought. At mining it becomes a fact
  with provenance. What merely inspired the thought carries no mark
  and stays discoverable through the research note.
- `(remark: …)` stands, short, where a reservation or an uncertainty
  must stay visible. It is named by what it is and not by who made
  it.

A suggestion or an alternative the principal did not take is gone,
unless he says it stays. A summary or a structured proposal the
principal orders into a brief is stored as shown, never re-narrated.

At any time the principal may have Claude give the brief a
structure: the text gathered under headings in a logical order, what
repeats pointed out, the grammar mended. Claude adds nothing, drops
nothing and rewords no thought. It shows the structure before it is
written, and the headings are the principal's to rename. The step is
the principal's to ask for, never a condition of the approval.

## Complete when

The brief is complete when the principal says so and approves it.
Approval happens only on his explicit word. Before the approval is
offered, the Map of the brief's definition is walked once.

The Map of the definition is a map of the finding, not of the brief.
It names what the finding looks at, and what of it enters the brief
is the principal's choice. It prescribes neither headings nor the
order of the conversation. The walk asks one question of each area:
has it been consciously considered? An area may leave nothing in the
brief. The walk asks and does not mend: a tension, an alternative
left undecided or a boundary left vague may stay in the brief as it
is, since resolving them is the intent's work. The areas are:

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

An approved brief is changed like any artefact. A new whole of
thinking is a new brief, not a change of the old one.

## How it is found

A brief is found by elicitation: Claude draws out what the principal
has not yet articulated and writes down what the two of them arrived
at, condensed where the talk was long, in whatever wording says it
best, reflected back before it is written. Writing happens once per
round, on the principal's confirmation.

Two instruments serve the finding. `/research <topic>` stores
durable findings in `research/`, indexed. `/ingest [file]` stores
outside material in `sources/`, registered and indexed. Both are
steps of the elicitation, proposed by Claude and run on the
principal's word. Claude proposes a research step against a named
need: an uncertainty, a comparison, an inspiration. After it, Claude
says what the research changed in the thought, what stays uncertain
and whether more research is likely to change anything. Whether to
go on is the principal's to say. What the research did not find, or
found not to hold, is a finding like any other and stands in the
research note. It enters the brief where the principal takes it.

Of the three origins, the second and the third go through
`/forge brief [name]`. A brief that arrives finished from outside is
stored as it came.

## Why

No structure is required, because a required one would force
premature tidiness. None is forbidden either.

The brief is rough, because the chiselling belongs to the intent.
The brief is the place where thoughts are thrown in; the intent is
the place where they are sifted.

What the finding yields and the brief does not take has no second
home. A draft intent beside a draft brief, a "notes" record kind and
a new artefact before the brief were each considered and rejected.
The brief holds the principal's choice. A finding or a source
already has `research/` and `sources/`. What merely fell by in the
conversation is gone with it.

Nothing marks authorship, because what is in the brief the principal
approved, whoever first said it. A mark that names a model, such as
an italic "(Claude)" before a block, was considered and dropped. Such
a mark reads differently on every model the forge runs on. The two
marks that stay carry something other than authorship, and the
remark is named by what it is so that it reads the same whatever
model the forge runs on.

A brief is not locked, because what it said at any version stands in
its history and in git.

A project may have several briefs, because a big new whole needs a
place where the thought can be tempered before it enters the trunk
of the chain, like a branch in git, without a new document kind. An
open thread was the wrong place for it: a thread is a question, not
a body of work. A working space with positions before the merge was
judged too heavy for now.

Why a brief keeps its own language while the rest of the chain has
one output language: the reason is not recorded.

Why the three origins are treated alike, and why a brief may be
mined before it is approved: the reason is not recorded.

## A worked example

A generic brief, under the header the template gives, might hold
five lines of thought:

```
# Faster onboarding of new colleagues

I want a new colleague to be productive in one week instead of a
month, because every late start costs the team a sprint.
Not wanted: a longer handbook; nobody reads the one we have.
The team of the sister department pairs each newcomer with a buddy
for the first week (source: sources/buddy-programme-notes.md).
Open: whether the buddy's week is counted against the buddy's own
targets (remark: the finance side of this is unverified).
```

Everything in it is a thought to be processed. The intent will turn
what survives into positions, cite the brief with its version, and
leave the rest where it stands.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language while
  the chain has one output language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
