---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: b725b3b8ca6c02a5
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is the step by which an installation of Forge of Thought
takes in a new release of the engine, and a migration is the step by
which one project is brought to a new shape of its files. This page
explains how a project follows a new release and why a release that
changes the shape of files comes with a migration. It is for anyone
who uses the forge, extends it or weighs it up.

## What it is

An upgrade is a pull of the engine. The pull is a fast-forward of the
engine's `main` from its origin, and nothing else is rewritten by it.
The steps you take after the pull are described in
[Upgrade the engine](../use/upgrade-the-engine.md).

A project records no version of the engine. The checks measure a
project against the conventions of the engine as it stands now. The
release notes say in their "Action required" lines what to do after
each release.

Artefacts do not expire with the conventions. An artefact is a
document of the chain, such as the brief or the intent. An artefact
stays valid under the conventions it was written to. A finished or
dormant project that no longer conforms is a fact to report. It is
never a defect to chase. Bringing a project to newer conventions is
the principal's decision, made project by project and never assumed.
The principal is the person whose thinking is forged in the project.

The engine does not know the projects. Each project is a repository
of its own, or a folder outside git, and the engine keeps no list of
them. Why this is so is explained in
[Projects and the engine](projects-and-the-engine.md).

## How it works

### An upgrade of a few lines

After a pull, the checks on each project say what the conventions
changed. The "Action required" lines of the releases crossed say what
to do. For an upgrade of a few lines, Claude brings the change into
the project on the principal's word.

### A release that changes the shape of files

A release that changes the shape of files comes with a migration. The
migration is one command, `/migrate [slug]`. It runs on the
principal's word, never on Claude's own judgement. Inside the command,
the script `scripts/forge-migrate.py` does every step that is
deterministic. Claude does, within the same command, what needs
judgement. Running it is described in
[Migrate a project](../use/migrate-a-project.md).

The script recognises the shape of a project as a set of marks, one
per step. It never reads a version of the engine from the project.
Each mark is a fact the script can see in the files:

- the project file `project.md` exists;
- no header of an artefact, a work specification, a recipe, an index
  or the documentation map carries a field that changes with a round;
- the folder `threads/` exists, or the project has no threads file;
- `.gitattributes` exists;
- the ledger file `ledger.md` is out of git.

The ledger is the table of a project's state. It is made from the
records at read time and never kept in git. What the migration made
of the ledger that was once kept by hand is explained in
[The ledger, made from the records](the-ledger.md).

The script runs only the steps whose marks are missing. Each step
checks its own mark afterwards. A project left unfinished is
reported. A library takes the steps for the headers, the project
file, the ledger and the attributes, and not the step for the
threads.

By default the script makes a dry run. The dry run prints the marks
and, for every missing step, what it would change. With `--apply` it
runs the missing steps. It commits nothing: a save follows with
`/save`. With `--undo` it takes back the last `--apply` from a
manifest of its own, which lies in the engine's `tmp/` folder. The
undo restores the tracked files that were changed or deleted, removes
the files that were created, and puts the ledger back where it was.

Some things the script cannot decide. It prints them for the
principal's judgement:

- the origin of each thread, which it guesses from the thread's first
  sentence;
- any text after the last thread that is not a thread;
- a line of waiting work in the old ledger that has no ID, which has
  no place in the records.

The script writes records, and the author of every record is the
principal's handle from the instance file. Without that handle it
refuses to run.

### Once per project, on one clone

A migration runs once per project, on one clone, on `main`. For a
project that is a repository of its own, `--apply` refuses in three
cases:

- the working tree has unsaved changes to tracked files;
- the branch is behind or diverged from its origin;
- the branch is not `main`.

The migration is one large change. It runs once, on one clone, and
everyone else pulls it before working on.

A project outside git is migrated the same way. Being outside git is
a property of a project, not a defect. None of the refusals of git
applies to it. The way back is the backup taken before `--apply`, and
the script tells you to take it. `--undo` refuses there. A run that
stops midway is finished by running it again, because the marks are
its memory.

### Nothing writes into the old shape

Until a project is migrated, nothing writes into it. The state map,
the checks and every command that would write into the project say
that the project has the shape before the migration and that the
remedy is `/migrate`, and then they stop. A project without the
project file `project.md` is of the shape before the migration. A
check reports this as one finding with that fix, and nothing else of
the new shape is raised against the project. A project of the old
shape is still read. The reason it is not written is that the engine
cannot write two shapes.

## Why

The way of upgrading by a pull and a few lines brought in by Claude
was made for upgrades of a few lines. A change of shape rewrites files
of every project, in the principal's clone and in every colleague's
clone. Such a change must come out the same everywhere. That is why a
script does every deterministic step, so that the result is the same
on every clone.

Artefacts stay valid under the conventions they were written to.
That is why a project that does not conform is reported and not
chased, and why bringing it current stays the principal's decision
for each project.

The engine cannot write two shapes. That is why a project of the old
shape is read but not written until it is migrated.

A migration is one large change. That is why it runs once, on one
clone, on a clean and current `main`, and why everyone else pulls.

The reason a project records no version of the engine, and why the
shape is recognised by marks rather than by such a version, is not
recorded.

## A worked example

A project with the placeholder slug `example-project` was made before
a release that changed the shape of files. It has no `project.md`.
Its intent's header carries `date` and `last_change`. Its threads live
in one file, `threads.md`. It has no `.gitattributes`, and its
`ledger.md` is kept in git.

After the engine is pulled, the state map of the project says that it
has the shape before the migration and offers `/migrate`. Nothing is
written into the project until then.

The principal asks for the migration on the one clone that will do
it. That clone is on `main`, clean and up to date with its origin. The
dry run shows all five marks missing and lists what each step would
change. On the principal's word the script runs with `--apply`, step
by step:

1. The fields that change with a round leave the headers.
2. `project.md` is made from the template, with the slug, the kind
   and the language.
3. What only the old ledger knew becomes records and index fields.
   The old ledger is copied, unchanged, to `ledger.archive.md`, and
   `ledger.md` leaves git.
4. `threads.md` is cut into one file per thread in `threads/`. The
   guessed origin of each thread is printed for the principal to
   judge.
5. `.gitattributes` is made from the template.

Each step checks its own mark. Nothing is committed yet. The
principal looks at the result and saves it with `/save`, or takes it
back with `--undo`. Colleagues working on the same project pull the
saved migration and do not run it themselves.

Had the run stopped after the second step, running it again would
find the first two marks present and run only the last three.

## See also

- [Upgrade the engine](../use/upgrade-the-engine.md): the steps after
  a pull of the engine.
- [Migrate a project](../use/migrate-a-project.md): running
  `/migrate`.
- [Projects and the engine](projects-and-the-engine.md): why the
  engine does not know the projects.
- [The ledger, made from the records](the-ledger.md): what the first
  migration made of the hand-kept ledger.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
