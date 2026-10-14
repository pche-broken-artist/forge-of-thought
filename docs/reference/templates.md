---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: a9c06d251521409a
inputs:
  - templates/CLAUDE.local.md
  - templates/brief.md
  - templates/intent.md
  - templates/threads.md
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

A template is a canonical skeleton in `templates/`: the shape a new file starts from. This page lists every template for someone extending the forge, with what each is the skeleton of, what creates a file from it and the fields or sections it fixes. Terms of the forge are in the [Glossary](glossary.md); where the templates sit among the other parts is on [What the forge is made of](../extend/what-it-is-made-of.md).

The principal is whoever's thinking is being forged. The ledger is the single file that holds a project's state in tables.

## Naming rule

A template named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. The four types are an artefact, a critic lens, a challenger persona and a check. Every other template is named after the file it is the skeleton of.

## Overview

| Template | What it is the skeleton of | Created by | Where the file lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts | `/setup` | `CLAUDE.local.md` at the engine root |
| `brief.md` | a brief | `/forge brief` | `00-brief.md`, `00-brief-<name>.md` |
| `intent.md` | the intent | `/forge intent` | `10-intent.md` |
| `threads.md` | the open threads | the intent's definition | `threads.md` |
| `assignment.md` | the assignment | `/forge assignment` | `20-assignment.md` |
| `solution-design.md` | the solution design | `/forge solution-design` | `40-solution-design.md` |
| `work.md` | a work specification | `/work` | `work/<name>.spec.md` |
| `ledger.md` | the ledger | `/new-project` | `ledger.md` |
| `decisions.md` | the decisions record | the forge | `decisions.md` |
| `history.md` | a history companion | the write step of each versioned document | `<file>.history.md` |
| `index.md` | a resource index | `/ingest`, `/research` | `sources/00-INDEX.md`, `research/00-INDEX.md` |
| `index-bundle.md` | a bundle index | `/ingest` | `sources/<slug>/00-INDEX.md` |
| `recipe.md` | any recipe | `/recipe` | `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | `/recipe readme`, `/new-project` | `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | `/recipe release-notes`, `/new-project` | `recipes/release-notes.md` |
| `recipe-presentation.md` | a presentation recipe | `/recipe presentation` | `recipes/<recipe>.md` |
| `recipe-screenplay.md` | a screenplay recipe | `/recipe screenplay` | `recipes/<recipe>.md` |
| `html-player.html` | the player page | `scripts/md2video.py` | `docs/videos/index.html` |
| `docs-map.md` | the documentation map | the planner of `/document` | `docs-map.md` |
| `artefact-definition.md` | the definition of an artefact | `/new-artefact` | `.claude/skills/forge/states/<state>.md` |
| `critic-definition.md` | a critic lens | the principal's decision | `.claude/agents/critic-<lens>.md` |
| `challenger-definition.md` | a challenger persona | the principal's decision | `.claude/agents/challenger-<persona>.md` |
| `check-definition.md` | a check | the principal's decision | `.claude/agents/check-<name>.md` |

The inputs name no command that creates a file from the three reviewer templates. They say only that new lenses, personas and checks come by the principal's decision.

## Instance and chain

### `CLAUDE.local.md`

- **Skeleton of:** the instance facts file, which stays out of git.
- **Created by:** `/setup`, on a new machine.
- **Fields:** two bullets, the principal's role and the conversation language.

### `brief.md`

- **Skeleton of:** a brief.
- **Created by:** `/forge brief`.
- **Fields:** a front-matter header only (`project`, `title`, `date`, `author`, `version`, `status`, `last_change`); the text below it is free-form.

### `intent.md`

- **Skeleton of:** the intent, the trunk of every project.
- **Created by:** `/forge intent`.
- **Fields:** a header (`version`, `date`, `status`, `last_change`, `project`, `audience`) and the sections Essence, Positions, Facts, Rejected directions and, optionally, Candidate structure for the layer below.

### `threads.md`

- **Skeleton of:** the project's open threads.
- **Created by:** the definition of the intent.
- **Fields:** a header with `project` and a list of threads, each opening with its ID and the artefact it concerns in brackets.

### `assignment.md`

- **Skeleton of:** the assignment.
- **Created by:** `/forge assignment`.
- **Fields:** a header (`version`, `date`, `status`, `last_change`, `project`, `audience`) and the sections Purpose & Context, Objective, Scope, Requirements, Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms.

### `solution-design.md`

- **Skeleton of:** the solution design.
- **Created by:** `/forge solution-design`.
- **Fields:** a header as above and the sections How the parts work together, Parts, Across the parts and Open. Each part is one item with its name, what it answers for, the positions it realises, its choice and its place.

### `work.md`

- **Skeleton of:** a work specification, the way and the why of a work product. The kind is explained in [The work product](../about/the-work-product.md).
- **Created by:** `/work`, at the specification's birth.
- **Fields:** a header (`version`, `date`, `status`, `last_change`, `project`, `file`) and the sections Task, Inputs, Method, Assumptions, Open and Making. `file` names the file the specification makes. Inputs cite items by ID and files by path, never copied.

### `ledger.md`

- **Skeleton of:** the ledger.
- **Created by:** `/new-project`.
- **Fields:** a header (`project`, `kind`, `language`, `updated`) and the tables Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings and Challenges, then the list Waiting on principal. A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal.

### `decisions.md`

- **Skeleton of:** the decisions record, append-only.
- **Created by:** the forge.
- **Fields:** a header with `project`; one record per decision, with the decision in one line and the fields Decision, Reason and Date.

### `history.md`

- **Skeleton of:** the history companion of a versioned document.
- **Created by:** the write step of the document it belongs to.
- **Fields:** a header (`project`, `document`) and one line per change: date, version, author, subject, kind, reason, Action, Was. The kinds are created, changed, closed, removed and approved. Reason is left out on `created`, and Was is always last.

## Resource indexes

### `index.md`

- **Skeleton of:** the index of a `sources/` or `research/` directory.
- **Created by:** `/ingest` writes the entries of sources, `/research` those of research.
- **Fields:** a header (`project`, `directory`, `updated`) and one entry per resource, in one of two forms.

| Entry | Heading | Fields |
|---|---|---|
| sources | the file or the bundle | What, Origin, Role, Use for |
| research | the dated file name | Question, Answer in short, Consult when |

A bundle appears in the directory index as one entry.

### `index-bundle.md`

- **Skeleton of:** the index of one bundle, `sources/<slug>/`.
- **Created by:** `/ingest`, at registration, if it is missing.
- **Fields:** a header (`bundle`, `project`, `date`, `origin`), one short paragraph on what the whole bundle is and why it entered sources, then one entry per file. The per-file entry is the sources entry of `index.md`, with the same fields in the same order.

## Recipes

### `recipe.md`

- **Skeleton of:** any recipe.
- **Created by:** `/recipe`.
- **Fields:** a header (`project`, `purpose`, `audience`, `version`, `updated`, `last_change`; optional `output` and `languages`) and the sections Inputs, Instructions, Format (optional) and Template. `languages` names the languages of the render: the first is primary and the rest are its translations, one render per language. Format names `pptx`, `docx`, `video` or `html-player`, the plain file made through pandoc or, for a screenplay, through `scripts/md2video.py`, and the published file made through a model.

### `recipe-readme.md`

- **Skeleton of:** the readme recipe.
- **Created by:** `/recipe readme`, and `/new-project`.
- **Fields:** the header of a recipe with `output: README.md`, and the sections Inputs, Instructions, Pinned facts (not rendered) and Template. The template carries the sections What this project is, What you get, How to start, Where it stands, Documentation, About this README and a dated footer.
- **Pinned facts (not rendered):** an optional section for facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them. The planner of the documentation reads them there as an owner. Each fact is one bullet, dropped the day a file owns it, and the section is omitted when the project has none.

### `recipe-release-notes.md`

- **Skeleton of:** the release-notes recipe.
- **Created by:** `/recipe release-notes`, and `/new-project`.
- **Fields:** the header of a recipe with `output: RELEASE-NOTES.md`, and the sections Inputs, Instructions and Template. The template holds one section per release with the groups Action required, Added, Changed, Removed, Fixed and Rejected, and a major's section with its highlights.

### `recipe-presentation.md`

- **Skeleton of:** a presentation recipe, whose render is a slide-by-slide deck definition.
- **Created by:** `/recipe presentation`.
- **Fields:** the header of a recipe and the sections Inputs, Instructions, Format and Template. Each slide is one section with On slide, Diagram and Speaker notes; the template lists the slides in a table of number, slide, content and diagram.

### `recipe-screenplay.md`

- **Skeleton of:** a screenplay recipe, whose render is the source of a video or of the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Fields:** the header of a recipe with `languages` and, for the player page only, an optional `output` into the engine's public folder, and the sections Inputs, Instructions, Format and Template.
- **Inputs:** session records registered as sources, the brief of the videos and a document the video shows, cited as a dependency by path.
- **Instructions:** the number of scenes, the audience and register, the one message, the beats pinned so that every render is the same cut, the rules of the quotes, the length, what the title card discloses, what must not appear, and the translation of the other languages from the primary.
- **Format:** one of `video` and `html-player`, never both, with the pace in words a second, the date in the tab bar and the labels of the captions by language.
- **Template:** a title card, a card of what the viewer will see, scenes and an end card. A scene carries the time of day, a caption of two parts (Now and Why) and a fenced block of what the terminal shows.

## The player page

### `html-player.html`

- **Skeleton of:** the player page of the engine.
- **Created by:** `scripts/md2video.py` writes the served page `docs/videos/index.html` from it. The script replaces the `FILES` placeholder with the list of the folder's html-player files and the `SCRIPTS` placeholder with one script tag per file. The data arrive through `forgeVideo()` calls, so the page works from a file on disk as well as from a public host.
- **Fields:** a single HTML file whose head comment says what it is. The served page is never edited; the skeleton is edited and the script writes the page anew.

## The documentation map

### `docs-map.md`

- **Skeleton of:** the documentation map, the file the documentation is made from. The fields of an entry are in the [Documentation map](documentation-map.md).
- **Created by:** the planner of `/document`.
- **Fields:** a header (`generated`, `target`, `owner`, `previous`), a Paths section with one line per reader, then one section per section of the outline with one entry per page, then Unowned and Did not fit. An entry has title, line, kind, reader, says, inputs, links, must-not, made, evidence for derived pages, and state. Every path is relative to the target's root.

## Definitions of members

### `artefact-definition.md`

- **Skeleton of:** the definition of a kind of artefact.
- **Created by:** `/new-artefact`.
- **Fields:** a front-matter `description` and seven blocks: Target, Inputs, Aim, Partner, Map, Instruments and Course. Every block is present; a block left empty says so with the reason. A closing paragraph says how the first artefact, its history companion and its ledger row are made.

### `critic-definition.md`

- **Skeleton of:** a critic lens file.
- **Fields:** front-matter (`name`, `description`, `tools`, `model`, `skills`) and one Lens section. The Lens section holds what the lens reads, what it goes after, its categories and any report sections of its own. The shared conduct is in the contract skill the front-matter names.

### `challenger-definition.md`

- **Skeleton of:** a challenger persona file.
- **Fields:** front-matter as above and one Lens section with two parts: who the persona is, and what it goes after.

### `check-definition.md`

- **Skeleton of:** a check file.
- **Fields:** front-matter as above and one Lens section with three parts: what the check reads, what it verifies with the owner of each rule cited, and its cost.

A description that carries a colon followed by a space is put whole in single quotes in all three reviewer files; otherwise the agent does not register.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
