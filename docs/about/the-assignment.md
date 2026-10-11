---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: fc01bb980bb8ee2a
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
the assignment is, what it holds, when it is complete, how it is
found and why its rules are as they are. It is written for the user
who will have an assignment made and for the evaluator who wants to
judge whether the artefact and its rules hold together. The
procedure of making one is the page [Distil an
assignment](../use/distil-an-assignment.md); the rule set of its
items is the page [Requirement style](../reference/requirement-style.md).

## What it is

The assignment is the distilled handover document of a project: the
file `20-assignment.md`, the layer of the chain directly below the
intent. The principal is the one whose thinking is being forged; the
recipients are those who will act on it, a team, colleagues or the
principal's future self. The assignment tells the recipients who they
are, what must be true at the end, what is theirs to decide and bring
back, what they shall not do, and what the principal has left open on
purpose.

The assignment assigns and does not solve. What keeps a document an
assignment is the kind of content, never its amount. The machinery of
executing delivery belongs to the recipients. An apparatus such as a
stakeholder matrix or an impact analysis may still appear in an
assignment where the principal judges it part of setting direction.

Its properties, in the words of the forge: complete, precise,
structured, self-contained, versioned. The name "assignment" was kept
deliberately. It does not preclude further layers of the chain below
it.

## Who writes and reads it

The principal composes it with Claude. The wording is Claude's, in
the requirement style; the substance is the principal's. Claude reads
the intent against what the assignment needs (recipients, objective,
delegation, success criteria, horizon) and takes the principal
through the joint pass described below. Where the intent is silent,
Claude raises an open question rather than filling the gap. A
substance change that surfaces while the assignment is being worked
goes to the intent first, never into the assignment directly; only a
wording fix is made in the assignment itself.

The readers are the recipients. The front-matter of every assignment
names them as its audience. An assignment is meant to be forwarded
without oral tradition.

## Made from

The assignment is made from the intent (`10-intent.md`, read with the
project's open threads in `threads.md`), from the project's decisions
(`decisions.md`) and from the ledger, the project's single source of
truth for state. Its shape is the template `templates/assignment.md`.
Its history lives in the companion `20-assignment.history.md` beside
it, never in its body.

The intent should be ready to be derived from before the pass begins.
Claude says whether it is, but readiness is never a gate.

## What it holds

The template gives the assignment these sections, each kept only
where the project has material for it:

- Purpose & Context: why the assignment exists, what problem or
  opportunity it addresses and what the reader needs in order to act;
  narrative, no solutioning.
- Objective: what must be true at the end, in a few sentences.
- Scope: what is in scope in plain text, and out-of-scope items with
  IDs.
- Requirements: the items, grouped under plain headings when clusters
  emerge.
- Constraints: deliberate boundaries the recipients respect and do
  not challenge.
- Assumptions: what the requirements rest on and what must stay true.
- Deliverables: what the recipients bring back and when; a
  deliverable may delegate specification work.
- Open Questions: each with an owner; a question owned by the
  recipients is part of the assignment, and they decide and report
  back.
- Success Criteria: optional; may be absent or delegated through a
  deliverable.
- Terms: the prefixes and the defined terms the document actually
  uses.

Narrative is confined to Purpose & Context and Objective. Everything
else is structured items with [stable IDs](stable-ids.md): a
three-letter prefix and a four-digit number, numbered in tens, each
new group starting at the next hundred, never renumbered. The
prefixes of an assignment are REQ for a requirement, OOS for out of
scope, CON for a constraint, ASM for an assumption, DEL for a
deliverable, TBC for an open question and SCR for a success
criterion. Negative mandates, out of scope and do-not, rank equally
with positive ones.

The items are written with shall and shall not, in full correct
sentences, one idea per item, each written once. The softer verbs and
MoSCoW wording are not used. There is no priority column and no
priority tag: everything in an assignment is essential, and an
exception carries a note reading *optional*. Testability is
recommended, not required. Success criteria are wanted, not
compulsory. Defined terms are capitalised in item text to signal that
they stand in the Terms section. An item must not depend on an
external link to be understood, agreed or later tested. The full rule
set is the page [Requirement style](../reference/requirement-style.md).

The assignment also carries the horizon as a boundary: what is
assigned now and what is expressly later. The reasons for that cut
stay in the intent.

## Complete when

The assignment is complete when nothing the recipients would need is
left to assumption. Delegated or open on purpose is complete; silent
is not. It is complete, too, when the recipients know what must be
true at the end, and why, well enough to act rightly where the plan
no longer fits.

Nothing is omitted for brevity's sake. Length is whatever fidelity
requires. There is no size target in either direction: the defect is
excess of the wrong kind, solving instead of assigning, never length
as such. Leaving a matter out is legitimate only as an explicit
delegation, that is a deliverable or an open question with an owner.
A silent omission is a defect.

When that completion is reached, Claude offers the approval. The
offer is a recommendation, never a gate.

## How it is found

The assignment is found in a joint pass of three phases, with no new
kind of interview. The pass is a working conversation of the usual
form: what is agreed is carried in the conversation and written once
at the round's end, on the principal's word.

1. Questions up front. Claude asks, one per message, only what is the
   principal's and the intent does not answer: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, what is
   later. There are none where the intent answers everything. A
   question on the detail of the handover belongs here. A question
   on substance the intent has not settled means the intent is not
   ready, and the work returns to it.
2. The recast. Claude writes the whole draft from the intent, and
   with it a provenance map: each group, its items and the positions
   of the intent they came from, plus the in-scope positions that
   landed nowhere and the items with no position behind them. Both
   lists are meant to be empty; the second is drift. The provenance
   map is a tool of the pass, not part of the assignment.
3. The walkthrough by group. A walkthrough is the forge's way of
   working a list of items needing the principal's decision one item
   per message, each closed with a verdict. Here one item of the
   walkthrough is one group of the assignment: what it covers, from
   which positions, what in it is delegated or open, what is optional
   or later. A verdict is given per group. A question on a single
   item opens a sub-item and closes it before the pass moves on.
   Dozens of items pass in a handful of messages, nothing is skipped
   and the provenance is visible at each.

Before the recast and again at the end of the pass, Claude walks the
areas the assignment must cover: the recipients, the objective, the
cut between now, later and out of scope, the line between assigning
and solving, the boundaries, success, and self-containment. An area
may stay empty when it was considered and found not to apply.

After the pass, Claude offers the critic lens essence as the
independent test of drift. The critic is an isolated reviewer, a
subagent that never sees the working conversation. It is never run
on Claude's own judgement, and its findings are settled in an
ordinary walkthrough.

There are three ways in. Where no assignment exists yet, the pass
runs whole. Where an assignment stands and the intent has moved, the
pass runs on what changed, the provenance map showing what the change
touched. Where only wording needs fixing, the fix is made in the
assignment directly. The procedure as you run it is the page [Distil
an assignment](../use/distil-an-assignment.md).

## Why

Why structured items and not prose. An item with a stable ID can be
cited, reviewed, traced into the layer below and changed one at a
time. Prose cannot be pointed at. This holds even at very high
abstraction.

Why shall and shall not. Shall is testable and binds. The softer
verbs (would, could, should, might, may) leave the recipient to guess
what is required. MoSCoW wording puts a priority where completeness
belongs.

Why no priorities. Priority tags were once wanted as an optional
attribute on items. They were dropped for the convention the forge
aligns its assignments with: everything in an assignment is essential,
and an exception is noted as optional.

Why testability is recommended and not required. Assignments are
deliberately high-level. Delegating the concretisation of an item to
the recipients through a deliverable is a legitimate outcome, not a
defect. For the same reason success criteria are wanted but not
compulsory: delegating them to the recipients as a deliverable is a
legitimate outcome.

Why a Terms section. So that the assignment can be forwarded without
oral tradition.

Why an item must not depend on an external link. The reason is not
recorded.

Why no size target. The goal is to have the assignment right, not
short. The defect to watch for is solving instead of assigning, and
that is a matter of the kind of content, not of its amount.

Why one template and not one per genre of assignment. Separate
templates per genre were rejected in favour of one universal skeleton
with optional sections. So that everything arriving from the
principal has a consistent shape.

Why a joint pass and not item by item. Most items are craft derived
from the intent, and a verdict on each would be ceremony. Why not
simply read the whole draft instead: without the provenance map one
sees what is there, not what is missing.

Why the name. "Mandate" was rejected outright by the principal; the
reason is not recorded. "Charter" carries project-management ceremony
and implies a project, which many assignments are not. "Assignment"
was retained, and it does not preclude further layers below it.

## A worked example

A generic group of a requirements section, in the shape the template
and the requirement style define. The slug, the terms and the items
are placeholders taken from no project.

```markdown
### Registration
- **REQ.0100** The Registration Service shall confirm a new Member's
  registration within one working day of the request.
- **REQ.0110** The Registration Service shall not retain a Member's
  identity document once the registration is confirmed.
- **REQ.0120** The Registration Service shall notify the Member of
  the confirmation in the Member's chosen channel. *optional*
```

Each item covers one idea, is written once and reads as a full
sentence. The defined Terms, Registration Service and Member, are
capitalised and stand in the Terms section of the same document. The
third item carries the only kind of priority an assignment knows, a
note reading *optional*. A matter the principal leaves to the
recipients is not left silent; it is an explicit delegation beside
the group:

```markdown
- **DEL.0010** The recipients shall define the success criteria for
  Registration and return them with the first version of their plan.
```

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID that is
  never renumbered.
- [Requirement style](../reference/requirement-style.md): the rule
  set.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
