---
generated: 2026-10-09
made: derived
inputs-hash: ff8f3894a08d6b1f
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About projects and the engine

This page explains how the forge is split into one public engine and
any number of projects, each a repository of its own, and why it is
cut that way. It is for anyone who uses the forge, extends it or
wants to judge it, and it was put together from `CLAUDE.md`, the
forge's own intent (`projects/forge/10-intent.md`) and its solution
design (`projects/forge/40-solution-design.md`).

## Two things, not one

The **engine** is one git repository: the universal core in its root
(`CLAUDE.md` for the agent, `README.md` for humans, `templates/`,
`scripts/`, `.claude/`) together with `projects/forge`, the forge's
own project, which is the forge run through its own process. The
engine is public. It contains nothing sensitive and no facts about
the instance it runs on.

A **project** is everything else under `projects/`. Every project is
a git repository of its own, nested inside the engine's working tree
but unknown to the engine's repository: `projects/*` is gitignored,
with `projects/forge` re-included. The engine does not know the
projects. Creating a project's repository and adding its remote is
the user's one-off act at creation; `/new-project` and `/spinoff`
create files only and never touch git.

The scripts in `scripts/` recognise a project by one thing: the
presence of `projects/<slug>/.git`. How they recognise it is written
once, in `scripts/forge_repos.py`, which the git scripts share.

## Why the split

Three reasons stand behind the shape.

- **Publication.** The engine is published, so it must carry nothing
  that belongs to one user: no company, no address, no identity, no
  content of anyone's projects. Keeping the projects in repositories
  of their own keeps that material out of the public repository by
  construction, not by discipline.
- **Access per project.** Each project has its own repository and
  therefore its own visibility. One project may be public, another
  private, a third kept on no remote at all; the engine's visibility
  decides nothing about them.
- **Seamless work inside.** The projects sit under `projects/` where
  the commands and scripts expect them, so working on a project
  feels like working in one tree, while git sees as many
  repositories as there are projects.

Users keep their projects wherever they choose and are themselves
responsible for what those contain and where they live, generated
decks carrying corporate branding included.

## A project's repository is its own business

A project may have any remote and any visibility, or none. A project
with no repository at all, and a project with a repository and no
remote, are both legitimate shapes: the first is a sensitive project
kept local, the second keeps the history that renders and recipes
rely on while sharing nothing. A project "not under git" is a
property, not a defect. The way into git for a project is
`git -C projects/<slug> init -b main`, then a remote if wanted.

The scripts carry no URL and no identity. The commit identity is
git's business, resolved per host by the user's own git
configuration; the forge sets none. `/setup` offers to write that
configuration and a global guard so that a commit on a host with no
identity fails aloud instead of silently taking a default.

### The gitignore pattern

The engine's `.gitignore` ignores `projects/*` and re-includes
`projects/forge` with `!projects/forge`. The pattern must be
`projects/*`, not `projects/`: with `projects/` the re-include fails
silently, and the forge's own project would drop out of the engine.

## A project has a kind

A project declares its kind in the YAML header of its ledger,
`kind: thought | library`, default `thought`. The rules of a kind
live in the engine; the project carries only the marker. A project's
optional `CLAUDE.md` is polish for that project and never carries
kind rules, because that would copy the engine into the project.

- A **thought** project carries the chain: a brief, an intent and
  whatever layers it takes below the intent, with its records,
  ledger, sources, research, recipes and renders.
- A **library** (`lib-<name>`) is shared material with no chain:
  a ledger, `sources/` and `research/` with their indexes, and a
  README rendered from `recipes/readme.md` as the catalogue of what
  it holds. Its documents are maintained by an owner who is also
  their author; whether a new version overwrites the old or stands
  beside it is the owner's choice.

Another project cites a library document by path. That citation is a
cross-repository dependency taken knowingly: only someone with both
repositories can read it, and no version is recorded, because a
library document is maintained by its owner and cited as a moving
target by design. Knowingly means written down where state lives:
the citing project's ledger carries a Dependencies table with one
row per document of another repository it relies on, registration
only, so that the dependency is known before a render loses its
template rather than discovered when it does.

## Where instance facts live

Who the principal is and what language the conversation runs in are
facts of one instance, not properties of the forge. They live in
`CLAUDE.local.md` at the engine root, gitignored, created from
`templates/CLAUDE.local.md` and filled by `/setup` on a new machine.
`CLAUDE.md` names the principal and the conversation language only
as things that exist, never by value.

Only what must be always on and is harmless in a public report
belongs there, because everything in `CLAUDE.local.md` reaches every
subagent, the isolated reviewers included, and a reviewer's report
is a public file or may be quoted into one. Git identities, names,
addresses and hosts live in the user's own git configuration outside
the engine, and instance facts are forbidden in a reviewer's report.

The forge's behaviour lives in the engine, never in the assistant's
private memory. Whatever the assistant learns about how the forge
should work, a working method, a rule of a command, a convention, is
written into `CLAUDE.md`, the commands or the templates and removed
from memory, so that every instance of the forge behaves the same and
a new user meets the same forge as its author. Memory is left with
what is personal to one principal.

## Upgrading the engine, and what a project does not record

The upgrade is `forge-pull` on the engine: a fast-forward of `main`.
A project records no engine version. After an upgrade, the checks
(`/check light` on the engine, `/check project` on each project)
measure the project against the current conventions and say what
has changed; the release notes' Action required lines say what to
do, and the assistant migrates on the user's word. That is the whole
migration path of any instance. No migration tool exists, knowingly.

## The shapes that were rejected

The relation between the engine and the projects could have taken
other shapes. Each was considered and dropped.

- **Git submodules, subtree and worktrees** model a dependency, and
  this relation is not one.
- **The engine as a template repository**, or **copying the engine
  into each project**: every comparable project that does so ends
  in manifests, override layers and migrations.
- **A plugin as the only shape**, for now.
- **A separate `local/` directory for user-local files**: it existed
  only to keep private material out of the repository, which the
  gitignored `projects/*` now does; shared assets such as deck
  templates live in a library project and are named by path.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrade the engine](../use/upgrade-the-engine.md): the upgrade and the migration path.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
