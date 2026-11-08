---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 44ee5921ad2910f9
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

A template is a canonical skeleton in `templates/` from which the
forge creates a file of one kind. This page lists every file of
`templates/`, says what it is the skeleton of and which command or
script creates from it, and gives its fields or sections in one line.
It is for the extender, who needs to know which skeleton a new file
starts from. Where the templates sit in the whole is
[What the forge is made of](../extend/what-it-is-made-of.md); every
term of the forge is in the [Glossary](glossary.md).

A skeleton named `<type>-definition.md` is the skeleton of the
definition of one member of a type the forge can be extended by: an
artefact, a critic lens, a challenger persona or a check. Every other
skeleton is the shape of a document or a file.

The principal is whoever's thinking is being forged. The ledger is
the single source of truth for the state of a project, made when it
is read and never kept in git.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `CLAUDE.local.md` | the instance facts of one installation | a new machine, at setup | `templates/CLAUDE.local.md` |
| `project.md` | the project file: slug, kind, language | the creation of a project | `templates/project.md` |
| `gitattributes` | the ways of merging by path | the creation of a project | `templates/gitattributes` |
| `gitignore` | what never enters a project's repository | the creation of a project | `templates/gitignore` |
| `brief.md` | the brief, the ask as it came | the start of a project | `templates/brief.md` |
| `intent.md` | the intent, the trunk of the chain | after the brief | `templates/intent.md` |
| `thread.md` | one open matter of the intent | a matter left open | `templates/thread.md` |
| `assignment.md` | the assignment to the recipients | a layer below the intent | `templates/assignment.md` |
| `brd.md` | the business requirements document | a layer below the assignment or the intent | `templates/brd.md` |
| `user-stories.md` | the user stories | a layer below the BRD | `templates/user-stories.md` |
| `solution-design.md` | how the things wanted are realised | a layer that realises the intent | `templates/solution-design.md` |
| `work.md` | the specification of a work product | a work product | `templates/work.md` |
| `ledger.md` | the shape of the ledger | made at read time | `templates/ledger.md` |
| `decisions.md` | the record of the principal's decisions | the creation of a project | `templates/decisions.md` |
| `history.md` | the history companion of a versioned document | any versioned document | `templates/history.md` |
| `index.md` | a resource index | `sources/` and `research/` | `templates/index.md` |
| `index-bundle.md` | the index of one bundle of sources | a bundle | `templates/index-bundle.md` |
| `research.md` | one research note | one card, one engine | `templates/research.md` |
| `research-plan.md` | the head of a research bundle | a research of several questions | `templates/research-plan.md` |
| `recipe.md` | the shape of any recipe | a render of no genre | `templates/recipe.md` |
| `recipe-readme.md` | the README recipe | every project | `templates/recipe-readme.md` |
| `recipe-release-notes.md` | the release-notes recipe | every thought project | `templates/recipe-release-notes.md` |
| `recipe-presentation.md` | a slide-by-slide deck recipe | a presentation | `templates/recipe-presentation.md` |
| `recipe-screenplay.md` | a screenplay recipe | a video | `templates/recipe-screenplay.md` |
| `recipe-user-stories-export.md` | the export recipe of the stories | stories pasted into a wiki or a tracker | `templates/recipe-user-stories-export.md` |
| `html-player.html` | the player page of the videos | the public folder of videos | `templates/html-player.html` |
| `docs-map.md` | the documentation map | a documentation run | `templates/docs-map.md` |
| `artefact-definition.md` | the definition of an artefact | a new kind of artefact | `templates/artefact-definition.md` |
| `critic-definition.md` | the file of a critic lens | a new lens | `templates/critic-definition.md` |
| `challenger-definition.md` | the file of a challenger persona | a new persona | `templates/challenger-definition.md` |
| `check-definition.md` | the file of a check | a new check | `templates/check-definition.md` |

## Entries

Each entry gives what the file is the skeleton of, what creates from
it, and its fields or sections.

### Instance and project files

#### `CLAUDE.local.md`
- **Skeleton of:** the file of instance facts, filled on a new machine.
- **Created by:** `/setup`.
- **Fields:** Principal (the role), Conversation language, Author (the
  principal's handle, which signs every record he decides).

#### `project.md`
- **Skeleton of:** the project file, written once at the creation of a
  project.
- **Created by:** `/new-project`, or the migration.
- **Fields:** `project` (the slug), `kind` (`thought` or `library`),
  `language` (ISO 639-1, the language of the chain's artefacts).
- **Fixture flag:** a fixture project carries `fixture: true`.
- **A project without the file:** it is of the shape before the
  migration. The one remedy is `/migrate`. A command reports the shape
  as a fact, a check reports it as one finding with that fix, and
  nothing else of the new shape is raised against it.

#### `gitattributes`
- **Skeleton of:** a project's `.gitattributes`, the ways of merging by
  path.
- **Created by:** `/new-project`, which copies it.
- **Holds:** line endings normalised for every file; the derived paths
  taken as ours at a merge (`renders/**`, `docs/**`, `published/*.md`);
  the three root files `/README.md`, `/RELEASE-NOTES.md` and
  `/CONTRIBUTING.md`, each anchored by a leading slash; the published
  `.pptx` and `.docx` marked binary.

#### `gitignore`
- **Skeleton of:** a project's `.gitignore`.
- **Created by:** `/new-project`, which copies it as it stands.
- **Holds:** the ledger (`ledger.md`) and the lock files of an open
  Office document (`~$*`).

### The chain

#### `brief.md`
- **Skeleton of:** a brief.
- **Created by:** `/forge brief`.
- **Fields:** a fixed header (`project`, `title`, `author`, `version`,
  `status`); the text below it is free-form.

#### `intent.md`
- **Skeleton of:** the intent.
- **Created by:** `/forge intent`.
- **Sections:** Essence; Positions; Facts; Rejected directions;
  Candidate structure for the layer below (optional).

#### `thread.md`
- **Skeleton of:** one thread, one file per thread in `threads/`.
- **Created by:** the intent's definition, worked through
  `/forge intent`.
- **Fields:** `id`, `concerns` (the artefact it concerns, as `/forge`
  names it, several comma-separated), `origin` (the principal, a
  document by path, or Claude's synthesis), `status` (`open` or
  `closed`).
- **Body:** the first sentence is the headline, the last dated
  paragraph is the state, and the opening date is stated.

#### `assignment.md`
- **Skeleton of:** the assignment.
- **Created by:** `/forge assignment`.
- **Sections:** Purpose & Context; Objective; Scope (in scope, out of
  scope); Requirements (grouped); Constraints; Assumptions;
  Deliverables; Open Questions; Success Criteria; Terms.

#### `brd.md`
- **Skeleton of:** the business requirements document.
- **Created by:** `/forge brd`.
- **Header:** `parent` is `20-assignment.md` or `10-intent.md`. A BRD
  made from a source is a work product instead.
- **Sections:** Purpose & Context; Objective; Stakeholders; Scope;
  Dependencies; Assumptions; Use cases; Business requirements;
  Touched areas of the enterprise; Qualities (one line per category,
  named after the public standard ISO/IEC 25010); Transition;
  Phasing; Success criteria; Open questions; Terms; Appendix:
  traceability.

#### `user-stories.md`
- **Skeleton of:** the user stories, the layer below the BRD. See
  [The user stories](../about/the-user-stories.md).
- **Created by:** `/forge user-stories`.
- **Header:** `parent` is `30-brd.md` or `10-intent.md`. Stories from a
  source are a work product instead.
- **Body:** optional group headings without IDs; one story each,
  headed with its ID and the function name.
- **Parts of a story:** a free sentence (who or what, what is to
  happen, so that); the acceptance criteria, one behaviour each; then
  Edge cases, Risks, Note and Questions, each left out where the story
  has nothing for it; and Reference, the one part every story has.

#### `solution-design.md`
- **Skeleton of:** the solution design.
- **Created by:** `/forge solution-design`.
- **Sections:** How the parts work together; Parts (grouped, each item
  with what it realises, its choice and where it lives); Across the
  parts; Open.

#### `work.md`
- **Skeleton of:** the specification of a work product, the way and
  the why of a file that holds the content. See
  [The work product](../about/the-work-product.md).
- **Created by:** `/work`.
- **Header:** `file` names the file the specification makes.
- **Sections:** Task; Inputs; Method; Assumptions; Open; Making.

### Records and state

#### `ledger.md`
- **Skeleton of:** the ledger.
- **Created by:** `scripts/forge-ledger.py`, at read time.
- **Header:** `project`, `updated`.
- **Tables:** Briefs; Documents; Renders; Published; Work; Sources;
  Dependencies; Research; Findings; Challenges. Then the list Waiting
  on principal, and Reports where there is something to report. Each
  table's comment says which record or field each column is read from.
  A library keeps only Renders, Sources, Dependencies, Research and
  Waiting on principal.

#### `decisions.md`
- **Skeleton of:** the append-only record of the principal's decisions.
- **Created by:** `/new-project`, with the sample record removed.
- **Record:** a heading with the decision in one line; Decision;
  Reason; Verdict; Date.
- **Verdict line:** stands only where the decision rules on a finding
  or a challenge, one line per ID. Its forms are `rejected`,
  `parked until <what>` and `obsolete`.

#### `history.md`
- **Skeleton of:** the history companion of a versioned document.
- **Created by:** `/new-project` for the recipes it scaffolds, and with
  each versioned document at its birth.
- **Header:** `project`, `document`.
- **Record:** one line, appended at the end and never rewritten, of
  date, version, author, subject, kind, reason, Action and Was. The
  kinds are `created`, `changed`, `closed`, `removed` and `approved`.

#### `index.md`
- **Skeleton of:** the resource index of `sources/` and of `research/`.
- **Created by:** `/new-project` (header filled, no entries); entries by
  `/ingest` and `/research`.
- **Header:** `project`, `directory`.
- **Fields of a sources entry:** What, Origin, Date (from the content,
  the file or the ingest), Form (text, extract of an original, or
  binary), Role, Use for.
- **Fields of a research entry:** Question, Answer in short, Consult
  when.

#### `index-bundle.md`
- **Skeleton of:** the index of one bundle, `sources/<slug>/`.
- **Created by:** `/ingest`, at registration if missing.
- **Header:** `bundle`, `project`, `date`, `origin`.
- **Body:** one short paragraph saying what the bundle is, why it
  entered `sources/` and whether it arrived whole or grows; then one
  entry per file with the fields of a sources entry, in their order.

### Research

#### `research.md`
- **Skeleton of:** one research note, one card on one engine. In full:
  [Research note and bundle](research-bundle.md).
- **Created by:** `/research`.
- **Header:** `date`, `project`, `topic`, `status`, `engine`, `model`,
  `usage`, `run`, `derived_from`.
- **Sections:** In short; Question; Key findings; Unexpected; Not
  found; Options; Relevance to this project; Sources; Opened and not
  used; Search record.

#### `research-plan.md`
- **Skeleton of:** `00-plan.md`, the head of a research bundle: the
  plan as confirmed and the synthesis under it.
- **Created by:** `/research`.
- **Header:** `date`, `project`, `topic`, `status`, `engines`,
  `derived_from`.
- **Sections:** Summary; Plan (Purpose, Perspectives, Assumptions,
  Left out, Cards, Agents, The second engine's review of the draft);
  Deviations from the plan; Synthesis (Completeness card by card,
  Answers side by side, Unexpected gathered, Not found gathered,
  Claude's view); Notes.
- **Card:** Question, Why it matters, What would answer it, Where to
  look, Disconfirming query, Stop rule.

### Recipes

The skeleton of every recipe shares one header (`project`, `purpose`,
`audience`, `version`, and optionally `output` and `languages`) and
the sections Inputs, Instructions, Format (optional) and Template.

#### `recipe.md`
- **Skeleton of:** any recipe; it owns the shape only.
- **Created by:** `/recipe`.
- **Format section:** `Format` is `pptx`, `docx`, `video` or
  `html-player`; then the plain file made by `/render`, and the
  published file made by `/publish`.

#### `recipe-readme.md`
- **Skeleton of:** the README recipe, output at the project root.
- **Created by:** `/new-project`; iterated with `/recipe readme`.
- **Template sections:** What this project is; What you get; How to
  start; Where it stands; Documentation; About this README; a dated
  footer. The instructions carry a fixed closing sentence, which this
  page does not repeat.
- **Pinned facts (not rendered):** an optional section of facts that no
  file of the project owns yet, one bullet each. The README does not
  print them. The documentation's planner reads them as an owner of
  the fact. A bullet is dropped on the day a file owns the fact, and
  the section is omitted where the project has none.

#### `recipe-release-notes.md`
- **Skeleton of:** the release-notes recipe.
- **Created by:** `/new-project`; iterated with `/recipe release-notes`.
- **Template:** one section per release, newest first; groups Action
  required, Added, Changed, Removed, Fixed, Rejected; an approved
  major opens with highlights; earlier releases are carried over
  verbatim.

#### `recipe-presentation.md`
- **Skeleton of:** a deck recipe, source material for a presentation.
- **Created by:** `/recipe presentation`.
- **Template:** a table of slides (number, slide, content, diagram);
  each slide is rendered as On slide, Diagram, Speaker notes.

#### `recipe-screenplay.md`
- **Skeleton of:** a screenplay recipe, from which `scripts/md2video.py`
  makes a video or the events of the player page.
- **Created by:** `/recipe screenplay`.
- **Header:** adds `languages`, the first primary, the rest its
  translations.
- **Template:** a title card; a card of what the viewer will see; one
  scene per beat with its time of day, a caption of Now and Why, and a
  fenced block of what the terminal shows; an end card.

#### `recipe-user-stories-export.md`
- **Skeleton of:** the export of the stories, for a wiki or a tracker.
  See [The user stories](../about/the-user-stories.md).
- **Created by:** `/recipe user-stories-export`.
- **Template:** the heading "User stories", a section heading, the
  purpose line in italics, then the stories one after another with the
  parts of a story; no table, and every line unwrapped.

### The documentation and the videos

#### `docs-map.md`
- **Skeleton of:** the documentation map. The fields in full:
  [Documentation map](documentation-map.md).
- **Created by:** the planner of `/document`.
- **Header:** `target` (`engine` or a slug), `owner`.
- **Sections:** Paths (one line per reader); one section per section
  of the outline, each with one entry per page; Unowned; Did not fit.
- **Entry:** title, line, kind, reader, says, inputs, links, must-not,
  made, evidence (derived pages only), state.

#### `html-player.html`
- **Skeleton of:** the player page of the videos.
- **Created by:** `scripts/md2video.py` writes the served page
  `docs/videos/index.html` from it, replacing the placeholders for the
  list of the folder's player files and for one script tag per file.
- **Rule:** the served page is never edited; the skeleton is, and the
  script writes the page anew.

### Definitions

#### `artefact-definition.md`
- **Skeleton of:** the definition of a kind of artefact, a state file.
- **Created by:** `/new-artefact`.
- **Header:** `description`.
- **Blocks:** Target; Inputs; Aim; Partner; Map; Instruments; Course,
  and a closing paragraph on how the files are made. Every block is
  present; a block empty on purpose says so with the reason.

#### `critic-definition.md`
- **Skeleton of:** an agent file of a critic lens,
  `critic-<lens>.md`.
- **Created by:** the principal's decision to add a lens; the inputs
  name no command.
- **Fields:** `name`, `description`, `tools`, `model`, `skills`; then
  one Lens section.
- **Lens section:** what you read; what to go after; categories; own
  report sections.

#### `challenger-definition.md`
- **Skeleton of:** an agent file of a challenger persona,
  `challenger-<persona>.md`.
- **Created by:** the principal's decision to add a persona; the
  inputs name no command.
- **Fields:** as the critic's, with the tools Read, Glob, Grep,
  WebSearch and WebFetch.
- **Lens section:** who you are; what to go after.

#### `check-definition.md`
- **Skeleton of:** an agent file of a check, `check-<name>.md`.
- **Created by:** the principal's decision to add a check; the inputs
  name no command.
- **Fields:** as the critic's.
- **Lens section:** what you read; what you verify; cost.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [The user stories](../about/the-user-stories.md): the kind the stories' skeleton and the export skeleton serve.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
