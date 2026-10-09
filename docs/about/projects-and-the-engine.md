---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About projects and the engine

This page explains how Forge of Thought separates the engine from the
projects it serves, what kinds of project there are, where the facts of
one installation live, and why the forge is built this way. It is for
anyone who uses the forge, extends it, or is weighing whether to adopt
it. It was put together from the repository layout and the git rules
in `CLAUDE.md`, from the design positions and rejected directions in
the forge's own intent (`projects/forge/10-intent.md`), and from the
description of the repositories in its solution design
(`projects/forge/40-solution-design.md`).

## One engine, many repositories

The engine is one git repository. It holds the universal core in its
root (`CLAUDE.md` for the assistant, `README.md` for humans,
`templates/`, `scripts/`, `.claude/`) together with one project, the
forge's own, in `projects/forge`. That project is Forge of Thought run
through its own process.

Every other project is a git repository of its own, nested under
`projects/<slug>/`. The engine ignores that directory in git, so it
never sees or records what a project contains: the engine does not know
the projects. The forge's git scripts recognise a project by the
presence of `projects/<slug>/.git`.

The ignore rule has one detail that matters. It must be written as
`projects/*` and then re-include the forge's own project with
`!projects/forge`. Written as `projects/` instead, the re-include fails
silently and the forge's own project would drop out of the engine.

## A project's repository is the user's

Creating a project's repository and giving it a remote is the user's
own one-off act. The commands that create projects make files only and
never touch git. A project may live under any remote with any
visibility, or have none:

- a project with a repository and a remote is the usual shape;
- a project with a repository and no remote is legitimate, for example
  a sensitive project kept local, and it keeps the history that renders
  and recipes rely on;
- a project with no repository at all is also legitimate, but keeps no
  such history.

A project "not under git" is a property, not a defect. The way into git
for a project is `git -C projects/<slug> init -b main`, then a remote
if wanted. The scripts carry no URL and no identity; the identity a
commit is made under is resolved by the user's own git configuration
per host, and the forge sets none.

### Why it is split this way

- **The engine can be published.** The engine, the core together with
  `projects/forge`, is public and contains nothing sensitive and no
  instance facts. Users keep their projects wherever they choose and are
  themselves responsible for what those contain and where they live,
  generated decks carrying corporate branding included.
- **Access per project.** Because each project is its own repository,
  access can be granted project by project rather than to everything at
  once.
- **The boundary is enforced by structure.** Keeping private material
  out of the engine is done by the ignored `projects/*` directory, not
  by a special folder for local files.

## Two kinds of project

A project has a kind, `thought` or `library`, declared in the header of
its ledger. The default is `thought`. The rules of each kind live in the
engine; the project carries only the marker. A project's optional
`CLAUDE.md` is polish, never a place for the rules of its kind, since
that would copy the engine into the project.

- **A thought project** carries the chain: a brief, an intent, and
  whatever layers below the intent it needs, with its records, sources,
  research, recipes and renders.
- **A library** is shared material with no chain. It has a ledger,
  `sources/` and `research/` with their indexes, and a README that
  catalogues what it holds. Its slug starts with `lib-`, and as its own
  repository it has its own visibility.

The material differs between the two. A thought project's sources are
inputs as of a date and are immutable. A library's documents are
maintained by an owner who is also their author: whether to overwrite
a document or add a new version beside it is the owner's choice.

### Citing a library

Another project cites a library document by its path. That citation is
a dependency across repositories, taken knowingly:

- only someone who has both repositories can read the cited document;
- an assignment is self-contained anyway, so it does not depend on the
  reader having the library;
- a version written into the citation is a visible pin, not a guarded
  one;
- a check is added when the lack of one starts to hurt.

"Knowingly" means written down where state lives. The citing project's
ledger has a Dependencies table with one row per document of another
repository it cites, such as a deck template named in a recipe. This is
registration only: no version is recorded, because a library document
is maintained by its owner and cited as a moving target by design. The
point is that a dependency is recorded, not discovered when a render
loses its template.

## Where the facts of one installation live

Who the principal is and what language the conversation runs in are
facts of one installation, not properties of the system. They live in
`CLAUDE.local.md` at the engine root, a file kept out of the
repository, created from `templates/CLAUDE.local.md` and filled by
`/setup` on a new machine. They never live in the engine itself:
`CLAUDE.md` names the principal and the conversation language only as
things that exist, never by value.

Everything in `CLAUDE.local.md` reaches every subagent, the isolated
reviewers included. So only what must be always on and is harmless in a
public report belongs there. Git identities, names, e-mail addresses
and hosts, live in the user's own git configuration outside the engine,
and such facts are never written into a reviewer's report.

The reverse also holds: the forge's behaviour lives in the engine,
never in the assistant's private memory. Claude Code keeps a memory per
directory outside the repository. Whatever it learns there about how
the forge should work, a working method, a rule of a command, a
convention, is written into `CLAUDE.md`, the commands or the templates
and removed from memory. The reason is that every installation of the
forge should behave the same, and a new user should meet the same forge
as anyone else. Memory keeps only what is personal to one principal.

## Upgrading without versions

A project records no engine version. The upgrade is `forge-pull` on the
engine, a fast-forward of `main`. The checks then measure each project
against the current conventions, not against the version it was made
with.

That is the whole migration path, for any installation: after the pull,
the light check and the project check on each project say what the
conventions changed, the release notes' Action required lines say what
to do, and Claude migrates on the user's word. No migration tool
exists, and that is deliberate.

## Shapes that were rejected

Other ways of relating the engine to its projects were considered and
dropped:

- **Git submodules, subtree and worktrees.** They model a dependency,
  and the relation between the engine and a project is not one.
- **The engine as a template repository, or copying the engine into
  projects.** Every comparable project that does so ends up with
  manifests, override layers and migrations.
- **A plugin as the only shape.** Not taken as the shape for now.
- **A `local/` folder for user-local files.** It existed only to keep
  private material out of the repository, which the ignored
  `projects/*` now does; deck templates live in a library and are named
  by path.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrade the engine](../use/upgrade-the-engine.md): the upgrade and the migration path.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
