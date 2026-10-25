---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 6dcc6b86d91a49b0
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
  - projects/forge/10-intent.md#REJ.0420
  - projects/forge/10-intent.md#REJ.0430
---

# The BRD

The BRD is the business requirements of a project: an artefact of
the chain (one of the versioned documents a thought travels through)
that turns what is asked into rules, behaviour and qualities a
business can review and a delivery team can estimate. This page is
for anyone who wants to know what a BRD holds, how it starts, and
why the forge names what it cannot know instead of writing it: the
user who works one, the extender who changes it, and the evaluator
who judges it.

## What it is

The BRD is the file `30-brd.md`. It stands below the assignment and
above the solution design. It breaks its parent into three kinds of
content:

- rules that the stakeholders of each area can review on their own;
- behaviour that must be agreed as a sequence;
- qualities, each with its value from the stakeholders.

It does this so that the delivery can estimate and the solution
design can start. The BRD admits the solution only at the level the
stakeholders need to agree the ask. The how is left to the solution
design. Where to stop is a judgement: the BRD stops when the teams
can estimate, or when more detail would not interest the
stakeholders or would be superseded by design.

The BRD is built on the standards of the field, such as
ISO/IEC/IEEE 29148, BABOK and IREB. Content that belongs to one
organisation (the roster of areas, the roles, the systems, the way
a BRD is published) lives in the instance's library, that is a
project of shared material beside the chain. The engine carries
only a generic way of finding a BRD.

## Who writes and reads it

The BRD is written by an analyst working as the principal (the
person whose thinking is being forged) of a project of his own. A
subject project has one principal. Claude works as his partner and
does the recast: it builds the whole from the parent, proposes the
groupings so that every stakeholder finds theirs and nothing stands
twice, draws the use cases from the parent's view of the process,
raises the touched areas one by one and writes the wording. The
principal decides:

- the scope of the document;
- the groupings;
- which areas apply;
- the owner of every open question;
- every value.

The stakeholders and the delivery teams read it.

## Made from

A BRD has one parent, named by the principal when he asks for it.
There are three ways in:

- The assignment, read with the intent and the threads for the
  reasons the assignment does not carry. The parent of each item is
  a requirement of the assignment. The assignment is
  [The assignment](the-assignment.md).
- The intent alone, where the project has no assignment. The parent
  of each item is a position of the intent. No assignment is
  invented for it.
- A file the principal puts in, such as a transcript, an offer or a
  document of someone else. It is registered as a source and cited
  by path. This way yields a draft BRD that is always a
  [work product](the-work-product.md) in `work/`, never `30-brd.md`.
  Each of its items cites its place in the source.

A file put in never makes the artefact, because what someone said
does not become the principal's position by being run through a
command. [Sources and research](sources-and-research.md) says why
what someone said is never silently the principal's position. Where
the principal wants such a BRD in the chain, an intent is handed
over from the same file first, and the BRD is re-parented on it.

The first two ways make `30-brd.md`. On the principal's word when he
asks, they make a work product in `work/` instead, as a quick look.

Around the parent Claude also reads:

- the decisions and the state of the project;
- the deliverables of an assignment, as the list of what the BRD is
  asked to bring back;
- the instance's roster of the areas of the enterprise a BRD must
  consider, and which of them are mandatory;
- the indexes of the project's resources and of every library it
  depends on, always;
- sources and research, as the principal directs.

## What it holds

The BRD has four prefixes of its own:

- **BR**: a business requirement, one rule of the business.
- **UC**: a use case at user-goal level.
- **DEP**: a dependency on what the BRD relies on outside itself.
- **NFR**: a non-functional requirement, a quality by category whose
  value is the stakeholders'.

Beside them it reuses four prefixes of the assignment:

- **OOS**: out of scope.
- **ASM**: an assumption.
- **TBC**: an open question, with its owner.
- **SCR**: a success criterion.

The template gives the sections in this order:

- Purpose & Context, and the Objective.
- Stakeholders: roles, never names, each with its involvement
  (responsible, approves, reviews, consulted, informed).
- Scope: what is in and out of scope, the scope of the document
  (what this BRD does not cover that a reader would expect, and
  where it is covered) and the impacted systems.
- Dependencies and Assumptions.
- Use cases: each with its actor, trigger, preconditions, success
  outcome, minimal guarantee, the parent it carries and the rules it
  exercises, then its steps and its exceptions.
- Business requirements, in groups by capability or process.
- Touched areas of the enterprise: each area of the instance's roster
  found or found not to apply, with the reason. A mandatory area is
  never silent. A project with no enterprise around it writes
  `Roster: none`.
- Qualities: one NFR per category that applies, such as reliability,
  performance, security and privacy, or compliance.
- Transition: data to migrate, people to train and the cut-over,
  where the change replaces something.
- Phasing: what each phase of the delivery brings. The phasing is
  always stated, even as "everything in the first phase".
- Success criteria and Open questions. Each open question says its
  owner and whether it blocks estimation. The list of what must be
  supplied from outside closes this section.
- Terms: every capitalised term defined; an entity also says its
  states and the system it is taken from.
- Appendix: traceability, a table of each parent item and the items
  that carry it.

The header names the parent in `parent:`, either `20-assignment.md`
or `10-intent.md`.

Every BR and UC cites its parent. An NFR cites the requirement or
position it follows from where there is one, and otherwise its
category. The items follow the rule set of
[Requirement style](../reference/requirement-style.md): the
assignment's style, made stricter for the BRD. In short:

- every BR and NFR is testable;
- one idea per item, with a short list inside it allowed where it is
  one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave;
- a BR and an NFR say `shall` or `shall not`, and the steps of a use
  case are in the active voice, present tense;
- the prefix says what an item is and the group where it belongs;
  a number never tells a type.

In a work product made from a source, a rule cites only the
principal's side of the file. What another party said is cited by a
DEP or by a note after an item, never by a `shall`.

## Complete when

A BRD is complete when three things hold:

- Nothing of the parent is left out in silence. Delegated, phased
  later or open with an owner counts as complete; silent does not.
- Every matter that must come from outside the forge is named with
  its owner.
- No open question that blocks estimation remains.

When this is reached, Claude offers the approval. The approval is
the principal's, recorded as an integer version. The stakeholders'
sign-off is the organisation's act outside the forge, recorded where
the organisation records it. The BRD keeps the roles and their
involvement in its Stakeholders section, never names. Where the
principal wants the sign-off kept, it goes into the project's
decisions. The reason the sign-off stays outside the forge is not
recorded.

## How it is found

The BRD is iterated with `/forge brd`, as
[Write a BRD](../use/write-a-brd.md) shows. Where there is no BRD
yet, it is found in one of two ways.

**Found together.** Claude first asks what the parent does not
answer: the stakeholders, the scope of the document and the
phasing. It then recasts the parent with a provenance map (a list of
every item of the parent, each traced to where it lands). The
result is worked through as a walkthrough (one item per message,
each closed by the principal's verdict), by group, with the touched
areas taken one at a time.

**Drafted automatically, on the principal's word.** Claude builds
the provenance map from the parent first. In a source, that map
lists every turn of the principal's side as an ask, a question or an
agreement. Claude then writes the items from the map, so that
nothing of the parent is lost in silence. It asks nothing. What the
parent does not answer it leaves as a TBC or an ASM. A TBC whose
owner the parent does not name carries `owner: unassigned`, a valid
open state, until the principal names a role. A step of a use case
or a guarantee that no place of the parent gives is marked as
Claude's reading. Claude returns the draft with three things:

- the provenance map;
- what it assumed;
- what must be supplied from outside.

Nothing is derived from the draft before the principal has judged
it.

### What the forge cannot know, it names

Much of a BRD is not in the intent or the assignment at all. It lies
in places outside the forge:

- the documentation of the supplier and of the systems touched;
- the standards and the regulation that apply;
- what the operations know.

The analyst brings this from outside. Claude writes none of it from
imagination: no value of a quality the stakeholders have not given,
no behaviour of a system it has not read, no rule of a standard it
has not been shown. In its place stands a DEP or a TBC with an
owner. The owner is a role of the roster or of the stakeholders
wherever one fits, and `unassigned` only where none does. An
assumption never settles an open question: what a TBC asks, no ASM
answers.

The pass ends with the list of what must be supplied from outside,
said plainly as the analyst's work. The list is divided in two:

- what the forge already holds, by path;
- what must be fetched.

The resource indexes are read so that a standard, a regulation or a
report the forge already holds is cited and never declared unknown.

### The reviewers

The BRD has no critic lens of its own:

- `/critique clarity` reads it with the BRD's Requirement style.
- `/critique essence` compares it with its parent, for drift.
- `/challenge business-analyst` hunts what only someone who knows
  the business and its world would see, such as an inside written as
  if a system had been consulted, a standard that applies and is
  missing, or a stakeholder not in the room. The persona is listed
  in [Challenger personas](../reference/challenger-personas.md).
- `/check brd` verifies the mechanics: traceability both ways, a
  parent on every item, the sections that may not be silent, terms
  and links, and leftovers of the template. The check is listed in
  [Checks](../reference/checks.md).

## Why

**Why a BRD at all.** It breaks the parent into what the
stakeholders of each area can review on their own, so that the
delivery can estimate and the solution design can start.

**Why the analyst is the principal of his own project.** A subject
project has one principal.

**Why a file put in yields a work product, not the artefact.** The
trunk of the chain is the intent. What someone said in a meeting
does not become the principal's position by being run through a
command. The way into the chain is an intent handed over from the
same file.

**Why a BRD can be drafted automatically.** It is the principal's
way of working: a BRD pulled fast out of a document, to see what it
shows. The provenance map comes before the items so that nothing of
the parent is lost in silence.

**Why the forge names what it cannot know.** The forge does not do
the analyst's work outside it, and will not. It reminds instead.
Writing that content from imagination would put in the BRD values,
behaviour and rules that nobody gave.

**Why no prefix for a related document.** The forge cites a document
by its path. An item carries no link, and related documents are a
list without IDs.

**Why no range of numbers for the qualities.** A type is never told
by a number. NFR is a prefix instead, and groups take the next
hundred by the ID scheme.

**Why no prefix for a functional requirement beside BR and NFR.** A
BR carries the functional substance at the level of the business. A
functional specification below the BRD belongs to the next stage.
The line between a BR and a functional requirement would otherwise
be drawn at every item, without ground in the content.

**Why the prefixes and the style are as they are.** The standards of
the field agree on the shape of a requirement and know no prefix.

**Why no critic lens of its own.** The clarity and the essence lens
read a BRD as they read an assignment. The mechanics belong to a
check, and the substance to a persona. A fourth kind of reviewer
would say the same things in different words. The persona was added
because it finds what the lenses and the check do not.

## A worked example

A generic business requirement with its parent, and a generic
quality whose value is still open. `REQ.NNNN` stands for the
requirement of the assignment the items carry.

```
## Business requirements

### Ordering
- **BR.0010** The Customer shall be able to cancel an order until
  the order is dispatched. (REQ.NNNN)

## Qualities
- **NFR.0020** Performance: The order service shall confirm a
  cancellation within the response time the stakeholders set
  (TBC.0010, owner: <role>). (category: performance)

## Open questions
- **TBC.0010** (owner: <role>; blocks estimation: yes) The response
  time of a cancellation, to be given by the stakeholders.

## Appendix: traceability
| Parent | Carried by |
|---|---|
| REQ.NNNN | BR.0010 |
```

The BR says `shall`, can be shown met or not, and ends with its
parent. The NFR carries no figure, because no stakeholder gave one.
Its value stands open as a TBC with an owner. That TBC blocks
estimation, so this BRD is not yet complete.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
