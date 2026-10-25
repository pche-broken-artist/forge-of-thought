---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 544b95b8fcb630de
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
he wants and why. The principal is the person whose thinking is
being forged and who has the final say on its content. This page is
for anyone who uses the forge or weighs it up. It explains what a
brief is, who writes it, how it differs from the intent below it,
and why it is rough on purpose.

## What it is

A brief is the first artefact of a project's chain of documents. It
holds what the principal wants and why. It also holds what he chose
to take from the research, the sources and the ideas gathered
around it.

A brief is free form.

- Structure: any headings, tables, lists, prose or use cases the
  principal finds useful.
- Required content: none.
- IDs: none, and no other conventions of the chain.
- Fixed part: only a minimal YAML header.

A brief holds thoughts to be processed, not decisions. Its thoughts
may be changed, reworked or dropped when the brief is mined, that
is, worked into the positions of the intent. Only the
[intent](the-intent.md) turns them into positions (the stances the
principal currently holds). Nothing in a brief is a position yet.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling (taking the thought apart and agreeing it piece by piece)
belongs to the intent. A brief polished until the intent has nothing
left to do has gone too far. Its usual shape is light:

- the topics of the whole;
- a few sentences on each, saying what the principal wants of it;
- the research that verifies or limits it, cited beside it;
- what is still open.

A brief is where thoughts are thrown in before they are sifted. Not
all of them survive, and the sifting belongs to the intent.

A brief is not the record of the exploration around it. That
exploration is wide: research, sources, the principal's ideas and
Claude's. It gathers as many ideas as it can. What goes into the
brief and what stays out is the principal's decision, made on what
was found. What stays out lives in `research/` where it is a
research finding, in `sources/` where it is a source, and otherwise
nowhere.

## Who writes and reads it

The brief belongs to the principal. What is in it he approved,
whoever first said it. Claude helps him put it together and writes
it down on his word, but does not decide what goes in and does not
chisel it into an intent. How a brief is composed with Claude is
described in [Write a brief](../use/write-a-brief.md).

Nothing in a brief marks authorship. Two marks stay, because they
carry something other than authorship:

- `(source: <path>)`: stands where the identity of a source
  supports, limits or contradicts the thought. At mining it becomes
  a fact with provenance in the intent.
- `(remark: …)`: a short note that stands where a reservation or an
  uncertainty must stay visible. It is named by what it is, not by
  who made it.

What merely inspired a thought carries no mark. It stays
discoverable through the research note. A suggestion or an
alternative the principal did not take is gone, unless he says it
stays.

The brief is read when it is mined into the intent. Positions mined
from it cite it as their provenance.

## Made from

A brief is made from the principal's thought, however it arrives.
Around it, research notes, sources and Claude's own proposals are
gathered. The existing intent and the ledger (the report of the
project's state, made from its documents) are read only to know what
already stands, never to shape the text.

Three origins are equally legitimate, and the forge does not
distinguish them:

- finished outside: the brief arrives whole and is stored as it
  came;
- begun outside: it is finished with Claude in the forge;
- born in the forge: it grows from the first word with Claude.

## What it holds

The file is `00-brief.md` for the founding brief. A later whole of
thinking is `00-brief-<name>.md`, with the same header, the same
states and the same rules.

The header comes from `templates/brief.md`:

```yaml
---
project: <slug>
title: <working title>
author: <principal>
version: 0.1
status: draft
---
```

Everything below the header is free form. Each brief has a history
companion beside it, `<file>.history.md`, as every versioned
document has.

A brief is kept in the language it is written in. It is the one
exception among the artefacts, which otherwise follow the language
of the project. The reason is not recorded. The languages of the
forge are described in [Languages](languages.md).

## Complete when

A brief is complete when the principal says so and approves it. It
is versioned like every artefact: a draft (0.1, 0.2, …) until he
approves it as 1.0, and changed after that as any artefact is.

A brief is not locked and not immutable. What it said at any version
stands in its history and in git.

## How it is found

A brief is usually composed in a round or two of conversation and
then mined. Before the approval is offered, the areas around the
thought are checked once, each consciously considered:

- the thought: what the principal wants, why, and what prompted it;
- the boundaries: what he does not want, and what is out of scope;
- the world around it: what exists that does the same or the
  opposite;
- the material: the sources and research the thought rests on;
- what is still open.

An area may leave nothing in the brief. A tension, an undecided
alternative or a vague boundary may stay in the brief as it is,
because resolving them is the intent's work.

A brief is mined into the single intent when the principal says so,
approved or not. Positions mined from it cite the brief, and the
version they were mined at is recorded in the intent's history. The
mining changes the intent, not the brief, so that is where the
record lives. The ledger shows one row per brief, and how far each
is mined, read from that record. "How much" is a judgement recorded
in the mining record and in the provenance of the positions. It is
never a metric.

A whole that dies on the way leaves the brief as it stands. The
intent then records it as one rejected direction, with the reason.
So the trace survives either way.

## Why

No structure is required. A required structure would force
premature tidiness. A templated brief with fixed chapters (goal,
high-level idea and so on) was rejected for this reason. No
structure is forbidden either.

The brief holds only what the principal chose. A second home for
what the exploration yields and the brief does not take was
rejected: a draft intent beside a draft brief, a notes record, or a
new artefact before the brief. What he does not take needs no home.
A research finding or a source has `research/` and `sources/`. What
merely fell by in the conversation is gone with it.

Nothing marks authorship, because what is in a brief the principal
approved, whoever first said it. A mark that names a model would
also read differently on every model the forge runs on. For the
same reason a remark is named by what it is, so that it reads the
same whatever model the forge runs on.

A project may have more than one brief. A big new whole needs a
place where the thought can be tempered before it enters the trunk
(the intent), like a git branch, without a new kind of document.
Otherwise it would land in the intent as a batch of unproven
positions. An open thread of the intent does not fit, because a
thread is a question, not a body of work. A working document with
positions before they are merged was judged too heavy for now.

## A worked example

A generic brief of five lines below its header:

```markdown
---
project: <slug>
title: Shared on-call rota
author: <principal>
version: 0.1
status: draft
---

I want one on-call rota for all teams instead of one per team.
Why: nights are covered twice in some weeks and not at all in others.
Not wanted: a new paging tool; we keep the one we have.
The comparison of rota models stands in research (source: research/<note>.md).
Open: whether weekends count double (remark: not yet discussed with the teams).
```

It has no IDs and no required headings. It says what is wanted, why
and what is not wanted. It cites the research that bears on it and
leaves one question open for the intent.

## See also

- [Write a brief](../use/write-a-brief.md): composing one.
- [The intent](the-intent.md): where the brief is mined.
- [Languages](languages.md): why a brief keeps its language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
