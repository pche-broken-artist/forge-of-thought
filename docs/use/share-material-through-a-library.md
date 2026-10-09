---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md
---

# Share material through a library

This page is for a user who has material that more than one project
needs, such as a standard, a deck template or a body of research,
and wants to keep it in one place instead of copying it into each
project. It shows how to create a library, fill it, point a project
at its documents and bring a library in when a project needs one
that is not there. The page was put together from the `/new-project`,
`/ingest` and `/forge` commands, the `light` check and the core
rules in `CLAUDE.md`.

## What a library is

A library is a project of kind `library`. Its slug starts with
`lib-`, and it has no chain: no brief, no intent, no decisions, no
reviews or challenges, no release notes. What it holds:

```
projects/lib-<name>/
  .git/  ledger.md
  README.md  logo.png
  recipes/readme.md
  recipes/readme.history.md
  sources/00-INDEX.md
  research/00-INDEX.md
```

- `ledger.md` records what the library holds, with `kind: library`
  in its header.
- `sources/` and `research/` hold the material, each catalogued by
  its `00-INDEX.md`.
- `recipes/readme.md` is the recipe of the library's README, and its
  render is a catalogue of what the library holds. A library has a
  README only, no release notes.
- `logo.png` is optional.

A functional file such as a `.potx` deck template or a graphic is a
source like any other, so a library's assets need no kind of their
own.

## Create a library

1. Run `/new-project lib-<name>`. The `lib-` prefix tells the command
   that this is a library; if your words leave the kind unclear, you
   are asked.
2. The command creates only the ledger, the two resource indexes and
   the readme recipe with its history companion. Its readme recipe
   takes the ledger and the two indexes as inputs.
3. It ends by proposing `/ingest` for the first documents.

The command writes files only and never touches git. The library,
like every project, is a repository of its own: initialising it and
adding a remote is your own one-off act, for example
`git -C projects/lib-<name> init -b main`. Until then the library is
"not under git", which is a property, not a defect.

## Put documents into the library

Documents enter a library by `/ingest`, exactly as in any other
project: stored in `sources/`, registered in the ledger, given an
entry in the index, and you are asked what each is for. A binary such
as a deck template is kept as it is when you answer "no" to the
conversion question.

A library's documents are maintained by their owner. When you run a
bare `/ingest` (the sweep) in a library and a document has changed
since it was registered, that is ordinary maintenance, not a breach:
the index entry and the ledger date are updated, and nothing else.
In a thought project the same change would be a breach of
immutability to resolve.

Running `/forge lib-<name>` on a library reports its sources and
research and whether it is under git, and stops there: there is no
chain to work and no next step beyond `/ingest`.

## Use a library document in a project

A project uses a library document by citing its path. Nothing is
copied.

1. Run `/ingest` in your project and point it at the document in the
   library, a path under `projects/lib-<name>/`.
2. Nothing is stored in the project's `sources/`. Instead the project
   gets an index entry that names the path and says what the
   document is for, and a row in the ledger's Dependencies table.
3. A library document cited by path carries no version in the
   ledger.

To move a document out of a project into a library, work the other
way round: ingest it in the library, replace the project's index
entry with the citation, and register the dependency.

A recipe may also point at a library file, for instance a deck
template or a Word reference document for a render. What a render's
format needs stands in the recipe's `## Format` section; how a
template or a reference document is named is described in the help
header of `scripts/md2pptx.ps1` and `scripts/md2docx.ps1`. A recipe
that cites a path in another project is a dependency like any other
and needs its row in the Dependencies table.

## Check that the libraries are there

Run `/forge <slug>` for your project. Among the rest, the map says
which libraries the project needs, from the Dependencies table, and
whether each is cloned alongside it in `projects/`.

The `light` check (`/check light <slug>`) verifies the same
bookkeeping:

- every path in the Dependencies table exists on disk;
- every index entry, recipe or chain citation that points into
  another project has a row;
- no row points inside the project itself.

When a library is missing, the check reports, as advice, that the
library is not cloned alongside and suggests bringing it in with
`/import-project <its remote>`. That command takes the library's git
address and brings it into `projects/`.

## See also

- [About projects and the engine](../about/projects-and-the-engine.md): why a library is a kind of project and what a dependency means.
- [Register a source](register-a-source.md): the ingest the library shares with every project.
