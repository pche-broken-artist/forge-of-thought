---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 7106191e2594c183
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is how a copy of the engine takes in a new release, and a
migration is how a project is brought to a new shape of its files
when a release changes that shape. This page explains both for the
user who runs the forge, for the extender who changes it and for the
evaluator who wants to know how projects stay usable as the engine
moves on. The steps themselves are on the how-to pages linked below.

## What it is

An upgrade is a pull of the engine: a fast-forward of its `main`
line, through `scripts/forge-pull.py`. Nothing else is installed or
converted by the pull itself.

A project records no engine version. The checks (the reviewers that
measure mechanical conformance with the conventions) measure a
project against the conventions as they stand now. The release notes
of each release say in their Action required lines what to do after
the pull. Why the engine keeps no list of its projects is explained
in [Projects and the engine](projects-and-the-engine.md).

Artefacts (the documents of the chain, such as the brief and the
intent) do not expire with the conventions. An artefact stays valid
under the conventions it was written to. When a finished or dormant
project no longer conforms, that is a fact to report. It is never a
defect to chase. Bringing a project to newer conventions is a
decision of the principal (the person whose thinking is forged),
made project by project and never assumed.

A migration is the narrower case. When a release changes the shape
of files, it comes with a migration: one command, `/migrate [slug]`,
backed by `scripts/forge-migrate.py`.

## How it works

### After a pull

After a pull of the engine, `/pull` shows the Action required lines
of the releases crossed. It offers `/check light` and `/check
project` on each project. Those checks say what the conventions
changed.

For an upgrade of a few lines, Claude brings the change into a
project on the principal's word, once the checks have named it.

### When the shape of files changes

A release that changes the shape of files does not rely on hand
edits. Its migration is one command that does two kinds of work:

- the deterministic steps: done by the script, every one of them;
- what needs judgement: done by Claude within the same command.

The migration runs on the principal's word, never on Claude's.

The script recognises the shape of a project as a set of marks, one
mark per step. It never reads an engine version, because the project
carries none. It runs only the steps whose mark is missing. Each step
verifies its own mark afterwards, and an unfinished project is
reported.

By default the script makes a dry run. It prints the marks and, for
every step still missing, what it would change. With `--apply` it
runs the missing steps. With `--undo` it takes back the last
`--apply`.

The script commits nothing. A `/save` follows the migration and
commits it. Until that save, the migration can be undone. The script
keeps a manifest of what it did, in the engine's `tmp/` folder. From
it, `--undo` restores changed and deleted tracked files from git's
index and removes the files it created. After the save, taking a
migration back is the principal's own work through git. That work
covers the engine and every project together, because the released
engine refuses the old shape.

### Once, on one clone

A migration runs once per project, on one clone (one copy of the
project's repository), on `main`. Everyone else pulls before working
on. The script with `--apply` refuses to run in each of these cases:

- the project is not a git repository;
- the working tree is not clean;
- the branch is behind or diverged from its origin;
- the branch is not `main`;
- the instance file names no author handle for the records the
  script writes.

### A project not yet migrated

Until a project is migrated, nothing writes into it. The state map,
the checks and every command that writes say that the project is of
the shape before the migration, name `/migrate` as the remedy, and
stop. A check reports this as one finding with that fix and raises
nothing else of the new shape against the project. A project of the
old shape is read, not written. The reason is that the engine cannot
write two shapes. The migration still stays the principal's decision
for each project.

One sign of the shape is the project file, `project.md`. It holds the
project's slug, its kind and the language of its artefacts. It is
written once, when a project is created or when it is migrated. A
project without this file is of the shape before the migration.

## Why

The way of an upgrade by Claude on the principal's word was made for
upgrades of a few lines. A release that changes the shape of files
rewrites files of every project, in every clone that colleagues hold.
That result must come out the same everywhere. A migration by hand
cannot promise that, so every deterministic step belongs to a script.

The migration runs once, on one clone, because it is one large
change. Everyone else pulls it.

A project carries no engine version, because the checks measure it
against the current conventions and the marks tell the script what is
missing. Any further reason for leaving the version out is not
recorded.

A project that no longer conforms is not treated as broken, because
an artefact stays valid under the conventions it was written to. Why
bringing it current is left to the principal project by project is
not recorded beyond that.

## A worked example

A generic project `<slug>` was made before a release that changed the
shape of files. After the pull of the engine, the state map of
`<slug>` says it is of the shape before the migration and names
`/migrate`. Nothing writes into it yet.

The principal decides to bring it current. On one clone, on a clean
`main` that is up to date with its origin, `/migrate <slug>` starts
with the dry run. The script prints its marks. For the migration the
script carries now, they are these:

- the project file `project.md` exists: missing;
- no header of an artefact, a specification, a recipe, an index or
  the documentation map carries a field that changes with a round:
  missing;
- the threads stand as one file each in `threads/`: missing;
- `.gitattributes` exists: missing;
- the ledger (the file that states the project's state) is out of
  git's index: missing.

For each missing mark it prints what it would change. With `--apply`
the script runs the five steps and checks each mark afterwards. The
hand-kept ledger is kept as an archive, and the ledger is from then
on made from the records; what that means is on
[The ledger, made from the records](the-ledger.md). Where judgement is
needed, such as the origin the script guessed for each thread, Claude
lays it before the principal.

The principal looks at the result. Had something been wrong, `--undo`
would have taken it all back. It is right, so `/save` commits and
pushes it. A colleague with another clone of `<slug>` pulls and works
on in the new shape. Run again, the dry run shows every mark present
and has nothing to do.

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

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
