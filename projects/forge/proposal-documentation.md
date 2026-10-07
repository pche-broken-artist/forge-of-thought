---
project: forge
date: 2026-10-05
title: The documentation of the engine — a proposal
author: Claude, handed over by the principal
judged: not yet
---

# The documentation of the engine — a proposal

This is a working file, not a document of a kind the forge knows. It
holds a proposal handed over to Claude on 2026-10-05 and not yet
judged (CLAUDE.md, Working methods, Handing over). Nothing is derived
from it and nothing is done on it until the principal has walked it
through. What he accepts lands in the intent (positions, rejections,
the thread THR.0340), in the solution design (parts) and in recipes;
this file is then deleted or moved to wherever working files get a
home (the brief `next-gen`, "Further outputs and working files").
Until then it sits in the project root outside the conventions, and
a check will name it; that is known.

## 0. What this rests on

The principal's words of 2026-10-05, in five decisions, each his:

1. Three readers, in this order: the **user** who clones the forge
   and forges his own thinking; the **extender** who adds an artefact,
   a lens, a persona, a genre or a check; the **evaluator** who never
   runs it and wants to understand what it is and how it works. The
   evaluator gets the concept pages and nothing made for him alone.
2. The package is the documentation and the cut of the README that
   points to it. The "what's new" piece beside the release notes is a
   round of its own, not this one. THR.0340 no longer waits for the
   engine split (THR.0230): pages of one topic each move whole
   between repositories if the split comes, so the reason to wait
   fell (research of 2026-10-03, point 7).
3. English only, the project's output language. A translation, if
   ever wanted, is a render of the same recipe in another language.
4. A quickstart now, no sample project; the tutorial with a worked
   example is a round of its own, after a public exemplar exists
   (THR.0200). The structure keeps its place.
5. The proposal lands in a file in the project root; a vehicle for
   handed-over work is an open matter of the brief `next-gen`.

What Claude read, by eight isolated readers on 2026-10-05, each
reporting what a part of the forge does, how, and what it defines:
CLAUDE.md on disk and every template; every command skill; the
`/forge` dispatcher, the four definitions, `/new-artefact`, the
walkthrough skill and the hook; the nine agents, the three contracts
and `.claude/settings.json`; the nine scripts; the intent 4.58 with
`threads.md`; the solution design 0.3 with `decisions.md`; the seven
research notes on documentation, news, the threshold of entry, how
things are born, adding a type, user extensions and CONTRIBUTING, and
the README of 4.58 with its recipe. Every reader reported the same
first fact: the CLAUDE.md in a subagent's context is the one of the
session start, not the file on disk (THR.0580). Everything below is
from the files on disk.

The recommendation of `research/2026-10-03-how-project-documentation-is-built.md`
is taken as the frame: plain pages in `docs/`, one topic and one
type each, sorted by the reader's journey at the top and by the four
kinds of Diátaxis at the page (start path, how-to, explanation,
reference), the README orienting and pointing, reference derived
from the definitions that own it, the rest rendered from recipes.
Where this proposal departs from the note, it says so.

## 1. What each reader must be able to do

- **The user**, after the start path: install, run `/setup`, make a
  project, put a brief in, work an intent round, save. After the
  how-to pages: every job the forge has a command for, without
  reading a skill file. After the concept pages: know why the forge
  asks what it asks, so that he works with it and not around it.
- **The extender**: know what the engine is made of (types and
  members), what a member's files are, what is written where, what
  is forbidden (a Lens that restates its contract, a roster written
  by hand), how a change is proved and recorded. For an artefact:
  the seven blocks, what each must say, how the template pairs with
  the definition, what `/new-artefact` does and what it leaves to
  him.
- **The evaluator**: what the forge is and is not, how a thought
  travels it, what the reviewers are and why isolation is not
  independence, how Claude Code runs it, what it costs to enter.

## 2. The shape

- **Where:** `docs/` at the engine root, plain Markdown, read on
  GitHub and in a clone; `docs/README.md` is the index, one line per
  page; relative `.md` links throughout, so that a site can be laid
  over the same files later without rewriting a page. No site now, no
  wiki (research options B and C, against).
- **Sections by the reader's journey**, each a directory:
  `start/`, `use/`, `about/`, `extend/`, `reference/`. Each page is
  one topic of one kind: `start/` and `use/` are how-to (the start
  path is how-to in miniature), `about/` is explanation, `extend/` is
  how-to for the extender with the explanation it needs, `reference/`
  is derived fact.
- **A page** opens with its title, one paragraph saying what it is
  for and for whom, then its matter, then "See also" with few,
  descriptive links. It establishes its own context (Every Page is
  Page One) and never depends on a link to be understood. It carries
  the render's YAML provenance like every render.
- **Two readers of one source:** `/man` reads the definitions in the
  session for the agent and the newcomer; `docs/reference/` is the
  same reading made into files for the person who opens the
  repository. Neither restates the other: both read the owners
  (POS.1070, POS.1190).

## 3. The page map

Paths are under `docs/`. "Made by" is section 4's: *recipe* means
one recipe of the forge project rendered by `/render`, *script*
means derived by the reference script, *recipe (pinned)* means a
recipe whose Template carries the text verbatim because it is not
derivable from any owner. "Inputs" names the owners the page is made
from; the positions give the why and are cited as inputs of the
explanation pages only.

### `docs/README.md` — the index

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `README.md` | index | all | one line per page, grouped by section; the three paths (use it, understand it, extend it); where news will be | the docs recipes (each `purpose` line) | recipe |

### `start/` — the start path

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `start/install.md` | how-to | user | prerequisites by function (always: a paid plan, Claude Code, git, PowerShell 7 for the hook; for some functions: markitdown with Python, pandoc, the document skills); installing; cloning the engine; `/setup` step by step incl. the git identity per host; what runs without the optional tools | `.claude/skills/setup/SKILL.md`, `scripts/*.ps1` help headers, CLAUDE.md Persistence | recipe |
| `start/first-project.md` | start path (quickstart) | user | a first project in one sitting: `/new-project`, the brief pasted or dictated, `/forge intent` and the first round, the verdict words, `write`, `/save`; what the files are afterwards. One sentence holds the place of the tutorial with a worked example (THR.0200) | `new-project`, `forge/states/brief.md`, `forge/states/intent.md`, `walkthrough`, `save` | recipe |

### `use/` — how-to, one page per job

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `use/work-the-chain.md` | how-to | user | the `/forge` map; a round over an artefact: ways in, the interview, the walkthrough, `write`; versions, approval, history records, threads; `/ledger` | `forge/SKILL.md`, the four state files (Course), `walkthrough`, `ledger`, CLAUDE.md Versioning & status, `templates/history.md`, `templates/threads.md` | recipe |
| `use/sources-and-research.md` | how-to | user | `/ingest` with a file, with pasted text, bare (the sweep); binaries and the one-form question; bundles; the Role; personal matter; `/research`; the indexes | `ingest`, `research`, `scripts/doc2md.ps1` header, `templates/index.md`, `templates/index-bundle.md` | recipe |
| `use/reviewers.md` | how-to | user | when to run which reviewer; `/critique`, `/challenge`, `/check` with and without a target; reading a report; settling findings and challenges by walkthrough; what each verdict writes; the immediate fixes of a check; rejected by DEC | `critique`, `challenge`, `check`, the three contracts (report shape), `templates/ledger.md` (states), `walkthrough` | recipe |
| `use/renders-and-publishing.md` | how-to | user | composing a recipe by genre; `/render`; the plain file; `/publish` and the designed file; the Format section; staleness; a render as an input of a render | `recipe` with its genres, `render`, `publish`, `templates/recipe*.md`, `scripts/md2docx.ps1` and `md2pptx.ps1` headers | recipe |
| `use/save-and-release.md` | how-to | user | `/save`, `/release`, what each runs and renders; the commit message from the records; branches by `forge-branch`; tags; what happens with no identity, no origin, a diverged remote | `save`, `release`, `scripts/forge-save.ps1`, `forge-branch.ps1`, `forge-status.ps1` headers | recipe |
| `use/upgrade-and-migrate.md` | how-to | user | `forge-pull` as the upgrade channel; the release notes and their Action required lines; `/check light` and `/check project` after a pull; migration on the user's word; a stale clone (THR.0490 as it stands) | `scripts/forge-pull.ps1` header, CLAUDE.md Persistence, `recipes/release-notes.md`, `check` | recipe |
| `use/projects.md` | how-to | user | a thought project and a library; `/new-project`; the project's repository and remote by hand; `/import-project`; `/spinoff`; dependencies on a library; `logo.png`; "not under git" as a property | `new-project`, `import-project`, `spinoff`, `ingest` (dependencies), `scripts/forge-clone.ps1` header, `templates/ledger.md` | recipe |

### `about/` — explanation: the mechanism and why

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `about/the-forge.md` | explanation | evaluator, user | what the forge is and is not; the principal and Claude; the ten prime directives with their reasons; what it costs to enter; what it is called and why | CLAUDE.md What this workspace is, Roles, Prime directives; POS.0005–0070, POS.0600–0620, POS.0780, POS.1050 | recipe |
| `about/working-methods.md` | explanation | user | the eleven methods, each with its reason; the verdict words and why they have letters; `??`; in pieces; handing over; the hook that repeats the rule | CLAUDE.md Working methods, `walkthrough`, `scripts/hook-walkthrough.ps1`; POS.0850–0910, POS.1160, POS.1170, POS.1210, POS.0190 | recipe |
| `about/document-chain.md` | explanation | all | the star: brief, intent as the trunk, the layers a project takes; document kinds; artefact versus render (authorship); intent-first; why the intent exists; threads; the ledger as the one state | CLAUDE.md Document chain, Document kinds, Ledger; POS.0100–0180, POS.0580, POS.1080, POS.1390, POS.1400, POS.0120 | recipe |
| `about/elicitation.md` | explanation | user, extender | what elicitation is; map, process and template kept apart; the seven blocks and what each is for; the Map walked, nothing recorded; found together versus handed over; certainty said in words | POS.1300–1320, POS.1370, POS.1410, `templates/artefact-definition.md` | recipe |
| `about/artefacts/brief.md` | explanation | user | the brief: what it is, its aim, Claude's part, the areas of its map, the ways in, the two marks, the template line by line, approval and mining | `forge/states/brief.md`, `templates/brief.md`; POS.0110, POS.0920, POS.1330 | recipe |
| `about/artefacts/intent.md` | explanation | user | the intent: aim, the Map's eight areas, the course of a round, threads and how they close, the template section by section, POS/FCT/REJ/THR, the reality check, the horizon | `forge/states/intent.md`, `templates/intent.md`, `templates/threads.md`; POS.0120, POS.1340, POS.1360, POS.1390 | recipe |
| `about/artefacts/assignment.md` | explanation | user | the assignment: aim and completeness, the joint pass in three phases, the provenance map, the template section by section, every prefix, the Requirement style with its reasons | `forge/states/assignment.md`, `templates/assignment.md`; POS.0130, POS.0200–0290, POS.1350 | recipe |
| `about/artefacts/solution-design.md` | explanation | user | the solution design: when a project takes one, aim, the Map's ten areas, the coverage map, the shape of a SOL and a TBC, the template, the architect challenger | `forge/states/solution-design.md`, `templates/solution-design.md`; POS.1400, POS.1420, POS.1390 | recipe |
| `about/versions-and-history.md` | explanation | user | the house scheme and status words; the history log and its record; the archive; `last_change`; decisions; the ledger; immutables; why the body is the state and the companion the record | CLAUDE.md Versioning & status, `templates/history.md`, `templates/decisions.md`, `templates/ledger.md`; POS.0300–0330, POS.0820 | recipe |
| `about/reviewers.md` | explanation | all | the three kinds and what each judges; isolation mechanically (subagent, what it sees, tools); contract versus Lens; reports, states, the ledger; why isolation is not independence; nothing blocks; the independent challengers to come | CLAUDE.md Isolated reviewers, the three contracts, the nine agents; POS.0400–0450, POS.0540, POS.0790, POS.0800, POS.1120, POS.1140 | recipe |
| `about/renders.md` | explanation | user | recipe, render, genre, provenance, staleness; the two steps of an output and their cost; README, release notes and CONTRIBUTING as renders; pinned text; why a regeneration passes under the principal's eyes | CLAUDE.md Document chain Renders, `templates/recipe.md`; POS.0590, POS.0710–0730, POS.0810, POS.1000, POS.1440 | recipe |
| `about/persistence.md` | explanation | user, evaluator | one engine repository, one per project; the scripts as the only door and why; the deny rules; the identity per host; `main`, branches, tags; the upgrade channel; portability and Python | CLAUDE.md Persistence, `.claude/settings.json`, the five git scripts' headers; POS.0550, POS.0830, POS.0940, POS.0950, POS.1050, POS.1100, POS.1110, POS.1200 | recipe |
| `about/operating-layer.md` | explanation | extender, evaluator | how Claude Code runs the forge: CLAUDE.md always-on, skills read on invocation, states and genres as supporting files, agents as subagents with a preloaded contract, the hook, the settings and the guard field, one model inherited, memory kept out; what a subagent receives and what it does not | `40-solution-design.md` SOL.0010–0040, SOL.0100–0110, SOL.0300, SOL.0330, SOL.0520, SOL.0600; POS.1030, POS.1070, POS.1090, POS.0930, POS.1170 | recipe |
| `about/the-forge-project.md` | explanation | evaluator, extender | the engine developed through itself: `projects/forge`, its briefs, intent, solution design, threads, decisions; the operating-layer record; a release of the engine; what a reader finds there | CLAUDE.md The system's own project; POS.0720, POS.0310, POS.0300 | recipe |

### `extend/` — for the extender

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `extend/how-the-engine-grows.md` | explanation + how-to | extender | the types of the engine and their members; the spine of every addition: the decision as a position, files from the skeleton, rosters scanned and never written, proof by the checks and one real run, the record and the release; what a Lens may and may not do; one mechanism in one place | `research/2026-09-30-adding-a-new-type-to-the-engine.md`, `new-artefact`, CLAUDE.md Isolated reviewers, Templates; POS.0030, POS.1070, POS.1430 | recipe |
| `extend/new-artefact.md` | how-to | extender | `/new-artefact` step by step; what to have thought through before; the seven blocks, one by one, with what each must say and an example from a definition on disk; the template as the pair; prefixes; reviewers; the solution-design item; the first run on real work | `new-artefact`, `templates/artefact-definition.md`, the four state files as models; POS.1310, POS.1320, POS.1380, POS.1430 | recipe |
| `extend/new-reviewer.md` | how-to | extender | a lens, a persona, a check from the three skeletons; the front-matter line by line, the quoting rule, the fixed tail of the description; the one Lens section and its parts per kind; what the contract owns; where the decision is recorded; proof | `templates/critic-definition.md`, `challenger-definition.md`, `check-definition.md`, the three contracts, `check-engine` | recipe |
| `extend/new-genre-command-script.md` | how-to | extender | a render genre (two files); a command (the skill shape, `description`, `argument-hint`, the guard field, citing by path); a script (the help header, what it may never carry, portability, Python) | `recipe/SKILL.md`, `templates/recipe.md`, SOL.0100, SOL.0110, SOL.0620, CLAUDE.md Portability | recipe |
| `extend/your-own-extensions.md` | how-to | extender | *later*: where a user's own members live and survive an upgrade — waits for THR.0300; until then a paragraph in `how-the-engine-grows.md` says what works today (Claude Code's user level, its two collision rules) and that the place is open | `research/2026-10-03-user-extensions-kept-apart-from-the-core.md` | recipe, phase 3 |

### `reference/` — derived from the owners

| Page | Kind | Reader | What it gives | Inputs | Made by |
|---|---|---|---|---|---|
| `reference/commands.md` | reference | all | every command with its arguments and purpose | CLAUDE.md Commands table; each skill's `description` and `argument-hint` | script |
| `reference/artefacts.md` | reference | user | the artefacts the forge has: `description`, Target, Inputs of each definition, with a link to its concept page | `.claude/skills/forge/states/*.md` | script |
| `reference/reviewers.md` | reference | user | the rosters: every lens, persona and check with its `description` and its Lens section | `.claude/agents/*.md` | script |
| `reference/genres.md` | reference | user | the genres with their description and checklist | `.claude/skills/recipe/genres/*.md` | script |
| `reference/scripts.md` | reference | user | every script: synopsis, parameters, what it needs, what it refuses, examples | `scripts/*.ps1` help headers | script |
| `reference/conventions.md` | reference | all | the ID scheme, the document kinds, the versioning scheme and status words, the record kinds, the finding and challenge states, the Requirement style | CLAUDE.md ID scheme, Document kinds, Versioning & status; `templates/history.md`, `templates/ledger.md`; `forge/states/assignment.md` Requirement style | script |
| `reference/layout.md` | reference | all | the repository layout of the engine, a thought project and a library | CLAUDE.md Repository layout | script |
| `reference/templates.md` | reference | extender | every template with the document it is the skeleton of | `templates/*.md` (the first comment of each) | script |
| `reference/glossary.md` | reference | all | the terms of the forge, one sentence each, in the words the files give them | the glossary is pinned in its recipe; not derivable from one owner | recipe (pinned) |

Thirty-seven pages with the index; thirty-six without
`your-own-extensions.md`. The count is the price of "explain every
skill, every mechanism, every template"; section 7 phases it.

## 4. How the pages are made

Three ways, chosen by what the page holds; nothing by hand, since a
hand-composed page would be a new document kind (research option 3,
against, and prime directive 2).

**(a) Explanation, how-to and the start path: one recipe per page,
rendered by `/render`.** The mechanism exists (a recipe's `output:`
path, the isolated subagent, provenance, the Renders table). Each
page is `projects/forge/recipes/docs-<section>-<page>.md` with
`output: /docs/<section>/<page>.md`; the prefix keeps the flat
`recipes/` the layout prescribes. A new genre `docs-page` gives the
recipes one shape and one interview: a genre file
`.claude/skills/recipe/genres/docs-page.md` and a skeleton
`templates/recipe-docs-page.md` (two files, as every genre). What
the genre fixes:

- the checklist: the reader and what he can do after the page; the
  kind and the one topic; the owners (inputs) and, for an
  explanation, the positions that give the why; what is pinned
  verbatim; the few links; what must not appear (instance facts,
  any project but `projects/forge`, company names);
- the instructions every docs recipe carries: the page stands
  alone; every claim derivable from the inputs or pinned; where the
  operating layer and the intent differ the operating layer's
  wording wins and the intent supplies the why; nothing of a skill
  copied as instructions to Claude, the page says what the command
  does for the person; UK English, plain; CLAUDE.md read from disk
  (THR.0580); the render's provenance front-matter;
- the template: `# <Title>`, the one paragraph of purpose and
  reader, the matter, `## See also`.

Chosen against one recipe per section producing many pages (one
long generation whose drift or failure touches every page; cannot
re-render one page) and against composing by hand (a new kind).
The cost: about thirty recipes to compose and keep, and a model
re-wording a page at every regeneration, which pinned text and
regeneration on the principal's word (section 5) bound.

**(b) Reference: derived by a script, deterministic.** A script
`scripts/docs-reference.py` reads the owners (the Commands table and
the skills' front-matter, the state files' heads, the agents, the
genres, the scripts' help headers, the tables of CLAUDE.md, the
templates' first comments) and writes `docs/reference/*.md`, each
with provenance front-matter naming its sources and the date. It is
the reading `/man` does, made into files. Run by `/release forge`
beside the README and the release notes, and by hand. The ledger's
Renders table carries one row for the set, Recipe = the script.

Chosen against rendering the reference by a model with "copy
verbatim" instructions (works today, no new mechanism, but a model
copying tables is neither cheap nor certain, and THR.0530 holds that
what can be done deterministically is done by a script) and against
not rendering the reference at all and linking to CLAUDE.md (free,
but those files address the agent, and a page for the human needs
one sentence of context at its head). The cost: a script to write
and keep with every change of a shape it reads, Python on the
machine of whoever releases the engine (THR.0150, the forge already
needs it for markitdown), and a stretch of the ledger's word
"recipe". This is the one new mechanism of the package; it can be
deferred, with the reference pages rendered by recipes meanwhile
and moved to the script when THR.0530 lands (TBC.0040 below).

**(c) The glossary: a recipe whose Template carries the text.** Not
derivable from one owner; the recipe pins it, the render copies it.
Legitimate today: the README recipe pins its masthead the same way.

**The index:** a recipe whose inputs are the docs recipes; it lists
each page from its recipe's `purpose` line, so that a page added is
a line added at the next render and never a hand edit.

## 5. When pages are regenerated

Today README and release notes are regenerated by every `/release`,
every other render as stale as the principal lets it (POS.0810).
Proposed for the documentation:

- `reference/` at every `/release forge`, by the script: cheap and
  deterministic, so nothing is lost by running it always.
- The recipe pages on the principal's word, by `/render
  docs-<page>`, never by a release: thirty model renders at every
  release would cost an hour and reword stable pages for nothing.
- `/release forge` reports, in its summary, the docs pages and the
  date each was generated, so that the principal sees what is old
  before he tags. A reminder, not a gate.

What is open and goes to the solution design as TBC.0050: how a
page's staleness is told when its inputs carry no version. The one
definition of stale (`/render` step 5) compares versions, and
CLAUDE.md, the skills and the agents have none, so a page citing
them is never stale by that definition. Three ways, none chosen
here: a content hash per unversioned input written into the
provenance by a script helper of `/render` (deterministic, extends
the definition cleanly, adds a helper); the file's modification
time against the page's generated date, as `/ingest` tells a
changed source (cheap, false positives after a fresh clone); the
principal's judgement with the release summary as his reminder
(nothing to build, the proposal's default until decided).

## 6. The README

`projects/forge/recipes/readme.md` goes to 0.57 and the README to
about one screen and a half: the title with the subtitle of
POS.0620 and the release-notes link; the masthead; "Short on time?";
1 Better with AI, or replaced by it?; 2 What you get; 3 Quickstart;
a new 4 **Documentation** — the link to `docs/README.md`, the three
paths in one line each, and the one sentence that the news will
have a place of its own; then Author and licence; About this
README; the footer. Chapters 4 to 14 of today's README (How it is
used, How the work feels, Roles, The document chain, Isolated
reviewers, Commands, Conventions, Repository layout, Setup,
Scripts, Planned extensions) leave the recipe as their pages land,
one chapter per page, so that at no moment is something documented
nowhere. The "You type" table moves to `about/working-methods.md`;
the Mermaid star to `about/document-chain.md`; Planned extensions
becomes a paragraph of `about/the-forge-project.md` (POS.0700). The
inputs the README no longer needs (`.claude/agents/`, the state
files, most skills, `scripts/`, `templates/ledger.md`) leave it;
its render time falls with them (THR.0410).

A project's README (the genre `readme`) is untouched: it is the
project's, not the engine's.

## 7. Phasing and cost

Pages in the order that keeps the README lossless and gives the
principal's priority, the depth, early. Each phase is one or two
rounds; a page's recipe is composed by Claude from this map and
judged by the principal (Handing over), one walkthrough item per
page or per section as he prefers.

| Phase | What | Pages | README chapters that leave |
|---|---|---|---|
| 1 | the frame: `docs/README.md`, the genre `docs-page`, the reference script, `start/install.md`, `start/first-project.md` | 2 + 9 reference + index | 12 Setup, 13 Scripts, 9 Commands (table), 10 Conventions, 11 Repository layout |
| 2 | the concepts the README carries today: `about/the-forge`, `working-methods`, `document-chain`, `reviewers`, `renders`, `persistence`, `versions-and-history` | 7 | 4, 5, 6, 7, 8, 14 |
| 3 | the depth: `about/elicitation`, the four `about/artefacts/*`, `about/operating-layer`, `about/the-forge-project`, the four `extend/*` | 11 | — |
| 4 | the jobs: the seven `use/*` | 7 | 9 (the prose), 12 (the how-to parts) |
| later | the tutorial (THR.0200), `extend/your-own-extensions.md` (THR.0300), the news (its own round) | 2 + 1 | — |

Phase 3 before phase 4 because the principal asked for the depth
first and the how-to pages are the ones most nearly covered by `/man`
in the meantime; the order is his to change. Cost, Claude's estimate
and not measured: a page render of one to three inputs takes one to
three minutes (the README with seven took three to six, THR.0410),
so about an hour of rendering for the whole set once, then only what
he asks for; composing the recipes is the larger work, about one
round per phase.

## 8. What the intent receives

New positions, worded here for the walkthrough, numbered at the
write:

- **POS (the documentation).** The engine's documentation is a set
  of single-topic pages in `docs/` at the engine root, each a render
  of a recipe of the forge project or derived by a script from the
  definitions, read on the platform and in a clone, with
  `docs/README.md` as its index; sorted by the reader's journey
  (start, use, about, extend, reference) and by one kind per page;
  for three readers in this order, the user, the extender, the
  evaluator; in the project's output language. The README orients
  and points and documents nothing itself beyond what it is, what
  one gets and how to start. Reference pages are derived
  deterministically from the owners they mirror; explanation and
  how-to pages are rendered from recipes of the genre `docs-page`
  and regenerated on the principal's word; a release regenerates
  the reference and reports the age of the rest. Reason: the README
  was the whole documentation and was poor as documentation; a page
  of one topic can say it well, and a derived reference cannot
  drift from what it mirrors.
- **POS (what a page is).** A page stands alone, says what it is for
  and for whom, derives every claim from its inputs or pins it,
  takes the operating layer's wording where it and the intent
  differ and the intent's reason, names no instance fact and no
  project but the forge's own, and links few and descriptive. The
  shape is the genre's; the rule is here.

Rejections:

- **REJ** A generated site or a wiki now: a toolchain and a public
  address for a decision on the public boundary not taken; a site
  can be laid over `docs/` later.
- **REJ** Pages composed by hand as a document kind of their own: a
  second place for what the intent holds as positions with reasons.
- **REJ** One recipe per section producing many pages: one long
  generation whose drift touches every page; no page can be
  regenerated alone.
- **REJ** The documentation regenerated by every release: an hour of
  renders and a re-wording of stable pages at every tag.

Threads:

- **THR.0340** closes into the position above, its open points
  answered: the conventions are rendered (derived, cheap), the cost
  per release is bounded by regenerating only the reference; what
  remains of it, a site if the outside reader becomes the first
  audience, is a line in the position's history. The decided order
  "after THR.0230" is withdrawn by the principal's word of
  2026-10-05.
- **THR.0200** notes that the documentation is the public face
  until the exemplar exists; the tutorial waits there.
- **THR.0530** is cited by the reference script as its first
  instance beyond the edge; nothing of it decided here.
- **THR.0580** gains the fact that every docs recipe must say
  CLAUDE.md is read from disk until the render skill says it once.
- **THR.0410** gains the README's render time falling with its
  inputs.
- A new thread for the staleness of unversioned inputs if the
  principal wants it in the intent rather than as a TBC of the
  design.

## 9. What the solution design receives

In the group *Rendering and publishing*, after SOL.0450:

- **SOL.0460 The documentation.** The pages of `docs/`, the index,
  the genre `docs-page`, the docs recipes of the forge project, the
  reference script, the regeneration rule. Realises: the two
  positions above, POS.0710, POS.1190. Choice: recipes rendered one
  per page and the reference by a script, against recipes for
  everything (no new mechanism, a model copying tables), against a
  site (a toolchain), against hand-written pages (a new kind); the
  cost is thirty recipes to keep, one script, and pages as stale as
  the principal lets them. Where: `docs/`,
  `projects/forge/recipes/docs-*.md`,
  `.claude/skills/recipe/genres/docs-page.md`,
  `templates/recipe-docs-page.md`, `scripts/docs-reference.py`.
  Breaks first: a page whose input has no version goes stale
  unseen (TBC.0050).

Parts amended:

- **SOL.0130** gains the genre `docs-page` in its sentence naming
  the genres.
- **SOL.0140** says that `/man` and `docs/reference/` read the same
  owners, the one in the session, the other into files.
- **SOL.0410** becomes "The engine's README and documentation":
  the README cut to orientation, the documentation beside it.
- **SOL.0500** names `docs/` among the root's contents.
- **SOL.0510** or **SOL.0620** names the reference script among the
  scripts and as the first in Python.
- **SOL.0530** says what a release regenerates (README, release
  notes, the reference) and reports (the docs pages' ages).

Open:

- **TBC.0040** (owner: principal) Whether the reference is derived
  by the script from the first phase or rendered by recipes until
  THR.0530 lands. Closed by: his word at the walkthrough. Blocks
  realisation: no.
- **TBC.0050** (owner: principal) How a page's staleness is told
  when its inputs carry no version (section 5). Closed by: a
  decision on the hash, the modification time, or judgement.
  Blocks realisation: no.
- **TBC.0060** (owner: principal) A mechanical check of the links in
  `docs/` — a new check, or a bullet of `check-engine`'s Lens
  (narrowing within its subject, the engine's consistency). Closed
  by: his decision; a new check is his alone. Blocks realisation:
  no.

CLAUDE.md changes, the smallest that hold: `docs/` with one comment
line in Repository layout; one sentence in Document chain, Renders,
that the engine's documentation is a set of renders of the forge
project in `docs/`; the script in the `scripts/` comment of the
layout. Nothing else: the rules live in the position, the genre and
the recipes.

## 10. What Claude assumed and chose

Assumed, to be confirmed or corrected:

1. The documentation documents the engine as it stands on disk at
   4.58, including what the intent still calls unjudged (the
   solution design is a proposal the principal has not read whole;
   the pages that cite it inherit that).
2. "Explain the template too" means the template is explained in
   the artefact's concept page, section by section, not a page of
   its own per template; the templates reference lists them.
3. The reference pages are for the human who opens the repository;
   the agent keeps `/man` and gets nothing new.
4. A project's own README and release notes are not documentation
   of the engine and stay as they are.
5. The docs recipes are the forge project's, since the engine's
   README and CONTRIBUTING already are; a library or a user project
   has no docs.

Chosen, each against what:

- `docs/` at the engine root, against `projects/forge/renders/docs/`
  (the layout's default for a render): a visitor looks for `docs/`
  at the root, and the root already holds the README and
  CONTRIBUTING on the same reasoning (SOL.0450).
- Five sections by the reader's journey, against the four kinds of
  Diátaxis as directories: the research's finding 2, the kinds sort
  pages and do not navigate.
- One page per artefact under `about/artefacts/`, against one page
  for all four: the principal's "explain every mechanism" and the
  size each definition has.
- `extend/` as a section of its own, against folding it into
  `about/`: the extender reads differently and the research names
  the contributor's path as one of the journeys.
- The glossary as a page, against glossing terms where they occur:
  both; the glossary is the one page a newcomer reads first.
- Prefix `docs-` on the recipes, against a subdirectory
  `recipes/docs/`: the layout prescribes a flat `recipes/`; a
  directory would be a convention to decide.
- The reference by a script (section 4b), the one real choice of
  the package; the alternative stands beside it as TBC.0040.
- Regeneration on the word (section 5), against regeneration by
  every release: cost and re-wording.
- Phase order (section 7), against the research's "cut the README
  first": the README is cut as pages land, so the order is free,
  and the principal asked for the depth.

## 11. What the reading found that the documentation would expose

Not findings to file here; material for the checks and the next
rounds, listed so that nothing of the reading is lost. Each is a
reader's observation, Claude's and not judged, with its place.

**Stale against the chain (known to THR.0520 or new):**
- POS.0600, POS.0620 still make the assignment the end of the chain;
  POS.0970 still says a library is to come; POS.1310 still says
  CLAUDE.md keeps a pointer per artefact (THR.0520 lists the first
  three).
- `templates/intent.md`: "IDs may be omitted while the intent is
  still fluid" against prime directive 7 and the history record's
  subject; "Candidate structure for assignment" presumes the chain
  continues to an assignment.
- `templates/ledger.md`: a finding's Resolution is "assignment
  version", a challenge's "intent version", while either may
  concern any artefact.
- `templates/brief.md` writes `last_change` by hand with a value,
  and carries `title` and `author` keys no other artefact has.
- CLAUDE.md, Ledger: "an unfinished conversation is saved into its
  thread of the intent" while threads live in `threads.md`.
- `templates/recipe-release-notes.md` cites "the Notes block, as
  before" that no current rule states; the record kind `approved`
  maps to no group.
- SOL.0410 names the README's inputs as the intent and CLAUDE.md
  (seven on disk); SOL.0620 calls the Python rewrite open while
  CLAUDE.md states it decided; SOL.0010 says CLAUDE.md carries the
  working methods "in short" while it carries them whole.
- POS.1090 says the reviewer commands "stay Claude's to start"
  while POS.0400 says no reviewer runs on his judgement; readable,
  but a page copying either would mislead.

**Unowned, so a page would have to invent it:**
- The checks' severity scale: the contract ranks by it and names
  none; the ledger's Severity column takes it.
- The syntax of a thread's origin mark: three origins named, said
  in words in the forge's own threads, no notation (keep it words).
- A challenge of the whole chain names the artefact it concerns,
  and the report shape and the ledger have no field for it.
- `obsolete` is a fifth verdict typed in full and absent from the
  verdict line and the hook.
- `forge` as a check's target means `projects/forge` for `light`,
  `project` and `history` and the engine root for `engine` and
  `single-source-of-truth`; said in each Lens, nowhere once.
- The reviewer skeletons' tool lists differ (the check writes
  nothing, the challenger searches the web) and no file says why.

**Scripts and skills, quirks a page would have to state or a fix
would remove:**
- `forge-pull` on a diverged clean tree sends the user to
  `forge-save`, which does nothing where nothing is staged.
- `md2pptx` defaults to the claude engine, `md2docx` to pandoc; both
  default `-Model` to `opus`, not the session model; the callers
  pass both explicitly, so only a hand run differs.
- `/render` looks for `## Format` only while `/publish`, the
  recipe template and `md2pptx` honour the older `## Build
  instructions`.
- `/recipe` registers a recipe in the Renders table at its first
  render; the ledger template wants one row per recipe.
- `sources/.gitignore` is created on demand by a sweep conversion,
  not by `/new-project`; the layout lists it as standing.
- The Briefs row is created by `/new-project` and again by `/forge
  brief`'s procedure; harmless, a restatement.
- `doc2md`'s synopsis names four formats and handles twelve.
- `/setup` says it runs no git operation and reads git's global
  configuration through `forge-status`.
- `critic-contract` carries calibration for particular artefacts
  (the solution design, the assignment) that their definitions own
  or should; `critic-clarity` restates the testability pointer.
- The critic's ledger step speaks of "verified" and "reopened"
  states the ledger template does not have.
- No `disable-model-invocation` on the reviewer commands: the rule
  that no reviewer runs on Claude's judgement is conduct and the
  hook, not the harness; a page must not claim a gate.

**One fact every reader met:** the CLAUDE.md a subagent receives is
the session's copy, not the disk's (THR.0580). The docs recipes will
say "read from disk" until the render skill says it once; the
reviewers' contracts have the same question open.

## 12. Questions for the principal, in the order of weight

1. The reference by a script from phase 1, or by recipes until
   THR.0530 (section 4b, TBC.0040)?
2. The phase order of section 7, or the jobs before the depth?
3. Thirty-seven pages: the map as it stands, or cut where two pages
   could be one (the four artefact pages into one; `use/projects`
   into `start/first-project`; `extend/new-genre-command-script`
   into `how-the-engine-grows`)?
4. Does the walkthrough run over this file section by section, or
   over the page map page by page?
