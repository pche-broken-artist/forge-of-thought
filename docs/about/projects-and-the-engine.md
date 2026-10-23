---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: a9d11b5f280b2e7e
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - projects/forge/10-intent.md#POS.0550
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

The engine is the one git repository that holds the forge itself,
and every other project is a git repository of its own that the
engine does not know. This page explains how the two are arranged,
how a project is recognised, what a project declares about itself,
and why the forge is built this way. It is for anyone who uses the
forge, extends it or weighs whether to adopt it.

## What it is

The engine is one public git repository. It holds two things:

- the universal core in its root: `CLAUDE.md` (the rules Claude
  works by), `README.md` for humans, `templates/`, `scripts/` and
  `.claude/`;
- `projects/forge`, the forge's own project (the forge run through
  its own process).

Every other project lives under `projects/` as a repository of its
own. The engine ignores `projects/` in git, with `projects/forge` as
the one exception. Each project repository may have any remote and
any visibility its owner gives it, or no remote at all, or no
repository at all.

A project is one of two kinds:

- **thought**: a project with a chain of documents, starting at a
  brief and running through the intent (the principal's positions);
  the default kind;
- **library**: shared material with no chain, used across projects.

Here the principal is the person whose thinking is being forged.

```
<engine root>/                  the engine: one public repository
  CLAUDE.md  README.md
  templates/  scripts/  .claude/
  .gitignore                    projects/*  and  !projects/forge
  projects/
    forge/                      the forge's own project, tracked
                                by the engine
    <slug>/                     a thought project: a repository
      .git/                     of its own, ignored by the engine
      project.md
      00-brief.md  10-intent.md  ...
    lib-<name>/                 a library: a repository of its
      .git/                     own, ignored by the engine
      project.md
      sources/  research/  recipes/readme.md
```

The full layout, file by file, is on
[Repository layout](../reference/repository-layout.md). Every term
used here has one line in the [Glossary](../reference/glossary.md).

## How it works

### How a project is recognised

The scripts ask git one question about a project: is the project's
directory the top of a repository? They never look for a `.git`
folder. When git names the project's directory as the top, the
project is under git, and the scripts commit, push and pull it.

Anything else is a project outside git. That covers two cases:

- the directory has no repository at all;
- the directory lies inside another repository, so that the top of
  the repository is somewhere above it.

For a project outside git, the forge writes its files to disk and
runs no git on it. The repository above it belongs to its owner.
The forge asks that repository nothing, not even what it tracks. A
project outside git is a property, not a defect.

### How a project comes in

A project is created by `/new-project`, which writes files only and
never touches git. Making the project a repository and adding a
remote is the user's own one-off act:

```
git -C projects/<slug> init -b main
```

A remote follows if one is wanted. The scripts carry no address
and no identity. An existing project with a remote is brought in by
`/import-project`. A project outside git comes in by hand, as a
copy or a link into `projects/`, and the forge knows it from then
on.

### The ignore pattern

The engine's `.gitignore` names `projects/*` and re-includes
`!projects/forge`. The pattern must be `projects/*` and not
`projects/`. With `projects/`, the re-include fails silently.

### The project file

Every project has a project file, `project.md`, written once at its
creation by `/new-project` or by a migration, never by a working
round. It declares three things:

- `project`: the slug of the project;
- `kind`: `thought` or `library`;
- `language`: the language of the chain's artefacts, as an ISO
  639-1 code.

It is read wherever the kind or the language of a project is needed.
The rules of each kind live in the engine. The project carries only
the marker. A project's optional `CLAUDE.md` is polish and never
holds rules of its kind.

A project without a project file has the shape from before a
migration. The one remedy is `/migrate`.

### A library

A library is a project of kind `library`, named with the prefix
`lib-`. It has no chain. It holds a ledger, `sources/` and
`research/` with their indexes, and a README rendered from
`recipes/readme.md` that catalogues what it holds. The ledger is the
project's state, made from its documents when it is read. Its
documents are maintained by their owner, who may overwrite one or
put a new version beside it.

Another project cites a library document by its path. Such a
citation is a dependency on another repository, taken knowingly:

- only someone who has both repositories can read it;
- the citation carries no version, because the library document is a
  moving target by design;
- the citing project registers it in the Dependencies table of its
  ledger.

How you use a library is on
[Share material through a library](../use/share-material-through-a-library.md).

### What lives outside the engine

The facts of one installation (an instance) live in
`CLAUDE.local.md` at the engine root. That file says who the
principal is by role, the language the conversation runs in and the
handle the principal signs records with. It is kept out of the
repository. The commit identity is not the forge's: it lives in the
user's own git configuration, resolved per host, and the forge sets
none.

How the forge behaves lives in the engine, in `CLAUDE.md`, the
commands and the templates. It never lives in the assistant's
private memory. The assistant (Claude Code) keeps a memory per
directory outside the repository. Whatever it learns there about
how the forge should work is written into the engine and removed
from that memory. Only what is personal to one principal stays in
memory.

### Two consequences

A project records no engine version: how it follows the engine is
on [Upgrades and migration](upgrades-and-migration.md).

The engine is the one public place of an instance, so a file a
project shows in public goes out into the engine's `docs/videos/`
while the project stays where it is, as
[The screenplay and its player](the-screenplay-and-its-player.md)
explains.

## Why

**Publication with nothing sensitive.** The engine (the core
together with `projects/forge`) is public. It contains nothing
sensitive and no instance facts. Users keep their projects wherever
they choose. They are responsible for what those projects contain
and where they live, generated decks with a company's branding
included. Keeping projects out of the engine's repository is what
lets the engine be published.

**Access per project.** Because every project is its own repository,
it has its own visibility. A library has its own repository and
therefore its own visibility too.

**A project without a remote, or without a repository, is
legitimate.** A sensitive project may be kept local. A repository
without a remote keeps the history that renders and recipes rely on.
A project with no repository does not keep it.

**Work inside the engine.** Projects lie under `projects/` inside
the engine's directory, and the same scripts serve the engine and
every project repository. A reason beyond that arrangement is not
recorded.

**The repository above is not asked.** A project lying inside
someone else's repository belongs to that repository's owner. So the
forge runs no git there and asks it nothing.

**Why instance facts are kept out and kept small.** Everything in
`CLAUDE.local.md` reaches every subagent (a separate Claude run with
its own brief, such as an isolated reviewer). So only what must be
always on and is harmless in a public report lives there. Names,
e-mail addresses and hosts live in the user's own git
configuration.

**Why behaviour never lives in memory.** Every instance of the forge
then behaves the same. A new user meets the same forge as the
principal.

**Why the project file exists.** The ledger is made when it is read
and is kept out of git. The slug, the kind and the language of a
project therefore need a home of their own. A library's repository
is, at its creation, this file alone.

### The shapes rejected

- **Git submodules, subtree and worktrees.** They model a
  dependency, and the relation between the engine and its projects
  is not one.
- **The engine as a template repository, or the engine copied into
  projects.** Every comparable project that does so ends in
  manifests, override layers and migrations.
- **A plugin as the only shape.** It is rejected for now. The reason
  is not recorded.
- **A `local/` folder for user-local files.** It existed only to
  keep company material out of the repository. The ignored
  `projects/*` does that. Deck templates live in a library and are
  named by path.

## A worked example

You start a new thought project with the placeholder slug
`my-idea`:

```
/new-project my-idea
```

The command writes `projects/my-idea/` with its `project.md`:

```
---
project: my-idea
kind: thought
language: en
---
```

The engine's git does not see the folder, because `projects/*` is
ignored. Until you act, `my-idea` is a project outside git: Claude
writes its files, and the scripts run no git on it.

You make it a repository of its own:

```
git -C projects/my-idea init -b main
```

Now git names `projects/my-idea` as the top of a repository, and the
scripts save it on its own. You may add a private remote, a public
one, or none. The engine's repository is unchanged throughout.

## See also

- [Share material through a library](../use/share-material-through-a-library.md):
  using a library.
- [Upgrades and migration](upgrades-and-migration.md): why a project
  records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md):
  the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout,
  file by file.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
