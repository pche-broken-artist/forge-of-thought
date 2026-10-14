---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: cb72dfaaa402aba0
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
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#REJ.0140
  - projects/forge/10-intent.md#REJ.0150
  - projects/forge/40-solution-design.md#SOL.0500
---

# Projects and the engine

The engine is one public git repository: the core of the forge
together with its own project, `projects/forge`. Every other project
is a git repository of its own, nested under `projects/`, a directory
the engine's git ignores. This page says what that shape is, how it
works and why it is so. It is for anyone who uses the forge, extends
it or evaluates it, and it stands on its own: the terms it needs are
glossed where they first appear, and the
[Glossary](../reference/glossary.md) has each of them in one line.

## What it is

The engine is a clone of one public repository. Its root holds the
universal core: `CLAUDE.md` for Claude, `README.md` for humans,
`templates/`, `scripts/` and `.claude/`. Beside the core lies
`projects/forge`, the forge run through its own process. The engine
contains nothing sensitive and no fact of an instance (one
installation of the engine on one machine). Its public home is named
in the README; this page does not repeat it. What lies where, file by
file, is the [Repository layout](../reference/repository-layout.md).

A project is a directory `projects/<slug>/`. It is a git repository
of its own, nested inside the engine's tree. The engine's
`.gitignore` excludes `projects/*` and re-includes `projects/forge`.
The engine does not know the projects: nothing in the engine records
which projects exist, where their remotes are or who may see them.
The scripts recognise a project by one sign, the directory
`projects/<slug>/.git`; how they do so is shared in
`scripts/forge_repos.py`.

A project may have any remote and any visibility, or none. Three
shapes are legitimate:

- a project with a repository and a remote;
- a project with a repository and no origin, which keeps the history
  the renders and recipes rely on;
- a project with no repository at all, which keeps no such history.

A project "not under git" is a property of that project, not a
defect.

A project has a kind, `thought` or `library`. The kind is declared in
the YAML header of the project's ledger (the project's single file of
state), and the default is `thought`. The rules of a kind live in the
engine. The project carries only the marker. A project's optional
`CLAUDE.md` stays polish and never holds the rules of a kind.

A thought project carries the chain: a brief, an intent and the
layers below it as the project needs them, with their records, its
sources and research, its recipes and renders. A library is a project
of kind `library`, its slug prefixed `lib-`. It has no chain: a
ledger, `sources/` and `research/` with their indexes, a readme
recipe and the README it renders, which is the catalogue of what the
library holds. A library is material shared across projects. Its
documents are maintained by an owner who is also their author. The
owner chooses whether a changed document is overwritten or a new
version is placed beside it. Another project cites a library document
by path. That citation is a dependency taken knowingly: it is written
into the Dependencies table of the citing project's ledger, one row
per document of another repository, with no version. How a library is
used in practice is
[Share material through a library](../use/share-material-through-a-library.md).

The facts of an instance live in `CLAUDE.local.md` at the engine
root: who the principal (the one whose thinking is forged) is, by
role, and what language the conversation runs in. That file is kept
out of the repository. The git identities, names, e-mail addresses
and hosts, live in the principal's own git configuration outside the
engine. The forge sets no identity anywhere, and its scripts carry no
URL and no identity.

The forge's behaviour lives in the engine, never in Claude's private
memory. Whatever Claude learns about how the forge should work, a
working method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory keeps only what is personal to one principal, such as his
idiom and his private choices.

A project records no engine version. The check `/check` measures a
project against the conventions as they stand today.

The engine is the one public place of an instance. A project's recipe
may send its format file out of the project into the engine's
repository, into `docs/videos/`, by its `output:` path. The engine
carries the file only. The recipe, the render, the provenance and the
history of that file stay in the project. What those files are and
how they are played is
[The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

A project is born as files. `/new-project` and `/spinoff` create
files only and never touch git. Putting the project under git is the
principal's one-off act at creation: `git -C projects/<slug> init -b
main`, then a remote if one is wanted. An existing project is brought
in by `/import-project`, whose script is `forge-clone.py`.

The scripts in `scripts/` are the only door to git, for reading state
as much as for writing it. For Claude the deny rules of
`.claude/settings.json` enforce this. The same scripts serve the
engine and every project that is a repository: `forge-save.py`
commits and pushes, `forge-pull.py` fast-forwards from the remotes,
`forge-status.py` reports state and changes nothing, `forge-clone.py`
brings a project in, and `forge-branch.py` switches to a branch or
creates one. Merging is git's, by hand or by merge request. Each
script describes itself in full in its own help header.

The commit identity is git's. It is resolved per host by the
principal's own configuration, through `includeIf` stanzas in
`~/.gitconfig`. `/setup` offers to write that configuration and one
global guard, `user.useConfigOnly = true` with no global `user.name`
or `user.email`. With the guard a commit in a repository on a host
with no stanza fails aloud instead of taking a default, and a save
commits nothing until git resolves an identity.

Everything in `CLAUDE.local.md` reaches every subagent (an isolated
worker that Claude launches, such as a reviewer). Therefore only what
must be always on, and is harmless in a public report, lives there.
Instance facts are forbidden in a reviewer's report. Every agent that
writes an outward-facing file reads its inputs from disk and treats
instance facts as not material, and the generated files are scanned
mechanically before they are kept.

The engine is upgraded by `forge-pull` on the engine, a fast-forward
of `main`. After the pull, `/pull` shows the Action required lines of
the releases crossed and offers `/check light` and `/check project`
on each project. The checks say what the conventions changed. The
release notes' Action required lines say what to do. Claude migrates
on the principal's word. No migration tool exists, knowingly. That is
the whole migration path of any instance, the principal's and a third
party's alike; the steps are
[Upgrade the engine](../use/upgrade-the-engine.md).

A library document cited by path is readable only by someone who has
both repositories. The assignment that cites it is self-contained
anyway. The citation carries no version, so the document is a moving
target by design. A check is added when that hurts.

A file a project shows in public is chosen in its recipe, file by
file, by naming an `output:` path into the engine's `docs/videos/`. A
file kept private names no `output:` and stays in the project's
`renders/`. The principal reads the file before the engine is saved;
that reading is the clearing of a public version, one step. The
engine serves `docs/` as web pages, and an empty `docs/.nojekyll`
keeps the files served as they lie. `docs/videos/` is flat, its files
in the order of their names. `/document` and its checks generate and
verify the documentation around that folder and leave it alone.
Whoever has the project regenerates the file.

## Why

The engine is public, and a public repository must contain nothing
sensitive and no fact of an instance. So the projects, which carry
the sensitive material, live outside the engine's history. Whoever
owns a project keeps it wherever he chooses and is responsible for
what it contains and where it lives, generated decks with corporate
branding included.

Each project is its own repository, so each may have its own remote
and its own visibility, or none. A library in particular has its own
repository and therefore its own visibility: access is granted
project by project, never for the engine as a whole.

A project lives inside the engine's tree so that every command and
every script reaches it by its slug, while the engine's git never
sees it. The gitignore pattern must be `projects/*` and not
`projects/`. With `projects/` the re-include of `projects/forge`
fails silently.

Several other shapes of the relation were rejected:

- git submodules, subtree and worktrees: they model a dependency,
  and this relation is not one;
- the engine as a template repository, and copying the engine into
  each project: every comparable project that does so ends in
  manifests, override layers and migrations;
- a plugin as the only shape of the engine, rejected for now: the
  reason is not recorded;
- a `local/` directory as the home of user-local files: it existed
  only to keep private material out of the repository, which the
  gitignored `projects/*` now does, and deck templates live in a
  library and are named by path.

A project records no engine version because the migration path is
the checks, not a manifest. The check measures the project against
the conventions as they are today, and the release notes say what to
do about what changed. A copied engine would have needed manifests
and migrations; the nested shape needs neither.

Instance facts stay out of the engine because the engine is public
and because everything in `CLAUDE.local.md` reaches every subagent,
the isolated reviewers included, whose reports are public files or
may be quoted into one. The commit identity stays with git because an
identity kept by the forge would duplicate what the principal's own
configuration already resolves per host.

The forge's behaviour stays out of Claude's memory so that every
instance of the forge behaves the same and a new user meets the same
forge as the principal.

A library document is cited with no version because its owner
maintains it as a moving target by design: the previous version of a
deck template is irrelevant, while a writing convention may usefully
say which versions it supports. The citation is registered in the
ledger so that the dependency is written down where state lives,
rather than discovered when a render loses its template.

The engine hosts what a project shows in public because it is the one
public place of the instance, while the project that made the file
stays where its sources require, in a private repository. The engine
carries the file only, so nothing of the project's thinking travels
with it.

## A worked example

The engine root, with its own project and two nested project
repositories, one of each kind:

```
forge-of-thought/              the engine: one public repository
  .git/
  .gitignore                   projects/* ignored, !projects/forge
  CLAUDE.md  README.md  templates/  scripts/  .claude/
  CLAUDE.local.md              instance facts, not in the repository
  docs/videos/                 the public files projects send out
  projects/
    forge/                     the engine's own project, tracked
    river-crossing/            kind: thought, a repository of its own
      .git/                    its own remote, private, or none
      ledger.md                kind: thought; a Dependencies row
      recipes/pitch.md         names a deck template by path
    lib-decks/                 kind: library, a repository of its own
      .git/
      ledger.md                kind: library
      sources/group-deck.potx  maintained by its owner
```

The principal clones the engine once. He creates a thought project
with `/new-project river-crossing`, which writes files and nothing
else. He runs `git -C projects/river-crossing init -b main` and adds
a private remote. The engine's git never sees the new directory,
because `projects/*` is ignored. `forge-status.py` lists the project
from then on, because it finds `projects/river-crossing/.git`.

He creates a library, `lib-decks`, the same way and puts a deck
template into its `sources/`. The recipe of a pitch in
`river-crossing` names that template by its path. The ledger of
`river-crossing` gets one row in its Dependencies table for the
template, with no version. A colleague who has only the engine and
`river-crossing` cannot read the template; the pitch's recipe says so
by the path alone.

Later a new release of the engine appears. The principal runs
`/pull`. The engine fast-forwards `main`; `/pull` shows the Action
required lines of the releases crossed and offers `/check light` and
`/check project` on `river-crossing` and on `lib-decks`. The checks
report what the conventions changed, and Claude migrates each project
on the principal's word. Neither project carries an engine version,
and none was needed.

## See also

- [Share material through a library](../use/share-material-through-a-library.md): using a library.
- [Upgrade the engine](../use/upgrade-the-engine.md): the upgrade and the migration path.
- [The screenplay and its player](the-screenplay-and-its-player.md): the public files a project sends into the engine.
- [Repository layout](../reference/repository-layout.md): the layout, file by file.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
