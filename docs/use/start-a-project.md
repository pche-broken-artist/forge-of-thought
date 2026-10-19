---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: f3c8f5dca1853ec0
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how to scaffold a new project with `/new-project`: either a thought project (the chain of documents from a brief onward) or a library (shared material, no chain). It is for you as the principal, the person whose thinking is being forged.

## When to use it

Use it when you begin a new body of work and nothing exists yet under `projects/<slug>/`. A thought project holds an idea as it travels the chain. A library holds material that several projects share; [Share material through a library](share-material-through-a-library.md) says what it is for.

## The command

```
/new-project <slug>
```

The slug is lowercase, with hyphens and no spaces. A library has the prefix `lib-`, for example `lib-<name>`.

## What happens

1. Claude decides the kind. A `lib-` prefix or your words make it a library; otherwise it is a thought project. When this is unclear, Claude asks.

   You should now see the kind named, or one question about it.

2. Claude decides the language of the chain's artefacts. It is English unless you name another. When your words leave it open, Claude asks. [Languages](../about/languages.md) says why a project declares one output language.

   You should now see the language settled.

3. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports. It never overwrites.

   You should now see either a stop with a report or the files appearing.

4. Claude writes the files. They are the same for every project:
   - `project.md`: the project file, made from its template, holding the slug, the kind and the language. It is written once, when the project is created.
   - `.gitattributes`: made from its template; it sets the ways of merging by path.
   - `.gitignore`: it keeps the ledger out of git.

   For a thought project it also creates:
   - the folders `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`, all empty
   - `sources/00-INDEX.md` and `research/00-INDEX.md`, the two resource indexes, with their headers filled and no entries
   - `decisions.md`, with the slug filled and no records
   - `recipes/readme.md` and `recipes/release-notes.md`, each with a history companion `recipes/<recipe>.history.md`

   For a library it creates only the two resource indexes and `recipes/readme.md` with its history companion. A library has no brief, no decisions, no reviews, no challenges and no release notes.

   You should now see the new folder `projects/<slug>/` with these files.

5. Thought project only: Claude asks you to paste or dictate the founding brief now, and hands it to the brief procedure. [Write a brief](write-a-brief.md) describes how the brief is composed.

   You should now see the brief file created, or the brief left for later.

6. Thought project only: the intent and every layer below it are not created. Each is born from its own first `/forge <state>`.

   You should now see no `10-intent.md` yet. That is as intended.

7. Thought project only: Claude makes the ledger once with `python scripts/forge-ledger.py <slug>`. The ledger is made by this script and never written by hand.

   You should now see a ledger for the new project.

8. Claude closes with a proposal. For a thought project it proposes `/forge intent`, to start the elicitation interview. For a library it proposes `/ingest` for the first documents.

   You should now see the proposed next step and a reminder that the project is not under git yet.

## What you have afterwards

A folder `projects/<slug>/` with the files above. The project is not under git: the command works on files only and never runs git. A project without git is a property, not a defect.

`logo.png` is optional. You may place it in the project root as the repository avatar; Claude mentions it once and never asks for it.

[Repository layout](../reference/repository-layout.md) lists every file of a thought project and of a library. [Projects and the engine](../about/projects-and-the-engine.md) says why a project is a repository of its own and what its project file declares. [Glossary](../reference/glossary.md) gives every term of the forge in one line.

## The step that is yours

Initialising the repository and adding a remote are your one-off act. To initialise the repository:

```
git -C projects/<slug> init -b main
```

Add a remote afterwards if you want one. The commit identity is git's, taken from your own git configuration; the forge sets none.

## If something goes wrong

- The slug names a folder that exists: Claude stops and reports, and changes nothing. Choose another slug.
- The kind or the language is unclear: Claude asks. Answer it, and the command continues.

## A worked example

You type:

```
/new-project my-idea
```

Claude infers a thought project, asks for the language, and you answer "English". It creates `projects/my-idea/` with `project.md`, `.gitattributes`, `.gitignore`, the five folders, the two indexes, `decisions.md` and the two recipes. It asks for the founding brief, you paste it, and the brief procedure takes it. It makes the ledger and proposes `/forge intent`. You then run:

```
git -C projects/my-idea init -b main
```

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
