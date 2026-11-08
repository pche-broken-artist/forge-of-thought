---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 550fb26d11d166f1
inputs:
  - .claude/skills/forge/states/user-stories.md
  - templates/user-stories.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - templates/recipe-user-stories-export.md
  - projects/forge/10-intent.md#POS.1990
  - projects/forge/10-intent.md#POS.2000
  - projects/forge/10-intent.md#POS.2010
  - projects/forge/10-intent.md#POS.2020
  - projects/forge/40-solution-design.md#SOL.0920
---

# The user stories

The user stories are an artefact of the chain, the file
`35-user-stories.md` of a project: the requirements broken into
behaviour seen from the outside, so that the stakeholders can approve
them, the delivery can build from them and the testers can test from
them. This page says what the artefact is, who writes and reads it,
what it is made from, what one story holds, when the stories are
complete, how they are found and why they are shaped as they are. It
also says what the export the stakeholders get looks like and why
that export leaves the intent out. It is for anyone who uses the
forge, extends it or judges it. How to iterate the stories and make
the export is the page [Write user stories](../use/write-user-stories.md).

## What it is

The user stories stand below the BRD and above the solution design.
The [BRD](the-brd.md) is their usual parent. The
[solution design](the-solution-design.md) is the layer that cites
them. The stories break the parent into behaviour seen from the
outside: what the user or the business sees happen, and under which
conditions it is accepted.

They serve three readers at once:

- the stakeholders, who approve the stories as a whole;
- the delivery, which makes its technical analysis and builds from
  them without an empty place;
- the testers, who write their test cases from them.

The relation to the parent is many to many. One item of the parent
may be served by several stories. One story may serve several items.
The solution design cites the stories, never the reverse.

The stories are the artefact. What the stakeholders are handed is not
the artefact but an export: a [render](renders-and-recipes.md) of
the genre `user-stories-export`, one heading per story with its
parts on lines of their own, pasted into a wiki or a tracker. The
export is described below.

## Who writes and reads it

The principal (the person whose thinking is being forged) writes the
stories with Claude. By default the work is handed over: Claude
drafts, the principal judges. The principal decides which stories
stand, their cut, the groupings, every value and the owner of every
question. Claude writes no behaviour the parent does not carry, no
value nobody gave, no technical solution, no priority and no
estimate.

The stakeholders, the delivery and the testers read the stories,
through the export. The ledger (the project's state report, made at
read time from the documents) reads the header of the file.

## Made from

The stories have one parent, named by the principal when he asks for
them. The trail of every story leads to that parent. The parent is
one of two:

- `30-brd.md`, read with the layers above it for the reasons the BRD
  does not carry; a story then cites the BR, NFR, UC or DEP it
  serves;
- `10-intent.md` with its `threads/`, where the change is small, the
  ask precise and without further impact, and the principal says so;
  a story then cites the position of the intent (a `POS`) it
  serves.

Whether the ask suffices for the intent to be the parent is the
principal's word, never Claude's. Claude may say why it thinks the
ask does not suffice.

A requirements document of someone else is a third way in, with a
different result. It is put in through `/ingest` and cited by path.
The stories it yields are a [work product](the-work-product.md) in
`work/`, never `35-user-stories.md`. Each such story cites its place
in the source.

Around the parent, Claude reads `decisions.md`, the ledger and the
indexes of the project's resources. The sources and the research
themselves are read as the principal directs.

## What it holds

The file carries the stories only. Groups are plain headings without
IDs, and they are optional. The stories carry one prefix of their
own, `US`. The skeleton of the file is `templates/user-stories.md`,
listed on the page [Templates](../reference/templates.md); its
header carries a `parent:` field naming `30-brd.md` or
`10-intent.md`.

One story is:

- a heading `US.NNNN — <name>`;
- a free sentence carrying who or what wants it, what happens and
  why; the form "As a… I want… so that…" is neither required nor
  forbidden;
- its acceptance criteria as bullets, in the indicative, one
  behaviour each;
- then only the parts it has, under fixed English labels, in this
  order:
  - `Edge cases`: a situation at the border of the behaviour and
    what happens in it;
  - `Risks`: each with its mitigation or its consequences, never
    alone;
  - `Note`: a link to an attachment or a technical analysis, with
    what lies behind the link;
  - `Questions`: each question with its owner;
  - `Reference`: the BR, NFR, UC or DEP it serves, or in a small
    change the POS.

`Reference` is the one part every story has. The reason is not
recorded. The other parts are left out where a story has nothing for
them, never left empty.

A story is one function as the one who uses it meets it: one actor
doing or seeing one thing. The variants of that function by
condition, its qualities and its transitions are its acceptance
criteria and edge cases, never stories of their own. A new story
begins where another actor does something else, or the same actor
reaches a different function. A quality that cuts across the whole
is a story of its own. A quality that concerns one function is a
criterion of its story.

A criterion carries no vague word: a word that names a quality
without a value gets a value, or becomes a question with an owner. A
story carries no priority, no estimate and no technical solution. The
file carries no section of notes, dependencies or introduction. The
labels are English; the content is in the project's language. The
rules of a story, rule by rule, are the Story style on the page
[Requirement style and Story style](../reference/requirement-style.md).

A story's past lives in the history companion of the file, never in
the story.

## Complete when

The stories are complete when all of this holds:

- every in-scope item of the parent is served by at least one story,
  or is said not to be, with the reason;
- every acceptance criterion can be tested;
- no two stories contradict each other, and no two describe one
  function twice;
- every open question has an owner;
- no question that blocks the delivery is open.

The principal's approval then follows the house scheme: an integer
version. The stakeholders' approval of the whole is the instance's
act, recorded in `decisions.md` where the principal wants it kept.
The reason it is the instance's act is not recorded.

## How it is found

Claude first resolves the project, the parent the principal names and
the stories as they stand. It says whether the parent is stable
enough to be derived from, because it is approved or because the
principal says so. That is never a gate.

The default way in is handing over, when there are no stories yet.
Claude walks the areas of the artefact's Map alone: the coverage, the
behaviour, the edge cases, the qualities, the dependencies, the
risks, the references outward, the contradictions and what stays
open. It returns first the cut: the name of every story with a short
description of what it covers, and the items of the parent that no
story serves, named by what they say. The principal gives his word on
the cut. Only then does Claude draft the whole stories, asking
nothing, and return the draft. The draft is walked story by story (a
walkthrough: one item per message, each closed with a verdict).
Nothing is derived from the draft before the principal has judged it.

The other ways in:

- a story whose parent does not suffice: the walk turns into an
  interview on that story, one question at a time;
- a requirements document put in: the default way runs on it, into
  `work/`;
- a parent that moved: the pass runs on what changed;
- a wording fix: made directly.

What is missing in the parent stands as a question with an owner,
never as an assumption. An answer that changes substance goes to the
parent first; only then do the stories follow.

Every round ends by naming what changed and what stays open. When
the completion above is reached, Claude offers the approval.

The first stories are created from the template as version 0.1, with
their history companion beside them. A write rewrites the file for
coherence, never appends. Empty sections and template comments are
deleted.

The reviewers of the stories are those the forge already has. No new
critic and no new persona were added. The critic lens `clarity`
reads the stories with their Story style. The lens `essence`
compares them with their parent. A challenger of the roster may be
sent where the principal wants the substance tried. A check,
`user-stories`, verifies the mechanics; it is listed on the page
[Checks](../reference/checks.md). It verifies:

- every in-scope item of the parent served or said not to be,
  counted and never judged;
- every story with a Reference to an item that exists;
- the shape and the order of the parts, none present and empty;
- questions with an owner, risks with a mitigation or consequences,
  notes with a link;
- no vague word and no conditional in a criterion;
- no skeleton residue.

### The export

The export the instance hands over is a render, never the artefact.
Its recipe is composed from the skeleton of the genre
`user-stories-export`, listed on the page
[Recipe genres](../reference/recipe-genres.md); the skeleton is
`templates/recipe-user-stories-export.md`. The input is
`35-user-stories.md` by default, or a work product in `work/` where
the stories were made from a source. The render lands in
`renders/user-stories-export.md` unless the recipe says otherwise.

The export has a fixed layout:

- two headings and a purpose line: `# User stories`, a section
  heading, and under it one sentence in italics, both given by the
  principal in the render's language;
- then the stories, one after another, in the order of the artefact;
  the group headings of the artefact are not carried;
- each story: its heading, a blank line, its sentence on a line of
  its own, its criteria directly below it, then only the parts it
  has, each after a blank line with its bold label on a line of its
  own, and last `**Reference:**` with its IDs on the same line;
- no table;
- no line wrapped: every sentence, item and label stands on one
  line, whatever its length;
- the questions keep their numbering and their owner;
- nothing of a story reworded, shortened or added;
- no front-matter, no history and no template comment of the input.

The Reference of a story carries its BR, NFR, UC and DEP into the
export. Every POS is left out. A story whose Reference holds only a
POS has no Reference part in the export. The labels of a story stay
in English whatever the language of the export.

## Why

Why the stakeholders' export leaves out every POS: the stakeholders
never see the intent.

Why the export is a render of its own genre and not a format of the
artefact: so that the artefact keeps its references and the export
changes without touching it. The cost is one more genre.

Why the export has no table: a Markdown table cannot break a line
inside a cell. A paste into a wiki or a tracker would run a story
into one paragraph.

Why no line of the export is wrapped, against the wrapping every
other document keeps: the wiki or the tracker it is pasted into may
break a wrapped line where it stands.

Why a story is one function, and its variants are criteria and edge
cases: the recorded reason is what the first making of stories
showed. A draft that cut the variants of one function into stories
of their own had to be merged. Walking the stories answered open
questions that belonged to the parent, and those answers were
carried up before the stories were written. Hence the cut first, the
draft second, and the parent changed first.

Why a story has the shape it has: it is the shape of the export the
instance hands over, kept by the render, and the principal's word.

Why there is no section of dependencies: the Reference carries them,
as a DEP of the parent, or in a small change as a question.

Why no persona of its own: what a persona would hunt in stories, the
business-analyst persona already hunts in the BRD above them. The
cost is that the substance of a story is tried only by the
principal's walk.

Why a check: what a story can get wrong mechanically is what a check
finds, such as a sentence without its why.

## A worked example

One generic story, as it stands in the artefact. The owner of the
question is a role, not a name.

```markdown
## Lending

### US.0030 — Renew a loan
A member renews a loan from the list of borrowed items, so that the item stays with them without a visit to the desk.
- The list shows a renew action beside every item whose due date has not passed.
- A renewal moves the due date forward by the loan period of the item's category.

**Edge cases:**
- Another member has reserved the item → the renew action is not shown and the item is marked as reserved.

**Questions:**
1. How many renewals of one loan are allowed? → the head of lending

**Reference:** BR.0120, UC.0040
```

The same story as the export shows it. The group heading is gone,
the two headings and the purpose line stand above, and every line
stands whole:

```markdown
# User stories

## Lending

*The stories of the lending service, for approval as a whole.*

### US.0030 — Renew a loan

A member renews a loan from the list of borrowed items, so that the item stays with them without a visit to the desk.
- The list shows a renew action beside every item whose due date has not passed.
- A renewal moves the due date forward by the loan period of the item's category.

**Edge cases:**
- Another member has reserved the item → the renew action is not shown and the item is marked as reserved.

**Questions:**
1. How many renewals of one loan are allowed? → the head of lending

**Reference:** BR.0120, UC.0040
```

Had this story been written in a small change under the intent, its
Reference would hold a POS alone. The artefact would keep it. The
export would show the story without a Reference part.

## See also

- [Write user stories](../use/write-user-stories.md): iterating them
  with `/forge user-stories` and making the export.
- [The BRD](the-brd.md): the usual parent of the stories.
- [The solution design](the-solution-design.md): the layer that
  cites the stories.
- [The work product](the-work-product.md): what stories from someone
  else's document become.
- [Renders and recipes](renders-and-recipes.md): the render, which
  the export is and the artefact is not.
- [Requirement style and Story style](../reference/requirement-style.md):
  the Story style, rule by rule.
- [Checks](../reference/checks.md): the `user-stories` check.
- [Recipe genres](../reference/recipe-genres.md): the export genre
  and its checklist.
- [Templates](../reference/templates.md): the stories' skeleton and
  the export recipe's skeleton among the templates.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
