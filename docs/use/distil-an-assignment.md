---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 7acd444041d26a26
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how you derive the assignment, the document that carries the in-scope substance of the intent to its recipients, with `/forge assignment`. It is for the principal, the person whose thinking is forged, who has an intent and wants the assignment made from it.

## When to use it

Use it when the intent is ready to be derived from and no assignment exists yet. Use it again when an assignment stands and the intent has moved. Claude says whether the intent is ready, as a fact and never as a gate. For what makes an assignment complete, see [The assignment](../about/the-assignment.md).

## The command

```
/forge assignment [slug]
```

The slug names the project. Without it, Claude resolves the project itself.

## What happens

The pass is joint: you and Claude work it together, in three phases. The first draft is made from `templates/assignment.md`, beside its history companion.

1. **Questions up front.** Claude reads the intent and the assignment as it stands. It asks only what is yours to answer and the intent does not: who the recipients are, what is delegated and what specified, whether success criteria are present, delegated or deliberately absent, and what is later. It asks one question per message. Where the intent answers everything, it asks none. A question on the detail of the handover is asked here. A question on substance the intent has not settled means the intent is not ready, and the work returns to the intent. You should now see either a question, one at a time, or none because the intent answers everything.

2. **The recast.** Claude writes the whole draft from the intent. With it comes a provenance map: for each group, its items and the positions of the intent they came from. The map also lists the in-scope positions that landed nowhere, and the items that have no position behind them (drift). Both lists are to be empty. The map is a tool of the pass and is not part of the assignment. You should now see the full draft and the map.

3. **The walkthrough by group.** A walkthrough is a list worked one item per message, each closed by a verdict line. Here one item is one group of requirements. Claude says what the group covers, from which positions, what in it is delegated or left open, and what is optional or later. You give one verdict per group. A question on a single item opens a sub-item, which is closed before the next group. Dozens of items pass in a handful of messages, and nothing is skipped. You should now see one message per group, with the provenance visible in each.

Two rules hold throughout:

- A substance change goes to the intent first, and the assignment follows from it.
- A wording fix is made in the assignment directly.

When the pass is done, Claude offers `/critique essence`, an independent test for drift. It never runs on Claude's own judgement. Its findings are settled as an ordinary walkthrough. How to run it is in [Critique the documents](critique-the-documents.md). You should now see the offer of the critique and, once the assignment is complete, the offer of the approval.

## What you have afterwards

- `20-assignment.md`, whose items follow the rules of [Requirement style](../reference/requirement-style.md).
- `20-assignment.history.md`, its history companion, recording what changed and why.
- The sections the project uses only: empty sections and template comments are deleted, and the Terms section lists only the prefixes and terms actually used.

Claude ends by naming what changed. The approval is a recommendation, never a gate.

## If something goes wrong

- The intent leaves a matter unanswered: Claude raises it as an open question instead of filling it. Leaving a matter out is legitimate only as an explicit delegation or an open question.
- You want to change the substance while reading the assignment: the change goes to the intent first.
- Many questions come up in the first phase: that is evidence the intent is not ready, never a measure of it.
- A requirement group has grown into a matter of its own: see [Spin off a group](spin-off-a-group.md).

## A worked example

This is one group's walkthrough item, generic, with a placeholder slug, after `/forge assignment example-project`.

```
### Reporting

Covers: how the recipients report progress to the principal.
From positions: the three positions of the intent on cadence,
format and audience.
Delegated: the format of the report (a deliverable: the
recipients propose it and bring it back).
Open: who receives the report besides the principal (a question
owned by the principal).
Optional: a dashboard, marked optional on its item.
Later: nothing.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer with one letter. Say `a` and the group stands as drafted. Say `q` about one item and Claude opens a sub-item, answers it and then returns to the verdict.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Write a BRD](write-a-brd.md): the business requirements that may be broken out of the assignment next.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
