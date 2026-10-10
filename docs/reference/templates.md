---
generated: 2026-10-10
made: mirrored
inputs-hash: 8a08723ba2af0fdc
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
  - CLAUDE.md
---

# Templates

This page lists every file in `templates/`, the canonical skeletons the
forge makes new files from. It is for someone extending the forge or
checking what a skeleton holds: for each file it says what it is the
skeleton of, what creates from it, and its fields or sections in one
line.

## The naming rule

A skeleton named `<type>-definition.md` is the skeleton of the
definition of one member of a type the forge can be extended by: an
artefact, a critic lens, a challenger persona or a check. Every other
skeleton is named after the document it shapes.

## Instance and chain documents

| File | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `templates/CLAUDE.local.md` | the instance facts file at the engine root, gitignored | `/setup` fills it on a new machine | Principal (the role whose thinking is forged); Conversation language |
| `templates/brief.md` | a brief | the brief's definition, `/forge brief` | Header only (project, title, date, author, version, status, last_change); the text below it is free-form |
| `templates/intent.md` | the intent | the intent's definition, `/forge intent` | Header (version, date, status, last_change, project, audience); Essence; Positions; Facts; Rejected directions; Candidate structure for the layer below (optional staging area) |
| `templates/threads.md` | the project's open threads | the intent's definition | Header (project); one list of threads, each `THR.NNNN`, the artefact it concerns in brackets, then its text |
| `templates/assignment.md` | the assignment | the assignment's definition, `/forge assignment` | Header (same fields as the intent, audience: recipients); Purpose & Context; Objective; Scope (in scope, out of scope); Requirements (grouped); Constraints; Assumptions; Deliverables; Open Questions; Success Criteria; Terms |
| `templates/solution-design.md` | the solution design | the solution design's definition, `/forge solution-design` | Header (audience: whoever realises the solution); How the parts work together; Parts (grouped SOL items: what it is, what it realises, the choice, where); Across the parts; Open |
| `templates/ledger.md` | a project's ledger | project scaffolding, `/new-project` | Header (project, kind, language, updated); tables Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings, Challenges; list Waiting on principal |
| `templates/decisions.md` | the decisions record | the forge, at the principal's decisions | Header (project); one record per decision: Decision, Reason, Date |
| `templates/history.md` | the history companion of a versioned document | written with every change of that document | Header (project, document); one log line per change: date, version, author, subject, kind, reason, Action, Was |

A few points of detail on these skeletons:

- The ledger's header comment is where the reduction for a library
  lives: a library keeps only Renders, Sources, Dependencies, Research
  and Waiting on principal.
- The ledger's Renders table also takes the documentation index as a
  row, written by `/document`.
- A history log line is
  `<date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>`.
  The kinds are created, changed, closed, removed and approved. Reason
  is left out on `created`; Action and Was appear only where the record
  has them, Was always last.

## Resource indexes

Two skeletons catalogue resources, so that a reader knows what exists
and what it is for without opening it.

| File | Skeleton of | Created by | Fields |
|---|---|---|---|
| `templates/index.md` | the `00-INDEX.md` of a `sources/` or a `research/` directory | `/ingest` writes the sources entries, `/research` the research entries | Header (project, directory, updated); one entry per resource |
| `templates/index-bundle.md` | the `00-INDEX.md` of a bundle, a subdirectory `sources/<slug>/` | `/ingest`, at registration of the bundle, if missing | Header (bundle, project, date, origin); one short paragraph on what the whole is and why it entered sources; one entry per file |

The fields of a resource index entry:

| Directory | Entry heading | Fields |
|---|---|---|
| sources | the file or bundle name | What; Origin; Role; Use for |
| research | the dated note name, `YYYY-MM-DD-<topic>.md` | Question; Answer in short; Consult when |

What each source field holds:

- **What**: what the resource is, in one or two sentences.
- **Origin**: where it came from (author, URL, meeting), the date best
  effort.
- **Role**: free text, for example a standard to verify against,
  inspiration, a counter-example, a meeting record.
- **Use for**: what to reach for it for.

What each research field holds:

- **Question**: what the note set out to answer.
- **Answer in short**: two or three lines of the conclusion.
- **Consult when**: the situations in which the note is worth opening.

In a bundle index each per-file entry has the fields of the sources
entry, in the same order. A bundle appears in the directory's own index
as one entry that points to its inner index.

## Recipes

| File | Skeleton of | Created by | Sections |
|---|---|---|---|
| `templates/recipe.md` | any render recipe | `/recipe` | Header (project, purpose, audience, version, updated, last_change, optional output path); Inputs; Instructions; Format (optional); Template |
| `templates/recipe-readme.md` | the readme-genre recipe, output `README.md` | `/recipe readme`, scaffolded by `/new-project` | Header (output `README.md`); Inputs; Instructions; Pinned facts (not rendered), optional; Template |
| `templates/recipe-release-notes.md` | the release-notes-genre recipe, output `RELEASE-NOTES.md` | `/recipe release-notes`, scaffolded by `/new-project` | Header (output `RELEASE-NOTES.md`); Inputs (the histories, the intent, decisions, the previous edition); Instructions; Template |
| `templates/recipe-presentation.md` | the presentation-genre recipe, a slide-by-slide deck definition | `/recipe presentation` | Header; Inputs; Instructions (including the per-slide format); Format (pptx); Template (a slide table) |

The Format section of a recipe is optional: a recipe without it ends at
the Markdown. Where present, it names the format (`pptx` or `docx`),
how the plain file made by `/render` through pandoc is set up
(reference document, page size), and how the published file made by
`/publish` through a model is set up (template, model, anything else
the model must know).

A genre skeleton is named `recipe-<genre>.md`, and `/recipe <genre>`
composes a recipe from it through a genre interview.

### The optional section "Pinned facts (not rendered)"

The readme skeleton has an optional section, "Pinned facts (not
rendered)". It holds facts of the project that no file of the project
owns yet, such as prerequisites, how a tool is installed, or the public
home of the repository. The README does not print them. The
documentation's planner reads them there as an owner of those facts.
Each fact is one bullet. A fact is dropped from the section the day a
file owns it, and the section is omitted when the project has none.

## The documentation map

| File | Skeleton of | Created by | Fields |
|---|---|---|---|
| `templates/docs-map.md` | the documentation map `docs-map.md`, kind `map`, beside the owning project's ledger | the planner agent of `/document` | Header (generated, target, owner, previous); one section per section of the outline (start, use, about, extend, reference), in that order; Unowned; Did not fit |

Each page entry in a section carries: title, kind (how-to, explanation
or reference), reader (user, extender or evaluator), says, inputs,
links, must-not, made (mirrored or derived), evidence (derived pages
only) and state (new, keep, regenerate or remove). Unowned lists every
fact a page needs that no file supports, with the page that needs it.
Did not fit lists what contradicted itself or the outline, and what was
done with it. The fields in full are on the documentation map page.

The map is read by the scripts `docs-state`, `docs-index` and
`docs-check` through `scripts/docs_map.py`, and by the writer agents.
It is never shown to the reader of the documentation.

## Skeletons of definitions

Each of these is the skeleton of one member of a type the forge extends
by (see the naming rule above).

| File | Skeleton of | Created by | Contents |
|---|---|---|---|
| `templates/artefact-definition.md` | the definition of a kind of artefact, `.claude/skills/forge/states/<state>.md` | `/new-artefact` | Front-matter description; seven blocks: Target, Inputs, Aim, Partner, Map, Instruments, Course; then how the files are made (the artefact from its template as 0.1, its history companion, its row in the ledger's Documents table) |
| `templates/critic-definition.md` | a critic lens file, `.claude/agents/critic-<lens>.md` | by the principal's decision to add a lens | Front-matter (name, description, tools, model, skills); a Lens section of four parts: what you read, what to go after, categories, own report sections |
| `templates/challenger-definition.md` | a challenger persona file, `.claude/agents/challenger-<persona>.md` | by the principal's decision to add a persona | Front-matter (name, description, tools, model, skills); a Lens section of two parts: who you are, what to go after |
| `templates/check-definition.md` | a check file, `.claude/agents/check-<name>.md` | by the principal's decision to add a check | Front-matter (name, description, tools, model, skills); a Lens section of three parts: what you read, what you verify, cost |

In the three agent skeletons the shared behaviour comes from the
contract skill named in the front-matter, and only the Lens section is
the file's own. When a description carries a colon followed by a space,
the whole description goes in single quotes, or the agent does not
register.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
