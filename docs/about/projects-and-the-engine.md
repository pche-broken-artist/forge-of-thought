---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: d020514ff0ac3bed
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

The engine is the one public repository of Forge of Thought: its core
and its own project. Every other project is a git repository of its
own that the engine does not know. This page explains how the two fit
together, how the scripts tell a project under git from one outside
it, and why the forge is split this way. It is for anyone who uses
the forge, extends it or weighs whether to adopt it.

## What it is

The **engine** is one git repository with a remote. It holds the
universal core in its root:

- `CLAUDE.md`: the rules Claude works by.
- `README.md`: the description for humans.
- `templates/`: the canonical skeletons.
- `scripts/`: the programs that do the mechanical work, git among it.
- `.claude/`: the commands, the agents and their settings.

Beside the core it holds `projects/forge`, the forge's own project:
Forge of Thought run through its own process. In the engine `main` is
the released line. Branches are allowed and left to git.

A **project** is one body of work forged with the engine. Every
project other than `projects/forge` lives under `projects/<slug>/`
and is a repository of its own where its owner wants one. Its owner
gives it whatever remote and visibility he chooses, or none. The
engine ignores these repositories: its `.gitignore` excludes
`projects/*` and re-includes `projects/forge` alone.

The engine carries no instance facts. An instance is one
installation of the forge. Who the principal is (the person whose
thinking is forged, named by role), the language the conversation
runs in and the handle the principal signs records with live in
`CLAUDE.local.md` at the engine root. That file is kept out of the
repository.

## How it works

### The layout

```
engine root/                 one git repository, public
  CLAUDE.md  README.md       the universal core
  templates/  scripts/  .claude/
  CLAUDE.local.md            instance facts, never in git
  .gitignore                 projects/*   then   !projects/forge
  projects/
    forge/                   the forge's own project, part of the engine
    <slug>/                  a thought project
      .git/                  its own repository, any remote or none
      project.md
    lib-<name>/              a library
      .git/                  its own repository, its own visibility
      project.md
```

The pattern in `.gitignore` must be `projects/*`, not `projects/`.
With `projects/` the re-include of `projects/forge` fails silently.
The file layout of a project, file by file, is on
[Repository layout](../reference/repository-layout.md).

### How a project is recognised

The scripts ask git one question about a project's directory: is it
the top of a repository? They never look for a `.git` folder to
decide. The reason for asking git rather than looking for a folder is
not recorded.

- If git names the project's directory as the top, the project is
  under git. The git scripts commit, push, pull and report on it.
- If the top lies elsewhere, the project is outside git. This is the
  case for a directory inside someone else's repository.
- If there is no repository at all, the project is outside git too.

On a project outside git the forge writes its files to disk and runs
no git. The repository above it, if any, is asked nothing, not even
what it tracks, because that repository belongs to its owner. Such a
project comes into the forge by hand: a copy or a link into
`projects/`. From then on the forge knows it.

A project not under git is a property, not a defect. A project
without a repository, or with a repository and no origin, is a
legitimate shape, such as a sensitive project kept local. The second
keeps the history that renders and recipes rely on; the first does
not.

### Who creates the repository

`/new-project` and `/spinoff` create files only and never touch git.
Initialising a project's repository and adding its remote are your
own one-off act at creation. The way in is
`git -C projects/<slug> init -b main`, then a remote if you want one.
The scripts carry no URL and no identity. The commit identity is
git's: your own git configuration resolves it per host, and the forge
sets none.

### The project file

Every project has a project file, `project.md`, in its root. It is
written once, at the project's creation, by `/new-project` or by a
migration, and never by a working round. It declares three things:

- `project`: the slug.
- `kind`: `thought` or `library`, `thought` by default.
- `language`: the language of the chain's artefacts, as an ISO 639-1
  code.

The rules of each kind live in the engine. The project carries only
the marker. A project's optional `CLAUDE.md` stays polish and never
holds rules of its kind, because that would copy the engine into the
project.

A project without this file has the shape from before the migration.
Its one remedy is `/migrate`. Until it runs, nothing writes into the
project.

### Libraries

A library is a project of kind `library`, its slug prefixed `lib-`.
It has no chain (the versioned documents a thought project forges).
It holds a ledger (the table of the project's state, made by a
script), `sources/` and `research/` with their indexes, and a README
that catalogues what it holds. Its documents are maintained by an
owner who is also their author.

Another project cites a library document by path. That citation is a
dependency across repositories, taken knowingly:

- Only someone with both repositories can read it.
- It carries no version, because the library document is a moving
  target by design.
- The citing project's ledger lists it in its Dependencies table, so
  that the dependency is written down where state lives.

How to use one is on
[Share material through a library](../use/share-material-through-a-library.md).

### What the engine knows of a project

The engine does not record which projects exist. A project records no
engine version either: `/check` measures it against the current
conventions, as
[Upgrades and migration](../about/upgrades-and-migration.md) explains.

The engine is the one public place of an instance: a project's recipe
may send a file it makes, such as a video for the player page, into
the engine's `docs/videos/`, as
[The screenplay and its player](../about/the-screenplay-and-its-player.md)
describes. The file goes out alone. Its recipe, render and history
stay in the project.

### Where behaviour lives

How the forge behaves lives in the engine, never in the assistant's
private memory. Claude Code keeps a memory per directory outside the
repository. Whatever it learns there about how the forge should work
is written into `CLAUDE.md`, the commands or the templates and
removed from memory. Memory keeps only what is personal to one
principal. Instance facts go to `CLAUDE.local.md`.

## Why

The engine is public and contains nothing sensitive and no instance
facts. Users keep their projects wherever they choose. They are
themselves responsible for what those projects contain and where they
live, branded decks a project generates included. Because each
project is its own repository, it has its own visibility. Access is
therefore granted project by project.

The project file exists because the slug, the kind and the language
need a home in git. The ledger is made at read time and is not in
git. A library's repository is, at its creation, this file alone.

Behaviour lives in the engine so that every instance behaves the
same. A new user meets the same forge as the principal.

### Shapes rejected

- **Git submodules, subtree and worktrees.** They model a
  dependency, and the relation of the engine to its projects is not
  one.
- **The engine as a template repository, or copied into each
  project.** Every comparable project that does so ends in manifests,
  override layers and migrations.
- **A plugin as the only shape.** The reason is not recorded.
- **A `local/` directory for files kept off the repository.** It
  existed only to keep company material out of the repository. The
  gitignored `projects/*` now does that, and deck templates live in a
  library, named by path.

## A worked example

Someone starts a project with the placeholder slug `my-project`.

1. `/new-project my-project` creates `projects/my-project/` with its
   files and its `project.md`, which says `project: my-project`,
   `kind: thought` and `language: en`. No git has run.
2. The project is now outside git. The forge writes its files, and
   the engine's own repository does not see them, because
   `projects/*` is ignored.
3. The owner types `git -C projects/my-project init -b main` and adds
   a private remote. Git now names `projects/my-project` as the top of
   a repository, so the git scripts treat it as under git.
4. Later the owner makes a library, `lib-shared`, as its own
   repository, and a recipe of `my-project` names a template in it by
   path. The ledger of `my-project` lists that template under
   Dependencies.
5. The engine is upgraded by a fast-forward of its `main`. Neither
   project changes, and neither records which engine version it was
   made with.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
