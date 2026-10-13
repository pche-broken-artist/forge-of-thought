---
project: forge
date: 2026-10-13
topic: the BRD layer of a colleague's fork re-read against today's engine - what it is, how it held on real work, what the definition of a `brd` artefact takes from it and refuses
status: immutable
derived_from: the principal's word of 2026-10-13 (the fork's BRD implementation to be extracted, judged and converted into the engine's own artefact); the bundle projects/lib-allwyn/sources/fork-brd/ (fourteen files, catalogued in its 00-INDEX.md; the template, the two skills, the agent, the critique template and the three critique rounds read whole, the three BRDs in their control, scope, use-case, requirement and traceability sections, the group standard's prose and its rules DS, AP, SIBR, RT, GR, the tutorial's impact analysis); research/2026-09-07-brd-layer-fork-analysis.md; 10-intent.md v5.8 (POS.0700, POS.1310, POS.1320, POS.1350, POS.1360, POS.1430, POS.1520); threads.md (THR.0360); decisions.md (DEC.0060); .claude/skills/forge/states/assignment.md; .claude/agents/critic-clarity.md
---

# Research: the BRD layer of the fork against today's engine

## Question

A business analyst built a BRD layer in a fork of the engine in
August 2026, at intent 2.8, adapted to Gemini. What is that
implementation, how did it hold on real work, and what does the
definition of a `brd` artefact of today's engine take from it and
refuse? The note of 2026-09-07 answered the first two questions
against intent 4.0; since then the engine has the shape of a
definition in seven blocks with a Map (POS.1310, POS.1320), the
handing-over of an artefact, the history log, the work product,
the checks as agents, the horizon rule (POS.1360) and the command
`/new-artefact` (POS.1430). This note re-reads the fork against
that engine and ends in the material for `/new-artefact brd`: the
seven blocks, the template, the prefixes, the reviewers, and what
belongs to the instance.

The fork's files are not quoted here beyond what the mechanisms
need: they carry names, the company's project content and the
group's internal standard, and this project is public. They stand
in the company library and are cited by path.

## What the fork contains, and what changed since 2026-09-07

The fork is as the earlier note found it; nothing in it moved
since. Its layer: a chain `00-brief → 10-intent → 20-assignment →
30-brd`; a template of nine chapters (document control with a
Version History, a RACI and a six-pillar stakeholder-domain
checklist; context and objective; scope, OOS, DEP, ASM, impacted
systems; use cases with a header, step and exception tables; core
business requirements by capability area; stakeholder-domain and
NFR requirements; success criteria; terminology; a REQ → BR
traceability matrix); the prefixes `BR`, `UC`, `DEP` and a document
code for the wiki; a drafting skill ("transform, never duplicate";
all in tables; atomic, testable, shall-language; what to avoid;
discovery questions inline as `TBC` with a role); a critic agent of
its own with a regression-first report and pass-fail checklists;
three BRDs (the agentic platform 0.4 after three critique rounds,
FLOW:BA 0.2, the forge itself 0.1); the group's standard v0.3 and
tutorial.

What changed is the engine. In September 2026 the engine had no
definition shape: a state file said how `/forge` iterates an
artefact, in prose. Today every artefact has a definition in seven
blocks and a Map, the assignment is found in a joint pass with a
provenance map (POS.1350), the horizon is divided across the
layers with the BRD carrying the phasing (POS.1360), a reviewer is
a lens, a persona or a check of a fixed kind, and a new kind of
artefact is born through one command that forgets nothing
(POS.1430). The question is no longer "what to borrow" but "where
each borrowed thing lands in a definition".

## Key findings

Epistemic tags as in the earlier note: **[C]** consensus in the
field, **[S]** one standard, **[F]** the fork's own, **[M]** my
judgement.

### 1. The verdict of 2026-09-07 stands

Re-read whole, the fork's material confirms the eight ideas worth
borrowing and the nine anti-patterns of the earlier note; none is
withdrawn here and none is repeated. Two of the anti-patterns are
stronger on re-reading, with the engine's own rules now behind
them: "all in tables" against prime directive 7 as it stands
(structure over prose, items with IDs; a recipe may tabulate for a
wiki), and the instance facts in the engine against POS.0950 and
the public repository the engine now is. [M]

### 2. How the layer held on real work: three BRDs, three rounds

The agentic-platform BRD went from 0.1 to 0.4 under the fork's
critic. Round one raised ten findings on 0.1: two of high severity
on divergence from the assignment (an operational tier hierarchy
inverted across scope, use cases, requirements and terms; a
traceability matrix mapping to wrong parent IDs), one high on the
silent omission of ten governance requirements of the assignment,
one high on missing stakeholder domains, then numbering,
untestable wording, non-atomic items, solutioning, glossary gaps
and a missing table of contents. Round three found nothing new,
fifteen findings resolved, ten discovery questions open and
assigned to roles. [F]

Read against the engine's reviewer kinds, the catches sort
themselves: the four high findings are drift between layers and
omission, which is the `essence` lens's job (POS.0410); the
untestable, non-atomic, solutioning and glossary findings are the
`clarity` lens's with a BRD rule set; the numbering, the matrix's
completeness, the table of contents and the terms-defined rule are
mechanical and a check's. The fork's one critic did all three
jobs; the engine has three places for them and need not add a
kind. [M]

The FLOW:BA BRD (0.2, one round) shows the template on a process
initiative: five use cases of the analysis process itself, eight
requirement groups, the NFR table with the template's example
values carried over. The BRD of the forge (0.1, never reviewed)
is the control case: a tool with no player, no payment and no
regulator fills every row of the six-pillar checklist with "Yes"
and a sentence, invents five success criteria with thresholds,
carries the template's availability and recovery values, and
cites a repository link and a wiki page among its references. A
roster that must be filled is filled; a template that carries a
value writes the requirement. Both confirmed on real content. [M]

### 3. The fork's drafting procedure in today's engine's words

The `draft-brd` skill, read as an elicitation, is the second phase
of the assignment's joint pass (POS.1350) alone: a recast of the
whole from the parent with a provenance map, which the fork calls
the traceability matrix. It has no first phase (questions up front
on what the parent does not answer) and no third (a walkthrough by
group); the critique rounds then did the work the walkthrough
would have done, at the price of three immutable reports. Its
"open discovery questions" are `TBC` items with a role as owner,
placed under the group they belong to; its "transformation, never
duplication" is the essence rule; its stakeholder domains are one
area of a Map, "who is touched", with a roster that is the
instance's. [M]

The group's tutorial adds what the fork's skill does not carry:
the **impact analysis** as a step of the process, after the core
requirements, with four mandatory areas (data migration, social
value, security, technology operations) and optional ones
(finance, compliance, BI, UX, operations), each tracked as a task
with an owner and closed before the BRD closes; the requirements
found there are written like any other. [S] In the engine this is
the Map walked over the areas the instance declares mandatory,
each "found" or "considered and found not to apply, with the
reason", never silently empty; the roster and which of its areas
are mandatory are the instance's, in the library (POS.1020). [M]

### 4. What the group's standard says the BRD is, and where that puts it in the chain

The standard's own words: the BRD "is typically the starting point
for an approved project", "is intended to set delivery teams up
for success by clearly stating the high-level business rules,
expectations and requirements", "facilitates analysis of the
change impact across the organisation and is often used as the
basis for estimations", "is often not agnostic of the solution:
teams should come together to break the back of the project ask"
with architects and subject-matter experts, and "will defer lower
levels of analysis to the next stage of delivery" by a judgement
call: when the teams can estimate, when lower detail is of limited
interest to the stakeholders, when the document is already long
and the rest is low risk, or when more detail would be superseded
by the next step. It distinguishes the scope of work (what is and
is not done) from the scope of the document (what this BRD does
not cover that a reader might expect, with where it is covered).
It asks for stakeholders early with their involvement (RACI or at
least who approves), assumptions tracked because they may stop
holding, related documents that are related and not necessary,
terms specific to the document, logical groupings that are MECE,
and of every requirement: a full sentence, testable, written once,
atomic within reason, at the appropriate level of detail, uniquely
numbered, without vague modals, without priority words, with
acronyms and technical terms defined. Notes after a requirement
are allowed and must carry no requirement; lists of two to nine
items in one requirement are allowed; a requirement may name the
stakeholder who owns it and the team that delivers it; "(TBC)" and
questions in red mark what needs discussion. [S]

In the engine's chain this places the BRD exactly where POS.0700
foresaw it: below the assignment, above the solution design. The
assignment carries the in-scope substance of the intent to the
recipients, complete and precise, assigning and not solving; the
BRD is the recipients' first answer where the recipients are an
analysis function: the ask broken into rules and behaviour that
stakeholders can review, estimators can size and designers can
start from, with the solution admitted at high level where the
standard admits it (AP.010) and the how left to the solution
design (POS.1400). The boundary to the solution design is the
standard's own judgement call, stated in the Aim, not a ban. [M]

One thing the fork's BRD does not carry and the engine requires:
**phasing**. POS.1360 makes the horizon mandatory in the BRD — what
each version delivers, in what order, with what dependencies, even
if only as the statement that everything is in the first version.
None of the three BRDs has it; the fork's template has no place
for it. It is an area of the Map and a section of the template.
[M]

### 5. Where the earlier note's ideas land in a definition

| Idea | Block of the definition | Template |
|---|---|---|
| transformation, never duplication | Partner (Claude recasts, never copies); Instruments (`/critique essence`) | — |
| traceability REQ → BR, 100 %, verified | Course (the provenance map of the recast); Instruments (a check) | the appendix, a table |
| stakeholder-domain coverage with an explicit "no" | Map ("who is touched", the roster the instance's) | a list of areas with found / not applicable and the reason |
| separate OOS, DEP, ASM | Map ("the boundaries") | three lists |
| use cases with traced steps and exceptions | Map ("the process view, where behaviour matters") | UC items, steps as a table |
| discovery questions inline with a role as owner | the TBC rule, as the assignment has it | TBC items under their group |
| testability mandatory | the Requirement style of the BRD | — |
| regression-first review head | already the critic contract's | — |
| NFR by category, values from stakeholders | Map ("the qualities"); the no-value rule of the template | a list by category, `TBC` where a value is not known |
| the standard's process clause (solution admitted at high level) | Aim (the boundary to the solution design) | — |

### 6. The seven blocks of `states/brd.md`, drafted

Proposed wording, in the shape of POS.1310, for the principal to
judge; the Map first, since it carries the most.

**Target.** `30-brd.md`. Shape of the result: `templates/brd.md`.

**Inputs.** The approved assignment (`20-assignment.md`), read
with the intent and the project's threads for the reasons it does
not carry; `decisions.md`, the ledger; the DEL items of the
assignment as the list of what the BRD is asked to bring back; the
instance's roster of areas and its standard, library documents
cited by path (POS.1020); sources and research as the principal
directs. Where a project has no assignment, the BRD is derived
from the intent's in-scope positions in the same way, and the
assignment is not invented for it.

**Aim.** The BRD breaks the assignment into rules and behaviour
that the stakeholders can review in isolation, the delivery teams
can estimate and the solution design can start from: every
in-scope requirement of the assignment carried by business
requirements and, where behaviour matters, by use cases; every
requirement atomic, testable and traced; the touched areas of the
enterprise each found or knowingly found not to apply; the
boundaries (out of scope, dependencies, assumptions) and the
scope of the document explicit; the qualities named by category
with their values from the stakeholders or open as TBC; the
phasing stated, even as "all in the first version"; every term
defined. It admits the solution at the level the stakeholders
need to agree the ask and leaves the how to the solution design;
where to stop is a judgement, made when the teams can estimate,
when more detail would not interest the stakeholders or would be
superseded by design. It is complete when nothing of the
assignment is left out in silence — delegated, phased later or
open with an owner is complete, silent is not — and when no TBC
that blocks estimation is open.

**Partner.** The analyst's work is Claude's: the recast of the
whole from the assignment with the provenance map, the groupings
proposed MECE, the use cases drawn from the assignment's process
view, the impact questions raised area by area, the wording in
the Requirement style. The principal, or the analyst working as
principal, decides the scope of the document, the groupings,
which areas apply and which are left, the owner of every TBC, and
every value. Claude writes no value the stakeholders have not
given (a TBC with an owner stands instead), copies nothing of the
assignment and invents no requirement the assignment does not
carry; what he finds missing in the assignment he raises as a
question, and a change of substance goes to the intent first.

**Map.** What the BRD finds; where it lands is the template's.
Walked before the recast, to see what the assignment does not
answer, and at the end; an area may stay empty when it was
considered and found not to apply, said with the reason where the
instance's standard makes the area mandatory.
- the stakeholders: who must review, who approves, who is
  consulted or informed, as roles;
- the scope of work and the scope of the document: what is done
  and not done, and what this BRD does not cover that a reader
  would expect, with where it is covered;
- the cut of the assignment: what is carried now, what is phased
  later and in which version, what is delegated onward;
- the process view: the behaviour that must be agreed as a
  sequence, with its actors, conditions and exceptions;
- the rules: the business requirements, grouped so that every
  stakeholder finds theirs and nothing is twice;
- the touched areas of the enterprise: the instance's roster,
  each found or found not to apply, the mandatory ones never
  silent;
- the systems and dependencies: what is impacted, what the BRD
  relies on outside itself;
- the qualities: the non-functional categories, with values from
  the stakeholders or open;
- the transition: data to migrate, people to train, the cut-over,
  where the change replaces something;
- the phasing: what each version delivers, in what order, with
  what dependencies;
- the assumptions: what the requirements rest on and would change
  if it stopped holding;
- success: how the stakeholders will know the ask was met;
- the terms: every capitalised term defined, nothing generic;
- what stays open: every TBC with an owner, and which of them
  block estimation.

**Instruments.** The provenance map of the recast, as the
assignment's definition has it; `/critique essence` for drift
from the assignment; `/critique clarity` with the BRD's
Requirement style; `/check brd` for the mechanics (every parent
REQ mapped, every mapped ID existing, IDs in tens, every
capitalised term defined, no link in an item, phasing present);
`/ingest` for the instance's roster and standard into the
library; `/recipe` for the wiki page the instance publishes, a
render and never the artefact.

**Course.** Resolve the project and read the assignment and the
BRD as it stands; say whether the assignment is ready to be
derived from (approved, or the principal's word that it is
stable), never as a gate. The ways in: no BRD yet, and the joint
pass of the assignment's definition runs adapted — questions up
front on the stakeholders, the scope of the document and the
phasing, which the assignment does not answer; the recast with the
provenance map; the walkthrough by group, the touched areas walked
one per item; an assignment that moved, and the pass runs on what
changed; a wording fix, made directly. End by naming what changed
and what stays open; when the Aim's completion is reached, offer
the approval — the principal's, as the house scheme has it — and
say that the stakeholders' sign-off is the instance's act,
recorded where the instance records it.

### 7. The template, in outline

Lists of items with IDs, as every artefact; a table only where
columns carry data (use-case steps, the traceability appendix, the
qualities). No value in any row of the skeleton; a `TBC`
placeholder where the fork had a figure. No Version History in the
body (the companion, POS.0310), no names (roles), no links in
items, no document code (the instance's render).

1. Purpose & Context — prose, from the assignment's.
2. Objective — prose, what must be true at the end.
3. Stakeholders — roles and their involvement (approves, reviews,
   consulted, informed).
4. Scope — in scope; out of scope `OOS`; scope of the document
   (what is covered elsewhere); impacted systems.
5. Dependencies `DEP` and Assumptions `ASM`.
6. Use cases `UC` — each with actor, preconditions, outcome, the
   requirements it exercises; the steps as a table; the exceptions.
7. Business requirements `BR` — groups by capability or process,
   MECE; a TBC under its group where a rule is not known.
8. Touched areas of the enterprise — the roster as a list: area,
   found (the items that carry it) or not applicable with the
   reason.
9. Qualities — by category, the value or a TBC.
10. Transition — migration, training, cut-over, as `BR` items in
    their own group.
11. Phasing — what each version delivers, in what order, with
    what dependencies.
12. Success criteria `SCR`.
13. Open questions `TBC` — with owners, and which block
    estimation.
14. Terms.
15. Appendix: traceability `REQ` → `BR`/`UC`, a table, generated
    from the items and verified by the check.

### 8. Prefixes and the Requirement style of the BRD

New: `BR` business requirement (atomic, testable), `UC` use case,
`DEP` dependency. Reused from the ID scheme: `OOS`, `ASM`, `TBC`,
`SCR`. Not in the engine: the document code and the wiki
convention (the instance's render recipe). The Requirement style
of the assignment holds, with these made stricter for the BRD:
testability mandatory; one idea per item, within reason, a list of
two to nine members allowed inside an item (RT.030); a note after
an item allowed and carrying no requirement (RT.040, RT.050); an
item may name the role that owns it (RT.060); no value that no
stakeholder gave.

### 9. Reviewers: no new kind

The `clarity` lens reads a BRD with the BRD's Requirement style
cited from its definition, as it does the assignment's; the
`essence` lens compares the BRD with the assignment as it does the
assignment with the intent; a check `brd` verifies the mechanics
listed under Instruments. A challenger persona `business-analyst`
is foreseen in the intent (POS on personas) and is created only
where its blind spots differ from the `cto`'s — recommended to
wait for the first BRD to show whether they do. The fork's
critique template is the calibration set: its checklist rows sort
into the three places above without remainder.

### 10. What belongs to the instance, and goes to the library

The six-pillar roster and the mandatory impact areas, the
statutes, the vendor and system names, the named roles of the
RACI, the wiki space, hub page and document code, the publishing
convention: one library document, "the BRD roster of the
instance", cited by path from a project's BRD (its front-matter or
its Touched areas section) and from the recipe of the wiki page;
the group's standard and tutorial already stand in the library's
bundle. A project with no enterprise around it has no roster, and
the Map's area is then walked against nothing and said so.

## Options and trade-offs

1. **Adopt the fork's layer as it is, adapted to the engine's
   file layout.** Fastest; carries all nine anti-patterns, a
   fourth reviewer kind and the instance into the engine. Refused
   by the earlier note; nothing here reopens it.
2. **A generic definition as drafted above, the roster and the
   publishing in the library.** The engine's shape, the fork's
   substance where it held, the standard's judgement calls in the
   Aim. The cost: the first BRD will show where the Map is wrong,
   and the roster must be written for the instance before the
   first walk.
3. **The BRD as a render of the assignment.** Weighed for
   completeness: the BRD adds content the assignment does not
   carry (use cases, qualities with values, transition, the areas,
   the phasing), so it is composed, not generated; a render is
   never edited by hand (POS.0710). Refused.

Recommendation: option 2.

## What was not found

- The fork's commit history: the fork under `tmp/` is not a
  repository of the forge, and git is read only through the
  scripts; the earlier note read nine commits from a clone.
- A line-by-line comparison of the agentic-platform BRD with the
  engine's own assignment of that initiative (1.0 approved): the
  natural first run of the new definition, not this note's.
- The conversations in which the fork's BRDs were elicited: only
  the skills and the reports exist; whether the analyst asked
  questions up front or only recast is not recorded.
- Whether the forge-as-BRD was ever used for anything.
- BABOK v4: the general practice is the companion note's.

## Relevance to this project

The material for `/new-artefact brd` is findings 6 to 10: the
seven blocks, the template outline, the prefixes with the BRD's
Requirement style, the reviewers, the library document. The way
in that POS.1380 and THR.0360 foresee — the brief `brd` born from
the conversation over the fork, mined into the intent, then the
definition — can now be short: this note and the companion are
the brief's material, and the brief itself is the principal's few
sentences on what he wants of the layer and what he refuses. Two
things the brief must say that this note cannot: whether the
stakeholders' sign-off is recorded by the forge (a DEC, a ledger
note) or left to the instance; and whether a BRD may be derived
from the intent where a project has no assignment, as the fork did
and the draft above allows. The first BRD on real work is the
agentic platform, whose assignment is approved, with the fork's
0.4 beside it as the comparison the essence lens reads; before it,
the instance's roster into the library. CHL.0030 under DEC.0060
(the growth path displaces the functions that own analysis) is
revisited in the same round: the definition above makes the
analyst the principal of the BRD, which answers it.

## Sources

- The bundle `projects/lib-allwyn/sources/fork-brd/`, its
  `00-INDEX.md` and the files it catalogues (private; cited by
  path, not quoted beyond the mechanisms).
- `research/2026-09-07-brd-layer-fork-analysis.md` (this project).
- The forge intent v5.8: POS.0700, POS.1310, POS.1320, POS.1350,
  POS.1360, POS.1400, POS.1430, POS.1520; `threads.md` THR.0360;
  `decisions.md` DEC.0060.
- `.claude/skills/forge/states/assignment.md`,
  `.claude/agents/critic-clarity.md`, `templates/assignment.md`.
- The group's "BRD — Standards & Guidelines" v0.3 and "FIC BRD
  tutorial", as held in the bundle.
