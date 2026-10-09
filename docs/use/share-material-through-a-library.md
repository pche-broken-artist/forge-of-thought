---
generated: 2026-10-09
made: derived
inputs-hash: 1015d1bcd1764909
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/forge/SKILL.md
  - .claude/agents/check-light.md
  - CLAUDE.md
---

# Share material through a library

This page is for a user who has material that more than one project
needs - a deck template, a reference document, a standard, a piece of
research - and wants to keep it in one place instead of copying it
into every project. It was put together from the skills
`new-project`, `ingest` and `forge`, the `light` check and
`CLAUDE.md`, and joins what they say into one procedure: make a
library, put documents into it, point a project at them, and keep
the two in step.

## What a library is

A library is a project of kind `library`. Its slug starts with
`lib-`, so it lives at `projects/lib-<name>/`. Unlike a thought
project it has no chain: no brief, no intent, no decisions, no
reviews or challenges, no release notes. What it holds is material
shared across projects, and nothing else:

- `ledger.md`, with `kind: library` in its header, reduced to the
  tables a library needs
- `sources/` and `research/`, each with its `00-INDEX.md` catalogue
- `recipes/readme.md` with its companion `recipes/readme.history.md`;
  the README rendered from it is the catalogue of what the library
  holds
- `README.md` and, if you supply one, `logo.png` in the root

A functional binary - a `.potx` template, a graphic - is a source
like any other, so a library's assets are ordinary resources. A
library carries no artefacts and no records beyond the history
companion of its readme recipe.

Like every project, a library is a git repository of its own, which
the engine does not track. Initialising it and adding a remote are
your one-off act; a library "not under git" is a property, not a
defect. Because it is a repository of its own, where it lives and who
can reach it is a matter of that repository, not of the engine or of
any project that uses it.

## Make a library

Run `/new-project lib-<name>`. The `lib-` prefix tells the command
that the kind is `library`; if your words leave the kind unclear, it
asks. It creates files only, never touching git:

- `projects/lib-<name>/ledger.md` from the ledger template, with
  `kind: library`
- `sources/00-INDEX.md` and `research/00-INDEX.md` from the index
  template, headers filled and no entries yet
- `recipes/readme.md` from the readme recipe template, with the
  ledger and the two indexes as its inputs, and its companion
  `recipes/readme.history.md`

Nothing of the chain is created. The command finishes by proposing
`/ingest` for the first documents and reminds you once that the
library is not under git until you initialise its repository.

## Put documents into the library

Documents enter a library the way they enter every project: through
`/ingest`, which stores the file in `sources/`, records it in the
ledger, adds an index entry and asks what it is for. The procedure is
the same as for any source and is described on the page linked
below; two things differ in a library.

First, a binary stays a binary when it is a functional thing. When
`/ingest` meets a `.pptx`, `.docx` or similar file it asks, per file,
whether to convert it to Markdown. For a deck template or a reference
document the answer is no: the binary is the source as it is, stored,
registered and indexed without an extract.

Second, a changed document is maintenance, not a breach. In a thought
project a source is immutable from registration, and a file changed
afterwards is a breach to resolve. In a library the documents are
maintained by their owner: when a bare `/ingest` sweep finds a file
changed since its registration, it updates the index entry and the
ledger date, nothing else. It still never re-registers silently;
it reports the change and asks.

## Use a library document from a project

A project never copies a library document. When you point a project
at a document that lives in `projects/lib-<name>/…`, `/ingest` stores
nothing in the project's `sources/`. Instead it

- adds an entry to the project's `sources/00-INDEX.md` that names the
  document's path and says what it is for, and
- adds a row to the Dependencies table of the project's `ledger.md`.

The row is registration only: a library document, cited by path,
carries no version in the project's ledger. What it is and is for
stays in the index.

A deck template or a Word reference document is used by a render in
the same way, by path. The format of a render and what each step
needs stand in the recipe's `## Format` section; that is where the
template or the reference document from the library is named. The
exact way a template or a reference document is named is the header
of the conversion script, `scripts/md2pptx.py` or
`scripts/md2docx.py`.

Moving a document the other way, out of a project into a library, is
the reverse of the same step: ingest it in the library, replace the
project's own entry with the citation, and register the dependency.

## See which libraries a project needs

Bare `/forge` on a project reports, among the rest of its map, which
libraries the project needs - the rows of the ledger's Dependencies
table - and whether each is cloned alongside under `projects/`. If a
library is missing, bring it in with `/import-project <git-url>`,
which clones an existing project into `projects/`.

The `light` check, which `/save` runs, verifies the same thing: every
path in the Dependencies table exists on disk, every index entry,
recipe or chain citation pointing outside the project has a row, and
no row points inside the project. A library that is not cloned
alongside is an advisory finding, worded "library `<name>` not cloned
alongside - `/import-project <its remote>`"; it informs you and
blocks nothing.

Bare `/forge` on the library itself reports its sources and research
from the ledger and the indexes, says whether it is under git, and
stops there: a library is material, not a project waiting for a
brief, so there are no target states and no next step beyond
`/ingest`.

## See also

- [About projects and the engine](../about/projects-and-the-engine.md): why a library is a kind of project and what a dependency means.
- [Register a source](register-a-source.md): the ingest the library shares with every project.
