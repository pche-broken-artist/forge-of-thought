---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: fe90df8522c5727e
inputs:
  - CLAUDE.md#Repository layout
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#The system's own project
  - projects/README.md
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
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/10-intent.md#REJ.0140
  - projects/forge/10-intent.md#REJ.0150
  - projects/forge/40-solution-design.md#SOL.0500
  - projects/forge/40-solution-design.md#SOL.0510
  - projects/forge/40-solution-design.md#SOL.0930
---

# Projects and the engine

The engine is the one repository a user clones, and every project is
a repository of its own that the engine does not track. This page
explains how the two are laid out, how a project is recognised, what
the forge's own project is, and why the shape is what it is. It is
for a user who wants to know where his work lives, for an extender
who develops the engine beside the forge's own project, and for an
evaluator who judges the split.

## What it is

The engine is one public git repository. It holds the core and
nothing else:

- `CLAUDE.md`, the instructions Claude works by
- `.claude/`, the skills, agents and settings
- `scripts/`, the scripts, the only platform-bound layer
- `templates/`, the canonical skeletons
- `docs/`, the generated documentation, see
  [Repository layout](../reference/repository-layout.md)
- `tests/`, the engine's tests
- `tmp/`, the working folder, its contents never in git
- the root files: the README, the release notes, the contributing
  guide, the security policy, the code of conduct, the licence and
  the avatar

The engine contains no project. Every project lives under
`projects/<slug>/` as a git repository of its own, with any remote
and any visibility its owner gives it, or with none. The engine's
`.gitignore` ignores `projects/*` whole. One file is re-included:
the directory's own `README.md`. So a clone of the engine has the
directory and a line on what belongs in it. The engine's
`.gitignore` carries no line of any project. Each project's ledger
(the project's state report, made at read time) is kept out of git
by the project's own `.gitignore`.

The forge's own project, `projects/forge`, is one project among the
others. It holds the thinking behind the engine: its brief, its
intent with the design positions and the rejected directions, its
threads, its decisions and its ledger. It is a repository of its
own beside the engine, public under the same account, and a user of
the engine never needs it.

## How it works

### How a project is recognised

A project is under git when git names the project's directory as
the top of a repository. That is the one question the scripts ask
of git. They never look for a `.git` directory. The reason for
asking git rather than looking for the directory is not recorded.

Anything else is a project outside git:

- a project whose top lies elsewhere, that is, a directory inside
  someone else's repository
- a project that has no repository at all

On a project outside git the forge writes its files to disk and runs
no git. The repository above it, if there is one, belongs to its
owner and is asked nothing, not even what it tracks. Such a project
comes in by hand, as a copy or a link into `projects/`, and the
forge knows it from then on. A project "not under git" is a
property, not a defect.

A project with a repository and no origin is a legitimate shape
too. So is a project without a repository, such as a sensitive
project kept local. The difference between the two: a repository
keeps the history that renders and recipes rely on, and a project
without one does not.

### How a project enters git

Initialising a project's repository and adding its remote are the
user's one-off act at the project's creation. `/new-project` and
`/spinoff` create files only and never touch git. The way in is
`git -C projects/<slug> init -b main`, then a remote if wanted. The
scripts carry no URL and no identity. The commit identity is git's,
resolved per host by the user's own configuration, and the forge
sets none. An existing project is brought in with
`/import-project <git-url>`, see
[Bring in an existing project](../use/bring-in-an-existing-project.md).

### The project file

Every project has a project file, `project.md`, in its root. It is
written once at the project's creation, by `/new-project` or by the
migration, and never by a working round. It is merged as text. It
declares three things:

- `project`: the slug
- `kind`: `thought` or `library`, default `thought`
- `language`: the language of the project's artefacts, as an ISO
  639-1 code

The rules of a kind live in the engine. The project carries only the
marker. A project's optional `CLAUDE.md` stays polish, never kind
rules. Because the rules would otherwise be copied from the engine
into the project. A project without a project file is of the shape
before the migration, and the one remedy is `/migrate`.

### The two kinds of project

A thought project carries the chain: a brief, an intent and the
layers below the intent that the project needs, with its threads,
decisions, sources, research, recipes and renders. The listing is
in [Repository layout](../reference/repository-layout.md).

A library is a project of kind `library`, prefixed `lib-`. It has no
chain. It holds a ledger, `sources/` and `research/` with their
indexes, and `recipes/readme.md` with the README it renders, a
catalogue of what the library holds. Its documents are maintained by
an owner who is also their author. Whether a change overwrites a
document or lays a new version beside it is the owner's choice.
Another project cites a library document by path. The citation is a
cross-repository dependency taken knowingly:

- only someone with both repositories can read it
- the assignment is self-contained anyway
- the citation carries no version, since the document is a moving
  target by design

Knowingly means written down where state lives. The citing project's
ledger carries a Dependencies table with one row per document of
another repository it cites. It records nothing but the citation; no
version is kept. How a library is used is in
[Share material through a library](../use/share-material-through-a-library.md).

### The forge's own project

`projects/forge` is a repository of its own, public under the same
account as the engine. Its repository is named `forge`. So
`/import-project` brings it into `projects/forge` without a rename.

A user clones the engine alone. Nothing he runs reads the project.

Whoever develops the engine clones the project beside it: the author
on any machine, and a contributor. Because the author's commands
read it:

- `/check engine`
- `/document`
- `/release forge`
- `/new-artefact`
- the renders of the README, the release notes and CONTRIBUTING

The paths `projects/forge/...` that the documentation cites are the
paths of that clone. How a contributor works with the two
repositories side by side is in
[Make a change to the forge](../extend/how-a-change-is-made.md).

What stays special about the project is in its recipes, not in the
scripts. A recipe (the file that says how a render is made) of this
project may name an `output:` with a leading slash. Such a root
render (an output generated from the project's documents) lands in
the engine root: the engine's README, its release notes and its
contributing guide are renders of `projects/forge/recipes/`. So a
release of the engine lands in two commits, the project's documents
in one and the engine's derived files in the other. The ledger reads
where a root render lies from the recipe. The renders are explained
in [Renders and recipes](renders-and-recipes.md). A process change is
complete only once that intent is updated and the README
re-rendered.

The project's own README on GitHub is a render of a recipe of its
own, `recipes/readme-project.md`. It is named apart because
`recipes/readme.md` of this project renders the engine's README.

### What `forge` names

The word `forge` means two different things, by the command.

In the commands of git, `/save`, `/pull`, the branch script
`forge-branch` and `/release`, `forge` names the whole: the engine's
repository and the forge's own project beside it where it is cloned.
Each gets its own commit, both prefixed `forge:`. The scripts label
the two `forge (engine)` and `forge (project)`. The release tag goes
on the engine alone. `forge-branch forge` switches both together.

In the commands over documents, such as `/forge`, `/check` and
`/document`, `forge` is the project.

### Where instance facts and behaviour live

The engine carries no instance facts. Who the principal (the person
whose thinking is forged) is, by role, and what language the
conversation runs in live in `CLAUDE.local.md`. That file is kept
out of the repository. Everything in it reaches every subagent (an
isolated run of Claude that sees nothing of the conversation), the
reviewers included. So only what must be always on and is harmless
in a public report lives there. The git identities, that is, names,
e-mail addresses and hosts, live in the user's own git configuration
outside the engine.

The forge's behaviour lives in the engine, never in the assistant's
private memory. Claude Code keeps a per-directory memory outside the
repository. Whatever it learns there about how the forge should work
is written into `CLAUDE.md`, the commands or the templates and
removed from memory. Memory keeps only what is personal to one
principal. So every instance behaves the same, and a new user meets
the same forge as the principal.

### What a project does not record

A project records no engine version; upgrade is a pull on the
engine, and a check measures the project against the current
conventions, see
[Upgrades and migration](upgrades-and-migration.md).

### The engine as the public place

The engine is the one public place of an instance: what a project
shows in public goes out as a file into the engine's `docs/videos/`
by the recipe's `output:`, while the project that made it stays
where its sources require, see
[The screenplay and its player](the-screenplay-and-its-player.md).

## Why

The forge is split into three parts: a public engine, the forge's
own project as a public repository beside it, and user projects in
repositories of their own. The engine and the forge's own project
contain nothing sensitive and no instance facts. Users keep their
projects wherever they choose. They are themselves responsible for
what those projects contain and where they live, generated decks
with corporate branding included. Because a library has its own
repository, it has its own visibility, and so does every project:
access is given per project, not for the instance as a whole.

The project file exists because the ledger left git. Once the ledger
is made at read time, the slug, the kind and the language would have
no home without a file of their own. A library's repository is, at
its creation, this file alone.

The forge's own project became a repository of its own against a
filtered branch of the engine for users. The design records what
made the choice possible: the ledger was made at read time, and the
user's path read nothing of the project. A further reason for
preferring it is not recorded.

The engine does not know the projects. A project without a
repository, or with one and no origin, is a legitimate shape, so the
forge demands no git of a project. What the forge promises instead
is that the scripts run no git on a project outside git, whatever
repository lies above it.

### The shapes rejected

Several shapes of the relation between the engine and the projects
were rejected:

- git submodules, subtree and worktrees: they model a dependency,
  which this relation is not
- the engine as a template repository, and copying the engine into
  each project: every comparable project that does so ends in
  manifests, override layers and migrations
- a plugin as the only shape: the reason is not recorded

A `local/` directory as the home of user-local files was dropped. It
existed only to keep sensitive material out of the repository, which
the gitignored `projects/*` now does. Deck templates live in a
library project instead and are named by path.

## The shape

```
<engine root>                   one public repository: the engine
├── CLAUDE.md
├── README.md  RELEASE-NOTES.md CONTRIBUTING.md   renders landing
│                                here from projects/forge/recipes/
├── .claude/  scripts/  templates/  docs/  tests/  tmp/
└── projects/                   gitignored (projects/*)
    ├── README.md               the one file of it the engine keeps
    ├── forge/                  the forge's own project: its own
    │   ├── .git/               public repository, named forge
    │   ├── project.md
    │   ├── 10-intent.md  ...
    │   └── recipes/            root renders with output: /...
    ├── <slug>/                 a thought project: its own
    │   ├── .git/               repository, any remote or none
    │   ├── project.md
    │   └── 00-brief.md  10-intent.md  ...
    ├── lib-<name>/             a library: its own repository,
    │   ├── .git/               its own visibility
    │   ├── project.md
    │   └── sources/  research/  recipes/readme.md
    └── <other>/                a project outside git: no .git
        └── project.md  ...     of its own, copied or linked in;
                                the forge runs no git on it
```

Each `.git/` under `projects/` is the top of a repository of its own.
Git names it as such, and that is how the scripts tell a project
under git from one outside it.

## A worked example

An instance has the engine cloned and three projects under
`projects/`:

- `projects/alpha`, a thought project with its own repository and a
  private remote
- `projects/lib-decks`, a library with its own repository, shared
  with a second instance
- `projects/notes`, a directory copied in by hand, with no
  repository

`/save alpha` commits and pushes the project's repository. `/save
lib-decks` does the same for the library. `/save notes` runs no git:
the project is outside git, and its files are written to disk only.
A recipe of `alpha` names `lib-decks/sources/deck-template.potx` by
path. The ledger of `alpha` then carries one row in its Dependencies
table for that document, with no version.

The user of this instance never cloned `projects/forge`. Nothing he
runs needs it. On the machine of a contributor to the engine,
`projects/forge` is cloned beside the engine. There `/save forge`
makes two commits, one in the engine and one in the project, both
prefixed `forge:`, while `/forge forge` opens the state map of the
project alone.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Bring in an existing project](../use/bring-in-an-existing-project.md): cloning a project, the forge's own among them, into `projects/`.
- [Upgrades and migration](upgrades-and-migration.md): why a project records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Renders and recipes](renders-and-recipes.md): the renders, the root renders of the forge's own project among them.
- [Make a change to the forge](../extend/how-a-change-is-made.md): how a contributor works with the engine and the forge's own project side by side.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
