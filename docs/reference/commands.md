---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 25e0142ad14c8ed8
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

This page lists every slash command of the forge with its signature, its purpose and its arguments. It is for anyone who needs to know what a command is called, what it takes and which file defines it.

In the signatures, `<x>` is an argument that must be given and `[x]` one that may be left out. A project slug is the short name of a project under `projects/`. The principal is the person whose thinking is being forged.

| Command | Purpose | Arguments | Skill file |
|---|---|---|---|
| `/setup` | First run after cloning the engine: prepare the instance | none | `.claude/skills/setup/SKILL.md` |
| `/new-project` | Scaffold a project by kind: a thought project or a library | `<slug>` | `.claude/skills/new-project/SKILL.md` |
| `/new-artefact` | Add a new kind of artefact to the forge | `<name>` | `.claude/skills/new-artefact/SKILL.md` |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | `.claude/skills/import-project/SKILL.md` |
| `/forge` | The state map of a project, or iterate one artefact through its definition | `[target-state] [project-slug]` | `.claude/skills/forge/SKILL.md` |
| `/ingest` | Store, register and index external input in `sources/` | `[file-or-path] [project-slug] [--bundle name]` | `.claude/skills/ingest/SKILL.md` |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | `.claude/skills/render/SKILL.md` |
| `/publish` | Make the designed file from a render, through a model | `<recipe> [project-slug]` | `.claude/skills/publish/SKILL.md` |
| `/document` | Generate the documentation of the engine or of a project into `docs/` | `[project-slug]` | `.claude/skills/document/SKILL.md` |
| `/recipe` | Compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | `.claude/skills/recipe/SKILL.md` |
| `/work` | Work a work product | `[name] [project-slug]` | `.claude/skills/work/SKILL.md` |
| `/critique` | Run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | `.claude/skills/critique/SKILL.md` |
| `/challenge` | Run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | `.claude/skills/challenge/SKILL.md` |
| `/research` | Research a topic from a plan the principal confirms first, quick or deep | `[--quick \| --deep [--engine <name>]] <topic> [project-slug]` | `.claude/skills/research/SKILL.md` |
| `/ledger` | State report from the ledger | `[project-slug]` | `.claude/skills/ledger/SKILL.md` |
| `/history` | The history of one item by its ID | `<ID> [project-slug]` | `.claude/skills/history/SKILL.md` |
| `/check` | Run a check on a project or on the engine | `[check] [project-slug]` | `.claude/skills/check/SKILL.md` |
| `/test` | Run the engine's tests | `[pytest arguments]` | `.claude/skills/test/SKILL.md` |
| `/save` | Save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | `.claude/skills/save/SKILL.md` |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name] [--auto]` | `.claude/skills/release/SKILL.md` |
| `/pull` | Look at the remote and, clean and behind, pull | `[project-slug]` | `.claude/skills/pull/SKILL.md` |
| `/end` | End a session: what is lost on a shutdown | none | `.claude/skills/end/SKILL.md` |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | `.claude/skills/spinoff/SKILL.md` |
| `/migrate` | Bring a project to the shape of a release that changed the shape of files | `[project-slug]` | `.claude/skills/migrate/SKILL.md` |
| `/man` | The forge's manual, read from its own definitions | `[command \| method \| question]` | `.claude/skills/man/SKILL.md` |
| `/manual` | Alias of `/man` | `[command \| method \| question]` | `.claude/skills/manual/SKILL.md` |

A command that writes starts on the principal's word, as every command's page says.

For the same facts printed in the conversation, which also answers a need said in free words, see [Look up a command, or ask how to do something](../use/look-up-a-command.md). Adding a command of one's own is described in [Add a command](../extend/add-a-command.md). Terms of the forge are defined in the [Glossary](glossary.md).

## `/setup`

- Signature: `/setup`
- Purpose: first run after cloning the engine; prepare the instance.
- Description: create and fill `CLAUDE.local.md` by interview, set the session model to the forge's default, offer the git identity per host, the global guard and the registration of the merge driver `ours`, written through `scripts/forge-config.py`; never overwrites.
- Arguments: none.
- Skill: `.claude/skills/setup/SKILL.md`

## `/new-project`

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind, a thought project or a library.
- Description: scaffold a new project from templates, a thought project (the chain) or a library (material only); files only, never git.
- Arguments: `<slug>`, the slug of the new project.
- Skill: `.claude/skills/new-project/SKILL.md`

## `/new-artefact`

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Description: add a new kind of artefact to the forge, with its position in the forge intent, its definition and template, its prefixes and its reviewers.
- Arguments: `<name>`, the name of the new artefact.
- Skill: `.claude/skills/new-artefact/SKILL.md`

## `/import-project`

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Description: clone through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Arguments: `<git-url>`, the address of the repository to bring in.
- Skill: `.claude/skills/import-project/SKILL.md`

## `/forge`

- Signature: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: the state map of a project, or iterate the target artefact through its definition.
- Description: work the document chain; bare gives the state map, with a target it iterates that artefact.
- Arguments: `[target-state] [project-slug]`.
- Skill: `.claude/skills/forge/SKILL.md`

## `/ingest`

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: store, register and index external input in `sources/`; bare, it sweeps `sources/` for unregistered files.
- Description: register external input (a file, or text pasted into the conversation) in `sources/`; store, ask what it is for, catalogue, nothing more.
- Arguments: `[file-or-path] [project-slug] [--bundle name]`. `--bundle name` adds the file to a bundle of one origin that keeps arriving.
- Skill: `.claude/skills/ingest/SKILL.md`

## `/render`

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Description: regenerate a render from its recipe in `recipes/`.
- Arguments: `<recipe> [project-slug]`.
- Skill: `.claude/skills/render/SKILL.md`

## `/publish`

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Description: make the designed `.pptx` or `.docx` from the render of a recipe, through a model; started by the principal only.
- Arguments: `<recipe> [project-slug]`.
- Skill: `.claude/skills/publish/SKILL.md`

## `/document`

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into `docs/`.
- Description: generate the documentation of the engine or of a project into `docs/`, pages of one topic each and their index, from a map.
- Arguments: `[project-slug]`.
- Skill: `.claude/skills/document/SKILL.md`

## `/recipe`

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre; bare gives the genre roster.
- Description: compose a render recipe by genre; bare gives the genre roster, with a genre a guided composition.
- Arguments: `[genre-or-recipe] [project-slug]`.
- Skill: `.claude/skills/recipe/SKILL.md`

## `/work`

- Signature: `/work [name] [slug]`
- Purpose: work a work product, its specification and its file; bare gives the project's work products.
- Description: work a work product; bare gives the roster of the project's work products, with a name it iterates the specification and makes the file.
- Arguments: `[name] [project-slug]`.
- Skill: `.claude/skills/work/SKILL.md`

## `/critique`

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents; bare gives the lens roster.
- Description: run a critic lens on the quality of a project's documents.
- Arguments: `[lens] [artefact|path] [project-slug]`.
- Skill: `.claude/skills/critique/SKILL.md`

## `/challenge`

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance; bare gives the persona roster.
- Description: run a challenger persona against the substance of any chain artefact.
- Arguments: `[persona] [artefact|path] [project-slug]`.
- Skill: `.claude/skills/challenge/SKILL.md`

## `/research`

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research a topic from a plan the principal confirms first, quick or deep; indexed.
- Description: research a topic from a plan the principal confirms first, on two model families, into a bundle of notes with a synthesis.
- Arguments: `[--quick | --deep [--engine <name>]] <topic> [project-slug]`.
  - The last token is the project slug if it names a directory under `projects/`; a first token `--quick` or `--deep` is the depth; the rest is the topic.
  - `--deep`: the whole course on the session model, a plan of several cards and a bundle with a synthesis.
  - `--deep --engine <name>`: adds a second engine beside the session model. It reviews the draft plan and takes every card. `<name>` is a row of the engine table of `scripts/forge-engine.py`. The option may be repeated for a third engine.
  - `--quick`: one card on the session model alone, shown in one message before anything is searched. It has no plan review, no second engine and no synthesis, and it takes no `--engine`.
  - Without a depth word, Claude proposes a depth with its reason and the principal decides.
- Skill: `.claude/skills/research/SKILL.md`

## `/ledger`

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger, the file that holds a project's state.
- Description: report project state from the ledger.
- Arguments: `[project-slug]`.
- Skill: `.claude/skills/ledger/SKILL.md`

## `/history`

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item: its wording today, its records, the archive rows and the citations, by a script; Claude adds a few sentences.
- Description: the history of one item by its ID, gathered by a script; read-only.
- Arguments: `<ID> [project-slug]`.
- Skill: `.claude/skills/history/SKILL.md`

## `/check`

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine; bare gives the check roster.
- Description: run a check on the conformance of a project or the engine with the conventions.
- Arguments: `[check] [project-slug]`.
- Skill: `.claude/skills/check/SKILL.md`

## `/test`

- Signature: `/test [pytest arguments]`
- Purpose: run the engine's tests; the sum back, a red test as pytest printed it.
- Description: run pytest over `tests/` from the engine root; nothing fixed, nothing written.
- Arguments: `[pytest arguments]`, passed on to `python -m pytest -q`.
- Skill: `.claude/skills/test/SKILL.md`

## `/save`

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes; `--quick` without the check.
- Description: save to git with the light check, then commit and push; no renders; `--quick` leaves the check out.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--quick]`.
- Skill: `.claude/skills/save/SKILL.md`

## `/release`

- Signature: `/release [slug] [-m "message"] [--tag name] [--auto]`
- Purpose: release one repository from `main`; `--auto` runs through and stops only at a serious thing.
- Description: release one repository from `main`: its tests, its checks settled by walkthrough (one item per message, each closed with a verdict), the documentation, the README and release notes, then `/save` with the release message and the tag at an approved major; `--auto` runs through and stops only at a serious thing.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--auto]`.
- Skill: `.claude/skills/release/SKILL.md`

## `/pull`

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin.
- Description: look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines are crossed and the checks offered.
- Arguments: `[project-slug]`.
- Skill: `.claude/skills/pull/SKILL.md`

## `/end`

- Signature: `/end`
- Purpose: end a session, one run of Claude Code: what lives only in the conversation, what is unsaved, what a shutdown would lose.
- Description: writes nothing and runs nothing but the status script; every remedy is an offer.
- Arguments: none.
- Skill: `.claude/skills/end/SKILL.md`

## `/spinoff`

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Description: spin a requirement group off into its own project; the principal's explicit decision only.
- Arguments: `<source-project> <group-name> <new-slug>`.
- Skill: `.claude/skills/spinoff/SKILL.md`

## `/migrate`

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the shape of files.
- Description: a dry run first, the migration on the principal's word, the threads' origins judged, then `/save`.
- Arguments: `[project-slug]`.
- Skill: `.claude/skills/migrate/SKILL.md`

## `/man`

- Signature: `/man [command | method | question]`
- Purpose: the forge's manual, read from its own definitions; a need in free words gets the way the forge has for it.
- Description: the manual, read from the files that own it.
- Arguments: `[command | method | question]`.
  - Bare: the commands and the working methods.
  - A command: its purpose, its arguments and its roster.
  - A method: its paragraph and skill.
  - A question in free words: the way the forge has for the need.
- Skill: `.claude/skills/man/SKILL.md`

## `/manual`

- Signature: `/manual [command | method | question]`
- Purpose: alias of `/man`.
- Description: the same as `/man`, with the same arguments.
- Arguments: `[command | method | question]`, the three of `/man`.
- Skill: `.claude/skills/manual/SKILL.md`

## See also

- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the same, printed in the session by `/man`, which also answers a need said in free words.
- [Add a command](../extend/add-a-command.md): adding a command of one's own, and how a command that writes waits for the principal's word.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
