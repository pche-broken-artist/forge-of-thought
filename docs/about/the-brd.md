---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: ab55d3ec002c8329
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
  - projects/forge/10-intent.md#POS.1800
  - projects/forge/10-intent.md#POS.1810
  - projects/forge/10-intent.md#POS.1820
  - projects/forge/10-intent.md#POS.1830
  - projects/forge/10-intent.md#POS.1840
  - projects/forge/10-intent.md#POS.1850
  - projects/forge/10-intent.md#REJ.0390
  - projects/forge/10-intent.md#REJ.0400
  - projects/forge/10-intent.md#REJ.0410
  - projects/forge/10-intent.md#REJ.0430
  - projects/forge/10-intent.md#REJ.0420
---

# The BRD

The BRD is the business requirements of a project: an artefact of the
chain (one of the versioned documents a thought travels through),
kept in `30-brd.md`. This page explains what a BRD holds, how it
starts, who works on it, when it is complete and why the forge names
what it cannot know instead of writing it. It is for anyone who uses
a BRD, extends the forge around it or weighs whether it fits their
work.

## What it is

The BRD stands below the assignment and above the solution design.
It breaks its parent into three kinds of content:

- rules that the stakeholders of each area can review on their own;
- behaviour that must be agreed as a sequence;
- qualities, each with a value given by the stakeholders.

Its purpose is that the delivery teams can estimate and the
solution design can start. It admits the solution only at the level
the stakeholders need to agree the ask. The how is left to the
solution design. Where to stop is a judgement: the BRD stops when
the teams can estimate, or when more detail would not interest the
stakeholders or would be superseded by design.

Its definition (the state file that says how the artefact is found)
is `.claude/skills/forge/states/brd.md`, and its template is
`templates/brd.md`.

## Who writes and reads it

The BRD is written by an analyst working as the principal (the
person whose thinking is forged, with final authority on the
content) of a project of his own. Claude works beside him as a
partner and does the recast:

- the whole drafted from the parent, with a provenance map that
  lists every item of the parent;
- groupings proposed so that every stakeholder finds theirs and
  nothing appears twice;
- use cases drawn from the parent's view of the process;
- the touched areas of the enterprise raised one by one;
- the wording kept in the BRD's requirement style.

The principal decides the scope of the document, the groupings,
which areas apply, the owner of every open question and every value.

The stakeholders and the delivery teams read the BRD. The
stakeholders review the rules of their area. The delivery teams
estimate from it.

## Made from

A BRD has one parent, named by the principal when he asks for it.
There are two parents of the chain:

- the assignment (see [The assignment](the-assignment.md)), read
  with the intent and its threads for the reasons the assignment
  does not carry; the parent of each item is then a requirement of
  the assignment;
- the intent alone, with its threads, where the project has no
  assignment; the parent of each item is then a position of the
  intent, and no assignment is invented for it.

A file the principal puts in is a third way in. Such a file may be a
transcript, an offer or a document of someone else. It is registered
as a source and cited by path. It is not a parent of the chain. It
yields a draft BRD that is always a work product in `work/` (see
[The work product](the-work-product.md)), never `30-brd.md`. Each
item of that draft cites its place in the source. Where the
principal wants that BRD in the chain, an intent is first handed
over from the same file, and the BRD is then re-parented on that
intent.

Around the parent the BRD also reads:

- the decisions of the project;
- the deliverables of an assignment, as the list of what the BRD is
  asked to bring back;
- the instance's roster of the areas of the enterprise, with which
  of them are mandatory, as a library document cited by path; a
  project with no enterprise around it has no roster;
- a standard the instance follows for BRDs, where it has one, also a
  library document;
- the indexes of the project's sources and research and of every
  library it depends on, always;
- sources and research as the principal directs.

## What it holds

The BRD has four prefixes of its own:

- **BR**: a business requirement, one rule of the business.
- **UC**: a use case, behaviour agreed as a sequence, at user-goal
  level.
- **DEP**: a dependency, what the BRD relies on outside itself.
- **NFR**: a non-functional requirement, a quality by category whose
  value is the stakeholders'.

Beside them it reuses four prefixes of the assignment:

- **OOS**: out of scope.
- **ASM**: an assumption.
- **TBC**: an open question, with an owner.
- **SCR**: a success criterion.

The template gives the BRD these sections, in this order:

- Purpose & Context, and Objective, the only narrative;
- Stakeholders, as roles and never names, each with its involvement
  (responsible, approves, reviews, consulted, informed);
- Scope, with what is in scope, the out-of-scope items, the scope of
  the document (what a reader would expect and this BRD does not
  cover, with where it is covered) and the impacted systems;
- Dependencies;
- Assumptions;
- Use cases, each with its actor, trigger, preconditions, success
  outcome, minimal guarantee, the parent it carries, the rules it
  exercises, its steps and its exceptions;
- Business requirements, in groups by capability or process;
- Touched areas of the enterprise, walked against the instance's
  roster, each area found or not applicable with the reason; a
  project with no enterprise around it writes `Roster: none`;
- Qualities, one NFR per category that applies;
- Transition, where the change replaces something: data to migrate,
  people to train, the cut-over;
- Phasing, always stated, even as "everything in the first phase";
- Success criteria;
- Open questions, each with its owner and whether it blocks
  estimation, closed by the list of what must be supplied from
  outside;
- Terms, every capitalised term defined;
- an appendix of traceability, from each item of the parent to the
  items that carry it.

The header names the parent: `parent: 20-assignment.md` or
`parent: 10-intent.md`. The appendix of traceability is compiled by
Claude at every write from the items and is never edited on its own.

Every BR and UC cites its parent. An NFR cites the item of the parent
it follows from where there is one. Otherwise it cites its category
of the template, because the qualities are asked of every ask
whether the parent named them or not.

The rules for writing the items are the assignment's, made stricter
(see [Requirement style](../reference/requirement-style.md)):

- testability is mandatory: every BR and NFR can be shown met or not;
- one idea per item, though a short list inside an item is allowed
  where it is one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave: a category without a value is a
  TBC with an owner;
- in a draft from a source, a rule cites only the principal's side;
  what another party said is cited by a DEP or a note, never by a
  `shall`;
- `shall` and `shall not` are the wording of a BR and an NFR;
- the steps of a UC are written in the active voice, present tense,
  as a scenario;
- a type is never told by a number: the prefix says what an item is,
  and the group says where it belongs.

### A worked example

A generic business requirement with its parent, a quality whose
value is not yet known, and the open question that holds the place
of the value:

```
### Ordering
- **BR.0010** The Customer shall receive a confirmation of every
  accepted order. (REQ.0040)

## Qualities
- **NFR.0010** Reliability (service hours, availability, recovery):
  The ordering service shall meet the availability the stakeholders
  set (TBC.0030, owner: Service Owner). (category: reliability)

## Open questions
- **TBC.0030** (owner: Service Owner; blocks estimation: yes) What
  availability does the ordering service need?
```

The BR ends with its parent in brackets. The NFR carries no figure,
because no stakeholder has given one. In its place stands a TBC with
the role that owns the answer.

## Complete when

A BRD is complete when three things hold:

- nothing of the parent is left out in silence; an item that is
  delegated, phased later or open with an owner counts as carried,
  and only a silent one does not;
- every matter that must come from outside the forge is named with
  its owner;
- no open question that blocks estimation remains.

When the BRD is complete, Claude offers the principal its approval.
The principal's approval makes the version an integer, as for every
versioned document of the forge. The stakeholders' sign-off is a
different act. It happens outside the forge, where the organisation
does it. The forge records the roles and their involvement in the
Stakeholders section. Where the principal wants the sign-off kept,
it is recorded as one of his decisions.

## How it is found

A BRD is iterated with `/forge brd` (see
[Write a BRD](../use/write-a-brd.md)). There are two ways to make the
first one.

Found together, the principal and Claude run a joint pass. Questions
come first on what the parent does not answer: the stakeholders, the
scope of the document and the phasing. The recast follows, with the
provenance map. Then the items are worked in a walkthrough (one item
per message, each closed by the principal's verdict), group by
group, with the touched areas walked one per item.

Drafted automatically, on the principal's word, Claude first builds
the provenance map from the parent. In a source, every turn of the
principal's side is listed in it as an ask, a question or an
agreement. Claude then walks what the BRD must find and writes the
items from the map, so that nothing of the parent is lost in silence.
It asks nothing. What the parent does not answer it leaves as a TBC
or an ASM. A TBC whose owner the parent does not name carries
`owner: unassigned` until the principal names a role. A step of a use
case or a guarantee that no place of the parent gives is marked as
Claude's reading. Claude returns the draft with three things:

- the provenance map;
- the list of what it assumed;
- the list of what must be supplied from outside.

Nothing is derived from the draft before the principal has judged
it. Where the result lands is the principal's word: in the chain as
`30-brd.md`, or as a work product in `work/` where it is a quick
look.

### What the forge cannot know, it names

Much of a BRD is not in the intent or the assignment at all. It lies
in places the analyst brings from outside:

- the documentation of the supplier and of the systems touched;
- the standards and the regulation that apply;
- what the operations know.

Claude writes none of it from imagination. It gives no value of a
quality the stakeholders have not given. It describes no behaviour
of a system it has not read. It states no rule of a standard it has
not been shown. In each such place stands a DEP or a TBC with an
owner. The owner is a role of the roster or of the stakeholders
wherever one fits, and `unassigned` only where none does. An
assumption never settles an open question: what a TBC asks, no ASM
answers.

Every pass ends with the list of what must be supplied from outside,
said plainly as the analyst's work. The list is divided in two:

- what the forge already holds, by path;
- what must be fetched.

### The reviewers

The BRD has no critic lens of its own. The reviewers are isolated
subagents (agents that run apart from the conversation and read
their inputs from disk):

- the `clarity` lens reads a BRD as it reads an assignment, with the
  BRD's requirement style;
- the `essence` lens compares the BRD with its parent, for drift;
- the challenger persona `business-analyst` hunts the world outside
  the parent: what was written as if a system or a regulation had
  been consulted, the standard that applies and is missing, the
  silent quality, the process that already exists, the stakeholder
  not in the room, solving in the wrong layer, the assumption that is
  a decision, and what cannot be known here; it reads the resource
  indexes first (see
  [Challenger personas](../reference/challenger-personas.md));
- the check `brd` verifies the mechanics: traceability both ways, a
  parent on every item, the sections that may not be silent, terms
  and links, and leftovers of the template (see
  [Checks](../reference/checks.md)).

## Why

The BRD stands as an artefact of the chain so that the delivery can
estimate and the solution design can start from rules, behaviour and
qualities the stakeholders have reviewed. It is built on the
standards of the field: ISO/IEC/IEEE 29148, BABOK and IREB. The
content of an organisation (the roster of areas, the roles, the
systems, the way it publishes) lives in the instance's library. The
engine carries only a generic set of areas to walk.

The analyst works as the principal of a project of his own, because
a project has one principal.

A file someone else gave never becomes a BRD of the chain. The trunk
of the chain is the intent. What someone said does not become the
principal's position by being run through a command (see
[Sources and research](sources-and-research.md)). The file yields a
work product instead, and the way into the chain is an intent handed
over from the same file.

The automatic draft exists because of the principal's way of
working: a BRD pulled fast out of a document to see what it shows.
The provenance map comes before the items, so that nothing of the
parent is lost in silence.

The forge names what it cannot know because it does not do that work
and will not; it reminds. The resource indexes are read in every
pass, so that a standard, a regulation or a report the forge already
holds is never called unknown. Why an assumption may never answer an
open question: the reason is not recorded.

The items follow the shape the standards agree on for a requirement.
The standards know no prefixes, and the forge adds none beyond the
four the BRD needs. Three further choices were rejected:

- **No prefix REF for a related document.** The forge cites a
  document by its path, an item carries no link, and related
  documents are a list without IDs.
- **No range of numbers for the qualities.** A type is never told by
  a number. NFR is a prefix instead, and groups take the next hundred
  by the ID scheme.
- **No FR beside BR and NFR.** A BR carries the functional substance
  at the business level. A functional specification below the BRD
  belongs to the next stage. The line between a BR and an FR would
  have to be drawn at every item, without ground in the content.

The BRD has no critic lens of its own, because the work has three
places already. The clarity and essence lenses read a BRD as they
read an assignment. The mechanics belong to a check. The substance
belongs to a persona. A fourth kind of reviewer would say the same
things in different words.

The stakeholders' sign-off stays outside the forge, where the
organisation does it. Why the forge does not record it as a rule:
the reason is not recorded.

## See also

- [Write a BRD](../use/write-a-brd.md): iterating it with `/forge brd`.
- [The assignment](the-assignment.md): the usual parent of a BRD.
- [The work product](the-work-product.md): what a BRD from someone
  else's file becomes.
- [Sources and research](sources-and-research.md): why what someone
  said is never silently the principal's position.
- [Requirement style](../reference/requirement-style.md): the rule
  set of its items.
- [Challenger personas](../reference/challenger-personas.md): the
  business-analyst persona.
- [Checks](../reference/checks.md): the `brd` check.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
