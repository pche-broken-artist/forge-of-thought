---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 4a55f3c0384da122
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Persistence (git)
  - projects/forge/10-intent.md#POS.0760
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.0960
  - projects/forge/10-intent.md#POS.0970
  - projects/forge/10-intent.md#POS.1020
  - projects/forge/10-intent.md#POS.1030
  - projects/forge/10-intent.md#REJ.0140
  - projects/forge/10-intent.md#REJ.0150
  - projects/forge/40-solution-design.md#Persistence
---

# Projects and the engine

The engine of the forge is one public git repository, and every
project is a git repository of its own, nested under `projects/`,
which the engine does not know. This page says how the engine and the
projects are laid out as repositories, how they are told apart, what
kinds of project exist, where the facts of one installation live, and
why it is all so. It is for anyone who uses the forge, extends it or
evaluates it; the layout file by file is the page
[Repository layout](../reference/repository-layout.md), and every
term of the forge stands in one line in the
[Glossary](../reference/glossary.md).

## What it is

The engine is one git repository. It holds the universal core in its
root together with `projects/forge`, the forge's own project:

- `CLAUDE.md`: the rules, read by Claude
- `README.md`: for humans, a render (an output generated from the
  documents, never edited by hand)
- `templates/`: the canonical skeletons
- `scripts/`: the scripts, the only door to git
- `.claude/`: the commands, the contracts of the reviewers and of the
  documentation agents, the agents and the settings
- `projects/forge`: the forge run through its own process, part of
  the engine's repository

The engine is public, published under CC BY 4.0 with attribution. It
contains nothing sensitive and no fact of one installation. Its
`main` is the released line. Branches are voluntary and left to git.

Every other project is a repository of its own under `projects/`. The
engine's `.gitignore` ignores `projects/*` and re-includes
`projects/forge` with `!projects/forge`. The pattern must be
`projects/*`, not `projects/`. Otherwise the re-include fails
silently. The engine does not know the projects: the scripts
recognise a project through its `projects/<slug>/.git`, and the
engine carries no URL and no identity of any repository.

A project may stand in any of three shapes:

- no repository at all: a sensitive project kept local, with no
  history
- a repository with no origin: kept local, with the history that the
  renders and recipes rely on
- a repository with a remote of its own, of whatever visibility its
  owner chooses

A project "not under git" is a property, not a defect.

A project has a kind, declared as `kind: thought | library` in the
YAML header of its ledger (the project's single source of truth for
state), default `thought`:

- a thought project carries the chain, the versioned documents from
  the brief onward
- a library carries shared material and no chain: a ledger,
  `sources/` and `research/` with their indexes, `recipes/readme.md`
  and the README it renders; its slug starts with `lib-`

The rules of a kind live in the engine. The project carries only the
marker. Its optional `CLAUDE.md` stays polish and never holds kind
rules.

Another project cites a library document by path. The citation is a
dependency taken knowingly: the project's ledger carries a
Dependencies table with one row per document of another repository
it cites, registration only, with no version recorded. How a library
is used in practice is the page
[Share material through a library](../use/share-material-through-a-library.md).

The facts of one instance (one installation of the engine) live in
`CLAUDE.local.md` at the engine root, created from
`templates/CLAUDE.local.md` by `/setup` and kept out of the
repository: who the principal is, by role, and what language the
conversation runs in. The principal is the one whose thinking is
forged. `CLAUDE.md` names the principal and the conversation language
only as things that exist, never by value. The git identities (names,
e-mail addresses and hosts) live in the user's own git configuration
outside the engine; the engine sets no identity anywhere. The forge's
behaviour lives in the engine, never in the assistant's private
memory. A project records no engine version.

The shape, drawn from the owners:

```
<engine clone>                         origin: the engine's remote,
|-- CLAUDE.md  README.md  LICENSE      the upgrade channel
|-- templates/  scripts/  .claude/     (forge-pull fast-forwards main)
|-- CLAUDE.local.md                    gitignored: the instance facts
`-- projects/                          gitignored: projects/*
    |-- forge/                         re-included: !projects/forge,
    |                                  part of the engine's repository
    |-- <slug>/.git                    kind: thought
    |                                  origin: its own remote, or none
    `-- lib-<name>/.git                kind: library
                                       origin: its own remote, or none
```

## How it works

A project is born as files. `/new-project` and `/spinoff` create
files only and never touch git. The way into git is the user's
one-off act at creation: `git -C projects/<slug> init -b main`, then
a remote if wanted. An existing project is brought in by
`forge-clone.py`, whose door is `/import-project`.

The scripts in `scripts/` are the only door to git, reading state
included, with no exception. For Claude this is enforced by the deny
rules of `.claude/settings.json`. The scripts serve the engine and
every project repository alike, each described in full by its own
help header:

- `forge-save.py`: commits and pushes
- `forge-pull.py`: fast-forwards from the remotes
- `forge-status.py`: reports state without changing anything
- `forge-clone.py`: brings an existing project in
- `forge-branch.py`: switches or creates a branch

Merging is git's, by hand or by merge request. How the scripts
recognise a project is in one module they share
(`scripts/forge_repos.py`). The scripts carry no URL and no identity.
How many scripts there are is not a rule.

The commit identity is git's business. It is resolved per host by
the user's own configuration, in `includeIf` stanzas of
`~/.gitconfig`, which `/setup` offers to write. `/setup` also offers
the one global guard, `user.useConfigOnly = true` with no global
`user.name` or `user.email`. So that a repository on a host with no
stanza fails aloud instead of taking a default, a save commits
nothing until git resolves an identity for the repository.

The engine's remote is the upgrade channel. An upgrade is
`forge-pull` on the engine, a fast-forward of `main`. After the pull,
`/pull` shows the Action required lines of the releases crossed and
offers `/check light` and `/check project` on each project. The
checks say what the conventions changed, the release notes' Action
required lines say what to do, and Claude migrates on the user's
word. No migration tool exists, knowingly. Because a project records
no engine version, `/check` measures it against the current
conventions. That is the whole migration path of any instance. The
steps are the page [Upgrade the engine](../use/upgrade-the-engine.md).

A library's documents are maintained by an owner who is also their
author. Whether a change overwrites a document or lands as a new
version beside it is the owner's choice. A thought project's sources
are the opposite: inputs as of a date, immutable. Nothing is
redefined for a library: `/ingest` by file or link, or an upload and
a sweep, registration and index work as everywhere. A library has its
own repository and therefore its own visibility.

Whatever Claude Code learns in its per-directory memory about how the
forge should work is written into `CLAUDE.md`, the commands or the
templates and removed from memory. Such a thing is a working method,
a rule of a command or a convention. Memory keeps what is personal to
one principal, such as his idiom and his private choices. Instance
facts go to `CLAUDE.local.md`. Everything in `CLAUDE.local.md`
reaches every subagent (an isolated helper Claude launches, the
reviewers among them). So only what must be always on and is harmless
in a public report lives there, and instance facts are forbidden in a
reviewer's report.

## Why

The engine is split from the projects so that it can be published.
The engine contains nothing sensitive and no instance facts. Users
keep their projects wherever they choose and are themselves
responsible for what those contain and where they live, generated
decks carrying corporate branding included.

Access is per project. Because every project is a repository of its
own, each has its own remote and its own visibility, or none. A
sensitive project kept local is a legitimate shape, not a defect.

Work inside the instance is the same for every project. The scripts
serve the engine and every project repository alike, finding each by
its `.git`, and `/ingest`, registration and the index work in a
library as everywhere. A further reason for the nesting is not
recorded beyond the shapes rejected below.

The engine does not know the projects. Because `git init` and the
remote are the user's one-off act, the engine carries no URL and no
identity, and a project starting "not under git" is a property.

The rules of a kind live in the engine and not in the project.
Because a project's `CLAUDE.md` holding kind rules would copy the
engine into the project.

A library citation carries no version. Because a library document is
maintained by its owner and cited as a moving target by design. The
citation is written down in the ledger's Dependencies table. Because
knowingly means written down where state lives, not discovered when a
render loses its template. A check is added when it hurts.

Instance facts live in `CLAUDE.local.md` and not in the engine.
Because the engine is public, and because everything in
`CLAUDE.local.md` reaches every subagent and may be quoted into a
public report. The git identities live in the user's own
configuration and not in the forge. Because an identity kept by the
forge duplicates what the user's own configuration already resolves,
and every repository would carry the same identity twice. The case of
one host serving two identities is accepted as a risk the user
resolves by hand.

The forge's behaviour lives in the engine and not in the assistant's
memory. So that every instance of the forge behaves the same, and a
new user meets the same forge as the principal.

A project records no engine version. Because `/check` measures the
project against the current conventions, and the release notes say
what to do, no migration tool is needed. The shapes that record a
version end in migrations, as the rejected shapes below say.

The gitignore pattern is `projects/*` and not `projects/`. Because
with `projects/` the re-include of `projects/forge` fails silently.

### The shapes rejected

- git submodules, subtree and worktrees: they model a dependency,
  which the relation between the engine and a project is not
- the engine as a template repository, and copying the engine into
  the projects: every comparable project that does so ends in
  manifests, override layers and migrations
- a plugin as the only shape, for now: the reason is not recorded
- a `local/` directory as the home of user-local files: it existed
  only to keep private material out of the repository, which the
  gitignored `projects/*` now does; deck templates live in a library
  project and are named by path

## A worked example

One instance, generic. The engine is cloned once; its `main` tracks
the engine's remote. `/setup` creates `CLAUDE.local.md` from the
template, naming the principal by role and the conversation language,
and offers the `includeIf` stanzas and the global guard.

The principal starts a thought project: `/new-project my-project`
creates the files under `projects/my-project/`, and nothing else. He
runs `git -C projects/my-project init -b main` and adds a private
remote. From then on `/save my-project` commits and pushes through
`forge-save.py`, because the scripts find the project by
`projects/my-project/.git`. The engine's own repository sees none of
it: `projects/*` is ignored.

Another team keeps a library, `lib-shared`, with a deck template
among its sources. The principal brings it in with `/import-project`
and the library's git URL, which clones it to `projects/lib-shared/`.
A deck recipe of `my-project` names
`projects/lib-shared/sources/deck-template.potx`, and the ledger of
`my-project` carries one row for it in its Dependencies table, with
no version. Only someone with both repositories can follow the
citation; the assignment of `my-project` is self-contained anyway.

A third project, `scratch`, holds sensitive thinking and is never
initialised. The scripts pass it by, `/save` does not list it, and
the forge says nothing of it as a defect.

An upgrade arrives: `/pull` on the engine fast-forwards `main`,
prints the Action required lines of the releases crossed and offers
`/check light` and `/check project my-project`. The checks say where
`my-project` no longer meets the conventions. Claude migrates it on
the principal's word, one step at a time, and `/save my-project`
records the result in the project's own repository. The engine's
repository is unchanged by any of it.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrade the engine](../use/upgrade-the-engine.md): the upgrade and the migration path.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
