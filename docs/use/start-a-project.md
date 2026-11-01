---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 38daf6cc555592ce
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - templates/gitignore
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how to scaffold a new project with `/new-project`, either a thought project (the chain of documents) or a library (shared material only). It is for you as the principal, the person whose thinking is forged, when you begin something new.

## When to use it

Use it when a new idea needs a place of its own, or when material is to be shared across projects and needs a library to live in. A project is a repository of its own that the engine does not track, and the command prepares only its files.

## The command

```
/new-project <slug>
```

The slug is lowercase, with hyphens and no spaces. A slug that starts with `lib-` makes a library. Anything else makes a thought project, unless your words say otherwise.

Two things are asked only where your words leave them open:

- The kind: a thought project or a library.
- The language of the chain artefacts: English unless you name another.

Both are written once into the project file `project.md`. Nothing later rewrites them.

## What happens

1. Claude checks the slug and the kind. You should now see the kind named, or one question if it was unclear.
2. Claude creates the files of the project under `projects/<slug>/`. The command touches only files and never git. You should now see the new folder with the files listed below.
3. For a thought project, Claude asks you to paste or dictate the founding brief at once and hands it to the procedure that composes a brief. You should now see the brief taken up there; [Write a brief](write-a-brief.md) says how it runs.
4. For a thought project, Claude makes the ledger once by its script. The ledger is the record of the project's state, made at read time from the documents and never kept in git. You should now see Claude propose `/forge intent` as the next step.
5. For a library, Claude proposes `/ingest` for the first documents instead. You should now see that proposal.

## What the command creates

For every project:

- `project.md`, the project file with the slug, the kind and the language.
- `.gitattributes`, from its template, with the ways of merging files by path.
- `.gitignore`, from its template. It keeps the ledger and the lock files of an open Office document (Word, PowerPoint, Excel) out of git.

For a thought project, beside them:

- The folders `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`, empty.
- The two resource indexes, `sources/00-INDEX.md` and `research/00-INDEX.md`, with their headers filled and no entries.
- `decisions.md`, with the slug filled and no records.
- The recipes `recipes/readme.md` and `recipes/release-notes.md`, each with its history companion. They produce the project's README and release notes at a release, not at this command.

For a library, beside the three common files:

- The two resource indexes.
- The recipe `recipes/readme.md` and its history companion. Its README is the catalogue of what the library holds.
- No brief, no decisions, no reviews, no challenges and no release notes.

What is not created now:

- The intent and every layer below it are born at their first `/forge <state>`.
- `logo.png` is yours to supply and is optional. The command mentions it once and never asks for it.

The full tree of both kinds is on [Repository layout](../reference/repository-layout.md). A library and what it is for are on [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

A folder `projects/<slug>/` with the files above, and for a thought project a founding brief on its way through its own procedure. The project is not under git yet. That is a property, not a defect, until you do the one-off act below.

## Put the project under git

This act is yours. Claude does not do it. Run:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. The commit identity comes from your own git configuration. The command sets none.

## If something goes wrong

- If `projects/<slug>/` already exists, the command stops and reports. It never overwrites.
- If the slug has capitals or spaces, it is not valid. Give it again in lowercase with hyphens.
- If your words do not make the kind clear, Claude asks. Answer it, and the command goes on.

## A worked example

You type:

```
/new-project my-idea
```

Claude infers a thought project, asks for the language of the chain artefacts, and you answer "English". It creates `projects/my-idea/` with `project.md` (`kind: thought`, `language: en`), the two ignore and attribute files, the five folders, the indexes, `decisions.md` and the two recipes. It asks for the founding brief, and you paste it. It makes the ledger and proposes `/forge intent`. Then you run `git -C projects/my-idea init -b main`.

For a library the same command with `lib-shared-parts` as the slug creates only the three common files, the two indexes and the README recipe with its companion, and proposes `/ingest`.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
