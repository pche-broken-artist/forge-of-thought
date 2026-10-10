---
generated: 2026-10-10
made: derived
inputs-hash: 251ac03f4467c1f5
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md
---

# Share material through a library

This page is for a user who has material that more than one
project needs: a deck template, a reference document, a standard, a
piece of research. It says how to keep that material in a library,
how a project uses it without copying it, and how the forge tells
you when a library is missing. It was put together from the
`new-project`, `ingest` and `forge` skills, the `light` check and
`CLAUDE.md`, joined into one procedure.

## What a library is

A library is a project of kind `library`. Its slug starts with
`lib-`, so `projects/lib-<name>/` is a library and the forge
recognises it as one from the prefix.

A library has no chain: no brief, no intent, no layers below. What
it holds is:

- `ledger.md`, with `kind: library` in its header;
- `sources/` and `research/`, each with its `00-INDEX.md`
  catalogue;
- `recipes/readme.md` with its history companion, whose render is
  the library's `README.md`: a catalogue of what the library holds;
- optionally `logo.png` as the repository avatar.

There are no decisions, no reviews, no challenges and no release
notes. The documents of a library are resources: a functional
binary such as a `.potx` template or a graphic is a source like any
other, and a library carries no artefacts and no records but the
history companion of its readme recipe. Its documents are
maintained by their owner.

## Create a library

Run `/new-project lib-<name>`. The `lib-` prefix tells the command
the kind; if your words leave it open, it asks.

For a library the command creates only the ledger, the two resource
indexes and the readme recipe with its companion. It touches no
git: initialising the repository and adding a remote are your own
one-off act, and a library that is "not under git" is a property,
not a defect. The command finishes by proposing `/ingest` for the
first documents.

## Put documents into the library

Documents enter a library the way they enter every project: by
`/ingest`, with a file, with text pasted into the conversation, or
bare to sweep `sources/` for files not yet registered. Each document
is stored, registered in the ledger and catalogued in the index,
and you are asked what it is for. The ingest itself is the same
procedure as in a thought project; see "Register a source" below.

A binary gets one question: convert it to Markdown? For material a
library typically holds, a deck template or a graphic, the answer
is no: the binary is the source as a functional thing, stored,
registered and indexed as it is.

## Keep the library current

In a thought project a registered source is immutable, and a file
changed after registration is a breach to resolve. In a library it
is not: a changed document is the owner's ordinary maintenance.

Run bare `/ingest` in the library. The sweep reports every file
changed since its registration and asks what to do with each; for a
library the answer is simple: the index entry and the ledger date
are updated, nothing else. Nothing is ever re-registered silently.

## Use a library document from a project

A library document is cited, not copied. In the project that needs
it, point `/ingest` at the document by its path in the library,
`projects/lib-<name>/…`. Nothing is stored in the project's
`sources/`. Instead the command:

1. adds an entry to the project's `sources/00-INDEX.md` that names
   the path and says what the document is for;
2. adds a row to the Dependencies table of the project's ledger.

A dependency is registration only: a library document cited by
path carries no version, and what it is and is for lives in the
index entry.

Moving a document the other way, out of a project into a library,
is the reverse: ingest it in the library, replace the project's
entry with the citation, register the dependency.

### A deck template or a Word reference document

When a render of the project needs a template for a PowerPoint
file or a reference document for a Word file, the recipe's
`## Format` section is where the format and what each step needs
stand; the file is named there by its path in the library, never
copied into the project. How exactly a template or a reference
document is named is in the header of the conversion script,
`scripts/md2pptx.py` or `scripts/md2docx.py`. A recipe citation
that points outside the project needs its Dependencies row like any
other citation.

## See what a project needs

Bare `/forge` reports the project's map. Among its lines it names
which libraries the project needs, from the ledger's Dependencies
table, and whether each is cloned alongside under `projects/`.

Run bare `/forge` in the library itself and you get a shorter
report: its kind, whether it is under git, its sources and research
from the ledger and the indexes, and nothing more. A library is
material, not a project waiting for a brief, so the map lists no
chain, no target states and no next step beyond `/ingest`.

## Bring a missing library in

The `light` check, which a save runs, verifies that every path in
the Dependencies table exists on disk. A library that is not cloned
alongside is reported as the finding "library `<name>` not cloned
alongside - `/import-project <its remote>`". The finding is
advisory: run `/import-project` with the library's remote and the
library appears under `projects/lib-<name>/`, where the citations
resolve again.

The same check also verifies the other direction: every index
entry, recipe or chain citation that points outside the project has
a Dependencies row, and no row points inside the project.

## The library's own repository

Every project under `projects/` is a git repository of its own,
ignored by the engine's repository, and a library is no exception.
It has its own remote if you give it one, and it is saved, pulled
and shared as a repository of its own, separately from each project
that cites it. The projects that use it hold only the citation; the
material travels with the library.

## See also

- [About projects and the engine](../about/projects-and-the-engine.md): why a library is a kind of project and what a dependency means.
- [Register a source](register-a-source.md): the ingest the library shares with every project.
