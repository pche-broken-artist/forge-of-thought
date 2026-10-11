---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: c4dc0677cfe3ee50
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project that holds material shared across projects
and has no chain of its own. This page is for you, the user who
wants to keep a style guide, a deck template or a piece of research
in one place and use it from several projects without copying it.
It says how a library is made, how documents enter it, how a project
cites one of its documents and how Claude tells you when a library
the project needs is not there.

## When to use it

Use a library when more than one project needs the same document:
a house style, a deck template, a glossary, a research note. The
library owns the document and keeps it up to date; each project
cites it by path and copies nothing. A library is not a project
waiting for a brief. It has no intent, no assignment, no reviews and
no release notes: only a ledger (the one file that records a
project's state), a `sources/` and a `research/` directory with
their indexes, and a readme recipe whose render is the catalogue of
what the library holds. Why a library is a kind of project and what
a dependency means is said on [Projects and the
engine](../about/projects-and-the-engine.md).

## The command

Four commands do the job, each at its own moment:

```
/new-project lib-<name>
/ingest <file> lib-<name>
/ingest projects/lib-<name>/sources/<document>.md <slug>
/forge <slug>
```

`lib-<name>` is the library's slug, always with the prefix `lib-`;
`<slug>` is the project that uses it.

## What happens

1. **Make the library.** You type `/new-project lib-<name>`. Claude
   reads the kind `library` from the `lib-` prefix or from your
   words; when that is unclear, it asks. It creates files only, and
   never touches git: `projects/lib-<name>/ledger.md` with
   `kind: library` in its header, `sources/00-INDEX.md`,
   `research/00-INDEX.md`, and `recipes/readme.md` with its history
   companion `recipes/readme.history.md`, the recipe's inputs being
   the ledger and the two indexes. No brief, no decisions file, no
   reviews, no challenges, no release notes. It ends by proposing
   `/ingest` for the first documents and by saying once that the
   library is not under git until you initialise its repository.
   Initialising the repository and adding a remote are your own
   one-off act, as for any project. You should now see
   `projects/lib-<name>/` with the ledger, the two indexes and the
   readme recipe, and one line on git.

2. **Put documents in.** You type `/ingest <file> lib-<name>`. This
   is the same ingest every project has; it is described on
   [Register a source](register-a-source.md). The file is stored in
   `sources/` under a short slug, its date recorded best effort and
   never asked, an index entry added to `sources/00-INDEX.md`, a row
   added to the ledger's Sources table. For a binary, Claude asks
   one question per file: convert to Markdown? Answer no for a
   document the library keeps as a functional thing, such as a deck
   template, a graphic or a logo; it is then stored, registered and
   indexed as it is. The reply closes with the question "what is it
   for?", and your answer becomes the entry's Role. You should now
   see the file in `projects/lib-<name>/sources/`, its index entry
   and its ledger row, and the question "what is it for?".

3. **Keep the documents up to date.** A library's documents are
   maintained by their owner. When a document in the library has
   changed since it was registered, a bare `/ingest` in the library
   reports it and asks what to do. Because the project is a
   library, the change is ordinary maintenance and not a breach:
   Claude updates the index entry and the date in the ledger,
   nothing else. In a thought project the same change would be a
   breach of immutability to resolve. You should now see the index
   entry and the ledger date brought up to the changed file.

4. **Refresh the catalogue.** The library's `README.md` is a render
   of `recipes/readme.md`, made by `/render readme`; it is the
   catalogue of what the library holds and is never edited by hand.
   You should now see a README that lists the library's sources and
   research as the ledger and the indexes have them.

5. **Cite a library document from a project.** In the project that
   needs the document, you type
   `/ingest projects/lib-<name>/sources/<document>.md <slug>`.
   Nothing is stored in the project's `sources/`. Claude adds an
   index entry that names the path and says what the document is
   for, and a row in the ledger's Dependencies table. A recipe may
   name a library file by path in the same way, for instance a deck
   template the library keeps as a binary; the citation needs the
   same Dependencies row. Moving a document out of a project into a
   library is the reverse: ingest it in the library, replace the
   project's entry with the citation, register the dependency. You
   should now see the index entry with the library path and the
   Dependencies row, and no new file in the project's `sources/`.

6. **See what the project depends on.** You type `/forge <slug>`.
   Among the lines of the state map (the report of where a project
   stands), Claude says which libraries the project needs, from the
   ledger's Dependencies table, and whether each is cloned
   alongside under `projects/`. For the library itself,
   `/forge lib-<name>` reports its sources and research and stops
   after the line on git: no chain, no target states, no next step
   beyond `/ingest`. You should now see one line per library the
   project needs, each saying whether it is present.

7. **Bring in a library that is missing.** When the map or a check
   says a library is not cloned alongside, you bring it in with
   `/import-project <git-url>`, the library's remote as the
   argument; how that runs is [Bring in an existing
   project](bring-in-an-existing-project.md). You should now see
   the library under `projects/lib-<name>/` and the dependency line
   of the map saying it is present.

## What you have afterwards

A library under `projects/lib-<name>/` with a ledger of
`kind: library`, two resource indexes, a readme recipe and a README
that catalogues its documents; a git repository of its own, which
the engine does not track, once you have initialised it. In each
project that uses it, an index entry naming the library document by
path and a row in the Dependencies table; no copy. On the project's
state map, one line per library saying whether it is cloned
alongside.

## If something goes wrong

- `/new-project` stops and reports when `projects/lib-<name>/`
  already exists; it never overwrites. The slug is lowercase with
  hyphens and no spaces. When the kind is unclear from the slug and
  your words, Claude asks.
- `/ingest` stops before storing when the text carries personal
  matter (a named private person, an identifying detail, health)
  and asks: store as it is, redact before registration, or drop. A
  registered source is immutable, so redaction happens first.
- On a name collision in `sources/`, the new file gets the suffix
  `-2`; a file already in the ledger is never renamed or modified.
- The light check, which a save runs, reports a path in the
  Dependencies table that does not exist on disk as the finding
  "library `<name>` not cloned alongside - `/import-project <its
  remote>`", advisory. It also reports an index entry, a recipe or
  a chain citation that points to `projects/<other>/…` without a
  Dependencies row, and a row that points inside the project. Such
  findings are bookkeeping and marked "immediate fix".
- A library that is "not under git" is a property, never a defect;
  the state map says so as a fact.

## A worked example

You want one style guide for all your projects.

1. `/new-project lib-<name>`. Claude creates
   `projects/lib-<name>/ledger.md` with `kind: library`,
   `sources/00-INDEX.md`, `research/00-INDEX.md`,
   `recipes/readme.md` and `recipes/readme.history.md`, proposes
   `/ingest` for the first documents and says the library is not
   under git until you initialise its repository.
2. `/ingest style-guide.md lib-<name>`. The file lands as
   `projects/lib-<name>/sources/style-guide.md`, gets an index entry
   and a Sources row. Claude asks "what is it for?"; you answer "the
   house style every render follows", and that becomes its Role.
3. `/ingest deck-template.pptx lib-<name>`. Claude asks whether to
   convert to Markdown; you answer no, and the deck template is
   stored, registered and indexed as a binary.
4. In the project `<slug>`:
   `/ingest projects/lib-<name>/sources/style-guide.md <slug>`.
   Nothing is copied. The project's `sources/00-INDEX.md` gets an
   entry naming that path and its purpose, and the project's ledger
   gets a Dependencies row.
5. `/forge <slug>`. The map shows the library among the project's
   dependencies and says it is cloned alongside.
6. On another machine where the project is present and the library
   is not, the map says the library is not cloned alongside;
   `/import-project <git-url>` with the library's remote brings it
   in, and the next map says it is present.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md):
  why a library is a kind of project and what a dependency means.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
