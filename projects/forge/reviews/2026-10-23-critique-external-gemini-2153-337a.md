---
date: 2026-10-23
project: forge
lens: external (Gemini)
target: the BRD layer, first build
reviewed: .claude/skills/forge/states/brd.md, templates/brd.md, .claude/agents/challenger-business-analyst.md, .claude/agents/check-brd.md; cross-referenced with CLAUDE.md, .claude/skills/forge/states/assignment.md, templates/assignment.md, and brd-layer-consultation.md sections 1–3
reviewer: Gemini, outside the forge
---

# Critique (external) — 2026-10-23

## Delta summary
- **New:** FND.2530, FND.2540, FND.2550, FND.2560, FND.2570, FND.2580, FND.2590, FND.2600, FND.2610, FND.2620
- **Verified resolved:** none
- **Still open:** none
- **Newly obsolete:** none

## Findings

### FND.2530 [high] [contradiction] — Quality categories mandate NFR items whose lack of parent REQ fails mechanical check
- **Location:** `.claude/skills/forge/states/brd.md` (Requirement style), `templates/brd.md` (## Qualities), `.claude/agents/check-brd.md` (What you verify, item 2)
- **Issue:** `templates/brd.md` provides 11 fixed NFR categories, and `brd.md` directs the analyst to walk these categories, leaving unmeasured ones as open TBCs with an owner. However, `brd.md` Requirement style specifies that "every item cites its parent (`REQ.NNNN`, `POS.NNNN`, or the source by path and place); an item with no parent is a finding of the check." Concurrently, `check-brd.md` item 2 mandates: "every BR, UC and NFR ends with its parent... an item with none is a finding." If the parent assignment did not explicitly define requirements for recovery time, localisation, or data integrity, any NFR retained from the standard quality categories will lack a parent REQ and fail the mechanical check.
- **Why it matters:** A standard BRD cannot pass `/check brd`. Either elicitation of standard non-functional qualities is blocked unless the upstream assignment already anticipated them, or the author is forced to invent fake parent links to general assignment requirements.
- **Suggested fix:** Explicitly permit emergent NFRs in `brd.md` and `check-brd.md`. Allow an NFR to cite a parent REQ when derived from one, or cite the document root/roster (e.g. `(roster: qualities)`, `(parent: assignment)`) or a TBC when elicited as a baseline architectural quality.

### FND.2540 [high] [inconsistency] — Ingesting arbitrary sources as BRD parent bypasses engine trunk and intent governance
- **Location:** `.claude/skills/forge/states/brd.md` (Inputs), `templates/brd.md` (front-matter `parent:`)
- **Issue:** `brd.md` allows generating `30-brd.md` directly from an external ingested file (`sources/<file>`) such as a meeting transcript or third-party proposal. In `CLAUDE.md`, the immutable trunk of every project chain is `10-intent.md`. `CLAUDE.md` explicitly mandates: "When source content does enter the intent, it is the principal's explicit act, cited with provenance: what someone said in a meeting is never silently promoted to the principal's own position." Deriving a BRD directly from a source bypasses the intent entirely and promotes raw source statements directly into binding, testable `BR` and `UC` items.
- **Why it matters:** It breaks the core architectural invariant of Forge of Thought. A project without an intent violates the repository layout rules (`00-brief.md 10-intent.md # the trunk of every project`), loses decision provenance, and creates unstable citations pointing to line numbers or arbitrary locations in external files. The brief notes that this change requires an intent position of its own at mining; introducing it here is premature.
- **Suggested fix:** Restrict `parent:` in `templates/brd.md` and `brd.md` to `20-assignment.md` and `10-intent.md`. If a user wishes to extract requirements from an unvetted transcript or offer, route it either through `/forge intent` or produce an isolated work product in `work/` under `.claude/skills/work/SKILL.md` rather than a core chain artefact.

### FND.2550 [high] [contradiction] — Automatic drafting mode conflicts with check ban on placeholders and prime directives
- **Location:** `.claude/skills/forge/states/brd.md` (Course, Partner), `.claude/agents/check-brd.md` (What you verify, item 5)
- **Issue:** In automatic mode, Claude walks the Map alone, "asks nothing", and leaves unknown information as a TBC with an owner or an ASM. However, parent assignments typically lack operational RACI roles, impacted system details, and estimation block flags. At the same time, `brd.md` Partner dictates that Claude "writes nothing of that from imagination: no value... no behaviour... no rule". Finally, `check-brd.md` item 5 forbids skeleton residue: "no template comment, no `…`, no `<placeholder>`, no `NNNN` left in the file."
- **Why it matters:** An automated draft is impossible to complete compliantly. Claude cannot ask questions, cannot invent owners or values without violating Prime Directive 1 and the Partner block, and cannot leave placeholders without failing `check-brd.md` item 5.
- **Suggested fix:** Define a compliant representation for unassigned automatic items (such as `owner: unassigned` or assigning ownership to `principal` by default). Update `check-brd.md` item 5 to differentiate between authoring placeholders (`<role>`) and valid open-state tags (`owner: unassigned`).

### FND.2560 [high] [duplication] — Challenger persona business-analyst overlaps critic-essence and mechanical checks
- **Location:** `.claude/agents/challenger-business-analyst.md` (Lens)
- **Issue:** The `challenger-business-analyst` lens includes "The ask changed on the way down" (parent narrowed, widened, or redefined; term redefined), "The value nobody gave", and "The open matter that is not open" (TBC without owner or blocking flag). In `CLAUDE.md`, parent drift and term redefinition are the assigned task of `/critique essence`. Untestable wording and values nobody gave belong to `/critique clarity`. Verifying that every TBC has an owner and an estimation block flag is assigned to `check-brd.md` item 3.
- **Why it matters:** `CLAUDE.md` enforces strictly separated jobs: critics evaluate document quality, checks evaluate mechanical syntax, and challengers challenge substance and thinking. Having a challenger perform traceability drift checks and TBC syntax auditing burns model context, creates duplicate findings across reports, and distracts the persona from substantive operational challenge.
- **Suggested fix:** Remove parent drift, term redefinition, and mechanical TBC checks from `challenger-business-analyst.md`. Refocus the persona entirely on domain viability: operational friction, unstated regulatory obligations, missing exception scenarios, integration realities, and business organizational feasibility.

### FND.2570 [medium] [substance] — Absence of business data entities and domain lifecycle in Map and Template
- **Location:** `.claude/skills/forge/states/brd.md` (Map), `templates/brd.md`
- **Issue:** The Map and Template jump from Scope and Impacted Systems directly to Use Cases and Business Requirements, omitting business domain entities, key data attributes, and entity lifecycle states (e.g., Order: Placed, Paid, Cancelled, Shipped).
- **Why it matters:** In BABOK v3, IREB, and ISO/IEC/IEEE 29148, business rules (`BR`) and use cases (`UC`) cannot be verified or estimated by delivery teams without shared definitions of core business entities and their state transitions. Omitting business data concepts forces delivery teams to invent entity structures during solution design or leaves rules like "an account must be active" ambiguous.
- **Suggested fix:** Add a "Domain entities and data concepts" section to the Map and `templates/brd.md` (specifying entity names, key business attributes, and lifecycle states), or expand the Terms section to encompass a formal business data dictionary.

### FND.2580 [medium] [contradiction] — Check-brd item pattern conflicts with use case template structure
- **Location:** `.claude/agents/check-brd.md` (What you verify, item 2), `templates/brd.md` (## Use cases)
- **Issue:** `check-brd.md` item 2 states: "every BR, UC and NFR ends with its parent (`.claude/skills/forge/states/brd.md`, Requirement style); an item with none is a finding." In `templates/brd.md`, a use case is a structured multi-line block where the parent is declared at the top (`- **Carries:** REQ.NNNN`), while the use case ends with an Exceptions table.
- **Why it matters:** An automated check verifying that a `UC` "ends with its parent" will fail on every template-compliant use case because the trailing text is an exception row or step table rather than `(REQ.NNNN)`.
- **Suggested fix:** Adjust `check-brd.md` item 2 to check that `UC` blocks declare their parent in the `- **Carries:**` line, restricting the trailing citation check (`ends with its parent`) to single-line `BR` and `NFR` items.

### FND.2590 [medium] [inconsistency] — Use case template lacks trigger and guarantees while over-coupling steps to BRs
- **Location:** `templates/brd.md` (## Use cases)
- **Issue:** The use case structure borrows Cockburn's steps and exceptions, but omits the initiating **Trigger** and collapses Cockburn's Minimal Guarantee and Success Guarantee into a single vague "Outcome". Concurrently, the step table forces every single action step to cite a distinct `BR` (`| Step | Action | BR |`), duplicating the header's `Exercises: BR.NNNN`.
- **Why it matters:** Without an explicit Trigger, temporal, batch, or event-driven business flows cannot be properly elicited. Forcing every action step to map 1:1 to a BR forces unnatural decomposition of high-level business rules into procedural UI micro-steps, violating the principle of avoiding solutioning below the line.
- **Suggested fix:** Add **Trigger** to the use case header. Split Outcome into **Success Outcome** and **Failure / Minimal Guarantee**. Make the `BR` column in the step table optional so that steps describe natural workflow, citing a `BR` only when a specific business rule governs that step.

### FND.2600 [medium] [ambiguity] — Phasing table conflates document versioning with release phases and lacks requirement IDs
- **Location:** `templates/brd.md` (## Phasing), `.claude/skills/forge/states/brd.md` (Map)
- **Issue:** The Phasing table uses the column header `Version` (`| Version | Delivers | Depends on |`), and contains free-text descriptions without referencing requirement IDs (`BR.NNNN`, `UC.NNNN`).
- **Why it matters:** Using "Version" in the phasing table causes immediate confusion with the forge's document revision numbers (`0.1, 1.0`). Furthermore, without citing requirement IDs in the phasing table, delivery teams cannot verify which requirements belong to an MVP versus later phases, and mechanical checks cannot verify scope coverage across phases.
- **Suggested fix:** Rename the column header from `Version` to `Phase / Release` (e.g., Phase 1, Phase 2) and add a mandatory column `Items carried` listing the specific `BR.NNNN` and `UC.NNNN` IDs delivered in that phase.

### FND.2610 [low] [substance] — Quality categories diverge from ISO/IEC 25010:2023 by omitting Safety and splitting Reliability
- **Location:** `templates/brd.md` (## Qualities)
- **Issue:** The 11 NFR categories split Reliability across `NFR.0010` (Availability and continuity) and `NFR.0050` (Reliability), and split Performance across `NFR.0020` (Performance) and `NFR.0100` (Scalability). Meanwhile, ISO/IEC 25010:2023's primary quality characteristic of Safety is missing entirely.
- **Why it matters:** Splitting related characteristics causes overlap and duplicate requirements (e.g., recovery point/time in NFR.0010 vs recoverability in NFR.0050). Omitting Safety leaves operational, human-safety, and fail-safe requirements without a defined category.
- **Suggested fix:** Align the quality categories with ISO/IEC 25010:2023: consolidate availability and recovery under Reliability, consolidate capacity and scalability under Performance Efficiency, and add Safety where applicable.

### FND.2620 [low] [ambiguity] — Stakeholder involvement table replaces RACI without defining execution responsibility
- **Location:** `templates/brd.md` (## Stakeholders), `.claude/skills/forge/states/brd.md` (Course)
- **Issue:** The Stakeholders table defines involvement as `approves / reviews / consulted / informed`. The "Responsible" role from RACI (the party responsible for driving the work or providing detailed operational input) is absent.
- **Why it matters:** Identifying who approves or reviews does not establish who owns the requirement from the business side or who is responsible for operational rollout.
- **Suggested fix:** Clarify whether "approves" represents Accountable, and include `responsible` (or `business owner`) in the involvement options.

---

## Recommendations

1. **Clarify Requirement Style grammar for Use Cases:** The assignment's Requirement Style enforces strict `shall` / `shall not` language. Cockburn use cases are written in the present active voice ("The User submits the form", "The System validates credentials"). Using `shall` inside use case steps makes scenarios stiff and unreadable. `brd.md` should clarify that `shall` applies to `BR` and `NFR` items, while `UC` steps follow active voice.
2. **Clarify Traceability Appendix status:** The comment in `templates/brd.md` claims the traceability table is "Generated from the items... Never edited by hand." Because the forge currently lacks a Python script to compile this table, Claude writes it during markdown iteration. Describing it as generated while having no generator script invites confusion; state clearly that Claude compiles the table during the write.
3. **Handle non-enterprise projects in Touched Areas:** The Touched Areas table assumes an enterprise roster path exists in `projects/lib-allwyn/...`. For open-source tools or personal projects, this path does not exist. `brd.md` should explicitly specify that if no roster applies, the section may state `Roster: none` with a single entry indicating that the enterprise roster is not applicable, preventing `check-brd.md` from raising an invalid file-path error.

---

## What you could not judge

1. **The private fork material:** The colleague's original BRD implementation, the 14 files in `projects/lib-allwyn/sources/fork-brd/` (including the group standard, tutorial, and three historical BRD critique rounds), and the proprietary six-pillar roster could not be viewed directly.
2. **First trial dynamics:** The practical ergonomics of the automatic drafting mode and the walkthrough by group on the planned trial (`agentic-platform` from assignment 1.3) could not be observed in execution.
