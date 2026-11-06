---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 909931a5874fa65e
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade of the engine is a fast-forward pull of its released line,
and a migration is the one command that brings a project to a new
shape of files when a release has changed that shape. This page
explains how a project follows a new release, why a project of an
older shape is a fact and not a defect, and why a change of the shape
of files is never brought in by hand. It is for the person who uses
the forge, for the one who extends it, and for the one who evaluates
it.

## What it is

An upgrade is a pull of the engine. The engine is one git repository
with a remote, and `main` is its released line. `forge-pull` (the
door is `/pull`) fast-forwards `main` from the remote, and on the
engine that is the upgrade channel. Nothing else happens at the pull
itself.

A project records no engine version. The checks (`/check light`,
`/check project`) measure a project against the conventions as they
stand today, never against the conventions it was written under.
After a pull of the engine, `/pull` shows the Action required lines
of the releases that were crossed and offers the two checks on each
project. The checks say what the conventions changed; the release
notes' Action required lines say what to do about it. This is the
whole upgrade path of any instance (one installation of the forge),
the principal's and a third party's alike. The principal is the
person whose thinking is being forged, the final authority on all
content.

Artefacts do not expire with the conventions. The conventions
evolve continuously, but an artefact (a document of the chain, such
as the intent) remains valid under the conventions it was written
to. Nonconformance of a finished or dormant project is a fact to
report, never a defect to chase. Bringing a project to newer
conventions is an explicit decision of the principal, made per
project and never assumed.

There are two sizes of change. An upgrade of a few lines is brought
in by Claude on the user's word, after the checks have named what
changed. A release that changes the shape of files comes with a
migration: `/migrate [slug]`, one command, run always on the user's
word and never on Claude's.

## How it works

### The upgrade of a few lines

The user pulls the engine. `/pull` lists the Action required lines
of the releases crossed and offers `/check light` and `/check
project` on each project. A check names what no longer conforms, as
a finding. Claude brings the project current on the user's word. A
project the principal leaves as it is stays a fact the checks report.

### The migration

The migration is one command, `/migrate [slug]`, and inside it a
script, `scripts/forge-migrate.py`, does every deterministic step,
while Claude, within the same command, does what needs judgement.

The script recognises the shape of a project as a set of marks, one
per step, never by an engine version kept in the project. A mark is
a fact of the files that is either there or not: the project file
exists, no header carries a field that changes with a round, the
`threads/` directory exists, `.gitattributes` exists, the ledger is
out of git's index. The script runs only the steps whose marks are
missing, and each step verifies its own mark afterwards. An
unfinished project is reported.

The marks of the migration the engine carries today, in the order
one run takes them:

- `A`: the fields that change with a round leave the headers, `date`
  and `last_change` from the artefacts and the work specifications,
  `updated` and `last_change` from the recipes, `updated` from the
  indexes, `generated` and `previous` from the documentation map.
- `B0`: `project.md` is written from `templates/project.md`, the slug
  from the directory's name, kind and language from the header of
  the hand-kept ledger (`thought` and `en` when absent).
- `B`: what only the hand-kept ledger knew becomes records, the
  mining of a brief as a record in the intent's history, the state
  of a work product as a record in its specification's history, a
  source's date, origin and form as fields of its index entry, a
  published file's provenance as its companion; then the hand-kept
  ledger is copied as it stands to `ledger.archive.md`, immutable,
  and `ledger.md` is taken out of git's index, nothing deleted, and
  put into the project's `.gitignore`. The ledger is the project's
  state report, made at read time from the documents; what the
  first migration made of the hand-kept one is told on [The ledger,
  made from the records](the-ledger.md).
- `C1`: the one threads file is cut into one file per thread in
  `threads/`, from `templates/thread.md`; the text is kept, the old
  file is deleted from the tree.
- `D`: `.gitattributes` is written from `templates/gitattributes`.

A library takes `A`, `B0`, `B` and `D`.

The dry run is the default: `python scripts/forge-migrate.py <slug>`
prints the marks and, for every step still missing, what it would
change. `--apply` runs the missing steps. What needs judgement is
printed for the principal rather than decided by the script: the
guessed origin of each thread, what follows the last thread and is
not a thread, and a Waiting line without an ID, which has no home in
the records. The author of every record the script writes is the
handle of the instance file; without it the script refuses.

The script commits nothing. `/save` follows, on the user's word.
Before the save, `--undo` takes the last `--apply` back from the
script's own manifest, `tmp/forge-migrate-<slug>.json` at the engine
root: changed and deleted tracked files are restored from the index,
created files are removed, the ledger is put back into the index and
the `.gitignore` line is taken out. The script stages nothing, so the
index still holds the files as they were before.

Where the project is a repository of its own, `--apply` refuses a
working tree with unsaved changes to tracked files, a branch behind
or diverged from its origin, and any branch but `main`. An untracked
file is no risk, since `--undo` restores tracked files only. The
migration runs once per project, on one clone, and everyone else
pulls before working on. `/migrate` shares this rule with every
command that makes a derived file: it runs on `main` only and, on a
repository behind or diverged from its origin, offers `/pull`.

A project outside git is migrated the same. None of the refusals of
git applies, because the forge runs no git on such a project. The
way back there is the backup the script tells the user to take
before `--apply`; `--undo` refuses on such a project. A run that
stops midway is finished by running it again, the marks being its
memory.

The slug `forge` names the engine's own project, whose repository is
the engine. The registration of the merge driver `ours` belongs to
`/setup` on every machine, not to the project's migration.

### Until a project is migrated

A project without `project.md` is of the shape before the migration.
Until it is migrated nothing writes into it. A command reports the
shape as a fact; a check reports it as one finding, with `/migrate`
as the fix, and raises nothing else of the new shape against the
project. The state map of `/forge`, `/check project` and every skill
that would write into the project say "shape before the migration,
run `/migrate`" and do not write. Saves made directly from the shell
are unaffected. How the engine stays unaware of the projects it
hosts is told on [Projects and the engine](projects-and-the-engine.md).

After a pull of the engine, Action required says to run `/migrate`
on every project, on one clone, then `/save`. The tag before a
migration is taken per project immediately before its `/migrate`,
the engine's before its own. Once a migration is saved, the way back
is the principal's own hand through git, always the engine and every
project together, since the engine refuses the old shape once
released.

## Why

A shape change is not brought in by hand because the position on
upgrades was made for upgrades of a few lines. A change of the shape
of files rewrites files of every project, here and in every
colleague's clone, and must come out the same everywhere. A script
for every deterministic step gives that sameness; Claude's judgement
is kept for what a script cannot decide.

Nothing writes into a project of the old shape because the engine
cannot write two shapes. A project of the old shape is read, not
written, until the principal migrates it, so that the migration
stays his decision per project.

The migration runs once, on one clone, because it is one large
change; everyone else pulls.

A project outside git is migrated the same because being outside git
is a property of the project, not a defect.

Nonconformance of a finished or dormant project is a fact and not a
defect because an artefact remains valid under the conventions it
was written to. Whether to bring it current is the principal's
decision per project.

Why a project records no engine version, and is measured against
the conventions of today instead, is not recorded.

## A worked example

A project `my-project` (a placeholder slug) was made before the
shape change. Its intent carries `date` and `last_change` in the
header, its threads stand in one file, its ledger is kept by hand
and tracked in git, and it has no `project.md`.

The user pulls the engine. `/pull` shows the Action required lines
of the release crossed, among them: run `/migrate` on every project,
on one clone, then `/save`. `/forge my-project` draws no state map;
it says "shape before the migration, run `/migrate`" and stops.
`/check project my-project` files one finding with that fix and
nothing else.

The user runs `/migrate my-project`. The dry run prints the five
marks: the project file missing, headers with changing fields,
the threads file present, `.gitattributes` missing, the ledger in
the index. For each it prints what `--apply` would change. The
repository is clean, on `main`, level with its origin, so `--apply`
runs. The fields leave the headers; `project.md` is written with
`project: my-project`, `kind: thought`, `language: en`; the ledger's
knowledge goes into the histories and the index entries, the
hand-kept ledger becomes `ledger.archive.md`, and `ledger.md` leaves
the index and enters `.gitignore`; each thread gets its file in
`threads/`; `.gitattributes` is written. The script prints the
guessed origin of each thread for the principal's judgement and one
Waiting line that had no ID. Each step verifies its mark; all five
hold.

Nothing is committed yet. The principal reads the guessed origins
with Claude, corrects two of them, and says `save`. `/save` commits
and pushes. A colleague on another clone runs `/pull` and works on;
she runs no migration of her own.

Had the principal wanted the change undone before the save, `--undo`
would have restored the tracked files from the index, removed the
created files, and put the ledger back. Had the project been outside
git, the dry run would have told him to take a backup first, no
refusal would have applied, and a run interrupted midway would have
been finished by running it again.

## See also

- [Upgrade the engine](../use/upgrade-the-engine.md): the steps
  after a pull of the engine.
- [Migrate a project](../use/migrate-a-project.md): running
  `/migrate`.
- [Projects and the engine](projects-and-the-engine.md): why the
  engine does not know the projects.
- [The ledger, made from the records](the-ledger.md): what the first
  migration made of the hand-kept ledger.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
