---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 0e1eb6db92514227
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

This page lists every command of the forge with its signature, its
purpose, its arguments and whether it is guarded. It is for the user
who looks for the right command, the extender who adds one and the
evaluator who wants to see the whole set at a glance.

A guarded command is one that carries `disable-model-invocation: true`
in its definition: Claude does not start it on its own, only the
principal (the person whose thinking is being forged) types it. In
signatures, `<x>` is a required argument, `[x]` an optional one and
`a | b` a choice. A project slug is the short name of a project under
`projects/`. Where it is left out, the command works on the project the
conversation is about, or as the entry says.

## The commands at a glance

| Command | Purpose | Arguments | Guarded |
|---|---|---|---|
| `/setup` | First run after cloning the engine: prepare the instance | none | yes |
| `/new-project` | Scaffold a project by kind: a thought project or a library | `<slug>` | yes |
| `/new-artefact` | Add a new kind of artefact to the forge | `<name>` | yes |
| `/import-project` | Bring an existing project into `projects/` | `<git-url>` | yes |
| `/forge` | The state map of a project, or iterate one artefact | `[target-state] [project-slug]` | no |
| `/ingest` | Store, register and index external input in `sources/` | `[file-or-path] [project-slug] [--bundle name]` | yes |
| `/render` | Regenerate a render from its recipe | `<recipe> [project-slug]` | yes |
| `/publish` | Make the designed file from a render, through a model | `<recipe> [project-slug]` | yes |
| `/document` | Generate the documentation into `docs/` | `[project-slug]` | yes |
| `/recipe` | Compose or iterate a render recipe by genre | `[genre-or-recipe] [project-slug]` | no |
| `/work` | Work a work product | `[name] [project-slug]` | no |
| `/critique` | Run a critic lens on the quality of the documents | `[lens] [artefact\|path] [project-slug]` | no |
| `/challenge` | Run a challenger persona against the substance | `[persona] [artefact\|path] [project-slug]` | no |
| `/research` | Research a topic from a plan the principal confirms first | `[--quick \| --deep [--engine <name>]] <topic> [project-slug]` | no |
| `/ledger` | State report from the ledger | `[project-slug]` | no |
| `/history` | The history of one item by its ID | `<ID> [project-slug]` | no |
| `/check` | Run a check on a project or on the engine | `[check] [project-slug]` | no |
| `/save` | Save one repository, or every one with changes | `[project-slug] [-m "message"] [--tag name] [--quick]` | yes |
| `/release` | Release one repository from `main` | `[project-slug] [-m "message"] [--tag name]` | yes |
| `/pull` | Look at the remote and pull a clean repository that is behind | `[project-slug]` | yes |
| `/end` | End a session | none | no |
| `/spinoff` | Split a group into its own project | `<source-project> <group-name> <new-slug>` | yes |
| `/migrate` | Bring a project to the shape of a release | `[project-slug]` | yes |
| `/man` | The forge's manual | `[command \| method \| question]` | no |
| `/manual` | Alias of `/man` | `[command \| method \| question]` | no |

## Entries

### /setup

- Signature: `/setup`
- Purpose: first run after cloning the engine. It creates and fills the
  instance file by interview, sets the session model to the forge's
  default, and offers the git identity per host, the global guard and
  the registration of the merge driver `ours`. It never overwrites.
- Arguments: none.
- Guarded: yes.

### /new-project

- Signature: `/new-project <slug>`
- Purpose: scaffold a new project from the templates, either a thought
  project (the chain) or a library (material only). It writes files
  only and never touches git.
- Arguments: `<slug>`, the short name of the new project.
- Guarded: yes.

### /new-artefact

- Signature: `/new-artefact <name>`
- Purpose: add a new kind of artefact to the forge: its position in the
  forge intent, its definition and template, its prefixes and its
  reviewers.
- Arguments: `<name>`, the name of the new artefact.
- Guarded: yes.

### /import-project

- Signature: `/import-project <git-url>`
- Purpose: bring an existing project into `projects/`. It clones
  through `scripts/forge-clone.py`, which reports the commit identity
  git resolves.
- Arguments: `<git-url>`, the address of the project's repository.
- Guarded: yes.

### /forge

- Signature: `/forge [slug]` and `/forge <state> [slug]`
- Purpose: work the document chain. Bare, it shows the state map of a
  project. With a target, it iterates that artefact through its
  definition.
- Arguments: `[target-state]`, the state file that names the artefact,
  and `[project-slug]`.
- Guarded: no.

### /ingest

- Signature: `/ingest [file] [slug] [--bundle name]`
- Purpose: register external input, a file or text pasted into the
  conversation, in `sources/`: store it, ask what it is for and
  catalogue it, nothing more. Bare, it sweeps `sources/` for files not
  yet registered.
- Arguments: `[file-or-path]`, `[project-slug]` and `[--bundle name]`,
  which adds the file to a bundle of one origin that keeps arriving.
- Guarded: yes.

### /render

- Signature: `/render <recipe> [slug]`
- Purpose: regenerate a render from its recipe in `recipes/`.
- Arguments: `<recipe>`, the recipe's name, and `[project-slug]`.
- Guarded: yes.

### /publish

- Signature: `/publish <recipe> [slug]`
- Purpose: make the designed `.pptx` or `.docx` from the render of a
  recipe, through a model. It is started by the principal only.
- Arguments: `<recipe>` and `[project-slug]`.
- Guarded: yes.

### /document

- Signature: `/document [slug]`
- Purpose: generate the documentation of the engine or of a project
  into `docs/`: pages of one topic each and their index, from the
  documentation map.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /recipe

- Signature: `/recipe [genre] [slug]`
- Purpose: compose a render recipe by genre. Bare, it shows the roster
  of genres. With a genre, it guides the composition.
- Arguments: `[genre-or-recipe]` and `[project-slug]`.
- Guarded: no.

### /work

- Signature: `/work [name] [slug]`
- Purpose: the one door to a work product. Bare, it shows the roster
  of the project's work products. With a name, it iterates that
  product's specification and makes its file.
- Arguments: `[name]`, the work product, and `[project-slug]`.
- Guarded: no.

### /critique

- Signature: `/critique [lens] [artefact] [slug]`
- Purpose: run a critic lens on the quality of a project's documents.
  Bare, it shows the lens roster.
- Arguments: `[lens]`, `[artefact|path]`, an artefact or any file of the
  project (without one, the whole chain), and `[project-slug]`.
- Guarded: no.

### /challenge

- Signature: `/challenge [persona] [artefact] [slug]`
- Purpose: run a challenger persona against the substance of any chain
  artefact. Bare, it shows the persona roster.
- Arguments: `[persona]`, `[artefact|path]` and `[project-slug]`.
- Guarded: no.

### /research

- Signature: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`
- Purpose: research a topic from a plan the principal confirms first,
  on two model families, into a bundle of notes with a synthesis. The
  result is indexed.
- Arguments:
  - `--quick`: the shallow depth.
  - `--deep`: the deep depth.
  - `--engine <name>`: with `--deep`, the engine that runs it.
  - `<topic>`: what is researched.
  - `[project-slug]`: the last token, taken as the slug if it names a
    project.
- Guarded: no.

### /ledger

- Signature: `/ledger [slug]`
- Purpose: report the state of a project from the ledger. It makes the
  ledger of the project named, or of every project if none is given.
- Arguments: `[project-slug]`.
- Guarded: no.

### /history

- Signature: `/history <ID> [slug]`
- Purpose: the history of one item by its ID: its wording today, its
  records, the archive rows that mention it and every citation,
  gathered by a script. Claude adds a few sentences of its own.
- Arguments: `<ID>`, the item's identifier, and `[project-slug]`.
- Guarded: no.

### /check

- Signature: `/check [check] [slug]`
- Purpose: run a check on the conformance of a project or of the engine
  with the conventions. Bare, it shows the check roster.
- Arguments: `[check]` and `[project-slug]`.
- Guarded: no.

### /save

- Signature: `/save [slug] [-m "message"] [--tag name] [--quick]`
- Purpose: save the forge to git: the light check, then commit and
  push. No renders are made. It saves one repository, or every one with
  changes.
- Arguments:
  - `[project-slug]`: the repository to save.
  - `-m "message"`: the commit message.
  - `--tag name`: a tag to set.
  - `--quick`: leave the check out.
- Guarded: yes.

### /release

- Signature: `/release [slug] [-m "message"] [--tag name]`
- Purpose: release one repository from `main`: its checks with a
  walkthrough, the README and release notes, then a save with the
  release message and the tag at an approved major version.
- Arguments: `[project-slug]`, `-m "message"` and `--tag name`.
- Guarded: yes.

### /pull

- Signature: `/pull [slug]`
- Purpose: look at the remote and pull a clean repository that is
  behind, one repository or every one with an origin. After a pull of
  the engine, the lines marked as action required are crossed and the
  checks are offered.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /end

- Signature: `/end`
- Purpose: end a session: it says what lives only in the conversation,
  what is unsaved and what a shutdown would lose. A session is one
  running conversation with Claude.
- Arguments: none.
- Guarded: no.

### /spinoff

- Signature: `/spinoff <project> <group> <slug>`
- Purpose: spin a requirement group off into its own project, on the
  principal's explicit decision only.
- Arguments: `<source-project>`, `<group-name>` and `<new-slug>`.
- Guarded: yes.

### /migrate

- Signature: `/migrate [slug]`
- Purpose: bring a project to the shape of a release that changed the
  shape of files. It runs a dry run first, migrates on the principal's
  word, judges the origins of the threads, then saves.
- Arguments: `[project-slug]`.
- Guarded: yes.

### /man

- Signature: `/man [command | method | question]`
- Purpose: the forge's manual, read from its own definitions.
- Arguments: one optional argument, of three kinds:
  - none: the commands and the working methods.
  - a command: its purpose, arguments and roster.
  - a method: its paragraph and skill.
  - a need in free words (a question): the way the forge has for it.
- Guarded: no.

### /manual

- Signature: `/manual [command | method | question]`
- Purpose: alias of `/man`. It takes the same three kinds of argument
  and gives the same answers.
- Arguments: as `/man`.
- Guarded: no.

## See also

- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the same, printed in the session by `/man`, which also answers a need said in free words.
- [Add a command](../extend/add-a-command.md): adding a command of one's own.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
