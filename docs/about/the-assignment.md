---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: dcdce17a4f8b7039
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

The assignment is the artefact of the chain that carries the in-scope
substance of the intent to the recipients, complete and precise, so
that they can act on it without the principal (the person whose
thinking is being forged) in the room. This page explains what makes
an assignment complete, where assigning ends and solving begins, what
kind of items it holds and why they are written the way they are. It
is for the user who will have one made and for the evaluator who
wants to judge one; the procedure of making it is the page
[Distil an assignment](../use/distil-an-assignment.md).

## What it is

The assignment is the file `20-assignment.md` of a project: the
handover document for the recipients, complete, precise, structured,
self-contained and versioned. It tells the recipients who they are,
what must be true at the end, what is theirs to decide and bring
back, what they shall not do, and what the principal has left open on
purpose. It assigns and does not solve. The intent stays the trunk of
the chain and the source of the substance; the assignment is the
intent's in-scope substance cast for the people who will act on it.

The name "assignment" was kept deliberately. It does not preclude
further layers of the chain below it.

## Who writes and reads it

The principal and Claude write it together: the substance is the
principal's, the wording is Claude's, in the Requirement style. The
recipients read it. They may be a team, colleagues or the principal's
future self; the template marks them as the audience of the file.
Claude reads the intent against what the assignment needs, that is
the recipients, the objective, the delegation, the success criteria
and the horizon, and raises as an open question what the intent is
silent on. It never fills such a gap itself. A substance change that
is asked for in the assignment is proposed to the intent first.
Only wording is fixed in the assignment directly.

## Made from

- `10-intent.md`, the intent of the project, read together with the
  project's threads in `threads/` (one open matter of the intent per
  file).
- `decisions.md`, the principal's decisions with their reasons.
- the ledger: the project's state, made at read time from its
  documents.

The first draft is created from the template `templates/assignment.md`.
Its history companion `20-assignment.history.md` is created from
`templates/history.md`. The companion, not the body, is where every
change and its reason are recorded.

## What it holds

The template gives one universal skeleton with optional sections.
Narrative stands in two sections only, Purpose & Context and
Objective. Everything else is items with stable IDs, so that each one
can be cited, reviewed, traced into the layer below and changed one
at a time; prose cannot be pointed at. Why every item carries an ID is
the page [Stable IDs](stable-ids.md).

The sections, in the order of the template:

- Purpose & Context: why the assignment exists and what the reader
  needs in order to act, without solutioning.
- Objective: what must be true at the end.
- Scope: what is in scope, in plain text, and what is out of scope as
  OOS items.
- Requirements: REQ items, grouped under plain headings when clusters
  emerge.
- Constraints: CON items, deliberate boundaries the recipients
  respect and do not challenge.
- Assumptions: ASM items, what the requirements rest on.
- Deliverables: DEL items, what the recipients bring back and when;
  a DEL may delegate specification work.
- Open Questions: TBC items, each with an owner; a question owned by
  the recipients is part of the assignment, they decide and report
  back.
- Success Criteria: SCR items, optional.
- Terms: the prefixes and the defined terms actually used, so that
  the document can be forwarded without oral tradition.

Empty sections and the template's comments are deleted from the
draft.

The items share one style. An item is an obligation in the
indicative, in a full correct sentence, one idea per item, each
written once. It is never a conditional, a permission or a wish, and
never MoSCoW wording. In English the obligation is "shall" and
"shall not", strictly. An artefact in another language uses that
language's own verb of obligation under the same rule of kind; the
forge names no word of any other language. Which language an
artefact is written in is the page [Languages](languages.md). There
is no priority column and no priority tag: everything in an
assignment is essential, and an exception carries a note reading
*optional*. Testability is recommended, not required. Success
criteria are wanted, not compulsory. A defined term is capitalised in
item text, as a sign that it stands in the Terms section. The full
rule set is the page
[Requirement style and Story style](../reference/requirement-style.md).

A worked example, one requirement item in the shape the template and
the style give, taken from no project:

```
### Records

- **REQ.0110** The Service shall record every change of a Record
  together with its author and the time of the change.
- **REQ.0120** The Service shall offer the history of a Record to its
  Owner. *optional*
```

The first item is one idea in one indicative sentence, with "shall"
as the English obligation. "Service", "Record" and "Owner" are
capitalised because they are defined in the Terms section. The second
item is the one way an item is marked as less than essential: a note
reading *optional*, never a priority tag. Where the principal wants
the recipients to concretise a matter, the item is not softened; it
becomes a DEL item that says what they bring back.

## Complete when

An assignment is complete when nothing the recipients would need is
left to assumption. Delegated or open on purpose is complete; silent
is not. A matter is legitimately left out only as an explicit
delegation, a DEL or a TBC item. The recipients also know what must
be true at the end, and why, well enough to act rightly where the
plan no longer fits.

Nothing is omitted for brevity's sake. There is no size target in
either direction: length is whatever fidelity requires. The defect an
assignment can have is excess of the wrong kind, solving instead of
assigning, never length as such.

The boundary between assigning and solving is the kind of content,
never its amount. Machinery of executing delivery belongs to the
recipients. An apparatus such as a stakeholder matrix or an impact
analysis is not banned as such: it may appear where the principal
judges it part of setting direction, and it is the recipients'
machinery only when it belongs to executing delivery.

When completion is reached, Claude offers the approval. The offer is
a recommendation, never a gate.

## How it is found

The assignment is found in a joint pass of three phases, with no new
kind of interview. Before the pass Claude says whether the intent is
ready to be derived from, never as a gate.

1. Questions up front: one per message, only for what is the
   principal's and the intent does not answer, such as who the
   recipients are, what is delegated and what specified, whether
   success criteria are present, delegated or deliberately absent,
   and what is later. Where the intent answers everything there are
   none. A question on substance the intent has not settled means
   the intent is not ready, and the work returns to it.
2. The recast: Claude writes the whole draft from the intent and,
   with it, a provenance map. The provenance map shows each group,
   its items and the positions of the intent they came from, the
   in-scope positions that landed nowhere, and the items with no
   position behind them. Both of the last two are to be none. The
   provenance map is a tool of the pass, not part of the assignment.
3. The walkthrough by group: a walkthrough is the forge's way of
   working a list one item per message, each closed with the
   principal's verdict. Here one item is one group of the
   assignment: what it covers, from which positions, what in it is
   DEL or TBC, what is optional or later. A question on a single item
   opens a sub-item and closes it before the pass moves on.

Before the recast and again at the end of the pass, Claude walks the
areas the assignment must cover: the recipients, the objective, the
cut between now, later and out of scope, the line between assigning
and solving, the boundaries, success, and self-containment. An area
may stay empty when it was considered and found not to apply.

After the pass Claude offers `/critique essence`, a reviewer that
reads the documents apart from the conversation, as the independent
test of drift between the intent and the assignment. It is never run
on Claude's own judgement. Its findings are settled in an ordinary
walkthrough.

The pass runs whole when no assignment exists yet. When an assignment
stands and the intent has moved, the pass runs on what changed, the
provenance map showing what the change touched. A wording fix is made
in the assignment directly.

## Why

**Why complete, and why no size target.** A silent omission is a
defect, because the recipients act without the principal in the room
and cannot ask what was meant. The goal is to have the assignment
right, not short. So the only legitimate way to leave a matter out
is to say so, as a delegation or an open question.

**Why the boundary is the kind of content.** An assignment assigns;
it does not solve. An enumerated ban on particular apparatus was once
in force and originated in one early case. It is not a universal
rule, because the same apparatus may be part of setting direction in
one project and machinery of delivery in another.

**Why structured items.** An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at.

**Why an obligation in the indicative.** An obligation in the
indicative is testable and binds. The softer verbs, would, could,
should, might and may, leave the recipient to guess what is required.
MoSCoW puts a priority where completeness belongs. In English the
word is "shall" and "shall not", strictly, following a standard the
forge aligns its English artefacts with.

**Why the verb follows the language of the artefact.** The alternative
was to keep "shall" in an artefact of every language and have a
render turn it into the language's own verb. It was dropped, because
it would make two wordings of one requirement and a translation at
every render. The document the stakeholders approve would then not
be the one the chain holds.

**Why no priorities.** Priority tags on items, such as critical,
important and nice-to-have, were once wanted as an optional attribute.
They were dropped in favour of the convention that everything in an
assignment is essential and an exception is noted as *optional*.

**Why testability is recommended and success criteria are not
compulsory.** Assignments are deliberately high-level. Delegating
concretisation, or the success criteria themselves, to the recipients
through a DEL item is a legitimate outcome, not a defect.

**Why one template.** Separate templates per genre of assignment were
rejected in favour of one universal skeleton with optional sections,
so that everything arriving from the principal has a consistent
shape.

**Why a joint pass of three phases.** Not item by item, because most
items are craft derived from the intent, and a verdict on each is
ceremony. Not "read the whole", because without the provenance map
one sees what is there, not what is missing. The questions come
first so that only what the intent does not answer is asked. The
walkthrough is by group so that dozens of items pass in a handful of
messages, nothing is skipped, and the provenance is visible at each.

**Why the name.** "Charter" was rejected because it carries
project-management ceremony and implies a project, which many
assignments are not. "Mandate" was rejected outright by the
principal; the reason is not recorded. "Assignment" was retained, and
it does not preclude further layers below it.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
