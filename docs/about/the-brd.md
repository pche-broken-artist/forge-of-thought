---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: c2613a831401bdda
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
`30-brd.md`, which breaks the assignment, or the intent, into rules,
behaviour and qualities that the stakeholders can review and the
delivery can estimate. This page says what a BRD holds, where it
stands in the chain, how it starts, what Claude will not write into
it and why the forge is shaped so. It is for the user who will have
one made, for the extender who wants to know what the definition
owns, and for the evaluator who asks why the BRD names what it
cannot know instead of writing it. How a BRD is iterated step by
step is the how-to [Write a BRD](../use/write-a-brd.md); every term
of the forge is one line of the [Glossary](../reference/glossary.md).

## What it is

A BRD is an artefact of the chain, the versioned documents a project
travels from the brief onward. Its file is `30-brd.md`. It stands
below the assignment and above the solution design; the usual parent
is [The assignment](the-assignment.md), and the layer that may
follow it is [The user stories](the-user-stories.md).

The BRD breaks its parent into three kinds of content:

- rules: the business requirements, grouped so that the
  stakeholders of each area find theirs and review them on their
  own;
- behaviour: what must be agreed as a sequence, written as use cases
  with actors, conditions and exceptions;
- qualities: the non-functional requirements by category, each with
  a value from the stakeholders or left open.

Its purpose is that the delivery teams can estimate and the solution
design can start from it. It admits the solution only at the level
the stakeholders need to agree the ask. The how is left to the
solution design. Where to stop is a judgement: when the teams can
estimate, when more detail would not interest the stakeholders, or
when more detail would be superseded by the design.

The BRD is built on the public standards of the field (ISO/IEC/IEEE
29148, BABOK, IREB) and on the organisation's own standard where the
instance, one installation of the forge, has one. The organisation's
content, that is the roster of areas and which of them are
mandatory, the roles, the systems and the publishing convention,
lives in a library of the instance, a project of its own beside the
others ([Projects and the engine](projects-and-the-engine.md)). The
engine carries only a generic Map of what a BRD finds.

The BRD's definition is `.claude/skills/forge/states/brd.md`, paired
with the template `templates/brd.md`. The definition says how the
BRD is found and owns its rules. The template says what comes out.

## Who writes and reads it

The BRD is found by an analyst working as the principal, the one
whose thinking is being forged, with Claude as partner. A project
has one principal, so the analyst runs a project of his own. The
recast is Claude's work: the whole built from the parent with a
provenance map, the groupings proposed so that every stakeholder
finds theirs and nothing is twice, the use cases drawn from the
parent's process view, the touched areas of the enterprise raised one
by one, and the wording in the Requirement style. The principal
decides the scope of the document, the groupings, which areas
apply, the owner of every open question and every value.

The stakeholders read it, each area its own rules, and the delivery
teams read it to estimate. The solution design starts from it. A
coding agent that takes a chain is given the artefacts that are
available; which of them, a person decides.

The stakeholders' approval happens outside the forge, where the
organisation does it. The forge records the principal's approval as
an integer version, and, in the Stakeholders section, the roles with
their involvement, never names. A decision in `decisions.md` keeps
the sign-off where the principal wants it kept; this is a choice,
not a rule. A report for a third party is a work product, not a BRD.

## Made from

One parent, named by the principal when he asks for the BRD. The
trail of every item leads to it. There are two parents a BRD can
have:

- `20-assignment.md`, read with `10-intent.md` and the threads for
  the reasons the assignment does not carry; the parent of an item
  is then a REQ;
- `10-intent.md` with the threads, where the project has no
  assignment; the parent of an item is then a POS, and no assignment
  is invented for it.

A file someone else gave, such as a transcript, an offer or a
document of another party, is a third way in. It is not a parent of
the chain. Registered through `/ingest` and cited by path, it yields
a draft BRD that is always a work product in `work/`, never
`30-brd.md` ([The work product](the-work-product.md)). The reason is
that what someone said does not become the principal's position by
being run through a command ([Sources and
research](sources-and-research.md)). Each item of such a draft cites
its place in the source, and the place is a turn of the principal's
side. Where the principal wants that BRD in the chain, an intent is
handed over from the same file first and the BRD is re-parented on
it.

Around the parent the BRD is made from:

- `decisions.md` and the ledger, the project's state report, made at
  read time from its documents;
- the DEL items of an assignment, as the list of what the BRD is
  asked to bring back;
- the roster of the instance: a library document, cited by path,
  that names the areas of the enterprise a BRD must consider and
  which of them are mandatory; a project with no enterprise around
  it has no roster, writes `Roster: none` and walks the area against
  nothing;
- the organisation's standard, where the instance has one, a library
  document likewise;
- the resource indexes of the project and of every library it
  depends on (`sources/00-INDEX.md`, `research/00-INDEX.md`,
  `projects/lib-*/sources/00-INDEX.md`), read always, so that a
  standard, a regulation or a report the forge already holds is
  cited and never declared unknown;
- sources and research as the principal directs.

## What it holds

The BRD has four prefixes of its own, beside four it reuses:

- BR: a business requirement, one rule of the business, testable;
- UC: a use case at user-goal level, behaviour agreed as a sequence;
- DEP: a dependency, what the BRD relies on outside itself;
- NFR: a non-functional requirement, a quality by category whose
  value is the stakeholders';
- OOS, ASM, TBC and SCR, reused from the assignment: out of scope,
  assumption, open question, success criterion.

Every BR and UC cites its parent, a REQ or a POS, in brackets at
its end. An NFR cites the REQ or POS it follows from where there is
one, and otherwise its category of the template, since the qualities
are asked of every ask whether the parent named them or not. An item
with neither is a finding of the check. A type is never told by a
number: the prefix says what an item is, and the group says where it
belongs.

The sections of the template, in order:

- Purpose & Context and Objective, the only narrative, from the
  parent's;
- Stakeholders: roles, never names, each with its involvement
  (responsible, approves, reviews, consulted, informed); the roles
  the roster names as signing or reviewing are walked into the
  table, each with its involvement or the reason it has none;
- Scope: what is in and out, the scope of the document, that is what
  this BRD does not cover that a reader would expect and where it is
  covered, and the impacted systems;
- Dependencies: the DEP items, among them what must be supplied from
  outside the forge, each with the role that brings it;
- Assumptions: what the requirements rest on and would change if it
  stopped holding;
- Use cases: each with actor, trigger, preconditions, success
  outcome, minimal guarantee, the parent it carries and the BR items
  it exercises; steps in the active voice, present tense, as a
  scenario and not as a rule; the exceptions where failure,
  compliance or contract matter;
- Business requirements: the BR items grouped by capability or
  process;
- Touched areas of the enterprise: the roster cited by path, or
  `Roster: none`; each area found, with the items that carry it, or
  not applicable with the reason; a mandatory area is never silent;
- Qualities: one NFR per category that applies; the categories are
  the template's (reliability, performance, security and privacy,
  compliance and regulatory, safety, usability and accessibility,
  localisation, maintainability and operability, compatibility and
  interoperability, data integrity), the values the stakeholders';
- Transition: data to migrate, people to train, the cut-over, where
  the change replaces something, as BR items in a group of their own;
- Phasing: always stated, even as "everything in the first phase";
  a phase is a release of the thing, never a version of the document;
- Success criteria: how the stakeholders will know the ask was met;
  may be delegated by the parent;
- Open questions: every TBC with an owner, a role or `unassigned`,
  and whether it blocks estimation; below them the list of what must
  be supplied from outside, each pointing at its DEP or TBC;
- Terms: every capitalised term defined; an entity also says the
  states it may be in and the system it is taken from, with no
  attribute, since how it is taken is the solution design's;
- Appendix: traceability, a table of every parent item and the items
  that carry it, compiled by Claude at every write and verified by
  the `brd` check.

A TBC is defined once, in Open questions, with its owner and whether
it blocks estimation. A BR or an NFR whose rule is not known cites
that TBC in brackets, as it cites its parent. No value anywhere in
the template stands as a requirement: a category without a value is
a TBC with an owner, never a figure from the skeleton.

The Requirement style of the BRD is the assignment's made stricter
([Requirement style and Story style](../reference/requirement-style.md)):

- testability is mandatory: every BR and NFR can be shown met or
  not;
- one idea per item, within reason: a list of two to nine members
  inside an item is allowed where they are one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave;
- a BR and an NFR are written as `shall` / `shall not` in English;
  the steps of a UC are written in the active voice, present tense;
- in a work product from a source, a rule cites the principal's side
  only; what another party said is cited by a DEP or by a note after
  an item, never by a shall.

## A worked example

A generic BR item with its parent, and a generic NFR whose value is
open, in the shape the template defines:

```
### Order intake
- **BR.0010** The Order Desk shall record every Order with its
  Customer, its requested delivery date and its origin channel.
  (REQ.0020)

## Qualities
- **NFR.0010** Reliability (service hours, availability, fault
  tolerance, recovery point, recovery time): Order intake shall meet
  the service hours and the availability the stakeholders set
  (TBC.0010). (REQ.0020)

## Open questions
- **TBC.0010** (owner: Head of Operations; blocks estimation: yes)
  Which service hours and which availability does order intake
  require?
```

The BR ends with the REQ it carries. The NFR names its category,
cites the TBC that holds its missing value and ends with its parent.
The TBC is defined once, with a role as owner and the word on
estimation.

## Complete when

The BRD is complete when three things hold:

- nothing of the parent is left out in silence: delegated, phased
  later or open with an owner is complete, silent is not;
- every matter that must come from outside the forge is named with
  its owner;
- no open question that blocks estimation remains.

## How it is found

The BRD is worked through `/forge brd`
([Write a BRD](../use/write-a-brd.md)). Claude first says whether the
parent is stable enough to be derived from, approved or by the
principal's word, never as a gate. A BRD starts in one of two ways:

- found together: questions up front on the stakeholders, the scope
  of the document and the phasing, which the parent does not answer;
  then the recast with the provenance map; then a walkthrough by
  group, that is one item per message closed with a verdict, the
  touched areas walked one per item;
- drafted automatically, on the principal's word: Claude first
  builds the provenance map from the parent, every item of the
  parent, or every turn of the principal's side in a source, listed
  as an ask, a question or an agreement. It then walks the Map alone
  and writes the items from the map, so that nothing of the parent
  is lost in silence. What the parent does not answer it leaves as a
  TBC or an ASM, asks nothing, and returns the draft with the
  provenance map, the list of what it assumed and the list of what
  must be supplied from outside. A step of a use case or a guarantee
  that no place of the parent gives is marked as Claude's reading,
  as the phasing is. A TBC whose owner the parent does not name
  carries `owner: unassigned`, a valid open state, until the
  principal names the role. Nothing is derived from the draft before
  the principal has judged it.

Where the result lands is the principal's word when he asks: in the
chain as `30-brd.md`, or as a work product in `work/` where it is a
quick look. A file put in runs the automatic way into `work/` only.
A parent that moved runs the pass on what changed. A wording fix is
made directly.

The Map of the definition is walked before the recast, to see what
the parent does not answer, and again at the end. An area may stay
empty when it was considered and found not to apply, said with the
reason where the roster makes the area mandatory. Every pass ends
by naming what changed, what stays open and what must come from
outside. When the completion is reached, Claude offers the approval,
the principal's as the house scheme has it, and says that the
stakeholders' sign-off is the organisation's act.

### What the forge cannot know, it names

Much of a BRD is not in the intent or the assignment at all. It is
in the documentation of the supplier and of the systems touched, in
the standards and the regulation that apply, and in what the
operations know. The analyst brings it from outside. Claude writes
nothing of that from imagination: no value of a quality the
stakeholders have not given, no behaviour of a system it has not
read, no rule of a standard it has not been shown. In their place
stands a DEP or a TBC with an owner. The owner is a role of the
roster or of the stakeholders wherever one fits, and `unassigned`
only where none does. The pass ends with the list of what must be
supplied from outside, said plainly as the analyst's work and
divided in two: what the forge already holds, by path, and what must
be fetched. An assumption never settles an open question: what a TBC
asks, no ASM answers. Claude copies nothing of the parent and
invents no requirement the parent does not carry. What it finds
missing in the parent it raises as a question, and a change of
substance goes to the intent first.

### The reviewers

The BRD has no critic lens of its own. The `clarity` lens reads it
with the BRD's Requirement style, and the `essence` lens compares it
with its parent, as both read an assignment. A challenger persona
`business-analyst` hunts what only someone who knows the business
and its world would see ([Challenger
personas](../reference/challenger-personas.md)):

- the inside written as if the system or the regulation had been
  consulted;
- the standard that applies and is not there;
- the quality that is silent;
- the process that already exists;
- the stakeholder not in the room;
- solving in the wrong layer;
- the assumption that is a decision;
- what cannot be known here.

It reads the resource indexes first. A check `brd` verifies the
mechanics ([Checks](../reference/checks.md)): traceability both ways,
a parent on every item, the sections that may not be silent, terms
and links, and residue of the skeleton.

## Why

The forge takes these positions on the BRD, each with the reason its
owners record.

**Why the BRD breaks the parent into rules, behaviour and
qualities.** So that the stakeholders of each area can review their
part on their own, the delivery can estimate and the solution design
can start. The standards of the field agree on the shape of a
requirement, and the BRD is built on them.

**Why the organisation's content lives in a library of the instance
and the engine carries a generic Map.** The roster of areas, the
roles, the systems and the publishing convention are the
organisation's, not the forge's. A library is a project of its own,
cited by path, so the engine stays generic and a project with no
enterprise around it writes `Roster: none`.

**Why a BRD from someone else's file is a work product and never
the artefact.** The trunk of the chain is the intent, and what
someone said in a meeting does not become the principal's position
by being run through a command. The file yields a work product, and
the way into the chain is an intent handed over from the same file
first.

**Why the provenance map comes first when a BRD is drafted
automatically.** The principal's way of working is a BRD pulled fast
out of a document to see what it shows. Items written before the map
lose asks of the parent; items written from the map lose nothing in
silence.

**Why the forge names what it cannot know instead of writing it.**
The forge does not do the analyst's outside work and will not; it
reminds. A draft that writes a value, a behaviour or a rule from
imagination presents as known what nobody gave, and what another
party said leaks into rules and use cases as if the principal had
decided it. The resource indexes are an input of every BRD so that
what the forge already holds is never called unknown. An assumption
never settles an open question, since what a TBC asks, no ASM
answers.

**Why four prefixes and a stricter style.** The standards agree on
the shape of a requirement and know no prefix. The forge adds only
the prefixes it needs to say what an item is, and rejects what was
added beyond them.

**Why no prefix REF for a related document.** The forge cites a
document by its path, an item carries no link, and related
documents are a list without IDs.

**Why no range of numbers for the qualities.** A type is never told
by a number. NFR is a prefix instead, and groups take the next
hundred by the ID scheme.

**Why no prefix FR beside BR and NFR.** A BR carries the functional
substance at the business level. A functional specification below
the BRD belongs to the next stage, and the line between a BR and an
FR would be drawn at every item without ground in the content.

**Why no critic lens of its own.** The `clarity` and the `essence`
lens read a BRD as they read an assignment, the mechanics are a
check's and the substance a persona's. A fourth kind of reviewer
would say the same things in different words. One critic doing
three jobs is what the forge's three kinds of reviewer were made to
avoid, and the persona finds what the lenses and the check do not.

**Why the stakeholders' sign-off stays outside the forge.** The
reason is not recorded.

## See also

- [Write a BRD](../use/write-a-brd.md): iterating it with
  `/forge brd`.
- [The assignment](the-assignment.md): the usual parent of a BRD.
- [The user stories](the-user-stories.md): the layer that may follow
  a BRD.
- [The work product](the-work-product.md): what a BRD from someone
  else's file becomes.
- [Sources and research](sources-and-research.md): why what someone
  said is never silently the principal's position.
- [Projects and the engine](projects-and-the-engine.md): the library,
  a project of its own, where an instance keeps its roster of areas.
- [Requirement style and Story style](../reference/requirement-style.md):
  the rule set of its items.
- [Challenger personas](../reference/challenger-personas.md): the
  business-analyst persona.
- [Checks](../reference/checks.md): the `brd` check.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
