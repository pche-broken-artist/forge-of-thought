---
generated: 2026-10-09
made: mirrored
inputs-hash: df7d055ee8603b7b
inputs:
  - .claude/skills/new-project/SKILL.md
  - CLAUDE.md
  - templates/ledger.md
---

# Start a project

This page is for the user who wants to begin a new project in the
forge. It says what `/new-project <slug>` creates, what it asks you,
and the one step it leaves to you: putting the project under git.

## Choose the kind and the language

Every project has a kind, declared as `kind:` in the header of its
ledger:

- `thought`: the default. A project with the chain of documents, from
  the brief onward.
- `library`: material shared across projects, with no chain. Its slug
  starts with `lib-`.

The command takes the kind from the `lib-` prefix or from your words.
When that is unclear it asks you.

The header also declares `language:`, the language of the project's
chain artefacts. It is English unless you name another; when your
words leave it open, the command asks.

## Start a thought project

Run `/new-project <slug>`. The slug is lowercase, with hyphens and no
spaces. If `projects/<slug>/` already exists, the command stops and
reports. It never overwrites.

It creates files only:

- `sources/`, `reviews/`, `challenges/` and `research/`, empty except
  that `sources/` and `research/` each hold a `00-INDEX.md` with its
  header filled and no entries.
- `ledger.md`, filled with the slug, `kind: thought`, the language and
  today's date, with the brief as a row at version 0.1, draft,
  pending.
- `decisions.md`, with the slug filled and no records yet.
- `recipes/readme.md` and `recipes/release-notes.md`, the recipes of
  the project's README and release notes, each with its history
  companion. The renders themselves are made later, at `/release`.

`logo.png` is yours to supply if you want an avatar for the project.
It is optional and the command does not ask for it.

### The founding brief

The command asks you to paste or dictate the brief now and hands it to
`/forge brief`, which takes it from there. How a brief is composed is
on [Write a brief](write-a-brief.md).

### What is not created yet

The intent and every layer below it do not exist after
`/new-project`. Each is born from its own first `/forge <state>`. The
command ends by proposing `/forge intent` as the next step.

## Start a library

For a slug such as `lib-<name>`, the command creates only:

- `ledger.md` with `kind: library`, reduced to the tables a library
  keeps: Renders, Sources, Dependencies, Research and Waiting on
  principal.
- `sources/00-INDEX.md` and `research/00-INDEX.md`.
- `recipes/readme.md` and its companion `recipes/readme.history.md`.
  The README of a library is its catalogue of what it holds.

There is no brief, no decisions file, no reviews or challenges and no
release notes. The command ends by proposing `/ingest` for the first
documents. What a library is for and how it is used is on
[Share material through a library](share-material-through-a-library.md).

## Put the project under git yourself

The command never touches git. A new project is not under git until
you make it so, and that is not a defect; the command says so once at
the end. The one-off act is yours:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. The commit identity is git's: it is
resolved on each host from your own git configuration, and the forge
sets none.

Why a project is a repository of its own that the engine does not know
is explained on [About projects and the engine](../about/projects-and-the-engine.md).

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for and how it is used.
- [About projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own that the engine does not know.
