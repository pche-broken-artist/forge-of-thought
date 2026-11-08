---
project: forge
title: User stories — a layer of user stories below the BRD
author: FT-
version: 0.6
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What I want
A layer of the chain for user stories, `35-user-stories.md`, between
the BRD and the solution design, worked through `/forge user-stories`.

## Why
User stories describe functionality from the user's point of view,
not as a technical specification. They hold the value — what, for
whom and why — and divide the work into parts that can be developed
and tested. The stakeholders approve them as a whole; once approved,
the delivery takes them over, makes its technical analysis on them
and develops from them, unless gaps remain; the testers write their
test cases from them. The analyst's output is a document with the
list of stories, most often in Confluence.

## What it starts from
From requirements of any kind (BR, NFR, security and others), a
many-to-many relation: one BR may yield several stories and one story
may cover several BRs. For a small change, where the specification is
precise and without further consequences, directly from the intent;
whether the specification suffices is the analyst's call.

## The shape of a story
- A story is one function as the one who uses it meets it. Its
  variants by condition, its qualities and its transitions are its
  acceptance criteria and edge cases, not stories of their own; a new
  story begins with another actor or another function. The usual
  behaviour is a criterion, an edge case is a situation at the border.
- ID `US.NNNN`, numbered in tens, groups in hundreds; the name a short
  noun for the function.
- The order of the parts: the name; a free sentence carrying who or
  what, what and why (the template "As a… I want… so that…" is
  neither required nor forbidden); the acceptance criteria as
  bullets; `Edge cases` (situation → what happens); `Risks`, always
  with a mitigation or the consequences; `Note`, only a link to an
  attachment or a technical analysis with an explanation of what lies
  behind it; `Questions` (question → owner); `Reference` (BR, NFR,
  DEP… or POS).
- Only `Reference` is mandatory; the other parts are left out where a
  story has nothing for them. The export for the stakeholders leaves
  out the references to POS, since they do not see the intent; a
  story with POS alone has no Reference line in the export.
- The labels of the parts in English and fixed, the content in the
  project's language.
- Non-functional requirements: a cross-cutting one as a story of its
  own, one concerning a single function as an acceptance criterion of
  that story.
- The document carries the stories only.

## Wording
Acceptance criteria in the indicative present, one behaviour per
bullet. No vague words ("fast", "suitably", "intuitively"); where a
value is missing, an open question is written. No technical solution
— components, API, data model — at most a link to an attachment or a
technical analysis.

## When they are done
- Every requirement is covered by at least one story, or it is said
  why not.
- Every acceptance criterion is testable.
- The stories do not contradict each other and the same function is
  not described twice differently.
- Every open question has an owner; a story with a question that
  blocks development is not done.
- The stakeholders have approved the stories as a whole.

## How they are made
Claude first proposes the cut: the names of the stories with a short
description, and the requirements no story covers, described in
words. Once the analyst approves it, Claude drafts the whole stories
from the BRD (for a small change from the intent) and the analyst
walks them story by story. Where the specification does not suffice,
the walk turns into an interview on the single story. What is missing
is not guessed: an open question is written.

## Check and output
- A new mechanical check `check-user-stories` on the pattern of
  `check-brd`: coverage of the requirements, cited IDs that exist,
  criteria and edge cases, questions with an owner, risks with a
  mitigation or consequences, a Note with a link and an explanation.
- The critic `clarity` knows the style of the stories and does not
  report its difference from the style of requirements.
- A render by a recipe produces exactly the format of the export
  (`sources/example-user-stories-v2.md`): fixed headings and a
  sentence on the purpose, no table, one heading per story, the parts
  on lines of their own, no wrapping, so that it can be pasted into
  Confluence and Jira.

## What I do not want
Priority, estimate, technical solution, graphic detail, a breakdown
into tasks, a section of notes, a separate section of dependencies (a
dependency is a `DEP` in the Reference, for a small change an open
question), an introduction or assumptions in the document.

## A change of the engine besides
ID prefixes of two or three letters (POS.0220, the ID scheme in
`CLAUDE.md`) and the expression `[A-Z]{2,3}` in the scripts, so that
`US`, `BR` and `UC` work. The rule of three letters came from the
alignment with the group's BRD standard (REJ.0100) and the engine
already broke it with `BR` and `UC` (POS.1830).

## The way
By POS.1780: this brief, then the definition with its template, the
check and the recipe, then a trial on a small project (the
specification: content in a CMS tied to a player's level), only then
the positions in the engine's intent and the item of the solution
design.
