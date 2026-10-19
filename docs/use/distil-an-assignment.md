---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: db74e4253d4b1f3d
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how you derive the assignment (`20-assignment.md`) from the intent with `/forge assignment`. It is for the principal, the person whose thinking is forged and who decides the content. The assignment carries the in-scope substance of the intent to its recipients, so that they can act without the principal in the room. A full account of what makes it complete is in [The assignment](../about/the-assignment.md).

## When to use it

Use it when the intent is settled enough to hand on and the project has no assignment yet. Use it also when an assignment stands and the intent has moved since.

Claude says at the start whether the intent is ready to be derived from. That is a remark, never a gate: you decide whether to go on.

## The command

```
/forge assignment [slug]
```

The slug names the project. The command runs on the project you name.

## What happens

The work is a joint pass of Claude and you, in three phases. The first draft is created from the assignment template, with its history companion beside it.

1. **Questions up front.** Claude asks only what is yours to answer and the intent does not already answer. Examples are who the recipients are, what is delegated and what specified, whether success criteria are present, delegated or deliberately absent, and what is later. It asks one question per message. If the intent answers everything, there are none.

   A question about the detail of the handover is answered here. A question about substance the intent has not settled means the intent is not ready, and the work returns to the intent.

   You should now see your answers reflected back, with no question left that the intent could have answered.

2. **The recast.** Claude writes the whole draft from the intent. With it, it shows a provenance map: each group, the items in it, and the positions of the intent they came from. The map also lists the in-scope positions that landed nowhere, and the items that have no position behind them (drift). Both lists are meant to be empty. The map is a tool of the pass and is not part of the assignment.

   You should now see the draft and a provenance map with both lists empty, or the gaps named.

3. **The walkthrough by group.** One item of the walkthrough is one group of requirements. For each group Claude says what it covers, from which positions, which of its items are delegated or open questions, and what is optional or later. You give one verdict per group. A question about a single item opens a sub-item, which is closed before the next group. Dozens of items pass in a handful of messages, and nothing is skipped.

   You should now see each group closed with your verdict.

Where a change touches substance, it goes to the intent first and the assignment follows from there. A fix of wording only is made in the assignment directly. What the intent is silent on, Claude raises as an open question rather than filling it.

After the pass, Claude offers `/critique essence`, the independent test of drift. It never runs it on its own judgement. How to run it is in [Critique the documents](critique-the-documents.md). Its findings are worked as an ordinary walkthrough.

You should now see the lens offered, and its findings, if you ran it.

When the assignment is complete, Claude names what changed and offers the approval. The approval is a recommendation, never a gate.

## What you have afterwards

- `20-assignment.md`, with the sections of the template: Purpose & Context, Objective, Scope, Requirements, and where used Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms. Empty sections and all template comments are deleted.
- `20-assignment.history.md`, its history companion, recording the changes.
- Items written in the Requirement style, whose rules are in [Requirement style](../reference/requirement-style.md). A matter left out is left out only as an explicit delegation or open question, never in silence.

If a requirement group has grown into a project of its own, see [Spin off a group](spin-off-a-group.md).

## A worked example

This is one group as it appears in the walkthrough. The slug `my-project` and the content are placeholders.

```
Group: Onboarding (proposed)

Covers: how a new customer gets from sign-up to a first use.
From positions: three positions of the intent about sign-up and
first use (the provenance map lists them).
Delegated: one deliverable asks the recipients to specify the
verification steps and return them.
Open: one question, owned by the recipients, on which sign-up
channels exist today.
Optional or later: a self-service tour, marked optional.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer with one verdict, for example `a`. If you answer `q` about one item, Claude opens a sub-item on that item, closes it, and then returns to the group.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
