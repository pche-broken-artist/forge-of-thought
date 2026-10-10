---
generated: 2026-10-10
made: mirrored
inputs-hash: a7a872d85c3d427a
inputs:
  - CLAUDE.md
  - .claude/skills/setup/SKILL.md
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/new-artefact/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/critique/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/check/SKILL.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/spinoff/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Commands

This page lists every command of the forge, for anyone who uses it,
extends it or weighs it up. Each command has its signature and purpose
as the engine's core document gives them, then the description and
argument hint its skill carries, and whether it is guarded: a guarded
command is never started on Claude's own judgement, only when the
person types it.

In a signature, square brackets mark an optional argument and angle
brackets a required one. The slug is the short name of a project.

## The commands

| Command | Purpose |
|---|---|
| `/setup` | first run after cloning the engine: prepare the instance |
| `/new-project <slug>` | scaffold a project by kind: a thought project or a library |
| `/new-artefact <name>` | add a new kind of artefact to the forge |
| `/import-project <git-url>` | bring an existing project into `projects/` |
| `/forge [slug]` | the state map of a project |
| `/forge <state> [slug]` | iterate the target artefact through its definition |
| `/ingest [file] [slug]` | store, register and index external input in sources/; bare = sweep sources/ |
| `/render <recipe> [slug]` | regenerate a render from its recipe |
| `/publish <recipe> [slug]` | make the designed file from a render, through a model |
| `/document [slug]` | generate the documentation of the engine or of a project into docs/ |
| `/recipe [genre] [slug]` | compose or iterate a render recipe by genre; bare = the genre roster |
| `/critique [lens] [artefact] [slug]` | run a critic lens on the quality of the documents; bare = the lens roster |
| `/challenge [persona] [artefact] [slug]` | run a challenger persona against the substance; bare = the persona roster |
| `/research <topic> [slug]` | best-practices research into research/, indexed |
| `/ledger [slug]` | state report from the ledger |
| `/check [check] [slug]` | run a check on a project or on the engine; bare = the check roster |
| `/save [slug] [-m "message"] [--tag name]` | save one repository, or every one with changes |
| `/release [slug] [-m "message"] [--tag name]` | release one repository from `main` |
| `/spinoff <project> <group> <slug>` | split a group into its own project |
| `/man [command \| method]` | the forge's manual, read from its own definitions |
| `/manual …` | alias of `/man` |

## What each skill declares

"Guarded" means the skill sets `disable-model-invocation`.

### /setup

- Description: First run after cloning the engine - create and fill
  CLAUDE.local.md by interview, set the session model to the forge's
  default, offer the git identity per host and the global guard in
  ~/.gitconfig; never overwrites, runs no git operation
- Argument hint: none
- Guarded: yes

### /new-project

- Description: Scaffold a new project from templates - a thought
  project (the chain) or a library (material only); files only, never
  git
- Argument hint: `<slug>`
- Guarded: yes

### /new-artefact

- Description: Add a new kind of artefact to the forge - its position
  in the forge intent, its definition and template, its prefixes, its
  reviewers
- Argument hint: `<name>`
- Guarded: yes

### /import-project

- Description: Bring an existing project into projects/ - clone
  through scripts/forge-clone.py, which reports the commit identity
  git resolves
- Argument hint: `<git-url>`
- Guarded: yes

### /forge

- Description: Work the document chain - bare = state map, with a
  target = iterate that artefact
- Argument hint: `[target-state] [project-slug]`
- Guarded: no

### /ingest

- Description: Register external input (a file, or text pasted into
  the conversation) in sources/ - store, catalogue, ask what it is
  for, nothing more
- Argument hint: `[file-or-path] [project-slug]`
- Guarded: yes

### /render

- Description: Regenerate a render from its recipe in recipes/
- Argument hint: `<recipe> [project-slug]`
- Guarded: yes

### /publish

- Description: Make the designed .pptx or .docx from the render of a
  recipe, through a model - started by the principal only
- Argument hint: `<recipe> [project-slug]`
- Guarded: yes

### /document

- Description: Generate the documentation of the engine or of a
  project into docs/ - pages of one topic each and their index, from a
  map
- Argument hint: `[project-slug]`
- Guarded: yes

### /recipe

- Description: Compose a render recipe by genre - bare = genre roster,
  with a genre = guided composition
- Argument hint: `[genre-or-recipe] [project-slug]`
- Guarded: no

### /critique

- Description: Run a critic lens on the quality of a project's
  documents - bare = lens roster
- Argument hint: `[lens] [artefact] [project-slug]`
- Guarded: no

### /challenge

- Description: Run a challenger persona against the substance of any
  chain artefact - bare = persona roster
- Argument hint: `[persona] [artefact] [project-slug]`
- Guarded: no

### /research

- Description: Research current best practices on a topic; store
  durable notes
- Argument hint: `<topic> [project-slug]`
- Guarded: no

### /ledger

- Description: Report project state from the ledger
- Argument hint: `[project-slug]`
- Guarded: no

### /check

- Description: Run a check on the conformance of a project or the
  engine with the conventions - bare = check roster
- Argument hint: `[check] [project-slug]`
- Guarded: no

### /save

- Description: Save the forge to git - the light check, then commit
  and push; no renders
- Argument hint: `[project-slug] [-m "message"] [--tag name]`
- Guarded: yes

### /release

- Description: Release one repository from main - its checks with
  walkthrough, README and release notes, then /save with the release
  message and the tag at an approved major
- Argument hint: `[project-slug] [-m "message"] [--tag name]`
- Guarded: yes

### /spinoff

- Description: Spin a requirement group off into its own project
  (principal's explicit decision only)
- Argument hint: `<source-project> <group-name> <new-slug>`
- Guarded: yes

### /man

- Description: The forge's manual, read from its own definitions -
  bare = the commands and the working methods, with a command = its
  purpose, arguments and roster, with a method = its paragraph and
  skill
- Argument hint: `[command | method]`
- Guarded: no

### /manual

- Description: Alias of /man - the forge's manual, read from its own
  definitions
- Argument hint: `[command | method]`
- Guarded: no

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
