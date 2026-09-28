---
project: forge
type: research
topic: artefact layers from idea to handover - how disciplines and tools define them, what each must contain and when it is complete
date: 2026-09-28
derived_from: 00-brief-elicitation.md v0.5
status: immutable
---

# Artefact layers from idea to handover

## Question

How do established disciplines and current tools define the layers of
documents that stand between a raw idea and the handover of work -
what each layer is for, what it must contain, and when it counts as
complete - and what does that say about the forge's brief, intent and
assignment?

The research looks outward. The comparison with the forge is kept to
the last section.

Surveyed on 2026-09-28: military doctrine on commander's intent and
mission orders (US Army, US Marine Corps, through secondary pages
that quote the doctrine); project method (PRINCE2 mandate, brief and
initiation documentation; the PMBOK project charter; the statement of
work of US defence acquisition); requirements engineering
(ISO/IEC/IEEE 29148, BABOK, both through secondary pages); product
practice (Shape Up, Amazon's PR/FAQ, the PRD and its critics, design
docs at Google, the Rust RFC template, architecture decision
records, the Now-Next-Later roadmap, the Definition of Ready);
advertising (the client brief and the creative brief); and four
spec-driven tools for work with AI agents (GitHub spec-kit, AWS Kiro,
the BMad Method, OpenSpec), with one independent review of them.

Epistemic tags: **[C]** consensus across the sources read, **[E]**
emerging, **[X]** contested. Where a statement rests on a secondary
page, or on memory, it says so. Quotations are as the fetch tool
returned them from the page; see "What was not found" for what that
means for their reliability and for which of them were checked a
second time.

## Key findings

### 1. Nearly every discipline has a ladder of about three steps, and none has the forge's three [C for the ladder, the mapping is this note's own]

The steps recur under different names: something that triggers the
work, something in which the thinking is worked out, and something
handed to those who will act.

| Discipline or tool | Trigger, raw | Worked understanding | Handed over |
|---|---|---|---|
| PRINCE2 | project mandate | project brief, then project initiation documentation | not read in this session |
| PMBOK | business case, needs | project charter | not read in this session |
| Military doctrine | the situation, the higher intent | commander's intent | mission orders, the intent inside them |
| ISO/IEC/IEEE 29148 | not a document | business and stakeholder requirements specifications | system and software requirements specifications |
| BABOK | business need | business and stakeholder requirements | solution requirements |
| Advertising | client (marketing) brief | the planner's work | creative brief |
| Shape Up | raw idea | shaping, behind closed doors | pitch |
| Amazon | idea | PR/FAQ in many drafts | the approved PR/FAQ |
| spec-kit | a prompt | spec, clarifications, research | plan, tasks |
| Kiro | a prompt | requirements, design | tasks |
| BMad Method | brainstorm, idea under test | brief, PRFAQ or PRD | spec |
| OpenSpec | not a document | proposal | delta specs, tasks |

Three observations hold across the table. The top step is a document
in few places only: PRINCE2 names it (the mandate), Shape Up and
Amazon treat it as something one reacts to, the AI tools reduce it to
a prompt. The middle step is where the documents multiply and where
the disciplines differ most. The bottom step is everywhere the one
with the strictest rules of content and wording.

Sources: PRINCE2 wiki (project brief; starting up a project); the
Wikipedia article on the project charter, citing the PMBOK Guide,
8th edition, 2025; Modern Requirements on ISO 29148 (2026-07-16);
Techcanvass on the BABOK classification; Shape Up chapters 2, 5, 6,
7, 10; Working Backwards pages; spec-kit, Kiro, BMad and OpenSpec
documentation.

### 2. Elsewhere "brief" names a short direction written for someone else, not the owner's raw idea [C]

- The **creative brief** is one to two pages written by a strategist,
  planner or account manager to direct a creative team: objectives,
  audience, a single-minded proposition, deliverables, timing. One
  guide puts the limit plainly: "Anything longer becomes a strategy
  document." It is derived from the client's brief, which states the
  business problem.
- The **PRINCE2 project brief** is written by the project manager
  from the project mandate, for the board's decision whether to
  authorise initiation. It has quality criteria: concise, reflecting
  the mandate, SMART objectives, scope boundaries, more than one
  delivery option considered. Once the initiation documentation
  exists it "is no longer used in project management activities".
- The **BMad product brief** is "a one- to two-page account of the
  product concept", used when the concept is already clear.

What matches the forge's brief in kind is the step above: the
PRINCE2 **project mandate**, which comes from outside the project
and "may contain limited or detailed information depending on the
source"; the **raw idea** Shape Up reacts to; the first draft of an
Amazon press release, which "should take only a few hours, not a few
days".

Sources: admove.ai guide (2026-08-17, weak source); Genero
practitioner interviews (no date, weak source); PRINCE2 wiki;
BMad documentation; workingbackwards.com.

### 3. The upper layer is deliberately lighter everywhere, but "short" and "rough" are two different properties [C]

**Rough on purpose.** Shape Up states the reason most clearly. Work
handed to a team must be at the right level of abstraction:
wireframes are too concrete ("they define too much detail too
early"), words alone too abstract (the team does "not have enough
information to make trade-offs"). Shaped work has three properties:
**rough**, **solved** (the main elements are there and connect) and
**bounded** (it "indicates what not to do"). PRINCE2's first process
does "the minimum necessary to decide whether proceeding with the
project is worthwhile". The Now-Next-Later roadmap portions certainty
out over horizons: what is now is specified, what is later stays
hazy on purpose.

**Short but not rough.** The creative brief and the commander's
intent are short because they are distilled, not because they are
unfinished. Doctrine as quoted by secondary pages: "The shorter the
commander's intent, the better it serves these purposes. Typically,
the commander's intent statement is three to five sentences long"
(FM 3-0, 2008, as quoted by Baillergeon and Sutherland); a
practitioner in 2022 gives "five to six lines". Amazon caps the
press release at under one page and the FAQ at five pages, and
reaches that through "ten drafts of the PR/FAQ or more".

The reason given for roughness is in every case the freedom of those
who act next: the builders, the creatives, the subordinates. No
source read gives the reason that the same author has a later layer
of his own in which the chiselling is done.

Sources: Shape Up chapters 2 and 3; PRINCE2 wiki; ProdPad
(2022-10-18); Armchair General (2008-06-13); From the Green
Notebook (2022-05-17); About Amazon excerpt of *Working Backwards*
(book of 2021).

### 4. Completion is stated in four ways, and the gate is the contested one [C for the four, X for the gate]

- **By decision of an authority.** The project board authorises
  initiation on the project brief; the charter "formally authorizes
  the project"; a PR/FAQ is done when "a go, no-go decision can be
  made"; a pitch is done when it is bet on, and it is "only ready to
  bet on when problem, appetite, and solution come together".
- **By a test on the reader.** The commander's intent "helps
  subordinate and supporting commanders act to achieve the
  commander's desired results without further orders, even when the
  operation does not unfold as planned" (ADP 6-0, 2019, paragraph
  1-45, as quoted by Everett 2022). A statement of work must let the
  contractor estimate cost and identify resources. BMad: a
  well-defined intent is "complete enough that someone else could
  build it without guessing".
- **By markers that must be gone.** spec-kit marks every unknown in
  the specification as `[NEEDS CLARIFICATION: specific question]`
  ("Don't guess"), and its completeness checklist requires that none
  remain, that requirements are testable and success criteria
  measurable; the planning step raises an error on "unresolved
  clarifications".
- **By a coverage map.** spec-kit's `clarify` step scans the
  specification against ten named categories, the last of them a
  catch-all, gives each the status Clear, Partial or Missing, asks
  at most five questions ("Maximum of 5 total questions across the
  whole session"), "EXACTLY ONE question at a time", and ends with a
  table in which every category is Resolved, Deferred, Clear or
  Outstanding. The taxonomy is a map for choosing what to ask, not a
  questionnaire.

The **Definition of Ready** is the contested form. It is not part of
the Scrum Guide; Pichler, who described it in 2010 (clear, testable,
feasible), adds that "once an effective collaboration has been
established, a DOR is usually no longer required"; critics hold that
it turns into a contract and a phase gate. The critics' own pages
could not be opened; the criticism is known here from a search
summary only.

Sources: PRINCE2 wiki; Wikipedia on the project charter;
workingbackwards.com; Shape Up chapter 6; From the Green Notebook;
AcqNotes on the statement of work (updated 2024-02-09); BMad
documentation; spec-kit `spec-driven.md`, `spec-template.md`,
`clarify.md`, `plan.md`; Roman Pichler (2010-12-16, updated
2024-02-02).

### 5. Rejected alternatives live in the working layer or beside it, never in what is handed over [C]

Four homes were found:

- **A fixed section of the working document.** Design docs at Google
  carry "Alternatives considered" and "Goals and non-goals", where a
  non-goal is something that could reasonably be a goal and was
  chosen not to be. The Rust RFC template carries "Rationale and
  alternatives", "Prior art", "Unresolved questions" and "Future
  possibilities".
- **A side file of the working layer.** spec-kit's `research.md`
  records each choice as Decision, Rationale, Alternatives
  considered. BMad keeps an `addendum.md` beside the brief and the
  PRD for rejected alternatives and overflow, and its idea-testing
  step writes a file that "records the decisions, the rejected
  options, and the reasons later skills need".
- **Separate, immutable records.** An architecture decision record
  holds context, decision, status and consequences on one or two
  pages; a reversed decision stays and is marked "deprecated" or
  "superseded" with a reference to its replacement. Nygard's reason:
  without the rationale a newcomer can only "blindly accept the
  decision" or "blindly change it".
- **Nowhere, on purpose.** Shape Up keeps no backlog: a pitch not bet
  on is let go ("There's nothing we need to track or hold on to"),
  on the ground that "really important ideas will come back to you".

The handed-over document carries the boundary and not the reasons:
no-gos in a pitch, non-goals in a BMad spec, scope exclusions in an
OpenSpec proposal, and a statement of work that excludes background
and how-to direction altogether.

Sources: Malte Ubl (2020-07-06); Rust RFC template; spec-kit
`plan.md`; BMad documentation; Michael Nygard (2011-11-15); Shape Up
chapters 6 and 7; OpenSpec concepts; AcqNotes.

### 6. Military doctrine separates intent from orders, but its intent is handed over [C on the doctrine, X on the practice]

The commander's intent states purpose, key tasks and end state; it
is understood "two echelons down"; mission orders give "directives
that emphasize to subordinates the results to be attained, not how
they are to achieve them". Marine doctrine, as a Marine Corps
Gazette article of 2001 renders it, holds that the intent carries
the enduring part of a mission, the why, while tasks change with the
situation; the same article wants the intent written by the
commander himself.

Two things matter for a comparison. The intent is not a private
working document: it stands inside the order and is the first thing
the recipients read. And it is a distillate of a few sentences,
never the place where thinking is sorted.

Practice falls short of doctrine, by the doctrine's own community:
intent statements that run to pages, that list tasks and lose the
purpose, that are written by staff; one study found company
commanders matching their battalion commander's intent in 34 per
cent of cases (Shattuck and Woods 2000, as cited by Wikipedia, not
read at source); and orders that grow prescriptive as they pass down
the echelons until they say "what to do and how to do it".

Sources: From the Green Notebook (2022-05-17); army.mil
(2017-01-05); Armchair General (2008-06-13); Marine Corps Gazette
(article of 2001-02-01); Wikipedia, "Intent (military)"; War Room,
US Army War College (2019-10-09); The Field Grade Leader
(2020-03-02). The doctrine publications themselves could not be
read: see below.

### 7. Whether the handed-over document must stand without its author is contested [X]

- **It must, where a contract or a machine reads it.** A statement
  of work is written so that the contractor needs no clarification
  from outside it, in `shall` wording, with background kept apart
  from obligation. The specs of the AI tools are read by an agent
  that cannot ask the author; BMad calls its spec "a short contract
  that Build reads".
- **It is paired with a live briefing, where people read it.** Shape
  Up posts the pitch and then holds a kick-off call. A creative-brief
  guide lists "briefing via email instead of live conversation"
  among the ways briefs fail. The BetterBriefs guide has a chapter
  named "Briefing the brief" and holds that "A brief is not a
  contract until the agency accepts it."

Even a complete document does not guarantee the outcome. Boeckeler,
reviewing Kiro, spec-kit and Tessl in 2025, found that with
elaborate specifications the agent still did not follow all the
instructions, and that the volume of generated Markdown became a
burden to review. BetterBriefs' survey shows the gap from the other
side: 78 per cent of marketers thought their briefs gave clear
direction, 5 per cent of agencies agreed.

Sources: AcqNotes; BMad documentation; Shape Up chapter 10;
admove.ai; BetterBriefs (2022-10-14); Marketing Week (2022-07-06);
Martin Fowler's site, Birgitta Boeckeler (2025-10-15).

### 8. The horizon has no layered model outside; it appears in fragments [E]

- Shape Up's **appetite** is a budget of time that shapes the
  solution ("Appetites start with a number and end with a design"),
  not a horizon; its default answer to a raw idea is "Interesting.
  Maybe some day."
- spec-kit ranks user stories P1 to P3 with a reason for each, and
  its template shows a scope line among the assumptions: "Mobile
  support is out of scope for v1".
- The Rust RFC template separates "Unresolved questions", including
  matters left for a later, independent proposal, from "Future
  possibilities", and rules of the latter that "having something
  written down in the future-possibilities section is not a reason
  to accept the current or a future RFC".
- The Now-Next-Later roadmap (first sketched 2012) is the one
  artefact built on horizons: now is specified, next less so, later
  hazy; it lists problems, not features.

No source read distributes the horizon over several layers, each
carrying a different aspect of it. The distinction between "later"
and "out of scope" is made in passing (the RFC template, the
spec-kit example) and nowhere as a rule.

Sources: Shape Up chapter 3; spec-kit `spec-template.md`; Rust RFC
template; ProdPad (2022-10-18).

### 9. The spec-driven tools start at the specification; the owner's raw words are not an artefact [E]

| Tool | Layers | What the top layer must hold |
|---|---|---|
| spec-kit | constitution; spec; plan with research, data model, contracts; tasks | what and why, never how ("no tech stack, APIs, code structure"); user scenarios, requirements in MUST wording, success criteria, assumptions |
| Kiro | steering files; requirements, design, tasks | user stories and acceptance criteria in EARS form, `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]` |
| BMad | optional brainstorm, idea test, research, brief, PRFAQ, PRD, UX, architecture; then spec | the spec: Why, Capabilities, Constraints, Non-goals, Success signal |
| OpenSpec | proposal, delta specs, design, tasks; archive | the proposal: intent, scope, approach |

Common ground: the top document says what and why and excludes how;
unknowns are marked, not guessed; the documents live in the
repository under version control. Differences: Kiro offers a
requirements-first and a design-first order and a quick form without
approval steps; BMad sizes the path to the work (four paths, most
documents optional) and says of all of them that they run one loop;
OpenSpec keeps the specification as the current truth and each
change as a delta that is archived once merged.

In none of them is the first statement of the idea kept as a
document in the owner's own words, locked and cited later as
provenance. BMad comes nearest with the file its idea-testing step
leaves, but that file is a record of decisions, not the owner's
text.

Boeckeler's review is the independent voice: one workflow does not
fit problems of every size, the functional and the technical are
hard to keep apart in practice, and the approach may repeat the fate
of model-driven development.

Sources: spec-kit repository; Kiro documentation (pages dated
2026-08-04 to 2026-09-25); BMad documentation; OpenSpec repository;
Boeckeler (2025-10-15).

### 10. Known failure modes, collected [C unless marked]

| Failure | Where it is described |
|---|---|
| The upper layer becomes a specification | Shape Up (wireframes too early); creative-brief guides (prescriptive direction); Cagan 2006 (specs long, seldom read, giving false confidence) |
| The upper layer stays too vague | Shape Up ("grab-bags", words too abstract); BetterBriefs (6 per cent of agencies clear on strategic direction); BMad (an input of one line is sent back) |
| The working document turns into a history | Ubl: amendments are written instead of the document being revised; Nygard: "Nobody ever reads large documents"; the remedies found are separate decision records and OpenSpec's archive beside a current specification |
| The handover depends on its author | the 34 per cent finding; the "game of telephone" (Collins 2020) |
| Completion criteria harden into a gate | Definition of Ready **[X]** |
| One process for work of every size | Boeckeler 2025; answered by Kiro's quick form and BMad's paths **[E]** |
| "Later" becomes "never" | a title found by search; the page could not be opened; not verified |

## Options and trade-offs

The options concern how far the forge's three layers, as drafted in
the brief this note derives from, should be adjusted to what the
outside world does.

**A. Keep the three layers and their completion statements as
drafted.** *For:* the ladder of three is the common shape (finding
1); the homes of rejections and boundaries match practice (finding
5). *Against:* leaves unused two mechanisms that are well documented
outside (findings 4 and 7).

**B. Keep the layers; borrow three mechanisms.** (1) A status per
area when a Map is walked, after spec-kit's coverage table, so that
"considered and left empty" is told apart from "not yet looked at".
(2) The reader test of the commander's intent as the measure of the
assignment: the recipients can act rightly when the plan no longer
fits. (3) An explicit word on the live briefing: the document is
written to stand alone, and a briefing beside it is normal, not a
sign of a defect. *For:* each answers a failure the sources
describe. *Against:* (1) is a new convention and costs ceremony at
every lock; the Definition of Ready shows how a checklist hardens
into a gate.

**C. Add a layer above the brief for the record of the finding**, as
BMad does with its session record and addendum. *For:* nothing found
is lost. *Against:* Shape Up argues the opposite with a reason
(important ideas come back); the sources are split, and a further
layer is a further document to keep.

**D. Rename or gloss the brief.** *For:* finding 2: an outside
reader takes "brief" for a short direction to someone else. *Against:*
a rename touches every file; a gloss in the outward-facing renders
costs one sentence.

## What was not found

- **The doctrine publications at source.** ADP 6-0 (2019), MCDP 1
  and a Military Review article of 2013 are PDF files the fetch tool
  could not read. The definition of commander's intent, its
  paragraph number and the rule of three to five sentences are given
  as secondary pages quote them. The backbrief, by which
  subordinates repeat the intent to their commander, is unverified,
  from memory, and is left out of the findings.
- **ISO/IEC/IEEE 29148:2018 and BABOK v3 at source.** The standard is
  sold and the preview could not be read; the BABOK page is behind a
  login. The outlines of the specifications and the definitions are
  from a vendor's article and a training provider's page. Section
  numbers are deliberately not given.
- **The PMBOK Guide and PMI's own pages.** Refused by the server; the
  charter is described through Wikipedia, which cites the 8th
  edition.
- **"The Client Brief" (IPA, ISBA, MCCA, PRCA) and the BetterBriefs
  guide itself.** The first is a PDF that could not be read, the
  second is behind a download form. Only the announcements were
  read. The evidence on the creative brief is therefore the weakest
  in this note.
- **The year of Shape Up.** The book's pages show no date; 2019 is
  unverified, from memory.
- **Any source that keeps the owner's raw words as a locked,
  immutable artefact and cites it as provenance.** Looked for in the
  project methods and in the four AI tools; not found.
- **Any source that divides the horizon among layers.** Not found.
- **Any source that holds a top layer to be defective when polished
  too far for the sake of the author's own next layer.** Not found;
  the argument is always the freedom of others.
- **Found not to hold:** that the document alone is the accepted
  standard of a handover between people (finding 7); that a
  definition of ready is part of Scrum (finding 4); that the
  Now-Next-Later roadmap dates from 2022, as a search summary said
  (the inventor's own page gives 2012 for the first sketch).
- **A limit of method.** Every page was read through a fetch tool
  that returns the page as processed by a small model, so a
  quotation is as the tool returned it and was not compared with the
  page character by character. Four pages that carry weight were
  fetched a second time, independently, with a request for the
  verbatim wording, and the two readings agree: Shape Up chapter 2
  (the three properties, wireframes and words), spec-kit's
  `clarify.md` (the cap of five, one question at a time, the status
  words) and `spec-template.md` (the clarification marker, the scope
  line, the priorities), and the Rust RFC template (the rule on
  future possibilities). The second reading corrected one count: the
  taxonomy of `clarify.md` has ten categories, not nine. Every other
  quotation rests on one reading; the doctrine quotations rest on
  secondary pages besides.

## Relevance to this project

**The three layers are sound and are the forge's own cut.** The
outside world confirms a ladder of about three steps and confirms
where things live: reasons and rejections in the working layer,
boundaries without reasons in what is handed over, the strictest
wording at the bottom. It does not offer the forge's layers ready
made. Two of the forge's choices have no model found outside and
should be treated as hypotheses to be tried, as the brief's own
closing section proposes: the brief as the owner's locked text, and
the horizon divided among the layers.

**Recommendation: option B in part, with D as a gloss.** In detail,
each point a proposal for the principal through `/forge intent`:

1. **Brief.** Keep completion by the principal's word. It is the
   form every discipline uses at the top (finding 4), and no
   checklist was found that works at that level without becoming a
   gate. To say what "rough" means, Shape Up's three properties are
   the best wording found: a brief may be rough and bounded, and
   need not be solved.
2. **Intent.** Keep "complete for now when no thread blocks the next
   layer". It is the same mechanism as spec-kit's markers that must
   be gone, the best documented completion test found. The
   distinction spec-kit draws at the end of its walk, between what
   is deferred and what is outstanding, corresponds to the brief's
   own distinction between deferred and dropped and supports it.
3. **Intent against chronicle.** The known remedy for a working
   document that turns into a history is what the forge already has:
   the current state in the body, the record in a companion and in
   separate decision records. Nothing to add.
4. **Assignment.** Keep the reader test as the statement of
   completion; it is the strongest form found (finding 4). Consider
   stating it as doctrine does, as acting rightly when the plan no
   longer fits, since that is what the purpose and the end state are
   for. Consider one sentence admitting the live briefing: "without
   the principal in the room" is the standard the document is
   written to, stricter than most human disciplines and equal to
   that of a contract or an agent's spec.
5. **Map.** The walk of a Map as a coverage map and not a
   questionnaire has a direct precedent in spec-kit's `clarify`,
   including one question at a time and a small cap on questions.
   A status per area is worth weighing against its ceremony; it is a
   new convention and the principal's to decide.
6. **Horizon.** No outside model. The Rust RFC rule, that a future
   possibility must not be used to justify the present proposal, is
   the one borrowed thought worth carrying into the brief `brd`.
7. **The word "brief".** One sentence in the outward-facing renders
   saying that a brief here is the owner's own statement of the
   idea, not a direction to others.

Option C is not recommended: the sources are split and the brief
this note derives from has already weighed a second home and
declined it. Nothing here is a new fact against that decision.

## Sources

All accessed 2026-09-28.

**Military doctrine, through secondary pages**

- Michael Everett, "The Science and Art of Command", From the Green Notebook, 2022-05-17 - https://fromthegreennotebook.com/2022/05/17/the-science-and-art-of-command/
- Douglas M. McBride Jr. and Reginald L. Snell, "Applying mission command to overcome challenges", US Army, 2017-01-05 - https://www.army.mil/article/179942/applying_mission_command_to_overcome_challenges
- Rick Baillergeon and John Sutherland, "Tactics 101: 027. Commander's Intent", Armchair General, 2008-06-13 - https://armchairgeneral.com/tactics-101-027-commanders-intent.htm/4
- "Commander's Intent: Easy to understand, tough to articulate", Marine Corps Gazette, article of 2001-02-01, published online 2019-08-14 - https://www.mca-marines.org/gazette/commanders-intent-easy-to-understand-tough-to-articulate/
- Doug Orsi and Bobby Mundell, "Will new doctrine fix mission command?", War Room, US Army War College, 2019-10-09 - https://warroom.armywarcollege.edu/articles/new-doctrine-mission-command/
- M. Reece Collins, "The Commander's Intent in Mission Command", The Field Grade Leader, 2020-03-02 - https://fieldgradeleader.themilitaryleader.com/cdr-intent/
- "Intent (military)", Wikipedia, no date noted - https://en.wikipedia.org/wiki/Intent_(military)
- Edward Beyne, "Commander's intent and end state", War and Business, 2026-01-04 (weak source, used only for its quotation of ADRP 5-0) - https://www.warandbusiness.com/p/commanders-intent-and-end-state-the

**Project method and acquisition**

- "Project brief", PRINCE2 wiki, no date or edition shown - https://prince2.wiki/management-products/baselines/project-brief/
- "Starting up a project", PRINCE2 wiki, no date or edition shown - https://prince2.wiki/processes/starting-up-a-project/
- "Project charter", Wikipedia, last edited 2026-02-22, citing the PMBOK Guide, 8th edition, 2025 - https://en.wikipedia.org/wiki/Project_charter
- "Statement of Work (SOW)", AcqNotes, updated 2024-02-09 - https://acqnotes.com/acqnote/tasks/statement-of-work

**Requirements engineering, through secondary pages**

- "ISO 29148 Explained", Modern Requirements, 2026-07-16 - https://www.modernrequirements.com/blogs/iso-29148-explained/
- "ISO/IEC/IEEE 29148 Requirements Specification Templates", ReqView documentation, no date shown - https://www.reqview.com/doc/iso-iec-ieee-29148-templates/
- "Types of Requirements, BABOK classification schema", Techcanvass, no date shown - https://techcanvass.com/blogs/types-of-requirements-as-per-babok

**Product practice**

- Ryan Singer, *Shape Up: Stop Running in Circles and Ship Work that Matters*, Basecamp, no date shown on the pages; chapters 1, 2, 3, 5, 6, 7, 10 - https://basecamp.com/shapeup
- "The Amazon Working Backwards PR/FAQ Process", workingbackwards.com, no date noted - https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- Colin Bryar and Bill Carr, "An insider look at Amazon's culture and processes", About Amazon, excerpt of the book of 2021 - https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- Cedric Chin, "Putting Amazon's PR/FAQ to Practice", Commoncog, 2022-09-08, updated 2026-05-08 - https://commoncog.com/putting-amazons-pr-faq-to-practice/
- Marty Cagan, "Revisiting the Product Spec", Silicon Valley Product Group, 2006-10-12 - https://www.svpg.com/revisiting-the-product-spec/
- Malte Ubl, "Design Docs at Google", Industrial Empathy, 2020-07-06 - https://www.industrialempathy.com/posts/design-docs-at-google/
- Rust RFC template, rust-lang/rfcs, no date noted - https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- Michael Nygard, "Documenting Architecture Decisions", Cognitect, 2011-11-15 - https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Janna Bastow, "Why I Invented the Now-Next-Later Roadmap", ProdPad, 2022-10-18 - https://www.prodpad.com/blog/invented-now-next-later-roadmap/
- Roman Pichler, "The Definition of Ready in Scrum", 2010-12-16, updated 2024-02-02 - https://www.romanpichler.com/blog/the-definition-of-ready/
- "The Double Diamond", Design Council, no date shown (read; not used in the findings) - https://www.designcouncil.org.uk/resources/the-double-diamond/

**Advertising**

- "New better briefing best practice guide to address industry shortcomings", IPA, 2022-07-06 - https://ipa.co.uk/news/betterbriefs-best-practice-guide
- Niamh Carroll, "Best practice guide unveiled to tackle ineffective briefs", Marketing Week, 2022-07-06 - https://www.marketingweek.com/best-practice-guide-better-briefs/
- "Best Practice Guide and UK results launch", BetterBriefs, 2022-10-14 - https://www.betterbriefs.com/library/why-poor-briefing
- "Creative Brief: What it is, Why Most Fail, and How to Write One That Works", admove.ai, 2026-08-17 (weak source) - https://www.admove.ai/blog/creative-brief-guide
- "Seasoned creatives explain the art of writing an effective creative brief", Genero, no date shown (weak source) - https://genero.com/insights/mastering-the-art-of-creative-briefs

**Spec-driven tools**

- GitHub spec-kit, repository and README, no version noted - https://github.com/github/spec-kit
- spec-kit, `spec-driven.md` - https://github.com/github/spec-kit/blob/main/spec-driven.md
- spec-kit, `templates/spec-template.md` - https://github.com/github/spec-kit/blob/main/templates/spec-template.md
- spec-kit, `templates/commands/clarify.md` - https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md
- spec-kit, `templates/commands/plan.md` - https://github.com/github/spec-kit/blob/main/templates/commands/plan.md
- Kiro documentation, Specs, page updated 2026-08-27 - https://kiro.dev/docs/specs/
- Kiro documentation, Feature specs, 2026-08-04 - https://kiro.dev/docs/specs/feature-specs/
- Kiro documentation, Specs best practices, 2026-09-25 - https://kiro.dev/docs/specs/best-practices/
- Kiro documentation, Steering, 2026-09-25 - https://kiro.dev/docs/steering/
- BMad Method, repository, no version noted - https://github.com/bmad-code-org/BMAD-METHOD
- BMad Method documentation, home, no date shown - https://docs.bmad-method.org/
- BMad Method documentation, "Choose a Planning Path" - https://docs.bmad-method.org/plan/choose-a-planning-path/
- BMad Method documentation, "Define Requirements and a Specification" - https://docs.bmad-method.org/plan/define-requirements-and-a-specification/
- BMad Method documentation, "Explore and Validate an Idea" - https://docs.bmad-method.org/plan/explore-and-validate-an-idea/
- OpenSpec, repository, no version noted - https://github.com/Fission-AI/OpenSpec
- OpenSpec, `docs/concepts.md` - https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md
- Birgitta Boeckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", martinfowler.com, 2025-10-15 - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

**Tried and not readable** (nothing is cited from these)

- ADP 6-0, *Mission Command*, US Army, 2019: PDF not readable by the tool.
- MCDP 1, *Warfighting*, US Marine Corps: refused by the server.
- "Commander's Intent and Concept of Operations", Military Review, 2013: refused by the server.
- ISO/IEC/IEEE 29148:2018, preview and catalogue page: PDF not readable; page refused.
- BABOK Guide v3, section 2.3, IIBA: behind a login.
- "The Client Brief", IPA, ISBA, MCCA, PRCA: PDF not readable.
- PMI, "The Charter - Selling your Project": refused by the server.
- Scrum.org and Medium pages on the Definition of Ready: empty or refused.
- DZone, "Waste #4: Handoffs": refused by the server.
- BMad documentation, a guessed page for the product brief: not found.
