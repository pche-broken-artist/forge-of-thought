---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 209e605814d36851
inputs:
  - .claude/skills/forge/states/user-stories.md
  - templates/user-stories.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - templates/recipe-user-stories-export.md
  - CLAUDE.md#Working methods
---

# Write user stories

This page shows how you break a BRD, or a small change of the intent,
into user stories with `/forge user-stories`, and how you hand the
stakeholders their export. It is for you as the principal, the person
whose thinking is being forged. What a story is and why the export
leaves the intent out is on [The user stories](../about/the-user-stories.md).

## When to use it

Use it when the requirements are settled enough to be broken into
behaviour seen from the outside, and you want stories that the
stakeholders can approve as a whole.

The stories need one parent, and you name it when you ask:

- The BRD (see [Write a BRD](write-a-brd.md)). Claude reads it
  together with the layers above it, for the reasons the BRD does not
  carry.
- The intent, where the change is small, the ask is precise and has no
  further impact. You say so when you ask.

Whether the ask suffices is your word. Claude may say why it thinks
it does not.

A requirements document of someone else is a different case. You
register it first with `/ingest`. The stories made from it are a work
product in `work/`, never `35-user-stories.md` (see
[Work a work product](work-a-work-product.md)).

## The command

```
/forge user-stories <slug>
```

The slug is the project's; it may be left out where the project is
already clear.

## What happens

The default way is handing over: Claude works the artefact alone and
returns a proposal for your judgement (see
[The working methods](../about/working-methods.md)). Nothing is
derived from the draft before you have judged it.

1. Claude walks the areas of the stories alone and returns the cut
   first. The cut is the name of every story with a short description
   of what it covers, and the items of the parent that no story
   serves, each named by what it says.

   You should now see a list of stories and a list of unserved items,
   and nothing yet drafted. Give your word on the cut.

2. Only when the cut is agreed does Claude draft the whole stories. It
   asks nothing during the drafting and returns the draft.

   You should now see the complete draft in `35-user-stories.md`.

3. You walk the draft story by story. A walkthrough is the way of
   working a list in which each item comes in one message and closes
   with the verdict line (see [Walk through a list](walk-through-a-list.md)).

   You should now see one story per message, each with the verdict
   line, and your verdicts carried to one write at the end of the
   round.

4. Where a story's parent does not suffice, the walk turns into an
   interview on that story, one question at a time.

   You should now see single questions in place of the verdict line
   until that story is clear.

5. Two cases run differently. A parent that moved runs the pass on
   what changed only. A wording fix is made directly.

6. The round ends. Claude names what changed and what stays open, and
   offers the approval.

   You should now see the list of changes, the open questions and the
   offer to approve.

The stakeholders' approval of the whole is your organisation's act.
It is recorded in the decisions where you want it kept.

## What you have afterwards

- `35-user-stories.md`, the stories, with their history beside it.
- Every item of the parent served by a story, or named as not served.
- The open questions, each with its owner.

## Check the stories

Three reviewers are offered, and none runs without your command:

- `/check user-stories` for the mechanics (see
  [Check conformance](check-conformance.md)).
- `/critique clarity` for the wording, measured against the Story
  style (see [Requirement style and Story style](../reference/requirement-style.md)).
- `/critique essence` for drift from the parent.

## Hand the stakeholders their export

The export is a render and never the artefact. Two commands make it.

1. Compose its recipe:

   ```
   /recipe user-stories-export
   ```

   Claude asks a short interview (see
   [Compose a recipe](compose-a-recipe.md)). It asks for three
   things: the input, the section heading and the purpose line. The
   input is `35-user-stories.md` by default, or a work product in
   `work/` where the stories were made from a source. The heading and
   the purpose line are the words of the export you hand over.

   You should now see the recipe of the export written for your
   project.

2. Render it (see [Render an output](render-an-output.md)):

   ```
   /render user-stories-export
   ```

   You should now see `renders/user-stories-export.md`.

The export has one heading per story, with its parts on lines of
their own. It has no table and no wrapped line, so it can be pasted
into a wiki or a tracker as it stands. Every reference to the intent
is left out, because the stakeholders never see the intent. A story
whose reference held only the intent has no reference part in the
export. Nothing else of a story is reworded, shortened or added.

## If something goes wrong

- Claude asks questions during the walk of a story: the parent does
  not carry what the story needs. Answer them; what is missing stays
  a question with an owner, never an assumption. A change of
  substance goes to the parent first.
- The draft contains a technical solution, a priority or an estimate:
  the stories hold none of these, so reject that part in the walk.
- Stories from someone else's document landed in `35-user-stories.md`:
  they belong in `work/`.

## A worked example

The project is `<slug>`, its parent the BRD. Claude returns the cut:

```
Stories
- Export the monthly report: the reader gets the monthly report as a
  file on request.
- Reset a password: a visitor who forgot the password sets a new one.

Items of the parent no story serves
- the archiving of reports older than two years
```

You accept the cut but ask for the archiving item to be named as out
of scope. Claude drafts both stories. In the walk, the first one
arrives:

```
### US.0010 — Export the monthly report
A reader asks for the monthly report and receives it as a file, so
that it can be filed outside the system.
- The report is offered as a file in the format the reader chooses.
- The file holds the figures of the month that was asked for.

**Edge cases:**
- the month has no data → the reader is told that the report is empty

**Questions:**
1. Which formats are offered? → <owner>

**Reference:** BR.0010, POS.0040
```

You answer the verdict line and the walk goes on. In
`renders/user-stories-export.md` the same story reads:

```
### US.0010 — Export the monthly report

A reader asks for the monthly report and receives it as a file, so that it can be filed outside the system.
- The report is offered as a file in the format the reader chooses.
- The file holds the figures of the month that was asked for.

**Edge cases:**
- the month has no data → the reader is told that the report is empty

**Questions:**
1. Which formats are offered? → <owner>

**Reference:** BR.0010
```

The reference to the intent is gone and the sentence stands on one
line.

## See also

- [The user stories](../about/the-user-stories.md): what the stories are, what a story holds and why the export leaves the intent out.
- [Write a BRD](write-a-brd.md): the usual parent of the stories.
- [Work a work product](work-a-work-product.md): the work product stories from someone else's document become.
- [Walk through a list](walk-through-a-list.md): the walk of the draft, one story per message.
- [The working methods](../about/working-methods.md): handing over, the way of composing in which Claude works an artefact alone and returns a proposal for the principal's judgement.
- [Compose a recipe](compose-a-recipe.md): the genre interview every recipe runs through.
- [Render an output](render-an-output.md): the render that makes the export.
- [Check conformance](check-conformance.md): running the `user-stories` check.
- [Requirement style and Story style](../reference/requirement-style.md): the Story style of a story's parts.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
