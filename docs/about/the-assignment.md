---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 2860f93a790d9d15
inputs:
  - .claude/skills/forge/states/assignment.md
  - templates/assignment.md
  - projects/forge/10-intent.md#POS.0130
  - projects/forge/10-intent.md#Structure and style of an assignment
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.1350
  - projects/forge/10-intent.md#REJ.0050
  - projects/forge/10-intent.md#REJ.0060
  - projects/forge/10-intent.md#REJ.0120
  - projects/forge/10-intent.md#REJ.0540
---

# The assignment

The assignment is the handover document of a project: it carries the
in-scope substance of the intent to the recipients, complete and
precise, so that they can act on it without the principal (the person
whose thinking is being forged) in the room. This page says what the
assignment is, who writes and reads it, what it is made from and
holds, when it counts as complete, how it is found and why it is
shaped as it is. It is written for the user who will compose one and
for the evaluator who wants to judge whether the forge's handover
holds together.

## What it is

The assignment is the artefact `20-assignment.md`, the layer directly
below the intent. It is a distilled handover: complete, precise,
structured, self-contained and versioned. Its readers are the
recipients, the people or teams who will carry the work out, and it
tells them five things:

- who they are;
- what must be true at the end;
- what is theirs to decide and bring back;
- what they shall not do;
- what the principal has left open on purpose.

An assignment assigns; it does not solve. What keeps a document an
assignment is the kind of content, never its amount. Machinery of
executing delivery belongs to the recipients. Any apparatus, such as
a stakeholder matrix or an impact analysis, may still appear where
the principal judges it part of setting direction. There is no size
target in either direction: length is whatever fidelity requires, and
the defect is excess of the wrong kind, solving instead of assigning,
never length as such.

The name "assignment" was kept deliberately. It does not preclude
further layers below it. Which layers a project takes below the
assignment is the project's own matter.

## Who writes and reads it

The principal composes the assignment with Claude. Claude reads the
intent against what the assignment needs and takes the principal
through a joint pass (How it is found). The wording is Claude's, in
the Requirement style; the substance is the principal's. What the
intent is silent on, Claude raises as an open question rather than
filling it. A change of substance that Claude would make, it proposes
to the intent first.

The recipients read the assignment. Its front-matter names them as
the audience. The document is written so that it can be forwarded
without oral tradition: every term it relies on stands in its own
Terms section.

A critic also reads it: at the end of the joint pass Claude offers
`/critique essence` as the independent test of drift between the
intent and the assignment. The critic is never run on Claude's own
judgement, and its findings are settled in an ordinary walkthrough
(the forge's way of working a list of items one per message, each
closed with a verdict).

## Made from

The assignment is made from three inputs:

- the intent, `10-intent.md`, read together with the project's
  threads in `threads/`, the open matters of the intent;
- `decisions.md`, the principal's decisions with their reasons;
- the ledger, the project's single source of truth for state, made
  at read time by a script.

The first draft is created from the template `templates/assignment.md`,
with its history companion `20-assignment.history.md` created from
`templates/history.md`. The body is the current state; the companion
is the record of every change.

## What it holds

The assignment follows one universal skeleton with optional sections.
Its front-matter carries the version, the status, the project's slug
and the audience, `recipients`. The body has these sections, in this
order:

- **Purpose & Context**: why the assignment exists, what problem or
  opportunity it addresses and what the reader needs in order to act,
  with no solutioning;
- **Objective**: what must be true at the end;
- **Scope**: what is in scope, as plain text, and what is out of scope,
  as `OOS` items;
- **Requirements**: `REQ` items, grouped under plain headings when
  clusters emerge;
- **Constraints**: `CON` items, deliberate boundaries the recipients
  respect and do not challenge;
- **Assumptions**: `ASM` items, what the requirements rest on and what
  must stay true;
- **Deliverables**: `DEL` items, what the recipients bring back and
  when; a deliverable may delegate specification work;
- **Open Questions**: `TBC` items, each with an owner; a question
  owned by the recipients is part of the assignment, and they decide
  and report back;
- **Success Criteria**: `SCR` items, optional; they may be absent or
  delegated through a deliverable;
- **Terms**: the prefixes and the defined terms the document actually
  uses, and nothing more.

Narrative is confined to Purpose & Context and Objective. Everything
else is items with stable IDs, in the format `PREFIX.NNNN`, numbered
in tens, each new group starting at the next hundred (why every item
carries an ID: [Stable IDs](stable-ids.md)). Groups are plain
headings with no IDs, no metadata and no lifecycle. An empty section
is deleted, and so are the template's comments. The Terms section
lists only what the document uses. A defined term is capitalised in
item text to signal that it appears in the Terms section.

Items follow the Requirement style, whose rule set stands on its own
page ([Requirement style and Story style](../reference/requirement-style.md)).
What the style amounts to:

- an item is an obligation in the indicative, one idea per item,
  written once, in a full correct sentence;
- in English the obligation is **shall** / **shall not**, strictly;
  would, could, should, might, may and MoSCoW wording are not used;
- an artefact in another language uses that language's own verb of
  obligation under the same rule of kind, and the forge names no word
  of any other language (which language an artefact is written in:
  [Languages](languages.md));
- there is no priority column and no priority tag; everything is
  essential, and an exception carries a note reading *optional*;
- testability is recommended, not required;
- success criteria are wanted but not compulsory; delegating them to
  the recipients as a deliverable is a legitimate outcome, not a
  defect.

The assignment also carries the cut of the intent: what of it is the
recipients' now, what is expressly later and what is out of scope.

## Complete when

The assignment is complete when nothing the recipients would need is
left to assumption. Delegated or open on purpose is complete; silent
is not. The recipients must know what must be true at the end, and
why, well enough to act rightly where the plan no longer fits.

Nothing is omitted for brevity's sake. Leaving a matter out is
legitimate only as an explicit delegation, that is, a `DEL` or a
`TBC` item. A silent omission is a defect.

When this completion is reached, Claude offers the approval. The
offer is a recommendation, never a gate.

## How it is found

Most of the assignment lies in the intent; the rest is found by
asking. Claude walks a map of what the assignment needs twice: before
the recast, to see what the intent leaves unanswered, and at the end
of the pass. An area of the map may stay empty when it was considered
and found not to apply. The areas are:

- the recipients: who they are, what they already know and what they
  will do with the assignment;
- the objective: what must be true at the end;
- the cut: what of the intent is theirs now, what is expressly later
  and what is out of scope;
- the line between assigning and solving: what is specified, what is
  theirs to decide and bring back, what is left open on purpose and
  whose it is;
- the boundaries: what they shall not do, what is not to be challenged
  and what the whole rests on;
- success: criteria present, delegated or deliberately absent;
- self-containment: what must be defined so that the assignment is
  read without the principal in the room.

The assignment is found in a joint pass of three phases, with no new
kind of interview. First come questions up front, one per message,
only for what is the principal's and the intent does not answer; there
are none where the intent answers everything. A question on the detail
of the handover belongs here. A question on substance the intent has
not settled means the intent is not ready, and the work returns to
it. Second comes the recast: Claude writes the whole draft from the
intent and, with it, a provenance map from each group to its items
and to the positions of the intent they came from, listing beside it
the in-scope positions that landed nowhere and the items with no
position behind them; both lists are to be empty. The provenance map
is a tool of the pass, not part of the assignment. Third comes the
walkthrough by group: one item of the walkthrough is one group, with
what it covers, from which positions, what in it is delegated or
open, and what is optional or later. A verdict is given per group; a
question on a single item opens a sub-item and closes it before the
pass moves on. The pass as a procedure, step by step, is
[Distil an assignment](../use/distil-an-assignment.md).

There are three ways in. Where no assignment exists yet, the joint
pass runs whole. Where an assignment stands and the intent has
moved, the pass runs on what changed, the provenance map showing what
the change touched. A wording fix is made in the assignment directly.
A substance change asked for in the assignment goes to the intent
first, and from there it propagates down.

## Why

**Why structured items and not prose.** An item with a stable ID can
be cited, reviewed, traced into the layer below and changed one at a
time. Prose cannot be pointed at. So narrative is confined to the two
sections that need it.

**Why the boundary is kind, not amount.** The defect of an assignment
is solving instead of assigning. An early case led to a list of
banned apparatus, such as stakeholder matrices and impact analyses;
that list was one case and not a universal rule. So the rule says
what kind of content belongs, and any apparatus may appear where it
serves setting direction.

**Why complete means nothing silent.** The recipients act without the
principal in the room. What is delegated or open on purpose they can
see and take up; what is silent they can only guess at. So a silent
omission is a defect and length is never one.

**Why an obligation in the indicative.** An obligation in the
indicative is testable and binds. The softer verbs, would, could,
should, might and may, leave the recipient to guess what is required.
MoSCoW puts a priority where completeness belongs. So a conditional, a
permission, a wish and MoSCoW wording are all out.

**Why shall in English, strictly.** The forge aligns its English
requirement wording with an external standard for such documents.
Which standard is not named on this page.

**Why the verb follows the language of the artefact.** The
alternative was to keep `shall` in an artefact of every language and
have a render turn it into the language's verb. That was dropped for
three reasons. One requirement would have two wordings. Every render
would translate again. And the document the stakeholders approve
would not be the one the chain holds. So an artefact in another
language carries its own verb of obligation under the same rule of
kind, and the forge names no word of any other language.

**Why no priorities.** Priority tags such as `critical`, `important`
and `nice-to-have` were wanted at first as an optional attribute.
They were dropped in favour of the convention that everything in an
assignment is essential and an exception is noted as *optional*.

**Why testability is recommended, not required.** Assignments are
deliberately high-level. Delegating concretisation through a `DEL`
item is a legitimate outcome.

**Why one skeleton for every assignment.** Separate templates per
genre of assignment were rejected in favour of one universal skeleton
with optional sections. So everything arriving from the principal has
a consistent shape.

**Why a Terms section.** So that the assignment can be forwarded
without oral tradition.

**Why a joint pass of three phases.** Not item by item, because most
items are craft derived from the intent, and a verdict on each is
ceremony. Not "read the whole", because without the map one sees what
is there, not what is missing. With the provenance map visible at
each group, dozens of items pass in a handful of messages and nothing
is skipped. The pass adds no new kind of interview: its questions and
its walkthrough are the forge's ordinary ones.

**Why the name.** "Mandate" was rejected outright by the principal;
the reason is not recorded. "Charter" carries project-management
ceremony and implies a project, which many assignments are not.
"Assignment" was retained, and it does not preclude further layers
below it.

## A worked example

One requirement item, generic and from no project, as it would stand
in the Requirements section of an assignment. The defined term is
capitalised and would appear in the Terms section.

```
### Intake

- **REQ.0110** The Service shall record every request it receives,
  with the time of receipt and the identity of the Requester, and
  shall make that record available to the Requester on demand.
```

What makes it an item of an assignment: it is one idea, written once,
in a full sentence; it is an obligation in the indicative, `shall`,
and neither a wish nor a permission; it carries no priority, so it is
essential; it says what must be true at the end and leaves how the
record is kept, the solving, to the recipients. Had the principal
chosen to leave the content of the record to the recipients, the
place for that would be a `DEL` item asking them to define it and
return, not a vaguer requirement.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID.
- [Languages](languages.md): which language an artefact is written
  in.
- [Requirement style and Story style](../reference/requirement-style.md):
  the rule set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
