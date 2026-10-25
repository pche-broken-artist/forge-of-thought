---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: dbbaa34a7c7ed3e7
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how you derive the assignment, the file `20-assignment.md`, from the intent with `/forge assignment`. It is for the principal, the person whose thinking is being forged, who has an intent and now wants to hand its in-scope substance to the recipients. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the intent is ready to be handed over and the project has no assignment yet. Use it again when an assignment stands and the intent has moved since. Claude says whether the intent is ready to be derived from. That is advice, never a gate.

What an assignment is and what makes it complete is on the page [The assignment](../about/the-assignment.md).

## The command

```
/forge assignment [slug]
```

The slug names the project. Claude resolves the project, then reads the intent and the assignment as it stands.

## What happens

The work is a joint pass of three phases. It is one conversation, with one write at its end, on your word.

1. **Questions up front.** Claude asks only what is yours to answer and the intent does not. Such questions are:
   - who the recipients are
   - what is delegated and what is specified
   - whether success criteria are present, delegated or deliberately absent
   - what is later

   It asks one question per message. Where the intent answers everything, it asks none. A question on a detail of the handover is asked here. A question on substance the intent has not settled means the intent is not ready, and the work returns to the intent.

   You should now see either no questions, or one question at a time until the open points are answered.

2. **The recast.** Claude writes the whole draft from the intent. With it comes a provenance map: each group, its items, and the positions of the intent they came from. The map also lists two things that should both be empty: in-scope positions that landed nowhere, and items that have no position behind them (drift). The map is a tool of the pass and is not part of the assignment.

   You should now see the draft and the provenance map, with both lists empty or each entry named.

3. **The walkthrough by group.** A walkthrough is the forge's way of working a list, one item per message. Here one item is one group of the draft. Claude states what the group covers, from which positions it comes, what in it is delegated or open, and what is optional or later. You give one verdict per group. A question on a single item opens a sub-item and is closed before the next group. Dozens of items pass in a handful of messages and nothing is skipped, because the provenance is visible at each.

   You should now see each group closed with a verdict, one after another.

Two rules hold throughout:

- A substance change goes to the intent first, and the assignment follows from it.
- A wording fix is made directly in the assignment.

After the pass, Claude names what changed and offers `/critique essence`, an independent test of drift run by a reviewer that never sees the conversation (a subagent, a separate Claude run). It never runs on Claude's own judgement. Its findings are worked as an ordinary walkthrough. See [Critique the documents](critique-the-documents.md).

When the assignment is complete, Claude offers the approval. That is a recommendation, never a gate.

## What you have afterwards

- `20-assignment.md`, made from the assignment template. Its sections are:
  - Purpose & Context
  - Objective
  - Scope
  - Requirements, in groups
  - Constraints
  - Assumptions
  - Deliverables
  - Open Questions
  - Success Criteria
  - Terms
- `20-assignment.history.md`, its history companion, which records the change.
- The items are written in the Requirement style, the rule set for the items, which is on the page [Requirement style](../reference/requirement-style.md).
- Empty sections and all template comments are deleted. The Terms section lists only the prefixes and terms actually used.

Anything the recipients would need is either written, delegated as a deliverable, or open on purpose as a question with an owner. Silence is not allowed.

## If something goes wrong

- **The intent does not settle a matter the assignment needs.** Claude raises it as an open question and does not fill it. If it is a matter of substance, the work returns to the intent.
- **The provenance map shows a position that landed nowhere, or an item with no position.** Neither is left standing: the position is carried into the assignment, or the item is removed, or the intent is changed first.
- **The intent moved after the assignment was approved.** Run the command again. The pass runs on what changed, and the provenance map shows what the change touched.

## A worked example

A generic project, `<slug>`, whose intent has positions on a notification service. Claude has written the recast and brings the first group to the walkthrough:

> **Group: Delivery channels.** Covers how messages reach the recipients of the service. It comes from three positions of the intent. It holds four requirements, one deliverable that delegates the choice of the message format to the recipients, and one open question owned by the recipients, on whether a second channel is needed at launch. One requirement is marked optional. Nothing in the group is later. No in-scope position of the intent is left out of it.

You answer with one verdict for the group. If you question a single requirement, Claude opens a sub-item on it, settles it, and then asks for the verdict on the group again.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Write a BRD](write-a-brd.md): the business requirements that may be broken out of the assignment next.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
