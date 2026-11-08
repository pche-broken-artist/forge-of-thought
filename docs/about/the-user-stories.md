---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 20f0cb5db0d3320f
inputs:
  - .claude/skills/forge/states/user-stories.md
  - templates/user-stories.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - projects/forge/10-intent.md#POS.1990
  - projects/forge/10-intent.md#POS.2000
  - projects/forge/10-intent.md#POS.2010
  - projects/forge/10-intent.md#POS.2020
  - projects/forge/40-solution-design.md#SOL.0920
---

# The user stories

The user stories are an artefact of the chain, the file
`35-user-stories.md` of a thought project, in which the requirements
of the layer above are broken into behaviour seen from the outside.
This page says what the artefact is, who writes and reads it, what
it is made from, what one story holds, when the stories are complete,
how they are found and why they have this shape. It is for the user
who will have stories written, for the extender who wants to know
where the layer sits among the others, and for the evaluator who
wants to know what the layer promises.

## What it is

The user stories stand below the [BRD](../about/the-brd.md) and
above the [solution design](../about/the-solution-design.md). They
break their parent into behaviour seen from the outside: what the
user or the business sees happen, and under which conditions it is
accepted.

They serve three readers at once. The stakeholders approve the
stories as a whole. The delivery, that is, the team that builds what
the stories describe, makes its technical analysis and builds from
them without an empty place. The testers write their test cases from
them.

The relation to the parent is many to many. One item of the parent
may be served by several stories. One story may serve several items.
The solution design cites the stories, never the reverse.

## Who writes and reads it

The principal (the person whose thinking is being forged) writes the
stories with Claude. By default the stories are handed over: Claude
drafts them from the parent and the principal judges. What that
looks like is said under How it is found.

The stakeholders, the delivery and the testers read the stories.
The stakeholders get them as an export, which is a render and not
the artefact itself. What the export is and what it leaves out is
said under How it is found.

## Made from

A story has one parent, named by the principal when he asks for the
stories, and the trail of every story leads to it. The parent is one
of two files:

- `30-brd.md`, the BRD, read with the layers above it for the reasons
  the BRD does not carry; a story then cites the BR, NFR, UC or DEP it
  serves;
- `10-intent.md`, the intent (the trunk of the chain, where the
  principal's positions stand) with its `threads/`, where the change
  is small, the ask precise and without further impact, and the
  principal says so; a story then cites the POS it serves. Whether
  the ask suffices is the principal's word, never Claude's; Claude may
  say why it thinks the ask does not suffice.

A requirements document written by someone else is a different case.
Registered through `/ingest` and cited by path, it yields stories
that are a [work product](../about/the-work-product.md) in `work/`,
never `35-user-stories.md`; each such story cites its place in the
source.

Around the parent, Claude reads `decisions.md`, the ledger (the
project's state, made at read time from its documents) and the
indexes of the project's resources, sources and research, as the
principal directs.

## What it holds

The document carries stories only, under one prefix of its own, US.
Groups are plain headings without IDs, and they are optional. The
front-matter carries `parent:`, naming `30-brd.md` or `10-intent.md`.

One story is:

- a heading `US.NNNN — <name>`;
- a free sentence carrying who or what wants it, what happens and
  why; the form "As a... I want... so that..." is neither required
  nor forbidden;
- its acceptance criteria as bullets in the indicative, one
  behaviour each;
- then only the parts it has, under fixed English labels, in this
  order:
  - `Edge cases`: a situation at the border of the behaviour and
    what happens in it;
  - `Risks`: each risk with its mitigation or its consequences,
    never alone;
  - `Note`: a link to an attachment or a technical analysis, with
    what lies behind the link;
  - `Questions`: each question with its owner;
  - `Reference`: the BR, NFR, UC or DEP the story serves, or in a
    small change the POS.

`Reference` is the one part every story has. The other parts are
left out where a story has nothing for them, never left empty. A
dependency is a DEP in the Reference, or a question; the document
has no section of dependencies, no section of notes and no
introduction. The labels are English; the content is in the
project's language.

A story is one function as the one who uses it meets it: one actor
doing or seeing one thing. The variants of that function by
condition, its qualities and its transitions are its acceptance
criteria and edge cases, never stories of their own. A quality that
cuts across the whole is a story of its own. A criterion carries no
vague word, that is, no word naming a quality without a value. A
story carries no priority, no estimate and no technical solution.
The rules of a story in full are the [Story
style](../reference/requirement-style.md).

A story's past lives in its history companion, never in the story.

## Complete when

The stories are complete when all of this holds:

- every in-scope item of the parent is served by at least one story,
  or is said not to be, with the reason;
- every acceptance criterion can be tested;
- no two stories contradict each other, and no two describe one
  function twice;
- every open question has an owner;
- no question that blocks the delivery is open.

Completion is then offered for the principal's approval, as the
house scheme of versions has it. The stakeholders' approval of the
whole is a separate act of the instance (one installation of the
forge), recorded in `decisions.md` where the principal wants it
kept.

## How it is found

The stories are iterated through `/forge user-stories`; what the
command does step by step is on [Write user
stories](../use/write-user-stories.md). Claude first says whether
the parent is stable enough to be derived from, approved or on the
principal's word, but never treats that as a gate.

Handing over is the default way in. Claude walks the areas the
stories must cover alone and returns first the cut: the name of
every story with a short description of what it covers, in words,
and the items of the parent no story serves, named by what they say.
Only once the principal has agreed the cut does Claude draft the
whole stories, asking nothing, and return the draft. The draft is
then walked story by story, that is, put to the principal as a
walkthrough, one story per message, each closed with his verdict.
Nothing is derived from the draft before the principal has judged
it.

The other ways in:

- a story whose parent does not suffice: the walk turns into an
  interview on that story, one question at a time;
- a requirements document put in: the default way runs on it into
  `work/`;
- a parent that moved: the pass runs on what changed;
- a wording fix: made directly.

Claude adds nothing the parent does not carry: no behaviour, no
value nobody gave, no technical solution, no priority, no estimate.
What is missing in the parent stands as a question with an owner,
never as an assumption. An answer that changes substance goes to the
parent first and comes down from there.

A write rewrites the document for coherence; it never appends. What
changed and what stays open is named at the end of every round.

### The reviewers

The stories get no critic lens and no challenger persona of their
own. The `clarity` lens reads them with their Story style. The
`essence` lens compares them with their parent. A challenger persona
already in the roster may be sent where the principal wants the
substance tried. The check `user-stories`
([Checks](../reference/checks.md)) verifies the mechanics: every
in-scope item of the parent served or said not to be, counted and
never judged; every story with a Reference to an item that exists;
the shape and the order of the parts, none present and empty;
questions with an owner, risks with a mitigation or consequences,
notes with a link; no vague word and no conditional in a criterion;
no residue of the template.

### The export the stakeholders get

What the instance hands over to its stakeholders is a
[render](../about/renders-and-recipes.md) of the genre
`user-stories-export` ([Recipe genres](../reference/recipe-genres.md)),
made by `/render` from the project's recipe. It is never the
artefact. Its shape is one heading per story, the parts of the story
on lines of their own and no line wrapped, so that it can be pasted
into a wiki or a tracker. It has no table. The export leaves out
every reference to a POS, and the whole Reference line of a story
that has no other reference. The labels of a story stay in English
whatever the language of the export.

## Why

The stories exist so that three readers can work from one document:
the stakeholders approve the behaviour as a whole, the delivery
builds from it without an empty place, and the testers test from it.

A story is one function, with its variants as criteria and edge
cases, and the stories are handed over in two steps, the cut first
and the draft on the cut agreed. The reason the positions give is
experience with the way in: a first draft tends to cut the variants
of one function into stories of their own, which the principal then
merges back; and walking the stories tends to answer questions the
parent left open, answers that belong in the parent before the
stories are written. Hence the cut before the draft, and hence a
change of substance going to the parent first.

The shape of a story is the shape of the export the instance hands
over, kept by the render, and the principal's word. A section of
dependencies was rejected because the Reference carries them: a
dependency is a DEP cited there, or a question.

The export is a render of its own genre, and not a format of the
artefact itself, so that the artefact keeps its POS references and
the export can change without touching it. The price is one more
genre. The export leaves out every reference to a POS because the
stakeholders never see the intent. It has no table because a
Markdown table cannot break a line inside a cell, and a paste into a
wiki or a tracker would run a story into one paragraph.

The stories get a check and no persona of their own. A check finds
what a story can get wrong mechanically. What a persona would hunt in
stories, the business-analyst persona already hunts in the BRD above
them. The price is that the substance of a story is tried only by
the principal's walk.

Why the Reference is the one part every story has is not recorded
beyond the trail: every story leads back to the item of the parent
it serves. Why the stakeholders' approval is an act of the instance
rather than of the forge is not recorded.

## A worked example

One generic story, as it stands in `35-user-stories.md`. The slugs
and items are placeholders.

```markdown
### US.0030 — Renew a loan
A reader renews a loan from his list of loans, so that a book he
still needs stays with him without a visit to the desk.
- The list offers renewal on every loan that is not yet overdue.
- A renewed loan ends 21 days after the day of the renewal.

**Edge cases:**
- the book is reserved by another reader → the renewal is refused and the reservation is shown

**Questions:**
1. How many renewals in a row are allowed? → the head of lending

**Reference:** BR.0120, UC.0030
```

The same story as the export shows it: one heading, the sentence,
each criterion, each edge case, each question and the Reference on
a line of its own, no line wrapped, so that a paste keeps the parts
apart. The second heading of the export and the sentence under it
are the principal's words; the exact layout is the skeleton's,
`templates/recipe-user-stories-export.md`.

```markdown
### US.0030 — Renew a loan
A reader renews a loan from his list of loans, so that a book he still needs stays with him without a visit to the desk.
- The list offers renewal on every loan that is not yet overdue.
- A renewed loan ends 21 days after the day of the renewal.
**Edge cases:**
- the book is reserved by another reader → the renewal is refused and the reservation is shown
**Questions:**
1. How many renewals in a row are allowed? → the head of lending
**Reference:** BR.0120, UC.0030
```

The Reference stays, because it cites items of the BRD. Had the
story cited a POS beside them, the export would show the Reference
without it. Had the story cited a POS alone, as in a small change
made from the intent, the export would have no Reference line at
all.

## See also

- [Write user stories](../use/write-user-stories.md): iterating them
  with `/forge user-stories` and making the export.
- [The BRD](../about/the-brd.md): the usual parent of the stories.
- [The solution design](../about/the-solution-design.md): the layer
  that cites the stories.
- [The work product](../about/the-work-product.md): what stories
  from someone else's document become.
- [Renders and recipes](../about/renders-and-recipes.md): the render,
  which the export is and the artefact is not.
- [Requirement style and Story style](../reference/requirement-style.md):
  the Story style, rule by rule.
- [Checks](../reference/checks.md): the `user-stories` check.
- [Recipe genres](../reference/recipe-genres.md): the export genre
  and its checklist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
