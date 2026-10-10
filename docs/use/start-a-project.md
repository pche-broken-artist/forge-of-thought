---
generated: 2026-10-10
made: mirrored
inputs-hash: 14b6b4fa13eba370
inputs:
  - .claude/skills/new-project/SKILL.md
  - CLAUDE.md
  - templates/ledger.md
---

# Start a project

This page is for a person who wants a new project in the forge. It
says what `/new-project <slug>` does, what it creates for each of the
two kinds of project, and the one step it leaves to you.

## Run the command

Type `/new-project <slug>`. Two things are decided at the start, and
both are written into the header of the project's ledger.

- **The kind.** `thought` is the default: a project with the chain of
  documents. `library` is material shared across projects, with no
  chain; its slug starts with `lib-`. The command takes the kind from
  the `lib-` prefix or from your words, and asks when it is unclear.
- **The language of the chain's artefacts.** English unless you name
  another; the command asks when your words leave it open.

For a thought project the slug is lowercase, with hyphens and no
spaces. If a folder `projects/<slug>/` already exists, the command
stops and reports. It never overwrites.

The command makes files only. It never touches git.

## What a thought project gets

Under `projects/<slug>/` the command creates:

- `sources/`, `reviews/`, `challenges/` and `research/`, empty except
  that `sources/` and `research/` each hold a `00-INDEX.md` with its
  header filled and no entries.
- `ledger.md`, filled with the slug, `kind: thought`, the language and
  today's date. The brief is listed as version 0.1, a draft, not yet
  mined.
- `decisions.md`, with the slug filled and no sample record.
- `recipes/readme.md` and `recipes/release-notes.md`, each with its
  history companion. The README and the release notes themselves are
  made later, by `/release`, not by this command.

`logo.png` is yours to supply and is optional. The command mentions it
once and never asks for it.

### The founding brief

The command then asks you to paste or dictate the brief now. It hands
the text to `/forge brief`, which creates the brief and carries it on.
How a brief is composed is not repeated here.

### What is not created yet

The intent (`10-intent.md`) and every layer below it do not exist yet.
Each is born from its own first `/forge <state>`. The command ends by
proposing `/forge intent` as the next step.

## What a library gets

A library holds material and has no chain. The command creates only:

- `ledger.md` with `kind: library`, reduced to the tables a library
  needs (Renders, Sources, Dependencies, Research and Waiting on
  principal).
- `sources/00-INDEX.md` and `research/00-INDEX.md`.
- `recipes/readme.md` and its history companion. A library's README is
  its catalogue.

It has no brief, no decisions, no reviews or challenges and no release
notes. The command ends by proposing `/ingest` for the first
documents.

## The step that is yours

A project is a repository of its own that the engine does not track.
A new project therefore starts without git, which is a property, not a
defect. The command says so once at the end. When you want it under
git, run:

```
git -C projects/<slug> init -b main
```

and add a remote if you want one. Which identity the commits carry is
git's own configuration on your machine. The forge sets none and has
nothing to propose.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for and how it is used.
- [About projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own that the engine does not know.
