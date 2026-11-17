---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 0efd6f1d9f0f84d0
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

This page shows how you derive the assignment from the intent with `/forge assignment`. The assignment is the document `20-assignment.md`, which carries the in-scope substance of the intent to the recipients (the teams, colleagues or future self who will act on it). It is written for the principal, the person whose thinking is being forged, who works the pass with Claude.

## When to use it

- The project has an intent and no assignment yet. The pass then runs whole.
- An assignment stands and the intent has moved. The pass then runs on what changed.
- You want a wording fix in an assignment that stands. You do not need the pass: the fix is made in the assignment directly.

A substance change you want in the assignment goes to the intent first, then comes down again. For what makes an assignment complete, read [The assignment](../about/the-assignment.md).

## The command

```
/forge assignment my-project
```

The slug is optional. Without it, Claude resolves the project itself. Replace `my-project` with the slug of your project.

## What happens

Claude first reads the intent and the assignment as it stands. It says whether the intent is ready to be derived from. That statement is advice and never a gate. Then the joint pass runs in three phases.

1. **Questions up front.** Claude asks one question per message, and only about what is yours and the intent does not answer. These are the typical questions:
   - who the recipients are
   - what is delegated and what is specified
   - whether success criteria are present, delegated or deliberately absent
   - what is later

   If the intent answers everything, Claude asks nothing. A question on the detail of the handover is asked here. A question on substance the intent has not settled means the intent is not ready, and the work returns to the intent.

   You should now see either a single question at a time, or none at all.

2. **The recast.** Claude writes the whole draft from the intent. With it comes a provenance map. The map lists each group, its items and the positions of the intent they came from. It also shows the in-scope positions that landed nowhere and the items that have no position behind them (drift). Both of those lists should be empty. The map is a tool of the pass and is not part of the assignment.

   You should now see a full draft and the provenance map beside it.

3. **The walkthrough by group.** One item of the walkthrough is one group of requirements. For each group Claude shows what it covers, which positions it comes from, what in it is delegated or open, and what is optional or later. You give one verdict per group. A question on a single item opens a sub-item, which is closed before the next group. Dozens of items pass in a handful of messages, and the provenance stays visible at each.

   You should now see one group per message, closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

After the pass Claude names what changed. It then offers `/critique essence`, the independent test of drift. It never runs that on its own judgement. See [Critique the documents](critique-the-documents.md) for running the lens. Its findings are settled as an ordinary walkthrough. When the assignment is complete, Claude offers the approval as a recommendation, never as a gate.

## What you have afterwards

- `20-assignment.md`, made from the assignment template, with its history beside it in `20-assignment.history.md`.
- Sections for purpose and context, objective, scope, requirements, constraints, assumptions, deliverables, open questions, success criteria and terms. A section the project has no material for is deleted.
- Requirements in groups, each an item of the Requirement style. The rules of that style are in [Requirement style and Story style](../reference/requirement-style.md).
- A terms section that lists only the prefixes and terms the document actually uses.

From here you can break business requirements out of the assignment ([Write a BRD](write-a-brd.md)). A requirement group that should become a project of its own is handled in [Spin off a group](spin-off-a-group.md).

## If something goes wrong

- **The intent is not ready.** Claude finds a matter of substance the intent has not settled. The work returns to the intent, and you settle it there first. Many questions are a sign of this, never its measure.
- **The intent is silent on something the assignment needs.** Claude raises it as an open question (TBC) and does not fill it by assumption.
- **You want a substance change inside the assignment.** It goes to the intent first. Only wording is fixed in the assignment directly.
- **The map shows an in-scope position that landed nowhere, or an item with no position.** Neither may remain at the end of the pass. Either the item is added or removed, or the intent is changed first.

The reason for these stops is recorded in the definition only as far as stated above. No printed error messages belong to this command.

## A worked example

A generic walkthrough item for one group, here named `Onboarding`, in a project with the slug `my-project`:

```
### Onboarding
Covers: how a new team joins the shared process.
From: three positions of the intent, all in scope.
Delegated: DEL.0010, the team produces its own entry checklist.
Open: TBC.0010 (owner: recipients), who confirms a team is ready.
Optional: REQ.0030, marked optional.
Later: nothing.

Proposition: accept the group as drafted.
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

If you answer `question` about REQ.0030, Claude opens a sub-item on that requirement, closes it, and only then moves to the next group. If you answer `modify` and the change is one of substance, Claude takes it to the intent first.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete.
- [Requirement style and Story style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Write a BRD](write-a-brd.md): the business requirements that may be broken out of the assignment next.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
