---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 848c85180a59559a
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Template
---

# Upgrade the engine

An upgrade of the engine is a pull of its `main` branch followed by a
look at each of your projects against the conventions the new
version brings. This page is for you, the user of a forge, when you
have taken a new version of the engine and want to know what to do
with the projects you keep. It says what the pull shows you, how the
checks measure a project and how Claude brings a project to the
current conventions on your word. The pull itself, what it refuses
and what it reports, is on [Pull from the remote](pull-from-the-remote.md).
Every term of the forge is in the [Glossary](../reference/glossary.md).

## When to use it

Use this job after `/pull forge`, or after a bare `/pull`, has
fast-forwarded the engine. The engine does not know your projects.
A project records no engine version. So the pull touches no project:
a project is exactly as it was before. Whether a project follows the
conventions the new engine holds is a separate question, and this
job answers it project by project.

A project you leave as it is stays valid. It remains valid under the
conventions it was written to. A finished or dormant project that no
longer conforms is a fact to report, never a defect to chase.
Bringing a project to newer conventions is an explicit decision of
the principal (the person whose thinking the forge works on), made
per project and never assumed.

## What you do

There is no migration tool, and that is deliberate. The job is three
commands, the first already run:

```
/pull forge
/check light <slug>
/check project <slug>
```

`<slug>` is the name of one of your projects, such as `my-project`.
The two checks are run once per project you keep, and only on your
word: `/pull` offers them, it never runs them itself.

## What happens

1. **The pull reports what it crossed.** `/pull` relays where the
   engine moved from and to, and the subjects of the commits between.
   Among them are the commits of the releases crossed, each named
   `release <version>`. It then reads `RELEASE-NOTES.md` and shows
   the Action required lines of every one of those releases.

   You should now see the Action required lines of each release the
   pull crossed, one release after another.

2. **You read what is required.** Each Action required line names
   what changed, with a pointer, and then says what to do in your
   projects after pulling. If you would rather read the whole,
   open `RELEASE-NOTES.md` yourself: it holds one section per
   release, newest first, written for the user who takes upgrades
   through the pull, and Action required stands first in every
   section.

   You should now see, for each release crossed, what the engine
   asks of your projects, or that it asks nothing.

3. **`/pull` offers the two checks.** For each project you keep it
   offers `/check light <slug>` and `/check project <slug>`. Say
   yes for the project you want measured; say nothing for a project
   you leave as it is.

   You should now see the offer, one line per project, and nothing
   run until you answer.

4. **The checks measure the project.** Each check compares the
   project with the current conventions and reports what no longer
   conforms. The release notes say what to do; the checks say where
   in this project it applies. Running a check and the shape of its
   report are on [Check conformance](check-conformance.md).

   You should now see the findings of each check, or a report that
   found nothing.

5. **The findings are walked.** Claude puts the findings to you one
   at a time, as a walkthrough (one item per message, each closed
   with your verdict on it).

   You should now see one finding per message, waiting for your
   verdict.

6. **Claude migrates on your word.** What you accepted, Claude
   changes in the project in the session. Nothing is changed before
   your word, and nothing is changed in a project whose findings you
   did not walk.

   You should now see each change named by its file and section.

Repeat steps 3 to 6 for every project you keep. A project you skip
is not behind and not broken: it stands under the conventions it was
written to.

## What you have afterwards

- The engine on the new version of `main`.
- For every project you walked, the project brought to the current
  conventions in the places you accepted.
- For every project you left, the project unchanged and valid as it
  was written.

## If something goes wrong

- **The pull stopped before pulling the engine.** A repository with
  unsaved changes or with a diverged history is not pulled; `/pull`
  names the one offer that fits, `/save` first or a merge by hand,
  and the rest is on [Pull from the remote](pull-from-the-remote.md).
  There is nothing to upgrade until the engine has moved.
- **No Action required lines appear.** The releases crossed asked
  nothing of your projects. The checks may still find something:
  they measure against the whole of the current conventions, not
  only against what the notes list.
- **A check reports findings in a project you do not mean to
  migrate.** That is the intended outcome: nonconformance is reported
  as a fact. Leave the findings as reported, and the project stays
  valid under its own conventions.

## A worked example

You keep one project, `my-project`, and the engine's origin has
moved on since your last pull.

1. You type `/pull forge`. Claude runs the pull and shows where
   `main` moved from and to with the subjects of the commits
   between, one of them a `release <version>` commit.
2. Claude then shows the Action required lines of that release,
   read from `RELEASE-NOTES.md`. One line says that a template has a
   new section, with the pointer to it, and that each project's copy
   is to carry it.
3. Claude offers `/check light my-project` and
   `/check project my-project`. You say yes to both.
4. The checks run and report one finding: the project's copy of
   that template lacks the new section.
5. Claude puts the finding to you as one message and asks for your
   verdict. You accept.
6. Claude adds the section to the project's file and names the file
   and section it wrote.

Had you answered no in step 3, `my-project` would have stayed as it
was, valid under the conventions it was written to.

## See also

- [Pull from the remote](pull-from-the-remote.md): the pull itself, what it refuses and reports.
- [Check conformance](check-conformance.md): running a check and settling its findings.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
