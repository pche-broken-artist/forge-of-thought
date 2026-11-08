---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: c2977a598ce3dd76
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
is for you as a user of the forge who wants to keep such material in
one place and have your projects cite it instead of copying it. It
shows how a library is born, how documents enter it, how a project
cites one, how a recipe names one, and how you see which libraries a
project needs. Why a library is a kind of project is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## When to use it

Use a library when the same file is wanted by more than one project.
Typical members are:

- a deck template that every deck render of your projects starts
  from;
- a Word reference document that every Word render of your projects
  starts from;
- a standard or a regulation that several projects cite;
- the roster of areas a BRD walks, where your instance (one
  installation of the forge) has an enterprise around it.

Use it also when a document already registered in one project turns
out to be wanted by another: it moves into a library and the project
keeps a citation.

## What you do

The library is created once, its documents enter one by one, and
each project that needs a document cites it by path:

```
/new-project lib-<name>
/ingest <file> lib-<name>
/ingest projects/lib-<name>/sources/<document> <slug>
```

The first line creates the library. The second registers a document
in it. The third, run for a thought project with the slug `<slug>`,
makes that project cite the library document. The `lib-` prefix is
the mark of a library: `/new-project` infers the kind `library` from
it.

## What happens

### Step 1: Create the library

Run `/new-project lib-<name>`. Claude (the machine that runs the
forge) infers the kind `library` from the `lib-` prefix or from your
words; when that is unclear, it asks. It asks for the language of
the project where your words leave it open; English is the default.
It then creates files only and never touches git:

- `project.md`, the project file with the slug, the kind and the
  language, written once;
- `.gitattributes`, the ways of merging by path;
- `.gitignore`, which keeps the ledger and the lock files of an open
  Office document out of git;
- `sources/00-INDEX.md` and `research/00-INDEX.md`, the two resource
  indexes, empty of entries;
- `recipes/readme.md`, the readme recipe whose render is the
  catalogue of the library, with its history companion
  `recipes/readme.history.md`.

A library gets no brief, no decisions file, no reviews or
challenges and no release notes. Its ledger (the single source of
truth for the state of a project, made at read time by the script
`scripts/forge-ledger.py` and never kept in git) is made like every
project's. Claude says once that the project is not under git until
you initialise its repository; that is a property of the project,
not a defect. Where `projects/lib-<name>/` already exists, the
command stops and reports instead of overwriting.

You should now see `projects/lib-<name>/` with the project file, the
two indexes and the readme recipe, and Claude proposing `/ingest`
for the first documents.

### Step 2: Put documents into the library

Run `/ingest <file> lib-<name>` for each document. The ingest is the
same one every project uses; its full course is in
[Register a source](register-a-source.md). What matters for a
library:

- The file is stored in `sources/` under a short descriptive slug,
  with no date in the name.
- For a binary file Claude asks one question: convert to Markdown?
  For a deck template or a reference document the answer is no: the
  file is a functional thing and is stored as it is, with no extract.
- Before anything is written Claude asks what the document is for.
  Your answer becomes the Role of its index entry.
- The entry lands in `sources/00-INDEX.md` with its Role, its Date and
  its Form, and the ledger is remade.

You should now see the file in `projects/lib-<name>/sources/` and
its entry in `projects/lib-<name>/sources/00-INDEX.md`.

### Step 3: Cite a library document from a project

In the project that needs the document, point `/ingest` at the
document's path: `/ingest projects/lib-<name>/sources/<document>
<slug>`. Another project's document is cited, not copied: nothing is
stored in the project's `sources/`. Claude adds an index entry that
names the path and says what the document is for. The ledger's
Dependencies table finds the citation by itself; nobody writes a
row there.

Moving a document out of a project into a library is the reverse:
ingest it in the library, then replace the project's entry with the
citation.

You should now see, in the project's `sources/00-INDEX.md`, an entry
that names the library path and, in the remade ledger, a row under
Dependencies for the library.

### Step 4: Name a template or a reference document in a recipe

A recipe that ends in a PowerPoint or a Word file names the file it
starts from in its `## Format` section. The section has two lines
for it:

- the plain file, made by `/render` through pandoc, names
  `reference <path | none>`;
- the published file, made by `/publish` through a model, names
  `template <path | none>`.

A deck template or a Word reference document is typically a document
of a library project. It is named by path, and the conversion
reaches it as the path it is given. Where no such file is wanted,
the line says `none`.

The roster of areas a BRD walks is a library document of the same
kind, cited by path; how the BRD uses it is in
[Write a BRD](write-a-brd.md).

You should now see the path in the recipe's Format section; the next
`/render` or `/publish` of that recipe starts from the file it
names.

### Step 5: See which libraries a project needs

Run `/forge <slug>` bare, with no target state. The state map it
reports includes which libraries the project needs, read from the
ledger's Dependencies table, and whether each is cloned alongside
under `projects/`. A library that is missing on this machine is
brought in with `/import-project` and the library's remote, the door
described in
[Bring in an existing project](bring-in-an-existing-project.md).

You should now see each library the project cites named in the map,
each with whether it is cloned alongside.

### Step 6: Maintain the library

A library has no chain. Bare `/forge lib-<name>` reports the
library's kind, its language, its sources and its research and
stops after the git line: no target states, no next step beyond
`/ingest`. `/forge <state> lib-<name>` says that a library has no
chain and stops; no state is worked there.

A document of a library is maintained by its owner. Where a file
changes after its registration, bare `/ingest lib-<name>` (the sweep)
reports it as changed and asks what to do. In a library a changed
document is ordinary maintenance: the index entry is updated, its
Date included, and nothing else. In a thought project the same event
would be a breach of immutability to resolve.

The library's README is a render of `recipes/readme.md`. Its inputs
are the ledger and the two indexes, so that the README is the
catalogue of what the library holds.

You should now see the index entry carrying the new Date, and the
README listing the library's documents after its next render.

## What you have afterwards

- A library under `projects/lib-<name>/` with its documents in
  `sources/`, each catalogued in `sources/00-INDEX.md` with what it
  is for.
- Projects that cite the library's documents by path, each citation
  an index entry of the project and a row under Dependencies in its
  ledger.
- Recipes whose Format section names a template or a reference
  document of the library by path.
- A state map (`/forge <slug>`) that names each library a project
  needs and whether it is cloned alongside.

## If something goes wrong

- **`/new-project` stops and reports that `projects/lib-<name>/`
  already exists.** The command never overwrites. Choose another
  slug, or work in the library that is there.
- **Claude asks whether the project is a library.** The slug has no
  `lib-` prefix, or your words left the kind open. Answer, or name
  the slug with the prefix.
- **`/forge <state> lib-<name>` says that a library has no chain and
  stops.** This is the rule, not an error: a library holds material
  and is not a project waiting for a brief. Work the chain in a
  thought project and cite the library from there.
- **`/ingest` stops before storing and asks about personal matter.**
  The document carries a named private person, an identifying detail
  or the like. Choose: store it as it is, redact it before
  registration, or drop it. It is never stored first and asked
  afterwards.
- **The check a save runs says that library `<name>` is not cloned
  alongside and names `/import-project` with its remote.** The
  project cites a document of a library that is not on this machine;
  the state map says the same of that library. The finding is
  advisory. Bring the library in with `/import-project`.
- **The check a save runs reports a path of the Dependencies table
  that does not exist on disk.** The citation names a document the
  library no longer has at that path. Correct the project's index
  entry, or restore the document in the library.
- **The sweep reports a library document as changed since its
  registration.** Say what to do with it. In a library the ordinary
  answer is to update the index entry with its Date; Claude never
  re-registers silently.
- **Claude says the library is not under git.** This is a property,
  not a defect. Initialising the repository and adding a remote are
  your one-off act.

## A worked example

You keep a deck template that every project's deck should start
from. The library is called `lib-<name>`; the project that needs it
has the slug `<slug>`.

1. `/new-project lib-<name>`. Claude infers the kind `library` from
   the prefix, asks for the language, creates the project file, the
   attributes, the ignore file, the two indexes and the readme recipe
   with its companion, says once that the library is not under git,
   and proposes `/ingest` for the first documents.
2. `/ingest deck-template.potx lib-<name>`. Claude stores the file as
   `projects/lib-<name>/sources/deck-template.potx`, asks whether to
   convert it to Markdown (you answer no: it is a functional thing),
   asks what it is for (you answer: the template every deck render
   starts from), writes the entry in `sources/00-INDEX.md` with that
   Role, its Date and its Form, and remakes the ledger. The reply is
   two lines: the file stored and its entry.
3. In the project: `/ingest
   projects/lib-<name>/sources/deck-template.potx <slug>`. Nothing is
   copied into `projects/<slug>/sources/`. Claude asks what it is
   for, adds an entry to the project's `sources/00-INDEX.md` that
   names the path, and remakes the ledger, whose Dependencies table
   now lists `lib-<name>`.
4. In the project's deck recipe, the `## Format` section names the
   published file's template as
   `projects/lib-<name>/sources/deck-template.potx`. The next
   `/publish` of that recipe starts from it.
5. `/forge <slug>`. The state map names `lib-<name>` among the
   libraries the project needs and says that it is cloned alongside.
6. A colleague clones `<slug>` on another machine without the
   library. There the map says that `lib-<name>` is not cloned
   alongside, and the check a save runs names `/import-project` with
   its remote. The colleague runs `/import-project` with the
   library's remote, and the next map says the library is cloned
   alongside.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md):
  why a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library
  shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md):
  cloning a library that is missing alongside.
- [Write a BRD](write-a-brd.md): the BRD that walks the instance's
  roster of areas, a library document.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
