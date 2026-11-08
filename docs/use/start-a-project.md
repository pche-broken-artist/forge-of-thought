---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: b794864f2077fd54
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - templates/gitignore
  - CLAUDE.md#Persistence (git)
---

# Start a project

`/new-project` scaffolds a new project under `projects/<slug>/`: either a thought project (the chain of documents) or a library (shared material only). This page is for you, the principal (the person whose thinking is being forged), when you begin something new. Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you have an idea to forge and no project for it yet, or when you want a place to keep material that several projects share.

- A thought project holds the chain: a brief, then the intent and the layers below it.
- A library holds material only, with no chain. Its slug starts with `lib-`. What a library is for is on [Share material through a library](share-material-through-a-library.md).

## The command

```
/new-project <slug>
```

The slug is lowercase with hyphens and no spaces, for example `my-idea`. For a library it starts with `lib-`, for example `lib-shared-notes`.

## What happens

1. Claude decides the kind. It takes a library from the `lib-` prefix or from your words, and asks where it is unclear. The default is a thought project.

   You should now see the kind settled, by your words or by one question.

2. Claude settles the language of the chain's artefacts. It is English unless you name another, and Claude asks where your words leave it open. Why a project declares one output language is on [Languages](../about/languages.md).

   You should now see the language settled, by your words or by one question.

3. For a thought project, Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports. It never overwrites.

   You should now see either a report that the folder exists or the next step.

4. Claude creates the files. Only files are made; it never touches git. For every project:
   - `project.md`, the project file, from its template. It holds the slug, the kind and the language, and is written once. What it declares is on [Projects and the engine](../about/projects-and-the-engine.md).
   - `.gitattributes`, from its template.
   - `.gitignore`, from its template. It keeps the ledger (the state of the project, made when it is read) and the lock files of an open Office document out of git.

   For a thought project, beside them:
   - the folders `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`
   - `sources/00-INDEX.md` and `research/00-INDEX.md`, the two resource indexes, with the header filled and no entries
   - `decisions.md`, with the slug filled and no records
   - `recipes/readme.md` and `recipes/release-notes.md`, each with its history companion `recipes/<recipe>.history.md`

   For a library, only the three files above, plus:
   - `sources/00-INDEX.md` and `research/00-INDEX.md`
   - `recipes/readme.md` with its history companion `recipes/readme.history.md`

   A library has no brief, no decisions, no reviews or challenges and no release notes. Its README is the catalogue of what it holds. Every file of both kinds is listed on [Repository layout](../reference/repository-layout.md).

   You should now see the new folder `projects/<slug>/` with these files.

5. For a thought project, Claude asks you to paste or dictate the founding brief at once and hands it to the brief procedure. Composing it is on [Write a brief](write-a-brief.md).

   You should now see Claude asking for your brief.

6. Claude makes the ledger once, by its script. It does not create the intent or any layer below it: each is born at its first `/forge <state>`.

   You should now see the ledger made and a proposal to run `/forge intent`, which starts the elicitation interview.

7. For a library, Claude proposes `/ingest` for the first documents instead of steps 5 and 6.

   You should now see that proposal.

8. Claude mentions once that `logo.png` is yours to supply if you want a repository avatar. It is optional and Claude does not ask for it.

## What you have afterwards

A project folder with its files and no git. The project is not under git until you initialise it, and that is a property, not a defect. Initialising it is your one-off act, and the command never does it. The way in is:

```
git -C projects/<slug> init -b main
```

Add a remote afterwards if you want one. The commit identity is git's, resolved from your own configuration.

## If something goes wrong

- The folder `projects/<slug>/` already exists: the command stops and reports, and nothing is overwritten.
- The kind is unclear from your words: Claude asks.
- The language is left open by your words: Claude asks.

## A worked example

You type:

```
/new-project my-idea
```

Claude asks nothing about the kind, since the slug has no `lib-` prefix, and asks which language the artefacts are in. You answer English. Claude creates `projects/my-idea/` with the project file, `.gitattributes`, `.gitignore`, the five folders, the two resource indexes, `decisions.md` and the two recipes with their companions. It asks for your brief and hands it on. It makes the ledger and proposes `/forge intent`. Then you run:

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

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
