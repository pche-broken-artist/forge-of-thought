---
project: forge
topic: landscape of comparable projects — inspiration and uniqueness check
date: 2026-08-25
author: Claude (three parallel web sweeps + direct verification), at the principal's request
derived_from: 10-intent.md v2.10
character: external research; immutable snapshot — supersede with a new
  note when the landscape moves. Epistemic tags per entry —
  [V] verified on the page on 2026-08-25, [S] from a secondary source or
  search snippet only, [M] from memory, unverified. Star counts are
  as read on the day and only indicate activity order of magnitude.
---

# Landscape of comparable projects

## Question

Do projects like Forge of Thought exist — a governed chain from a raw
idea to a versioned, adversarially reviewed assignment — and if so, what
can be borrowed from them, and how unique is the forge? The sweep
covered GitHub, GitLab (its own handbook and Duo platform), the Claude
Code plugin ecosystem, and the standards the forge's conventions
descend from. Three families were searched separately:
AI spec-driven frameworks (Spec Kit, BMAD and kin), structured-thinking
and adversarial-review tooling (ADR, RFC/PEP processes, multi-agent
critique), and requirements standards (29148, INCOSE, BABOK, …).

## Answer in one paragraph

Many neighbours, no twin. The AI spec-driven family is large and very
active, but every member runs to code: none stops at an assignment by
design, none keeps a verbatim immutable brief, and almost none keeps
stable never-renumbered item IDs across versions. Isolated adversarial
review is emerging as the recognised fix for "a model reviewing its own
output rationalises" — but it is mostly applied to code, and the forge's
critic/challenger split with blind contexts is ahead of the field; what
the field has that the forge lacks is packaging (review packages,
per-round checkpoints and diffs, "what I could not assess" sections,
different-family models — the last already planned as POS.0800). The
forge's recipe → render → pptx pipeline has no counterpart at all.
Where the forge departs from the standards (no priorities, testability
recommended not required, shall-only wording) the departures are
defensible and should be stated with the standard they depart from.

The uniqueness matrix at the end scores every project against the
forge's seven distinctive properties.

---

## Family 1 — AI spec-driven frameworks (idea → spec → code)

### GitHub Spec Kit — https://github.com/github/spec-kit
GitHub's CLI + slash-command toolkit for Spec-Driven Development with
any coding agent; ~131k stars, v1.0, pushed 2026-08-25 [V]. Chain:
constitution → specify → clarify → plan → tasks → implement → analyze.
Specs per feature in numbered directories; items `FR-001`, `SC-001`;
no decision log, no isolated reviewers (`analyze` is a same-agent
consistency pass), chain continues to code.
- Inspiration: `[NEEDS CLARIFICATION: …]` inline markers that must be
  zero before the next layer — a mechanical counterpart to THR/TBC.
- Inspiration: per-template self-review checklists ("unit tests for
  English") run before hand-over — a fixed rubric `/critique` could
  carry.
- Inspiration: the constitution with numbered non-negotiable articles
  is CON made into a gate checked at every layer.

### BMAD-METHOD — https://github.com/bmad-code-org/BMAD-METHOD
Agile-role persona agents (Analyst, PM, Architect, Dev, UX) carrying an
idea brief → PRD → architecture → epics/stories → code; ~52k stars,
v6, pushed 2026-08-23 [V]. Persona reviewers ("Validate PRD",
"Implementation Readiness", "party mode") run inside the working
context — not isolated. Its `advanced-elicitation` skill serves five
critique methods from a CSV catalogue, runs the chosen ones and halts
with Apply / Reject — "never change the work unless the user accepts".
- Inspiration: "Correct Course" as a named workflow for mid-stream
  change assessment after an accepted challenge.
- Inspiration: an elicitation-method catalogue kept as data rather than
  hard-coded in the agent — a maintainable way to grow `/forge intent`
  techniques.
- Inspiration: epic retrospectives as an institutionalised learning
  loop — an immutable note after each approved major.
- Difference to state: the forge's reviewer isolation is the stronger
  design; BMAD's reviewers see the conversation.

### OpenSpec (Fission-AI) — https://github.com/Fission-AI/OpenSpec
Lightweight brownfield SDD; ~66k stars, pushed 2026-08-24 [V]. Every
change is a proposal folder (`proposal.md`, delta specs with SHALL +
Given/When/Then scenarios, `design.md`, `tasks.md`), archived with a
timestamp on completion and merged into canonical specs.
- Inspiration: **delta specs** (`ADDED / MODIFIED / REMOVED`
  requirements) as the unit of change to an approved assignment —
  cleaner than diffing 2.0 against 1.x prose; relevant once
  assignments live past 1.0.
- Inspiration: timestamped archive of completed changes as the
  immutable record of what an iteration round did.

### Kiro specs (AWS) — https://kiro.dev/docs/specs/
Proprietary IDE-native workflow `requirements.md → design.md →
tasks.md` with review checkpoints between phases [V docs]; EARS syntax
for acceptance criteria [M].
- Inspiration: an explicit approval checkpoint between layers — the
  forge's "challenge a layer before the next is derived" (POS.0450)
  made visible in the `/forge` map.

### cc-sdd (gotalab) — https://github.com/gotalab/cc-sdd
Kiro-style harness for Claude Code / Codex / Cursor; 3.6k stars, pushed
2026-05 [V]. Discovery (`brief.md`) → EARS requirements → Mermaid design
→ tasks → per-task independent reviewer (code level).
- Inspiration: a discovery step that first routes the work type before
  choosing a template — a genre selector for briefs, like
  `/recipe <genre>`.

### Agent OS (Builder Methods) — https://github.com/buildermethods/agent-os
Standards and product-mission injection plus "shape spec" questioning;
5.3k stars, pushed 2026-05 [V]. Earlier versions carried
`product/decisions.md` in ADR style [M].
- Inspiration: shaping questions run before drafting — a fixed
  elicitation checklist per artefact genre.

### claude-task-master — https://github.com/eyaltoledano/claude-task-master
PRD → dependency-ordered task graph over MCP, with complexity analysis;
28k stars, pushed 2026-04 [V]. Numeric task IDs with dotted subtasks.
- Inspiration: a computed complexity/readiness report over assignment
  groups — "Claude may propose spin-off readiness" turned into a render.

### Tessl spec-driven-development tile — https://github.com/tesslio/spec-driven-development-tile
Methodology tile for the (proprietary) Tessl platform: one question at
a time → `.spec.md` with YAML front-matter and `targets` → approval
pause → implement → work-review; 53 stars [V].
- Inspiration: front-matter `targets` — each spec declares what it
  governs; an assignment could declare its recipients and scope in
  front-matter for machine checks.

### Superpowers (obra) — https://github.com/obra/superpowers
Skills framework: Socratic brainstorming (one question at a time,
design shown in digestible sections, design doc before code) →
writing-plans → execution with two-stage review by fresh subagents
(spec compliance first, quality second); ~277k stars, pushed
2026-08-19 [V].
- Inspiration: the explicit two-stage order — "does it match the
  upstream artefact" before "is it good" — is a defensible ordering for
  running `/critique` (intent ↔ assignment divergence) before
  `/challenge` on a newly derived layer.
- Validation: fresh-context reviewers are the forge's isolation rule,
  applied to code.

### Conductor (Google, gemini-cli-extensions) — https://github.com/gemini-cli-extensions/conductor
"Context-driven development": setup files (`product.md`,
`product-guidelines.md`, `tech-stack.md`, `workflow.md`) → per-track
`spec.md`, `plan.md`, `metadata.json` → review command; 3.7k stars,
pushed 2026-08-11 [V].
- Inspiration: `workflow.md` as a first-class per-project process
  override (the forge uses project `CLAUDE.md`), and machine-readable
  `metadata.json` beside the human-readable state.

### adversarial-spec (zscole) — https://github.com/zscole/adversarial-spec
Claude Code plugin: draft a PRD/spec, send it to opponent models (GPT,
Gemini, Grok…) for parallel critique, synthesise, repeat until
consensus; per-round checkpoints with diffs and cost report; 556 stars,
pushed 2026-01 [V].
- Inspiration — direct match for POS.0790–0800 (different-family
  challengers): per-round checkpoint + diff + cost as the record
  format; "consensus reached" as a computed exit signal for a
  challenge loop. The forge would keep the principal as the only
  synthesiser (POS.0070).

### multi-model-review (formin) — https://github.com/formin/multi-model-review
Spec Kit extension: author with one LLM, build with a second, review
with a third in a separate session that never sees the builder's
context, via a portable review package; 7 stars [V].
- Inspiration: the **review package** — an explicit list of what the
  reviewer may see (artefacts and diff, never the conversation) — is
  the forge's isolation rule made into an artefact; useful when
  challengers run outside Claude Code (POS.0800).

### intent-gate (baixinghao) — https://github.com/baixinghao/intent-gate
MCP server + plugin: PRD → red-team gap analysis → Mermaid contracts
with `TBDn` placeholders → question ledger → lint gate → code unlock;
optional red/blue review with the blue team on an "information diet";
ledger of human rulings verbatim; 2 stars, pushed 2026-08-15 [V].
- Inspiration: **every answer must land on an anchor** — a THR/TBC
  resolution cites the POS/REQ it changed; unanchored answers are
  rejected. The forge does this by discipline; intent-gate makes it a
  check.
- Inspiration: a resolution funnel by cost — check sources first, then
  batch-confirm AI inferences with the principal, then ask a structured
  question with ≥3 mutually exclusive options.

### ai-prd-workflow (nurettincoban) — https://github.com/nurettincoban/ai-prd-workflow
Tool-agnostic prompt pipeline: create PRD (interview) → verify PRD →
features → RFCs → tests → implement → cold-context review → change
management → workflow-status audit; 284 stars, pushed 2026-07 [V].
Feature numbers persist and are cited by RFCs.
- Inspiration: `/workflow-status` audits artefact existence against the
  filesystem and detects drift — the forge's `/forge` map computed
  rather than read from the ledger.

### claude-plugin-prd-workflow (Yassinello) — https://github.com/Yassinello/claude-plugin-prd-workflow
PRD lifecycle with status folders and `PRD-001` IDs; review agents
grade seven dimensions (Clarity, Feasibility, UX, Dependencies,
Acceptance Criteria, Risks, Simplification) A–F; 12 stars, stale since
2025-11 [V].
- Inspiration: a fixed critique rubric with named dimensions and a
  grade per dimension makes critique runs comparable across versions.

### prd-generator-plugin (rodrigorjsf) — https://github.com/rodrigorjsf/prd-generator-plugin
Nine-agent pipeline: interview → researchers restricted to
vendor/standards/government sources → validator in fresh context →
analyst → architect → PRD/ARCHITECTURE/ER; downstream skills carry the
PRD version they derive from and a guardian flags drift; 2 stars [V].
- Inspiration: every derived artefact stamped with the upstream version
  it was derived from — the forge's render provenance generalised to
  the assignment (cite the intent version it distils).

### ai-prd-generator (cdeust) — https://github.com/cdeust/ai-prd-generator
Confidence-driven clarification rounds and multi-LLM verification with
atomic claim decomposition; claim-by-claim verification report; licence
gated; 10 stars [V].
- Inspiration: epistemic status per claim, extended from challenges to
  research notes (as this note does).

### rjmurillo/ai-agents — https://github.com/rjmurillo/ai-agents
Orchestrated multi-agent SDLC with a critic (APPROVE / APPROVE WITH
CONDITIONS / REJECT) and ADRs that steer later agents; 42 stars, 2.6k
commits, pushed 2026-08-25 [V].
- Inspiration: decisions feeding forward as constraints — the critic
  and challengers reading `decisions.md` so a rejected challenge is not
  re-raised. (The forge's challenger already reads the chain; making
  DEC an explicit input is the cheap version.)

### MetaGPT — https://github.com/FoundationAgents/MetaGPT
"One-line requirement → PRD, design, tasks, repo" with role SOPs; 70k
stars, slowing (pushed 2026-01) [V]. Fully automatic, no human in the
loop.
- Counter-example: shows what the forge deliberately is not — no
  principal composing.

### GSD Core (open-gsd) — https://github.com/open-gsd/gsd-core
Context-engineering SDD: questions → research → `REQUIREMENTS.md` →
`ROADMAP.md` → discuss → plan → execute in clean-context waves →
verify; `STATE.md` and `CONTEXT.md` as cross-session memory; 8.7k stars,
pushed 2026-08-25 [V] (origin repo ~64k stars [S]).
- Inspiration: a "Discuss" verb that harvests decisions before planning
  — the forge's THR sweep as a named step producing DEC before the
  assignment is derived.

### LeanSpec (codervisor) — https://github.com/codervisor/leanspec
Front-matter Markdown specs under 2k tokens with `status`, `priority`,
`depends_on`, `related`; spec IDs are directory numbers; kanban and
stats; 283 stars, pushed 2026-05 [V].
- Inspiration: `depends_on` / `related` links rendered as a dependency
  board — assignment groups declaring cross-group dependencies.

### MetaSpec (ACNet-AI) — https://github.com/ACNet-AI/MetaSpec
Meta-framework generating domain-specific "Spec-Driven X" toolkits
(development, design, testing, documentation, operations); v0.9.5
alpha, 51 stars [V].
- Inspiration: the notion that spec-driven working is domain-agnostic —
  the same claim the forge makes in POS.0780 (a platform assignment and
  a D&D campaign through one machinery).

### GitLab Spec-Driven Development (design document) — https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/spec_driven_development/
GitLab's own SDD, created 2026-04-16, status ongoing, DevOps stage Plan
[V]. "A structured planning layer for capturing intent and driving
agentic execution on GitLab work items." Three layers: context
gathering (git-stored Memory + a **Decision log** widget of pending and
decided entries with author, date, assignee, read into every plan
session), plan generation (Markdown **Agent plan** on the work item
capturing *Why, How, What and a clear list of pending questions*, with
versioning, an audit trail, a lightweight review flow and a
**readiness score** as "lightweight quality gate"), plan validation
(Duo Developer executes, Duo Review validates the MR against the
plan). Recorded decisions: Markdown over YAML for human readability;
approval workflow out of scope for the current phase; long-lived spec
storage unresolved. Internal preview 2026-05-30, GA TBD. No public
repo for the feature; GitLab Duo Agent Platform is the vehicle.
- Inspiration: the closest *institutional* sibling of the intent
  document — Why/How/What plus pending questions, versioned, with a
  decision log fed into every session. Validates the forge's
  intent + THR + DEC trio from an independent origin.
- Inspiration: **readiness score** as an advisory signal on whether an
  artefact is ready for the next layer — fits POS.0430 (advisory,
  never blocking) if reported by `/forge` rather than enforced.
- Inspiration: "resolve a comment thread with *Make a decision* and it
  lands in the log" — the forge's THR → DEC path in one gesture.
- Difference to state: GitLab's specs live on work items and end in
  merge requests; the forge's chain lives in files and ends where the
  owner is satisfied.

### Directories for ongoing monitoring
- awesome-spec-driven-development —
  https://github.com/engineering4ai/awesome-spec-driven-development [V listing]
- spec-compare (cameronsjo, updated 2026-07-23) —
  https://github.com/cameronsjo/spec-compare [V listing] — also lists
  Spec Kitty, Traycer, MoAI-ADK, MUSUBI (not profiled).

---

## Family 2 — structured thinking and adversarial review

### adr-tools (npryce) — https://github.com/npryce/adr-tools
Bash CLI for Nygard-format ADRs, `adr new -s 9` supersedes and edits
both records' status lines; ~5.6k stars, dormant [V]. Documents its own
decisions in `doc/adr` — the same self-hosting reflex as
`projects/forge/`.
- Inspiration: an explicit `supersedes: DEC.NNNN` field so overturned
  decisions are linked, not merely appended.

### MADR — https://github.com/adr/madr (https://adr.github.io/madr/)
The de-facto ADR template: Context, Decision Drivers, **Considered
Options with pros/cons**, Consequences, **Confirmation**; ~2.4k stars,
active, four verbosity variants [V].
- Inspiration: Considered Options is the published analogue of the
  POS/REJ split — a DEC could optionally list the rejected alternative
  with its reason (today REJ lives only in the intent).
- Inspiration: Confirmation ("how will we check this decision is being
  followed") has no forge counterpart.

### log4brains — https://github.com/thomvaill/log4brains
Docs-as-code ADR manager with static-site publishing; ADRs immutable,
only status evolves; ~1.6k stars, slowing [V].
- Validation: "immutable content, mutable status" is the forge's rule
  for reviews, challenges and decisions.
- Inspiration: a timeline render over `decisions.md` — a
  `decisions-timeline` recipe.

### Agent Decision Records (AgDR) — https://github.com/me2resh/agent-decision-record
Open standard extending ADR for decisions made by AI agents: front-matter
`id, timestamp, agent, model, trigger, status`, Y-statement body ("In
the context of…, facing…, I decided…, accepting…"); 43 stars [V].
- Inspiration: recording which model and which command produced a
  finding or challenge — cheap provenance the ledger rows lack today
  (challenge files name the persona, not the model); relevant once
  challengers run on other families (POS.0800).
- Inspiration: a one-sentence Y-statement as the required opener of
  every DEC.

### rust-lang/rfcs — https://github.com/rust-lang/rfcs
The canonical RFC process: PR per proposal, template with motivation,
drawbacks, rationale and alternatives, prior art, **unresolved
questions**, future possibilities; ten-day Final Comment Period;
outcomes merged / closed / **postponed**; ~6.6k stars [V].
- Inspiration: unresolved questions split by *when they must be
  resolved* (before merge / before stabilisation / out of scope) —
  TBC items carrying a resolve-by layer.
- Inspiration: a declared last-call window before an integer version
  is approved.
- Difference: RFC review is public and conversational; the forge
  isolates its reviewers.

### Python PEPs (PEP 1) — https://github.com/python/peps · https://peps.python.org/pep-0001/
Enhancement-proposal process with statuses Draft / Accepted /
Provisional / Deferred / Rejected / Withdrawn / Final / Superseded;
required sections include Rationale, **Rejected Ideas**, **Open
Issues**; roles: **Editors** (format only, "don't pass judgment") and a
**PEP-Delegate** (substance); `Replaces` / `Superseded-By` header
pairs; ~5k stars [V].
- Validation: Editor vs Delegate is exactly the critic vs challenger
  split — a citable external precedent.
- Validation: Rejected Ideas inside the proposal itself = REJ living in
  the intent.
- Inspiration: `Replaces` / `Superseded-By` pairs on DEC records.

### IETF Internet-Drafts — https://datatracker.ietf.org/ [M]
Versioned drafts `draft-name-NN`, immutable once posted, each revision
a new number.
- Inspiration: immutable per-version snapshots of the intent would let
  a challenge cite `10-intent.md@2.7` durably; git history plus
  front-matter versions approximate this already.

### Multiagent Debate (Du et al., ICML 2024) — https://github.com/composable-models/llm_multiagent_debate
Reference implementation: several LLM instances answer, read each
other's answers, revise over rounds; ~549 stars, research code [V].
- Inspiration: evidence that seeing other agents' answers improves
  accuracy. An optional second round in which each challenger reads the
  others' challenge *files* (artefacts, not conversation) would borrow
  the effect without breaking isolation.

### LLM Council (Karpathy) — https://github.com/karpathy/llm-council
Several models answer; each ranks the anonymised others; a chairman
synthesises; ~24k stars, explicitly a hack [V].
- Inspiration: anonymised peer ranking as a bias-free way to order
  challenge severity.
- Difference to state: the chairman is what the forge deliberately
  withholds — the principal composes (POS.0070).

### agent-review-panel (wan-huiyan) — https://github.com/wan-huiyan/agent-review-panel
Claude Code skill: 4–6 auto-selected reviewer personas (Correctness
Hawk, Security Auditor, Devil's Advocate, Feasibility Analyst, Risk
Assessor, Clarity Editor) review code, plans or documents independently
with no cross-talk, then debate, then a judge rules; anti-groupthink
mechanisms — blind final scoring, private reflection, sycophancy
detection, **correlated-bias warnings on unanimous agreement**,
confidence gating for human review; Markdown report plus HTML
dashboard; 32 stars, v3.9 [V].
- Inspiration — direct match for POS.0790 ("agreement is never
  validation"): a correlated-bias warning whenever critic and
  challengers agree, and confidence gating that flags low-confidence
  verdicts to the principal.
- Difference: the judge role again is the principal's in the forge.

### premortem (AndyShaman) — https://github.com/AndyShaman/premortem
Claude Code skill: past-tense framing ("the plan already failed —
explain how"), three parallel helpers over six angles (Customer,
Operator, Adversary, Assumptions, Situation, Future Maintainer),
hole IDs with importance, confidence and status, **history snapshots
with a diff on rerun**, a **reverse-premortem** against over-caution,
verdict continue / reduce stake / delay / abort; 55 stars [V]. Siblings:
claude-premortem-skill, gokulrajaram/premortem.
- Inspiration: the rerun **delta** — which challenges closed, worsened,
  or are new between two runs of the same persona on successive intent
  versions. The critic already reports deltas; the challenger does not.
- Inspiration: reverse-premortem as a built-in counter-case in the
  challenger definition ("why proceeding despite these challenges could
  still be right").
- Inspiration: a crisp overall verdict beside per-item severity.

### claude-skill-steelman (techiejd) — https://github.com/techiejd/claude-skill-steelman
`/steelman` argues the two or three strongest alternatives to a stated
direction and lists blind spots; 8 stars [V].
- Inspiration: a `steelman` challenger persona whose lens genuinely
  differs from `cto` — it reads the intent's REJ list and tries to
  revive rejected directions. Satisfies the forge's persona-creation
  rule (distinct blind spots only).

### pm-skills → strategy-red-team (phuryn) — https://github.com/phuryn/pm-skills
68 PM skills; the red-team skill extracts load-bearing claims, steelmans
then attacks each, frames "fails if ___", ranks by impact × likelihood ×
cost-to-test, and closes with **What's well-reasoned** and **What I
couldn't assess** [V via directory page].
- Inspiration: a mandatory closing section "What I could not assess" in
  every challenge file — the fabrication ban made structural.
- Inspiration: a kill criterion and cheapest test per ASM item in the
  assignment.

### devils-advocate-agent (dungnotnull) — https://github.com/dungnotnull/devils-advocate-agent
Standalone debate engine: fallacy detection, RAG-grounded
counterarguments from arXiv/Semantic Scholar, four intensity levels
(Skeptic → Demolisher); 3 stars [V].
- Inspiration: an intensity dial per challenge run (the forge has one
  register per persona).

### Karpathy's LLM Wiki — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Pattern (April 2026): raw sources immutable, wiki written by the LLM,
schema file (CLAUDE.md), `index.md` catalogue, append-only `log.md`,
periodic lint for contradictions and orphans [V]. Community
implementations add pin-based human corrections that survive
regeneration.
- Validation: structurally the forge already is this — `sources/`
  immutable, intent LLM-drafted, CLAUDE.md as schema, DEC append-only,
  `/check` as lint. Worth citing as independent convergence.
- Inspiration: a cheap non-adversarial consistency lint over the whole
  chain (stale THR references, dangling citations) distinct from
  `/critique`.
- Validation: "pins that survive regeneration" is POS.0810's pinned
  wording in recipes.

### obsidian-second-brain (eugeniughelbur) — https://github.com/eugeniughelbur/obsidian-second-brain
Claude Code plugin over an Obsidian vault: self-rewriting notes,
**bi-temporal facts** (when believed vs when learned), nine
"thinking tools" commands, nightly reconciliation agents; ~4.2k stars
[V].
- Inspiration: bi-temporal marking on POS items (held since v /
  changed at v) would make intent drift against the brief measurable
  without reading the changelog.
- Difference to state: self-rewriting on ingest is the opposite of the
  forge's rule that source content enters the intent only by the
  principal's explicit act (POS.0180).

### prfaq (punt-labs) — https://github.com/punt-labs/prfaq
Claude Code plugin for Amazon Working Backwards PR/FAQ: research dir →
discovery interview → cited draft → peer review flagging unsupported
claims and cognitive biases → stress test by four personas (engineer,
customer, executive, builder) → iteration; stage and version tracked;
PDF/Word export [V].
- Closest end-to-end sibling outside SDD: interview → versioned
  document → persona panel → render. Its personas see the conversation
  and may debate together; the forge isolates.
- Inspiration: **stage-calibrated evidence standards** — critic
  strictness scaling with version (0.x drafts vs pre-approval).

### claude-shapeup (abreed05) — https://github.com/abreed05/claude-shapeup
Shape Up pitch skill: problem / appetite / solution / rabbit holes /
no-gos, one file per section, hard stops on violations; new, 0 stars [V].
- Inspiration: *appetite* and *rabbit holes* have no forge prefix (CON
  by convention could carry both); no-gos = OOS exactly.
- Difference: hard stops are blocking gates — contrary to POS.0430.

### wshobson/agents — https://github.com/wshobson/agents
Largest Claude Code agent marketplace (202 agents, 16 orchestrators,
~39k stars) with tiered model assignment — Opus for review and
architecture, Sonnet for docs, Haiku for ops [V].
- Inspiration for THR.0160: model tiering per role declared in each
  agent's and command's front-matter, exactly the open thread.

### Curated lists — https://github.com/hesreallyhim/awesome-claude-code (~53k stars [V]), https://github.com/VoltAgent/awesome-claude-code-subagents [S]
Discovery channels for personas rather than design sources; the forge's
rule that personas are created only by the principal's decision is
stricter than any list.

### Also seen
- ng/adversarial-review — https://github.com/ng/adversarial-review —
  Optimizer/Skeptic agent pair for multi-model code review [S].
- robertoecf/adversarial-review — https://github.com/robertoecf/adversarial-review
  — review triad: prompt optimisation, red-team review, plan
  validation [S].
- alecnielsen/adversarial-review — https://github.com/alecnielsen/adversarial-review
  — Claude + Codex adversarial debate loop [S].
- multi-agent-debate research repos (mad_llm, DebateLLM) —
  https://github.com/topics/multi-agent-debate — Q&A/benchmark
  oriented, no document lifecycle [S].

---

## Family 3 — standards and canonical frameworks

Included because the forge's conventions descend from them and because
its deliberate departures should be stated against a named standard.

### ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html
The reference requirements-engineering standard, 2nd ed. 2018;
consensus. Sentence anatomy `[condition] [subject] shall [action]
[object] [constraint]`; modal rule shall = requirement, should =
preference, will = fact, may = permission; recommended attributes per
requirement (identification, priority, dependency, risk, source,
rationale, difficulty, type, verification method, status); quality
characteristics of individual requirements (necessary, unambiguous,
complete, singular, feasible, verifiable, correct, conforming) and of
sets; document outlines for BRS / StRS / SyRS / SRS.
- Borrow: the characteristics list is a ready-made critic checklist;
  the BRS outline is a skeleton source for the future `30-brd.md`.
- Departure to state: 29148 requires *verifiable* and *priority*; the
  forge makes testability advisory (POS.0270) and bans priorities
  (POS.0260). Its *will* = fact register is what ASM items carry.

### IEEE 830-1998 — https://standards.ieee.org/ieee/830/1222/
Legacy SRS practice, superseded by 29148. Its "modifiable" property
(stable IDs, no redundancy, cross-reference) is the forge's ID rationale;
its "ranked for importance" is what the forge rejects — cite 29148,
not 830.

### INCOSE Guide to Writing Requirements v4 (2023) — https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf
42 rules and 15 characteristics; consensus rulebook for wording. Rules
directly matching the forge: single-thought sentence (R18), active
voice (R2), defined terms (R4), vague terms (R7), escape clauses (R8),
open-ended clauses (R9), solution-free (R31), universal qualifiers
(R32), uniform terms (R36–40).
- Borrow: R7/R8/R9/R32 as named checks in the critic's style section.
- Departure: verifiable (C7) expected of every requirement.

### EARS — https://alistairmavin.com/ears/
Five sentence templates (ubiquitous, WHEN, WHILE, IF…THEN, WHERE),
2009, endorsed by INCOSE, used by Kiro and cc-sdd; consensus.
- Borrow: an *optional* pattern in the assignment guidance; the
  unwanted-behaviour template is a natural form for OOS/shall-not.

### BABOK Guide v3 (IIBA, 2015) — https://www.iiba.org/knowledgehub/business-analysis-body-of-knowledge-babok-guide/5-requirements-life-cycle-management/
Requirement classification (business, stakeholder, solution,
transition) and lifecycle (trace, maintain, prioritise, assess change,
approve); consensus in BA practice.
- Validation: the assignment sits at the business-requirements layer,
  a BRD at the stakeholder layer — the chain design holds. Note that
  "BRD" is not a BABOK artefact (it speaks of a requirements package).
- Departure: prioritisation is a mandatory task there.

### Volere template — https://www.volere.org/templates/volere-requirements-specification-template/
27-section template plus the atomic "snow card"; consensus. Sections
Mandated Constraints, Facts and Assumptions, Scope, Open Issues and
**Waiting Room** map onto CON, ASM, scope, TBC and — without a forge
counterpart — parked ideas.
- Borrow: a Waiting Room group for parked ideas in the intent (today
  only parked CHL exist); *fit criterion* as the optional testability
  field SCR already is.

### Wiegers — Vision and Scope document — https://www.processimpact.com/goodies.html
Closest published analogue of the assignment: high-level, freezes
direction, explicit *Limitations and Exclusions* (= OOS) and *Business
Objectives and Success Criteria* (= SCR); consensus.
- Borrow: Wiegers' five project dimensions (features, quality,
  schedule, cost, staff — each constrained / driven / accepted) as a
  CON-level note instead of per-item priorities.

### RFC 2119 / RFC 8174 — https://www.rfc-editor.org/rfc/rfc8174.html
Keyword convention (MUST/SHALL, SHOULD, MAY), upper-case only since
2017; consensus.
- Borrow: one boilerplate line in the assignment's Terms section
  stating that *shall / shall not* are the only requirement keywords
  and *optional* the sole exception.

### MoSCoW and its criticism — https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html
DSDM 1994; contested. Documented failure modes ("everything becomes
Must", Won't ambiguous between not-now and never) support the forge's
rejection; DSDM's own ≤60 % Must guidance shows priorities exist to
manage time-boxing — delivery planning, out of the forge's scope.

### PRINCE2 7 (2023) — https://prince2.wiki/management-products/baselines/project-brief/
Mandate (any form, minimal, the trigger) → Project brief (definition,
objectives, scope and exclusions, constraints and assumptions,
tolerances, interfaces) → PID; baselines approved by the board;
consensus in UK/EU governance.
- Validation: mandate ↔ `00-brief.md`, brief ↔ `20-assignment.md`,
  integer-approved baselines ↔ the house versioning.
- Borrow: *interfaces* and *tolerances* as completeness prompts for the
  assignment interview (no first-class kind in the forge).

### Amazon Working Backwards — PR/FAQ — https://workingbackwards.com/resources/working-backwards-pr-faq/
Fictional press release plus FAQ iterated to clarity before any build;
emerging-to-consensus in product management.
- Borrow: the FAQ discipline — hardest questions written with honest
  answers — is what challengers and TBC do; a PR/FAQ is a natural
  *render recipe* (executive pitch), not a chain artefact.

### Shape Up — the Pitch — https://basecamp.com/shapeup/1.5-chapter-06
Problem, appetite, solution, rabbit holes, no-gos; "rough, solved,
bounded"; emerging.
- Validation: "bounded but not detailed" articulates POS.0210
  (assigns, does not solve) well.
- Borrow: appetite as an explicit CON elicitation.

### Design Docs at Google — https://www.industrialempathy.com/posts/design-docs-at-google/
Context and scope, **goals and non-goals**, design, alternatives
considered, cross-cutting concerns; reviewed, then a historical record.
- Borrow: the non-goals definition ("things that could reasonably be
  goals but are chosen not to be") is the sharpest available wording
  for OOS; alternatives considered = REJ.

### Architecture Decision Records (Nygard 2011; MADR 4.0 2024) — https://adr.github.io/adr-templates/
Direct validation of `decisions.md` as append-only with supersession;
see MADR above for the Considered Options borrow.

### arc42 v9 (2025) — https://arc42.org/overview/
12-section architecture template; sections 1–3 (goals, constraints,
context) are meant to be imported from upstream requirements; section
9 expects ADRs, section 10 quality scenarios; consensus in EU
docs-as-code.
- Borrow: the skeleton for a future `40-solution-design.md`, with
  REQ/CON/OOS feeding sections 1–3 by ID.

### C4 model — https://c4model.com/
System Context → Container → Component → Code diagrams; consensus for
lightweight architecture pictures.
- Borrow: a `context-picture` render recipe at assignment level, before
  any architecture layer exists.

### ISO/IEC/IEEE 42010:2022 — https://www.iso.org/standard/74393.html
Architecture description: stakeholders, concerns, viewpoints, views,
decisions with rationale; consensus.
- Validation: concern → stakeholder → viewpoint → view is the recipe →
  render logic; a recipe is a viewpoint definition, a render a view —
  citable justification for POS.0710.

### Semantic Versioning and docs-as-code — https://semver.org/
SemVer is consensus for software and ad hoc for documents. The forge's
integer-equals-signed-off scheme is classic document-control practice
(ISO 9001 QMS, PRINCE2 baselines), not SemVer — worth one sentence in
the README to pre-empt "why not semver".

### ReqIF 1.2 (OMG) — https://www.omg.org/spec/ReqIF/1.2/About-ReqIF/
Requirements interchange: stable identifiers never reused, typed
attributes, typed relations (derives-from, satisfies); consensus in
regulated industries.
- Borrow when the BRD layer arrives: an explicit *derived-from REQ.NNNN*
  relation per BRD item is the cheapest bidirectional traceability.

### OpenAPI 3.2 (2025) — https://spec.openapis.org/oas/v3.2.0.html
Spec-first practice: the contract is the source of truth, everything
else generated — the forge's "the engine specifies" ethos in another
domain; irrelevant until an integration layer exists.

### Diátaxis — https://diataxis.fr/
Tutorials / how-to / reference / explanation; consensus in technical
writing.
- Borrow: audit the README render against the four modes — it mixes
  explanation, reference and how-to; the readme recipe could make the
  separation a structure rule.

---

## Uniqueness matrix

Seven properties that together define the forge; ✔ has it, ~ partial,
✘ absent. Only projects with at least one ✔ or two ~ are listed.

| Project | a versioned docs with history | b immutable verbatim brief | c isolated blind reviewers | d decision log incl. overruled findings | e stable never-renumbered IDs | f stops at assignment by design | g renders from recipes |
|---|---|---|---|---|---|---|---|
| **Forge of Thought** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| GitHub Spec Kit | ~ | ✘ | ~ | ✘ | ✔ | ~ | ✘ |
| BMAD-METHOD | ~ | ~ | ~ | ~ | ~ | ✘ | ~ |
| OpenSpec | ~ | ✘ | ✘ | ✘ | ~ | ✘ | ✘ |
| GitLab SDD (design) | ✔ | ✘ | ~ | ✔ | ? | ✘ | ✘ |
| adversarial-spec | ✔ | ~ | ✔ | ~ | ✘ | ~ | ~ |
| intent-gate | ~ | ✘ | ✔ | ✔ | ✔ | ~ | ✔ |
| multi-model-review | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | ✘ |
| prfaq | ✔ | ✘ | ~ | ✘ | ✘ | ✔ | ✔ |
| premortem | ~ | ✘ | ✔ | ✘ | ✔ | n/a | ✘ |
| agent-review-panel | ✘ | ✘ | ✔ | ✘ | ✘ | n/a | ~ |
| Superpowers | ✘ | ✘ | ~ | ✘ | ✘ | ✘ | ✘ |
| rjmurillo/ai-agents | ? | ✘ | ✔ | ✔ | ✘ | ✘ | ✘ |
| ADR / MADR / log4brains | ✔ | n/a | n/a | ✔ | ✔ | n/a | ~ |
| PEP / RFC processes | ✔ | ✘ | ~ | ✔ | ✔ | n/a | ✘ |
| LLM Wiki pattern | ~ | ✔ (sources) | ✘ | ✔ | ✘ | n/a | ~ |

Reading: no project has all seven; none in the AI family has b or f;
c is the property the field is now converging on, mostly for code.
The combination is unique; the parts are not.

---

## Relevance to this project

### Recommendation
Do not change the chain. The research confirms the design and finds no
project to adopt wholesale. Take four packaging ideas into the intent
as open threads or positions, in this order of value:

1. **Challenger rerun delta and "what I could not assess"**
   (premortem, pm-skills red-team): the challenger reports which
   challenges closed, persist or are new against the previous run of
   the same persona, and every challenge file closes with a section of
   what the reviewer could not assess. Smallest change, largest
   sharpening of POS.0420.
2. **Correlated-bias warning** (agent-review-panel) as the operational
   form of POS.0790: when critic and challengers agree, the report says
   so as a warning, not as a confirmation.
3. **Review package** (multi-model-review, adversarial-spec) as the
   mechanism for POS.0800's different-family challengers: a defined
   bundle of artefacts the external reviewer receives, per-round
   checkpoint files with a diff — the forge's isolation rule made
   portable.
4. **Model tiering in front-matter** (wshobson/agents) as evidence for
   THR.0160: the marketplace convention is Opus-class for review and
   architecture, cheaper tiers for mechanical work.

Worth recording as positions without mechanics, for the growth path:
delta specs for post-1.0 assignment changes (OpenSpec), `derived-from`
traceability on BRD items (ReqIF/29148), arc42 as the solution-design
skeleton, a `steelman` persona that tries to revive REJ items, and
`supersedes` links on DEC (ADR/PEP).

### Departures from the standards to state explicitly
In the README (and the assignment's Terms section), name the standard
each departure departs from: no priorities (29148 attribute set, BABOK
prioritise task, MoSCoW); testability recommended not required (29148
and INCOSE *verifiable*); shall-only wording (29148 and BCP 14 graded
modals, mapped to ASM for facts and SCR for goals); integer = signed-off
is document-control practice, not SemVer.

### Proposed changes — not written, for the principal's decision
- `/forge intent`: new THR for the four packaging ideas above, or
  directly POS where the principal already agrees.
- `/forge intent`: a POS naming the standards the assignment style
  aligns with and departs from, so the README can cite them.
- Ledger: the ledger template has no table for research notes; if the
  principal wants research tracked as state, a `## Research` table is
  a convention to decide on, not to introduce here.
- Monitoring: revisit awesome-spec-driven-development and spec-compare
  before the public split (THR.0130) — the public README will be read
  against Spec Kit and BMAD, and should say in one sentence how the
  forge differs (stops at the assignment; blind reviewers; verbatim
  brief; renders).
