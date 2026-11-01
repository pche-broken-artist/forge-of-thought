---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: c8f5c710f7d1fa12
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

This page lists every skeleton in `templates/`: what each is the skeleton
of, which command or procedure creates a file from it, and the fields or
sections it fixes. It is for the extender, who needs to know which
skeleton to change or to add when the shape of a file changes. For where
the templates sit among the other parts of the forge, see
[What the forge is made of](../extend/what-it-is-made-of.md); the terms
used here are in the [Glossary](glossary.md).

Each template is the canonical skeleton of one kind of file. A
skeleton is copied and filled, and its comments are deleted in the file
made from it unless the entry says they are kept. The principal (whoever's
thinking is being forged) is the one the commands below work with.

## Overview

| Template | Skeleton of | Created by | Lives as |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts | `/setup` | `CLAUDE.local.md` at the engine root |
| `project.md` | the project file | `/new-project`, or the migration | `project.md` |
| `gitattributes` | the ways of merging by path | `/new-project` | `.gitattributes` |
| `gitignore` | what never enters git | `/new-project` | `.gitignore` |
| `brief.md` | a brief | `/forge brief` | `00-brief.md`, `00-brief-<name>.md` |
| `intent.md` | the intent | `/forge intent` | `10-intent.md` |
| `thread.md` | a thread of the intent | the intent's definition | `threads/THR.NNNN.md` |
| `assignment.md` | the assignment | `/forge assignment` | `20-assignment.md` |
| `brd.md` | the business requirements document | `/forge brd` | `30-brd.md` |
| `solution-design.md` | the solution design | `/forge solution-design` | the solution design file |
| `work.md` | a work specification | `/work` | `work/<name>.spec.md` |
| `ledger.md` | the ledger | `scripts/forge-ledger.py` | `ledger.md` |
| `decisions.md` | the record of decisions | `/new-project` | `decisions.md` |
| `history.md` | a history companion | the birth of a versioned document | `<file>.history.md` |
| `index.md` | a resource index | `/new-project`; entries by `/ingest` and `/research` | `sources/00-INDEX.md`, `research/00-INDEX.md` |
| `index-bundle.md` | the index of a bundle | `/ingest` | `sources/<slug>/00-INDEX.md` |
| `research.md` | a research note | `/research` | `research/YYYY-MM-DD-<topic>.md`, or `<card>.<engine>.md` in a bundle |
| `research-plan.md` | the head of a research bundle | `/research` | `research/YYYY-MM-DD-<topic>/00-plan.md` |
| `recipe.md` | a render recipe, generic | `/recipe` | `recipes/<recipe>.md` |
| `recipe-readme.md` | the README recipe | `/new-project`; iterated by `/recipe readme` | `recipes/readme.md` |
| `recipe-release-notes.md` | the release notes recipe | `/new-project`; iterated by `/recipe release-notes` | `recipes/release-notes.md` |
| `recipe-presentation.md` | a presentation recipe | `/recipe presentation` | `recipes/<recipe>.md` |
| `recipe-screenplay.md` | a screenplay recipe | `/recipe screenplay` | `recipes/<recipe>.md` |
| `html-player.html` | the player page | `scripts/md2video.py` | `docs/videos/index.html` |
| `docs-map.md` | the documentation map | the planner of `/document` | `docs-map.md` |
| `artefact-definition.md` | the definition of an artefact | `/new-artefact` | `.claude/skills/forge/states/<state>.md` |
| `critic-definition.md` | a critic lens | the principal's decision | `.claude/agents/critic-<lens>.md` |
| `challenger-definition.md` | a challenger persona | the principal's decision | `.claude/agents/challenger-<persona>.md` |
| `check-definition.md` | a check | the principal's decision | `.claude/agents/check-<name>.md` |

## The naming rule

A skeleton named `<type>-definition.md` is the skeleton of the
definition of one member of a type the forge can be extended by. There
are four such types: an artefact, a critic lens, a challenger persona and
a check. A skeleton named `recipe-<genre>.md` is the skeleton of the
recipe of one genre. Any other name is the skeleton of a file of that
name.

## Instance and project files

### `CLAUDE.local.md`
- **Skeleton of:** the instance facts file at the engine root, which is
  not tracked in git.
- **Created by:** `/setup` on a new machine.
- **Fields:** one line each for Principal (a role), Conversation
  language and Author (the principal's short handle, signed on every
  record he decides).

### `project.md`
- **Skeleton of:** the project file.
- **Created by:** `/new-project`, or the migration of a project made
  before the file existed. It is written once and never by a round of
  work.
- **Fields:** `project` (the slug), `kind` (`thought` or `library`),
  `language` (an ISO 639-1 code, the language of the chain's
  artefacts). A fixture project also carries `fixture: true`.
- **A project without the file:** it has the shape from before the
  migration. The one remedy is `/migrate`. A command reports the shape
  as a fact, a check raises it as one finding with that remedy, and
  nothing else of the new shape is raised against the project.

### `gitattributes`
- **Skeleton of:** the `.gitattributes` of a project, copied as it
  stands.
- **Created by:** `/new-project`.
- **Holds:** line-ending normalisation for all files; `merge=ours` for
  the derived files (`renders/`, `README.md`, `RELEASE-NOTES.md`,
  `CONTRIBUTING.md`, `docs/`, `published/*.md`); `binary` for the
  published `.pptx` and `.docx` files.

### `gitignore`
- **Skeleton of:** the `.gitignore` of a project, copied as it stands.
- **Created by:** `/new-project`.
- **Holds:** the ledger (`ledger.md`) and the lock files of an open
  Office document (`~$*`).

## The chain

### `brief.md`
- **Skeleton of:** a brief.
- **Created by:** `/forge brief`, which `/new-project` hands the
  principal's text to.
- **Fields:** the header only, `project`, `title`, `author`, `version`,
  `status`. The text below it is free-form.

### `intent.md`
- **Skeleton of:** the intent.
- **Created by:** the first `/forge intent` of a project.
- **Sections:** Essence; Positions; Facts; Rejected directions;
  Candidate structure for the layer below (optional).

### `thread.md`
- **Skeleton of:** one thread of the intent, one file in `threads/`.
- **Created by:** the intent's definition, which owns the rules of a
  thread, its life and its closing.
- **Fields:** `id`, `concerns` (the artefact it concerns, as `/forge`
  names it; several are comma-separated), `origin` (the principal, a
  document by path, or Claude's synthesis), `status` (`open` or
  `closed`). The body is free text: the first sentence is the headline,
  the last dated paragraph is the state.

### `assignment.md`
- **Skeleton of:** the assignment.
- **Created by:** `/forge assignment`.
- **Sections:** Purpose & Context; Objective; Scope (in scope, out of
  scope); Requirements; Constraints; Assumptions; Deliverables; Open
  Questions; Success Criteria; Terms.

### `brd.md`
- **Skeleton of:** the business requirements document.
- **Created by:** `/forge brd`.
- **Fields:** the header carries `parent:`, which is either
  `20-assignment.md` or `10-intent.md`. A BRD made from a source is a
  work product instead.
- **Sections:** Purpose & Context; Objective; Stakeholders; Scope;
  Dependencies; Assumptions; Use cases; Business requirements; Touched
  areas of the enterprise; Qualities; Transition; Phasing; Success
  criteria; Open questions; Terms; Appendix: traceability. The
  categories of Qualities follow the public standard ISO/IEC 25010 and
  the practice of a regulated business. No value in the skeleton stands
  as a requirement.

### `solution-design.md`
- **Skeleton of:** the solution design.
- **Created by:** `/forge solution-design`.
- **Sections:** How the parts work together; Parts; Across the parts;
  Open.

## Work, records and state

### `work.md`
- **Skeleton of:** the specification of a work product. The file the
  specification makes lies beside it. The kind is explained in
  [The work product](../about/the-work-product.md).
- **Created by:** `/work`.
- **Fields:** the header carries `file:`, the file the specification
  makes.
- **Sections:** Task; Inputs; Method; Assumptions; Open; Making.

### `ledger.md`
- **Skeleton of:** the ledger, the one place where the state of a
  project is read.
- **Created by:** `scripts/forge-ledger.py`, at read time. It is never
  in git.
- **Tables:** Briefs; Documents; Renders; Published; Work; Sources;
  Dependencies; Research; Findings; Challenges. Then Waiting on
  principal, and Reports where there is something to report. A library
  keeps only Renders, Sources, Dependencies, Research and Waiting on
  principal.

### `decisions.md`
- **Skeleton of:** the append-only record of the principal's decisions.
- **Created by:** `/new-project`, with the slug filled and the sample
  record removed.
- **Fields of a record:** Decision; Reason; Verdict; Date.
- **The Verdict line:** present only where the decision rules on a
  finding or a challenge, one line per ID it rules on. Its forms are
  `<ID> rejected`, `<ID> parked until <what>` and `<ID> obsolete`.

### `history.md`
- **Skeleton of:** the history companion of a versioned document.
- **Created by:** the birth of the document, beside it. `/new-project`
  also makes one for each recipe it scaffolds.
- **Fields of a record:** one line each, appended and never rewritten,
  `date | version | author | subject | kind | reason | Action | Was`.
  The kinds are `created`, `changed`, `closed`, `removed` and
  `approved`. The reason is left out on `created`; `Action` and `Was`
  stand only where the record has them, `Was` always last.

## Resource indexes

### `index.md`
- **Skeleton of:** the index of `sources/` or of `research/`.
- **Created by:** `/new-project`, with the header filled and no entries.
  `/ingest` writes the entries of sources and `/research` those of
  research.
- **Fields of a sources entry:** What; Origin; Date (from the content,
  the file or the ingest); Form (text, extract of an original, or
  binary); Role; Use for.
- **Fields of a research entry:** Question; Answer in short; Consult
  when.

### `index-bundle.md`
- **Skeleton of:** the index of one bundle of sources.
- **Created by:** `/ingest`, at the registration of the bundle if the
  index is missing.
- **Fields:** the header carries `bundle`, `project`, `date` and
  `origin`. An opening paragraph says what the whole is and whether it
  arrived whole or grows. Each file then has an entry with the fields of
  a sources entry of `index.md`, in its order.

## Research

The research note and plan are described in full on
[Research note and bundle](research-bundle.md).

### `research.md`
- **Skeleton of:** one research note, one card on one engine.
- **Created by:** `/research`.
- **Fields:** the header carries `date`, `project`, `topic`, `status`,
  `engine`, `model`, `usage`, `run` and `derived_from`.
- **Sections:** In short; Question; Key findings; Unexpected; Not
  found; Options; Relevance to this project; Sources; Opened and not
  used; Search record.

### `research-plan.md`
- **Skeleton of:** the head of a research bundle, `00-plan.md`.
- **Created by:** `/research`.
- **Fields:** the header carries `date`, `project`, `topic`, `status`,
  `engines` and `derived_from`.
- **Sections:** Summary; Plan (Purpose, Perspectives, Assumptions, Left
  out, Cards, Agents, The second engine's review of the draft);
  Deviations from the plan; Synthesis (Completeness card by card,
  Answers side by side, Unexpected gathered, Not found gathered, Claude's
  view); Notes.

## Recipes

### `recipe.md`
- **Skeleton of:** a render recipe, the shape every genre keeps.
- **Created by:** `/recipe`.
- **Fields:** the header carries `project`, `purpose`, `audience` and
  `version`, and optionally `output` and `languages`.
- **Sections:** Inputs; Instructions; Format (optional); Template.

### `recipe-readme.md`
- **Skeleton of:** the recipe of a README.
- **Created by:** `/new-project`; iterated by `/recipe readme`.
- **Sections:** the shape of `recipe.md`, with a section Pinned facts
  (not rendered) between Instructions and Template. The Template is the
  README: What this project is; What you get; How to start; Where it
  stands; Documentation; About this README.
- **Pinned facts (not rendered):** optional. One bullet each for a fact
  of the project that no file of the project owns yet, such as a
  prerequisite, how a tool is installed or the public home of the
  repository. The README does not print them. The planner of the
  documentation reads them as an owner. A bullet is dropped the day a
  file owns the fact, and the section is omitted when there are none.

### `recipe-release-notes.md`
- **Skeleton of:** the recipe of the release notes.
- **Created by:** `/new-project`; iterated by `/recipe release-notes`.
- **Sections:** the shape of `recipe.md`. The Template has one section
  per release, newest first, with the groups Action required, Added,
  Changed, Removed, Fixed and Rejected.

### `recipe-presentation.md`
- **Skeleton of:** the recipe of a presentation, a slide-by-slide deck
  definition.
- **Created by:** `/recipe presentation`.
- **Sections:** the shape of `recipe.md`. Its Template is a table of
  slides (number, slide, content, diagram), and each slide is rendered
  with On slide, Diagram and Speaker notes.

### `recipe-screenplay.md`
- **Skeleton of:** the recipe of a screenplay, the source of a video or
  of the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Fields:** the header carries `project`, `purpose`, `audience`,
  `version` and `languages` (the first primary, the rest translations),
  and optionally `output`, which for a player file may send it into the
  engine's `docs/videos/`.
- **Sections:** Inputs; Instructions (the beats, the quotes, the length,
  the title card, what must not appear, the translation); Format (one of
  `video` or `html-player`, never both); Template. The Template is a
  title card, a card of what the viewer will see, one scene per beat and
  an end card. A scene carries a time, a caption of two parts (Now and
  Why) and a fenced block of what the terminal shows.

### `html-player.html`
- **Skeleton of:** the player page of the engine.
- **Created by:** `scripts/md2video.py`, which writes the served page
  `docs/videos/index.html` from it. It replaces one placeholder with the
  list of the folder's player files and another with a script tag per
  file.
- **Edited:** the served page is never edited; the skeleton is, and the
  script writes the page anew.

## The documentation map

### `docs-map.md`
- **Skeleton of:** the documentation map of a target. Its fields are
  given in full on [Documentation map](documentation-map.md).
- **Created by:** the planner agent of `/document`.
- **Fields:** the header carries `target` (`engine` or a slug) and
  `owner`.
- **Sections:** Paths; then one section per section of the outline
  (start, use, about, extend, reference); Unowned; Did not fit. Each
  page has one entry with title, line, kind, reader, says, inputs,
  links, must-not, made, evidence (derived pages only) and state.

## Definitions of what the forge can be extended by

### `artefact-definition.md`
- **Skeleton of:** the definition of a kind of artefact.
- **Created by:** `/new-artefact`.
- **Sections:** an opening paragraph, then seven blocks: Target;
  Inputs; Aim; Partner; Map; Instruments; Course. A block empty on
  purpose says so with the reason.

### `critic-definition.md`
- **Skeleton of:** a critic lens file.
- **Created by:** the principal's decision to add a lens.
- **Holds:** the front-matter (`name`, `description`, `tools`, `model`,
  `skills`) and one section, Lens, in four parts: what the lens reads,
  what to go after, the categories of a finding, and the report sections
  of its own.

### `challenger-definition.md`
- **Skeleton of:** a challenger persona file.
- **Created by:** the principal's decision to add a persona.
- **Holds:** the front-matter and one section, Lens, in two parts: who
  the persona is and what to go after.

### `check-definition.md`
- **Skeleton of:** a check file.
- **Created by:** the principal's decision to add a check.
- **Holds:** the front-matter and one section, Lens, in three parts: what
  the check reads, what it verifies and the cost of its scope.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
