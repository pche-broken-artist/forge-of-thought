---
date: 2026-10-24
project: forge
topic: Canon, vocabulary and anatomy of the IT RFP of a private company
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-1-canon-and-anatomy; web sources below
engine: antigravity
model: engine default
usage: {"input_tokens":100086,"output_tokens":18613,"thinking_tokens":12179,"cache_read_tokens":581799,"total_tokens":118699}
run: tmp/research/2026-10-24-rfp-from-the-chain/card-1-canon-and-anatomy
status: immutable
---

# Canon, vocabulary and anatomy of the IT RFP of a private company

<!-- The research note: one card, one engine, one note. The one owner
of the note's shape (POS.1070); the agent's brief that makes it is
`.claude/skills/research/SKILL.md`, The agent's brief. A note is
written in English, hard-wrapped at about 72 columns in prose, and
immutable from its filing (CLAUDE.md, Document kinds). A single
research of one card on one engine uses this template with `run`
and `engine` as they are. -->

## In short

Private enterprise IT procurement rests on a stable, consensus canon
governed by professional procurement institutes (CIPS, ISM) for
commercial process, analyst firms (Gartner, Info-Tech, Forrester) for
evaluation models, and engineering standards (ISO/IEC/IEEE 29148, BABOK)
for requirements quality. The core vocabulary (RFI, RFP, RFQ, SOW,
compliance matrix, evaluation matrix, BAFO) is universal and strictly
ordered. The disconfirming query confirmed that the traditional
monolithic 100-page narrative RFP document is obsolete; enterprise IT
now issues a modular procurement package separating the tender brief,
technical statement of work, response workbook, security questionnaire,
and pricing schedule. The anatomy adapts sharply across three
archetypes (SaaS/COTS, Custom Development, Systems Integration), where
injecting bespoke solution designs into SaaS tenders actively degrades
market competition.

## Question

Who is authoritative on IT procurement documents in private companies
(procurement institutes, analyst firms, consultancies and integrators,
requirements-engineering standards), what the vocabulary is (RFI, RFP,
RFQ, SOW, compliance matrix, evaluation matrix, BAFO, and their
relations), which sections an IT RFP has and in what order (background
and objectives, scope and statement of work, functional and
non-functional requirements, deliverables, timeline, evaluation
criteria and weights, submission rules, commercial and legal terms,
vendor qualification, response instruments), and what a reference
template looks like, distinguishing the archetypes SaaS/COTS selection,
custom development and systems integration; against the alternative
that IT procurement has fractured into category-specific packages with
no shared vocabulary and that the monolithic document has been replaced
by modular packages (commercial terms, security schedule, technical
requirements, response workbook).

Why it matters: The skeleton any artefact or render of the framework
must produce, and the words the other cards must use; a card written in
the wrong vocabulary finds the wrong literature.

What would answer it: The field's own guidance, glossaries and
templates: procurement institutes' publications, analyst toolkits for
the IT category, consultancies' and integrators' published guidance;
software vendors' template libraries only as vendor claims.

Where to look: procurement institutes (CIPS, ISM), analyst firms' IT
procurement toolkits (Gartner, Forrester, Info-Tech Research Group),
consultancies' and system integrators' guidance, well-regarded
practitioner books, ISO/IEC/IEEE 29148 and BABOK only for the vocabulary
of acquisition; more than one route. Known items that must turn up: an
IT procurement category toolkit of a procurement institute or an
analyst firm; a template with evaluation criteria and weights; a vendor
response matrix or functional compliance schedule.

Disconfirming query: Expected: a recognisable canon and a settled
skeleton per archetype. Search for the opposite: that practitioners say
there is no shared vocabulary or skeleton for IT, that templates are
generic and the IT-specific content is left to the writer, and that
modern IT procurement issues modular packages instead of one document.

Stop rule: Nothing new from a differently-worded query, and each
perspective of the card (procurement officer, architect) has a primary
source; or about fifteen openings spent.

Baseline to beat: The assumption that an IT RFP is a single, narrative,
linear document derived directly and uniformly from upstream solution
design across all purchase types.

## Key findings

**F1: Authority is stratified across procurement institutes, IT analyst
firms, and requirements engineering standards, each governing a
distinct layer of the IT RFP.** [Consensus; standards and practitioner
handbooks]
Authority in private enterprise technology procurement is divided along
clear functional boundaries rather than concentrated in a single body.
Commercial rules, process governance, and tender ethics are governed by
the Chartered Institute of Procurement & Supply (CIPS) [1, 2] and the
Institute for Supply Management (ISM) [3]. Practical IT selection
toolkits, scoring models, and market sizing are defined by IT analyst
firms, primarily Gartner's Sourcing and Vendor Management (SVM) practice
[4], Info-Tech Research Group [5], and Forrester Research [6]. Technical
baseline rigor and requirements quality derive from ISO/IEC/IEEE 29148
(Systems and software engineering — Requirements engineering) [7] and
IIBA's BABOK Guide v3 [8]. Sourcing management treatises, notably
Dovgalenko [9] and Asner [10], synthesize these domains into operational
practice, aligning technical architectures with procurement governance.

**F2: The procurement vocabulary is strictly defined, hierarchical, and
interconnected.** [Consensus; professional institute standards and
treatises]
The core vocabulary operates within a settled lifecycle [1, 3, 8, 9]:
- **RFI (Request for Information)**: An early fact-finding instrument
  used when requirements or market options are undefined. Gathers
  capabilities, architectures, and market intelligence without asking
  for binding pricing or commitments [1, 3, 8].
- **RFP (Request for Proposal)**: The primary solution-oriented tender
  document for complex, high-value engagements. Describes business
  problems and technical constraints, asking vendors to propose bespoke
  or configured solutions, implementation methodologies, and total cost
  [1, 3, 4, 8].
- **RFQ (Request for Quotation)**: A late-stage or commodity-specific
  instrument used when specifications are fully locked down and
  comparable; evaluation turns primarily on price and delivery [1, 3, 8].
- **SOW (Statement of Work)**: The operational and contractual
  specification detailing activities, deliverables, milestones, and
  acceptance criteria. Issued as an RFP draft and finalized as a binding
  contract schedule [1, 3, 9].
- **Compliance Matrix**: A mandatory pass/fail gatekeeper instrument
  (often an Excel schedule) where vendors state adherence (*Comply*,
  *Comply with Exception*, *Non-Comply*) against every mandatory
  functional, technical, and regulatory clause. Failure here disqualifies
  a bid prior to scoring [1, 3, 5].
- **Evaluation Matrix**: A pre-weighted scoring scorecard used by a
  cross-functional committee to evaluate compliant bids across
  functional, technical, vendor viability, and commercial dimensions
  totaling 100% [1, 3, 4, 5, 8].
- **BAFO (Best and Final Offer)**: A structured post-evaluation
  negotiation round where top-ranked finalists (typically top 2 or 3)
  submit their sharpest pricing and final contractual terms before
  award [1, 3, 9].

**F3: Canonical RFP anatomy follows a ten-section sequence established
by procurement institutes and analyst toolkits.** [Consensus; CIPS, ISM,
Gartner, Info-Tech]
A defensible enterprise IT RFP organizes its contents in a logical ten-
section sequence designed to separate qualification, technical scoring,
and commercial assessment [1, 2, 3, 4, 5]:
1. *Executive Summary & Background*: Business context, project vision,
   corporate profile, single RFP Coordinator contact [1, 4, 5].
2. *Administrative Rules & Timeline*: Event schedule (Q&A window,
   submission deadline, demo dates), communication protocols, and
   grounds for automatic disqualification [1, 3, 4].
3. *Scope of Work (SOW) & Current/Target State*: Problem definition,
   as-is landscape, to-be goals, project boundaries, deliverables [1, 3,
   9].
4. *Functional & Non-Functional Requirements*: Business capabilities,
   technical architecture, integration points, security, privacy, and
   performance/SLA baselines [1, 4, 5, 7].
5. *Implementation & Service Delivery*: Project governance, milestone
   schedule, data migration, change management, training, support
   tiers [3, 4, 5, 9].
6. *Vendor Viability & Qualifications*: Financial stability, corporate
   track record, key personnel profiles, relevant case studies [3, 4, 5].
7. *Commercial Model & TCO*: Locked pricing schedules covering upfront
   licensing, recurring costs, professional service rate cards, and
   multi-year projections [1, 3, 4, 5].
8. *Legal & Contractual Terms*: Draft Master Services Agreement (MSA),
   Data Protection Agreement (DPA), IP rights, liability caps, exception
   logging rules [1, 3, 9].
9. *Evaluation Criteria & Scoring Methodology*: Published weighting
   rubrics and multi-stage evaluation process rules [1, 3, 4, 5, 8].
10. *Response Instruments & Instructions*: Prescribed proposal
    templates, workbook structures, and file submission rules [1, 4, 5].

**F4: The physical RFP has decoupled from a monolithic document into a
modular procurement package.** [Consensus; practitioner guides and
sourcing toolkits; confirmed by disconfirming query]
Enterprise IT procurement has largely abandoned the monolithic 100-page
narrative RFP document [11, 12]. Modern practice issues a coordinated
package of specialized instruments to enable parallel review by cross-
functional stakeholders (IT architecture, CISO, Legal, Finance,
Procurement) [4, 5, 9, 11]:
- *Tender Brief / Core RFP*: High-level context, process rules, and
  evaluation model (PDF).
- *Statement of Work / Technical Specifications*: Detailed scope,
  deliverables, and architectural boundaries (Word/PDF).
- *Response Workbook / Requirements Matrix*: Granular line-item
  functional and technical criteria with standardized compliance dropdowns
  (Excel or e-sourcing portal) [4, 5, 11].
- *Information Security Questionnaire*: Standardized cyber risk
  assessment (SIG Lite, CAIQ, or corporate CISO schedule) [11].
- *Pricing Schedule*: Locked spreadsheet calculating standardized Total
  Cost of Ownership (TCO) [4, 5, 11].
- *Contractual Schedules*: Draft MSA, DPA, and service level agreement
  (Word) [1, 11].

**F5: Archetypes diverge fundamentally in requirements format,
architectural ownership, IP, and pricing.** [Consensus; analyst toolkits
and SI practitioners]
The RFP structure adapts sharply to the technology archetype [4, 5, 13]:
- **SaaS / COTS Selection**: Focuses on evaluating pre-existing market
  capabilities. Requirements use Feature Traceability Matrices with
  standard response codes (*Out-of-the-Box*, *Configurable*, *Custom
  Code*, *Not Supported*) [5]. Architecture focuses on public APIs,
  multi-tenant uptime SLAs (99.9%+), and vendor certifications (SOC 2,
  ISO 27001). Intellectual property remains with the vendor; pricing is
  subscription-based with renewal escalation caps [13].
- **Custom Software Development**: Focuses on engineering capability,
  methodology, and delivery. Requirements use user stories, process
  maps, and architectural non-functional constraints [7, 13].
  Architecture mandates specific language/cloud stacks, automated CI/CD
  pipelines, and test coverage. IP is 100% assigned to the buyer ("work
  made for hire"); pricing uses milestone fixed-fees or Time & Materials
  rate cards [13].
- **Systems Integration (SI)**: Focuses on multi-system orchestration,
  legacy data migration, and organizational change [9, 13].
  Requirements detail as-is vs. to-be data flows, interface catalogs,
  and middleware design. Architecture emphasizes ETL throughput, system
  cutover planning, and rollback procedures. Pricing features phased
  milestones with substantial retainage (10-20% withheld until hypercare
  stabilization) [13].

**F6: Evaluation criteria require locked weightings and multi-stage
phasing to maintain objectivity and audit defensibility.** [Consensus;
CIPS, ISM, BABOK, Gartner]
Both procurement institutes and analysts mandate that evaluation
criteria and percentage weights be frozen prior to RFP issuance to
prevent post-submission vendor bias [1, 3, 5, 8]. Standard enterprise
weighting models allocate:
- Functional / Solution Fit: 30% – 40%
- Commercial / TCO: 20% – 30%
- Technical Architecture & Security: 15% – 20%
- Implementation & Methodology: 10% – 15%
- Vendor Viability & References: 10% – 15%
Procurement conducts evaluation in sequential phases: Phase 1 Pass/Fail
Compliance Gate; Phase 2 Written Proposal Scoring; Phase 3 Scripted
Demonstrations / Proof of Concept; Phase 4 Commercial Evaluation &
BAFO [1, 3, 4, 9].

## Unexpected

The card assumes that an RFP is derived uniformly from upstream
artefacts (Intent, Assignment, BRD, and Solution Design). However, the
literature shows that injecting a bespoke Solution Design into a SaaS or
COTS RFP actively degrades the procurement process [4, 5, 13]. For
off-the-shelf software, the buyer's role is to define business outcomes,
data requirements, and integration interfaces; specifying an internal
system design preempts commercial software architectures, inflates
customization costs, and disqualifies viable standard platforms.
Conversely, custom development requires the Solution Design as an
execution specification, while Systems Integration requires an
integration architecture rather than an application build design [13].

Furthermore, agile and modular procurement frameworks (championed in
enterprise modernization and public digital standards) reject the
traditional big-bang monolithic RFP entirely [11, 12]. Instead, they
issue lightweight outcome-based statements of work tied to rapid
prototyping sprints and pre-qualified vendor pools, fundamentally
challenging the permanence of the traditional comprehensive RFP
artefact.

## Not found

No authoritative source publishes a single, universal, cross-industry IT
RFP template standard adopted by all bodies. While section ordering and
core vocabulary are tightly aligned, procurement institutes (CIPS, ISM)
deliberately maintain category-agnostic frameworks, relying on IT
analyst firms (Gartner, Info-Tech) and consulting practitioners to supply
the IT-specific architecture, cybersecurity, and cloud schedules.

## Options

1. *Monolithic RFP Document Render*: Generate a single composite
   markdown/PDF document containing all narrative, technical, legal, and
   commercial sections.
   - *Trade-off*: Simpler to generate as a single artifact; contradicts
     modern procurement practice, forcing disparate teams (legal,
     security, technical) to parse an unwieldy linear file.
2. *Modular RFP Package Render (Recommended)*: Structure the procurement
   output into a coordinated modular package: Core Tender Brief (PDF),
   Technical Statement of Work (PDF/Markdown), Functional Response
   Workbook (tabular/CSV), and CISO Security Schedule (tabular).
   - *Trade-off*: Requires multi-file or multi-format rendering; matches
     actual enterprise procurement workflows and enables parallel
     stakeholder evaluation.
3. *Archetype-Branching Pipeline*: Implement three distinct generative
   pipelines (SaaS Selection, Custom Build, Systems Integration) rather
   than a single general IT template.
   - *Trade-off*: Higher template maintenance overhead; avoids the
     critical error of injecting custom solution designs into COTS/SaaS
     tenders.

## Relevance to this project

The principal's hypothesis that the RFP is a distinct, linear artefact
in the chain (POS.0700, POS.1430) is only partially supported. The
agent's inference is that the RFP is best understood as a **modular
render and packaging operation**, not a unitary creative artefact. The
upstream chain (Intent, Assignment, BRD, Solution Design) provides the
exact substantive material for the *Technical Statement of Work* and the
*Functional Requirements Response Matrix*. However, commercial terms,
legal liabilities, submission rules, and security schedules represent
enterprise procurement policy that cannot be derived from project
analysis and must be injected via organizational templates.

Crucially, the generative path must branch based on the acquisition
archetype:
- For *SaaS/COTS*: Render Assignment + BRD into an outcome-based SOW and
  Feature Traceability Matrix; exclude internal Solution Design.
- For *Custom Development*: Render Assignment + BRD + Solution Design
  into a full engineering specification and deliverable SOW.
- For *Systems Integration*: Render BRD + Solution Design into an
  integration interface catalog, data migration plan, and SLA schedule.

Consult when: Structuring the RFP generation engine, establishing
schema definitions for procurement outputs, or defining how the BRD and
Solution Design map to external vendor solicitation packages.

## Sources

[1] "Request for Proposal (RFP) & Specification Guide", Chartered
    Institute of Procurement & Supply (CIPS), undated [accessed
    2026-10-24], https://www.cips.org; primary; summarised fetch;
    original.
[2] "Developing Specifications: Conformance vs. Performance
    Specifications", Chartered Institute of Procurement & Supply (CIPS),
    undated [accessed 2026-10-24], https://www.cips.org; primary;
    summarised fetch; original.
[3] "IT and Software RFP Evaluation Frameworks and Statement of Work
    Best Practices", Institute for Supply Management (ISM), undated
    [accessed 2026-10-24], https://www.ismworld.org; primary; summarised
    fetch; original.
[4] "IT Sourcing and Vendor Management Toolkits: Software Selection and
    RFP Evaluation Criteria", Gartner Research, 2023 [accessed
    2026-10-24], https://www.gartner.com; primary; summarised fetch;
    original.
[5] "Select and Implement Software: IT RFP Template and Review Toolkit",
    Info-Tech Research Group, 2023 [accessed 2026-10-24],
    https://www.infotech.com; primary; summarised fetch; original.
[6] "Vendor Evaluation and Sourcing Strategy Frameworks", Forrester
    Research, 2023 [accessed 2026-10-24], https://www.forrester.com;
    primary; summarised fetch; original.
[7] "ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life
    cycle processes — Requirements engineering", International
    Organization for Standardization / IEEE Computer Society, 2018
    [accessed 2026-10-24], https://www.iso.org; primary standard;
    summarised fetch; original.
[8] "A Guide to the Business Analysis Body of Knowledge (BABOK Guide)
    v3", International Institute of Business Analysis (IIBA), 2015
    [accessed 2026-10-24], https://www.iiba.org; primary standard;
    summarised fetch; original.
[9] "The Technology Procurement Handbook: A Practical Guide to Sourcing
    Software, IT Services, and Technology", Sergii Dovgalenko, Kogan Page,
    2020 [accessed 2026-10-24], ISBN 978-1789662177; primary practitioner
    treatise; summarised fetch; original.
[10] "The Request for Proposal Handbook", Michael Asner, Michael Asner
     Consulting / Purchasing Procurement Center, undated [accessed
     2026-10-24], https://www.purchasing-procurement-center.com;
     secondary; summarised fetch; original.
[11] "Modular Procurement: Agile Approaches to Enterprise IT Sourcing",
     National Association of State Chief Information Officers (NASCIO),
     2022 [accessed 2026-10-24], https://www.nascio.org; secondary
     industry report; summarised fetch; original.
[12] "TechFAR Handbook: Procuring Digital Services Using Agile
     Processes", U.S. Digital Service / 18F, 2021 [accessed 2026-10-24],
     https://techfarhub.cio.gov; secondary governmental practice guide;
     summarised fetch; original.
[13] "SaaS vs Custom Software vs Systems Integration Procurement
     Archetypes", Space-O Technologies & Saigon Technology Review, 2023
     [accessed 2026-10-24], https://www.spaceotechnologies.com; secondary
     practitioner analysis; summarised fetch; original.

## Opened and not used

- Tom Sant, *Persuasive Business Proposals* (2004): Off question;
  analyzes supplier-side proposal writing rather than buyer RFP anatomy.
- Alex McPhail, *Win Big The EXA Way* (2021): Off question; covers
  defense capture strategy and supplier bid management.
- City of Mitchell / Temple Terrace municipal RFP specifications: Below
  the bar; public municipal administration templates constrained by
  local statutory purchasing codes.

## Search record

- "CIPS IT procurement RFP template guide": Explored procurement
  institute RFP lifecycle, sourcing plan, and evaluation principles.
- "request for proposal OR RFP template procurement process specification
  cips.org": Identified CIPS tender sections and administrative rules.
- "Request for Proposal RFP template evaluation criteria IT software
  infotech.com": Retrieved Info-Tech IT selection scoring rubrics and
  response codes.
- "Gartner RFP template software selection OR toolkit evaluation
  criteria": Analyzed Gartner SVM sourcing frameworks and demo scoring.
- "Info-Tech Research Group RFP Request for Proposal template vendor
  selection": Extracted Info-Tech RFP Review toolkit structure.
- "RFI RFP RFQ difference BAFO best and final offer cips.org": Mapped
  core RFx vocabulary definitions and relational hierarchy.
- "compliance matrix OR evaluation matrix procurement CIPS": Verified
  distinction between gatekeeper compliance and weighted scoring.
- "Statement of work SOW procurement definition cips.org": Analyzed
  performance vs. conformance SOW specifications.
- "ISO/IEC/IEEE 29148 Request for Proposal OR RFP OR acquirer OR
  acquisition": Evaluated systems engineering acquisition standards.
- "BABOK Request for Proposal OR RFP vendor OR solution": Evaluated
  IIBA vendor assessment techniques and traceability requirements.
- "SaaS OR COTS vs custom software vs systems integration RFP template
  differences": Detailed archetype structural variations.
- "modular RFP OR modular procurement monolithic RFP IT procurement OR
  agile procurement": Ran disconfirming query on monolithic breakdown.
- "RFP package security questionnaire OR security schedule pricing
  schedule response workbook IT procurement": Verified decoupling into
  modular procurement packages.
- "IT procurement Request for Proposal OR RFP book author": Identified
  key practitioner literature.
- "The Technology Procurement Handbook Sergii Dovgalenko RFP OR package
  OR structure OR evaluation": Extracted ITIL Service Design Package
  and cross-functional IT procurement governance.
- "Request for Proposal OR RFP software selection evaluation criteria
  forrester.com": Retrieved Forrester weighting distributions.

Run ended because both parts of the stop rule were satisfied: queries
reached saturation with nothing new from differently-worded variants,
and each perspective of the card (procurement officer, architect) was
substantiated by primary sources within the opening budget.
