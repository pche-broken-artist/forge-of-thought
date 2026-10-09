---
project: forge
purpose: readme
audience: humans arriving at the repository
version: 0.59
updated: 2026-10-09
last_change: 0.59 (2026-10-09): the pinned facts name Python as the one prerequisite of the scripts and the Python scripts by name; PowerShell 7 leaves.
output: /README.md
---

# Recipe — readme

<!-- A recipe is the iterated thing; its render is generated output.
Never polish a render by hand: change the recipe, run
/render readme. Recipes are tools: version + updated date in
front-matter and no status (a recipe is never approved); its Version
History lives in the companion <recipe>.history.md, last_change
summarising the newest row. -->

## Inputs
- CLAUDE.md
- projects/forge/10-intent.md
- .claude/skills/forge/states/   # the definitions of the artefacts:
                                 # one line each in the chain picture
- docs/README.md                 # the documentation index: its
                                 # version line and the three paths

## Instructions
- The README orients and points. It presents what Forge of Thought
  is, why, what one gets, how to start and where the documentation
  is, to a human meeting the repository for the first time. It
  documents nothing itself: every mechanism, convention, command,
  role and setup step lives in `docs/` and the README sends the
  reader there. It must stand alone for what it says: no claim may
  require opening CLAUDE.md or the intent.
- Every claim must be derivable from the inputs (the only exceptions:
  the fixed Quickstart commands, the fixed "Short on time?" paragraph
  and the author-and-licence text this recipe itself carries). Invent
  nothing; omit rather than embellish. Anything superseded in the
  inputs must not survive in the README.
- Never name a git remote, a company, a company system, a person or
  any instance-specific value — the README describes the engine and
  must stay valid for any instance of the forge. Projects other than
  `projects/forge` are never named: they live in repositories of
  their own that the engine does not know. The README never names
  who the current principal is: the identity of an instance is not
  a property of the system.
- Where two inputs state the same thing, the wording of the operating
  layer wins (CLAUDE.md, a definition); the intent supplies the why.
  State each thing once: no sentence appears in two sections.
- Tone: plain, direct, no marketing. UK English. No long dash
  anywhere: a colon, a full stop or a spaced hyphen where one would
  stand. Every core term (principal, brief, intent, render, recipe)
  is set in bold at its first definition, and "principal" is defined
  at its first use.
- The title is `# Forge of Thought <version>` — the current version
  of the forge intent (its front-matter version), no status
  annotations. Below it one line: the subtitle fixed by POS.0620,
  followed by ` · [Documentation](docs/README.md) ·
  [Release notes](RELEASE-NOTES.md)`, the two links a reader looks
  for first, on the first line. The name
  appears large exactly once; there is no separate version line, and
  the intent version in the title is the only version that appears
  in the README's own words.
- The masthead is the identity statement of Forge of Thought, built
  to be scanned: one short paragraph, three bold-led bullets, one
  closing paragraph. The opening paragraph leads with the identity
  sentence — Forge of Thought is an **AI cognitive extension** of a
  thinking human, the **principal** — then says what it does (takes
  a raw, half-formed idea — a process redesign, a platform
  initiative, an organisational change, a D&D campaign; the fourth
  example is fixed, it signals domain-agnosticism per POS.0780 —
  and tempers it into a precise, self-contained handover for whoever
  delivers it: a team, a colleague, your future self), and closes as
  a bridge naming the working principle: it rests on one principle —
  **the machine carries every part of the work that is not
  deciding** — in three forms. The three forms follow as bullets with
  fixed bold lead-ins: **It thinks with you.** — interviews and
  probes, criticises, challenges, inspires; extracts what the
  principal has not yet articulated; lays out options with their
  trade-offs; the bullet ends "It proposes; you decide."; **It keeps
  the work consistent.** — nothing wanders off in forgotten chats:
  the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output; **It carries the tedious
  work.** — audience-facing outputs — a pitch, a deck, this README,
  the whole documentation — are **renders** (bold here: the term's
  first definition): generated from the artefacts, regenerated
  whenever the thinking moves, never written by hand twice. The
  closing paragraph carries the ontological sentence saying what the
  forge technically is — a git repository: slash commands and
  isolated agents — challenger personas and critic lenses — for
  Claude Code, templates, and the conventions binding them — and
  states where the chain currently ends as a fact, never as the
  goal. The masthead presents the forge as a place where thoughts
  are forged (POS.0620). No conventions in the masthead.
- Directly below the masthead and before Section 1 stands one short
  paragraph for the reader with little time, with no heading of its
  own and fixed in wording (the two files are renders of this
  project, and the recipe carries their paths): "Short on time? Two
  one-page notes say it briefly:
  [for a CTO](projects/forge/renders/cto-pitch.md) and
  [for a CEO](projects/forge/renders/ceo-pitch.md). Each has a Word
  version beside it." Two sentences and the two links, nothing
  added; the links are relative, exactly as given.
- Section 1 is the challenge, its heading the question — fixed
  wording "Better with AI, or replaced by it?" — and its body the
  pain the forge answers, scannable. The body opens with the fixed
  answer sentence "Forge of Thought is for those who chose to be
  better." followed in the same paragraph by the lead-in "The
  failure modes it exists to remove:" — then five bullets, no
  closing line: thinking scattered across chat sessions that die,
  taking their context with them; handovers whose completeness
  depends on the mood of the day they were written; the same
  thinking retold to every audience — a pitch, a deck, a mail — each
  version rewritten by hand and drifting from the others; feedback
  and decisions with no place to land, so the same ground is fought
  over twice; assumptions nobody attacked before reality did. No
  rhetoric and no restatement of the principle — the masthead
  already carries the answer.
- Section 2 is "What you get": a strictly concrete capability list —
  six bullets, no philosophy (that is the masthead's job): a
  versioned document chain growing from a brief — your idea put
  together, yours by your approval — through the intent to the
  layers your project needs, an assignment to hand over and a
  solution design among them; an elicitation interview that forges
  the intent; blind adversarial reviewers — critics of the
  documents, challengers of the thinking, checks of the
  conventions — every verdict recorded; audience-specific renders
  generated from recipes, including an actual PowerPoint file
  through the user's own template; external sources registered
  immutably and used only as the principal directs; everything in
  files and git — nothing depends on a chat's memory. Each bullet
  ends with a relative link in parentheses to the page of `docs/`
  that explains it, taken from the index's own listing (the chain to
  `docs/about/the-document-chain.md`, the interview to
  `docs/about/elicitation.md`, the reviewers to
  `docs/about/isolated-reviewers.md`, the renders to
  `docs/about/renders-and-recipes.md`, the sources to
  `docs/about/sources-and-research.md`, git to
  `docs/about/persistence-in-git.md`).
- Section 3 is a Quickstart with a common head and two named paths.
  The head, "First, once per machine", is a short fenced block: clone
  this repository (no URL; the reader is already looking at it, with
  a comment "you are looking at it"), install Claude Code first
  (comment: what to install and how is `docs/start/install.md`),
  start `claude` — always from the engine root — and `/setup`
  (comment: first run only; what it asks is `docs/start/setup.md`).
  Then two bold-led paths, each its own fenced block: **Starting a
  new project** — `/new-project my-idea`, `/forge intent`, `/save`;
  **Bringing an existing project** — `/import-project <project url>`
  (comment: clones into `projects/`) and `/forge <project-slug>`
  (comment: the slug is the repository's name; select the project
  before any work — the forge cannot guess it). Closing sentence:
  each project lives inside `projects/<slug>/` as a git repository
  of its own, which the engine does not track — that is why you name
  it first; the first sitting from nothing to a saved intent is
  `docs/start/first-result.md`.
- Section 4 is "The document chain in one picture". It carries the
  star, never a line: it must make visible at first glance that the
  chain branches richly. It is this mermaid block, pinned verbatim
  (solid arrows = built today, dashed = illustrative growth):

  ```mermaid
  flowchart LR
      B["00-brief"] --> I["10-intent"]
      I --> A["20-assignment"]
      I --> SD["40-solution-design"]
      A --> SD
      I --> RI(["renders: pitch, deck, summary …"])
      A --> RA(["renders: mail …"])
      A -.-> BRD["30-brd<br>business analysis"]
      BRD -.-> SD
      A -.-> RFP["an RFP"]
      I -.-> ART["an article"]
      ART -.-> RT(["render: a translation"])
      I -.-> ST["strategy"]
      SD -.-> IMP["implementation deck"]

      classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
      classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
      classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
      class B,I,A,SD built
      class BRD,RFP,ART,ST,IMP future
      class RI,RA,RT render
  ```

  Directly under it one bold legend line: blue = chain artefacts
  (light = not built yet), green = renders; dashed arrows = growth
  that does not exist yet. The dashed layers are a fixed illustrative
  set of this recipe (business analysis, an RFP, an article with its
  translation render, strategy, an implementation deck), never
  presented as planned or existing. Below the legend: one line per
  artefact the forge has, one per definition in
  `.claude/skills/forge/states/`, in the order of their file numbers,
  the name in bold and one sentence from the definition's
  `description`, each ending with a link to its page in `docs/about/`
  as the index lists it; then one sentence that below the intent a
  project takes the layers it needs, none a condition of another, and
  many end at the intent; then exactly one principle set as a `>`
  callout block, one line: a render is never edited by hand — what is
  iterated is its recipe. No other callout anywhere, and nothing
  else in this section: the chain is explained in `docs/`.
- Section 5 is "Documentation". It opens with one sentence: the
  documentation of the forge is in [`docs/`](docs/README.md), pages
  of one topic each, generated from the engine like this README.
  Then the three readers as three bullets, one line each, taken from
  the index's "Where to start": the user, the extender, the
  evaluator, each with where to begin as a relative link into
  `docs/`. Then one sentence giving the version the documentation
  was generated for and the date, taken from the index's own version
  line, and that the index says it too. Nothing else: no page list,
  no summary of what the pages say.
- The section "Author and licence" precedes "About this README" and
  carries this fixed text verbatim, nothing more: "Forge of Thought ©
  Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com. Licensed under
  [CC BY 4.0](LICENSE): use and adapt it freely; credit the author
  and link to this repository." and, as a paragraph of its own,
  "Feedback, ideas and changes are welcome: see
  [CONTRIBUTING.md](CONTRIBUTING.md)." (POS.1440 of the intent; the
  link is relative, exactly as given). The author line is the one
  place the README names a person: it is the licence holder, not the
  current principal.
- The closing section is titled "About this README" and states that
  this file is a render: never edited by hand, regenerated by
  `/render readme` whenever the process changes (and by every
  `/release` of the engine); fixes go into the recipe or the inputs;
  the documentation in `docs/` is generated the same way, from the
  engine, and its index says when and for which version. The
  render's YAML front-matter provenance is kept by design.
- Keep the visible dated footer `_Last updated: <render date>_` at the
  end of the file.

## Pinned facts (not rendered)
These facts have no owner among the engine's files and this recipe
is their one home until they get one (brief `documentation`, THR.0340:
the place of the pinned facts). The README does not print them; the
documentation's planner reads them here as an owner, and
`docs/start/install.md` and `docs/start/setup.md` are where they
reach the reader. Update them here when they change.
- Prerequisites: git; Python 3.8 or newer, on PATH as `python` -
  the scripts and the per-prompt hook are Python (on Linux or macOS,
  where only `python3` exists, give it that name by an alias or the
  `python-is-python3` package); a paid Claude subscription.
- Installing Claude Code: Windows `irm https://claude.ai/install.ps1
  | iex`; macOS/Linux `curl -fsSL https://claude.ai/install.sh |
  bash`; or `npm install -g @anthropic-ai/claude-code`. Sign in on
  first run — usage draws from the same pool as Claude chat. Always
  start `claude` from the engine root so CLAUDE.md and
  CLAUDE.local.md load.
- The forge is cloned, not copied: `forge-save.py` refuses an
  engine that is not a git repository.
- Script prerequisites: `doc2md.py` needs markitdown
  (`pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`); the `pandoc`
  engine of `md2pptx.py` and `md2docx.py`, behind `/render`, needs
  pandoc (https://pandoc.org/installing.html); their `claude`
  engine, behind `/publish`, needs the `document-skills` plugin,
  installed once from an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`), unless
  Claude Code already brings the docx and pptx skills; the git
  scripts need nothing beyond git.

## Template
# Forge of Thought <version>

*<subtitle per POS.0620>* · [Documentation](docs/README.md) · [Release notes](RELEASE-NOTES.md)

<masthead per the instruction: identity paragraph — AI cognitive
extension of a thinking human, the principal; what it does; the
principle as bridge — then the three bold-led bullets (It thinks
with you / It keeps the work consistent / It carries the tedious
work); closing paragraph with the ontological sentence (a git
repository: slash commands, isolated agents — challenger personas
and critic lenses — templates, conventions), where the chain ends
today as fact — no mention of who the current principal is>

<the fixed "Short on time?" paragraph with the two links to the CTO
and the CEO note, exactly as the instruction gives it>

## 1. Better with AI, or replaced by it?
<the fixed answer sentence and lead-in, then the five pain bullets
per the instruction; no closing line>

## 2. What you get
<the six concrete capability bullets per the instruction, each
ending with its link into docs/>

## 3. Quickstart
<common head "First, once per machine" as a fenced block: clone this
repository → install Claude Code (docs/start/install.md) → claude
from the engine root → /setup (docs/start/setup.md); then two
bold-led paths, each a fenced block: Starting a new project
(/new-project my-idea → /forge intent → /save) and Bringing an
existing project (/import-project <project url> →
/forge <project-slug>, with the select-before-work comment); one
closing sentence: each project is a repository of its own inside
projects/, untracked by the engine — that is why you name it first;
the first sitting is docs/start/first-result.md>

## 4. The document chain in one picture
<the pinned star chain diagram (mermaid) with its legend line; one
line per artefact from the definitions, each linked to its docs
page; the one sentence on layers taken as needed; the
render-never-hand-edited callout>

## 5. Documentation
<one sentence with the link to docs/README.md; the three readers as
bullets with where each begins; the version and date the
documentation was generated for>

## 6. Author and licence
<the fixed author-and-licence text>

## 7. About this README
<this file is a render of projects/forge — regenerated by
/render readme, never edited by hand; fixes go into the recipe or the
inputs; the documentation is generated the same way and its index
says when and for which version; provenance front-matter kept by
design; system changes are recorded in projects/forge/>

_Last updated: <render date>_
