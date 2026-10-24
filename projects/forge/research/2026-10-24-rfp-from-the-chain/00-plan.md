---
date: 2026-10-24
project: forge
topic: an RFP for an IT project derived from the artefacts of the chain
status: immutable
engines: claude (antigravity reviewed the draft plan only; its card runs failed on quota)
derived_from: the principal's word of 2026-10-24 (a research on the RFP: its parts, its template, what of it follows from intent, assignment, BRD and solution design and what a person must add; IT projects of a private group; the document and its boundary to the process); the second engine's review of the draft plan, tmp/research/2026-10-24-rfp-from-the-chain/plan-review/; 00-brief-research.md v0.2 (the first research run the new way); research/2026-10-13-what-a-brd-contains-and-how-it-is-found-today.md (what the project knew of the vendor side)
---

# An RFP for an IT project derived from the artefacts of the chain

<!-- The head of a research bundle: the plan as confirmed, word for
word, and under it the synthesis made when every note has returned
(templates/research-plan.md; .claude/skills/research/SKILL.md). -->

## Summary

The principal's hypothesis holds in a narrow form. Six notes of one
engine agree that most of an IT RFP's substance follows from the
chain, and that what does not follow is a thin set of sourcing
decisions no layer above owns; so the RFP is best made as a render
of the chain plus a thin artefact that holds those decisions, not as
a layer that restates requirements.

What follows from the chain: the intent gives background, problem
and objectives; the assignment gives scope, out of scope,
constraints (which become mandatory items), deliverables (the core
of the statement of work) and success criteria (acceptance and
performance); the BRD gives the functional requirements, the
scenarios behind them, the non-functional requirements and the
dependencies as integration requirements; the solution design gives
only justified constraints (integration, data, identity, security),
and whether more of it enters depends on the archetype (cards 1, 3).

What a person must add, consistently in every source: legal,
commercial, security, risk and vendor-management requirements; the
evaluation process and its weights; the tiering of items into
pass/fail gates and rated items; the standard contract; the
submission instructions; budget, timeline, confidentiality; the
regulatory and contractual gates (data protection, sector rules such
as DORA, IP, liability, security attestations) as disqualifying
conditions (cards 3, 4).

What decides who wins and has no upstream owner: the tier of each
item, the weights, the scale and its anchors, the hurdle thresholds,
the award formula (which the one peer-reviewed study says can change
the winner by itself), the response-code set and the evidence each
code demands, the pricing model per scope item, and the archetype
decision whether the buyer's design is asked for or left to the
bidder (card 4). These are decisions with reasons that deserve a
history and a reviewer, which the forge gives to artefacts, not to
recipes; the rows of the compliance matrix and of the pricing
schedule, by contrast, are a mechanical projection of the BRD and
the deliverables.

What a derived RFP must avoid: writing the solution as requirements,
a checklist of business rules, the solution design's choices as
"shall" items; the counter-movement asks for the problem, the fixed
limits, scenarios and disclosed weighting inside the RFP, and the
classic form persists while its content moves to outcomes (card 2).
The RFP wants a different requirement style from the chain's: every
"shall" is read as a disqualifier, use cases score badly, the
recommended form is a capability statement; the requirement part
becomes contract text. The derivation is therefore a transformation
with rules of its own, not a copy (cards 1, 3).

The skeleton to produce is the procurement institute's four parts
and appendices (instructions and conditions with the evaluation; the
requirement; the information the proposer supplies; the proposed
contract; schedules), issued as a package with a core document, not
one monolithic file; the vocabulary is RFI before, RFP where the need
is not fully defined, RFT/ITT where it is, RFQ where price decides
(card 1). The RFP ends at the proposal due date: before it the
document changes by amendment, vendor questions are answered to all;
after it nothing is written into it, and the exchanges that follow
are the procurement officer's; what returns upstream is a changed
requirement, through the intent first (card 5). The market's
"AI RFP generation" has the shape of a render, template plus sources
plus instruction, and leaves evaluation criteria to people in every
tool opened (card 6).

Where the engines differ: nothing can be said. The second engine's
quota was exhausted after its review of the draft plan and before
any card ran; this bundle is one engine's work, its agreement across
six cards is consistency under one set of priors, not validation,
and the principal closed it single-engine on 2026-10-24.

Unexpected, worth the principal's eye: the requirement part of an
RFP is contract text; the award formula gets the least attention and
decides the most; the classic RFP may already be the minority route
for technology purchases; the CIPS cycle does not contain the word
RFP; vendors name prior engagement during requirements definition as
the strongest predictor of winning, which is what a chain composed
before vendor contact prevents.

## Plan (confirmed 2026-10-24)

### Purpose

Whether and how the forge derives a Request for Proposal (RFP) for an
IT project from the artefacts of its chain - the intent (positions and
objectives), the assignment (scope, out of scope, constraints,
deliverables, success criteria), the BRD (business rules, use cases,
dependencies, non-functional requirements) and the solution design
(what is built or done and the choices it rests on) - all of them or a
subset: what an RFP of a private company group is made of, what its
template looks like, what of it follows from the chain and what a
person must add, and where the forge stops. The principal's
hypothesis: a further artefact of the chain (POS.0700, POS.1430); the
research is to say whether that holds or whether the RFP is a render.
Known: nothing on RFPs in `research/`; the BRD research of 2026-10-13
touches the vendor side only marginally; agentic-platform has a
terminated RFP in its history and two requirement catalogues derived
from it in its `sources/`. The principal's answers before the plan:
the hypothesis is an artefact, to be examined; a private group, public
procurement law left out; the document and one card on the boundary
to the process, not the process itself.

### Perspectives

- The buyer's procurement officer: cards 1, 5, 6.
- The requirements engineer who must keep the RFP traceable to what
  was specified: cards 3, 4.
- The IT or solution architect who specifies the solution: cards 1, 2.
- The vendor who must answer the RFP (bid/no-bid, the risk premium of
  ambiguity, what structure lets it estimate): cards 2, 4.
- The evaluator who scores the proposals: cards 3, 4, 5, 6.
- Security and compliance (CISO, DPO: attestations and gates that
  disqualify before scoring): card 3, as what a person supplies.
- The lawyer and the commercial owner: no card; named in card 3 as
  what a person supplies.

### Assumptions

The operational answer lives in IT advisory and procurement practice
(analyst toolkits, procurement institutes, consultancies and
integrators); the requirements-engineering standards (ISO/IEC/IEEE
29148, BABOK, IREB) give the frame and the vocabulary of acquisition
but are abstract on the RFP itself. There is no single IT RFP
skeleton: SaaS/COTS selection, custom development and systems
integration differ, and every card reads for the archetype.
"Derivable" can be judged section by section against the four
artefacts. Regulatory and contractual gates (data protection, sector
resilience rules, IP, liability, security attestations) are part of a
private company's RFP as disqualifying conditions, supplied by
people, not boilerplate. Premortems: the planner's own, that good
practice is moving away from the classic monolithic RFP towards
outcome-based briefs, staged dialogues and agile procurement, so that
an "RFP artefact" would codify a form the field is leaving; the
second engine's, that the RFP's relation to the chain is branching,
not linear: for a COTS/SaaS purchase the solution design in the RFP
poisons the competition and is the winner's to produce, for a custom
build it belongs in and the RFP becomes an execution tender; cards 2
and 3 are to answer both.

### Left out

Public procurement law (EU directives, national acts) as a
structure; the vendor's side (proposal writing, response tools);
contract negotiation and the contract itself; RFQ for commodities;
the evaluation and selection process beyond what card 5 draws as the
boundary. Not left out: the regulatory and contractual gates named
above, as what a person supplies (card 3).

### Cards

#### Card 1: canon, vocabulary and anatomy of the IT RFP of a private company
- **Question:** Who is authoritative on IT procurement documents in private companies (procurement institutes, analyst firms, consultancies and integrators, requirements-engineering standards), what the vocabulary is (RFI, RFP, RFQ, SOW, compliance matrix, evaluation matrix, BAFO, and their relations), which sections an IT RFP has and in what order (background and objectives, scope and statement of work, functional and non-functional requirements, deliverables, timeline, evaluation criteria and weights, submission rules, commercial and legal terms, vendor qualification, response instruments), and what a reference template looks like, distinguishing the archetypes SaaS/COTS selection, custom development and systems integration; against the alternative that IT procurement has fractured into category-specific packages with no shared vocabulary and that the monolithic document has been replaced by modular packages (commercial terms, security schedule, technical requirements, response workbook).
- **Why it matters:** The skeleton any artefact or render of the framework must produce, and the words the other cards must use; a card written in the wrong vocabulary finds the wrong literature.
- **What would answer it:** The field's own guidance, glossaries and templates: procurement institutes' publications, analyst toolkits for the IT category, consultancies' and integrators' published guidance; software vendors' template libraries only as vendor claims.
- **Where to look:** procurement institutes (CIPS, ISM), analyst firms' IT procurement toolkits (Gartner, Forrester, Info-Tech Research Group), consultancies' and system integrators' guidance, well-regarded practitioner books, ISO/IEC/IEEE 29148 and BABOK only for the vocabulary of acquisition; more than one route. Known items that must turn up: an IT procurement category toolkit of a procurement institute or an analyst firm; a template with evaluation criteria and weights; a vendor response matrix or functional compliance schedule.
- **Disconfirming query:** Expected: a recognisable canon and a settled skeleton per archetype. Search for the opposite: that practitioners say there is no shared vocabulary or skeleton for IT, that templates are generic and the IT-specific content is left to the writer, and that modern IT procurement issues modular packages instead of one document.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (procurement officer, architect) has a primary source; or about fifteen openings spent.

#### Card 2: where the specification-driven RFP fails and where the outcome-based one wins
- **Question:** The documented failure modes of IT RFPs (the solution over-specified instead of the outcome, requirement inflation, vague or hidden evaluation criteria, vendor-written RFPs, boilerplate) and the counter-movement (outcome-based RFPs, staged RFI then RFP, agile and iterative procurement, vendor dialogue), distinguished by archetype (SaaS/COTS selection, custom development, systems integration), and seen also from the vendor's side (bid/no-bid decisions, how ambiguity raises the risk premium, what structure lets a vendor estimate honestly); against the alternative that the classic requirements-driven RFP works, that outcome-based and agile procurement are marginal in private enterprise, and that detailed requirements remain the norm.
- **Why it matters:** Decides what a derived RFP must avoid, and whether the form itself is changing under the framework's feet (the planner's premortem).
- **What would answer it:** Surveys and benchmarks of IT procurement and project failure, practitioner and advisory literature on outcome-based and agile procurement, vendor-side accounts of unanswerable RFPs; public-sector studies only as a reference for failure modes.
- **Where to look:** industry surveys and benchmarks (Standish Group, Gartner, Bain or similar sourcing studies), procurement institutes' and advisory firms' guidance on outcome-based procurement, vendor-side bid management literature; more than one route. Known items: one survey or benchmark of IT procurement or RFP failure and cancellation rates; one source on outcome-based procurement; one vendor-side text on what makes an RFP unanswerable.
- **Disconfirming query:** Expected: the classic RFP has known failure modes and the field is moving towards outcome-based forms. Search for the opposite: evidence that outcome-based or agile procurement failed or remained marginal in private enterprise, and that detailed requirements remain the norm.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (architect, vendor) has a primary source; or about fifteen openings spent.

#### Card 3: what of an RFP follows from the chain and what a person must add, by archetype
- **Question:** Section by section, what an intent (background, objectives, positions), an assignment (scope, out of scope, constraints, deliverables, success criteria), a BRD (business requirements, use cases, non-functional requirements, dependencies) and a solution design (target architecture, integration constraints) can supply to an RFP, and what is always supplied by people: budget, timeline, commercial terms, evaluation weights, legal terms, vendor qualification, confidentiality, and the regulatory and contractual gates (data protection, sector resilience rules, IP, liability, security attestations); and, by archetype, whether a solution design belongs in the RFP at all: for a SaaS/COTS selection, does embedding the buyer's design over-constrain the market so that the design is the winner's to produce, and for a custom build does the RFP with a design become an execution tender; against the alternative that enterprise IT RFPs reject pre-specified solution designs because they prevent vendors from proposing their own architectures.
- **Why it matters:** The principal's central question, and the one that decides whether the RFP is an artefact with thinking of its own or a generated document from the artefacts above it; the second engine's premortem (the relation is branching, not linear, and depends on make-or-buy) is answered here.
- **What would answer it:** Requirements-to-RFP guidance of IT advisory firms and procurement practice (traceability matrices, section-by-section guidance on what the buyer specifies and what it leaves to bidders); the standards (ISO/IEC/IEEE 29148 on the acquisition process and the acquirer's request, BABOK's vendor assessment) only as the frame.
- **Where to look:** IT advisory firms' requirements-to-RFP and vendor selection guidance (Info-Tech Research Group, Gartner, Forrester), procurement institutes, practitioner guidance on specifying for COTS against custom, requirements-engineering bodies for the frame; more than one route. Known items: a practitioner requirements-to-RFP traceability matrix from an advisory firm; what 29148 says the acquirer's request contains; guidance on how much solution to specify in a COTS/SaaS RFP.
- **Disconfirming query:** Expected: the requirements part of an RFP is derivable and substantial, and the solution design's place depends on the archetype. Search for the opposite: evidence that enterprise IT RFPs reject pre-specified solution designs outright because they prevent vendors from proposing COTS architectures, and that the derivable part is small.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (requirements engineer, evaluator, security and compliance as what a person supplies) has a primary source; or about fifteen openings spent.

#### Card 4: how a requirement becomes a response instrument
- **Question:** How a declarative requirement (a business rule, a use case, a non-functional requirement) is turned into the instruments a bidder answers and an evaluator scores: a compliance matrix with response codes (out-of-the-box, configurable, custom, third-party, roadmap), weighted scoring with hurdle criteria and thresholds, price and quality normalisation, and a pricing schedule tied to scope items (fixed price per milestone, time and materials rate card, subscription tiers); and which of these follow mechanically from the requirements and which need a person's judgement; against the alternative that compliance matrices lead to box-ticking without substance and that free-form responses evaluated by experts serve better.
- **Why it matters:** Decides whether an RFP artefact of the framework has items and decisions of its own (response codes, weights, hurdles, the pricing shape) beyond what the artefacts above it carry, and what of that can be derived automatically.
- **What would answer it:** Bid evaluation methodologies and templates of procurement institutes and advisory firms, published compliance matrices and scoring rubrics, guidance on pricing schedule design.
- **Where to look:** procurement institutes' evaluation guidance, advisory firms' vendor evaluation toolkits, published RFP response templates and compliance matrices, practitioner guidance on weighted scoring and price normalisation; more than one route. Known items: one described system of compliance response codes; one method of price and quality normalisation; one pricing schedule template tied to scope.
- **Disconfirming query:** Expected: compliance matrices and weighted scoring are the norm and largely derivable from the requirements. Search for the opposite: critiques that matrices produce box-ticking without substance and that expert evaluation of free-form proposals outperforms them.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (evaluator, vendor, requirements engineer) has a primary source; or about fifteen openings spent.

#### Card 5: where the document ends and the process begins
- **Question:** What of the RFP process (vendor questions and answers, amendments, security and compliance questionnaires, evaluation, shortlist, best-and-final offers, contract) belongs in the RFP document and its annexes, what returns upstream into the requirements (vendor answers as sources, changes of what is wanted), and where a framework for specifying should stop; against the alternative that the document cannot be separated from the process.
- **Why it matters:** The boundary the principal asked for: the framework specifies and does not run procurement; what comes back from vendors must have a place in the chain.
- **What would answer it:** Procurement process models (the sourcing cycle of the procurement institutes) and practitioner guidance on the RFP lifecycle.
- **Where to look:** procurement institutes' process models, sourcing-software vendors' process descriptions (vendor claims), practitioner guidance on vendor Q&A, amendments and clarifications; more than one route. Known items: a sourcing cycle with the RFP placed in it; guidance on handling vendor questions and amendments.
- **Disconfirming query:** Expected: a clean boundary between the document and the process. Search for the opposite: that the RFP is a living document amended through the process and cannot be frozen.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (procurement officer, evaluator) has a primary source; or about fifteen openings spent.

#### Card 6: how buyer-side tools generate an RFP from requirements today, and what they leave to people
- **Question:** What buyer-side sourcing platforms and AI RFP generators (the buyer's side only: tools that write and issue an RFP, never tools that answer one) take as input, what they produce automatically, what they ask the user to supply, and what independent reviews say of the result; against the alternative that no tool derives an RFP from requirements documents and all start from a questionnaire.
- **Why it matters:** The market's answer to "what can be derived automatically"; a derivation the market already sells need not be invented, and one it cannot sell is a warning.
- **What would answer it:** The vendors' own documentation of inputs and outputs (vendor claims) and independent reviews of the results.
- **Where to look:** buyer-side sourcing platforms' documentation (strategic sourcing modules of the large procurement suites, RFP-issuing tools), AI RFP generators aimed at buyers, analyst and user reviews; more than one route. Known items: at least two named buyer-side tools with their inputs and outputs described; one independent review of an AI-generated RFP.
- **Disconfirming query:** Expected: tools derive sections from requirements. Search for the opposite: reviews saying the tools produce boilerplate and the substance is still typed in.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (procurement officer, evaluator) has a primary source; or about fifteen openings spent.

### Agents

Six cards, two engines (the session model and the Antigravity CLI),
twelve agents, one per card per engine, run in parallel and never
speaking to each other; no second round unless the notes name gaps,
and then on the principal's word. Card 1 runs with the others, not
before: the topic's vocabulary is common enough to write the cards
now; a canon card 1 finds that the others missed is a named gap for a
second round.

### The second engine's review of the draft

The Antigravity CLI read the draft of six cards
(`tmp/research/2026-10-24-rfp-from-the-chain/plan-review/`, 90 s,
30,564 tokens) and said: three questions missing (the transformation
of a requirement into a compliance matrix and scoring instrument; the
divergence of archetypes SaaS/COTS, custom build, systems integration;
the derivation of a pricing schedule); three assumptions not to be
taken for granted (that the standards hold the operational answer;
that one skeleton serves all IT RFPs; that law plays no part for a
private company, since regulatory gates disqualify); two perspectives
missing (the vendor as the consumer of the RFP; security and
compliance), the evaluator misplaced; merge the canon card and the
anatomy card, split the derivation card into text and response
instrument, narrow the failure card to the boundary between
specification-driven and outcome-based by archetype; sharper
disconfirming queries and known items per card (surveys instead of
NDA-shielded post-mortems, an advisory firm's traceability matrix
instead of the standards, buyer-side tools named as such); and a
premortem of its own, the branching relation of the RFP to the chain
by make-or-buy. Taken by the principal in the walkthrough of
2026-10-24, item by item: all of it, with two bounds: the failure card
keeps its failure modes beside the boundary (item 3), and the two
premortems stand side by side, each marked (item 7). Nothing of the
review entered the plan by Claude's own judgement.

## Deviations from the plan

- The plan said twelve agents on two engines. Six ran: the session
  model's, one per card. The second engine (Antigravity CLI) reviewed
  the draft plan (90 s) and then returned RESOURCE_EXHAUSTED on all
  six card packets launched in parallel on its default model; a rerun
  of five of them on `gemini-3.8-flash-high` returned "Individual
  quota reached, resets in 124h"; the sixth (card 2), believed to be
  running, had died of the same error. No second-engine note exists
  in this bundle; the Claude notes carry no comparison.
- The six card packets were launched at once; the plan did not say
  how many runs the engine's quota bears, and the day's earlier runs
  (a ping, a trial card, the plan review) had already used part of
  it. A rule for the brief: one engine's quota is a budget of the
  research day, unknowable before a run, to be spent one or two runs
  at a time, and the adapter is to say the reset time plainly.
- A false refusal of card 2's run: the citation reports of the Claude
  notes were written into the packet folders while the other engine
  was still running, and `forge-engine` refused the changed tree.
  The skill now puts the reports under `tmp/research/<run>/cite/`.
- The principal closed the research on 2026-10-24 with the six notes
  of one engine, the second engine's run owed; this bundle is
  immutable from that closing, so a later run on another engine is a
  new research citing this one, not an addition to it.
- Card 3's and card 1's agents found no primary source for the
  custom-build archetype and none for ISO/IEC/IEEE 29148's
  acquisition text; the plan's assumption that the standards give the
  frame is unmet, and the archetype split stands at two (product
  selection; services and implementation partner), not three.

## Synthesis (2026-10-24)

### Completeness, card by card

- Card 1 (canon and anatomy): answered. Stop rule met in both parts
  (nothing new from the last two queries; the procurement officer and
  the architect each with primary sources), 13 openings. The
  disconfirming query found nobody denying a shared vocabulary or
  skeleton and found the "modular package" to be the canon's own
  shape; "kill the RFP" exists only in vendor blogs and a paywalled
  abstract.
- Card 2 (where the RFP fails): answered. Ended on the opening budget
  (17 attempts); the architect and the vendor each with primaries.
  The disconfirming query found no openable evidence that
  outcome-based or agile procurement failed in private enterprise,
  and consistent indirect evidence that detailed-requirements RFPs
  remain the norm (the same complaint in 2009 and 2026, rising RFP
  volume, selection guidance still built on weighted requirements).
- Card 3 (what follows from the chain): answered for the SaaS/COTS
  branch, not for the custom build. Ended on the opening budget (17
  attempts, 9 lost to unreachable pages); the second part of the stop
  rule unmet: no primary on the custom-build archetype or on 29148's
  acquisition clauses, the evaluator and compliance perspectives on
  public-body guidance and a regulation copy, not on a private
  group's practice. The disconfirming query found no evidence that
  enterprise RFPs reject pre-specified designs outright, only the
  softer rule: justify every technical requirement, keep mandatory
  ones few.
- Card 4 (requirement to response instrument): answered. Ended on the
  opening budget (14); each perspective with a primary (evaluator,
  vendor, requirements engineer). The disconfirming query found the
  box-ticking critique as practitioner claim, aimed at yes/no items
  not at the matrix, and no source that expert free-form evaluation
  outperforms a matrix; the one controlled study found weakens expert
  ratings too.
- Card 5 (document and process): answered. Ended on the opening
  budget (14); the procurement officer and the evaluator with
  primaries; the first part of the stop rule met weakly (no
  private-group primary ever reached). The disconfirming query found
  the "living RFP" position as a methodological argument, not as
  practice, and even there a document is issued and final offers made
  against it.
- Card 6 (buyer-side tools): answered. Ended over the opening budget
  (19 fetches, 9 failed); the procurement officer with primaries, the
  evaluator only through the same pages and one 2023 test. The
  disconfirming query found no independent review in either
  direction: the field is vendor claims and one dated practitioner
  test.

### Answers side by side

One engine only (Deviations). Per card the answer of the session
model, as its note's In short has it:

- Card 1: there is a canon (CIPS template with guidance notes of
  January 2025; Info-Tech's RFP family; Forrester's paywalled
  template); a settled four-part skeleton with appendices, the same
  in every route opened; the IT content lives in the requirement
  part, generic at the institute, filled per category by the
  analysts; two archetypes supported, custom development not found.
- Card 2: the dominant failure is the solution written as
  requirements; the remedy converges on the problem, the limits and
  scenarios; the vendor prices, games or declines an unclear RFP; the
  form persists, the content moves to outcomes.
- Card 3: the requirements core follows from the chain and is the
  bulk of the work; legal, commercial, security, risk, evaluation,
  contract and gates are people's; tiering is a decision with no
  upstream owner; for SaaS/COTS the design is the winner's, with
  justified constraints surviving; the custom build unsourced.
- Card 4: the rows of the instruments follow mechanically from the
  requirements; everything that gives them effect (codes, gates,
  weights, scale, formula, pricing model) is a buyer decision, and
  the formula alone can change the winner.
- Card 5: the seam is the proposal due date; amendments before it,
  equal-treatment exchanges after it; the document carries the rules
  of its process; what returns upstream is a changed requirement.
- Card 6: no buyer-side tool opened derives an RFP from a structured
  requirements set; inputs are a template, a request, a prompt, a
  form or a conversation; criteria are human input everywhere; the
  market's generation has the shape of a render.

Agreement across the six notes (the render shape of the market, the
thin set of sourcing decisions, the SaaS/COTS branch, the style
transformation) is consistency under one engine's priors, not
validation; a second family has not read these cards.

### Unexpected, gathered

Finds that reconfigure a question or bring a mechanism from
elsewhere, shown before any judgement:

- The requirement part of an RFP is contract text (CIPS Part 2 and
  3): whatever the chain supplies becomes an obligation, which asks a
  different standard of wording than an intent or a BRD (card 1).
- The RFP wants a different requirement style: "shall" is read as
  mandatory, use cases are hard to answer and to score, the
  recommended form is a capability statement; the derivation is a
  transformation, not a copy (card 3).
- The award formula, not the criteria, is where buyers pay least
  attention and where the outcome is most sensitive; monetising
  quality dissolves the weight question into a price question
  (card 4).
- The market's "AI RFP generation" has the shape of the forge's
  render: template, sources, instruction, regenerate (card 6).
- The CIPS cycle names RFI, ITT and RFQ and never RFP; an artefact
  called "RFP" names one member of a family (card 5).
- Prior engagement with the buyer during requirements definition is
  the vendor's strongest predictor of winning; a chain composed before
  vendor contact is what vendors try to get into (card 2).
- The classic RFP may be the minority route for technology purchases
  (a Gartner survey reported by trade press: agile or lean methods
  and panels more frequent in Australia); the chain's derivable
  content is needed under any route (card 3).
- Two items of the DORA gate (the description of functions and
  services, the service levels) are derivable from the assignment
  and the BRD; the gate is not wholly outside the chain (card 3).
- The institute's pricing clause asks the proposer for its
  dependencies and assumptions: the chain's ASM and DEP items have a
  mirror on the supplier's side of the same document (card 1).
- Product-security questions (SBOM, disclosure policy, MFA, SSO,
  logs) are project-independent and belong with reusable material,
  not a project's chain (card 3, the agent's inference).
- Info-Tech issues a Scenario Template beside the RFP: the chain's
  use cases may have a destination other than the requirement tables
  (card 1, not opened).

Finds that add a source to a point already made (noise by the test
of the research of 2026-10-24): the agile route moving the design
into the dialogue (card 5, the same as card 2's F7 and card 3's F4);
the three-way choice amend, cancel, other (card 5, a detail of F2).

### Not found, gathered

- The acquisition text of ISO/IEC/IEEE 29148 and BABOK's Vendor
  Assessment technique: paywalled; nothing cited (cards 1, 3, 5).
- A primary treating custom development as an RFP archetype of its
  own, or saying where the solution design belongs in a custom-build
  RFP (cards 1, 2, 3).
- Any private-company or private-group procurement guide on Q&A,
  amendments, clarification, final offers, evaluation methodology or
  response templates: everything reachable was public-sector,
  supplier-side or advisory (cards 3, 4, 5).
- A requirements-to-RFP traceability matrix from an advisory firm;
  Gartner's toolkits and surveys (every page 403); Forrester's
  template body (cards 1, 3).
- A benchmark of IT procurement or RFP failure and cancellation
  rates (McKinsey/Oxford timed out, Standish not opened); a
  quantification of the risk premium ambiguity adds to a bid
  (card 2).
- An independent review (2024 to 2026) of an RFP generated by a
  buyer-side platform's AI; Coupa's sourcing-event agent; the Gartner
  Market Guide's own text (card 6).
- A buyer-side primary using the terms "compliance matrix" or "BAFO"
  (CIPS writes "BFO"); ISM's glossary; IT-specific evaluation weights
  (card 1).
- A study comparing matrix-based with free-form expert evaluation;
  a private-sector figure for how often the formula changes the
  winner (card 4).

### Claude's view

My own, marked as such; verified where it rests on the notes'
sources, a hypothesis where it goes beyond them.

Verified on the notes: the RFP is two things in one package. The
document is generated: its requirement part is a transformation of
the chain (intent, assignment, BRD; the solution design only as
justified constraints for a purchase, more for a build), its other
parts are people's text (instructions, evaluation process, terms,
contract, gates), and its shape is the institute's four parts and
schedules. The decisions that make it an instrument (archetype, the
tier of every item, the weights, the hurdles, the award formula, the
response codes and their evidence, the pricing model per scope item,
the gates and who supplies them) are nobody's upstream and change
who wins.

Hypothesis, mine: the forge should give those decisions a home of
their own, a thin artefact of sourcing decisions with items, a
history and a reviewer, placed beside or below the solution design,
and make the RFP itself a render of the chain, that artefact and a
person-supplied file of terms, in the CIPS skeleton, with a recipe
that translates the chain's style (shall and use cases into
capabilities and scenarios) and names the archetype. The artefact
would also be the versioned home of the amendment and Q&A record up
to the proposal due date, which card 5 says a render cannot give;
after the due date the forge stops. Vendor questions and proposals
come in as sources; a changed requirement goes to the intent first.
This is the agent's option 3 of card 3 and option 2 of card 4, which
I take over, and it is what the market's render-shaped tools cannot
do (card 6), which I read as the opening rather than the warning.

Two cautions. Nothing above has been read by a second family; the
six notes share one engine's priors and all six found the same
shape, which is exactly the consistency POS.0790 warns about. And
the custom-build branch is unsourced across three cards: if the
group's first RFP is a build, the hypothesis above is untested where
it matters most.

What I propose for the chain, through `/forge intent` and never
here: a position that an RFP is a render over a thin artefact of
sourcing decisions, the artefact born through `/new-artefact` on a
real purchase (POS.1430, POS.1380); the brief `next-gen` or a brief
of its own to carry the material until then; and a quick research
card on the custom-build archetype before the first build is sourced.

## Notes

- `card-1-canon-and-anatomy.claude.md`, from
  `tmp/research/2026-10-24-rfp-from-the-chain/card-1-canon-and-anatomy/`
- `card-2-where-the-rfp-fails.claude.md`, from `…/card-2-where-the-rfp-fails/`
- `card-3-what-follows-from-the-chain.claude.md`, from
  `…/card-3-what-follows-from-the-chain/`
- `card-4-requirement-to-response-instrument.claude.md`, from
  `…/card-4-requirement-to-response-instrument/`
- `card-5-document-and-process.claude.md`, from `…/card-5-document-and-process/`
- `card-6-buyer-side-tools.claude.md`, from `…/card-6-buyer-side-tools/`
- No `<card>.antigravity.md`: the second engine's quota was exhausted
  before any card ran (Deviations). Its review of the draft plan is
  in `…/plan-review/antigravity.md`, under `tmp/`, not a note of the
  bundle. The citation reports of the six notes are in `…/cite/`.
