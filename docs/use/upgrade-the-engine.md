---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 0fdf280818020c78
inputs:
  - .claude/skills/pull/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
  - CLAUDE.md#Persistence (git)
---

# Upgrade the engine

An upgrade of the engine is a pull of its `main` branch followed by
the work of bringing your projects to the conventions the new
release holds. This page is for you, the user who keeps one or more
projects under the engine: it says what you do after the pull, what
Claude shows you, and when a project has to be migrated rather than
merely checked. In this job you are the principal (the one whose
thinking is forged): every write to a project runs on your word and
on nobody else's. The pull itself, the running of a check and the
migration each have a page of their own, linked below; this page
joins them into one job.

## When to use it

Use this job whenever `/pull` has brought the engine forward. The
pull of the engine changes nothing in your projects: a project
records no engine version, and the checks measure it against the
conventions that hold now. A project you leave as it is stays
valid under the conventions it was written to. Its nonconformance
with the newer conventions is a fact the checks report, never a
defect to chase. One case is different: a release that changed the
shape of files. A project of the old shape is read and not written
until you migrate it, and the Action required lines of the release
say so. Why this is so is the page
[Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/pull
```

Then, project by project, on your word:

```
/check light my-project
/check project my-project
```

And where an Action required line names a migration, once per
project:

```
/migrate my-project
```

`my-project` stands for the slug of your project. `light` and
`project` are two checks of the check roster; what each verifies is
the page [Check conformance](check-conformance.md). Bare `/pull`
takes the engine and every project of yours that has an origin;
`/pull forge` takes the engine and the forge's own project beside
it where that project is cloned.

## What happens

1. **The pull.** Claude looks at the remote and says the state of
   each repository as a fact: up to date, behind, ahead, diverged,
   no origin, not under git. What is clean and behind is pulled;
   nothing is merged and no check runs unasked. How the pull runs in
   full is the page [Pull from the remote](pull-from-the-remote.md).
   You should now see where the engine moved from and to, and the
   subjects of the commits between.

2. **The Action required lines.** After a pull of the engine Claude
   reads the release notes (`RELEASE-NOTES.md` at the engine root)
   and shows you the Action required lines of every release the
   pull crossed. Action required is the first group of every
   release's section, before Added, Changed, Removed, Fixed and
   Rejected, and each of its lines carries, word for word, the
   `Action` of the record that documented the change: what you must
   do after it. You should now see a list of what the releases ask
   of you, release by release.

3. **The offer of the checks.** Claude offers `/check light <slug>`
   and `/check project <slug>` on each project you keep, and runs
   them only on your word. The two checks measure the project
   against the current conventions and say what the conventions
   changed. The findings are walked one at a time (a walkthrough:
   every item one message, closed with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`), and
   Claude brings the project current on your word, for an upgrade
   of a few lines. Bringing a project to newer conventions is your
   decision, made per project and never assumed. You should now see
   each finding settled with a verdict, and the project's documents
   changed where you accepted.

4. **The migration, where a release changed the shape of files.**
   Where an Action required line names a migration, Claude offers
   `/migrate <slug>` for each project you keep that is of the shape
   before the migration, as `templates/project.md` describes it.
   Until a project is migrated nothing writes into it: the checks
   and every writing command say what that template says and stop.
   A migration runs once per project, on one clone, on `main`, and
   on your word, never on Claude's. Claude shows you a dry run
   first, applies it on your word, judges with you what the script
   printed, remakes the ledger (the project's state file, made at
   read time, never in git) and proposes `/save <slug>`. The
   migrated shape reaches the remote by that save. Everyone else
   who works on the project then pulls it; nobody migrates a second
   time. The steps in full are the page
   [Migrate a project](migrate-a-project.md). You should now see
   the dry run, then the applied steps, then the proposal of the
   save.

## What you have afterwards

- The engine at the new release, its `main` fast-forwarded.
- The Action required lines of the releases crossed, read and
  acted on.
- Each project you chose to bring current measured by the two
  checks, its findings settled by verdict, its documents changed
  on your word.
- Each project of an old shape of files migrated once, saved, and
  on the remote for everyone else to pull.
- Any project you left as it is, valid under the conventions it was
  written to; one of the old shape, read but not written until you
  migrate it.

## If something goes wrong

- **A repository has unsaved changes or a diverged history.** The
  pull stops there with one offer: `/save` first, or a merge by
  hand or by `/save`, which rebases your commits onto the remote.
  Nothing is pulled from that repository.
- **The remote cannot be read.** The status run says what waits on
  GitHub outside git, the open pull requests and the unanswered
  discussions, or that it could not read them and why. Nothing of
  it is pulled, merged or answered.
- **The migration refuses to run.** A migration runs on `main` only
  and refuses a repository behind or diverged from its origin,
  offering `/pull`. A project already in shape ends at the dry run.
- **Something went wrong in a migration.** The way back is the
  migration script's, as its help header says. A tag before the
  migration is taken through `/save <slug> --tag <name>` before the
  migration is applied.
- **A project is of the old shape and you have not migrated it.**
  The checks and every writing command say what
  `templates/project.md` says and stop. This is not an error; the
  project is read until you migrate it.

## A worked example

You run `/pull`. Claude reports that the engine is behind and
clean and that your project `my-project` is up to date. It pulls the
engine, reports where `main` moved from and to, and lists the
subjects of the commits between, among them the commits of two
releases.

Claude reads the release notes and shows the Action required lines
of those two releases. One line says that a convention of the
history companion changed; the other says that the release changed
the shape of files and that each project of the old shape is to be
migrated.

Claude offers `/check light my-project` and `/check project
my-project`. You say yes. Both checks report that `my-project` is
of the shape before the migration, as `templates/project.md`
describes it, and stop there.

Claude offers `/migrate my-project`. You say yes. Claude shows the
dry run: the marks of the shape, the steps that would run and what
each would change. You accept, and Claude applies the migration,
then shows you what the script printed and walks with you what
needs judgement. Claude remakes the ledger and proposes `/save
my-project`; you accept, and the migrated shape reaches the remote.

Claude offers the two checks again. You say yes. The findings on the
history companion are walked one at a time; you accept them, and
Claude changes the project's documents on your word. Your colleague
on the same project runs `/pull my-project` on her clone and has the
migrated project, with nothing to migrate.

## See also

- [Pull from the remote](pull-from-the-remote.md): the pull itself.
- [Check conformance](check-conformance.md): running a check and
  settling its findings.
- [Migrate a project](migrate-a-project.md): the migration of a
  project to a new shape of files.
- [Upgrades and migration](../about/upgrades-and-migration.md): why
  a project records no engine version and when a migration comes
  with a release.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
