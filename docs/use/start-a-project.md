---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 1e65f008ab606716
inputs:
  - .claude/skills/new-project/SKILL.md
  - templates/project.md
  - CLAUDE.md#Persistence (git)
---

# Start a project

This page shows how to scaffold a new project with `/new-project`, either a thought project (the chain of documents) or a library (shared material only). It is for you as the principal, the person whose thinking is forged. Claude is the assistant that runs the command.

## When to use it

Use it when you begin a new body of work, or when you want a place to keep material that several projects share. A thought project holds a chain of versioned documents. A library holds material only and has no chain; see [Share material through a library](share-material-through-a-library.md) for what a library is for.

## The command

```
/new-project <slug>
```

The slug is lowercase with hyphens and no spaces. A library takes the prefix `lib-`, as in `lib-<name>`.

## What happens

1. Claude decides the kind. It takes a library from the `lib-` prefix or from your words, and a thought project otherwise. If your words leave the kind open, it asks.

   You should now see the kind settled, or a question about it.

2. Claude decides the language of the chain's documents. It is English unless you name another. If your words leave it open, it asks. A project declares one output language; [Languages](../about/languages.md) gives the reason.

   You should now see the language settled, or a question about it.

3. Claude checks the slug. If `projects/<slug>/` already exists, it stops and reports; it never overwrites.

   You should now see either a stop with a report, or the work going on.

4. Claude creates the files. The kind and the language are written once into the project file `project.md`. Nothing is created in git; the command makes files only.

   For every project it creates:
   - `project.md`, the project file with the slug, the kind and the language
   - `.gitattributes`, from its template, which sets the ways of merging by path
   - `.gitignore`, with the line `ledger.md`, so that the ledger stays out of git

   For a thought project it creates, beside these:
   - `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`
   - `sources/00-INDEX.md` and `research/00-INDEX.md`, the two resource indexes, with the header filled and no entries
   - `decisions.md`, with the slug filled in
   - `recipes/readme.md` and `recipes/release-notes.md`, the recipes for the README and the release notes
   - a history companion for each recipe, `recipes/readme.history.md` and `recipes/release-notes.history.md`

   For a library it creates only:
   - the two resource indexes
   - `recipes/readme.md`, the recipe for the README, which is the library's catalogue
   - its history companion `recipes/readme.history.md`

   You should now see the new folder `projects/<slug>/` with these files.

5. For a thought project, Claude asks you at once for the founding brief, to paste or to dictate. It hands the text to the brief procedure; [Write a brief](write-a-brief.md) describes it.

   You should now see Claude asking for the brief.

6. Claude makes the ledger once with its script, `python scripts/forge-ledger.py <slug>`. The ledger is the state report of the project, made at read time and never written by hand.

   You should now see a `ledger.md` in the project, which git ignores.

7. Claude proposes the next step. For a thought project it is `/forge intent`, which starts the elicitation interview. For a library it is `/ingest`, for the first documents.

   You should now see that proposal.

## What you have afterwards

- The files listed above, and nothing else. The intent and every layer below it do not exist yet; each is born at its first `/forge <state>`.
- A project that is not under git. That is a property, not a defect.
- No `logo.png`. It is optional, the avatar of the repository, and you supply it if you want one.

## What you do yourself

Putting the project under git is your one-off act. The command never does it. Run:

```
git -C projects/<slug> init -b main
```

Then add a remote if you want one. Until you have run the first line, the project is not under git.

## If something goes wrong

- The slug names a folder that already exists: Claude stops and reports. Choose another slug, or leave the existing project alone.
- The slug has capitals or spaces: Claude asks for a slug in lowercase with hyphens.

## A worked example

You type:

```
/new-project my-idea
```

Claude takes a thought project, since there is no `lib-` prefix. You say the documents should be in English, and Claude writes `project.md` with the kind `thought` and the language `en`. It creates the folders and files listed above and asks you for the founding brief. You paste the brief, and the brief procedure takes it from there. Claude makes the ledger and proposes `/forge intent`. At the end it reminds you that the project is not under git. You run `git -C projects/my-idea init -b main`.

For a library you would type `/new-project lib-my-material`. Claude would create only the common files, the two indexes and the README recipe with its history, and would propose `/ingest`.

## See also

- [Write a brief](write-a-brief.md): composing the founding brief.
- [Share material through a library](share-material-through-a-library.md): what a library is for.
- [Projects and the engine](../about/projects-and-the-engine.md): why a project is a repository of its own and what its project file declares.
- [Languages](../about/languages.md): why a project declares one output language.
- [Repository layout](../reference/repository-layout.md): every file of a thought project and of a library.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
