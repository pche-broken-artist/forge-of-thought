---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 1b92aab7f2a17286
inputs:
  - templates/CLAUDE.local.md
  - templates/project.md
  - templates/gitattributes
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
  - CLAUDE.md#Templates
---

# Templates

This page lists every skeleton in `templates/`, says what each is the skeleton of, which command or procedure creates a file from it, and what it holds, for the extender who adds or changes a kind of file. A template says what comes out; the definition of an artefact says how it is found. Where the templates sit in the whole is described in [What the forge is made of](../extend/what-it-is-made-of.md), and the terms used here are in the [Glossary](glossary.md). The principal is whoever's thinking is being forged. The ledger is the file that states the state of a project, made when it is read.

## Overview

| Template | Skeleton of | When it fits | Where the made file lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance file | first run on a new machine | `CLAUDE.local.md` at the engine root |
| `project.md` | the project file | creating or migrating a project | `project.md` of the project |
| `gitattributes` | the ways of merging by path | a project under git | `.gitattributes` of the project |
| `brief.md` | a brief | the principal's ask | `00-brief.md`, later `00-brief-<name>.md` |
| `intent.md` | the intent | the trunk of every project | `10-intent.md` |
| `thread.md` | a thread | an open matter of the intent | `threads/THR.NNNN.md` |
| `assignment.md` | the assignment | handing work to recipients | `20-assignment.md` |
| `brd.md` | the business requirements document | a BRD below an assignment or the intent | `30-brd.md` |
| `solution-design.md` | the solution design | how the things wanted are realised | the solution design file of the chain |
| `work.md` | a work specification | a work product | `work/<name>.spec.md` |
| `ledger.md` | the ledger | state of a project | `ledger.md`, not in git |
| `decisions.md` | the decision record | the principal's decisions | `decisions.md` |
| `history.md` | a history companion | any versioned document | `<file>.history.md` |
| `index.md` | a resource index | `sources/` and `research/` | `00-INDEX.md` of each |
| `index-bundle.md` | a bundle index | a set of files that is one source | `sources/<slug>/00-INDEX.md` |
| `research.md` | a research note | one card, one engine | `research/` |
| `research-plan.md` | the head of a research bundle | a research of several questions | `research/<date>-<topic>/00-plan.md` |
| `recipe.md` | a render recipe | any render | `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | the README of a project | `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | the release notes of a project | `recipes/release-notes.md` |
| `recipe-presentation.md` | the presentation recipe | slide-by-slide source material | `recipes/<name>.md` |
| `recipe-screenplay.md` | the screenplay recipe | a video or a player-page course | `recipes/<name>.md` |
| `html-player.html` | the player page | the served page of the videos | `docs/videos/index.html` |
| `docs-map.md` | the documentation map | the documentation of a target | `docs-map.md` beside the ledger |
| `artefact-definition.md` | the definition of an artefact | a new kind of artefact | a state file of the forge |
| `critic-definition.md` | a critic lens | a new lens | an agent file |
| `challenger-definition.md` | a challenger persona | a new persona | an agent file |
| `check-definition.md` | a check | a new check | an agent file |

## The naming rule

A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. The four types are an artefact, a critic lens, a challenger persona and a check. Every other template is the skeleton of a file a project holds.

## Entries

Each entry has the same three lines: what the template is the skeleton of, what creates a file from it, and what it holds.

### CLAUDE.local.md

- **Skeleton of:** the instance file, which carries facts of one installation and never a property of the forge.
- **Made by:** copied at the first run on a new machine and filled by `/setup`.
- **Holds:** three lines, the principal's role, the conversation language and the author handle with which every record he decides is signed.

### project.md

- **Skeleton of:** the project file.
- **Made by:** `/new-project` at the creation of a project, or the migration; never by a round of work.
- **Holds:** front-matter with `project` (the slug), `kind` (`thought` or `library`) and `language` (ISO 639-1, the language of the chain's artefacts). A fixture project also carries `fixture: true`.
- **A project without the file:** it has the shape from before the migration. The one remedy is `/migrate`. A command reports the shape as a fact, a check raises one finding with that fix, and nothing else of the new shape is raised against it.

### gitattributes

- **Skeleton of:** the ways of merging by path of a project.
- **Made by:** copied into a project as its `.gitattributes`.
- **Holds:** line-ending normalisation for every file; the derived paths (`renders/**`, the README, the release notes, `CONTRIBUTING.md`, `docs/**` and `published/*.md`) merged as `ours`, so that they are taken as they stand at a merge and made again; the published `.pptx` and `.docx` files marked binary.

### brief.md

- **Skeleton of:** a brief.
- **Made by:** `/forge brief`.
- **Holds:** a fixed header only (`project`, `title`, `author`, `version`, `status`); the text below it is free-form.

### intent.md

- **Skeleton of:** the intent, the trunk of every project.
- **Made by:** `/forge intent`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and the sections Essence, Positions, Facts, Rejected directions and, optionally, Candidate structure for the layer below.

### thread.md

- **Skeleton of:** a thread, one file per thread in `threads/`.
- **Made by:** `/forge intent`, which owns the rules of a thread, its life and its closing.
- **Holds:** a header that is the thread's state: `id`, `concerns` (the artefact, named as `/forge` names it; several comma-separated), `origin` (the principal by default, a document by path, or Claude's synthesis) and `status` (`open` or `closed`). The body is free text: its first sentence is its headline, its last dated paragraph its state.

### assignment.md

- **Skeleton of:** the assignment.
- **Made by:** `/forge assignment`.
- **Holds:** the header (`audience: recipients`) and the sections Purpose & Context, Objective, Scope, Requirements, Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms.

### brd.md

- **Skeleton of:** the business requirements document.
- **Made by:** `/forge brd`.
- **Holds:** the header with `parent:`, which names `20-assignment.md` or `10-intent.md`. A BRD made from a source is a work product instead. The sections are Purpose & Context, Objective, Stakeholders, Scope, Dependencies, Assumptions, Use cases, Business requirements, Touched areas of the enterprise, Qualities, Transition, Phasing, Success criteria, Open questions, Terms and an appendix of traceability. The Qualities categories follow the public standard ISO/IEC 25010 and the practice of a regulated business. No value in the skeleton stands as a requirement: a value comes from the stakeholders or is an open question with an owner.

### solution-design.md

- **Skeleton of:** the solution design.
- **Made by:** `/forge solution-design`.
- **Holds:** the header (`audience`: whoever realises the solution, a person or an agent) and the sections How the parts work together, Parts, Across the parts and Open. A part states what it is, what it realises, the choice made against what and at what cost, and where it lives.

### work.md

- **Skeleton of:** the specification of a work product. [The work product](../about/the-work-product.md) is the kind it serves.
- **Made by:** `/work`.
- **Holds:** the header with `file:` (the file the specification makes) and the sections Task, Inputs, Method, Assumptions, Open and Making. The specification holds the way and the reason; the file beside it holds the content.

### ledger.md

- **Skeleton of:** the ledger.
- **Made by:** `scripts/forge-ledger.py` at read time; the ledger is never in git.
- **Holds:** the header (`project`, `updated`) and one table per concern: Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings and Challenges, then the lists Waiting on principal and, only when there is something, Reports. Each table's comment says which record or field each column is read from. A project of kind `library` keeps only Renders, Sources, Dependencies, Research and Waiting on principal; the Findings table returns with a check's first finding.

### decisions.md

- **Skeleton of:** the decision record, append-only.
- **Made by:** the forge, when the principal decides.
- **Holds:** one record per decision with Decision, Reason, Verdict and Date.
- **The Verdict line:** it is present only where the decision rules on a finding or a challenge. It has one line per ID ruled on, and reads `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`.

### history.md

- **Skeleton of:** the history companion of a versioned document.
- **Made by:** written with the document at its birth, and appended at each change.
- **Holds:** the header (`project`, `document`) and one line per record: date, version, author, subject, kind, reason, Action and Was. The kinds are created, changed, closed, removed and approved. A record of state carries the current version and does not raise it.

### index.md

- **Skeleton of:** the resource index of a `sources/` or `research/` directory.
- **Made by:** `/ingest` writes the sources entries and `/research` the research entries.
- **Holds:** the header (`project`, `directory`) and one entry per resource.
- **A sources entry:** What, Origin, Date (best effort, from the content, the file or the ingest), Form (text, extract of an original, or binary), Role and Use for.
- **A research entry:** Question, Answer in short and Consult when.

### index-bundle.md

- **Skeleton of:** the index of a bundle, a set of related files that counts as one source.
- **Made by:** `/ingest`, at registration, if the index is missing.
- **Holds:** the header (`bundle`, `project`, `date`, `origin`), one short opening paragraph saying what the bundle is and whether it arrived whole or grows, and one entry per file with the fields of the sources entry of `index.md`.

### research.md

- **Skeleton of:** a research note, one card on one engine. The note and the bundle are described in full in [Research note and bundle](research-bundle.md).
- **Made by:** `/research`.
- **Holds:** the header (`date`, `project`, `topic`, `status`, `engine`, `model`, `usage`, `run`, `derived_from`) and the sections In short, Question, Key findings, Unexpected, Not found, Options, Relevance to this project, Sources, Opened and not used and Search record.

### research-plan.md

- **Skeleton of:** the head of a research bundle, `00-plan.md`.
- **Made by:** `/research`.
- **Holds:** the header (`date`, `project`, `topic`, `status`, `engines`, `derived_from`) and the sections Summary, Plan, Deviations from the plan, Synthesis and Notes. The plan holds Purpose, Perspectives, Assumptions, Left out, Cards, Agents and the second engine's review of the draft. A card has a question, why it matters, what would answer it, where to look, a disconfirming query and a stop rule. The synthesis holds completeness card by card, the answers side by side, the unexpected and the not found gathered, and Claude's view.

### recipe.md

- **Skeleton of:** a render recipe.
- **Made by:** `/recipe`.
- **Holds:** the header (`project`, `purpose`, `audience`, `version`, optionally `output` and `languages`) and the sections Inputs, Instructions, an optional Format and Template. The Format section names the format (`pptx`, `docx`, `video` or `html-player`) and what the plain and the published file need.

### recipe-readme.md

- **Skeleton of:** the readme recipe.
- **Made by:** `/new-project` scaffolds it; `/recipe readme` iterates it.
- **Holds:** the sections Inputs, Instructions, Pinned facts (not rendered) and Template. The Template is a README with What this project is, What you get, How to start, Where it stands, Documentation, About this README and a dated footer. The Instructions fix a closing sentence, which this page does not repeat.
- **Pinned facts (not rendered):** an optional section for facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them. The planner of the documentation reads them as an owner. One bullet each; the section is dropped the day a file owns the fact, and omitted when the project has none.

### recipe-release-notes.md

- **Skeleton of:** the release-notes recipe.
- **Made by:** `/new-project` scaffolds it; `/recipe release-notes` iterates it; every `/release` of the project renders it.
- **Holds:** Inputs (the histories of the chain, the decisions and the previous edition), Instructions and a Template. The Template has one section per release, newest first, with the groups Action required, Added, Changed, Removed, Fixed and Rejected. An approved major opens with a few sentences of highlights and folds the minors since the previous major into it.

### recipe-presentation.md

- **Skeleton of:** the presentation recipe, whose render is source material for a deck.
- **Made by:** `/recipe presentation`.
- **Holds:** Inputs, Instructions (one section per slide with On slide, Diagram and Speaker notes), Format (`pptx`) and a Template that is a table of slides: number, slide, content and diagram.

### recipe-screenplay.md

- **Skeleton of:** the screenplay recipe, whose render is the source of a video or of the events of the player page.
- **Made by:** `/recipe screenplay`.
- **Holds:** the header with `languages` (the first primary, the rest translations) and, for a player-page file, `output` into the engine's `docs/videos/`. The sections are Inputs (session records, the brief of the videos, a document the video shows), Instructions (the pinned beats, the quotes, the length, the translation), Format (`video` or `html-player`, never both) and a Template.
- **The Format of a player-page file:** it also names the section of the course on the player page and the name the page lists per language. The number in `output` is the place in the course.
- **The Template:** a title card, a card of what the viewer will see, scenes and an end card. A scene has a real time of day, a caption of two parts (Now and Why) and a fenced block of what the terminal shows.

### html-player.html

- **Skeleton of:** the player page of the engine.
- **Made by:** `scripts/md2video.py`, which writes the served page `docs/videos/index.html` from it. It replaces one placeholder with the list of the folder's player files and another with a script tag per file.
- **Holds:** the page's head comment says that the served page is never edited: the skeleton is edited and the script writes the page anew.

### docs-map.md

- **Skeleton of:** the documentation map, kind `map`. The map's fields are given in full in [Documentation map](documentation-map.md).
- **Made by:** the planner of `/document`, to `docs-map.md` beside the ledger of the owning project.
- **Holds:** the header (`target`, `owner`), a Paths section with one line per reader, one section per section of the outline with one entry per page, and the sections Unowned and Did not fit. An entry has title, line, kind, reader, says, inputs, links, must-not, made, evidence for derived pages, and state.

### artefact-definition.md

- **Skeleton of:** the definition of a kind of artefact.
- **Made by:** `/new-artefact`.
- **Holds:** the front-matter `description` and seven blocks: Target, Inputs, Aim, Partner, Map, Instruments and Course, then a closing paragraph on how the files are made. Every block is present; a block empty on purpose says so with the reason.

### critic-definition.md

- **Skeleton of:** a critic lens file.
- **Made by:** the extender, on the principal's decision.
- **Holds:** front-matter (`name`, `description`, `tools`, `model`, `skills`) and a Lens section of four parts: what the lens reads, what to go after, the categories of a finding and any own report sections. The shared behaviour comes from the contract skill the front-matter names.

### challenger-definition.md

- **Skeleton of:** a challenger persona file.
- **Made by:** the extender, on the principal's decision.
- **Holds:** front-matter as above, with web search among the tools, and a Lens section of two parts: who the persona is, a role of its own and never a mirror of the principal, and what to go after.

### check-definition.md

- **Skeleton of:** a check file.
- **Made by:** the extender, on the principal's decision.
- **Holds:** front-matter as above and a Lens section of three parts: what the check reads, what it verifies with the owner of each rule cited and never restated, and its cost.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
