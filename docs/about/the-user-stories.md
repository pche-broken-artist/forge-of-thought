---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 715bbbcd216b62f9
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

The user stories are the document of a project that breaks its
parent into behaviour seen from the outside. This page says what the
document is, what one story holds, how the stories are found and
reviewed, and why the export that the stakeholders get leaves the
intent out. It is for the one who uses the forge, the one who extends
it and the one who evaluates it. The words of the forge used here are
in the [Glossary](../reference/glossary.md).

## What it is

The user stories are an artefact of the chain, that is a document of
the chain of versioned documents along which an idea travels. The
file is `35-user-stories.md`. It stands below the BRD (see
[The BRD](the-brd.md)) and above the solution design (see
[The solution design](the-solution-design.md)).

The stories break the parent into behaviour seen from the outside:
what the user or the business sees happen, and under which conditions
it is accepted. They are written for three readers:

- the stakeholders, who approve the stories as a whole;
- the delivery, which makes its technical analysis and builds from
  the stories without an empty place;
- the testers, who write their test cases from them.

The stories and the items of the parent do not pair one to one. One
item of the parent may be served by several stories. One story may
serve several items. The solution design cites the stories, never the
reverse.

```
the parent: the BRD, or the intent in a small change
      ^
      |  Reference: a story cites the items it serves,
      |  several stories to one item, one story to several
      |
35-user-stories.md  ----- /render ----->  the export (a render)
      ^
      |  cites the stories, never the reverse
      |
the solution design
```

The stakeholders are not handed this file. They are handed the
export, which is a render: an output generated from the artefact for
its audience (see [Renders and recipes](renders-and-recipes.md)). The
section "The export" below describes it.

## Who writes and reads it

The principal (the person whose thinking is being forged) writes the
stories with Claude. By default the work is handed over: Claude works
alone from the parent and returns a proposal, which the principal
judges.

The work is divided. Claude makes the recast:

- the whole list of stories drawn from the parent, with the reference
  of each;
- the groupings it proposes;
- the edge cases that each behaviour invites;
- the wording in the Story style.

The principal decides which stories stand, their cut (which stories
there are and what each covers), the groupings, every value and the
owner of every question.

Claude writes no behaviour that the parent does not carry and no
value that nobody gave. It writes no technical solution: no
component, API, data model or detail of the design. It writes no
priority and no estimate.

The stakeholders, the delivery and the testers read the stories in
the export. The solution design cites them. The reviewers read the
file itself, as the section "The reviewers" below says.

## Made from

The stories have one parent. The principal names it when he asks for
the stories, and the trail of each story leads to it. The
front-matter of the file names the parent under `parent:`.

- **The BRD** (`30-brd.md`): the usual parent. It is read with the
  layers above it for the reasons it does not carry. A story cites
  the item of the BRD it serves: a BR, an NFR, a UC or a DEP.
- **The intent** (`10-intent.md`) with its threads (matters of the
  project set aside to be taken up later): the parent where the
  change is small, the ask is precise and without further impact,
  and the principal says so. A story then cites the POS (an item of
  the intent) it serves. Whether the ask suffices is the principal's
  word, never Claude's. Claude may say why it thinks it does not.

A requirements document of someone else is not a parent. It is
registered as a source through `/ingest` and cited by path. The
stories made from it are a work product in `work/` (see
[The work product](the-work-product.md)), never `35-user-stories.md`.
Each such story cites its place in the source.

Around the parent Claude reads:

- `decisions.md` (the principal's decisions with their reasons);
- the ledger (the file that states where the project stands);
- the indexes of the project's resources;
- sources and research, as the principal directs.

## What it holds

The document carries the stories only, under one prefix of its own:
US. Its front-matter carries the version, the status, the project and
the parent. Groups are optional and are plain headings without IDs.
The history is kept in the companion file
`35-user-stories.history.md`. A story's past lives there, never in
the story.

A story is one function as the one who uses it meets it. Its variants
by condition, its qualities and its transitions are its acceptance
criteria and edge cases, never stories of their own. A quality that
cuts across the whole is a story of its own. A quality that concerns
one function is a criterion of that function's story.

A story holds these parts, in this order:

- the heading `### US.NNNN — <name>`: the ID and the name of the
  function;
- the sentence: free prose that carries who or what wants it, what
  happens and why. The form "As a… I want… so that…" is neither
  required nor forbidden;
- the acceptance criteria: bullets in the indicative, one behaviour
  each;
- `Edge cases`: each written `<situation> → <what happens>`;
- `Risks`: each written `<risk> → <mitigation | consequences>`, never
  a risk alone;
- `Note`: a link to an attachment or a technical analysis, with what
  lies behind it;
- `Questions`: numbered, each written `<question> → <owner>`;
- `Reference`: the BR, NFR, UC or DEP that the story serves, or the
  POS in a small change without a BRD.

`Reference` is the one part every story has. The other labelled parts
are left out where a story has nothing for them. None is left empty.
The five labels are fixed and in English. The content is in the
project's language.

A story does not hold:

- a vague word in a criterion, that is a word that names a quality
  without a value;
- a priority or an estimate;
- a technical solution;
- a section of notes, of dependencies or of introduction. A
  dependency is a DEP in the Reference, or a question.

The rules of the wording are the Story style (see
[Requirement style and Story style](../reference/requirement-style.md)).
The shape is that of the template `templates/user-stories.md` (see
[Templates](../reference/templates.md)).

## Complete when

The stories are complete when all of this holds:

- every in-scope item of the parent is served by at least one story,
  or is said not to be, with the reason;
- every acceptance criterion can be tested;
- no two stories contradict each other or describe one function
  twice;
- every open question has an owner;
- no question that blocks the delivery is open.

When that is reached, Claude offers the approval of the document.
That approval belongs to the principal, as the versioning scheme of
the forge has it. The stakeholders' approval of the whole is a
different act: it is the act of the instance (one installation of the
forge). It is recorded in `decisions.md` where the principal wants it
kept.

## How it is found

The stories are worked with `/forge user-stories`; the job is
described in [Write user stories](../use/write-user-stories.md). The
rules belong to the definition
`.claude/skills/forge/states/user-stories.md`, which is paired with
the template.

At the start Claude says whether the parent is stable enough to be
derived from: approved, or stable on the principal's word. It says
so, and the work is never stopped on it.

Where there are no stories yet, the work is handed over by default.
Claude walks the Map of the definition alone and returns first the
cut. The cut is the name of every story with a short description of
what it covers, in words, and the items of the parent that no story
serves, named by what they say. The principal gives his word on the
cut. Only on the cut agreed does Claude draft the whole stories. It
asks nothing while it drafts, and it returns the draft. The draft is
then worked story by story in a walkthrough (a list worked one item
per message, each item closed by the principal's verdict). Where the
parent does not suffice for a story, the walkthrough turns into an
interview on that story, one question at a time.

The other ways in are shorter:

- a requirements document of someone else: the default way runs on
  it, and the result is a work product in `work/`;
- a parent that moved: the pass runs on what changed;
- a fix of wording: it is made directly.

The Map of the definition names what the stories are to find. Claude
walks it before the recast, to see what the parent does not answer,
and again at the end. An area may stay empty when it was considered
and found not to apply. The areas:

- the coverage: every in-scope item of the parent and the stories
  that serve it, or the reason none does;
- the behaviour: for each story who or what wants it, what happens
  and why, and the conditions under which it is accepted;
- the edge cases: the situations at the border of each behaviour and
  what happens in them;
- the qualities: the non-functional items that cut across the whole,
  as stories of their own, and those that concern one function, as
  criteria of its story;
- the dependencies: what a story needs from outside itself, cited as
  a DEP of the parent, or in a small change asked as a question;
- the risks: where a story carries one, its mitigation or its
  consequences;
- the references outward: an attachment or a technical analysis that
  a story points to, with what lies behind the link;
- the contradictions: two stories, or a story and its parent, that do
  not agree;
- what stays open: every question with its owner, and which of them
  block the delivery.

What is missing in the parent stands in the stories as a question
with an owner, never as an assumption. A change of substance goes to
the parent first. A round ends with Claude naming what changed and
what stays open.

## The reviewers

The stories have no critic and no persona of their own. The reviewers
that the forge already has read them:

- the `clarity` lens of the critic (`/critique clarity`) reads the
  stories with their Story style;
- the `essence` lens of the critic (`/critique essence`) compares
  them with their parent and looks for drift from it;
- a challenger of the roster may be sent where the principal wants
  the substance tried;
- the check `user-stories` (`/check user-stories`, see
  [Checks](../reference/checks.md)) verifies the mechanics.

The check verifies:

- that every in-scope item of the parent is served or said not to be.
  This coverage is counted, never judged;
- that every story has a Reference to an item that exists;
- the shape and the order of the parts, with none present and empty;
- that every question has an owner, every risk a mitigation or
  consequences, and every note a link;
- that no criterion holds a vague word or a conditional;
- that nothing of the template is left in the file.

## The export

The export is what the instance hands over to its stakeholders, to be
pasted into a wiki or a tracker. It is a render of the genre
`user-stories-export` (see
[Recipe genres](../reference/recipe-genres.md)), never the artefact.
`/render` makes it from the project's recipe (the versioned file that
says how a render is made). The recipe is composed from the template
of the genre, `templates/recipe-user-stories-export.md`. Its input is
`35-user-stories.md` by default, or a work product in `work/` where
the stories were made from a source. Its output is
`renders/user-stories-export.md` by default.

The layout of the export:

- two headings and a purpose line in italics open it. The first
  heading is `# User stories`. The second heading and the purpose
  line are the principal's words, in the language of the render;
- the stories follow one after another, in the order of the artefact.
  The group headings of the artefact are not carried;
- each story is its heading `### US.NNNN — <name>`, a blank line, its
  sentence on a line of its own and its criteria directly below;
- then come only the parts the story has, each after a blank line,
  its bold label on a line of its own and its items below it;
- `**Reference:**` comes last, with its IDs on the same line;
- there is no table, and no line is hard-wrapped: every sentence,
  item and label stands on one line, whatever its length;
- nothing of a story is reworded, shortened or added. The questions
  keep their numbering and their owner. The labels stay in English
  whatever the language;
- the front-matter of the artefact, its history and the comment of
  its template are not carried.

The export leaves out every reference to a POS. It carries the BR,
NFR, UC and DEP of a Reference. A story whose Reference holds only
POS has no Reference part in the export. The artefact itself keeps
all its references.

## Why

- **The cut first, and one function per story.** A draft cut by
  condition splits one function into variants that the stakeholders
  read as one. The walk of the stories also answers open questions of
  the parent, and those answers go up into the parent before the
  stories are written.
- **The shape of a story.** It is the shape of the export that the
  instance hands over, which the render keeps, and it is the
  principal's word.
- **No section of dependencies.** The Reference carries them: a
  dependency is a DEP there, or it is a question.
- **No critic and no persona of their own.** What a story can get
  wrong mechanically is what the check finds. What a persona would
  look for in stories, the business-analyst persona already looks for
  in the BRD above them. A check without a persona was chosen against
  a persona of the stories' own. The price is that the substance of a
  story is tried only by the principal's walk.
- **The export as a render of its own genre.** It was chosen against
  a format of the artefact itself. As a render, the export changes
  without touching the artefact, and the artefact keeps its
  references to the intent. The price is one more genre.
- **No POS in the export.** The stakeholders never see the intent.
- **No table and no wrapped line in the export.** A Markdown table
  cannot break a line inside a cell, and a paste into a wiki or a
  tracker would run a story into one paragraph. A wiki or a tracker
  may also break a wrapped line where it stands.
- **`Reference` as the one part every story has.** The reason is not
  recorded.
- **The stakeholders' approval as the act of the instance.** The
  reason is not recorded.

## A worked example

One generic story as it stands in `35-user-stories.md`. It has two
criteria, one edge case, one question and its Reference. It carries
no risk and no note, and those two parts are absent.

```
### US.0010 — Export of the order list
A logged-in customer downloads the list of his orders as a file, so
that he can work with it outside the application.
- The export holds every order that the list shows under the filter
  in use.
- The file is ready for download within 10 seconds of the request.

**Edge cases:**
- The filter matches no order → the download is not offered and the
  list says that it is empty.

**Questions:**
1. In which file format is the list exported? → the product owner

**Reference:** BR.0040, NFR.0020
```

The same story as the export shows it, under the two headings and the
purpose line:

```
# User stories

## Order list

*The behaviour of the order list, for approval as a whole.*

### US.0010 — Export of the order list

A logged-in customer downloads the list of his orders as a file, so that he can work with it outside the application.
- The export holds every order that the list shows under the filter in use.
- The file is ready for download within 10 seconds of the request.

**Edge cases:**
- The filter matches no order → the download is not offered and the list says that it is empty.

**Questions:**
1. In which file format is the list exported? → the product owner

**Reference:** BR.0040, NFR.0020
```

The words of the story are the same in both. The export adds a blank
line after the heading and puts every sentence and every item on one
line. Had the story come from a small change with the intent as its
parent, its Reference would hold a POS only. The export would then
end with the question and carry no Reference part.

## See also

- [Write user stories](../use/write-user-stories.md): iterating them
  with `/forge user-stories` and making the export.
- [The BRD](the-brd.md): the usual parent of the stories.
- [The solution design](the-solution-design.md): the layer that cites
  the stories.
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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
