---
generated: 2026-10-09
made: mirrored
inputs-hash: 219b77010bac6548
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - CLAUDE.md
---

# Distil an assignment

This page is for the person who has an intent and wants to carry its
in-scope substance to the recipients as an assignment. It says how to
run `/forge assignment [slug]`, what you are asked, what you see and
what you decide.

## Before you start

Run `/forge assignment` with the project's slug, or without it if the
project can be resolved. Claude reads the intent (with the project's
open threads) and the assignment as it stands, and tells you whether
the intent looks ready to be derived from. This is a remark, never a
gate: you decide whether to go on.

The result is `20-assignment.md`, with its history companion
`20-assignment.history.md`. A first draft is created from the
assignment template, and empty sections and template comments are
deleted.

## The three ways in

- **No assignment yet.** The whole pass below runs.
- **An assignment exists and the intent has moved.** The pass runs on
  what changed, and the provenance map shows what the change touched.
- **A wording fix.** It is made in the assignment directly.

A substance change you ask for while working on the assignment goes to
the intent first. The assignment follows from there.

## The pass

The derivation is one joint pass of three phases. No new kind of
interview is involved.

### 1. Questions up front

Claude asks questions one per message, and only about what is yours to
say and the intent does not answer. Typical ones are who the recipients
are, what is delegated and what is specified, whether success criteria
are present, delegated or deliberately absent, and what comes later.
If the intent answers everything, there are no questions.

A question on the detail of the handover is asked here. A question on
substance the intent has not settled means the intent is not ready, and
the work returns to the intent. Many questions are evidence of that,
never its measure.

### 2. The recast

Claude writes the whole draft from the intent. With it comes a
provenance map, which lists:

- each group of the assignment, its items and the positions of the
  intent they came from;
- the in-scope positions that landed nowhere (there should be none);
- the items that came from no position, which is drift (there should be
  none).

The map is a tool of the pass. It is not part of the assignment.

### 3. The walkthrough by group

One item of the walkthrough is one group of requirements. For each
group Claude shows what it covers, from which positions, what in it is
a deliverable or an open question, and what is optional or later. You
give one verdict per group. If you have a question about a single
item, it opens a sub-item that is closed before the walkthrough moves
on.

Dozens of items pass in a handful of messages, nothing is skipped, and
the provenance stays visible at each group. The reason for this shape:
most items are craft derived from the intent, so a verdict on each
would be ceremony; and reading the whole draft without the map shows
what is there, not what is missing.

## How the items are written

The items are written with "shall" and "shall not", and carry no
priorities. The rules are on [Requirement style](../reference/requirement-style.md).
What makes an assignment complete, and where assigning ends and solving
begins, is explained in [About the assignment](../about/the-assignment.md).

## After the pass

Claude names what changed. Then `/critique essence` is offered as the
independent test of drift. It runs only on your word, and its findings
are settled like any other walkthrough. How to run it is on
[Critique the documents](critique-the-documents.md).

When the assignment is complete, Claude offers the approval. This is a
recommendation, never a gate: only you approve.

## See also

- [About the assignment](../about/the-assignment.md): what makes an assignment complete and where assigning ends.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
