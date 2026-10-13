---
project: forge
date: 2026-10-13
topic: what an IT or AI strategy contains, light but complete - the mix of structure and checklist that stays agile
status: immutable
derived_from: the principal's word of 2026-10-13 in the project ai-strategy (a strategy artefact for the forge, research first); 00-brief-next-gen.md v0.3 (Work without a known artefact); 10-intent.md v5.6 (POS.0700, POS.1430); research/2026-10-03-work-without-a-known-artefact-and-its-working-files.md; web sources below
---

# Research: what an IT or AI strategy contains, light but complete

## Question

What is today the minimal complete content of an IT strategy, and
of an AI strategy, for a mid-sized company in a regulated industry:
the sections and questions that keep structure and serve as a
checklist of what not to forget, while the document can be written
and changed in an agile way, without the weight of the large
frameworks?

Sub-questions: which sections recur across practice; how an AI
strategy differs from an IT strategy; which light methods hold
structure without volume; how a strategy is kept alive; which
failures are common enough to become a checklist; what a regulated
company must add. The large frameworks (TOGAF, Balanced Scorecard,
COBIT) are reference only, not the subject. Sources 2023 to 2026
preferred, primary before secondary; some primaries are paywalled
and are marked so.

The note serves the definition of a kind of artefact `strategy` for
the forge (`/new-artefact`): its Relevance section proposes the
candidate Map of that definition.

## Key findings

### 1. The recurring core of an IT strategy (consensus)

Across templates and guides from Gartner (2009 template, still
circulated), CIO Index (14 components; a 23-section template
organised around *where we are, where we need to go, what gaps to
close*), Info-Tech (scope, year in review, key initiative plan,
operational strategy), BMC, TechTarget and a 2025 IT Tool Kit guide,
the same core recurs, under varying names:

- executive summary, half a page, first;
- business context and alignment: the business goals the strategy
  serves, in the business's words;
- current state: capabilities, technical debt, risks, what worked
  and what did not (Info-Tech makes "year in review" a section of
  its own);
- vision or target state, dated;
- principles or guiding policy;
- initiatives, prioritised by value against feasibility and cost;
- roadmap, sequenced, with owners;
- resources: budget, people, skills;
- operating model and organisation;
- governance: decision rights, approval, vendor and service
  management;
- risks and assumptions;
- metrics and KPIs, SMART, with baselines;
- change management and communication.

Info-Tech advises a firm roadmap of twelve months and warns against
projecting three to five years in detail; the strategy itself may
look further but only as direction. The sources differ in length
(from one page to 23 sections) and emphasis, not in the core.
Epistemic status: consensus on the content list; no 2025 standard
exists, and the longest templates are the least read (Gartner's own
observation below).

### 2. What an AI strategy adds (consensus on the areas, emerging on the weights)

Gartner's AI strategy framework names four pillars: *vision* (how AI
supports enterprise goals, the benefits, how success is measured),
*value* (the organisational barriers to capturing value and the
change actions that remove them), *risk* (regulatory, reputational,
competency, technology) and *adoption* (initiatives prioritised by
value against feasibility, business and IT agreeing the ranking).
The full workbook is gated. Practitioner guides of 2025 and 2026
agree on these additions to the IT core:

- a use-case funnel: one intake, the same weighted criteria for
  every use case, a visible portfolio, a decision on who decides;
- data: access, quality, ownership, and the split between personal
  and non-personal data; delivery of data per use case rather than
  per transformation programme;
- governance with proportionate tiers: acceptable-use policy, AI
  governance, data governance, risk management, approval of new
  tools fast where the risk is low;
- people and skills: literacy for everyone, expert tiers with
  defined skills and tools, and the 10-20-70 weighting (10 % of the
  effort in algorithms, 20 % in technology, 70 % in people and
  process) that several guides repeat;
- measurement with baselines taken before pilots, and monitoring
  after deployment;
- an operating model that names who owns AI: a central team,
  federated experts, the business.

The evidence that these weights matter comes from three 2025
studies, all of them secondary here except McKinsey's own page:

- McKinsey, *The state of AI in 2025*: nearly nine in ten
  organisations use AI regularly, but only about 6 % are "high
  performers" (5 % or more of EBIT attributed to AI). High
  performers are nearly three times as likely to redesign workflows
  when deploying AI, three times as likely to report senior leaders
  owning the AI initiatives, and three times as likely to scale
  agents across functions. Workflow redesign is the factor with the
  strongest contribution to impact. (The McKinsey page itself timed
  out on fetch; the figures are from its search abstract and
  consistent secondary reports.)
- MIT NANDA, *The GenAI Divide: State of AI in Business 2025*
  (August 2025): about 95 % of enterprise generative-AI pilots show
  no measurable P&L impact; the causes named are the learning gap,
  brittle workflows and poor fit with daily operations, not model
  quality; the largest returns were found in back-office automation
  while budgets went to sales and marketing. The sample is small
  and reported inconsistently (52 organisations interviewed, 153
  leaders surveyed, by the report's own count): a preliminary
  finding, widely quoted beyond its weight.
- Gartner, June 2025: over 40 % of agentic AI projects will be
  cancelled by the end of 2027, for rising cost, unclear business
  value and weak risk controls; "agent washing" by vendors
  (assistants and RPA relabelled as agents) is named.

Older but still cited: MIT Sloan Management Review with BCG (2019)
argued that a standalone AI strategy is not enough; it must be
complementary to and interdependent with the business strategy.
MIT Sloan's *Leading with AI* (2024) reduces the plan to three
anchors: business priorities, the data strategy, and employee
skills.

### 3. Light forms that keep structure (established, decades old)

Three forms recur whenever practitioners describe a short strategy
that still forces decisions:

- **Rumelt's kernel** (*Good Strategy / Bad Strategy*, 2011; *The
  Crux*, 2022): a *diagnosis* of the challenge, a *guiding policy*
  that says how it is met and rules things out, and *coherent
  actions* that reinforce one another rather than coexisting as a
  list. The guiding policy is a signpost, not the trip. Rumelt's
  "bad strategy" catalogue is the readiest checklist of failure:
  fluff, failure to face the challenge, mistaking goals for
  strategy, bad strategic objectives.
- **Playing to Win** (Lafley and Martin, 2013): five integrated
  choices, *winning aspiration, where to play, how to win, the
  capabilities needed, the management systems that keep them*; each
  answer must make the others more true; where *not* to play
  matters as much. The Leading Edge Forum's one-page IT strategy
  (Bowden, 2016) is this cascade reduced to a tagline, *where to
  play* and *how to win*, with the rule "speak about the business
  as much as possible and about technology as little as possible".
- **Gartner's one-page strategy** (insight of October 2024,
  webinars 2025): the one page is a storytelling device, because
  "lengthy, technical documents are rarely used in practice" and
  the document itself is often the barrier to buy-in; the four
  steps are behind the paywall and were not retrieved.

The measurement layer is usually OKR where the strategy is light:
objectives from the guiding policy, key results as the measures,
reviewed quarterly. Strategy "cards" (customer problem, thesis,
indicators, resources, risks, stop/scale triggers) appear in
practitioner blogs as the unit of a modular strategy; the source is
weak and the idea plain.

What the light forms drop: the inventory sections (architecture,
infrastructure, service management, vendor management) and the
operational appendices. Practice attaches these as a living
appendix or keeps them in the operating documents, not in the
strategy.

### 4. Keeping a strategy alive (emerging consensus)

The sources agree that a fixed annual document goes stale and that
the remedy is a rolling review, not a rewrite:

- a quarterly strategy review with distinct decisions from the
  monthly steering and the weekly operating review; the direction
  ("north star") stable, the path flexible;
- Steenbeek (June 2026) proposes for a data-and-AI strategy an
  A.D.A.P.T. cycle per quarter: *Ambition* re-checked against the
  drivers, *Diagnostics* of plan against actuals, *Assurance* that
  the controls ran, *Progress* of capability maturity, *Tuning* of
  priorities, funding, owners, timelines and roadmap; explicitly
  "not a new strategy every three months";
- the review cadence tied to reversibility: reversible decisions
  move fast, hard-to-reverse ones get slower, deeper review;
- assumptions written explicitly so that the review has something
  to check.

This matches the forge's own mechanics (versions, history, a thread
per open matter) better than a document with a date on its cover.

### 5. The failure checklist (consensus on the items, secondary sources)

From the 2025 studies and the practitioner post-mortems, the
failures named often enough to deserve a line in a checklist:

1. AI treated as a technology purchase, not a capability.
2. No workflow redesign: the tool is added to the old process.
3. Pilot purgatory: no path from pilot to production (integration,
   infrastructure, governance not planned).
4. Weak data foundations, readiness overestimated.
5. Unclear ownership and decision rights; task forces without
   authority; no shared definition of success.
6. No baseline, so no measurable value; cost unclear against value.
7. Change management arriving late; middle management the most
   resistant group (Prosci, via secondary sources).
8. Budget where the hype is, not where the return is.
9. Risk controls weak or absent; approval either blocking everything
   or nothing.
10. Vendor claims taken at face value ("agent washing").
11. Rumelt's four: fluff, the challenge not faced, goals mistaken for
    strategy, objectives that do not add up.
12. Strategy as a document instead of a mechanism: no cadence, no
    owner of the strategy itself.

### 6. What a regulated company adds (consensus on duties, timing contested)

- **EU AI Act** (Regulation (EU) 2024/1689): prohibited practices
  and general-purpose-AI obligations are in force. The Digital
  Omnibus agreement of May 2026 defers the high-risk obligations:
  stand-alone Annex III systems to 2 December 2027, AI embedded in
  regulated products to 2 August 2028; Article 50 transparency for
  systems already on the market to 2 December 2026. Legal status at
  the time of writing is disputed between sources (formal adoption
  expected before 2 August 2026; one source reports publication as
  Regulation (EU) 2026/1744): verify before relying on a date. One
  source reports the Article 4 AI-literacy duty softened into a
  promotion duty of the Commission and Member States; unverified.
- Deployer duties that a strategy must at least name: an inventory
  of AI systems in use, their risk classification, human oversight
  documented, use within the provider's instructions, logging and
  audit trails, incident reporting, transparency to end users.
- **GDPR** and the sector regulator: the split between personal and
  non-personal data is a design decision of the data area, not a
  compliance afterthought; a gambling operator adds the gambling
  regulator's requirements on fairness, player protection and the
  zero-tolerance processes the directors already name (lottery,
  draw, prize payout).
- Reference frameworks worth citing, not adopting whole: NIST AI RMF
  with its Generative AI Profile (govern, map, measure, manage) and
  ISO/IEC 42001 for an AI management system.

## Options and trade-offs

1. **The full template** (CIO Index's 14 components or 23 sections,
   Gartner's demand/control/supply). Complete, nothing forgotten;
   heavy, written once, rarely read, stale within a quarter. Fit for
   an audit, not for a strategy that is to be lived.
2. **The kernel or the one page alone** (Rumelt, Playing to Win,
   Gartner's page). Forces the choices, readable by the leadership,
   says what is ruled out; carries no owners, no dates, no budget,
   no measures, and leaves the checklist to the author's memory.
3. **Layered: kernel, checklist of areas, rolling appendix.** The
   first page is the kernel (diagnosis, guiding policy, coherent
   actions, in the company's words); the body walks a fixed list of
   areas, each with items or the explicit statement that the area
   was considered and left; the appendix holds what changes
   quarterly (initiatives with owners and dates, KPIs with
   baselines, budget, risks with triggers) and is reviewed on a
   cadence. Readable at the top, complete underneath, agile where
   change happens. The cost is discipline: the areas must be walked
   honestly, and an empty area must say why.

Recommendation: option 3. It is what the principal asked for (a
structure and a list of what not to forget, without a large
framework), and it is what the forge already knows how to run: the
list of areas is a Map, the explicit "considered and left" is the
Map's rule, the rolling appendix is versions with history, the open
matters are threads.

## What was not found

- A single authoritative 2025 or 2026 standard for the content of
  an IT or AI strategy; the field is templates and guides.
- Gartner's four steps of the one-page strategy and its AI strategy
  workbook: paywalled.
- Primary text of the MIT NANDA report and of McKinsey's survey
  page (timeout); their figures are taken from abstracts and
  consistent secondary reporting.
- Any evidence on the *right length* of a strategy; only the
  observation that long ones are not read.
- Guidance specific to lottery or gambling operators on AI
  strategy; the regulated-industry material is generic (finance,
  health) and the EU AI Act.

## Relevance to this project

The candidate Map of the artefact `strategy`, as a list of areas
the finding must consciously consider; an area may stay empty with
the reason. The first four are the kernel and are never empty; the
rest are the body; the last three are the rolling appendix.

1. **Mandate.** Why now, which business strategy it serves, in the
   business's words; the scope (IT, AI, both; which parts of the
   company); the horizon, with a firm twelve months and direction
   beyond.
2. **Diagnosis.** The crux: the few barriers that limit value most,
   what was tried and why it stalled, the evidence. Not a list of
   everything wrong.
3. **Ambition and target state.** Dated; what will be true; what is
   deliberately not pursued.
4. **Guiding policy.** The few choices that rule things out and
   make the others more true (platform-first against light, build
   against buy, two speeds, data per use case, in-house capability
   against vendors).
5. **Where to play: the use-case portfolio.** The funnel: intake,
   criteria, who decides, the portfolio as it stands, what is ruled
   out.
6. **Coherent actions.** Initiatives sequenced with owners, dates
   and dependencies; each traceable to the guiding policy;
   workflow redesign named where a tool is introduced.
7. **Operating model.** Who owns what between the central team,
   the technology division and the business; decision rights; the
   single point of contact for a user; how a request becomes a
   standard request.
8. **People and capabilities.** Literacy for all; expert tiers with
   their skills, tools, training; the internal capacity needed to
   run the chosen model, and whether it exists.
9. **Data and technology foundations.** The data-access model
   (personal and non-personal, per use case), the platform and
   gateways, security architecture, the local or commercial model
   choice.
10. **Governance, risk and compliance.** The AI-risk acceptance
    framework with proportionate tiers, the approval path for new
    tools, the AI-system inventory and classification (EU AI Act),
    GDPR, the sector regulator, responsible-AI commitments.
11. **Economics.** Budget, cost governance, value tracking,
    build-or-buy, what is expensive by design.
12. **Measures.** KPIs with baselines, definition of done per
    deliverable, what "success" means to the leadership.
13. **Risks and assumptions.** Explicit, each with the trigger that
    would change the strategy.
14. **Communication and adoption.** Who hears what, when; the
    change plan; the resistance expected.
15. **Cadence.** How the strategy is reviewed, by whom, what each
    review may change; the version and the history.

Two further recommendations for the definition. First, the
failure checklist of finding 5 belongs to the critic's or the
challenger's reading of a strategy, not to the Map: a persona or a
lens that hunts fluff, goals mistaken for strategy, actions without
a policy, initiatives without redesign, measures without baselines.
Second, the template should open with the kernel on one page in
prose and keep the areas as sections of items with IDs; the
appendix areas (12 to 15, and the dated parts of 6) are what a
quarterly round rewrites, the kernel is what it re-checks.

## Sources

- CIO Index, *14 Components of a Complete IT Strategy*,
  https://cioindex.com/toolkit/crafting-a-winning-it-strategy-the-14-essential-components-for-success/
  (undated; footer 2026), and *IT Strategic Plan Template*,
  https://cioindex.com/reference/it-strategic-plan-template/
- TechTarget, *10 free IT strategic planning templates and examples
  for CIOs*,
  https://www.techtarget.com/searchcio/tip/Free-IT-strategic-planning-templates-for-CIOs
- Gartner, *IT Strategy Template* (Dave Aron, 2009), as published by
  Camden Council,
  https://camden.moderngov.co.uk/documents/s62975/Appendix%20B.pdf
- Info-Tech Research Group, *Build a Business-Aligned IT Strategy*,
  https://www.infotech.com/research/ss/build-a-business-aligned-it-strategy
- BMC, *8 Components of a Great IT Strategy*,
  https://www.bmc.com/blogs/it-strategy/
- IT Tool Kit, *IT Strategic Planning Guide 2025*,
  https://www.ittoolkit.com/it-strategic-planning-guide-2025-framework-best-practices/
- Gartner, *AI Strategy for Business* (four pillars; workbook gated),
  https://www.gartner.com.au/en/information-technology/topic/ai-strategy-for-business
- Gartner, *The Art of the One-Page Strategy* (October 2024;
  paywalled, 403 on fetch),
  https://www.gartner.com/en/articles/the-art-of-the-one-page-strategy
- BRM Institute / Leading Edge Forum, Mike Bowden, *How Do You
  Present a Good IT Strategy? On One Page* (2016),
  https://brm.institute/how-do-you-present-a-good-it-strategy/
- McKinsey, *The state of AI in 2025: Agents, innovation, and
  transformation*,
  https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
  (fetch timed out; figures from the abstract and secondary reports)
- MIT NANDA, *The GenAI Divide: State of AI in Business 2025*, via
  Fortune (18 August 2025),
  https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
- Gartner press release of June 2025 on agentic AI cancellations,
  via w.media, https://w.media/?p=20821
- MIT Sloan, *Leading with AI* (2024),
  https://mitsloan.mit.edu/ideas-made-to-matter/leading-ai-driven-organization
- MIT Sloan Management Review and BCG, *Reshaping Business With
  Artificial Intelligence* (2019),
  https://shop.sloanreview.mit.edu/products/59181
- Rumelt, *Good Strategy / Bad Strategy* (2011), summary at
  https://www.aakashg.com/good-strategy-bad-strategy/ ; *The Crux*
  (2022)
- Lafley and Martin, *Playing to Win* (2013), summary at
  https://fs.blog/playing-to-win-how-strategy-really-works/
- Irina Steenbeek, *Do We Still Need DM Strategy? Part 2: Rolling the
  DM & AI Strategy* (7 June 2026),
  https://datacrossroads.nl/2026/06/07/do-we-still-need-dm-strategy-part-2-rolling-the-dm-ai-strategy/
- Think Insights, *Fixed Plans vs Adaptive Strategy*,
  https://thinkinsights.net/strategy/fixed-plans-vs-adaptive-strategy
- Cleverence, *Why Strategy Must Be a Living System* (practitioner
  blog, weak),
  https://www.cleverence.com/articles/business-blogs/why-strategy-should-be-treated-as-a-living-system-4827
- Gibson Dunn, *EU AI Act Omnibus Agreement: Postponed High-Risk
  Deadlines and Other Key Changes* (27 May 2026),
  https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- OneTrust, *EU Digital Omnibus proposes delay of AI compliance
  deadlines*,
  https://www.onetrust.com/blog/eu-digital-omnibus-proposes-delay-of-ai-compliance-deadlines/
- Noze, *AI Act: the checklist for organisations from 2 August
  2026*,
  https://www.noze.it/en/insights/ai-act-checklist-obligations-august-2026/
- Practitioner guides on AI strategy content (vendor blogs, 2025 to
  2026): Lucid, https://lucid.co/blog/enterprise-ai-strategy ;
  Iternal, https://iternal.ai/ai-strategy-guide ; Baytech,
  https://www.baytechconsulting.com/blog/ready-set-scale-cto-enterprise-ai-checklist ;
  StackAI,
  https://www.stackai.com/insights/why-your-ai-strategy-is-failing-and-how-to-build-a-successful-enterprise-ai-roadmap-for-2026 ;
  CIO.com, *Beyond the hype: 4 critical misconceptions derailing
  enterprise AI adoption*, https://www.cio.com/article/4116299/
