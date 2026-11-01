---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: debf3584b23d7c42
inputs:
  - templates/CLAUDE.local.md
  - templates/project.md
  - templates/gitattributes
  - templates/gitignore
  - templates/brief.md
  - templates/intent.md
  - templates/thread.md
  - templates/assignment.md
  - templates/brd.md
  - templates/solution-design.md
  - templates/work.md
  - templates/ledger.md
  - templates/decisions.md
  - templates/history.md
  - templates/index.md
  - templates/index-bundle.md
  - templates/research.md
  - templates/research-plan.md
  - templates/recipe.md
  - templates/recipe-readme.md
  - templates/recipe-release-notes.md
  - templates/recipe-presentation.md
  - templates/recipe-screenplay.md
  - templates/html-player.html
  - templates/docs-map.md
  - templates/artefact-definition.md
  - templates/critic-definition.md
  - templates/challenger-definition.md
  - templates/check-definition.md
  - .claude/skills/new-project/SKILL.md
  - CLAUDE.md#Templates
---

# Templates

The templates are the skeletons in `templates/` that every new file of a project, and every new kind of member of the forge, is made from. This page is for the extender: it lists each skeleton, what it is the skeleton of, which command or procedure creates from it, and what it holds. The principal is whoever's thinking is being forged. The ledger is the state of a project, made at read time by a script.

Every template is canonical: a new project takes its files from these skeletons and never from a copy elsewhere. A skeleton carries its own comments, which say who owns its rules; they are deleted from the file made from it, except where noted below.

## Naming rules

- A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. The types are an artefact, a critic lens, a challenger persona and a check.
- A skeleton named `recipe-<genre>.md` is the skeleton of a render recipe of one genre. The skeleton named `recipe.md` is the shape every recipe has.
- A skeleton without a type or genre in its name is the skeleton of one document of a project, or of a file beside it.

## Overview

| Template | What it is the skeleton of | When it fits | Where it lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance file | first run on a new machine | `templates/`; copy at the engine root |
| `project.md` | the project file | creation of a project | `templates/`; copy at the project root |
| `gitattributes` | the ways of merging by path | creation of a project | `templates/`; copy as `.gitattributes` |
| `gitignore` | what never enters git | creation of a project | `templates/`; copy as `.gitignore` |
| `brief.md` | a brief | the ask arrives | `templates/`; copy `00-brief.md` |
| `intent.md` | the intent | first `/forge intent` | `templates/`; copy `10-intent.md` |
| `thread.md` | one thread of the intent | a matter of the intent stays open | `templates/`; copy `threads/THR.NNNN.md` |
| `assignment.md` | the assignment | the intent is handed to recipients | `templates/`; copy `20-assignment.md` |
| `brd.md` | the BRD | requirements are written for review and estimate | `templates/`; copy `30-brd.md` |
| `solution-design.md` | the solution design | how the things wanted are realised | `templates/`; copy of the layer |
| `work.md` | a work specification | a work product is made | `templates/`; copy `work/<name>.spec.md` |
| `ledger.md` | the ledger | made at read time | `templates/`; copy `ledger.md` |
| `decisions.md` | the decisions record | creation of a project | `templates/`; copy `decisions.md` |
| `history.md` | the history companion | any versioned document | `templates/`; copy `<file>.history.md` |
| `index.md` | the resource index of `sources/` or `research/` | creation of a project; each new resource | `templates/`; copy `00-INDEX.md` |
| `index-bundle.md` | the index of one bundle of sources | a bundle is registered | `templates/`; copy `sources/<slug>/00-INDEX.md` |
| `research.md` | one research note | a research card is answered | `templates/`; copy in `research/` |
| `research-plan.md` | the head of a research bundle | a research of several questions | `templates/`; copy `00-plan.md` |
| `recipe.md` | the shape of every render recipe | a recipe is composed | `templates/`; copy `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | creation of a project | `templates/`; copy `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | creation of a thought project | `templates/`; copy `recipes/release-notes.md` |
| `recipe-presentation.md` | the presentation recipe | a deck is wanted | `templates/`; copy in `recipes/` |
| `recipe-screenplay.md` | the screenplay recipe | a video or a player is wanted | `templates/`; copy in `recipes/` |
| `html-player.html` | the player page | a public player is served | `templates/`; written to `docs/videos/index.html` |
| `docs-map.md` | the documentation map | a documentation run | `templates/`; copy `docs-map.md` |
| `artefact-definition.md` | the definition of a kind of artefact | a new artefact is added | `templates/`; copy under `.claude/skills/forge/states/` |
| `critic-definition.md` | a critic lens file | a new lens is added | `templates/`; copy under `.claude/agents/` |
| `challenger-definition.md` | a challenger persona file | a new persona is added | `templates/`; copy under `.claude/agents/` |
| `check-definition.md` | a check file | a new check is added | `templates/`; copy under `.claude/agents/` |

## The entries

Each entry has three lines: what the template is the skeleton of, what creates from it, and what it holds.

### `CLAUDE.local.md`
- **Skeleton of:** the instance file, which holds the facts of one installation.
- **Created by:** `/setup`, on a new machine. The copy is gitignored and stays at the engine root.
- **Holds:** the principal's role, the conversation language and the principal's handle, which signs every record he decides.

### `project.md`
- **Skeleton of:** the project file.
- **Created by:** `/new-project`, or the migration. It is written once and never by a working round.
- **Holds:** front-matter with `project` (the slug), `kind` (`thought` or `library`) and `language` (two-letter code of the chain's artefacts). A fixture project carries `fixture: true`. There is no body.
- **A project without the file** is of the shape before the migration. The one remedy is `/migrate`. A command reports the shape as a fact, a check reports it as one finding with that fix, and nothing else of the new shape is raised against the project.

### `gitattributes`
- **Skeleton of:** the `.gitattributes` of a project, which sets the ways of merging by path.
- **Created by:** `/new-project`, copied as `.gitattributes`.
- **Holds:** line-ending normalisation for every file. Derived files are taken as ours at a merge and made again: `renders/**`, `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**` and `published/*.md`. The published `.pptx` and `.docx` files are binary and never merged.

### `gitignore`
- **Skeleton of:** the `.gitignore` of a project.
- **Created by:** `/new-project`, copied as it stands.
- **Holds:** two entries. `ledger.md` stays out of git because the ledger is made at read time. `~$*` keeps out the lock files of an open Office document (Word, PowerPoint, Excel).

### `brief.md`
- **Skeleton of:** a brief, `00-brief.md` or a later `00-brief-<name>.md`.
- **Created by:** the `/forge brief` procedure, which `/new-project` hands the pasted brief to.
- **Holds:** a fixed header (`project`, `title`, `author`, `version`, `status`) and a free-form text below it.

### `intent.md`
- **Skeleton of:** the intent, `10-intent.md`.
- **Created by:** the first `/forge intent`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and the sections Essence, Positions, Facts, Rejected directions and, optionally, Candidate structure for the layer below. Items carry IDs from birth.

### `thread.md`
- **Skeleton of:** one thread of the intent, one file per thread in `threads/`.
- **Created by:** the intent's procedure, when a matter stays open.
- **Holds:** a header with `id`, `concerns` (the artefact it concerns, as `/forge` names it, several comma-separated), `origin` (the principal by default, a document by path, or Claude's synthesis) and `status` (`open` or `closed`). The body is free: its first sentence is its headline, its last dated paragraph its state, and it names the day it was opened.

### `assignment.md`
- **Skeleton of:** the assignment, `20-assignment.md`.
- **Created by:** the first `/forge assignment`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and the sections Purpose & Context, Objective, Scope, Requirements (grouped), Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms.

### `brd.md`
- **Skeleton of:** the BRD, `30-brd.md`.
- **Created by:** the first `/forge brd`.
- **Holds:** the header (`version`, `status`, `project`) and `parent:`, which names the document the BRD is made from: `20-assignment.md` or `10-intent.md`. A BRD made from a source is a work product instead. The sections are Purpose & Context, Objective, Stakeholders, Scope, Dependencies, Assumptions, Use cases, Business requirements, Touched areas of the enterprise, Qualities (one item per category), Transition, Phasing, Success criteria, Open questions, Terms and Appendix: traceability. No value in the skeleton stands as a requirement.

### `solution-design.md`
- **Skeleton of:** the solution design.
- **Created by:** the first `/forge solution-design`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and the sections How the parts work together, Parts, Across the parts and Open. A part states what it realises, the choice it rests on and where it is.

### `work.md`
- **Skeleton of:** the specification of a work product (see [The work product](../about/the-work-product.md)).
- **Created by:** `/work`.
- **Holds:** the header (`version`, `status`, `project`, `file`, the file the specification makes) and the sections Task, Inputs, Method, Assumptions, Open and Making. Inputs are cited by ID and by path, never copied.

### `ledger.md`
- **Skeleton of:** the ledger.
- **Created by:** `python scripts/forge-ledger.py <slug>`, at read time. It is never written by hand and never in git.
- **Holds:** a header with `project` and `updated`, then one table per concern: Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings and Challenges, then the list Waiting on principal and, only when there is something, Reports. A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal. The skeleton's comments say which record or field each column is read from.

### `decisions.md`
- **Skeleton of:** the decisions record of a project.
- **Created by:** `/new-project`, with the slug filled and the sample record removed.
- **Holds:** one record per decision, numbered in the global sequence, newest last, append-only. A record has `Decision`, `Reason`, `Verdict` and `Date`.
- **The Verdict line** is present only where the decision rules on a finding or a challenge. It has one line per ID ruled on, in the form `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`.

### `history.md`
- **Skeleton of:** the history companion of a versioned document.
- **Created by:** the command that creates the document, beside it. `/new-project` makes the companions of the two recipes it scaffolds.
- **Holds:** a header with `project` and `document`, then one line per change, appended at the end: date, version, author, subject, kind, reason, `Action` and `Was`. The kinds are `created`, `changed`, `closed`, `removed` and `approved`. A birth is two records: one of the file and one naming every item born with it.

### `index.md`
- **Skeleton of:** the resource index, `00-INDEX.md`, of `sources/` or of `research/`.
- **Created by:** `/new-project`, with the header filled and no entries. `/ingest` writes the sources entries and `/research` writes the research entries.
- **Holds:** a header with `project` and `directory`. A sources entry has the fields What, Origin, Date, Form, Role and Use for. A research entry has the fields Question, Answer in short and Consult when. A bundle appears as one entry that points to its own index.

### `index-bundle.md`
- **Skeleton of:** the index of one bundle of sources, `sources/<slug>/00-INDEX.md`.
- **Created by:** `/ingest`, at registration of the bundle, if the index is missing.
- **Holds:** a header with `bundle`, `project`, `date` and `origin`, one short paragraph (whether the bundle arrived whole or grows), then one entry per file with the fields of a sources entry in `index.md`, in the same order.

### `research.md`
- **Skeleton of:** one research note: one card, one engine, one note. The note in full is described in [Research note and bundle](research-bundle.md).
- **Created by:** `/research`.
- **Holds:** a header with `date`, `project`, `topic`, `status`, `engine`, `model`, `usage`, `run` and `derived_from`, and the sections In short, Question, Key findings, Unexpected, Not found, Options, Relevance to this project, Sources, Opened and not used and Search record.

### `research-plan.md`
- **Skeleton of:** the head of a research bundle, `00-plan.md`: the confirmed plan and, under it, the synthesis.
- **Created by:** `/research`, for a research of several questions.
- **Holds:** a header with `date`, `project`, `topic`, `status`, `engines` and `derived_from`, and the sections Summary, Plan (Purpose, Perspectives, Assumptions, Left out, Cards, Agents, The second engine's review of the draft), Deviations from the plan, Synthesis and Notes. A card has Question, Why it matters, What would answer it, Where to look, Disconfirming query and Stop rule.

### `recipe.md`
- **Skeleton of:** the shape every render recipe has.
- **Created by:** `/recipe`.
- **Holds:** a header with `project`, `purpose`, `audience` and `version`, and the optional keys `output` (a path that replaces the default render path) and `languages` (the first primary, the rest its translations). The sections are Inputs, Instructions, an optional Format and Template. The Format section names the format (`pptx`, `docx`, `video` or `html-player`), how the plain file is made by `/render` and how the published file is made by `/publish`.

### `recipe-readme.md`
- **Skeleton of:** the readme recipe, `recipes/readme.md`.
- **Created by:** `/new-project`, with the slug and date filled and the comments kept for the first `/recipe` iteration. The recipe is iterated with `/recipe readme`.
- **Holds:** the header (output `README.md`), the sections Inputs, Instructions, an optional Pinned facts (not rendered) and Template. The template's sections are What this project is, What you get, How to start, Where it stands, Documentation and About this README, followed by a dated footer.
- **Pinned facts (not rendered)** lists facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them. The documentation's planner reads them there as an owner. Each fact is one bullet, dropped the day a file owns the fact, and the section is left out when the project has none.

### `recipe-release-notes.md`
- **Skeleton of:** the release-notes recipe, `recipes/release-notes.md`.
- **Created by:** `/new-project` for a thought project, iterated with `/recipe release-notes`.
- **Holds:** the header (output `RELEASE-NOTES.md`), Inputs (the histories of the intent and of the layers below it, the current intent, the decisions and the previous edition), Instructions and a Template with one section per release. A section has the groups Action required, Added, Changed, Removed, Fixed and Rejected. An approved major opens with a few sentences of highlights.

### `recipe-presentation.md`
- **Skeleton of:** a presentation recipe: the render is slide-by-slide source material for a deck.
- **Created by:** `/recipe presentation`.
- **Holds:** the header, Inputs, Instructions (audience, the one message, density, per-slide format), Format (`pptx`) and a Template that is a table of slides with their content and diagram.

### `recipe-screenplay.md`
- **Skeleton of:** a screenplay recipe: the render is the screenplay of a video or of the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Holds:** the header with `languages` and an optional `output` (only for `html-player`, a path in the engine's public `docs/videos/` folder). The sections are Inputs (session records registered as sources, the brief of the videos, a document the video shows), Instructions (the beats pinned so that every render is the same cut, the quotes, the length, the title card, what must not appear, the translation), Format (`video` or `html-player`, never both) and a Template of a title card, a card of what the viewer will see, scenes and an end card. A scene has a time, a caption of two parts (Now and Why) and a fenced block with what the terminal shows.

### `html-player.html`
- **Skeleton of:** the player page of the engine.
- **Created by:** `scripts/md2video.py`, which writes the served page `docs/videos/index.html` from this skeleton. The script replaces one placeholder with the list of the folder's player files and another with one script tag per file.
- **Holds:** a page that plays the videos from their player files. The served page is never edited: the skeleton is edited and the script writes the page again.

### `docs-map.md`
- **Skeleton of:** the documentation map, `docs-map.md`, which lies beside the owning project's ledger and is never shown to the reader of the documentation.
- **Created by:** the planner of `/document`.
- **Holds:** a header with `target` (`engine` or a slug) and `owner`, a Paths section (one line per reader), one section per section of the documentation outline, with one entry per page, then Unowned and Did not fit. An entry has title, line, kind, reader, says, inputs, links, must-not, made, evidence (derived pages only) and state. The fields in full are in [Documentation map](documentation-map.md).

### `artefact-definition.md`
- **Skeleton of:** the definition of a kind of artefact, a state file under `.claude/skills/forge/states/`.
- **Created by:** `/new-artefact`.
- **Holds:** a description in the front-matter and seven blocks: Target, Inputs, Aim, Partner, Map, Instruments and Course. Every block is present. A block that is empty on purpose says so with the reason.

### `critic-definition.md`
- **Skeleton of:** a critic lens file, `.claude/agents/critic-<lens>.md`.
- **Created by:** no command is named for it. A lens is added only on the principal's decision.
- **Holds:** front-matter (`name`, `description`, `tools`, `model`, `skills`) and one Lens section. The Lens section has four parts: what the lens reads, what to go after, the categories of a finding and the report sections of its own.

### `challenger-definition.md`
- **Skeleton of:** a challenger persona file, `.claude/agents/challenger-<persona>.md`.
- **Created by:** no command is named for it. A persona is added only on the principal's decision.
- **Holds:** the same front-matter as a critic lens, with web search and fetch among the tools, and one Lens section of two parts: who the persona is, and what blind spots it goes after.

### `check-definition.md`
- **Skeleton of:** a check file, `.claude/agents/check-<name>.md`.
- **Created by:** no command is named for it. A check is added only on the principal's decision.
- **Holds:** the same front-matter as a critic lens and one Lens section of three parts: what the check reads, what it verifies (each rule with its owner cited) and its cost.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
