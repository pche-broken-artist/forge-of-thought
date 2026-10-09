---
generated: 2026-10-09
made: mirrored
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

This page lists the files in `templates/`, the engine's canonical
skeletons, for someone extending the forge. For each it says what the
file is the skeleton of, what creates from it, and what it holds. The
skeletons themselves are not reproduced here; open the file for that.

Every new project is made from these skeletons. A skeleton carries its
rules in comments that are deleted when the file is born; the rules
themselves belong to the definition, the contract or the section of
`CLAUDE.md` the comment cites.

## Naming rule

A skeleton named `<type>-definition.md` is the skeleton of the
definition of one member of a type the forge can be extended by. There
are four such types: an artefact, a critic lens, a challenger persona
and a check. Other skeletons carry the name of the document they
produce.

## Skeletons of the chain and its records

| File | Skeleton of | Created from it by | Fields or sections |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts file at the engine root (gitignored) | `/setup` on a new machine | Principal (role); Conversation language |
| `brief.md` | a brief, `00-brief.md` or `00-brief-<name>.md` | `/forge brief` | Front-matter only is fixed: project, title, date, author, version, status, last_change; the body is free-form |
| `intent.md` | the intent, `10-intent.md` | `/forge intent` | Front-matter (version, date, status, last_change, project, audience); Essence; Positions; Facts; Rejected directions; Candidate structure for the layer below (optional) |
| `threads.md` | the project's open threads, `threads.md` | the intent's definition (Threads and files) | Front-matter (project); one list of threads, each with its ID and the artefact it concerns in brackets |
| `assignment.md` | the assignment, `20-assignment.md` | `/forge assignment` | Front-matter; Purpose & Context; Objective; Scope (in scope, out of scope); Requirements in groups; Constraints; Assumptions; Deliverables; Open Questions; Success Criteria; Terms |
| `solution-design.md` | the solution design, `40-solution-design.md` | `/forge solution-design` | Front-matter; How the parts work together; Parts in groups (each part: what it is, what it realises, the choice, where); Across the parts; Open |
| `ledger.md` | the ledger, `ledger.md` | `/new-project` at scaffold time | Front-matter (project, kind, language, updated); tables Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings, Challenges; list Waiting on principal |
| `decisions.md` | the append-only record of decisions, `decisions.md` | the forge, as the principal decides | Front-matter (project); one record per decision with Decision, Reason and Date |
| `history.md` | the history companion `<file>.history.md` of a versioned document | the forge, at the birth of the document and with every change | Front-matter (project, document); one line per change: date, version, author, subject, kind, reason, Action, Was |

Notes on the table:

- The ledger skeleton holds the one statement of how a `library` keeps
  only the Renders, Sources, Dependencies, Research and Waiting on
  principal parts; the other tables are deleted at scaffold time, and
  the Findings table returns with a check's first finding.
- The history line kinds are created, changed, closed, removed and
  approved. Reason is left out on `created`; Action and Was are written
  only where the record has them, Was always last. Lines are not
  wrapped.
- Statuses in the intent, assignment and solution design front-matter
  are `draft`, `approved` or `superseded`.
- The skeletons for decisions and threads name no command of their own
  in the inputs; the table gives the document that owns the rules.

## Skeletons of resource indexes

| File | Skeleton of | Created from it by | Fields or sections |
|---|---|---|---|
| `index.md` | the `00-INDEX.md` of `sources/` or `research/` | `/ingest` (sources) and `/research` (research) | Front-matter (project, directory, updated); one entry per resource |
| `index-bundle.md` | the `00-INDEX.md` inside a bundle `sources/<slug>/` | `/ingest`, at registration if missing | Front-matter (bundle, project, date, origin); one short paragraph on the whole; one entry per file |

### Fields of a sources entry

The heading is the file or bundle name in backticks.

| Field | Holds |
|---|---|
| What | what the resource is, in one or two sentences |
| Origin | where it came from: author, URL, meeting; date best effort |
| Role | free text: a standard to verify against, inspiration, a counter-example, a meeting record |
| Use for | what to reach for it for, the questions it answers best |

### Fields of a research entry

The heading is the note's file name, `YYYY-MM-DD-<topic>.md`.

| Field | Holds |
|---|---|
| Question | what the note set out to answer |
| Answer in short | two or three lines of the conclusion |
| Consult when | the situations in which the note is worth opening |

### Fields of a bundle index

The bundle index opens with its own header and a short paragraph on what
the whole bundle is and why it entered sources. Each file then has an
entry with the fields of a sources entry, in the same order. A bundle
appears as a single entry in the directory's index, pointing to its
inner index: two levels, never deeper.

## Skeletons of recipes

| File | Skeleton of | Created from it by | Fields or sections |
|---|---|---|---|
| `recipe.md` | a render recipe, `recipes/<recipe>.md` | `/recipe` | Front-matter (project, purpose, audience, version, updated, last_change, optional output); Inputs; Instructions; Format (optional); Template |
| `recipe-readme.md` | the readme genre, output `README.md` in the project root | `/recipe readme`; scaffolded by `/new-project` | Inputs (ledger, brief, intent); Instructions; Template: title, subtitle, What this project is, Where it stands, Renders, Waiting on the principal, Layout, About this README, dated footer |
| `recipe-release-notes.md` | the release-notes genre, output `RELEASE-NOTES.md` | `/recipe release-notes`; scaffolded by `/new-project` | Inputs (the histories, the intent, decisions, the previous edition); Instructions; Template: one section per release with groups Action required, Added, Changed, Removed, Fixed, Rejected |
| `recipe-presentation.md` | the presentation genre, slide-by-slide source material | `/recipe presentation` | Inputs; Instructions (message, density, vocabulary, per-slide format); Format (pptx); Template: slide table with number, slide, content, diagram |

Notes on the table:

- A recipe's Format section is optional. A recipe without it ends at the
  Markdown. When present it says the format (`pptx` or `docx`), the
  reference and page size of the plain file made by `/render`, and the
  template and model of the published file made by `/publish`. It is
  never copied into the render.
- Every recipe keeps its history in `recipes/<recipe>.history.md`.
- The readme skeleton's Instructions end with a fixed closing sentence
  for the section About this README; it is not repeated here.

## Skeletons of definitions

| File | Skeleton of | Created from it by | Fields or sections |
|---|---|---|---|
| `artefact-definition.md` | the definition of a kind of artefact, the state file `.claude/skills/forge/states/<state>.md` | `/new-artefact` | Front-matter (description); the seven blocks Target, Inputs, Aim, Partner, Map, Instruments, Course; a closing paragraph on how the files are made |
| `critic-definition.md` | a critic lens file, `.claude/agents/critic-<lens>.md` | a new lens, only by the principal's decision; no command is named in the inputs | Front-matter (name, description, tools, model, skills: `critic-contract`); a Lens section of four parts: what you read, what to go after, categories, own report sections |
| `challenger-definition.md` | a challenger persona file, `.claude/agents/challenger-<persona>.md` | a new persona, only by the principal's decision; no command is named in the inputs | Front-matter (same keys, skills: `challenger-contract`); a Lens section of two parts: who you are, what to go after |
| `check-definition.md` | a check file, `.claude/agents/check-<name>.md` | a new check, only by the principal's decision; no command is named in the inputs | Front-matter (same keys, skills: `check-contract`); a Lens section of three parts: what you read, what you verify, cost |

Notes on the table:

- The three reviewer skeletons hold the front-matter and the Lens
  section and nothing else. Shared behaviour is in the contract skill
  named in the front-matter.
- When a reviewer's description carries a colon followed by a space,
  the whole description goes in single quotes, with an apostrophe inside
  doubled; otherwise the agent does not register.
- In the artefact definition every block is present; a block empty on
  purpose says so with the reason.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
