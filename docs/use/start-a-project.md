---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: e9be4072bfb16224
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - templates/gitignore
  - CLAUDE.md#Persistence (git)
---

# Start a project

`/new-project <slug>` scaffolds a new project under `projects/<slug>/`:
either a thought project (the chain of documents) or a library
(material shared across projects, no chain). This page is for you, the
principal (the person whose thinking is being forged), when you begin
something new.

## When to use it

Use it when you have an idea to forge and no project for it yet, or
when you want a place to keep material that several projects share.
The command creates files only. It never touches git.

## The command

```
/new-project my-idea
```

For a library, the slug starts with `lib-`:

```
/new-project lib-templates
```

The slug is lowercase with hyphens and no spaces. Replace `my-idea`
with your own slug.

## What happens

1. Claude decides the kind. A slug with the `lib-` prefix, or your
   words, make it a library. Otherwise it is a thought project. Where
   this is unclear, Claude asks.

   You should now see the kind settled, by your words or by one
   question.

2. Claude decides the language of the chain artefacts (the intent and
   the layers below it). The default is English. Where your words
   leave it open, Claude asks. Learn why a project declares one
   language in [Languages](../about/languages.md).

   You should now see the language settled, by your words or by one
   question.

3. Claude checks the slug. If `projects/<slug>/` already exists, it
   stops and reports. It never overwrites.

   You should now see either the next step or a report that the
   folder exists.

4. Claude creates the files. Every project gets three:
   - `project.md` from its template, holding the slug, the kind and
     the language. It is written once, here, and the kind and the
     language are recorded in it.
   - `.gitattributes` from its template.
   - `.gitignore` from its template. It keeps the ledger (the
     project's state, made when it is read, never kept in git) and
     the lock files of an open Office document out of git.

   You should now see these three files in `projects/<slug>/`.

5. For a thought project, Claude creates beside them:
   - the folders `sources/`, `reviews/`, `challenges/`, `research/`
     and `threads/`, empty
   - `sources/00-INDEX.md` and `research/00-INDEX.md`, the two
     resource indexes, with a header and no entries
   - `decisions.md`, with the slug filled in and no records
   - `recipes/readme.md` and `recipes/release-notes.md`, the recipes
     of the project's README and release notes, each with its history
     companion in `recipes/`

   You should now see these folders and files. The README and the
   release notes themselves are not made now. A release makes them.

6. For a library, Claude creates only the two resource indexes and
   `recipes/readme.md` with its history companion, since a library's
   README is its catalogue. A library has no brief, no decisions, no
   reviews, no challenges and no release notes. Claude then proposes
   `/ingest` for the first documents. What a library is for is on
   [Share material through a library](share-material-through-a-library.md).

   You should now see the indexes and the README recipe, and a
   proposal to bring in your first documents.

7. For a thought project, Claude asks you to paste or dictate the
   founding brief now and hands it to the brief procedure. How the
   brief is composed is on [Write a brief](write-a-brief.md).

   You should now see the brief taken in hand, as that page describes.

8. For a thought project, Claude makes the ledger once with its
   script and proposes `/forge intent` as the next step, which starts
   the elicitation interview.

   You should now see a proposal to run `/forge intent`.

## What you have afterwards

- A folder `projects/<slug>/` with the files above. For every
  project that includes the project file, so the kind and language
  are fixed.
- No intent and no layer below it. Each is born from its own first
  `/forge <state>`.
- No `logo.png`. The repository avatar is optional and yours to
  supply. Claude mentions it once and does not ask for it.
- A project that is not yet under git. This is a property of a new
  project, not a defect. Claude says so once at the end.

For every file of a thought project and of a library, see
[Repository layout](../reference/repository-layout.md).

## Your one-off act: git

A project is a repository of its own that the engine does not track.
Making it one is your act, done once, after the command:

```
git -C projects/my-idea init -b main
```

Add a remote afterwards if you want one. The commit identity is git's
own, resolved per host from your configuration, so the command
proposes none. Why a project is a repository of its own, and what its
project file declares, is on
[Projects and the engine](../about/projects-and-the-engine.md).

## If something goes wrong

- The folder `projects/<slug>/` exists already: the command stops and
  reports. Choose another slug. It never overwrites.
- The slug is not lowercase with hyphens, or holds a space: the slug
  is refused. Write it again in that form.

## A worked example

You type:

```
/new-project my-idea
```

Your words leave the language open, so Claude asks for it, and you
answer English. Claude writes `project.md` with `project: my-idea`,
`kind: thought` and `language: en`, then `.gitattributes`,
`.gitignore`, the folders, the two indexes, `decisions.md` and the
two recipes with their history companions. It asks for the brief, and
you paste it. It makes the ledger and proposes `/forge intent`. You
then run:

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

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
