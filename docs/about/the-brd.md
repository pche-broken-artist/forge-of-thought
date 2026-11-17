---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 9e5caa1d5067c58f
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

The BRD is the document of a project that holds its business
requirements, in the file `30-brd.md`. This page is for the people who
use Forge of Thought (the forge), who extend it or who evaluate it. It
says what a BRD holds, how it starts, and why the forge names what it
cannot know instead of writing it.

## What it is

The BRD is an artefact of the [chain](../reference/glossary.md), that
is one of the versioned documents a project builds one below the
other. It stands below the [assignment](the-assignment.md) and above
the solution design. It breaks its parent (the document it is derived
from) into three kinds of content:

- rules, which the stakeholders of each area review on their own;
- behaviour that must be agreed as a sequence;
- qualities, each with a value from the stakeholders.

The purpose is that the delivery teams can estimate from it and the
solution design can start from it.

A BRD admits the solution only at the level the stakeholders need in
order to agree the ask. How the ask is solved is left to the solution
design. A report for a third party is a
[work product](the-work-product.md), not a BRD.

Two files of the engine define it. The definition
(`.claude/skills/forge/states/brd.md`) says what a BRD is to find and
how it is found. The template (`templates/brd.md`) gives the shape of
the result.

## Who writes and reads it

An analyst writes it. He works as the principal (the person whose
thinking is being forged) of a project of his own. Claude is his
partner and does the recast, that is the breaking of the parent into
the items of the BRD.

Claude brings:

- the whole BRD from the parent, with the provenance map (the list of
  every item of the parent, each marked as an ask, a question or an
  agreement);
- groupings in which every stakeholder finds theirs and nothing stands
  twice;
- the use cases, drawn from the parent's process view;
- the touched areas of the enterprise, raised one by one;
- the wording, in the Requirement style of the BRD.

The principal decides:

- the scope of the document;
- the groupings;
- which areas apply;
- the owner of every open question;
- every value.

Claude copies nothing of the parent and invents no requirement the
parent does not carry. What it finds missing in the parent, it raises
as a question. A change of substance goes to the
[intent](../reference/glossary.md) first.

The stakeholders read the BRD to review it. The delivery teams read
it to estimate. A coding agent that takes a chain is given the
artefacts that are available, and a person decides which.

## Made from

A BRD has one parent. The principal names it when he asks for the
BRD, and the trail of every item leads to it. Two documents of the
chain can be the parent:

- The assignment (`20-assignment.md`). It is read with the intent
  (`10-intent.md`) and the [threads](../reference/glossary.md)
  (`threads/`) for the reasons the assignment does not carry. The
  parent of an item is then a requirement of the assignment (a REQ).
- The intent with its threads, where the project has no assignment.
  The parent of an item is then a position of the intent (a POS). No
  assignment is invented for it.

A file someone else gave is a third way in, and it is not a parent of
the chain. Such a file may be a transcript, an offer or another
person's document. It is registered as a source through `/ingest` and
cited by path. It yields a draft BRD that is always a work product in
`work/`, never `30-brd.md`. Each item of the draft cites its place in
the file. The reason is that what someone said is never silently
promoted to the principal's position (see
[Sources and research](sources-and-research.md)). Where the principal
wants that BRD in the chain, an intent is handed over from the same
file first, and the BRD is re-parented on that intent.

Around the parent, these are read:

- The decisions of the project (`decisions.md`).
- The ledger (the file that holds the state of the project).
- The DEL items of an assignment, which list what the BRD is asked to
  bring back.
- The roster of the [instance](../reference/glossary.md) (one
  installation of the forge). The roster names the areas of the
  enterprise a BRD must consider and says which of them are
  mandatory. It is a document of the instance's
  [library](projects-and-the-engine.md) (a project of its own), cited
  by path. A project with no enterprise around it has no roster. Its
  BRD says `Roster: none`, and the areas are walked against nothing.
- The resource indexes of the project (`sources/00-INDEX.md`,
  `research/00-INDEX.md`) and of every library it depends on. They
  are read always. A standard, a regulation or a report that the
  forge already holds is then cited and never declared unknown.
- Sources and research, as the principal directs.

## What it holds

The header carries `version`, `status`, `project` and `parent`. The
`parent` names the file the BRD is derived from: `20-assignment.md` or
`10-intent.md`. The history is kept in the companion
`30-brd.history.md`, never in the BRD.

The items are lists with IDs. A table stands only where columns carry
data. Four prefixes are the BRD's own:

- BR: a business requirement;
- UC: a use case at user-goal level;
- DEP: a dependency on what the BRD relies on outside itself;
- NFR: a non-functional requirement, that is a quality by category
  whose value comes from the stakeholders.

Four more are reused:

- OOS: out of scope;
- ASM: an assumption;
- TBC: an open question;
- SCR: a success criterion.

The sections, in the order of the template:

| Section | What it holds |
|---|---|
| Purpose & Context | Why the BRD exists and what the reader needs in order to review and estimate, from the parent's own Purpose & Context. The related documents are listed by path or name, without IDs. |
| Objective | What must be true at the end. |
| Stakeholders | Roles, never names, each with its involvement: responsible, approves, reviews, consulted or informed. |
| Scope | What is in scope. What is out of scope, as OOS items. The scope of the document: what this BRD does not cover that a reader would expect, and where it is covered. The impacted systems. |
| Dependencies | DEP items: another system, project or document the BRD relies on. What must be supplied from outside the forge is a DEP with the role that brings it. |
| Assumptions | ASM items: what the requirements rest on and would change if it stopped holding. |
| Use cases | UC items. Each has its actor, trigger, preconditions, success outcome and minimal guarantee, the parent it carries, the BR items it exercises and its steps. The exceptions stand where failure, compliance or contract matter. |
| Business requirements | BR items, grouped by capability or process. Every stakeholder finds theirs and nothing stands twice. |
| Touched areas of the enterprise | The roster, cited by path, or `Roster: none`. Each area is found, with the items that carry it, or not applicable, with the reason. |
| Qualities | NFR items, one per category that applies. The categories come from the template (ISO/IEC 25010 and the practice of a regulated business): reliability, performance, security and privacy, compliance and regulatory, safety, usability and accessibility, localisation, maintainability and operability, compatibility and interoperability, data integrity. The values come from the stakeholders. No value of the template stands as a requirement. |
| Transition | BR items in a group of their own: data to migrate, people to train, the cut-over. The section stands only where the change replaces something. |
| Phasing | What each phase of the delivery brings, in what order, with what dependencies. It is always stated, even as "all in the first version". A phase is a release of the thing, never a version of the document. |
| Success criteria | SCR items: how the stakeholders will know the ask was met. The parent may delegate them. |
| Open questions | Every TBC, with its owner and whether it blocks estimation. The list of what is to be supplied from outside, each entry pointing at its DEP or TBC. |
| Terms | Every capitalised term of the items. An entity also names the states it may be in and the system it is taken from. No attribute is listed. |
| Appendix: traceability | One row per item of the parent, with the BRD items that carry it. Claude compiles it at every write from the items. It is never edited on its own. |

The wording of the items follows the Requirement style of the
assignment, made stricter for the BRD. The whole rule set is on
[Requirement style and Story style](../reference/requirement-style.md).
What is stricter:

- Testability is mandatory. Every BR and NFR can be shown met or not.
- An item holds one idea, within reason. A list of two to nine
  members inside an item is allowed where they are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value stands that no stakeholder gave. A category without a
  value is a TBC with an owner, never a figure from the template.
- A TBC is defined once, in Open questions, with its owner and
  whether it blocks estimation. A BR or an NFR whose rule is not
  known cites the TBC in brackets, as it cites its parent.
- Every BR and UC cites its parent: a REQ or a POS. In a work product
  made from a file, the parent is the path and the place, and the
  place is a turn of the principal's side. What another party said is
  cited only by a DEP or by a note after an item, never by a `shall`.
- An NFR cites the REQ or POS it follows from where there is one, and
  otherwise its category of the template. The qualities are asked of
  every ask, whether the parent named them or not. An item with
  neither is a finding of the check.
- A BR and an NFR are worded with `shall` or `shall not`. The steps
  of a UC are written in the active voice, present tense, as a
  scenario and not as a rule: "the Customer submits the order".
- A type is never told by a number. The prefix says what an item is,
  the group says where it belongs.

## Complete when

A BRD is complete when three things hold:

- Nothing of the parent is left out in silence. What is delegated,
  phased later or open with an owner counts as complete. What is
  silent does not.
- Every matter that must come from outside the forge is named with
  its owner.
- No TBC that blocks estimation is open.

Where to stop is a judgement. It is made when the teams can estimate,
when more detail would not interest the stakeholders, or when more
detail would be superseded by design.

When the BRD is complete, Claude offers the approval. The approval
belongs to the principal, and the forge records it as an integer
version. The stakeholders' sign-off is a separate act. It belongs to
the organisation and happens outside the forge, where the
organisation does it. The BRD records the roles with their
involvement in its Stakeholders section, never names. Where the
principal wants the sign-off kept, it is recorded as a decision in
`decisions.md`. That is his choice, not a rule.

## How it is found

A BRD is worked with `/forge brd`. The steps are on
[Write a BRD](../use/write-a-brd.md). This section says how the
finding works.

Claude first says whether the parent is stable enough to be derived
from: it is approved, or the principal says so. This is information,
never a gate. The course then depends on where the BRD starts:

- **Found together.** There is no BRD yet. The questions the parent
  does not answer come first: the stakeholders, the scope of the
  document and the phasing. The recast follows, with the provenance
  map. Then comes the walkthrough (the list worked with the principal
  one item per message, each closed with his verdict), group by
  group, the touched areas one per item.
- **Drafted automatically.** There is no BRD yet, and the principal
  asks for a draft. Claude builds the provenance map from the parent
  first. It then walks the Map of the definition alone and writes the
  items from the provenance map. It asks nothing. What the parent
  does not answer, it leaves as a TBC or as an ASM. A step of a use
  case or a guarantee that no place of the parent gives is marked as
  Claude's reading, as the phasing is. A TBC whose owner the parent
  does not name carries `owner: unassigned`, a valid open state until
  the principal names the role. Claude returns the draft with the
  provenance map, the list of what it assumed and the list of what
  must be supplied from outside. Nothing is derived from the draft
  before the principal has judged it.
- **From a file someone else gave.** The automatic way runs on the
  file, and the result goes into `work/`. The provenance map then
  lists every turn of the principal's side.
- **After the parent moved.** The pass runs on what changed.
- **A wording fix.** It is made directly.

Where the result of the first two ways lands is the principal's word
when he asks. It lands in the chain as `30-brd.md`, or in `work/` as
a work product where it is a quick look. The conclusion of such a
quick look reaches the chain through the intent first, as with any
work product.

The definition carries a Map: the list of what a BRD finds. Claude
walks it before the recast, to see what the parent does not answer,
and again at the end. The Map of the engine is generic:

- the stakeholders, as roles;
- the scope of the work and the scope of the document;
- the cut of the parent: what is carried now, what is phased later
  and what is delegated onward;
- the process view: the behaviour that must be agreed as a sequence;
- the rules;
- the touched areas of the enterprise;
- the systems and the dependencies;
- the qualities;
- the things the business talks about: the entities, their states and
  the system each is taken from;
- what comes from outside;
- the transition;
- the phasing;
- the assumptions;
- success;
- the terms;
- what stays open.

An area may stay empty when it was considered and found not to apply.
Where the roster makes the area mandatory, the BRD gives the reason.
The roles the roster names as signing or reviewing are walked into
the Stakeholders table, each with its involvement or the reason it
has none.

### What the forge cannot know, it names

Much of a BRD is not in the intent or the assignment at all. It is
in three places outside them:

- the documentation of the supplier and of the systems touched;
- the standards and the regulation that apply;
- what the operations know.

The analyst brings it from outside. The forge does not do that work.
It reminds. Claude writes none of it from imagination:

- no value of a quality the stakeholders have not given;
- no behaviour of a system it has not read;
- no rule of a standard it has not been shown.

In its place stands a DEP or a TBC with an owner. The owner is a role
of the roster or of the stakeholders wherever one fits, and
`unassigned` only where none does. The pass ends with the list of
what must be supplied from outside, said plainly as the analyst's
work. The list is divided in two: what the forge already holds, by
path, and what must be fetched.

An assumption never settles an open question. What a TBC asks, no ASM
answers.

### The reviewers

A BRD has no critic [lens](../reference/glossary.md) of its own.
Three reviewers read it, each for a different thing:

- The critic reads it through two lenses it already has.
  `/critique clarity` reads the BRD with the BRD's Requirement style.
  `/critique essence` compares it with its parent and looks for
  drift.
- The challenger [persona](../reference/challenger-personas.md)
  `business-analyst` hunts what only someone who knows the business
  and its world would see: what was written from the parent though it
  belongs to the world outside it. It reads the resource indexes
  first. It runs as `/challenge business-analyst`.
- The [check](../reference/checks.md) `brd` verifies the mechanics.
  It runs as `/check brd`. The mechanics are:
  - traceability both ways;
  - a parent on every item;
  - the sections that may not be silent;
  - terms and links;
  - residue of the template.

## Why

**Why it exists.** The delivery must be able to estimate and the
solution design must be able to start. The stakeholders of each area
must be able to review their rules on their own. The BRD is built on
the standards of the field (ISO/IEC/IEEE 29148, BABOK, IREB).

**Why the analyst is the principal of a project of his own.** A
project on a subject has one principal.

**Why the engine carries a generic Map.** The content of the
organisation lives in the instance's library, not in the engine. That
content is the roster of areas and which of them are mandatory, the
roles, the systems and the publishing convention. The reason is not
recorded.

**Why a draft on the principal's word, and the provenance map
first.** The recorded reason is the principal's way of working: a BRD
pulled fast out of a document, to see what it shows. The provenance
map comes first for a reason of its own. Items written before it lose
what the parent asks.

**Why a file from someone else never makes `30-brd.md`.** The trunk
of the chain is the intent. What someone said in a meeting does not
become the principal's position by being run through a command. The
file therefore yields a work product, and the way into the chain is
an intent handed over from the same file.

**Why the forge names what it cannot know.** Two failures are
recorded as the reason. A draft that does not read what the forge
holds calls it unknown. A source's answers leak into rules and use
cases.

**Why these prefixes and no others.** The standards of the field
agree on the shape of a requirement and know no prefix. Three things
a reader might expect are absent:

- No prefix REF for a related document. The forge cites a document by
  its path, an item carries no link, and related documents are a list
  without IDs.
- No range of numbers for the qualities. A type is never told by a
  number. NFR is a prefix instead, and groups take the next hundred,
  as the ID scheme has it.
- No prefix FR beside BR and NFR. A BR carries the functional
  substance at the business level. A functional specification below
  the BRD belongs to the next stage. The line between a BR and an FR
  would be drawn at every item without ground in the content.

**Why no lens of its own.** The clarity lens and the essence lens
read a BRD as they read an assignment. The mechanics belong to a
check and the substance to a persona. The engine has these three
places for the three jobs. A fourth kind of reviewer would say the
same things in different words.

**Why the sign-off happens outside the forge.** The reason is not
recorded.

## A worked example

A generic example, taken from no project: one business requirement
with its parent, and one quality whose value nobody has given yet.

```markdown
## Business requirements

### Ordering
- **BR.0010** The Shop shall confirm every accepted Order to the
  Customer. (REQ.0040)

## Qualities
- **NFR.0010** Reliability (service hours, availability, fault
  tolerance, recovery point, recovery time): The Shop shall meet the
  service hours, availability and recovery the stakeholders set
  (TBC.0010). (category: reliability)

## Open questions
- **TBC.0010** (owner: Operations lead; blocks estimation: yes) Which
  service hours, availability and recovery must the Shop meet?
```

- `BR.0010` is one sentence that can be shown met or not. It is
  worded with `shall`. It cites its parent in brackets: a requirement
  of the assignment.
- `NFR.0010` carries no figure. No stakeholder has given one. It
  cites the open question `TBC.0010` in brackets. It names its
  category of the template. The parent named no quality here.
- `TBC.0010` is defined once, in Open questions, with the role that
  owns it and whether it blocks estimation. No assumption may answer
  it.
- The capitalised terms (Shop, Order, Customer) are each defined in
  Terms.

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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
