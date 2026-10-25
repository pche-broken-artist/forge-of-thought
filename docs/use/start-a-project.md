---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: d653610e30056720
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how to scaffold a new project with `/new-project`: either a thought project (the chain of documents) or a library (shared material only). It is for you, the person who starts one. Throughout, "the principal" means whoever's thinking is being forged, and that is you.

## When to use it

Use it when you begin a new line of thinking and want a place for it, or when you want a library of material that several projects share. Run it once per project. The command never overwrites: if the project already exists, it stops and says so.

## The command

```
/new-project <slug>
```

The slug is lowercase with hyphens and no spaces. A slug that starts with `lib-` makes a library, and any other slug makes a thought project. If your words leave the kind open, Claude asks. It also asks for the language of the chain artefacts (the documents of the chain, such as the intent) where your words leave that open. The default is English.

The command creates files only. It never touches git.

## What happens

1. Claude checks the slug and the kind.
   You should now see no question left open about the kind and the language, and no stop for an existing project.
2. Claude writes the project file `projects/<slug>/project.md` from its template. It holds the slug, the kind and the language, and it is written once.
   You should now see `project.md` with those three values.
3. Claude writes the two files every project has: `.gitattributes` from its template, and a `.gitignore` with the single line `ledger.md`. The ledger (the single source of truth for state) is made when it is read, by a script, and never kept in git.
   You should now see both files in the project folder.
4. For a thought project, Claude creates the rest of the scaffold:
   - the empty folders `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`
   - `sources/00-INDEX.md` and `research/00-INDEX.md`, the two resource indexes, with their headers filled and no entries
   - `decisions.md`, with the slug filled in
   - `recipes/readme.md` and `recipes/release-notes.md`, each with a history companion beside it

   You should now see these folders and files under `projects/<slug>/`.
5. For a library, Claude creates only the two indexes `sources/00-INDEX.md` and `research/00-INDEX.md`, plus `recipes/readme.md` with its history companion `recipes/readme.history.md`. The README of a library is its catalogue. A library has no brief, no decisions, no reviews or challenges and no release notes. Claude then proposes `/ingest` for the first documents, and the remaining steps do not apply.
   You should now see the three common files, the two indexes and the readme recipe.
6. For a thought project, Claude asks you to paste or dictate the founding brief at once and hands it to the brief procedure. How the brief is composed is on [Write a brief](write-a-brief.md).
   You should now see the brief taken in hand.
7. Claude does not create the intent or any layer below it. Each is born at its first `/forge <state>`.
   You should now see no `10-intent.md` yet.
8. Claude makes the ledger once with its script and proposes the next step, `/forge intent`, which starts the elicitation interview.
   You should now see a `ledger.md` in the project folder and the proposal of the next step.

## What you have afterwards

A folder `projects/<slug>/` with the files above and no git repository. A project starts "not under git", which is a property and not a defect. Claude says so once at the end.

`logo.png` is optional. If you want a repository avatar, put it in the project root yourself. Claude mentions it once and never asks for it.

## The one act that is yours

A project is a repository of its own that the engine does not track. Initialising it and adding a remote are your one-off act, and the command does not do them. The way in is:

```
git -C projects/<slug> init -b main
```

Add a remote afterwards if you want one. The commit identity is git's, resolved on each host from your own git configuration, and the forge sets none. After this first act, the forge's scripts are the door to every write of git.

## If something goes wrong

- The project already exists: the command stops and reports. It never overwrites, so choose another slug or leave the existing project as it is.
- The slug is not lowercase with hyphens, or has spaces: Claude does not scaffold it. Give a slug in the right form.
- The kind is unclear from your words: Claude asks. Answer with `thought` or `library`.

## A worked example

You want a new thought project and give it the slug `my-idea`.

```
/new-project my-idea
```

Claude asks which language the chain artefacts are in, and you answer "English". It writes `projects/my-idea/project.md` with `kind: thought` and `language: en`, creates the folders, indexes, `decisions.md` and the two recipes, and asks for your brief. You paste it. Claude hands it on, makes the ledger and proposes `/forge intent`. You then run, once:

```
git -C projects/my-idea init -b main
```

For a library you would run `/new-project lib-shared-notes` instead. See [Share material through a library](share-material-through-a-library.md) for what a library is for.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
