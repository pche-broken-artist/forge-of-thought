---
project: forge
purpose: readme
audience: humans arriving at the repository
version: 0.28
updated: 2026-09-01
output: /README.md
---

# Recipe — readme

<!-- A recipe is the iterated thing; its render is generated output.
Never polish a render by hand: change the recipe, run
/render readme. Recipes are tools: bare version + updated date in
front-matter, no status, no Version History — history lives in git. -->

## Inputs
- CLAUDE.md
- projects/forge/10-intent.md

## Instructions
- The README presents the current, actual state of the system to a
  human meeting the repository for the first time — a colleague, a
  future principal, the principal returning after weeks. It must stand
  alone: no claim may require opening CLAUDE.md or the intent.
- Every claim must be derivable from the inputs (the only exceptions:
  the fixed Setup commands, the one fixed requirement example and the
  author-and-licence text this recipe itself carries). Invent nothing; omit rather than embellish.
  Anything superseded in the inputs must not survive in the README.
- Never name a git remote, a company, a company system, a person or
  any instance-specific value — the README describes the engine and
  must stay valid for any instance of the forge. Projects other than
  `projects/forge` are never named: they live in repositories of
  their own that the engine does not know.
- Where both inputs state the same rule, CLAUDE.md wording wins (it is
  the operational core); the intent supplies the why — use it for the
  short rationale sentences (e.g. why 10-intent.md exists, why blind
  reviewers). State each rule once: no sentence appears in two
  sections (the only-door-to-git rule lives in Saving and syncing
  only).
- Tone: plain, direct, no marketing. UK English. Tables for
  enumerable facts (roles, chain, commands, prefixes), prose only
  where reasoning is being explained. Table cells carry one short
  sentence each; longer mechanics move to prose below the table or to
  Setup. Every core term (principal, brief, intent, assignment,
  render, recipe, ledger, challenger, critic) is set in bold at its
  first definition, and "principal" is defined at its first use.
- The title is `# Forge of Thought <version>` — the current version
  of the forge intent (its front-matter version), no status
  annotations. Below it one line: the subtitle fixed by POS.0620,
  followed by ` · [Release notes](RELEASE-NOTES.md)`. The name
  appears large exactly once; there is no separate version line.
- The masthead is the identity statement of Forge of Thought, built
  to be scanned: one short paragraph, three bold-led bullets, one
  closing paragraph. The opening paragraph leads with the identity
  sentence — Forge of Thought is an **AI cognitive extension** of a
  thinking human, the **principal** — then says what it does (takes
  a raw, half-formed idea — a process redesign, a platform
  initiative, an organisational change, a D&D campaign; the fourth
  example is fixed, it signals domain-agnosticism per POS.0780 —
  and tempers it into a
  precise, self-contained handover for whoever delivers it: a team,
  a colleague, your future self), and closes as a bridge naming the
  working principle: it rests on one principle — **the machine
  carries every part of the work that is not deciding** — in three
  forms. The three forms follow as bullets with fixed bold lead-ins:
  **It thinks with you.** — interviews and probes, criticises,
  challenges, inspires; extracts what the principal has not yet
  articulated; lays out options with their trade-offs; the bullet
  ends "It proposes — you decide."; **It keeps the work
  consistent.** — nothing wanders off in forgotten chats: the
  thinking lives in versioned, templated artefacts, with decisions,
  state and history keeping themselves in order and consistency
  guarded across every output; **It carries the tedious work.** —
  audience-facing outputs — a pitch, a deck, even this README — are
  **renders** (bold here: this is the term's first definition): generated from the artefacts through recipes, regenerated
  whenever the thinking moves, never written by hand twice. The
  closing paragraph carries the ontological sentence saying what the
  forge technically is — a git repository: slash commands and agent
  personas for Claude Code, templates, and the conventions binding
  them — and states where the chain currently ends as a fact, never
  as the goal. The README never names who the current principal is:
  the identity of an instance is not a property of the system. The
  masthead presents the forge as a place where thoughts are forged
  (POS.0620). No conventions in the masthead, and never anchor the
  text to a chain version number — the intent version in the title
  is the only version that appears.
- Section 1 is the challenge, its heading the question — fixed
  wording "Better with AI, or replaced by it?" — and its body the
  pain the forge answers, scannable. The body opens with the fixed
  answer sentence "Forge of Thought is for those who chose to be
  better." followed in the same paragraph by the lead-in "The
  failure modes it exists to remove:" — then five bullets, no
  closing line: thinking
  scattered across chat sessions that die, taking their context with
  them; handovers whose completeness depends on the mood of the day
  they were written; the same thinking retold to every audience — a
  pitch, a deck, a mail — each version rewritten by hand and
  drifting from the others; feedback and decisions with no place to
  land, so the same ground is fought over twice; assumptions nobody
  attacked before reality did. No rhetoric and no restatement of the
  principle — the masthead already carries the answer.
- Section 2 is "What you get": a strictly concrete capability list —
  six bullets, no philosophy (that is the masthead's job): a
  versioned document chain growing from a brief — your own text,
  locked verbatim once it is done — to a self-contained assignment; an elicitation interview that
  forges the intent; two kinds of blind adversarial reviewers, every
  verdict recorded; audience-specific renders generated from
  recipes, including an actual PowerPoint file through the user's
  own template; external sources registered immutably and used only
  as the principal directs; everything in files and git — nothing
  depends on a chat's memory.
- Section 3 is a Quickstart with a common head and two named paths.
  The head, "First, once per machine", is a short fenced block: clone
  this repository (no URL; the reader is already looking at it, with
  a comment "you are looking at it"), install Claude Code first
  (pointer to Setup), start `claude` — always from the engine root —
  and `/setup` (comment: first run only — fills CLAUDE.local.md,
  sets the model, Fable). Then two bold-led paths, each its own
  fenced block: **Starting a new project** — `/new-project my-idea`,
  `/forge intent`, `/save`; **Bringing an existing project** —
  `/import-project <project url>` (comment: clones into `projects/` —
  your git configuration supplies the identity) and `/forge my-idea` (comment: select
  the project before any work — the forge cannot guess it). Closing
  sentence: each project lives inside `projects/<slug>/` as a git
  repository of its own, which the engine does not track — that is
  why you name it first.
- The language rule appears once, in Conventions, and says only this:
  the forge dictates the output language — all artefacts are written
  in English; the briefs are the exception, stored verbatim in
  whatever language they were written. The conversation language is
  per-instance configuration (it lives in `CLAUDE.local.md`) and its
  value is never mentioned in the README.
- The "How it is used" story is loose narrative, not documentation:
  second person, four to six short paragraphs, commands appearing in
  passing inside sentences, concrete micro-examples (a downloaded
  security standard the intent is later verified against; a group
  pitch as a render) beating abstractions. The opening
  thought-arrives line carries one non-corporate example — a
  campaign taking shape for your D&D table — echoing the masthead's
  domain-agnostic signal. It mentions that composing
  a recipe can be guided by a genre interview. No rule may be stated
  there that the later sections do not also carry — the story
  illustrates, it never legislates.
- The "How the work feels" section is drawn from the Working methods
  section of CLAUDE.md only: the eight names are load-bearing and
  must appear verbatim (Walkthrough, Propose never decide, Step by
  step, Elicitation interview, Draft early, Reflect back,
  Intent-first, Recommend do not push); the one-sentence glosses are
  re-derived.
  It never mentions commands that no longer exist.
- The worked example: until an exemplar project is chosen and
  published (THR.0200 of the intent), the subsection "What it looks
  like in practice" carries exactly one sentence — a worked example
  from a real project will appear here once one is published — and
  nothing else. Never construct an example from memory or from
  projects the inputs do not contain.
- Roles: a proper two-column table with a real header row (Role /
  What they own), followed by the standing-rules paragraph and one
  sentence on the collaboration model: one instance serves one
  principal, recipients collaborate through the artefacts; more
  principals means more instances (see Planned extensions).
- The Commands table mirrors CLAUDE.md's Commands table one to one in
  commands and signatures; descriptions are at most one or two
  sentences per cell. The `/ingest` and `/save` mechanics move to a
  short prose paragraph below the table. `/forge` and `/ledger` are
  described so the difference is obvious: `/forge` is the chain map
  with a recommended next step; `/ledger` is the quick state readout
  from the ledger. The star mechanics of `/forge <state>` are
  explained plainly: the command is simply the name of the artefact
  you want to work on.
- "A typical journey" is a plain-language bullet story — what a
  person does and wants, in order: brief, iterated intent, reviewer
  pressure and verdicts, a presentation recipe rendered including the
  PowerPoint, the distilled assignment, saving as you go. Commands
  appear only in parentheses as secondary information. No project
  slugs at all — the journey speaks of "your project".
- The chain section keeps the iteration rule and the write cadence to
  one line each — they matter to the user but are agent discipline,
  not README substance. The brief's row and the paragraph after its
  callout carry the brief rule per CLAUDE.md: an intent composed and
  then locked (draft → approved), three equally legitimate origins,
  `/forge brief` as the door, later wholes as `00-brief-<name>.md`,
  mined into the single intent with the ledger tracking how far.
- The three chain artefacts get paragraphs of equal weight, each
  answering what it is, what it holds and why it is shaped so.
  Brief: per CLAUDE.md — free-form, any structure the principal finds
  useful, thoughts to be processed rather than decisions, draft →
  locked, three origins, later wholes, mined with ledger state.
  Intent: the consolidated *current* state — positions (POS), open
  threads (THR), rejected directions with their reason (REJ), each
  with a stable ID — rewritten for coherence every round rather than
  appended, with a changelog; audience principal + Claude only.
  Assignment: distilled from the intent for the recipients and the
  one document they receive — requirements, out-of-scope,
  constraints, assumptions, deliverables, open questions with owner,
  optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR) —
  complete and precise, assigning rather than solving,
  self-contained.
- Exactly two principles in the README are set as `>` callout blocks,
  both in the chain section, one line each: a locked brief is
  immutable — composed, then locked, never touched again (below the
  per-document table); a render is never edited by hand — what is iterated is its
  recipe (opening the "Renders and recipes" material). The callout is
  where the rule is stated: the surrounding prose does not repeat it.
  No other callouts anywhere (the quoted illustrative requirement excepted).
- The renders-and-recipes material in the chain section is two
  paragraphs under their callout: (1) "Renders and recipes" — recipe
  iterated, render generated, provenance front-matter, a render may
  serve as an input of another render; (2) "From Markdown to slides" — everything is
  Markdown; recipe composition may be guided by genre
  (`/recipe presentation`); `scripts/md2pptx.ps1` turns a deck render
  into an actual PowerPoint file, with a `.potx` template named by
  path — typically a document of a library project; the Markdown
  stays the source of truth; all other format conversion happens
  outside the forge.
- Conventions includes: the ID scheme and prefix table; the Terms
  rule; the language rule (as above); the requirement style —
  illustrated by this one fixed example, quoted verbatim and marked
  as illustrative: "REQ.0010 The Platform shall record every request
  and every response passing through the Gateway, with the identity
  of the requesting User and the time." (the only text in the README
  not derived from the inputs besides Setup); completeness over
  brevity; the boundary in one sentence — an assignment assigns, it
  does not solve; the machinery of executing delivery belongs to the
  recipients (no enumerated list of banned apparatus); the
  versioning scheme; project kinds — `thought` (the chain) and
  `library` (`lib-` prefix, shared material, no chain) — and naming
  (slugs), illustrated only with `forge` and the `lib-` prefix, never
  with invented or instance projects. Naming has no numbered section
  of its own.
- Section for reviewers carries, after the summary, one paragraph on
  "isolation is not independence" per the intent (POS.0790): the two
  reviewers share the author's model family, their agreement is never
  validation, and the calibration point lies outside the forge.
- Section for reviewers opens with a punchy three-paragraph summary —
  clean context first ("they cannot be told what we really meant"),
  then challengers (a growing roster of persona lenses attacking the
  substance of the thinking), then the critic (auditor of the
  documents and of the project's consistency across artefacts) —
  before any procedural detail. Critique finding states are given as
  a list, not as inline arrow-and-pipe notation.
- Open threads (THR) are not enumerated; growth is summarised from
  POS.0700 — the layer growth path — and the multi-principal outlook
  (more principals, more instances). The engine/projects split is
  no longer planned: it is the shape of the repository, described in
  Setup and the chain section as fact (POS.0940).
- The repository layout block mirrors CLAUDE.md's layout block in
  full, including `CLAUDE.local.md`, the gitignored `projects/*`
  with its per-project `.git/`, the library layout and the generated
  `.pptx` sibling of a deck render.
- The chain diagram shows the star, never a line: it must make
  visible at first glance that the chain branches richly. It is this
  mermaid block, pinned verbatim (solid arrows = built today, dashed
  = illustrative growth):

  ```mermaid
  flowchart LR
      B["00-brief<br>(draft → locked)"] --> I["10-intent"]
      I --> A["20-assignment"]
      I --> RI(["renders: pitch, deck, summary …"])
      A --> RA(["renders: mail …"])
      A -.-> BRD["30-brd<br>business analysis"]
      A -.-> RFP["an RFP"]
      I -.-> ART["an article"]
      ART -.-> RT(["render: a translation"])
      I -.-> ST["strategy"]
      BRD -.-> SD["40-solution-design"]
      SD -.-> IMP["implementation deck"]

      classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
      classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
      classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
      class B,I,A built
      class BRD,RFP,ART,ST,SD,IMP future
      class RI,RA,RT render
  ```

  Directly under it one bold legend line: blue = chain artefacts
  (light = not built yet), green = renders; dashed arrows = growth
  that does not exist yet. The dashed layers are a fixed illustrative set of this recipe
  (business analysis, an RFP, an article with its translation
  render, strategy, solution design, an implementation deck),
  never presented as planned or existing. Below the legend two
  sentences: adding a layer is one definition file declaring its
  inputs — nothing is renumbered and nothing existing is reworked,
  which is why files are numbered in tens; and the authorship
  boundary per POS.0710 — a chain artefact is composed by the
  principal, a render is generated from artefacts (the article and
  its translation in the diagram illustrate it).
- Setup is written for a reader who has never used Claude Code and
  has four parts:
  - "Prerequisites" — one consolidated list: git; PowerShell 7
    (pwsh) — the scripts are PowerShell, needed on macOS/Linux too;
    Python 3 (for markitdown); a paid Claude subscription.
  - "Getting the forge and Claude Code" — clone this repository (the
    engine); install Claude Code (commands
    fixed by this recipe, update them here when they change):
    Windows `irm https://claude.ai/install.ps1 | iex`; macOS/Linux
    `curl -fsSL https://claude.ai/install.sh | bash`; or
    `npm install -g @anthropic-ai/claude-code`. Sign in on first
    run — usage draws from the same pool as Claude chat. Always
    start `claude` from the engine root so CLAUDE.md and
    CLAUDE.local.md load. Then run `/setup` once: it creates
    `CLAUDE.local.md` from its template and fills it with you in a
    short interview (who the principal is, the conversation
    language, your git identities per host) — gitignored, never
    committed — and creates `.claude/settings.local.json` with the
    session model set to Fable, the strongest available model, which
    the whole forge including the blind reviewers runs on; it tells
    you so in one sentence, and `/model` or editing that file
    changes it at any time (permissions come from the shared
    `.claude/settings.json`). `/setup` never overwrites existing
    files. Upgrading the engine is
    `scripts/forge-pull.ps1` — a fast-forward of `main`; the projects
    are untouched by it.
  - "Your projects" — each project is a directory under `projects/`
    and a git repository of its own: `/new-project` creates the
    files; `git init` in that directory and a remote if wanted are a
    one-off act of yours, while the commit identity follows the host —
    resolved by your own git configuration (per-host conditional
    includes recommended), a per-repository local identity as a
    legitimate override. An
    existing project is brought in with `/import-project <git-url>`,
    which clones it into `projects/<repository name>` through
    `scripts/forge-clone.ps1` and reports the identity git resolves
    (the matching `CLAUDE.local.md` identity is offered only as a
    fallback where none resolves). The
    engine ignores `projects/*` (except its own `projects/forge`)
    and the scripts find your project through its `.git`. A project
    without a repository is reported as "not under git" — a fact,
    not an error.
  - "Script prerequisites" — one bullet per script: `doc2md.ps1`
    needs markitdown
    (`pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`);
    `md2pptx.ps1` needs the `document-skills` plugin, installed once
    from an interactive Claude Code session
    (`/plugin marketplace add anthropics/skills`, then
    `/plugin install document-skills@anthropic-agent-skills`), with
    a deck template named by path (`-Template <file.potx>`) —
    typically a document of a library project — or none, in which
    case Claude designs the visuals; the git scripts need nothing
    beyond git.
  - "Saving and syncing" — leads with `/save` as the recommended
    door and names its pre-commit steps (README and release-notes
    Unreleased-head re-render on core changes, scope-routed
    conformance check, findings settled with the principal); the
    scripts follow as the underlying mechanism and the only intended
    door to git (stated here and nowhere else), each serving the
    engine and every project repository — a bare save commits each
    repository with changes on its own and pushes where it has a
    remote; linear history on `main`, one remote per repository, no
    URL anywhere.
- The Scripts section lists every script the repository uses — one
  table row per file in `scripts/`: script, one-sentence purpose,
  when it is run, and an install note where one is needed pointing
  to Setup. Purposes come from CLAUDE.md — the Persistence section
  for the git scripts, the external-inputs rule for `doc2md.ps1`,
  the renders rule for `md2pptx.ps1`; invent nothing beyond them.
- The section "Author and licence" precedes "About this README" and
  carries this fixed text verbatim, nothing more: "Forge of Thought ©
  Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com. Licensed under
  [CC BY 4.0](LICENSE): use and adapt it freely; credit the author
  and link to this repository." The author line is the one place the
  README names a person: it is the licence holder, not the current
  principal.
- The closing section is titled "About this README" and states that
  this file is a render: never edited by hand, regenerated by
  `/render readme` whenever the process changes (and by every `/save`
  touching the core); fixes go into the recipe or the inputs. The
  render's YAML front-matter provenance is kept by design.
- Keep the visible dated footer `_Last updated: <render date>_` at the
  end of the file.

## Template
# Forge of Thought <version>

*<subtitle per POS.0620>* · [Release notes](RELEASE-NOTES.md)

<masthead per the instruction: identity paragraph — AI cognitive
extension of a thinking human, the principal; what it does; the
principle as bridge — then the three bold-led bullets (It thinks
with you / It keeps the work consistent / It carries the tedious
work); closing paragraph with the ontological sentence (a git
repository: slash commands, agent personas, templates, conventions),
where the chain ends today as fact — no mention of who the current
principal is>

## 1. Better with AI, or replaced by it?
<the fixed answer sentence and lead-in, then the five pain bullets
per the instruction; no closing line>

## 2. What you get
<the six concrete capability bullets per the instruction>

## 3. Quickstart
<common head "First, once per machine" as a fenced block: clone this
repository → install Claude Code (see Setup) → claude from the
engine root → /setup; then two bold-led paths, each a fenced block:
Starting a new project (/new-project my-idea → /forge intent →
/save) and Bringing an existing project (/import-project
<project url> → /forge my-idea, with the select-before-work
comment); one closing sentence: each project is a repository of its
own inside projects/, untracked by the engine — that is why you name
it first>

## 4. How it is used
### The flow
<the general arc: an idea is dumped verbatim as a brief — alone or in
conversation with the forge; the intent is forged from it through
interviews, iterated over days and sessions, everything living in
files; sources are registered as they arrive and used only when the
principal directs, /research grounds key topics; two blind reviewers
press on the thinking and the documents, nothing blocks; the
assignment is distilled for the recipients; renders as a first-class
idea: recipes iterated (optionally through a genre interview),
outputs — a pitch, slides incl. the actual PowerPoint, a mail, this
very README — regenerated whenever the chain moves; /save keeps it
all in git>

### What it looks like in practice
<one sentence only: a worked example from a real project will appear
here once one is published>

## 5. How the work feels
<one lead sentence: the forge is as much a way of working as a set of
files, and these are the named methods of that work — the vocabulary
you and Claude share; then a bold-name list of the eight Working
methods from CLAUDE.md, one sentence each, walkthrough first and
given two sentences because it is the one you will use most;
close with one sentence: none is a command, you invoke any of them in
a word>

## 6. Roles
<two-column table with header Role / What they own; standing-rules
paragraph; collaboration-model sentence>

## 7. The document chain
<the pinned star chain diagram (mermaid) with its legend line and
the two sentences below it; per-document table; the brief-immutability callout
and the brief-rule paragraph (composed then locked, origins, later
briefs, mining); why 10-intent.md exists; iteration rule and write cadence one line
each; feedback rule; the render-never-hand-edited callout followed by
the two renders paragraphs: "Renders and recipes", "From Markdown to
slides">

## 8. Two isolated reviewers
<punchy three-paragraph opening per the instruction; then /challenge
subsection; /critique subsection with finding states as a list>

## 9. Commands
<intro sentence; commands table mirroring CLAUDE.md with short cells;
prose paragraph below the table with /ingest and /save mechanics;
note that plain conversation works too>
### A typical journey
<plain-language bullet story per the instruction>

## 10. Conventions
<IDs and numbering; prefix table; Terms rule; language rule;
requirement style with the fixed illustrative item; completeness over
brevity; the assigns-not-solves boundary sentence; versioning scheme;
project kinds; naming with forge and the lib- prefix only>

## 11. Repository layout
<fenced tree mirroring CLAUDE.md layout in full>

## 12. Setup
### Prerequisites
<consolidated list>
### Getting the forge and Claude Code
<clone; install commands; sign-in; run from root; /setup
(CLAUDE.local.md interview, settings.local.json with Fable);
forge-pull as the upgrade>
### Your projects
<a repository of its own per project; /new-project creates files,
git init is yours; /import-project brings an existing one through
forge-clone; "not under git" is a fact>
### Script prerequisites
<one bullet per script>
### Saving and syncing
</save first with its pre-commit steps; the scripts as mechanism and
the only intended door to git, serving the engine and every project
repository; linear main, one remote per repository, no URL>

## 13. Scripts
<table of every script in scripts/: script, one-sentence purpose,
when it is run, install note pointing to Setup>

## 14. Planned extensions
<growth path per POS.0700; more principals, more instances;
projects/forge/ as the system's own project>

## 15. Author and licence
<the fixed author-and-licence text>

## 16. About this README
<this file is a render of projects/forge — regenerated by
/render readme, never edited by hand; fixes go into the recipe or the
inputs; provenance front-matter kept by design; system changes are
recorded in projects/forge/>

_Last updated: <render date>_
