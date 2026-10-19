---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: e3070287c712bfaf
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project of kind `library` that holds material shared
across projects and has no chain of its own. This page is for the
user who wants to keep documents in one library, keep them up to
date there, and cite them from the projects that use them. Why a
library is a kind of project at all is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## When to use it

Use a library when the same document serves more than one project.
Examples are a reference text, a deck template or a graphic. The
document then lives once, in the library, and each project cites it
by its path. Nothing is copied into the project.

A library has a slug that begins with `lib-` and lies beside the
other projects, as `projects/lib-<name>/`. It holds only these
files:

- `project.md`: the project file, with the slug, the kind and the
  language.
- `.gitattributes`: the ways of merging by path.
- `.gitignore`: it keeps the ledger out of git.
- `ledger.md`: the ledger, that is the file of the project's state.
  A script makes it at read time, like every project's ledger.
- `sources/` and `research/`, each with its `00-INDEX.md` catalogue.
- `recipes/readme.md` and its history companion
  `recipes/readme.history.md`.
- `README.md`: the catalogue of what the library holds, a render of
  its readme recipe.
- `logo.png`: optional.

A library has no brief, no intent, no decisions, no reviews, no
challenges and no release notes. Its documents are maintained by
their owner.

## The command

```
/new-project lib-<name>
```

## What happens

1. **Create the library.** Type `/new-project lib-<name>`. Claude
   (the model that works the forge with you) reads the `lib-` prefix
   as the kind `library`. Where the kind is unclear, it asks. It also
   asks for the language of the project when your words leave it
   open; English is the default. It then writes the files listed
   above and nothing more. The command writes files only and never
   touches git. Initialising the library's own repository and adding
   a remote are your one-off act. A library that is not under git is
   a property, not a defect. Claude closes by proposing `/ingest` for
   the first documents.
   You should now see `projects/lib-<name>/` with `project.md`,
   `.gitattributes`, `.gitignore`, the two empty indexes and the
   readme recipe with its companion.

2. **Put a document into the library.** Type
   `/ingest <file> lib-<name>`. The ingest is the same as in every
   project, and [Register a source](register-a-source.md) walks it
   in full. In short:
   - If the text carries personal matter, Claude stops first and
     asks whether to store it as it is, redact it or drop it.
   - The file is stored in `sources/` under a short descriptive
     slug, with no date in the name.
   - For a binary file, Claude asks whether to convert it to
     Markdown. Answer no for a functional file such as a deck
     template or a graphic: it is then stored and indexed as it is.
   - Claude asks what the document is for, one question per source.
     You answer with the role, or tell Claude to infer it.
   - An entry is added to `sources/00-INDEX.md` and the ledger is
     remade by the script.

   You should now see a reply of at most two lines: the file stored
   and its index entry.

3. **Keep a document current.** You change a document in the library
   as its owner. Then type `/ingest lib-<name>` with no file. This
   sweep registers any file not yet in the index. It also reports
   each file changed since its registration, with a question about
   what to do with it. In a library a changed document is ordinary
   maintenance: Claude updates its index entry, the `Date` included,
   and nothing else. Nothing is re-registered silently.
   You should now see the changed document named, and after your
   answer its index entry with the new date.

4. **Cite the document from a project.** Point the project at the
   document in the library, for example
   `/ingest projects/lib-<name>/sources/<file> <slug>`. Nothing is
   stored in the project's `sources/`. Claude adds an entry to the
   project's index that names the library path and says what the
   document is for. The ledger finds the citation by itself and lists
   it in its Dependencies table. You add nothing there by hand.
   You should now see the new entry in
   `projects/<slug>/sources/00-INDEX.md` naming the path under
   `projects/lib-<name>/`.

5. **See which libraries a project needs.** Type `/forge <slug>`.
   The state map of the project lists the libraries it needs, read
   from the Dependencies table, and says whether each is cloned
   alongside.
   You should now see `lib-<name>` in that list, marked as present.

## What you have afterwards

- A library under `projects/lib-<name>/` with its documents
  registered in `sources/00-INDEX.md`.
- One or more projects whose indexes cite those documents by path.
- A Dependencies table in each citing project's ledger that lists
  the library, made by the script from the citations.

For a library itself, `/forge lib-<name>` reports its sources and
research and whether it is under git, and stops there. It shows no
chain, no states to work and no next step beyond `/ingest`.

## If something goes wrong

- **A library the project needs is not on this machine.** The state
  map says it is not cloned alongside. The light check reports the
  same as an advisory finding: library `<name>` not cloned
  alongside, with `/import-project <its remote>` as the remedy.
  Bring it in with `/import-project <git-url>`, as
  [Bring in an existing project](bring-in-an-existing-project.md)
  describes.
- **The kind was not clear.** When neither the `lib-` prefix nor
  your words settle the kind, Claude asks before it writes anything.
- **A document belongs in a library but sits in a project.** Ingest
  it into the library, then replace the project's index entry with
  the citation of the library path.

## A worked example

You keep a deck template that several projects use.

1. `/new-project lib-<name>` creates `projects/lib-<name>/` with
   its project file, its attributes, its ignore file, the two indexes
   and the readme recipe. Claude proposes `/ingest`.
2. `/ingest <template-file> lib-<name>` stores the template. Asked
   whether to convert it, you answer no, so it stays a binary. Asked
   what it is for, you answer "the deck template for every project".
   The entry lands in `projects/lib-<name>/sources/00-INDEX.md`.
3. In the project `<slug>`, you type
   `/ingest projects/lib-<name>/sources/<template-file> <slug>`.
   The project's index gains an entry that names that path. Nothing
   is copied.
4. `/forge <slug>` lists `lib-<name>` among the libraries the
   project needs, cloned alongside.
5. Later you replace the template in the library. `/ingest
   lib-<name>` reports it as changed. On your word Claude updates
   its index entry and its date. Every project that cites the path
   now reaches the new template.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md):
  why a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
