---
date: 2026-10-24
project: forge
topic: where the specification-driven RFP fails and where the outcome-based one wins
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-24-rfp-from-the-chain/card-2-where-the-rfp-fails
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-2-where-the-rfp-fails; web sources below
---

# The specification-driven RFP fails by writing the solution as requirements; the outcome-based form wins on content, while the RFP as a form persists

## In short

The practitioner and advisory literature opened agrees on one
failure mode above all others: the RFP writes the solution as
requirements ("the system shall follow the current paper-based
process"), inflates the list, and gets checkbox answers that do not
differentiate vendors; the buyer thereby takes the design risk and
caps what the vendor will do [1][2][3][4][5]. From the vendor's side
an unclear RFP produces high bids that price the risk, low bids that
live on change orders, no-bids and incomparable bids [7]; the
strongest predictor of a winnable RFP is having shaped its
requirements before issue [8]. The counter-movement is consistent:
state the problem and the limits (budget, dates, scope size,
conditions), write use cases or scenarios instead of feature lists,
run an RFI first where market knowledge is thin, and let the vendor
propose the mechanism [1][2][3][4][5][6]. All of this is practitioner
claim; no controlled study was found, and the field's benchmarks of
IT project failure (McKinsey/Oxford, Standish) could not be opened.
The disconfirming query did real work: the complaint about
over-specified RFPs is word for word the same in 2009 [3] and 2026
[4], the RFP volume vendors answer keeps rising [9], and
outcome-based contracting is reported at 67% of organisations by a
consultancy survey [10] against "at most 15 percent of new deals" in
2009 trade press [11] - so detailed-requirements RFPs remain the
norm in practice while the recommended content moves to outcomes.
The form is not leaving; its content is. The one unexpected thing:
the branching premortem is supported only for the COTS/SaaS archetype
(selection needs less detail, use cases and fit-gap scoring [6]); for
custom development and systems integration no opened source says
where the solution design belongs.

## Question

#### Card 2: where the specification-driven RFP fails and where the outcome-based one wins
- **Question:** The documented failure modes of IT RFPs (the solution over-specified instead of the outcome, requirement inflation, vague or hidden evaluation criteria, vendor-written RFPs, boilerplate) and the counter-movement (outcome-based RFPs, staged RFI then RFP, agile and iterative procurement, vendor dialogue), distinguished by archetype (SaaS/COTS selection, custom development, systems integration), and seen also from the vendor's side (bid/no-bid decisions, how ambiguity raises the risk premium, what structure lets a vendor estimate honestly); against the alternative that the classic requirements-driven RFP works, that outcome-based and agile procurement are marginal in private enterprise, and that detailed requirements remain the norm.
- **Why it matters:** Decides what a derived RFP must avoid, and whether the form itself is changing under the framework's feet (the planner's premortem).
- **What would answer it:** Surveys and benchmarks of IT procurement and project failure, practitioner and advisory literature on outcome-based and agile procurement, vendor-side accounts of unanswerable RFPs; public-sector studies only as a reference for failure modes.
- **Where to look:** industry surveys and benchmarks (Standish Group, Gartner, Bain or similar sourcing studies), procurement institutes' and advisory firms' guidance on outcome-based procurement, vendor-side bid management literature; more than one route. Known items: one survey or benchmark of IT procurement or RFP failure and cancellation rates; one source on outcome-based procurement; one vendor-side text on what makes an RFP unanswerable.
- **Disconfirming query:** Expected: the classic RFP has known failure modes and the field is moving towards outcome-based forms. Search for the opposite: evidence that outcome-based or agile procurement failed or remained marginal in private enterprise, and that detailed requirements remain the norm.
- **Stop rule:** Nothing new from a differently-worded query, and each perspective of the card (architect, vendor) has a primary source; or about fifteen openings spent.

The baseline the note must beat: the folk knowledge that RFPs are
long, that vendors tick every box, and that "outcomes not
requirements" is the fashionable advice. To beat it the note has to
name the mechanism of each failure with a source that stands on its
own, show the vendor's economics rather than assert them, and say
with evidence whether the classic form is actually being displaced
or only criticised.

## Key findings

F1. **The dominant documented failure mode is the solution written
as requirements: the RFP specifies "how", the buyer takes the design
risk, and the requirement becomes the vendor's ceiling.** [consensus
among practitioner and advisory claims; no controlled study] The
Best Value research group names three pitfalls of the overprescribed
RFP: the buyer becomes the expert and carries the cost when the
specified solution fails, non-experts gain an advantage because a
detailed specification makes all bidders look alike and price
decides, and the buyer must micromanage because the requirement is
the vendor's ceiling - "Overprescribed RFPs do not give the client
the advantages they hope for but only add risk to the project" [1].
Info-Tech, citing Bonfire, states the counter-rule as "IT RFPs should
specify the problem to be resolved rather than the solution to be
provided" and adds that "the half-life of an IT requirement is less
than six months" (a secondary citation inside [2]) [2]. A 2026
regulated-industry column gives the pattern its canonical example,
"The system shall follow the current paper-based process", and the
diagnosis "The issue is rarely that too little was specified but
that too much of the wrong thing was" (section The Real Downstream
Impact) [4]. The group that publishes [1] sells the method it
recommends, so its claim is also a vendor claim.

F2. **Requirement inflation and checkbox formats defeat
differentiation; the remedy the literature converges on is a short
set of use cases or scenarios.** [consensus, practitioner claims]
"Most RFPs are grossly over-specified"; one WCM RFP of about 200
requirements drew the answer "Our solution natively provides this
capability" to most of them, and the author proposes 40 or 50
narratives in place of 200 or 300 requirements, each doubling as a
later acceptance test [3]. Real Story Group: "vendors have seen them
all and have figured out how to check all the boxes"; keep canonical
requirements to a minimum and "develop use cases, sometimes called
scenarios, journeys, or stories" [5]. Argon Digital, for package
selection: selection needs less detail than building; use cases or
user stories, business rules, data needs and quality attributes;
weighted scoring with direct examination of high-priority items [6].
[4] reaches the same place from a regulated industry: specify
process variability, friction, critical quality risks and measures
of success, not screen flows.

F3. **From the vendor's side an unclear RFP is priced, gamed or
declined: high bids cover the risk, low bids live on change orders,
strong suppliers no-bid, and bids become incomparable.** [single
source for the mechanism, practitioner claim; no quantification
found] Perkins (2007) sets out the four outcomes under their own
headings: unclear specs make good bidders "bid extremely high to
cover their risk"; others bid low and expect "the inevitable change
orders"; "Fuzzy RFPs force bidders to make numerous assumptions"
so even strong suppliers skip the bid; and "Not all bidders will make
the same assumptions", so the bids cannot be compared [7]. The
structure that lets a vendor estimate honestly is, by the same
literature, the one in F1 and F2: the problem, the fixed limits
(budget, dates, scope size in employees, transactions or sites,
mandatory conditions, the documents) [1] and scenarios that say what
must happen rather than how [3][5].

F4. **Vendor-written RFPs and pre-set evaluation criteria are
treated on the vendor side as the first qualification question, and
prior engagement during requirements definition as the strongest
predictor of winning.** [single source, practitioner claim, December
2025] "Prior engagement with the buyer during requirements
definition is the strongest predictor"; red flags are requirements
that mirror one vendor's proprietary terminology, a compressed
response window ("often ten business days or fewer for a complex
enterprise deal"), evaluation weighted mainly on price with the rest
reduced to pass/fail gates [8]. Info-Tech's "Critical Insight" that
"Vendors generally do not like RFPs" and that vendors believe the
decision is already made points the same way from the buyer-advisory
side [2]. Evaluation criteria defined and weighted while the RFP is
drafted is Info-Tech's remedy [2].

F5. **The vendor's economics of answering are measurable and show a
market that answers more RFPs, not fewer, with a stable win rate and
price as the top loss reason.** [vendor report; self-selected survey
of 1,650+ proposal professionals with APMP, 2024] Average annual
submissions rose to 175; 77% of teams use a go/no-go process, down
from 80%; teams answered about 65% of the RFPs they were invited to;
win rate 43% against 44% the year before; 67% cite price as a top
reason for losing against 55% two years earlier [9]. Info-Tech,
citing third parties, gives 3-5% of anticipated contract value as
what vendors budget to respond and 44% as a win rate [2]. The report
is the publisher's own survey of its market, so the direction of the
figures is sounder than their level.

F6. **The counter-movement is real in advisory content but its
displacement of the classic form is contested and poorly measured.**
[contested; consultancy survey against dated trade press] Deloitte
(2 April 2026, survey of "more than 500 global business and
technology executives", year not stated) reports "67% of
organizations reported adopting outcome-based outsourcing models",
"from 45% to 67% in just two years"; the measure is organisations
that use the model somewhere, not share of spend or of contracts
[10]. Against it, CIO (2009): outcome-based contracts "at most 15
percent of new outsourcing deals", possibly covering only part of
the work, time-and-materials the most common model, and the named
difficulties - stakeholders with different goals, outcomes the
vendor cannot influence ("The supplier cannot influence things
beyond the supplier's realm of responsibility"), clients unwilling
to give up control [11]. The two measure different things seventeen
years apart; contradicted in level, not in direction. For agile
procurement in private enterprise the one institute source found
(WorldCC State of Agility) is members-only; its listing shows only
"90% see Agile as strategically vital" (2025 teaser) [12], which is
an attitude, not adoption.

F7. **Disconfirming result: detailed-requirements RFPs remain the
norm in practice; what is changing is the recommended content, not
the instrument.** [emerging, my reading of the sources, marked as
mine] The complaint is identical in 2009 ("Most RFPs are grossly
over-specified" [3]) and 2026 (a section titled "Why Solution-Driven
RFPs Persist" [4]); the buyer-advisory blueprint still structures a
seven-phase RFP with requirements and weighted criteria [2]; package
selection guidance still ends in a weighted requirement matrix [6];
and the vendor side answers a rising volume of RFPs [9]. Every
source that argues for outcomes argues for them inside an RFP, as
its content - problem, limits, scenarios - never as a replacement of
the RFP by a dialogue. The only "no RFP" alternatives met were Best
Value's two-page requirement [1], which is still a solicitation, and
the RFI-first step [2], which precedes the RFP rather than
replacing it.

F8. **The archetype distinction is supported for COTS/SaaS selection
and silent for the rest.** [single source for COTS; not found for
custom and SI] For a package: "still need to define the
requirements", but less detail than building from scratch; use
cases, business rules, data, quality attributes; gaps no candidate
meets "can add significant costs to the COTS implementation" [6].
[1]'s ERP example (10 sites, 3,500 staff, $5.5M budget as the whole
requirement) and [4]'s MES case are package selections too. No
opened source says what an RFP for a custom build or a systems
integration should carry, or whether the solution design belongs in
it; see Not found.

## Unexpected

The buyer's chain as a defence against capture, or as the thing the
vendor expects to shape: [8] names prior engagement during
requirements definition as the strongest predictor of a vendor's
win, and requirements in one vendor's terminology as the sign of a
written-for RFP. A chain composed before any vendor contact (intent,
assignment, BRD) is exactly what [8] says vendors try to get into;
whether that makes a derived RFP cleaner or less winnable for the
vendors a buyer wants is a lead, not a finding [8].

Regulated industries are pushing outcome-led requirements while
keeping the controls prescriptive: [4] (BioPhorum, nine authors,
May 2026) proposes "confidence that only appropriately authorized
personnel can perform GMP-critical activities" in place of an
operator-authorization step, and cites a Harvard Kennedy School RFP
guidebook (2021) and a 2023 Gartner commentary it does not quote.
The guidebook and the Gartner piece were not opened; they are leads
for the public-sector reference the card allows [4].

Price dominates where the literature says outcomes should: 67% of
vendors cite price as a top loss reason [9], and [8] names
price-dominated weighting as a red flag. Whatever an RFP says about
outcomes, the vendor experiences the evaluation as a price contest;
a derived RFP that discloses its weighting would be acting on this
[8][9].

A dated figure for the cost an RFP imposes on the market: vendors
budget 3-5% of anticipated contract value to respond, 23.8 hours of
writing per response (Info-Tech citing LinkedIn 2017 and
Marketingprofs 2021, both tertiary) [2]. Whether a short,
outcome-led RFP lowers that cost is nowhere measured.

## Not found

A benchmark of IT procurement or RFP failure and cancellation rates:
the McKinsey/Oxford study page timed out three times (two hosts), the
Standish CHAOS reports surfaced only as university-hosted copies and
a 2004 vendor page and were not opened; no RFP-specific cancellation
rate surfaced in any query. The figures the search engine's summary
gave for both (45% over budget, 56% less value; 31% cancelled) rest
on snippets and are not findings of this note.

A quantification of the risk premium ambiguity adds to a bid: looked
for under "risk premium", "contingency", "price to win"; the vendor
literature describes the mechanism [7] and the qualification gate
[8] but gives no percentage.

A source that distinguishes the RFP for custom development and for
systems integration from the one for COTS/SaaS selection: the
build-versus-buy results were a state-government guide, vendor
blogs and a forum thread; nothing above the bar was opened.

Evidence that outcome-based or agile procurement failed in private
enterprise: one academic case of a failed outcome-based fixed-price
outsourcing surfaced in a snippet (not opened, repository page); the
Fraunhofer paper on procurement in agile projects was blocked by
bot protection; WorldCC's agility reports are members-only [12].
The "marginal in private enterprise" half of the disconfirming query
therefore stands on [11] (2009) and on the inference in F7, not on
a current measurement.

Gartner and Forrester RFP research (use-case-based templates,
outcome-driven implementation RFP): paywalled abstracts only, not
opened.

## Options

1. A derived RFP that carries the problem and the limits, not the
   solution: the intent's objective and positions as the problem
   statement, the assignment's constraints, out-of-scope items and
   success criteria as the fixed limits [1], the BRD's use cases as
   the scenarios vendors must answer [3][5][6], and the solution
   design withheld. Fits COTS/SaaS and SI selection as the sources
   describe it; leaves a custom build under-specified for a vendor
   that must estimate.
2. The same RFP with the solution design included, as an execution
   tender for a custom build. No opened source supports or refutes
   it (F8); it is the second engine's premortem unverified.
3. A two-step derivation, RFI then RFP, with the RFI the chain's
   problem statement alone and the RFP written after the market has
   answered [2]. Costs a round; matches the one staged form the
   advisory literature actually recommends.
4. No RFP artefact: the chain is handed to a procurement function as
   it stands. Loses the one thing every source agrees the buyer must
   write deliberately, the scenarios and the disclosed criteria.

## Relevance to this project

My recommendation, marked as mine: whatever the forge derives, it
must derive the content the counter-movement prescribes - problem,
limits, scenarios, disclosed weighting - and must not derive a
checklist of the BRD's business rules or the solution design's
choices, because that is precisely the over-specified RFP every
source opened describes [1][2][3][4][5]. On the planner's premortem:
the evidence says the form is not leaving but the content is (F7);
an RFP artefact would not codify a dying form, but an artefact that
templated requirements as shall-statements would codify the failure
mode. On the second engine's premortem: the branch is supported for
COTS/SaaS (withhold the solution, let the vendor propose it, F8) and
unverified for custom builds; the forge should not decide that
branch from this note. Chosen against option 4 because the scenarios
and the criteria are buyer work no procurement function invents from
a chain, and against option 2 because nothing opened supports it.
Whether the result is an artefact or a render is cards 3 and 4's
question; this note only says what it must and must not contain.

Consult when: deciding what sections a derived RFP carries and which
chain items feed them; deciding whether the solution design enters
the RFP for a given archetype; drafting the evaluation criteria of
an RFP; judging a vendor's objection that an RFP is unanswerable.

## Sources

1. "Procurement tip: The Pitfalls of Overprescribing your RFP",
   Isaac Kashiwagi, PBSRG (Performance Based Studies Research Group,
   promoter of the Best Value Approach, which it trains and
   licenses); dated "08 Dec", year not shown, footer 2018, related
   posts 2024 (undated as to year). https://pbsrg.com/?p=19530
   Kind: primary (the group's own position) with a vendor interest.
   Read in full. Original.
2. "Drive Successful Sourcing Outcomes With a Robust RFP Process"
   (search title "create a better RFP process"), Donna Glidden and
   Steve Jeffery, Info-Tech Research Group; undated on page, its
   cited data 2017-2022 (undated).
   https://www.infotech.com/research/ss/create-a-better-rfp-process
   Kind: secondary (advisory blueprint; its figures cite Bonfire,
   Loopio, LinkedIn, Marketingprofs). Read partially: the public
   summary and Guided Implementation outline; the full blueprint is
   members-only. Original.
3. "Think Beyond the RFP", Kas Thomas, InformationWeek, 11 August
   2009 (byline); originally at E-TechnologyManagement.com.
   https://www.informationweek.com/it-sectors/think-beyond-the-rfp
   Kind: primary (practitioner account). Read in full. Copy of the
   author's own earlier post, as the page states.
4. "Why Your MES RFP Is Failing Before It Starts", nine BioPhorum
   members (Grossman, Berg, Clayton, Cook, Kaci, Farley, Wilson,
   Gunther, Agirtmis), Bioprocess Online guest column, 6 May 2026
   (byline); employers not disclosed.
   https://www.bioprocessonline.com/doc/why-your-mes-rfp-is-failing-before-it-starts-0001
   Kind: primary (industry consortium's position). Read in full;
   Table 1 not in the fetched text. Original (a sister site carries
   the same column).
5. "Technology Selection Quick Tip: Whatever you do, avoid check-box
   RFPs", Real Story Group (research and advisory firm selling
   member research and selection tools), 18 May 2016 (byline),
   author not named.
   https://my.realstorygroup.com/Blog/technology-selection-quick-tip-whatever-you-do-avoid-check-box-rfps
   Kind: secondary (analyst advice). Read in full. Original.
6. "How to Evaluate and Select the Right COTS Solution", Joy Beatty
   (ArgonDigital) with Karl Wiegers credited, ArgonDigital (a
   requirements and software-selection consultancy); undated on
   page, image path suggests February 2014 (undated).
   https://argondigital.com/blog/general/evaluating-candidate-cots-packages
   Kind: secondary (practitioner guidance). Read in full. Original.
7. "RFPs: The Costs of Being Unclear", Bart Perkins (managing
   partner, Leverage Partners), Computerworld opinion, 11 June 2007
   (byline).
   https://www.computerworld.com/article/1687682/rfps-the-costs-of-being-unclear.html
   Kind: primary (practitioner account). Read in full. Original.
8. "Qualifying RFPs Before You Bid", Mithun A. Sridharan (founder,
   Think Insights), 17 December 2025 (byline).
   https://thinkinsights.net/commercial-excellence/qualifying-rfps-you-bid
   Kind: primary (practitioner account); its Gartner and McKinsey
   figures are tertiary and not used. Read in full. Original.
9. "RFP Response Trends & Benchmarks, 2024 Report", Loopio in
   partnership with APMP; dated by its title and the PDF's InDesign
   stamp 2024-01-09 (structured data); survey of 1,650+ proposal
   professionals.
   https://link.loopio.com/hubfs/Content%20Pieces/Reports/2024%20RFP%20Trends%20&%20Benchmarks%20Report%20%7C%20Loopio%20(Digital%20Copy).pdf
   Kind: primary (the publisher's own survey; a vendor of RFP
   response software surveying its market). Read partially: the
   fetch returned the binary, the text was extracted locally from
   the fetched file with pdftotext and read in the Overview (pp.
   4-5), Chapter 1 (volume, participation, go/no-go) and Chapter 2
   (win rates, price as loss reason). Original.
10. "The power of a multidimensional workforce: Outsourcing for
    strategic advantage", Chris Coulston and Ajit Nema, Deloitte
    Global, 2 April 2026 (byline); draws on a Deloitte survey of
    500+ executives whose year the page does not state.
    https://www.deloitte.com/global/en/services/consulting/perspectives/the-power-multidimensional-workforce-outsourcing-strategic-advantage.html
    Kind: primary for its own survey figure (consultancy report).
    Read in full. Original.
11. "What Matters Most in Outsourcing: Outcomes vs. Tasks",
    Stephanie Overby, CIO, 11 November 2009 (byline).
    https://www.cio.com/article/280845/outsourcing-what-matters-most-in-outsourcing-outcomes-vs-tasks.html
    Kind: secondary (trade press quoting an independent consultant
    and Forrester). Read in full. Original (syndicated copies exist
    on Computerworld and Computerwoche).
12. "State of Agility in Procurement & Supply" listing, World
    Commerce & Contracting Knowledge Library; entries dated 21 May
    2024, 29 June 2025, 24 June 2026 (structured data).
    https://worldcc.com/Portals/IACCM/Reports/State-of-Agility-Procurement-Supply-2024.pdf
    Kind: primary publisher, but only the listing with teasers was
    served; the reports are members-only. Read partially: the
    listing's teaser lines. Original.
13. "Delivering large-scale IT projects on time, on budget, and on
    value", McKinsey with the BT Centre for Major Programme
    Management, Oxford; 2012 per search results.
    https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
    Kind: primary. Not opened: three fetches timed out (two on this
    host, one on the Brazilian mirror). Not cited for content.
14. "7 Red Flags in your RFP that Send Vendors the Wrong Signals",
    Procurious.
    https://www.procurious.com/procurement-news/7-red-flags-rfp-send-vendors-wrong-signals
    Kind: secondary. Not opened: the fetch returned the site name
    only. Not cited for content.
15. Fraunhofer publication on procurement in agile projects.
    https://publica.fraunhofer.de/handle/publica/394248
    Kind: primary (academic). Not opened: blocked by bot protection
    (Anubis). Not cited for content.

## Opened and not used

- [12] WorldCC listing: opened for the agility survey, served only
  teasers; used solely to record that the report is members-only.
- Loopio [9], chapters 3-7 (writing, team size, AI, career,
  resources): off the question, not read.
- Info-Tech [2], member-reported impact figures (9.2/10, $196,115
  saved): self-reported marketing, below the bar.
- Think Insights [8], the Gartner 2026 and McKinsey figures it
  cites: tertiary, not needed for the card.

## Search record

Queries, in order: IT RFP failure modes over-specified
requirements; outcome-based RFP software procurement; bid no-bid
decision ambiguous RFP risk premium vendor; agile procurement
software failed enterprise detailed requirements remain norm
(disconfirming, first wording); Standish Group CHAOS report large
software projects failure rate; McKinsey Oxford large IT projects
cost overrun study; outcome-based contracting IT services adoption
survey World Commerce Contracting; RFP red flags vendor should not
bid ambiguous requirements; Gartner RFP use cases instead of
requirements software selection; outcome-based contracts failure
evidence payment by results IT outsourcing (disconfirming); RFP
custom software development vs COTS SaaS selection; Loopio RFP
response trends benchmark; Deloitte global outsourcing survey
outcome-based contracts percentage; the same limited to
deloitte.com; enterprise software buyers still use RFP detailed
requirements survey 2025 (disconfirming); agile procurement private
sector adoption low survey CIPS (disconfirming). Sixteen queries.

Openings: seventeen fetch attempts on fifteen URLs; twelve returned
readable content (one of them, the Loopio PDF, read through local
text extraction of the fetched file), three failed (McKinsey, three
timeouts on two hosts; Procurious, empty; Fraunhofer, blocked), one
served a listing in place of the report (WorldCC).

The disconfirming query found: no source saying outcome-based or
agile procurement failed in private enterprise that could be opened;
one dated trade-press figure for its marginality [11]; and indirect
but consistent evidence that detailed-requirements RFPs remain the
norm (the unchanged complaint 2009-2026 [3][4], rising RFP volume
[9], advisory and selection guidance still built on weighted
requirements [2][6]).

The run ended on the opening budget: seventeen attempts spent, with
the architect's perspective holding primaries [1][3][4] and the
vendor's [7][8][9]; the last two disconfirming queries brought
nothing openable that had not been seen.
