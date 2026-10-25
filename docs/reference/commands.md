---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: eac07f29ac3f8a87
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

This page lists every command of the forge with its signature, its purpose, its arguments and whether it is guarded. It is for the user, the extender and the evaluator who want the whole roster in one place. A command is typed by the principal (the person whose thinking is being forged) into the conversation with Claude.

A command is guarded when its definition carries `disable-model-invocation: true`. Claude does not start a guarded command on its own judgement; it runs only when the principal types it. An unguarded command may also be started by Claude where its situation arises.

In a signature, `<x>` is an argument that is required and `[x]` is one that may be left out. `project-slug` names a project under `projects/`.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | first run after cloning the engine: prepare the instance | none | yes |
| `/new-project <slug>` | scaffold a project by kind: a thought project or a library | `<slug>` | yes |
| `/new-artefact <name>` | add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project <git-url>` | bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge [slug]` | the state map of a project | `[target-state] [project-slug]` | no |
| `/forge <state> [slug]` | iterate the target artefact through its definition | `[target-state] [project-slug]` | no |
| `/ingest [file] [slug] [--bundle name]` | store, register and index external input in `sources/` | `[file-or-path] [project-slug] [--bundle name]` | yes |
| `/render <recipe> [slug]` | regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish <recipe> [slug]` | make the designed file from a render, through a model | `<recipe> [project-slug]` | yes |
| `/document [slug]` | generate the documentation into `docs/` | `[project-slug]` | yes |
| `/recipe [genre] [slug]` | compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work [name] [slug]` | work a work product | `[name] [project-slug]` | no |
| `/critique [lens] [artefact] [slug]` | run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | no |
| `/challenge [persona] [artefact] [slug]` | run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | no |
| `/research [--quick \| --deep [--engine <name>]] <topic> [slug]` | research a topic from a plan the principal confirms first | `[--quick \| --deep [--engine <name>]] <topic> [project-slug]` | no |
| `/ledger [slug]` | state report from the ledger | `[project-slug]` | no |
| `/history <ID> [slug]` | the history of one item | `<ID> [project-slug]` | no |
| `/check [check] [slug]` | run a check on a project or on the engine | `[check] [project-slug]` | no |
| `/save [slug] [-m "message"] [--tag name] [--quick]` | save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | yes |
| `/release [slug] [-m "message"] [--tag name]` | release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull [slug]` | look at the remote and pull a clean repository that is behind | `[project-slug]` | yes |
| `/end` | end a session | none | no |
| `/spinoff <project> <group> <slug>` | split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/migrate [slug]` | bring a project to the shape of a release | `[project-slug]` | yes |
| `/man [command \| method]` | the forge's manual, read from its own definitions | `[command \| method]` | no |
| `/manual …` | alias of `/man` | `[command \| method]` | no |

## The commands

Each entry gives the signature and purpose of the row in the table of commands, the `description` and the `argument-hint` of the command's definition, and whether it is guarded. A definition that has no `argument-hint` takes no arguments.

### `/setup`

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance.
- Description: first run after cloning the engine. It creates and fills the instance file by interview, sets the session model to the forge's default, and offers the git identity per host, the global guard and the registration of the merge driver `ours`, written through `scripts/forge-config.py`. It never overwrites.
- Arguments: none.
- Guarded: yes.

### `/new-project`

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a library.
- Description: scaffold a new project from templates, a thought project (the chain) or a library (material only). It makes files only and never touches git.
- Arguments: `"<slug>"`.
- Guarded: yes.

### `/new-artefact`

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Description: add a new kind of artefact to the forge, with its position in the forge intent, its definition and template, its prefixes and its reviewers.
- Arguments: `"<name>"`.
- Guarded: yes.

### `/import-project`

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Description: bring an existing project into `projects/` by cloning it through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Arguments: `"<git-url>"`.
- Guarded: yes.

### `/forge`

- Signatures: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: with no state, the state map of a project; with a state, iterate the target artefact through its definition.
- Description: work the document chain. Bare, it gives the state map; with a target, it iterates that artefact.
- Arguments: `"[target-state] [project-slug]"`.
- Guarded: no.

### `/ingest`

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in `sources/`. `--bundle` puts it into a growing bundle, born at its first file. Bare, it sweeps `sources/`.
- Description: register external input (a file, or text pasted into the conversation) in `sources/`: store it, ask what it is for, catalogue it, nothing more.
- Arguments: `"[file-or-path] [project-slug] [--bundle name]"`.
- Guarded: yes.

### `/render`

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Description: regenerate a render from its recipe in `recipes/`.
- Arguments: `"<recipe> [project-slug]"`.
- Guarded: yes.

### `/publish`

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Description: make the designed `.pptx` or `.docx` from the render of a recipe, through a model. Only the principal starts it.
- Arguments: `"<recipe> [project-slug]"`.
- Guarded: yes.

### `/document`

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into `docs/`.
- Description: generate the documentation of the engine or of a project into `docs/`, pages of one topic each and their index, from a map.
- Arguments: `"[project-slug]"`.
- Guarded: yes.

### `/recipe`

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre. Bare, it lists the genre roster.
- Description: compose a render recipe by genre. Bare, it gives the genre roster; with a genre, a guided composition.
- Arguments: `"[genre-or-recipe] [project-slug]"`.
- Guarded: no.

### `/work`

- Signature: `/work [name] [slug]`
- Purpose: work a work product: its specification and its file. Bare, it lists the project's work products.
- Description: work a work product. Bare, it gives the roster of the project's work products; with a name, it iterates that specification and makes its file.
- Arguments: `"[name] [project-slug]"`.
- Guarded: no.

### `/critique`

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents. Bare, it lists the lens roster.
- Description: run a critic lens on the quality of a project's documents. Bare, it gives the lens roster.
- Arguments: `"[lens] [artefact|path] [project-slug]"`.
- Guarded: no.

### `/challenge`

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance. Bare, it lists the persona roster.
- Description: run a challenger persona against the substance of any chain artefact. Bare, it gives the persona roster.
- Arguments: `"[persona] [artefact|path] [project-slug]"`.
- Guarded: no.

### `/research`

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research from a plan the principal confirms first. `--deep` runs on the session model into a bundle with its synthesis. `--engine <name>` adds a named engine beside it, on the principal's word. `--quick` makes one card into one note. Without a depth word Claude proposes one. The result is indexed.
- Description: research a topic from a plan the principal confirms first, on two model families, into a bundle of notes with a synthesis.
- Arguments: `"[--quick | --deep [--engine <name>]] <topic> [project-slug]"`.
- Guarded: no.

### `/ledger`

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger.
- Description: report project state from the ledger.
- Arguments: `"[project-slug]"`.
- Guarded: no.

### `/history`

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Description: the history of one item by its ID: its wording today, its records, the archive rows that mention it and every citation, gathered by a script. Claude adds a few sentences of its own.
- Arguments: `"<ID> [project-slug]"`.
- Guarded: no.

### `/check`

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine. Bare, it lists the check roster.
- Description: run a check on the conformance of a project or the engine with the conventions. Bare, it gives the check roster.
- Arguments: `"[check] [project-slug]"`.
- Guarded: no.

### `/save`

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes. `--quick` leaves out the check.
- Description: save the forge to git: the light check, then commit and push. It makes no renders. `--quick` leaves the check out.
- Arguments: `'[project-slug] [-m "message"] [--tag name] [--quick]'`.
- Guarded: yes.

### `/release`

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`.
- Description: release one repository from `main`: its checks with a walkthrough, the README and the release notes, then `/save` with the release message and the tag at an approved major.
- Arguments: `'[project-slug] [-m "message"] [--tag name]'`.
- Guarded: yes.

### `/pull`

- Signature: `/pull [slug]`
- Purpose: look at the remote and, when the repository is clean and behind, pull one repository or every one with an origin. After a pull of the engine, the lines marked Action required are crossed and the checks are offered.
- Description: look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines are crossed and the checks offered.
- Arguments: `"[project-slug]"`.
- Guarded: yes.

### `/end`

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose. A session is one run of Claude in one conversation.
- Description: end a session by saying what lives only in the conversation, what is unsaved and what a shutdown would lose.
- Arguments: none.
- Guarded: no.

### `/spinoff`

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Description: spin a requirement group off into its own project, on the principal's explicit decision only.
- Arguments: `"<source-project> <group-name> <new-slug>"`.
- Guarded: yes.

### `/migrate`

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the shape of files: a dry run, the migration on the principal's word, then `/save`.
- Description: bring a project to the shape of a release that changed the shape of files: a dry run first, the migration on the principal's word, the threads' origins judged, then `/save`.
- Arguments: `"[project-slug]"`.
- Guarded: yes.

### `/man`

- Signature: `/man [command | method]`
- Purpose: the forge's manual, read from its own definitions.
- Description: the forge's manual, read from its own definitions. Bare, it gives the commands and the working methods. With a command, it gives that command's purpose, arguments and roster. With a method, it gives the method's paragraph and skill.
- Arguments: `"[command | method]"`.
- Guarded: no.

### `/manual`

- Signature: `/manual …`
- Purpose: alias of `/man`.
- Description: alias of `/man`, the forge's manual, read from its own definitions.
- Arguments: `"[command | method]"`.
- Guarded: no.

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
