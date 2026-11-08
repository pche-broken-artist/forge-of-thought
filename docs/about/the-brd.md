---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: f569c3aeef733f2c
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
delivery teams can estimate. This page says what the BRD is, who
writes and reads it, what it is made from, what it holds, when it is
complete, how it is found and why it is shaped as it is. It is for
the user who will write one, for the extender who wants to know where
its rules live, and for the evaluator who wants to see what the forge
does and does not claim to know. How to iterate one is
[Write a BRD](../use/write-a-brd.md).

## What it is

The BRD is an artefact of the chain, the versioned documents a
project's thinking travels through. It stands below the assignment
and above the solution design. Its usual parent is the assignment
([The assignment](the-assignment.md)); where the project has no
assignment, the intent is the parent. The layer that may follow it
is the user stories ([The user stories](the-user-stories.md)).

The BRD breaks its parent into three things:

- rules, the business requirements, grouped so that the stakeholders
  of each area review theirs on their own;
- behaviour that must be agreed as a sequence, the use cases;
- qualities, each by category, with a value from the stakeholders.

It does this so that the delivery can estimate and the solution
design can start. It admits the solution only at the level the
stakeholders need to agree the ask. The how is left to the solution
design. Where to stop is a judgement: the BRD stops when the teams
can estimate, when more detail would not interest the stakeholders,
or when more detail would be superseded by design.

The BRD is built on the standards of the field: ISO/IEC/IEEE 29148,
BABOK and IREB, and the standard of the instance's own organisation
where it has one. The organisation's content, that is, the roster of
areas and which of them are mandatory, the roles, the systems and the
publishing convention, lives in a library of the instance, a project
of its own ([Projects and the engine](projects-and-the-engine.md)).
The engine carries only a generic Map of what a BRD finds. Its
definition is the state file `.claude/skills/forge/states/brd.md`;
its template, the skeleton of the result, is `templates/brd.md`.

## Who writes and reads it

The BRD is written by an analyst working as the principal, the
person whose thinking is being forged, of a project of his own.
Because a project has one principal, the analyst does not share the
project with the people he writes for. Claude, the analyst's partner,
does the recast: the whole of the parent carried over with a
provenance map, the groupings proposed, the use cases drawn from the
parent's process view, the touched areas raised one by one, the
wording in the Requirement style. The principal decides the scope of
the document, the groupings, which areas apply, the owner of every
open question and every value.

The stakeholders and the delivery teams read it. The stakeholders
review the rules of their own area and give the values of the
qualities. The delivery teams estimate from it. The solution design
starts from it.

## Made from

A BRD has one parent, named by the principal when he asks for it,
and the trail of every item leads to that parent. There are three
ways in:

- the assignment `20-assignment.md`, read with the intent and the
  threads (the open matters of the intent, one file each) for the
  reasons the assignment does not carry; the parent of an item is a
  requirement of the assignment, cited as `REQ.NNNN`;
- the intent `10-intent.md` with the threads, where the project has
  no assignment; the parent of an item is a position of the intent,
  cited as `POS.NNNN`; no assignment is invented for it;
- a file the principal puts in, such as a transcript, an offer or a
  document of someone else, registered as a source and cited by
  path.

The first two ways make `30-brd.md`. On the principal's word, when he
asks, they make a work product in `work/` instead, as a quick look;
its conclusion reaches the chain through the intent, as any work
product's does. The third way makes a work product only, never the
artefact ([The work product](the-work-product.md)). Because what
someone said does not become the principal's position by being run
through a command, a BRD from someone else's file is not a document
of the chain ([Sources and research](sources-and-research.md)). In
such a work product each item cites its place in the source, and that
place is a turn of the principal's side. Where the principal wants
that BRD in the chain, an intent is handed over from the same file
first, and the BRD is re-parented on it.

Around the parent, Claude reads:

- `decisions.md`, the principal's decisions with their reasons;
- the ledger, the project's single source of truth for state, made
  at read time;
- the DEL items of the assignment, as the list of what the BRD is
  asked to bring back;
- the roster of the instance: a library document, cited by path,
  that names the areas of the enterprise a BRD must consider and
  which of them are mandatory; a project with no enterprise around
  it has no roster, writes `Roster: none` and walks the areas against
  nothing;
- the organisation's standard, where the instance has one, a library
  document likewise;
- the resource indexes of the project and of every library it
  depends on (`sources/00-INDEX.md`, `research/00-INDEX.md` and the
  same files of each library), read always, so that a standard, a
  regulation or a report the forge already holds is cited and never
  declared unknown;
- sources and research, as the principal directs.

## What it holds

The header carries the version, the status, the project and the
parent, as `parent: 20-assignment.md` or `parent: 10-intent.md`.

The BRD has four prefixes of its own:

- `BR`, a business requirement: one rule of the business, testable;
- `UC`, a use case at user-goal level: behaviour agreed as a
  sequence, with its actor, trigger, preconditions, success outcome,
  minimal guarantee, steps and exceptions;
- `DEP`, a dependency: what the BRD relies on outside itself;
- `NFR`, a non-functional requirement: a quality by category, its
  value the stakeholders' or an open question.

Beside them it reuses `OOS` (out of scope), `ASM` (assumption),
`TBC` (open question, with an owner) and `SCR` (success criterion).
A type is never told by a number: the prefix says what an item is,
the group says where it belongs.

Its sections, in the order of the template:

- Purpose & Context and Objective, the only narrative of the
  document, drawn from the parent's;
- Stakeholders, a table of roles and their involvement, that is,
  responsible, approves, reviews, consulted or informed; never names;
  the roles the roster names as signing or reviewing each appear with
  their involvement or the reason they have none;
- Scope: what is in, what is out as `OOS` items, the scope of the
  document (what this BRD does not cover that a reader would expect,
  and where it is covered), and the impacted systems;
- Dependencies, the `DEP` items, each with the role that brings it;
- Assumptions, the `ASM` items: what the requirements rest on and
  would change if it stopped holding;
- Use cases, the `UC` items;
- Business requirements, the `BR` items in groups by capability or
  process, so that every stakeholder finds theirs and nothing is
  twice;
- Touched areas of the enterprise: the roster cited by path, or
  `Roster: none`, and one row per area, found in the items that
  carry it or not applicable with the reason; a mandatory area is
  never silent;
- Qualities, the `NFR` items, one per category that applies; the
  categories are the template's, drawn from ISO/IEC 25010 and the
  practice of a regulated business; no value comes from the template;
- Transition: data to migrate, people to train, the cut-over, where
  the change replaces something, as `BR` items in a group of their
  own;
- Phasing, always stated, even as "everything in the first phase":
  what each phase of the delivery brings, in what order, with what
  dependencies; a phase is a release of the thing, never a version of
  the document;
- Success criteria, the `SCR` items, which the parent may have
  delegated;
- Open questions, the `TBC` items, each with an owner and whether it
  blocks estimation, followed by the list of what must be supplied
  from outside;
- Terms: every capitalised term of the items defined; a term that is
  a thing the business handles also says the states it may be in and
  the system it is taken from, and no attribute;
- an appendix of traceability, parent by parent, which Claude
  compiles at every write from the items and never edits on its own.

Every `BR` and every `UC` cites its parent. An `NFR` cites the
requirement or position it follows from; where the parent named none,
it cites its category, because the qualities are asked of every ask
whether the parent named them or not. An item with neither is a
finding of the check. An open question is defined once, in Open
questions, with its owner and whether it blocks estimation. A `BR` or
an `NFR` whose rule is not known cites that `TBC` in brackets, as it
cites its parent. The owner of a `DEP` or a `TBC` is a role of the
roster or of the stakeholders wherever one fits; `unassigned` stands
only where none does. An assumption never settles an open question:
what a `TBC` asks, no `ASM` answers.

The wording of the items is the Requirement style of the assignment
made stricter ([Requirement style and Story
style](../reference/requirement-style.md)): testability is mandatory;
one idea per item, with a short list inside it allowed where the
members are one rule; a note after an item carries no requirement;
an item may name the role that owns it; no value that no stakeholder
gave; `shall` and `shall not` in English for a `BR` and an `NFR`; the
steps of a `UC` in the active voice and the present tense, as a
scenario and not as a rule.

## Complete when

The BRD is complete when three things hold:

- nothing of the parent is left out in silence; delegated, phased
  later or open with an owner is complete, silent is not;
- every matter that must come from outside the forge is named with
  its owner;
- no open question that blocks estimation remains.

When the completion is reached, Claude offers the approval, the
principal's, recorded as an integer version. The stakeholders'
sign-off is the organisation's act, outside the forge, where the
organisation does it. The forge records the roles and their
involvement in the Stakeholders section, never names. Where the
principal wants the sign-off kept, it goes into `decisions.md` as a
decision; that is his choice, not a rule.

## How it is found

The BRD is iterated through `/forge brd`
([Write a BRD](../use/write-a-brd.md)). Claude first says whether the
parent is stable enough to be derived from, approved or by the
principal's word, and never as a gate. The first BRD is created from
the template as version 0.1 with its history companion beside it.

Two ways make a new BRD. Found together, the pass is the joint pass
of the assignment's definition, adapted: questions up front on the
stakeholders, the scope of the document and the phasing, which the
parent does not answer; then the recast with the provenance map; then
a walkthrough, that is, the items worked one per message with a
verdict on each, group by group, the touched areas one per item.

Drafted automatically, on the principal's word, Claude first builds
the provenance map from the parent: every item of the parent, or in a
source every turn of the principal's side, listed as an ask, a
question or an agreement. It then walks the Map alone and writes the
items from the map, so that nothing of the parent is lost in silence.
What the parent does not answer it leaves as a `TBC` or as an `ASM`.
A step of a use case or a guarantee that no place of the parent gives
it marks as its own reading, as it marks the phasing. A `TBC` whose
owner the parent does not name carries `owner: unassigned`, a valid
open state, until the principal names the role. It asks nothing and
returns the draft with the provenance map, the list of what it
assumed and the list of what must be supplied from outside. Nothing
is derived from the draft before the principal has judged it.

A file put in runs the automatic way into `work/`. A parent that
moved runs the pass on what changed. A wording fix is made directly.
A write rewrites the document for coherence and never appends; empty
sections and the template's comments are deleted. Every pass ends by
naming what changed, what stays open and what must come from outside.

What the forge cannot know, it names. Much of a BRD is not in the
intent or the assignment at all: it is in the documentation of the
supplier and of the systems touched, in the standards and the
regulation that apply, and in what the operations know. The analyst
brings that from outside. Claude writes nothing of it from
imagination: no value of a quality the stakeholders have not given,
no behaviour of a system it has not read, no rule of a standard it
has not been shown. In its place stands a `DEP` or a `TBC` with an
owner. The pass ends with the list of what must be supplied from
outside, said plainly as the analyst's work and divided in two: what
the forge already holds, by path, and what must be fetched. Claude
copies nothing of the parent, invents no requirement the parent does
not carry, and raises what it finds missing in the parent as a
question. A change of substance goes to the intent first.

The BRD has no reviewer of its own kind. The critic lens `clarity`
reads it with the BRD's Requirement style, and `essence` compares it
with its parent, as both read an assignment. The challenger persona
`business-analyst` hunts what only someone who knows the business and
its world would see: the inside written as if the system or the
regulation had been consulted, the standard that applies and is not
there, the quality that is silent, the process that already exists,
the stakeholder not in the room, solving in the wrong layer, the
assumption that is a decision, and what cannot be known here; it
reads the resource indexes first
([Challenger personas](../reference/challenger-personas.md)). The
check `brd` verifies the mechanics: traceability both ways, a parent
on every item, the sections that may not be silent, terms and links,
and residue of the template ([Checks](../reference/checks.md)).

A page the instance publishes from a BRD is a render, made from a
recipe, and never the artefact. A report for a third party is a work
product, not a BRD. A coding agent that takes a chain is given the
artefacts that are available; which ones, a person decides.

## Why

The BRD exists so that the delivery can estimate and the solution
design can start from rules, behaviour and qualities the stakeholders
have reviewed on their own.

The analyst works as the principal of a project of his own because a
project has one principal.

The organisation's content lives in a library of the instance, and
the engine carries a generic Map. The reason is not recorded.

A BRD from someone else's file is a work product and never an
artefact of the chain, because the trunk of the chain is the intent,
and what someone said in a meeting does not become the principal's
position by a command. The way into the chain is an intent handed
over from the same file.

An automatic draft starts from the provenance map, so that nothing of
the parent is lost in silence. The recorded reason is the principal's
way of working: a BRD pulled fast out of a document to see what it
shows, and the finding that items written before the map lose asks of
the parent.

What the forge cannot know, it names, because the forge does not do
the analyst's work and will not; it reminds. The resource indexes are
an input of every BRD, so that a standard, a regulation or a report
the forge holds is never called unknown. The recorded reason is a
draft that declared unknown what the project's library already held,
and in which what another party said leaked into rules and use cases.

The prefixes are four and the style is the assignment's made
stricter, because the standards of the field agree on the shape of a
requirement and know no prefix.

There is no prefix `REF` for a related document, because the forge
cites a document by its path, an item carries no link, and the
related documents are a list without IDs.

There is no range of numbers for the qualities, because a type is
never told by a number: `NFR` is a prefix instead, and groups take
the next hundred by the ID scheme.

There is no prefix `FR` beside `BR` and `NFR`, because a `BR` carries
the functional substance at the business level, a functional
specification below the BRD belongs to the next stage, and the line
between a `BR` and an `FR` would be drawn at every item without
ground in the content.

There is no critic lens of the BRD's own, because the engine has
three places for three jobs: the `clarity` and `essence` lenses for
the quality of the document, a check for the mechanics, a persona for
the substance. A fourth kind of reviewer would say the same things in
different words. The persona was kept because it found what the
lenses and the check do not.

The stakeholders' sign-off happens outside the forge, where the
organisation does it. The reason is not recorded beyond that.

## A worked example

A generic BRD of an order desk, from an assignment. The rule that is
not known cites its open question in brackets, and the quality
without a value does the same; both open questions are defined once,
in Open questions.

```markdown
## Business requirements

### Order intake
- **BR.0010** The Order Desk shall record every Order with its
  Customer, its lines and the date it was received. (REQ.0020)
- **BR.0020** The Order Desk shall reject an Order whose Customer is
  not active in the Customer Register (TBC.0010). (REQ.0020)
  Note: the rule for an active Customer is the Sales lead's.

## Qualities
- **NFR.0010** Reliability (service hours, availability, fault
  tolerance, recovery point, recovery time): The Order Desk shall
  meet the service hours, availability and recovery the stakeholders
  set (TBC.0020). (category: reliability)

## Open questions
- **TBC.0010** (owner: Sales lead; blocks estimation: no) Which
  Customers count as active in the Customer Register?
- **TBC.0020** (owner: Operations lead; blocks estimation: yes) The
  service hours, the availability and the recovery the Order Desk
  must meet.

**To be supplied from outside:** the service levels of the Customer
Register, from its owner (DEP.0010); the values of TBC.0020.

## Appendix: traceability
| Parent | Carried by |
|---|---|
| REQ.0020 | BR.0010, BR.0020 |
```

The two `BR` items end with their parent, a requirement of the
assignment. The `NFR` ends with its category, because the assignment
named no quality. No figure stands in the `NFR`: its value waits on
the Operations lead, and because that question blocks estimation the
BRD is not complete until it is answered.

## See also

- [Write a BRD](../use/write-a-brd.md): iterating it with `/forge brd`.
- [The assignment](the-assignment.md): the usual parent of a BRD.
- [The user stories](the-user-stories.md): the layer that may follow a BRD.
- [The work product](the-work-product.md): what a BRD from someone else's file becomes.
- [Sources and research](sources-and-research.md): why what someone said is never silently the principal's position.
- [Projects and the engine](projects-and-the-engine.md): the library, a project of its own, where an instance keeps its roster of areas.
- [Requirement style and Story style](../reference/requirement-style.md): the rule set of its items.
- [Challenger personas](../reference/challenger-personas.md): the business-analyst persona.
- [Checks](../reference/checks.md): the `brd` check.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
