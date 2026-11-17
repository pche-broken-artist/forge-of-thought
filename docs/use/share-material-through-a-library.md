---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 0b2b233f4d1e98b0
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
  - templates/recipe.md
  - scripts/md2pptx.py
  - scripts/md2docx.py
  - .claude/skills/forge/states/brd.md#Inputs
---

# Share material through a library

A library is a project of kind `library` that holds material shared
across projects and has no chain (the brief, the intent and the
layers below the intent that a project of kind `thought` carries).
This page is for the principal (the person whose thinking is forged,
addressed here as "you") who wants to keep a document once and use
it in several projects. It shows how such a library is made and how
a project cites a document of it by path. Why a library is a kind of
project is explained in
[Projects and the engine](../about/projects-and-the-engine.md). The
terms of the forge are each said in one line in the
[Glossary](../reference/glossary.md).

## When to use it

Use a library when a document belongs to no single project and more
than one project needs it. Typical material:

- a document that several projects cite, such as a standard;
- a deck template or a Word reference document that a recipe names
  by its path;
- the roster of areas a BRD walks.

The roster (the areas of the enterprise a BRD must consider, and
which of them are mandatory) is a library document of the instance
(one installation of the forge), cited by path.
[Write a BRD](write-a-brd.md) says how it is used.

A document that already lives in one project can move into a library
later. Step 3 below says how.

## What you do

You make the library with one command. The name after the prefix
`lib-` is yours to choose:

```
/new-project lib-<name>
```

The other lines of the job follow in the order you meet them.
`<slug>` is the slug of the project that uses the library:

| Line | What it does |
|---|---|
| `git -C projects/lib-<name> init -b main` | makes the library a git repository (your one-off act) |
| `/ingest <file> lib-<name>` | registers a document in the library |
| `/ingest projects/lib-<name>/sources/<document> <slug>` | cites a library document in the project `<slug>` |
| `/forge <slug>` | reports the state map of the project `<slug>`, its libraries included |
| `/ingest` | without a file: sweeps `sources/` for new and changed documents |
| `/import-project <its remote>` | brings in a library that is missing alongside |

## What happens

1. **The library is born.** `/new-project lib-<name>` creates
   `projects/lib-<name>/`. Claude takes the kind `library` from the
   prefix `lib-` or from your words. It asks where the kind is
   unclear. The language of the project is English where you name no
   other. Claude asks where your words leave the language open. The
   command creates files only:

   - `project.md`: the project file with slug, kind and language,
     written once;
   - `.gitattributes`: the ways of merging by path;
   - `.gitignore`: what never enters git, that is the ledger and the
     lock files of an open Office document;
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the resource
     indexes, one catalogue per directory;
   - `recipes/readme.md`: the readme recipe, whose inputs are the
     ledger and the two indexes;
   - `recipes/readme.history.md`: the history of that recipe.

   The ledger is the file of a project's state. A script makes it at
   read time, and it is never kept in git. The ledger of a library is
   made by the same script as the ledger of every project.

   A library gets none of these:

   - a brief;
   - decisions;
   - reviews or challenges;
   - release notes.

   The command never touches git. The library is a git repository of
   its own, and making it one is your one-off act:
   `git -C projects/lib-<name> init -b main`, then a remote if you
   want one. Claude closes by proposing `/ingest` for the first
   documents.

   You should now see `projects/lib-<name>/` with these files, and
   one remark that the project is not under git.

2. **Documents enter by `/ingest`.** `/ingest <file> lib-<name>`
   registers a document in the library as it does in every project.
   The whole course is on [Register a source](register-a-source.md).
   In short:

   - Claude copies the file into `sources/` under a short descriptive
     name.
   - For a binary file it asks whether to convert it to Markdown. On
     yes the Markdown extract is the source. On no the binary itself
     is the source, as a functional thing such as a deck template, a
     graphic or a logo.
   - It asks what the document is for, before the entry is written.
   - It adds the entry to `sources/00-INDEX.md` and remakes the
     ledger.

   Registration carries no content of the document into any other
   document.

   You should now see a short reply that names the file stored and
   its index entry.

3. **A project cites a library document by its path.** In the
   project that needs the document you point `/ingest` at the path:
   `/ingest projects/lib-<name>/sources/<document> <slug>`. The
   document is cited, not copied: nothing is stored in the `sources/`
   of the project. Claude adds an entry to the project's
   `sources/00-INDEX.md` that names the path and says what the
   document is for. The ledger finds the citation by itself and lists
   it in its Dependencies table. A document that already lives in a
   project moves into a library the other way round: you ingest it
   in the library, and the entry of the project is replaced by the
   citation.

   You should now see the entry with the path in the project's index
   and a row for it in the Dependencies table of the project's
   ledger.

4. **A recipe names a template or a reference document by path.** A
   recipe (the file that says how a render, that is a generated
   output, is made) may carry a Format section. Two of its lines
   take a path:

   - `reference <path | none>` stands on the line of the plain file,
     which `/render` makes;
   - `template <path | none>` stands on the line of the published
     file, which `/publish` makes.

   A deck template or a Word reference document is typically a
   document of a library, named as
   `projects/lib-<name>/sources/<document>`. The conversion scripts
   receive the file as the path they are given.

   You should now see the path of the library document on that line
   of the recipe's Format section.

5. **The state map says which libraries a project needs.** Bare
   `/forge` reports the state map of a project. One of its lines
   names the libraries the project needs (the Dependencies table of
   the ledger) and says whether each is cloned alongside (present on
   disk as `projects/lib-<name>/`).

   You should now see every library the project cites named in the
   state map, each with the word whether it is cloned alongside.

6. **A changed document is maintenance.** `/ingest` without a file
   sweeps `sources/`. Claude takes the project from the conversation
   and asks where it is ambiguous. The sweep registers the files not
   yet in the index. It reports every file changed after its
   registration (its modification time is later than the Date of its
   index entry) and asks what to do with it. In a library a changed
   document is the ordinary maintenance of its owner: Claude updates
   the index entry, its Date included, and nothing else. No file is
   re-registered silently.

   You should now see the entry of the changed document with its new
   Date.

## What you have afterwards

A library, that is a project without a chain:

| In `projects/lib-<name>/` | What it is |
|---|---|
| `project.md` | the project file: slug, kind, language |
| `.gitattributes` | the ways of merging by path |
| `.gitignore` | what never enters git: the ledger and the Office lock files |
| `ledger.md` | the ledger, made by the script and never in git |
| `README.md` | the catalogue of the library (a render of its readme recipe) |
| `recipes/readme.md` | the readme recipe |
| `recipes/readme.history.md` | the history of the readme recipe |
| `sources/00-INDEX.md` | the index of the documents |
| `research/00-INDEX.md` | the index of the research |
| the documents in `sources/` | the shared material, maintained by its owner |

In every project that uses the library:

- an entry in `sources/00-INDEX.md` that names the path of the
  library document and says what it is for;
- a row in the Dependencies table of the project's ledger;
- where a recipe needs a template or a reference document, its path
  in the Format section of that recipe;
- no copy of the document.

## If something goes wrong

**The folder `projects/lib-<name>/` already exists.** `/new-project`
stops and reports it. It never overwrites a project. A slug is
written in lowercase, with hyphens and without spaces.

**The library is reported as "not under git".** That is a property
of a project that has no repository yet, not a defect.
`git -C projects/lib-<name> init -b main` makes the repository.

**You ask for a state of the chain in a library.** `/forge <state>`
in a library answers that a library has no chain, and stops. No state
is worked there. Bare `/forge` in a library reports this and stops:

- the kind and the language of the library;
- whether it is under git;
- its sources and its research.

It names no next step beyond `/ingest`.

**A document carries personal matter.** `/ingest` stops before it
stores anything and asks which of three you want:

- store the document as it is;
- redact it before registration;
- drop it.

**A library is not cloned alongside.** The state map says so. The
light check (the check of a project's bookkeeping) reports every
path of the Dependencies table that does not exist on disk. Its
finding for a missing library reads:

```
library `<name>` not cloned alongside — `/import-project <its remote>`
```

The finding is advisory. You bring the library in with
`/import-project` and the remote of the library:
[Bring in an existing project](bring-in-an-existing-project.md) says
how.

**The sweep reports a changed document.** In a library the report is
settled as step 6 says: the index entry is updated. In a project of
kind `thought` the same report means a breach of immutability, which
you resolve. A source there is immutable from its registration.

## A worked example

The library `lib-<name>` is to hold a Word reference document and a
standard. The project `<slug>` uses both.

You make the library:

```
/new-project lib-<name>
```

Claude creates `projects/lib-<name>/` with the project file,
`.gitattributes`, `.gitignore`, the two indexes and the readme recipe
with its history. It proposes `/ingest` and says that the project is
not under git. You make the repository:

```
git -C projects/lib-<name> init -b main
```

You register the Word reference document:

```
/ingest <styles>.docx lib-<name>
```

Claude asks whether to convert the file to Markdown. You answer no:
the file is the source as it is. Claude asks what it is for, and you
answer. The file now lies in `projects/lib-<name>/sources/`, with its
entry in the index there.

You register the standard:

```
/ingest <standard>.pdf lib-<name>
```

This time you answer yes to the conversion. The source is the
Markdown extract, `projects/lib-<name>/sources/<standard>.md`.

A recipe of the project `<slug>` makes a Word document. The line of
the plain file in its Format section names the reference document by
path:

```
- Plain file, made by `/render` through pandoc: reference
  projects/lib-<name>/sources/<styles>.docx, page size A4.
```

You cite the standard in the project:

```
/ingest projects/lib-<name>/sources/<standard>.md <slug>
```

Nothing is copied. `projects/<slug>/sources/00-INDEX.md` gains an
entry that names the path and says what the standard is for.

You ask for the state map:

```
/forge <slug>
```

The state map names `lib-<name>` among the libraries the project
needs and says that it is cloned alongside.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why
  a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Write a BRD](write-a-brd.md): the BRD that walks the instance's
  roster of areas, a library document.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
