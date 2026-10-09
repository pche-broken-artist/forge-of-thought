---
generated: 2026-10-09
made: mirrored
inputs-hash: b29ed7800f7adb0d
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
  - templates/artefact-definition.md
  - templates/critic-definition.md
  - templates/challenger-definition.md
  - templates/check-definition.md
  - CLAUDE.md
---

# Templates

This page lists every file in `templates/`, the canonical skeletons the forge creates documents from. It is for someone extending the forge who needs to know which skeleton shapes which document, what creates from it, and what fields or sections it fixes.

## The naming rule

A skeleton named `<type>-definition.md` is the skeleton of the definition of one member of a type the forge can be extended by. There are four such types: an artefact, a critic lens, a challenger persona and a check. Other skeletons are named after the document they shape (`brief.md`, `ledger.md`) or, for recipes, `recipe-<genre>.md`.

## The skeletons

### Instance and chain

| Skeleton | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts file at the engine root (gitignored) | `/setup`, on a new machine | Principal (role); Conversation language |
| `brief.md` | a brief (`00-brief.md`, `00-brief-<name>.md`) | `/forge brief` | Front-matter only (project, title, date, author, version, status, last_change); the text below it is free-form |
| `intent.md` | the intent (`10-intent.md`) | `/forge intent` | Front-matter (version, date, status, last_change, project, audience); sections Essence, Positions, Facts, Rejected directions, Candidate structure for the layer below (optional) |
| `threads.md` | the project's open threads (`threads.md`) | `/forge intent` | Front-matter (project); one list of open threads, each with the artefact it concerns |
| `assignment.md` | the assignment (`20-assignment.md`) | `/forge assignment` | Front-matter as the intent; sections Purpose & Context, Objective, Scope (in scope, out of scope), Requirements (grouped), Constraints, Assumptions, Deliverables, Open Questions, Success Criteria, Terms |
| `solution-design.md` | the solution design (`40-solution-design.md`) | `/forge solution-design` | Front-matter as the intent; sections How the parts work together, Parts (items with what they realise, the choice and where), Across the parts, Open |

### State and records

| Skeleton | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `ledger.md` | a project's ledger | `/new-project` | Front-matter (project, kind, language, updated); tables Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings, Challenges; list Waiting on principal. A library keeps only Renders, Sources, Dependencies, Research and Waiting on principal |
| `decisions.md` | a project's decisions record | the forge, appending one record per decision | Front-matter (project); one record per decision with Decision, Reason, Date |
| `history.md` | the history companion of a versioned document (`<file>.history.md`) | the definition of the document it belongs to, when the document is first made | Front-matter (project, document); one line per change: date, version, author, subject, kind, reason, Action, Was |

The history line's kinds are created, changed, closed, removed and approved. Reason is left out on `created`; Action and Was appear only where the record has them, with Was always last.

### Resource indexes

| Skeleton | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `index.md` | the `00-INDEX.md` of a `sources/` or `research/` directory | `/ingest` (sources), `/research` (research) | Front-matter (project, directory, updated); one entry per resource |
| `index-bundle.md` | the `00-INDEX.md` inside a source bundle (`sources/<slug>/`) | `/ingest`, at registration of the bundle, if missing | Front-matter (bundle, project, date, origin); one opening paragraph; one entry per file |

#### Fields of a sources entry

An entry is headed by the file or bundle name. Its fields are:

- **What:** what the resource is, in one or two sentences.
- **Origin:** where it came from, with a best-effort date.
- **Role:** free text, such as a standard to verify against, inspiration, a counter-example or a meeting record.
- **Use for:** what to reach for it for, the questions it answers best.

#### Fields of a research entry

An entry is headed by the note's dated file name. Its fields are:

- **Question:** what the note set out to answer.
- **Answer in short:** two or three lines of the conclusion.
- **Consult when:** the situations in which the note is worth opening.

#### Fields of a bundle index

The bundle index has its own header (bundle slug, project slug, date, origin) and one short opening paragraph saying what the whole bundle is and why it entered sources. Each file in the bundle then has an entry with the fields of the sources entry above, in the same order. The bundle skeleton cites the sources entry and does not repeat it.

### Recipes

| Skeleton | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `recipe.md` | any render recipe (`recipes/<recipe>.md`) | `/recipe` | Front-matter (project, purpose, audience, version, updated, last_change, optional output); sections Inputs, Instructions, Format (optional), Template |
| `recipe-readme.md` | the readme-genre recipe | `/recipe readme`, scaffolded by `/new-project` | The recipe shape; output is `README.md` in the project root; its template has sections for what the project is, where it stands, renders, what waits on the principal, layout and an "About this README" closing with a dated footer |
| `recipe-release-notes.md` | the release-notes-genre recipe | `/recipe release-notes`, scaffolded by `/new-project` for a thought project | The recipe shape; output is `RELEASE-NOTES.md`; one section per release, newest first, with the groups Action required, Added, Changed, Removed, Fixed and Rejected |
| `recipe-presentation.md` | the presentation-genre recipe | `/recipe presentation` | The recipe shape; Instructions fix the per-slide format (On slide, Diagram, Speaker notes); Format is `pptx`; its template is a table of slide number, slide, content and diagram |

The genre skeletons are named `recipe-<genre>.md`. Every recipe carries `updated` in place of `date` and no status.

### Definitions of the forge's extensible types

| Skeleton | Skeleton of | Created by | Fields or sections |
|---|---|---|---|
| `artefact-definition.md` | the definition of a kind of artefact (`.claude/skills/forge/states/<state>.md`) | `/new-artefact` | Front-matter (description); the seven blocks Target, Inputs, Aim, Partner, Map, Instruments, Course, then a paragraph on how the files are made |
| `critic-definition.md` | a critic lens file (`.claude/agents/critic-<lens>.md`) | the principal's decision to add a lens | Agent front-matter (name, description, tools, model, skills); a Lens section of four parts: what you read, what to go after, categories, own report sections |
| `challenger-definition.md` | a challenger persona file (`.claude/agents/challenger-<persona>.md`) | the principal's decision to add a persona | Agent front-matter as the critic's; a Lens section of two parts: who you are, what to go after |
| `check-definition.md` | a check file (`.claude/agents/check-<name>.md`) | the principal's decision to add a check | Agent front-matter as the critic's; a Lens section of three parts: what you read, what you verify, cost |

For the three reviewer skeletons, the file holds the front-matter and the Lens section only. The shared behaviour comes from the contract skill named in the front-matter, and the skeleton's comment is deleted in the finished file. A description that carries a colon followed by a space is put whole in single quotes, or the agent does not register.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
