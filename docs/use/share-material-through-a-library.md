---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: d244632c85636a2c
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md#Repository layout
---

# Share material through a library

A library is a project of the kind `library`: a place for material
that several projects share, with no chain of artefacts of its own.
This page is for you, the user who keeps a deck template, a house
graphic or a reference document in one place and wants every project
to use it from there. It says how a library is born, how documents
enter it, how a project cites one of them, and how Claude tells you
when a library a project needs is not there.

## When to use it

Use a library when the same document serves more than one project:
a deck template, a graphic, a logo, a standard, a research note.
Each project would otherwise carry its own copy in `sources/`, and
the copies would drift apart. A library holds the one copy; the
projects cite it by path.

Use a thought project, not a library, when what you want to keep is
thinking: a library carries no brief, no intent, no decisions, no
reviews and no challenges. Why a library is nevertheless a project
of the forge is said in [Projects and the engine](../about/projects-and-the-engine.md).

## What you do

Each step of the job has its own command. The slug of a library
starts with `lib-`; Claude infers the kind from that prefix or from
your words and asks when it is unclear.

To make a library:

```
/new-project lib-<name>
```

To put a document into it, or to sweep its `sources/` folder for
files you dropped there:

```
/ingest <file> lib-<name>
/ingest lib-<name>
```

To point a project at a document of the library, name the path of
the document in the ingest of that project:

```
/ingest projects/lib-<name>/sources/<file> <slug>
```

To see which libraries a project needs and whether each is there:

```
/forge <slug>
```

To bring a missing library in beside the projects:

```
/import-project <git-url>
```

## What happens

### 1. The library is born

`/new-project lib-<name>` creates files only; it never touches git.
A library gets a smaller set of files than a thought project:

- `ledger.md`, with `kind: library` in its header, reduced as the
  ledger template says for that kind
- `sources/00-INDEX.md` and `research/00-INDEX.md`, the catalogues
  of the two resource folders
- `recipes/readme.md`, the recipe of the README, with the ledger
  and the two indexes as its inputs, and its history companion
  `recipes/readme.history.md`

No brief, no decisions, no reviews or challenges and no release
notes are created. The README of a library is a catalogue of what
it holds: a render of `recipes/readme.md`. Claude finishes by
proposing `/ingest` for the first documents and by saying once that
the project is not under git until you initialise its repository;
that is a property of the project, not a defect.

You should now see `projects/lib-<name>/` with the ledger, the two
indexes and the readme recipe, and Claude's offer to ingest the
first documents.

### 2. Documents enter by ingest

`/ingest <file> lib-<name>` stores the file in `sources/` under a
short slug, registers it in the library's ledger (the table of its
state, freely rewritten) and adds an entry to `sources/00-INDEX.md`
that says what the file is. A date is recorded if it can be found
for free; Claude never asks you for one. This is the same ingest
every project uses; the whole of it is in
[Register a source](register-a-source.md).

Two questions can come your way. For a binary file (a PDF, a DOCX,
a PPTX, an XLSX) Claude asks whether to convert it to Markdown: say
no for a file that is wanted as a functional thing, such as a deck
template, a graphic or a logo, and it is stored, registered and
indexed as it is, with no extract. After every registration Claude
asks "what is it for?": your answer is the Role of the index entry,
or you tell Claude to infer it from what the file itself declares,
and the entry is then marked *(inferred)*.

You should now see the file in `projects/lib-<name>/sources/`, a row
in the library's ledger and an entry in its index, and Claude's
question what the file is for.

### 3. A changed document is maintenance

The documents of a library are maintained by their owner. When one
of them changes, a bare `/ingest lib-<name>` reports the files whose
modification time is later than their registration date and asks
what to do with each. In a library a changed document is ordinary
maintenance: Claude updates the index entry and the date in the
ledger, nothing else. Nothing is re-registered silently.

This differs from a thought project. There a changed source is a
breach of immutability to resolve: re-register beside as a new
source, restore, or accept the change knowingly on your word.

You should now see the index entry and the ledger date of the
changed document brought up to date.

### 4. A project cites, never copies

When you point a project at a document that lives in a library
(`projects/lib-<name>/…`), nothing is stored in the project's
`sources/`. Claude adds an index entry to the project's
`sources/00-INDEX.md` that names the path and says what the document
is for, and a row in the Dependencies table of the project's ledger.
A recipe that names a library file by path, such as a deck template
for a render, is a citation of the same kind and needs the same
row: the check that runs at a save looks for every citation pointing
outside the project and expects a Dependencies row for each.

Moving a document out of a project into a library is the reverse:
ingest it in the library, replace the project's entry with the
citation, register the dependency.

You should now see an index entry in the project that names
`projects/lib-<name>/…`, and a row in the Dependencies table of the
project's ledger.

### 5. The map says what the project needs

Bare `/forge <slug>` reports, among the rest of the project's state,
which libraries the project needs, read from the Dependencies table
of its ledger, and whether each is cloned alongside under
`projects/`. On a library itself the map is short: it says the kind,
whether the library is under git, its sources and research, and
stops there; a library is material, not a project waiting for a
brief, so there are no target states and no next step beyond
`/ingest`.

You should now see one line per library the project depends on,
each with the word whether it is present.

### 6. A missing library is brought in

When a library a project cites is not cloned alongside, the light
check reports it as an advisory finding: library `<name>` not cloned
alongside, with the command to bring it in. `/import-project
<git-url>` clones it from its remote into `projects/`; the whole of
that job is in
[Bring in an existing project](bring-in-an-existing-project.md).

You should now see `projects/lib-<name>/` beside the other projects,
and the finding gone from the next check.

## What you have afterwards

- one library under `projects/lib-<name>/`, a git repository of its
  own once you initialise it, with a ledger of kind `library`, the
  two resource indexes, a readme recipe with its history, and the
  documents in `sources/` and `research/`
- a README of the library that catalogues what it holds, rendered
  from `recipes/readme.md`
- in every project that uses the library, an index entry per cited
  document and a Dependencies row per citation, and no copy
- a `/forge` map of each such project that names the library and
  says whether it is present

## If something goes wrong

- **Claude asks what kind of project you mean.** The slug does not
  start with `lib-` and your words left the kind open. Answer
  `library`, or give the slug the prefix.
- **`/new-project` stops and reports that the folder exists.** The
  command never overwrites a project. Choose another slug.
- **`/ingest` stops before storing a file.** The text carries
  personal matter: a named private person, an identifying detail,
  health, anything of the kind. Claude asks whether to store the
  file as it is, redact it before registration, or drop it; a
  registered source is immutable, so this is asked first and never
  afterwards.
- **The file lands under a slug ending in `-2`.** A file of that
  slug is already registered; the new one got the suffix.
- **The index entry's Role shows a bare dash.** You have not yet
  answered "what is it for?". Answer, or tell Claude to infer it.
- **A sweep reports a file changed since registration.** In a
  library this is maintenance: Claude updates the index entry and
  the ledger date on your word. Nothing is re-registered silently.
- **The light check reports that library `<name>` is not cloned
  alongside.** A path in the Dependencies table does not exist on
  disk. The finding is advisory and names the command to run:
  `/import-project <its remote>`. Bring the library in with it.
- **The light check reports a citation without a Dependencies row,
  or a row pointing inside the project.** Every index entry, recipe
  or chain citation that points to `projects/<other>/…` needs a row,
  and no row may point inside the project itself. Add or remove the
  row; the check marks this as an immediate fix.

## A worked example

You keep a deck template that three projects render their pitches
with. You make a library for it:

```
/new-project lib-assets
```

Claude creates `projects/lib-assets/` with `ledger.md` (kind
`library`), `sources/00-INDEX.md`, `research/00-INDEX.md`,
`recipes/readme.md` and `recipes/readme.history.md`, says once that
the library is not under git until you initialise its repository,
and offers `/ingest` for the first documents.

You drop `deck-template.potx` into `projects/lib-assets/sources/`
and sweep:

```
/ingest lib-assets
```

Claude finds the unregistered file and asks whether to convert it to
Markdown. You say no: the template is wanted as a functional thing.
It is registered as it is, indexed, and Claude asks what it is for.
You answer "the deck template of every pitch"; that is the Role of
the entry.

Now you point the project `alpha` at it:

```
/ingest projects/lib-assets/sources/deck-template.potx alpha
```

Nothing is copied into `projects/alpha/sources/`. The project's
`sources/00-INDEX.md` gets an entry naming the path and what it is
for, and the Dependencies table of `projects/alpha/ledger.md` gets a
row for `lib-assets`. The pitch recipe of `alpha` names the template
by that path.

On another machine, with `alpha` cloned but `lib-assets` not,
`/forge alpha` reports that the project needs `lib-assets` and that
it is not cloned alongside, and the light check at the next save
files the advisory finding with the command to run:

```
/import-project <git-url>
```

After it, `projects/lib-assets/` stands beside `projects/alpha/`,
and the next `/forge alpha` says the library is present.

## See also

- [Projects and the engine](../about/projects-and-the-engine.md): why a library is a kind of project.
- [Register a source](register-a-source.md): the ingest the library shares with every project.
- [Bring in an existing project](bring-in-an-existing-project.md): cloning a library that is missing alongside.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
