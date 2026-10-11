---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: d428177294646f35
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/ledger.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how you scaffold a new project with `/new-project`, either a thought project (the chain of documents) or a library (shared material only). It is for anyone who is about to forge a first thought, or to collect material for several projects. The principal is the person whose thinking is forged, and the command works for that person.

## When to use it

Use it when a new idea needs a place of its own, or when material is to be shared across projects. It creates files only. It never touches git.

## The command

```
/new-project <slug>
```

The slug is lowercase, with hyphens and no spaces. Replace `<slug>` with the name you choose.

Claude decides the kind of project from the slug and from your words:

- A thought project is the default. It holds the chain of documents.
- A library has a slug that starts with `lib-`. It holds material shared across projects and has no chain.

If your words leave the kind open, Claude asks. For a library, see [Share material through a library](share-material-through-a-library.md).

Every project also declares the language of its chain documents. It is English unless you name another. If your words leave it open, Claude asks. Both choices are written in the header of the project's ledger (the single record of the project's state):

```
project: <slug>
kind: thought
language: en
```

For why a project has one output language, see [Languages](../about/languages.md).

## What happens

### A thought project

1. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports. It never overwrites.

   You should now see the slug accepted, or a report that the folder exists.

2. Claude creates the folder structure and the first files.

   - `sources/`, `research/`, `reviews/` and `challenges/`. The first two each hold an empty index. The other two are empty.
   - `ledger.md`, with the slug, the kind, the language and today's date. The brief is listed as a 0.1 draft, pending.
   - `decisions.md`, with no records yet.
   - `recipes/readme.md` and `recipes/release-notes.md`, each with a history companion. They are the recipes that later make the README and the release notes. The command does not render them.

   You should now see these files under `projects/<slug>/`.

3. Claude asks you to paste or dictate the founding brief now. The brief is the first document of the chain. Composing it is described in [Write a brief](write-a-brief.md), not here.

   You should now see Claude asking for the brief.

4. Claude creates no intent and no lower layer. Each is born when you first run `/forge <state>` for it.

   You should now see no `10-intent.md` in the folder.

5. Claude updates the ledger and proposes the next step: run `/forge intent` to start the elicitation interview. It also reminds you that the project is not under git until you initialise its repository.

   You should now see the proposal of `/forge intent` and the reminder.

### A library

Claude creates only the following under `projects/<slug>/`:

- `ledger.md`, with `kind: library`. It keeps only the tables a library needs: renders, sources, dependencies, research and what waits on the principal.
- `sources/00-INDEX.md` and `research/00-INDEX.md`, the two empty catalogues.
- `recipes/readme.md` and its history companion `recipes/readme.history.md`. The README of a library is its catalogue.

A library has no brief, no decisions, no reviews or challenges and no release notes. Claude finishes by proposing `/ingest` for the first documents.

You should now see the library files and the proposal of `/ingest`.

## What you have afterwards

- A folder `projects/<slug>/` with the files above, and a ledger that declares the kind and the language.
- For a thought project, a brief handed to its own procedure, and a ledger row for it.
- No git repository. A project that starts without one is a property, not a defect.
- A `logo.png` is optional. You may put one in the project's root as its avatar. Claude mentions it once and never asks for it.

## The one-off act that is yours

A project is a repository of its own that the engine does not track. Initialising it and adding a remote are your one-off act:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. The commit identity is git's, resolved from your own configuration. Claude proposes none and the forge sets none. For why a project is separate from the engine, see [Projects and the engine](../about/projects-and-the-engine.md).

## If something goes wrong

- The slug names a folder that exists: Claude stops and reports. Choose another slug.
- The kind or the language is unclear: Claude asks you. Answer, and it goes on.

## A worked example

You type:

```
/new-project <slug>
```

Claude infers a thought project, asks for the language, and you answer "English". It creates `projects/<slug>/` with the ledger, the decisions file, the two indexes, the two recipes and the empty folders. It asks for the brief and hands it to the brief procedure. It ends by proposing `/forge intent` and reminding you that the project is not under git. You then run, in the shell:

```
git -C projects/<slug> init -b main
```

For `/new-project lib-<name>`, Claude infers a library from the prefix and creates the smaller set above.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for and how it is used.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own that the engine does not know.
- [Languages](../about/languages.md): why a project declares one output language and what each kind of document carries.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
