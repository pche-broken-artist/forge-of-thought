---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 51a17aedff4daff1
inputs:
  - .claude/reference/commands.md
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
  - .claude/skills/thread/SKILL.md
  - .claude/skills/work/SKILL.md
  - .claude/skills/critique/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/history/SKILL.md
  - .claude/skills/check/SKILL.md
  - .claude/skills/test/SKILL.md
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

This page lists every command of the forge with its signature, its purpose and its arguments. It is for the user, the extender and the evaluator who want the exact form of a command. The principal is the person whose thinking is forged; the session is one running conversation with Claude. The terms of the forge are explained in the [Glossary](glossary.md).

A command that writes starts on the principal's word, as every command's page says.

## Overview

In the signatures, square brackets mark an optional argument, angle brackets a required one and a bar a choice. `slug` is the short name of a project; where it is left out, the command works on the project it finds.

| Command | Purpose | Arguments | Skill file |
|---|---|---|---|
| `/setup` | first run after cloning the engine: prepare the instance | none | `.claude/skills/setup/SKILL.md` |
| `/new-project` | scaffold a project by kind: a thought project or a library | `<slug>` | `.claude/skills/new-project/SKILL.md` |
| `/new-artefact` | add a new kind of artefact to the forge | `<name>` | `.claude/skills/new-artefact/SKILL.md` |
| `/import-project` | bring an existing project into `projects/` | `<git-url>` | `.claude/skills/import-project/SKILL.md` |
| `/forge` | the state map of a project, or iterate the target artefact through its definition | `[slug]` or `<state> [slug]` | `.claude/skills/forge/SKILL.md` |
| `/ingest` | store, register and index external input in sources/ | `[file] [slug] [--bundle name]` | `.claude/skills/ingest/SKILL.md` |
| `/render` | regenerate a render from its recipe | `<recipe> [slug]` | `.claude/skills/render/SKILL.md` |
| `/publish` | make the designed file from a render, through a model | `<recipe> [slug]` | `.claude/skills/publish/SKILL.md` |
| `/document` | generate the documentation of the engine or of a project into docs/ | `[slug]` | `.claude/skills/document/SKILL.md` |
| `/recipe` | compose or iterate a render recipe by genre | `[genre] [slug]` | `.claude/skills/recipe/SKILL.md` |
| `/thread` | work the threads of a project | `[text \| THR.NNNN] [slug]` | `.claude/skills/thread/SKILL.md` |
| `/work` | work a work product: its specification and its file | `[name] [slug]` | `.claude/skills/work/SKILL.md` |
| `/critique` | run a critic lens on the quality of the documents | `[lens] [artefact] [slug]` | `.claude/skills/critique/SKILL.md` |
| `/challenge` | run a challenger persona against the substance | `[persona] [artefact] [slug]` | `.claude/skills/challenge/SKILL.md` |
| `/research` | research a topic from a plan the principal confirms first | `[--quick \| --deep [--engine <name>]] <topic> [slug]` | `.claude/skills/research/SKILL.md` |
| `/ledger` | state report from the ledger | `[slug]` | `.claude/skills/ledger/SKILL.md` |
| `/history` | the history of one item | `<ID> [slug]` | `.claude/skills/history/SKILL.md` |
| `/check` | run a check on a project or on the engine | `[check] [slug]` | `.claude/skills/check/SKILL.md` |
| `/test` | run the engine's tests | `[pytest arguments]` | `.claude/skills/test/SKILL.md` |
| `/save` | save one repository, or every one with changes | `[slug] [-m "message"] [--tag name] [--quick]` | `.claude/skills/save/SKILL.md` |
| `/release` | release one repository from `main` | `[slug] [-m "message"] [--tag name] [--auto]` | `.claude/skills/release/SKILL.md` |
| `/pull` | look at the remote and, clean and behind, pull | `[slug]` | `.claude/skills/pull/SKILL.md` |
| `/end` | end a session | none | `.claude/skills/end/SKILL.md` |
| `/spinoff` | split a group into its own project | `<project> <group> <slug>` | `.claude/skills/spinoff/SKILL.md` |
| `/migrate` | bring a project to the shape of a release that changed the shape of files | `[slug] [--comments]` | `.claude/skills/migrate/SKILL.md` |
| `/man` | the forge's manual, read from its own definitions | `[command \| method \| question]` | `.claude/skills/man/SKILL.md` |
| `/manual` | alias of `/man` | as `/man` | `.claude/skills/manual/SKILL.md` |

## Entries

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance.
- Skill description: create and fill the instance file by interview, set the session model to the forge's default, offer the git identity per host, the global guard and the registration of the merge driver `ours`, written through `scripts/forge-config.py`; never overwrites.
- Arguments: none.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a library.
- Skill description: scaffold a new project from templates, a thought project (the chain) or a library (material only); files only, never git.
- Argument hint: `"<slug>"`

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Skill description: add a new kind of artefact to the forge: its position in the forge intent, its definition and template, its prefixes, its reviewers.
- Argument hint: `"<name>"`

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Skill description: clone through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Argument hint: `"<git-url>"`

### /forge

- Signature: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: the state map of a project; with a state, iterate the target artefact through its definition.
- Skill description: work the document chain; bare is the state map, with a target it iterates that artefact.
- Argument hint: `"[target-state] [project-slug]"`

### /ingest

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in sources/; bare sweeps sources/.
- Skill description: register external input (a file, or text pasted into the conversation) in sources/: store, ask what it is for, catalogue, nothing more.
- Argument hint: `"[file-or-path] [project-slug] [--bundle name]"`

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Skill description: regenerate a render from its recipe in recipes/.
- Argument hint: `"<recipe> [project-slug]"`

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Skill description: make the designed .pptx or .docx from the render of a recipe, through a model; started by the principal only.
- Argument hint: `"<recipe> [project-slug]"`

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into docs/.
- Skill description: generate the documentation into docs/, pages of one topic each and their index, from a map.
- Argument hint: `"[project-slug]"`

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare is the genre roster.
- Skill description: compose a render recipe by genre; bare is the genre roster, with a genre it is a guided composition.
- Argument hint: `"[genre-or-recipe] [project-slug]"`

### /thread

- Signature: `/thread [text | THR.NNNN] [slug]`
- Purpose: work the threads of a project.
- Skill description: work the threads of a project.
- Argument hint: `"[text | THR.NNNN] [project-slug]"`
- The three forms:
  - bare: the open threads
  - a text: the birth of a thread
  - an ID: that thread taken up

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product: its specification and its file; bare lists the project's work products.
- Skill description: bare is the roster of the project's work products; with a name it iterates its specification and makes its file.
- Argument hint: `"[name] [project-slug]"`

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare is the lens roster.
- Skill description: run a critic lens on the quality of a project's documents.
- Argument hint: `"[lens] [artefact|path] [project-slug]"`

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare is the persona roster.
- Skill description: run a challenger persona against the substance of any chain artefact.
- Argument hint: `"[persona] [artefact|path] [project-slug]"`

### /research

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research a topic from a plan the principal confirms first, quick or deep; indexed.
- Skill description: research a topic from a plan the principal confirms first, on two model families, into a bundle of notes with a synthesis.
- Argument hint: `"[--quick | --deep [--engine <name>]] <topic> [project-slug]"`
- The two depths: `--quick` and `--deep`. `--engine <name>` is given after `--deep`.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger, the single record of a project's state, made from its documents when it is read.
- Skill description: report project state from the ledger.
- Argument hint: `"[project-slug]"`

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Skill description: the history of one item by its ID, gathered by a script; Claude adds a few sentences of its own.
- Argument hint: `"<ID> [project-slug]"`

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare is the check roster.
- Skill description: run a check on the conformance of a project or the engine with the conventions.
- Argument hint: `"[check] [project-slug]"`

### /test

- Signature: `/test [pytest arguments]`
- Purpose: run the engine's tests; the sum back, a red test as pytest printed it.
- Skill description: pytest over tests/, the sum back, a red test as pytest printed it; nothing fixed, nothing written.
- Argument hint: `"[pytest arguments]"`. The arguments are those of pytest.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes; `--quick` without the check.
- Skill description: save the forge to git: the light check, then commit and push; no renders; `--quick` leaves the check out.
- Argument hint: `'[project-slug] [-m "message"] [--tag name] [--quick]'`

### /release

- Signature: `/release [slug] [-m "message"] [--tag name] [--auto]`
- Purpose: release one repository from `main`; `--auto` runs through and stops only at a serious thing.
- Skill description: release one repository from main: its tests, its checks with walkthrough, the documentation, README and release notes, then `/save` with the release message and the tag at an approved major; `--auto` runs through and stops only at a serious thing.
- Argument hint: `'[project-slug] [-m "message"] [--tag name] [--auto]'`

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin.
- Skill description: look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines crossed and the offer of the checks.
- Argument hint: `"[project-slug]"`

### /end

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Skill description: end a session: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Arguments: none.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Skill description: spin a requirement group off into its own project (the principal's explicit decision only).
- Argument hint: `"<source-project> <group-name> <new-slug>"`

### /migrate

- Signature: `/migrate [slug] [--comments]`
- Purpose: bring a project to the shape of a release that changed the shape of files; `--comments` replaces the skeletons' comments by the line that names the skeleton.
- Skill description: a dry run first, the migration on the principal's word, the threads' origins judged, then `/save`.
- Argument hint: `"[project-slug] [--comments]"`

### /man

- Signature: `/man [command | method | question]`
- Purpose: the forge's manual, read from its own definitions; a need in free words gets the way the forge has for it.
- Skill description: the forge's manual, read from its own definitions.
- Argument hint: `"[command | method | question]"`
- The three arguments:
  - bare: the commands and the working methods
  - a command: its purpose, arguments and roster
  - a method: its paragraph and skill
  - a question in free words: the way the forge has for the need

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`.
- Skill description: alias of `/man`, the forge's manual, read from its own definitions.
- Argument hint: `"[command | method | question]"`, the same three arguments as `/man`.

## See also

- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the same, printed in the session by `/man`, which also answers a need said in free words.
- [Add a command](../extend/add-a-command.md): adding a command of one's own, and how a command that writes waits for the principal's word.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
