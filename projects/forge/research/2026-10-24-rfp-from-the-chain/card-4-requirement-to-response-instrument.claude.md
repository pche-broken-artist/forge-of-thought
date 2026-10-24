---
date: 2026-10-24
project: forge
topic: how a requirement becomes a response instrument
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-24-rfp-from-the-chain/card-4-requirement-to-response-instrument
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-4-requirement-to-response-instrument; web sources below
---

# A requirement becomes a response instrument through decisions no requirement carries

## In short

The rows of the instruments follow mechanically from the
requirements: one line of the compliance matrix per business rule,
use case or non-functional requirement, and one line of the pricing
schedule per scope item. Everything that gives those rows their
effect does not follow: the set of response codes and what evidence
each code demands, the mandatory flag that turns an item into a
disqualifying gate, the weights, the minimum-score thresholds, the
scale and its anchors, the formula that turns price and quality
scores into a ranking, and the pricing model (fixed price per
milestone, rate card, outcome-based) are decisions of the buyer, and
the academic evidence says the formula alone can change who wins
[5][6][7]. This is well supported: public RFP documents [1][8],
supplier frameworks [9], a procurement regulation [3], two
peer-reviewed economic studies [5][6] and practitioner guidance [4]
[7] agree on the division, though not on which formula or which
weights are right. The disconfirming query found the critique of
box-ticking as practitioner claim (yes/no items make bidders look
alike and hide price and scope [4][10]) but found no source showing
that free-form expert evaluation outperforms a matrix; the one
controlled study found [11] says expert quality ratings themselves
carry considerable randomness, which weakens the alternative as much
as the matrix. The unexpected lead: the award formula, not the
criteria, is where buyers pay least attention and where the outcome
is most sensitive [5].

## Question

Card 4: how a requirement becomes a response instrument.

Question: How a declarative requirement (a business rule, a use case,
a non-functional requirement) is turned into the instruments a bidder
answers and an evaluator scores: a compliance matrix with response
codes (out-of-the-box, configurable, custom, third-party, roadmap),
weighted scoring with hurdle criteria and thresholds, price and
quality normalisation, and a pricing schedule tied to scope items
(fixed price per milestone, time and materials rate card,
subscription tiers); and which of these follow mechanically from the
requirements and which need a person's judgement; against the
alternative that compliance matrices lead to box-ticking without
substance and that free-form responses evaluated by experts serve
better.

Why it matters: Decides whether an RFP artefact of the framework has
items and decisions of its own (response codes, weights, hurdles, the
pricing shape) beyond what the artefacts above it carry, and what of
that can be derived automatically.

What would answer it: Bid evaluation methodologies and templates of
procurement institutes and advisory firms, published compliance
matrices and scoring rubrics, guidance on pricing schedule design.

Where to look: procurement institutes' evaluation guidance, advisory
firms' vendor evaluation toolkits, published RFP response templates
and compliance matrices, practitioner guidance on weighted scoring
and price normalisation; more than one route. Known items: one
described system of compliance response codes; one method of price
and quality normalisation; one pricing schedule template tied to
scope.

Disconfirming query: Expected: compliance matrices and weighted
scoring are the norm and largely derivable from the requirements.
Search for the opposite: critiques that matrices produce box-ticking
without substance and that expert evaluation of free-form proposals
outperforms them.

Stop rule: Nothing new from a differently-worded query, and each
perspective of the card (evaluator, vendor, requirements engineer)
has a primary source; or about fifteen openings spent.

The baseline the note must beat: the expectation that the
instruments are the norm and largely derivable, so that an RFP
layer would add little beyond a re-shaping of the BRD. The note
beats it if it can name, with sources, which parts of each
instrument are derivation and which are decisions with consequences
of their own.

## Key findings

F1. **A compliance matrix in practice is a graded availability key,
not a yes/no column, and each code demands its own supplementary
evidence.** (consensus in public-sector practice; evidence: a public
RFP response template read directly, an advisory firm's guidance;
the other code sets seen only in search results). The City of
Federal Way ERP RFP (2024) rates every functional requirement 4
"Standard and available" (out of the box or with configuration
included in the proposal), 3 third-party software with the name of
the recommended application, 2 "Software does not include this
requirement and requires modification" with the estimated cost of
the modification, 0 "Software will not meet requirement", and F
"Requirement will be available in future release" with the
anticipated release month and year; every item also requires a
comment, hyperlinks and cross-references to other items are
forbidden, and each requirement carries a buyer-side rank R
(Required), I (Important), N (Nice to Have) or E (Explore) [1]. The
search result list showed the same family of keys elsewhere (a
template separating basic from significant configuration; a
Yes/Partially/Future/No key; a Standard/Configuration/Customization/
Not Available template), but none of these pages was opened, so they
are reported here as search-list observations only. The advisory
side adds why the key needs guarding: "Vendors will often state that
a functional requirement is available through third-party
applications" (bullet under "Request definition surrounding software
modification"), so the buyer should ask whether the integration is
proven and licensed separately, and "If you leave any possible
variation open in your requirements, vendors will fill it with their
own assumptions." (opening of "Requirements specificity is key") [2].
The card's five codes (out-of-the-box, configurable, custom,
third-party, roadmap) are therefore a recognisable rendering of this
family, but the exact set, its grading and the evidence demanded per
code vary by buyer and are the buyer's choice.

F2. **Hurdle criteria and minimum-score thresholds are a separate
mechanism from weighting, and good practice requires them to be
declared in the RFP before proposals are read.** (consensus;
evidence: a state procurement regulation, practitioner guidance, a
public RFP). Utah's administrative rule lets a procuring unit
"establish minimum score thresholds to advance proposals from one
stage in the RFP process to the next", requires that "If used,
minimum score thresholds must be set forth in the RFP", and forbids
a threshold based on "a natural break in scores that was not defined
and set forth in the RFP" or on "a predetermined number of offerors,
unless a written exception is provided by the procurement official"
(rule effective 22 October 2024) [3]. Practitioner guidance says the
same from the other end: disqualifying ("kill-switch") answers should
dismiss a bidder outright rather than be given a weight, and
questions asked only for information should not be scored at all
[4]. The Federal Way RFP applies the gate at the matrix level:
software missing "a significant number of required features and
technology preferences may be eliminated" [1]. Which requirements
are gates and where a threshold sits is nowhere derived from the
requirement text; the regulation's whole point is to force that
decision to be taken and published first.

F3. **Weights, scales and their anchors are judgement, and the
choice of the award method itself is an economic decision with known
failure modes.** (consensus on the first part, contested on the
method; evidence: practitioner claim, economic working paper). The
practitioner side: critical questions should carry "the lion's share
of total weight", weights set by category first and then by
question; fine scales give false precision, "In reality, I'd
challenge anyone to properly differentiate a score of "12" from
"13."" (reason 4); and evaluators need concrete descriptions of what
each score point means [4]. The economic side: Bergman and Lundberg
(2011) argue that price-to-quality scoring, the most common method,
is "non-transparent, making accurate representation of the
procurer's preferences difficult", is open to manipulation through
dependence on irrelevant alternatives and is non-linear in bid
prices; "We prefer quality-to-price scoring, where money values are
assigned to different quality levels", and "When the costs of
quality are relatively well-known, however, lowest price is the
preferable award criteria." (abstract) [6]. Read through the fetch
tool's summary of the abstract page; the full paper was not read.

F4. **Price and quality normalisation is a formula choice that can
change the winner; the literature counts dozens of formulas,
distinguishes relative from absolute ones and gives warnings rather
than one answer.** (consensus that the choice matters; contested
which formula; evidence: peer-reviewed study on 382 real tenders,
practitioner-lawyer analysis). Stilger, Siderius and Van Raaij
(Journal of Public Procurement, 2017) study 38 formulas: "The choice
of formula critically affects which bid wins." (abstract). An
absolute formula "does not utilize information from the submitted
bids as a reference point", which avoids the ranking paradox and lets
bidders price their own compliance, but "of 14 absolute formulas we
have studied, all except four need some extra input such as
reference price or price range", so the buyer must know the market
price before tendering; on 382 real tenders "the practical occurrence
of the ranking paradox for most formulas is small"; the authors
recommend formulas with straight iso-utility curves and protection
against a winner with an extremely high price, and observe that "The
formula itself often gets far less attention; formulas are often
chosen without carefully analysing their properties." (Conclusion)
[5]. The practitioner analysis of the most common UK formula (lowest
price divided by bid price times the price weight) names three
problems: outlier low bids distort every other score, "The
Goldilocks bid, the one that is "just right", is being squeezed out
of the running." (Problem 2), and "the F1 formula operates on
relative difference whereas the five point scale operates on
absolute difference." (Problem 3); it proposes scoring price by its
distance from zero with a cap at twice the median bid, at the cost
of anchoring and of revealing the price of a quality point in
advance [7]. Search results also pointed to a public price-quality
guide that converts quality points into a dollar premium deducted
from the price, and to a Nordic non-linear model, but neither page
could be opened (see Not found).

F5. **A pricing schedule tied to scope has a stable generic shape,
and the buyer form and the supplier framework meet in the same three
or four blocks.** (consensus by convergence of two primaries;
evidence: a buyer's response form, a supplier's published pricing
framework). The New Zealand EECA Pricing Schedule Response Form
demands a breakdown of all costs and the total excluding GST, rates
"either hourly or daily or both" where fee-based, a statement of how
risks and contingencies are managed, and assumptions: "if the
Respondent would expect us to pay more than the quoted price or
estimate if particular assumptions or dependencies are not
satisfied, the Respondent must call out those assumptions and
dependencies." (Instructions for Respondents); its tables are Unit
Pricing (item, unit price, quantity, sub-total), Fixed price with
payment milestones (milestone, estimated payment date, instalment
amount), Rate card (individual, role, organisation, hourly and day
rate), Expenses (item, maximum limit, expected quantity) and
Assumptions; a respondent may propose another pricing approach but
"must also submit a Pricing Schedule that conforms." [8]. From the
supplier side, a G-Cloud 14 pricing framework offers exactly the
counterpart: Time and Materials "based on our G-Cloud 14 SFIA Rate
Card" invoiced monthly for work completed, Fixed Price where "Each
work package will include a detailed breakdown of delivery and
payment milestones.", and Outcome Based Pricing procured against the
desired deliverables of a statement of work [9]. The form is generic;
which scope items become milestones, which work is rate-based and
which is outcome-based is not in the form and not in the
requirements. Subscription tiers appeared only in search results (a
G-Cloud document mentioning monthly subscription fees for retained
support) and were not opened.

F6. **The box-ticking critique exists and is directed at the yes/no
item, not at the matrix; no source was found that expert evaluation
of free-form proposals outperforms a matrix, and the one controlled
study found undermines expert ratings too.** (the critique: single
sources, practitioner claim; the alternative: not found; the study:
single source, experimental). A 2006 practitioner column says
"Don't just ask "Do you ...?" Ask "How do you ... ?" and "How much ...
?"" (section Beyond "Yes" and "No" Responses) and "Numbers are
facts; flowery words from the marketing department are not."
(section Don't Talk Past One Another) [10]; the 2018 consultant list
says "Odds are your suppliers will end up looking too similar if the
bulk of responses fall into simple yes/no buckets." (reason 3) and
warns against crediting long non-answers for their length [4]. Both
keep the matrix and ask for elaborate, evidenced answers inside it.
Against the alternative, a 2024 Warwick Business School PhD thesis
tested subjective quality ratings experimentally under different
conditions (accountability, evaluation mode, evaluability,
moderation) and reports "there is considerable randomness in quality
rating", that "even small differences in quality rating which may be
due to noise can alter the outcome of a tender." and that "rating is
subjective and contextual, prone to change under different
conditions" (abstract) [11]. Read through the fetch tool's summary of
the repository record; the full thesis was not read, and its sample
is not stated in the abstract.

F7. **What follows mechanically and what needs a person, by
instrument.** (the agent's synthesis of F1 to F6; inference marked as
the agent's own). Mechanical from the requirements: the row set of
the matrix (one per BR, UC, NFR, with the parent ID), the row set of
the pricing schedule (one per deliverable or scope item), the
mandatory flag where a requirement is already a constraint or a
shall-not, and the demand for a comment and evidence per row. A
person's judgement, with consequences for who wins: the response-code
set and the evidence each code triggers (F1), which items are gates
and where thresholds sit (F2), weights, scale and anchors (F3), the
award formula and whether quality is monetised (F3, F4), the pricing
model per scope item and the milestone mapping (F5). The evidence is
consistent across the evaluator [3][4][5][6][7], the vendor [2][9]
and the requirements engineer [1][8] perspectives; no source was
found that derives any of the judgement items from requirement text.

## Unexpected

The literature's own emphasis is inverted against the card's. The
card treats the matrix and the weights as the instruments and the
formula as normalisation; Stilger et al. find that criteria and
weights get "abundant attention from both buyers and bidders" while
"The formula itself often gets far less attention", and that the
formula "critically affects which bid wins" [5]. Lead: if the forge
ever carries an evaluation plan, the formula is an item with a
history, not a footnote.

Monetising quality dissolves the weight question into a price
question. Bergman and Lundberg prefer quality-to-price scoring, where
each quality level is given a money value [6], and Stilger et al.
note that absolute formulas let bidders "calculate the monetary
value that buyers attribute to each weighted sub-criterion" [5].
Lead, the agent's own: a position of the intent that says what an
outcome is worth is closer to this method than a weight is.

Outcome-based pricing appears in a supplier's standard framework
beside time and materials and fixed price [9]. Lead for the
planner's premortem on outcome-based briefs: the pricing shape
already has a slot for it in the market's own templates.

## Not found

- An openly published vendor-evaluation toolkit of an advisory or
  analyst firm (searched twice with "advisory", "toolkit", "vendor
  evaluation"; results were vendor-software blogs and glossaries,
  excluded by kind).
- Official CIPS guidance on quality-price weighting (one query; the
  results were a third-party study aid, government guides and blogs;
  no CIPS page in the list).
- The Queensland price-quality guide note converting quality to a
  dollar premium (HTTP 404 on opening), the Connecticut Form RFP-16
  price schedule with four pricing methodologies (request rejected by
  the host), the Durham NC proponent response template with its
  basic/significant configuration distinction (HTTP 403). All three
  are known from search results only and are cited for nothing.
- Any study comparing outcomes of matrix-based evaluation with
  free-form expert evaluation (two differently worded queries on
  box-ticking and tick-box; the closest is the Warwick thesis on the
  noise of expert ratings [11]).
- A private-company (non-public-sector) RFP response template or
  evaluation methodology; everything retrievable was public-sector
  or supplier-side. A figure for how often hurdles disqualify or how
  often the formula changes the winner in private tenders: no source,
  a gap.
- A described subscription-tier pricing schedule tied to scope items:
  seen in a search result for a G-Cloud document, not opened.

## Options

1. The RFP as a render of the BRD and the solution design, the
   judgement items supplied as recipe parameters (code set, weights,
   thresholds, formula, pricing model). Trade-off: the rows are
   derived for free and stay traceable, but the decisions that
   decide the winner live in a recipe, which the forge says is a
   tool with no record of thinking, while the evidence says these
   decisions deserve a history [5][6].
2. The RFP as an artefact of the chain with items of its own: one
   item per judgement decision of F7 (the code set and its evidence
   demands, each gate, each weight group, the formula, the pricing
   model per scope item), the matrix and schedule rows generated
   from the parents and carried as a table. Trade-off: the decisions
   get IDs, histories and reviewers, at the cost of a layer that is
   partly derivation; the derivation part must be kept mechanical or
   it drifts from the BRD.
3. A split: the matrix and the pricing schedule as renders, the
   evaluation plan (gates, weights, thresholds, formula) as a small
   artefact or as a section a person supplies. Trade-off: honours the
   division the evidence draws most cleanly, but puts the response
   codes, which are a buyer decision too (F1), on the render side.

## Relevance to this project

The card asked whether an RFP artefact would have items and
decisions of its own beyond the artefacts above it. The answer from
the sources is yes for every instrument's effect and no for its
rows: the response-code set, the gates and thresholds, the weights,
the scale, the award formula and the pricing model are decisions no
BR, UC, NFR or SOL carries, and the choice among them changes who
wins [5][6][7]; the rows themselves are a mechanical projection of
the BRD and the deliverables [1][8]. The agent's recommendation,
marked as its own: option 2 or 3, chosen against option 1, because
a decision that selects the supplier should have a history and a
reviewer, and the forge gives those to artefacts, not to recipes;
between 2 and 3, option 2 keeps the response codes with the other
decisions, which F1 says they are. The disconfirming side does not
move this: the critique asks for evidenced, graded answers inside the
matrix [2][4][10], which is what the code set with its per-code
evidence demand provides, and the noise of expert ratings [11] is an
argument for anchors and declared thresholds, not against the
instrument. What the forge cannot derive and must ask a person: the
code set, the gates, the weights, the formula and the pricing model;
what it can offer: the rows, the mandatory flags from constraints,
and the warnings of F3 and F4 as checks on the person's choices.

Consult when: deciding whether the RFP is an artefact or a render;
designing the response-code key and the evidence each code demands;
choosing a price-quality formula or a threshold; shaping a pricing
schedule from deliverables; answering a reviewer who says the matrix
is box-ticking.

## Sources

1. Enterprise Resource Planning Software and Implementation Services,
   bid 2024-0816, City of Federal Way, Washington; dated by the bid
   dates on the page (start 16 August 2024, end 17 September 2024).
   https://www.federalwaywa.gov/bids/enterprise-resource-planning-software-and-implementation-services
   Kind: primary (a public RFP's response instructions). How read:
   through the fetch tool's summary of the page, the functional
   response codes and evaluation remarks; the RFP document proper
   not retrieved. Original.
2. Creating the Perfect RFP for an ERP Software Evaluation, Brian
   Potts, Third Stage Consulting Group; byline dates published 24
   March 2019, updated 27 August 2026.
   https://www.thirdstageconsulting.com/?p=1387
   Kind: secondary (advisory firm's guidance). How read: through the
   fetch tool's summary of the page. Original (reached by redirect
   from thirdstage-consulting.com).
3. Utah Admin. Code R33-107-501.5, Minimum Score Thresholds, hosted
   by Cornell Legal Information Institute; dated by the history on
   the page (adopted via Utah State Bulletin 2024-21, effective 22
   October 2024).
   https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R33-107-501-5
   Kind: primary (regulatory text). How read: through the fetch
   tool's summary, quoting the rule text. Copy of the Utah rule as
   hosted by LII; the state's own publication was not sought.
4. 13 Reasons your RFP Scoring Sucks, Brian Seipel (guest author,
   procurement consultant at Source One Management Services),
   Sourcing Innovation blog; byline 15 October 2018.
   https://sourcinginnovation.com/wordpress/?p=7308
   Kind: secondary (practitioner claim). How read: through the fetch
   tool's summary of the page. Original.
5. A Comparative Study of Formulas for Choosing the Economically Most
   Advantageous Tender, Przemyslaw S. Stilger, Jan Siderius and Erik
   M. Van Raaij, Journal of Public Procurement vol. 17 issue 1, pp.
   89-125, Spring 2017; dated by the journal header in the PDF.
   https://www.ippa.org/images/JOPP/vol17/issue-1/Article_4_Stilger-et-al.pdf
   Kind: primary (peer-reviewed study on 382 real tenders). How read:
   partially, from text extracted locally from the fetched PDF: the
   abstract, the introduction, the section Relative versus Absolute
   Formulas and Ranking Paradox, and the Conclusion; the formula
   tables not read. Original (publisher's site). One author is CEO of
   an e-tendering firm, as the paper's own footnote states.
6. Tender Evaluation and Award Methodologies in Public Procurement,
   Mats Bergman and Sofia Lundberg, Umeå Economic Studies no. 821,
   S-WoPEc; dated 16 March 2011 on the page.
   https://swopec.hhs.se/umnees/abs/umnees0821.htm
   Kind: primary (economic working paper; abstract page). How read:
   abstract only, through the fetch tool's summary; the full paper
   not opened. Original repository listing.
7. Goldilocks and the three problems: issues with the most common
   tender evaluation method, Hector Denfield (Sharpe Pritchard),
   Local Government Lawyer; byline 7 December 2018.
   https://www.localgovernmentlawyer.co.uk/procurement-and-contracts/308-procurement-features/39482-goldilocks-and-the-three-problems-issues-with-the-most-common-tender-evaluation-method
   Kind: secondary (practitioner-lawyer analysis). How read: through
   the fetch tool's summary of the page. Original.
8. Request for Proposal (RFP) Pricing Schedule Response Form, Energy
   Efficiency and Conservation Authority (EECA), New Zealand; dated
   by the docx core properties (created 1 May 2026, revision 4); no
   date in the text.
   https://www.eeca.govt.nz/assets/RFP-pricing-schedule-response-form.docx
   Kind: primary (a buyer's response form). How read: in full, from
   text extracted locally from the fetched docx. Original.
9. Parico Limited: Pricing Framework, G-Cloud 14 pricing document on
   the UK Digital Marketplace; dated by the PDF metadata (7 May 2024)
   and the URL.
   https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/710012/821651127142221-pricing-document-2024-05-07-0944.pdf
   Kind: primary (a supplier's own pricing document). How read: in
   full (one page), from text extracted locally from the fetched
   PDF. Original. A vendor document about its own offer, used as
   such.
10. Computer Counsel: How to Make the RFP and Procurement Process
    Work for You, John Gliedman, Computerworld opinion column;
    byline 20 March 2006.
    https://www.computerworld.com/article/1722081/computer-counsel-how-to-make-the-rfp-and-procurement-process-work-for-you.html
    Kind: secondary (practitioner opinion). How read: through the
    fetch tool's summary of the page. Original.
11. Could do better: an investigation of the fairness and fitness for
    purpose of public tender evaluation, Janet Izatt, PhD thesis,
    Warwick Business School, University of Warwick; dated 2024
    (November 2024) by the repository record.
    https://wrap.warwick.ac.uk/193733
    Kind: primary (experimental study; repository record). How read:
    abstract only, through the fetch tool's summary; the thesis body
    not read. Original repository.

## Opened and not used

- https://www.forgov.qld.gov.au/__data/assets/pdf_file/0031/377905/guide-note-price-quality-method-for-evaluating-tenders.pdf
  - attempted, HTTP 404; not retrieved, cited for nothing.
- https://www.durhamnc.gov/DocumentCenter/View/47236/RFP-23-0008-Proponent-Response-Template
  - attempted, HTTP 403; not retrieved, cited for nothing.
- https://biznet.ct.gov/SCP_Documents/Bids/48201/Price_Schedule.pdf
  - attempted, the host returned a "Request Rejected" page; not
  retrieved, cited for nothing.
- https://www.thirdstage-consulting.com/?p=1387 - a 301 redirect to
  [2]; counted with [2], not a separate page.

## Search record

Queries, in order: (1) RFP compliance matrix response codes
out-of-the-box configurable third-party roadmap; (2) weighted
scoring RFP evaluation hurdle criteria minimum threshold; (3) tender
evaluation price quality normalisation formula relative scoring;
(4) RFP pricing schedule template fixed price milestones rate card
subscription; (5) criticism compliance matrix box-ticking vs expert
judgement free-form (disconfirming); (6) ERP RFP response key
standard configuration modification third party future release;
(7) Bergman Lundberg tender evaluation scoring rules; (8) software
selection yes/no checklist vendors answer yes demo scripts
(disconfirming, reworded); (9) CIPS tender evaluation weighting
quality price ratio; (10) RFP weighted scoring false precision
evaluators judgement; (11) tick-box tender evaluation method
statements outcome-based (disconfirming, reworded again).

Openings: 14 pages fetched, of which 11 read (1 to 11 above) and 3
not retrieved (listed under Opened and not used); the three binary
files among the 11 were read from text extracted locally after the
fetch. Reason the run ended: the opening budget, spent at fourteen,
with each perspective of the card holding a primary source (the
evaluator: 3, 5, 6; the vendor: 9, and 2 for the vendor's conduct;
the requirements engineer: 1, 8). The last reworded disconfirming
query (11) still brought one new source [11], so the first part of
the stop rule was not what ended it.
