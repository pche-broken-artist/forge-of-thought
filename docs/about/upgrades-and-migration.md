---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: b0e4d425ae47bdf2
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - projects/forge/10-intent.md#POS.2030
  - projects/forge/40-solution-design.md#SOL.0800
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is a pull of a new release of the engine (one git
repository, whose branch `main` is the released line). A migration is
the one command that brings a project to a new shape of files when a
release changes that shape. This page explains how a project follows
the engine, why a small change needs no more than a pull and a few
lines, and why a change of the shape of files comes with a migration.
It is for whoever uses the forge, extends it or weighs it.

## What it is

**An upgrade is a pull.** The engine is upgraded by a fast-forward of
its `main`, through `/pull`. Claude never pulls or merges on its own
judgement.

**The engine does not know the projects.** Every project under
`projects/` is a repository of its own, and the engine's git ignores
it. Why this is so is told in
[Projects and the engine](projects-and-the-engine.md). A project may
also live outside git: that is a property, not a defect.

**A project records no engine version.** No file of a project says
which release of the engine it was written under. The checks
(`/check`) measure a project against the current conventions. Why a
project records no engine version: the reason is not recorded.

**Artefacts do not expire with the conventions.** The conventions
evolve continuously. An [artefact](../reference/glossary.md) remains
valid under the conventions it was written to. A finished or dormant
project that no longer conforms is a fact to report, never a defect
to chase. Bringing a project to newer conventions is an explicit
decision of the principal (the person whose thinking is being
forged). The decision is made per project and is never assumed.

**An upgrade is one of two sizes.** It asks a project for a few
lines, or it changes the shape of files (which files a project has,
what their headers carry and what git tracks). An upgrade of a few
lines is brought in by Claude on the principal's word. A change of
the shape of files comes with a migration.

## How it works

```
a pull of the engine
        |
        v
Action required of the releases crossed, the checks on each project
        |
        +-- a few lines -----------> Claude, on the principal's word
        |
        +-- the shape of files ----> /migrate, once per project,
                                     on one clone, on main;
                                     then /save; everyone else pulls
```

### After a pull

After a pull of the engine, `/pull` shows the Action required lines
of the releases crossed. Action required is the part of the release
notes that says what to do. `/pull` then offers `/check light` and
`/check project` on each project. The checks say what the conventions
changed. The steps are told in
[Upgrade the engine](../use/upgrade-the-engine.md).

### An upgrade of a few lines

The checks name what no longer conforms. Where that is a matter of a
few lines, Claude brings the project to the new conventions on the
principal's word. This is the whole upgrade path of any instance (one
installation of the forge), the principal's own and a third party's
alike.

### A change of the shape of files

A release that changes the shape of files comes with a migration
(`/migrate [slug]`), run always on the principal's word. It is one
command. The script `scripts/forge-migrate.py` does every
deterministic step. Claude does, within the same command, what needs
judgement. One example of judgement: the script guesses the origin of
each [thread](../reference/glossary.md) and prints its guess, and
Claude judges the origins from that print.

**The shape is a set of marks.** The script recognises the shape of a
project from the project itself, never by an engine version in it. It
reads one mark per step:

- the project file exists (`project.md`: the slug, the kind and the
  language of the project);
- no header of an artefact, a work specification, a recipe, a
  resource index or the documentation map carries a field that
  changes with a round;
- the directory `threads/` exists, or the project has no threads
  file;
- the file `.gitattributes` exists;
- [the ledger](the-ledger.md) (`ledger.md`, the file of a project's
  state, made at read time and never in git) is out of git's index.

Each kind of document named here, and each other term of the forge
that this page leaves unexplained, has its line in the
[Glossary](../reference/glossary.md).

**Only the missing steps run.** Without an option the script makes a
dry run (a run that changes nothing): it prints the marks and, for
every step still missing, what it would change. With `--apply` it
runs the missing steps and no others. Each step verifies its own mark
afterwards, and a project left unfinished is reported. A project of
the kind `library` takes every step but the one for the threads.

**Nothing is committed, and a run can be undone.** The migration
commits nothing: `/save` follows it. Before that save, `--undo` takes
back the last `--apply` from the script's own manifest (its list of
what the run changed, created and deleted). The tracked files the run
changed or deleted are restored, and the files it created are
removed. Nothing the run did is left behind, and nothing the run did
not make is removed.

**Once per project, on one clone, on `main`.** A migration is one
large change. It runs once per project, on one clone, and everyone
else pulls before working on. A project already migrated on another
clone is pulled through `/pull` and not migrated again. Whose machine
or instance the clone is on makes no difference: everyone who uses
the engine migrates their own projects. Where the project is a
repository of its own, `--apply` refuses in three cases:

- the working tree has unsaved changes to tracked files (an untracked
  file is no risk: the undo restores tracked files);
- the branch is behind its origin or has diverged from it, for which
  `/pull` is offered;
- the branch is any other than `main`.

Every record the script writes carries the handle that the instance
file (`CLAUDE.local.md`) names as the author. Without that handle the
script refuses as well.

**A project outside git is migrated the same.** The forge runs no git
on such a project, and none of the three refusals applies. The way
back is the backup taken before `--apply`: the dry run and `--apply`
both say so, and `--undo` refuses there. A run that stops midway is
finished by running it again. The marks are its memory.

**Until a project is migrated, nothing writes into it.** A project
without the project file is of the shape before the migration. A
command that would write into it reports the shape as a fact ("shape
before the migration, run `/migrate`") and stops. A check reports the
shape as one finding with that one fix, and raises nothing else of
the new shape against the project. The project is still read. The one
remedy is `/migrate`, and running it stays the principal's decision
per project.

### What needs no migration

A change of a template's wording is not a change of the shape of
files. A [template](../reference/templates.md) carries a comment that
says how a file is made and kept. The comment is read in the
template, by whoever makes the file or checks it. A file made from a
template carries none of that comment. Of the template's comments it
keeps one line, which names the template and never repeats its
wording:

```
<!-- Shape: templates/<name>.md -->
```

The line tells whoever writes into the file that the file has a shape
and where the shape stands. A change of a template's wording
therefore changes no file of any project, and no migration follows
it.

A file made before this rule may keep the comment it was born with.
Nothing reads that comment, no check reports it, and what holds is
the template's wording alone. The owner of a project may have the
comment replaced by the line. Nobody is made to, and an immutable
file keeps its comment. The replacement is a second form of the
migration (the script's option `--comments`), told in
[Migrate a project](../use/migrate-a-project.md): a step of its own
that has no mark, is never a condition of a write and runs only on
the owner's word.

## Why

**Why one command with a script.** The upgrade path of a pull, the
checks and Claude's hand was made for upgrades of a few lines. A
change of the shape of files rewrites files of every project, in
every clone. It must come out the same everywhere, and a migration by
hand cannot promise that. One script for every deterministic step
gives the same result on every clone.

**Why marks.** The marks were chosen against an engine version
written into the project, which the rule that a project records no
engine version excludes. Why a project records no engine version: the
reason is not recorded. The marks are also the memory of a run: a run
that stopped is run again, and only the missing steps run.

**Why a project of the old shape is read and not written.** The
engine cannot write two shapes. The migration stays the principal's
decision per project.

**Why once, on one clone, on `main`.** The migration is one large
change. It is made once and pulled by everyone else, in keeping with
the aim that the result is the same on every clone.

**Why a project outside git is not refused.** Being outside git is a
property of a project, not a defect.

**Why the way back is the engine and every project together.** The
engine refuses the old shape once the release is out.

**Why a file keeps one line of its template and not the comment.** A
rule that a comment owns stands once, in the template. A change of
the template's wording then changes no file of any project. The one
line stays for whoever writes into the file.

## A worked example

A generic project (`my-project`) was made before a release that
changed the shape of files. It is a repository of its own, and none
of the three refusals above applies to it.

The principal pulls the engine. Action required says to run the
migration on every project the clone keeps, on one clone, and then to
save. Until then a command that would write into `my-project` says
"shape before the migration, run `/migrate`" and stops.

The principal asks for `/migrate my-project`. The dry run prints the
five marks, none of them present, and what each missing step would
change. On the principal's word the missing steps run:

| What the script reads | Before the migration | After the migration |
|---|---|---|
| The project file | none | `project.md`: the slug from the directory's name, the kind and the language from the header of the hand-kept ledger (`thought` and `en` when absent) |
| The headers | `date` and `last_change` in the header of an artefact, `updated` in the header of a resource index | no field that changes with a round |
| The threads | one file (`threads.md`) | one file per thread under `threads/`, the old file deleted |
| The attributes | none | `.gitattributes`, made from its template |
| The ledger | `ledger.md`, kept by hand and tracked in git | `ledger.md` out of git's index and named in `.gitignore`; the hand-kept one copied as it stood to `ledger.archive.md`, immutable |

What only the hand-kept ledger knew moves to where it now lives:

- that a brief was taken into the intent: a record in the intent's
  history;
- the state of a work product: a record in the history of its
  specification;
- the date and the form of a source: the fields `Date` and `Form` of
  its entry in `sources/00-INDEX.md`;
- the provenance of a published file: the companion
  `published/<recipe>.md`.

What has no home in the records is printed for the principal. The
rest of that story is told in
[The ledger, made from the records](the-ledger.md).

The script prints the origin it guessed for each thread, and Claude
judges the origins from the print. `/check light` and `/check
project` follow. The run has committed nothing, and the principal
saves with `/save`. Had the result not been wanted, `--undo` before
the save would have taken the whole run back.

A colleague who keeps a clone of `my-project` pulls and migrates
nothing. A dry run on either clone now finds every mark present and
nothing to change.

Under the command, the script takes three forms:

```
python scripts/forge-migrate.py my-project            # dry run
python scripts/forge-migrate.py my-project --apply    # perform
python scripts/forge-migrate.py my-project --undo     # take back
```

## See also

- [Upgrade the engine](../use/upgrade-the-engine.md): the steps after
  a pull of the engine.
- [Migrate a project](../use/migrate-a-project.md): running
  `/migrate`, and its second form for the templates' comments.
- [Projects and the engine](projects-and-the-engine.md): why the
  engine does not know the projects.
- [The ledger, made from the records](the-ledger.md): what the first
  migration made of the hand-kept ledger.
- [Templates](../reference/templates.md): the templates and the line
  that names one in a file made from it.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
