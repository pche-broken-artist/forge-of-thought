---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 77f3b8d1f4ea80f7
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how you derive the assignment, the document that carries the intent to its recipients, with `/forge assignment`. It is for the principal (the person whose thinking is being forged) who has an intent and wants to hand its in-scope substance on.

## When to use it

- You have an intent and no assignment yet.
- You have an assignment, and the intent has moved since.
- You want to fix the wording of an assignment that stands.

The assignment has to be complete: nothing its recipients would need is left to assumption. What that means is on [The assignment](../about/the-assignment.md).

## The command

```
/forge assignment [slug]
```

The slug names the project; `my-project` stands in for it here.

```
/forge assignment my-project
```

## What happens

Claude first reads the intent and the assignment as it stands. It says whether the intent is ready to be derived from. That statement is advice and never a gate. Then one of three ways follows.

- No assignment yet: the joint pass runs whole, in the three phases below.
- An assignment that stands and an intent that moved: the pass runs on what changed, and the provenance map shows what the change touched.
- A wording fix: it is made in the assignment directly.

A change of substance asked for in the assignment goes to the intent first. The assignment is then derived from the changed intent.

1. **Questions up front.** Claude asks one question per message. It asks only what is yours to answer and the intent does not answer:
   - who the recipients are;
   - what is delegated and what is specified;
   - whether success criteria are present, delegated or deliberately absent;
   - what is later.

   Where the intent answers everything, there are no questions. A question about the detail of the handover is asked here. A question about substance the intent has not settled means the intent is not ready, so the work returns to it. You should now see the questions come one at a time, or none at all.

2. **The recast.** Claude writes the whole draft from the intent. With it comes a provenance map: each group, the items in it and the positions they came from. The map also lists the in-scope positions that landed nowhere, and the items that have no position behind them (drift). Both lists are to be empty. The map is a tool of the pass and no part of the assignment. You should now see a full draft and its map.

3. **The walkthrough by group.** One item of the walkthrough is one group of requirements. Claude says what the group covers, from which positions, what in it is a deliverable or an open question, and what is optional or later. You give one verdict per group. A question about a single item opens a sub-item, which is closed before the next group. You should now see a handful of messages carry dozens of items, with the provenance visible at each.

After the pass, Claude offers `/critique essence`, the independent test of drift. It never runs on Claude's own judgement, and its findings are settled in an ordinary walkthrough. The run is described on [Critique the documents](critique-the-documents.md). When the assignment is complete, Claude offers the approval. It is a recommendation and never a gate.

The items are written in the Requirement style: the rule set is on [Requirement style](../reference/requirement-style.md). Claude chooses the wording and you decide the substance.

## What you have afterwards

- `20-assignment.md`, made from the assignment template, with a history companion `20-assignment.history.md` beside it.
- The sections the template gives, those with no content deleted:
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
- A Terms section that lists only the prefixes and terms the assignment actually uses.
- A closing statement from Claude of what changed.

A requirement group that grows into a project of its own is split off by [Spin off a group](spin-off-a-group.md).

## If something goes wrong

- The intent is silent on a matter the assignment needs: Claude raises it as an open question (a TBC item) and does not fill it.
- A question on substance turns up during the pass: the intent is not ready. The work returns to the intent, and the assignment follows from it.
- The map shows an in-scope position that landed nowhere, or an item with no position: both are to be none, so the draft is corrected before the verdicts.

## A worked example

The group below is generic. Claude presents it as one walkthrough item:

```
### Data handover

Covers: how the recipients receive and check the data they
work from.
From positions: the intent's positions on the source of the
data and on who validates it.
In it: three requirements, one deliverable (DEL: a validation
approach, to be brought back), one open question owned by the
recipients (TBC: the delivery format).
Optional: one requirement on an archive copy, marked optional.
Later: nothing.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer with one verdict, for example `a`. Had you asked a question on the archive item, a sub-item would open, be settled, and the group would then close with its verdict.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
