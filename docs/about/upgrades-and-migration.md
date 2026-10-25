---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: c9c81508aff79189
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is how an installation of the forge takes in a new
release of the engine. A migration is the one command that brings a
project to a new shape of files when a release changes that shape.
This page explains how a project follows the engine, why most
upgrades need no migration at all, and why a change of the shape of
files does. It is written for anyone who runs the forge, extends it
or weighs whether to adopt it.

## What it is

An upgrade is a pull of the engine: a fast-forward of its `main`
line from its remote. Nothing more is fetched or rewritten by the
upgrade itself.

A project records no engine version. The checks (the reviewers that
verify mechanical conformance with the conventions) measure every
project against the conventions of the engine as it stands now. The
release notes say in their Action required lines what a user must do
after a release.

Artefacts (the documents of the chain, such as the brief and the
intent) do not expire with the conventions. An artefact remains
valid under the conventions it was written to. A finished or dormant
project that no longer conforms is a fact to report. It is never a
defect to chase.

Bringing a project to newer conventions is a decision of the
principal (the person whose thinking is forged). It is made per
project and never assumed.

A migration is the narrower case. A release that changes the shape
of files (where things live, what a header carries, which files a
project has) comes with a migration: one command, `/migrate [slug]`,
run through the script `scripts/forge-migrate.py`.

## How it works

### After a pull of the engine

After a pull, Claude shows the Action required lines of the releases
crossed. It then offers the checks on each project, and the checks
name what the conventions changed. For an upgrade of a few lines,
Claude brings the project current on the user's word.

### When the shape of files changes

A release that changes the shape of files comes with a migration.
The migration runs on the principal's word, never on Claude's. Within
the one command, the script does every deterministic step and Claude
does what needs judgement.

The script recognises the shape of a project as a set of marks, one
per step. It never reads an engine version from the project, because
the project carries none. It runs only the steps whose marks are
missing, and each step verifies its own mark afterwards.

The script works in three modes:

- the dry run: the default, which prints the marks and, for every
  step still missing, what it would change;
- `--apply`: runs the missing steps;
- `--undo`: takes back the last `--apply` from the script's own
  record of what it changed.

The script commits nothing. A save follows the migration. Until that
save, the migration can be undone.

### Once per project, on one clone

A migration runs once per project, on one clone (one copy of the
project's repository), on `main`. Everyone else pulls. On a project
that is a repository of its own, `--apply` refuses to run in any of
these cases:

- the working tree has unsaved changes to tracked files;
- the branch is behind or diverged from its origin;
- the branch is not `main`.

The reason is that the migration is one large change, made once.

### A project outside git

A project outside git is migrated the same way. Being outside git is
a property of a project, not a defect. None of the refusals above
applies to it. Its way back is the backup the user takes before
`--apply`, and `--undo` refuses there. A run that stops midway is
finished by running it again. The marks are its memory: the second
run sees which steps are done and runs only the rest.

### Before a project is migrated

Until a project is migrated, nothing writes into it. The state map,
the checks and every command that writes say that the project has
the shape before the migration and that the remedy is `/migrate`.
Then they stop. A check reports this as one finding with that fix,
and raises nothing else of the new shape against the project. A
project of the old shape is still read.

The reason is that the engine cannot write two shapes.

## Why

An ordinary upgrade is a few lines. A user and Claude can bring a
project current by hand, guided by the checks and the release
notes.

A change of the shape of files is different. It rewrites files of
every project, in every clone of every colleague. The result must
come out the same everywhere, and a migration by hand cannot promise
that. So every deterministic step belongs to a script, and Claude is
left only what needs judgement.

The migration runs once, on one clone, because it is one large
change. Everyone else takes it by pulling, so that no two clones
migrate the same project differently.

The marks let a run know what is left to do, on any project and
after any interruption. Why the project carries no engine version
instead is not stated beyond that the checks measure it against the
current conventions. The reason is not recorded.

Bringing a project current stays the principal's decision per
project, because an artefact remains valid under the conventions it
was written to.

## A worked example

A generic project, `my-project`, was written under an older shape.
Its headers carry fields that change with every round. It has no
project file (`project.md`, which holds the slug, the kind and the
language). Its open threads sit together in one file, and its ledger
(the table of the project's state) is kept in git by hand.

A new release changes that shape. After the pull of the engine, the
Action required lines say to run the migration on every project, on
one clone, then save. Any command that would write into `my-project`
says it has the shape before the migration and stops.

The principal runs `/migrate my-project`. The dry run prints the
marks, one per step:

- the project file exists: missing;
- no header carries a field that changes with a round: missing;
- the ledger is out of git: missing;
- the threads are one file each: missing;
- the file of merge settings, `.gitattributes`, exists: missing.

For each missing mark it prints what it would change.

On the principal's word, `--apply` runs the five steps in its fixed
order:

1. The changing fields leave the headers.
2. The project file is written from its template.
3. What only the ledger knew becomes records, and the hand-kept
   ledger is copied as it stands to `ledger.archive.md`.
4. The threads file is cut into one file per thread.
5. `.gitattributes` is written from its template.

Each step verifies its own mark. What needs judgement is printed for
the principal, such as the guessed origin of a thread.

The principal looks at the result. If it is wrong, `--undo` takes it
back. If it is right, a save commits it, and the colleagues pull.
From then on `my-project` has the new shape, and the commands write
into it again.

## See also

- [Upgrade the engine](../use/upgrade-the-engine.md): the steps after
  a pull of the engine.
- [Migrate a project](../use/migrate-a-project.md): running
  `/migrate`.
- [Projects and the engine](projects-and-the-engine.md): why the
  engine does not know the projects.
- [The ledger, made from the records](the-ledger.md): what the first
  migration made of the hand-kept ledger.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
