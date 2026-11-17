---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: ecd785acb9003866
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - templates/gitignore
---

# Start a project

This page shows how to scaffold a new thought project or a library with `/new-project`. It is for the principal, the person whose thinking is forged, who is starting a new body of work.

## When to use it

Use it when you begin a new piece of work. A thought project holds the chain of documents from the brief onward. A library (slug prefix `lib-`) holds material only, shared across projects: see [Share material through a library](share-material-through-a-library.md). Why a project is a repository of its own is explained in [Projects and the engine](../about/projects-and-the-engine.md).

## The command

```
/new-project <slug>
```

The slug is lowercase with hyphens and no spaces. For a library, start it with `lib-`, for example `lib-<name>`.

## What happens

1. Claude decides the kind. It takes `library` from the `lib-` prefix or from your words, and `thought` otherwise. Where it is unclear, it asks.

   You should now see the kind settled, with a question only if your words left it open.

2. Claude settles the language of the chain artefacts. The default is English. It asks only where your words leave the language open. Why a project declares one language is explained in [Languages](../about/languages.md).

   You should now see the language settled.

3. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports. It never overwrites.

   You should now see either a new folder or a report that the slug is taken.

4. Claude creates the files, and only files. It never touches git. Every project gets:
   - `project.md`: the project file, with the slug, the kind and the language, written once
   - `.gitattributes`, made from its template
   - `.gitignore`, made from its template: it keeps the ledger and the lock files of an open Office document out of git

   A thought project also gets:
   - `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`
   - the two resource indexes, `sources/00-INDEX.md` and `research/00-INDEX.md`
   - `decisions.md`
   - the readme and release-notes recipes in `recipes/`, each with its history companion

   A library gets only the two indexes and the readme recipe with its history companion, besides the three files every project gets. Every file is listed in [Repository layout](../reference/repository-layout.md).

   You should now see these files under `projects/<slug>/`.

5. For a thought project, Claude asks you to paste or dictate the founding brief at once and hands it to the brief procedure. How the brief is composed is described in [Write a brief](write-a-brief.md).

   You should now see Claude taking your brief text.

6. For a thought project, Claude makes the ledger once with its script. The intent and the layers below it are not created now. Each is born at its first `/forge <state>`.

   You should now see Claude propose `/forge intent` as the next step.

7. For a library, Claude proposes `/ingest` for the first documents instead of steps 5 and 6.

   You should now see that proposal.

## What you have afterwards

A folder `projects/<slug>/` with the files above, and a new project that is not under git. That is a property, not a defect. A `logo.png` is optional: put it in the project folder if you want one. Claude mentions it once and does not ask for it.

The one act that is yours is to initialise the repository, and then to add a remote if you want one:

```
git -C projects/<slug> init -b main
```

## If something goes wrong

- The slug already exists: Claude stops and reports. Choose another slug, or work in the existing project.
- The slug has capitals or spaces: the command wants lowercase with hyphens.

## A worked example

You type:

```
/new-project my-idea
```

Your words do not name a language, so Claude asks. You answer "English". Claude creates `projects/my-idea/` with the project file, the two git files, the folders, the two indexes, `decisions.md` and the two recipes. It asks for the founding brief, and you paste it. Claude makes the ledger and proposes `/forge intent`. You then run `git -C projects/my-idea init -b main`.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
