---
project: forge
date: 2026-10-13
topic: what a business requirements document contains and how it is found today - the standards, the light forms, the use case against the story, the qualities, traceability, and analysis with a model
status: immutable
derived_from: the principal's word of 2026-10-13 (general practice to enrich the research of the fork's BRD layer); research/2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md (companion); research/2026-09-07-brd-layer-fork-analysis.md; research/2026-09-28-artefact-layers-from-idea-to-handover.md; the group's BRD standard and tutorial in projects/lib-allwyn/sources/fork-brd/; projects/flow-ba/sources/ai-ba-use-cases.md (by its index entry); web sources below
---

# Research: what a BRD contains and how it is found today

## Question

What does current practice say a business requirements document
contains and how it is found — the standards (ISO/IEC/IEEE 29148,
BABOK, IREB, INCOSE), the light forms practitioners use beside or
instead of a BRD, the use case against the user story, the
non-functional qualities, traceability, and analysis assisted by a
language model — and what of it the Map of the engine's `brd`
artefact must carry and its reviewers must check? Companion of the
note on the fork's layer, same date; the earlier notes of
2026-09-07 and 2026-09-28 already placed the BRD in the standards'
families and are not repeated, only extended.

Several primaries are sold or gated (ISO 29148, BABOK, the INCOSE
guide, the IREB handbook's current edition); where a finding rests
on a secondary page or an abstract, it says so.

## Key findings

### 1. The standards, as far as they can be read

- **ISO/IEC/IEEE 29148:2018** defines the information items — a
  business or mission requirements specification, a stakeholder
  requirements specification, system and software specifications —
  and the characteristics of a requirement and of a set; the
  outlines of the StRS and BRS are in the sold text, and no page
  read for this note reproduces them (ReqView's templates "preserve
  the structure of sections provided in the standard" and show
  none). [S; the outline unverified here]
- **BABOK v3** (2015) classifies requirements as business,
  stakeholder, solution (functional and non-functional) and
  transition; its tasks include assessing requirement changes and
  approving requirements. No BABOK v4 exists: IIBA moved from one
  expanded book to a modular ecosystem (the Business Analysis
  Standard, an Agile Extension, a data-analytics guide) and keeps
  the six knowledge areas and thirty tasks unchanged. [S; IIBA's
  own pages]
- **IREB CPRE** (Foundation handbook 1.3.2, revised 2026)
  distinguishes single requirements, coherent sets, documents and
  documentation structures, and says there is no universal
  structure: a requirements document is tailored to the project;
  its natural-language rules and templates are in the handbook,
  which restricts reproduction. [S; secondary course pages for the
  rules]
- **INCOSE Guide to Writing Requirements** Rev 4 (July 2023)
  defines fourteen characteristics of needs and requirements and
  of their sets (C1 "necessary" and on) and some forty rules, each
  tied to characteristics; the PDF refused the fetch. [S; a review
  page]
- **ISO/IEC 25010:2023** (second edition, November 2023) gives
  nine product-quality characteristics with sub-characteristics —
  functional suitability, performance efficiency, compatibility,
  interaction capability, reliability, security, maintainability,
  flexibility, safety — as the reference model for stating and
  measuring quality. [S; the names from secondary pages, the
  standard sold]

What the four requirement standards agree on, through every
secondary page: a requirement is one sentence, necessary,
unambiguous, singular, verifiable, feasible, traceable and uniquely
identified; a set is complete, consistent and traceable; a document
states its purpose, scope, stakeholders, definitions and the
requirements grouped by a logic the reader can follow. The group's
own standard says the same in its DS and SIBR rules. [C]

### 2. Right-sizing: the BRD against the light forms

Practitioner guides frame the BRD as a waterfall document — an
overview with purpose, scope and outcomes, measurable objectives,
stakeholders and roles, functional and non-functional requirements
— and say its depth should fit the project; in agile settings a
vision document or a product brief fills the same place and the
rules travel into the backlog, with non-functional requirements as
constraints in the definition of done or in the architecture. The
one firm statement found: style, depth and nature of the BRD
reflect the context and are sufficient for the project, which is
the group standard's own judgement call on when to defer (its
"Purpose of a BRD"). [C on the principle; vendor blogs for the
wording]

For the engine this confirms what the fork's control case showed:
a fixed roster filled for a tool with no player is wrong by the
standard's own rule; the Map asks each area and lets it be found
not to apply.

### 3. Use cases against stories

Cockburn's forms: a **brief** use case is one paragraph, for an
early stage or a backlog; a **casual** one is a few paragraphs
with the main path and the main deviations; a **fully dressed**
one carries title, level, scope, primary actor, stakeholders and
interests, preconditions, minimum and success guarantees, trigger,
a main success scenario of three to nine numbered steps in active
voice with no conditionals, extensions numbered by the step they
branch from, each opening with a condition stated as a fact and
ending by returning, succeeding or failing within the minimum
guarantee, and optional technology and data variations. Levels:
summary, user goal, sub-function; below that, too small for a use
case. "Most use cases should stay brief or casual; fully dress only
the important ones." [C; Cockburn's book through a working guide]

When to use which: Cockburn himself starts with brief, coarse use
cases for the big picture and is "fairly indifferent" afterwards
between use cases and stories — the choice is "how much the people
involved can keep in their heads and how good their conversations
are"; use cases are stronger where failure handling, compliance,
security or contract matter, because the form forces behaviour in
failure to be written. [C; an interview and practitioner pages]

For the engine: a `UC` item is a user-goal use case; the template
carries the fully dressed fields, and the definition says that
brief suffices where the behaviour is not contested and fully
dressed is for the critical paths. The fork's three-table use case
is the fully dressed form in tables; the fields are right, the
form is the template's choice.

### 4. The qualities

The categories recur across every source: availability and
continuity (with recovery point and time), performance (response,
throughput, capacity under peak), security and privacy
(authentication, authorisation, encryption, audit, retention and
residency), compliance and regulatory, reliability (maturity,
fault tolerance, recoverability), usability and accessibility,
localisation, maintainability and operability (monitoring,
support, service levels), compatibility and interoperability,
scalability, data integrity. The measurable form is the same
everywhere: a value, a condition, a population — "within two
seconds for 95 % of requests in the evening window". [C]

The rule that follows for the engine, already the companion's: the
category list is the template's, the value is the stakeholders',
and a category without a value is a `TBC` with an owner, never a
figure from the skeleton.

### 5. Traceability

Wiegers (2013, still the reference): links are filled in as the
work is done, not as it is planned; a listed test means the test
exists, not that it passed; whoever knows the link records it; a
spreadsheet holds a couple of hundred requirements and a larger
set needs a tool; good tools flag a link as suspect when either
end changes. Practitioner post-mortems add the common faults:
treating the matrix as a one-off artefact of the BRD, leaving the
non-functional requirements out of it, linking the BRD to the
functional specification but not onward to design and test. [C]

For the engine: the REQ → BR/UC matrix is the provenance map of
the recast, generated from the items and verified by a check; the
onward links (to the solution design's SOL items, to tests) are
the next layers' matrices, not the BRD's; the matrix is a view, the
links live in the items ("serves REQ.NNNN"), so that a moved
requirement makes its links suspect by the check, not by memory.

### 6. Analysis with a model

The one empirical study found (Kabadi et al., ESEM 2026, an
industry setting): a multi-phase method turns incomplete business
requirements into functional user stories benchmarked against
production-derived and analyst-written stories; analysts write
more precisely, the model's stories reach higher recall in every
domain and surface implicit requirements the elicitation missed;
the authors conclude the model complements the analyst and the
combination gives the more complete backlog. Figures are in the
paper, not its abstract. [emerging; one study]

Practitioner guidance (Modern Analyst, October 2025, page not
readable at the time of writing, abstract only) casts the model as
a co-analyst for elicitation preparation: interview questions,
missing stakeholders, first drafts. No source found on the
model-specific traceability failure (a link that looks valid and
is not) or on BRD generation benchmarked as such. [emerging]

The company's own experience, in the FLOW:BA project's source on
AI use by the business analysts: eleven use cases already run —
review of an assignment, transcript to business requirements,
use-case generation, impact analysis, inconsistency finding,
business requirement to a lower-level specification, wording,
search of system documentation, assessment of a new assignment
against existing documentation, diagrams. [the project's source,
by its index entry]

What this means for the engine's definition: the model recasts and
finds gaps well and must not be let to fill them — recall is its
strength, precision the analyst's — which is the Partner block as
drafted in the companion (Claude recasts, raises, never invents a
value or a requirement the assignment does not carry) and the
reason the walkthrough by group exists.

### 7. The failure checklist of a BRD

From the standards' rules, the group's "what to avoid", the fork's
three critique rounds and the practitioner post-mortems, the
faults named often enough to become what a reviewer hunts:

1. Drift from the parent: a hierarchy inverted, a term redefined,
   a requirement silently dropped (essence).
2. Copying the parent instead of transforming it (essence).
3. A compound requirement; a vague modal; an untestable adjective;
   a value nobody gave (clarity).
4. Solutioning below the standard's line: schemas, endpoints,
   screens, tasks (clarity, by the Aim's boundary).
5. A term capitalised and not defined; a requirement in a note; a
   requirement that needs a link to be understood (clarity, check).
6. A roster filled for form's sake, or an area left silent that
   the instance declares mandatory (the Map walk).
7. A matrix that maps to the wrong parent, or not every parent
   (check).
8. No phasing; no scope of the document; stakeholders without
   their involvement (the Map walk).
9. The non-functional categories absent, or present with the
   template's example values (clarity, the no-value rule).
10. Open questions without an owner, or not said which of them
    block estimation (the Map walk).

## Options and trade-offs

The question has no options of its own; it feeds the companion's.
One choice it sharpens: whether the template carries the fully
dressed use case for every `UC` or lets the definition say brief,
casual or fully dressed by the weight of the behaviour. The second
follows the field; the first is simpler to check. Recommendation:
the fields of the fully dressed form in the template, the
definition saying that an uncontested behaviour needs the header
and the main scenario only.

## What was not found

- The section outlines of the StRS and BRS of ISO 29148, the
  INCOSE rules in their own wording, IREB's natural-language rules
  from the handbook: all behind sale or copyright; the secondary
  pages agree on the substance.
- A benchmark of BRD generation by a model, or any study of
  model-specific traceability failures.
- A 2025 or 2026 "lean BRD" guide of any standing; the right-sizing
  principle stands only in the group's standard and in vendor
  prose.
- The Modern Analyst article's own text (server error at the time
  of writing).

## Relevance to this project

Three things for `/new-artefact brd`, beside the companion's
blocks:

1. **The Map's areas hold** against the field: stakeholders with
   involvement, scope of work and of the document, the cut, the
   process view, the rules grouped, the touched areas, systems and
   dependencies, the qualities, the transition, the phasing, the
   assumptions, success, the terms, what is open. Nothing in the
   standards asks for an area the list lacks; the "transition"
   area (BABOK's fourth class, the tutorial's data migration) is
   the one most templates forget and the Map must keep.
2. **The use case** in the template with the fully dressed fields,
   the weight of each decided by the definition; `UC` at user-goal
   level.
3. **The failure checklist** of finding 7 is the reviewers'
   material: items 1–2 the `essence` lens, 3–5 and 9 the `clarity`
   lens with the BRD's Requirement style, 5 and 7 the `brd` check,
   6, 8 and 10 the Map walk of the definition, said aloud at the
   end of the pass.

## Sources

- IIBA, *The updated Business Analysis Standard*,
  https://www.iiba.org/business-analysis-blogs/the-updated-business-analysis-standard-your-foundation-for-success/
  and the Standard's preface,
  https://www.iiba.org/knowledgehub/the-business-analysis-standard/preface/
- BA Times, *BABOK Version 3 vs. Version 2*,
  https://www.batimes.com/?p=6133
- ReqView, *ISO/IEC/IEEE 29148 Requirements Specification
  Templates*, https://www.reqview.com/doc/iso-iec-ieee-29148-templates/
- IREB, CPRE Foundation Level handbook (English v1.1.1, 2022;
  French v1.3.2, 2026), https://www.ireb.org/downloads
- INCOSE, *Guide to Writing Requirements* Rev 4 (2023),
  https://www.incose.org/docs/default-source/working-groups/requirements-wg/gtwr/incose_rwg_gtwr_v4_040423_final_drafts.pdf
  (403 on fetch); review at
  https://www.se-trends.de/en/review-incose-guide-for-writing-requirements/
- ISO/IEC 25010:2023, https://iso.org/standard/78176.html ; the
  characteristics via https://shiftasia.com/community/8-items-nonfunctional-requirement-under-iso-25010/
- Cockburn, *Writing Effective Use Cases* (2001), through the
  working guide
  https://cdn.jsdelivr.net/npm/usecases-skill@0.1.0/skills/usecases/use-case-guide.md
  and the interview at https://www.softhouse.se/?p=228
- Wiegers, *Links in the requirements chain, part 2* (Jama, 2013),
  https://www.jamasoftware.com/blog/links-in-the-requirements-chain-part-2
- Kabadi et al., *Can LLMs Identify Missing Elements in
  Requirements Elicitation?* (ESEM 2026),
  https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.82
- Modern Analyst, *10 Practical Ways Business Analysts Can Use
  LLMs* (October 2025),
  https://modernanalyst.com/Resources/Articles/tabid/115/ID/7070/10-Practical-Ways-Business-Analysts-Can-Use-LLMs.aspx
  (500 on fetch) and *Writing Non-Functional Requirements That
  Developers Actually Use*,
  https://modernanalyst.com/Resources/Articles/tabid/115/ID/7107/
- Microsoft Learn, *Identify non-functional requirements*,
  https://docs.microsoft.com/en-us/learn/modules/work-with-requirements/4-non-functional-requirements
- Scrum.org forum, *User Stories (Agile) vs BRDs (Waterfall)*,
  https://www.scrum.org/node/6443 ; practitioner guides on BRD
  sections (Slite, MasterClass, Business Analyst Mentor) as
  secondary.
- The group's "BRD — Standards & Guidelines" v0.3 and "FIC BRD
  tutorial", in `projects/lib-allwyn/sources/fork-brd/`.
- `projects/flow-ba/sources/ai-ba-use-cases.md`, by its entry in
  that project's `sources/00-INDEX.md`.
