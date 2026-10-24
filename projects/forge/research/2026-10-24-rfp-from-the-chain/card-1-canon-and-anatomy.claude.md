---
date: 2026-10-24
project: forge
topic: canon, vocabulary and anatomy of the IT RFP of a private company
status: immutable
engine: claude
model: the session model
usage: —
run: tmp/research/2026-10-24-rfp-from-the-chain/card-1-canon-and-anatomy
derived_from: the plan research/2026-10-24-rfp-from-the-chain/00-plan.md, card-1-canon-and-anatomy; web sources below
---

# The IT RFP of a private company has a recognisable canon and a settled four-part skeleton; its IT substance is category work layered on a generic shell

## In short

There is a canon. A procurement institute (CIPS) publishes an RFP
template with guidance notes dated January 2025 and a position on
tendering and post-tender negotiation; an analyst firm (Info-Tech
Research Group) publishes a generic RFP template, category RFP
templates and the surrounding instruments (RFI, RFQ, vendor response
template, evaluation tool); Forrester publishes an enterprise software
RFP template behind its paywall. The vocabulary is shared: RFI (or
EOI) before, RFP where the need is not fully defined, RFT/ITT/ITB
where it is, RFQ where price decides, a proposal that is not a binding
offer, post-tender negotiation and best and final offers, a statement
of work carried from the RFP into the contract. The skeleton is
settled and the same in all three routes opened: instructions and
conditions (with evaluation criteria and weights), the requirement
(scope of work or specification), the information to be provided by
proposers (pricing, non-price commercial, technical), the proposed
contract, and appendices that carry the terms, the technical
specifications and the response template. The sections the card
expected are all there; the order differs from the card's, with
instructions and evaluation first and the contract last. This is
consensus across the sources opened. The disconfirming query found
nobody saying there is no shared vocabulary or skeleton; it did find
that the institute's template is generic in exactly the part where
the IT content lives (the requirement), that the analysts fill that
part per category, and that the "one document" is in truth one
package of several instruments with a core document, so the card's
dichotomy is false on both sides. The archetype split is only half
supported: product selection (requirements questionnaire) against
services and implementation partner (statement of work, roles,
milestones) is in the sources; custom development as a third
archetype of its own was not found in any primary. The one unexpected
thing: the institute's template says the requirement part and much of
the response "is intended to form part of the final Contract", which
makes whatever the chain supplies to an RFP contract text.

## Question

#### Card 1: canon, vocabulary and anatomy of the IT RFP of a private company
- **Question:** Who is authoritative on IT procurement documents in
  private companies (procurement institutes, analyst firms,
  consultancies and integrators, requirements-engineering standards),
  what the vocabulary is (RFI, RFP, RFQ, SOW, compliance matrix,
  evaluation matrix, BAFO, and their relations), which sections an IT
  RFP has and in what order (background and objectives, scope and
  statement of work, functional and non-functional requirements,
  deliverables, timeline, evaluation criteria and weights, submission
  rules, commercial and legal terms, vendor qualification, response
  instruments), and what a reference template looks like,
  distinguishing the archetypes SaaS/COTS selection, custom
  development and systems integration; against the alternative that
  IT procurement has fractured into category-specific packages with
  no shared vocabulary and that the monolithic document has been
  replaced by modular packages (commercial terms, security schedule,
  technical requirements, response workbook).
- **Why it matters:** The skeleton any artefact or render of the
  framework must produce, and the words the other cards must use; a
  card written in the wrong vocabulary finds the wrong literature.
- **What would answer it:** The field's own guidance, glossaries and
  templates: procurement institutes' publications, analyst toolkits
  for the IT category, consultancies' and integrators' published
  guidance; software vendors' template libraries only as vendor
  claims.
- **Where to look:** procurement institutes (CIPS, ISM), analyst
  firms' IT procurement toolkits (Gartner, Forrester, Info-Tech
  Research Group), consultancies' and system integrators' guidance,
  well-regarded practitioner books, ISO/IEC/IEEE 29148 and BABOK only
  for the vocabulary of acquisition; more than one route. Known items
  that must turn up: an IT procurement category toolkit of a
  procurement institute or an analyst firm; a template with
  evaluation criteria and weights; a vendor response matrix or
  functional compliance schedule.
- **Disconfirming query:** Expected: a recognisable canon and a
  settled skeleton per archetype. Search for the opposite: that
  practitioners say there is no shared vocabulary or skeleton for IT,
  that templates are generic and the IT-specific content is left to
  the writer, and that modern IT procurement issues modular packages
  instead of one document.
- **Stop rule:** Nothing new from a differently-worded query, and
  each perspective of the card (procurement officer, architect) has a
  primary source; or about fifteen openings spent.

The baseline the note must beat is the generic skeleton any
procurement blog gives: overview, requirements, pricing, evaluation,
terms, submission. The note beats it if it names who publishes the
reference template, shows the skeleton and its order from the
publisher's own text, locates the evaluation weights and the response
instrument in it, says where the IT content enters and who supplies
it, and reports what the disconfirming query did to the picture.

## Key findings

**F1. The procurement-institute canon exists and is current: CIPS
publishes an RFP template with guidance notes dated January 2025 and
a position on tendering and post-tender negotiation.** (consensus on
existence; single source for the institute's wording; evidence: the
institute's own publications) The guidance notes define the
instrument: "A Request for Proposal (RFP) is a document issued by an
organisation to gather proposals or offers from suppliers for goods
or services" (Overview, p. 4) and present the template as "a solid
framework to handle commercial risks and issues in typical sourcing
situations" that "should be adjusted to fit the organisation's
specific needs" (Overview) [1]. The 2013 position says CIPS considers
tendering "most appropriate for high value and high risk purchases
and where transparency is paramount" (Background, p. 1) [2]. Both
documents are hosted on a content-management asset host, not on
cips.org; the attribution rests on the documents' own text and
copyright lines and on the same host serving several CIPS Knowledge
assets, and no cips.org page surfaced in search (Not found). ISM
surfaced nowhere (Not found).

**F2. The analyst route confirms the canon with a family of
instruments: Info-Tech Research Group publishes a generic RFP
template, category RFP templates and the instruments around them.**
(consensus between institute and analyst; evidence: the analyst's
public template pages, read through a summarising fetch; the
templates themselves are member-only) The generic template has
eleven sections: "Overview", "RFP Process and Conditions", "Proponent
Evaluation Process", "Proponent Background", "Proponent Business
Processes", "Technical Environment", "Required Products and Services",
"Pricing", "Respondent Response Requirements", "Legal Requirements",
"List of Schedules" [3]. Beside it the page names a Request for
Information Template, a Request for Quotation Template, a Vendor
Response Template, a Scenario Template and a Proposal Receipt
Template [3]; the vendor response template has nine sections ending
in "Requirements" [4]; a category template (IT asset management)
carries "The Statement of Work", "Proposal Preparation Instructions",
"Scope of Work", "Specifications and Requirements", "Vendor
Qualifications and References", "Budget and Estimated Pricing",
"Vendor Certification" [5]; an implementation-partner blueprint ends
in "Short-Form, Long-Form, and Lean RFP templates, Supplementary RFx
Material, and the RFx Vendor Evaluation Tool" [6][7]. Forrester's
Enterprise Software RFP Template (22 Feb 2022) is client-only; its
public abstract says the RFP "serves as the call to potential
bidders" and that the template helps "position your RFP to be more
outcomes driven" [8]. Gartner's category RFP templates (CRM, analytics
and BI, RPA, low-code, EHS, ESG, field service, 2024 to 2025) appeared
only as search-engine abstracts and every Gartner page returned 403;
they are not cited for content (Not found).

**F3. The skeleton is settled and the same in every route opened:
four parts and appendices.** (consensus; evidence: institute template
[1], analyst template [3], trade-press template [11]) CIPS: "The RFP
is structured into four main parts": "Instructions to proposers and
proposal conditions", "The requirement", "Information to be supplied
by proposers", "Proposed contract" (Discussion and explanation, p. 6),
followed by Part 5 appendices: "RFP Document", "Terms and
Conditions", "Technical Specifications", "Proposal Submission
Template", "Supporting Documents", "Confidentiality Obligations"
(Contents) [1]. Info-Tech's eleven sections map onto the same four
parts plus schedules [3]. TechTarget's eight-section template (title
page, change log, RFP overview, company overview, project
requirements, proposal rules and templates, evaluation process,
contract negotiations) is the same anatomy in a flatter list [11].
Every section the card listed is present: background and objectives
(CIPS Part 2 "Background and context", Appendix 1 "Overview of the
Project"), scope and statement of work (Appendix 1 "Scope of Work
(SOW)"), requirements (Part 2 "Detailed description of the
requirement", Appendix 3), deliverables (Part 2: the requirement
"needs to very clearly set out the deliverables"), timeline (1.5 "RFP
key dates" with "Estimated commencement date"), evaluation criteria
and weights (1.15), submission rules (1.10), commercial and legal
terms (Part 4, Appendix 2), vendor qualification (3.2 "Financial
Information", "History and previous job performance"), response
instruments (Appendix 4) [1]. The order differs from the card's: the
canon opens with the rules of the process and the evaluation, puts
the requirement second, the response demands third and the contract
last; the card's order (background first, legal terms late,
evaluation in the middle) is the trade-press order, not the
institute's. CIPS states the design rule behind the third part: "keep
all the 'response' obligations in one place" (Part 3, p. 19) [1].

**F4. Evaluation criteria and weights are part of the document and
disclosed to the proposers, as a weighted points system summing to
100, with a warning about the burden disclosure creates.** (consensus;
evidence: institute template and position, analyst template) CIPS
1.15 gives seven example criteria (compliance with requirements, value
for money, experience and capability, innovation and added value,
sustainability and social responsibility, risk management,
implementation plan and timeline), the steps "Define the criteria to
be used in a weighted points system", "Decide on the weighting ...
Should add up to 100", a worked table (price 30, quality 20, lead time
5, ESG 20, qualifications 10, supplier diversity 15) and a two-supplier
scorecard (1.15, pp. 12 to 14); its margin note: "the more
prescriptive you are in defining evaluation criteria and weightings,
the higher the burden you face in demonstrating that you evaluated the
proposals as stated" [1]. The 2013 position distinguishes two kinds of
selection criteria, objective pre-qualification (financial standing,
quality procedures, capacity, track record) and qualitative or
quantitative criteria (proposed solution, standards, price, whole-life
cost), says criteria "should be agreed prior to the tenders being
invited", and that "evaluation should never be a purely mechanistic
process" (Selection criteria, pp. 4 to 5) [2]. Info-Tech carries a
"Proponent Evaluation Process" section and separate evaluation tools
[3][6]; TechTarget recommends "a table showing points by section"
[11]. Weights are the issuer's choice in every source; no source gives
IT-specific weights.

**F5. The response instrument the card called a vendor response
matrix or functional compliance schedule turns up in the buyer-side
canon as a submission template with requirement-by-requirement
tables.** (consensus on the instrument; the vendor-side term is split
by side, see Not found) CIPS Appendix 4 "Proposal Submission Template"
has nine sections; section 4 "Technical and Operational Details" is a
table "Requirement Component | Proposed Solution | Compliance Notes",
section 7 "Compliance with RFP Requirements" a table "Requirement |
Comply? (Yes/No) | Comments or Deviations | Regional Compliance
Considerations", section 9 "Data Privacy and Security" a question
table (pp. 40 to 41); compliance with the contract terms is collected
separately, "often presented in a standard clarification register"
(3.2, p. 21) [1]. Info-Tech's Vendor Response Template ends in a
"Requirements" section [4]; TechTarget notes buyers "may also provide
a pre-formatted spreadsheet that vendors must return in the same
format" [11]. The term "compliance matrix" was found only in
proposal-industry (vendor-side) sources that were not opened; no
buyer-side primary uses it (Not found).

**F6. The requirement part is where the IT content lives, and the
institute's guidance is generic there by design; the analysts fill it
per category.** (consensus on the shell; contested on whether the IT
content is "left to the writer": true of the institute, false of the
analysts) CIPS Part 2: "There is no one way to do this, but a
well-described requirement (sometimes also referred to as a scope of
work or specification) is essential" (p. 17); it lists what a
requirement usually addresses: background and context, organisation
overview, detailed description, deliverables, quality requirements and
performance standards (with KPIs), approvals, "Boundaries and
Exclusions", "Buying Organisation inputs"; and distinguishes a
prescriptive specification from one that is "more functional or
performance-based and describe[s] the expected outcomes or the problem
that needs to be solved", which is "usually the case for an RFP rather
than RFT" (pp. 17 to 18) [1]. Appendix 3 "Technical Specifications"
asks for "Existing Infrastructure or Systems ... any technical,
operational, or integration considerations" (p. 39) [1]. The 2013
position says specifications for complex requirements "should be
output or outcome-based ... or functional" and "described in terms of
commonly used standards" (Pre-requisites, p. 2) [2]. Info-Tech's
generic template has "Technical Environment" and "Required Products
and Services" as section heads [3] and supplies category templates for
the content (ITAM, business intelligence, network management
outsourcing, storage, hyperconverged infrastructure, ERP
implementation partner) [5][6]. The warning that carries the vendor's
perspective into this card: "When the requirements are vague,
suppliers may not bid; if they do, their prices may also increase to
reflect the additional risk" (Part 2, p. 17) [1].

**F7. Two archetypes are supported by the sources, a third is not:
product selection against services and implementation partner; custom
development as its own skeleton was not found.** (emerging; single
source per claim; evidence: analyst blueprint and template pages,
trade press) Product selection: Info-Tech's category templates lead
with specifications and requirements and vendor qualifications [5];
Forrester's template is for "enterprise software" and outcomes [8].
Services and integration: TechTarget's IT-services article has the RFP
tie "technical needs to business goals and KPIs", specify "which roles
and responsibilities belong to internal staff and which belong to the
provider", specify how vendors present pricing, and build the
statement of work "from the RFP's details" after selection, avoiding
"joint responsibilities" [12]; Info-Tech's ERP blueprint says "Define
your implementation partner requirements separately from your software
requirements" and that "ERP implementation is not a one-and-done
exercise" [6]; its ITAM template opens with "The Statement of Work"
[5]. Custom development: no primary opened treats it as a separate
archetype; the search returned only development-agency blogs (not
opened, vendor content on their own market). CIPS does not split by
archetype at all; its one template covers goods and services alike
[1].

**F8. The requirements-engineering standards give the frame of
acquisition but say nothing of the RFP's content, as the plan
assumed.** (single source; evidence: the standards' public scopes,
read as copies on standards-store pages) ISO/IEC/IEEE 26512:2018
"applies the Agreement processes (acquisition and supply)" of
ISO/IEC/IEEE 12207 and 15288 and "addresses requirements for primary
document outputs of the acquisition and supply process: the request
for proposal and the proposal", feeding "the statement of work", but
only for information for users (documentation products and services);
it is withdrawn from 4 Aug 2026 and replaced by ISO/IEC/IEEE
26512:2026, "Requirements for acquirers and suppliers of information
products and services" [9]. The public scope of ISO/IEC/IEEE
29148:2018 names requirements processes and information items and does
not mention acquisition, supply or a request for proposal [10]; the
body is paywalled and was not read. BABOK's vendor assessment
technique (10.49 in v3) was not opened (Not found).

**F9. The disconfirming alternative fails on its own terms: nobody
opened says there is no shared vocabulary or skeleton, and the
"monolithic document" was never one; it is one package with a core
document and separable instruments.** (consensus among the opened
primaries; the "RFP is dead" position exists but was reached only
through vendor blogs and a paywalled abstract, so it stands as a lead
under Unexpected) CIPS 1.4 "Documents to be Included" lists "RFP
Document", "Terms and Conditions", "Technical Specifications",
"Response Templates", "Supporting Documents" (p. 8), i.e. a package;
its Part 5 appendices are those instruments [1]. The 2013 position
lists an ITT as a covering letter, an acknowledgement form, a
specification, a cost, price and delivery schedule, a quality
schedule, a declaration, guarantees, policy questions, company profile
and accounts, references (Documentation, pp. 2 to 3) [2]. Info-Tech
issues the RFP beside RFI, RFQ, vendor response, scenario and
evaluation templates and "Supplementary RFx Material" [3][7]. The
modular shape the card named (commercial terms, security schedule,
technical requirements, response workbook) is thus the canon's own
shape, with a core document that holds the instructions, the
evaluation and the requirement. On the vocabulary, one conflict inside
the institute's own material: the 2025 guidance expands RFP as
"Request for Proposal" and distinguishes it from RFT/ITT/ITB by "the
requirements' specificity" (Overview, p. 4) [1], while a CIPS Knowledge
tip of 2015/2016 writes "Request for quotation (RFQ) or request for
price (RFP)" as alternatives in one role [13]; the 2025 document is the
younger and the dedicated one.

**F10. Vocabulary as the canon uses it (for the other cards).**
(consensus where two sources agree, single source where one) RFI or
EOI: market information and shortlisting before an RFP or RFT [1].
RFP: "used when the organisation's needs are not fully defined,
allowing suppliers more flexibility" [1]. RFT/ITT/ITB: "when the
requirements are clear and precise" [1]; tendering: "the public
release by an organisation of the requirements of goods or services
for a project in order to allow formal bids" [2]. RFQ: price request
for a defined specification [2, Background; 13]. Proposal: "a written
response ... not considered a legally binding offer" (1.1) [1].
Requirement, scope of work, specification, SOW: used as near-synonyms
for the second part [1]; in services, the SOW is the contract document
drafted from the RFP after selection [12]. Post-tender negotiation:
"negotiations ... after the receipt of tenders but prior to contract
award"; best and final offers, written "BFO" by CIPS, obtained by
inviting suppliers to improve against an anonymised price list, to be
announced "at the ITT stage" [2]. Pre-qualification: evaluation of
financial standing, quality procedures, capacity, track record before
the ITT, so that these criteria "would then not be required in the
ITT" [2]. Evaluation matrix: not a term in the sources; CIPS says
"Weighted Scoring System" and "Proposal Evaluation Scorecard" [1],
Info-Tech "Proposal Evaluation Tool" and "RFx Vendor Evaluation Tool"
[3][6]. Compliance matrix, BAFO: vendor-side and US-procurement terms
not found in the buyer-side primaries (Not found).

## Unexpected

The requirement part of an RFP is contract text. CIPS closes Part 2
with "This Part of the Proposal document is intended to form part of
the final Contract" (p. 18) and opens Part 3 with "Much of the
information provided in response to this section will form part of
the final contract" (p. 19) [1]. The card asks what of the RFP follows
from the chain; this says that whatever the chain supplies into Part 2
becomes an obligation of the supplier and of the buyer ("Buying
Organisation inputs"), which is a different standard of wording than
an intent or a BRD is written to. A lead for cards 3 and 4.

The institute's pricing clause asks the proposer to state
"Dependencies and Assumptions" explicitly, "such as: Commodity Prices,
Exchange Rates, Levels of Risk or Uncertainty" (3.1, p. 20) [1]. The
chain's ASM and DEP items have a mirror on the supplier's side of the
same document; the RFP may be the place where the buyer's assumptions
and the supplier's are set against each other. A lead for card 4.

Disclosed weights carry a liability even in a private company. CIPS's
margin note at 1.15 (F4) and the 2013 position's remark that the
changed offer in post-tender negotiation must not "alter the
competition to the extent that other bidders may challenge the award"
(p. 5) [2] say that the procedural discipline the card excluded as
public-law structure is present in private practice as risk
management. A lead for cards 5 and 6.

Gartner's abstract of April 2025 reads, in the search engine's
rendering, "Traditional requests for proposals are not business
buyers' primary approach to software acquisition" [14]; the page
returned 403 and was not opened, so this is a lead from a snippet of a
client-only abstract, not a finding. Together with Forrester's
"outcomes driven" positioning [8] and CIPS's 2013 preference for
"output or outcome-based" specifications [2], it points at the plan's
own premortem: the instrument persists but its requirement part is
being pushed from prescription towards outcomes. A lead for card 2.

Info-Tech's RFP family includes a "Scenario Template" beside the RFP
and the vendor response template [3][4]. If scenarios are the
instrument for scripted demonstrations, the chain's use cases (UC)
have a destination other than the requirement tables. A lead, not
opened; the page was not fetched.

## Not found

- ISM (Institute for Supply Management): no ISM glossary or toolkit
  page surfaced in two queries ("ISM ... glossary 'best and final
  offer'", "ismworld.org glossary ... request for proposal"); only
  third-party glossaries came back.
- A cips.org page: both queries aimed at cips.org returned CIPS
  documents on a content-management asset host, never the institute's
  own domain; the attribution of [1], [2] and [13] rests on their text
  and copyright lines.
- Gartner toolkits: at least ten category RFP templates (2024 to
  2025) and the April 2025 buyer-preference abstract appeared as
  search results; every gartner.com page returned 403. Nothing from
  Gartner is cited for content.
- A primary buyer-side definition of "compliance matrix" or "BAFO":
  the search returned proposal-industry and US government-contracting
  glossaries only (vendor blogs on their own market and public-sector
  sources, excluded by kind); APMP's body of knowledge did not surface
  as an open page. CIPS writes "Best and Final Offers (BFO)" [2].
- A primary treating custom development as an RFP archetype of its
  own: the query on "custom software development RFP vs SaaS RFP vs
  systems integration RFP" returned development-agency and tool-vendor
  blogs only.
- Consultancies' and system integrators' published guidance on IT
  RFPs: two queries aimed at consultancy guidance returned vendor
  blogs and one university IT PMO page behind a login [18]; no
  consultancy or integrator publication was found.
- Any practitioner statement that there is no shared vocabulary or
  skeleton for IT RFPs: the disconfirming query ("no standard" RFP
  format IT ...) found none; the nearest was a tool vendor's blog
  saying generic templates "fall short" for IT, not opened.
- The acquisition clauses of ISO/IEC/IEEE 29148 and BABOK's Vendor
  Assessment (10.49): both paywalled; the one BABOK copy found was an
  unauthorised PDF on a university server, not opened.
- The Harvard Kennedy School Government Performance Lab guide
  "Transforming IT Procurement, Part 3: Writing the RFP" (2023): host
  unresolvable from here and the archive copy blocked [16]; it is
  public-sector in any case.
- IT-specific evaluation weights: no source gives them; CIPS's worked
  table is for goods (price, quality, lead time, ESG, qualifications,
  diversity) [1].

## Options

- Adopt the institute's four-part skeleton with appendices as the
  reference template (instructions and conditions with evaluation;
  requirement; information to be provided: pricing, non-price
  commercial, technical; proposed contract; appendices: terms,
  technical specifications, submission template, supporting
  documents). For: the most explicit published structure, dated 2025,
  with the design rules stated (one place for response obligations,
  dates stated once); against: generic by design in the requirement
  part, with no IT category content.
- Adopt the analyst's flat section list (Info-Tech's eleven, or a
  category template's seven). For: IT category content and the
  surrounding instruments exist; against: member-only, undated, and
  the content was not read.
- Treat the RFP as a package (core document plus schedules and a
  response template) rather than as one document, naming the core
  document's three parts and the schedules separately. For: this is
  what both routes actually issue (F9) and it keeps the person-supplied
  schedules (terms, security questions) apart from what a chain could
  supply; against: more files to govern.

## Relevance to this project

Use CIPS's vocabulary and four-part skeleton as the reference the
other cards write in, and say "package" rather than "document" when
the whole is meant; this rests on F3 and F9 and is chosen against the
trade-press order and the card's own order, which no institute uses.
The reference template is the CIPS RFP template as its guidance
describes it [1], with the analyst's category templates [5] as the
model of how the requirement part is filled for IT. In this agent's
own inference, not a finding: of the skeleton, the parts that match
the chain are Part 2 (background and context, detailed description,
deliverables, quality and performance standards, boundaries and
exclusions, buyer inputs) and Appendix 3 (existing systems and
integration considerations), and the left-hand column of the
submission template's requirement tables; Parts 1, 3 and 4, the
weights of 1.15, the pricing structure and the contract are what a
person supplies, which is the question of cards 3 and 5, not this one.
The archetype distinction the plan expects is weaker in the canon than
the plan assumes: the institute does not split by archetype, the
analysts split product from implementation partner, and custom
development has no skeleton of its own in anything opened (F7); cards
2 and 3 should not presume three settled skeletons.

Consult when: naming the sections of an RFP skeleton or recipe; fixing
the words the forge uses for RFI, RFP, RFT/ITT, RFQ, SOW, proposal,
post-tender negotiation and best and final offer; deciding where the
evaluation criteria and weights stand and whether to disclose them;
designing the response instrument (requirement-by-requirement tables
and a clarification register for the terms); judging whether a
"modular package" is a departure from the canon (it is not).

## Sources

1. Request for Proposal (RFP) Guidance Notes. CIPS (Chartered
   Institute of Procurement & Supply), by its own text ("the RFP
   template provided by CIPS"). Dated January 2025 by the page
   footers; 44 pages, A4.
   https://udntho.files.cmp.optimizely.com/download/assets/RFP_Guidance_Notes.pdf/c8f77ab6b4e911f09e0ff6477f09c9f9
   Kind: primary. Read in full, as text extracted from the PDF
   (Overview, Use of the template, Part 1 clauses 1.1 to 1.22 with
   the evaluation example and scorecard, Parts 2 to 5, Appendices 1,
   3 and 4; Appendix 2's contract clauses skimmed). Original; hosted
   on a content-management asset host, not cips.org.
2. CIPS Positions on Practice: P&SM: Tendering & Post Tender
   Negotiation. CIPS. Dated by the copyright line "©CIPS 2013"; 7
   pages.
   https://udntho.files.cmp.optimizely.com/download/assets/POP+-+Tendering+and+Post+Tender+Negotiation.pdf/47a45a78bafd11f0b502aef7ee74a2a4
   Kind: primary. Read in full, as text extracted from the PDF.
   Original; same host as [1].
3. Request for Proposal (RFP) Template. Info-Tech Research Group;
   authors David Yackness, Rebecca Zhao, Katie Forth. Undated.
   https://www.infotech.com/research/request-for-proposal-rfp-template
   Kind: primary (analyst toolkit; the public template page, the
   template itself member-only). Read through a summarising fetch of
   the public page. Original.
4. Vendor Response Template. Info-Tech Research Group; Yackness,
   Zhao, Forth. Undated.
   https://www.infotech.com/research/vendor-response-template
   Kind: primary (public template page). Summarising fetch. Original.
5. ITAM RFP Template. Info-Tech Research Group; Sandi Conrad.
   Undated.
   https://www.infotech.com/research/it-itam-rfp-template
   Kind: primary (public template page). Summarising fetch. Original.
6. Select an ERP Implementation Partner. Info-Tech Research Group;
   Lisa Highfield, Robert Fayle, Chad Shortridge. Undated.
   https://www.infotech.com/research/ss/select-an-erp-implementation-partner
   Kind: primary (public blueprint page). Summarising fetch.
   Original.
7. Supplementary RFx Material. Info-Tech Research Group; Highfield,
   Fayle, Shortridge. Undated.
   https://www.infotech.com/research/supplementary-rfx-material
   Kind: primary (public template page; only its one-sentence
   description and the related items were visible). Summarising
   fetch. Original.
8. Enterprise Software RFP Template. Forrester; Liz Herbert and
   Rebecca Rose. 22 February 2022, byline.
   https://www.forrester.com/report/enterprise-software-rfp-template/RES177091
   Kind: primary (analyst report; client-only). Read partially: the
   public abstract only, through a summarising fetch. Original.
9. ISO/IEC/IEEE 26512:2018, Systems and software engineering,
   Requirements for acquirers and suppliers of information for users.
   Scope as reproduced on the Estonian Centre for Standardisation
   store page; standard dated 06.06.2018 and withdrawn 04.08.2026 per
   the page's structured history.
   https://www.evs.ee/en/iso-iec-ieee-26512-2018
   Kind: primary (a standard's scope). Read partially: the scope,
   through a summarising fetch. Copy of the scope (iso.org returned
   403).
10. ISO/IEC/IEEE 29148:2018, Systems and software engineering, Life
    cycle processes, Requirements engineering. Scope as reproduced
    on genorma.com; published 28 November 2018, stage 90.92 dated 16
    February 2026 per the page.
    https://genorma.com/en/standards/iso-iec-ieee-29148-2018
    Kind: primary (a standard's scope). Read partially: the scope,
    through a summarising fetch. Copy of the scope.
11. How to write an RFP for a software purchase, with template. Eric
    St-Jean, TechTarget (Informa TechTarget). 2 June 2023, byline.
    https://www.techtarget.com/it-strategy/tip/How-to-write-an-RFP-for-a-software-purchase-with-template
    Kind: secondary (trade press). Summarising fetch. Original.
12. How to write an RFP and statement of work for an IT services
    contract. Mary K. Pratt, TechTarget, quoting two consultants of
    an IT services consulting firm. 24 March 2020, byline.
    https://www.techtarget.com/it-strategy/tip/How-to-write-an-RFP-and-statement-of-work-for-an-IT-services-contract
    Kind: secondary (trade press). Summarising fetch. Original.
13. Counterfeit Tips: Stage 7, Issue ITT/RFP. CIPS Knowledge. Dated
    by copyright lines "CIPS, 2015" and "CIPS, 2016".
    https://udntho.files.cmp.optimizely.com/download/assets/Stage+7+-+Issue++ITT+RFP.doc/f9b6362cb95f11f097fd6e97cfb03987
    Kind: primary, narrow (counterfeit prevention). Read partially,
    through a summarising fetch of a binary .doc whose later sections
    were only partly readable; used for one point of vocabulary only
    (F9). Original.
14. Gartner Insights Abstract, document 8043233 (buyer purchase
    approaches, April 2025 per the search result). Not opened: HTTP
    403. Cited only as a snippet-based lead under Unexpected, never
    for content.
    https://www.gartner.com/en/documents/8043233
15. Gartner Insights Abstract, document 5179363 (CRM RFP template,
    March 2024 per the search result). Not opened: HTTP 403. Not
    cited for content.
    https://www.gartner.com/en/documents/5179363
16. Transforming IT Procurement, Part 3: Writing the RFP. Harvard
    Kennedy School Government Performance Lab, 2023 by the path. Not
    opened: host unresolvable, archive copy blocked. Not cited for
    content.
    https://gplpen.hks.harvard.edu/wp-content/uploads/2023/05/Transforming-IT-Procurement-Part-3-Writing-the-RFP.pdf
17. ISO/IEC/IEEE 26512:2026 page at iso.org. Not opened: HTTP 403;
    its scope read as a copy via [9]'s successor note.
    https://www.iso.org/standard/91114.html
18. SaaS guidelines, a university IT project management office. Not
    opened: redirects to an institutional login.
    https://uit.stanford.edu/pmo/SaaS-guidelines
19. ISO/IEC/IEEE 26512:2026 at the ANSI webstore. Not opened: HTTP
    403.
    https://webstore.ansi.org/standards/iso/isoiecieee265122026

## Opened and not used

- None beyond the thirteen listed as used; [13] was opened for a
  different purpose (counterfeit prevention) and used for one
  vocabulary point only. The six pages that could not be opened are
  listed above as not opened.

## Search record

Queries, in order: IT RFP structure sections software selection; CIPS
request for proposal guidance knowledge; Gartner RFP toolkit software
selection template; Info-Tech Research Group RFP template software;
RFI RFP RFQ difference procurement definition; RFP is dead modular
procurement outcome-based software buying (disconfirming); site:cips.org
request for proposal RFP tender documents; ISM glossary "best and
final offer" "request for proposal"; ISO/IEC/IEEE 29148 acquisition
"request for proposal"; BABOK vendor assessment technique RFP RFI RFQ;
compliance matrix RFP requirements traceability definition APMP;
custom software development RFP vs SaaS RFP vs systems integration RFP
differences statement of work; "Transforming IT Procurement" "Writing
the RFP" Harvard Growth Lab; IIBA BABOK v3 vendor assessment technique
description; APMP glossary compliance matrix "best and final offer";
RFP package security questionnaire SIG separate schedule commercial
terms technical requirements response workbook modular
(disconfirming); ISO/IEC/IEEE 29148:2018 scope acquisition supply
agreement processes; systems integrator implementation services RFP
template ERP implementation partner selection; ismworld.org glossary
supply management terms request for proposal; "no standard" RFP format
IT "every RFP is different" (disconfirming); Gartner software selection
without RFP agile sourcing "proof of concept" instead of RFP 2025
(disconfirming); CIPS knowledge tendering RFQ RFP ITT definitions
procurement cycle; APMP body of knowledge compliance matrix definition
proposal; RFP for SaaS versus custom build versus implementation
partner differences consultancy guide.

Openings (fetches of a page): thirteen opened and read ([1] to [13]),
of which [1] and [2] as full text extracted from the PDF and the rest
through a summarising fetch; six attempted and not opened ([14] to
[19]: four HTTP 403, one unresolvable host plus a blocked archive
copy, one institutional login).

The disconfirming queries found no source saying there is no shared
vocabulary or skeleton; they found the "kill the RFP" position only in
vendor blogs and a paywalled abstract (leads under Unexpected), and
they found the modular package to be the canon's own shape (F9).

The run ended on both parts of the stop rule together: the last two
differently-worded queries (consultancy archetype guidance; APMP
compliance matrix) brought nothing not already seen, and each
perspective of the card has a primary source (the procurement
officer: [1], [2], [3]; the architect: [1] Part 2 and Appendix 3, [5],
[6]). The opening budget was near its end at thirteen of about
fifteen.
