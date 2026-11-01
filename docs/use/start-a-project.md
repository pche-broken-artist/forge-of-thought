---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 6fa401341a29ae9d
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - templates/gitignore
  - CLAUDE.md#Persistence (git)
---

# Start a project

`/new-project <slug>` scaffolds a new project under `projects/<slug>/`: either a thought project (the chain of versioned documents) or a library (shared material, no chain). This page is for you, the principal (the person whose thinking is forged), when you begin a new body of work.

## When to use it

Use it once per project, before anything else is written for it. Use the thought kind when an idea is to travel the chain. Use the library kind when documents are to be shared across projects: the slug then starts with `lib-`.

## The command

```
/new-project <slug>
```

A slug is lowercase with hyphens and no spaces. A library is named with the prefix, as in `lib-<name>`.

## What happens

1. Claude settles the kind. It takes a library from the `lib-` prefix or from your words, and asks where this is unclear. You should now see the kind agreed.
2. Claude settles the language of the chain's documents. It is English unless you name another; Claude asks where your words leave it open. You should now see the language agreed.
3. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports, and never overwrites. You should now see either a stop or the folder being made.
4. Claude creates the files, and only files: the command never touches git. You should now see the files listed below under `projects/<slug>/`.
5. For a thought project, Claude asks you to paste or dictate the founding brief at once and hands it to the brief procedure. How the brief is composed is the page [Write a brief](write-a-brief.md). You should now see the brief file begun.
6. For a thought project, Claude makes the ledger once by its script. The ledger is the state of the project, made at read time and never kept in git. You should now see a `ledger.md` in the project.
7. Claude proposes the next step: `/forge intent` to start the elicitation interview. It also reminds you that the project is not under git yet. You should now see that proposal.

## What you have afterwards

For every project:

- `project.md`, the project file, holding the slug, the kind and the language. It is written once here, never by a later round.
- `.gitattributes`, copied from its template: the ways of merging by path.
- `.gitignore`, copied from its template: it keeps the ledger and the lock files of an open Office document (`~$*`) out of git.

For a thought project, beside them:

- `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`, empty except that `sources/` and `research/` each hold a `00-INDEX.md`, a catalogue with no entries yet.
- `decisions.md`, with the slug filled in and no records.
- `recipes/readme.md` and `recipes/release-notes.md`, the recipes of the README and of the release notes, each with its history companion `recipes/<recipe>.history.md`. Their renders are made later, at a release, not here.
- The founding brief, with its companion.

For a library, only:

- the two indexes, `sources/00-INDEX.md` and `research/00-INDEX.md`.
- `recipes/readme.md` with its history companion. A library's README is its catalogue.
- No brief, decisions, reviews, challenges or release notes. Claude proposes `/ingest` for the first documents. What a library is for is described in [Share material through a library](share-material-through-a-library.md).

Not created: the intent and every layer below it. Each is born at its first `/forge <state>`. `logo.png` is yours to supply and is optional; Claude mentions it once and never asks for it.

## The one step that is yours

The project is a repository of its own that the engine does not track, and the command creates no git. Initialising the repository is your one-off act:

```
git -C projects/<slug> init -b main
```

Add a remote afterwards if you want one. A project that stays outside git is a property, not a defect. The commit identity comes from your own git configuration, not from the forge. Why a project is a repository of its own, and what its project file declares, is explained in [Projects and the engine](../about/projects-and-the-engine.md). Why a project declares one output language is in [Languages](../about/languages.md).

## If something goes wrong

- The folder `projects/<slug>/` already exists: the command stops and reports, and changes nothing.
- The slug has capitals or spaces: it is not valid; give a lowercase slug with hyphens.
- The kind or language is unclear from your words: Claude asks; answer it.

## A worked example

You type:

```
/new-project my-idea
```

Claude takes the thought kind, the default. You say the documents are to be in `<language>`, so the project file reads:

```
---
project: my-idea
kind: thought
language: <xx>
---
```

Claude creates the folders, the files above and the recipes, asks for the brief and hands it on, makes the ledger, and proposes `/forge intent`. You then run:

```
git -C projects/my-idea init -b main
```

For a library, `/new-project lib-<name>` gives the same project file with `kind: library` and the smaller set of files.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
