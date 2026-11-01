---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: da929ceb9fd68d1f
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project that holds material shared across projects
and has no chain of documents of its own. This page is for the
principal (the person whose thinking is forged, who decides
everything in a project) and for anyone keeping a project's
material. It shows how a library is made, how documents go into it
and how another project cites one of them. Why a library is a kind
of project is explained in
[Projects and the engine](../about/projects-and-the-engine.md).
Every term of the forge has one line in the
[Glossary](../reference/glossary.md).

## When to use it

Use a library when the same document serves more than one project.
Examples are a deck template, a graphic, a standard or a piece of
research. The document then lives once, in the library. Each project
that needs it cites it by its path and keeps no copy.

## The command

```
/new-project lib-<name>
```

The prefix `lib-` marks the project as a library. Claude infers the
kind `library` from that prefix or from your words. Where the kind
is unclear, it asks.

## What happens

1. **The library is made.** Claude creates `projects/lib-<name>/`
   with these files and nothing more:
   - `project.md`: the project file, with the slug, the kind
     `library` and the language, written once;
   - `.gitattributes`: the ways git merges files by path;
   - `.gitignore`: what never enters git, the ledger and the lock
     files of an open Office document among them;
   - `sources/00-INDEX.md` and `research/00-INDEX.md`: the two
     catalogues of the library's documents, empty at first;
   - `recipes/readme.md`: the recipe of the library's README, with
     the ledger and the two indexes as its inputs;
   - `recipes/readme.history.md`: the history companion of that
     recipe.

   A library has no brief, no decisions, no reviews, no challenges
   and no release notes. Its README is a catalogue of what it holds,
   generated from its recipe. You should now see the folder
   `projects/lib-<name>/` with those files, and Claude proposing
   `/ingest` for the first documents.

2. **You put the library under git, if you want.** The command
   writes files only and never touches git. Initialising the
   library's repository and adding a remote are your own one-off
   act. A library that is not under git is a property, not a defect.
   You should now see Claude saying once that the library is not
   under git until you initialise it.

3. **Documents enter by `/ingest`.** You register each document in
   the library as in any project, with the steps described in
   [Register a source](register-a-source.md). Claude stores the
   file in `sources/`. It asks what the document is for before it
   writes the index entry. For a binary file it asks whether to
   convert it to Markdown. A deck template or a graphic is kept as a
   functional file, so you answer no and it is stored as it is. You
   should now see the file in `sources/` and its entry in
   `sources/00-INDEX.md`.

4. **A changed document is maintenance.** In a library, the owner
   keeps the documents up to date. When you run `/ingest` without
   arguments, Claude sweeps `sources/` and reports the files changed
   since their registration. In a library such a change is ordinary
   maintenance. Claude updates the document's index entry, its date
   included, and nothing else. You should now see the entry carrying
   the new date.

5. **A project cites the library's document.** In the project that
   needs the document, you point it at the path in the library, such
   as `projects/lib-<name>/sources/<document>`. Nothing is stored in
   that project's `sources/`. Claude adds an index entry that names
   the path and says what the document is for. You should now see
   the entry with the path in the project's `sources/00-INDEX.md`.

6. **The ledger lists the dependency.** The ledger is the project's
   single record of state, made from the documents by
   `python scripts/forge-ledger.py <slug>` whenever it is read and
   never kept in git. It finds the citation by itself and lists the
   path in its Dependencies table. Nobody writes that row by hand.
   You should now see the library's path under Dependencies.

7. **The state map says what the project needs.** Bare `/forge` in
   the project reports, among the rest, which libraries the project
   needs and whether each is cloned alongside it under `projects/`.
   You should now see each library named, with whether it is there.

The same `/forge` in the library itself reports its sources and its
research and stops. A library has no chain and no next step beyond
`/ingest`.

## What you have afterwards

- A library `projects/lib-<name>/` whose documents live once and
  are maintained by their owner.
- A README of the library that catalogues what it holds.
- In each project that uses a document: an index entry naming the
  path, a row in the ledger's Dependencies table and a line in the
  state map.

Moving a document out of a project into a library is the reverse of
step 5. You ingest the document in the library and replace the
project's own entry with the citation.

## If something goes wrong

- **The folder already exists.** `/new-project` stops and reports.
  It never overwrites an existing project.
- **A library is not cloned alongside.** A cited path that is not on
  disk is reported by the light check as an advisory finding, in the
  words "library `<name>` not cloned alongside - `/import-project
  <its remote>`". You bring the library in with `/import-project`,
  as described in
  [Bring in an existing project](bring-in-an-existing-project.md).
- **The document carries personal matter.** `/ingest` stops before
  storing anything and asks whether to store it as it is, redact it
  first or drop it.
- **A bundle that arrived whole is given more files.** `/ingest
  --bundle <name>` refuses and says why. Only a bundle registered as
  growing takes files one by one.

## A worked example

You make a library for material several projects share.

```
/new-project lib-<name>
```

Claude creates `projects/lib-<name>/` with its project file, its
`.gitattributes` and `.gitignore`, the two indexes and the readme
recipe, and proposes `/ingest`. You register a deck template.

```
/ingest <deck-template>.pptx lib-<name>
```

Claude asks whether to convert it to Markdown. You answer no,
because the template is used as a file. It asks what the template is
for, and you answer. The template lies in
`projects/lib-<name>/sources/` with its index entry.

In a project `<slug>` you then point at that template. Claude stores
nothing there and adds an entry to `projects/<slug>/sources/00-INDEX.md`
that names `projects/lib-<name>/sources/<deck-template>.pptx` and
says what it is for. Bare `/forge <slug>` lists `lib-<name>` among the
libraries the project needs and says whether it is cloned alongside.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md): cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
