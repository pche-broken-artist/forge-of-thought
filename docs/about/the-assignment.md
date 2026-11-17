---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: a4031d8c2fdf4fd1
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
in-scope substance of the [intent](../reference/glossary.md) to the
recipients (those the work is handed to), complete and precise. This
page says what the assignment is, what makes it complete, where
assigning ends and solving begins, and why its items are worded as
they are. It is for a reader who is about to hand work over through
the forge, and for a reader who weighs whether that way of handing
over holds.

## What it is

The assignment is the file `20-assignment.md` of a project. It is the
distilled handover document for the recipients: complete, precise,
structured, self-contained and versioned. It carries the whole
in-scope substance of the intent. The recipients are to act on it
without the principal in the room. The principal is the person whose
thinking is being forged.

The assignment tells the recipients:

- who they are;
- what must be true at the end;
- what is theirs to decide and bring back;
- what they shall not do;
- what the principal has left open on purpose.

An assignment assigns. It does not solve. The boundary between the
two is the kind of content, never its amount. The machinery of
executing delivery belongs to the recipients. Any apparatus, such as
a stakeholder matrix or an impact analysis, may appear where the
principal judges it part of setting direction.

## Who writes and reads it

The principal and Claude write the assignment together. The substance
belongs to the principal. The wording is written by Claude, in the
Requirement style. Where the intent is silent on something the
assignment needs, Claude raises it as an open question and does not
fill it.

A change of substance does not start in the assignment. Claude
proposes it to the intent first. Only a fix of wording is made in the
assignment directly.

The recipients read the assignment and act on it. A question the
assignment leaves to the recipients is part of the assignment: they
decide and report back.

## Made from

The assignment is made from three inputs:

- the intent (`10-intent.md`), read with the project's
  [threads](../reference/glossary.md) (`threads/`);
- the project's decisions (`decisions.md`);
- the ledger (the file that states where the project stands).

Its definition (`.claude/skills/forge/states/assignment.md`) says how
the assignment is found. Its template (`templates/assignment.md`)
gives the shape of the result. The history of the assignment is kept
in a companion file (`20-assignment.history.md`), never in the
assignment itself.

## What it holds

The header carries the version, the status (`draft`, `approved` or
`superseded`), the project and the audience (`recipients`). The
sections follow in this order:

- **Purpose & Context**: why the assignment exists, what problem or
  opportunity it addresses and what the reader needs in order to act.
  It holds no solutioning.
- **Objective**: what must be true at the end.
- **Scope**: what is in scope, as a short plain list, and what is out
  of scope, as `OOS` items.
- **Requirements**: `REQ` items, grouped under plain headings when
  clusters emerge.
- **Constraints**: `CON` items, the deliberate boundaries the
  recipients respect and do not challenge.
- **Assumptions**: `ASM` items, what the requirements rest on and
  what must stay true.
- **Deliverables**: `DEL` items, what the recipients bring back and
  when. A deliverable may delegate specification work.
- **Open Questions**: `TBC` items, each with an owner.
- **Success Criteria**: `SCR` items. The section may be absent, or
  delegated through a `DEL` item.
- **Terms**: the prefixes and the terms the document actually uses.

Narrative is confined to Purpose & Context and Objective. Everything
else is an item with a stable ID. The page [Stable IDs](stable-ids.md)
says why every item carries an ID.

Each requirement is an obligation in the indicative. In English the
obligation is **shall** and **shall not**, strictly. An
[artefact](../reference/glossary.md) in another language uses that
language's own verb of obligation, under the same rule of kind: never
a conditional, a permission or a wish. The forge names no word of any
other language. Which language an artefact is written in is said on
the page [Languages](languages.md).

Items carry no priorities. Everything in an assignment is essential
by default, and an exception carries a note reading *optional*.
Testability is recommended, not required. Success criteria are
wanted, not compulsory. A negative mandate (an out-of-scope item or a
do-not) ranks equally with a positive one.

The assignment is read without its author beside it. Every assignment
carries a Terms section, and defined terms are capitalised in item
text. An item does not depend on an external link to be understood,
agreed or later tested.

The whole rule set is on the page [Requirement style and Story
style](../reference/requirement-style.md).

## Complete when

An assignment is complete when two things hold. Nothing the
recipients would need is left to assumption. The recipients know what
must be true at the end, and why, well enough to act rightly where
the plan no longer fits.

Complete does not mean that everything is specified. A matter
delegated to the recipients is complete. A matter left open on
purpose is complete. A matter passed over in silence is not. Leaving
a matter out is legitimate only as an explicit delegation: a `DEL`
item or a `TBC` item.

Nothing is omitted for brevity's sake. There is no size target in
either direction: length is whatever fidelity requires. The defect is
excess of the wrong kind, that is solving instead of assigning, never
length as such.

The definition names the areas an assignment has to answer:

- the recipients: who they are, what they already know and what they
  will do with the assignment;
- the objective: what must be true at the end;
- the cut: what of the intent is theirs now, what is expressly later
  and what is out of scope;
- the line between assigning and solving: what is specified, what is
  theirs to decide and bring back, what is left open on purpose and
  whose it is;
- the boundaries: what they shall not do, what is not to be
  challenged and what the whole rests on;
- success: criteria present, delegated or deliberately absent;
- self-containment: what must be defined for the assignment to be
  read without the principal in the room.

An area may stay empty when it was considered and found not to apply.
When the assignment is complete, Claude offers the approval. The
offer is a recommendation, never a gate.

## How it is found

The assignment is found in a joint pass of the principal and Claude.
The pass has three phases and is no new kind of interview. The page
[Distil an assignment](../use/distil-an-assignment.md) gives the pass
as a procedure.

1. **Questions up front.** Claude asks one question per message, and
   only what is for the principal to say and the intent does not
   answer:
   - who the recipients are;
   - what is delegated and what is specified;
   - whether success criteria are present, delegated or deliberately
     absent;
   - what is later.

   Where the intent answers everything, there is no question.
2. **The recast.** Claude writes the whole draft from the intent, and
   with it the provenance map. The provenance map shows, group by
   group, the items and the positions of the intent they came from. A
   position is an item of the intent that says what the principal
   holds or wants. The provenance map also names the in-scope
   positions that landed nowhere and the items that came from no
   position, which are drift. Both are to be none. The provenance map
   is a tool of the pass, not part of the assignment.
3. **The walkthrough by group.** A walkthrough is a list worked one
   item per message, each item closed by the principal's verdict.
   Here one item is one group of the assignment: what it covers, from
   which positions it came, what in it is delegated or open, and what
   is optional or later. The principal gives one verdict per group. A
   question on a single item is opened and closed before the pass
   moves on.

Where no assignment exists yet, the pass runs whole. Where an
assignment stands and the intent has moved, the pass runs on what
changed, and the provenance map shows what the change touched.

A question on substance that the intent has not settled means that
the intent is not ready. The work then returns to the intent. Many
questions are evidence of that, never its measure. Claude says at the
start whether the intent is ready to be derived from. That statement
is never a gate.

After the pass Claude offers `/critique essence`, the independent
test of drift. The test never runs on Claude's own judgement. Its
findings are settled in an ordinary walkthrough.

## Why

### Complete, not short

The recipients act without the principal in the room. What the
assignment passes over in silence, they would have to assume. Where
the plan no longer fits, they have to know the end and the reason
well enough to act rightly. The goal is to have the assignment right,
not short. For that reason a silent omission is a defect, and length
is not.

### The boundary is the kind of content

What keeps a document an assignment is the kind of content, never its
amount. No apparatus is banned as such: a stakeholder matrix, an
impact analysis or a table of contents may appear where the principal
judges it part of setting direction. It is the recipients' machinery
only when it belongs to executing delivery. The defect is solving
instead of assigning, never length as such.

### Items, not prose

An item with a stable ID can be cited, reviewed, traced into the
layer below and changed one at a time. Prose cannot be pointed at.

### An obligation in the indicative

An obligation in the indicative is testable and binds. The softer
verbs (would, could, should, might, may) leave the recipient to guess
what is required. For that reason an item is never a conditional, a
permission or a wish. MoSCoW wording is not used either: it puts a
priority where completeness belongs.

### The verb follows the language of the artefact

The other way would be to keep `shall` in an artefact of every
language and to have a [render](../reference/glossary.md) turn it
into the language's verb. That way is rejected, for three reasons:

- one requirement would have two wordings;
- every render would need a translation;
- the document the stakeholders approve would not be the one the
  [chain](../reference/glossary.md) holds.

### No priorities

Everything in an assignment is essential. Priority tags on items,
such as `critical`, `important` and `nice-to-have`, are rejected in
favour of that rule, with the note *optional* for an exception.

### Testability and success criteria

Assignments are deliberately high-level. Delegating the
concretisation to the recipients through a `DEL` item is a legitimate
outcome. The same holds for success criteria: handing them to the
recipients as a deliverable ("define success criteria and return") is
a legitimate outcome, not a defect.

### A Terms section

Every assignment carries a Terms section. The purpose: the assignment
can be forwarded without oral tradition.

### One template

Separate templates per genre of assignment are rejected in favour of
one template with optional sections. The purpose: everything that
arrives from the principal has a consistent shape.

### A joint pass of three phases

Two other ways are not used. The first is a verdict item by item:
most items are craft derived from the intent, and a verdict on each
is ceremony. The second is reading the whole draft: without the
provenance map one sees what is there, not what is missing. By group,
dozens of items pass in a handful of messages, nothing is skipped and
the provenance is visible at each.

### The name

The name "assignment" is kept deliberately. It does not preclude
further layers below the assignment. Two other names are rejected.
"Charter" carries project-management ceremony and implies a project,
which many assignments are not. "Mandate" is rejected outright by the
principal: the reason is not recorded.

## A worked example

One requirement of an assignment written in English, with what stands
beside it. The content is a placeholder.

```markdown
## Requirements

### Answering
- **REQ.0010** Every Request shall receive an answer.

## Deliverables
- **DEL.0010** The recipients shall define the time within which a
  Request is answered and return it by <date>.

## Terms
REQ requirement · DEL deliverable

| Term | Meaning |
|---|---|
| Request | A question a customer sends in. |
```

The requirement is one idea in one full sentence. It is an obligation
in the indicative: either every Request received an answer or one did
not, and the recipients know that it binds. It carries no priority,
since every item is essential. "Request" is capitalised, which
signals that the Terms section defines it. The item is understood
without anything outside the document.

The requirement does not say how quickly a Request is answered.
Passed over in silence, that would be a gap: the recipients would
have to assume. The deliverable hands the matter to them in so many
words. The assignment is then complete on this point and still solves
nothing. How answers are produced is machinery of executing delivery
and belongs to the recipients. The requirement stays high-level,
which the style allows: testability is recommended, not required.

The same matter in wordings the Requirement style does not use:

```markdown
- Every Request should receive an answer.
- Every Request may receive an answer.
- Must have: an answer to every Request.
```

The first two leave the recipient to guess what is required. The
third puts a priority where completeness belongs.

In an assignment written in another language the same item uses that
language's own verb of obligation.

## See also

- [Distil an assignment](../use/distil-an-assignment.md): the joint
  pass as a procedure.
- [Stable IDs](stable-ids.md): why every item carries an ID.
- [Languages](languages.md): which language an artefact is written
  in.
- [Requirement style and Story
  style](../reference/requirement-style.md): the rule set.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
