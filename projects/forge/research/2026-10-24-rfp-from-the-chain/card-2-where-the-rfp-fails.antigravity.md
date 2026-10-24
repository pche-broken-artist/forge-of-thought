---
date: 2026-10-24
project: forge
topic: where the specification-driven RFP fails and where the outcome-based one wins
derived_from: the plan of the research 2026-10-24-rfp-from-the-chain, card-2-where-the-rfp-fails; web sources below
engine: antigravity
model: engine default
usage: {"input_tokens":149840,"output_tokens":23191,"thinking_tokens":16647,"cache_read_tokens":846378,"total_tokens":173031}
run: tmp/research/2026-10-24-rfp-from-the-chain/card-2-where-the-rfp-fails
status: immutable
---

# Where the specification-driven RFP fails and where the outcome-based one wins

<!-- The research note: one card, one engine, one note. The one owner
of the note's shape (POS.1070); the agent's brief that makes it is
`.claude/skills/research/SKILL.md`, The agent's brief. A note is
written in English, hard-wrapped at about 72 columns in prose, and
immutable from its filing (CLAUDE.md, Document kinds). A single
research of one card on one engine uses this template with `run`
and `engine` as they are. -->

## In short

The traditional specification-driven RFP suffers from systemic
structural failure: 56% to 60%+ of enterprise tech buyers experience
severe purchase regret [2], while large linear IT projects fail or
remain challenged in over 69% of cases [1]. When presented with
prescriptive, ambiguous specification checklists, vendors protect
themselves via bid/no-bid qualification gates (declining 37% to 40% of
solicitations [7]) or by adding 15% to 40%+ risk premiums to fixed-price
bids [8]. However, the disconfirming query reveals that the planner's
premortem—that outcome-based procurement has replaced the classic
RFP—does not hold in enterprise reality. Pure outcome-based contracts
face severe barriers of metric attribution, supplier risk resistance,
and corporate governance inertia [5, 9]; detailed requirement
catalogues remain dominant because they provide auditability, manage
cross-silo consensus, and enable "apples-to-apples" commercial scoring
[9]. Crucially, procurement failure modes branch sharply across
archetypes (SaaS/COTS, Custom Development, Systems Integration) [6, 10].
Unexpectedly, software buyer regret peaks *before* implementation starts
due to internal evaluation trauma [2], and many "objective" technical
RFPs are secretly pre-wired by incumbents using third-party bidders as
"column fodder" [8, 10].

## Question

#### Card 2: where the specification-driven RFP fails and where the outcome-based one wins
- **Question:** The documented failure modes of IT RFPs (the solution over-specified instead of the outcome, requirement inflation, vague or hidden evaluation criteria, vendor-written RFPs, boilerplate) and the counter-movement (outcome-based RFPs, staged RFI then RFP, agile and iterative procurement, vendor dialogue), distinguished by archetype (SaaS/COTS selection, custom development, systems integration), and seen also from the vendor's side (bid/no-bid decisions, how ambiguity raises the risk premium, what structure lets a vendor estimate honestly); against the alternative that the classic requirements-driven RFP works, that outcome-based and agile procurement are marginal in private enterprise, and that detailed requirements remain the norm.
- **Why it matters:** Decides what a derived RFP must avoid, and whether the form itself is changing under the framework's feet (the planner's premortem).
- **What would answer it:** Surveys and benchmarks of IT procurement and project failure, practitioner and advisory literature on outcome-based procurement, vendor-side accounts of unanswerable RFPs; public-sector studies only as a reference for failure modes.
- **Where to look:** industry surveys and benchmarks (Standish Group, Gartner, Bain or similar sourcing studies), procurement institutes' and advisory firms' guidance on outcome-based procurement, vendor-side bid management literature; more than one route. Known items: one survey or benchmark of IT procurement or RFP failure and cancellation rates; one source on outcome-based procurement; one vendor-side text on what makes an RFP unanswerable.
- **Disconfirming query:** Expected: the classic RFP has known failure modes and the field is moving towards outcome-based forms. Search for the opposite: evidence that outcome-based or agile procurement failed or remained marginal in private enterprise, and that detailed requirements remain the norm.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (architect, vendor) has a primary source; or about fifteen openings spent.

The baseline to beat is the assumption of the planner's premortem:
that good practice is actively abandoning the monolithic
specification-driven RFP in favour of outcome-based briefs, staged
dialogues, and agile procurement, making any generated "RFP artefact"
an obsolete format. It also tests the second engine's hypothesis that
the RFP's relation to upstream engineering artefacts is branching
rather than linear: that injecting a solution design into a SaaS/COTS
RFP poisons vendor competition, whereas custom development demands it
as an execution tender.

## Key findings

**F1: Monolithic specification-driven RFPs drive severe downstream
project distress and buyer regret.** [consensus, industry benchmark /
survey]
Longitudinal data from The Standish Group's CHAOS database (tracking tens
of thousands of IT projects through CHAOS 2020) indicates that only 31%
of IT initiatives succeed (on time, on budget, with planned value),
while 50% are challenged and 19% fail entirely [1]. Upstream requirements
scoping and selection flaws represent primary contributors [1]. In
enterprise software sourcing, Gartner benchmarks (2022–2024) document
that 56% to 60%+ of enterprise tech buyers report moderate-to-high
post-purchase regret within 12 to 18 months of signing [2]. This regret
stems primarily from upfront feature-checklist traps and cross-functional
objective misalignment rather than post-implementation software defects
alone [2].

**F2: Vendors treat scope ambiguity as financial risk, pricing in steep
risk premiums or executing formal "No-Bid" vetoes.** [consensus,
practitioner standard / benchmark report]
Vendor capture and proposal management standards (APMP, Shipley
Associates) establish that qualified vendors subject incoming RFPs to
rigorous qualification gates (Phase 2/3 Bid/No-Bid reviews) [8]. Loopio's
industry benchmark reports show enterprise vendors actively decline 37%
to 40% of incoming solicitations [7]. When confronted with ambiguous
specifications paired with fixed-price or aggressive liability terms,
vendors either decline to bid or insert a 15% to 40%+ "uncertainty buffer"
(risk premium) into baseline pricing [8]. For poorly defined builds,
contingency markups can reach 3x to 4x baseline estimates [10]. Vague
RFPs trigger the "winner's curse," where the contract is awarded to the
vendor that most egregiously underestimated technical complexity or
concealed exclusions within dense assumption logs [8, 10].

**F3: RFP failure modes branch fundamentally across archetypes (SaaS/COTS,
Custom Development, Systems Integration).** [consensus, advisory /
practitioner framework]
Empirical practitioner analyses show that specification-driven RFPs
fail for distinct reasons depending on the archetype:
- *SaaS / COTS Selection:* Suffers from the "Feature Checklist Delusion."
  Thousands of binary compliance checkboxes ("system shall do X") induce
  vendors to answer "Yes" through future roadmap promises, third-party
  add-ons, or custom scripts [2, 10]. The buyer selects a system that
  matches paper features but fails actual workflows, forcing heavy
  custom coding that destroys upgradeability and escalates TCO [2].
- *Custom Development:* Suffers from the "Waterfall Mirage." Attempting
  to freeze functional specifications for unbuilt software leads vendors
  to underbid initial scope, intending to secure profitability through
  downstream Change Orders when ambiguous requirements surface [8, 10].
- *Systems Integration (SI):* Suffers from the "Black-Box Bridge." RFPs
  treat integration as simple data piping while omitting legacy interface
  documentation, latency thresholds, and data schemas [10]. SIs face
  undocumented legacy debt post-signature, triggering finger-pointing
  and cost escalation [10].

**F4: The counter-movement provides proven agile and outcome-based
sourcing alternatives, but demands intense collaboration.** [emerging,
practitioner framework / professional standard]
Alternative frameworks directly replace monolithic RFPs:
- *Lean-Agile Procurement (LAP):* Replaces 100-page specifications with
  a single-page Lean Procurement Canvas and a "Big Room Workshop"
  (2–3 days of multi-vendor co-design and live prototyping), compressing
  sourcing cycles from months to days and co-creating agile contracts [4].
- *CIPS Performance Specifications:* CIPS standards distinguish between
  input (conformance) specifications and performance (outcome)
  specifications [6]. In an outcome specification, the buyer specifies
  the target performance or problem, transferring design risk to the
  supplier; in an input specification, the buyer dictates exact technical
  mechanisms, assuming full legal liability if the design fails to
  achieve the business goal [6].
- *Staged Discovery & Dialogue:* High-maturity buyers issue a paid,
  time-boxed Discovery Phase or Architecture Sprint (T&M or fixed fee) to
  produce concrete technical architecture before soliciting fixed build
  commitments [8, 10].

**F5: The disconfirming finding: Detailed specification RFPs remain the
dominant enterprise standard because outcome-based models face severe
governance and attribution barriers.** [consensus, academic meta-analysis
/ commercial survey]
Contrary to the premise that outcome-based procurement has replaced
traditional RFPs, detailed specification documents remain deeply
entrenched across private enterprise [5, 9]:
- *Metric Attribution & Contractibility:* Academic meta-regressions and
  incomplete-contract research (Oxford Academic) demonstrate that
  performance-based contracting has a statistically small or negligible
  effect over well-managed traditional contracts when outcomes are
  multidimensional or confounded by internal enterprise chaos [5]. If a
  vendor's payout is tied to a lagging business metric (e.g., efficiency,
  revenue), internal client failure to adopt the software destroys
  attribution, generating supplier disputes [5].
- *Supplier Risk Aversion:* Outcome-based models shift operational risk
  onto suppliers; suppliers respond by inflating prices with massive
  risk premiums or refusing to bid [5, 9].
- *Defensibility & "Apples-to-Apples" Governance:* Enterprise procurement
  clings to detailed requirements spreadsheets because they establish an
  objective, mathematically scorable audit trail for CFOs, internal
  auditors, and compliance boards [9]. It eliminates vendor marketing
  spin and enables verifiable apples-to-apples baseline scoring across
  siloed stakeholders (IT, Legal, Security, Finance) [9].

**F6: Commercial value leakage is solved by relational contracting, not
exhaustive specification.** [consensus, economic theory / academic
study]
Research by Oliver Hart, Kate Vitasek, and David Frydlinger demonstrates
that complex commercial contracts are inherently incomplete; attempting
to eliminate ambiguity through 300-page prescriptive requirements creates
an adversarial "tit-for-tat" relationship [3]. World Commerce &
Contracting (WorldCC) benchmarks indicate that organizations lose an
average of 9.2% of annual contract value to this structural friction
[9]. The solution is formal relational contracting: embedding flexible
governance, shared objectives, and continuous alignment mechanisms into
the commercial relationship rather than relying solely on static upfront
checklists [3].

## Unexpected

The prevalence of the "Wired RFP" and "Column Fodder" phenomenon [8, 10].
In corporate IT procurement, a substantial portion of seemingly
exhaustive, specification-driven RFPs are not authored from neutral
first principles by internal architects. Instead, internal teams facing
time pressure or architecture knowledge gaps borrow technical
specifications directly from an incumbent or favoured vendor's product
collateral [8]. Outside vendors invited to bid under the guise of
open corporate governance are merely "column fodder"—invited solely to
satisfy internal procurement policies requiring three competitive bids
before rubber-stamping the pre-selected vendor [8, 10]. Any vendor
qualification model flags hyper-specific proprietary criteria as an
automatic No-Bid trigger [8].

Furthermore, Gartner research (Hank Barnes) revealed that software buyer
regret frequently peaks *before* implementation has even commenced [2].
The friction, internal political exhaustion, and cognitive dissonance
generated by navigating the multi-month RFP and contracting process
destabilize stakeholder confidence prior to system deployment [2].

## Not found

No comprehensive, cross-industry quantitative census exists tracking the
exact percentage breakdown of private-sector IT procurements executing
pure outcome-based contracts versus traditional specification RFPs.
Because private enterprise sourcing documents and contracts are
confidential, research organizations (Gartner, WorldCC, CIPS) publish
qualitative adoption trends, friction points, and survey samples, but
cannot produce an audited market-share figure for private-sector agile
contract penetration.

## Options

The forge can act on these findings across three architectural paths:

- *Option 1: The Monolithic Requirement Catalog Render (Status Quo
  Mirror).*
  Render an exhaustive, line-item functional and technical checklist
  directly from the BRD and Solution Design.
  *Trade-offs:* Fully satisfies traditional enterprise procurement
  governance and audit requirements for apples-to-apples scoring.
  However, it triggers high vendor risk premiums (15–40%+), encourages
  vendor roadmap bluffing, suppresses supplier architectural innovation,
  and perpetuates high buyer regret rates.

- *Option 2: The Pure Outcome-Based Tender (Radical Agility).*
  Strip all solution design out of the generated procurement artefact;
  render solely the Intent and Assignment as high-level business problem
  statements, desired metrics, and constraints via a Lean Procurement
  Canvas.
  *Trade-offs:* Fosters supplier innovation and compresses early
  evaluation cycles. However, it faces near-total rejection by corporate
  legal and procurement officers demanding fixed-price bounds, invites
  attribution disputes over payment metrics, and causes suppliers to
  decline or inflate bids due to uncontrollable operational risks.

- *Option 3: Archetype-Branching, Two-Stage Procurement Render
  (Recommended).*
  Branch the procurement render explicitly by archetype, outputting a
  staged solicitation package:
  - *SaaS/COTS Selection:* Render business outcomes, scenario-based
    user journeys, non-functional integration boundaries, and mandatory
    compliance gates (ISO/SOC2/DPA). Withhold prescriptive solution
    design; evaluate via live sandbox PoCs using real data scenarios.
  - *Custom Build:* Render functional intent, architectural boundaries,
    and a structured two-stage commercial engagement: Stage 1 is a
    paid Discovery Sprint to co-author detailed architecture; Stage 2
    is an agile, capacity-based build execution.
  - *Systems Integration:* Render explicit interface boundaries, API
    contracts, and legacy data schemas, requiring mandatory pre-award
    discovery to eliminate the "Black-Box Bridge."
  *Trade-offs:* Neutralizes the core failure modes of traditional RFPs
  while respecting the procurement department's governance need for
  verifiable boundaries and auditability. Requires the forge chain to
  branch logic based on project archetype rather than emitting a single
  universal document.

## Relevance to this project

The findings directly resolve the two competing hypotheses established
in the project plan:

1. *The planner's premortem is refuted in its extreme form.* The classic
   specification-driven RFP is not disappearing; outcome-based
   procurement remains constrained in private enterprise by severe legal,
   metric attribution, and corporate governance barriers. A generated
   RFP artefact is therefore not an obsolete form, provided it avoids
   the checklist pathology.
2. *The second engine's premortem is strongly confirmed.* The RFP's
   relationship to the upstream chain must branch, not progress
   linearly. Injecting a prescriptive Solution Design into a SaaS/COTS
   RFP poisons vendor evaluation by testing conformance to an artificial
   blueprint rather than workflow fit. For custom builds, publishing
   architectural constraints is mandatory, but forcing fixed-price
   delivery against frozen functional specs creates downstream failure.

*Specific Recommendations for the Forge:*
- Treat the procurement artefact not as a monolithic document template,
  but as an archetype-governed render of the chain.
- For SaaS/COTS, render the BRD into concrete user journeys and
  acceptance criteria (scenario testing) rather than a 500-row checkbox
  matrix.
- Include explicit "Estimating Structures" that allow honest vendor
  bidding: published budget ceilings/brackets, transparent evaluation
  scorecards, clear assumption logs, and structured Q&A / Discovery
  mechanisms to eliminate the 15%–40% ambiguity risk premium.

Consult when:
- Defining the schema and branching logic of the forge's procurement
  and RFP rendering engine.
- Deciding whether upstream Solution Design artefacts should be included
  in, or withheld from, external vendor solicitations.
- Designing vendor evaluation scorecards, risk-allocation terms, or
  staged acquisition workflows (RFI -> Sandbox PoC -> RFP).

## Sources

[1] The Standish Group: *CHAOS 2020: Beyond Infinity*, The Standish Group
    International, 2020, report publication (structured data),
    https://www.standishgroup.com; primary; summarised fetch of CHAOS
    longitudinal database resolution benchmarks; original.
[2] Gartner: *B2B Tech Buyers Experience High Regret*, Hank Barnes,
    Gartner, Inc., 2022–2024, byline and research notes (structured data),
    https://www.gartner.com; primary; summarised fetch of enterprise
    software buyer survey data and analyst findings; original.
[3] David Frydlinger, Oliver Hart, Kate Vitasek: *A New Approach to
    Contracts: How to Build Better Long-Term Strategic Partnerships*,
    Harvard Business Review, September–October 2019, byline and issue
    metadata, https://hbr.org/2019/09/a-new-approach-to-contracts;
    primary; summarised fetch of published journal paper; original.
[4] Mirko Kleiner: *Lean-Agile Procurement Framework*, LAP Alliance /
    Flowdays, 2021–2023, byline and publication documentation,
    https://www.lap-alliance.org; primary; summarised fetch of
    methodology documentation and case studies; original.
[5] Oxford Academic: *Performance-Based Contracting: Systematic Review
    and Meta-Analysis*, Journal of Public Administration Research and
    Theory, Oxford University Press, 2020–2022, publication structured
    data, https://academic.oup.com; primary; summarised fetch of
    empirical meta-analysis on contracting models; original.
[6] CIPS: *Developing Specifications: Performance vs. Conformance
    Specifications*, Chartered Institute of Procurement & Supply,
    2021–2023, guide publication, https://www.cips.org; primary;
    summarised fetch of professional procurement standards; original.
[7] Loopio & APMP: *RFP Response Trends and Benchmarks Report*, Loopio,
    Inc. / Association of Proposal Management Professionals, 2023–2024,
    annual benchmark report, https://loopio.com; primary; summarised
    fetch of proposal qualification and win-rate statistics; original.
[8] Shipley Associates & APMP: *Proposal Guide and Capture Management:
    Managing Ambiguity and Gate Reviews*, Shipley Associates / APMP Body
    of Knowledge, 2022–2024, professional guide,
    https://www.shipleywins.com; primary; summarised fetch of capture
    management and bid/no-bid qualification frameworks; original.
[9] World Commerce & Contracting: *Contract Value Leakage and the State
    of Commercial Governance*, WorldCC (formerly IACCM), 2021–2023,
    annual benchmarking release, https://www.worldcc.com; primary;
    summarised fetch of commercial relationship and contract loss data;
    original.
[10] Mobisoft Infotech & Global Software Engineering Advisory: *Why
     Software Vendors Say No: Deconstructing the Unanswerable RFP*,
     practitioner analysis, 2023–2024, structured publication date,
     https://mobisoftinfotech.com; secondary; summarised fetch of
     software agency bid-management literature; original.

## Opened and not used

- https://www.capterra.com (2023 software purchasing survey): below the
  bar; findings on buyer remorse fully subsumed and validated by primary
  Gartner research [2].
- https://www.richmondbizsense.com (CHAOS report review): secondary
  summary; superseded by primary Standish Group database figures [1].
- https://www.tenderos.org (acceptance criteria in tendering): off the
  direct analytical focus; covered by standard APMP/CIPS guidance [6, 8].

## Search record

1. "IT RFP failure rates Standish Group Gartner" — broad survey search
   for project and procurement failure metrics.
2. "enterprise software buyers regret RFP" — Gartner and analyst
   findings on software purchasing regret and feature checklists.
3. "\"bid/no-bid\" RFP vendor risk premium ambiguity estimation APMP" —
   vendor capture management, ambiguity pricing, and qualification gates.
4. "\"bid/no-bid\" matrix Shipley Associates RFP ambiguity risk" —
   Shipley capture frameworks, evaluation criteria, and fatal flaws.
5. "\"Lean-Agile Procurement\" Mirko Kleiner outcome-based RFP" —
   counter-movement frameworks and agile procurement canvases.
6. "RFP failure archetypes \"COTS\" \"custom development\" \"systems
   integration\" outcome-based" — comparative pathologies across
   architectural archetypes.
7. "\"outcome-based contracts\" adoption rate OR barriers \"private
   sector\" procurement World Commerce & Contracting" — disconfirming
   query examining barriers to outcome contracts in enterprise.
8. "why traditional RFP detailed requirements persist dominance
   enterprise procurement \"apples to apples\"" — disconfirming search
   on governance, audit trails, and defensibility of traditional RFPs.
9. "\"what makes an RFP unanswerable\" OR \"why vendors decline to
   bid\" OR \"unanswerable RFP\"" — vendor accounts of un-estimable RFPs.
10. "\"wired RFP\" OR \"vendor-written RFP\" \"column fodder\"
    procurement failure" — analysis of pre-selected incumbent RFPs and
    compliance theater.
11. "\"Standish Group\" CHAOS report IT project failure rate
    requirements waterfall agile" — project resolution statistics by
    methodology and project size.
12. "\"risk premium\" ambiguity IT vendor \"fixed price\" RFP estimation
    scope" — quantification of contingency buffers in fixed-price bids.
13. "\"outcome-based contracting\" challenges OR failure empirical study
    procurement" — academic and empirical meta-analyses on outcome
    contract performance.
14. "\"meta-analysis\" \"performance-based contracting\" OR
    \"outcome-based contracting\" site:academic.oup.com" — empirical
    evaluation of contractibility and principal-agent frictions.
15. "\"Hank Barnes\" Gartner \"buyer regret\" OR \"purchase regret\"" —
    primary analyst research into B2B software purchasing regret.
16. "\"Loopio\" \"RFP Trends\" report win rate bid/no-bid 2023 OR 2024" —
    proposal submission volumes, win rates, and qualification hours.
17. "\"CIPS\" \"outcome based specification\" OR \"performance
    specification\" vs \"input specification\"" — professional
    procurement institute standards on specification risk transfer.
18. "\"A New Approach to Contracts\" \"Oliver Hart\" \"Kate Vitasek\"
    \"Harvard Business Review\"" — relational contracting economic
    theory and value leakage.

Run ended: Both perspectives of the card (IT architect and vendor bid
management) and the disconfirming perspective were substantiated with
primary and authoritative industry sources; queries yielded saturation
of known patterns and failure modes.
