---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: e6926dd3308b8dd0
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is a fast-forward pull of the engine, and a migration is
the one command that brings a project to a new shape of files when a
release has changed that shape. This page explains how a project
follows a new release of the engine, why a project carries no engine
version, and why a change of the shape of files is not left to hand
work. It is for the user who keeps projects on an engine that moves,
for the extender who changes the shape of a file, and for the
evaluator who asks what an upgrade promises.

## What it is

The engine is one git repository with a remote, and `main` is its
released line. Every project under `projects/` is a repository of its
own, and the engine does not know it: why that is so is said on
[Projects and the engine](projects-and-the-engine.md). An upgrade is
therefore an operation on the engine alone: `/pull` on the engine
fast-forwards its `main` from the remote, which is the engine's
upgrade channel. The steps after the pull are on
[Upgrade the engine](../use/upgrade-the-engine.md).

A project records no engine version. What a project conforms to is
measured by `/check` against the conventions the engine has now,
never against a number the project carries. The reason for this rule
is not recorded.

After a pull, `/pull` shows the Action required lines of the releases
that were crossed and offers `/check light` and `/check project` on
each project. The checks say what the conventions changed. The
release notes say in their Action required lines what to do about
it.

Artefacts do not expire with the conventions. The conventions evolve
continuously and `/check` measures against the current ones, but an
artefact remains valid under the conventions it was written to. A
finished or dormant project that no longer conforms is a fact to
report, never a defect to chase. Bringing a project to newer
conventions is a decision of the principal (the one whose thinking is
forged), made per project and never assumed.

An upgrade comes in two sizes:

- An upgrade of a few lines: Claude brings it into a project on the
  principal's word, after the checks have named what changed.
- A release that changes the shape of files: it comes with a
  migration, `/migrate [slug]`, run on the principal's word, never on
  Claude's. Running it is described on
  [Migrate a project](../use/migrate-a-project.md).

## How it works

A migration is one command with a script, `scripts/forge-migrate.py`,
for every deterministic step and Claude within the same command for
what needs judgement.

The script recognises the shape of a project as a set of marks, one
per step, never by an engine version in the project. It runs only
the steps whose mark is missing, and each step verifies its own mark
afterwards. An unfinished project is reported. The marks of the
migration the engine carries today are:

- the project file `project.md` exists (step B0);
- no header of an artefact, a work specification, a recipe, an index
  or the documentation map carries a field that changes with a
  round (step A);
- `threads/` exists, or the project has no threads file (step C1);
- `.gitattributes` exists (step D);
- `ledger.md` is out of git's index (step B).

What the steps make of a project is this. Step A takes the changing
fields out of the headers. Step B0 writes the project file from
`templates/project.md`, with the slug from the directory's name and
the kind and the language from the hand-kept ledger's header. Step B
turns what only the ledger knew into records: the mining of a brief
into a record of the intent's history, the state of a work product
into a record of its specification's history, a source's date, origin
and form into fields of its index entry, a published file's
provenance into its companion. The hand-kept ledger is then copied as
it stands to `ledger.archive.md`, immutable, and `ledger.md` is taken
out of git's index and put into the project's `.gitignore`, nothing
deleted. What the ledger (the project's state, made at read time
from its documents) became through this step is said on
[The ledger, made from the records](the-ledger.md). Step C1 cuts the
threads file into one file per thread under `threads/`, keeps the
text, guesses each thread's origin from its first sentence and prints
the guess for the principal's judgement. Step D writes
`.gitattributes` from its template. A library takes the steps A, B0,
B and D. The author of every record the script writes is the handle
the instance file gives; without it the script refuses.

The dry run is the default: `python scripts/forge-migrate.py <slug>`
prints the marks and, for every step still missing, what it would
change. `--apply` runs the missing steps. The script commits nothing;
`/save` follows. Before the save it can be undone: `--undo` takes
back the last `--apply` from the script's own manifest,
`tmp/forge-migrate-<slug>.json` at the engine root. A changed or a
deleted tracked file is restored from git's index, since the script
stages nothing; a created file is removed, the ledger is put back
into the index and the line in `.gitignore` is taken out.

A migration runs once per project, on one clone, on `main`, and
everyone else pulls before working on. So `--apply` refuses, where
the project is a repository of its own, a working tree with unsaved
changes to tracked files, a branch behind or diverged from its
origin, and any branch but `main`. An untracked file is no risk,
because `--undo` restores tracked files. This is the same rule as for
everything that makes a derived file: `/release`, `/publish`,
`/document` and `/migrate` run on `main` only, refuse a repository
behind or diverged from its origin and offer `/pull`.

A project outside git is migrated the same. Being outside git is a
property of a project, not a defect, and the forge runs no git on
such a project. None of the refusals of git applies to it. Its way
back is the backup the script tells the principal to take before
`--apply`; `--undo` refuses there. A run that stops midway is
finished by running it again, the marks being its memory.

The slug `forge` names the engine's own project, whose repository is
the engine. The registration of the merge driver `ours` is not part
of a migration: it is done by `/setup` on every machine, not in the
project.

Until a project is migrated nothing writes into it. A project without
the project file is of the shape before the migration, and the one
remedy is `/migrate`. The documentation map, `/check project` and
every skill that would write into such a project say "shape before
the migration, run `/migrate`" and stop: a command reports the shape
as a fact, a check as one finding with that fix, and nothing else of
the new shape is raised against the project. The project is read, not
written, until the principal migrates it.

The tag before a migration is taken per project immediately before
its `/migrate`, the engine's before its own. After the save, the way
back is the principal's own hand through git, and always the engine
and every project together. Because the engine refuses the old shape
once released, an engine taken back alone would meet projects it
cannot read.

## Why

The position on upgrades was made for upgrades of a few lines, which
Claude brings in on the principal's word after the checks have named
them. A change of the shape of files is different in kind: it
rewrites files of every project, in the principal's clone and in
every colleague's, and must come out the same everywhere. A hand
migration cannot promise that. So every deterministic step is a
script's, and only what needs judgement is Claude's, within the same
command.

The migration is one large change. So it runs once, on one clone, on
a clean `main` that is not behind its origin, and everyone else
pulls. The engine cannot write two shapes. So a project of the old
shape is read and not written until it is migrated, and the migration
stays the principal's decision per project.

A project outside git is migrated like any other, because being
outside git is a property of the project, not a defect. The refusals
of git do not apply to it, because no git runs on it; its safety is
the backup taken before `--apply`, and its memory is the marks.

Why a project records no engine version is not recorded.

## A worked example

A project `<slug>` was made before the shape changed. Its intent and
its recipes carry `date` and `last_change` in their headers, its
threads stand in one file `threads.md`, its ledger is kept by hand
and tracked in git, and it has no `project.md` and no
`.gitattributes`.

After the engine is pulled, `/pull` shows the Action required line of
the release that changed the shape and offers `/check project <slug>`.
The check reports one finding: the project is of the shape before the
migration, the fix is `/migrate <slug>`. Nothing else of the new
shape is raised against it, and no command writes into the project.

The principal runs `/migrate <slug>`. The dry run prints the five
marks, all missing, and for every step what it would change. On his
word `--apply` runs: the changing fields leave the headers (A),
`project.md` is written with the slug, the kind and the language
(B0), what only the ledger knew becomes records and index fields, the
hand-kept ledger moves to `ledger.archive.md` and `ledger.md` leaves
git's index (B), `threads.md` is cut into `threads/THR.NNNN.md`, one
file per thread, the guessed origins printed for his judgement (C1),
and `.gitattributes` is written (D). Each step verifies its mark. The
script commits nothing.

The principal looks at what the script printed, judges the guessed
origins, and runs `/save <slug>`. Had something been wrong, `--undo`
before the save would have put the project back as it was. Every
colleague with a clone of `<slug>` runs `/pull` before working on and
never runs the migration again: the marks are all present, and a
second dry run shows nothing to do.

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

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
