---
project: forge
purpose: readme
audience: humans arriving at the repository
version: 0.73
output: /README.md
---

# Recipe — readme

<!-- A recipe: CLAUDE.md, Document chain, Renders (what it is) and
Versioning & status (how it is versioned). This skeleton owns the
shape only. -->

## Inputs
- CLAUDE.md
- projects/forge/10-intent.md
- .claude/skills/forge/states/   # the definitions of the artefacts:
                                 # one line each in the chain picture
- docs/README.md                 # the documentation index: its
                                 # version line, the three paths and
                                 # the contents
- RELEASE-NOTES.md               # the newest approved section: what
                                 # the major closed and what was added

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
- Portability is said as the inputs say it (POS.0830): developed and
  run on Windows; the git scripts, the ledger and docs-state run on
  Linux on a user's machine; the conversions and the two hooks are
  written to run unchanged on Linux and macOS, never said as having
  run there.
- Tone: plain, direct, no marketing. UK English. No long dash
  anywhere: a colon, a full stop or a spaced hyphen where one would
  stand. Every core term (principal, brief, intent, render, recipe)
  is set in bold at its first definition, and "principal" is defined
  at its first use.
- The title is `# Forge of Thought <version>` — the current version
  of the forge intent (its front-matter version), no status
  annotations. Below it one line: the subtitle fixed by POS.0620,
  followed by ` · [Documentation](docs/README.md) ·
  [Videos](<the pinned course address>) ·
  [Release notes](RELEASE-NOTES.md)`, the two links a reader looks
  for first, on the first line. The name
  appears large exactly once; there is no separate version line, and
  the intent version in the title is the only version that appears
  in the README's own words.
- Directly below the title line, before the masthead, stands one line
  for the reader who has never seen the forge: bold-led "**New here?
  Watch first.**", then one sentence: ten videos and eight short
  clips of real sessions, in two languages, show
  the forge at work before a word of this README is read; the link
  named "Videos" to the pinned course address. Nothing else on that
  line.
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
- Section 2 is "Watch it work": the videos as the first thing after
  the challenge, because seeing beats reading for a newcomer. One
  opening sentence: every video is a real session of the forge, cut
  to a few minutes and played in the browser as a simulated
  terminal with captions, in two languages, nothing staged. Then
  the ten videos as ten bullets in the order of the pinned list,
  each bold-led by the video's name, one sentence on what it shows
  (taken from the pinned list), and two links at the end: "watch"
  to the course address with the video's anchor (the pinned
  address, a `#` and the video's file name), and "read" to the page
  of `docs/` the pinned list pairs it with, as a relative link. A
  closing sentence: the whole course is at the course page, where
  each video has its scenes as chapters and the language is a
  switch, and where the eight short clips of the pinned list stand
  in the order of a talk. No other content in this section.
- Section 3 is "What you get": a strictly concrete capability list —
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
- Section 4 is "What is new in <major>", the major being the newest
  approved section of RELEASE-NOTES.md. One short bold-led paragraph
  per thing that section's opening paragraph says the major closed,
  in its order, and one per command born in the span (the Added
  group of that section, the commands only), each paragraph saying
  what the reader can now do and why it matters, two or three
  sentences, ending with a relative link to the page of `docs/` the
  index lists for it. A closing line points to RELEASE-NOTES.md for
  the full account. Nothing older than the newest major.
- Section 5 is a Quickstart with a common head and two named paths.
  The head, "First, once per machine", is a short fenced block: a
  comment line that git, Python and Claude Code must be installed
  first (what and how is `docs/start/install.md`), clone this
  repository (no URL; the reader is already looking at it, with a
  comment "you are looking at it"), start `claude` — always from the
  engine root — and `/setup` (comment: first run only; what it asks
  is `docs/start/setup.md`). Then two bold-led paths, each its own
  fenced block: **Starting a new project** — `/new-project my-idea`,
  `/forge intent`, then the one-off act in the reader's own terminal
  at the engine root, `git -C projects/my-idea init -b main`, with
  the comment that Claude writes nothing into git itself, the init
  and a remote being the reader's one-off act, then `/save`, with the comment that a save that commits
  nothing names its cause (no repository, or no git identity for the
  host) and `docs/start/first-result.md` says what to do;
  **Bringing an existing project** — `/import-project <project url>`
  (comment: clones into `projects/`) and `/forge <project-slug>`
  (comment: the slug is the repository's name; select the project
  before any work — the forge cannot guess it). Closing sentence:
  each project lives inside `projects/<slug>/` as a git repository
  of its own, which the engine does not track — that is why you name
  it first; then one sentence: `projects/forge` is the forge's own
  project, the exemplar every render and page of the documentation
  derives from, and the one directory under `projects/` the engine
  tracks; a user never needs to open it; the first sitting from
  nothing to a saved intent is
  `docs/start/first-result.md`.
- Section 6 is "The document chain in one picture". It carries the
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
      A --> BRD["30-brd"]
      BRD --> SD
      A -.-> RFP["an RFP"]
      I -.-> ART["an article"]
      ART -.-> RT(["render: a translation"])
      I -.-> ST["strategy"]
      SD -.-> IMP["implementation deck"]

      classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
      classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
      classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
      class B,I,A,BRD,SD built
      class RFP,ART,ST,IMP future
      class RI,RA,RT render
  ```

  Directly under it one bold legend line: blue = chain artefacts
  (light = not built yet), green = renders; dashed arrows = growth
  that does not exist yet. The dashed layers are a fixed illustrative
  set of this recipe (an RFP, an article with its translation render,
  strategy, an implementation deck), never
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
- Section 7 is "Documentation". It opens with one sentence: the
  documentation of the forge is in [`docs/`](docs/README.md), pages
  of one topic each, generated from the engine like this README.
  Then the three readers as three bullets, one line each, taken from
  the index's "Where to start": the user, the extender, the
  evaluator, each opening with the video to watch first (the user:
  how a brief is born; the extender: a new artefact; the evaluator:
  a challenger; each as a "watch" link with its anchor) and then
  where to begin reading as a relative link into `docs/`. Then one sentence giving the version the documentation
  was generated for and the date, taken from the index's own version
  line, and that the index says it too. Then the five sections of
  the documentation as five bullets in the index's order, each the
  section's name linked to its heading in the index and one sentence
  on what the section holds; the page titles stay in the index.
  Then a paragraph on how the videos are made, two sentences: each
  is a screenplay rendered from the session records of the
  principal's rollout project and made into a player file by
  `scripts/md2video.py`; the files live in `docs/videos/`, served
  as the course page, and the documentation on making one is the
  page "Make a teaching video from a recipe" (a relative link).
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
is their one home until they get one (POS.1450 and SOL.0500: the
place of the pinned facts). The README does not print them; the
documentation's planner reads them here as an owner, and
`docs/start/install.md` and `docs/start/setup.md` are where they
reach the reader. Update them here when they change.
- Prerequisites: git; Python 3.8 or newer, on PATH as a real
  executable named `python` - the scripts and the per-prompt hook
  are Python, and the hook is started without a shell, so a shell
  alias does not reach it (on Debian or Ubuntu the package
  `python-is-python3`; elsewhere on Linux and on macOS a symlink,
  `ln -s "$(command -v python3)" /usr/local/bin/python`); a paid
  Claude subscription.
- Installing Claude Code: Windows `irm https://claude.ai/install.ps1
  | iex`; macOS/Linux `curl -fsSL https://claude.ai/install.sh |
  bash`; or `npm install -g @anthropic-ai/claude-code`. Sign in on
  first run — usage draws from the same pool as Claude chat. Always
  start `claude` from the engine root so CLAUDE.md and
  CLAUDE.local.md load.
- Public home of the engine:
  https://github.com/pche-broken-artist/forge-of-thought, the address
  a clone and a project's README point to.
- The teaching videos: the course page
  https://pche-broken-artist.github.io/forge-of-thought/videos/,
  served by GitHub Pages from `docs/videos/` of this repository
  (POS.1540); a player page and one `html-player.js` file per video
  and language, made by `scripts/md2video.py` from screenplay renders
  (POS.1530). The videos, in the order of the course, each with its
  anchor on the course page, what it shows, and the page of `docs/`
  it pairs with:
  1. How a brief is born (`#01-brief-elicitation`): a brief found by
     questions, a critique from outside, research, the approval, the
     mining; `docs/use/write-a-brief.md`.
  2. One item, one verdict (`#02-walkthrough`): a list settled one
     item per message, the verdict line, one write at the end of
     the round; `docs/use/walk-through-a-list.md`.
  3. From the brief to the intent (`#03-brief-to-intent`): the
     brief mined into positions, rejections and threads, cited at
     its version; `docs/use/forge-the-intent.md`.
  4. A critic and walking its findings (`#04-critique`): an
     isolated reviewer of document quality, its findings mended or
     rejected with a reason; `docs/use/critique-the-documents.md`.
  5. A check at a save (`#05-check-at-save`): a save runs the
     check, conformance findings settled before the commit, a
     release with more; `docs/use/save-your-work.md`.
  6. A challenger: peer review of the substance (`#06-challenger`):
     a persona attacks the thinking, accepted goes into the
     intent, rejected keeps its reason;
     `docs/use/challenge-the-thinking.md`.
  7. History and threads (`#07-history-threads`): why an item
     changed, one command away; the open threads as the project's
     memory; `docs/use/read-the-history-of-an-item.md`.
  8. Solution design: a new layer of the chain
     (`#08-new-artefact`): the chain grows by a definition and a
     template, the first solution design;
     `docs/extend/add-an-artefact.md`.
  9. The BRD, a new artefact (`#12-brd`): a new artefact from its
     definition to its first document; `docs/use/write-a-brd.md`.
  10. Research: a plan, two LLMs and a synthesis
     (`#13-deep-research`): the plan confirmed before the search, the
     same cards on two model families, the synthesis;
     `docs/use/research-a-topic.md`.
  The section "Presentation shorts" of the course page holds eight
  short clips in the order of a talk (`#s01-git-wall` to
  `#s08-github`): the wall between reading git and writing it, the
  principal deciding by a letter, a mistake becoming a rule,
  research planned first, elicitation one question at a time,
  handing over, reviewers that never saw the conversation, and
  GitHub from an issue to an answer.
- The forge is cloned, not copied: `forge-save.py` refuses an
  engine that is not a git repository.
- Script prerequisites: `doc2md.py` needs markitdown
  (`pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`); the `pandoc`
  engine of `md2pptx.py` and `md2docx.py`, behind `/render`, needs
  pandoc (https://pandoc.org/installing.html); `md2video.py`, behind
  `/render` of a screenplay, needs Pillow (`pip install pillow`) and
  ffmpeg on PATH for the video format and nothing beyond Python for
  the player format; their `claude`
  engine, behind `/publish`, needs the `document-skills` plugin,
  installed once from an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`), unless
  Claude Code already brings the docx and pptx skills; the git
  scripts need nothing beyond git.

## Template
# Forge of Thought <version>

*<subtitle per POS.0620>* · [Documentation](docs/README.md) · [Videos](<the pinned course address>) · [Release notes](RELEASE-NOTES.md)

**New here? Watch first.** <one sentence on the eight videos, with the link "Videos" to the course address>

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

## 2. Watch it work
<the opening sentence; the eight videos as bold-led bullets in the
pinned order, one sentence each and the two links watch / read; the
closing sentence on the course page>

## 3. What you get
<the six concrete capability bullets per the instruction, each
ending with its link into docs/>

## 4. What is new in <major>
<one bold-led paragraph per thing the newest approved section of
RELEASE-NOTES.md says the major closed, and per command born in the
span, each ending with its link into docs/; a closing line pointing
to RELEASE-NOTES.md>

## 5. Quickstart
<common head "First, once per machine" as a fenced block: git,
Python and Claude Code installed first (docs/start/install.md) →
clone this repository → claude from the engine root → /setup
(docs/start/setup.md); then two bold-led paths, each a fenced block:
Starting a new project (/new-project my-idea → /forge intent → git
init in your own terminal → /save, with what a save that commits
nothing means) and Bringing an
existing project (/import-project <project url> →
/forge <project-slug>, with the select-before-work comment); one
closing sentence: each project is a repository of its own inside
projects/, untracked by the engine — that is why you name it first;
one sentence on projects/forge, the forge's own project a user never
opens; the first sitting is docs/start/first-result.md>

## 6. The document chain in one picture
<the pinned star chain diagram (mermaid) with its legend line; one
line per artefact from the definitions, each linked to its docs
page; the one sentence on layers taken as needed; the
render-never-hand-edited callout>

## 7. Documentation
<one sentence with the link to docs/README.md; the three readers as
bullets, each opening with its video to watch and then where to
begin reading; the version and date the documentation was generated
for; then the five sections as five bullets, each linked to its
heading in the index with one sentence on what it holds; then the
two sentences on how the videos are made, with the link to the page
on making one>

## 8. Author and licence
<the fixed author-and-licence text>

## 9. About this README
<this file is a render of projects/forge — regenerated by
/render readme, never edited by hand; fixes go into the recipe or the
inputs; the documentation is generated the same way and its index
says when and for which version; provenance front-matter kept by
design; system changes are recorded in projects/forge/>

_Last updated: <render date>_
