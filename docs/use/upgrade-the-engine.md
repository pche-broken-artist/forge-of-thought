---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: bb3f2ae051567884
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Template
---

# Upgrade the engine

Upgrading the engine is a pull of the engine's repository followed
by one decision per project: whether to bring that project to the
conventions the new engine carries. This page is for you, the user
who takes new versions of the engine and keeps projects of your own
under it. It says what you do after the pull, what Claude shows you
and what becomes of a project you leave as it is. The pull itself is
on the page [Pull from the remote](pull-from-the-remote.md).

## When to use it

Use this job whenever the engine has moved and you have pulled it,
or are about to. The engine is upgraded by a pull: a fast-forward of
its `main` branch from its remote. Your projects are not touched by
that pull. A project records no engine version. What the engine's
conventions now expect of a project is measured only when you ask
for it, by a check.

A project you do not bring over is not broken. An artefact (a
document of a project's chain, such as its brief or its intent)
stays valid under the conventions it was written to. Nonconformance
of a finished or a dormant project is a fact to report, never a
defect to chase. Bringing a project to the newer conventions is your
explicit decision, made per project and never assumed.

## What you do

```
/pull
```

Then, for each project you keep, with the project's slug in place of
`my-project`:

```
/check light my-project
/check project my-project
```

`light` and `project` are two checks of the forge's roster. Claude
(the model that runs the forge) offers them after the pull and runs
them only on your word.

## What happens

1. **The pull.** `/pull` looks at the remote and reports the state of
   each repository: the engine and every project with an origin.
   Clean and behind, the engine is pulled; Claude relays where it
   moved from and to and the subjects of the commits between.
   You should now see the pull report, with one line per release the
   engine crossed.

2. **The Action required lines.** After a pull of the engine, Claude
   reads `RELEASE-NOTES.md` and shows you the `Action required` lines
   of every release the pull crossed. The release notes are written
   for you, the user who takes upgrades through a pull. `Action
   required` stands first in each release's section. Each line says
   what changed and what to do in your projects after pulling. You
   may also open `RELEASE-NOTES.md` yourself and read these lines
   there.
   You should now see the `Action required` lines, one group per
   release crossed, and Claude's offer of `/check light` and
   `/check project` on each of your projects.

3. **Your word on the checks.** Claude runs no check unasked. Name
   the projects you want measured. A project you leave out stays as
   it is.
   You should now see Claude running the two checks on the projects
   you named, and nothing on the others.

4. **The two checks.** `/check light <slug>` and
   `/check project <slug>` measure the project against the current
   conventions, the ones the engine now carries. What a check finds
   is a finding (a reviewer's result, with an ID). Where a convention
   changed, the findings say so. Running a check and what it
   produces is on the page
   [Check conformance](check-conformance.md).
   You should now see the findings of each check, or that a check
   found nothing.

5. **Settling the findings.** The findings are settled one at a time,
   in a walkthrough (one item per message, each closed with your
   verdict). The `Action required` lines say what to do; the findings
   say where the project differs. Claude migrates on your word and
   only there: a finding you decline leaves the project as it is.
   You should now see each finding closed with your verdict, and the
   changes you accepted written into the project.

## What you have afterwards

- The engine at the version you pulled.
- Each project you named measured against the current conventions,
  with the migrations you accepted written into it.
- Each project you did not name untouched by the upgrade, and valid
  under the conventions it was written to.
- No record in any project of which engine version it was last
  measured against. The next upgrade measures it afresh, by the same
  two checks.

There is no migration tool. The whole migration path is the one
above: the pull, the `Action required` lines, the two checks and
Claude migrating on your word. This holds for every instance (one
installation of the forge), yours and a third party's alike.

## If something goes wrong

- **The engine was not pulled.** `/pull` pulls only a repository that
  is clean and behind. The engine with unsaved changes, or with a
  history that diverged from its remote, stops with one offer:
  `/save` first, or a merge by hand or through `/save`, which rebases
  your commits onto the remote. Nothing is pulled until you have done
  so. The states and their offers are on the page
  [Pull from the remote](pull-from-the-remote.md).
- **A check reports a project you do not want to change.** That is a
  fact reported, not a defect to chase: a finished or a dormant
  project remains valid under the conventions it was written to.
  Decline the findings and leave the project as it is.
- **The `Action required` lines were not shown.** They are shown
  after a pull of the engine, for the releases the pull crossed. If
  the engine was already up to date, there were no releases crossed
  and nothing to show; read `RELEASE-NOTES.md` yourself for anything
  older you have not yet acted on.

## A worked example

You keep two projects, `my-project` and `another-project`, and the
engine has moved since you last pulled.

```
You:     /pull
Claude:  The engine is behind its origin and clean; my-project and
         another-project are up to date. Pulling the engine.
         The engine moved forward by two releases:
           release <newer>: <its subject>
           release <older>: <its subject>
         Action required, from RELEASE-NOTES.md:
           <newer>: <what changed>. For you: <what to do in your
                    projects>
           <older>: <what changed>. For you: <what to do in your
                    projects>
         Shall I run /check light and /check project on my-project
         and on another-project?
You:     Only on my-project. another-project is finished; leave it.
Claude:  /check light my-project: two findings.
         /check project my-project: one finding.
         Shall we walk them through?
You:     Yes.
Claude:  <the first finding: what the convention now expects, where
         my-project differs, what the Action required line says to
         do>
You:     accept
Claude:  <the second finding ...>
You:     accept
Claude:  <the third finding ...>
You:     reject, that part of the project is closed.
Claude:  Two changes written into my-project; the third finding left
         as it stands.
```

Afterwards `my-project` carries the two migrations you accepted,
`another-project` is untouched and valid under the conventions it
was written to, and neither project records which engine version it
was measured against.

## See also

- [Pull from the remote](pull-from-the-remote.md): the pull itself.
- [Check conformance](check-conformance.md): running a check and
  settling its findings.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
