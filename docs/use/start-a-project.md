---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 5e275cf69a60243c
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/ledger.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how to scaffold a new project with `/new-project`, either a thought project (the chain of documents) or a library (shared material only). It is for you as the principal, the person whose thinking is being forged.

## When to use it

Use it when you begin a new body of thinking, or when you want a place to keep material that several projects share. A project is a repository of its own under `projects/`.

## The command

```
/new-project <slug>
```

The slug is lowercase with hyphens and no spaces. Claude takes the kind from the slug and from your words:

- A slug with the prefix `lib-` is a library: material shared across projects, with no chain.
- Any other slug is a thought project, the default.

Claude asks when your words leave the kind unclear. It also asks which language the chain artefacts are written in when your words leave that open, and assumes English unless you name another.

The kind and the language are declared in the header of the project's ledger, the file that holds the project's state. The header carries `kind:` (`thought` or `library`) and `language:` (an ISO 639-1 code such as `en`).

## What happens

The command creates files only. It never touches git.

1. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports. It never overwrites.

   You should now see either a stop with a report, or the work going ahead.

2. Claude creates the files of the kind.

   For a thought project:

   - `sources/`, `reviews/`, `challenges/` and `research/`, empty except for a `00-INDEX.md` in `sources/` and in `research/`
   - `ledger.md`, with the slug, `kind: thought`, the language and today's date, and the brief row as a 0.1 draft, pending
   - `decisions.md`, with the slug filled and no sample record
   - `recipes/readme.md` and `recipes/release-notes.md`, each with its history companion

   For a library:

   - `ledger.md` with `kind: library`, reduced to the tables a library keeps (Renders, Sources, Dependencies, Research and Waiting on principal)
   - `sources/00-INDEX.md` and `research/00-INDEX.md`
   - `recipes/readme.md` with its history companion, the recipe of the library's README, which is its catalogue

   A library has no brief, no decisions, no reviews or challenges and no release notes.

   You should now see the new folder `projects/<slug>/` with these files.

3. For a thought project, Claude asks you to paste or dictate the founding brief now and hands it to the brief procedure. How the brief is composed is described in [Write a brief](write-a-brief.md).

   You should now see a brief file in the project and its row in the ledger.

4. Claude creates no intent and no layer below it. Each is born at its own first `/forge <state>`, so the first one is `/forge intent`, which starts the elicitation interview.

   You should now see Claude propose `/forge intent` as the next step.

5. For a library, Claude finishes by proposing `/ingest` for the first documents. The brief step and the intent do not apply.

   You should now see Claude propose `/ingest`.

## What you have afterwards

- A project folder holding the files of its kind.
- A project that is not under git yet. A project that starts without git is a property, not a defect, and Claude tells you so once at the end.
- Optionally a `logo.png` in the project root as the repository avatar. You supply it. Claude mentions it once and never asks for it.

## Put it under git

Initialising the repository and adding a remote are your one-off act. The command does neither. The way in is:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. The commit identity is git's, resolved per host from your own git configuration. Neither the command nor the scripts set an identity or carry a URL.

## If something goes wrong

- The command stops and reports when `projects/<slug>/` already exists. Choose another slug or leave the existing project as it is.
- When the slug or your words leave the kind or the language open, Claude asks. Answer once and the command goes on.

## A worked example

You type:

```
/new-project my-idea
```

Claude infers a thought project from the slug and asks for the language. You answer "English". It creates `projects/my-idea/` with the files above and asks for the brief. You paste your text, and the brief procedure stores it. Claude ends by proposing `/forge intent` and reminds you that the project is not under git. You then run:

```
git -C projects/my-idea init -b main
```

For a library the same command with a slug such as `lib-shared` creates only the reduced ledger, the two indexes and the README recipe, and Claude proposes `/ingest`.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own.
- [Languages](../about/languages.md): why a project declares one output language.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
