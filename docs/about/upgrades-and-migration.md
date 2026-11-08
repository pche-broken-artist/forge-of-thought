---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 90a17f80244eb025
inputs:
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/10-intent.md#POS.1740
  - CLAUDE.md#Persistence (git)
  - templates/project.md
  - scripts/forge-migrate.py
---

# Upgrades and migration

An upgrade is a pull of the engine, and a migration is what a
project needs when a release of the engine changes the shape of its
files. This page explains how a project follows a new release, why
an artefact written to older conventions is not a defect, and why a
change of the shape of files is carried out by one command with a
script rather than by hand. It is for whoever runs the forge on a
project, for whoever extends the engine, and for whoever evaluates
how the forge keeps its projects usable across releases.

## What it is

The [engine](../reference/glossary.md) is one git repository with a
remote. Every project under `projects/` is a repository of its own,
which the engine does not know (see
[Projects and the engine](projects-and-the-engine.md)). A project
may also lie outside git altogether: a project "not under git" is a
property, not a defect.

An upgrade is a fast-forward pull of the engine's `main`. The
script `forge-pull` is the upgrade channel on the engine, and
`/pull` is its door. Nothing else happens to a project by the
upgrade itself.

A project records no engine version. What a project is measured
against is the current conventions: the checks (the reviewers that
verify mechanical conformance with the conventions) compare a
project with the conventions as they stand today, not with the
release the project was last worked under. After a pull, `/pull`
shows the Action required lines of the releases that were crossed
and offers `/check light` and `/check project` on each project. The
checks say what the conventions changed. The release notes' Action
required lines say what to do about it.

Artefacts do not expire with the conventions. The conventions
evolve continuously, and an artefact remains valid under the
conventions it was written to. Nonconformance of a finished or
dormant project is therefore a fact to report, never a defect to
chase. Bringing a project to newer conventions is an explicit
decision of the principal (whoever's thinking is being forged, the
final authority on content), made per project and never assumed.

A migration is the exception to the lightness of an upgrade. A
release that changes the shape of files comes with a migration. The
shape of files is what files a project has and what their headers
carry: whether the project file exists, whether a header carries a
field that changes with a round, whether the threads live in one
file or one file each, whether the ledger is tracked in git. Until
a project is migrated, nothing writes into it. The map, the checks
and every writing command say what the project file skeleton says
and stop: a project without the project file is of the shape before
the migration, the one remedy is `/migrate`, a command reports the
shape as a fact, a check reports it as one finding with that fix,
and nothing else of the new shape is raised against the project.

## How it works

Two kinds of upgrade are told apart by what they change.

An upgrade of a few lines is brought in after the checks have named
it. The checks say what the conventions changed, the release notes
say what to do, and Claude migrates the project on the principal's
word. This is the whole migration path of any instance, the
principal's own or a third party's alike.

A release that changes the shape of files comes with a migration:
`/migrate [slug]`, one command. A script, `scripts/forge-migrate.py`,
runs every deterministic step, and Claude, within the same command,
does what needs judgement. The result is then the same on every
clone. Running it is described in
[Migrate a project](../use/migrate-a-project.md).

The script recognises the shape of a project as a set of marks, one
per step, never by an engine version in the project. The marks it
knows are these:

- the project file `project.md` exists;
- no header of an artefact, a work specification, a recipe, an index
  or the documentation map carries a field that changes with a round;
- `threads/` exists, or the project has no threads file;
- `.gitattributes` exists;
- `ledger.md` is out of git's index.

A library takes only the marks that apply to it: the project file,
the headers, the ledger and the attributes.

The script runs only the steps whose marks are missing, and each
step verifies its own mark afterwards. A project left unfinished is
reported. The dry run is the default: it prints the marks and, for
every step still missing, what the step would change. `--apply`
performs the missing steps.

What the steps do, in the order of one run:

- the fields that change with a round leave the headers of the
  artefacts, the work specifications, the recipes, the indexes and
  the documentation map;
- `project.md` is written from `templates/project.md`, the slug from
  the directory's name, the kind and the language from the header
  of the hand-kept ledger, `thought` and `en` when absent;
- what only the hand-kept ledger knew becomes records: the mining of
  a brief as a record in the intent's history, the state of a work
  product as a record in its specification's history, a source's
  date, origin and form as fields of its index entry, a published
  file's provenance as its companion; then the hand-kept ledger is
  copied as it stands to `ledger.archive.md`, immutable, and
  `ledger.md` is taken out of git's index and put into the project's
  `.gitignore` (what became of the ledger is the matter of
  [The ledger, made from the records](the-ledger.md));
- the threads file is cut into one file per thread under `threads/`,
  the text kept, the artefact each thread concerns taken from its
  bracket, its origin guessed from the first sentence and printed
  for the principal's judgement, and the old file deleted from the
  tree;
- `.gitattributes` is written from `templates/gitattributes`.

A Waiting line without an ID has no home in records and is printed
for the principal instead. The author of every record the script
writes is the handle of the instance file. Without that handle the
script refuses.

The script commits nothing. `/save` follows, on the principal's
word. `--undo` takes back the last `--apply` from the script's own
manifest in the engine's `tmp/`: changed and deleted tracked files
are restored from the index, created files are removed, the ledger
is put back into the index, and the ignore line is taken out. This
is possible because the script stages nothing.

Where the project is a repository of its own, `--apply` refuses to
run in three situations:

- the working tree has unsaved changes to tracked files (an
  untracked file is no risk, since `--undo` restores tracked files);
- the branch is behind or diverged from its origin;
- the branch is any but `main`.

The migration is one large change. It runs once, on one clone, and
everyone else pulls before working on. This is the same rule that
holds for everything that makes a derived file: `/release`,
`/publish`, `/document` and `/migrate` run on `main` only, refuse a
repository behind or diverged from its origin and offer `/pull`.

A project outside git is migrated the same, under none of the
refusals of git. The forge runs no git on it. The way back is the
backup the script tells the principal to take before `--apply`, and
`--undo` refuses there. A run that stops midway is finished by
running the script again, the marks being its memory.

A tag is taken on each project immediately before its migration,
and on the engine before its own. Going back after the save is the
principal's own hand in git, and always the engine and every project
together. Because the engine refuses the old shape once it is
released.

The steps after a pull, from the Action required lines to the saved
project, are the matter of
[Upgrade the engine](../use/upgrade-the-engine.md).

## Why

The migration is a script and one command because of what a shape
change does. The position on upgrades was made for upgrades of a
few lines, which Claude brings in on the principal's word. A change
of the shape of files rewrites files of every project, here and in
every colleague's clone, and must come out the same everywhere. A
migration done by hand cannot promise that. A script for every
deterministic step can, and Claude is kept for what needs judgement.

The shape is read as marks and not as a recorded engine version
because a project records no engine version. Why a project records
none is not recorded.

Artefacts do not expire because an artefact remains valid under the
conventions it was written to. A finished or dormant project that no
longer conforms is reported, not chased, and the decision to bring
it current stays with the principal per project.

A project of the old shape is read and not written because the
engine cannot write two shapes. Until the principal migrates it, the
migration stays his decision per project.

The migration runs once, on one clone, because it is one large
change. Everyone else pulls the result instead of running it again.

A project outside git is migrated the same because being outside git
is a property, not a defect. Its safeguards are different in kind,
a backup and the marks, not absent.

## A worked example

A project `my-project` was last worked under older conventions. It
has no `project.md`, its intent header carries a date, its threads
stand in one file, and its hand-kept ledger is tracked in git. The
engine is pulled, and `/pull` shows the Action required lines of the
releases crossed, among them the line that says to run the
migration on every project, on one clone, then save. From here on
the checks report `my-project` as one finding, the shape before the
migration with `/migrate` as its fix, and nothing of the new shape
is raised against it besides. Nothing writes into the project.

The principal runs the dry run, `/migrate my-project`. The script
prints the five marks: the project file is missing, the headers
carry a field that changes with a round, the threads file exists,
`.gitattributes` is missing, the ledger is in git's index. Under
each missing mark it prints what the step would change, and nothing
is written.

The project is on `main`, clean and up to date with its origin, so
the principal lets the migration apply. The date leaves the intent
header. `project.md` appears with the slug, the kind and the language
taken from the ledger's header. The records that only the ledger
knew are appended to the histories, the ledger is copied to
`ledger.archive.md`, and `ledger.md` leaves the index. The threads
file is cut into one file per thread, and the script prints each
guessed origin for the principal to judge, with one Waiting line
that had no ID. `.gitattributes` is written. Each step verifies its
mark, and the script reports the project as finished.

Nothing is committed yet. If the result is not wanted, `--undo`
takes it back from the manifest. If it is, `/save` records it, and
everyone else working on `my-project` pulls before working on. A
second run of the dry run finds every mark present and nothing to
do.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
