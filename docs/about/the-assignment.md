---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 7af576f7bb20535b
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

The assignment is the document that hands the in-scope substance of
an intent to the people who will act on it. This page explains what
makes an assignment complete, where assigning ends and solving
begins, and why the assignment is shaped as it is. It is written for
anyone who uses the forge to hand work over and for anyone who wants
to judge whether the approach holds.

## What it is

The assignment is `20-assignment.md`, a versioned artefact of a
project's chain. It is the distilled handover document for the
recipients (the people the work is handed to). It carries the whole
in-scope substance of the intent to them, complete and precise. Its
aim is that the recipients can act on it without the principal in
the room. The principal is the person whose thinking is being forged
and who has the final word on all content.

The assignment tells the recipients:

- who they are;
- what must be true at the end;
- what is theirs to decide and bring back;
- what they shall not do;
- what the principal has left open on purpose.

It also tells them why the end matters. They should know the end and
the reason well enough to act rightly where the plan no longer fits.

## Who writes and reads it

The principal and Claude write it together. The substance is the
principal's. The wording is Claude's, in the forge's
[Requirement style](../reference/requirement-style.md). Claude does
not fill a gap the intent leaves. It raises the gap as an open
question (a `TBC` item) instead. When the principal wants a change of
substance, Claude proposes it to the intent first, and the
assignment follows from there.

The recipients read it.

## Made from

The assignment is made from three inputs:

- the intent (`10-intent.md`), read together with the project's
  threads, the open matters of the intent;
- the record of the principal's decisions (`decisions.md`);
- the ledger, the single source of truth for the project's state.

The intent is the source. The assignment is derived from it and
never replaces it.

## What it holds

One skeleton serves every assignment (`templates/assignment.md`). Its
sections are these, each deleted where it stays empty:

- Purpose & Context: why the work exists and what the reader needs in
  order to act, as narrative;
- Objective: what must be true at the end, as narrative;
- Scope: what is in scope, and the out-of-scope items (`OOS`);
- Requirements: the requirement items (`REQ`), grouped under plain
  headings;
- Constraints: deliberate boundaries the recipients respect and do
  not challenge (`CON`);
- Assumptions: what the requirements rest on (`ASM`);
- Deliverables: what the recipients bring back, which may include
  specification work handed to them (`DEL`);
- Open Questions: each with an owner (`TBC`);
- Success Criteria: optional (`SCR`);
- Terms: the prefixes and terms actually used in the document.

Narrative stands only in Purpose & Context and in Objective.
Everything else is an item with a stable ID; the page
[Stable IDs](../about/stable-ids.md) explains why every item carries
one. The items follow a few rules:

- each is written with **shall** or **shall not**;
- none carries a priority, because everything is essential by
  default, and an exception carries a note reading *optional*;
- testability is recommended, not required;
- success criteria are wanted, not compulsory;
- an item does not depend on an external link to be understood,
  agreed or later tested.

The full rule set is on the page
[Requirement style](../reference/requirement-style.md). The terms of
the forge, in one line each, are in the
[Glossary](../reference/glossary.md).

### A worked example

A generic requirement item, taken from no project, looks like this:

```
### Ordering
- **REQ.0010** The Service shall confirm every Order to the Customer
  within one working day of its receipt.
- **REQ.0020** The Service shall not ask the Customer for payment
  details before the Order is confirmed. *optional*
```

The item is one idea, in a full sentence, with **shall** or **shall
not**. Order, Service and Customer are capitalised because they are
defined in the Terms section. The second item is not essential, so
it carries the note *optional*; no other item needs a mark. The group
heading `Ordering` has no ID of its own.

## Complete when

The assignment is complete when nothing the recipients would need is
left to assumption. A matter delegated or left open on purpose is
complete. A matter left out in silence is not.

Leaving a matter out is legitimate only as an explicit delegation:

- a `DEL` item, which hands the work to the recipients to do and
  bring back;
- a `TBC` item, which names an open question and its owner.

Nothing is omitted for the sake of brevity. There is no size target
in either direction: the length is whatever fidelity requires.

### Where assigning ends and solving begins

An assignment assigns. It does not solve. What keeps a document an
assignment is the kind of content, never its amount. The defect is
excess of the wrong kind, that is, solving instead of assigning. It
is never length as such.

The machinery of executing delivery belongs to the recipients. Any
apparatus, such as a stakeholder matrix or an impact analysis, may
still appear in an assignment. It belongs there where the principal
judges it part of setting direction.

## How it is found

The assignment is found in a joint pass of the principal and Claude,
in three phases. No new kind of interview is used.

1. Questions up front. Claude asks only what is the principal's and
   the intent does not answer, one question per message. Where the
   intent answers everything, there are no questions. A question on
   substance the intent has not settled means the intent is not
   ready, and the work returns to it.
2. The recast. Claude writes the whole draft from the intent. With
   it, Claude makes a provenance map: each group, its items and the
   positions of the intent they came from. The provenance map also
   lists the in-scope positions that landed nowhere and the items
   with no position behind them. Both lists are meant to be empty.
   The provenance map is a tool of the pass, not part of the
   assignment.
3. The walkthrough by group. A walkthrough is the forge's way of
   working a list of decisions one item per message, each closed
   with a verdict. Here one item of the walkthrough is one group of
   the assignment, with its provenance shown. A question on a single
   item is settled before the walkthrough moves on.

After the pass Claude offers an independent test of drift by a
critic lens, `/critique essence`. It is never run on Claude's own
judgement. The procedure is on the page
[Distil an assignment](../use/distil-an-assignment.md).

## Why

**Why items and not prose.** An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at.

**Why shall and not softer verbs or MoSCoW.** Shall is testable and
binds. The softer verbs (would, could, should, might, may) leave the
recipient to guess what is required. MoSCoW wording puts a priority
where completeness belongs.

**Why no priorities.** Priority tags on items (`critical`,
`important`, `nice-to-have`) were first wanted as an optional
attribute and then dropped. Everything is essential, and an
exception is noted as *optional*.

**Why testability is only recommended.** Assignments are
deliberately high-level. Handing the concretisation to the
recipients through a `DEL` item is a legitimate outcome.

**Why success criteria are not compulsory.** Delegating them to the
recipients as a deliverable ("define success criteria and return")
is a legitimate outcome, not a defect.

**Why a Terms section.** It lets the assignment be forwarded without
oral tradition.

**Why one skeleton.** Separate templates per genre of assignment were
rejected. One universal skeleton with optional sections gives
everything arriving from the principal a consistent shape.

**Why the boundary is a kind and not a list.** A fixed ban on
apparatus such as stakeholder matrices, RACI, impact analyses, MECE
decompositions and tables of contents came from one early case. It
is not a universal rule, so the kind of content decides instead.

**Why no size target.** The goal is to have the assignment right,
not short.

**Why a joint pass of three phases.** Not item by item: most items
are craft derived from the intent, and a verdict on each would be
ceremony. Not by reading the whole draft: without the provenance map
one sees what is there, not what is missing.

**Why the name.** "Mandate" was rejected outright by the principal;
the reason is not recorded. "Charter" carries project-management
ceremony and implies a project, which many assignments are not.
"Assignment" was kept deliberately. It does not preclude further
layers below it.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](../about/stable-ids.md): why every item carries an ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
