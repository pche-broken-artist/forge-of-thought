---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 432264fc6bdd5607
inputs:
  - templates/CLAUDE.local.md
  - templates/brief.md
  - templates/intent.md
  - templates/threads.md
  - templates/assignment.md
  - templates/solution-design.md
  - templates/ledger.md
  - templates/decisions.md
  - templates/history.md
  - templates/index.md
  - templates/index-bundle.md
  - templates/recipe.md
  - templates/recipe-readme.md
  - templates/recipe-release-notes.md
  - templates/recipe-presentation.md
  - templates/docs-map.md
  - templates/artefact-definition.md
  - templates/critic-definition.md
  - templates/challenger-definition.md
  - templates/check-definition.md
  - CLAUDE.md#Templates
---

# Templates

The templates are the canonical skeletons in `templates/`: every new project, document, recipe and definition starts from one of them. This page is for the extender who needs to know which skeleton exists, what it is the skeleton of, and which procedure creates from it. For where the templates sit in the whole, see [What the forge is made of](../extend/what-it-is-made-of.md).

## Naming rule

A template named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. There are four such types: an artefact, a critic lens, a challenger persona and a check.

## Overview

| Template | Skeleton of | Created by | Lives at |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts | `/setup` | engine root, `CLAUDE.local.md` |
| `brief.md` | a brief | `/forge brief` | `00-brief.md` |
| `intent.md` | the intent | `/forge intent` | `10-intent.md` |
| `threads.md` | the open threads | worked through the intent's definition | `threads.md` |
| `assignment.md` | the assignment | `/forge assignment` | `20-assignment.md` |
| `solution-design.md` | the solution design | `/forge solution-design` | `40-solution-design.md` |
| `ledger.md` | the ledger | a new project's scaffold | `ledger.md` |
| `decisions.md` | the decision records | a new project's scaffold | `decisions.md` |
| `history.md` | a history companion | with the birth of any versioned document | `<file>.history.md` |
| `index.md` | a resource index | `/ingest`, `/research` | `sources/00-INDEX.md`, `research/00-INDEX.md` |
| `index-bundle.md` | a bundle index | `/ingest` | `sources/<slug>/00-INDEX.md` |
| `recipe.md` | a render recipe | `/recipe` | `recipes/<recipe>.md` |
| `recipe-readme.md` | the readme recipe | `/recipe readme` | `recipes/readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | `/recipe release-notes` | `recipes/release-notes.md` |
| `recipe-presentation.md` | a presentation recipe | `/recipe presentation` | `recipes/<recipe>.md` |
| `docs-map.md` | the documentation map | the planner of `/document` | `docs-map.md` |
| `artefact-definition.md` | the definition of an artefact | `/new-artefact` | `.claude/skills/forge/states/<state>.md` |
| `critic-definition.md` | a critic lens | added by the principal's decision | `.claude/agents/critic-<lens>.md` |
| `challenger-definition.md` | a challenger persona | added by the principal's decision | `.claude/agents/challenger-<persona>.md` |
| `check-definition.md` | a check | added by the principal's decision | `.claude/agents/check-<name>.md` |

The "Created by" column for the scaffolded files, the two indexes and the three definitions of reviewers is taken from the conventions that name them. The skeletons themselves name the owner only for the rest.

## Entries

### `CLAUDE.local.md`
- **Skeleton of:** the instance facts file at the engine root, gitignored.
- **Created by:** `/setup` on a new machine.
- **Holds:** two bullets, the principal's role (whose thinking is being forged) and the conversation language.

### `brief.md`
- **Skeleton of:** a brief, the ask a project starts from.
- **Created by:** `/forge brief`.
- **Holds:** front-matter `project`, `title`, `date`, `author`, `version`, `status`, `last_change`; the text below it is free-form.

### `intent.md`
- **Skeleton of:** the intent, the trunk of every project.
- **Created by:** `/forge intent`.
- **Holds:** front-matter `version`, `date`, `status`, `last_change`, `project`, `audience`; sections Essence, Positions, Facts, Rejected directions and an optional Candidate structure for the layer below.

### `threads.md`
- **Skeleton of:** the project's open threads.
- **Created by:** the work on the intent.
- **Holds:** front-matter `project`; a heading and a list of items, each with its thread ID, the artefact it concerns in brackets and its text.

### `assignment.md`
- **Skeleton of:** the assignment handed to the recipients.
- **Created by:** `/forge assignment`.
- **Holds:** front-matter as the intent's, with `audience: recipients`; sections Purpose & Context, Objective, Scope, Requirements, Constraints, Assumptions, Deliverables, Open Questions, Success Criteria and Terms.

### `solution-design.md`
- **Skeleton of:** the solution design, how the things wanted are realised.
- **Created by:** `/forge solution-design`.
- **Holds:** front-matter as the intent's; sections How the parts work together, Parts, Across the parts and Open. Each part names what it realises, the choice made and where it lives.

### `ledger.md`
- **Skeleton of:** the ledger, the single source of truth for state.
- **Created by:** the scaffold of a new project; rewritten by every operation.
- **Holds:** front-matter `project`, `kind` (thought or library), `language`, `updated`; tables Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings and Challenges, and the list Waiting on principal. A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal.

### `decisions.md`
- **Skeleton of:** the append-only decision records.
- **Created by:** the scaffold of a new project.
- **Holds:** front-matter `project`; one record per decision with Decision, Reason and Date.

### `history.md`
- **Skeleton of:** the history companion of a versioned document.
- **Created by:** the birth of the document it belongs to.
- **Holds:** front-matter `project` and `document`; one line per change in the order date, version, author, subject, kind, reason, Action, Was. The kinds are created, changed, closed, removed and approved. The full field list is in the history companion's own reference page.

### `index.md`
- **Skeleton of:** the resource index of `sources/` or `research/`.
- **Created by:** `/ingest` for sources, `/research` for research.
- **Holds:** front-matter `project`, `directory`, `updated`; one entry per resource, in one of two forms.

A sources entry, headed by the file or bundle name:

| Field | Holds |
|---|---|
| What | what the resource is, in one or two sentences |
| Origin | where it came from, with the date as well as it is known |
| Role | free text: a standard to verify against, inspiration, a counter-example, a meeting record |
| Use for | what to reach for it for, the questions it answers best |

A research entry, headed by the dated note's file name:

| Field | Holds |
|---|---|
| Question | what the note set out to answer |
| Answer in short | two or three lines of the conclusion |
| Consult when | the situations in which the note is worth opening |

### `index-bundle.md`
- **Skeleton of:** the catalogue of one bundle, a set of related files that counts as one source.
- **Created by:** `/ingest`, at registration of the bundle if the index is missing.
- **Holds:** front-matter `bundle`, `project`, `date`, `origin`; one short paragraph on what the whole is and why it entered sources; then one entry per file, with the fields of the sources entry above, in the same order.

### `recipe.md`
- **Skeleton of:** a render recipe of any genre.
- **Created by:** `/recipe`.
- **Holds:** front-matter `project`, `purpose`, `audience`, `version`, `updated`, `last_change` and an optional `output`; sections Inputs, Instructions, an optional Format and Template.

### `recipe-readme.md`
- **Skeleton of:** the recipe of a project's README.
- **Created by:** `/recipe readme`.
- **Holds:** the recipe sections with the output path `README.md`; the Template carries the README's sections: What this project is, What you get, How to start, Where it stands, Documentation and About this README, then a dated footer.
- **Optional section "Pinned facts (not rendered)":** facts of the project that no file of the project owns yet, such as prerequisites, how a tool is installed or the public home of the repository. The README does not print them. The planner of `/document` reads them there as an owner. One bullet each; a fact is dropped the day a file owns it, and the section is left out when the project has none.
- **Fixed closing:** the skeleton fixes the closing sentence of the README verbatim. It is not repeated here.

### `recipe-release-notes.md`
- **Skeleton of:** the recipe of a project's release notes.
- **Created by:** `/recipe release-notes`.
- **Holds:** the recipe sections with the output path `RELEASE-NOTES.md`; Inputs are the histories of the chain, the decisions and the previous edition. The Template has one section per release with the groups Action required, Added, Changed, Removed, Fixed and Rejected, and a major's section with highlights.

### `recipe-presentation.md`
- **Skeleton of:** the recipe of a slide deck.
- **Created by:** `/recipe presentation`.
- **Holds:** the recipe sections with Format `pptx`; Instructions fix the per-slide format (title, On slide, Diagram, Speaker notes); the Template is a table of slide number, slide, content and diagram.

### `docs-map.md`
- **Skeleton of:** the documentation map, one entry per page and everything a page is made from.
- **Created by:** the planner of `/document`. It is read by the documentation scripts and by the writers, never by the reader of the documentation.
- **Holds:** front-matter `generated`, `target`, `owner`, `previous`; sections Paths, one section per section of the documentation, Unowned and Did not fit. The fields of an entry are on [Documentation map](documentation-map.md).

### `artefact-definition.md`
- **Skeleton of:** the definition of a kind of artefact.
- **Created by:** `/new-artefact`.
- **Holds:** front-matter `description`; seven blocks, each present: Target, Inputs, Aim, Partner, Map, Instruments and Course; then a closing paragraph on how the files are made.

### `critic-definition.md`
- **Skeleton of:** a critic lens file.
- **Created by:** hand, on the principal's decision.
- **Holds:** agent front-matter `name`, `description`, `tools`, `model`, `skills`, then one Lens section of four parts: what it reads, what to go after, the categories of its findings and its own report sections.

### `challenger-definition.md`
- **Skeleton of:** a challenger persona file.
- **Created by:** hand, on the principal's decision.
- **Holds:** agent front-matter as the critic's, then one Lens section of two parts: who the persona is and what blind spots it goes after.

### `check-definition.md`
- **Skeleton of:** a check file.
- **Created by:** hand, on the principal's decision.
- **Holds:** agent front-matter as the critic's, then one Lens section of three parts: what it reads, what it verifies and its cost.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
