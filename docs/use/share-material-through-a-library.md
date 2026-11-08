---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: d313467c2cbf65ab
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

A library is a project that holds material shared across projects
and has no chain of its own. This page is for you, the user who
keeps a deck template, a reference document, a standard or a roster
in one place and wants every project to cite it from there instead
of copying it. It shows how a library is born, how documents enter
it, how a project cites one of them, and how Claude tells you when a
library a project needs is not there.

## When to use it

Use a library when the same document serves more than one
[project](../about/projects-and-the-engine.md): a presentation
template, a Word reference document that carries the house styles,
a group standard, a regulation, or the roster of the areas of the
enterprise a BRD must walk. A library is a project of kind
`library`; its slug starts with `lib-`. It carries no brief, no
intent and no layer below one: only the material and its
catalogue. The documents in it are maintained by their owner, and a
project reaches one of them by its path.

Use a thought project instead when the material is the thinking of
one principal (the person whose thinking is being forged) and is to
be mined into a brief and an intent.

## What you do

The commands, each typed as it stands, with `lib-<name>` for the
library's slug and `<slug>` for the project that uses it:

```
/new-project lib-<name>
/ingest <file> lib-<name>
/ingest projects/lib-<name>/sources/<file> <slug>
/forge <slug>
```

The first makes the library. The second puts a document into it. The
third makes a project cite that document by its path. The fourth
shows, in the state map of the project, which libraries it needs and
whether each one is cloned alongside.

## What happens

### 1. The library is born

Type `/new-project lib-<name>`. Claude reads the kind from the
prefix `lib-` or from your words; where that leaves it unclear, it
asks. The slug is lowercase, hyphens and no spaces. The command
writes files only and never touches git: initialising the library's
own repository and adding a remote are your one-off act, the way in
named in `CLAUDE.md`, Persistence. A library that is not under git
is a property, not a defect, and Claude says so once at the end.

What the command creates:

- `project.md`: the project file, with the slug, the kind `library`
  and the language, written once
- `.gitattributes`: the ways of merging by path
- `.gitignore`: what never enters git, the ledger among it
- `sources/00-INDEX.md` and `research/00-INDEX.md`: the catalogues
  of the material, empty at birth
- `recipes/readme.md` with its companion `recipes/readme.history.md`:
  the recipe of the README, whose inputs are the ledger and the two
  indexes, so that the README is the catalogue of what the library
  holds

Nothing else: no brief, no decisions file, no reviews or challenges,
no release notes. The ledger (the single source of truth for the
project's state, made at read time by `python
scripts/forge-ledger.py lib-<name>`) is made like every project's and
is never in git.

You should now see the folder `projects/lib-<name>/` with those
files, and Claude proposing `/ingest` for the first documents.

### 2. Documents enter the library

Type `/ingest <file> lib-<name>`. This is the same ingest every
project shares; the whole of it is on
[Register a source](register-a-source.md). In short: the document is
stored in `sources/`, Claude asks what it is for before the index
entry exists, and for a binary (a deck template, a reference
document) Claude asks whether to convert it to Markdown. A template
that is to be used as a template is kept as it is: the binary is
the source as a functional thing, with no extract.

You should now see the file under `projects/lib-<name>/sources/` and
its entry in `sources/00-INDEX.md`, with its role, its date and its
form.

### 3. A changed document is maintenance

The owner of a library's document may change it. Bare `/ingest` in
the library sweeps `sources/` and reports every file changed since
its registration, with a question what to do with each. In a
library the answer is ordinary maintenance: the index entry is
updated, its Date included, and nothing else. In a thought project
the same report would mean a breach of a source's immutability;
in a library it does not. Claude never re-registers silently.

You should now see the index entry carrying the new date and the
file left where it is.

### 4. A project cites a library document

In the project that uses the document, type
`/ingest projects/lib-<name>/sources/<file> <slug>`. Nothing is
stored in the project's `sources/`: another project's document is
cited, not copied. Claude adds an entry to the project's
`sources/00-INDEX.md` that names the path and says what the document
is for. The ledger finds the citation by itself and lists it in its
Dependencies table; the rows there are the citations the script
found, and nobody adds one by hand.

Moving a document out of a project into a library is the reverse:
ingest it in the library, then replace the project's entry with the
citation.

You should now see the citation in the project's index and, after
the ledger is remade, the library's document under Dependencies.

### 5. A template or a reference document is named in a recipe

A render that is to become a deck or a Word document names its
template in the recipe's `## Format` section: for the plain file,
`reference <path | none>`; for the published file,
`template <path | none>`. The path is typically that of a document
in a library project, `projects/lib-<name>/sources/<file>`. The
conversion scripts take the path as they are given it; a recipe
without a Format section ends at the Markdown.

The roster of the areas a BRD walks is such a library document too,
cited by path from the instance's library; what the BRD does with it
is on [Write a BRD](write-a-brd.md).

You should now see the path in the recipe's Format section, and the
file made from the render carrying the template's styles.

### 6. The state map says what the project needs

Type `/forge <slug>` in the project. The map lists, among the rest,
which libraries the project needs, read from the ledger's
Dependencies table, and whether each is cloned alongside under
`projects/`.

Typed in the library itself, `/forge lib-<name>` reports the kind,
the language, whether the library is under git, and its sources and
research, then stops: a library is material, not a project waiting
for a brief, and it has no chain, no target states and no next step
beyond `/ingest`.

You should now see the libraries the project depends on, each with
the word whether it is cloned alongside.

## What you have afterwards

- one library, `projects/lib-<name>/`, a repository of its own once
  you initialise it, with its material catalogued in
  `sources/00-INDEX.md` and `research/00-INDEX.md` and a README
  that is the catalogue
- in every project that uses it, an index entry that cites the
  document by path and a row under Dependencies in the ledger
- recipes that name a template or a reference document by that path

## If something goes wrong

- `projects/lib-<name>/` already exists: `/new-project` stops and
  reports; it never overwrites.
- `/forge <state> lib-<name>`: Claude says that a library has no
  chain and stops; no state is worked there.
- A library a project cites is not cloned alongside: the light
  check, which a save runs, reports it as an advisory finding,
  "library `<name>` not cloned alongside - `/import-project <its
  remote>`". Bring the library in as
  [Bring in an existing project](bring-in-an-existing-project.md)
  says.
- Bare `/ingest` reports a changed document in the library: update
  its index entry, its Date included, and nothing else.
- A document that carries personal matter: `/ingest` stops before
  storing it and asks whether to store it as it is, redact it before
  registration, or drop it.
- The library is "not under git": a property, not a defect; the
  way in is yours, named in `CLAUDE.md`, Persistence.

## A worked example

A house keeps its presentation template and the roster of the areas
every BRD must consider in one library, and a thought project uses
both.

1. `/new-project lib-<name>`. Claude creates
   `projects/lib-<name>/` with `project.md` (kind `library`),
   `.gitattributes`, `.gitignore`, the two empty indexes and the
   readme recipe with its companion, says once that the library is
   not under git until you initialise it, and proposes `/ingest`.
2. `/ingest deck-template.potx lib-<name>`. Claude stores it as
   `sources/deck-template.potx`, asks whether to convert it to
   Markdown (no: it is a template, used as a functional thing), asks
   what it is for, and writes the index entry.
3. `/ingest area-roster.md lib-<name>`. A text file gets no
   conversion question; Claude asks what it is for and writes the
   entry.
4. In the thought project `<slug>`:
   `/ingest projects/lib-<name>/sources/area-roster.md <slug>`.
   Nothing is stored; the project's index gains an entry naming the
   path, and the remade ledger lists the roster under Dependencies.
5. In the project's deck recipe, the Format section says
   `template projects/lib-<name>/sources/deck-template.potx`, and
   the published deck is made in the template's style.
6. `/forge <slug>` shows `lib-<name>` among the libraries the
   project needs, cloned alongside. On a second machine where it is
   not, the map says so, the light check files the advisory finding
   at the next save, and `/import-project` with the library's
   remote brings it in.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
