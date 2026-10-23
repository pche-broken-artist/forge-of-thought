---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 50f8ae6e44041a78
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project that holds material shared across projects
and has no chain of documents of its own. This page is for you, the
principal (the person whose thinking the forge works on), when the
same documents serve more than one project. It shows how to create a
library, put documents into it, keep them up to date and cite them
from a project.

## When to use it

Use a library when a document, a template or a piece of research is
needed by several projects. Each project then cites the library's
file by its path instead of keeping a copy of its own. Why a library
is a kind of project, and not something else, is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## The command

```
/new-project lib-<name>
```

The prefix `lib-` tells Claude that the project is a library. The
other commands of this job are `/ingest`, `/forge` and
`/import-project`, shown in the steps below.

## What happens

1. **Create the library.** Run `/new-project lib-<name>`. Claude
   reads the kind `library` from the `lib-` prefix or from your
   words, and asks when it is unclear. It creates only these files
   under `projects/lib-<name>/`:
   - `project.md`: the project file, with the slug, the kind
     `library` and the language.
   - `.gitattributes`: the ways git merges the files by path.
   - `.gitignore`: one line, `ledger.md`.
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the two
     resource indexes, empty.
   - `recipes/readme.md`: the recipe of the library's README, with
     the library's inputs (the ledger and the two indexes).
   - `recipes/readme.history.md`: the recipe's history.

   A library gets no brief, no decisions, no reviews, no challenges
   and no release notes. Its README is a render of its recipe, and
   it is the catalogue of what the library holds. You may add a
   `logo.png` of your own as the repository avatar. The command
   touches no git. Initialising the library's repository and adding
   a remote are your own one-off act, and a library that is not
   under git is a property, not a defect.

   You should now see the files above under `projects/lib-<name>/`
   and a proposal to run `/ingest` for the first documents.

2. **Put documents into it.** Run `/ingest <file> lib-<name>` for
   each document. This is the same registration every project uses,
   described in [Register a source](register-a-source.md). Claude
   stores the file in `sources/` under a short slug name. For a
   binary file it asks whether to convert it to Markdown. Answer no
   for a file that is used as it is, such as a deck template or a
   graphic. Claude then asks what the document is for, and writes
   the index entry only after your answer.

   You should now see the file in `projects/lib-<name>/sources/` and
   its entry in `sources/00-INDEX.md`.

3. **Keep the documents up to date.** In a library, changing a
   document is the owner's ordinary maintenance. Replace the file and
   run `/ingest lib-<name>` with no file. Claude sweeps `sources/`,
   registers files that have no entry yet and reports files changed
   since their registration. For a changed document of a library it
   updates the index entry, its Date included, and nothing else.

   You should now see the changed document's entry in
   `sources/00-INDEX.md` carrying a new Date.

4. **Cite a library document from a project.** Point the project at
   the library's file by its path, for example
   `/ingest projects/lib-<name>/sources/<file> <slug>`. Nothing is
   copied into the project's `sources/`. Claude adds an index entry
   in the project that names the path and says what the document is
   for. The ledger (the state report Claude makes from the documents
   whenever it is read) finds the citation by itself and lists it in
   its Dependencies table.

   You should now see the new entry in the project's
   `sources/00-INDEX.md` naming `projects/lib-<name>/...`, and the
   path in the Dependencies table of the project's ledger.

5. **See which libraries a project needs.** Run `/forge <slug>` for
   the project. The state map lists the libraries the project needs,
   taken from the ledger's Dependencies table, and says whether each
   is cloned alongside under `projects/`.

   You should now see each library the project cites, with whether
   it is present beside the project.

Run `/forge lib-<name>` on the library itself and the state map
reports its sources and research and whether it is under git. It
stops there: a library has no chain to work and no next step beyond
`/ingest`.

## What you have afterwards

- A library under `projects/lib-<name>/` with its project file, its
  git attributes and ignore file, `sources/` and `research/` with
  their indexes, and a README recipe whose render is the catalogue.
- A ledger for the library, made by
  `python scripts/forge-ledger.py lib-<name>` like every project's,
  never written by hand and never in git.
- Projects that cite the library's documents by path, each citation
  listed in that project's Dependencies table.

To move a document out of a project into a library, do the reverse:
ingest it into the library, then replace the project's index entry
with the citation of the library's path.

## If something goes wrong

- **A library a project needs is not cloned alongside.** The light
  check reports it as an advisory finding: "library `<name>` not
  cloned alongside - `/import-project <its remote>`". Bring the
  library in with `/import-project` and its remote, as described in
  [Bring in an existing project](bring-in-an-existing-project.md).
- **The slug is already taken.** If `projects/lib-<name>/` already
  exists, `/new-project` stops and reports it. It never overwrites.
- **The document carries personal matter.** `/ingest` stops before
  storing and asks whether to store it as it is, redact it first or
  drop it.
- **A changed source is reported in a project that is not a
  library.** In a thought project a source is immutable, so a change
  is a breach to resolve, not maintenance. Claude asks whether to
  register the changed file beside as a new source, restore the
  original, or accept the change knowingly on your word.

## A worked example

You keep a shared deck template for several projects.

1. `/new-project lib-<name>` creates `projects/lib-<name>/` with
   `project.md`, `.gitattributes`, `.gitignore`,
   `sources/00-INDEX.md`, `research/00-INDEX.md`,
   `recipes/readme.md` and `recipes/readme.history.md`.
2. `/ingest deck-template.potx lib-<name>` stores the file as
   `sources/deck-template.potx`. Asked whether to convert it, you
   answer no, because the template is used as it is. Asked what it is
   for, you answer "the deck template of our presentations". The
   entry appears in `sources/00-INDEX.md`.
3. In the project `<slug>`, you point at
   `projects/lib-<name>/sources/deck-template.potx`. Claude adds an
   entry naming that path to the project's `sources/00-INDEX.md`, and
   the project's ledger lists the path under Dependencies.
4. `/forge <slug>` names `lib-<name>` among the libraries the project
   needs and says it is cloned alongside.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why
  a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
