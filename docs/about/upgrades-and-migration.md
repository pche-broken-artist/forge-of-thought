---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 21ba7167bfd8ba4f
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is how an instance of Forge of Thought (one installation of
it) takes in a new release of the engine. A migration is the extra
step a release brings when it changes the shape of the files in a
project. This page explains how a project follows a new release, why
an old project is not a defect, and why a change of shape comes with
a migration instead of being done by hand. It is written for anyone
who uses the forge, extends it or evaluates it. The steps themselves
are on [Upgrade the engine](../use/upgrade-the-engine.md) and
[Migrate a project](../use/migrate-a-project.md).

## What it is

An upgrade is a pull of the engine: a fast-forward of its `main`
branch from the remote. Nothing else is installed.

A project records no engine version. The checks measure a project
against the conventions as they are today, whatever release the
project was written under. After a pull, the release notes say in
their Action required lines what to do. The pull also offers the
checks `/check light` and `/check project` on each project, so that
they name what the conventions changed.

Artefacts (the documents of a project's chain of thought) do not
expire with the conventions. An artefact stays valid under the
conventions it was written to. A finished or dormant project that no
longer conforms is a fact to report, never a defect to chase.
Bringing a project to newer conventions is a decision of the
principal (the person whose thinking the project forges). He makes it
per project, and it is never assumed.

A migration is the exception for one kind of release: a release that
changes the shape of files. Such a release comes with a migration,
run through one command, `/migrate [slug]`, on the principal's word
and never on Claude's.

## How it works

### An upgrade of a few lines

Most releases change a convention by a few lines. After the pull,
the checks name what no longer fits, the Action required lines say
what to do, and Claude brings the project in on the principal's word.

### A release that changes the shape of files

A release that rewrites the files of every project comes with a
migration. The migration is one command. A script,
`scripts/forge-migrate.py`, does every deterministic step. Claude,
within the same command, does what needs judgement.

The script recognises the shape of a project as a set of marks, one
mark per step. It never reads an engine version, since the project
carries none. For the migration the script carries today, the marks
are these:

- the project file `project.md` exists
- no header of an artefact, a work specification, a recipe, an index
  or the documentation map carries a field that changes with a round
- the project's threads live as files in `threads/`, or the project
  has no threads file
- `.gitattributes` exists
- `ledger.md` is out of git's index

A library (a project of shared material with no chain) takes all of
these but the threads.

The script runs only the steps whose mark is missing. Each step
verifies its own mark afterwards, and an unfinished project is
reported. Run without options, the script makes a dry run: it prints
the marks and, for every missing step, what it would change. With
`--apply` it runs the missing steps. It commits nothing: `/save`
follows. Until that save, `--undo` takes the last `--apply` back from
a manifest the script keeps of its own run.

Where something has no home in the new shape, the script prints it
for the principal instead of guessing. One example is a line waiting
on the principal that carries no ID. Another is the origin of a
thread, which the script guesses and prints for his judgement.
What the first migration made of the hand-kept ledger is told on
[The ledger, made from the records](the-ledger.md).

The script writes records, and the author of each record is the
principal's handle from the instance file. Without that handle it
refuses to run.

### Once per project, on one clone

A migration runs once per project, on one clone (one copy of the
repository on one machine), on `main`. Everyone else pulls before
working on. For a project that is a repository of its own, `--apply`
refuses:

- a working tree with unsaved changes to tracked files
- a branch behind its origin or diverged from it
- any branch but `main`

The migration is one large change, and these refusals keep it to one
run on one clone.

### A project outside git

A project outside git is migrated the same way, because being
outside git is a property, not a defect. None of the refusals of git
applies to it. The way back is the backup the principal takes before
`--apply`, and `--undo` refuses there. A run that stops midway is
finished by running it again: the marks are its memory, so the
second run does only what the first left undone.

### Until the migration, nothing writes

Until a project is migrated, nothing writes into it. A project
without its project file is of the shape before the migration. A
command that meets it reports the shape as a fact and stops. A check
reports it as one finding, whose one fix is `/migrate`, and raises
nothing else of the new shape against it. The project is read, not
written, because the engine cannot write two shapes. Whether and when
to migrate stays the principal's decision per project.

## Why

The way of upgrading by checks and a few lines brought in by hand was
made for small changes. A change of shape rewrites files of every
project, here and in every colleague's clone, and it must come out the
same everywhere. A migration done by hand cannot promise that. A
script for every deterministic step can, and so the result is the
same on every clone.

The marks, rather than a version, let a run that stopped be finished
by running it again. Why a project carries no engine version at all
is not recorded beyond the rule itself. Why the engine does not know
its projects is explained on
[Projects and the engine](projects-and-the-engine.md).

## A worked example

A generic project `my-project` was written under the old shape. It
has no `project.md`, its headers still carry a date, and its threads
sit in one file. The engine has just been pulled, and the Action
required lines say to run the migration.

1. The dry run:

   ```
   /migrate my-project
   ```

   The script prints the marks, missing ones included, and what each
   missing step would change. Nothing is written yet.

2. On the principal's word, the migration itself (through the script,
   `python scripts/forge-migrate.py my-project --apply`). The script
   creates the project file, takes the changing fields out of the
   headers, moves what only the old ledger knew into records, cuts the
   threads into one file each, writes `.gitattributes` and takes the
   ledger out of git. It prints the thread origins it guessed and any
   line it found no home for.

3. The principal looks at what was printed. If the result is wrong,
   `--undo` takes it back before anything is saved.

4. `/save` commits the migrated project. Colleagues pull it; none of
   them migrates it again.

From then on every command writes into `my-project` again.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
