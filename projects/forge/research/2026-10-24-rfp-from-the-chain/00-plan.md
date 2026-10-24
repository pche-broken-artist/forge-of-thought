---
date: 2026-10-24
project: forge
topic: an RFP for an IT project derived from the artefacts of the chain
status: immutable
engines: claude, antigravity
derived_from: the principal's word of 2026-10-24 (a research on the RFP: its parts, its template, what of it follows from intent, assignment, BRD and solution design and what a person must add; IT projects of a private group; the document and its boundary to the process); the second engine's review of the draft plan, tmp/research/2026-10-24-rfp-from-the-chain/plan-review/; 00-brief-research.md v0.2 (the first research run the new way); research/2026-10-13-what-a-brd-contains-and-how-it-is-found-today.md (what the project knew of the vendor side)
---

# An RFP for an IT project derived from the artefacts of the chain

<!-- The head of a research bundle: the plan as confirmed, word for
word, and under it the synthesis made when every note has returned
(templates/research-plan.md; .claude/skills/research/SKILL.md). -->

## Summary

Two model families, twelve notes, one shape. The principal's
hypothesis holds in a narrow form: most of an IT RFP's substance
follows from the chain, what does not follow is a thin set of
sourcing decisions no layer above owns, and both engines, reading
different sources, arrive at the same picture: the RFP is a render
of the chain over an explicit layer of human decisions, branched by
the archetype of the purchase, never a layer that restates
requirements.

What follows from the chain, by both engines: the intent gives
background, problem and objectives; the assignment gives scope, out
of scope, constraints (which become mandatory items), deliverables
(the core of the statement of work) and success criteria; the BRD
gives the functional requirements, the scenarios behind them, the
non-functional requirements and the dependencies as integration
requirements; the solution design gives integration boundaries and
technical guardrails, and whether more of it enters depends on the
archetype (cards 1, 3).

What a person must add, the same list in both engines: legal,
commercial, security, risk and vendor-management requirements; the
evaluation process and its weights; the tiering of items into
pass/fail gates and rated items; the standard contract; the
submission rules and the timetable; budget, pricing structure,
confidentiality; the regulatory gates (data protection, DORA and
NIS2 resilience clauses, security attestations) as disqualifying
conditions, which the second engine shows have moved from the
contract stage into the RFP as pre-scoring gates (cards 3, 4).

What decides who wins and has no upstream owner, both engines
agreeing on the division and citing the same economists: the tier of
each item, the weights, the scale, the hurdle thresholds, the award
formula (relative price scoring suffers rank reversal and can change
the winner by itself), the response-code set and the evidence each
code demands, the pricing model per scope item, and whether the
buyer's design is asked for or left to the bidder (card 4). The rows
of the compliance matrix and of the pricing schedule are a
mechanical projection of the BRD and the deliverables; everything
that gives them effect is a buyer decision with reasons, which the
forge gives a history and a reviewer to only in an artefact.

What a derived RFP must avoid: the solution written as requirements,
a checklist of business rules, the solution design's choices as
"shall" items; the counter-movement asks for the problem, the fixed
limits, scenarios and disclosed weighting inside the RFP, and the
classic form persists while its content moves to outcomes (card 2,
both engines). The RFP wants a different requirement style from the
chain's: every "shall" is read as a disqualifier, use cases score
badly, the recommended form is a capability statement, and the
requirement part becomes contract text; the second engine gives the
frame: an RFP is a Lastenheft, the problem space, and a buyer's
design in it is a Pflichtenheft injected where the vendor's belongs
(cards 1, 3).

The skeleton to produce is the procurement institute's four parts
and appendices, issued as a package with a core document (both
engines; the second calls the monolithic narrative RFP obsolete, the
first finds the package to be the canon's own shape); the vocabulary
is RFI before, RFP where the need is not fully defined, RFT/ITT where
it is, RFQ where price decides (card 1). The RFP ends at the proposal
due date: before it the document changes by amendment, vendor
questions are answered to all; after it nothing is written into it,
and what returns upstream is a changed requirement, through the
intent first; the contract incorporates the RFP, its addenda and the
proposal in an order of precedence (card 5, both). The market's "AI
RFP generation" has the shape of a render, template plus sources plus
prompt, leaves criteria and gates to people in every tool either
engine opened, and the second engine adds the loop it is causing:
AI-inflated RFPs answered by AI-inflated proposals, driving buyers to
three-to-five-page outcome briefs with live demonstrations (card 6).

Where the engines differ, the valuable part: the second engine
sources three archetypes with distinct anatomies, the custom build
included (a design in the RFP turns it into an execution tender), and
quantifies what the first could not: the vendor's risk premium for
ambiguity at 15 to 40 per cent and more as a practitioner rule of
thumb, the share of solicitations vendors decline at 37 to 40 per
cent, and the regret of software buyers after a purchase at 56 to 60
per cent (Gartner); the first found the custom build unsourced and no
figures. The second demotes the compliance
matrix to a hygiene filter, since SaaS vendors claim 90 per cent
compliance and AI answers the rest, and elevates scripted
demonstrations and proofs of concept; the first keeps the matrix with
graded codes and per-code evidence. The second finds the document not
cleanly frozen in complex IT procurement: competitive dialogue
iterates specifications with shortlisted vendors until a freeze at
the final offer; the first finds the seam at the due date with
amendments before it. The second is consistently more assertive and
found more; the first marks more as not found. Agreement is
consistency of two families on the same web, not validation.

Unexpected, worth the principal's eye: the requirement part of an RFP
is contract text; the award formula gets the least attention and
decides the most; regulatory gates now disqualify before scoring;
the classic RFP may already be the minority route for technology
purchases; the CIPS cycle does not contain the word RFP; vendors name
prior engagement during requirements definition as the strongest
predictor of winning, which is what a chain composed before vendor
contact prevents and may cost; many "objective" RFPs are wired, their
specifications borrowed from an incumbent's collateral and the other
bidders invited as column fodder for a three-bid rule; buyer regret
peaks before implementation, from the procurement itself; and the
e-sourcing platforms treat an RFP as a relational schema of lines, so
a monolithic text forces re-keying.

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

- Twelve agents ran as planned, but not in one wave. The six session
  agents returned within twenty minutes. The second engine
  (Antigravity CLI) reviewed the draft plan (90 s) and then returned
  RESOURCE_EXHAUSTED on all six card packets launched in parallel on
  its default model, and "Individual quota reached, resets in 124h"
  on a rerun of five on `gemini-3.8-flash-high`: the login was not
  the enterprise licence. The research was closed single-engine on
  2026-10-24 at 17:05 on the principal's word, committed in that
  state, and reopened the same day when the login was corrected.
- A rule for the brief: one engine's quota is a budget of the
  research day, unknowable before a run, to be spent one or two runs
  at a time, never six at once; the adapter is to say the reset time
  plainly (it does).
- Contamination, found and cured. The six packets rerun after the
  reopening were launched from folders under the forge's `tmp/`, a
  tree the engine's own settings trust whole (`trustedWorkspaces`);
  with its tools allowed, the engine walked up to the bundle the
  packet cites and read the first engine's notes lying beside it.
  Measured: card 4's note 71 per cent identical sentences and 14 of
  14 URLs shared with the first engine's; cards 3, 5 and 6 rewritten
  with 13 of 18, 14 of 14 and 14 of 15 shared URLs; cards 1 and 2
  independent (0 of 11, 1 of 15). The four were set aside in `tmp/`
  as evidence, `forge-engine` was changed to copy every packet to an
  isolated folder outside every repository and the trusted tree and
  to run the engine there, and cards 3 to 6 were run again: shared
  URLs 0 of 30, 0 of 16, 0 of 21, 0 of 12. The engine's sandbox
  restrains its terminal, not its reading.
- The measure of independence, once made a script
  (`forge-cite --independence`), found a fifth rewritten note: card 2's,
  made in the same wave, 11 of 15 URLs shared with the first engine's
  (among them a `?p=` address no two agents find alone); the hand
  measure had undercounted it by cutting URLs at a parenthesis. The
  isolated copy outside the repository was no lock either: a probe
  showed an engine with its tools allowed reading any path on the
  disk, trusted folder or not, and the engine reads permission rules
  from the user's global settings alone, which the forge must not
  write. The lock built that evening: `forge-engine` gives the engine a
  profile of its own for the run (`tmp/research/<run>/.home/`), a copy
  of the user's settings with deny rules for every entry of the engine
  root but `tmp/`, for the folder where the first engine's notes wait,
  and for the shell, and starts the engine with HOME and USERPROFILE
  on it; a probe confirmed the deny rules hold under `--allow-all`
  ("Matches user-configured deny rule"), the shell is refused, the
  engine's own web tools work and the login is found; the user's
  global settings untouched. Card 2 was run again under that profile,
  from a packet that no longer names the bundle's path: shared URLs 0
  of 13, independent. The first engine's notes are filed only after
  the second engine's return from now on (the skill, step 5).
- Fabricated citations, returned once. The citation check found 2
  dead URLs in the second engine's card 3, 4 in card 6 and 11 of 15
  in card 4 (domains of the shape `technologymatch.com/rfp-compliance-
  matrix-response-codes`, never existing). The three notes went back
  to their agent with the report, as the skill has it; the returned
  notes resolve 15 of 15, 12 of 12 and 12 of 16 URLs, card 4's one
  dead URL standing under Opened and not used, cited for nothing. The
  first engine's six notes had no dead cited URL; their dead links
  are pages the agents themselves listed as not opened.
- A false refusal of card 2's first run: the citation reports of the
  first engine's notes were written into the packet folders while
  the second engine ran; the skill now puts the reports under
  `tmp/research/<run>/cite/`.
- Card 1's and card 3's first-engine agents found no primary source
  for the custom-build archetype and none for ISO/IEC/IEEE 29148's
  acquisition text; the second engine's agents did source the custom
  build (card 2 F8, card 3 F5) and cite 29148 and IREB for the frame
  (card 3, card 4), so the plan's assumption that the standards give
  the frame is met by one engine only.

## Synthesis (2026-10-24)

### Completeness, card by card

- Card 1 (canon and anatomy): answered by both engines. First: stop
  rule met in both parts, 13 openings; disconfirming query found
  nobody denying a shared vocabulary or skeleton and the modular
  package to be the canon's own shape. Second: both parts of the stop
  rule met within the budget; disconfirming query found the
  monolithic narrative RFP obsolete and the modular package the norm.
- Card 2 (where the RFP fails): answered by both. First: opening
  budget (17 attempts), architect and vendor with primaries; no
  openable evidence that outcome-based or agile procurement failed in
  private enterprise, consistent indirect evidence that
  detailed-requirements RFPs remain the norm. Second (its independent
  run, under the profile): stop rule met, 13 URLs of which 7
  unverifiable (403 and timeouts, Gartner among them), none dead;
  disconfirming query found outcome-based procurement constrained by
  metric attribution, supplier risk resistance and governance, the
  detailed catalogue kept for auditability, consensus across silos and
  comparable scoring; the form persisting, the content shifting.
- Card 3 (what follows from the chain): answered by both; the custom
  build sourced by the second engine only. First: opening budget (17
  attempts, 9 lost), second part of the stop rule unmet (custom
  build, 29148). Second: every perspective with a primary within
  fifteen openings, 29148 and IREB cited for the frame, the custom
  build as an execution tender sourced; disconfirming query in both:
  enterprises reject prescriptive designs for COTS, the derivable
  share is large, not small.
- Card 4 (requirement to response instrument): answered by both.
  First: opening budget (14), each perspective with a primary;
  disconfirming found the box-ticking critique aimed at yes/no items
  and no superiority of free-form evaluation. Second, after one
  return for fabricated citations: every perspective with a primary;
  disconfirming found the matrix saturated by vendor compliance claims
  and AI answers, scripted demonstrations elevated.
- Card 5 (document and process): answered by both. First: opening
  budget (14), procurement officer and evaluator with primaries, no
  private-group primary reached. Second: stop rule met; disconfirming
  found the "living RFP" as a methodology and, in complex IT,
  competitive dialogue iterating until the final offer.
- Card 6 (buyer-side tools): answered by both. First: over the
  budget (19 fetches, 9 failed), evaluator weak; no independent
  review either way. Second, after one return: stop rule met;
  disconfirming found consensus that uncalibrated AI output is
  boilerplate and the substance stays human.

### Answers side by side

- Card 1. Claude: a canon exists (CIPS 2025 template and guidance,
  Info-Tech's RFP family, Forrester paywalled); a settled four-part
  skeleton with appendices; the IT content lives in the requirement
  part, generic at the institute, filled per category by the
  analysts; two archetypes supported, custom development not found.
  Antigravity: the same canon, ISM and Gartner named beside; the
  monolithic narrative RFP obsolete, the modular package (tender
  brief, technical SOW, response workbook, security questionnaire,
  pricing schedule) the norm; three archetypes with sharply different
  anatomy. Consistent on canon, skeleton and package; the archetype
  count differs by what each engine could source.
- Card 2. Claude: the solution written as requirements is the
  dominant failure; the remedy converges on problem, limits,
  scenarios; vendors price, game or decline an unclear RFP, no
  quantification found; form persists, content moves; branching
  supported for COTS only. Antigravity: the same failure and remedy
  from different sources; buyer regret after a purchase at 56 to 60
  per cent and peaking before implementation (Gartner); large linear
  IT projects failed or challenged in over 69 per cent of cases;
  vendors declining 37 to 40 per cent of solicitations and adding 15
  to 40 per cent and more to fixed-price bids for ambiguity; the
  wired RFP with column-fodder bidders; outcome-based procurement
  constrained by metric attribution and governance; branching across
  all three archetypes. Consistent; the second engine found figures
  the first did not, and asserts more.
- Card 3. Claude: the requirements core follows from the chain and is
  the bulk of the work; legal, commercial, security, risk,
  evaluation, contract and gates are people's; tiering has no
  upstream owner; SaaS/COTS: the design is the winner's, justified
  constraints survive; the custom build unsourced; recommendation: a
  thin artefact of sourcing decisions plus a render. Antigravity: the
  same mapping and the same human list; the custom build sourced (a
  full design makes an execution tender; a two-phase discovery and
  build procurement where the design is incomplete); DORA and NIS2
  clauses as pre-scoring disqualifiers; the RFP as a Lastenheft;
  recommendation: an archetype-branched composite render with a
  "human parameter manifest". Consistent in substance; the first
  gives the decisions an artefact with history, the second a manifest
  it does not version.
- Card 4. Claude: rows mechanical, effect-giving parameters human;
  the award formula can change the winner (Stilger 2017, Bergman and
  Lundberg); the matrix kept with graded codes and per-code evidence;
  recommendation: the decisions as an artefact. Antigravity: the same
  division, named as a mechanical pipeline and a commercial policy
  layer; rank reversal of relative price scoring (Bergman and
  Lundberg); the matrix saturated in SaaS and demoted to a hygiene
  filter, scripted demonstrations and proofs of concept carrying the
  evaluation; recommendation: a dual-artefact model with an explicit
  governance configuration, and a warning against rank-reversing
  formulas as a check. Consistent on the division; they differ on the
  matrix's weight in the evaluation.
- Card 5. Claude: the seam is the proposal due date; amendments
  before, equal-treatment exchanges after; the document carries its
  process rules; vendor answers return as sources, a changed
  requirement goes to the intent first; the Q&A and amendment record
  needs a versioned home. Antigravity: the same seam and the same
  change-control reading; the contract incorporates RFP, Q&A logs,
  addenda and proposal in an order of precedence; competitive
  dialogue in complex IT iterates specifications until the final
  offer; proprietary vendor architectures cannot be fed upstream; the
  e-sourcing platforms treat the RFP as relational data. Consistent
  on the seam; the second engine's dialogue finding bends it for
  complex purchases.
- Card 6. Claude: no buyer-side tool derives an RFP from a structured
  requirements set; inputs are templates, requests, prompts, forms or
  conversations; criteria are human everywhere; the market's
  generation has the shape of a render; the Coupa agent a lead.
  Antigravity: the same picture from a partly different set of tools;
  the intake platforms (Zip, Fairmarkit, Tonkean) as the locus of
  innovation; the double-AI loop pushing buyers to short outcome
  briefs and live gates. Consistent; the second engine adds the
  market's reaction.

Agreement across the twelve notes is consistency of two model
families reading the same web, stronger than one family's agreement
and still not validation (POS.0790): neither engine reached a
private group's internal procurement practice, and both lean on
public-sector and advisory material.

### Unexpected, gathered

Finds that reconfigure a question or bring a mechanism from
elsewhere:

- The requirement part of an RFP is contract text (CIPS Part 2 and 3,
  Claude card 1); whatever the chain supplies becomes an obligation.
- The RFP wants a different requirement style: "shall" is mandatory,
  use cases score badly, the form is a capability statement (Claude
  card 3); the RFP is a Lastenheft, the problem space, and a buyer's
  design in a COTS RFP is a Pflichtenheft where the vendor's belongs
  (Antigravity card 3).
- The award formula gets the least attention and decides the most;
  relative price scoring reverses ranks when a bidder is added or
  dropped (both engines, card 4).
- Regulatory resilience rules (DORA Article 30, NIS2) have moved from
  contract negotiation into the RFP as pass/fail gates before any
  scoring (Antigravity card 3); two of their items are derivable from
  the chain (Claude card 3).
- The compliance matrix has lost its discriminating power in SaaS:
  vendors claim 90 per cent compliance, AI answers the rest;
  evaluation moves to scripted demonstrations and proofs of concept
  (Antigravity card 4); Info-Tech issues a Scenario Template beside
  the RFP, a destination for the chain's use cases (Claude card 1).
- The market's "AI RFP generation" has the shape of the forge's
  render (both, card 6), and it has produced a loop: AI-inflated RFPs
  met by AI-inflated proposals, pushing buyers to three-to-five-page
  outcome briefs with live gates (Antigravity card 6).
- The CIPS cycle names RFI, ITT and RFQ and never RFP (Claude card 5).
- Prior engagement during requirements definition is the vendor's
  strongest predictor of winning; a chain composed before vendor
  contact is what vendors try to get into, and a cold RFP risks
  no-bids (both engines, card 2).
- Many specification-driven RFPs are wired: the specifications
  borrowed from an incumbent's collateral, the other bidders invited
  as column fodder to satisfy a three-bid rule; vendors treat
  hyper-specific proprietary criteria as a no-bid trigger
  (Antigravity card 2).
- Software buyers' regret peaks before implementation begins: the
  procurement process itself, not the system, exhausts the
  stakeholders (Antigravity card 2, citing Gartner).
- The classic RFP may be the minority route for technology purchases
  (Gartner survey via trade press, Claude card 3); agile frameworks
  reject the big-bang RFP outright (Antigravity card 1).
- The e-sourcing platforms treat an RFP as a relational schema of
  requirement lines linked to bid cells and scorecards; a monolithic
  text forces re-keying (Antigravity card 5).
- The institute's pricing clause asks the proposer for its own
  dependencies and assumptions: the chain's ASM and DEP items have a
  mirror on the supplier's side (Claude card 1).
- Product-security questions are project-independent and belong with
  reusable material (Claude card 3, the agent's inference).
- Vendor architectures received in proposals cannot be fed upstream
  without breaching confidentiality and fairness: the return channel
  is asymmetric (Antigravity card 5).

Finds that add a source to a point already made: the agile route
moving the design into the dialogue (several cards); the three-way
choice amend, cancel, other (Claude card 5); intake platforms as a
front door (Antigravity card 6, a detail of its F1).

### Not found, gathered

- The acquisition text of ISO/IEC/IEEE 29148 and BABOK's Vendor
  Assessment: paywalled for the first engine (cards 1, 3, 5); the
  second engine cites both for the frame without quoting the body.
- A primary on the custom-build archetype: not found by the first
  engine (cards 1, 2, 3); sourced by the second from practitioner and
  advisory texts, not from a standard.
- Any private-company procurement guide on Q&A, amendments,
  clarification, final offers, evaluation methodology or response
  templates: neither engine reached one; everything is public-sector,
  supplier-side or advisory.
- A benchmark of RFP failure or cancellation rates; a measured risk
  premium for ambiguity (the second engine's 15 to 30 per cent is a
  rule of thumb, not a study).
- A formula that derives evaluation weights from requirement text;
  a universal weighting ratio between commercial and technical
  criteria (both engines, card 3 and 4).
- An independent review of an RFP generated by a buyer-side
  platform's AI; a controlled study of outcomes of AI-generated
  against human-drafted RFPs (both, card 6).
- A measured cost of over-specifying a design in a COTS purchase; a
  measured frequency of material amendments in private IT RFPs
  (second engine, cards 3 and 5).
- A buyer-side primary using "compliance matrix" or "BAFO" (CIPS
  writes "BFO"); ISM's glossary; IT-specific evaluation weights
  (first engine, card 1).

### Claude's view

My own, marked as such; verified where it rests on the notes'
sources, a hypothesis where it goes beyond them.

Verified on the notes of both families: the RFP is two things in one
package. The document is generated: its requirement part is a
transformation of the chain into the problem space, a Lastenheft
(intent, assignment, BRD; of the solution design only integration
boundaries and justified constraints for a purchase, the design
itself for a build), its other parts are people's text (instructions,
evaluation process, terms, contract, gates), and its shape is the
institute's four parts and schedules issued as a package. The
decisions that make it an instrument (archetype, the tier of every
item, the weights, the hurdles, the award formula, the response codes
and their evidence, the pricing model per scope item, the gates and
who supplies them) are nobody's upstream and change who wins.

Hypothesis, mine: the forge should give those decisions a home of
their own, a thin artefact of sourcing decisions with items, a
history and a reviewer, placed below the solution design, and make
the RFP itself a render of the chain, that artefact and a
person-supplied file of terms, in the CIPS skeleton as a package,
with a recipe that branches on the archetype and translates the
chain's style (shall and use cases into capabilities and scenarios).
From the second engine I take three things into this: the scenario
and demonstration scripts as an instrument of their own made from the
use cases, beside a matrix demoted to a filter; the rank-reversal
warning as a check on the chosen formula; and the regulatory gates
asked up front as pass/fail items the compliance owner supplies. The
artefact is also the versioned home of the amendment and Q&A record
up to the proposal due date, after which the forge stops; where a
project runs a competitive dialogue, the record runs to the final
offer. Vendor questions and proposals come in as sources; a changed
requirement goes to the intent first; a vendor's architecture never
goes upstream.

Two cautions. Two families agreeing on the same web is still
consistency; neither reached a private group's own practice, and
both engines were briefed from one plan written by one of them. And
the custom-build branch rests on one engine's practitioner sources:
if the group's first RFP is a build, the branch is the least tested
part.

What I propose for the chain, through `/forge intent` and never
here: a position that an RFP is a render over a thin artefact of
sourcing decisions, branched by archetype, the artefact born through
`/new-artefact` on a real purchase (POS.1430, POS.1380); the brief
`next-gen` or a brief of its own to carry the material until then;
and, before the first custom-build sourcing, a quick research card on
that branch.

## Notes

- `card-1-canon-and-anatomy.claude.md` and `.antigravity.md`, from
  `tmp/research/2026-10-24-rfp-from-the-chain/card-1-canon-and-anatomy/`
- `card-2-where-the-rfp-fails.claude.md` and `.antigravity.md`, from
  `…/card-2-where-the-rfp-fails/` (the second engine's first run
  contaminated, kept there as `antigravity.contaminated.md`; the
  filed note is the run under the profile)
- `card-3-what-follows-from-the-chain.claude.md` and `.antigravity.md`,
  the second from `…/card-3-what-follows-from-the-chain-return/` (the
  first run contaminated, the second returned for dead URLs; both
  kept in `…/card-3-what-follows-from-the-chain/`)
- `card-4-requirement-to-response-instrument.claude.md` and
  `.antigravity.md`, the second from
  `…/card-4-requirement-to-response-instrument-return/` (likewise)
- `card-5-document-and-process.claude.md` and `.antigravity.md`, the
  second from `…/card-5-document-and-process/` (its first run
  contaminated, kept there)
- `card-6-buyer-side-tools.claude.md` and `.antigravity.md`, the
  second from `…/card-6-buyer-side-tools-return/` (likewise)
- The second engine's review of the draft plan:
  `…/plan-review/antigravity.md`, under `tmp/`, not a note of the
  bundle. The citation reports of all twelve notes: `…/cite/`.
