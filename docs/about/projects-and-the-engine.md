---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 1c7a6486befb99c6
inputs:
  - CLAUDE.md#Repository layout
  - .claude/reference/repository-layout.md
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

The engine and the projects of the forge are separate git
repositories. The engine is one public repository that holds the
forge and no project. Every project is a repository of its own, in a
directory the engine ignores. This page explains that split and the
reasons for it, for a reader who uses the forge, extends it or weighs
it.

## What it is

**The engine** is the core of the forge and nothing else. It is what
is cloned to get an [instance](../reference/glossary.md) (one
installation of the forge). Its root holds:

- `CLAUDE.md`: the universal core, the text Claude reads.
- `.claude/`: the skills with the commands among them, the agents,
  the reference files read on demand and the settings.
- `scripts/`: the scripts, such as the ones that write to git.
- `templates/`: the templates (the canonical skeletons).
- `docs/`: the documentation, generated.
- `tests/`: the tests of the engine.
- `tmp/`: the working folder of the engine. The folder is in git, its
  contents never.
- The root files: `README.md`, `RELEASE-NOTES.md` and
  `CONTRIBUTING.md` (all three generated), the security policy, the
  code of conduct, the licence, the logo and the files that configure
  git and the tests.

[Repository layout](../reference/repository-layout.md) gives the root
file by file.

**A project** is one directory, `projects/<slug>/`. The slug is the
short name of the project and the name of its directory. Every
project of an instance lives there, and each is a git repository of
its own. Its owner gives that repository whatever remote and
visibility he wants, or none.

The two meet in one directory. The engine's repository ignores
everything under `projects/` but one file, the directory's own
`README.md`. With that file a fresh clone of the engine has the
directory and a line on what belongs in it, and no project.

```
<engine>/                  repository: the engine, public
  CLAUDE.md
  CLAUDE.local.md          the instance file, never in git
  .claude/  scripts/  templates/
  docs/  tests/  tmp/
  README.md  ...           the root files
  .gitignore               ignores projects/*, keeps projects/README.md
  projects/
    README.md              the one file of projects/ the engine keeps
    forge/                 repository: the forge's own project, public,
                           cloned only by whoever develops the engine
    <slug>/                repository: a project of kind thought, with
                           the remote and the visibility its owner chose
    lib-<name>/            repository: a library
    <slug>/                no repository of its own: a project outside git
```

The pattern in the engine's `.gitignore` is `projects/*`, not
`projects/`. With `projects/` the one file could not be kept, and git
would not say so. The engine's `.gitignore` carries no line of any
single project.

## How it works

### The engine does not know the projects

A new project is scaffolded by `/new-project <slug>`. Both
`/new-project` and `/spinoff` create files only and never touch git.
Making the repository (`git init`) and giving it a remote is a
one-off act of the project's owner. An existing project is brought in
by `/import-project <git-url>`, as
[Bring in an existing project](../use/bring-in-an-existing-project.md)
describes.

A project that starts outside git has a property, not a defect. Three
shapes are legitimate:

- A repository with a remote, of the visibility its owner gives it.
- A repository with no origin: a sensitive project kept local. It
  keeps the history that its renders (the outputs generated for one
  audience) and their recipes (the files that say how a render is
  made) rely on. Both are explained on
  [Renders and recipes](renders-and-recipes.md).
- No repository at all: also kept local. It does not keep that
  history.

A project records no engine version: a check measures it against the
conventions of the engine as they stand, as
[Upgrades and migration](upgrades-and-migration.md) explains.

The engine is the one public place of an instance: what a project
shows in public goes out as a file into the engine's `docs/videos/`,
while its recipe, its render and its history stay in the project, as
[The screenplay and its player](the-screenplay-and-its-player.md)
explains.

### How a project under git is recognised

A project is under git when git names its directory as the top of a
repository. That is the one question the scripts ask. They ask git
itself and never look for a `.git` directory. The reason is not
recorded. The answer and the directory are compared as resolved
paths, so a project linked into `projects/` is judged like one that
lies there.

A project whose top lies elsewhere is a directory inside someone
else's repository. A project may also have no repository at all. Both
are, for the forge, a project outside git:

- The scripts write its files to disk.
- The scripts run no git on it.
- The repository above it is asked nothing, not even what it tracks.
- It comes in by hand, as a copy or a link into `projects/`. The
  forge knows it from then on.

### The project file

Every project has a project file, `project.md`. It is written once,
at the creation of the project, and no later work rewrites it. It
declares three things:

- `project`: the slug.
- `kind`: `thought` or `library`. The default is `thought`.
- `language`: the language of the project's artefacts, as an ISO
  639-1 code.

An artefact is a document of the
[chain](../reference/glossary.md) (the versioned documents a thought
travels through, from the brief and the intent onward). A project of
kind `thought` carries a chain. A project of kind `library` carries
none.

The project file is read wherever the kind and the language of a
project are needed. The rules of a kind live in the engine, and the
project carries only the marker. A project may have a `CLAUDE.md` of
its own. That file is polish where it is genuinely needed, never the
rules of a kind.

### A library

A [library](../use/share-material-through-a-library.md) is a project
of kind `library`: a collection of documents used across projects.
Its slug starts with `lib-`. It holds:

- the project file
- a [ledger](../reference/glossary.md) (the file that shows the state
  of a project, made when it is read and never in git)
- `sources/` and `research/`, each with its index
- the recipe of its README and the README made from it, which is its
  catalogue

The documents of a library are maintained by an owner who is also
their author. Whether he overwrites a document or puts a new version
beside it is his choice. The sources of a thought project are
different: they are inputs as of a date and immutable.

Another project cites a library document by path. The citation is a
dependency across two repositories, taken knowingly:

- Only someone who has both repositories can read it.
- It carries no version. The document is a moving target by design.
- It is registered. The ledger of the citing project carries a
  Dependencies table with one row for every document of another
  repository the project cites.

### The forge's own project

`projects/forge` is the forge itself run through its own process: the
thinking behind the engine. It holds a brief, an
[intent](../reference/glossary.md) (the trunk document of a project)
with the design positions and the rejected directions, the threads,
the decisions and a ledger.

It is one project among the others. It is a repository of its own
beside the engine, public under the same account. The repository is
named `forge`. With that name `/import-project` brings it into
`projects/forge` without a rename.

Who clones it depends on what the person does:

- Someone who only uses the forge clones the engine alone. Nothing
  such a user runs reads the project.
- Whoever develops the engine clones the project beside the engine.
  That is the author of the engine on any machine, and a contributor.

The reason for the second rule is that the author's commands read the
project:

- `/check engine`
- `/document`
- `/release forge`
- `/new-artefact`
- the renders of the README, the release notes and CONTRIBUTING

The paths `projects/forge/...` that the documentation cites are the
paths of that clone.

What stays special about this project is in its recipes, not in the
scripts. The README, the release notes and CONTRIBUTING of the engine
are renders made from `projects/forge/recipes/`. These root renders
land in the engine root, by the `output:` of their recipe. A release
of the engine therefore lands in two commits: the documents of the
project in one repository, the derived files of the engine in the
other.

The project's own README, the one its repository shows to a visitor,
is a render of a recipe of its own. That recipe is named apart, since
the recipe `readme` of this project renders the README of the engine.

A change of how the forge behaves that touches both repositories is
merged in both or in neither, in one sitting, never with a release
between the two. The reason is that git merges no two repositories as
one, and that the release is where the engine and the intent are read
together. Such a change is complete only once the intent is updated
and the README rendered again.
[Make a change to the forge](../extend/how-a-change-is-made.md) shows
how a contributor works with the two side by side.

### What `forge` names in a command

The word `forge` names two different things, by the kind of command:

- In the commands of git (`/save`, `/pull`, the branch script
  `forge-branch` and `/release`), `forge` names the whole: the
  engine's repository and the forge's own project beside it, where it
  is cloned. Each gets its own commit, with the prefix `forge:`. The
  two are labelled `forge (engine)` and `forge (project)`.
- In the commands over documents, `forge` is the project.

### What lives in neither

Two things belong neither in the engine's repository nor in a
project.

Instance facts live in `CLAUDE.local.md`, a file of the instance kept
out of the repository. They are who the principal is, by role, and
what language the conversation runs in. The principal is the person
whose thinking is forged. `CLAUDE.md` names both facts only as things
that exist, never by value. The git identities live in the
principal's own git configuration, outside the engine. The scripts
carry no address and no identity.

The forge's behaviour lives in the engine, never in Claude's private
memory. Claude Code keeps a memory per directory, outside the
repository. Whatever is learnt there about how the forge should work
is written into `CLAUDE.md`, the commands or the templates, and
removed from the memory. The memory is left with what is personal to
one principal, such as his idiom and his private choices.

## Why

**Publication with nothing sensitive.** The forge is split into three
parts:

- a public engine
- the forge's own project, a public repository beside it
- the projects of those who use the forge, each in a repository of
  its own

The engine and the forge's own project contain nothing sensitive and
no instance facts. The owners keep their projects wherever they
choose. They are themselves responsible for what their projects
contain and where they live, a generated deck with a corporate
branding included.

**Access per project.** A project that is a repository of its own has
its own visibility. A sensitive project stays local, with a
repository and no origin or with no repository at all.

**A project outside git.** The repository above such a project
belongs to its owner. For that reason it is asked nothing and no git
is run in it.

**The project file.** The ledger is never in git, so the slug, the
kind and the language would have no home there. A library's
repository is, at its creation, this file alone.

**The kind as a marker.** Rules of a kind written into a project's
own `CLAUDE.md` would copy the engine into the project.

**A citation taken knowingly.** Knowingly means written down where
the state lives, not discovered when a render loses its template.

**The forge's own project as a repository of its own.** With it the
engine knows no project at all, its own included. A repository of its
own was chosen against a filtered branch of the engine made for
users. What is recorded of that choice is what makes it possible: the
ledger is made at read time, and nothing a user runs reads the
project.

**Instance facts out of the engine.** Everything in
`CLAUDE.local.md` reaches every subagent (a separate run of Claude
given one task, such as an isolated reviewer). Therefore only what
must be always on and is harmless in a public report lives there.

**Behaviour in the engine.** Every instance of the forge then behaves
the same, and a new user meets the same forge as its author.

### The shapes rejected

- Git submodules, subtree and worktrees. They model a dependency, and
  the relation between the engine and a project is not one.
- The engine as a template repository, and the engine copied into
  each project. Every comparable project that does so ends in
  manifests, override layers and migrations.
- A plugin as the only shape of the forge, for now. The reason is not
  recorded.
- A directory `local/` as the home of user-local files. Its one
  purpose was to keep an owner's material out of the engine's
  repository, and the ignored `projects/*` does that. A deck template
  lives in a library and is named by path.
- A filtered branch of the engine for users, in place of a repository
  of its own for the forge's own project.

## A worked example

One instance holds four projects. All slugs are placeholders.

```
<engine>/projects/
  README.md
  my-project/          kind: thought, a repository with a private remote
  my-private-idea/     kind: thought, a repository with no origin
  lib-my-templates/    kind: library, a repository of its own
  my-notes/            a link to a directory inside another repository
```

`my-project` was scaffolded by `/new-project my-project`, which
created its files and touched no git. Its owner then made the
repository and gave it a private remote. Its project file reads:

```
---
project: my-project
kind: thought
language: en
---
```

`my-private-idea` is a sensitive project kept local. It has a
repository, so it keeps the history its renders and recipes rely on.

`lib-my-templates` holds a deck template. A recipe of `my-project`
names that template by path. The ledger of `my-project` shows the
citation as one row of its Dependencies table. Someone who has
`my-project` and not the library cannot read the template.

For the first three, git names the project's directory as the top of
a repository: they are under git. For `my-notes`, git names the top
of the repository above it: it is a project outside git. The scripts
write its files to disk, run no git on it and ask the repository
above it nothing.

The engine's repository holds none of the four, only
`projects/README.md`. There is no `projects/forge` here, and nothing
run on this instance reads it. If the owner of the instance began to
develop the engine, `/import-project <git-url>` with the address of
the forge's own project would clone it into `projects/forge`, beside
the others.

## See also

- [Share material through a library](../use/share-material-through-a-library.md):
  using a library.
- [Bring in an existing project](../use/bring-in-an-existing-project.md):
  cloning a project, the forge's own among them, into `projects/`.
- [Upgrades and migration](upgrades-and-migration.md): why a project
  records no engine version and how it follows the engine.
- [The screenplay and its player](the-screenplay-and-its-player.md):
  the public files a project sends into the engine.
- [Renders and recipes](renders-and-recipes.md): the renders, the
  root renders of the forge's own project among them.
- [Make a change to the forge](../extend/how-a-change-is-made.md):
  how a contributor works with the engine and the forge's own project
  side by side.
- [Repository layout](../reference/repository-layout.md): the layout,
  file by file.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
