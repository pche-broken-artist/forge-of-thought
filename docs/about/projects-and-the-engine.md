---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 54a4388cfd33e2af
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - projects/forge/10-intent.md#POS.0760
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.0960
  - projects/forge/10-intent.md#POS.1590
  - projects/forge/10-intent.md#POS.0970
  - projects/forge/10-intent.md#POS.1020
  - projects/forge/10-intent.md#POS.1030
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#REJ.0140
  - projects/forge/10-intent.md#REJ.0150
  - projects/forge/40-solution-design.md#SOL.0500
---

# Projects and the engine

The engine is the one public git repository that holds the forge
itself, and every project is a git repository of its own that the
engine does not know. This page explains how the two fit together on
disk, what a project declares about itself, where the facts of one
installation live, and why the relation has this shape and not
another. It is for anyone who uses the forge, extends it or weighs
whether to adopt it.

## What it is

The engine is one git repository with a remote. It holds the
universal core in its root:

- `CLAUDE.md` (the rules Claude works by)
- `README.md` (the page for humans)
- `templates/` (the canonical skeletons)
- `scripts/` (the scripts, among them the only way into git)
- `.claude/` (the commands, the agents and the settings)

Beside the core it holds `projects/forge`, the forge's own project:
Forge of Thought run through its own process.

Every other project lives under `projects/` as a git repository of
its own. The engine ignores the whole of `projects/` except
`projects/forge`. The scripts recognise a project by its
`projects/<slug>/.git`. A project may have any remote and any
visibility its owner gives it, or no remote, or no repository at
all. A project "not under git" is a property, not a defect.

A project is one of two kinds:

- a **thought project** (the chain of versioned documents that forges
  one idea, from a brief through the intent onward)
- a **library** (material shared across projects, with no chain: a
  ledger, sources and research with their indexes, and a README that
  catalogues them; its slug begins with `lib-`)

The ledger is the project's record of its state. This term and every
other term of the forge are on the [Glossary](../reference/glossary.md).

## How it works

### The nesting on disk

The diagram shows one engine with its own project and two nested
project repositories.

```
<engine root>/                 the engine's repository (public)
  CLAUDE.md  README.md
  templates/  scripts/  .claude/
  docs/                        the documentation; docs/videos/
  .gitignore                   projects/*  and  !projects/forge
  projects/
    forge/                     the forge's own project, tracked
                               by the engine's repository
    <slug>/                    a thought project
      .git/                    its own repository
      project.md               project: <slug>, kind: thought
    lib-<name>/                a library
      .git/                    its own repository
      project.md               project: lib-<name>, kind: library
```

The engine's `.gitignore` carries the pattern `projects/*` and
re-includes the forge's own project with `!projects/forge`. The
pattern must be `projects/*` and not `projects/`. With `projects/`
the re-include fails silently. The full layout, file by file, is on
[Repository layout](../reference/repository-layout.md).

### Creating a project and putting it under git

`/new-project` creates the files of a project and never touches git.
Putting a project under git is the user's own act, done once at its
creation:

```
git -C projects/<slug> init -b main
```

A remote follows if one is wanted. A project with a repository but
no remote is a legitimate shape, for instance a sensitive project
kept local. It keeps the history that its renders and recipes rely
on. A project with no repository at all is legitimate too, but it
keeps no history. The scripts in `scripts/` carry no address and no
identity. The commit identity belongs to git and is resolved by the
user's own git configuration, per host. The forge sets none.

### The project file

Every project has a project file, `project.md`, in its root. It
declares three things:

- `project` (the slug)
- `kind` (`thought` or `library`; `thought` by default)
- `language` (the language of the chain's artefacts, as an ISO 639-1
  code)

The file is written once, when the project is created, by
`/new-project` or by the migration. No working round writes it. Git
merges it as plain text. Every command that needs the kind or the
language of a project reads it from this file. A project without the
file has the shape from before the migration. The one remedy is
`/migrate`. Until it runs, nothing writes into the project.

The project carries only the marker of its kind. The rules of each
kind live in the engine. A project's optional `CLAUDE.md` is polish
only and never holds rules of a kind. Rules of a kind in the project
would copy the engine into the project.

### A library and the projects that use it

Another project cites a library document by its path. That citation
crosses from one repository into another. It is a dependency taken
knowingly. "Knowingly" means it is written down where state lives.
The project registers it in the Dependencies table of its ledger, one
row per document of another repository it cites. The row records no
version. A library document is maintained by its owner and is a
moving target by design. Only someone who has both repositories can
read the cited document. The assignment that comes out of a thought
project is self-contained anyway. How to use a library is on
[Share material through a library](../use/share-material-through-a-library.md).

### Facts of one installation

An installation of the forge is an instance. Its facts live in
`CLAUDE.local.md` at the engine root. That file is kept out of the
repository. It names two things:

- the principal (the person whose thinking is being forged), by role
- the language the conversation runs in

Everything in `CLAUDE.local.md` reaches every subagent, the isolated
reviewers included. A subagent is a separate run of Claude that does
one job and sees nothing of the conversation that started it. So the
file holds only what must always be present and is harmless in a
public report. Names, e-mail addresses and hosts of git identities
live in the user's own git configuration, outside the engine.

The forge's behaviour lives in the engine and never in the
assistant's private memory. Claude Code keeps a memory per directory,
outside the repository. Whatever it learns there about how the forge
should work is written into `CLAUDE.md`, the commands or the
templates, and removed from the memory. The memory keeps only what is
personal to one principal.

### Upgrades and public files

A project records no engine version: it follows the engine, and how
it does is on [Upgrades and migration](upgrades-and-migration.md).

The engine is the one public place of an instance: what a project
shows in public goes out as a file into the engine's `docs/videos/`,
as [The screenplay and its player](the-screenplay-and-its-player.md)
describes.

## Why

The engine is public and contains nothing sensitive and no instance
facts. Users keep their projects wherever they choose. They are
responsible themselves for what their projects contain and where
they live. Generated decks that carry an organisation's branding are
among those contents.

Each project is its own repository and therefore has its own
visibility. Access can then be given project by project. A library is
a repository of its own for the same reason.

The engine does not know the projects. Upgrading the engine is a
fast-forward of its `main` branch.

Why the projects sit inside the engine's tree, rather than anywhere
on disk, beyond the fact that the scripts find them there by their
`.git`: the reason is not recorded.

The project file exists because the ledger is made at read time and
kept out of git. Without the project file the slug, the kind and the
language would have no home. A library's repository, at its
creation, is this file alone.

Instance facts stay out of the engine. The engine can then be public.
Behaviour stays out of the memory. Every instance of the forge then
behaves the same, and a new user meets the same forge as the
principal who built it.

### The shapes rejected

These shapes of the relation between the engine and its projects
were rejected:

- git submodules, subtree and worktrees (they model a dependency, and
  this relation is not one)
- the engine as a template repository, and copying the engine into
  each project (every comparable project that does so ends in
  manifests, override layers and migrations)
- a plugin as the only shape for now (the reason is not recorded)
- a `local/` directory as the home of user-local files (it existed
  only to keep material that must not be public out of the
  repository, which the ignored `projects/*` now does; deck templates
  live in a library and are named by path)

## A worked example

An instance has the engine and three projects under `projects/`:
`forge`, `my-idea` and `lib-decks`.

- `projects/forge` is tracked by the engine's repository and is
  public with it.
- `projects/my-idea` is a thought project. Its owner ran
  `git -C projects/my-idea init -b main` and added no remote. The
  project stays on this machine and keeps its history. Its project
  file reads:

  ```
  ---
  project: my-idea
  kind: thought
  language: en
  ---
  ```

- `projects/lib-decks` is a library with a private remote. It holds a
  deck template. Its project file reads `project: lib-decks` and
  `kind: library`.

A recipe in `my-idea` names the deck template in `lib-decks` by its
path. `my-idea` registers that path in the Dependencies table of its
ledger, with no version. The engine's repository never lists
`my-idea` or `lib-decks`.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
