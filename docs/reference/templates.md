---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: c765c97ac2bd0832
inputs:
  - templates/CLAUDE.local.md
  - templates/project.md
  - templates/gitattributes
  - templates/brief.md
  - templates/intent.md
  - templates/thread.md
  - templates/assignment.md
  - templates/solution-design.md
  - templates/work.md
  - templates/ledger.md
  - templates/decisions.md
  - templates/history.md
  - templates/index.md
  - templates/index-bundle.md
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

This page lists every skeleton in `templates/`: what each is the skeleton of, which command or procedure creates a file from it, and what it holds. It is for the extender who adds or changes a kind of document and needs to know which skeleton owns its shape. The principal (the person whose thinking is being forged) is named in some entries below.

The templates are the canonical skeletons for every new project. A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by: an artefact, a critic lens, a challenger persona or a check. Where a template does not name the command that creates from it, the entry says so. Terms of the forge are explained in the [Glossary](glossary.md); where the templates sit in the whole is described in [What the forge is made of](../extend/what-it-is-made-of.md).

## Overview

| Template | What it is for | When it fits | Where the result lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts of one installation | on a new machine | `CLAUDE.local.md` at the engine root |
| `project.md` | the project file: kind and language | at the creation of a project | `project.md` in the project |
| `gitattributes` | the ways of merging by path | at the creation of a project | `.gitattributes` in the project |
| `brief.md` | the header of a brief | a brief is born | `00-brief.md`, `00-brief-<name>.md` |
| `intent.md` | the intent | the intent is born | `10-intent.md` |
| `thread.md` | one open thread | a thread is opened | one file in `threads/` |
| `assignment.md` | the assignment | the assignment is born | `20-assignment.md` |
| `solution-design.md` | the solution design | the solution design is born | the project's solution design |
| `work.md` | a work specification | a work product is made | the specification beside the work file in `work/` |
| `ledger.md` | the shape of the ledger | the ledger is made | `ledger.md` |
| `decisions.md` | the record of decisions | the principal decides | `decisions.md` |
| `history.md` | the history companion | a versioned document is born | `<file>.history.md` |
| `index.md` | a resource index | a source or a research note is registered | `00-INDEX.md` of `sources/` and `research/` |
| `index-bundle.md` | the index of a bundle | related files are one source | `00-INDEX.md` inside `sources/<slug>/` |
| `recipe.md` | the shape of every recipe | a recipe is composed | `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | a project needs its README | `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | a project needs release notes | `recipes/release-notes.md` |
| `recipe-presentation.md` | the presentation recipe | a deck is wanted | a recipe in `recipes/` |
| `recipe-screenplay.md` | the screenplay recipe | a video or player is wanted | a recipe in `recipes/` |
| `html-player.html` | the player page | the player events are made | `docs/videos/index.html` |
| `docs-map.md` | the documentation map | the documentation is planned | the map beside the owning project |
| `artefact-definition.md` | the definition of a kind of artefact | a new kind of artefact is added | the new definition file |
| `critic-definition.md` | a critic lens file | a lens is added | `.claude/agents/critic-<lens>.md` |
| `challenger-definition.md` | a challenger persona file | a persona is added | `.claude/agents/challenger-<persona>.md` |
| `check-definition.md` | a check file | a check is added | `.claude/agents/check-<name>.md` |

## The entries

Every entry has the same three lines: what the template is the skeleton of, which command or procedure creates from it, and what it holds.

### `CLAUDE.local.md`

- **Skeleton of:** the file of instance facts, kept at the engine root and not checked in.
- **Created by:** not named in the template.
- **Holds:** three bullets: Principal (the role whose thinking is being forged), Conversation language, Author (the principal's handle, the author of every record he decides). The git identity is not here; it is git's, per host.

### `project.md`

- **Skeleton of:** the project file, written once at the creation of a project and never by a round of work.
- **Created by:** `/new-project`, or the migration.
- **Holds:** a front-matter of three fields: `project` (the slug), `kind` (`thought` or `library`) and `language` (the language of the chain's artefacts, ISO 639-1). A fixture project carries `fixture: true`. The file is merged as text and read wherever the kind and the language of a project are needed.
- **A project without the file:** it is of the shape before the migration. The one remedy is `/migrate` (the script `scripts/forge-migrate.py`). A command reports that shape as a fact; a check reports it as one finding with that fix. Nothing else of the new shape is raised against such a project.

### `gitattributes`

- **Skeleton of:** the `.gitattributes` of a project. The project's file is copied from this template.
- **Created by:** not named in the template.
- **Holds:** the ways of merging by path.
  - All files: line endings normalised (`* text=auto`), so that files do not fight between machines.
  - Derived files, made only on `main`, taken as ours at a merge and made again: `renders/**`, `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**`, `published/*.md`.
  - The published files: `published/*.pptx` and `published/*.docx`, binary and never merged.

### `brief.md`

- **Skeleton of:** a brief.
- **Created by:** the brief's definition, `.claude/skills/forge/states/brief.md`.
- **Holds:** only a header: `project`, `title`, `author`, `version` and `status`. The text below the header is free-form.

### `intent.md`

- **Skeleton of:** the intent.
- **Created by:** the intent's definition, `.claude/skills/forge/states/intent.md`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and these sections:
  - Essence
  - Positions
  - Facts
  - Rejected directions
  - Candidate structure for the layer below (optional, deleted once the layer exists)

### `thread.md`

- **Skeleton of:** one open thread, one file per thread in `threads/`.
- **Created by:** not named in the template. The rules of a thread, its life and its closing are in the intent's definition, `.claude/skills/forge/states/intent.md`.
- **Holds:** a header that is the thread's state, then the thread's text. The first sentence of the text is its headline, and its last dated paragraph is its state.
  - `id`: `THR.NNNN`
  - `concerns`: the artefact it concerns, as `/forge` names it; several, comma-separated
  - `origin`: the principal (the default), a document by path, or Claude's synthesis
  - `status`: `open` or `closed`

### `assignment.md`

- **Skeleton of:** the assignment.
- **Created by:** the assignment's definition, `.claude/skills/forge/states/assignment.md`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and these sections, the last six deleted when empty:
  - Purpose & Context
  - Objective
  - Scope (in scope, out of scope)
  - Requirements (grouped)
  - Constraints
  - Assumptions
  - Deliverables
  - Open Questions
  - Success Criteria
  - Terms
- The history lives in the companion, never in the file.

### `solution-design.md`

- **Skeleton of:** the solution design, how the things wanted are realised.
- **Created by:** the solution design's definition, `.claude/skills/forge/states/solution-design.md`.
- **Holds:** the header (`version`, `status`, `project`, `audience`) and these sections:
  - How the parts work together
  - Parts (grouped; each item names what it realises, the choice it rests on and where it lives)
  - Across the parts
  - Open

### `work.md`

- **Skeleton of:** a work specification. It holds the way and the why of a work product; the file beside it holds the content. The kind is described in [The work product](../about/the-work-product.md).
- **Created by:** the command `/work` (`.claude/skills/work/SKILL.md`).
- **Holds:** the header (`version`, `status`, `project`, and `file`, the file the specification makes, named by the work alone) and these sections:
  - Task
  - Inputs (items by ID and files by path, never copied)
  - Method
  - Assumptions
  - Open
  - Making (how the file is made from the specification; never copied into the file)

### `ledger.md`

- **Skeleton of:** the ledger. The ledger is the single source of truth for state. It is made at read time by `scripts/forge-ledger.py` from the records, and is never kept in git.
- **Created by:** `scripts/forge-ledger.py`.
- **Holds:** the header (`project`, `updated`) and one table per section. The template's comments state which record or field each column is read from; the script keeps them.
  - Briefs: File, Version, Status, Mined, Note
  - Documents: File, Version, Status, Date
  - Renders: Render, Audience, Recipe, Inputs, Generated
  - Published: File, Recipe, From render, Model, Published, State
  - Work: File, Specification, Inputs, Made, State
  - Sources: File, Date, Date origin, Form
  - Dependencies: Path, Library, Used by, Note
  - Research: File, Date, Derived from
  - Findings: ID, Severity, Category, State, Source review, Resolution
  - Challenges: ID, State, Headline, Source review, Resolution
  - Waiting on principal: one line per matter
  - Reports: what the merged files cannot say; the section stands only when there is something
- A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal. The Findings table returns with a check's first finding.
- `ledger.archive.md` is the hand-kept ledger as it stood at the migration, immutable. Its Briefs, Work, Findings and Challenges rows are read for every item without a record of the new shape, and a newer record overrides.

### `decisions.md`

- **Skeleton of:** the decisions file, append-only.
- **Created by:** not named in the template.
- **Holds:** a header (`project`) and one record per decision of the principal, newest last. A record is never edited; a later decision supersedes it by a new record that names it. A record has the heading `DEC.NNNN` and the decision in one line, then four fields:
  - `Decision`: what was decided
  - `Reason`: why, including what was weighed against it
  - `Verdict`: see below
  - `Date`
- **The Verdict line:** it stands only where the decision rules on a finding or a challenge, one line per ID, in the form `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`. A partial verdict is read as the verdict on the whole ID; the rest is a `changed` record of the history.

### `history.md`

- **Skeleton of:** the history companion of a versioned document.
- **Created by:** not named in the template.
- **Holds:** a header (`project`, `document`) and a log of records, one line each, appended at the end and never rewritten. The record has the fields date, version, author, subject, kind, reason, `Action` and `Was`, separated by a vertical bar.
  - Kinds: `created`, `changed`, `closed`, `removed`, `approved`.
  - The subject is an ID, several IDs, or a place without an ID.
  - Reason is left out on `created`; `Action` and `Was` only where the record has them; `Was` is always last.
  - Records of state carry the current version and do not raise it. The template gives the shapes of three: the mining of a brief, a finding or a challenge settled, and a work product's state (`current`, `stale`, `by hand`).
  - `rejected`, `parked` and `obsolete` are a decision's Verdict, never a record here.

### `index.md`

- **Skeleton of:** a resource index, the catalogue of `sources/` or of `research/`.
- **Created by:** `/ingest` writes the entries of the sources index; `/research` writes those of the research index.
- **Holds:** a header (`project`, `directory`: `sources` or `research`) and one entry per resource. A bundle is one entry pointing to its own index.
  - A sources entry, headed by the file or bundle:
    - `What`: what the resource is
    - `Origin`: where it came from
    - `Date`: `YYYY-MM-DD`, from the content, the file or the ingest; best effort, never asked
    - `Form`: text, extract of an original, or binary; one form per source
    - `Role`: free text, such as a standard to verify against or a meeting record
    - `Use for`: the questions it answers best
  - A research entry, headed by `YYYY-MM-DD-<topic>.md`:
    - `Question`: what the note set out to answer
    - `Answer in short`: two or three lines of the conclusion
    - `Consult when`: the situations in which the note is worth opening

### `index-bundle.md`

- **Skeleton of:** the index of one bundle, `sources/<slug>/`. This skeleton is the one owner of the bundle index.
- **Created by:** not named in the template.
- **Holds:** a header (`bundle`, `project`, `date`, `origin`, where the whole came from), one short paragraph on what the bundle is and why it entered sources, then one entry per file. Each entry has the fields of the sources entry in `index.md`, in its order.

### `recipe.md`

- **Skeleton of:** every recipe. It owns the shape only.
- **Created by:** not named in the template. The genre skeletons below are composed through `/recipe`.
- **Holds:** a header (`project`, `purpose`, `audience`, `version`, and optionally `output` and `languages`) and these sections:
  - Inputs: artefacts the render is generated from, by path
  - Instructions: audience, tone, what to emphasise and omit
  - Format (optional): the plain file made by `/render` and the published file made by `/publish`
  - Template: the literal skeleton of the render, always Markdown
- `output` overrides the default `renders/<recipe>.md`. `languages` makes the first language primary and the rest its translations, one render per language.

### `recipe-readme.md`

- **Skeleton of:** the readme recipe, whose render is the project's README.
- **Created by:** `/recipe readme`.
- **Holds:** a header with `output: README.md` and these sections:
  - Inputs: the ledger, the brief, the intent and the layers below it
  - Instructions: the audience, the rule that every claim is derivable from the inputs, the title, the closing section and the dated footer
  - Pinned facts (not rendered)
  - Template: the sections of the README
- **Pinned facts (not rendered):** an optional section. It lists facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them; the documentation's planner reads them as an owner. Each is one bullet, dropped the day a file owns the fact. The section is omitted when the project has none.

### `recipe-release-notes.md`

- **Skeleton of:** the release-notes recipe, whose render is `RELEASE-NOTES.md`.
- **Created by:** `/recipe release-notes`.
- **Holds:** a header with `output: RELEASE-NOTES.md` and these sections:
  - Inputs: the histories of the intent and of the layers below it, their archives, the intent, the decisions and the previous edition
  - Instructions: one section per release, newest first; each record becomes a bullet under the group its kind gives; sections of earlier releases are carried over verbatim; at an approved major the minors fold into it
  - Template: the groups of a release section, in order: Action required, Added, Changed, Removed, Fixed, Rejected

### `recipe-presentation.md`

- **Skeleton of:** the presentation recipe. The render is slide-by-slide source material for a deck, from which `/render` makes a plain PowerPoint file and `/publish` the designed one.
- **Created by:** `/recipe presentation`.
- **Holds:** the header of `recipe.md` and these sections:
  - Inputs, which may include another render of the project
  - Instructions: one section per slide, the message, density limits, vocabulary, what must not appear, diagrams as inline Mermaid or as a reference to a render
  - Format: `pptx`
  - Template: a table of slides (number, title, content, diagram)
- The per-slide format has the fields On slide, Diagram and Speaker notes.

### `recipe-screenplay.md`

- **Skeleton of:** the screenplay recipe. The render is a screenplay from which `scripts/md2video.py` makes a video or the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Holds:** a header with `languages` and, for an html-player, an `output` into the engine's `docs/videos/`, and these sections:
  - Inputs: session records registered as sources, the brief of the videos, a document the video shows being born
  - Instructions: the shape of the screenplay (title card, a card of what the viewer will see, scenes, end card), the pinned beats, the rules for quotes, length, the disclosure on the title card, what must not appear, and translation
  - Format: `video` or `html-player`, never both; the pace, the date in the tab bar and the labels of the captions
  - Template: the title card, the card, the scenes and the end card
- A scene has a real time of day, a caption of two parts (Now and Why) and a fenced block of what the terminal shows.

### `html-player.html`

- **Skeleton of:** the player page of the engine.
- **Created by:** `scripts/md2video.py` writes the served page, `docs/videos/index.html`, from this skeleton. It replaces a FILES placeholder with the list of the folder's html-player files and a SCRIPTS placeholder with one script tag per file. The data arrive through calls of `forgeVideo()`, so the page works from a file on disk as well as from GitHub Pages.
- **Holds:** the page's markup, styles and code. The served page is never edited; the skeleton is edited and the script writes the page anew.

### `docs-map.md`

- **Skeleton of:** the documentation map. Its fields in full are on the page [Documentation map](documentation-map.md).
- **Created by:** the planner agent of `/document`. The scripts `docs-state`, `docs-index` and `docs-check` read it through `scripts/docs_map.py`, and so do the writer agents. The reader of the documentation never sees it.
- **Holds:** a header (`target`: `engine` or a slug; `owner`) and these sections:
  - Paths: one line per reader (user, extender, evaluator), three to five pages in reading order
  - one section per section of the outline (`start`, `use`, `about`, `extend`, `reference`), each with one entry per page
  - Unowned: facts a page needs and no file supports
  - Did not fit: what contradicted itself or the outline
- An entry has the fields `title`, `line`, `kind`, `reader`, `says`, `inputs`, `links`, `must-not`, `made`, `evidence` (derived pages only) and `state`. Every path is relative to the target's root.

### `artefact-definition.md`

- **Skeleton of:** the definition of a kind of artefact.
- **Created by:** `/new-artefact` (`.claude/skills/new-artefact/SKILL.md`).
- **Holds:** a front-matter with a `description` ("Iterate NN-<artefact>.md: ...") and seven blocks, every one present; a block empty on purpose says so with the reason:
  - Target
  - Inputs
  - Aim
  - Partner
  - Map
  - Instruments
  - Course
- It closes with how the files are made: the first artefact from its template as version 0.1, with its history companion from `history.md`.

### `critic-definition.md`

- **Skeleton of:** a critic lens file.
- **Created by:** not named in the template.
- **Holds:** front-matter (`name: critic-<lens>`, `description`, `tools: Read, Glob, Grep`, `model: inherit`, the skill `critic-contract`) and a Lens section only. The Lens section has four parts: what you read, what to go after, the categories of a finding, and the own report sections. Shared behaviour is the contract skill's.

### `challenger-definition.md`

- **Skeleton of:** a challenger persona file.
- **Created by:** not named in the template.
- **Holds:** front-matter (`name: challenger-<persona>`, `description`, `tools: Read, Glob, Grep, WebSearch, WebFetch`, `model: inherit`, the skill `challenger-contract`) and a Lens section only. The Lens section has two parts: who you are (a role of its own, never a mirror of the principal) and what to go after.

### `check-definition.md`

- **Skeleton of:** a check file.
- **Created by:** not named in the template.
- **Holds:** front-matter (`name: check-<name>`, `description`, `tools: Read, Glob, Grep`, `model: inherit`, the skill `check-contract`) and a Lens section only. The Lens section has three parts: what you read, what you verify (each rule with its owner cited, never restated) and the cost, that is the scope read.
- In the three agent skeletons, a `description` that carries a colon followed by a space is put whole in single quotes, or the agent does not register.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
