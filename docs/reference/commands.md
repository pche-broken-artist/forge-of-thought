---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: b7458ad411a151d4
inputs:
  - CLAUDE.md#Commands
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
  - .claude/skills/history/SKILL.md
  - .claude/skills/check/SKILL.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/pull/SKILL.md
  - .claude/skills/end/SKILL.md
  - .claude/skills/spinoff/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Commands

This page lists every command of the forge with its signature, its purpose, its arguments and whether it is guarded. It is for the user, the extender and the evaluator who need the exact shape of a command at a glance.

A command is typed in the conversation with Claude (the assistant that works the forge for the principal, the person whose thinking is forged). A guarded command carries `disable-model-invocation: true` in its skill, which means Claude does not start it on its own judgement; the principal starts it. In a signature, `<x>` is an argument that must be given and `[x]` is one that may be left out. The slug is the short name of a project.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | first run after cloning the engine: prepare the instance | none | yes |
| `/new-project` | scaffold a project by kind: a thought project or a library | `<slug>` | yes |
| `/new-artefact` | add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project` | bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` | the state map of a project | `[slug]` | no |
| `/forge <state>` | iterate the target artefact through its definition | `[target-state] [project-slug]` | no |
| `/ingest` | store, register and index external input in sources/; bare = sweep sources/ | `[file-or-path] [project-slug]` | yes |
| `/render` | regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | make the designed file from a render, through a model | `<recipe> [project-slug]` | yes |
| `/document` | generate the documentation of the engine or of a project into docs/ | `[project-slug]` | yes |
| `/recipe` | compose or iterate a render recipe by genre; bare = the genre roster | `[genre-or-recipe] [project-slug]` | no |
| `/critique` | run a critic lens on the quality of the documents; bare = the lens roster | `[lens] [artefact] [project-slug]` | no |
| `/challenge` | run a challenger persona against the substance; bare = the persona roster | `[persona] [artefact] [project-slug]` | no |
| `/research` | best-practices research into research/, indexed | `<topic> [project-slug]` | no |
| `/ledger` | state report from the ledger | `[project-slug]` | no |
| `/history` | the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences | `<ID> [project-slug]` | no |
| `/check` | run a check on a project or on the engine; bare = the check roster | `[check] [project-slug]` | no |
| `/save` | save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/release` | release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull` | look at the remote and, clean and behind, pull one repository or every one with an origin; after a pull of the engine, the Action required lines crossed and the offer of the checks | `[project-slug]` | yes |
| `/end` | end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose | none | no |
| `/spinoff` | split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/man` | the forge's manual, read from its own definitions | `[command \| method]` | no |
| `/manual` | alias of `/man` | `[command \| method]` | no |

## The entries

Each entry gives the row of the Commands table of `CLAUDE.md`, the `description` and the `argument-hint` of the skill, and whether the skill carries `disable-model-invocation: true`. A command with no `argument-hint` takes no arguments.

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

### /forge (the state map)

- Signature: `/forge [slug]`
- Purpose: the state map of a project
- Description: Work the document chain - bare = state map, with a target = iterate that artefact
- Argument hint: `"[target-state] [project-slug]"`
- Guarded: no

### /forge (iterate an artefact)

- Signature: `/forge <state> [slug]`
- Purpose: iterate the target artefact through its definition
- Description: Work the document chain - bare = state map, with a target = iterate that artefact
- Argument hint: `"[target-state] [project-slug]"`
- Guarded: no

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
- Guarded: no

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare = the lens roster
- Description: Run a critic lens on the quality of a project's documents - bare = lens roster
- Argument hint: `"[lens] [artefact] [project-slug]"`
- Guarded: no

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare = the persona roster
- Description: Run a challenger persona against the substance of any chain artefact - bare = persona roster
- Argument hint: `"[persona] [artefact] [project-slug]"`
- Guarded: no

### /research

- Signature: `/research <topic> [slug]`
- Purpose: best-practices research into research/, indexed
- Description: Research current best practices on a topic; store durable notes
- Argument hint: `"<topic> [project-slug]"`
- Guarded: no

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger
- Description: Report project state from the ledger
- Argument hint: `"[project-slug]"`
- Guarded: no

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences
- Description: The history of one item by its ID - its wording today, its records, the archive rows that mention it and every citation, gathered by a script; Claude adds a few sentences of its own
- Argument hint: `"<ID> [project-slug]"`
- Guarded: no

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare = the check roster
- Description: Run a check on the conformance of a project or the engine with the conventions - bare = check roster
- Argument hint: `"[check] [project-slug]"`
- Guarded: no

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

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin; after a pull of the engine, the Action required lines crossed and the offer of the checks
- Description: Look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines crossed and the offer of the checks
- Argument hint: `"[project-slug]"`
- Guarded: yes

### /end

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose
- Description: End a session - what lives only in the conversation, what is unsaved, what a shutdown would lose
- Argument hint: none
- Guarded: no

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
- Guarded: no

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`
- Description: Alias of /man - the forge's manual, read from its own definitions
- Argument hint: `"[command | method]"`
- Guarded: no

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
