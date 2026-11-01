---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 13f83f851cd3b40a
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

This page lists every slash command of the forge with its signature, its purpose, its arguments and whether it is guarded. It is for the user, the extender and the evaluator who want the whole roster in one place. Terms of the forge are in the [Glossary](glossary.md).

A command is guarded when its definition carries `disable-model-invocation: true`. A guarded command runs when the principal (the person whose thinking is being forged) types it. Claude does not start it on its own.

In a signature, `<x>` is an argument that is required, `[x]` is one that may be left out, and `|` separates alternatives. A project slug is the short name of a project. Left out, it names the project the work is in.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | First run after cloning the engine: prepare the instance | none | yes |
| `/new-project` | Scaffold a project by kind | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` | The state map of a project, or iterate one artefact | `[target-state] [project-slug]` | no |
| `/ingest` | Store, register and index external input | `[file-or-path] [project-slug] [--bundle name]` | yes |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed file from a render, through a model | `<recipe> [project-slug]` | yes |
| `/document` | Generate the documentation into `docs/` | `[project-slug]` | yes |
| `/recipe` | Compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work` | Work a work product | `[name] [project-slug]` | no |
| `/critique` | Run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | no |
| `/challenge` | Run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | no |
| `/research` | Research a topic from a confirmed plan, quick or deep | `[--quick \| --deep [--engine <name>]] <topic> [project-slug]` | no |
| `/ledger` | State report from the ledger | `[project-slug]` | no |
| `/history` | The history of one item by its ID | `<ID> [project-slug]` | no |
| `/check` | Run a check on a project or on the engine | `[check] [project-slug]` | no |
| `/save` | Save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | yes |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name] [--auto]` | yes |
| `/pull` | Look at the remote and pull a clean repository that is behind | `[project-slug]` | yes |
| `/end` | End a session | none | no |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/migrate` | Bring a project to the shape of a release | `[project-slug]` | yes |
| `/man` | The forge's manual | `[command \| method \| question]` | no |
| `/manual` | Alias of `/man` | `[command \| method \| question]` | no |

## Entries

Each entry gives the signature, the purpose from the Commands table, what the command's definition says it is, its arguments and whether it is guarded. Where a command has no argument hint in its definition, the entry says it takes none.

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine, to prepare the instance.
- Definition says: creates and fills the instance file by interview, sets the session model to the forge's default, and offers the git identity per host, the global guard and the registration of the merge driver `ours`. These are written through `scripts/forge-config.py`. It never overwrites.
- Arguments: none.
- Guarded: yes.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind, a thought project or a library.
- Definition says: scaffolds a new project from the templates, either a thought project (the chain) or a library (material only). It writes files and never touches git.
- Arguments: `<slug>`, the name of the new project.
- Guarded: yes.

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Definition says: adds the kind's position in the forge intent, its definition and template, its prefixes and its reviewers.
- Arguments: `<name>`, the name of the new artefact.
- Guarded: yes.

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Definition says: clones the project through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Arguments: `<git-url>`, the address of the repository to bring in.
- Guarded: yes.

### /forge

- Signatures: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: the state map of a project; with a state, iterate the target artefact through its definition.
- Definition says: works the document chain. Bare, it shows the state map. With a target, it iterates that artefact.
- Arguments: `[target-state] [project-slug]`.
- Guarded: no.

### /ingest

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in `sources/`; bare, sweep `sources/` for unregistered files.
- Definition says: registers external input (a file, or text pasted into the conversation) in `sources/`. It stores, asks what the input is for, catalogues, and does nothing more.
- Arguments: `[file-or-path] [project-slug] [--bundle name]`. `--bundle name` grows a bundle of one origin file by file.
- Guarded: yes.

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Definition says: regenerates a render from its recipe in `recipes/`.
- Arguments: `<recipe> [project-slug]`.
- Guarded: yes.

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Definition says: makes the designed `.pptx` or `.docx` from the render of a recipe, through a model. Only the principal starts it.
- Arguments: `<recipe> [project-slug]`.
- Guarded: yes.

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into `docs/`.
- Definition says: generates pages of one topic each and their index, from a map.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare, the genre roster.
- Definition says: composes a render recipe by genre. Bare, it shows the genre roster. With a genre, it runs a guided composition.
- Arguments: `[genre-or-recipe] [project-slug]`.
- Guarded: no.

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product, its specification and its file; bare, the project's work products.
- Definition says: bare, it shows the roster of the project's work products. With a name, it iterates that product's specification and makes its file.
- Arguments: `[name] [project-slug]`.
- Guarded: no.

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare, the lens roster.
- Definition says: runs a critic lens on the quality of a project's documents. Bare, it shows the lens roster.
- Arguments: `[lens] [artefact|path] [project-slug]`.
- Guarded: no.

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare, the persona roster.
- Definition says: runs a challenger persona against the substance of any chain artefact. Bare, it shows the persona roster.
- Arguments: `[persona] [artefact|path] [project-slug]`.
- Guarded: no.

### /research

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research a topic from a plan the principal confirms first, quick or deep; indexed.
- Definition says: researches a topic on two model families, into a bundle of notes with a synthesis.
- Arguments:
  - `--quick`: the quick depth.
  - `--deep`: the deep depth.
  - `--engine <name>`: with `--deep`, names the engine the research runs on.
  - `<topic>`: the topic to research.
  - `[project-slug]`: the project the notes belong to.
- Guarded: no.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger, the file that holds the state of a project and is made when it is read.
- Definition says: reports project state from the ledger.
- Arguments: `[project-slug]`.
- Guarded: no.

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item, its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Definition says: gathers the item's wording today, its records, the archive rows that mention it and every citation, by a script. Claude adds a few sentences of its own.
- Arguments: `<ID> [project-slug]`.
- Guarded: no.

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare, the check roster.
- Definition says: runs a check on the conformance of a project or the engine with the conventions. Bare, it shows the check roster.
- Arguments: `[check] [project-slug]`.
- Guarded: no.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes; `--quick` without the check.
- Definition says: saves to git with the light check, then commit and push. It makes no renders. `--quick` leaves the check out.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--quick]`.
- Guarded: yes.

### /release

- Signature: `/release [slug] [-m "message"] [--tag name] [--auto]`
- Purpose: release one repository from `main`; `--auto` runs through and stops only at a serious thing.
- Definition says: runs the checks with a walkthrough (a list of items worked one at a time, each settled by the principal), then the documentation, the README and the release notes. It then runs `/save` with the release message and the tag at an approved major. `--auto` runs through and stops only at a serious thing.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--auto]`.
- Guarded: yes.

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin.
- Definition says: looks at the remote and pulls a clean repository that is behind. After a pull of the engine it crosses the lines marked Action required and offers the checks.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /end

- Signature: `/end`
- Purpose: end a session, the working period in Claude Code, and say what would be lost.
- Definition says: reports what lives only in the conversation, what is unsaved and what a shutdown would lose.
- Arguments: none.
- Guarded: no.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Definition says: spins a requirement group off into its own project, on the principal's explicit decision only.
- Arguments: `<source-project> <group-name> <new-slug>`.
- Guarded: yes.

### /migrate

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the shape of files.
- Definition says: runs a dry run first, then the migration on the principal's word, then the threads' origins are judged, then `/save`.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /man

- Signature: `/man [command | method | question]`
- Purpose: the forge's manual, read from its own definitions; a need in free words gets the way the forge has for it.
- Definition says: reads the manual from the forge's own definitions.
- Arguments: one optional argument, of three kinds:
  - bare: the commands and the working methods.
  - a command: its purpose, its arguments and its roster.
  - a method: its paragraph and its skill.
  - a question in free words: the way the forge has for that need.
- Guarded: no.

### /manual

- Signature: `/manual [command | method | question]`
- Purpose: alias of `/man`.
- Definition says: an alias of `/man`, the forge's manual read from its own definitions. It takes the same three arguments.
- Arguments: `[command | method | question]`.
- Guarded: no.

## See also

- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the same, printed in the session by `/man`, which also answers a need said in free words.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
