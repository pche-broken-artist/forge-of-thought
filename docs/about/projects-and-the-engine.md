---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 4913fbe482998510
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

The engine is the one public repository of Forge of Thought, and
every other project is a git repository of its own that the engine
does not know. This page explains how the two are laid out side by
side, how the forge tells whether a project is under git, what a
project declares about itself, and why the relation has this shape
and not another. It is for anyone who uses the forge, extends it or
weighs it.

## What it is

The engine is the core of the forge together with its own project.
The core is the root of the repository: `CLAUDE.md` for Claude,
`README.md` for humans, `templates/`, `scripts/` and `.claude/`. Its
own project is `projects/forge`, the forge run through its own
process. The engine is a clone of one public repository.

Every other project lives under `projects/`, and that directory is
ignored by the engine's git. Each such project is a repository of its
own where its owner wants one. It has whatever remote and visibility
its owner gives it, or no remote, or no repository at all.

A project has a kind:

- `thought`: a project with the chain of versioned documents, from
  the brief to the intent and the layers below it.
- `library`: shared material used across projects, with no chain.

The principal is whoever's thinking is being forged. Who that is,
and the other facts of one installation (an instance), live outside
the engine.

## How it works

### The layout

```
forge-of-thought/            the engine: one public repository
├── CLAUDE.md                the core
├── README.md
├── templates/
├── scripts/
├── .claude/
├── .gitignore               ignores projects/*, re-includes projects/forge
└── projects/
    ├── forge/               the engine's own project, inside the engine's repository
    ├── <slug>/              a thought project: a repository of its own
    │   ├── .git/
    │   ├── project.md
    │   └── ...
    └── lib-<name>/          a library: a repository of its own
        ├── .git/
        ├── project.md
        └── ...
```

The engine's `.gitignore` holds the pattern `projects/*` with
`!projects/forge` beside it. The pattern must be `projects/*` and not
`projects/`. With `projects/` the re-include of `projects/forge`
fails silently. The layout file by file is on
[Repository layout](../reference/repository-layout.md).

### How a project is recognised

The scripts ask git one question of a project: is the project's
directory the top of a repository? They never look for a `.git`
folder.

- Where git names the project's directory as the top, the project is
  under git, and the git scripts serve it.
- Where the top lies elsewhere, or there is none, the project is a
  project outside git. This holds for a folder inside someone else's
  repository as much as for a folder with no repository.

On a project outside git the forge writes the project's files to disk
and runs no git. The repository above such a project is its owner's.
The forge asks it nothing, not even what it tracks. A project outside
git comes in by hand: a copy or a link into `projects/`. From then on
the forge knows it.

The reason for asking git for the top, rather than looking for a
`.git`, is not recorded.

### The engine does not know the projects

Creating a project creates files only. `/new-project` and `/spinoff`
never touch git. Initialising a project's repository and adding its
remote are the user's one-off act:

```
git -C projects/<slug> init -b main
```

A remote follows if one is wanted. A project that starts "not under
git" is in a legitimate shape, not a defect. A project with a
repository and no origin keeps the history that renders and recipes
rely on. A project with no repository does not keep it.

### The project file

Every project has a project file, `project.md`, at its root. It is
written once, at the creation of the project, by `/new-project` or by
a migration, and never by a round of work. It declares three things:

- `project`: the slug of the project.
- `kind`: `thought` or `library`, `thought` by default.
- `language`: the language of the chain's artefacts, as an ISO 639-1
  code.

The rules of a kind live in the engine. The project carries only the
marker. A project's optional `CLAUDE.md` stays polish for that
project and never holds rules of a kind.

A project without this file has the shape from before the migration.
The one remedy is `/migrate`.

### A library

A library is a project of kind `library`. Its slug starts with
`lib-`. It holds no chain. It holds:

- a [ledger](../reference/glossary.md) (the state of the project,
  made from its documents when it is read);
- `sources/` and `research/`, each with its index;
- `recipes/readme.md` and the README it renders, which is the
  catalogue of what the library holds.

A library's documents are maintained by their owner, who is also
their author. The owner chooses whether to overwrite a document or to
put a new version beside it. Another project cites a library document
by its path. That citation is a dependency across repositories, taken
knowingly:

- Only someone who has both repositories can read the cited document.
- The citation carries no version, because the document is a moving
  target by design.
- The citing project registers it in the Dependencies table of its
  ledger, one row per document of another repository it cites.

How to use a library is on
[Share material through a library](../use/share-material-through-a-library.md).

### Instance facts and behaviour

Facts of one instance live in `CLAUDE.local.md` at the engine root.
That file is kept out of the repository. It names who the principal
is by role, the conversation language and the handle the principal
signs records with. Everything in it reaches every subagent (an
isolated agent that Claude launches for one job, such as a reviewer).
So only what must be always on and is harmless in a public report
lives there. The commit identity is not one of those facts: it lives
in the user's own git configuration, outside the engine.

The forge's behaviour lives in the engine: in `CLAUDE.md`, the
commands and the templates. It never lives in the assistant's private
memory. Whatever Claude learns there about how the forge should work
is written into the engine and removed from memory. Memory keeps only
what is personal to one principal.

### Versions and public files

A project records no engine version; how a project follows the engine
is on [Upgrades and migration](upgrades-and-migration.md).

The engine is the one public place of an instance, and a file a
project shows in public goes out into the engine, as
[The screenplay and its player](the-screenplay-and-its-player.md)
explains.

## Why

**Publication with nothing sensitive.** The engine is public. It
contains nothing sensitive and no instance facts. Users keep their
projects wherever they choose. They are themselves responsible for
what those projects contain and where they live, generated decks
included.

**Access per project.** Because each project is a repository of its
own, each has its own remote and its own visibility. A library has
its own repository for the same reason, and so its own visibility.

**Working inside one tree.** The reason the projects sit inside the
engine's tree, rather than anywhere else on disk, is not recorded.

**Why the project file exists.** The ledger is made when it is read
and is not kept in git. Without a file of their own, a project's
slug, kind and language would have no home. A library's repository,
at its creation, is the project file alone.

**Why the kind is only a marker.** Rules of a kind written into a
project would copy the engine into the project.

**Why only harmless facts are instance facts.** Every subagent
receives `CLAUDE.local.md`, the reviewers included. A report is a
public file or may be quoted into one.

**Why behaviour stays out of memory.** Every instance of the forge
then behaves the same, and a new user meets the same forge as the
principal.

**Why a library's citation is registered.** "Knowingly" means written
down where state lives. A dependency is then not discovered only when
a render loses its template.

**Why the forge asks nothing of a repository above a project.** That
repository belongs to its owner.

### The shapes rejected

- Git submodules, subtree and worktrees. They model a dependency, and
  the relation between the engine and a project is not one.
- The engine as a template repository, and the engine copied into
  each project. Every comparable project that does so ends in
  manifests, override layers and migrations.
- A plugin as the only shape, for now.
- A `local/` folder as the home of files kept to one user. It existed
  only to keep material that must not be published out of the
  repository. The ignored `projects/*` does that now, and shared
  material such as deck templates lives in a library, named by path.

## A worked example

A user creates a thought project and a library. The slugs are
placeholders.

1. `/new-project example-project` writes the project's files under
   `projects/example-project/`, among them `project.md` with
   `kind: thought` and `language: en`. It runs no git. The project is
   outside git, and the forge runs no git on it.
2. The user runs `git -C projects/example-project init -b main` and
   adds a private remote. Git now names `projects/example-project/`
   as the top of a repository, so the git scripts serve it. The
   engine's own repository does not see it, because `projects/*` is
   ignored.
3. `/new-project lib-example` creates a library whose `project.md`
   says `kind: library`. The user gives it a repository and a remote
   of its own, with a visibility of its own.
4. A recipe of `example-project` names a deck template in
   `lib-example` by its path. The ledger of `example-project` shows it
   as one row of its Dependencies table, with no version.
5. Another folder lies inside an unrelated repository, and the user
   links it into `projects/`. Git names the unrelated repository's
   root as the top, not the folder. The forge writes that project's
   files and runs no git on it.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
