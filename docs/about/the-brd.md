---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: d2297e50698eae6a
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

The BRD is the business requirements document of a project: the
artefact of the chain that turns what was asked into rules, behaviour
and qualities that stakeholders can review and delivery teams can
estimate. This page explains what a BRD holds, how it starts, who
reviews it, and why the forge names what it cannot know instead of
writing it. It is for anyone who writes a BRD, extends the forge or
wants to judge whether the layer is sound.

## What it is

The BRD is the file `30-brd.md`. It is an artefact of the chain (a
versioned document the principal composes with Claude). It stands
below the assignment and above the solution design.

A BRD breaks its parent into three kinds of content:

- rules: business requirements that the stakeholders of each area
  can review on their own;
- behaviour: use cases, where something must be agreed as a sequence
  of steps;
- qualities: non-functional requirements by category, with values
  that come from the stakeholders.

The purpose is that the delivery can estimate and the solution design
can start. A BRD admits the solution only at the level the
stakeholders need to agree the ask. The how is left to the solution
design. Where to stop is a judgement: detail ends when the teams can
estimate, or when more would not interest the stakeholders, or when
it would be superseded by design.

The BRD is built on the public standards of the field, such as
ISO/IEC/IEEE 29148, BABOK and IREB. The engine carries a generic Map
of what a BRD must find. The content of a particular organisation
(its roster of areas and which of them are mandatory, its roles, its
systems, its publishing convention) lives in the instance's library,
not in the engine. An instance is one installation of the forge.

## Who writes and reads it

The BRD is written by an analyst working as the principal of a
project of his own. The principal is the person whose thinking is
forged and who has the final word on every content. A project has
one principal, so the analyst takes that role in his own project.

Claude is the partner and does the recast. Claude builds the whole
from the parent with a provenance map, proposes groupings so that
every stakeholder finds their part and nothing appears twice, draws
the use cases from the parent's process view, raises the touched
areas one by one and words the items. The principal decides:

- the scope of the document;
- the groupings;
- which areas apply;
- the owner of every open question;
- every value.

Claude copies nothing of the parent and invents no requirement the
parent does not carry. What Claude finds missing in the parent is
raised as a question. A change of substance goes to the intent
first.

The stakeholders and the delivery teams read the BRD.

## Made from

A BRD has one parent, named by the principal when he asks for it.
There are two parents of the chain and one third way in.

- The assignment, read with the intent and the threads for the
  reasons the assignment does not carry. The parent of each item is
  a requirement of the assignment. See [The
  assignment](the-assignment.md).
- The intent with its threads, where the project has no assignment.
  The parent of each item is a position of the intent. No assignment
  is invented for it.
- A file the principal puts in: a transcript, an offer, a document
  of someone else. It is registered as a source and cited by path.
  It yields a draft BRD that is always a work product in `work/`,
  never `30-brd.md`. See [The work product](the-work-product.md).

A file put in never becomes the artefact. What someone said does not
become the principal's position by being run through a command. See
[Sources and research](sources-and-research.md). Where the principal
wants such a BRD in the chain, an intent is handed over from the same
file first, and the BRD is then re-parented on it.

The first two ways make `30-brd.md`. On the principal's word when he
asks, they may instead make a work product in `work/` as a quick
look. Its conclusion reaches the chain through the intent, as any
work product's does.

Around the parent, a BRD also reads:

- `decisions.md` of the project;
- the deliverables an assignment lists, as what the BRD is asked to
  bring back;
- the instance's roster of the areas of the enterprise, a library
  document cited by path;
- the resource indexes of the project and of every library it
  depends on, always;
- sources and research, as the principal directs.

The resource indexes are always read. This is so that a standard, a
regulation or a report the forge already holds is cited and never
declared unknown.

## What it holds

The sections come from the template `templates/brd.md`. Its header
carries `parent:`, which names `20-assignment.md` or `10-intent.md`.

- Purpose & Context, and Objective: the only narrative.
- Stakeholders: roles with their involvement (responsible, approves,
  reviews, consulted, informed), never names.
- Scope: in scope, out of scope, the scope of the document (what a
  reader would expect that this BRD does not cover, and where it is
  covered), and the impacted systems.
- Dependencies: what the BRD relies on outside itself.
- Assumptions: what the requirements rest on.
- Use cases: at user-goal level, with actor, trigger, preconditions,
  success outcome, minimal guarantee, the parent it carries and a
  table of steps with exceptions.
- Business requirements: grouped by capability or process.
- Touched areas of the enterprise: each area of the roster found, or
  not applicable with the reason. A project with no enterprise
  around it writes `Roster: none`.
- Qualities: one item per category that applies.
- Transition: data to migrate, people to train, the cut-over, where
  the change replaces something.
- Phasing: always stated, even as "everything in the first phase".
- Success criteria.
- Open questions: each with an owner and whether it blocks
  estimation, followed by the list of what must be supplied from
  outside.
- Terms: every capitalised term defined.
- Appendix: traceability, a table from each parent item to the items
  that carry it.

### The items

A BRD has four prefixes of its own:

- `BR`: a business requirement;
- `UC`: a use case at user-goal level;
- `DEP`: a dependency on something outside the BRD;
- `NFR`: a non-functional requirement, that is a quality by category
  whose value is the stakeholders'.

Beside them it reuses `OOS` (out of scope), `ASM` (assumption), `TBC`
(open question) and `SCR` (success criterion).

Every BR and UC cites its parent. An NFR cites the parent it follows
from where there is one. Otherwise it cites its category of the
template, because the qualities are asked of every ask, whether the
parent named them or not. A type is never told by a number: the
prefix says what an item is, and the group says where it belongs.

The rule set of the items is the assignment's, made stricter. See
[Requirement style](../reference/requirement-style.md). The stricter
rules are these:

- every BR and NFR is testable;
- one idea per item, though a short list inside an item is allowed
  where it is one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave: a category without a value is a
  TBC with an owner, never a figure from the template;
- in a work product from a source, a rule cites only the principal's
  side; what any other party said is cited only by a DEP or a note;
- `shall` and `shall not` word a BR and an NFR, and the steps of a UC
  are written in the active voice, present tense, as a scenario.

## Complete when

A BRD is complete when three things hold.

- Nothing of the parent is left out in silence. Delegated, phased
  later or open with an owner counts as complete. Silent does not.
- Every matter that must come from outside the forge is named with
  its owner.
- No open question that blocks estimation remains.

When this is reached, Claude offers the approval. The approval is the
principal's, recorded as an integer version. The stakeholders'
sign-off is the organisation's act, outside the forge. The forge
records the stakeholders only as roles with their involvement. A
decision in `decisions.md` keeps the sign-off where the principal
wants it kept. This is a choice, not a rule. The reason the sign-off
stays outside the forge is not recorded.

## How it is found

You iterate a BRD with `/forge brd`. See [Write a
BRD](../use/write-a-brd.md) for the steps.

A BRD is found in one of two ways.

- Found together. Questions come first on what the parent does not
  answer: the stakeholders, the scope of the document and the
  phasing. Then the recast with the provenance map follows, and then
  a walkthrough by group. A walkthrough is the forge's way of working
  a list of items with the principal one at a time, each closed by
  his verdict. The touched areas are walked one per item.
- Drafted automatically, on the principal's word. Claude first
  builds the provenance map from the parent: every item of the
  parent, or in a source every turn of the principal's side, listed
  as an ask, a question or an agreement. Then Claude writes the items
  from the map, asks nothing, and returns the draft with three
  things: the map, what was assumed, and what must be supplied from
  outside.

In an automatic draft, what the parent does not answer stays as a TBC
or an ASM. A TBC whose owner the parent does not name carries `owner:
unassigned`. This is a valid open state until the principal names
the role. A step of a use case or a guarantee that no place of the
parent gives is marked as Claude's reading. Nothing is derived from
the draft before the principal has judged it.

### What the forge cannot know, it names

Much of a BRD is not in the intent or the assignment at all. It is
in:

- the documentation of the supplier and of the systems touched;
- the standards and the regulation that apply;
- what the operations know.

The analyst brings this from outside. The forge does not do that
work. It reminds.

Claude writes nothing of it from imagination. That means no value of
a quality the stakeholders have not given, no behaviour of a system
Claude has not read, and no rule of a standard Claude has not been
shown. In its place stands a DEP or a TBC with an owner. The owner is
a role of the roster or of the stakeholders wherever one fits, and
`unassigned` only where none does.

An assumption never settles an open question. What a TBC asks, no ASM
answers.

The pass ends with the list of what must be supplied from outside. It
is divided in two: what the forge already holds, by path, and what
must be fetched.

### The reviewers

A BRD has no critic lens of its own. Its reviewers run as isolated
subagents (separate runs of Claude that never see the working
conversation).

- The `clarity` lens reads it with the BRD's Requirement style, as it
  reads an assignment.
- The `essence` lens compares it with its parent.
- The challenger persona `business-analyst` hunts what only someone
  who knows the business and its world would see. It reads the
  resource indexes first. See [Challenger
  personas](../reference/challenger-personas.md).
- The check `brd` verifies the mechanics: traceability both ways, a
  parent on every item, the sections that may not be silent, terms
  and links, and leftovers of the template. See
  [Checks](../reference/checks.md).

The persona looks for, among other things:

- the inside written as if the system or the regulation had been
  consulted;
- a standard that applies and is not there;
- a quality that is silent;
- a process that already exists;
- a stakeholder not in the room;
- solving in the wrong layer;
- an assumption that is really a decision;
- what cannot be known here.

## Why

**Why the forge names what it cannot know.** The content of the
supplier's documentation, the standards and the operations' knowledge
is not in the parent. Written from imagination, it would look like a
requirement while resting on nothing. A DEP or a TBC with an owner
says plainly what is missing and who brings it.

**Why a provenance map comes first.** The map is built from the
parent before the items are written. This is so that nothing of the
parent is lost in silence.

**Why the automatic draft exists.** It serves the principal's way of
working: a BRD pulled fast out of a document, to see what it shows.

**Why a BRD from someone else's file is a work product.** The trunk
of the chain is the intent. What someone said in a meeting does not
become the principal's position by a command. The way into the chain
is an intent handed over from the same file.

**Why there is no prefix `REF`.** The forge cites a document by its
path. An item carries no link. Related documents are a list without
IDs.

**Why qualities have no range of numbers.** A type is never told by a
number. NFR is a prefix instead, and groups take the next hundred by
the ID scheme.

**Why there is no `FR`.** A BR carries the functional substance at
the business level. A functional specification below the BRD belongs
to the next stage. The line between a BR and an FR would otherwise be
drawn at every item, without ground in the content.

**Why the prefixes and the stricter style.** The standards agree on
the shape of a requirement and know no prefix. Anything added beyond
them was rejected.

**Why no lens of its own.** The clarity and essence lenses read a BRD
as they read an assignment. The mechanics belong to a check, and the
substance to a persona. A fourth kind of reviewer would say the same
things in different words.

**Why a persona was added.** A single reviewer doing three jobs was
split into the three places the forge has for them: a lens, a check
and a persona. The persona finds what the lenses and the check do
not.

## A worked example

A generic group of business requirements, with an item and its
parent, and a quality whose value is still open:

```markdown
### Order intake
- **BR.0010** The service shall record every order with the time it
  was received. (REQ.0120)

## Qualities
- **NFR.0010** Reliability (service hours, availability, fault
  tolerance, recovery point, recovery time): The service shall meet
  the service hours, availability and recovery the stakeholders set
  (TBC.0010, owner: Operations lead). (category: reliability)

## Open questions
- **TBC.0010** (owner: Operations lead; blocks estimation: yes) What
  availability and recovery time does the service need?
```

The BR cites its parent, a requirement of the assignment. The NFR
names no figure, because no stakeholder gave one. Its value stands as
an open question with a role as owner. Because the question blocks
estimation, the BRD is not complete until it is answered.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
