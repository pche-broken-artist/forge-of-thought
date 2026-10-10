---
generated: 2026-10-10
made: derived
inputs-hash: c7850657e0f8792f
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - projects/forge/10-intent.md
---

# About the assignment

This page explains what an assignment is in the forge, what it must
carry and why it is written the way it is. It is for the user who
will hand one to recipients and for the evaluator who wants to judge
whether the design holds. It was put together from the assignment's
definition (`.claude/skills/forge/states/assignment.md`), its
template (`templates/assignment.md`) and the forge's own intent
(`projects/forge/10-intent.md`): the definition gives the wording,
the intent gives the reasons and what was rejected on the way.

## What it is

The assignment is the handover document of a project: the file
`20-assignment.md`, the layer directly below the intent. It carries
the in-scope substance of the intent to the recipients, complete and
precise, so that they can act on it without the principal in the
room. Reading it, the recipients know who they are, what must be
true at the end, what is theirs to decide and bring back, what they
shall not do, and what the principal has left open on purpose.

The deeper aim is that they can act rightly where the plan no longer
fits. An assignment that only lists tasks fails the moment reality
departs from it; one that says what must be true at the end, and
why, lets the recipients choose well on their own. That is what the
forge asks of it.

## What complete means

Complete means nothing the recipients would need is left to
assumption. The distinction the forge draws is between delegated and
silent: a matter handed over expressly (as a deliverable the
recipients bring back, or as an open question with an owner) is
complete; a matter simply not mentioned is not. A silent omission is
a defect. Leaving something out is legitimate only as an explicit
delegation.

There is no size target in either direction. Nothing is omitted for
brevity's sake, and length is whatever fidelity requires. The forge
once had size targets for the assignment and dropped them: the goal
is to have it right, not short. The defect an assignment can have is
excess of the wrong kind, never length as such.

## Assigning, not solving

An assignment assigns; it does not solve. What keeps a document an
assignment is the kind of content in it, never its amount. The
machinery of executing delivery belongs to the recipients.

The forge once enumerated a ban on particular apparatus (stakeholder
matrices, impact analyses and the like), and later withdrew it as a
universal rule: that ban had come from one early case. Any such
apparatus may appear in an assignment where the principal judges it
part of setting direction; it is the recipients' machinery only when
it belongs to executing delivery. The line is drawn by judgement
about the content, not by a list of forbidden forms.

## How it is written

An assignment is structured items with stable IDs, even at very high
abstraction. Narrative is confined to two sections, Purpose & Context
and Objective; everything else is an item. The reason is practical:
an item with a stable ID can be cited, reviewed, traced into the
layer below and changed one at a time; prose cannot be pointed at.
The IDs are global and stable, never renumbered, so an item keeps its
address even when it moves between groups. Groups are plain headings
with no IDs and no lifecycle of their own.

Requirements are written as shall and shall not, in full, correct
sentences, one idea per item, each written once. The softer verbs
(would, could, should, might, may) and MoSCoW wording are not used.
The reason: shall is testable and binds; the softer verbs leave the
recipient to guess what is required, and MoSCoW puts a priority
where completeness belongs.

There are no priorities and no priority column. Everything in an
assignment is essential; an exception carries a note reading
*optional* on that item. Priority tags such as critical, important
and nice-to-have were wanted at first as an optional attribute and
were dropped in favour of the convention that everything is
essential and exceptions are noted.

Testability is recommended, not required. Assignments are
deliberately high-level, and delegating concretisation to the
recipients through a deliverable item is a legitimate outcome, not
a shortcoming.

Success criteria are wanted but not compulsory. They may be present,
delegated to the recipients as a deliverable ("define success
criteria and return"), or deliberately absent; the second and third
are not defects.

Every assignment carries a Terms section, so it can be forwarded
without oral tradition. Defined terms are capitalised in item text to
signal that they appear there. For the same reason an item must not
depend on an external link to be understood, agreed or later tested:
the document has to stand on its own wherever it ends up.

Negative mandates, what is out of scope and what the recipients
shall not do, rank equally with positive ones.

One skeleton serves every assignment. Separate templates per genre
of assignment were considered and rejected in favour of one
universal skeleton with optional sections, so that everything
arriving from the principal has a consistent shape. The sections
the skeleton offers are Purpose & Context, Objective, Scope,
Requirements, Constraints, Assumptions, Deliverables, Open
Questions, Success Criteria and Terms; empty sections are deleted
rather than left standing. The full rule set is in
[Requirement style](../reference/requirement-style.md).

## How it is found

The assignment is distilled from the intent, which is read with the
project's threads and decisions. Claude reads the intent against what
the assignment needs: recipients, objective, delegation, success
criteria, horizon. What the intent is silent on he raises as an open
question rather than filling it; a change of substance he proposes to
the intent first, since substance lives in the intent and propagates
down. The wording is Claude's, the substance the principal's.

The work runs as a joint pass of three phases, with no new kind of
interview:

1. Questions up front, one per message, only for what is the
   principal's and the intent does not answer: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, what is
   later. Where the intent answers everything there are none. A
   question on substance the intent has not settled is a sign that
   the intent is not ready, and the work returns to it.
2. The recast: Claude writes the whole draft from the intent, and
   with it a provenance map that shows each group, its items and
   the positions of the intent they came from, together with the
   in-scope positions that landed nowhere and the items with no
   position behind them. Both lists are meant to be empty. The map
   is a tool of the pass, not part of the assignment.
3. The walkthrough by group: one item of the walkthrough is one
   group of the assignment, what it covers, from which positions,
   what in it is delegated or open, what is optional or later. A
   verdict falls per group; a question on a single item opens a
   sub-item and closes it before moving on. After the pass, an
   independent critique for drift is offered.

Two alternatives were considered and set aside. Why not item by
item: most items are craft derived from the intent, and a verdict on
each is ceremony. Why not simply read the whole: without the map one
sees what is there, not what is missing. The procedure, step by
step, is [Distil an assignment](../use/distil-an-assignment.md).

## Why the name

"Assignment" was kept deliberately. "Mandate" was rejected outright
by the principal; "charter" carries project-management ceremony and
implies a project, which many assignments are not. The name does not
preclude further layers below the assignment: a project takes the
layers it needs, and the assignment is one of them, not the last by
definition.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
