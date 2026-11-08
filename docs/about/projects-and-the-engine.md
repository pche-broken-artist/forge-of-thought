---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 6538154aec1d245e
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

The engine is one public git repository: the core of Forge of Thought
together with its own project, `projects/forge`; every other project
is a git repository of its own, nested under the engine's `projects/`
directory and unknown to the engine. This page explains that shape:
how the forge tells a project under git from a project outside git,
what a project file declares, where the facts of one installation
live, and why the relation between the engine and the projects was
given this shape and not another. It is for the user who sets up a
project, for the extender who touches the scripts that read the
repositories, and for the evaluator who asks why.

## What it is

The engine is one git repository with a remote. `main` is its
released line. Branches are voluntary and left to git. The root
holds the universal core: `CLAUDE.md` for Claude, `README.md` for
humans, `templates/`, `scripts/`, `.claude/` and the documentation
in `docs/`. Beside the core lies `projects/forge`, the forge's own
project: the forge run through its own process, with its brief, its
intent, its decisions and its recipes. Today that project is part of
the engine's repository; it is the one directory under `projects/`
that the engine tracks.

Every other project is a repository of its own. The engine's
`.gitignore` excludes `projects/*` and re-includes `projects/forge`
alone. So the engine does not know the projects: it carries none of
their files, none of their history and no address of theirs. The
owner of a project gives it whatever remote and whatever visibility
he wants, or none. A project with a repository and no remote is a
legitimate shape: it keeps the history that the renders and the
recipes rely on. A project with no repository at all is a legitimate
shape too; it keeps no history. The forge calls neither a defect.
"Not under git" is a property of a project.

A project is under git when git names the project's directory as the
top of a repository. That is the one question the scripts ask of git.
They never look for a `.git` directory. A project whose top lies
elsewhere, such as a directory inside somebody else's repository, is
for the forge a project outside git. So is a project with no
repository at all. On a project outside git the forge writes files to
disk and runs no git. The repository above it, if there is one, is
its owner's and is asked nothing, not even what it tracks. A project
outside git comes into the forge by hand: a copy or a link into
`projects/`. From then on the forge knows it.

Every project has a project file, `project.md`, written once at its
creation and never by a working round. It declares three things:

- `project`: the slug, the name of the project's directory
- `kind`: `thought` or `library`, default `thought`
- `language`: the language of the chain's artefacts, as an ISO 639-1
  code

The rules of a kind live in the engine. The project carries only the
marker. A project may carry an optional `CLAUDE.md` of its own, and
that file stays polish: it never holds the rules of a kind.

A thought project carries the chain: a brief, an intent and the
layers below it that the project needs. A library is a project of
kind `library` with no chain. It holds material shared across
projects, maintained by an owner who is also its author, with its own
repository and therefore its own visibility. Its slug begins with
`lib-`. Another project cites a library document by path. The
citation is a dependency across repositories, taken knowingly: the
citing project registers it in its ledger, the single source of truth
for state that is made at read time and never kept in git. No version
is recorded, since a library document is a moving target by design.
How a library is set up and used is on
[Share material through a library](../use/share-material-through-a-library.md).

The engine carries no facts of one installation. Who the principal is
(the person whose thinking is forged, named by role), what language
the conversation runs in and the handle he signs records with live in
`CLAUDE.local.md`, a file of the instance kept out of the repository.
The commit identity is git's, resolved per host by the user's own git
configuration; the forge sets none. The scripts carry no URL and no
identity. The forge's behaviour lives in the engine, in `CLAUDE.md`,
the commands and the templates, and never in the assistant's private
memory: Claude Code keeps a memory per directory outside the
repository, and whatever it learns there about how the forge should
work is written into the engine and removed from memory. Memory is
left with what is personal to one principal.

A project records no engine version; how a project follows the engine
is on [Upgrades and migration](upgrades-and-migration.md).

The engine is the one public place of an instance: what a project
shows in public goes out as a file into the engine's `docs/videos/`,
chosen in the project's recipe, while the project itself stays where
its sources require; the shape of that file is on
[The screenplay and its player](the-screenplay-and-its-player.md).

The shape, drawn:

```
<engine root>/                   one repository, public
├── CLAUDE.md  README.md  LICENSE
├── templates/  scripts/  .claude/  docs/
├── .gitignore                   projects/*  and  !projects/forge
└── projects/
    ├── forge/                   the forge's own project: tracked
    │                            by the engine's repository
    ├── <slug>/                  a thought project: a repository
    │   ├── .git/                of its own, any remote or none
    │   ├── project.md
    │   ├── 00-brief.md  10-intent.md  ...
    │   └── ledger.md            never in git
    ├── lib-<name>/              a library: a repository of its own
    │   ├── .git/
    │   ├── project.md
    │   └── sources/  research/  recipes/
    └── <slug>/                  a project outside git: files only,
        └── project.md  ...      no git run on it
```

## How it works

The engine's `.gitignore` carries the pattern `projects/*` followed by
the re-include `!projects/forge`. The pattern must be `projects/*`
and not `projects/`. Because with `projects/` the re-include fails
silently. The same file ignores `projects/forge/ledger.md`, since a
ledger is never in git.

The scripts recognise a project by one question to git: is the
project's directory the top of a repository? The answer decides
everything that follows. A project under git is served by the git
scripts; a project outside git is written to disk and skipped or
refused by them, whatever repository may lie above it. The question
is asked in one place, the module `scripts/forge_repos.py`, which the
git scripts share.

A project is born without git. `/new-project` and `/spinoff` create
files only and never touch git. Initialising the repository and
adding a remote are the user's one-off act at creation: the way into
git is `git -C projects/<slug> init -b main`, then a remote if one is
wanted. An existing project is brought in by `/import-project`
through `scripts/forge-clone.py`. A project outside git is brought in
by hand, as a copy or a link into `projects/`.

The scripts in `scripts/` are the door to every write of git, on the
engine and on every project repository alike: `forge-save.py` commits
and pushes, `forge-pull.py` fast-forwards from the remotes,
`forge-status.py` reports the state without changing anything,
`forge-branch.py` switches or creates a branch. Reading git directly
is open. No remote is configured anywhere in the forge. Because git
carries that information itself.

The project file is read wherever the kind and the language of a
project are needed, and it is merged as text. A project without a
project file is of the shape before the migration that introduced it.
The one remedy is `/migrate`: a command reports that shape as a fact,
a check reports it as one finding with that fix, and nothing else of
the new shape is raised against the project.

The engine is upgraded by `forge-pull` on the engine, a fast-forward
of `main`. Because a project records no engine version, `/check`
measures the project against the current conventions, and the
release notes say what to do; the rest is on
[Upgrades and migration](upgrades-and-migration.md).

Everything in `CLAUDE.local.md` reaches every subagent, that is,
every isolated agent Claude launches in a run of its own, the
reviewers included. So only what must be always on and is harmless in
a public report lives there. Names, e-mail addresses and hosts live in
the user's own git configuration outside the engine, and no fact of
an instance enters a reviewer's report.

Immutability of a document, such as a source or a review, is a process
rule, not a git mechanism. Git protects nothing from a commit that
rewrites a file. The rule costs nothing. A mechanism would be one more
layer to maintain, and it still would not stop a hand edit.

## Why

The engine is split from the projects so that it can be published.
The engine, the core together with `projects/forge`, is public and
contains nothing sensitive and no fact of one installation. Users
keep their projects wherever they choose. They are themselves
responsible for what those projects contain and where they live, a
generated deck with corporate branding included.

Each project is a repository of its own so that its owner decides its
visibility, project by project. A library has its own repository and
therefore its own visibility. A sensitive project may be kept local,
with no remote at all.

The engine does not know the projects so that nothing of theirs can
reach the public repository: the engine carries no address, no
identity and no file of a project.

The forge asks git whether a project is under git and asks nothing of
a repository above the project. Because that repository is its owner's.
The forge runs no git inside somebody else's repository. Why git is
asked for the top of the repository rather than a `.git` directory
looked for is not recorded here.

A project has a project file because the ledger is never in git: the
slug, the kind and the language would otherwise have no home that is.
A library's repository is, at its creation, this file alone.

The rules of a kind live in the engine and never in a project's own
`CLAUDE.md`. Because a project that carried them would copy the engine
into the project.

A project records no engine version so that the whole migration path
of any instance is the same: a pull of the engine, then the checks,
which say what the conventions changed.

A library document is cited without a version because it is a moving
target by design: its owner maintains it, and whether a new version
overwrites the old or stands beside it is the owner's choice. The
dependency is written down where state lives, in the ledger, so that
it is known before a render loses its template, not discovered then.

The forge's behaviour lives in the engine and not in the assistant's
memory so that every instance of the forge behaves the same, and a new
user meets the same forge as the principal.

The engine is the one public place of an instance because it is
public and served by GitHub Pages from its `docs/`, while a project
that makes a public file may have to stay in a private repository.
The engine carries the file only; the recipe, the render, the
provenance and the history stay in the project, and whoever has the
project regenerates it.

### The shapes rejected

- Git submodules, subtree and worktrees. They model a dependency,
  and the relation between the engine and a project is not one.
- The engine as a template repository, and copying the engine into
  each project. Every comparable project that does so ends in
  manifests, override layers and migrations.
- A plugin as the only shape, for now.
- A `local/` directory as the home of user-local files. It existed
  only to keep material of one installation out of the repository,
  which the gitignored `projects/*` now does. Deck templates live in a
  library project and are named by path.

## A worked example

A user clones the engine and creates a thought project with
`/new-project platform-notes`. The command writes the files of the
project under `projects/platform-notes/`, among them this project
file:

```
---
project: platform-notes
kind: thought
language: en
---
```

The command runs no git. At this point `projects/platform-notes` is a
project outside git: the engine ignores the directory, and the git
scripts skip it, which is a property of the project and not a defect.
The user then runs `git -C projects/platform-notes init -b main` and,
since this project is to be shared with two colleagues, adds a private
remote. From now on git names `projects/platform-notes` as the top of
a repository, and the git scripts serve it: `/save platform-notes`
commits and pushes on the project's own remote, and the engine's
repository is untouched.

Beside it the user keeps a library, `projects/lib-decks`, with a deck
template in its `sources/`. A recipe of `platform-notes` names the
template by path. The ledger of `platform-notes` lists it in its
Dependencies table, with no version, and the recipe works for anyone
who has both repositories.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrades and migration](upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Where the forge is going](where-it-is-going.md): the forge's own project as a repository of its own, a direction decided and not yet built.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
