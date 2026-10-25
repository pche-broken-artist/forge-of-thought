---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: fd4d418dd8aeba62
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project of its own kind that holds material shared
across projects: documents, templates, graphics and research, with no
chain of artefacts. This page is for you if you want to keep such
material in one place and use it from several projects without
copying it. It shows how a library is made, how documents enter it,
how a project cites one of them, and how you find out which libraries
a project needs. The principal (the person whose thinking is being
forged) decides what goes into a library and what each document is
for. Why a library is a kind of project is explained in
[Projects and the engine](../about/projects-and-the-engine.md); every
term of the forge has its line in the [Glossary](../reference/glossary.md).

## When to use it

- Several projects need the same document, such as a deck template, a
  standard or a piece of research.
- You want to move a document out of one project so that others can
  use it too.
- A project's state map lists a library that is not on your machine.

## The command

```
/new-project lib-<name>
```

The prefix `lib-` makes the project a library. A project's kind is
declared as `kind: library` in its project file (`project.md`).

## What happens

1. **The library is made.** `/new-project lib-<name>` creates
   `projects/lib-<name>/` with only these files:
   - `project.md`: the project file, with the slug, the kind
     `library` and the language;
   - `.gitattributes`: the ways git merges files by path;
   - `.gitignore`: with the line `ledger.md`;
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the two
     resource indexes, empty;
   - `recipes/readme.md` and its history companion
     `recipes/readme.history.md`: the recipe of the library's README.

   The library gets no brief, no decisions, no reviews or challenges
   and no release notes. Its README is a catalogue of what it holds,
   made from the ledger and the two indexes. The ledger (the one
   record of a project's state) is made at read time by
   `python scripts/forge-ledger.py lib-<name>`, as for every project,
   and is never kept in git. The command touches no git: the library
   is "not under git" until you initialise its repository, and that is
   a property, not a defect.

   You should now see the folder `projects/lib-<name>/` with these
   files, and a proposal to run `/ingest` for the first documents.

2. **Documents enter the library.** You register each document with
   `/ingest`, exactly as in any project; how that runs is on
   [Register a source](register-a-source.md). Claude asks what each
   document is for before it writes the index entry. A binary you
   keep as a functional thing (a deck template, a graphic, a logo) is
   stored as it is, with no Markdown extract.

   You should now see the document in `projects/lib-<name>/sources/`
   and its entry in `sources/00-INDEX.md`.

3. **A changed document is maintenance.** In a library the owner keeps
   the documents up to date. When you run a bare `/ingest` in the
   library, Claude reports each document changed since its
   registration and asks what to do with it. In a library the answer
   is ordinary upkeep: the index entry is updated, its Date included,
   and nothing else. A thought project treats the same change
   differently, as a breach of a source's immutability.

   You should now see the changed document's index entry carry the
   new Date.

4. **A project cites a library document.** You point the project at
   the document's path with `/ingest`. Nothing is copied into the
   project's `sources/`. Claude adds an index entry that names the
   path, such as `projects/lib-<name>/sources/<file>`, and says what
   it is for. The ledger finds the citation by itself and lists it in
   its Dependencies table. Nobody writes that row.

   You should now see the new entry in the project's
   `sources/00-INDEX.md`, naming the library path, and the library in
   the Dependencies table of the project's ledger.

5. **Moving a document into a library.** This is the reverse of step
   4. You ingest the document into the library, then the project's
   own entry is replaced by the citation of the library path.

   You should now see the document in the library's `sources/` and a
   citation in place of the project's own entry.

6. **You see which libraries a project needs.** A bare `/forge` in a
   project reports its state map. One of its lines names the libraries
   the project needs, from the ledger's Dependencies table, and says
   whether each is cloned alongside. In a library itself, `/forge`
   reports the sources and research and the git state, and stops
   there: a library has no chain and no next step beyond `/ingest`.

   You should now see each library the project cites, marked as
   cloned alongside or not.

## What you have afterwards

- A library under `projects/lib-<name>/` with its project file, its
  indexes and its README recipe.
- Its documents registered in its `sources/` and `research/`, each
  with an index entry.
- In every project that uses one of them, an index entry naming the
  library path, and the library listed in that project's ledger under
  Dependencies.

## If something goes wrong

- **A library is not cloned alongside.** The light check (the check
  of a project's bookkeeping, fit for a save) verifies that every path
  in the Dependencies table exists on disk. A missing library is
  reported as a finding: the library `<name>` is not cloned alongside,
  and you bring it in with `/import-project` and its remote. The
  finding is advisory. How a project is cloned in is on
  [Bring in an existing project](bring-in-an-existing-project.md).
- **The slug has no `lib-` prefix and the kind is unclear.** Claude
  asks whether the new project is a thought project or a library
  before it creates anything.

## A worked example

You keep a deck template that two projects use.

1. Make the library:

   ```
   /new-project lib-<name>
   ```

   `projects/lib-<name>/` appears with `project.md`, `.gitattributes`,
   `.gitignore`, the two indexes and the readme recipe.

2. Register the template in the library:

   ```
   /ingest deck-template.potx lib-<name>
   ```

   Claude asks whether to convert it to Markdown; you answer no,
   because it is a functional file. It asks what the file is for; you
   answer "the deck template of our pitches". The file lands in
   `projects/lib-<name>/sources/deck-template.potx` with its index
   entry.

3. Point a project at it:

   ```
   /ingest projects/lib-<name>/sources/deck-template.potx <slug>
   ```

   Nothing is copied. The project's `sources/00-INDEX.md` gains an
   entry naming the path and its purpose, and the ledger of `<slug>`
   lists `lib-<name>` under Dependencies.

4. Run `/forge <slug>`. The state map says that the project needs
   `lib-<name>` and whether it is cloned alongside.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why
  a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
