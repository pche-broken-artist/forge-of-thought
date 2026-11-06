---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: f1ce4728ef452a29
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

The assignment is the artefact of the chain that carries the in-scope
substance of the intent to the recipients, complete and precise, so
that they can act on it without the principal in the room. This page
says what the assignment is, what makes it complete, where assigning
ends and solving begins, and why it is shaped as it is. It is written
for the user who makes one with Claude and for the evaluator who
judges whether one is sound.

## What it is

The assignment is the handover document of a project, the file
`20-assignment.md`. It is complete, precise, structured,
self-contained and versioned. It stands one layer below the
[intent](../reference/glossary.md), the trunk of the chain where the
principal (the person whose thinking is being forged) holds his
positions. The assignment restates the in-scope substance of those
positions as instructions the recipients can act on: who they are,
what must be true at the end, what is theirs to decide and bring
back, what they shall not do, and what the principal has left open on
purpose.

The assignment assigns and does not solve. What keeps a document an
assignment is the kind of content it carries, never its amount. The
machinery of executing delivery belongs to the recipients. Any
apparatus of analysis, such as a stakeholder matrix or an impact
analysis, may still appear where the principal judges it part of
setting direction. There is no list of forbidden apparatus.

The assignment is defined in `.claude/skills/forge/states/assignment.md`
and worked through `/forge assignment`. Its shape is the template
`templates/assignment.md`.

## Who writes and reads it

The principal writes it with Claude. The wording is Claude's, in the
[Requirement style](../reference/requirement-style.md); the substance
is the principal's. Where the intent is silent on something the
recipients would need, Claude raises it as an open question (a `TBC`
item) rather than filling the gap. Where the assignment would need a
change of substance, Claude proposes the change to the intent first,
and the assignment follows. When the assignment reaches completion,
Claude offers the approval as a recommendation, never as a gate.

The assignment is read by the recipients. Its front-matter names them
as its audience. They are expected to read it without the principal
in the room and without oral tradition, which is why every assignment
carries a Terms section.

## Made from

The assignment is made from the intent, read together with the
project's threads (the open matters of the intent, one file each),
from the decisions of the project, and from the ledger (the project's
state report, made at read time). Most of what it needs is in the
intent. The rest is found by asking the principal.

## What it holds

The assignment follows one universal skeleton with optional sections.
Its sections, in the order of the template, are these:

- Purpose & Context: why the assignment exists and what the reader
  needs in order to act, in a few paragraphs of narrative
- Objective: what must be true at the end, in a few sentences
- Scope: what is in scope, in plain text, and what is out of scope,
  as items
- Requirements: the items, grouped under plain headings when
  clusters emerge
- Constraints: the deliberate boundaries the recipients respect and
  do not challenge
- Assumptions: what the requirements rest on and what must stay true
- Deliverables: what the recipients bring back and when, including
  specification work delegated to them
- Open Questions: each with an owner; a question owned by the
  recipients is part of the assignment, since they decide and report
  back
- Success Criteria: optional; may be absent or delegated
- Terms: the prefixes and the defined terms actually used

Narrative is confined to Purpose & Context and Objective. Everything
else is written as items with stable IDs, one idea per item, each
written once, in full and correct sentences. Why every item carries
an ID is the matter of [Stable IDs](../about/stable-ids.md). The
prefixes of the assignment are `REQ` for a requirement, `OOS` for
what is out of scope, `CON` for a constraint, `ASM` for an
assumption, `DEL` for a deliverable, `TBC` for an open question and
`SCR` for a success criterion. Negative mandates (out of scope,
do-not) rank equally with positive ones.

Items are written with shall and shall not. They carry no priorities
and no priority column: everything in an assignment is essential, and
an exception carries a note reading *optional*. Testability is
recommended, not required. Success criteria are wanted, not
compulsory; delegating them to the recipients as a deliverable is a
legitimate outcome, not a defect. A defined term is capitalised in
item text to signal that it appears in the Terms section. The rule
set in full is the [Requirement style](../reference/requirement-style.md).

Empty sections are deleted. The Terms section lists only the prefixes
and terms the document actually uses. The history of the assignment
lives in its companion `20-assignment.history.md`, never in the body.

## Complete when

The assignment is complete when nothing the recipients would need is
left to assumption. Delegated or open on purpose is complete; silent
is not. It is complete, too, when the recipients know what must be
true at the end, and why, well enough to act rightly where the plan
no longer fits.

Nothing is omitted for the sake of brevity. A silent omission is a
defect. Leaving a matter out is legitimate only as an explicit
delegation, that is, a `DEL` or a `TBC` item. There is no size target
in either direction: length is whatever fidelity requires. The defect
an assignment can have is excess of the wrong kind, solving instead
of assigning, never length as such.

## How it is found

The assignment is found in a joint pass of three phases and no new
kind of interview:

1. Questions up front, one per message, only for what is the
   principal's and the intent does not answer: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, what is
   later. Where the intent answers everything, there are none.
2. The recast: Claude writes the whole draft from the intent, and
   with it a provenance map, which lists for each group the items
   and the positions they came from, the in-scope positions that
   landed nowhere, and the items with no position behind them. Both
   of the last two are to be empty. The provenance map is a tool of
   the pass, not part of the assignment.
3. A walkthrough by group. A walkthrough is the method by which a
   list of items is worked one item per message, each closed with a
   verdict. Here one item of the walkthrough is one group of the
   assignment: what it covers, from which positions, what in it is
   delegated or open, what is optional or later. Dozens of items
   pass in a handful of messages and nothing is skipped.

A question up front on the detail of the handover is answered in the
pass. A question on substance the intent has not settled means the
intent is not ready, and the work returns to the intent. Many such
questions are evidence of that, never its measure.

Before the recast and again at the end of the pass, Claude walks the
areas an assignment needs: the recipients, the objective, the cut
between now, later and out of scope, the line between assigning and
solving, the boundaries, success, and self-containment. An area may
stay empty when it was considered and found not to apply.

The pass runs whole where no assignment exists yet. Where an
assignment stands and the intent has moved, the pass runs on what
changed, the provenance map showing what the change touched. A
wording fix is made in the assignment directly. After the pass,
Claude offers `/critique essence` as the independent test of drift
between the intent and the assignment; it never runs it on its own
judgement. The pass as a procedure, step by step, is
[Distil an assignment](../use/distil-an-assignment.md).

## Why

**Why complete and self-contained.** The recipients act without the
principal in the room. What the assignment leaves to assumption, they
guess. What it tells them about the end and the reason lets them act
rightly where the plan no longer fits. The size targets were dropped
because the goal is to have the assignment right, not short.

**Why items with stable IDs rather than prose.** An item with a
stable ID can be cited, reviewed, traced into the layer below and
changed one at a time. Prose cannot be pointed at. This holds even at
very high abstraction.

**Why shall and not MoSCoW.** Shall is testable and binds. The softer
verbs, would, could, should, might and may, leave the recipient to
guess what is required. MoSCoW puts a priority where completeness
belongs. Priority tags on items were considered as an optional
attribute and dropped: everything in an assignment is essential, and
the exceptions are noted as *optional*.

**Why testability is recommended, not required.** Assignments are
deliberately high-level. Delegating concretisation to the recipients
through a `DEL` item is a legitimate outcome.

**Why one skeleton.** Separate templates per genre of assignment were
rejected in favour of one universal skeleton with optional sections,
so that everything arriving from the principal has a consistent
shape.

**Why a Terms section.** So that the assignment can be forwarded
without oral tradition.

**Why a joint pass of three phases.** Why not item by item: most
items are craft derived from the intent, and a verdict on each is
ceremony. Why not "read the whole": without the provenance map one
sees what is there, not what is missing.

**Why the name.** "Mandate" was rejected outright by the principal;
the reason is not recorded. "Charter" carries project-management
ceremony and implies a project, which many assignments are not.
"Assignment" was kept deliberately, and the name does not preclude
further layers below it.

## A worked example

A generic group of a Requirements section, taken from no project,
shows the shape of an item:

```
### Intake
- **REQ.0010** The Intake Register shall record every request with
  its requester, its date of arrival and its Service Line before any
  work on the request begins.
- **REQ.0020** The Intake Register shall not accept a request without
  a named requester.
- **DEL.0010** The recipients shall define the fields of the Intake
  Register beyond those named in REQ.0010 and return them with the
  first design.
```

Each item is one idea in one full sentence, written with shall or
shall not. It carries an ID that is cited, not renumbered. It carries
no priority; all three are essential. "Intake Register" and "Service
Line" are capitalised because they are defined in the Terms section
of the same document. The first two items are testable; the third
delegates concretisation to the recipients, which is complete, since
nothing is left silent.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](../about/stable-ids.md): why every item carries an ID.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
