---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 2c9f7eb62c0a360c
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is how an installation of the forge takes in a new release
of the engine, and a migration is how a project follows a release that
changes the shape of its files. This page explains both: what they
are, how they run and why they are built this way. It is for anyone
who uses the forge, extends it or weighs it up. The person whose
thinking is forged is called the principal (the one with the final
word on every project).

## What it is

An upgrade is a pull of the engine. The pull is a fast-forward of
`main` on the engine's repository, nothing more. In the image of the
owners, that pull is the upgrade channel.

A project records no engine version. The checks measure a project
against the conventions as they stand today. After a pull, the
release notes say in their Action required lines what to do.

Artefacts do not expire with the conventions. An artefact is a
document of the chain, such as an intent or an assignment. It stays
valid under the conventions it was written to. A finished or dormant
project that no longer conforms is a fact to report. It is never a
defect to chase. Bringing a project to newer conventions is the
principal's decision, made project by project and never assumed.

A migration is the narrower case. It is needed only when a release
changes the shape of files: the files a project holds, or the fields
they carry. Such a release comes with a migration of its own.

## How it works

### An upgrade of a few lines

After a pull of the engine, the pull command shows the Action required
lines of every release crossed. It then offers to run the checks on
each project. The checks name what the changed conventions mean for
that project. The release notes say what to do. Where the change is a
few lines, Claude brings it in on the principal's word.

### A release that changes the shape of files

Such a release comes with one command, `/migrate [slug]`. It runs
through one script, `scripts/forge-migrate.py`. The script does every
deterministic step. Claude does, within the same command, what needs
judgement. The migration always runs on the principal's word, never
on Claude's.

The script recognises the shape of a project as a set of marks. There
is one mark per step, and each mark is something that can be seen in
the project. Examples of marks:

- the project file `project.md` exists;
- no header carries a field that changes with every round of work;
- the threads live as one file each in `threads/`;
- `.gitattributes` exists;
- the ledger (the state report of a project, made from its documents
  at read time) is out of git.

The script never looks for an engine version in the project. It runs
only the steps whose mark is missing. Each step checks its own mark
afterwards, and a project left unfinished is reported.

The script has three ways of running:

- the default is a dry run: it prints the marks and, for every
  missing step, what it would change;
- `--apply` runs the missing steps;
- `--undo` takes back the last `--apply`, from a record of what that
  run changed and created.

The script commits nothing. A save follows the migration. So a
migration can be undone before it is saved.

Some steps leave matters for the principal to judge. The script
prints them rather than deciding. Examples are a guessed origin of a
thread and a waiting line in the old ledger that has no item to
belong to. The hand-kept ledger of the old shape is kept as it stood
in `ledger.archive.md`, unchanged from then on.

### Once per project, on one clone

A migration is one large change, and it runs once per project, on one
clone. Everyone else pulls before working on. For a project with a
repository of its own, `--apply` refuses to run in three cases:

- the working tree has unsaved changes to tracked files;
- the branch is behind or diverged from its origin;
- the branch is not `main`.

### A project outside git

A project outside git is migrated the same way. Being outside git is
a property of a project, not a defect. None of the refusals above
applies to it, since the forge runs no git on it. Its way back is the
backup the script tells you to take before `--apply`. `--undo` refuses
there. A run that stops midway is finished by running it again. The
marks are its memory: the second run does only what is still missing.

### Until a project is migrated

Until a project is migrated, nothing writes into it. A project without
its project file is of the shape before the migration. The state map,
the checks and every command that writes say so and stop. A command
reports the old shape as a fact. A check reports it as one finding,
whose one fix is `/migrate`. Nothing else of the new shape is raised
against such a project. The reason is that the engine cannot write two
shapes. A project of the old shape is still read.

## Why

An upgrade is a pull because the engine does not know the projects. A
project records no engine version because that version would be one
more thing to keep. The checks measuring against the current
conventions do that work instead.

Artefacts do not expire because conventions evolve continuously. An
artefact remains valid under the conventions it was written to. So
nonconformance is reported, and the step to newer conventions is left
to the principal for each project.

The upgrade of a few lines by Claude was made for small changes. A
release that changes the shape of files rewrites files of every
project, in every clone. Such a change must come out the same
everywhere. A migration done by hand cannot promise that. One command
with a script for every deterministic step can.

## A worked example

Take a generic project, `my-project`, under git with an origin, made
before a release that changed the shape of files. The engine has just
been pulled. The Action required lines say to run the migration on
every project, on one clone, then save.

1. You run `/migrate my-project`. The dry run prints the marks. The
   project file is missing, the headers still carry a date field, the
   threads sit in one file, there is no `.gitattributes`, and the
   ledger is still in git. For each missing step it says what it
   would change.
2. On the principal's word, the migration runs with `--apply`. The
   script writes `project.md` from the template, takes the changing
   fields out of the headers, turns what only the old ledger knew into
   records, keeps the old ledger as `ledger.archive.md` and takes
   `ledger.md` out of git. It cuts the threads file into one file per
   thread and adds `.gitattributes`. Each step checks its own mark.
3. The script prints what needs judgement, such as the guessed origin
   of each thread. Claude lays these out for the principal.
4. Nothing is committed yet. Had something gone wrong, `--undo` would
   take the run back. All is well, so a save follows.
5. A colleague with another clone of `my-project` pulls before working
   on. The colleague does not migrate again.

Had `my-project` been outside git, the same run would have taken
place without the refusals. A backup taken before `--apply` would have
been the way back.

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

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
