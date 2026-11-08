---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 470a893691dcd097
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
  - templates/user-stories.md
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
  - templates/recipe-user-stories-export.md
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

The templates are the canonical skeletons in `templates/`: each is the shape of one kind of file the forge creates, and this page lists every one, what it is the skeleton of and which procedure creates from it. It is for the extender who needs to know which skeleton owns a file's shape. The principal is the person whose thinking is being forged. The ledger is the file that holds the state of a project, made at read time.

A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type that the forge can be extended by. There are four: an artefact, a critic lens, a challenger persona and a check.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts of one installation | on a new machine | `templates/CLAUDE.local.md`, made at the engine root |
| `project.md` | the project file | at the creation of a project | `templates/project.md`, made as `project.md` |
| `gitattributes` | the ways of merging by path | at the creation of a project | `templates/gitattributes`, made as `.gitattributes` |
| `gitignore` | what never enters git | at the creation of a project | `templates/gitignore`, made as `.gitignore` |
| `brief.md` | the brief | when a project or a whole of the ask begins | `templates/brief.md`, made as `00-brief.md` |
| `intent.md` | the intent | when the brief has been taken up | `templates/intent.md`, made as `10-intent.md` |
| `thread.md` | one open matter of the intent | when a matter stays open | `templates/thread.md`, made in `threads/` |
| `assignment.md` | the assignment | when work is handed to recipients | `templates/assignment.md`, made as `20-assignment.md` |
| `brd.md` | the business requirements document | when requirements need review and estimation | `templates/brd.md`, made as `30-brd.md` |
| `user-stories.md` | the user stories | when behaviour is agreed as stories | `templates/user-stories.md`, made as `35-user-stories.md` |
| `solution-design.md` | the solution design | when the realisation is designed | `templates/solution-design.md`, made as the solution design file |
| `work.md` | a work specification | when a work product is specified | `templates/work.md`, made in `work/` |
| `ledger.md` | the ledger | at every read of state | `templates/ledger.md`, made as `ledger.md` |
| `decisions.md` | the record of decisions | at the creation of a project | `templates/decisions.md`, made as `decisions.md` |
| `history.md` | the history companion of a versioned document | with every versioned document | `templates/history.md`, made beside the document |
| `index.md` | a resource index | for `sources/` and `research/` | `templates/index.md`, made as `00-INDEX.md` |
| `index-bundle.md` | the index of one bundle | when a bundle of sources is registered | `templates/index-bundle.md`, made as `sources/<slug>/00-INDEX.md` |
| `research.md` | one research note | when a card of a research returns | `templates/research.md`, made in `research/` |
| `research-plan.md` | the head of a research bundle | when a research of several questions is planned | `templates/research-plan.md`, made as `00-plan.md` |
| `recipe.md` | the generic render recipe | when no genre fits | `templates/recipe.md`, made in `recipes/` |
| `recipe-readme.md` | the readme recipe | at the creation of a project | `templates/recipe-readme.md`, made as `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | at the creation of a thought project | `templates/recipe-release-notes.md`, made as `recipes/release-notes.md` |
| `recipe-presentation.md` | the presentation recipe | for a slide-by-slide deck | `templates/recipe-presentation.md`, made in `recipes/` |
| `recipe-screenplay.md` | the screenplay recipe | for a video or a player page | `templates/recipe-screenplay.md`, made in `recipes/` |
| `recipe-user-stories-export.md` | the recipe that exports the stories | when stories go to a wiki or a tracker | `templates/recipe-user-stories-export.md`, made in `recipes/` |
| `html-player.html` | the player page | when the videos folder is written | `templates/html-player.html`, served as `docs/videos/index.html` |
| `docs-map.md` | the documentation map | at every documentation run | `templates/docs-map.md`, made as `docs-map.md` |
| `artefact-definition.md` | the definition of a kind of artefact | when a new artefact is added | `templates/artefact-definition.md` |
| `critic-definition.md` | a critic lens | when a new lens is added | `templates/critic-definition.md` |
| `challenger-definition.md` | a challenger persona | when a new persona is added | `templates/challenger-definition.md` |
| `check-definition.md` | a check | when a new check is added | `templates/check-definition.md` |

## Entries

Each entry says what the file is the skeleton of, which procedure creates from it where a skeleton comment or the project-creation command names one, and its fields or sections.

### CLAUDE.local.md

- **Skeleton of:** the instance file `CLAUDE.local.md` at the engine root.
- **Created by:** no procedure is named in the skeleton.
- **Fields:** three bullets: the principal's role, the conversation language and the author handle that signs the records the principal decides.

### project.md

- **Skeleton of:** the project file `project.md`.
- **Created by:** the project-creation command (`/new-project`) or the migration, once, at the creation of a project. No round of work writes it.
- **Fields:** front-matter with `project` (the slug), `kind` (`thought` or `library`) and `language` (an ISO 639-1 code, the language of the chain's artefacts).
- **A project without the file:** it is of the shape before the migration. The one remedy is `/migrate`. A command reports that shape as a fact, a check raises it as one finding with that fix, and nothing else of the new shape is raised against it.
- **The fixture flag:** a fixture project carries `fixture: true` in the same front-matter.

### gitattributes

- **Skeleton of:** the `.gitattributes` of a project, copied from the template by the project-creation command.
- **Fields:** one rule per line.
  - `* text=auto` normalises line endings.
  - `renders/**`, `docs/**` and `published/*.md` are merged as ours: they are derived files, made only on `main`.
  - `/README.md`, `/RELEASE-NOTES.md` and `/CONTRIBUTING.md` are the same way, anchored by a leading slash. A bare name matches at every depth and, with `core.ignorecase`, in every case, `recipes/readme.md` among them.
  - `published/*.pptx` and `published/*.docx` are binary and never merged.

### gitignore

- **Skeleton of:** the `.gitignore` of a project, copied by the project-creation command as it stands.
- **Fields:** two entries: `ledger.md`, because the ledger is made at read time and never kept in git, and `~$*`, the lock files of an open Office document.

### brief.md

- **Skeleton of:** a brief, `00-brief.md` or a later `00-brief-<name>.md`.
- **Created by:** `/forge brief`, which the project-creation command hands the brief to.
- **Fields:** front-matter with `project`, `title`, `author`, `version` and `status`. The text below the header is free-form.

### intent.md

- **Skeleton of:** the intent, `10-intent.md`.
- **Created by:** its own first `/forge intent`. The project-creation command does not create it.
- **Sections:** Essence, Positions, Facts, Rejected directions and, as an optional staging area, Candidate structure for the layer below.

### thread.md

- **Skeleton of:** one thread, one file in `threads/`.
- **Created by:** no procedure is named in the skeleton.
- **Fields:** front-matter with the thread's id, `concerns` (the artefacts it concerns, as `/forge` names them, comma-separated), `origin` (the principal, a document by path, or Claude's synthesis) and `status` (`open` or `closed`). The body is the thread: its first sentence is its headline and its last dated paragraph its state.

### assignment.md

- **Skeleton of:** the assignment, `20-assignment.md`.
- **Created by:** its own first `/forge assignment`.
- **Sections:** Purpose & Context, Objective, Scope (in scope, out of scope), Requirements (grouped), Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms. Constraints, Assumptions and Success Criteria are deleted when empty.

### brd.md

- **Skeleton of:** the business requirements document, `30-brd.md`.
- **Created by:** its own first `/forge brd`.
- **Front-matter:** `version`, `status`, `project` and `parent`, which is `20-assignment.md` or `10-intent.md`. A BRD made from a source is a work product, not this artefact.
- **Sections:** Purpose & Context, Objective, Stakeholders, Scope, Dependencies, Assumptions, Use cases, Business requirements, Touched areas of the enterprise, Qualities, Transition, Phasing, Success criteria, Open questions, Terms and Appendix: traceability.
- **Qualities:** the categories follow ISO/IEC 25010 and the practice of a regulated business. The skeleton states no value; a value comes from the stakeholders or is an open question with an owner.

### user-stories.md

- **Skeleton of:** the user stories, `35-user-stories.md`.
- **Created by:** its own first `/forge user-stories`. The kind is explained on [The user stories](../about/the-user-stories.md).
- **Front-matter:** `version`, `status`, `project` and `parent`, which is `30-brd.md` or `10-intent.md`. Stories made from a source are a work product.
- **Parts of a story:** a heading `US.NNNN — <function name>`, a free sentence, the acceptance criteria as items, then Edge cases, Risks, Note, Questions and Reference. Reference is the one part every story has. The others are left out where a story has nothing for them. Groups are plain headings without ids and are optional.

### solution-design.md

- **Skeleton of:** the solution design.
- **Created by:** its own first `/forge solution-design`.
- **Sections:** How the parts work together, Parts (grouped items that each say what they realise, the choice made and where), Across the parts and Open.

### work.md

- **Skeleton of:** the specification of a work product, in `work/`. The kind is explained on [The work product](../about/the-work-product.md).
- **Created by:** `/work`.
- **Front-matter:** `version`, `status`, `project` and `file`, the file the specification makes.
- **Sections:** Task, Inputs, Method, Assumptions, Open and Making. Assumptions and Open are deleted when empty.

### ledger.md

- **Skeleton of:** the ledger, `ledger.md`.
- **Created by:** the ledger script (`scripts/forge-ledger.py`) at read time.
- **Fields:** front-matter with `project` and `updated`. The tables are Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings, Challenges, then the lists Waiting on principal and Reports. A comment under each heading says which record or field each column is read from. A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal, and the Findings table returns with a check's first finding.

### decisions.md

- **Skeleton of:** the record of decisions, `decisions.md`.
- **Created by:** the project-creation command, with the slug filled and the sample record removed.
- **Fields:** one record per decision: Decision, Reason, Date, and a Verdict line.
- **The Verdict line:** it is present only where the decision rules on a finding or a challenge. It takes one line per id: that id `rejected`, `parked until <what>` or `obsolete`.

### history.md

- **Skeleton of:** the history companion of a versioned document, `<file>.history.md`.
- **Created by:** the project-creation command for the recipes' companions; every versioned document keeps one beside it.
- **Fields:** front-matter with `project` and `document`. Records are one line each: date, version, author, subject, kind (`created`, `changed`, `closed`, `removed` or `approved`), reason, then `Action` and `Was` where the record has them.

### index.md

- **Skeleton of:** the resource index, `00-INDEX.md` of `sources/` and of `research/`.
- **Created by:** the project-creation command (header filled, no entries). Entries are written by `/ingest` for sources and by `/research` for research.
- **Fields of a sources entry:** What, Origin, Date, Form, Role and Use for. Form is `text`, `extract of <original>` or `binary`.
- **Fields of a research entry:** Question, Answer in short and Consult when.

### index-bundle.md

- **Skeleton of:** the index of one bundle, `sources/<slug>/00-INDEX.md`.
- **Created by:** no procedure is named in the skeleton.
- **Fields:** front-matter with `bundle`, `project`, `date` and `origin`; an opening paragraph that says what the bundle is and whether it arrived whole or grows; then one entry per file with the fields of a sources entry in the same order.

### research.md

- **Skeleton of:** one research note, one card on one engine.
- **Created by:** `/research`. The note and the plan are in full on [Research note and bundle](research-bundle.md).
- **Sections:** In short, Question, Key findings, Unexpected, Not found, Options, Relevance to this project, Sources, Opened and not used and Search record.

### research-plan.md

- **Skeleton of:** the head of a research bundle, `00-plan.md`.
- **Created by:** `/research`.
- **Sections:** Summary, Plan (Purpose, Perspectives, Assumptions, Left out, Cards, Agents and the second engine's review), Deviations from the plan, Synthesis and Notes.

### recipe.md

- **Skeleton of:** a render recipe in `recipes/`.
- **Created by:** `/recipe`.
- **Fields:** front-matter with `project`, `purpose`, `audience` and `version`, and the optional `output` and `languages`. Sections: Inputs, Instructions, an optional Format and Template.

### recipe-readme.md

- **Skeleton of:** the readme recipe, `recipes/readme.md`.
- **Created by:** the project-creation command; iterated through `/recipe readme`. The README itself is rendered at every release.
- **Sections:** Inputs, Instructions, Pinned facts (not rendered) and Template. The Template section holds the README's own sections: what the project is, what you get, how to start, where it stands, documentation and about this README.
- **Pinned facts (not rendered):** optional. It holds facts of the project that no file owns yet, such as prerequisites or the public home of the repository. The README does not print them. The documentation's planner reads them here as an owner. One bullet each, dropped the day a file owns the fact.

### recipe-release-notes.md

- **Skeleton of:** the release-notes recipe, `recipes/release-notes.md`.
- **Created by:** the project-creation command; iterated through `/recipe release-notes`. Every release of the project renders it.
- **Sections:** Inputs (the histories of the chain, the decisions and the previous edition), Instructions and Template: one section per release with the groups Action required, Added, Changed, Removed, Fixed and Rejected.

### recipe-presentation.md

- **Skeleton of:** a presentation recipe, whose render is slide-by-slide source material for a deck.
- **Created by:** `/recipe presentation`.
- **Fields:** the generic recipe fields, a Format of `pptx`, and a Template table of slides. Each slide section holds On slide, Diagram and Speaker notes.

### recipe-screenplay.md

- **Skeleton of:** a screenplay recipe, whose render is the source of a video or of the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Fields:** front-matter with `languages` (the first primary) and an optional `output` into the engine's public videos folder. Instructions pin the beats, the quotes, the length and the translation. Format is `video` or `html-player`, never both. The Template holds a title card, a card of what the viewer will see, scenes (each a time, a Now and a Why caption and a fenced block of terminal lines) and an end card.

### recipe-user-stories-export.md

- **Skeleton of:** the recipe that exports the stories for a wiki or a tracker. The kind it serves is explained on [The user stories](../about/the-user-stories.md).
- **Created by:** `/recipe user-stories-export`.
- **Fields:** the input is the stories file. The Template is two headings, a purpose line in italics, then each story with its parts. No line is hard-wrapped. Reference carries the business-requirement, quality, use-case and dependency items and leaves out every position.

### html-player.html

- **Skeleton of:** the player page of the engine's videos folder.
- **Created by:** the video script (`scripts/md2video.py`) writes the served page `docs/videos/index.html` from it. It replaces one placeholder with the list of the folder's player files and another with a script tag per file. The served page is never edited: the skeleton is edited and the script writes the page anew.

### docs-map.md

- **Skeleton of:** the documentation map, `docs-map.md`, beside the owning project's ledger. The fields are in full on [Documentation map](documentation-map.md).
- **Created by:** the planner of `/document`.
- **Sections:** Paths (one line per reader), one section per section of the outline with one entry per page, Unowned and Did not fit. Front-matter holds `target` and `owner`.

### artefact-definition.md

- **Skeleton of:** the definition of a kind of artefact, a state file whose description opens it.
- **Created by:** `/new-artefact`.
- **Sections:** Target, Inputs, Aim, Partner, Map, Instruments and Course, then a closing paragraph on how the files are made. Every block is present; a block empty on purpose says so with the reason.

### critic-definition.md

- **Skeleton of:** a critic lens file, `critic-<lens>.md` in the agents folder.
- **Fields:** front-matter (`name`, `description`, `tools`, `model`, `skills`) and one Lens section with four parts: what the lens reads, what to go after, the categories and its own report sections.

### challenger-definition.md

- **Skeleton of:** a challenger persona file, `challenger-<persona>.md` in the agents folder.
- **Fields:** the same front-matter, with web tools among the `tools`, and one Lens section with two parts: who the persona is and what to go after.

### check-definition.md

- **Skeleton of:** a check file, `check-<name>.md` in the agents folder.
- **Fields:** the same front-matter and one Lens section with three parts: what the check reads, what it verifies and its cost.

For where the templates sit in the whole, see [What the forge is made of](../extend/what-it-is-made-of.md). For the terms used here, see the [Glossary](glossary.md).

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [The user stories](../about/the-user-stories.md): the kind the stories' skeleton and the export skeleton serve.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
