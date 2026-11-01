---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 987309d04ac5e166
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

The engine is the one public repository of Forge of Thought: the
rules, commands, templates and scripts, together with the forge's
own project. Every other project is a git repository of its own,
and the engine does not know about it. This page explains how the
two fit together, how a project is recognised and why the line is
drawn there. It is written for anyone who uses the forge, extends
it or weighs it up.

## What it is

The engine is one git repository with a remote of its own. Its
`main` branch is the released line. It holds two things:

- the universal core in its root: `CLAUDE.md` for Claude,
  `README.md` for humans, `templates/`, `scripts/` and `.claude/`;
- `projects/forge`, the forge's own project, where the forge is run
  through its own process.

Every other project lives under `projects/<slug>/`. The engine's
git ignores that directory, so the projects never enter the engine's
history. Each project is a repository of its own where its owner
wants one. It can have any remote and any visibility, or no remote
at all, or no repository at all. A project is a piece of work the
forge carries: a thought project (a chain of documents around one
idea) or a library (shared material). The principal (the person
whose thinking is being forged) decides where each project lives
and what it contains.

```
forge-of-thought/            the engine: one public repository
├── CLAUDE.md  README.md
├── templates/  scripts/  .claude/
├── docs/                    the documentation, and docs/videos/
└── projects/                ignored by the engine's git, except forge
    ├── forge/               the forge's own project, part of the engine
    ├── <slug>/              a thought project: a repository of its own
    │   ├── .git/
    │   └── project.md
    └── lib-<name>/          a library: a repository of its own
        ├── .git/
        └── project.md
```

The engine's `.gitignore` carries the pattern `projects/*` and
re-includes the forge's own project with `!projects/forge`. The
pattern must be `projects/*`, not `projects/`. With `projects/` the
re-include fails without any message.

## How it works

### How a project is recognised

The scripts ask git one question about a project's directory: is it
the top of a repository? Where git says yes, the project is under
git. The scripts never look for a `.git` folder to decide this.

Anything else is a project outside git. That covers two cases:

- a project with no repository at all;
- a project whose directory sits inside someone else's repository,
  so that the top of the repository lies higher up.

For a project outside git, the forge writes its files to disk and
runs no git on it. The repository above it belongs to its owner.
The forge asks it nothing, not even what it tracks. The one
exception to the rule is the forge's own project, whose repository
is the engine.

A project outside git comes in by hand: you copy it, or link it,
into `projects/`. From then on the forge knows it.

### How a project comes into git

Creating a project's repository and adding its remote are the
user's one-off act at creation. `/new-project` creates files only
and never touches git. The way in is:

```
git -C projects/<slug> init -b main
```

and then a remote, if one is wanted. A project that is not under git
has a property, not a defect. A project with a repository and no
origin is also a legitimate shape.

The scripts in `scripts/` are the door to any write of git; reading
git directly is open. They carry no remote address and no identity.
The commit identity is resolved by the user's own git configuration
on each host.

### The project file

Every project has a project file, `project.md`, in its root. It is
written once, when the project is created, by `/new-project` or by a
migration, and never by a round of work. It declares three things:

| Field | What it says |
|---|---|
| `project` | the project's slug |
| `kind` | `thought` or `library`; `thought` is the default |
| `language` | the language of the chain's artefacts, as an ISO 639-1 code |

The rules of each kind live in the engine. The project carries only
the marker. A project's optional `CLAUDE.md` is polish and never
holds rules of its kind, because that would copy the engine into the
project. A project without a project file has the shape from before
a migration, and `/migrate` is the one remedy.

### Libraries

A library is a project of kind `library`, its slug prefixed `lib-`.
It has no chain: a ledger (the state report the forge builds from
the documents), `sources/` and `research/` with their indexes, and a
README rendered from `recipes/readme.md`. It is its own repository,
so it has its own visibility.

A library's documents are maintained by their owner. Another project
cites a library document by its path. That citation is a dependency
across repositories, taken knowingly:

- only someone who has both repositories can read it;
- it carries no version, because the document is a moving target by
  design;
- the citing project's ledger lists it in its Dependencies table.

How to use one is on
[Share material through a library](../use/share-material-through-a-library.md).

### Instance facts and behaviour

An instance is one installation of the forge. Who the principal is,
the language the conversation runs in and the handle the principal
signs records with are facts of the instance. They live in
`CLAUDE.local.md` at the engine root, which is kept out of the
repository. The engine itself carries no instance facts.

How the forge behaves lives in the engine, never in the assistant's
private memory. A working method or a rule that Claude learns in its
memory is written into `CLAUDE.md`, the commands or the templates,
and removed from memory. Memory keeps only what is personal to one
principal.

### Versions and public files

A project records no engine version: it is measured against the
current conventions, as
[Upgrades and migration](../about/upgrades-and-migration.md) explains.

The engine is the one public place of an instance, so what a project
shows in public goes out as a file into the engine's `docs/videos/`,
as [The screenplay and its player](../about/the-screenplay-and-its-player.md)
describes.

## Why

**Publication with nothing sensitive.** The engine is public and
contains nothing sensitive and no instance facts. Users keep their
projects wherever they choose. They are responsible for what those
projects contain and where they live, generated decks with corporate
branding included.

**Access per project.** Because each project is its own repository,
each has whatever remote and visibility its owner gives it. A
sensitive project can be kept local. A repository with no origin
still keeps the history that renders and recipes rely on. A project
with no repository does not.

**Work inside the engine.** The projects lie under the engine's
`projects/`, where the commands reach them, while the engine's git
ignores them. The reason this layout was chosen for seamless work is
not recorded beyond the rejected shapes below.

**One question to git.** A project placed inside another repository
has no `.git` of its own but still lies in a repository. Asking git
for the top of the repository tells the two apart. The repository
above is its owner's, so the forge leaves it alone.

**The project file.** The slug, the kind and the language need a
home that is in git. The ledger is made at read time and is not in
git. A library's repository is, at its creation, this file alone.

**No instance facts in the engine.** `CLAUDE.local.md` reaches every
subagent (a separate Claude run with its own context), the reviewers
included. So only what must always be present and is harmless in a
public report lives there. Git identities such as names, e-mail
addresses and hosts live in the user's own git configuration
outside the engine.

**Behaviour in the engine.** Every instance of the forge then
behaves the same, and a new user meets the same forge as the
principal.

**Library citations without a version.** A library document is
maintained by its owner and is a moving target by design. Listing it
in the ledger makes the dependency written down where state lives,
not discovered when a render loses its template.

### Shapes that were rejected

- **Git submodules, subtree and worktrees.** They model a
  dependency, and the relation between the engine and a project is
  not one.
- **The engine as a template repository, or the engine copied into
  each project.** Every comparable project that does so ends in
  manifests, override layers and migrations.
- **A plugin as the only shape, now.** The reason is not recorded.
- **A `local/` folder for user-local files.** It existed only to
  keep sensitive material out of the repository. The ignored
  `projects/*` now does that, and deck templates live in a library,
  named by path.

## A worked example

A principal works on a thought project `my-project` and keeps shared
deck templates in a library `lib-shared`.

```
forge-of-thought/
└── projects/
    ├── forge/
    ├── my-project/          git: top of its own repository, private remote
    │   └── project.md       project: my-project, kind: thought, language: en
    └── lib-shared/          git: top of its own repository, no remote
        └── project.md       project: lib-shared, kind: library, language: en
```

The engine's git sees neither directory. The scripts ask git about
each one and find each to be the top of its own repository, so
saving `my-project` commits and pushes to its own remote. A recipe
in `my-project` names a deck template in `lib-shared` by path, and
the project's ledger lists that template as a dependency. A third
directory copied into `projects/` from inside another repository
would be a project outside git: the forge would write its files and
run no git on it.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
