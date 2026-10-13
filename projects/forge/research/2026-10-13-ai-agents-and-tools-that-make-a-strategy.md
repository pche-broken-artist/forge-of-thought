---
project: forge
date: 2026-10-13
topic: AI agents and tools that make a strategy with a person - what exists, what they ask, what they return, where they stop
status: immutable
derived_from: the principal's word of 2026-10-13 in the project ai-strategy (look whether an AI agent for strategy creation exists); research/2026-10-13-what-an-it-or-ai-strategy-contains-light-but-complete.md; research/2026-10-03-work-without-a-known-artefact-and-its-working-files.md; web sources below
---

# Research: AI agents and tools that make a strategy

## Question

Which products, agents and open procedures make a strategy
together with a person today: strategy platforms with AI, the
consulting firms' internal assistants, open-source prompt skills
for the assistant models; what questions do they ask, what
structure do they return, and where do they stop? And what of it
can the definition of the forge's `strategy` artefact borrow, and
does any of it replace or complement the forge's own approach?

Companion of the note on what a strategy contains, same date.
Vendor pages are the main source for the products; none was tested
and no independent evaluation was found: the claims are what the
makers say.

## Key findings

### 1. Strategy platforms with AI features (vendor claims, 2024 to 2026)

The market segment is "strategy execution" software: OKR and
scorecard tools that have added drafting and analysis. A Cascade
comparison of May 2026 and vendor pages describe:

- **Cascade** (Tapestry AI): converts existing decks, spreadsheets
  and PDFs into a structured, live plan; links parent goals to
  contributing initiatives automatically; drafts updates from
  meeting, mail and file context; audits whether execution matches
  the stated intent and flags risks and dependencies.
- **Quantive StrategyAI** (announced February 2024): ingests the
  company's documents (a Balanced Scorecard, a roadmap) and
  converts them into an OKR execution plan; for a business question
  it builds a "decision map" of the angles and a strategy map, and
  recommends analysis frameworks; converts decisions into goals
  with owners and outcomes.
- **ClearPoint Strategy** (Next AI, page updated July 2026): drafts
  objectives, KPIs and initiative descriptions from a short prompt
  within a framework the customer already uses (Balanced Scorecard,
  OKR, custom); updates measures and milestones from natural
  language; exception reports and forecasts. The vendor's own
  statement of limits is the most useful line found: AI "won't
  execute" the plan, cannot decide priorities, negotiate
  stakeholder trade-offs or assign real accountability, and a
  general chatbot "starts from zero each session" unless the plan
  lives in the tool.
- **WorkBoard** (a "chief of staff" agent for alignment and
  accountability, scorecards from connected systems),
  **Wave by McKinsey** (custom planning agents, opportunities from
  transformation benchmarks, value tracking), **Profit.co**,
  **Perdoo**, **Tability** (OKR drafting), **Planview** (scenario
  comparison, portfolio optimisation), **Envisio** (status updates
  and executive summaries).

What they share: the framework is the customer's choice and the
tool fills it; the inputs are the customer's existing documents and
connected data; the outputs are objectives, KPIs, initiatives and
alignment links; the value claimed is in execution tracking, not in
finding the strategy. None asks the diagnostic questions; none
reconstructs a strategy from a conversation.

### 2. The consulting firms' assistants (press reporting, 2025)

McKinsey's **Lilli** (firm-wide since 2023; over 75 % of staff use
it monthly by June 2025; drafts slides from prompts, the only place
staff may enter confidential client data), BCG's **Deckster** (slide
building from 800 to 900 templates) and **GENE** (a brainstorming
chatbot), Bain's **Sage** (a chat platform built with OpenAI). All
are knowledge, research and slide assistants for the consultant;
none is described as a strategy generator, and the method stays
with the people. Wave by McKinsey (above) is the client-facing
product and is an execution platform.

### 3. Open-source prompt skills for the assistant models (2025 to 2026)

The closest thing to "an agent that makes a strategy" is a family
of Markdown skill files for Claude:

- **strategy-skills-for-claude** (GitHub, aapersh; unofficial;
  licence not stated): 21 skills in six domains, each a workflow
  with an output format and a quality bar: *Diagnosis and Framing*
  (Situation Assessment, Growth Barriers, Assumption Audit);
  *Market and Competitive Intelligence*; *Strategic Choice and
  Economics* (Strategic Options, Business Case Builder, Portfolio
  Review, Pricing); *Operating Model and Execution* (Operating
  Model Design, Initiative Prioritizer, Transformation Roadmap);
  *Risk, Performance and Value Governance* (War Gaming, Risk and
  Mitigation, KPI Architect, Value Realization); *Alignment and
  Executive Communication* (Stakeholder Alignment, Narrative
  Builder, Decision Memo). The method is the consulting one: crisp
  problem framing, MECE structure, hypothesis-led analysis, 80/20,
  answer-first, assumption-conscious. One skill at a time, by hand.
- **strategy-kernel** (ClaudSkills registry, community): Rumelt's
  crux applied as a skill: a diagnosis, standard and reframed, a
  guiding policy, coherent actions; triggered when "actions feel
  scattered". A single file, questions not published.
- **strategic-planning-facilitator** (same registry): SWOT, OKR
  goals and an execution roadmap for small and mid-sized
  businesses.

These are prompts, not agents: no memory across sessions, no
sources of their own, no provenance, no versioning; the person
supplies the facts and judges the output. Their value is the
question lists and the quality bars, which are readable and
borrowable.

### 4. What the makers say the tools cannot do (consensus)

Three limits recur, stated by the vendors themselves and by the
practitioner posts: the tool does not decide priorities or
negotiate trade-offs; it does not assign accountability; it does
not know the company's plan unless the plan lives where the tool
can read it. The MIT NANDA 2025 finding of the "learning gap"
(tools that do not retain feedback or adapt to context) is the same
limit seen from the user's side.

## Options and trade-offs

1. **Adopt a strategy platform** (Cascade, Quantive, ClearPoint).
   Execution tracking, dashboards, OKR alignment, drafting from
   existing decks. Cost, a new system, the company's plan in a
   vendor's cloud, and nothing for the part the forge is for: the
   finding, the provenance, the challenge, the history. Not the
   question asked.
2. **Use the open skills as they are.** Free, readable, consulting
   structure; one skill per prompt, no memory, no sources, no
   record; the output would have to be re-entered into the forge by
   hand.
3. **Borrow from both into the definition.** The question lists
   and quality bars of the skills, the "ingest existing documents
   into a structured plan" step of the platforms and their honest
   limits become parts of the `strategy` definition; the forge
   supplies what none of them has: immutable sources with
   provenance, the intent as the issue tree, isolated challengers,
   versions with history.

Recommendation: option 3. Nothing found replaces the forge's
approach, and nothing complements it as a tool worth installing;
what is worth taking is text.

## What was not found

- An agent that reconstructs a strategy from meeting transcripts
  and checks it against a reference content: the gap the forge is
  being asked to fill.
- A multi-agent system that produces diagnosis, policy and roadmap
  as separate roles with a shared record.
- Any independent evaluation of the platforms' AI features, or
  their pricing; everything is vendor-sourced.
- GPT-side equivalents of the Claude skills; the search surfaced
  none.

## Relevance to this project

For the definition of the `strategy` artefact (`/new-artefact
strategy`):

- **Map.** Add two questions the skills ask and the templates do
  not: the *assumption audit* (which beliefs the strategy rests on,
  which are untested, what would falsify them) and the *situation
  assessment* as a disciplined diagnosis (what is true, what is
  the crux, what evidence). Both land in the candidate Map of the
  companion note under Diagnosis and under Risks and assumptions.
- **Partner.** The vendors' limits are the Partner block, already
  the forge's rule: Claude drafts, structures, aligns and tracks;
  the principal decides the priorities, the trade-offs and the
  owners. Say it in the definition in these words so that the
  first `/forge strategy` does not drift into generating a plan.
- **Instruments.** Ingest existing documents into the structure is
  what `/ingest` plus the reconstruction already do, with
  provenance the platforms lack; the definition should name the
  reconstruction from sources as a way in, beside elicitation and
  handing over.
- **Reviewers.** The skills' quality bars (decision-oriented,
  evidence-aware, assumption-conscious, answer-first) and the
  failure checklist of the companion note are the material for a
  challenger persona *strategist* (foreseen in POS of the forge
  intent on personas) or for a calibration of the critic's reading
  of a strategy; the principal decides whether the blind spots
  differ enough from the `cto` persona.
- **Render.** The *decision memo* (answer first, then the reasoning,
  then what is asked of the reader) is the shape of the render for
  the leadership forum, not of the artefact.
- Where a skill file is actually read for its questions, it is a
  source: ingest it into the forge project before citing it.

## Sources

- Cascade, *Best AI Strategy Platforms in 2026* (5 May 2026),
  https://www.cascade.app/blog/best-ai-strategy-platforms
- Quantive, *Quantive StrategyAI* and its help centre,
  https://www.quantive.com/resources/blog/quantive-strategyai ;
  https://help.quantive.com/en/articles/9330771-key-use-cases-for-quantive-strategyai ;
  SiliconANGLE (29 February 2024),
  https://siliconangle.com/2024/02/29/quantive-unveils-ai-driven-strategy-platform-enhance-business-decision-making/
- ClearPoint Strategy, *AI Strategic Planning: The Complete 2026
  Guide* (updated 6 July 2026),
  https://www.clearpointstrategy.com/blog/ai-strategic-planning
- People Managing People, *10 Best AI Strategy Tools Reviewed in
  2026*, https://peoplemanagingpeople.com/tools/best-ai-strategy-tools/
- Fortune (2 June 2025) on McKinsey's Lilli,
  https://fortune.com/2025/06/02/mckinsey-ai-consulting-powerpoints-proposal-technology/
- Business Insider, *Inside the AI boom that's transforming how
  consultants work at McKinsey, BCG, and Deloitte*,
  https://www.businessinsider.nl/inside-the-ai-boom-thats-transforming-how-consultants-work-at-mckinsey-bcg-and-deloitte
- Plus AI, *How the top consulting firms are using AI* (secondary,
  partly unverified), https://plusai.com/blog/how-consulting-firms-use-ai
- aapersh, *strategy-skills-for-claude* (GitHub),
  https://github.com/aapersh/strategy-skills-for-claude
- ClaudSkills registry, *strategy-kernel*,
  https://claudskills.com/skills/strategy-kernel/ and
  *strategic-planning-facilitator*,
  https://claudskills.com/skills/strategic-planning-facilitator/
- Futurum Group, *Microsoft Copilot Becomes an Agentic Work
  Platform* (September 2026; general productivity, not strategy),
  https://futurumgroup.com/insights/microsoft-copilot-becomes-an-agentic-work-platform/
- MIT NANDA 2025 via Fortune (18 August 2025), for the learning gap,
  https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo
