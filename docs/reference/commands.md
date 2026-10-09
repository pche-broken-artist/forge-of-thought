---
generated: 2026-10-09
made: mirrored
inputs-hash: 132800c3993cec04
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

This page lists every command of the forge, in the order the Commands
table of `CLAUDE.md` gives them, for the person who uses the forge, the
one who extends it and the one who judges it. Each command has its
signature and purpose from that table, then the `description` and
`argument-hint` of its skill, and whether it is guarded against being
started on Claude's own judgement.

In the signatures, `<x>` is an argument that is required and `[x]` one
that is optional. What a command does in full is its skill's, in
`.claude/skills/<command>/SKILL.md`.

## Guarded commands

A command marked "guarded" carries `disable-model-invocation` in its
skill: it runs only when the person types it. A command marked "open"
does not carry it.

## The commands

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance
- Description: First run after cloning the engine - create and fill CLAUDE.local.md by interview, set the session model to the forge's default, offer the git identity per host and the global guard in ~/.gitconfig; never overwrites, runs no git operation
- Argument hint: none
- Guarded: yes

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a library
- Description: Scaffold a new project from templates - a thought project (the chain) or a library (material only); files only, never git
- Argument hint: `"<slug>"`
- Guarded: yes

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge
- Description: Add a new kind of artefact to the forge - its position in the forge intent, its definition and template, its prefixes, its reviewers
- Argument hint: `"<name>"`
- Guarded: yes

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`
- Description: Bring an existing project into projects/ - clone through scripts/forge-clone.py, which reports the commit identity git resolves
- Argument hint: `"<git-url>"`
- Guarded: yes

### /forge (state map)

- Signature: `/forge [slug]`
- Purpose: the state map of a project
- Description: Work the document chain - bare = state map, with a target = iterate that artefact
- Argument hint: `"[target-state] [project-slug]"`
- Guarded: open

### /forge (iterate)

- Signature: `/forge <state> [slug]`
- Purpose: iterate the target artefact through its definition
- Description: the same skill as above
- Argument hint: the same as above
- Guarded: open

### /ingest

- Signature: `/ingest [file] [slug]`
- Purpose: store, register and index external input in sources/; bare = sweep sources/
- Description: Register external input (a file, or text pasted into the conversation) in sources/ - store, catalogue, ask what it is for, nothing more
- Argument hint: `"[file-or-path] [project-slug]"`
- Guarded: yes

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe
- Description: Regenerate a render from its recipe in recipes/
- Argument hint: `"<recipe> [project-slug]"`
- Guarded: yes

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model
- Description: Make the designed .pptx or .docx from the render of a recipe, through a model - started by the principal only
- Argument hint: `"<recipe> [project-slug]"`
- Guarded: yes

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into docs/
- Description: Generate the documentation of the engine or of a project into docs/ - pages of one topic each and their index, from a map
- Argument hint: `"[project-slug]"`
- Guarded: yes

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare = the genre roster
- Description: Compose a render recipe by genre - bare = genre roster, with a genre = guided composition
- Argument hint: `"[genre-or-recipe] [project-slug]"`
- Guarded: open

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare = the lens roster
- Description: Run a critic lens on the quality of a project's documents - bare = lens roster
- Argument hint: `"[lens] [artefact] [project-slug]"`
- Guarded: open

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare = the persona roster
- Description: Run a challenger persona against the substance of any chain artefact - bare = persona roster
- Argument hint: `"[persona] [artefact] [project-slug]"`
- Guarded: open

### /research

- Signature: `/research <topic> [slug]`
- Purpose: best-practices research into research/, indexed
- Description: Research current best practices on a topic; store durable notes
- Argument hint: `"<topic> [project-slug]"`
- Guarded: open

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger
- Description: Report project state from the ledger
- Argument hint: `"[project-slug]"`
- Guarded: open

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare = the check roster
- Description: Run a check on the conformance of a project or the engine with the conventions - bare = check roster
- Argument hint: `"[check] [project-slug]"`
- Guarded: open

### /save

- Signature: `/save [slug] [-m "message"] [--tag name]`
- Purpose: save one repository, or every one with changes
- Description: Save the forge to git - the light check, then commit and push; no renders
- Argument hint: `'[project-slug] [-m "message"] [--tag name]'`
- Guarded: yes

### /release

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`
- Description: Release one repository from main - its checks with walkthrough, README and release notes, then /save with the release message and the tag at an approved major
- Argument hint: `'[project-slug] [-m "message"] [--tag name]'`
- Guarded: yes

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project
- Description: Spin a requirement group off into its own project (principal's explicit decision only)
- Argument hint: `"<source-project> <group-name> <new-slug>"`
- Guarded: yes

### /man

- Signature: `/man [command | method]`
- Purpose: the forge's manual, read from its own definitions
- Description: The forge's manual, read from its own definitions - bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill
- Argument hint: `"[command | method]"`
- Guarded: open

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`
- Description: Alias of /man - the forge's manual, read from its own definitions
- Argument hint: `"[command | method]"`
- Guarded: open

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
