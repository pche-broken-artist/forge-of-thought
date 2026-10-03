---
project: forge
type: research
topic: how a solution design is built - what established practice and the spec-driven tools put into the document that says how what is wanted is realised, and how it avoids repeating the layer above and the thing below
date: 2026-10-03
derived_from: 10-intent.threads.md, THR.0520 (intent v4.51)
status: immutable
---

# How a solution design is built

## Question

How is a solution design document built in established practice, so
that it says how what is wanted is realised, stays true, and repeats
neither the requirements above it nor the thing that realises it
below?

The question comes from THR.0520: the intent of the forge's own
project carries more solution than intent, and a layer for the
solution is to be added. Four hypotheses from the working
conversation, written nowhere yet, are tested in the last section.

Not repeated here, and cited instead: the survey of layers from idea
to handover, which already read design docs at Google, the Rust RFC
template and decision records for where rejected alternatives live
(`2026-09-28-artefact-layers-from-idea-to-handover.md`, below "the
layers note"); the reading of the forge as closer to open work than
assumed (`2026-10-03-work-without-a-known-artefact-and-its-working-files.md`,
Relevance); the classification of the forge intent's items
(`2026-10-01-what-of-the-intent-belongs-to-an-assignment.md`).

Epistemic tags: **[C]** consensus across the sources read, **[E]**
emerging, **[X]** contested. Every finding says whether it is
verified at a page fetched in this session, taken from a secondary
source, or this note's own synthesis.

How the sources were read. Every page was opened through a fetch
tool that returns a small model's extraction of the page, not the
page itself; quotations are as the tool returned them and were not
compared with the pages character by character. Three sources came
back as full text and were read directly: the Rust RFC template (raw
file), the OpenSpec design template (raw file) and the AWS guide's
page on the ADR process. Two pages that carry weight were fetched a
second time with a request for word-for-word quotation and the two
readings agree: the account of design docs at Google and the BMad
page on architecture. Search summaries are marked as such. What
could not be read is listed under "What was not found".

## Key findings

### 1. There are two families of design document, and only one of them is meant to stay true [C for the two families; the naming is this note's]

Verified at the pages fetched; the division into two families is
this note's synthesis.

**The design of a change.** A design doc, an RFC, a KEP, a PEP, an
OpenSpec `design.md`, a Kiro `design.md` and a spec-kit `plan.md`
each describe one change to a system, are argued and accepted, and
are then history.

- The design doc at Google (Ubl, 2020-07-06): context and scope,
  goals and non-goals, the actual design (an overview, then a
  system-context diagram, APIs, data storage, code only for novel
  algorithms, the degree of constraint), alternatives considered,
  cross-cutting concerns. Length: "The sweet spot for a larger
  project seems to be around 10-20ish pages"; mini docs of one to
  three pages for incremental work. Its job: "The design doc is the
  place to write down the trade-offs you made in designing your
  software." It is written by the engineers who will build, reviewed
  lightly or formally; the page gives no formal approval rule. The
  companion book chapter says design documents are approved before
  major projects begin and should be reviewed again at launch
  against their stated goals (Software Engineering at Google,
  chapter 10).
- The Rust RFC template (read in full): Summary, Motivation,
  Guide-level explanation, Reference-level explanation, Drawbacks,
  Rationale and alternatives, Prior art, Unresolved questions,
  Future possibilities. The design sits in two sections for two
  readers: how one should think about the feature, and "the
  technical portion", detailed enough that "it is reasonably clear
  how the feature would be implemented" and "corner cases are
  dissected by example".
- The Kubernetes KEP template: Summary, Motivation (Goals,
  Non-Goals), Proposal (user stories, notes and caveats, Risks and
  Mitigations), Design Details (Test Plan, Graduation Criteria,
  Upgrade and Downgrade Strategy, Version Skew Strategy), a
  Production Readiness Review questionnaire, Implementation History,
  Drawbacks, Alternatives. It splits what is proposed from how: the
  Proposal gives "enough detail that reviewers can understand
  exactly what you're proposing, but should not include things like
  API designs or implementation"; those go to Design Details.
  Approval is by named KEP approvers for the status "implementable".
- PEP 12 (page modified 2026-03-04): Abstract, Motivation,
  Specification, Rationale ("why particular design decisions were
  made"), Backwards Compatibility, Security Implications, How to
  Teach This, Reference Implementation, Rejected Ideas, Open Issues.

**The description of a system.** arc42, the C4 model, the 4+1 view
model, ISO/IEC/IEEE 42010, IEEE 1016, TOGAF's building blocks and
the enterprise high-level and low-level design describe the system
as it stands and are meant to be kept current.

- arc42, twelve sections (documentation site and overview page):
  1 Introduction and Goals ("Requirements, stakeholder, (top)
  quality goals"); 2 Constraints; 3 Context and Scope; 4 Solution
  Strategy ("Fundamental solution decisions and ideas"); 5 Building
  Block View ("Abstractions of source code, black-/whiteboxes"); 6
  Runtime View ("how do building blocks interact"); 7 Deployment
  View; 8 Crosscutting Concepts ("Recurring solution approaches and
  patterns"); 9 Architecture Decisions ("Important, expensive, risky
  or contentious decisions"); 10 Quality Requirements; 11 Risks and
  Technical Debt; 12 Glossary. No length is prescribed; a one-page
  canvas exists for small systems.
- The C4 model: four levels of zoom (system context, containers,
  components, code), with the remark that "you don't need to use all
  4 levels of diagram; only those that add value - the system
  context and container diagrams are sufficient for most software
  development teams". C4 is a set of diagrams and says nothing on
  text; its FAQ maps the levels onto arc42's sections 3 and 5.
- The 4+1 view model (Kruchten, 1995, through Wikipedia): logical,
  process, development and physical views, each for a different
  stakeholder, plus scenarios, which "illustrate and validate the
  architecture design".
- ISO/IEC/IEEE 42010 (through Wikipedia and a secondary page of the
  arc42 quality site; the standard was not read): an architecture
  description identifies stakeholders and their concerns, answers
  them through views that follow viewpoints, records
  correspondences between elements, and records decisions with
  their rationale. It prescribes no sections.
- IEEE 1016-2009 (through Wikipedia; not read at source; listed
  there as "Inactive - Reserved"): a software design description is
  organised as design views, each following a viewpoint; twelve
  viewpoints are named (context, composition, logical, dependency,
  information, patterns use, interface, structure, interaction,
  state dynamics, algorithm, resource).
- TOGAF (secondary pages only; the standard is behind a login): an
  Architecture Building Block describes a required capability and
  shapes the Solution Building Blocks that implement it; an SBB
  specification holds functionality and attributes, interfaces,
  dependencies on other SBBs, performance and configuration,
  "design drivers and constraints", and its relation to the ABBs.
- High-level and low-level design (one secondary page): the HLD is
  written by a solution architect from the requirements
  specification and describes "the overall architecture of a system
  and shows how different components interact"; the LLD is written
  by designers and developers from the reviewed HLD and goes down to
  algorithms, data structures and interfaces.

What this means for "stays true", this note's synthesis: the first
family does not try. It is frozen at acceptance and read later as
the record of why. Ubl says so: design docs "tend to get out of sync
with reality over time" and yet remain "the most accessible entry
point to learn about the thinking that guided the creation of the
system". OpenSpec makes it a rule: at archive the `design.md` moves
with the change into the archive, while the specifications are kept
as the current truth. Only the second family promises a current
picture, and it is the one whose staleness is documented (finding
5).

### 2. The unit of content is one of four things: a section of prose, a building block, a decision, or a view [C]

Verified at the pages fetched unless marked.

- **A section of prose** in the design of a change (finding 1).
- **A building block**, in arc42's section 5. Its black box template
  is the nearest thing found to an item for a part: "Purpose/
  Responsibility", "Interface(s)", and four optional fields, among
  them "directory/file location", "Fulfilled requirements (if you
  need traceability to requirements)" and "Open
  issues/problems/risks". The section asks to describe the
  important, complex or risky blocks and not to aim at
  completeness, and to make every piece of source code locatable in
  the view (the last clause is the tool's paraphrase).
- **A decision.** Nygard's record (2011): Title, Context ("the
  forces at play"), Decision ("We will ..."), Status ("proposed",
  "accepted", "deprecated", "superseded"), Consequences ("All
  consequences should be listed here"); "one or two pages long";
  numbered and never reused; a reversed decision is kept and marked
  superseded. MADR 4.0.0 (2024-09-17) adds Decision Drivers,
  Considered Options, Pros and Cons of the Options, and
  Confirmation: "Describe how the implementation of/compliance with
  the ADR can/will be confirmed." The Y-statement (Zimmermann, 2020)
  folds a decision into one sentence: "In the context of
  [situation], facing [need], we decided for [choice] and neglected
  [alternatives] to achieve [benefits], accepting that [costs]"
  (the bracketed wording is the tool's rendering of the template).
  The AWS guide (read in full, undated): the records together are
  "the decision log"; "When the team accepts an ADR, it becomes
  immutable"; a rejected record keeps its reason "to prevent future
  discussions on the same topic"; the strength of the form is that
  it "focuses on the reason for the decision rather than how the
  team implemented it".
- **A view**, in 42010, 1016 and 4+1: the same system described
  once per concern.

Two points on which the sources agree. First, decisions are recorded
selectively. arc42 lists what deserves a record: decisions that are
critical, risky, expensive, long-lasting, unconventional or
"astonishing"; Zimmermann's first practice is to "prioritize by
significance". Second, arc42 itself has two homes for decisions,
section 4 for the few fundamental ones and section 9 for the rest,
and warns against stating one in both; where a decision is recorded,
centrally or beside the block it concerns, is left to judgement.

Zimmermann (2023, updated 2026-09-03) names the ways a decision
record goes wrong. Those that bear on a record written by an AI:
"Fairy Tale" (only pros), "Sales Pitch", "Dummy Alternative" (an
implausible option set up to lose), "Mega-ADR" (several designs in
one record), "Blueprint or Policy in Disguise", and deciding first
and justifying second. Among his practices: "Disclose confidence
levels".

### 3. The spec-driven tools let the agent write the design, a human approves it, and the design is optional in three of the four [E]

Verified at the pages and repository files fetched, except where
marked.

| Tool | The design document | Derived from | Written by, approved how | When skipped |
|---|---|---|---|---|
| Kiro | `design.md`: "technical architecture, sequence diagrams, and implementation considerations" | `requirements.md`, or nothing: a design-first order derives the requirements from the design | the agent; an approval step between phases | Quick Spec generates all three files "without approval gates" |
| spec-kit | `plan.md` (summary, technical context, constitution check, project structure, complexity tracking) with `research.md`, `data-model.md`, `contracts/`, `quickstart.md` | the specification and the constitution | the agent; errors on unresolved clarifications and on unjustified violations of the constitution | no skip found in the files read |
| BMad | a short architecture document, "the spine" | "a spec, a raw idea, a long architecture document to shorten, or an existing codebase, where it reads the real code and records the conventions already there" | the agent with the human: "Coaching is the default: the important calls are shown with the alternatives weighed, then you choose"; or "A Fast path drafts the whole spine with `[ASSUMPTION]` tags instead" | "Most changes do not" need one; a "clear, local change with established patterns" is "usually unnecessary" |
| OpenSpec | `design.md`: Context, Goals / Non-Goals, Decisions, Risks / Trade-offs (the template, read in full); the schema adds Migration Plan and Open Questions | the proposal only, not the specifications | the agent; no gate | "You can skip design if you don't need it"; created for cross-cutting changes, new dependencies, data model changes, security or performance complexity, "or ambiguity benefiting from pre-coding decisions" |

Four details matter for the forge.

- **BMad's spine is the most deliberate answer to duplication.** It
  "records only the decisions that would conflict if two people made
  them independently"; "A decision goes in the spine only when the
  answer is yes, the call is non-obvious, and it is a real
  trade-off. Everything else is left to the code"; "The stack, the
  folder tree, and the full data shape are starting points; the code
  owns them"; "Each decision gets a stable ID so specs and stories
  can cite it."
- **spec-kit keeps the decisions beside the plan**, in
  `research.md`, each as Decision, Rationale, Alternatives
  considered; departures from the constitution go to a Complexity
  Tracking table in the plan.
- **OpenSpec's template forbids the upward copy in a comment**: the
  Context is the "Current state and constraints that shape the
  approach. See proposal.md for motivation - don't restate it". Its
  schema asks to "Resolve any design Open Questions before writing
  tasks" (the tool's summary of the schema file).
- **Kiro's sections** as an independent reviewer saw them in 2025:
  a component architecture diagram, then "Data Flow, Data Models,
  Error Handling, Testing Strategy, Implementation Approach,
  Migration Strategy" (Boeckeler, 2025-10-15). Kiro's own page
  (2026-10-02) gives system architecture and component design,
  sequence diagrams and data flow, error handling and testing
  strategy.

What users report goes wrong:

- Boeckeler: "spec-kit created a LOT of markdown files for me to
  review. They were repetitive, both with each other, and with the
  code that already existed"; "To be honest, I'd rather review code
  than all these markdown files"; "I frequently got confused when to
  stay on the functional level, and when it was time to add
  technical details"; and an agent that took descriptions of
  existing classes for a new specification "and generated them all
  over again, creating duplicates".
- A practitioner guide to Kiro (search summary only; checked by its
  author against Kiro's documentation on 2026-08-25): someone edits
  the task list directly, nobody re-syncs, "and two weeks later the
  spec describes a design the code no longer follows"; and the sign
  of an over-specified change is "design.md restating
  requirements.md in different words".
- A search for user reports on spec-kit's plan files in its issue
  tracker returned nothing usable; none is cited.

### 4. Upward the design cites by identifier and does not restate; downward it names the place and leaves the detail there [C on the rule, X on whether links survive]

Verified at the pages fetched unless marked.

**Upward.**

- arc42 section 4 is a short table: quality goal, scenario, solution
  approach, link to the section with the detail; "Keep the
  explanation of these key decisions short."
- The building block's optional field "Fulfilled requirements (if
  you need traceability to requirements)" (finding 2).
- An ADR's Context, MADR's Decision Drivers and the Y-statement's
  "in the context of ..., facing ..." name the requirement that
  drives the decision; the AWS guide: "Functional and non-functional
  requirements are the most common inputs to the ADR process."
- The traceability matrix (Wikipedia) maps requirements to design,
  code and tests, and is the form known to decay: manual tracking is
  "cumbersome, error-prone, and often leads to traceability
  information that is of insufficient quality".

**Downward.**

- Ubl: no copying of formal interface or data definitions into the
  document, schemas only "in rough form", code only for novel
  algorithms; a document that is "This is how we are going to
  implement it" with no trade-offs should have been the program.
- BMad: "the code owns them" (finding 3).
- arc42: the optional "directory/file location" of a block.
- MADR's Confirmation names the check, "a design/code review or a
  test with a library such as ArchUnit". The AWS guide uses the
  record in code review: a reviewer who finds a change that violates
  a record "shares a link to the ADR".
- Fitness functions (Paul and Wang, 2019-01-11) make a design aim
  executable: they measure "how close an architecture is to
  achieving an architectural aim", run as tests in the pipeline.

**What keeps a living description alive.**

- Docs as code (Write the Docs): the same tools as code, among them
  version control, plain text markup, reviews and automated tests.
- Google (the book chapter): documentation under source control,
  with "clear ownership", changed "with the code it documents",
  with freshness dates and reminders, and removed or marked when
  obsolete; the wiki before it failed because "many became
  obsolete".
- Living documentation (Martraire, through Hilton, 2021): reliable
  "thanks to automated checks and manual reconciliation with its
  implementation"; knowledge worth writing is of long-term interest
  and wide relevance, and knowledge that is cheaply recreated is
  not written.

This note's synthesis: the practices that work share one rule. The
document holds what cannot be read off the thing itself: why, what
it was chosen against, what it must not become, how the parts fit.
What can be read off the thing is linked, generated or left out. A
link upward is a cited identifier at the item, not a matrix kept by
hand; a link downward is a path, with a check that the path still
exists and still honours the decision.

### 5. Design documents go stale, and the evidence is practitioners' reports and a few studies not read at source [C that they do; the numbers unverified]

- Ubl: updates after shipping accumulate as amendments, "a state
  more akin to the US constitution with a bunch of amendments rather
  than one consistent piece of documentation" (verified, two
  readings).
- Wan et al., ESEC/FSE 2023 (abstract read): interviews with 32
  practitioners in 21 organisations; documentation is one of four
  areas of difficulty in architecture practice. That most
  participants saw design documentation and code drift apart is from
  a search summary of the paper, not the abstract.
- A Fraunhofer IESE survey (search summary only; the PDF could not
  be read): 147 industrial participants; architecture documentation
  frequently outdated and updated with strong delay; developers find
  a one-size-fits-all architecture document unfit for their tasks.
- A case study on loss of architectural knowledge (Feilkas et al.,
  2009; search summary only): between 70 and 90 per cent of the
  inconsistencies between documentation and code were flaws of the
  documentation.
- Boeckeler names three ambitions for a specification: spec-first
  (written before, then left), spec-anchored (kept after
  completion), spec-as-source (the specification is what is edited
  and the code is generated). Staying true is a property only the
  second and third claim, and the third is the one she likens to
  model-driven development (the layers note, finding 9).

Looked for and not found: a study showing that any one form of
design document stays current longer than another.

### 6. Open matters are kept as a list in the design, sorted by when they must be closed, and closed by a time-boxed trial [C]

Verified at the pages fetched unless marked.

- The Rust RFC template sorts its unresolved questions three ways:
  to be resolved "through the RFC process before this gets merged",
  "through the implementation of this feature before stabilization",
  and "out of scope for this RFC" for a later proposal.
- PEP 12: Open Issues, "Any points that are still being
  decided/discussed", beside Rejected Ideas.
- OpenSpec: Open Questions in the design, to be resolved before
  tasks are written (finding 3).
- arc42 section 11: "a prioritized list of identified technical
  risks or technical debts", each with a suggested way to mitigate
  or reduce it; the optional "Open issues/problems/risks" of a
  building block is the local form.
- KEP: Risks and Mitigations inside the Proposal, and Graduation
  Criteria saying what must be shown before the feature moves from
  alpha to beta to general availability: a hypothesis with its
  proof named in advance.
- Spikes (SAFe page, the public part): "Defined initially in Extreme
  Programming (XP)", their purpose "to gain the knowledge necessary
  to reduce the risk of a technical approach, better understand a
  requirement, or increase the reliability of a story estimate";
  they are estimated and demonstrated like other work. That a spike
  is time-boxed and its code thrown away is common knowledge not
  verified at a page in this session (the guideline text is behind a
  login; the Agile Alliance glossary page was not found).
- BMad's `[ASSUMPTION]` tag marks, at the decision itself, a choice
  the agent made without the human (finding 3).
- Zimmermann's strong justification is evidence of this kind: "We
  performed a Proof-of-Concept and results were convincing".

### 7. Solutions that are not software have the same three things, and add who does it [C on the forms, the comparison is this note's]

Verified at the pages fetched unless marked.

- **Options appraisal** (the Green Book, HM Treasury, 2026 edition,
  updated 2026-02-05). A longlist is narrowed by an options
  framework of five categories of choice: scope, solution, delivery,
  implementation, funding. Each choice is rated against critical
  success factors; red choices are discarded. The shortlist
  includes business as usual, a do-minimum option, the "preferred
  way forward" and a more and a less ambitious variant. The record
  of rejection is required: "Practitioners should explain
  transparently what options have been considered as well as the
  reasons they have or have not been progressed to shortlist
  appraisal."
- **The service blueprint** (Gibbons, 2017-08-27, reviewed
  2026-07-15): "a diagram that visualizes the relationships between
  different service components - people, props (physical or digital
  evidence), and processes"; its rows are customer actions,
  frontstage actions, backstage actions and support processes,
  divided by the lines of interaction, of visibility and of internal
  interaction. The unit is a step in a lane.
- **The target operating model** (Wikipedia): the desired state of
  how an organisation works, described in six elements (processes
  and capabilities, organisation, locations, information, suppliers,
  management systems) or as people, process and technology; from a
  one-page canvas to a hundred pages, beyond which it "becomes a
  manual rather than a model".
- **The concept of operations** (Wikipedia, citing the IEEE
  standard): a narrative of the proposed system "from the viewpoint
  of an individual who will use that system", with goals, policies
  and constraints, the organisations and their interactions, and
  "clear designation of responsibilities and authorities".
- **A process design** (search summary only): purpose and scope,
  entry and exit criteria, inputs and outputs, the flow, the
  activities, exceptions, business rules, roles and
  responsibilities, measures.

The same shape carries over: parts (steps, roles, elements), choices
with what they were chosen against, and what is open. Two things are
added. The part is something done by someone, so each part names who
does it. And the appraisal always sets the choice against doing
nothing and against the least that would meet the objective, which
the software forms ask only in passing (the RFC's "What is the
impact of not doing this?").

### 8. Whether what is wanted and how it is realised can be kept apart is contested; the documents can be, the work cannot [X]

- **Kept apart, as a rule.** spec-kit's specification excludes the
  how (the layers note, finding 9). OpenSpec: specifications define
  "observable behavior ... not implementation details". The KEP
  keeps API designs out of the Proposal. arc42 keeps goals,
  constraints and quality requirements in sections of their own.
  TOGAF separates the capability required (ABB) from the product
  that implements it (SBB).
- **Not separable in the work.** The Twin Peaks model (Nuseibeh,
  2001; through a secondary page and a search summary, the paper
  not read): requirements and architecture are developed
  "iteratively and in parallel", each refining the other, while
  "their distinct content is preserved". Kiro offers a design-first
  order in which the requirements are derived from the design.
  Boeckeler found the line hard to hold in practice (finding 3).
- **A given solution choice is a constraint.** arc42's section 2
  holds "Technical and organizational constraints, conventions":
  what the design must honour and did not decide. spec-kit's
  constitution and Kiro's steering files play the same part; a
  departure from the constitution must be justified in the plan.
  This is the outside world's home for a principle the owner sets
  for the solution.
- **Observable behaviour is counted as requirement.** In OpenSpec
  and spec-kit, what a user or another system sees (inputs, outputs,
  errors) belongs to the specification even though another
  realisation would change it.

### 9. What is known to fail [C unless marked]

| Failure | Where it is described |
|---|---|
| The design restates the layer above | the Kiro guide (search summary); OpenSpec's "don't restate it" |
| The design restates the thing below | Ubl (copied schemas and interfaces; the "implementation manual"); Boeckeler ("repetitive ... with the code that already existed") |
| A living description drifts from the thing | finding 5 |
| The document becomes a pile of amendments | Ubl; the layers note, finding 10 |
| A traceability matrix kept by hand decays | Wikipedia on requirements traceability |
| Decisions justified after the fact, with a dummy alternative | Zimmermann 2023 |
| One record holding a whole design | Zimmermann's "Mega-ADR" and "Novel/Epic" |
| Everything recorded, nothing significant | arc42 FAQ; Zimmermann; BMad's three-part test |
| The volume generated by an agent exceeds what a human will review **[E]** | Boeckeler 2025 |
| An agent reads a description of what exists as an order to build it **[E]** | Boeckeler 2025 |
| A design for work that needed none **[E]** | OpenSpec, BMad, Kiro's quick form, Ubl's cost-benefit question |

## Options and trade-offs

Findings and options only. A new prefix, section or layer is the
principal's decision; nothing below is a convention.

### The kinds of items

**A. One kind of item: a part, with its decision inside.** The item
says what is built or done, which positions it realises, the choice
it rests on with what it was chosen against and why, and where it
lives. *For:* the arc42 black box plus a Y-statement is exactly this
and both are established (finding 2); one kind keeps the document
short and each part readable alone; fits the forge's rule of
structure over prose. *Against:* a decision that spans several parts
has no natural home and would be repeated or hung on one part
arbitrarily, which is why arc42 has sections 4, 8 and 9 beside
section 5; a part with no real choice gets a hollow "chosen
against", the Dummy Alternative.

**B. Two kinds: parts and decisions.** Parts say what and where;
decisions say why, against what, at what price, and name the parts
they bind. *For:* the arc42 division; a cross-cutting decision is
stated once; a part with no choice carries none. *Against:* two
kinds and the links between them, in a document that must also link
up and down; the reader of one part must follow links to know why it
is as it is.

**C. Decisions only.** The document is the list of choices that
would otherwise be made inconsistently; the parts are whatever the
files are. *For:* BMad's spine and a decision log; the least
duplication of the thing below, since nothing describes it; the
shortest to keep true. *Against:* no picture of the whole, so it
does not serve the principal's stated aim of asking for a proposal
of the whole solution and working over it; nothing says which
position is realised where, so the coverage question cannot be
asked.

**D. Views or sections with prose.** A design doc or an arc42
document. *For:* the commonest form; carries flow and reasons well.
*Against:* against prime directive 7; no stable IDs for the layers
below or the files to cite; prose is the form in which amendments
pile up.

### How it cites what stands above

1. **By identifier at the item** (arc42's "Fulfilled requirements",
   BMad's stable IDs). Cheap, local, checkable mechanically.
2. **A coverage map made at the pass and not kept**: positions with
   no part, parts with no position. The assignment's definition has
   this already as the provenance map of its joint pass, "a tool of
   the pass, not part of the assignment". One mechanism for two
   layers.
3. **A matrix kept in the document.** The form known to decay.
4. **No citation, and a reviewer's test of drift.** The forge has
   the lens `essence` for that; alone it finds drift and cannot show
   what is missing.

### How it cites what realises it below

1. **The item names the path**, and the detail is the file's
   (arc42's file location; the rule the intent's definition already
   states under "Threads and files", including its exception: where
   the realisation is only part of a file, the item keeps the full
   information).
2. **The file names the item back.** The forge's files do this
   today toward the intent (the state files cite the POS that says
   what they are to achieve). Two directions are two things to keep.
3. **A check as the fitness function**: every named path exists,
   every file of the realising layer is named by some item, and the
   file does not contradict the decision. The forge's check `engine`
   does the equivalent today against the intent.
4. **Generated from the thing.** An inventory of files can be
   generated; reasons cannot.

### What the Map could name

In the manner of the three existing Map blocks: areas the finding
looks at, any of which may stay empty when considered and found not
to apply. Each has a precedent given in brackets.

- what is to be realised: the positions and boundaries the design
  answers, and what of them it knowingly leaves unanswered (42010's
  concerns; arc42 1 and 10);
- the ground: what already exists and must be kept or replaced, the
  outside systems, and what the principal has fixed in advance
  (arc42 2 and 3; Ubl's degree of constraint; BMad reading the
  existing code);
- the approach as a whole: the few ideas the solution rests on
  (arc42 4; the overview of a design doc);
- the parts: what is built or done, by whom where it is not
  software, and where each lives (arc42 5; TOGAF's SBB; the service
  blueprint);
- how the parts work together: the main courses of events (arc42 6;
  the scenarios of 4+1);
- what holds across the parts (arc42 8; Ubl's cross-cutting
  concerns);
- the choices: for each real one, what it was chosen against,
  including doing nothing or the least that would do, why, and what
  it costs (ADR, the RFC's drawbacks and rationale, the Green Book);
- what is unproven or open: by what trial each would be settled and
  what must be settled before realisation starts (the RFC's three
  classes; arc42 11; spikes; KEP graduation criteria);
- how it will be known to hold: by what check the thing is compared
  with the design (MADR's Confirmation; fitness functions; the KEP
  test plan);
- the way there, where the solution replaces something that runs
  (KEP upgrade strategy; OpenSpec's Migration Plan);
- what is deliberately not designed and left to the file or to the
  one who realises (BMad: "Everything else is left to the code";
  non-goals).

## What was not found

- ISO/IEC/IEEE 42010:2022 and IEEE 1016-2009 at source. Both are
  described through Wikipedia and one secondary page; no clause is
  quoted. The site of the 42010 working group refused the
  connection.
- The TOGAF standard at source (redirects to a login). Building
  blocks are described through a vendor's guide and a search
  summary.
- The Fraunhofer survey (PDF not readable by the tool), the full
  text of Wan et al. 2023, Feilkas et al. 2009 and Nuseibeh 2001.
  Their numbers and claims are marked where used.
- The Y-statement's original article (refused); the template is
  from its author's own later post.
- SAFe's guideline text on spikes (behind a login) and the Agile
  Alliance glossary entry (not found).
- Who approves a PEP and how; not fetched, and left out.
- A list of Kiro's design sections in Kiro's own words beyond the
  three phrases quoted; the fuller list is a reviewer's of 2025.
- User reports on spec-kit's plan files from its own issue tracker.
- Any source in which a human hands the whole design to an agent and
  the proposal opens with a list of what was assumed and chosen.
  The nearest is BMad's Fast path, which tags assumptions at each
  decision.
- Any framework whose design layer may hang directly under a
  document of the owner's stances with no requirements in between
  and is kept as a current description. OpenSpec's design hangs
  under a proposal, and is a design of a change.
- Not surveyed: design practice in hardware and construction, where
  the drawing set and the specification have their own rules of
  precedence.

## Relevance to this project

### The four hypotheses

**1. The test "would the sentence still hold if the thing were
realised in a wholly different way?", and a principle set for the
solution is intent, the mechanism that honours it solution.**
Precedent for the division is consensus (finding 8, first group),
and the second half has a named home outside: the constraint, which
the design must honour and did not decide. Three things the test
misses, this note's own reading. First, a constraint fails the test
on its face: a sentence such as "everything is Markdown under git"
would not hold under another realisation, yet it is the principal's
and belongs above. The second half of the hypothesis is therefore
not a gloss but a second criterion, and the two need an order: first
"did the principal fix this, whatever the solution", then the
counterfactual. Second, observable behaviour: the names of commands
and what the user sees would change with the realisation, and the
outside tools still count them as specification. The hypothesis
would send them to the solution; that is defensible for a principal
who is his own user, and it should be a decision, not an accident
of the test. Third, the Twin Peaks finding: the division holds for
documents and not for the order of work. Designing will move the
intent; the forge's rule of intent-first already gives the way back,
and the design's definition would need to say that a finding of the
design which changes what is wanted returns to the intent.

**2. Derived from the intent directly, or from an assignment or a
BRD; many projects need none.** Supported throughout (finding 3):
BMad's architecture takes a spec, a raw idea or existing code;
OpenSpec's design depends on the proposal alone; three tools of four
make it optional. What it misses is a stated criterion for when one
is written. OpenSpec's list and BMad's test are the two found; both
come to this: write it where a choice is non-obvious, a real
trade-off, and would be made inconsistently if left unwritten. A
second gap: BMad also derives the document from what already
exists. The forge's own case is that one, a design recovered from
skills, templates and scripts that already run, and it is a
different piece of work from designing forward.

**3. The principal may hand the whole to the AI, which returns a
proposal stating at its head what it assumed and what it chose, with
what each choice was chosen against.** There is precedent for the
handing over (every tool in finding 3 has the agent write the
design; BMad's Fast path and Kiro's Quick Spec skip the dialogue)
and for marking assumptions (BMad's tag). Three cautions. BMad's
default is the other mode, the important calls shown with their
alternatives and the human choosing, and the fast mode is the
exception. The reported failure of agent-written designs is volume
that nobody reviews (finding 9), so the proposal is only as good as
its selectivity: the few real choices, not every part. And an
alternative written after the choice is the Dummy Alternative; a
plain "no real alternative was considered" is more honest than an
invented one, and Zimmermann's "disclose confidence levels" is the
matching practice. The head-of-document list itself has no
precedent found; it is consistent with a design doc's overview and
cheap to try.

**4. One kind of item, "SOL", a part with its choice inside; open
matters as TBC; facts cited from the intent; a part realised in a
file of its own names the file and leaves the detail there.** The
item has close precedent: arc42's black box (responsibility, file
location, fulfilled requirements, open issues) with a Y-statement
for the choice. The rule for files is the practice that works
(finding 4) and is already the forge's own, in the intent's
definition. What it misses:

- the price of a choice: every decision form has consequences or
  "accepting that", the draft has only "against" and "why";
- matters that hold across parts, and how the parts work together:
  a list of parts shows neither (arc42 6 and 8);
- a state for a choice: proposed by Claude or accepted by the
  principal. The outside forms keep this in a status field; the
  forge's body is the current state and its companion the record,
  so superseded choices need no field, but "assumed, not yet
  judged" does need to be visible;
- how an open matter is closed and by when: the outside forms sort
  open questions by what must be settled before realisation and
  what is settled by it (finding 6). THR.0520 names "a hypothesis to
  verify" as a kind the solution needs; a TBC with its trial and its
  deadline may be enough, and whether TBC, which the ID scheme
  places in the assignment, may also live here is a change of
  convention for the principal;
- a check: nothing in the draft says how the design is known to
  hold against the files. The check `engine` is the forge's fitness
  function and would be pointed at the design;
- the exception of the partial file: where the realisation is a
  section of a shared file, the forge's rule keeps the full
  information in the item. Much of the forge's solution lives in
  sections of CLAUDE.md, so for the forge's own project the promise
  "repeats nothing a file carries" holds only as far as the
  realisation sits in files of its own.

### Recommendation

Each point is a proposal for the principal, to be worked in THR.0520
through `/forge intent`.

1. **Decide first which family it is.** A description of the
   solution as it stands, kept current, or the design of a change,
   frozen when realised. The forge's regime (the body is the current
   state, the history beside it) makes it the first, the family
   known to go stale. That is workable only with the three
   protections the sources agree on: the document holds what cannot
   be read off the files, it links and does not copy, and a check
   compares it with the files.
2. **Items: option A, with two additions and one trial.** One kind
   of item for a part, carrying its choice in the Y-statement's
   terms where there was a real choice (decided for, against what,
   to achieve what, accepting what) and nothing where there was
   none. Add an item of the same kind for what holds across parts,
   so that a cross-cutting choice is stated once. Add a short head
   in prose: the approach as a whole and, where Claude drafted it,
   what was assumed. Reason: it is the smallest form with precedent
   that still gives a picture of the whole, which option C does not.
   Try it on one real project before a template is fixed; if
   choices spanning parts turn out to be the rule, option B is the
   known remedy.
3. **Upward: the identifier at the item, and the provenance map of
   the assignment's joint pass reused as the coverage tool.** No
   matrix in the document.
4. **Downward: the path at the item, the existing rule of
   "Threads and files" applied as it stands, and the check as the
   test that the design still holds.** Whether the files cite the
   design or the intent is a separate decision with a cost in every
   file.
5. **The Map: the eleven areas listed under Options as the
   candidate**, to be cut by the principal. The two that the draft
   idea lacks and the sources insist on are "how it will be known
   to hold" and "what is deliberately not designed".
6. **When to write one: a criterion, not a rule.** A solution design
   where a choice is non-obvious, a real trade-off, and would be
   made differently by two realisers; otherwise none.
7. **For the dividing test: state the two criteria in order**, the
   principal's fixed word first, the counterfactual second, and
   decide knowingly where observable behaviour goes.

### What stays uncertain, and whether more research would change it

Uncertain: the standards and the staleness studies were not read at
source, so no clause or number from them should be relied on; no
source shows a design layer of this exact position and regime, so
the recommendation is assembled from parts with precedent and not
copied from a whole; whether one kind of item is enough is a
question only a trial answers.

More reading is unlikely to move the recommendation on the item, the
citations or the Map: the sources agree and the gaps are in the
standards' wording, not their substance. Two things could move it.
A trial of the division on a real intent would show how many choices
span parts and how much of the solution sits in partial files. And a
closer reading of practice outside software (construction and
hardware, where drawing and specification have rules of precedence)
could add to the question of what prevails when the design and the
thing disagree, which no source read here answers.

## Sources

All fetched 2026-10-03.

**Design of a change**

- Malte Ubl, Design Docs at Google - https://www.industrialempathy.com/posts/design-docs-at-google/ - 2020-07-06 (two readings)
- Rust RFC template - https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md - undated (full text)
- Kubernetes KEP template - https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md - undated
- PEP 12, Sample reStructuredText PEP Template - https://peps.python.org/pep-0012/ - modified 2026-03-04
- Software Engineering at Google, chapter 10, Documentation - https://abseil.io/resources/swe-book/html/ch10.html - book of 2020

**Description of a system**

- arc42 documentation, overview of sections - https://docs.arc42.org/home/ - undated
- arc42 template overview - https://arc42.org/overview - undated
- arc42, section 4 Solution Strategy - https://docs.arc42.org/section-4/
- arc42, section 5 Building Block View - https://docs.arc42.org/section-5/
- arc42, section 8 Crosscutting Concepts - https://docs.arc42.org/section-8/
- arc42, section 9 Architecture Decisions - https://docs.arc42.org/section-9/
- arc42, section 11 Risks and Technical Debt - https://docs.arc42.org/section-11/
- arc42 FAQ, C-9-1, What kind of decisions shall I describe or document? - https://faq.arc42.org/questions/C-9-1/
- C4 model, diagrams - https://c4model.com/diagrams - undated
- C4 model, FAQ - https://c4model.com/faq - undated
- ISO/IEC 42010, Wikipedia - https://en.wikipedia.org/wiki/ISO/IEC_42010 (secondary)
- ISO/IEC/IEEE 42010:2022, arc42 quality site - https://quality.arc42.org/standards/iso-42010 (secondary)
- Software design description (IEEE 1016), Wikipedia - https://en.wikipedia.org/wiki/Software_design_description (secondary)
- 4+1 architectural view model, Wikipedia - https://en.wikipedia.org/wiki/4%2B1_architectural_view_model (secondary)
- What is Solution Building Blocks (SBBs) in TOGAF ADM - https://togaf.visual-paradigm.com/?p=200 - 2023-10-10 (secondary)
- Difference between High Level Design and Low Level Design - https://www.geeksforgeeks.org/system-design/difference-between-high-level-design-and-low-level-design/ - undated (secondary, weak)

**Decision records**

- Michael Nygard, Documenting Architecture Decisions - https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions - 2011-11-15
- MADR, Markdown Architectural Decision Records - https://adr.github.io/madr/ - version 4.0.0, 2024-09-17
- Architectural Decision Records, home - https://adr.github.io/ - undated
- Olaf Zimmermann, Architectural Decisions: The Making Of - https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html - 2020-04-27
- Olaf Zimmermann, How to create Architectural Decision Records and how not to - https://ozimmer.ch/practices/2023/04/03/ADRCreation.html - 2023-04-03, updated 2026-09-03
- AWS Prescriptive Guidance, ADR process - https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html - undated (full text)

**Spec-driven tools**

- Kiro documentation, Specs - https://kiro.dev/docs/specs/ - 2026-10-02
- Kiro documentation, Feature specs - https://kiro.dev/docs/specs/feature-specs/ - undated on this reading
- Kiro documentation, Specs best practices - https://kiro.dev/docs/specs/best-practices/ - 2026-09-25
- spec-kit, plan template - https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md
- spec-kit, plan command - https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md
- BMad Method documentation, Design UX and Architecture - https://docs.bmad-method.org/plan/design-ux-and-architecture/ - undated (two readings)
- BMad Method documentation, Choose a Planning Path - https://docs.bmad-method.org/plan/choose-a-planning-path/
- OpenSpec, design template - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/schemas/spec-driven/templates/design.md (full text)
- OpenSpec, schema of the spec-driven workflow - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/schemas/spec-driven/schema.yaml
- OpenSpec, concepts - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/concepts.md
- Birgitta Boeckeler, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html - 2025-10-15

**Links, staleness and checks**

- Requirements traceability, Wikipedia - https://en.wikipedia.org/wiki/Requirements_traceability (secondary)
- Docs as Code, Write the Docs - https://www.writethedocs.org/guide/docs-as-code/ - undated
- Peter Hilton, Principles of living documentation - https://hilton.org.uk/blog/living-documentation-principles - 2021 (secondary, on Martraire's book)
- Peter Hilton, Martraire's principles of documentation - https://hilton.org.uk/blog/martraire-documentation-principles - 2021-05-18 (secondary)
- Paula Paul and Rosemary Wang, Fitness function-driven development - https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development - 2019-01-11
- Z. Wan et al., Software Architecture in Practice: Challenges and Opportunities - https://arxiv.org/abs/2308.09978 - ESEC/FSE 2023 (abstract only)
- Twin Peaks model - https://t2informatik.de/en/smartpedia/twin-peaks-model/ - undated (secondary)
- Spikes, Scaled Agile Framework - https://framework.scaledagile.com/spikes - undated (public part only)

**Solutions that are not software**

- The Green Book (2026), HM Treasury - https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026 - updated 2026-02-05
- Sarah Gibbons, Service Blueprints: Definition - https://www.nngroup.com/articles/service-blueprints-definition/ - 2017-08-27, reviewed 2026-07-15
- Target operating model, Wikipedia - https://en.wikipedia.org/wiki/Target_operating_model (secondary)
- Concept of operations, Wikipedia - https://en.wikipedia.org/wiki/Concept_of_operations (secondary)

**Search results only** (summaries returned by the search tool; used
only where the text says so)

- Fraunhofer IESE, survey on software architecture documentation for developers - https://www.iese.fraunhofer.de/content/dam/iese/dokumente/alte-dateien/study_software_architecture_documentation_for_developers_survey-en-fraunhofer_iese.pdf - PDF not readable
- M. Feilkas et al., The Loss of Architectural Knowledge during System Evolution, 2009 - https://wwwbroy.in.tum.de/publ/papers/2009_icpc_feilkas.pdf
- Kiro spec-driven development, a practitioner guide - https://www.verdent.ai/guides/agents/kiro-spec-driven-development
- Summaries of B. Nuseibeh, Weaving Together Requirements and Architectures, 2001
- Summaries of TOGAF's Architecture Definition Document and building blocks
- Summaries of process documentation templates

**Tried and not readable** (nothing is cited from these)

- The Open Group, TOGAF standard, architecture content: redirects to a login.
- ISO/IEC/IEEE 42010 working group site, conceptual model: connection refused.
- O. Zimmermann, Y-Statements (Medium): refused.
- Agile Alliance glossary, Spike: not found.
- Architecture decision record, Wikipedia: not found under the address tried.
- BMad documentation index file: not found.
- C4 model home page: returned too little to use.
