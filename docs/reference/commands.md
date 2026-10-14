---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: c43fb6e677685a09
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
  - .claude/skills/work/SKILL.md
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

This page lists every command of the forge with its signature, its purpose, its arguments and whether it is guarded. It is for the user, the extender and the evaluator who want the facts of a command in one place.

A command is guarded when its skill carries `disable-model-invocation: true`. Square brackets in a signature mark an optional argument, angle brackets a required one. The principal (the person whose thinking is forged) is the one who starts a guarded command; Claude does not start it on its own.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | First run after cloning the engine: prepare the instance | none | yes |
| `/new-project` | Scaffold a project by kind | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` | The state map of a project, or iterate one artefact | `[target-state] [project-slug]` | no |
| `/ingest` | Store, register and index external input in sources/ | `[file-or-path] [project-slug]` | yes |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed file from a render, through a model | `<recipe> [project-slug]` | yes |
| `/document` | Generate the documentation into docs/ | `[project-slug]` | yes |
| `/recipe` | Compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work` | Work a work product | `[name] [project-slug]` | no |
| `/critique` | Run a critic lens on the quality of the documents | `[lens] [artefact] [project-slug]` | no |
| `/challenge` | Run a challenger persona against the substance | `[persona] [artefact] [project-slug]` | no |
| `/research` | Best-practices research into research/, indexed | `<topic> [project-slug]` | no |
| `/ledger` | State report from the ledger | `[project-slug]` | no |
| `/history` | The history of one item | `<ID> [project-slug]` | no |
| `/check` | Run a check on a project or on the engine | `[check] [project-slug]` | no |
| `/save` | Save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull` | Look at the remote and pull what is clean and behind | `[project-slug]` | yes |
| `/end` | End a session | none | no |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/man` | The forge's manual, read from its own definitions | `[command \| method]` | no |
| `/manual` | Alias of `/man` | `[command \| method]` | no |

## The commands

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance.
- Description: first run after cloning the engine; creates and fills `CLAUDE.local.md` by interview, sets the session model to the forge's default, offers the git identity per host and the global guard in `~/.gitconfig`; never overwrites, runs no git operation.
- Argument hint: none.
- Guarded: yes.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a library.
- Description: scaffold a new project from templates, a thought project (the chain) or a library (material only); files only, never git.
- Argument hint: `<slug>`
- Guarded: yes.

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Description: add a new kind of artefact to the forge: its position in the forge intent, its definition and template, its prefixes, its reviewers.
- Argument hint: `<name>`
- Guarded: yes.

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Description: bring an existing project into `projects/` by cloning through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Argument hint: `<git-url>`
- Guarded: yes.

### /forge

- Signatures: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: with no state, the state map of a project; with a state, iterate the target artefact through its definition.
- Description: work the document chain; bare = state map, with a target = iterate that artefact.
- Argument hint: `[target-state] [project-slug]`
- Guarded: no.

### /ingest

- Signature: `/ingest [file] [slug]`
- Purpose: store, register and index external input in sources/; bare = sweep sources/.
- Description: register external input (a file, or text pasted into the conversation) in sources/; store, catalogue, ask what it is for, nothing more.
- Argument hint: `[file-or-path] [project-slug]`
- Guarded: yes.

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Description: regenerate a render from its recipe in recipes/.
- Argument hint: `<recipe> [project-slug]`
- Guarded: yes.

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Description: make the designed .pptx or .docx from the render of a recipe, through a model; started by the principal only.
- Argument hint: `<recipe> [project-slug]`
- Guarded: yes.

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into docs/.
- Description: generate the documentation of the engine or of a project into docs/, pages of one topic each and their index, from a map.
- Argument hint: `[project-slug]`
- Guarded: yes.

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare = the genre roster.
- Description: compose a render recipe by genre; bare = genre roster, with a genre = guided composition.
- Argument hint: `[genre-or-recipe] [project-slug]`
- Guarded: no.

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product: its specification and its file; bare = the project's work products.
- Description: work a work product; bare = the roster of the project's work products, with a name = iterate its specification and make its file.
- Argument hint: `[name] [project-slug]`
- Guarded: no.

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare = the lens roster.
- Description: run a critic lens on the quality of a project's documents; bare = lens roster.
- Argument hint: `[lens] [artefact] [project-slug]`
- Guarded: no.

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare = the persona roster.
- Description: run a challenger persona against the substance of any chain artefact; bare = persona roster.
- Argument hint: `[persona] [artefact] [project-slug]`
- Guarded: no.

### /research

- Signature: `/research <topic> [slug]`
- Purpose: best-practices research into research/, indexed.
- Description: research current best practices on a topic; store durable notes.
- Argument hint: `<topic> [project-slug]`
- Guarded: no.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger.
- Description: report project state from the ledger.
- Argument hint: `[project-slug]`
- Guarded: no.

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Description: the history of one item by its ID: its wording today, its records, the archive rows that mention it and every citation, gathered by a script; Claude adds a few sentences of its own.
- Argument hint: `<ID> [project-slug]`
- Guarded: no.

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare = the check roster.
- Description: run a check on the conformance of a project or the engine with the conventions; bare = check roster.
- Argument hint: `[check] [project-slug]`
- Guarded: no.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name]`
- Purpose: save one repository, or every one with changes.
- Description: save the forge to git: the light check, then commit and push; no renders.
- Argument hint: `[project-slug] [-m "message"] [--tag name]`
- Guarded: yes.

### /release

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`.
- Description: release one repository from main: its checks with walkthrough, README and release notes, then `/save` with the release message and the tag at an approved major.
- Argument hint: `[project-slug] [-m "message"] [--tag name]`
- Guarded: yes.

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin; after a pull of the engine, the Action required lines crossed and the offer of the checks.
- Description: look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines crossed and the offer of the checks.
- Argument hint: `[project-slug]`
- Guarded: yes.

### /end

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Description: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Argument hint: none.
- Guarded: no.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Description: spin a requirement group off into its own project (the principal's explicit decision only).
- Argument hint: `<source-project> <group-name> <new-slug>`
- Guarded: yes.

### /man

- Signature: `/man [command | method]`
- Purpose: the forge's manual, read from its own definitions.
- Description: the forge's manual, read from its own definitions; bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill.
- Argument hint: `[command | method]`
- Guarded: no.

### /manual

- Signature: `/manual ...`
- Purpose: alias of `/man`.
- Description: alias of `/man`: the forge's manual, read from its own definitions.
- Argument hint: `[command | method]`
- Guarded: no.

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
