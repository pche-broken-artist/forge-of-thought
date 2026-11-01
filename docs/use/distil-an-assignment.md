---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: fda189c650b6dbf4
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how to derive the assignment, the document that
carries the intent to the people who will act on it, with
`/forge assignment`. It is for the principal (whoever's thinking is
being forged) who has an intent and wants it handed over complete and
precise. For what makes an assignment complete, see
[The assignment](../about/the-assignment.md). Terms of the forge are
in the [Glossary](../reference/glossary.md).

## When to use it

- The project has an intent and no assignment yet: the pass runs
  whole.
- The assignment stands and the intent has moved: the pass runs on
  what changed.
- The assignment needs only a wording fix: you do not need the pass.
  The fix is made in the assignment directly.

A change of substance asked for while you work on the assignment is
different. It goes to the intent first, and the assignment follows
from there.

## The command

```
/forge assignment [slug]
```

Without a slug Claude resolves the project itself. The target is
`20-assignment.md` in the project, shaped by the assignment template.
Its history is kept in the companion `20-assignment.history.md`.

## What happens

Claude first reads the intent, its threads and the assignment as it
stands. It tells you whether the intent looks ready to be derived
from. This is advice, never a gate. Then the joint pass runs in three
phases.

1. **Questions up front.** Claude asks, one per message, only what is
   yours to answer and the intent does not already answer. These are
   who the recipients are, what is delegated and what is specified,
   whether success criteria are present, delegated or deliberately
   absent, and what comes later. Where the intent answers everything,
   there are no questions. A question about the detail of the
   handover is asked here. A question about substance that the intent
   has not settled means the intent is not ready, and the work returns
   to the intent.

   You should now see your answers reflected back, and no question
   left that the intent could have answered.

2. **The recast.** Claude writes the whole draft from the intent. With
   it comes a provenance map: each group, its items and the positions
   of the intent they came from. The map also lists any in-scope
   position that landed nowhere, and any item that has no position
   behind it (drift). Both lists are meant to be empty. The map is a
   tool of the pass and is not part of the assignment.

   You should now see a complete draft and the provenance map beside
   it.

3. **The walkthrough by group.** Each item of the walkthrough is one
   group of requirements. Claude says what the group covers, which
   positions it comes from, what in it is a deliverable (`DEL`) or an
   open question (`TBC`), and what is optional or later. You give one
   verdict per group. If you have a question about a single item, it
   opens a sub-item that is closed before the walk moves on. Dozens
   of items pass in a handful of messages, nothing is skipped, and the
   provenance is visible at each step.

   You should now see every group closed with your verdict.

The items are written in the Requirement style (shall and shall not,
no priorities, one idea each). The rules are on the page
[Requirement style](../reference/requirement-style.md). Claude words
them. The substance stays yours. Where the intent is silent, Claude
raises a `TBC` instead of filling the gap.

After the pass, Claude offers `/critique essence`, the independent
test of drift. It never runs on Claude's own judgement. How to run it
is on [Critique the documents](critique-the-documents.md). Its
findings are settled as an ordinary walkthrough.

When the assignment is complete, Claude offers the approval as a
recommendation. You decide.

## What you have afterwards

- `20-assignment.md`, with purpose and context, objective, scope,
  requirements in groups, and constraints, assumptions, deliverables,
  open questions and success criteria where they apply. Empty sections
  and template comments are deleted.
- A terms section that lists only the prefixes and terms actually
  used.
- The companion `20-assignment.history.md`, with the round recorded.
- A statement from Claude of what changed in the round.

Two follow-ups are open to you:

- A requirement group may become a project of its own: see
  [Spin off a group](spin-off-a-group.md).
- The business requirements may be broken out of the assignment next:
  see [Write a BRD](write-a-brd.md).

## If something goes wrong

- **The intent is not ready.** Claude says so and the work returns to
  the intent. Many questions in phase 1 are a sign of this, not a
  measure of it.
- **The intent is silent on something the recipients need.** Claude
  does not fill it. It raises a `TBC`, or you delegate the matter
  with a `DEL`. Delegated or open on purpose counts as complete;
  silent does not.
- **A substance change comes up in the walkthrough.** It is made in
  the intent first, and the assignment is then derived again for what
  it touched.
- **The provenance map shows an orphan.** A position that landed
  nowhere or an item with no position is not left standing. Either
  the item is placed or removed, or the position is carried into the
  assignment.

## A worked example

The walkthrough item for one group looks like this. The project and
the group are generic.

```
### Reporting

Covers: how the teams shall report progress to the principal.
From positions: three in-scope positions of the intent on cadence
and content of reports.
Deliverables and open questions: one DEL asks the recipients to
propose the report format and bring it back; one TBC, owned by the
recipients, asks who receives the report on their side.
Optional or later: a dashboard is marked optional on its item.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer with one letter. A question on the dashboard item would
open a sub-item, be answered and be closed before the next group is
shown. The verdicts of all groups are carried to one write at the end
of the round.

## See also

- [The assignment](../about/the-assignment.md): what makes an
  assignment complete.
- [Requirement style](../reference/requirement-style.md): the rule
  set of the items.
- [Critique the documents](critique-the-documents.md): running the
  essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that
  becomes a project of its own.
- [Write a BRD](write-a-brd.md): the business requirements that may
  be broken out of the assignment next.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
