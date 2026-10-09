---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - CLAUDE.md
---

# Distil an assignment

This page is for the person who has an intent and wants the
assignment derived from it. It says what you do with
`/forge assignment [slug]`, what you see in each phase, and what
happens at the end.

The command derives `20-assignment.md` from the intent in one joint
pass of three phases. Without a slug it works on the project the
command resolves; with one, on that project. The result is shaped by
`templates/assignment.md`.

## Before you start

Claude reads the intent (with the project's open threads) and the
assignment as it stands, and tells you whether the intent looks ready
to derive from. That is advice, never a gate: you may go on either
way.

Which way the pass goes depends on what exists:

- No assignment yet: the whole pass runs, in the three phases below.
- An assignment exists and the intent has moved: the pass runs on what
  changed, and the provenance map shows what the change touched.
- A wording fix: it is made in the assignment directly.
- A change of substance that you ask for while working on the
  assignment: it goes to the intent first, and the assignment follows
  from there.

## The three phases

### 1. Questions up front

Claude asks questions one per message, and only those the intent does
not answer and that are yours to answer: who the recipients are, what
is delegated and what is specified, whether success criteria are
present, delegated or deliberately absent, and what is for later. If
the intent answers everything, there are no questions.

A question on the detail of the handover is asked here. A question on
substance the intent has not settled means the intent is not ready,
and the work goes back to it. Many questions are a sign of that, not a
measure of it.

### 2. The recast

Claude writes the whole draft of the assignment from the intent. With
it you get a provenance map, which for each group lists:

- the items in it,
- the positions of the intent they came from,
- the in-scope positions that landed nowhere (there should be none),
- the items that came from no position (drift; there should be none).

The map is a tool of the pass and is not part of the assignment.

### 3. The walkthrough by group

You are walked through the draft one group at a time (a `###` heading
under Requirements). For each group Claude says what it covers, which
positions it comes from, what in it is a deliverable or an open
question, and what is optional or later. You give one verdict per
group. If you have a question about a single item, it opens a
sub-item that is closed before the walk moves on.

Dozens of items pass in a handful of messages and nothing is skipped,
with the provenance in front of you each time. The reason for going by
group: most items are craft derived from the intent, so a verdict on
each would be ceremony; and reading the whole draft without the map
shows what is there, not what is missing.

What is agreed is written once, at the end of the round, on your word.

## How the items are written

The items are written with shall and shall not, carry no priorities,
and are worded by Claude; the substance is yours. The rule set is on
the page [Requirement style](../reference/requirement-style.md). What
makes an assignment complete, and where assigning ends and solving
begins, is explained in [About the assignment](../about/the-assignment.md).

## After the pass

When the pass is done, `/critique essence` is offered as the
independent test of drift. It is offered, never run on Claude's own
judgement; running it is described in
[Critique the documents](critique-the-documents.md). Its findings are
settled in an ordinary walkthrough.

Claude then names what changed. When the assignment is complete in the
sense described in [About the assignment](../about/the-assignment.md),
it offers the approval. That is a recommendation, never a gate.

## See also

- [About the assignment](../about/the-assignment.md): what makes an assignment complete and where assigning ends.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
