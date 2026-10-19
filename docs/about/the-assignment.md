---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: f5b2095a96d600da
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - projects/forge/10-intent.md#POS.0130
  - projects/forge/10-intent.md#Structure and style of an assignment
  - projects/forge/10-intent.md#POS.1350
  - projects/forge/10-intent.md#REJ.0050
  - projects/forge/10-intent.md#REJ.0060
  - projects/forge/10-intent.md#REJ.0120
---

# The assignment

The assignment is the handover document of a project: it carries
what the principal wants to the people who are to act on it. This
page explains what makes an assignment complete, where assigning
ends and solving begins, and why the assignment is written and
found the way it is. It is for anyone who uses the forge to hand
work over, and for anyone weighing whether the forge's handover
holds up.

## What it is

An assignment is an artefact of the chain, the file
`20-assignment.md` of a project. An artefact is one of the
versioned documents the chain is made of (see the
[Glossary](../reference/glossary.md) for every term of the forge in
one line). The assignment carries the in-scope substance of the
intent to the recipients, complete and precise. The intent is the
artefact that holds what the principal (the person whose thinking
is being forged) currently holds and wants. The recipients are
whoever receives the assignment and acts on it.

The assignment is meant to let the recipients act without the
principal in the room. It tells them these things:

- who they are;
- what must be true at the end;
- what is theirs to decide and bring back;
- what they shall not do;
- what the principal has left open on purpose.

The recipients should know the end and its reason well enough to
act rightly where the plan no longer fits.

## Who writes and reads it

The principal and Claude write it together. The substance is the
principal's. The wording is Claude's, in the requirement style
described below. The recipients read it.

Its history is not kept in the body. It lives in a companion file
beside it, `20-assignment.history.md`, which records every change
and why it was made.

## Made from

The assignment is made from the intent, read together with the
project's open threads (the matters of the intent not yet settled).
Claude also reads the project's decisions and its ledger (the file
that holds the state of the project). The shape of the result is
the template `templates/assignment.md`.

A change of substance asked for in the assignment goes to the
intent first, and the assignment follows. Only wording is fixed in
the assignment directly.

## What it holds

One template serves every assignment. Its sections are optional
where they do not apply, and an empty section is deleted. The
sections are these:

- Purpose & Context: why the assignment exists and what the reader
  needs in order to act, in prose.
- Objective: what must be true at the end, in prose.
- Scope: what is in scope, and the out-of-scope items (OOS).
- Requirements: the requirement items (REQ), grouped under plain
  headings where clusters emerge.
- Constraints: deliberate boundaries the recipients respect and do
  not challenge (CON).
- Assumptions: what the requirements rest on and what must stay
  true (ASM).
- Deliverables: what the recipients bring back (DEL); a deliverable
  may delegate specification work to them.
- Open Questions: each with an owner (TBC); a question the
  recipients own is part of the assignment, and they decide it and
  report back.
- Success Criteria: optional; they may be absent or delegated
  through a DEL item (SCR).
- Terms: only the prefixes and terms the document actually uses.

Narrative stands only in Purpose & Context and in Objective.
Everything else is an item with a stable ID, of the form
`PREFIX.NNNN` (see [Stable IDs](../about/stable-ids.md) for why
every item carries one).

The items follow a requirement style. The full rule set is on
[Requirement style](../reference/requirement-style.md). Its main
lines are these:

- Items are written with **shall** and **shall not**.
- Items carry no priorities. Everything is essential, and an
  exception is marked by a note reading *optional* on that item.
- Testability is recommended, not required.
- Success criteria are wanted but not compulsory.
- Defined terms are capitalised in item text, as the sign that they
  stand in the Terms section.
- No item depends on an external link to be understood, agreed or
  later tested.
- Negative mandates (out of scope, do-not) rank equally with
  positive ones.

## Complete when

An assignment is complete when nothing the recipients would need
is left to assumption. A matter delegated or left open on purpose
is complete. A matter passed over in silence is not: a silent
omission is a defect. Leaving a matter out is legitimate only as an
explicit delegation, that is a DEL or a TBC item. The recipients
must also know what must be true at the end, and why.

Nothing is left out for brevity's sake. There is no size target in
either direction, and the length is whatever fidelity requires.

The boundary of an assignment is the kind of content, never its
amount. An assignment assigns and does not solve. The machinery of
executing delivery belongs to the recipients. Any apparatus (a
stakeholder matrix, an impact analysis) may still appear where the
principal judges it part of setting direction. The defect is
content of the wrong kind, solving instead of assigning, and never
length as such.

## How it is found

The assignment is found in a joint pass of three phases. The pass
uses no new kind of interview. The steps of it as a procedure are
on [Distil an assignment](../use/distil-an-assignment.md).

1. Questions up front. Claude asks only what belongs to the
   principal and the intent does not answer, such as who the
   recipients are, what is delegated and what is later. Where the
   intent answers everything, there are no questions. A question
   on substance the intent has not settled means the intent is not
   ready, and the work returns to it.
2. The recast. Claude writes the whole draft from the intent, and
   with it a provenance map. The provenance map lists each group of
   the draft, its items and the positions of the intent they came
   from. It also lists the in-scope positions that landed nowhere
   and the items that came from no position, and both lists are to
   be empty. The provenance map is a tool of the pass, not part of
   the assignment.
3. The walkthrough by group. A walkthrough is the forge's way of
   working a list of items with the principal, one item per
   message, each closed with his verdict. Here one item is one
   group of the draft: what it covers, from which positions, what
   in it is delegated or open, what is optional or later. A
   question on a single item is settled before the walkthrough
   moves on.

After the pass, Claude offers the critic lens `essence` as an
independent test of drift. It never runs it on its own judgement.

## Why

**Why complete and not short.** The goal is to have the assignment
right, not short. The recipients are to act on it without the
principal in the room, and a matter left out in silence is one they
cannot act on.

**Why the boundary is the kind of content.** What keeps a document
an assignment is the kind of content: it assigns and does not
solve. A fixed list of banned apparatus is not a universal rule.
The reason is that such apparatus can be part of setting
direction, and is the recipients' machinery only when it belongs
to executing delivery.

**Why items with stable IDs.** An item with a stable ID can be
cited, reviewed, traced into the layer below and changed one at a
time. Prose cannot be pointed at.

**Why shall, and not MoSCoW.** Shall is testable and binds. The
softer verbs (would, could, should, might, may) leave the recipient
to guess what is required. MoSCoW wording puts a priority where
completeness belongs.

**Why no priorities.** Priority tags on items (`critical`,
`important`, `nice-to-have`) were rejected. In their place the
forge follows a convention of business requirements documents:
everything is essential, and an exception is noted as *optional*.

**Why testability is only recommended.** Assignments are
deliberately high-level. Delegating the concretisation to the
recipients through a DEL item is a legitimate outcome.

**Why success criteria are not compulsory.** Delegating them to the
recipients as a deliverable ("define success criteria and return")
is a legitimate outcome, not a defect.

**Why a Terms section.** Every assignment carries one. With it the
assignment can be forwarded without oral tradition.

**Why one template.** Separate templates per genre of assignment
were rejected. One universal template with optional sections gives
everything arriving from the principal a consistent shape.

**Why a joint pass of three phases.** Two other ways were weighed.
Item by item was set aside because most items are craft derived
from the intent, and a verdict on each is ceremony. Reading the
whole was set aside because without the provenance map one sees
what is there, not what is missing.

**Why the name.** "Mandate" was rejected outright by the principal.
"Charter" carries project-management ceremony and implies a
project, which many assignments are not. "Assignment" was kept
deliberately, and it does not preclude further layers below it.

## A worked example

A requirement item, plainly generic, in the shape the template and
the requirement style give:

```markdown
### Order confirmation
- **REQ.0010** The Service shall send the Customer a confirmation
  of every Order within one working day of its receipt.
- **REQ.0020** The Service shall not ask the Customer for payment
  details in the confirmation.
- **REQ.0030** The Service shall offer the confirmation in the
  Customer's language. *Optional.*

## Deliverables
- **DEL.0010** The recipients shall define the success criteria of
  the order confirmation and return them.
```

Each item covers one idea in full sentences with shall or shall
not. The capitalised words (Service, Customer, Order) would stand
in the Terms section. The third item is the one exception to
"everything is essential", and says so. The deliverable delegates
the success criteria instead of leaving them out in silence.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](../about/stable-ids.md): why every item carries an
  ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
