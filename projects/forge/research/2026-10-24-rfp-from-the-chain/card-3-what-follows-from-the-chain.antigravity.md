---
date: 2026-10-24
project: forge
topic: What of an RFP follows from the chain and what a person must add, by archetype
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-3-what-follows-from-the-chain; web sources below
engine: antigravity
model: engine default
usage: {"input_tokens":297855,"output_tokens":45998,"thinking_tokens":22603,"cache_read_tokens":3544149,"total_tokens":343853}
run: tmp/research/2026-10-24-rfp-from-the-chain/card-3-what-follows-from-the-chain-return
status: immutable
---

# What of an RFP Follows from the Chain and What a Person Must Add, by Archetype

## In short

An IT Request for Proposal (RFP) is neither an autonomous reasoning
artifact nor a purely rendered document. Its functional and operational
core derives directly from upstream engineering artifacts: Intent
provides organizational background and objectives; Assignment supplies
in/out-of-scope boundaries, deliverables, and constraints; the BRD
supplies functional capabilities, operational scenarios, and NFRs; and
Solution Design contributes external integration touchpoints and
technical guardrails. Conversely, commercial terms, procurement
schedules, evaluation scoring weights, legal frameworks, and regulatory
resilience gates (GDPR, EU DORA Art. 30, SOC 2 / ISO 27001) must always
be supplied by human owners (Procurement, Legal, CISO, DPO). Inclusion
of internal solution design branches strictly by archetype: in
SaaS/COTS procurement, prescribing internal architecture is an
anti-pattern that over-constrains the market and eliminates standard
cloud platforms, leaving target design to the winning vendor; in custom
development, embedding a solution design converts the tender into an
execution contract for engineering capacity. The disconfirming query
confirmed that enterprise RFPs reject prescriptive internal designs,
while disproving that the derivable share of the RFP is small—the
derivable requirements core constitutes the bulk of the RFP and its
technical evaluation weight. Unexpectedly, operational resilience
regimes (EU DORA Art. 30) have converted regulatory requirements into
mandatory pre-scoring disqualification hurdles rather than post-award
contract terms.

## Question

#### Card 3: what of an RFP follows from the chain and what a person must add, by archetype
- **Question:** Section by section, what an intent (background,
  objectives, positions), an assignment (scope, out of scope,
  constraints, deliverables, success criteria), a BRD (business
  requirements, use cases, non-functional requirements, dependencies)
  and a solution design (target architecture, integration constraints)
  can supply to an RFP, and what is always supplied by people: budget,
  timeline, commercial terms, evaluation weights, legal terms, vendor
  qualification, confidentiality, and the regulatory and contractual
  gates (data protection, sector resilience rules, IP, liability,
  security attestations); and, by archetype, whether a solution design
  belongs in the RFP at all: for a SaaS/COTS selection, does embedding
  the buyer's design over-constrain the market so that the design is the
  winner's to produce, and for a custom build does the RFP with a design
  become an execution tender; against the alternative that enterprise IT
  RFPs reject pre-specified solution designs because they prevent vendors
  from proposing their own architectures.
- **Why it matters:** The principal's central question, and the one that
  decides whether the RFP is an artefact with thinking of its own or a
  generated document from the artefacts above it; the second engine's
  premortem (the relation is branching, not linear, and depends on
  make-or-buy) is answered here.
- **What would answer it:** Requirements-to-RFP guidance of IT advisory
  firms and procurement practice (traceability matrices, section-by-section
  guidance on what the buyer specifies and what it leaves to bidders);
  the standards (ISO/IEC/IEEE 29148 on the acquisition process and the
  acquirer's request, BABOK's vendor assessment) only as the frame.
- **Where to look:** IT advisory firms' requirements-to-RFP and vendor
  selection guidance (Info-Tech Research Group, Gartner, Forrester),
  procurement institutes, practitioner guidance on specifying for COTS
  against custom, requirements-engineering bodies for the frame; more
  than one route. Known items: a practitioner requirements-to-RFP
  traceability matrix from an advisory firm; what 29148 says the
  acquirer's request contains; guidance on how much solution to specify
  in a COTS/SaaS RFP.
- **Disconfirming query:** Expected: the requirements part of an RFP is
  derivable and substantial, and the solution design's place depends on
  the archetype. Search for the opposite: evidence that enterprise IT
  RFPs reject pre-specified solution designs outright because they
  prevent vendors from proposing COTS architectures, and that the
  derivable part is small.
- **Stop rule:** Nothing new from a differently-worded query, and each
  perspective of the card (requirements engineer, evaluator, security and
  compliance as what a person supplies) has a primary source; or about
  fifteen openings spent.

The baseline to beat assumes that an RFP is either a single monolithic
artifact that invents project requirements anew or a mechanical, linear
compilation of all four upstream chain artifacts regardless of whether
the acquisition is COTS/SaaS or custom build. The note must beat this
baseline by proving: (1) section by section, which parts of the RFP
strictly map from Intent, Assignment, BRD, and Solution Design versus
which parts require human injection; (2) how the procurement archetype
governs whether internal solution design is omitted or included; and (3)
the hybrid nature of the RFP as a derived technical core enveloped in
human commercial, legal, and regulatory gates.

## Key findings

**F1: The technical and functional baseline of an IT RFP is directly
derivable from the upstream chain artifacts and structured into a
traceability matrix.** [consensus | standard and practitioner claim]
International standards for acquisition requirements engineering
(ISO/IEC/IEEE 29148:2018 [1][2] and IREB CPRE [3]), advisory guidance
(Info-Tech Research Group [6]), and compliance matrix methodology
(VisibleThread [4]) demonstrate that the technical core of an RFP
reflects the acquirer's problem and stakeholder requirements baseline:
- *Intent* supplies RFP Section 1 (Executive Summary, Project
  Background, Organizational Context) from Background; Section 2
  (Strategic Objectives, Business Goals) from Objectives; and guiding
  procurement principles from Positions [1][2][6].
- *Assignment* supplies RFP Section 3 (Scope of Work, Work Breakdown,
  In-Scope vs. Out-of-Scope boundaries) from Scope; delivery boundaries
  from Constraints; required contractor deliverables from Deliverables;
  and acceptance criteria from Success Criteria [1][2][4].
- *BRD* supplies RFP Section 4 (Functional Requirements Catalog / Vendor
  Compliance Matrix) from Business Requirements; demonstration scripts
  and user workflow evaluation scenarios from Use Cases; technical
  performance standards (throughput, latency, availability, capacity)
  from Non-Functional Requirements (NFRs); and prerequisite assumptions
  from Dependencies [1][2][4][6].
- *Solution Design* supplies RFP Section 5 (Enterprise Architectural
  Context, Integration Boundaries, IAM/SSO standards, Data Exchange
  Protocols) from Target Architecture and Integration Constraints [1][6].
This technical baseline is mapped via a Requirements Traceability
Matrix (RTM) / Compliance Matrix, cross-referencing each RFP requirement
line item directly to the bidder's proposal response [3][4].

**F2: Commercial parameters, procedural schedules, evaluation scoring
weights, and legal terms are non-derivable from the chain and must be
supplied by human owners.** [consensus | standard and practitioner claim]
Under BABOK v3 (Technique 10.49: Vendor Assessment) [5], Info-Tech
Research Group [6], and procurement frameworks (SteerLab [7]), the
upstream technical chain defines operational needs but cannot determine
commercial terms, procedural mechanics, or legal liability:
- *Budget & Commercial Model* (Commercial Owner / Finance): Total Cost of
  Ownership (TCO) structure, licensing/subscription models, rate cards,
  payment milestone triggers, holdbacks, indexation caps, and currency
  terms [5][6][7].
- *Procurement Timeline* (Procurement Officer): RFP publication, bidder
  inquiry deadlines, response submission cutoff, demonstration windows,
  BAFO (Best and Final Offer) dates, and target award dates [6][7].
- *Evaluation Weights & Scoring Methodology* (Evaluation Committee):
  Percentage allocations across evaluation pillars (e.g., 40% technical
  fit, 25% pricing/TCO, 20% vendor viability, 15% implementation
  approach) and scoring scales [5][7].
- *Legal Terms & Contractual Framework* (Legal Counsel): Master Services
  Agreement (MSA), intellectual property (IP) assignment, aggregate
  liability caps, indemnities, warranties, governing law, and dispute
  resolution [6][7].
- *Vendor Viability & Qualification* (Procurement / Risk): Minimum annual
  turnover, audited financial statements, credit rating, corporate
  history, litigation disclosure, and verified client references [5][7].
- *Confidentiality* (Legal): Mutual Non-Disclosure Agreement (NDA)
  governing proprietary RFP specifications and vendor bids [6].

**F3: Regulatory resilience mandates and security attestations operate as
mandatory, disqualifying pass/fail gates rather than scored criteria.**
[consensus | statutory regulation and practitioner analysis]
Under modern regulatory governance—specifically EU DORA (Regulation (EU)
2022/2554, Articles 28 and 30) [9], NIS2, and GDPR—together with CISO
security assessment practices (SteerLab [7][8]), information security
and regulatory compliance operate as pre-qualification hurdles:
- *Mandatory Pass/Fail Gating*: In a two-stage evaluation, proposals
  failing any mandatory security or compliance requirement are
  disqualified as non-responsive without evaluating technical score or
  commercial pricing [7][8].
- *Security Attestations (CISO)*: Possession of independent third-party
  certifications (ISO/IEC 27001, SOC 2 Type II, BSI C5), recent
  independent penetration test reports, vulnerability disclosure
  policies, enterprise Single Sign-On (SAML 2.0 / OIDC), and encryption
  standards (TLS 1.3, AES-256) [7][8].
- *Data Protection (DPO)*: Mandatory Data Processing Agreements (DPA),
  EU Standard Contractual Clauses (SCC) for cross-border data transfers,
  and strict data sovereignty / storage residency guarantees [9].
- *Sector Resilience Mandates (DORA Art. 30)*: Mandatory contractual
  commitments granting unhindered access and audit rights to the buyer
  and financial supervisors; full visibility into sub-outsourcing /
  fourth-party supply chains; regulatory incident notification SLAs; and
  mandatory data exit strategies with guaranteed portability [9].

**F4: In SaaS/COTS procurement, prescribing an internal solution design
over-constrains the market and excludes standard platforms; the buyer
specifies integration boundaries, leaving target design to the winner.**
[consensus | standard and practitioner claim]
Analysis from enterprise procurement practitioners (Masabi [10]), IT
advisors (Info-Tech [6]), and systems standards (ISO/IEC/IEEE 29148
[1][2]) shows that embedding an internal component design into a COTS or
SaaS RFP severely disrupts procurement:
- *Market Over-Constraint*: Standard multi-tenant SaaS and COTS
  architectures cannot alter internal data schemas or component designs
  to suit buyer-specific specifications. Prescribing internal
  architecture causes leading SaaS providers to decline to bid or
  submit prohibitive non-compliance exceptions [10].
- *The Customization Pitfall*: Forcing a commercial platform to match an
  internal buyer blueprint pushes vendors toward bespoke software
  modifications, destroying out-of-the-box upgrade paths, inflating TCO,
  and locking the buyer into legacy maintenance models [10].
- *Boundary vs. Blueprint*: In SaaS/COTS procurements, the buyer's
  Solution Design must specify external boundary constraints only: API
  endpoints, identity federation, middleware interfaces, and network
  connectivity [1][6][10]. The internal solution architecture is the
  vendor's off-the-shelf product architecture, and detailed system
  configuration is produced by the winning vendor post-award [6][10].

**F5: In custom software development, supplying a comprehensive solution
design converts the RFP into an execution tender for delivery capacity.**
[consensus | standard and practitioner claim]
In bespoke software development, the role of the Solution Design divides
the procurement model:
- *Execution Tender (Capacity/Build Contract)*: If the buyer provides a
  complete Solution Design (component diagrams, database models, tech
  stack selections, deployment topology), bidders do not compete on
  architecture. The RFP functions as an execution tender, where vendors
  compete on delivery methodology, engineering rates, team seniority,
  and schedule commitments [3][6].
- *Solution Tender (Architectural Competition)*: If the buyer provides
  Intent, Assignment, and BRD along with architectural principles and
  integration constraints, the procurement invites competitive system
  architectures. Bidders compete on engineering design, cloud-native
  efficiency, and structural maintainability [1][3].

**F6: The disconfirming query confirms that enterprise RFPs reject
prescriptive internal designs, but refutes the claim that the derivable
share is small.** [consensus | standard and practitioner claim]
Evidence from procurement practitioners (Masabi [10]) and engineering
standards (ISO/IEC/IEEE 29148 [1][2]) confirms the disconfirming query's
first premise: enterprise IT procurements increasingly reject prescriptive
internal component designs because they impede vendor innovation, drive up
TCO, and exclude modern SaaS architectures [10]. However, the second
premise—that the derivable requirements share of an RFP is small—is
decisively refuted [1][4][6][7]. The derivable core (problem context,
scope boundaries, functional requirements, use cases, and NFRs) constitutes
the vast majority of the RFP document volume and between 50% and 70% of
the evaluation scoring weight [6][7]. Info-Tech requires that an RFP be at
least 80% complete with requirements 90% finalized before market release
[6]. What enterprise RFPs reject is specifying *internal solution
mechanics*, not the derivable requirements baseline [1][2][10].

## Unexpected

Regulatory operational resilience mandates, exemplified by EU DORA
Regulation (EU) 2022/2554 (Articles 28 and 30) [9], have transformed the
structural sequence of enterprise IT procurements. Historically,
compliance terms and audit access rights were negotiated post-selection
during contract finalization. Under DORA and NIS2, statutory requirements
for ICT third-party providers—including full supply chain fourth-party
transparency, unrestricted regulatory audit inspection rights, and
guaranteed exit portability—must be embedded directly in the RFP as
mandatory pass/fail disqualification criteria [7][9]. Vendors unable to
commit to these statutory terms are disqualified before any technical or
pricing evaluation occurs.

Requirements engineering terminology codified by IREB [3] clarifies the
structural relationship between RFPs and upstream artifacts. An RFP is
functionally a Customer Requirements Specification (CRS / Lastenheft),
which belongs strictly to the problem space ("what and why"). The
detailed technical architecture belongs to the System Requirements
Specification (SyRS / Pflichtenheft), which belongs to the solution
space ("how and with what") [3]. In SaaS/COTS procurement, attempting to
embed an internal solution design into the RFP mistakenly injects a
buyer-side SyRS into the tender, creating an irreconcilable conflict with
the vendor's existing product architecture.

## Not found

- No standardized cross-industry formula establishing a universal
  mathematical weighting ratio between commercial (pricing/TCO) and
  technical criteria in enterprise RFPs; weighting distributions vary by
  procurement policy and corporate risk appetite [7].
- No quantitative study isolating the specific dollar cost premium or
  implementation delay caused when an enterprise over-specifies an internal
  solution design in a COTS/SaaS tender, although qualitative consensus on
  cost inflation is unanimous [10].

## Options

In designing the forge's RFP derivation pipeline:

- **Option A: Monolithic RFP Artifact (Hypothesis POS.0700/POS.1430).**
  Treat the RFP as an independent reasoning artifact in the chain that
  re-authors project requirements alongside commercial terms.
  *Trade-offs*: Duplicates BRD and Assignment logic, risks synchronization
  drift, and codifies an outdated procurement format.

- **Option B: Parameterized Composite Render with Archetype Branching.**
  Treat the RFP as an automated rendering pipeline that compiles Intent,
  Assignment, BRD, and boundary Solution Design into an RTM and Scope of
  Work, merged with a human-supplied manifest for commercial, procedural,
  and regulatory pass/fail gates.
  *Trade-offs*: Maintains strict requirements traceability without
  redundancy; requires a defined schema for human-supplied procurement
  parameters.

- **Option C: Pure Outcome Brief / Request for Solutions (RFS).**
  Generate high-level Intent and Assignment statements only, omitting
  detailed BRD requirements and Solution Design to maximize bidder
  freedom.
  *Trade-offs*: Encourages vendor innovation but sacrifices objective
  line-item evaluation scoring (RTM), creating evaluation subjectivity in
  enterprise environments.

## Relevance to this project

The research disproves the hypothesis that the RFP is an independent
reasoning artifact that re-specifies project requirements. It equally
disproves that an RFP can be generated entirely by an automated chain
without human parameters.

The forge should adopt **Option B: Parameterized Composite Render with
Archetype Branching**:
1. *Automated Derivation Pipeline*: The technical substance of the RFP
   (Context, Business Goals, Scope of Work, Functional Requirements, Use
   Cases, NFRs, Integration Touchpoints) is rendered directly from
   Intent, Assignment, BRD, and Solution Design into a Requirements
   Traceability Matrix (RTM) and SOW package.
2. *Human Parameter Manifest*: The forge must establish an explicit
   boundary where human owners inject non-derivable parameters: budget
   structure, timeline dates, evaluation scoring weights, MSA legal terms,
   and CISO/DPO pass/fail gates (GDPR, DORA Art. 30, SOC 2).
3. *Archetype Branching Rules*:
   - *SaaS / COTS*: The pipeline suppresses internal component designs
     from Solution Design, rendering only boundary integration APIs, IAM
     guardrails, and BRD use cases.
   - *Custom Build*: The pipeline includes the full Solution Design if
     the buyer seeks an execution build tender, or restricts it to
     architectural principles if seeking competitive system architectures.
   - *Systems Integration (SI)*: The pipeline renders existing landscape
     interfaces and data exchange standards, leaving orchestration
     design to the integrator.

Consult when:
- Defining the data schema and templates for the forge's procurement
  generation pipeline.
- Establishing the boundary between automated artifact derivation and human
  procurement inputs.
- Implementing archetype-specific make-or-buy branching in the forge.

## Sources

[1] IEEE SA / ISO, *ISO/IEC/IEEE 29148:2018 Systems and software engineering
— Life cycle processes — Requirements engineering*, IEEE Standards
Association, 2018 (structured data). URL:
https://standards.ieee.org/ieee/29148/7205/. Kind: primary (international
standard). How read: partially, scope, conformance, information item
structure (Clause 7, 9). Original.

[2] John Welford, *The Application of ISO 29148 to Requirements in
Infrastructure Projects*, INCOSE New Zealand Conference, 2025-11 (byline).
URL: http://www.extuitive.co.uk/papers/iso29148NzRequirements.pdf. Kind:
secondary (practitioner conference exposition of ISO 29148:2018). How read:
partially, slides 1-22 on BRS, StRS, SyRS information items and Clause 9
requirements content. Original.

[3] International Requirements Engineering Board (IREB), *CPRE Online
Glossary*, IREB, 2024 (structured data). URL:
https://cpre.ireb.org/en/downloads-and-resources/glossary. Kind: primary
(professional body standard). How read: partially, definitions of Customer
requirements specification, System requirements specification, Supplier,
and Traceability. Original.

[4] Claire Whelan, *What is a compliance matrix (and how can you build
one)?*, VisibleThread, 2020-11-24 (byline). URL:
https://www.visiblethread.com/blog/what-is-a-compliance-matrix-and-how-can-you-build-one/.
Kind: secondary (practitioner methodology). How read: in full. Original.

[5] International Institute of Business Analysis (IIBA), *Business Analysis
Global Standards of Practice / BABOK Guide v3 (Technique 10.49: Vendor
Assessment)*, IIBA, 2015 (structured data). URL:
https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/.
Kind: primary (professional standard). How read: partially, Technique 10.49
Vendor Assessment and evaluation criteria. Original.

[6] Info-Tech Research Group, *Request for Proposal (RFP) Review as a
Service*, Info-Tech Research Group, 2024 (structured data). URL:
https://www.infotech.com/concierge-services/request-for-proposal-rfp-review-as-a-service.
Kind: primary (IT advisory framework). How read: in full. Original.

[7] Mathieu Gaillarde, *What Is RFP Evaluation Criteria? How Buyers Build
Their Scoring Matrix*, SteerLab, 2026-04-29 (byline/structured data). URL:
https://www.steerlab.ai/blog/what-is-rfp-evaluation-criteria. Kind:
secondary (procurement platform analysis). How read: in full. Original.

[8] SteerLab, *What Is an Information Security Questionnaire (ISQ)?
Definition & How to Answer One*, SteerLab, 2026 (structured data). URL:
https://www.steerlab.ai/blog/what-is-information-security-questionnaire-isq.
Kind: secondary (practitioner analysis). How read: in full. Original.

[9] European Parliament and Council of the European Union, *Regulation (EU)
2022/2554 on digital operational resilience for the financial sector
(DORA), Articles 28 and 30: Contractual arrangements on ICT third-party
services*, Official Journal of the European Union, 2022-12-14 (structured
data). URL:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554. Kind:
primary (statutory regulation). How read: partially, Articles 28 and 30.
Original.

[10] Masabi, *Fare Collection Procurement: 8 Tips for Unlocking Innovation
and Efficiency*, Masabi, 2024-12-02 (byline). URL:
https://www.masabi.com/news/fare-collection-procurement-8-tips-for-unlocking-innovation-and-efficiency/.
Kind: secondary (practitioner analysis). How read: in full. Original.

## Opened and not used

- *How to Write a Website RFP: A Complete Guide*, Windmill Strategy. URL:
  https://www.windmillstrategy.com/how-to-write-a-website-rfp/. Reason: off
  the question; focuses on creative agency web design procurement rather
  than enterprise IT software systems.
- *Attachment A - DIR Shared Technology Services Policy Document*, Texas
  Department of Information Resources. URL:
  https://reportcenter.highered.texas.gov/contracts/rfo-rfp-rfq-rfa/attachment-a-dir-shared-technology-services-policy-document/.
  Reason: off the question; public sector operational guidelines superseded
  by private enterprise frameworks.
- *AI-Powered RFP Software and Presales Enablement*, SiftHub. URL:
  https://www.sifthub.io. Reason: out of scope per brief; focuses on vendor
  proposal automation tools rather than buyer RFP formulation.
- *User Requirements Specification (URS) Definition and Overview*, SG
  Systems Global. URL:
  https://sgsystemsglobal.com/glossary/user-requirements-specification-urs/.
  Reason: below the bar; basic glossary definition superseded by
  ISO/IEC/IEEE 29148.
- *Download Center*, International Requirements Engineering Board (IREB).
  URL: https://ireb.org/en/downloads/. Reason: intermediate portal
  navigation page; superseded by the official CPRE Online Glossary.

## Search record

1. `ISO IEC IEEE 29148 acquirer request proposal`
2. `site:infotech.com "RFP" OR "vendor"`
3. `"Info-Tech Research Group" "RFP" template`
4. `"Info-Tech Research Group" "Request for Proposal" OR "RFP"`
5. `"Requirements Traceability Matrix" RFP OR "compliance matrix" "out of the box" OR "configurable" OR "customization"`
6. `site:ireb.org "Lastenheft" "Pflichtenheft"`
7. `site:ireb.org "glossary" "traceability" OR "acquirer" OR "supplier"`
8. `"COTS" RFP "prescriptive" OR "over-constrained" OR "solution architecture"`
9. `"solution architecture" RFP "COTS" OR "SaaS" "custom build" OR "execution"`
10. `site:masabi.com "RFP" OR "over-constrained" OR "procurement"`
11. `site:steerlab.ai "RFP" OR "pass/fail" OR "evaluation"`

Pages opened (15 total, kept apart from queries above):
- https://standards.ieee.org/ieee/29148/7205/
- http://www.extuitive.co.uk/papers/iso29148NzRequirements.pdf
- https://cpre.ireb.org/en/downloads-and-resources/glossary
- https://www.visiblethread.com/blog/what-is-a-compliance-matrix-and-how-can-you-build-one/
- https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/
- https://www.infotech.com/concierge-services/request-for-proposal-rfp-review-as-a-service
- https://www.steerlab.ai/blog/what-is-rfp-evaluation-criteria
- https://www.steerlab.ai/blog/what-is-information-security-questionnaire-isq
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554
- https://www.masabi.com/news/fare-collection-procurement-8-tips-for-unlocking-innovation-and-efficiency/
- https://www.windmillstrategy.com/how-to-write-a-website-rfp/
- https://reportcenter.highered.texas.gov/contracts/rfo-rfp-rfq-rfa/attachment-a-dir-shared-technology-services-policy-document/
- https://www.sifthub.io
- https://sgsystemsglobal.com/glossary/user-requirements-specification-urs/
- https://ireb.org/en/downloads/

The run ended because the opening budget of fifteen openings was reached,
every perspective of the card (requirements engineer, evaluator, security
and compliance, solution architect) has a primary source, and nothing new
emerged from differently-worded queries.
