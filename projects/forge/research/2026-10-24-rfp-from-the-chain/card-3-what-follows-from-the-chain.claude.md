---
date: 2026-10-24
project: forge
topic: what of an RFP follows from the chain and what a person must add, by archetype
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-24-rfp-from-the-chain/card-3-what-follows-from-the-chain
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-3-what-follows-from-the-chain; web sources below
---

# The requirements of an RFP follow from the chain; its gates, tiers, weights and terms are supplied by people, and the solution design belongs in it only for a custom build

## In short

The practitioner literature agrees, without a controlled study
behind it, that the requirements core of an IT RFP is what the
buyer's own analysis produces beforehand: the problem and its
outcomes, functional and performance requirements, scope and
constraints. That part maps section by section onto the intent, the
assignment and the BRD, and it is substantial: an advisory firm
treats "Define Business Requirements" as the phase that feeds the
RFP, and a procurement officer names functional and performance
requirements as the two kinds that should dominate. What people must
add is equally clear and consistently listed: legal, commercial,
security, risk and vendor-management requirements, the tiering of
requirements into mandatory pass/fail gates and rated items, the
evaluation weights, the standard contract, and the regulatory gates,
which for a financial entity in the EU are enumerated in DORA
Article 30 and for product security in a government buyer's guide.
On the archetype the sources are one-sided for SaaS/COTS: specify the
problem, functions and performance, not the technical "how", because
a prescriptive design narrows the field and the vendor's design is
part of what is bought; the solution design is the winner's to
produce, with only justified constraints from it (integration, data,
security) surviving as technical requirements. For a custom build no
primary source was found; practitioners in a single thread say the
same business requirements are needed and that "shall" statements
and use cases fit a build, and vendor blogs (not opened) say a
detailed design makes bidders price a specification rather than
propose a solution. The disconfirming query found no evidence that
enterprise RFPs reject pre-specified designs outright, only the
softer, well-attested form: every technical requirement should be
asked "why", and mandatory ones kept few. Unexpected: an RFP wants a
different requirement style from the chain's (capabilities, not
"the system shall"; use cases score badly), and a 2024 Gartner
survey reported by trade press says the classic RFP is now the
minority route for technology purchases, so an "RFP artefact" would
codify one route of several.

## Question

#### Card 3: what of an RFP follows from the chain and what a person must add, by archetype
- **Question:** Section by section, what an intent (background,
  objectives, positions), an assignment (scope, out of scope,
  constraints, deliverables, success criteria), a BRD (business
  requirements, use cases, non-functional requirements,
  dependencies) and a solution design (target architecture,
  integration constraints) can supply to an RFP, and what is always
  supplied by people: budget, timeline, commercial terms, evaluation
  weights, legal terms, vendor qualification, confidentiality, and
  the regulatory and contractual gates (data protection, sector
  resilience rules, IP, liability, security attestations); and, by
  archetype, whether a solution design belongs in the RFP at all:
  for a SaaS/COTS selection, does embedding the buyer's design
  over-constrain the market so that the design is the winner's to
  produce, and for a custom build does the RFP with a design become
  an execution tender; against the alternative that enterprise IT
  RFPs reject pre-specified solution designs because they prevent
  vendors from proposing their own architectures.
- **Why it matters:** The principal's central question, and the one
  that decides whether the RFP is an artefact with thinking of its
  own or a generated document from the artefacts above it; the
  second engine's premortem (the relation is branching, not linear,
  and depends on make-or-buy) is answered here.
- **What would answer it:** Requirements-to-RFP guidance of IT
  advisory firms and procurement practice (traceability matrices,
  section-by-section guidance on what the buyer specifies and what
  it leaves to bidders); the standards (ISO/IEC/IEEE 29148 on the
  acquisition process and the acquirer's request, BABOK's vendor
  assessment) only as the frame.
- **Where to look:** IT advisory firms' requirements-to-RFP and
  vendor selection guidance (Info-Tech Research Group, Gartner,
  Forrester), procurement institutes, practitioner guidance on
  specifying for COTS against custom, requirements-engineering
  bodies for the frame; more than one route. Known items: a
  practitioner requirements-to-RFP traceability matrix from an
  advisory firm; what 29148 says the acquirer's request contains;
  guidance on how much solution to specify in a COTS/SaaS RFP.
- **Disconfirming query:** Expected: the requirements part of an RFP
  is derivable and substantial, and the solution design's place
  depends on the archetype. Search for the opposite: evidence that
  enterprise IT RFPs reject pre-specified solution designs outright
  because they prevent vendors from proposing COTS architectures,
  and that the derivable part is small.
- **Stop rule:** Nothing new from a differently-worded query, and
  each perspective of the card (requirements engineer, evaluator,
  security and compliance as what a person supplies) has a primary
  source; or about fifteen openings spent.

The baseline the note must beat is the principal's hypothesis as it
stands: that the RFP is a further artefact of the chain, and the
plain intuition behind it, that an RFP is "the requirements plus
some commercial boilerplate". The note beats it if it can say, from
sources, which sections are a transformation of what the chain
holds, which are decisions nobody upstream has taken, and whether
the solution design's place is one rule or two.

## Key findings

**F1. The requirements core of an IT RFP is produced before the RFP
and is what the buyer's analysis supplies; it is the bulk of the
preparatory work, not a small part.** [consensus; practitioner
claim, advisory-firm method] Info-Tech's RFP method puts "Define
Business Requirements" as the phase before "Perform RFI/RFP", with
the outcome "A detailed list of required business, technical, legal
and procurement requirements", and warns that "Defining requirements
can't be rushed or you'll find yourself answering many questions"
and that vendors "are choosing to not respond to RFPs due to their
length and lack of complete requirements" [1]. A former state
procurement director distinguishes three kinds of requirement,
functional ("what the system does"), performance ("how well it does
it") and technical ("how it is built"), and wants the first two to
carry the RFP [2]. Mapped onto the chain (the mapping is the
agent's own inference, not a source's): the intent supplies the
background, the problem statement and the objectives (Info-Tech's
"What do you want the end result to look like?" [1]); the assignment
supplies scope and out of scope, constraints (which become
mandatory requirements, F3), deliverables (the core of a statement
of work) and success criteria (acceptance and performance
requirements); the BRD supplies the functional requirements, the
scenarios behind them, the non-functional requirements as
performance requirements, and the dependencies as integration and
interface requirements; the solution design supplies technical
requirements and constraints, whose place depends on the archetype
(F4, F5). For a COTS/SaaS purchase the business-analysis side adds
that what must be specified is the business process and the data
(data dictionaries, field mapping for migration and integration),
not the standard built-in functions [8].

**F2. A fixed set of RFP content is always supplied by people and
has no upstream source in a requirements chain: the legal,
commercial, security, risk and vendor-management requirements, the
standard contract, the evaluation process and its weights, and the
proposal instructions.** [consensus; practitioner claim and
procurement-body guidance] Info-Tech's "Your Challenge" is that many
RFPs lack requirements "from across the business (Legal, Finance,
Security, Risk, Procurement, VMO)"; its requirement categories are
"Risk, Legal, Support, Security, Technical, Commercial, Operational,
and Vendor Management Governance"; it asks "Do you have a standard
contract that can be included or do you want to review the vendor's
contract?", tells the drafter to "Consider the RFP Evaluation
Process as you draft the RFP, including weighting the RFP
components", and to "Provide strict, prescriptive instructions
detailing how the vendor should submit their responses" [1]. The
evaluator's mechanics are a procurement body's: mandatory criteria
"are evaluated on a pass/fail basis", failing bids "are given no
further consideration", point-rated criteria measure relative merit
on a stated marking scale, and "a specific pass mark can be set in
order for a bid to be considered responsive" [4]. None of these is a
restatement of a requirement; each is a decision of the buyer's
organisation. Budget, timeline and confidentiality were not
separately sourced (see Not found); the sources treat them as part
of the commercial and procurement items above.

**F3. Mandatory requirements are a disqualifying gate, every
"shall" is read as mandatory, and mandatory requirements should be
few; so the tiering of requirements is a decision a person takes,
not a property the chain carries.** [consensus; practitioner claim,
procurement-body guidance] Info-Tech has the drafter sort
requirements into "absolute", "bargaining", "concession" and
"dropped/out of scope", and keep absolute ones to a minimum because
vendors that miss them are removed [1]. Kim warns against "treating
preferences as hard requirements", which disadvantages COTS
platforms, and wants subject-matter experts to say which functions
are critical for Day 1 and which "nice to have" [2]. A business
architect states that in an RFP "will", "shall" and "must" all mean
mandatory, so "The system shall…." becomes a mandatory capability;
mandatory items are scored pass or fail, desirable ones weighted,
and groups with minimum scores identify well-rounded solutions [3].
The Canadian guidance confirms the two-stage mechanics [4]. The
consequence for the chain (the agent's inference): an assignment
written throughout in "shall" would, transplanted, make every item a
disqualifier; someone must decide which of the chain's items are
absolute and which are rated, and that decision has no upstream
owner.

**F4. For a SaaS/COTS selection the sources are one-sided: specify
the problem, the functions and the performance, not the technical
design; a prescribed design narrows the field and the vendor's
design is part of what is bought. Justified constraints from the
design survive as technical requirements.** [consensus among
practitioners; no controlled study; one survey reported second-hand]
Info-Tech quotes "IT RFPs should specify the problem to be resolved
rather than the solution to be provided" and "If the problem
resolution is the goal, vendors are free to implement the latest
technologies to meet that need" [1]. Kim: RFPs that lean on
"pages of requirements specifying software the bidder must use"
crowd out functional and performance requirements; "Focusing more on
what we need and less on how to build it", and for every technical
specification keep asking "why they are necessary before including
them" [2]. Lambert: requirements for a commercial product should be
"'informative' rather than 'prescriptive'", written to compare
products, not to design a system; Goldsmith in the same thread: the
vendor's design is part of the value of an acquisition, so the RFP
should identify the "whats" rather than impose a design [3].
Gartner's Finkeldey, as reported: traditional RFPs "often begin with
predefined solutions" and "risk locking organisations into outdated
approaches that fail to address evolving needs" [6]. None of the
sources says to drop technical requirements altogether; Kim's test
is justification, and Brandenburg's COTS guidance keeps data
migration and integration as areas that must be specified [8]. The
agent's reading: for this archetype the solution design is not an
RFP input but the winner's deliverable, and what the chain's design
contributes is a short list of constraints (integration standards,
data residency, identity, security) each with its reason.

**F5. For a custom build the evidence is thin and partly
conflicting: the same business requirements are needed, "shall"
statements and use cases are acceptable there, and whether a
detailed design belongs in the RFP depends on the pricing model
wanted.** [contested; single thread of practitioner claims; vendor
blogs seen only as search results] Lambert: "shall" phrasing is
acceptable for custom builds but works poorly in procurement; use
cases suit custom builds but are hard for vendors to answer and for
evaluators to score; Goldsmith: the same "REAL business
requirements need to be defined for projects that develop a custom
system", and decomposing them in detail does not turn them into
system requirements [3]. No opened source states that an RFP with a
design "becomes an execution tender". The search results that said
the nearest thing were vendor and agency blogs not opened (a
specified stack and architecture give bidders "a specification to
price" rather than something to propose; fixed-price bids on an
RFP without design detail are padded for risk; where specifications
are unfinished the statement of work should fund discovery and
design first), and the two-stage tender pattern surfaced only from
construction-industry sources, also not opened. Treat F5 as a
reading of the card's second branch that the run could not source
to a primary; see Not found.

**F6. Regulatory and contractual gates are enumerated conditions,
supplied by the compliance and legal side and put to bidders as
pass/fail; part of their content overlaps with what the chain
holds.** [primary, regulation text as a documentation copy;
primary, government buyer's guide] DORA Article 30(2) requires every
ICT services contract of a financial entity to contain, among other
things, "a clear and complete description of all functions and ICT
services to be provided", "the locations, namely the regions or
countries, where the contracted or subcontracted functions" are
provided, "provisions on availability, authenticity, integrity and
confidentiality in relation to the protection of data", "provisions
on ensuring access, recovery and return in an easily accessible
format of personal and non-personal data", "service level
descriptions", assistance "at no additional cost" on incidents,
cooperation with authorities, "termination rights and related
minimum notice periods", and participation in security training;
Article 30(3) adds for critical or important functions "full service
level descriptions ... with precise quantitative" targets, reporting
obligations, tested contingency plans, participation in TLPT, "the
right to monitor, on an ongoing basis", and "exit strategies, in
particular the establishment of a mandatory adequate transition
period" [7]. CISA's Secure by Demand guide gives the buyer's product
security questions and the evidence to demand (a machine-readable
SBOM, a public vulnerability disclosure policy, MFA and SSO at no
extra cost, security logs retained, a roadmap for eliminating
vulnerability classes) and places them "before procurement" as
questions and "during procurement" as contract language [5]. The
agent's reading: items (a) and (e) of Article 30(2) and the service
levels of 30(3)(a) are the one place where a gate's content is
derivable, from the assignment's deliverables and the BRD's
non-functional requirements; the rest is the compliance function's
and the lawyer's.

**F7. The classic monolithic RFP is receding as the route of a
technology purchase; agile or lean buying and panels or marketplaces
are reported as more frequent.** [emerging; one vendor-independent
survey reported by trade press, the report itself paywalled] Gartner
surveyed 1,135 senior technology buyers; globally "the traditional
RFP is becoming less common than expected" and agile or lean
methods are the most frequent approach; in Australia 40 per cent of
purchases followed agile or lean methods, 12 per cent a traditional
RFP or RFQ and 26 per cent panels or marketplaces [6]. Against this,
a January 2026 opinion by a former state procurement director still
treats the RFP as the standard instrument to be written better [2],
and an advisory firm still sells four RFP templates [1]; the trend
is reported, not settled.

**F8. The disconfirming query found no evidence that enterprise IT
RFPs reject pre-specified solution designs outright, and no evidence
that the derivable part is small.** [the disconfirming result;
absence of evidence after two differently worded queries] Queries
for RFPs that excluded or declined bidders over a pre-specified
design returned US federal bid-protest decisions (not opened, public
procurement law being out of the research's scope) whose snippets
describe RFPs that left architecture to offerors while evaluating it
and one that required COTS components; one COTS vendor's blog
arguing that prescriptive RFPs force it to decline was unreachable.
What the opened sources support is the softer form in F4: justify
every technical requirement and keep mandatory ones few. On the size
of the derivable part, the only sources that speak of it make
requirements definition the longest and most neglected phase [1][2].

## Unexpected

The RFP wants a different requirement style from the chain's. In an
RFP every "shall", "will" and "must" is read as mandatory, "The
system shall…." statements become disqualifiers, and use cases are
"hard for vendors to answer and for evaluators to score"; the
recommended form is a capability statement, comparable across
products, with mandatory and desirable marked [3]. The card assumes
the BRD's items can be carried into the RFP; [3] says they must be
re-cast on the way, which is a transformation with rules of its own,
not a copy. Lead with provenance in one practitioner thread.

What people supply is written in the same form as what the chain
supplies. Info-Tech's requirement categories list Legal, Commercial,
Risk and Vendor Management Governance beside Technical and
Operational [1]: the RFP's requirements section is one merged list,
in which the derived and the human-supplied items are
indistinguishable to the bidder. Where the forge draws its boundary
would therefore be invisible in the output and would have to be
held in provenance.

The RFP may be the minority route. If Gartner's survey holds beyond
Australia [6], a project that reaches the point of asking the market
is more likely to run an agile or lean dialogue or buy from a panel
than to issue an RFP; the chain's derivable content would be needed
in any of these routes, under another name (a request for solution,
an outcome brief). Lead, from a single survey reported second-hand.

Two of the regulatory gate's items are derivable. DORA Article
30(2)(a) and (e) and 30(3)(a) ask for the description of functions
and services and the service levels with quantitative targets [7],
which an assignment's deliverables and a BRD's non-functional
requirements already hold. The gate is not wholly outside the chain.

Product-security questions are project-independent. CISA's list
(SBOM, disclosure policy, MFA, SSO, logs) is the same for every
software purchase [5]; the agent's inference is that such a list
belongs with the instance's reusable material, not with one
project's chain.

## Not found

- No reliable primary source on what ISO/IEC/IEEE 29148:2018 says
  the acquirer's request contains. The standard is paywalled; the
  publisher's preview PDF was fetched but arrived as unreadable
  binary, and the search results give only the scope statement.
  The frame the card wanted from 29148 is unsourced in this note.
- No source found on BABOK's vendor assessment technique beyond
  procurement-vendor blogs (not opened); the BABOK text was not
  reachable.
- No primary source for the custom-build archetype (the second
  branch of the card): nothing opened says that an RFP carrying a
  solution design becomes an execution tender, or how much design a
  custom-build RFP should hold. The only material was vendor blogs
  and a construction-industry pattern, seen in search results only.
- No requirements-to-RFP traceability matrix from an advisory firm
  was opened; the search returned a US state agency's business
  requirements matrix (a .docx, not opened) and vendor-side
  compliance-matrix guides, which are the vendor's instrument, not
  the buyer's.
- Budget, timeline and confidentiality as RFP sections were not
  separately sourced; the opened sources fold them into commercial
  and procurement items without naming them.
- No source on IP and liability terms as RFP conditions in a private
  company group; the one regulation reached is sector-specific
  (financial entities) and the GDPR processor terms (Article 28)
  were not opened.
- The Virginia IT agency's "solution-based RFP" guidance, named in
  the search results as the one procurement manual with a section on
  the archetype, returned 404 on three URLs.
- Gartner's own report behind the survey of F7 was not opened
  (paywalled abstract); the global percentages are not in the note.

## Options

1. The RFP as a render of the chain, with a human-supplied source.
   The chain's sections render into the requirements core (F1); the
   legal, commercial, security and evaluation content (F2, F6) comes
   from a source file people write; the recipe translates the
   requirement style (Unexpected, first lead). Trade-off: tiering
   (F3), weights (F2) and the archetype decision (F4, F5) are
   decisions with reasons and no record; a render has no history of
   its own and nothing in the chain owns them.
2. The RFP as an artefact of the chain with thinking of its own:
   the tiering of every item, the weights, the archetype and what of
   the design survives as a constraint, the gates and who supplies
   them, each with its reason and history. Trade-off: it duplicates
   the chain's content in a second versioned place, which the forge
   forbids (CLAUDE.md, prime directive 10), unless the artefact holds
   only the decisions and cites the items.
3. A thin artefact of sourcing decisions plus a render. The artefact
   holds what no upstream layer owns: archetype, tier per item,
   weights, gates and their suppliers, the pricing model wanted (F5),
   with history; the render composes the RFP from the chain, that
   artefact and the human-supplied terms. Trade-off: one more layer
   and a definition to write; the content stays in one place each.

## Relevance to this project

The agent's recommendation is option 3, chosen against option 1
because the sources are unanimous that the RFP contains decisions
with consequences, which items disqualify, how the rest is weighed,
whether the design is asked for or left to the bidder (F2, F3, F4),
and a render cannot carry a decision with its reason and history;
and against option 2 because the requirements content already lives
in the chain and would be duplicated. So the principal's hypothesis
holds in a narrow form: there is an artefact's worth of thinking
between the chain and the RFP, but it is thin and it is about the
sourcing, not about the requirements; the RFP document itself is
generated. On the archetype the sources answer the SaaS/COTS branch
plainly (the design is the winner's, constraints from it survive if
justified, F4) and leave the custom-build branch unsourced (F5); the
second engine's premortem, that the relation branches on
make-or-buy, is supported for one branch and open for the other.
Three inferences are the agent's own and marked so above: the
section-by-section mapping in F1, the reading that the assignment's
"shall" items would all become disqualifiers if transplanted (F3),
and that the product-security list belongs to reusable material
rather than a project (Unexpected).

Consult when: deciding whether the RFP is a layer, a render or both
(Options); defining what a sourcing-decision artefact must hold (F2,
F3, F6); writing the recipe's style translation from the chain's
"shall" and use cases to RFP capabilities (Unexpected, first lead);
choosing how much of a solution design enters a SaaS/COTS RFP (F4);
listing the gates a compliance or legal function must supply, in a
financial entity especially (F6); and before investing in an RFP
route at all, given F7.

## Sources

1. "Drive Successful Sourcing Outcomes With a Robust RFP Process",
   Info-Tech Research Group (Donna Glidden, Steve Jeffery;
   contributor George Bordon). Undated (no date on the page; it
   quotes a 2019 source). https://www.infotech.com/research/ss/drive-successful-sourcing-outcomes-with-a-robust-rfp-process
   Kind: secondary (advisory firm's method page). How read:
   partially, the visible excerpt of a members-only blueprint
   (executive summary, phases, "Define RFP Requirements", insights);
   the templates themselves are gated. Original; the one quote
   "IT RFPs should specify the problem..." is the page's quotation of
   Bonfire, 2019, a copy within the source.
2. "Measure Twice, Cut Once: A Smarter Approach to Writing RFPs",
   Daniel C. Kim, GovTech Opinion. 30 January 2026, by byline.
   https://www.govtech.com/opinion/measure-twice-cut-once-a-smarter-approach-to-writing-rfps
   Kind: secondary (practitioner opinion by a former state
   procurement director, now at a procurement consultancy). How
   read: in full. Original.
3. "Would you define or document requirements differently when the
   intent is to acquire a commercial off-the-shelf (COTS) product
   rather than build a custom-developed solution?", question by
   Chris Adams, answer by Sandy Lambert, comments by Robin Goldsmith,
   Modern Analyst. Dated by the comment thread, February 2014; the
   answer itself undated.
   https://modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/2880/Would-you-define-or-document-requirements-differently-when-the-intent-is-to-acquire-a-commercial-off-the-shelf-COTS-product-rather-than-build-a-custom-developed-solution.aspx
   Kind: secondary (practitioner claims, two authors disagreeing in
   part). How read: in full. Original.
4. "Evaluation Criteria", Treasury Board of Canada Secretariat,
   Professional Audit Support Services. Page details 2009-12-15
   (structured data, not labelled as modified). https://www.canada.ca/en/treasury-board-secretariat/corporate/organization/professional-audit-support-services/evaluation-criteria.html
   Kind: primary (a procurement body's own evaluation guidance; used
   for the mechanics of mandatory and rated criteria, not for public
   procurement law). How read: in full. Original.
5. "Secure by Demand Guide: How Software Customers Can Drive a
   Secure Technology Ecosystem", Cybersecurity and Infrastructure
   Security Agency (CISA) with FBI. August 2024, inferred from file
   paths on the page (no date shown). https://www.cisa.gov/resources-tools/resources/secure-demand-guide
   Kind: primary (government buyer's guidance). How read: in full
   (the landing page with the guide's questions; the PDF not
   separately opened). Original.
6. "Tech projects to move away from traditional RFP and RFT", Lilia
   Guan, ARN. 2 December 2024, by byline. https://www.arnnet.com.au/?p=3615211
   Kind: secondary (trade press reporting a Gartner survey and
   quoting Derry Finkeldey; the Gartner report is paywalled and not
   opened). How read: in full. Original article; a report of
   someone else's result.
7. "Article 30, Key contractual provisions", Regulation (EU)
   2022/2554 (DORA), as reproduced by Springlex (Springflod AB, a
   Swedish financial-services cybersecurity consultancy), which
   states the text "has no legal effect" and the authentic version
   is the Official Journal's. Regulation of 14 December 2022; the
   page undated. https://www.springlex.eu/packages/dora/dora-regulation/article-30/?ref=dora-info
   Kind: primary text in a documentation copy. How read: in full for
   Article 30. Copy of the Official Journal text; the EUR-Lex
   original was fetched and returned empty (see Opened and not
   used).
8. "What Requirements to Specify for COTS and SaaS Projects", Laura
   Brandenburg, Bridging the Gap. Undated (comments 2010 to 2013,
   footer copyright 2026). https://www.bridging-the-gap.com/vendor-selection-best-practices-interview-with-susan-penny-brown/
   Kind: secondary (practitioner claim). How read: in full. Original.
   Used only for what a COTS requirements set must cover; it does
   not mention RFPs.

## Opened and not used

- https://www.vita.virginia.gov/procurement/buy-it-manual/chapter-24---requests-for-proposals-and-competitive-negotiations/2421-solution-based-rfps.html
  — 404; the search result named it as the one manual section on
  solution-based RFPs. Not opened.
- https://www.vita.virginia.gov/procurement/buy-it-manual/chapter-24---requests-for-proposals-and-competitive-negotiations
  — 404. Not opened.
- https://www.vita.virginia.gov/procurement/buy-it-manual/chapter-24---requests-for-proposals-and-competitive-negotiations/24512-completing-the-rfp-package.html
  — 404. Not opened.
- https://assets.vde-verlag.de/iec-normen/preview-pdf/info_isoiecieee29148%7Bed2.0%7Den.pdf
  — ISO/IEC/IEEE 29148:2018 preview; fetched as unreadable binary
  (no text layer extractable with the tools at hand). Not read.
- https://www.nigp.org/resource/global-best-practices/request-for-proposals-global-best-practice.pdf?dl=true
  — NIGP "Request for Proposals" global best practice; fetched as
  unreadable binary. Not read.
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554
  — the authentic DORA text; the fetch returned an empty page.
  Replaced by the copy [7].
- https://cm.twobirds.com/en/insights/2024/global/dora-some-insights-on-contractual-clauses-in-agreements-between-financial-entities
  — law-firm commentary on Article 30; 403. Not opened.
- https://knowledgeonecorp.com/blog/?tag=%2FRFP
  — a COTS vendor's blog "What is a 'Prescriptive' RFQ/RFP and why
  is it bad?", the strongest voice for the disconfirming side; 404,
  and a vendor's blog on its own market in any case. Not opened.
- https://www.dora-info.eu/dora/article-30/ — redirected to [7];
  no content of its own.

## Search record

Queries run, in order: requirements to RFP traceability matrix
vendor selection IT; ISO/IEC/IEEE 29148 acquisition request for
proposal acquirer requirements specification; COTS SaaS RFP how much
solution to specify, over-specification, vendors propose own
architecture; Info-Tech Research Group RFP template vendor selection
requirements; BABOK vendor assessment RFP RFI RFQ; Gartner RFP SaaS
selection requirements, vendors should propose; RFP security
questionnaire SOC 2 ISO 27001 mandatory, disqualify before scoring;
enterprise RFP should not prescribe solution design, custom vs COTS;
ISO/IEC/IEEE 29148:2018 acquisition process "request for proposal"
StRS contents; DORA Article 30 key contractual provisions;
outcome-based RFP, agile procurement replacing traditional RFP 2025;
RFP evaluation criteria weighting set before issue, pass/fail vs
scored; custom software development RFP fixed price, detailed
specification, statement of work, estimate ambiguity; Gartner
Finkeldey traditional RFP less common survey; RFP detailed
architecture excluded COTS vendors, pre-specified design rejected
(the disconfirming query); systems integration RFP design then
build, two-stage tender; VITA Virginia BUY IT manual
"solution-based" RFP.

Openings (fetches of a page), seventeen attempted, eight readable:
Info-Tech [1], GovTech [2], Bridging the Gap [8], Modern Analyst
[3], VITA 24.2.1 (404), 29148 preview (binary), Treasury Board of
Canada [4], EUR-Lex DORA (empty), CISA [5], NIGP PDF (binary), Bird
& Bird (403), ARN [6], KnowledgeOne (404), VITA chapter 24 (404),
dora-info (redirect), Springlex DORA Article 30 [7], VITA 24.5.1.2
(404).

The run ended on the opening budget: seventeen openings attempted
against a budget of about fifteen, nine of them lost to unreachable
or unreadable pages. The last two differently worded queries (the
disconfirming query and the two-stage tender query) brought nothing
new that could be opened, which satisfies the first part of the stop
rule; the second part is not satisfied, since the custom-build
archetype and the 29148 frame have no primary source in this note,
and the evaluator's and the compliance perspectives rest on
public-body guidance and a regulation copy rather than on a private
group's practice.
