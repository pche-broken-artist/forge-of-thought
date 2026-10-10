---
generated: 2026-10-10
made: derived
inputs-hash: 767384dc3958239d
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About projects and the engine

This page explains how the engine and the projects relate: what is
one repository and what is many, why the split is drawn where it is,
what a project's kind means, where the facts of one installation live
and how a project keeps up with the engine. It is for anyone who uses
the forge, extends it or evaluates it. It was put together from
`CLAUDE.md` (Repository layout and Persistence), the forge's intent
and its solution design.

## One engine, many projects

The engine is one git repository. It holds the universal core in its
root (`CLAUDE.md` for the agent, `README.md` for humans, `templates/`,
`scripts/`, `.claude/`) together with `projects/forge`, the system's
own project: the forge run through its own process. `main` is the
released line; branches are voluntary and left to git.

Every other project lives under `projects/` as a git repository of
its own, nested inside the engine's working tree. The engine's
`.gitignore` excludes `projects/*` and re-includes `projects/forge`
with `!projects/forge`. The pattern must be `projects/*`, not
`projects/`: with the directory itself ignored, the re-include fails
silently. The scripts recognise a project by `projects/<slug>/.git`;
how they do so lives in `scripts/forge_repos.py`, which the git
scripts share.

The engine does not know the projects. Initialising a project's
repository and adding its remote are the user's one-off act at
creation: `/new-project` and `/spinoff` create files only and never
touch git. The way in is `git -C projects/<slug> init -b main`, then
a remote if wanted. A project may therefore have any remote and any
visibility, or none. A project "not under git" is a property, not a
defect; a project with a repository and no origin is a legitimate
shape too, say a sensitive project kept local. The difference is
that a repository keeps the history the renders and recipes rely on,
and a bare directory does not.

The scripts in `scripts/` are the only door to git, reading state
included. The same scripts serve the engine and every project
repository: `forge-save.py` commits and pushes, `forge-pull.py`
fast-forwards from the remotes, `forge-status.py` reports state
without changing anything, `forge-clone.py` brings an existing
project in (`/import-project` is its door) and `forge-branch.py`
switches or creates a branch. Merging is git's, by hand or by merge
request. The scripts carry no URL and no identity.

## Why the split is drawn this way

The forge is split into a public engine and user projects in
repositories of their own for three reasons.

- **Publication.** The engine, the core together with
  `projects/forge`, is public under the licence CC BY 4.0 and
  contains nothing sensitive and no instance facts. Users keep their
  projects wherever they choose and are themselves responsible for
  what those contain and where they live, generated decks carrying
  corporate branding included.
- **Access per project.** Because each project is its own
  repository, each has its own visibility, and access can be granted
  project by project.
- **Work in one place.** The projects sit inside the engine's working
  tree, so the commands and the scripts reach the engine and every
  project alike, with no copy of the engine and no manifest to keep
  in step.

## A project has a kind

A project declares its kind in the YAML header of its ledger,
`kind: thought | library`, default `thought`. The rules of a kind live
in the engine; the project carries only the marker. A project's
optional `CLAUDE.md` stays polish, never kind rules: rules in the
project would copy the engine into it.

A **thought project** carries the chain: a brief, an intent and the
layers below it that the project needs, with its records, state,
resources, recipes and renders.

A **library** is a project of kind `library`, prefix `lib-`, and has
no chain. It carries a ledger, `sources/` and `research/` with their
indexes, `recipes/readme.md` and the README rendered from it, which
is the catalogue of what the library holds. It is material shared
across projects: deck templates, conventions, anything several
projects use. Nothing is redefined for it; registration and indexing
work as everywhere. Its material differs in one way from a thought
project's sources, which are inputs as of a date and immutable: a
library's documents are maintained by an owner who is also their
author, and whether a change overwrites the document or stands as a
new version beside it is the owner's choice.

Another project cites a library document by path. That citation is a
cross-repository dependency taken knowingly: only someone with both
repositories can read it, the version named in the citation is a
visible, unguarded pin, and a check is added when it hurts. Knowingly
means written down where state lives: the citing project's ledger
carries a Dependencies table with one row per document of another
repository it cites, registration only, no version recorded, since a
library document is maintained by its owner and cited as a moving
target by design.

## Instance facts and the forge's behaviour

The engine carries no instance facts. Who the principal is (by role)
and what language the conversation runs in are facts of one
installation, not properties of the system. They live in
`CLAUDE.local.md` at the engine root: gitignored, created from
`templates/CLAUDE.local.md` and filled by `/setup` on a new machine.
`CLAUDE.md` names the principal and the conversation language only as
things that exist, never by value.

Everything in `CLAUDE.local.md` reaches every subagent, the isolated
reviewers included, so only what must be always on and is harmless in
a public report belongs there. Git identities, names, e-mail
addresses and hosts live in the user's own git configuration outside
the engine: the commit identity is resolved per host by `includeIf`
stanzas in `~/.gitconfig`, which `/setup` offers to write, and the
forge sets no identity anywhere. The recommended guard is
`user.useConfigOnly = true` with no global name or e-mail, so that a
repository on a host with no stanza fails aloud instead of taking a
default.

The forge's behaviour lives in the engine, never in the assistant's
private memory. Claude Code keeps a per-directory memory outside the
repository; whatever it learns there about how the forge should work,
a working method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
That way every instance of the forge behaves the same, and a new user
meets the same forge as its author. Memory is left with what is
personal to one principal: idiom and private choices.

## No engine version in a project

A project records no engine version. The upgrade is `forge-pull` on
the engine, a fast-forward of `main`, and the checks measure a
project against the current conventions: after the pull,
`/check light` and `/check project` on each project say what the
conventions changed, the Action required lines of the release notes
say what to do, and Claude migrates on the user's word. No migration
tool exists, knowingly. This is the whole migration path of any
instance.

## Shapes rejected

Other shapes of the engine-to-projects relation were considered and
dropped:

- **Git submodules, subtree and worktrees.** They model a dependency,
  which this relation is not.
- **The engine as a template repository, or copying the engine into
  projects.** Every comparable project that does so ends in
  manifests, override layers and migrations.
- **A plugin as the only shape.** Not taken now.
- **A `local/` directory for user-local files.** It existed only to
  keep private material out of the repository, which the gitignored
  `projects/*` now does; deck templates live in a library project
  and are named by path.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrade the engine](../use/upgrade-the-engine.md): the upgrade and the migration path.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
