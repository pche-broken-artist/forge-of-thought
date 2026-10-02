---
project: forge
document: 10-intent.md
---

# Open threads — 10-intent.md

<!-- The open threads of the intent: CLAUDE.md, Document chain 2. -->

- **THR.0090** Multi-principal use. Current working assumption: a second
  principal receives Forge — including the `forge` project itself — via
  git and runs their own instance. How genuine multi-user operation
  would work is an open point for the future; deliberately not being
  worked on now. One case named 2026-09-06 (CHL.0140, POS.0700): an
  assignment handed to a colleague's instance as his brief — how it
  is seeded, how the IDs continue, where the essence lens finds a
  parent; this thread's, when it is taken up.
- **THR.0140** The delivery side. Whether the forge's output one day
  feeds a delivery chain as grown layers of the forge or hands over
  to a separate delivery framework is open and deliberately not
  worked on now; it is taken up when a subject project first needs
  the linkage — flow-ba is a natural candidate.
- **THR.0150** The scripts in Python. Decided by the principal
  2026-10-02, on the feedback of the forge's users: scripts are
  written in Python, not PowerShell; a new script is written in
  Python at once and the existing PowerShell scripts are rewritten
  later (POS.0830). This reverses what stood here: POSIX `sh` had
  been considered and left undecided, and a rewrite in Python
  excluded as a dependency without benefit, Python staying only for
  markitdown. Open, Claude's list, marked as his: the order and the
  time of the rewrite; how Python is found on each platform; the
  per-prompt hook, which `.claude/settings.json` starts through
  `pwsh`; what the git door asks of a machine once it is Python,
  since today Python is needed only where documents are converted.
- **THR.0170** Branch documents. Considered on 2026-08-27 alongside
  POS.0920 and deferred as too heavy for now: a working document per
  large whole (`branches/<name>.md` — a verbatim seed followed by
  positions and threads worked like the intent, states `open | merged
  | dropped`, merged into the intent with provenance or dropped to a
  REJ). To be taken up only if a brief in draft turns out to need
  structured, position-level work before it can be locked and mined;
  until then a draft brief is the branch.

- **THR.0190** A plugin as a later distribution layer. Claude Code
  plugins would give the only real upgrade channel and project =
  repository, but a plugin carries no `CLAUDE.md`, and commands are
  discovered only up to the repository root — so it forces changes
  nobody needs yet: shortening the core to a bootstrap skill injected by
  a SessionStart hook (as Superpowers does; its repository `CLAUDE.md`
  is for contributors only), rewriting the commands from
  `projects/<slug>/` to the repository root, solving multi-project
  operations. A `CLAUDE.md` split is not a cheap step: 435 lines, and
  moving half the rules from always-on to on-demand is a behaviour
  change ("200 lines" is a recommendation, not a limit). `@import` of
  the forge `CLAUDE.md` into a user's works but carries only
  `CLAUDE.md`, not commands and agents. No preparation now; taken up
  when `forge-pull` proves an insufficient upgrade channel. Research:
  `2026-08-29-claude-code-packaging.md`,
  `2026-08-29-framework-distribution-in-the-field.md`.
  2026-09-14: to be merged into the brief `engine-split` (THR.0230),
  after THR.0350. The research
  above answered a different question — how
  the forge reaches users with projects of their own, where the clone
  with nested repositories won (POS.0940), rightly — and is not
  reused for the three-layer question; that question gets research of
  its own.
  2026-09-28, from `00-brief-elicitation.md`: the objections
  recorded here largely fall once CLAUDE.md stays in the engine and
  a framework is a package of instances; for the brief
  `engine-split`.
- **THR.0200** The public face: an exemplar project for the README — the
  forge itself, or one created later; the company projects cannot
  travel. Until one exists the README carries a one-sentence placeholder
  (readme recipe 0.24). Repository name and licence settled in POS.0990.
- **THR.0210** A guard rail for the public boundary. The rewrite before
  publication (POS.0980) found the leak surface where the challenge
  predicted it: the forge project's own artefacts quoting the substance
  of subject projects — a sentence of a company intent in a CTO
  challenge, a deck's name in a position. A grep before a push is a net,
  not a rule. Wanted: a standing rule that `projects/forge` never
  carries the *content* of a subject project — only process facts: that
  a project exists, its versions, dates and counts — and a home for it:
  CLAUDE.md, the challenger and critic prompts (they read the subject
  projects as evidence), a check as a sweep, or all three. Opened
  2026-08-30 at the principal's direction.
  **Parked 2026-09-03** by the principal: the risk is small while he
  knows of it, and a rule with its checks would add weight the forge
  does not need now; not closed, to be taken up when the boundary is
  next at stake (a publication of a further project, a reviewer run on
  `projects/forge` with subject projects in reach). Claude's proposed
  solution, recorded for that day: a check, not a critic lens, and
  not the check alone. Not a lens, because the critic reads the chain
  and the leak surface lies outside it — challenges, research notes,
  templates, recipes, README — and a lens runs on the principal's word
  while the boundary must hold before every push; the matter is a
  convention of the repository, which is the engine check's job at
  every `/release` of the engine. Not the check alone, because a check
  catches a leak after it is written, and challenges, reviews and
  research are immutable from creation and written by isolated agents
  that read subject projects as evidence — a leak there is repaired
  only by breaking immutability again. Hence two homes: a check of
  its own owning the rule (POS.1140) (the engine — core, operating
  layer, `projects/forge` with its immutable documents — carries no
  content of any subject project; a process fact is admissible:
  existence, slug, kind, versions, dates, states, counts, commands run;
  content is not: a position, a requirement, a quoted or paraphrased
  sentence, a deliverable's name, a person, an organisation, a host;
  verified by reading, never by a term list, POS.0980), and one
  sentence under Inputs in both contract skills (POS.1120) citing
  that item, reaching every agent.
  CLAUDE.md deliberately left out: the rule concerns one project, not
  every session, and THR.0240 argues against another sentence in the
  core. A position under the next free POS number records the
  decision when it falls.
  At stake again 2026-09-20: a company name stood in an unsaved line
  of the ledger and was caught by hand before any save. Found the
  same day and left as they are, the principal to say: three mentions
  of a library's name, which carries the company's, in history rows
  already published — the intent's row 3.23 and rows 0.2 and 0.3 of
  the executive pitch recipe; append-only records. The principal's
  proposal of that day: a check, perhaps `light`, that nothing
  specific to his work for a company reaches the engine's git.
  Claude's sketch, offered once: a sweep for names over the engine
  only, since private projects are meant to carry company matter, the
  names held in `CLAUDE.local.md` so that the list itself never
  reaches git; the rule on content stays a rule. A neighbour of the
  gate of THR.0400. To be taken up; nothing decided.
- **THR.0230** Can the forge be split into an engine and the rest?
  One of three separate tasks the principal named on 2026-09-26, and
  the only one this thread carries; the other two are THR.0420, the
  derivations of the forge for other jobs, and THR.0300, everything
  a user makes for himself. Opened
  2026-09-03 at the principal's direction; a large rebuild if taken up,
  to be worked out first and decided later — the principal is not sure
  it is a good idea. The idea: whatever every framework needs alike is
  lifted out of the forge into an engine they share — git through the
  scripts, the ledger and its upkeep, versioning and Version History,
  the ID scheme, isolated agents on the session model, recipes and
  renders, sources and research with their indexes, `/save` and
  `/check`, `/setup` and the instance facts — so that a new framework is
  written as content only. Forge of Thought becomes the first framework
  on that engine, not the engine itself; the picture is several small
  cooperating frameworks on one engine, not one large one that absorbs
  everything (much could be pushed into the forge, but CLAUDE.md is
  already large — THR.0240 — and the separation helps there). The
  frameworks that would sit on such an engine are THR.0420's, and
  the boundary is drawn against its cases, outlined there in varying
  depth: the product framework and the project-management one in
  enough detail to draw it against, the test analysts' version so far
  by its artefacts alone.
  What they show about the boundary: the chain is the framework's
  (its artefacts, their number, order and templates); "everything is
  Markdown" is a forge rule — the engine carries recipe and render, the
  framework names the output form; a dependency between frameworks is
  the Dependencies mechanism across a framework boundary; the ledger's
  tables are partly the framework's (tasks); agent types beyond the two
  (a verifier) are the framework's.
  *Agents.* Critic and challenger alike: the mechanism — isolated
  subagent, ledger record, states, walkthrough — is the engine's, the
  prompt content the framework's. Challenger personas are the
  framework's (a UX challenger, a challenger of a work plan). For the
  critic a nested point: what is generic (consistency, formal
  correctness) and what is the framework's — in the forge the drift
  brief → intent → assignment, perhaps further down.
  *How the engine reaches a framework at every session* — no decision
  now, every path recorded: one engine repository with the frameworks as
  directories in it (simplest, one `forge-pull` upgrades everything, but
  one CLAUDE.md and one command tree for all); the engine as a Claude
  Code plugin with each framework a repository of its own (the cleanest
  boundary; the finding of THR.0190 applies — a plugin carries no
  CLAUDE.md, so a bootstrap skill by SessionStart hook — the largest
  rebuild); engine and framework as two repositories joined by `@import`
  and a clone alongside (CLAUDE.md travels, commands and agents do not —
  copied or linked). THR.0190 is from now read as part of this question
  and stays a thread of its own.
  *Order of work.* The second framework must exist in outline before the
  boundary can be drawn; the engine is not built ahead of it. Where the
  engine is thought: decided 2026-09-07 — as a brief born in the forge
  (`00-brief-<name>.md`, the way `00-brief-public-engine.md` was),
  carrying the boundary list, the outline of the second framework and
  the target shape; mined into the intent once locked. A project of its
  own only afterwards, by spinoff of the decided part, if the decision
  calls for one.
  THR.0220 was settled on today's forge at 3.33 (POS.1100) as an engine
  matter that carries over; THR.0210 stays open on the same
  recommendation. CHL.0150 (2026-09-06, parked until after 4.0): since
  3.0 every new position has been the engine's and the boundary is
  being drawn by accretion; taken up after 4.0 if the split proves
  useful.
  2026-09-14 the principal drew a picture of three layers, and on
  2026-09-26 corrected it into the three separate tasks named above.
  What is left to this thread: an engine that owns the mechanics,
  ideally a thing of its own, the technical shape unknown and a
  further git-inside-git nesting unwanted, with the forge as one
  framework on it, through which he releases substantial new
  functionality on git. Whether that split is within our powers at
  all is what the thread asks. It is worked as one brief
  `engine-split` born in the forge (`/forge brief engine-split`)
  together with THR.0190, which closes into it at its birth; the
  name is his of 2026-09-26, after `layers` said nothing he could
  read back and `frameworks` was overtaken the same day when the
  three tasks parted. The two connections are one-way and
  conditional: if the forge is split, the derivations of THR.0420
  can live on the engine instead of each carrying a copy of the
  mechanics, and nothing in THR.0300 waits for the split at all.
  A matter for the brief, Claude's observation of 2026-09-26: the
  word *engine* today means the forge's own repository against the
  projects (POS.0500), so the deeper engine this brief proposes
  overloads it, and the brief settles that vocabulary before it
  settles anything else. His reasons for
  taking it up soon: every further change makes the split harder;
  against it, the BRD layer and the field feedback (THR.0350) are
  wanted quickly. Order agreed 2026-09-14: THR.0350 first, since the
  brief is to be born by co-elicitation, the technique the
  run record faulted. The order of the briefs is POS.1380's since
  2026-09-28: `brd` first, then `engine-split`. The
  brief's first item is research of its own into what Claude Code
  offers today for an engine carrying several frameworks — the
  packaging research of 2026-08-29 served the
  engine/projects split and is not reused. Whether every new position
  should name its layer waits for the brief to say what the layers
  are. CHL.0150 stays parked with the brief.
  2026-09-28, from `00-brief-elicitation.md`, material for the brief
  `engine-split` and nothing decided. The two ideas of the split, a
  thin engine of its own and a large forge into which frameworks are
  installed like plugins, are one thing seen from two ends, and the
  question they open is what the unit of installation is. A Claude
  Code plugin cannot carry CLAUDE.md as always-on context and
  carries everything else (research
  `2026-08-29-claude-code-packaging.md`), which divides by itself:
  the engine is the repository with CLAUDE.md and the mechanisms, a
  framework is a package of instances (definition pairs, lenses,
  personas, checks, genres). The cost is the one CHL.0110 named: the
  rules of particular artefacts must first move from CLAUDE.md into
  the definitions, which is what the elicitation per artefact does
  (POS.1310). The installation mechanism is a research question.
  How new types are added to the engine is THR.0480 (2026-09-30),
  to be settled before this split.
- **THR.0240** The size of CLAUDE.md. 523 lines on 2026-09-03 and
  growing with every iteration; THR.0190 already records that a split
  moves rules from always-on to on-demand and is a behaviour change, not
  a cut. To be dealt with sooner or later whatever becomes of THR.0230,
  which would help. Opened 2026-09-03 at the principal's direction. To
  think through: what must be always-on, what can live in commands,
  skills and templates and be read when its situation arises, and how
  the effect is measured — by behaviour, never by line count. Measured
  2026-09-06 at the THR.0270 trial (POS.1120): every reviewer subagent
  receives, in its first user message before the task, the whole
  CLAUDE.md together with `CLAUDE.local.md` (then still carrying the
  git identities, since moved out, POS.0950), the assistant's memory
  file and the git status — about 600 lines, the largest block of its
  context, several times its own agent body and contract together; the
  instance facts of `CLAUDE.local.md` (principal, language, git
  identities) thereby reach an isolated reviewer that needs none of
  them. The cost of CLAUDE.md is paid once per reviewer run, not once
  per session. The single-source-of-truth check of 2026-09-06 (history
  3.49) took CLAUDE.md from 636 to 584 lines by citation alone; what
  must be always-on is still this thread's question. First instance
  of the answer, 2026-09-14: the walkthrough paragraph became one
  sentence and a pointer to a skill, with a hook repeating the hard
  sentence at every prompt (POS.1170) — always-on is one sentence and
  a pointer, the detail a file read when its situation arises.
  The single-source-of-truth check of 2026-09-20 found seventeen
  restatements; nine were settled the same day (history 4.16) and
  eight low ones deferred until after THR.0390, whose condition fell
  when that thread closed on 2026-09-26 — they are on the table
  again, with no date set. They reach
  into the wording of CLAUDE.md and into the Commands table the
  README and `/man` derive from: state vocabularies enumerated in
  three places, the critic contract restating prime directive 8, the
  brief's rules restated in two state files, genre checklists beside
  their skeletons, index fields and ledger columns restated by
  `/ingest` and `/research`, the bundle index entry as a declared
  copy, sentences echoed inside CLAUDE.md and in skills, rosters
  written out by name. The report is not filed; a re-run of the check
  gives them again.
  2026-09-28: the elicitation per artefact (POS.1310) is the move of
  the rules of particular artefacts out of CLAUDE.md into their
  definitions. The brief's estimate is 43 to 53 lines fewer of 663
  in the always-on part, the state files growing by about as much;
  the line count is an effect, the proof is conduct (POS.1380).
- **THR.0250** Two suggested functions: an expander and an essence
  manager. A tip the principal received on 2026-09-03 — where from not
  recorded. The essence manager got its detail the same day: at the end
  of the chain a blind agent, without context, distils the essence of
  the final document by itself, and that essence is checked against the
  brief to see how far the whole intent drifted. The `essence` lens of
  the critic (POS.0410) is that mechanism applied to every adjacent pair
  of the chain; whether an end-to-end distillation is a further thing or
  the same lens run brief-to-last-layer is open. The expander has a name
  only. Parked until more detail arrives.
- **THR.0290** Research on the reviewer mechanism. What `/research`
  gains from kinds — the principal's idea of 2026-09-04 alongside the
  checks, which became POS.1140 — deferred on 2026-09-06 by his word:
  one command with one output today; taken up when a second way of
  researching appears. Opened 2026-09-04; the check half closed at
  3.44.
- **THR.0300** Everything a user makes for himself, kept at his own
  place and not in the forge's git. Not agents alone: agents, checks,
  critics, challengers, research, whatever a user writes for his own
  use, with no ambition of contributing it to the engine — the
  principal's word of 2026-09-26, widening his idea of 2026-09-04,
  which named reviewers, checks and other agents. One of the three
  separate tasks of that day (THR.0230, THR.0420), and the one that
  is a matter of today's forge and waits for nothing. Offered as
  possibly interesting, no priority. It would need a place the engine
  does not know and
  `forge-pull` never overwrites, on the pattern of `CLAUDE.local.md`
  and `settings.local.json` (gitignored), and the rosters of
  `/critique`, `/challenge` and `/check` would list what lies there
  beside the engine's own. Open: how a local agent takes the shared
  contract skill (POS.1120), what happens when the engine renames or
  reshapes it, and
  whether Claude Code's own user-level agents already serve. Opened
  2026-09-04. Merged on 2026-09-14 into the brief of THR.0230 as a
  third layer and taken back out on 2026-09-26 by the principal's
  correction, which also widened it from agents to everything a user
  writes for himself.
  2026-09-28, from `00-brief-elicitation.md`, material and nothing
  decided. The elicitation is to be user-definable like a check, and
  the boundary that says where to stop is mechanism versus instance.
  The engine owns the mechanism: the `/forge` dispatcher, the shape
  of a state file, the contract of a template, the shape of the
  conversation, the numbering of layers. An instance is one pair of
  files, state file plus template; a user-defined check is an
  instance of the check contract, a user-defined artefact an
  instance of the same kind. The engine never defines an instance,
  the user never changes the mechanism. The test: does CLAUDE.md
  have to change for it? If not, it is this thread's; if yes, it is
  a derivation (THR.0420). Order: the shape first (POS.1310), then
  the extension point. Open: where a user's definition lives so that
  `forge-pull` never overwrites it; a remark in the brief, for
  `engine-split`: if the mechanism is one, the dispatcher reads both
  roots, the engine's and the local one.
- **THR.0320** A harness lens. The principal's direction of
  2026-09-05: the critic roster gets a lens `harness` that reviews
  the operating layer — CLAUDE.md and the skills, commands and agents
  of `.claude/` — against current Claude Code conventions, and the
  knowledge comes from the official plugins (`plugin-dev`, whose
  `skill-reviewer` and `skill-development` carry the conventions for
  skills, commands and agents; `claude-md-management`, whose
  `claude-md-improver` reads CLAUDE.md), while the output is the
  classic critic's: a dated immutable report in `reviews/`, FND in
  the ledger, settled by walkthrough like every lens (POS.0400,
  POS.0410). The trial of the same day is the evidence that the
  shape fits a foreign agent (`reviews/2026-09-05-critique-harness.md`,
  FND.0190–0280, filed under THR.0290). Open: the mechanism by which
  `/critique harness` reaches the plugin — a mapping in `.claude/skills/critique/SKILL.md`
  from the lens to the plugin agent with the skeleton's Output section
  carried in the prompt, or an own `critic-harness` agent naming the
  critic contract and the plugin's skills alike in its front-matter
  (`skills:`, the field verified 2026-09-06, POS.1120); the plugin as an
  engine dependency — named by `/setup` and CLAUDE.md, and what the
  lens does when the plugin is absent; whether
  `claude-md-improver`'s rubric, written for codebases (build
  commands, architecture map), serves a constitution like the forge's
  CLAUDE.md beyond its conciseness criterion; the regression step of
  every lens, which the trial skipped. Relation: the first concrete
  kind of THR.0290, and the shape of the operating layer it reviews
  is POS.1120's and THR.0240's question. Opened 2026-09-05.

- **THR.0340** The README split from the documentation. The README is
  today the engine's whole documentation — 829 lines on 2026-09-08,
  longer than CLAUDE.md, sixteen chapters that are three things at
  once: an invitation (why, what you get, quickstart), a user's guide
  (the flow, roles, the chain, the reviewers, the commands) and a
  reference (conventions, setup, scripts). Decided in substance
  2026-09-08 at the principal's direction: the split must come — a
  short README that invites and points, the guide and the reference as
  renders of their own recipes into `docs/` (the mechanism exists: a
  recipe's `output:` path, POS.1070; the ledger's Renders table;
  `/release` re-rendering them). Decided order: after THR.0230, not
  before — the engine/framework boundary divides today's README
  between two repositories (setup, scripts, conventions, the reviewer
  mechanism and the mechanical commands to the engine; the chain, the
  lenses and personas, the requirement style and `/forge` to the
  forge), so a `docs/` cut made now would be cut again along that
  line. Open: whether the conventions chapter is rendered at all or
  the documentation points to CLAUDE.md, which is readable as it
  stands; the cost of more renders per `/release` (the README alone
  takes five to eight minutes today; the measurements are
  `research/2026-09-14-save-and-release-duration.md`). Trigger: the boundary drawn by
  the brief of THR.0230. Opened 2026-09-08. Also here, since it is
  the README's: the footer (`_Last updated_`) is kept for now and the
  principal will give further input (noted 2026-09-14 from the
  ledger).

- **THR.0350** Lessons of the first run in the field. The record of
  the forge applied to a private project of the principal's,
  10–13 September 2026, is registered as
  `sources/forge-run-record-health.md`: a timeline, eight failures,
  thirteen things that worked, thirteen engine gaps and sixteen
  proposals (P.01–P.16), item-numbered for citation. To be analysed
  properly and learned from — a walkthrough of the proposals, one at
  a time — when the principal has the time; deferred 2026-09-13 at
  his word, nothing decided. What he stated the same day, in his own
  words, to be worked from — his stance, not yet positions:
  - A brief that is born by joint elicitation carries Claude's part
    too: he speaks, sources are ingested as they arrive, and the two
    of them work the sources into the brief; the brief is then worked
    into the intent. That is the wanted model. The record's "brief =
    the principal's words only" (G.01) is not the model but a
    misreading of it; what broke the run was Claude saying "written"
    while nothing was written (F.01). Open: whether the brief marks
    what he said and what Claude said (Claude's recommendation of
    2026-09-13: yes, lightly, block by block, since the intent later
    asks whose word a position rests on; not decided). P.07 of the
    record (an intent draft beside a draft brief) is thereby set
    aside as the wrong fix.
  - The walkthrough is the failure he minds most: one item, worked
    until it is agreed, and only then the next; never a proposed
    resolution and the offer of the next item in one message. To be
    made to hold, not promised again.
  - The report of that project need not have been a new artefact:
    in the wanted model the brief is led by elicitation over the
    research and the ingested sources, worked into the intent, and
    the report is a render of it. How the later artefacts are handled
    is to be worked out as part of this thread.
  - To consider: a mechanism that puts a fresh sentence into the
    context at every prompt (the harness's hook that runs on each user
    message, `UserPromptSubmit`, adding context), so that the rules
    that matter — the one-item walkthrough above all — do not drift in
    a long conversation. Opened 2026-09-13.
  Priority given 2026-09-14: the first thread to be worked, before the
  briefs `brd` and `engine-split` (THR.0230) — that brief is to be
  born by the co-elicitation the record faulted (F.01, G.01, P.07, the
  marking of whose word is whose), so that technique must hold first.
  Walked through the same day, one proposal per message, directly
  into the intent (the record is the anchor; a brief of it would have
  been a copy):
  - P.01 accepted → POS.0190. P.02 accepted in the principal's own
    words as In pieces → POS.1160. P.03 accepted without the
    "no warnings" part → POS.0020. P.04 accepted as a trial, the
    hook and the `walkthrough` skill → POS.1170, POS.0850. P.05
    accepted → POS.1090 (Step by step). P.06 accepted with the
    principal's addition, the role always asked → POS.1040.
  - P.07 rejected → REJ.0180. P.08 accepted, origin on THR only →
    POS.0230, POS.1180; the marking of whose word is whose in a
    co-elicited brief decided yes, lightly → POS.0110. P.09 split:
    `terminal:` accepted → POS.0160; the layer opened as THR.0360.
    P.10 the pasted-text half accepted → POS.1040, the editing
    mechanism rejected → REJ.0200. P.11 accepted, unconditional →
    POS.1040. P.12 rejected for now → REJ.0190. P.13 deferred into
    THR.0360 with Claude's view of what a render is. P.14 covered by
    POS.1160 and POS.0190. P.15 accepted, the ledger cites → POS.0160;
    `/setup` asks the language first → POS.1050. P.16 not worked —
    too specific for now.
  - Of the principal's stance of 2026-09-13: the co-elicited brief
    is POS.0110; the walkthrough shape POS.0850 with a new depth rule
    from his correction; the report of `health` as a render is
    THR.0360's; the per-prompt hook is POS.1170.
  Still to do from this thread: the sweep of this project's ledger
  (POS.0160), and the observation of the hook in the next
  walkthroughs.
  2026-09-28: the model of the co-elicited brief stated here on
  2026-09-13 was turned. A brief holds the principal's choice from
  the finding, not the pile, and carries no mark of authorship
  (POS.0110, POS.1330).

- **THR.0360** A layer with an external audience. The first real run
  below the intent (project `health`,
  `sources/forge-run-record-health.md`, D.05, G.05) needed a report
  for a third party, not an assignment: a layer built ad hoc without
  a state file, a template or a recipe genre, every write a bundle
  across five documents. Whether it is a layer of its own (`report`),
  a generic `layer`, or a case of the BRD layer's mechanics, is worked
  in the brief `brd`, where the mechanics of layers below the intent
  are designed (POS.0700). Belongs here too (P.13, G.07) — Claude's
  view of 2026-09-14, not decided: the render is the Markdown; a
  `.docx` or `.pptx` is a conversion of a render or of an artefact,
  cheap and deterministic where it can be, with a row of its own,
  never blurred into "render"; a document the principal polishes in
  an editor is an artefact he composes, never a render, and the forge
  needs the way back — `doc2md`, a comparison, carry-over
  intent-first — because editing in an editor and having Claude
  absorb it is a way of working he finds comfortable. Of that view
  the conversions are decided since 2026-09-27 (POS.0590): a plain
  file made with the render, a designed file made by `/publish`
  with a ledger table of its own; the rest stays undecided. The `timeline`
  recipe genre waits for a second need (W.12). The brief `brd` is to
  be born (`/forge brief brd`) from the conversation over a
  colleague's fork of the engine — its files not transferred, its
  mechanisms walked through point by point — and from
  `research/2026-09-07-brd-layer-fork-analysis.md`; POS.0700 closes
  into positions of its own and CHL.0030 under DEC.0060 is revisited
  in that round (the principal's direction of 2026-09-07). Opened
  2026-09-14 from THR.0350; origin: the principal's word and the
  record.
  2026-09-28: the brief `brd` is the first instance of the
  definition shape (POS.1310, POS.1380), and the horizon returns in
  it: mandatory in the BRD, its shape in the intent and the
  assignment still to be solved (POS.1360).
  A thought to carry into the brief `brd`: what is proposed for now
  must be worth it on its own; a later possibility is never what
  justifies it
  (`research/2026-09-28-artefact-layers-from-idea-to-handover.md`).
- **THR.0370** Mermaid diagrams in Word. `scripts/md2docx.ps1`
  (POS.1150) converts a render to Word through pandoc and leaves
  Mermaid blocks as code. Agreed in the walkthrough of 2026-09-12 but
  not built: the route would be `mermaid-cli` rendering each block to
  PNG through headless Chrome before pandoc runs (a pandoc Lua
  filter), installed by the user one-off like markitdown and pandoc —
  never by the script, never `npx` fetching at run time, no online
  service. Open: whether to take the dependency at all, and global
  versus repository-local installation. The LLM route (a sibling of
  `md2pptx.ps1` on the `document-skills:docx` skill) was set aside on
  2026-09-12: it would end at a picture too, with less determinism.
  On 2026-09-27 the principal took that route for another purpose,
  the design of the document: it is the `claude` engine of
  `md2docx.ps1` behind `/publish` (POS.0590, POS.1150). Mermaid in
  the plain file stands as it was.
  Word to PDF is the recipient's, never the forge's (POS.1150).
  Deferred 2026-09-12 by the principal — "needs more thought"; opened
  as a thread 2026-09-14 from the ledger.
- **THR.0380** Executive pitch, loose ends. The five-slide deck
  (`recipes/executive-pitch.md` 0.4, `renders/executive-pitch.md` and
  `.pptx` of 2026-09-11) stays in `projects/forge` with the default
  deck template (decided 2026-09-10). Open from the render run: the
  S03 counts rest on the recipe's Template alone, no input carries
  them; and the headless build had no `document-skills:pptx` skill
  available and built the deck with python-pptx instead — to watch at
  the next build. Opened 2026-09-14 from the ledger.
- **THR.0400** A gate in front of the tools. On 2026-09-20 Claude
  read git state directly, past the scripts, twice, and on a bare yes
  to one change wrote its consequences as well — with the rules fully
  in context and the session in an automatic permission mode, so that
  nothing stopped it. The principal's three rules of that day: where
  the forge has a script, the script is used; a command of Claude's
  own, beyond plain reading, is explained and approved first;
  nothing is written, run or changed that was not agreed and
  approved. Done the same day, as the soft half: the per-prompt hook
  prints the three rules beside its two walkthrough lines
  (POS.1170). Open, the hard half: a `PreToolUse` hook,
  `scripts/hook-gate.ps1` in Claude's proposal, that reads each
  command and each write before it runs and answers deny (raw `git`,
  raw `pandoc` or `markitdown`, with the script to use instead),
  allow (plain reading; writes to the session's scratch and to
  memory) or ask (a state-changing forge script, any other command
  of Claude's own, a write into the repository). Known before it is
  built: telling reading from acting, and `git` as a command from
  the word in a string, is a heuristic, so what is unsure asks; the
  price is a dialog per write, an isolated render included; whether
  "ask" holds in an automatic permission mode, and whether the hook
  leaves the principal's own `!` commands alone, is to be tried, not
  assumed. Whether writes are gated file by file or left to the
  reminder is undecided. Deferred by the principal until the forge
  has been shown to the group (THR.0390): the script needs tuning
  and there is no time for it now; that condition fell when THR.0390
  closed on 2026-09-26, and nothing is scheduled in its place.
  Claude's reading of 2026-09-26,
  offered once: the "deny raw `git`" part of the hard half is done
  by the deny list of POS.1200, so what the gate still owes is
  `pandoc`, `markitdown` and the ask on writes.
  A silent refusal of a save, 2026-09-26, the first save since the
  deny list was added: `./scripts/forge-save.ps1 forge -m <message>`
  was refused by the permission layer with no dialog and no reason
  given, the script never starting. Six probes settled what did it. A
  one-line command carrying `git ` inside quotes runs; a two-line one
  runs; a here-string carrying the word runs; the message's exact
  sentence printed by `Write-Output` runs; the save whose here-string
  carried that sentence was refused; the same save with that one
  sentence reworded went through (commit 6cfd6f2). So no pattern
  matched a word. What was refused was the pair of a state-changing
  call and a text saying that raw git is denied to Claude — a
  judgement of content and intent, so the automatic permission mode's
  classifier and not the deny list; POS.1200 is not at fault.
  Research of the same day adds that no rule could have been more
  precise anyway: a rule cannot target a tool's primary content field,
  and `Bash(command:…)` is ignored with a startup warning. Two
  remedies were weighed and neither taken: `-MessageFile` on
  `forge-save.ps1`, so that no prose rides on the command line (the
  principal: a file is not a good solution); and dropping the prose
  statement of the ban to leave only the deny rule, his own proposal,
  against which stands that the trigger was the commit message and not
  the rule's prose, and for which stands that the ban is today written
  three times (the deny list, CLAUDE.md, the hook) — whether the
  classifier reads the hook's line as well is not verifiable from
  here. Left as it is on his word of 2026-09-26 and watched. What the
  incident adds to this thread's own case: the refusal explained
  nothing, where a gate of the forge's own would have named the rule
  and the script to use instead. The loop to expect: the forge's
  commit messages describe the forge's rules, git among them, so the
  pair will recur.
  The sweep of THR.0210 — names
  from `CLAUDE.local.md` searched in what is about to be saved — is
  a neighbour of this gate and stays that thread's. Opened
  2026-09-20 (Claude's proposal, the principal's rules).
- **THR.0410** The duration of `/save` and `/release`. Watched since
  2026-09-14, the measurements so far in
  `research/2026-09-14-save-and-release-duration.md` (POS.1100,
  POS.0810); the watch continues at the next releases, and what
  follows from the measurements is not decided. One observation of
  2026-09-20: a render of the README reads the whole intent and ran
  close to eight minutes. Opened 2026-09-20 from a line of the ledger
  that had stood without an ID since 4.10.
- **THR.0420** Derivations of the forge for other jobs. The forge as
  it stands serves the forging of a thought into an assignment; the
  principal wants versions of it that serve other work, and said on
  2026-09-26 that this is a task of its own, separate from the engine
  question (THR.0230) and from a user's own additions (THR.0300). One
  tool that does everything is explicitly not wanted: a derivation is
  reached by extending, rebuilding or forking the forge, and each
  stands as a framework in its own right. Three cases are named so
  far. The version for online product managers is the product
  framework: a screen described functionally per module, one artefact
  per module, HTML prototypes rendered from them — one and the same
  thing, by the principal's word of 2026-09-26. A version for test
  analysts, his word of the same day: their primary work is producing
  test cases and test strategies, and that is the work such a version
  would serve — the outline as far as it goes today. A
  project-management framework, his of 2026-09-03: inputs from the
  forge's assignments; later meeting inputs over which an agent runs
  unattended, sorting tasks and new requirements into artefacts —
  Markdown or otherwise — or handing them on through MCP;
  verification of an implementation against its assignment; a
  high-level idea. The two outlined ones were held in THR.0230 until
  the tasks parted; that thread's boundary analysis rests on their
  outlines, which is why they are described here in full. A derivation needs no engine — a fork
  carries the whole forge and is cut down — so the connection to
  THR.0230 is one-way and conditional: if the forge is split, the
  derivations can live on the engine instead of each carrying a copy
  of the mechanics. Whether each derivation gets a brief of its own,
  and which is taken first, is undecided; nothing is scheduled.
  Opened 2026-09-26 from THR.0230 at the principal's direction.
  2026-09-28: the line against THR.0300 is drawn there (mechanism
  versus instance, the test on CLAUDE.md). Without it a user's local
  additions grow into a derivation, and the one tool that does
  everything comes in through the door for user artefacts.
- **THR.0430** A command that ends a session. It verifies that
  nothing lives only in the conversation — an unwritten round, a
  repository with changes (`forge-status`), a stale render — and
  says what a shutdown would lose; then it records in the ledger the
  time spent and the tokens burnt in the session. Claude cannot
  measure either from inside the conversation; the harness can:
  `/cost` reports the session, and the transcripts under
  `~/.claude/projects/` carry usage and timestamps per message, so a
  script can sum them per project by working directory, for past
  sessions too — a lower bound where a project was worked on more
  than one machine. Open: the name of the command, the ledger's
  shape for the figures (a table, or a line in the header), whether
  the sum is per session or cumulative, and the research of the
  transcript format before any script. Opened 2026-09-27 at the
  principal's direction.
- **THR.0460** `/recipe` and `/forge`: one dispatcher or two.
  Today the states of `/forge` and the genres of `/recipe` are one
  mechanism written twice in different shapes. A recipe is composed
  and not found (POS.1300), so the seven blocks are not its shape;
  whether `/recipe` becomes `/forge recipe <genre> [name]` is a
  question of mechanism, left open as a small matter. A remark in
  the brief: one mechanism would unify the language question and
  "composed from the skeleton"; against it stands that `/forge` is
  the door of the chain. Opened 2026-09-28 from
  `00-brief-elicitation.md`.
- **THR.0470** The intent is too long to be read. At 4.32 the forge
  intent has 2 997 lines, and the principal finds it so talkative
  that a human cannot read it: an intent is to be structured
  decisions and the understanding of the aim. Worked 2026-09-29 by
  walkthrough, thirteen matters, every verdict the principal's. What
  was decided stands in POS.0120 (what a position carries, detail
  and the file that performs it, the threads in a file of their
  own), POS.0310 (the history as a log, the old table in an
  archive), POS.0730 (release notes derived from the log) and
  POS.1140 (the check `history`). Answered: no assignment is made
  for the forge; it would be a third copy beside the intent and the
  operating layer, and precise wording has its home in the intent
  until the file that performs it exists.
  Order agreed 2026-09-29, ahead of the order of POS.1380: nine
  steps, taken in this order.

  | Step | What | State |
  |---|---|---|
  | 1 | Write the round of 2026-09-29 as 4.34, by the rules of the day | done 2026-09-29 |
  | 2 | Cut out the threads: `10-intent.threads.md` is born, the threads move into it word for word, and everything that names them is mended so that they work on their own | done 2026-09-30 |
  | 3 | Build the operating layer of the log, the check `history` with it | done 2026-09-30 |
  | 4 | Prepare in the engine's `tmp/` the cleaned intent and the records of the history, the whole intent at once | done 2026-09-30, three passes |
  | 5 | Write the instructions for the independent verification, one set for both verifiers | done 2026-10-01 |
  | 6 | An isolated agent here and ChatGPT at the principal's, over the same three files | done 2026-10-01, M365 Copilot in the place of ChatGPT |
  | 7 | Walk both reports with the principal and mend the prepared files | done 2026-10-01 |
  | 8 | Write the project: the table moves to the archive, the log begins, the intent is replaced | done 2026-10-02, intent 4.42 |
  | 9 | The check `history` over the project, and a look at the result | done 2026-10-02, the report filed as FND.0440 to FND.0530 and settled at 4.44 |

  Step 2 mends what names the threads today: `CLAUDE.md` (where a
  THR lives, the document kinds, the repository layout, the
  sentence on saving an unfinished conversation); the template of
  the intent and a new template of the threads file; the definition
  of `/forge intent`, which starts from the threads inside the
  intent; the checks that read IDs from the intent; the ledger,
  whose lines under Waiting point at threads. Step 1 stays first
  because the decisions of 2026-09-29 lived only in the
  conversation; the plan and the open questions went into this
  thread, which moves with the others in step 2.
  Step 4 cleans the intent without its threads, whole and at once,
  not finding by finding: Claude moves text and changes no stance,
  and rephrases only where a sentence would break once the story is
  taken out. The way to a position goes into the history; detail
  goes there where the file that performs it exists, and the
  position names the file. The real intent stays untouched until
  step 8, so no backup is needed.
  The cleaning of step 4 ran in two rounds on 2026-09-30, twelve
  isolated agents, one per group, the instructions in the engine's
  `tmp/cleaning/instructions.md`. The first round kept whatever it
  doubted and took about a tenth off the intent; its doubts were
  grouped into six kinds and the principal settled each with a rule,
  and the second round ran again from the original text: (A) a rule
  that a file of the engine carries word for word or in the same
  sense leaves the item, which keeps what holds and why and names
  the file; (B) a sentence that is both story and reason keeps the
  reason in the words it has, a REJ's measurement that is its reason
  stays; (C) an item keeps the latest date its text names, no date
  added or inferred, a date older than the present shape listed for
  the principal; (D) a reference to a brief or a source stays by
  path, one to a thread, challenge, finding or decision that changed
  the item leaves, one needed to understand the item stays; (E) what
  no longer exists leaves unless the present rule depends on it; (F)
  understanding wins over length, every changed item read once more
  on its own. The definitions of the elicitation stay whole. (A2)
  Rule A holds only where a file as a whole carries the detail; what
  only a section of CLAUDE.md carries stays in the item (POS.0120).
  Steps 5 and 6: the verifiers compare the live intent, the prepared
  intent and the prepared history. Where a position names a file,
  the verifier checks that the file carries the detail and says
  nothing else. The isolated agent reads the engine's files itself;
  ChatGPT gets them from the principal, and the instructions work
  with them and without them, saying what stays unverified without
  them. By the principal's word this verification stands in place
  of the walkthrough of every position.
  The migration reaches the other instances through the release
  notes (POS.0940): each convention change of the migration carries
  an Action required line in the Notes of its history row, with the
  full procedure for a project, so that Claude on another instance
  can carry it out on its user's word. The Notes line of 4.37 was
  grouped as Changed; the Action required line of step 2 stands in
  the row of 4.38. The engine is released once, after step 8, so
  that the other instances take the migration whole.
  Offered by Claude and to run only on the principal's word: a
  mechanical check that every sentence of the old intent stands
  either in the new intent or in a `Was` of the history.
  How steps 5 to 8 ran, 2026-10-01, the write on 2026-10-02. The
  instructions of the verification and the three reports lie in the
  engine's `tmp/verification/`, outside git. The first run of the
  isolated agent gave 25 findings, none high and no text lost: detail
  had left five items for a section of CLAUDE.md against rule A2, an
  exception had left POS.1040, two items could no longer be
  understood on their own. M365 Copilot, without the engine's
  files, gave two findings on one item. The principal walked two
  findings and left the rest to Claude's judgement; Claude mended
  the prepared files and named where he decided against a verifier.
  A second run of the isolated agent over the mended files gave 15
  findings, none high, mostly at other places than the first: seven
  mended, the date of POS.0060 by the principal's verdict, the rest
  left as text the cleaning had kept in doubt. The mechanical check
  ran on the principal's word: 148 units, every word of the old
  intent in the new item or in its `Was`, nothing changed without a
  record. Claude's reading, marked as his: two readers found
  different places from run to run, so a further run would find more
  of the same kind, matters of judgement and not of loss.
  The fifteen places where an item and the file it names said
  different things, left by the cleaning, were walked with the
  principal on 2026-10-02 and settled at 4.45, each in the record of
  its item: the intent mended in eight items; the skill `ingest`,
  the FCT row of CLAUDE.md and the help of `scripts/forge-save.ps1`
  mended to the intent; one place found to hold as it stood
  (POS.0440). For the brief the intent holds (POS.0110, REJ.0180,
  REJ.0220), and the operating layer, CLAUDE.md and
  `.claude/skills/forge/states/brief.md`, was brought current with
  it at 4.47, when the definitions moved into their state files
  (POS.1380).
  What is left of the migration: the release of the engine, by which
  the other instances and the other projects take it, and the open
  question below.
  Until a step is done, what it changes stands as it stood on
  2026-09-28: the threads in the intent, the companions as tables
  with their Notes, the release notes compiled from them.
  Open: whether large files are split into smaller ones under a
  master index. The intent has been divided by kind of content, not
  by size: what holds, what is being worked, how it was reached. The
  question is taken up again after the cleaning, on the measured
  length of what is left. Measured 2026-10-01: the intent has 2 068
  lines after the cleaning against 2 363 before it.
  Claude's count of 2026-09-28, the estimates unverified: the
  threads are 711 lines; the stories, the measurements and the
  closed matters inside threads about 510; operating detail about
  320; the three definitions in full 318 (POS.1330 to POS.1350). Two
  samples of the log made on 2026-09-29 lie in the engine's `tmp/`,
  outside git; the shape they show is POS.0310's. Opened 2026-09-28.
- **THR.0480** How a new type is added to the engine — a new
  artefact of the chain, a whole new chain, a new elicitor, a new
  reviewer, genre, command or script. Opened 2026-09-30 at the
  principal's direction; can be worked at any time, and is to be
  settled before the engine split (THR.0230), which inherits its
  answer. The principal's words of 2026-09-30, saved unfinished and
  nothing decided: (1) the creation of new types — or whatever we
  come to call it — is a matter we should work on, at the least
  somewhere around the engine-split work; (2) it should be led
  centrally, as one table of rules for how each type is created, not
  a sentence in every dispatcher as today; (3) the aim is to make it
  very easy for a future user to add new artefacts, a whole new chain
  and new elicitors of his own; (4) the elicitors belong on that list
  — they are in the intent (POS.1300 to POS.1380) and not yet
  implemented. Occasion: two researches of the day on the engine
  itself, `research/2026-09-30-how-everything-in-the-forge-is-born.md`
  (how the members of every type are made in a project) and
  `research/2026-09-30-adding-a-new-type-to-the-engine.md` (what
  adding a member to each type costs, every existing member searched
  by name). What the second found and this thread starts from: a
  persona costs one file and no edits, a layer two files and about
  eleven places, because the operating layer writes "assignment"
  where it means "the last layer"; the friction is the rosters
  written into CLAUDE.md's sentences while the dispatchers scan the
  same names from disk; the numbering of Document chain is cited 31
  times and the first fourth layer meets it. Claude's addition,
  marked as his: by POS.1310 the state file of `/forge` is the
  elicitor, so a new artefact always means a new definition in the
  seven blocks and a template as a pair; the second research first
  described a layer by today's state file and was corrected to the
  seven blocks, with a section on the elicitor, before its first
  save, on the principal's word of 2026-09-30.
- **THR.0490** A stale clone goes unnoticed. The principal works on
  more than one machine, so a local engine behind its origin is the
  normal case, not the exception. On 2026-10-01 the `/forge` map was
  reported from a clone one commit behind (6856009 against f371de0)
  and nothing in the forge could have said so: the map reports
  whether a project is under git and nothing of its state against
  the remote, and `scripts/forge-status.ps1` neither fetches nor
  reports ahead/behind — it prints "clean" and the origin's URL. The
  principal's word of 2026-10-01: the pull is to be offered
  unprompted at `/forge`, as it was on 2026-09-30, and the rule is to
  live in the forge, not in the assistant's memory. Open: where it
  lives — `forge-status` fetching and reporting ahead/behind for the
  engine and every project with an origin, and the `/forge` map
  showing that line and offering `forge-pull` before anything else;
  or a session-start step beside THR.0430's session end. Claude's
  recommendation, marked as his: both, since a map drawn from a stale
  clone is a map of the wrong state. Nothing decided. Opened
  2026-10-01.
- **THR.0500** The reviewers' mechanism out of the session. The
  principal's words of 2026-10-02: one mechanism for critic,
  challenger and check; and rather than Claude doing the bookkeeping,
  a skill or a command told which agents to run, which handles the
  rest without the conversation's context. Decided the same day for
  now: the simple and reliable way first, the `/check` procedure
  files a check's report in the session (POS.1140), so that the
  history and the elicitation are finished first; whether the filing
  is rewritten into a script is kept here. What the research of that
  day found
  (`research/2026-10-02-running-reviewers-without-the-conversation.md`):
  launching and filing separate; filing (the next ID, the file, the
  ledger row) is bookkeeping for a script, in Python by THR.0150; a
  `SubagentStop` hook can hand a reviewer's final message to the
  script, its input only partly documented and to be tried first; a
  subagent may launch subagents, so one command for every reviewer is
  possible as a skill run in isolation; a saved workflow can run the
  named agents but cannot write. Open beside it: nothing keeps two
  critics or two challengers from running at once, each taking the
  next ID and editing the ledger itself; and on 2026-10-01 the
  harness refused a general subagent's write of its report, untested
  for a reviewer. A script that numbers and files for all three would
  close both. Claude's additions, marked as his: a script must know
  the shape of the report and of the ledger table, which the template
  and the contract own today, so the shape would stand in two places;
  and a new kind of reviewer gives FND unless accepting its finding
  changes a stance, which keeps the prefixes at two (CHL stays, the
  principal's verdict of 2026-10-02). Bears on THR.0460 and THR.0480.
  Opened 2026-10-02.
- **THR.0510** Live reference material by nightly export. The
  principal's thought of 2026-10-02, not worked through and nothing
  decided: the important content of the company's architecture
  repository is exported every evening into Markdown and kept in git;
  people pull it, or reach it another way, and work over the files
  (all services of a product from the service catalogue), and a live
  connector (MCP) is asked only for what the files do not hold:
  cheaper and faster. A process of its own, outside the forge. Open
  whether its form is a library at all or a plain git directory; the
  library of today is rather a proof of concept of the approach.
  Bears on POS.0970 and POS.1020, and on what `/ingest` does with a
  changed document in a library. Opened 2026-10-02.

Note: the ID THR.0120 was inadvertently used twice — first for the
readme-recipe thread (opened 1.14, closed 1.16), then for the
assignment-apparatus boundary (opened 1.24, closed 2.4). Citations of
THR.0120 in the record of POS.0210 (history, 4.42) and in the
archive's row of 2.4 refer to the latter. Recorded
as-is; IDs are never renumbered. Likewise POS.0005 and REJ.0125,
outside the numbering in tens, and the group Working methods starting
at POS.0850 rather than at a hundred, stand as they are by DEC.0110
and DEC.0130.
