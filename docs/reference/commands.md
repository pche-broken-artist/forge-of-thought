---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 63513311dc388220
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

This page lists every command of the forge with its signature, its purpose, its arguments and whether it is guarded. It is for the user, the extender and the evaluator who need the exact shape of a command.

Terms used below:

- **Principal**: the person whose thinking is forged.
- **Slug**: the short name of a project, the name of its directory under `projects/`.
- **Guarded**: the command's skill carries `disable-model-invocation: true`, so Claude does not start it on its own; it runs when the principal types it.
- **Square brackets** in a signature mark an optional argument. Angle brackets mark a required one.

## Overview

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | Prepare the instance after cloning the engine | none | yes |
| `/new-project` | Scaffold a project | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact | `<name>` | yes |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` | State map, or iterate one artefact | `[target-state] [project-slug]` | no |
| `/ingest` | Register external input in sources/ | `[file-or-path] [project-slug]` | yes |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed file from a render | `<recipe> [project-slug]` | yes |
| `/document` | Generate the documentation | `[project-slug]` | yes |
| `/recipe` | Compose a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work` | Work a work product | `[name] [project-slug]` | no |
| `/critique` | Run a critic lens | `[lens] [artefact\|path] [project-slug]` | no |
| `/challenge` | Run a challenger persona | `[persona] [artefact\|path] [project-slug]` | no |
| `/research` | Research best practices on a topic | `<topic> [project-slug]` | no |
| `/ledger` | Report project state | `[project-slug]` | no |
| `/history` | The history of one item | `<ID> [project-slug]` | no |
| `/check` | Run a check | `[check] [project-slug]` | no |
| `/save` | Commit and push | `[project-slug] [-m "message"] [--tag name] [--quick]` | yes |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull` | Look at the remote and pull | `[project-slug]` | yes |
| `/end` | End a session | none | no |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/migrate` | Bring a project to a new file shape | `[project-slug]` | yes |
| `/man` | The forge's manual | `[command \| method]` | no |
| `/manual` | Alias of `/man` | `[command \| method]` | no |

## The commands

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine, to prepare the instance.
- Description: creates and fills `CLAUDE.local.md` by interview, sets the session model to the forge's default, and offers the git identity per host, the global guard and the registration of the merge drivers in the global git configuration that git reads. It never overwrites and runs no git operation.
- Arguments: none.
- Guarded: yes.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a project by kind, a thought project or a library.
- Description: scaffolds a new project from templates, either a thought project (the chain) or a library (material only). It works on files only and never touches git.
- Arguments: `<slug>`.
- Guarded: yes.

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge.
- Description: adds the kind with its position in the forge intent, its definition and template, its prefixes and its reviewers.
- Arguments: `<name>`.
- Guarded: yes.

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`.
- Description: clones the project through `scripts/forge-clone.py`, which reports the commit identity git resolves.
- Arguments: `<git-url>`.
- Guarded: yes.

### /forge

- Signatures: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: the first form gives the state map of a project. The second iterates the target artefact through its definition.
- Description: works the document chain. Bare, it gives the state map. With a target, it iterates that artefact.
- Arguments: `[target-state] [project-slug]`.
- Guarded: no.

### /ingest

- Signature: `/ingest [file] [slug]`
- Purpose: store, register and index external input in sources/. Bare, it sweeps sources/.
- Description: registers external input (a file, or text pasted into the conversation) in sources/. It stores it, asks what it is for and catalogues it, nothing more.
- Arguments: `[file-or-path] [project-slug]`.
- Guarded: yes.

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe.
- Description: regenerates a render from its recipe in `recipes/`.
- Arguments: `<recipe> [project-slug]`.
- Guarded: yes.

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed file from a render, through a model.
- Description: makes the designed `.pptx` or `.docx` from the render of a recipe, through a model. The principal alone starts it.
- Arguments: `<recipe> [project-slug]`.
- Guarded: yes.

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project into `docs/`.
- Description: generates pages of one topic each and their index, from a documentation map.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose or iterate a render recipe by genre. Bare, it lists the genre roster.
- Description: composes a render recipe by genre. Bare, it gives the genre roster. With a genre, it gives a guided composition.
- Arguments: `[genre-or-recipe] [project-slug]`.
- Guarded: no.

### /work

- Signature: `/work [name] [slug]`
- Purpose: work a work product, its specification and its file. Bare, it lists the project's work products.
- Description: bare, it gives the roster of the project's work products. With a name, it iterates the specification and makes the file.
- Arguments: `[name] [project-slug]`.
- Guarded: no.

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of the documents. Bare, it lists the lens roster.
- Description: runs a critic lens on the quality of a project's documents.
- Arguments: `[lens] [artefact|path] [project-slug]`.
- Guarded: no.

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance. Bare, it lists the persona roster.
- Description: runs a challenger persona against the substance of any chain artefact.
- Arguments: `[persona] [artefact|path] [project-slug]`.
- Guarded: no.

### /research

- Signature: `/research <topic> [slug]`
- Purpose: best-practices research into `research/`, indexed.
- Description: researches current best practices on a topic and stores durable notes.
- Arguments: `<topic> [project-slug]`.
- Guarded: no.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: state report from the ledger.
- Description: reports project state from the ledger.
- Arguments: `[project-slug]`.
- Guarded: no.

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item, by a script, with a few sentences added by Claude.
- Description: gives the item's wording today, its records, the archive rows that mention it and every citation, gathered by a script. Claude adds a few sentences of its own.
- Arguments: `<ID> [project-slug]`.
- Guarded: no.

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on a project or on the engine. Bare, it lists the check roster.
- Description: runs a check on the conformance of a project or the engine with the conventions.
- Arguments: `[check] [project-slug]`.
- Guarded: no.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save one repository, or every one with changes. `--quick` leaves the check out.
- Description: saves the forge to git with the light check, then commit and push. It makes no renders.
- Arguments: `[project-slug] [-m "message"] [--tag name] [--quick]`.
- Guarded: yes.

### /release

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`.
- Description: runs the repository's checks with a walkthrough, makes the README and release notes, then saves with the release message and the tag at an approved major.
- Arguments: `[project-slug] [-m "message"] [--tag name]`.
- Guarded: yes.

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and, clean and behind, pull one repository or every one with an origin. After a pull of the engine, it crosses the Action required lines and offers the checks.
- Description: looks at the remote and pulls a clean repository that is behind.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /end

- Signature: `/end`
- Purpose: end a session, saying what lives only in the conversation, what is unsaved and what a shutdown would lose.
- Description: the same, as the skill states it. A session here is one run of Claude with the principal.
- Arguments: none.
- Guarded: no.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: split a group into its own project.
- Description: spins a requirement group off into its own project, on the principal's explicit decision only.
- Arguments: `<source-project> <group-name> <new-slug>`.
- Guarded: yes.

### /migrate

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the shape of files: a dry run, the migration on the principal's word, then `/save`.
- Description: a dry run first, the migration on the principal's word, the threads' origins judged, then `/save`.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /man

- Signature: `/man [command | method]`
- Purpose: the forge's manual, read from its own definitions.
- Description: bare, it gives the commands and the working methods. With a command, it gives the purpose, arguments and roster. With a method, it gives the method's paragraph and skill.
- Arguments: `[command | method]`.
- Guarded: no.

### /manual

- Signature: `/manual …`
- Purpose: alias of `/man`.
- Description: the forge's manual, read from its own definitions; it takes the same arguments as `/man`.
- Arguments: `[command | method]`.
- Guarded: no.

## See also

- [Look up a command](../use/look-up-a-command.md): the same, printed in the session by `/man`.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
