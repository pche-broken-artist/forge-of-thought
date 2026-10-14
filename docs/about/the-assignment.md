---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 47ce455f6effa37d
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

The assignment is the artefact that carries the in-scope substance
of the intent to the recipients, complete and precise, so that they
can act on it without the principal in the room. This page says what
an assignment is, what makes it complete, where assigning ends and
solving begins, and why its items are shaped as they are. It is
written for the person whose thinking is forged (the principal) and
for anyone who wants to judge whether an assignment of the forge is a
good one.

## What it is

An assignment is the handover document of a project: the file
`20-assignment.md`, the layer directly below the intent. It is
distilled from the intent, structured in items with stable IDs,
self-contained and versioned. Its audience is the recipients: the
people or teams who will act on it.

An assignment assigns; it does not solve. It says who the recipients
are, what must be true at the end, what is theirs to decide and
bring back, what they shall not do, and what the principal has left
open on purpose. The machinery of executing delivery belongs to the
recipients.

The name "assignment" was kept deliberately. It does not preclude
further layers below it.

## Who writes and reads it

The principal composes it with Claude. The wording is Claude's, in
the Requirement style; the substance is the principal's. Claude
reads the intent against what the assignment needs (recipients,
objective, delegation, success criteria, horizon) and takes the
principal through a joint pass. What the intent is silent on, Claude
raises as an open question rather than filling it. A change of
substance that Claude sees a need for it proposes to the intent
first.

The recipients read it. They are meant to read it without the
principal in the room, which is why the assignment carries its own
Terms section and why no item may depend on an external link to be
understood, agreed or later tested.

## Made from

The assignment is made from the intent (`10-intent.md`), read
together with the project's open threads (`threads.md`), from the
decisions record (`decisions.md`) and from the ledger, the project's
single source of state. The first draft is created from
`templates/assignment.md`, with its history companion
`20-assignment.history.md` created from `templates/history.md`.

The definition that owns the assignment is
`.claude/skills/forge/states/assignment.md`. It is worked through
`/forge assignment`.

## What it holds

The template gives the assignment one shape, the same for every
genre of assignment. Narrative is confined to two sections, Purpose
& Context and Objective. Everything else is items with stable IDs,
grouped under plain headings:

- requirements (`REQ`), the heart of the assignment, grouped when
  clusters emerge;
- out of scope (`OOS`), what the recipients shall not do; a negative
  mandate ranks equally with a positive one;
- constraints (`CON`), deliberate boundaries that are respected, not
  challenged;
- assumptions (`ASM`), what the requirements rest on;
- deliverables (`DEL`), what the recipients bring back, which may
  delegate specification work;
- open questions (`TBC`), each with an owner; a question owned by
  the recipients is part of the assignment, they decide and report
  back;
- success criteria (`SCR`), optional;
- a Terms section, listing only the prefixes and terms the document
  actually uses, with defined Terms capitalised in item text.

Empty sections are deleted. The horizon of the assignment is a
boundary: what is assigned now and what is expressly later, without
the reasons, which stay in the intent. "Later" is not out of scope:
out of scope is never done, later is done, only not now.

Every item is written with **shall** or **shall not**, covers one
idea, is written once, and is a full, correct sentence. There is no
priority column and no priority tag: everything in an assignment is
essential, and an exception carries a note reading *optional*.
Testability is recommended, not required. Success criteria are
wanted, not compulsory. The rule set in full is
[Requirement style](../reference/requirement-style.md); why every
item carries an ID is [Stable IDs](stable-ids.md).

A generic requirement item, in the shape the template defines, looks
like this:

```
### Intake

- **REQ.0010** The Intake Service shall accept a Request in the
  formats listed in the Terms section and shall reject any other
  format with a message that names the format received.
- **REQ.0020** The Intake Service shall record every accepted
  Request with the time of receipt. *optional*
```

"Intake" is a group: a plain heading with no ID. "Intake Service"
and "Request" are capitalised because they are defined in the Terms
section. The note *optional* is the only priority an item ever
carries.

## Complete when

An assignment is complete when nothing the recipients would need is
left to assumption. Delegated or open on purpose is complete; silent
is not. Leaving a matter out is legitimate only as an explicit
delegation: a deliverable (`DEL`) or an open question (`TBC`). A
silent omission is a defect.

It is also complete only when the recipients know what must be true
at the end, and why, well enough to act rightly where the plan no
longer fits.

Nothing is omitted for brevity's sake. There is no size target in
either direction: length is whatever fidelity requires. The defect
is excess of the wrong kind, solving instead of assigning, never
length as such. The boundary is the kind of content, not its amount.
Any apparatus (a stakeholder matrix, an impact analysis) may appear
where the principal judges it part of setting direction; it is the
recipients' machinery only when it belongs to executing delivery.

When completion is reached, Claude offers the approval as a
recommendation, never as a gate.

## How it is found

The assignment is found in a joint pass of three phases, with no new
kind of interview; the procedure, step by step, is
[Distil an assignment](../use/distil-an-assignment.md).

1. Questions up front, one per message, only for what is the
   principal's and the intent does not answer: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, what is
   later. Where the intent answers everything, there are none. A
   question on substance the intent has not settled means the
   intent is not ready, and the work returns to it.
2. The recast: Claude writes the whole draft from the intent, and
   with it a provenance map. The provenance map shows, group by
   group, which items came from which positions of the intent, plus
   the in-scope positions that landed nowhere and the items with no
   position behind them; both lists are meant to be empty. The map
   is a tool of the pass, not part of the assignment.
3. The walkthrough by group. A walkthrough is the forge's way of
   working a list one item per message, each closed with a verdict
   (see [Glossary](../reference/glossary.md)). Here one item of the
   walkthrough is one group of the assignment: what it covers, from
   which positions, what in it is delegated or open, what is
   optional or later. A question on a single item opens a sub-item
   and closes it before moving on.

Before the recast and at the end of the pass, Claude walks the
definition's Map: the recipients, the objective, the cut, the line
between assigning and solving, the boundaries, success, and
self-containment. An area may stay empty when it was considered and
found not to apply.

The pass runs whole where no assignment exists yet. Where an
assignment stands and the intent has moved, the pass runs on what
changed, the provenance map showing what the change touched. A
wording fix is made in the assignment directly. A substance change
asked for in the assignment goes to the intent first.

After the pass, Claude offers `/critique essence` as the independent
test of drift. It is never run on Claude's own judgement, and its
findings are settled in an ordinary walkthrough.

## Why

**Why complete, and why silent omission is a defect.** Because the
recipients act without the principal in the room. What they would
need and do not find, they fill by assumption, and the assignment
then no longer says what the principal meant. A delegation or an
open question with an owner is visible and is theirs to settle; a
silence is not.

**Why no size target.** Because the goal is to have it right, not
short. Length is whatever fidelity requires, and the only excess
that counts is solving where assigning was wanted.

**Why the kind of content, not its amount, is the boundary.** The
forge once banned a list of apparatus (stakeholder matrices, RACI,
impact analyses, MECE decompositions, tables of contents) from the
assignment. That ban came from one early case and is not a universal
rule. The same apparatus is setting direction in one project and
executing delivery in another, so the principal judges, project by
project, what belongs.

**Why items with stable IDs rather than prose.** Because an item
with a stable ID can be cited, reviewed, traced into the layer below
and changed one at a time. Prose cannot be pointed at.

**Why shall and shall not, and not MoSCoW.** Because shall is
testable and binds. The softer verbs (would, could, should, might,
may) leave the recipient to guess what is required. MoSCoW puts a
priority where completeness belongs.

**Why no priorities.** Priority tags on items (critical, important,
nice-to-have) were once wanted as an optional attribute. They were
dropped in favour of the convention of the BRD standard the forge is
aligned with: everything is essential, and an exception is noted as
*optional*.

**Why testability is recommended, not required.** Because
assignments are deliberately high-level. Delegating concretisation
to the recipients through a deliverable is a legitimate outcome.

**Why success criteria are wanted but not compulsory.** Because
delegating them to the recipients as a deliverable ("define success
criteria and return") is a legitimate outcome, not a defect.

**Why a Terms section and no dependence on external links.** So that
the assignment can be forwarded without oral tradition, and so that
an item can be understood, agreed and later tested on its own.

**Why one template for every genre of assignment.** Separate
templates per genre were rejected in favour of one universal
skeleton with optional sections, so that everything arriving from
the principal has a consistent shape.

**Why a joint pass of three phases.** Why not item by item: most
items are craft derived from the intent, and a verdict on each is
ceremony. Why not "read the whole": without the provenance map one
sees what is there, not what is missing. The walkthrough by group
lets dozens of items pass in a handful of messages with nothing
skipped and the provenance visible at each. The reason for using no
new kind of interview is not recorded beyond that the walkthrough
already exists.

**Why the name.** "Mandate" and "charter" were rejected as the name
of the handover document. Mandate was rejected outright by the
principal; the reason is not recorded. Charter carries
project-management ceremony and implies a project, which many
assignments are not. "Assignment" was retained.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
