---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: 14a95f79756a4e7c
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

This page lists every skeleton in `templates/`, what each is the skeleton of, and the procedure that creates files from it. It is for the extender who adds or changes a kind of document. Terms of the forge are in the [Glossary](glossary.md); where the templates sit in the whole is on [What the forge is made of](../extend/what-it-is-made-of.md).

The templates are the canonical skeletons for every new project. A template says what comes out; the rules of the document belong to its definition (the state file of the artefact) or to the command that uses it. Where a template does not say which procedure creates from it, the entry says so.

## The naming rule

A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. There are four such types: an artefact, a critic lens, a challenger persona and a check.

## Overview

| Template | Skeleton of | Created by | Lives in a project as |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts | not stated in the template | `CLAUDE.local.md` at the engine root |
| `project.md` | the project file | `/new-project` or the migration | `project.md` |
| `gitattributes` | the ways of merging by path | not stated in the template | `.gitattributes` |
| `brief.md` | a brief | the brief's definition | `00-brief.md`, `00-brief-<name>.md` |
| `intent.md` | the intent | the intent's definition | `10-intent.md` |
| `thread.md` | a thread | the intent's definition | `threads/THR.NNNN.md` |
| `assignment.md` | the assignment | the assignment's definition | `20-assignment.md` |
| `solution-design.md` | the solution design | the solution design's definition | the solution design file |
| `work.md` | a work specification | `/work` | `work/<name>.spec.md` |
| `ledger.md` | the ledger | `scripts/forge-ledger.py` | `ledger.md` |
| `decisions.md` | the decisions record | not stated in the template | `decisions.md` |
| `history.md` | a history companion | made with the document it belongs to | `<file>.history.md` |
| `index.md` | a resource index | `/ingest`, `/research` | `sources/00-INDEX.md`, `research/00-INDEX.md` |
| `index-bundle.md` | the index of a bundle | not stated in the template | `sources/<slug>/00-INDEX.md` |
| `recipe.md` | a render recipe | `/recipe` | `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | `/recipe readme` | `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | `/recipe release-notes` | `recipes/release-notes.md` |
| `recipe-presentation.md` | a presentation recipe | `/recipe presentation` | `recipes/<recipe>.md` |
| `recipe-screenplay.md` | a screenplay recipe | `/recipe screenplay` | `recipes/<recipe>.md` |
| `html-player.html` | the player page of the engine | `scripts/md2video.py` | `docs/videos/index.html` |
| `docs-map.md` | the documentation map | the planner of `/document` | `docs-map.md` |
| `artefact-definition.md` | the definition of an artefact | `/new-artefact` | `.claude/skills/forge/states/<state>.md` |
| `critic-definition.md` | a critic lens | not stated in the template | `.claude/agents/critic-<lens>.md` |
| `challenger-definition.md` | a challenger persona | not stated in the template | `.claude/agents/challenger-<persona>.md` |
| `check-definition.md` | a check | not stated in the template | `.claude/agents/check-<name>.md` |

## Entries

### `CLAUDE.local.md`
- **Skeleton of:** the instance facts of one installation, kept at the engine root and not in git.
- **Created by:** not stated in the template.
- **Fields:** Principal (whose thinking is forged, as a role), Conversation language, Author (the principal's short handle, the author of every record the principal decides).

### `project.md`
- **Skeleton of:** the project file.
- **Created by:** `/new-project`, or the migration. It is written once, never by a round, and merged as text.
- **Fields:** `project` (the slug), `kind` (`thought` or `library`), `language` (ISO 639-1, the language of the chain's artefacts). A fixture project also carries `fixture: true`.
- **A project without the file** is of the shape before the migration. The one remedy is `/migrate`. A command reports that shape as a fact, a check reports it as one finding with that fix, and nothing else of the new shape is raised against the project.

### `gitattributes`
- **Skeleton of:** the `.gitattributes` of a project, copied from this template.
- **Created by:** not stated in the template.
- **Contents:** line endings normalised with `* text=auto`. Derived files are taken as ours at a merge and made again: `renders/**`, `README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**` and `published/*.md`. The published `.pptx` and `.docx` files are binary and never merged.

### `brief.md`
- **Skeleton of:** a brief.
- **Created by:** the brief's definition.
- **Fields:** a header only (`project`, `title`, `author`, `version`, `status`). The text below the header is free-form.

### `intent.md`
- **Skeleton of:** the intent.
- **Created by:** the intent's definition.
- **Header:** `version`, `status` (`draft`, `approved` or `superseded`), `project`, `audience`.
- **Sections:** Essence, Positions, Facts, Rejected directions, and an optional Candidate structure for the layer below. The last is left out where the project takes no layer, and deleted once the layer exists.

### `thread.md`
- **Skeleton of:** one thread, one file in `threads/`.
- **Created by:** the intent's definition, which also holds the rules of a thread, its life and its closing.
- **Header:** `id`, `concerns` (the artefact it concerns, as `/forge` names it; several are comma-separated), `origin` (the principal by default, a document by path, or Claude's synthesis), `status` (`open` or `closed`).
- **Body:** free text. Its first sentence is its headline, its last dated paragraph its state, and it records the date it was opened.

### `assignment.md`
- **Skeleton of:** the assignment.
- **Created by:** the assignment's definition.
- **Header:** `version`, `status`, `project`, `audience` (recipients).
- **Sections:** Purpose & Context, Objective, Scope (in scope, and out of scope as items), Requirements (grouped), Constraints, Assumptions, Deliverables, Open Questions, Success Criteria, Terms. Constraints, Assumptions and Success Criteria are deleted when empty.

### `solution-design.md`
- **Skeleton of:** the solution design.
- **Created by:** the solution design's definition.
- **Header:** `version`, `status`, `project`, `audience` (whoever realises the solution).
- **Sections:** How the parts work together, Parts (grouped), Across the parts, Open. An item of Parts carries what it is, what it realises, the choice it rests on and where it lives.

### `work.md`
- **Skeleton of:** the specification of a [work product](../about/the-work-product.md). The specification holds the way and the why, and the file beside it holds the content.
- **Created by:** `/work`.
- **Header:** `version`, `status`, `project`, `file` (the file the specification makes, `work/<name>.<ext>`).
- **Sections:** Task, Inputs (items by ID and files by path, never copied), Method, Assumptions, Open, Making. Assumptions and Open continue the project's own numbering, after every specification it already has, and are deleted when empty. Making says how the file is made from the specification and is never copied into the file.

### `ledger.md`
- **Skeleton of:** the ledger, the single source of truth for state. It is made when it is read and is never in git.
- **Created by:** `scripts/forge-ledger.py`. The script keeps the comments of the skeleton, which say what each table holds and which record or field each column is read from.
- **Header:** `project`, `updated`. Kind and language are echoed from the project file.
- **Tables:** Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings, Challenges. After them come Waiting on principal and Reports, which stands only when there is something to report.
- **Library:** a project of kind `library` keeps only Renders, Sources, Dependencies, Research and Waiting on principal. The Findings table returns with a check's first finding.

### `decisions.md`
- **Skeleton of:** the decisions record, append-only. Newest is last, and a later decision supersedes an earlier one by a new record that names it.
- **Created by:** not stated in the template.
- **Header:** `project`.
- **A record** is headed `DEC.NNNN` with the decision in one line, then four fields: Decision, Reason, Verdict, Date.
- **The Verdict line** appears only where the decision rules on a finding or a challenge, one line for each ID it rules on. Its three forms are `<ID> rejected`, `<ID> parked until <what>` and `<ID> obsolete`. A partial verdict is read as the verdict on the whole ID, and the rest is recorded as a `changed` record in the history.

### `history.md`
- **Skeleton of:** the history companion of a versioned document, a log of one line per change, appended at the end and never rewritten.
- **Created by:** made with the document it belongs to. At the birth of a document there is one record of the file and one naming every item born with it.
- **Header:** `project`, `document` (the versioned document it belongs to).
- **A record** has the fields date, version, author, subject, kind, reason, and then `Action` and `Was` where the record has them, `Was` always last.
- **Kinds:** `created`, `changed`, `closed`, `removed`, `approved`. The reason is left out on `created`.
- **Records of state** carry the current version and do not raise it. The template names their shapes: the mining of a brief, a finding or a challenge settled, and a work product's state.

### `index.md`
- **Skeleton of:** the resource index of a `sources/` or a `research/` directory.
- **Created by:** `/ingest` writes the sources entries and `/research` the research entries.
- **Header:** `project`, `directory` (`sources` or `research`).
- **A sources entry**, headed by the file or bundle in backticks, has the fields:
  - What: what the resource is.
  - Origin: where it came from.
  - Date: the day, taken from the content, the file or the ingest. It is best effort and never asked.
  - Form: `text`, `extract of <original>` or `binary`. A source has one form.
  - Role: free text, such as a standard to verify against or a meeting record.
  - Use for: the questions it answers best.
- **A research entry**, headed by the note's file name, has the fields:
  - Question: what the note set out to answer.
  - Answer in short: the conclusion in two or three lines.
  - Consult when: the situations in which the note is worth opening.
- **A bundle** is one entry that points to its own index.

### `index-bundle.md`
- **Skeleton of:** the index of one bundle, the directory `sources/<slug>/` that counts as one source.
- **Created by:** not stated in the template.
- **Header:** `bundle` (the slug), `project`, `date`, `origin` (where the whole came from).
- **Body:** one short paragraph saying what the bundle is and why it entered `sources/`, and whether it arrived whole or grows. Then one entry per file, with the fields of the sources entry of `index.md`, in the same order.

### `recipe.md`
- **Skeleton of:** a render recipe in general. It owns the shape only.
- **Created by:** `/recipe`.
- **Header:** `project`, `purpose`, `audience`, `version`. Optional: `output` (overrides the default `renders/<recipe>.md`) and `languages` (the first primary, the rest its translations, one render per language).
- **Sections:** Inputs (artefacts by path, one per line), Instructions, an optional Format, Template. The Format section names the format (`pptx`, `docx`, `video` or `html-player`), the plain file made by `/render` and the published file made by `/publish`. A recipe without it ends at the Markdown.

### `recipe-readme.md`
- **Skeleton of:** the readme recipe of a project. It is the one owner of what a README carries.
- **Created by:** `/recipe readme`.
- **Header:** `project`, `purpose: readme`, `audience`, `version`, `output: README.md`.
- **Sections:** Inputs, Instructions, an optional Pinned facts (not rendered), Template.
- **Template headings:** What this project is, What you get, How to start, Where it stands, Documentation, About this README, then a dated footer.
- **Pinned facts (not rendered):** facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them. The planner of the documentation reads them there as an owner. Each is one bullet and is dropped the day a file owns the fact. The section is omitted when the project has none.

### `recipe-release-notes.md`
- **Skeleton of:** the release-notes recipe of a project.
- **Created by:** `/recipe release-notes`.
- **Header:** `project`, `purpose: release-notes`, `audience`, `version`, `output: RELEASE-NOTES.md`.
- **Sections:** Inputs (the histories of the intent and of the layers below it, the current intent, the decisions and the previous edition), Instructions, Template.
- **Template:** one section per release, newest first, with the groups Action required, Added, Changed, Removed, Fixed, Rejected. An approved major opens with a few sentences of highlights, and the sections of earlier releases are carried over verbatim.

### `recipe-presentation.md`
- **Skeleton of:** a presentation recipe. Its render is a slide-by-slide deck definition, from which `/render` makes a plain PowerPoint file and `/publish` the designed one.
- **Created by:** `/recipe presentation`.
- **Header:** `project`, `purpose`, `audience`, `version`, optional `output`.
- **Sections:** Inputs, Instructions, Format (`pptx`), Template. The Template is a table of slides: number, slide, content, diagram.
- **Per-slide format:** a heading `SNN`, then On slide, Diagram (only where the template assigns one) and Speaker notes.

### `recipe-screenplay.md`
- **Skeleton of:** a screenplay recipe. Its render is the source from which `scripts/md2video.py` makes a video or the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Header:** `project`, `purpose`, `audience`, `version`, `languages` (the first primary, the rest translations). An optional `output` may point an html-player file into the engine's public folder `docs/videos/`.
- **Sections:** Inputs (session records registered as sources, the brief of the videos, a document the video shows), Instructions, Format, Template.
- **Instructions** carry the audience, the one message, the pinned beats, the rules for quotes, the length, the disclosure on the title card, what must not appear and the rule of translation.
- **Format** is one of `video` or `html-player`, never both. It states the pace in words a second, the date in the tab bar and the labels of the captions by language.
- **Template:** a title card, a card of what you will see, scenes and an end card. A scene has a time of day, a caption of two parts (Now and Why) and a fenced block of what the terminal shows.

### `html-player.html`
- **Skeleton of:** the player page of the engine. The served page `docs/videos/index.html` is written from it.
- **Created by:** `scripts/md2video.py`. It replaces the `FILES` placeholder with the list of the folder's html-player files and the `SCRIPTS` placeholder with a script tag per file. The data arrive through `forgeVideo()` calls, so the page works from a file on disk as well as from GitHub Pages.
- **Rule:** the served page is never edited. The skeleton is edited and the script writes the page anew.

### `docs-map.md`
- **Skeleton of:** the documentation map of the engine or of a project. The [Documentation map](documentation-map.md) page gives its fields in full.
- **Created by:** the planner of `/document`. The scripts and the writer agents read it. The reader of the documentation never sees it.
- **Header:** `target` (`engine` or a slug), `owner`.
- **Sections:** Paths (one line per reader), then one section per section of the outline (`start`, `use`, `about`, `extend`, `reference`), then Unowned and Did not fit.
- **An entry** has the fields title, line, kind, reader, says, inputs, links, must-not, made, evidence (derived pages only) and state.

### `artefact-definition.md`
- **Skeleton of:** the definition of a kind of artefact, in seven blocks.
- **Created by:** `/new-artefact`.
- **Header:** `description`.
- **Blocks:** Target, Inputs, Aim, Partner, Map, Instruments, Course. Every block is present. A block that is empty on purpose says so with the reason.

### `critic-definition.md`
- **Skeleton of:** a critic lens file.
- **Created by:** not stated in the template.
- **Header:** `name` (`critic-<lens>`), `description`, `tools` (Read, Glob, Grep), `model: inherit`, `skills` (the critic contract).
- **Body:** a Lens section only, in four parts: what you read, what to go after, the categories of a finding and the report sections of its own.

### `challenger-definition.md`
- **Skeleton of:** a challenger persona file.
- **Created by:** not stated in the template.
- **Header:** `name` (`challenger-<persona>`), `description`, `tools` (Read, Glob, Grep, WebSearch, WebFetch), `model: inherit`, `skills` (the challenger contract).
- **Body:** a Lens section only, in two parts: who you are, and what to go after.

### `check-definition.md`
- **Skeleton of:** a check file.
- **Created by:** not stated in the template.
- **Header:** `name` (`check-<name>`), `description`, `tools` (Read, Glob, Grep), `model: inherit`, `skills` (the check contract).
- **Body:** a Lens section only, in three parts: what you read, what you verify, and the cost.

For the three agent files, a description that contains a colon followed by a space is put whole in single quotes, or the agent does not register.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
