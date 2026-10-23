---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 1b1e46174c025c9b
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
  - .claude/skills/migrate/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Commands

This page lists every command of the forge with its signature, purpose, arguments and whether it is guarded. It is for the user, the extender and the evaluator who need the exact form of a command. Each command is a skill in `.claude/skills/<command>/SKILL.md`, and the entries follow the order of the Commands table in `CLAUDE.md`.

A command is guarded when its skill carries `disable-model-invocation: true`. Claude does not start a guarded command on its own judgement. The principal (the person whose thinking is forged) starts it. A command that is not guarded may also be started by Claude.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | Prepare the instance after cloning the engine | none | yes |
| `/new-project` | Scaffold a project by kind | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` (bare) | The state map of a project | `[target-state] [project-slug]` | no |
| `/forge <state>` | Iterate the target artefact through its definition | `[target-state] [project-slug]` | no |
| `/ingest` | Register external input in `sources/` | `[file-or-path] [project-slug] [--bundle name]` | yes |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed file from a render | `<recipe> [project-slug]` | yes |
| `/document` | Generate the documentation into `docs/` | `[project-slug]` | yes |
| `/recipe` | Compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work` | Work a work product | `[name] [project-slug]` | no |
| `/critique` | Run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | no |
| `/challenge` | Run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | no |
| `/research` | Best-practices research into `research/` | `<topic> [project-slug]` | no |
| `/ledger` | State report from the ledger | `[project-slug]` | no |
| `/history` | The history of one item | `<ID> [project-slug]` | no |
| `/check` | Run a check on a project or on the engine | `[check] [project-slug]` | no |
| `/save` | Save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | yes |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull` | Look at the remote and pull what is clean and behind | `[project-slug]` | yes |
| `/end` | End a session | none | no |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/migrate` | Bring a project to the shape of a release | `[project-slug]` | yes |
| `/man` | The forge's manual | `[command \| method]` | no |
| `/manual` | Alias of `/man` | `[command \| method]` | no |

## The entries

Each entry gives the signature and purpose as the Commands table of `CLAUDE.md` states them, the description and argument hint of the skill, and whether the command is guarded.

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance.
- Description: first run after cloning the engine - create and fill `CLAUDE.local.md` by interview, set the session model to the forge's default, offer the git identity per host, the global guard and the registration of the merge driver `ours`, written through `scripts/forge-config.py`; never overwrites.
- Argument hint: none.
- Guarded: yes.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a library.
- Description: scaffold a new project from templates - a thought project (the chain) or a library (material only); files only, never git.
- Argument hint: `"<slug>"`.
- Guarded: yes.

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Description: add a new kind of artefact to the forge - its position in the forge intent, its definition and template, its prefixes, its reviewers.
- Argument hint: `"<name>"`.
- Guarded: yes.

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Description: bring an existing project into `projects/` - clone through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Argument hint: `"<git-url>"`.
- Guarded: yes.

### /forge (bare)

- Signature: `/forge [slug]`
- Purpose: the state map of a project.
- Description: work the document chain - bare = state map, with a target = iterate that artefact.
- Argument hint: `"[target-state] [project-slug]"`.
- Guarded: no.

### /forge with a state

- Signature: `/forge <state> [slug]`
- Purpose: iterate the target artefact through its definition.
- Description: the same skill as the bare form.
- Argument hint: the same as the bare form.
- Guarded: no.

### /ingest

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in `sources/`; `--bundle` into a growing bundle, born at its first file; bare = sweep `sources/`.
- Description: register external input (a file, or text pasted into the conversation) in `sources/` - store, ask what it is for, catalogue, nothing more.
- Argument hint: `"[file-or-path] [project-slug] [--bundle name]"`.
- Guarded: yes.

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Description: regenerate a render from its recipe in `recipes/`.
- Argument hint: `"<recipe> [project-slug]"`.
- Guarded: yes.

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Description: make the designed `.pptx` or `.docx` from the render of a recipe, through a model - started by the principal only.
- Argument hint: `"<recipe> [project-slug]"`.
- Guarded: yes.

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into `docs/`.
- Description: generate the documentation of the engine or of a project into `docs/` - pages of one topic each and their index, from a map.
- Argument hint: `"[project-slug]"`.
- Guarded: yes.

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare = the genre roster.
- Description: compose a render recipe by genre - bare = genre roster, with a genre = guided composition.
- Argument hint: `"[genre-or-recipe] [project-slug]"`.
- Guarded: no.

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product: its specification and its file; bare = the project's work products.
- Description: work a work product - bare = the roster of the project's work products, with a name = iterate its specification and make its file.
- Argument hint: `"[name] [project-slug]"`.
- Guarded: no.

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare = the lens roster.
- Description: run a critic lens on the quality of a project's documents - bare = lens roster.
- Argument hint: `"[lens] [artefact|path] [project-slug]"`.
- Guarded: no.

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare = the persona roster.
- Description: run a challenger persona against the substance of any chain artefact - bare = persona roster.
- Argument hint: `"[persona] [artefact|path] [project-slug]"`.
- Guarded: no.

### /research

- Signature: `/research <topic> [slug]`
- Purpose: best-practices research into `research/`, indexed.
- Description: research current best practices on a topic; store durable notes.
- Argument hint: `"<topic> [project-slug]"`.
- Guarded: no.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger.
- Description: report project state from the ledger.
- Argument hint: `"[project-slug]"`.
- Guarded: no.

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Description: the history of one item by its ID - its wording today, its records, the archive rows that mention it and every citation, gathered by a script; Claude adds a few sentences of its own.
- Argument hint: `"<ID> [project-slug]"`.
- Guarded: no.

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare = the check roster.
- Description: run a check on the conformance of a project or the engine with the conventions - bare = check roster.
- Argument hint: `"[check] [project-slug]"`.
- Guarded: no.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes; `--quick` without the check.
- Description: save the forge to git - the light check, then commit and push; no renders; `--quick` leaves the check out.
- Argument hint: `'[project-slug] [-m "message"] [--tag name] [--quick]'`.
- Guarded: yes.

### /release

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`.
- Description: release one repository from `main` - its checks with walkthrough, README and release notes, then `/save` with the release message and the tag at an approved major.
- Argument hint: `'[project-slug] [-m "message"] [--tag name]'`.
- Guarded: yes.

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin; after a pull of the engine, the Action required lines crossed and the offer of the checks.
- Description: look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines crossed and the offer of the checks.
- Argument hint: `"[project-slug]"`.
- Guarded: yes.

### /end

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Description: end a session - what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Argument hint: none.
- Guarded: no.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Description: spin a requirement group off into its own project (principal's explicit decision only).
- Argument hint: `"<source-project> <group-name> <new-slug>"`.
- Guarded: yes.

### /migrate

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the shape of files: a dry run, the migration on the principal's word, then `/save`.
- Description: bring a project to the shape of a release that changed the shape of files - a dry run first, the migration on the principal's word, the threads' origins judged, then `/save`.
- Argument hint: `"[project-slug]"`.
- Guarded: yes.

### /man

- Signature: `/man [command | method]`
- Purpose: the forge's manual, read from its own definitions.
- Description: the forge's manual, read from its own definitions - bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill.
- Argument hint: `"[command | method]"`.
- Guarded: no.

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`.
- Description: alias of `/man` - the forge's manual, read from its own definitions.
- Argument hint: `"[command | method]"`.
- Guarded: no.

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
