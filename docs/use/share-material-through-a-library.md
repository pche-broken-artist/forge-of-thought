---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: b1453a7549cf952c
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

A library is a project of kind `library`: a place for material that
several projects share, such as a deck template, a Word reference
document or a standard, with no document chain of its own. This page
is for you as the user of the forge: how you create a library, how
documents enter it, how a project cites a document of the library by
its path, and how a library that is missing beside your project is
brought in. What a project is and why a library is one of its kinds
is said in [Projects and the engine](../about/projects-and-the-engine.md).

## When to use it

Use a library when a document is not the thinking of one project but
material that more than one project reaches for: a deck template or a
reference document that renders are made with, the roster of areas a
BRD walks, a group standard. A thought project carries its own
sources in `sources/`; a document that lives in a library is cited
from there instead of being copied, and the project's state shows the
library as a dependency.

## What you do

Four commands do the work, each described in full on its own page
where one exists.

```
/new-project lib-<name>
/ingest <file> lib-<name>
/ingest projects/lib-<name>/sources/<document> <slug>
/import-project <git-url>
```

- `/new-project lib-<name>` creates the library. The slug carries the
  prefix `lib-`; Claude reads the kind `library` from the prefix or
  from your words, and asks when it is unclear.
- `/ingest <file> lib-<name>` puts a document into the library. The
  ingest is the one every project has; its steps are on
  [Register a source](register-a-source.md).
- `/ingest projects/lib-<name>/sources/<document> <slug>` cites a
  library document from the project `<slug>`.
- `/import-project <git-url>` brings a library in that a project
  needs and that is not cloned alongside; the page is
  [Bring in an existing project](bring-in-an-existing-project.md).

## What happens

1. **The library is created.** `/new-project lib-<name>` validates the
   slug (lowercase, hyphens, no spaces) and refuses to overwrite a
   folder that already exists. It creates files only, never a git
   repository: the project file `project.md` (slug, kind, language),
   `.gitattributes` and `.gitignore`, the two resource indexes
   `sources/00-INDEX.md` and `research/00-INDEX.md`, and the readme
   recipe `recipes/readme.md` with its history companion
   `recipes/readme.history.md`. The recipe's inputs are the ledger and
   the two indexes, so that the library's README is a catalogue of
   what it holds. No brief, no decisions, no reviews, no challenges
   and no release notes are made. The ledger (the single source of
   truth for the project's state, made at read time by a script and
   never kept in git) is made like every project's, by
   `python scripts/forge-ledger.py lib-<name>`. Claude closes by
   proposing `/ingest` for the first documents and says once that the
   project is not under git until you initialise its repository: a
   fact, not a defect.
   You should now see `projects/lib-<name>/` with `project.md`,
   `.gitattributes`, `.gitignore`, `sources/00-INDEX.md`,
   `research/00-INDEX.md`, `recipes/readme.md` and
   `recipes/readme.history.md`, and one line saying the project is
   not under git.

2. **A document enters the library.** `/ingest <file> lib-<name>`
   stores the file in `sources/` under a short descriptive slug. For
   a binary file Claude asks once whether to convert it to Markdown;
   for a deck template or a reference document the answer is no, and
   the binary is stored, registered and indexed as it is, as a
   functional thing. The date is taken from the content or the file
   where it can be read for free, never asked. Before anything is
   written, Claude asks one question, "what is it for?", and the
   answer becomes the Role of the index entry. Then the entry is
   added to `sources/00-INDEX.md` and the ledger is remade.
   You should now see the file in `projects/lib-<name>/sources/` and
   its entry in `sources/00-INDEX.md`, and a reply of two lines at
   most: the file stored and its index entry.

3. **The library is maintained.** A document of a library is
   maintained by its owner: a changed file is ordinary maintenance,
   not a breach of immutability. Bare `/ingest lib-<name>` sweeps
   `sources/` for files not yet in the index and reports files
   changed since their registration, with a question what to do with
   each; in a library the answer is to update the index entry, its
   Date included, and nothing else. Nothing is re-registered in
   silence.
   You should now see the entry of the changed document carrying a
   new Date, the file itself untouched.

4. **A project cites a library document.** When you point a project
   at a document that lives in a library,
   `/ingest projects/lib-<name>/sources/<document> <slug>`, nothing is
   stored in the project's `sources/`: Claude adds an index entry
   that names the path and says what the document is for. The ledger
   finds the citation by itself and lists it in its Dependencies
   table. Moving a document out of a project into a library is the
   reverse: ingest it in the library, then replace the project's
   entry with the citation.
   You should now see an entry in the project's `sources/00-INDEX.md`
   naming `projects/lib-<name>/sources/<document>`, no new file in
   its `sources/`, and a row in the ledger's Dependencies table.

5. **A template or a reference document is named in a recipe.** A
   recipe that names a format has a `## Format` section: its
   published file names `template <path | none>`, its plain file
   `reference <path | none>`. Such a file is typically a document of
   a library project, and you write its path there; the conversion
   scripts receive the path as it is written.
   You should now see the path of the library document in the
   recipe's Format section.

6. **The state map shows the library.** Bare `/forge <slug>` on a
   thought project reports which libraries the project needs, from
   the ledger's Dependencies table, and whether each is cloned
   alongside. A library that is missing is brought in with
   `/import-project <git-url>`. Bare `/forge lib-<name>` on the
   library itself reports its sources and research and stops after
   the git line: a library is material, not a project waiting for a
   brief, so no target state and no next step beyond `/ingest` is
   offered.
   You should now see every library the project needs named in the
   map, each marked as cloned alongside or not.

The roster of areas a BRD walks is such a library document too, cited
by path from the BRD's definition; the BRD page says what the roster
does: [Write a BRD](write-a-brd.md).

## What you have afterwards

- A project `projects/lib-<name>/` of kind `library`: the project
  file, `.gitattributes`, `.gitignore`, `sources/` and `research/`
  with their indexes, and a readme recipe whose render is the
  catalogue of what the library holds.
- Documents in the library's `sources/`, each with an index entry
  that says what it is and what it is for, maintained by their owner.
- In every project that uses them, an index entry citing the
  document by its path and a row in the ledger's Dependencies table;
  no copy.
- Recipes whose Format section names a template or a reference
  document of the library by its path.

## If something goes wrong

- **`/forge <state> lib-<name>` stops.** A library has no chain, so
  Claude says so and works no state there. Material enters by
  `/ingest`; nothing else is expected of a library.
- **`/new-project lib-<name>` stops because the folder exists.** The
  command never overwrites; choose another slug or work in the
  existing library.
- **The kind is unclear.** Without the `lib-` prefix and without
  your words saying it, Claude asks whether the project is a library
  or a thought project before it creates anything.
- **The light check reports a missing library.** The check run by a
  save verifies that every path in the ledger's Dependencies table
  exists on disk; a path into a library that is not cloned beside the
  engine gives the finding "library `<name>` not cloned alongside -
  `/import-project <its remote>`" (the owner's long dash rendered
  here as a hyphen). The finding is advisory: run `/import-project`
  with the library's remote and the path resolves.
- **A library document has changed.** In a library this is not a
  breach: the sweep of `/ingest` reports it and the index entry is
  updated, its Date included. Claude never re-registers in silence.
- **The text carries personal matter.** `/ingest` stops before
  storing and asks whether to store as it is, redact first or drop;
  a registered source is immutable, so redaction happens before
  registration.
- **The library is not under git.** `/new-project` says this once at
  the end; it is a property, not a defect. Initialising the
  repository and adding a remote are your own one-off act.

## A worked example

The principal (the person whose thinking is forged, who decides what
is written) wants one deck template and one Word reference document
for every project of the instance (one installation of the forge).

1. `/new-project lib-<name>`. Claude reads the kind `library` from
   the prefix, asks for the language only if the words leave it open,
   and creates `projects/lib-<name>/` with `project.md`,
   `.gitattributes`, `.gitignore`, `sources/00-INDEX.md`,
   `research/00-INDEX.md`, `recipes/readme.md` and
   `recipes/readme.history.md`. It proposes `/ingest` for the first
   documents and says once that the project is not under git.
2. `/ingest deck-template.potx lib-<name>`. The file is a binary;
   Claude asks whether to convert it to Markdown, the answer is no,
   and the template is stored as it is in
   `projects/lib-<name>/sources/deck-template.potx`. Claude asks
   "what is it for?"; the answer, "the deck template of every
   rendered deck", becomes the Role of the entry in
   `sources/00-INDEX.md`. The ledger is remade.
3. `/ingest report-styles.docx lib-<name>`. The same way: no
   conversion, stored as it is, its role asked and written, its
   entry added.
4. In the thought project `<slug>`,
   `/ingest projects/lib-<name>/sources/deck-template.potx <slug>`.
   Nothing lands in the project's `sources/`; its `sources/00-INDEX.md`
   gains an entry naming the path and saying what it is for, and
   the ledger's Dependencies table gains the row.
5. In the project's recipe for the deck, the Format section names
   `template projects/lib-<name>/sources/deck-template.potx` for the
   published file; a recipe for a Word document names
   `reference projects/lib-<name>/sources/report-styles.docx` for the
   plain file.
6. On another machine, bare `/forge <slug>` reports that the project
   needs `lib-<name>` and that it is not cloned alongside;
   `/import-project <git-url>` brings it in, and the next map shows
   it alongside.

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

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
