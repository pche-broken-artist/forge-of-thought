---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 0312193367965adc
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

The BRD is the business requirements of a project: the artefact
`30-brd.md`, which breaks the assignment, or the intent where there is
no assignment, into rules, behaviour and qualities that the
stakeholders can review and the delivery teams can estimate. This page
says what a BRD holds, who works on it, where it comes from, when it is
complete and why it is shaped as it is. It is for the analyst who
writes one, for whoever extends the forge around it, and for whoever
evaluates what the forge promises of it. How a BRD is iterated step by
step is the page [Write a BRD](../use/write-a-brd.md).

## What it is

A BRD is an artefact of the chain, the row of versioned documents a
project's thinking travels. It stands below the assignment and above
the solution design; its usual parent is described on the page
[The assignment](the-assignment.md). The BRD breaks that parent into
three kinds of content:

- rules: business requirements that the stakeholders of each area
  can review on their own;
- behaviour: use cases, where a sequence of steps must be agreed;
- qualities: non-functional requirements by category, with a value
  from the stakeholders or an open question in its place.

The purpose is that the delivery can estimate and the solution design
can start. The BRD admits the solution only at the level the
stakeholders need in order to agree the ask. The how is left to the
solution design.

The BRD is built on the standards of the field, ISO/IEC/IEEE 29148,
BABOK and IREB among them. Its definition, the file that says how it
is found and owns its rules, is `.claude/skills/forge/states/brd.md`.
Its template, the skeleton of what comes out, is `templates/brd.md`.

The content that belongs to a particular organisation is kept out of
the engine: the roster of areas and which of them are mandatory, the
roles, the systems and the publishing convention live in a library of
the instance (one installation of the forge). The engine carries a
generic Map of the definition, the list of what a BRD finds. What a
library is, and that it is a project of its own, is said on the page
[Projects and the engine](projects-and-the-engine.md). The reason this
split was chosen is not recorded.

## Who writes and reads it

The analyst writes it, working as the principal (the person whose
thinking is being forged) of a project of his own. A project has one
principal. Claude is the partner and does the recast: it proposes the
whole from the parent with a provenance map, proposes the groupings so
that every stakeholder finds theirs and nothing is twice, draws the
use cases from the parent's view of the process, raises the touched
areas one by one and words the items in the Requirement style. The
analyst decides the scope of the document, the groupings, which areas
apply, the owner of every open question and every value.

Much of a BRD is not in the intent or the assignment at all. It lies
in the documentation of the supplier and of the systems touched, in
the standards and the regulation that apply, and in what the
operations know. The analyst brings that from outside. Claude writes
nothing of it from imagination: no value of a quality the stakeholders
have not given, no behaviour of a system it has not read, no rule of a
standard it has not been shown. In the place of each stands a
dependency or an open question with an owner. The pass ends with the
list of what must be supplied from outside, said plainly as the
analyst's work and divided in two: what the forge already holds, by
path, and what must be fetched. The forge does not do that work and
will not; it reminds.

Claude copies nothing of the parent and invents no requirement the
parent does not carry. What it finds missing in the parent it raises
as a question. A change of substance goes to the intent first.

The stakeholders read the BRD and review the rules of their area; the
delivery teams read it to estimate; the solution design starts from
it. A coding agent that takes a chain is given the artefacts that are
available, and a person decides which. A report for a third party is
not a BRD; it is a work product.

## Made from

One parent, named by the principal when he asks for the BRD. The
trail of every item leads to it. Two parents are possible:

- `20-assignment.md`, read with `10-intent.md` and the project's
  `threads/` for the reasons the assignment does not carry; the
  parent of an item is then a REQ, a requirement of the assignment;
- `10-intent.md` with `threads/`, where the project has no
  assignment; the parent of an item is then a POS, a position of
  the intent, and no assignment is invented for it.

A file the principal puts in, such as a transcript, an offer or a
document of someone else, is a third way in. It is not a parent of
the chain. Registered as a source and cited by path, it yields a draft
BRD that is always a work product in `work/`, never `30-brd.md`. What
a work product is and how it is worked is said on the page
[The work product](the-work-product.md). The reason is that what
someone said does not become the principal's position by being run
through a command; the page
[Sources and research](sources-and-research.md) says why nothing said
by someone else is silently the principal's position. Each item of
such a draft cites its place in the source. Where the principal wants
that BRD in the chain, an intent is handed over from the same file
first and the BRD is re-parented on it.

Around the parent, Claude reads:

- `decisions.md`, the project's decisions;
- the ledger, the project's state report, made at read time;
- the DEL items of an assignment, as the list of what the BRD is
  asked to bring back;
- the roster of the instance: the areas of the enterprise a BRD must
  consider and which of them are mandatory, a library document cited
  by path; a project with no enterprise around it has no roster,
  writes `Roster: none` and walks the areas against nothing;
- a standard of the organisation for the BRD, where the instance has
  one, a library document likewise;
- the resource indexes of the project and of every library it
  depends on (`sources/00-INDEX.md`, `research/00-INDEX.md`, and the
  indexes of the libraries), always, so that a standard, a regulation
  or a report the forge already holds is cited and never declared
  unknown;
- sources and research, as the principal directs.

## What it holds

The header carries the version, the status, the project and the
parent (`20-assignment.md` or `10-intent.md`). The history lives in
the companion `30-brd.history.md`, never in the body.

The items follow the forge's ID scheme. Four prefixes are the BRD's
own:

- BR, a business requirement: one rule of the business, testable;
- UC, a use case: behaviour agreed as a sequence, at user-goal
  level;
- DEP, a dependency: what the BRD relies on outside itself;
- NFR, a non-functional requirement: a quality by category, its
  value the stakeholders' or an open question.

Four more are reused from the assignment: OOS (out of scope), ASM
(assumption), TBC (open question, with an owner) and SCR (success
criterion). Every BR and UC cites its parent, a REQ or a POS. An NFR
cites the REQ or POS it follows from where there is one, and otherwise
its category of the template. The qualities are asked of every ask
whether the parent named them or not. A type is never told by a
number: the prefix says what an item is, the group says where it
belongs.

The sections, in the order of the template:

- Purpose & Context and Objective: the only narrative, from the
  parent's;
- Stakeholders: roles, never names, each with its involvement
  (responsible, approves, reviews, consulted, informed); the roles
  the roster names as signing or reviewing appear here, each with
  its involvement or the reason it has none;
- Scope: what is in scope, the OOS items, the scope of the document
  (what this BRD does not cover that a reader would expect, and
  where it is covered) and the impacted systems;
- Dependencies: the DEP items, each with the role that brings it;
- Assumptions: the ASM items, what the requirements rest on and
  would change if it stopped holding;
- Use cases: each with its actor, trigger, preconditions, success
  outcome, minimal guarantee, the parent it carries and the BR items
  it exercises, then its steps and its exceptions;
- Business requirements: the BR items grouped by capability or
  process, a TBC under its group where a rule is not known;
- Touched areas of the enterprise: the roster cited by path, or
  `Roster: none`, and one row per area, found or not applicable
  with the reason; a mandatory area is never silent;
- Qualities: one NFR per category that applies, the categories
  taken from ISO/IEC 25010 and the practice of a regulated business
  (reliability, performance, security and privacy, compliance,
  safety, usability and accessibility, localisation,
  maintainability and operability, compatibility, data integrity);
- Transition: data to migrate, people to train, the cut-over, where
  the change replaces something;
- Phasing: always stated, even as "everything in the first phase";
  a phase is a release of the thing, never a version of the
  document;
- Success criteria: how the stakeholders will know the ask was met,
  which the parent may have delegated;
- Open questions: every TBC with its owner and whether it blocks
  estimation, and the list of what must be supplied from outside;
- Terms: every capitalised term defined; a term that is an entity
  of the business also says the states it may be in and the system
  it is taken from, with no attribute listed;
- Appendix, traceability: a table of every parent item and what
  carries it, compiled by Claude at every write and never edited on
  its own.

Nothing in the skeleton stands as a requirement. A value comes from
the stakeholders or is a TBC with an owner. A TBC whose owner is not
yet named carries `owner: unassigned`, a valid open state until the
principal names the role. An assumption never settles an open
question: what a TBC asks, no ASM answers.

The wording of the items is the assignment's Requirement style made
stricter; the whole rule set is on the page
[Requirement style](../reference/requirement-style.md). What the BRD
adds:

- testability is mandatory: every BR and NFR can be shown met or
  not;
- one idea per item, within reason: a short list inside an item is
  allowed where its members are one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave: a category without a value is
  a TBC with an owner, never a figure from the skeleton;
- every BR and UC cites its parent; in a work product from a source
  it cites the path and the place, and the place is a turn of the
  principal's side: what another party said is cited only by a DEP
  or by a note after an item, never by a `shall`;
- `shall` and `shall not` are the wording of a BR and an NFR; the
  steps of a UC are written in the active voice, present tense, as
  a scenario and not as a rule.

## A worked example

A group of business requirements, each closing with its parent, with
an open question under its group:

```markdown
### Order intake
- **BR.0010** The Order Desk shall record every order received
  through the order form within one working day of its receipt.
  (REQ.0030)
- **BR.0020** The Order Desk shall not accept an order without a
  purchase order number. (REQ.0030)
- **TBC.0010** (owner: Head of Order Desk) Whether an order received
  by telephone is recorded at all.
```

A quality whose value the stakeholders have not yet given, so that a
TBC with an owner stands in its place, and the row the TBC makes in
Open questions:

```markdown
## Qualities
- **NFR.0010** Reliability (service hours, availability, recovery
  time): The order register shall meet the service hours and the
  recovery time the stakeholders set (TBC.0020, owner: Head of
  Operations). (category: reliability)

## Open questions
- **TBC.0020** (owner: Head of Operations; blocks estimation: yes)
  The service hours and the recovery time of the order register.
```

The traceability appendix then carries the row `REQ.0030 | BR.0010,
BR.0020`. The NFR cites its category, since in this example the
parent named no quality.

## Complete when

A BRD is complete when three things hold:

- nothing of the parent is left out in silence; delegated, phased
  later or open with an owner is complete, silent is not;
- every matter that must come from outside the forge is named with
  its owner;
- no TBC that blocks estimation is open.

Where to stop is a judgement. It is made when the teams can estimate,
when more detail would not interest the stakeholders, or when more
detail would be superseded by the design.

## How it is found

The BRD is found through `/forge brd`, in the ways the definition
names:

- found together: the joint pass of the assignment, adapted; the
  questions the parent does not answer come first (the
  stakeholders, the scope of the document, the phasing), then the
  recast with the provenance map, then a walkthrough (one item per
  message, each closed with the principal's verdict) by group, the
  touched areas walked one per item;
- drafted automatically, on the principal's word: Claude first
  builds the provenance map from the parent, every item of the
  parent (or, in a source, every turn of the principal's side)
  listed as an ask, a question or an agreement, then walks the Map
  of the definition alone and writes the items from the map, so
  that nothing of the parent is lost in silence; what the parent
  does not answer it leaves as a TBC or an ASM; a step of a use
  case or a guarantee that no place of the parent gives it marks as
  its own reading, as it marks the phasing; it asks nothing and
  returns the draft with the provenance map, the list of what it
  assumed and the list of what must be supplied from outside;
  nothing is derived from the draft before the principal has judged
  it;
- a file put in: the automatic way runs on it into `work/`;
- a parent that moved: the pass runs on what changed;
- a wording fix: made directly.

Where the result of the first two ways lands is the principal's word
when he asks: in the chain as `30-brd.md`, or as a work product in
`work/` where it is a quick look. The first BRD is created from the
template as version 0.1 with its history companion beside it. A write
rewrites the whole for coherence and never appends; empty sections
and the template's comments are deleted.

Before deriving, Claude says whether the parent is stable enough to
be derived from, approved or by the principal's word, never as a gate.
Every pass ends by naming what changed, what stays open and what must
come from outside. When the completion above is reached, Claude
offers the approval, which is the principal's and is recorded as an
integer version. The stakeholders' sign-off is the organisation's
act, outside the forge, where the organisation does it; the BRD
records the roles and their involvement, never names. A decision in
`decisions.md` holds the sign-off where the principal wants it kept;
that is a choice, not a rule.

The BRD has reviewers but no lens of its own. The critic lens
`clarity` reads it with the BRD's Requirement style, and the lens
`essence` compares it with its parent, as both read an assignment.
The challenger persona `business-analyst` hunts what only someone who
knows the business and its world would see: the inside written as if
the system or the regulation had been consulted, the standard that
applies and is not there, the quality that is silent, the process
that already exists, the stakeholder not in the room, solving in the
wrong layer, the assumption that is a decision, and what cannot be
known here; it reads the resource indexes first. The persona is on
the page [Challenger personas](../reference/challenger-personas.md).
The check `brd` verifies the mechanics: traceability both ways, a
parent on every item, the sections that may not be silent, terms and
links, and skeleton residue; it is on the page
[Checks](../reference/checks.md).

## Why

Why the BRD breaks the parent into rules, behaviour and qualities:
so that the stakeholders of each area can review their part on their
own, the delivery can estimate and the solution design can start.

Why the analyst is the principal of a project of his own: a project
has one principal.

Why the organisation's content lives in a library of the instance
while the engine carries a generic Map: the reason is not recorded.

Why a BRD may be drafted automatically: the way of working wants a
BRD pulled fast out of a document to see what it shows. Why the
provenance map comes before the items: so that nothing of the parent
is lost in silence.

Why a file someone else gave yields a work product and never a BRD
of the chain: the trunk of the chain is the intent, and what someone
said in a meeting does not become the principal's position by being
run through a command. The way into the chain is an intent handed
over from the same file, with the BRD re-parented on it.

Why the forge names what it cannot know instead of writing it: the
forge does not do the analyst's work outside the parent and will not;
it reminds. The resource indexes are read always so that a standard,
a regulation or a report the forge holds is never called unknown.

Why four prefixes and a stricter style, and no others: the standards
of the field agree on the shape of a requirement and know no prefix;
what goes beyond them is left out. In particular:

- no prefix REF for a related document: the forge cites a document
  by its path, an item carries no link, and related documents are a
  list without IDs;
- no number range for the qualities: a type is never told by a
  number; NFR is a prefix instead, and groups take the next hundred
  as the ID scheme has it;
- no prefix FR beside BR and NFR: a BR carries the functional
  substance at the business level; a functional specification below
  the BRD belongs to the next stage, and the line between a BR and
  an FR would be drawn at every item without ground in the content.

Why no critic lens of the BRD's own: the engine has three places for
the three jobs. Document quality is a lens's, and `clarity` and
`essence` read a BRD as they read an assignment; the mechanics are a
check's; the substance is a persona's. A fourth kind of reviewer
would say the same things in different words.

Why the stakeholders' sign-off is outside the forge: the reason is
not recorded.

## See also

- [Write a BRD](../use/write-a-brd.md): iterating it with
  `/forge brd`.
- [The assignment](the-assignment.md): the usual parent of a BRD.
- [The work product](the-work-product.md): what a BRD from someone
  else's file becomes.
- [Sources and research](sources-and-research.md): why what someone
  said is never silently the principal's position.
- [Projects and the engine](projects-and-the-engine.md): the library,
  a project of its own, where an instance keeps its roster of areas.
- [Requirement style](../reference/requirement-style.md): the rule
  set of its items.
- [Challenger personas](../reference/challenger-personas.md): the
  business-analyst persona.
- [Checks](../reference/checks.md): the `brd` check.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
