---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 8365868bd11bdba1
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how you scaffold a new project with `/new-project`, either a thought project (the chain of documents) or a library (shared material only). It is for you as the principal, the person whose thinking is being forged. The command creates files only and never touches git.

## When to use it

Use it when you begin a new body of thinking, or when you want a place for material that several projects share. A thought project holds the chain, from the brief onward. A library holds sources and research and has no chain. What a library is for is on [Share material through a library](share-material-through-a-library.md).

## The command

```
/new-project <slug>
```

The slug is lowercase, with hyphens and no spaces. A library takes the prefix `lib-`, for example `lib-<name>`. If a project of that slug already exists, the command stops and reports. It never overwrites.

## What happens

1. Claude decides the kind. A `lib-` prefix or your words say `library`; otherwise the kind is `thought`. Where it is unclear, Claude asks.

   You should now see the kind settled, by your words or by one question.

2. Claude settles the language of the chain's artefacts. It is English unless you name another. Where your words leave it open, Claude asks. Why a project declares one output language is on [Languages](../about/languages.md).

   You should now see the language settled.

3. Claude writes the files every project has. The kind and the language are written once into the project file.

   - `project.md`: the project file, from its template, holding the slug, the kind and the language
   - `.gitattributes`: from its template, the ways of merging files by path
   - `.gitignore`: one line, `ledger.md`, so that the ledger stays out of git

   The ledger is the state of the project, made on demand by a script from the documents, never written by hand.

   You should now see these three files in `projects/<slug>/`.

4. For a thought project, Claude adds the working folders and records.

   - `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the two resource indexes, with a header and no entries
   - `decisions.md`: with the slug filled in and no records
   - `recipes/readme.md` and `recipes/release-notes.md`, each with its history companion `recipes/<recipe>.history.md`

   The renders of those two recipes are made later, at a release, not by this command.

   You should now see the folders and files listed above.

5. For a library, Claude adds only the indexes and the readme recipe.

   - `sources/00-INDEX.md` and `research/00-INDEX.md`
   - `recipes/readme.md` and its companion `recipes/readme.history.md`, whose README is the catalogue of what the library holds

   A library has no brief, no decisions, no reviews or challenges and no release notes. Claude proposes `/ingest` for the first documents, and steps 6 to 8 do not apply.

   You should now see the library with its two indexes and the readme recipe.

6. For a thought project, Claude asks you at once for the founding brief, to paste or to dictate, and hands it to the brief procedure. How the brief is composed is on [Write a brief](write-a-brief.md).

   You should now see the brief taken up and the question of whether the text is finished.

7. Claude makes the ledger once, with its script. The intent and every layer below it are not created now. Each is born at its first `/forge <state>`.

   You should now see a `ledger.md` in the project.

8. Claude proposes the next step, `/forge intent`, to start the elicitation interview. It also reminds you that the project is not under git until you initialise its repository.

   You should now see that proposal and that reminder.

## What you have afterwards

A project folder under `projects/<slug>/` holding the files above. `logo.png` is optional and yours to supply; Claude mentions it once and does not ask for it. Every file of a thought project and of a library is listed on [Repository layout](../reference/repository-layout.md).

## The one step that is yours

A project is a repository of its own that the engine does not track. Starting it under git is your one-off act, and the command does not do it:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. A project that starts without git is not defective. Why a project is a repository of its own, and what its project file declares, is on [Projects and the engine](../about/projects-and-the-engine.md).

## If something goes wrong

- The slug is already taken: the command stops and reports, and nothing is overwritten. Choose another slug.
- The slug is not lowercase with hyphens: the command asks for a valid one.

## A worked example

You type:

```
/new-project <slug>
```

Claude asks nothing about the kind, because the slug has no `lib-` prefix and your words say nothing else. You said "in German", so the language is settled. It writes `project.md` with `kind: thought` and `language: de`, then `.gitattributes`, `.gitignore`, the folders, the two indexes, `decisions.md` and the two recipes. It asks for the brief, you paste it, and the brief procedure takes it. Claude makes the ledger and proposes `/forge intent`. You then run:

```
git -C projects/<slug> init -b main
```

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
