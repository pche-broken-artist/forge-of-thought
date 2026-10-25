---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: f173adf9ebed6220
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

A brief is the principal's own text of one whole of thinking: what
he wants and why, put together before it is worked into positions.
The principal is the person whose thinking is being forged, and the
final authority on what the documents say. This page is for anyone
who uses the forge or weighs it, and wants to know what a brief is,
who writes it, what it holds and why it is left rough on purpose.

## What it is

A brief is the first artefact of a project's chain, the chain being
the series of versioned documents an idea travels through. It holds
what the principal wants and why, with what he chose to take from
the finding around it. The finding is the wide search that happens
while the brief is composed: research, sources, his ideas and
Claude's.

A brief holds thoughts to be processed, not decisions. Nothing in it
is yet a position. Its thoughts may be changed, reworked or dropped
when the brief is mined, that is, worked into the intent. Only the
intent turns them into positions. How that works is said on
[The intent](the-intent.md).

A brief is not the record of the finding. What the principal does
not take from the finding stays out of the brief.

## Who writes and reads it

The brief is the principal's. What is in it he approved, whoever
first said it.

Claude helps compose it. At the opening Claude is the active one:

- it inspires;
- it brings how the same thing is done elsewhere and how original
  the idea is;
- it verifies what can be verified;
- it proposes research and the intake of outside material.

When the brief is written, Claude takes what the talk arrived at and
writes it down so that it is understood, on the principal's word to
write. It may translate, mend the grammar and word an idea of its
own that the principal has accepted. What it has formulated it
reflects back before it is written. It does not decide what goes in.
It does not shape the brief into an intent.

The brief is read when it is mined into the intent. A position mined
from it cites the brief, with the version it was mined at, as its
provenance. The ledger (the record of the project's state, made from
the documents whenever it is read) shows one row per brief in its
Briefs table, from the brief's header and the record of the mining.

## Made from

The principal's thought, however it arrives. Around it, gathered
while the brief is composed:

- research notes, in `research/`;
- sources, in `sources/`;
- Claude's own proposals.

The existing intent and the ledger are read only to know what
already stands, never to shape the text.

## What it holds

A brief has a minimal YAML header and nothing else is fixed. The
header comes from `templates/brief.md`:

```
---
project: <slug>
title: <working title>
author: <principal>
version: 0.1
status: draft
---
```

Below the header the text is free form. It may carry any headings,
tables, lists, prose or use cases the principal finds useful. It has
no required content, no IDs and no conventions of the chain.

Its usual shape is light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it;
- the research that verifies or limits a topic, cited beside it;
- what is still open.

It may carry a mechanism where the mechanism is part of the idea.

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)`: stands where the identity of a source
  supports, limits or contradicts the thought. It becomes a fact
  with provenance when the brief is mined.
- `(remark: …)`: a short note that stands where a reservation or an
  uncertainty must stay visible. It is named by what it is, not by
  who made it.

What merely inspired a thought carries no mark. It stays
discoverable through the research note. A suggestion or an
alternative the principal did not take is gone, unless he says it
stays.

A brief is kept in the language it is written in. It is the one
artefact that does not follow the project's language. Why is said on
[Languages](languages.md).

A project may have more than one brief:

- `00-brief.md`: the founding brief.
- `00-brief-<name>.md`: a later whole of thinking, born during the
  project's life. It has the same header, the same states and the
  same rules.

Each brief has a history companion beside it, `<file>.history.md`,
as every versioned document has.

## Complete when

The brief is complete when the principal says so and approves it.
Before the approval is offered, Claude walks the Map of the
definition once, asking whether each area has been consciously
considered. An area may leave nothing in the brief.

A brief is versioned like every artefact. It is a draft until the
principal approves it, which makes it 1.0. After that it is changed
as any artefact is. It is not locked and not immutable: what it said
at any version stands in its history and in git. A new whole of
thinking is a new brief.

A brief is mined into the single intent when the principal says so,
approved or not. How far each brief is mined is recorded in the
intent's history, because the mining changes the intent and not the
brief. That record is a judgement, never a metric. A whole that dies
on the way leaves the brief as it stands and one rejected direction
in the intent, with the reason. The trace survives either way.

## How it is found

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude;
- it is born with Claude from the first word.

The command `/forge brief [name]` is the way in for the latter two.
How you compose one is said on [Write a brief](../use/write-a-brief.md).

The Map of the definition names what the finding looks at. It
prescribes neither headings nor the order of the conversation. Its
areas:

- the thought: what the principal wants, why, and what prompted it;
- the boundaries: what he does not want, and what is out of scope;
- the world around it: what exists that does the same or the
  opposite, as inspiration, counter-example or proof that it exists;
- the material: the sources and research the thought rests on,
  gathered and registered, so that the intent can cite them;
- what is still open: what was not decided or verified during the
  finding.

The walk of the Map asks and does not mend. A tension, an
alternative left undecided or a vague boundary may stay in the brief
as it is.

Two instruments serve the finding:

- `/research <topic>`: durable findings into `research/`, indexed.
- `/ingest [file]`: outside material into `sources/`, registered and
  indexed.

Claude proposes them. They run on the principal's word.

When the talk turns to taking the idea apart and agreeing it piece
by piece (definitions, blocks, wording), Claude says in one sentence
that this is the work of the intent. It offers once to go on in the
intent. This is a recommendation, never a gate. No walkthrough (the
one-item-per-message review of a list of items) runs over the text
of a brief.

## Why

No structure is required. A required structure would force
premature tidiness. A brief templated with chapters, such as goal and
high-level idea, was rejected for that reason.

A brief is rough on purpose, neither perfect nor detailed. Shaping
the thoughts into positions is the work of the intent. A brief
polished until the intent has nothing left to do has gone too far.
It is where thoughts are thrown in before they are sifted, and not
all of them survive.

What the finding yields and the brief does not take has no second
home. A draft intent beside a draft brief, a separate notes record
and a new artefact before the brief were all rejected. The brief
holds the principal's choice. A finding or a source already has
`research/` and `sources/`. What merely fell by in the conversation
is gone with it.

Nothing marks authorship, because what is in the brief the principal
approved, whoever first said it. A mark naming the model, such as
*(Claude)* before every block not the principal's own, was rejected.
Such a mark reads differently on every model the forge runs on. A
remark is named by what it is for the same reason, so that it reads
the same whatever model the forge runs on.

A later brief exists because a big new whole needs a place where the
thought can be tempered before it enters the intent, much like a git
branch, without a new document kind. A thread was wrong for it,
because a thread is a question, not a body of work. A working space
with positions before the merge was judged heavy for now.

## A worked example

A generic brief of five lines below its header:

```
---
project: <slug>
title: Faster onboarding
author: <principal>
version: 0.1
status: draft
---

New colleagues should be productive in their first week, not their first month.
Why: the first month now goes on finding out who owns what.
Not wanted: a longer handbook; nobody reads the one there is.
A buddy per newcomer looks promising (source: research/<note>.md).
Open: who has the time to be a buddy (remark: not yet asked).
```

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
