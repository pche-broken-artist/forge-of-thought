---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 6c5ad6c131f301ff
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

This page lists every command of the forge with its signature, its
purpose and its arguments, for the user, the extender and the
evaluator. The principal is whoever's thinking is being forged. A
project is the folder under `projects/` that holds one principal's
chain of documents, and the slug is its short name. In a signature,
`<x>` is required and `[x]` is optional. The same facts are printed
in the conversation by `/man`, as
[Look up a command, or ask how to do something](../use/look-up-a-command.md)
describes.

## Overview

| Command | Purpose | Arguments | Skill file |
|---|---|---|---|
| `/setup` | first run after cloning the engine: prepare the instance | none | `.claude/skills/setup/SKILL.md` |
| `/new-project <slug>` | scaffold a project by kind: a thought project or a library | `<slug>` | `.claude/skills/new-project/SKILL.md` |
| `/new-artefact <name>` | add a new kind of artefact to the forge | `<name>` | `.claude/skills/new-artefact/SKILL.md` |
| `/import-project <git-url>` | bring an existing project into `projects/` | `<git-url>` | `.claude/skills/import-project/SKILL.md` |
| `/forge [slug]`, `/forge <state> [slug]` | the state map of a project; iterate the target artefact through its definition | `[target-state] [project-slug]` | `.claude/skills/forge/SKILL.md` |
| `/ingest [file] [slug] [--bundle name]` | store, register and index external input in `sources/` | `[file-or-path] [project-slug] [--bundle name]` | `.claude/skills/ingest/SKILL.md` |
| `/render <recipe> [slug]` | regenerate a render from its recipe | `<recipe> [project-slug]` | `.claude/skills/render/SKILL.md` |
| `/publish <recipe> [slug]` | make the designed file from a render, through a model | `<recipe> [project-slug]` | `.claude/skills/publish/SKILL.md` |
| `/document [slug]` | generate the documentation of the engine or of a project into `docs/` | `[project-slug]` | `.claude/skills/document/SKILL.md` |
| `/recipe [genre] [slug]` | compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | `.claude/skills/recipe/SKILL.md` |
| `/work [name] [slug]` | work a work product: its specification and its file | `[name] [project-slug]` | `.claude/skills/work/SKILL.md` |
| `/critique [lens] [artefact] [slug]` | run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | `.claude/skills/critique/SKILL.md` |
| `/challenge [persona] [artefact] [slug]` | run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | `.claude/skills/challenge/SKILL.md` |
| `/research [--quick \| --deep [--engine <name>]] <topic> [slug]` | research a topic from a plan the principal confirms first | `[--quick \| --deep [--engine <name>]] <topic> [project-slug]` | `.claude/skills/research/SKILL.md` |
| `/ledger [slug]` | state report from the ledger | `[project-slug]` | `.claude/skills/ledger/SKILL.md` |
| `/history <ID> [slug]` | the history of one item | `<ID> [project-slug]` | `.claude/skills/history/SKILL.md` |
| `/check [check] [slug]` | run a check on a project or on the engine | `[check] [project-slug]` | `.claude/skills/check/SKILL.md` |
| `/test [pytest arguments]` | run the engine's tests | `[pytest arguments]` | `.claude/skills/test/SKILL.md` |
| `/save [slug] [-m "message"] [--tag name] [--quick]` | save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | `.claude/skills/save/SKILL.md` |
| `/release [slug] [-m "message"] [--tag name] [--auto]` | release one repository from `main` | `[project-slug] [-m "message"] [--tag name] [--auto]` | `.claude/skills/release/SKILL.md` |
| `/pull [slug]` | look at the remote and pull a clean repository that is behind | `[project-slug]` | `.claude/skills/pull/SKILL.md` |
| `/end` | end a session | none | `.claude/skills/end/SKILL.md` |
| `/spinoff <project> <group> <slug>` | split a group into its own project | `<source-project> <group-name> <new-slug>` | `.claude/skills/spinoff/SKILL.md` |
| `/migrate [slug]` | bring a project to the shape of a release that changed the shape of files | `[project-slug]` | `.claude/skills/migrate/SKILL.md` |
| `/man [command \| method \| question]` | the forge's manual, read from its own definitions | `[command \| method \| question]` | `.claude/skills/man/SKILL.md` |
| `/manual …` | alias of `/man` | `[command \| method \| question]` | `.claude/skills/manual/SKILL.md` |

A command that writes starts on the principal's word, as every
command's page says. How a command of one's own is added, and how
such a command waits for that word, is described in
[Add a command](../extend/add-a-command.md).

## The commands

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine: prepare the instance.
- Arguments: none.
- Skill description: first run after cloning the engine. It creates
  and fills `CLAUDE.local.md` by interview, sets the session model to
  the forge's default, offers the git identity per host, the global
  guard and the registration of the merge driver `ours`, written
  through `scripts/forge-config.py`. It never overwrites.
- Skill file: `.claude/skills/setup/SKILL.md`

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind: a thought project or a
  library.
- Arguments: `<slug>`.
- Skill description: scaffold a new project from templates, either a
  thought project (the chain) or a library (material only). It makes
  files only, never git.
- Skill file: `.claude/skills/new-project/SKILL.md`

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Arguments: `<name>`.
- Skill description: add a new kind of artefact to the forge: its
  position in the forge intent, its definition and template, its
  prefixes, its reviewers.
- Skill file: `.claude/skills/new-artefact/SKILL.md`

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Arguments: `<git-url>`.
- Skill description: bring an existing project into `projects/`. It
  clones through `scripts/forge-clone.py`, which reports the commit
  identity git resolves.
- Skill file: `.claude/skills/import-project/SKILL.md`

### /forge

- Signature: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: the state map of a project; or iterate the target artefact
  through its definition.
- Arguments: `[target-state] [project-slug]`.
- Skill description: work the document chain. Without a target it
  shows the state map, with a target it iterates that artefact.
- Skill file: `.claude/skills/forge/SKILL.md`

### /ingest

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in `sources/`.
  Without a file it sweeps `sources/` for unregistered files.
- Arguments: `[file-or-path] [project-slug] [--bundle name]`.
- Skill description: register external input (a file, or text pasted
  into the conversation) in `sources/`: store it, ask what it is for,
  catalogue it, nothing more.
- Skill file: `.claude/skills/ingest/SKILL.md`

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Arguments: `<recipe> [project-slug]`.
- Skill description: regenerate a render from its recipe in
  `recipes/`.
- Skill file: `.claude/skills/render/SKILL.md`

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Arguments: `<recipe> [project-slug]`.
- Skill description: make the designed `.pptx` or `.docx` from the
  render of a recipe, through a model. Started by the principal only.
- Skill file: `.claude/skills/publish/SKILL.md`

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project
  into `docs/`.
- Arguments: `[project-slug]`.
- Skill description: generate the documentation of the engine or of a
  project into `docs/`: pages of one topic each and their index, from
  the documentation map.
- Skill file: `.claude/skills/document/SKILL.md`

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre. Without a
  genre it lists the genres.
- Arguments: `[genre-or-recipe] [project-slug]`.
- Skill description: compose a render recipe by genre. Without a
  genre it lists the genre roster, with a genre it guides the
  composition.
- Skill file: `.claude/skills/recipe/SKILL.md`

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product: its specification and its file.
- Arguments: `[name] [project-slug]`.
- Skill description: without a name, the roster of the project's work
  products. With a name, iterate its specification and make its file.
- Skill file: `.claude/skills/work/SKILL.md`

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents.
- Arguments: `[lens] [artefact|path] [project-slug]`.
- Skill description: run a critic lens on the quality of a project's
  documents. Without arguments it lists the lens roster.
- Skill file: `.claude/skills/critique/SKILL.md`

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance.
- Arguments: `[persona] [artefact|path] [project-slug]`.
- Skill description: run a challenger persona against the substance
  of any chain artefact. Without arguments it lists the persona
  roster.
- Skill file: `.claude/skills/challenge/SKILL.md`

### /research

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research a topic from a plan the principal confirms first,
  quick or deep; the result is indexed.
- Arguments: `[--quick | --deep [--engine <name>]] <topic> [project-slug]`.
  - `--quick`: the quick depth.
  - `--deep`: the deep depth.
  - `--engine <name>`: given with `--deep`, names the engine.
  - `<topic>`: the topic to research.
- Skill description: research a topic from a plan the principal
  confirms first, on two model families, into a bundle of notes with
  a synthesis.
- Skill file: `.claude/skills/research/SKILL.md`

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger. The ledger is the single
  source of truth for the state of a project, made from its documents
  at read time.
- Arguments: `[project-slug]`.
- Skill description: report project state from the ledger.
- Skill file: `.claude/skills/ledger/SKILL.md`

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records,
  the archive rows and the citations, by a script; Claude adds a few
  sentences.
- Arguments: `<ID> [project-slug]`.
- Skill description: the history of one item by its ID: its wording
  today, its records, the archive rows that mention it and every
  citation, gathered by a script. Claude adds a few sentences of its
  own.
- Skill file: `.claude/skills/history/SKILL.md`

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine. Without
  arguments it lists the check roster.
- Arguments: `[check] [project-slug]`.
- Skill description: run a check on the conformance of a project or
  the engine with the conventions. Without arguments it lists the
  check roster.
- Skill file: `.claude/skills/check/SKILL.md`

### /test

- Signature: `/test [pytest arguments]`
- Purpose: run the engine's tests; the sum comes back, and a red test
  as pytest printed it.
- Arguments: `[pytest arguments]`, passed on to pytest.
- Skill description: run the engine's tests with pytest over
  `tests/`. The sum comes back, a red test as pytest printed it.
  Nothing is fixed, nothing is written.
- Skill file: `.claude/skills/test/SKILL.md`

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes. `--quick`
  leaves the check out.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--quick]`.
- Skill description: save the forge to git: the light check, then
  commit and push. It makes no renders. `--quick` leaves the check
  out.
- Skill file: `.claude/skills/save/SKILL.md`

### /release

- Signature: `/release [slug] [-m "message"] [--tag name] [--auto]`
- Purpose: release one repository from `main`. `--auto` runs through
  and stops only at a serious thing.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--auto]`.
- Skill description: release one repository from `main`: its tests,
  its checks with a walkthrough (the items needing a decision worked
  one per message), the documentation, the README and the release
  notes, then `/save` with the release message and the tag at an
  approved major. `--auto` runs through and stops only at a serious
  thing.
- Skill file: `.claude/skills/release/SKILL.md`

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one
  repository or every one with an origin.
- Arguments: `[project-slug]`.
- Skill description: look at the remote and pull a clean repository
  that is behind. After a pull of the engine, the Action required
  lines are crossed and the checks are offered.
- Skill file: `.claude/skills/pull/SKILL.md`

### /end

- Signature: `/end`
- Purpose: end a session: what lives only in the conversation, what
  is unsaved, what a shutdown would lose.
- Arguments: none.
- Skill description: end a session. It says what lives only in the
  conversation, what is unsaved and what a shutdown would lose.
- Skill file: `.claude/skills/end/SKILL.md`

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Arguments: `<source-project> <group-name> <new-slug>`.
- Skill description: spin a requirement group off into its own
  project, on the principal's explicit decision only.
- Skill file: `.claude/skills/spinoff/SKILL.md`

### /migrate

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the
  shape of files.
- Arguments: `[project-slug]`.
- Skill description: bring a project to the shape of a release that
  changed the shape of files: a dry run first, the migration on the
  principal's word, the threads' origins judged, then `/save`.
- Skill file: `.claude/skills/migrate/SKILL.md`

### /man

- Signature: `/man [command | method | question]`
- Purpose: the forge's manual, read from its own definitions; a need
  in free words gets the way the forge has for it.
- Arguments: `[command | method | question]`.
  - Without an argument: the commands and the working methods.
  - A command: its purpose, arguments and roster.
  - A method: its paragraph and skill.
  - A question in free words: the way the forge has for the need.
- Skill file: `.claude/skills/man/SKILL.md`

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`.
- Arguments: `[command | method | question]`, the same three as
  `/man`.
- Skill description: alias of `/man`, the forge's manual, read from
  its own definitions.
- Skill file: `.claude/skills/manual/SKILL.md`

## See also

- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the same, printed in the session by `/man`, which also answers a need said in free words.
- [Add a command](../extend/add-a-command.md): adding a command of one's own, and how a command that writes waits for the principal's word.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
