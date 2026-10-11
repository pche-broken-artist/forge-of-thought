---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 2f69d902c779efb6
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
---

# Distil an assignment

`/forge assignment [slug]` derives the assignment, the file `20-assignment.md`, from the intent. This page is for the user who has an intent and wants to carry its in-scope substance to the recipients, who are the teams, colleagues or future self that will act on it. The principal is the person whose thinking is being forged and who has the final word on all content.

## When to use it

- You have no assignment yet and the intent is ready to be derived from.
- An assignment stands and the intent has moved since.
- You want a wording fix in an assignment that stands.

## The command

```
/forge assignment [slug]
```

The slug names the project. Where it is left out, Claude resolves the project itself. Claude is the assistant that runs the command.

## What happens

Claude reads the intent and the assignment as it stands. It says whether the intent is ready to be derived from. That is a remark and never a gate. The pass then runs in three phases.

1. **Questions up front.** Claude asks one question per message. It asks only what is yours and the intent does not answer:
   - who the recipients are
   - what is delegated and what is specified
   - whether success criteria are present, delegated or deliberately absent
   - what is left for later

   Where the intent answers everything, Claude asks nothing. A question about the detail of the handover is asked here. A question about substance that the intent has not settled means the intent is not ready, and the work returns to the intent. You should now see a short run of single questions, or none.

2. **The recast.** Claude writes the whole draft from the intent. With it comes a provenance map, which lists:
   - each group of the draft
   - its items
   - the positions of the intent each item came from
   - the in-scope positions that landed nowhere, which should be none
   - the items that came from no position, which are drift and should be none

   The provenance map is a tool of the pass and is not part of the assignment. You should now see the whole draft and the provenance map beside it.

3. **The walkthrough by group.** A walkthrough is a list worked one item per message, each closed with the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`. Here one item is one group of requirements. Claude says what the group covers, from which positions it comes, what in it is a deliverable or an open question, and what is optional or later. You give one verdict per group. A question on a single item opens a sub-item and is closed before the next group. You should now see one group per message, with its provenance visible, until every group has its verdict.

The first draft is made from `templates/assignment.md`. Its history companion `20-assignment.history.md` is made with it. The draft has these sections, and empty ones are left out:

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

The Terms section lists only the prefixes and terms the assignment uses.

### Where a change goes

- A substance change that you ask for in the assignment goes to the intent first. The assignment follows from there.
- A wording fix is made in the assignment directly.
- Where the intent is silent, Claude raises the matter as an open question and does not fill it in. The wording of the items is Claude's. The substance is yours.

The items are written in the Requirement style: "shall" and "shall not", with no priorities. The rules are on [Requirement style](../reference/requirement-style.md).

## What you have afterwards

- `20-assignment.md` and its history companion, written once at the end of the round on your word.
- Claude names what changed.
- When the assignment is complete, Claude offers `/critique essence` as the independent test of drift. It is offered and never run on Claude's own judgement. Its findings are worked as an ordinary walkthrough. How it is run is on [Critique the documents](critique-the-documents.md).
- After that Claude offers the approval. It is a recommendation and never a gate.

## If something goes wrong

- The intent is not ready: Claude says so and the work returns to the intent. Many questions in phase one are evidence of that, never its measure.
- The assignment would need a substance change: it is made in the intent first and then carried down.
- A group has grown into something that should stand alone: it becomes a project of its own only on your decision. See [Spin off a group](spin-off-a-group.md).

## A worked example

This is one walkthrough item as Claude shows it. The group and its content are generic.

```
### Reporting

Covers: how the recipients report progress back to you.
From: two positions of the intent, one on cadence and one on form.
In it:
  - two requirement items (cadence, form)
  - one deliverable: a first report by the end of the first phase
  - one open question, owned by the recipients: the channel
Optional: the form of the report, marked optional on that item.
Later: dashboards, expressly out for this assignment.

(a)ccept / (m)odify / (r)eject / (p)ark
```

You answer `a`, or `m` with what to change, and Claude moves to the next group. Nothing in the group is skipped, and each verdict is carried to the one write at the end.

## See also

- [The assignment](../about/the-assignment.md): what makes an assignment complete and where assigning ends.
- [Requirement style](../reference/requirement-style.md): the rule set of the items.
- [Critique the documents](critique-the-documents.md): running the essence lens.
- [Spin off a group](spin-off-a-group.md): a requirement group that becomes a project of its own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
