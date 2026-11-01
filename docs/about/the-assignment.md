---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: e8337c45940cc76a
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
the intent to the people who will act on it, complete and precise.
This page explains what makes an assignment complete, where
assigning ends and solving begins, how its items are written and why
it is found the way it is. It is for anyone who works with an
assignment and for anyone weighing how the forge hands work over.

## What it is

The assignment is the file `20-assignment.md` of a project. It is the
distilled handover document for the recipients (the teams,
colleagues or future self who receive the work). It carries the
whole in-scope substance of the intent (the document of the
principal's positions; the principal is the person whose thinking is
being forged). It is complete, precise, structured, self-contained
and versioned.

The assignment assigns. It does not solve. The recipients are to be
able to act on it without the principal in the room. They are to
know what must be true at the end, and why, well enough to act
rightly where the plan no longer fits.

## Who writes and reads it

The principal and Claude write it together. The wording is Claude's,
in the requirement style. The substance is the principal's. Where the
intent is silent, Claude raises an open question rather than filling
the gap. A change of substance asked for in the assignment goes to
the intent first, and the assignment follows it. A change of wording
only is made in the assignment directly.

The recipients read it. Its front-matter names them as its audience.

## Made from

The assignment is made from three inputs:

- the intent, read together with the project's threads (its open
  matters);
- `decisions.md`, the principal's decisions with their reasons;
- the ledger (the project's state report, built by a script from the
  documents).

Its shape comes from the template `templates/assignment.md`. Its
history lives in a companion file beside it,
`20-assignment.history.md`, never in its body.

## What it holds

The template gives one skeleton with these sections:

- **Purpose & Context**: why the assignment exists and what the
  reader needs in order to act, in narrative.
- **Objective**: what must be true at the end, in narrative.
- **Scope**: what is in scope, and the out-of-scope items (`OOS`).
- **Requirements**: the requirement items (`REQ`), grouped under
  plain headings when clusters emerge.
- **Constraints**: deliberate boundaries the recipients respect and
  do not challenge (`CON`).
- **Assumptions**: what the requirements rest on and what must stay
  true (`ASM`).
- **Deliverables**: what the recipients bring back, which may
  delegate specification work (`DEL`).
- **Open Questions**: each with an owner (`TBC`). A question the
  recipients own is part of the assignment: they decide and report
  back.
- **Success Criteria**: optional, and may be absent or delegated
  through a deliverable (`SCR`).
- **Terms**: the prefixes and the terms the document actually uses.

Sections left empty are deleted. Narrative is confined to Purpose &
Context and Objective. Everything else is an item with a stable ID
(see [Stable IDs](stable-ids.md)).

Each item is written with **shall** or **shall not**. No item carries
a priority. Everything in an assignment is essential by default. An
exception is marked by a note reading *optional* on that item. Each
item covers one idea in full, correct sentences. An item is
understood without following an external link. Defined terms are
capitalised in item text, because they appear in the Terms section.

Testability is recommended, not required. Assignments are
deliberately high-level. Delegating the concrete detail through a
deliverable is a legitimate outcome. Success criteria are likewise
wanted but not compulsory: they may be present, delegated, or
deliberately absent. A missing section of that kind may be a
deliberate delegation to the recipients, not a defect.

The full rule set is on [Requirement style](../reference/requirement-style.md).
Every prefix and term is in one line on the [Glossary](../reference/glossary.md).

## Complete when

An assignment is complete when nothing the recipients would need is
left to assumption. A matter delegated or left open on purpose is
complete. A matter left out in silence is not. The recipients must
also know what must be true at the end, and why.

Nothing is left out for brevity's sake. There is no size target in
either direction. Length is whatever fidelity requires. Leaving a
matter out is legitimate only as an explicit delegation, that is a
deliverable item or an open question.

The boundary between assigning and solving is the kind of content,
never its amount. The machinery of executing delivery belongs to the
recipients. Any apparatus, such as a stakeholder matrix or an impact
analysis, may still appear where the principal judges it part of
setting direction. The defect is excess of the wrong kind (solving
instead of assigning), never length as such.

When this completeness is reached, Claude offers the approval. The
offer is a recommendation, never a gate.

## How it is found

The assignment is found in a joint pass of three phases. The pass
uses no new kind of interview. How you run it is on
[Distil an assignment](../use/distil-an-assignment.md).

1. **Questions up front.** Claude asks, one per message, only what
   belongs to the principal and the intent does not answer: who the
   recipients are, what is delegated and what specified, whether
   success criteria are present, and what is later. Where the intent
   answers everything, there are no questions. A question on
   substance the intent has not settled means the intent is not
   ready, and the work returns to it.
2. **The recast.** Claude writes the whole draft from the intent.
   With it comes a provenance map: each group, its items, and the
   positions they came from. The provenance map also lists the
   in-scope positions that landed nowhere and the items with no
   position behind them. Both lists are to be empty. The provenance
   map is a tool of the pass, not part of the assignment.
3. **The walkthrough by group.** A walkthrough is the forge's way of
   taking the principal through a list one item per message, each
   closed with a verdict. Here one item of the walkthrough is one
   group of the assignment: what it covers, from which positions,
   what in it is delegated or open, what is optional or later. A
   question on a single item opens a sub-item that is closed before
   the walkthrough moves on. After the pass, Claude offers an
   independent critique for drift (`/critique essence`).

Where an assignment already stands and the intent has moved, the
pass runs on what changed. The provenance map then shows what the
change touched.

## Why

**Why items with stable IDs.** An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at.

**Why a Terms section.** It lets the assignment be forwarded without
oral tradition.

**Why shall and no priorities.** Priority tags on items were once
wanted as an optional attribute. They were dropped in favour of a
convention where everything is essential and exceptions are noted as
*optional*. MoSCoW wording and the softer verbs (would, could,
should, might, may) are excluded with them. Why "shall" was chosen
over another verb of obligation is not recorded.

**Why one skeleton.** Separate templates per genre of assignment were
rejected. One universal skeleton with optional sections gives
everything that arrives from the principal a consistent shape.

**Why a joint pass of three phases.** Item by item was rejected
because most items are craft derived from the intent, and a verdict
on each is ceremony. Simply reading the whole was rejected because
without the provenance map one sees what is there, not what is
missing. The questions up front keep the principal's time for what
only the principal can answer.

**Why the name.** "Assignment" was kept deliberately. It does not
preclude further layers below it. "Charter" was rejected because it
carries project-management ceremony and implies a project, which
many assignments are not. "Mandate" was rejected outright by the
principal; the reason is not recorded.

## A worked example

A generic requirement group, as the template shapes it, with an
optional item and a delegation beside it:

```markdown
### Reporting
- **REQ.0010** Every Recipient shall receive the Monthly Report
  within five working days of the close of the month.
- **REQ.0020** The Monthly Report shall not contain personal data
  of any Customer.
- **REQ.0030** The Monthly Report shall be available in a printable
  form. *optional*

## Deliverables
- **DEL.0010** The recipients shall propose the measures the
  Monthly Report carries and return them for agreement.
```

Each item states one idea with "shall" or "shall not". `Recipient`,
`Monthly Report` and `Customer` are capitalised because the Terms
section defines them. No item carries a priority. The third item is
marked *optional* as the one exception. The choice of measures is
left to the recipients through a deliverable, so the assignment
stays complete without solving it.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
