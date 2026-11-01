---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: b94c94f611ef1bff
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

The engine is one public git repository, and every project worked in
it is a git repository of its own that the engine does not know.
This page explains how the two are arranged, how the forge tells a
project under git from a project outside it, what a project declares
about itself, where the facts of one installation live, and why the
arrangement is as it is. It is written for the user who keeps
projects in the forge, for the extender who changes the engine, and
for the evaluator who wants to know what is public and what is not.

## What it is

The engine is the universal core together with the forge's own
project. The core is the root of the repository: `CLAUDE.md` for
Claude, `README.md` for humans, `templates/`, `scripts/` and
`.claude/`. The forge's own project is `projects/forge`, the engine
run through its own process. The engine's repository has a remote of
its own. Its `main` is the released line. Branches are voluntary and
left to git.

Every other project lives under `projects/`, which the engine's
`.gitignore` leaves out. The pattern is `projects/*` with
`projects/forge` re-included (`!projects/forge`). The pattern must be
`projects/*` and not `projects/`, because with `projects/` the
re-include fails silently. The engine's `.gitignore` also carries
`projects/forge/ledger.md`, since the ledger (the single source of
truth for a project's state, made at read time) is never in git.

A project is a repository of its own where its owner wants one, with
whatever remote and visibility the owner gives it, or with none. The
engine does not know the projects: it carries no URL and no identity
of any of them. Initialising a project's repository and adding its
remote are the user's one-off act at creation. `/new-project` and
`/spinoff` create files only and never touch git. A project that
starts "not under git" has a property, not a defect.

Three shapes of a project are legitimate:

- a repository with an origin: the usual shape, kept wherever the
  owner chooses;
- a repository with no origin: it keeps the history the renders and
  recipes rely on, and stays on one machine;
- no repository at all: a sensitive project kept local; it keeps no
  history.

An existing project is brought in through `/import-project`, the door
to `scripts/forge-clone.py`.

## How it works

### How the forge recognises a project under git

The scripts ask git one question: does git name the project's
directory as the top of a repository? That is the only test. The
scripts never look for a `.git` entry. A project whose top lies
elsewhere, such as a directory inside another's repository, or that
has no top at all, is for the forge a project outside git. On such a
project the forge writes files to disk and runs no git. The
repository above it belongs to its owner and is asked nothing, not
even what it tracks. A project outside git comes in by hand, as a
copy or a link into `projects/`, and the forge knows it from then on.

The scripts in `scripts/` are the door to a write of git. Claude
commits, pushes, pulls, merges, branches and tags only through a
script. Reading git directly is open to it, since reading changes
nothing. The one exception is the few commands that finish the step
of a conflict, which run on the principal's yes. The principal is the
person whose thinking is being forged. The same scripts serve the
engine and every project repository alike; how many scripts there
are is whatever the door needs, never a rule. The commit identity is
git's business: it is resolved per host by the user's own
configuration, and the forge sets none. `/setup` offers to write
that configuration and one global guard, so that a commit in a
repository on a host with no identity fails aloud instead of taking a
default.

### The project file

Every project has a project file, `project.md`, written once at its
creation by `/new-project` or by the migration, never by a working
round. It is merged as text. It declares three things:

- `project`: the slug of the project;
- `kind`: `thought` or `library`, `thought` the default;
- `language`: the language of the chain's artefacts, as an ISO
  639-1 code, English when absent.

The file is read wherever the kind and the language of a project are
needed. The rules of a kind live in the engine; the project carries
only the marker. A project's optional `CLAUDE.md` is polish and never
holds kind rules, because that would copy the engine into the
project. A project without a project file is of the shape before the
migration; the one remedy is `/migrate`, and until it has run nothing
writes into the project.

### Thought projects and libraries

A project of kind `thought` carries the chain: a brief, an intent and
whatever layers the project needs below the intent, with its
threads, records, sources, research, recipes, renders and reviews.
The [Repository layout](../reference/repository-layout.md) lists it
file by file.

A project of kind `library` carries no chain. It is a collection of
documents used across projects: a ledger, `sources/` and `research/`
with their indexes, `recipes/readme.md` and the README it renders.
Its slug carries the prefix `lib-`. It is a repository of its own and
therefore has a visibility of its own. Nothing is redefined for it:
`/ingest` registers and indexes as everywhere. A library's documents
are maintained by an owner who is also their author; whether a change
overwrites a document or puts a new version beside it is the owner's
choice. A thought project's sources, by contrast, are inputs as of a
date and immutable.

Another project cites a library document by its path. The citation
is a cross-repository dependency taken knowingly: only someone with
both repositories can read it, the assignment is self-contained
anyway, and the citation carries no version, because the document is
a moving target by design. The citing project registers it in the
Dependencies table of its ledger, one row per document of another
repository, registration only. What the document is for lives where
it is used. How a library is used from day to day is on
[Share material through a library](../use/share-material-through-a-library.md).

### Instance facts and the engine's behaviour

The engine carries no instance facts. An instance is one installation
of the forge. Who the principal is, by role, and what language the
conversation runs in live in `CLAUDE.local.md`, a file of the
instance kept out of the repository. Everything in that file reaches
every subagent (an isolated run of Claude that sees nothing of the
conversation), the reviewers included. So only what must be always
on and is harmless in a public report lives there. Git identities,
that is names, e-mail addresses and hosts, live in the user's own git
configuration outside the engine. Instance facts are forbidden in a
reviewer's report. `CLAUDE.md` names the principal and the
conversation language only as things that exist, never by value.

The forge's behaviour lives in the engine, never in the assistant's
memory. Claude keeps a per-directory memory outside the repository.
Whatever it learns there about how the forge should work, a working
method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory is left with what is personal to one principal: his idiom and
his private choices.

### What a project does not record, and where its public files go

A project records no engine version; how a project follows the engine
across releases is on
[Upgrades and migration](upgrades-and-migration.md).

The engine is the one public place of an instance: a project that
shows a file in public sends it as a file into the engine's
`docs/videos/`, while its recipe, render, provenance and history stay
in the project, as [The screenplay and its player](the-screenplay-and-its-player.md)
describes.

## Why

The forge is split into a public engine and user projects so that the
engine can be published. The engine contains nothing sensitive and no
instance facts. Users keep their projects wherever they choose and
are themselves responsible for what those projects contain and where
they live, generated decks carrying corporate branding included.

Each project is a repository of its own so that access is given per
project: a repository of its own has a visibility of its own, and a
sensitive project may be kept local with no remote or no repository
at all. The projects sit inside the engine's tree under one
gitignored directory so that one set of scripts serves the engine and
every project alike.

The forge asks git for the top of a repository, and never looks for a
`.git` entry, so that it runs git only on a repository that is the
project's own. A directory inside someone else's repository is that
owner's; the forge writes its files there and asks the repository
above nothing.

The project file exists because its three facts would otherwise have
no home: the ledger, where they used to be read, is no longer in git,
and a library's repository is at its creation this file alone.

Instance facts live outside the repository because the engine is
public and because everything the instance file holds reaches every
subagent and may be quoted into a public report. The forge's
behaviour lives in the engine and not in the assistant's memory so
that every instance of the forge behaves the same and a new user
meets the same forge as the principal.

### The shapes rejected

Several shapes of the relation between the engine and the projects
were considered and dropped:

- git submodules, subtree and worktrees: they model a dependency,
  which this relation is not;
- the engine as a template repository, and copying the engine into
  each project: every comparable project that does so ends in
  manifests, override layers and migrations;
- a plugin as the only shape: dropped for now; the reason is not
  recorded;
- a `local/` directory as the home of user-local files: it existed
  only to keep company material out of the repository, which the
  gitignored `projects/*` now does; deck templates live in a library
  project and are named by path.

## A worked example

One instance of the forge, drawn as a tree. Every name below is a
placeholder.

```
forge-of-thought/              the engine: one public repository
  CLAUDE.md  README.md         the universal core
  templates/  scripts/  .claude/
  .gitignore                   projects/*  and  !projects/forge
  projects/
    forge/                     the engine's own project, in the
                               engine's repository
    example-topic/             a thought project: a repository of
      .git/                    its own, with a private remote
      project.md               project: example-topic
                               kind: thought
                               language: en
      00-brief.md  10-intent.md  ...
    lib-example/               a library: a repository of its own
      .git/                    with a visibility of its own
      project.md               kind: library
      sources/  recipes/readme.md  README.md
    copied-topic/              a project outside git: copied in by
      project.md  ...          hand, no .git, no git run on it
```

The engine's repository tracks the core and `projects/forge` and
nothing else under `projects/`. `example-topic` cites a deck template
of `lib-example` by its path in a recipe and registers that path in
the Dependencies table of its ledger, with no version. On
`copied-topic` the forge writes its files and runs no git, since git
names no top for it. A reviewer run in any of these projects reads
the instance's `CLAUDE.local.md` with everything else, and its report
names no person, host or address from it.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
