---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 0a79355b14eaaedb
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project of kind `library` that holds material shared
across projects and has no chain of documents of its own. This page
is for the person who keeps such material in one place and wants
other projects to use it. It shows how a library is made, how
documents enter it and how a project cites them.

## When to use it

Use a library when several projects need the same documents. A deck
template, a graphic or a shared reference are such documents. A
project does not copy them. It cites them by their path in the
library.

Why a library is a kind of project of its own is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## The command

```
/new-project lib-<name>
```

The slug starts with `lib-`. Claude infers the kind `library` from
that prefix.

## What happens

1. **The library is made.** `/new-project lib-<name>` creates the
   folder `projects/lib-<name>/` with these files and nothing else:
   - `project.md`: the project file, with the slug, the kind
     `library` and the language.
   - `.gitattributes`: the ways git merges the files by path.
   - `.gitignore`: one line, `ledger.md`.
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the two
     resource indexes, empty.
   - `recipes/readme.md` with its history companion
     `recipes/readme.history.md`: the recipe of the library's README.

   A library gets no brief, no decisions, no reviews, no challenges
   and no release notes. Its README is a catalogue of what it holds,
   made from the recipe. The recipe's inputs are the ledger and the two
   indexes. The ledger is the state record of a project. It is made at
   read time by `python scripts/forge-ledger.py lib-<name>`, as for
   every project, and it is never kept in git. The command writes files
   only and never touches git. A library that starts "not under git" is
   a property, not a defect.
   You should now see `projects/lib-<name>/` with those files, and
   Claude proposing `/ingest` for the first documents.

2. **Documents enter the library.** Each document is registered with
   `/ingest <file> lib-<name>`, the same way a source enters any
   project (see [Register a source](register-a-source.md)). Claude asks
   what the document is for before it writes the index entry. For a
   binary file it asks whether to convert it to Markdown. A deck
   template or a graphic is kept as it is: the binary itself is the
   source.
   You should now see the document in `sources/` of the library and
   its entry in `sources/00-INDEX.md`.

3. **A changed document is kept up to date.** In a library, a
   document that changes is the owner's ordinary maintenance, not a
   breach. Run `/ingest lib-<name>` with no file. Claude reports the
   files changed since their registration and asks what to do with
   each. For a library it updates the index entry, its Date included,
   and nothing else.
   You should now see the changed document's entry with a new Date.

4. **A project cites a library document.** Point the project at the
   document by its path, for example
   `/ingest projects/lib-<name>/sources/<file> <slug>`. Nothing is
   copied into the project's `sources/`. Claude adds an index entry
   that names the path and says what the document is for. The ledger
   finds the citation by itself and lists it in its Dependencies
   table.
   You should now see the entry with the library path in the
   project's `sources/00-INDEX.md`.

5. **The project's state map shows the libraries.** Run
   `/forge <slug>`. The state map says which libraries the project
   needs, from the ledger's Dependencies table, and whether each is
   cloned alongside it. Run on the library itself, `/forge lib-<name>`
   reports its sources and research and stops: a library has no chain
   and no next step beyond `/ingest`.
   You should now see each library the project cites, with whether it
   is present beside the project.

## What you have afterwards

- A library `projects/lib-<name>/` with its documents registered in
  its indexes and a README that catalogues them.
- A project whose index cites the library documents by path, and
  whose ledger lists them as dependencies.

## If something goes wrong

- **A library the project cites is not there.** The light check
  verifies that every path in the Dependencies table exists on disk.
  A missing library is reported as an advisory finding: the library is
  not cloned alongside, and the way to bring it in is
  `/import-project <its remote>`. How that works is on
  [Bring in an existing project](bring-in-an-existing-project.md).
- **The kind is unclear.** If the slug has no `lib-` prefix and your
  words leave it open, Claude asks whether the project is a library.
- **You want to move a document out of a project into a library.**
  Ingest it in the library, then replace the project's entry with the
  citation of its new path.

## A worked example

You keep a shared deck template for several projects.

1. `/new-project lib-<name>` creates `projects/lib-<name>/` with its
   project file, `.gitattributes`, `.gitignore`, the two indexes and
   the readme recipe.
2. `/ingest <template-file> lib-<name>` stores the template. Asked
   whether to convert it, you say no: the template is used as it is.
   Asked what it is for, you answer with its role. The entry appears
   in `projects/lib-<name>/sources/00-INDEX.md`.
3. In a project `<slug>`, `/ingest projects/lib-<name>/sources/<template-file> <slug>`
   adds an entry that names that path. Nothing is copied.
4. `/forge <slug>` lists `lib-<name>` among the libraries the project
   needs and says it is cloned alongside.

For every term used here in one line, see the
[Glossary](../reference/glossary.md).

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why
  a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
