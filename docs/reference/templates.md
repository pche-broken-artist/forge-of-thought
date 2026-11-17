---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f249fe97489b956a
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

A template is a skeleton in `templates/`: the shape a file of the
forge is made from. This page is for the extender, the person who adds
to the forge, and lists every skeleton, what it is the skeleton of,
which procedure creates from it where its own comment or the
new-project skill says so, and its fields or sections in one line. For
where templates sit among the parts of the forge, see
[What the forge is made of](../extend/what-it-is-made-of.md); for the
terms used here, see the [Glossary](glossary.md). The principal is the
person whose thinking is being forged.

## Overview

| Template | What it is for | When it fits | Where it lives |
|---|---|---|---|
| CLAUDE.local.md | the instance facts of one installation | on a new installation | `templates/CLAUDE.local.md`, made into `CLAUDE.local.md` at the engine root |
| project.md | the project file: slug, kind, language | at the creation of a project | `templates/project.md`, made into `project.md` |
| gitattributes | the ways of merging by path | every project | `templates/gitattributes`, copied to `.gitattributes` |
| gitignore | what never enters git | every project | `templates/gitignore`, copied to `.gitignore` |
| brief.md | a brief | a project's ask | `templates/brief.md`, made into `00-brief.md` |
| intent.md | the intent | the trunk of every project | `templates/intent.md`, made into `10-intent.md` |
| thread.md | one thread | a matter set aside to be taken up later | `templates/thread.md`, made into `threads/<id>.md` |
| assignment.md | the assignment | a project that hands work to recipients | `templates/assignment.md`, made into `20-assignment.md` |
| brd.md | the business requirements document | a project that takes the layer | `templates/brd.md`, made into `30-brd.md` |
| user-stories.md | the user stories | a project that takes the layer | `templates/user-stories.md`, made into `35-user-stories.md` |
| solution-design.md | the solution design | how the things wanted are realised | `templates/solution-design.md` |
| work.md | a work specification | a work product | `templates/work.md`, made into `work/<name>.spec.md` |
| ledger.md | the shape of the ledger | made at read time | `templates/ledger.md`, made into `ledger.md` |
| decisions.md | the record of decisions | every thought project | `templates/decisions.md`, made into `decisions.md` |
| history.md | the history companion of a versioned document | every versioned document | `templates/history.md`, made into `<file>.history.md` |
| index.md | a resource index | `sources/` and `research/` | `templates/index.md`, made into `00-INDEX.md` |
| index-bundle.md | the index of one bundle of sources | a bundle in `sources/<slug>/` | `templates/index-bundle.md` |
| research.md | one research note | one card, one engine | `templates/research.md` |
| research-plan.md | the head of a research bundle | a research of several questions | `templates/research-plan.md`, made into `00-plan.md` |
| recipe.md | the base recipe | any render | `templates/recipe.md`, made into `recipes/<recipe>.md` |
| recipe-readme.md | the readme recipe | every project | `templates/recipe-readme.md`, made into `recipes/readme.md` |
| recipe-release-notes.md | the release-notes recipe | a thought project | `templates/recipe-release-notes.md`, made into `recipes/release-notes.md` |
| recipe-presentation.md | the presentation recipe | a deck's source material | `templates/recipe-presentation.md` |
| recipe-screenplay.md | the screenplay recipe | a video or a player page | `templates/recipe-screenplay.md` |
| recipe-user-stories-export.md | the recipe that exports the stories | stories pasted into a wiki or a tracker | `templates/recipe-user-stories-export.md` |
| html-player.html | the player page | the engine's folder of videos | `templates/html-player.html`, written by a script to `docs/videos/index.html` |
| docs-map.md | the documentation map | a documentation run | `templates/docs-map.md`, made into `docs-map.md` |
| artefact-definition.md | the definition of a kind of artefact | a new kind of artefact | `templates/artefact-definition.md` |
| critic-definition.md | a critic lens | a new lens | `templates/critic-definition.md`, made into `.claude/agents/critic-<lens>.md` |
| challenger-definition.md | a challenger persona | a new persona | `templates/challenger-definition.md`, made into `.claude/agents/challenger-<persona>.md` |
| check-definition.md | a check | a new check | `templates/check-definition.md`, made into `.claude/agents/check-<name>.md` |

## Rules that hold for every template

- A skeleton named `<type>-definition.md` is the skeleton of the
  definition of one member of a type the forge can be extended by.
  The types are an artefact, a critic lens, a challenger persona and a
  check.
- A file made from a skeleton keeps of its comments the one line that
  names it, `<!-- Shape: templates/<name>.md -->`, where the skeleton
  has it, and none of the others.
- Not every skeleton carries that line. The entries below say which do
  not: the two git templates, `CLAUDE.local.md`, the ledger, the player
  page, the documentation map and the four definition skeletons.
- Why a file keeps only that line, and what holds for a file made
  before the rule, is on
  [Upgrades and migration](../about/upgrades-and-migration.md).

## The templates

### CLAUDE.local.md

- Skeleton of: the instance facts file, `CLAUDE.local.md`, at the
  engine root.
- Created by: no procedure is named in the skeleton.
- Fields: Principal (the role whose thinking is forged), Conversation
  language, Author (the principal's short handle, the author of every
  record he decides).
- Names itself: no.

### project.md

- Skeleton of: the project file.
- Created by: `/new-project` or the migration, once, never by a round
  of work. It is merged as text and read wherever the kind and the
  language of a project are needed.
- Fields: `project` (the slug), `kind` (`thought` or `library`),
  `language` (ISO 639-1, the language of the chain's artefacts).
- A fixture project carries `fixture: true`.
- A project without the file is of the shape before the migration. The
  one remedy is `/migrate`. A command reports the shape as a fact, a
  check as one finding with that fix, and nothing else of the new shape
  is raised against the project.
- Names itself: yes.

### gitattributes

- Skeleton of: a project's `.gitattributes`, the ways of merging by
  path. It is copied by `/new-project`.
- Contents: line endings normalised for all files (`* text=auto`);
  derived files taken as ours at a merge and made again (`renders/**`,
  `docs/**`, `published/*.md`, and three root files); the published
  `.pptx` and `.docx` files binary, never merged.
- The three root files, `/README.md`, `/RELEASE-NOTES.md` and
  `/CONTRIBUTING.md`, are anchored with a leading slash. A bare name
  matches at every depth and, with `core.ignorecase`, in every case, so
  a file such as `recipes/readme.md` would match.
- Names itself: no.

### gitignore

- Skeleton of: a project's `.gitignore`. It is copied by `/new-project`
  as it stands.
- Contents: `ledger.md`, which is made at read time and never in git,
  and `~$*`, the lock files of an open Office document (Word,
  PowerPoint, Excel).
- Names itself: no.

### brief.md

- Skeleton of: the brief, `00-brief.md`; later briefs are
  `00-brief-<name>.md`.
- Created by: `/forge brief`, to which `/new-project` hands over.
- Fields: `project`, `title`, `author`, `version` (0.1), `status`
  (draft). Only the header is fixed; the text below it is free-form.
- Names itself: yes.

### intent.md

- Skeleton of: the intent, `10-intent.md`.
- Created by: no procedure is named in the skeleton; its definition is
  `.claude/skills/forge/states/intent.md`.
- Header: `version`, `status`, `project`, `audience`.
- Sections: Essence, Positions, Facts, Rejected directions, and the
  optional Candidate structure for the layer below. Positions, facts and
  rejected directions are items with IDs.
- Names itself: yes.

### thread.md

- Skeleton of: one thread, a matter of a project set aside to be taken
  up later; one file per thread in `threads/`.
- Created by: the rules of a thread, its birth, upkeep, life and
  closing, are in `.claude/skills/thread/SKILL.md`.
- Header:
  - `id`: the thread's number.
  - `concerns`: an artefact as `/forge` names it, or another document by
    path; several, comma-separated.
  - `origin`: the principal (the default), a document by path, or
    Claude's synthesis.
  - `owner`: the handle of whoever opened it; changed when the thread is
    handed over.
  - `priority`: high, medium or low.
  - `blocks`: what waits on it, only where something does.
  - `status`: open or closed.
- Body, three parts:
  - The opening paragraph: the matter in one whole sentence, the
    situation, what is to be settled and what will close the thread,
    Claude's view where he has one, and the date it was opened.
  - A dated continuation, one paragraph each time the thread is taken
    up.
  - A dated closing paragraph: how the matter ended and where what was
    decided now stands.
- Names itself: yes.

### assignment.md

- Skeleton of: the assignment, `20-assignment.md`.
- Created by: no procedure is named in the skeleton; its definition is
  `.claude/skills/forge/states/assignment.md`.
- Header: `version`, `status`, `project`, `audience` (recipients).
- Sections: Purpose & Context, Objective, Scope (in scope, out of
  scope), Requirements (grouped), Constraints, Assumptions,
  Deliverables, Open Questions, Success Criteria, Terms. Constraints,
  Assumptions and Success Criteria are deleted where empty.
- Names itself: yes.

### brd.md

- Skeleton of: the business requirements document, `30-brd.md`.
- Created by: no procedure is named in the skeleton; its definition is
  `.claude/skills/forge/states/brd.md`.
- Header: `version`, `status`, `project`, and `parent:`, either
  `20-assignment.md` or `10-intent.md`. A BRD made from a source is a
  work product instead.
- Sections: Purpose & Context, Objective, Stakeholders (roles, never
  names), Scope, Dependencies, Assumptions, Use cases (actor, trigger,
  preconditions, success outcome, minimal guarantee, steps,
  exceptions), Business requirements (grouped), Touched areas of the
  enterprise, Qualities, Transition, Phasing, Success criteria, Open
  questions, Terms, and the Appendix: traceability.
- Qualities lists one quality item per category that applies. The
  categories are those of ISO/IEC 25010 and the practice of a
  regulated business; categories found not to apply are deleted with
  the reason.
- No value in the skeleton stands as a requirement.
- Names itself: yes.

### user-stories.md

- Skeleton of: the user stories, `35-user-stories.md`.
- Created by: no procedure is named in the skeleton; its definition is
  `.claude/skills/forge/states/user-stories.md`. For the kind, see
  [The user stories](../about/the-user-stories.md).
- Header: `version`, `status`, `project`, and `parent:`, either
  `30-brd.md` or `10-intent.md` (a small change, on the principal's
  word). Stories made from a source are a work product instead.
- Document: the stories only, in optional groups that are plain
  headings without IDs.
- The parts of a story:
  - A heading with the story's number and the function name.
  - One free sentence: who or what, what is to happen, so that.
  - Acceptance criteria, one behaviour each.
  - Edge cases: situation, then what happens.
  - Risks: risk, then mitigation or consequences.
  - Note: what lies behind the link, with the link.
  - Questions: numbered, each with its owner.
  - Reference: business requirements, non-functional requirements, use
    cases, dependencies, or a position of the intent.
- Which parts a story has and which it leaves out is decided by the
  Story style of its definition.
- Names itself: yes.

### recipe-user-stories-export.md

- Skeleton of: the recipe that exports the stories. The skeleton's
  comment says it is iterated through `/recipe user-stories-export`. For
  the kind it serves, see
  [The user stories](../about/the-user-stories.md).
- Header: `project`, `purpose`, `audience` (the stakeholders who
  approve, the delivery that builds and the testers), `version`.
- Input: `35-user-stories.md`.
- The Template reproduces the stories without a table and without
  group headings. A story that has no Reference part after leaving out
  the intent's positions has none in the export.
- No line is hard-wrapped, because the export is pasted into a wiki or
  a tracker that may break a wrapped line where it stands.
- Names itself: yes.

### solution-design.md

- Skeleton of: the solution design.
- Created by: no procedure is named in the skeleton; its definition is
  `.claude/skills/forge/states/solution-design.md`.
- Header: `version`, `status`, `project`, `audience`.
- Sections: How the parts work together, Parts (items grouped, each
  with what it realises, the choice made against what and at what
  cost, and where it lives), Across the parts, Open.
- Names itself: yes.

### work.md

- Skeleton of: a work specification, the way and the why of a work
  product; the file beside it holds the content. For the kind, see
  [The work product](../about/the-work-product.md).
- Created by: the work command, `.claude/skills/work/SKILL.md`.
- Header: `version`, `status`, `project`, `file` (the file the
  specification makes, `work/<name>.<ext>`).
- Sections: Task, Inputs (items by ID and files by path, never
  copied), Method, Assumptions, Open, Making. Assumptions and Open are
  deleted where empty; their numbers continue the project's next free
  ones, after every specification it already has.
- Names itself: yes.

### ledger.md

- Skeleton of: the ledger, the single source of truth for state.
- Created by: `scripts/forge-ledger.py`, at read time. The ledger is
  never in git, and the script keeps the skeleton's comments.
- Header: `project`, `updated`.
- Sections, each a table:
  - Briefs: file, version, status, mined, note.
  - Documents: file, version, status, date.
  - Renders: render, audience, recipe, inputs, generated.
  - Published: file, recipe, from render, model, published, state.
  - Work: file, specification, inputs, made, state.
  - Sources: file, date, date origin, form.
  - Dependencies: path, library, used by, note.
  - Research: file, date, derived from.
  - Findings: ID, severity, category, state, source review,
    resolution.
  - Challenges: ID, state, headline, source review, resolution.
  - Waiting on principal: one line per matter.
  - Reports: only where there is something to report.
- A project of kind `thought` keeps every table. A project of kind
  `library` keeps only Renders, Sources, Dependencies, Research and
  Waiting on principal; the Findings table returns with a check's first
  finding.
- Names itself: no.

### decisions.md

- Skeleton of: the record of the principal's decisions, `decisions.md`.
- Created by: `/new-project`, with the slug filled and the sample
  record removed.
- Header: `project`. The file is append-only.
- A record has a heading with the decision's number and a one-line
  statement, then Decision, Reason, Verdict and Date.
- Verdict line: `<ID> rejected | parked until <what> | obsolete`. It
  stands only where the decision rules on a finding or a challenge, one
  line per ID.
- Names itself: yes.

### history.md

- Skeleton of: the history companion of a versioned document,
  `<file>.history.md`. `/new-project` makes the first records of the
  readme and release-notes recipes from it.
- Header: `project`, `document` (the versioned document it belongs to).
- A record is one line, appended at the end and never rewritten:
  `date | version | author | subject | kind | reason | Action | Was`.
- Kinds: created, changed, closed, removed, approved. The reason is left
  out on `created`; `Action` and `Was` stand only where the record has
  them, `Was` always last.
- Names itself: yes.

### index.md

- Skeleton of: a resource index, `00-INDEX.md`, of `sources/` and of
  `research/`. `/ingest` writes the sources entries and `/research` the
  research entries; `/new-project` makes the files with the header
  filled and no entries.
- Header: `project`, `directory` (`sources` or `research`).
- A sources entry is a file or a bundle with: What, Origin, Date (from
  the content, the file or the ingest; best effort, never asked), Form
  (text, extract of an original, or binary; one form per source), Role,
  Use for.
- A research entry is a note with: Question, Answer in short, Consult
  when.
- A bundle is one entry that points to its own index.
- Names itself: yes.

### index-bundle.md

- Skeleton of: the index of one bundle of sources, `sources/<slug>/`.
  The rules of a bundle are in `.claude/skills/ingest/SKILL.md`.
- Header: `bundle`, `project`, `date`, `origin`.
- Body: one short paragraph saying what the bundle is, why it entered
  `sources/`, and whether it arrived whole or grows; then one entry per
  file with the fields of a sources entry of `index.md`, in its order.
- Names itself: yes.

### research.md

- Skeleton of: one research note, one card on one engine, written in
  English and immutable from its filing. For the note and the bundle in
  full, see [Research note and bundle](research-bundle.md).
- Created by: `/research`, through the agent's brief in
  `.claude/skills/research/SKILL.md`.
- Header: `date`, `project`, `topic`, `status`, `engine`, `model`,
  `usage`, `run`, `derived_from`.
- Sections: In short, Question, Key findings, Unexpected, Not found,
  Options, Relevance to this project, Sources, Opened and not used,
  Search record. Options is left out where the card asked for a fact.
- Names itself: yes.

### research-plan.md

- Skeleton of: the head of a research bundle,
  `research/<date>-<topic>/00-plan.md`: the confirmed plan and, under
  it, the synthesis. For the bundle in full, see
  [Research note and bundle](research-bundle.md).
- Created by: `/research`, as `.claude/skills/research/SKILL.md` says.
- Header: `date`, `project`, `topic`, `status`, `engines`,
  `derived_from`. The status is `draft` from the plan's confirmation and
  `immutable` from the synthesis's filing.
- Sections: Summary, Plan (Purpose, Perspectives, Assumptions, Left
  out, Cards, Agents, the second engine's review of the draft),
  Deviations from the plan, Synthesis (completeness card by card,
  answers side by side, unexpected gathered, not found gathered,
  Claude's view), Notes.
- A card has: Question, Why it matters, What would answer it, Where to
  look, Disconfirming query, Stop rule.
- Names itself: yes.

### recipe.md

- Skeleton of: the base recipe, `recipes/<recipe>.md`.
- Header: `project`, `purpose`, `audience`, `version`; optional
  `output` (a path read relative to the project root, a leading slash
  meaning the engine root) and optional `languages` (the first is
  primary, the rest its translations, one render per language).
- Sections: Inputs (artefacts by path, one per line), Instructions,
  Format (optional), Template (the literal skeleton of the render,
  always Markdown).
- The Format section is never copied into the render. It names the
  format, one of `pptx`, `docx`, `video`, `html-player` or `png`, and
  two files:
  - The plain file, made by `/render` through pandoc, with a reference
    document and a page size (A4 or Letter). A `video` or `html-player`
    is made through `scripts/md2video.py` instead and has no published
    file. A `png` is drawn by the renderer itself, with the width in
    pixels stated, and has no plain file through a script and no
    published file.
  - The published file, made by `/publish` through a model, with a
    template, the model and anything else it must know.
- Names itself: yes.

### recipe-readme.md

- Skeleton of: the readme recipe, `recipes/readme.md`, whose output is
  the project's `README.md`. `/new-project` makes it, with the slug and
  date filled and its comments kept for the first `/recipe` iteration;
  in a library it takes the ledger and the two indexes as inputs.
- Header: `project`, `purpose`, `audience`, `version`, `output`.
- Sections: Inputs, Instructions, Pinned facts (not rendered), Template.
- Pinned facts (not rendered) is optional. It holds facts of the project
  that no file owns yet, such as prerequisites, how a tool is installed
  or the public home of the repository, one bullet each. The README does
  not print them; the documentation's planner reads them there as an
  owner. A bullet is dropped the day a file owns the fact.
- The Template sections: What this project is, What you get, How to
  start, Where it stands, Documentation, About this README, and a dated
  footer.
- Names itself: yes.

### recipe-release-notes.md

- Skeleton of: the release-notes recipe, `recipes/release-notes.md`,
  whose output is `RELEASE-NOTES.md`. `/new-project` makes it like the
  readme recipe. Every `/release` of the project renders it.
- Header: `project`, `purpose`, `audience`, `version`, `output`.
- Sections: Inputs (the histories of the intent and of each layer
  below it, their archives, the intent, the decisions and the previous
  edition), Instructions, Template.
- The Template: one section per release, newest first, with the groups
  Action required, Added, Changed, Removed, Fixed and Rejected; an
  approved major version carries highlights and folds the minors since
  the previous major into it.
- Names itself: yes.

### recipe-presentation.md

- Skeleton of: the presentation recipe. The skeleton's comment says it
  is composed through `/recipe presentation`; the render is a
  slide-by-slide deck definition from which `/render` makes a plain
  PowerPoint file and `/publish` the designed one.
- Header: `project`, `purpose`, `audience`, `version`, optional
  `output`.
- Sections: Inputs, Instructions, Format (`pptx`), Template.
- Each slide in the render: a heading, On slide, Diagram (only where
  the Template assigns one, a Mermaid block or a reference to a render
  of the project declared in Inputs) and Speaker notes. The Template is
  a table of slide, content and diagram.
- Names itself: yes.

### recipe-screenplay.md

- Skeleton of: the screenplay recipe. The skeleton's comment says it is
  composed through `/recipe screenplay`; the render is a screenplay from
  which `scripts/md2video.py` makes the video or the events of the
  player page.
- Header: `project`, `purpose`, `audience`, `version`, `languages`, and
  an optional `output` for the `html-player` format, which points into
  the engine's public folder of videos.
- Sections: Inputs, Instructions, Format (`video` or `html-player`,
  never both), Template.
- The Template: a title card, a card of what the viewer will see, one
  scene per beat and an end card. A scene has a real time of day, a
  caption of two parts (Now and Why) and a fenced block of what the
  terminal shows.
- Names itself: yes.

### html-player.html

- Skeleton of: the player page, from which `scripts/md2video.py` writes
  the served page `docs/videos/index.html`. The script replaces one
  placeholder with the list of the folder's `html-player` files and
  another with a script tag per file.
- The served page is never edited. The skeleton is edited and the
  script writes the page anew.
- Names itself: no.

### docs-map.md

- Skeleton of: the documentation map, `docs-map.md`. For its fields in
  full, see [Documentation map](documentation-map.md).
- Created by: the planner agent of `/document`.
- Header: `target` (`engine` or a project slug), `owner`.
- Sections: Paths (the pages of each reader: user, extender,
  evaluator), then one section per section of the outline in the
  outline's order (start, use, about, extend, reference), Unowned and
  Did not fit.
- A page entry has: title, line, kind, reader, says, inputs, links,
  must-not, made, evidence (derived pages only) and state (`new`,
  `keep`, `regenerate` or `remove`).
- Names itself: no.

### artefact-definition.md

- Skeleton of: the definition of a kind of artefact.
- Created by: `/new-artefact`, as the skeleton's comment says.
- Front-matter: `description`.
- Blocks, every one present, one left empty on purpose says so with its
  reason: Target, Inputs, Aim, Partner, Map, Instruments, Course.
- Names itself: no.

### critic-definition.md

- Skeleton of: a critic lens file, `.claude/agents/critic-<lens>.md`.
- Created by: no procedure is named in the skeleton.
- Front-matter: `name`, `description`, `tools` (Read, Glob, Grep),
  `model` (inherit), `skills` (the critic contract).
- The file holds front-matter and one section, Lens, in four parts: what
  you read, what to go after, categories, own report sections.
- Where a description carries a colon followed by a space, the whole
  description goes in single quotes, an apostrophe inside doubled, or
  the agent does not register.
- Names itself: no.

### challenger-definition.md

- Skeleton of: a challenger persona file,
  `.claude/agents/challenger-<persona>.md`.
- Created by: no procedure is named in the skeleton.
- Front-matter: `name`, `description`, `tools` (Read, Glob, Grep,
  WebSearch, WebFetch), `model` (inherit), `skills` (the challenger
  contract).
- The file holds front-matter and one section, Lens, in two parts: who
  you are (a role of its own, never a mirror of the principal) and what
  to go after.
- The quoting of a description with a colon followed by a space is the
  same as for a critic lens.
- Names itself: no.

### check-definition.md

- Skeleton of: a check file, `.claude/agents/check-<name>.md`.
- Created by: no procedure is named in the skeleton.
- Front-matter: `name`, `description`, `tools` (Read, Glob, Grep),
  `model` (inherit), `skills` (the check contract).
- The file holds front-matter and one section, Lens, in three parts:
  what you read, what you verify (each rule with its owner cited and
  never restated) and cost.
- The quoting of a description with a colon followed by a space is the
  same as for a critic lens.
- Names itself: no.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): where the templates sit in the whole.
- [Documentation map](documentation-map.md): the map's fields in full.
- [Research note and bundle](research-bundle.md): the research note and plan in full.
- [The work product](../about/the-work-product.md): the kind the work skeleton serves.
- [The user stories](../about/the-user-stories.md): the kind the stories' skeleton and the export skeleton serve.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a file keeps only the line that names its template, and what holds for a file made before that rule.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
