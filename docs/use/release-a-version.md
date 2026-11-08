---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: ffdf3cbfa506c3a7
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` is the command that publishes one repository: it runs the
tests and the checks, regenerates the README and the release notes,
writes the state render and saves with a release message and, at an
approved major, a tag. This page is for you, the principal (the person
whose thinking is forged), when you want to put out a version.

## When to use it

Use it when the work of a round is settled and you want it on the
remote as a release. A release is made from `main` only, and it is one
repository at a time, never a sweep. The ordinary save between
releases is [Save your work](save-your-work.md). The reasons for the
two doors and for `main` only are in
[Persistence in git](../about/persistence-in-git.md).

## The command

```
/release <slug> -m "<message>" --tag <name> --auto
```

Only the slug is needed. The other parts are optional:

- `-m "message"` replaces the message Claude would draft.
- `--tag name` asks for a tag of your own naming. At an approved major
  version the tag `v<major>` is proposed anyway.
- `--auto` runs the release through and stops only at a serious thing
  (see below).

Without a slug Claude asks which repository. The word `forge` names the
whole: the engine and the forge's own project cloned beside it, saved
as two commits. Why the engine lands in two commits is explained in
[Projects and the engine](../about/projects-and-the-engine.md).

## What happens

1. Claude reads the state of the repository and its remote. You should
   now see that the repository is on `main` and level with its origin.
   On any other branch the release stops and names the branch and the
   way back (the branch script, after you have saved). A repository
   behind its origin or diverged from it is refused, with the offer of
   `/pull`. `--auto` stops here as any release does.
2. For the engine only, Claude runs the tests through `/test` before any
   check or agent runs (see [Run the tests](run-the-tests.md)). You
   should now see a green result. A red test stops the release, with the
   failures as `/test` reports them. If pytest is missing, Claude says
   that the tests did not run, and goes on only on your word. A
   project's release runs no tests.
3. Claude runs the checks and reports the result, even when clean. For a
   project these are `light` and `project`. For the engine they are
   `engine` on the engine root, and `light` and `project` on the forge's
   own project. You should now see either "the checks passed" or the
   findings, which are settled one by one by walkthrough (see
   [Check conformance](check-conformance.md)). A finding you have not
   settled when you order the release to go on is parked by that word,
   said aloud. The check is advisory, so you may order the release at
   any moment.
4. Claude offers `/critique essence` once, in one sentence. You should
   now see the offer. On your word it runs and its findings are settled
   by walkthrough. On your no, or silence, nothing runs.
5. Claude reports the age of the documentation, the version of
   `docs/README.md` against the intent's version, and offers
   `/document` (see
   [Generate the documentation](generate-the-documentation.md)). A
   repository without `docs/` has no age, and that is no finding. On
   your word the documentation is generated before the renders, so that
   the README reads the current index. On your no, or silence, nothing
   runs. A release by hand never regenerates the documentation on its
   own judgement.
6. Claude regenerates the README and the release notes through
   `/render`, always, with no test of staleness. You should now see the
   two files and a short summary of what materially changed in them. You
   rule on that change before the commit. Other renders are never
   regenerated here. Why these two are renders is in
   [Renders and recipes](../about/renders-and-recipes.md).
7. Claude writes the state render: the ledger as the tracked file
   `renders/state.md`, in the project's repository (for the engine, in
   the forge's own project). You should now see that file written.
8. Claude runs `/save --quick` (see [Save your work](save-your-work.md)),
   without a second light check, since step 3 ran it already. The
   message is `release <intent version>: <one line>`, unless you gave
   `-m`. The line sums up the rounds since the last release. At an
   integer version the tag `v<major>` is proposed and taken on your
   word. For the forge's own intent, Claude first names what that
   intent asks a major to pass, as a reminder and never as a gate. What
   a major approves is in
   [Versioning and history](../about/versioning-and-history.md). You
   should now see the commit and, if you agreed, the tag on the remote.

## What `--auto` decides on its own

With `--auto` the release runs through. Claude asks one question before
anything runs: whether the documentation runs, the default being yes.

It stops at:

- a red test, and a missing pytest alike
- a finding of severity high
- a finding whose fix would change a position or a rule's meaning
- a finding the report calls a decision
- a hit of the instance-fact scan that the released version did not
  already carry
- the proposition before the save
- the tag of a major

It decides without asking:

- The checks and every run of agents run without asking. The model and
  the size are said as information.
- A finding whose fix lies in the operating layer or in bookkeeping, and
  changes no position and no rule's meaning, is fixed and recorded by
  Claude.
- `critique essence` is neither offered nor run.
- The delta of the regenerated files is not ruled on at the renders. It
  is carried into the proposition before the save.

Before the save Claude stops once with one proposition. It carries what
Claude fixed on its own, what materially changed in the regenerated
files and the drafted message. The push waits for your word. The tag of
a major is never taken by `--auto`: the release stops before it and
asks. Nothing is parked on your behalf.

## What you have afterwards

- The tests and the checks have run, with their findings settled or
  parked.
- The README and the release notes are regenerated, and the state render
  is written.
- One commit with the release message, two for `forge`, and the tag at
  an approved major.

## If something goes wrong

- The repository is not on `main`: the release stops and names the
  branch and the way back.
- The repository is behind or diverged: the release is refused and
  `/pull` is offered.
- A test is red: the release stops, you fix it, and you start again.
- Pytest is not installed: Claude says so, and the release goes on only
  on your word. With `--auto` it stops.
- A check finds something: you settle it by walkthrough, or park it by
  ordering the release on.
- A recipe of the README or the release notes is missing: that is a
  finding of the check, and the repository is released without the
  render.

## A worked example

You have finished a round on a project with the placeholder slug
`my-project`, and its intent is at an integer version.

```
/release my-project
```

Claude finds the repository on `main` and level with its origin, runs
`light` and `project`, and reports that the checks passed. You decline
`critique essence`. It reports the documentation one version behind the
intent and offers `/document`. You agree, and the pages are
regenerated. Claude then regenerates the README and the release notes
and shows a summary of what changed. You accept it. It writes
`renders/state.md`, then saves with the message
`release <intent version>: <one line>` and proposes the tag
`v<major>`. You agree, and the commit and the tag go to the remote.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Run the tests](run-the-tests.md): the tests a release of the engine
  runs first.
- [Check conformance](check-conformance.md): the checks and how their
  findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README
  and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the
  command the release offers and, with `--auto`, asks about once.
- [Versioning and history](../about/versioning-and-history.md): what a
  major approves.
- [Persistence in git](../about/persistence-in-git.md): why there are
  two doors and two speeds, and why a release is made on `main` only.
- [Projects and the engine](../about/projects-and-the-engine.md): why a
  release of the engine lands in two commits.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
