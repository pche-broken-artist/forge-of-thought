---
generated: 2026-10-10
made: mirrored
inputs-hash: 6d6fa5d2d8da4fbd
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - CLAUDE.md
---

# Distil an assignment

This page is for the person who has an intent and wants to hand its
in-scope substance to the recipients as an assignment. It says how
`/forge assignment [slug]` derives `20-assignment.md` from the intent,
what you are asked and what you see at each step.

## What the command does

The command works the assignment and the intent together, in one joint
pass of three phases. It first reads the intent and the assignment as
it stands, and says whether the intent is ready to be derived from.
That is a remark, never a gate.

Which way the pass runs depends on what exists:

- No assignment yet: the pass runs whole, in the three phases below.
- An assignment that stands and an intent that has moved: the pass
  runs on what changed, and the provenance map shows what the change
  touched.
- A wording fix: it is made in the assignment directly.

## The three phases

### 1. Questions up front

You are asked only what is yours to say and the intent does not
answer. Typical questions are who the recipients are, what is
delegated and what is specified, whether success criteria are present,
delegated or deliberately absent, and what is later. The questions come
one per message. Where the intent answers everything, none are asked.

A question on the detail of the handover is asked here. A question on
substance that the intent has not settled means the intent is not
ready, and the work goes back to it.

### 2. The recast

Claude writes the whole draft from the intent. With it comes a
provenance map, which lists:

- each group, its items, and the positions they came from;
- the in-scope positions that landed nowhere (there should be none);
- the items that came from no position, which are drift (there should
  be none).

The map is a tool of the pass. It is not part of the assignment.

### 3. The walkthrough by group

The draft is walked one group at a time, not one item at a time. For
each group you see what it covers, which positions it comes from, what
in it is a deliverable or an open question, and what is optional or
later. You give one verdict per group. A question on a single item
opens a sub-item and is closed before the walk moves on.

Most items are craft derived from the intent, so a verdict on each
would be ceremony. Dozens of items pass in a handful of messages and
nothing is skipped, with the provenance visible at each group. The
map is what lets you see what is missing and not only what is there.

## When you want to change something

A substance change you ask for while working on the assignment goes to
the intent first. A wording fix is made in the assignment directly.

## After the pass

Claude names what changed. Then `/critique essence` is offered as the
independent test of drift. It is never run on Claude's own judgement,
and its findings are settled by an ordinary walkthrough.

When the assignment is complete, the approval is offered. It is a
recommendation, never a gate.

## How the files come about

The first draft is created from the assignment template, with its
history companion `20-assignment.history.md` beside it. The Terms
section lists only the prefixes and terms actually used. Empty
sections and all template comments are deleted.

The items are written with shall and shall not and carry no
priorities. The rules are on the Requirement style page.

## See also

- [About the assignment](../about/the-assignment.md): what makes an assignment complete and where assigning ends.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
