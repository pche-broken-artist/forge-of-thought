---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 0586feca8ece6eba
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

The assignment is the document of the chain that hands the in-scope
substance of the intent to the people who will act on it. This page
explains what makes an assignment complete, where assigning ends and
solving begins, and why the assignment is shaped as it is. It is
written for anyone who uses the forge to hand work over, and for
anyone weighing whether the way it hands work over is sound.

## What it is

The assignment is the file `20-assignment.md` of a project. It is an
artefact: a versioned document of the chain, composed by the
principal (the person whose thinking is being forged) with Claude.
It sits below the intent, the document that holds what the principal
currently thinks and wants.

The assignment carries the in-scope substance of the intent to the
recipients, complete and precise. Its aim is that the recipients can
act on it without the principal in the room. To do so they need to
know the following:

- who they are;
- what must be true at the end;
- what is theirs to decide and bring back;
- what they shall not do;
- what the principal has left open on purpose.

They also need to know what must be true at the end, and why, well
enough to act rightly where the plan no longer fits.

The assignment assigns. It does not solve.

## Who writes and reads it

The principal owns the substance. Claude owns the wording, which it
writes in the requirement style of the forge. Where the intent is
silent on something the assignment needs, Claude raises it as an
open question instead of filling the gap. A change of substance that
is asked for in the assignment goes to the intent first and comes
down from there. Only wording is fixed in the assignment directly.

The readers are the recipients. They may be teams, colleagues or the
principal's own future self.

## Made from

The assignment is made from the intent, read together with the open
matters that belong to it, the project's decisions and the ledger
(the project's state, made from its documents whenever it is read).
Its shape comes from the template `templates/assignment.md`. Its
history is kept in a companion file beside it,
`20-assignment.history.md`, never in its body.

## What it holds

Narrative is confined to two sections: Purpose & Context, and
Objective. Everything else is items, each with a stable ID of the
form `PREFIX.NNNN` (see [Stable IDs](stable-ids.md)). The template
gives these sections:

- **Purpose & Context:** why the assignment exists and what the
  reader needs in order to act, with no solutioning.
- **Objective:** what must be true at the end.
- **Scope:** what is in scope, as a short list, and what is out of
  scope, as `OOS` items.
- **Requirements:** `REQ` items, grouped under plain headings where
  clusters emerge.
- **Constraints:** `CON` items, deliberate boundaries the recipients
  respect and do not challenge.
- **Assumptions:** `ASM` items, what the requirements rest on and
  what must stay true.
- **Deliverables:** `DEL` items, what the recipients bring back. A
  deliverable may delegate specification work.
- **Open Questions:** `TBC` items, each with an owner. A question
  owned by the recipients is part of the assignment: they decide and
  report back.
- **Success Criteria:** `SCR` items. This section is optional.
- **Terms:** the prefixes and the terms the assignment actually uses.

Empty sections are deleted. There is one template for every kind of
assignment, with optional sections.

The items follow a few principles. The full rule set is on the page
[Requirement style](../reference/requirement-style.md).

- Items are written with **shall** and **shall not**.
- Items carry no priorities. Everything is essential by default, and
  an exception carries a note reading *optional*.
- Testability is recommended, not required.
- Success criteria are wanted but not compulsory. Delegating them to
  the recipients as a deliverable is a legitimate outcome.
- Negative mandates (out of scope, do-not) rank equally with positive
  ones.
- Every assignment carries a Terms section. Defined terms are
  capitalised in item text.
- An item does not depend on an external link to be understood,
  agreed or later tested.

"Later" is not "out of scope". Out of scope is never done. Later is
done, only not now.

## Complete when

An assignment is complete when nothing the recipients would need is
left to assumption. A matter that is delegated, or left open on
purpose, is complete. A matter that is silent is not. A silent
omission is a defect.

Nothing is left out for brevity's sake. Length is whatever fidelity
requires, and there is no size target in either direction. Leaving a
matter out is legitimate only as an explicit delegation: a `DEL` or
a `TBC` item.

The boundary of an assignment is the kind of its content, never its
amount. Assigning stays in the assignment. The machinery of
executing delivery belongs to the recipients. An apparatus such as a
stakeholder matrix or an impact analysis may still appear, where the
principal judges it part of setting direction. The defect is excess
of the wrong kind (solving instead of assigning), never length as
such.

## How it is found

The assignment is found in a joint pass of Claude and the principal.
The pass has three phases and introduces no new kind of interview.
The steps themselves are on the page
[Distil an assignment](../use/distil-an-assignment.md).

1. **Questions up front.** Claude asks only what belongs to the
   principal and is not answered by the intent: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, and what
   is later. Where the intent answers everything, there are no
   questions. A question on substance the intent has not settled
   means the intent is not ready, and the work returns to it.
2. **The recast.** Claude writes the whole draft from the intent.
   With it Claude makes a provenance map: each group, its items, and
   the positions of the intent they came from. The provenance map
   also lists in-scope positions that landed nowhere and items that
   came from no position (drift). Both lists should end up empty.
   The provenance map is a tool of the pass, not part of the
   assignment.
3. **The walkthrough by group.** A walkthrough is the forge's way of
   working a list of decisions with the principal, one item per
   message, each closed with a verdict. Here one item of the
   walkthrough is one group of the assignment: what it covers, from
   which positions, what in it is delegated or open, what is
   optional or later. A question on a single item is settled before
   moving on. After the pass Claude offers an independent review of
   drift by a critic, and the principal decides whether to run it.

When an assignment already stands and the intent has moved, the pass
runs on what changed, and the provenance map shows what the change
touched.

## Why

**Why complete and self-contained.** The recipients act without the
principal in the room. They must know the end and the reason well
enough to act rightly where the plan no longer fits. The Terms
section exists so that the assignment can be forwarded without oral
tradition.

**Why no size target.** The goal is to have the assignment right, not
short. A length limit would push matters out in silence, and a
silent omission is the defect the assignment guards against.

**Why the boundary is the kind of content.** An enumerated ban on
particular apparatus (stakeholder matrices, impact analyses and the
like) came from one early case and is not a universal rule. What
decides is whether a piece of content sets direction or executes
delivery.

**Why items with stable IDs.** An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at.

**Why shall, and not MoSCoW.** Shall is testable and binds. The
softer verbs (would, could, should, might, may) leave the recipient
to guess what is required. MoSCoW wording puts a priority where
completeness belongs.

**Why no priorities.** Priority tags on items (such as critical,
important, nice-to-have) were wanted at first as an optional
attribute. They were dropped in favour of the convention of the group
BRD standard: everything is essential, and an exception is noted as
*optional*.

**Why testability is only recommended.** Assignments are
deliberately high-level. Delegating concretisation to the recipients
through a deliverable is a legitimate outcome.

**Why one template.** Separate templates per genre of assignment were
rejected. One universal skeleton with optional sections gives
everything arriving from the principal a consistent shape.

**Why a joint pass of three phases.** Two other ways were weighed:

- **Item by item:** most items are craft derived from the intent, and
  a verdict on each would be ceremony.
- **Reading the whole draft:** without the provenance map one sees
  what is there, not what is missing.

**Why the name "assignment".** Two other names were weighed:

- **Mandate:** rejected outright by the principal. The reason is not
  recorded.
- **Charter:** it carries project-management ceremony and implies a
  project, which many assignments are not.

The name was kept deliberately. It does not preclude further layers
below the assignment.

## A worked example

A requirement item, generic and taken from no project, in the shape
the template and the requirement style give:

```
### Monthly reporting
- **REQ.0010** The Reporting Service shall deliver the Monthly
  Summary to every Subscriber by the fifth working day of the
  following month.
- **REQ.0020** The Reporting Service shall not send a Monthly
  Summary that contains another Subscriber's data.
- **REQ.0030** The Reporting Service shall offer the Monthly Summary
  as a download in addition to delivery. *optional*
```

Each item covers one idea, in one full sentence, with shall or shall
not. The capitalised words are defined terms that appear in the Terms
section. The third item is the exception to "everything is
essential", so it carries the note *optional*. Where the principal
leaves the delivery format to the recipients, that is said in a `DEL`
or a `TBC` item, not left unsaid.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
