---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: e9d9e99b6f2be019
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository from `main`: it runs the checks,
regenerates the README and the release notes, writes the state render
and then saves with a release message. This page is for you, as the
person who orders a release, and says what it runs, renders and tags,
in what order, and what `--auto` decides on its own. In this page the
principal is whoever's thinking is being forged, so you; a ledger is
the state of a project, made from its documents when it is read; a
walkthrough is the way a list of items is settled one at a time; a
subagent is an isolated Claude run that sees nothing of the
conversation.

## When to use it

Use it when the settled sources of one repository are to be published
as a version. It is always one repository, never a sweep. The slug
`forge` means the whole: the engine and the forge's own project cloned
beside it, saved as two commits. See
[Projects and the engine](../about/projects-and-the-engine.md) for why
the engine lands in two commits.

## The command

```
/release my-project -m "one line of what changed" --tag v2
```

The arguments are `/release [slug] [-m "message"] [--tag name]
[--auto]`. All are optional.

- `slug` names the repository. Without it Claude asks which one.
- `-m` supplies the commit message. Without it Claude drafts it.
- `--tag` names a tag. Any tag other than the one of a major is your
  own request.
- `--auto` runs the release through and stops only at a serious
  thing (see below).

## What happens

1. **The branch and the origin are read.** A release runs on `main`
   only. On another branch it stops and tells you the branch the
   repository is on and how to get back. A repository behind or
   diverged from its origin is refused, with the offer of `/pull`.
   The reason is in
   [Persistence in git](../about/persistence-in-git.md). You should
   now see either the release going on or the branch or the origin
   named as the reason it stopped.
2. **The tests run, for the engine only.** Before any check or
   subagent runs, the tests run through `/test`, so that a broken
   script stops the release before it costs anything. A red test
   stops the release, with the failures as `/test` reports them. If
   pytest is not installed, Claude says that the tests did not run,
   and the release goes on only on your word. A project's release
   runs no tests. See [Run the tests](run-the-tests.md). You should
   now see the tests reported green, or the release stopped.
3. **The checks run and are settled.** For a project these are
   `light` and `project`. For the engine they are `engine` on the
   engine root, and `light` and `project` on the forge's own
   project. They are launched at once and awaited together, and the
   result is reported even when clean. Findings are settled by
   walkthrough. A finding you have not settled when you order the
   release to go on is parked by that word, said aloud, because the
   check is advisory. The checks run before the renders so that a fix
   of the walkthrough is already in what the renders are made from.
   See [Check conformance](check-conformance.md). You should now see
   the checks reported as passed, or every finding settled or parked.
4. **`critique essence` is offered once.** It is the lens that
   guards what a release publishes. Claude offers it in one sentence.
   It runs on your word only; on a no or on silence nothing runs. You
   should now see either the critique settled or the release going
   on.
5. **The age of the documentation is reported.** Claude reports the
   version in `docs/README.md` against the version of the intent. A
   repository without `docs/` has none, and that is no finding. Claude
   then offers `/document`. On your word it runs before the renders,
   so that the README reads the current index. On a no or on silence
   nothing runs. A release never regenerates the documentation on its
   own judgement. See
   [Generate the documentation](generate-the-documentation.md). You
   should now see the age reported and, if you said yes, the pages
   regenerated.
6. **The README and the release notes are regenerated.** Both are
   made through `/render`, always, with no test of staleness, and
   they are launched at once and awaited together. Claude reports a
   short summary of what materially changed in them, and you rule on
   that change before the commit. Other renders are never
   regenerated here. A project whose recipe is missing is reported
   and released without that render. See
   [Renders and recipes](../about/renders-and-recipes.md) for why
   these two are renders. You should now see the summary of what
   changed.
7. **The state render is written.** The ledger is written as the
   tracked file `renders/state.md`, so that the state is on the
   remote. For the engine the file is in the forge's own project. You
   should now see `renders/state.md` written.
8. **The save runs.** Claude runs `/save --quick`, without a second
   light check, because step 3 ran one and nothing since has changed
   what it reads. The message is `release <intent version>: <one
   line>`, drafted from the records of the intent's history since the
   last release, unless you supplied `-m`. For a library the version
   is left out and the line says what changed. At an integer version,
   which is an approved major, the tag `v<major>` is proposed and
   taken on your word. Before proposing it for the forge's own
   intent, Claude names what that intent asks a major to pass. This is
   a reminder, never a gate. See
   [Versioning and history](../about/versioning-and-history.md) for
   what a major approves, and [Save your work](save-your-work.md) for
   the save. You should now see the commit made, and the tag if you
   agreed to one.

## What `--auto` decides

`--auto` runs the release through and stops only at a serious thing.
Nothing is parked on your behalf: what it cannot settle stays open,
and the release waits for your word.

- **Before anything runs**, it asks once whether the documentation
  runs. The default is yes, and the models and the number of pages are
  said before the writers are launched.
- **It stops** at a branch that is not `main`, at a repository behind
  or diverged, at a red test and at a missing pytest.
- **The checks and every run of subagents** run without asking. The
  model and the size are said as information.
- **A finding is fixed and recorded by Claude** when its fix lies in
  the operating layer or in bookkeeping and changes no position and no
  rule's meaning. It is listed in the one proposition before the
  save.
- **A finding stops the release** when its severity is high, when its
  fix would change a position or a rule's meaning, or when the report
  calls it a decision.
- **`critique essence`** is neither offered nor run.
- **At the renders** the one stop is a hit of the instance-fact scan
  that the released version did not already carry. A hit the released
  version carried stands as before. The change in the regenerated files
  is not ruled on here but carried into the proposition before the
  save.
- **Before the save** it stops once with one proposition. The
  proposition holds what Claude fixed on its own, what materially
  changed in the regenerated files and the drafted message. The push
  waits for your word.
- **The tag of a major** is never taken by `--auto`. The release stops
  before it and asks.

## What you have afterwards

- The README and the release notes regenerated from the settled
  sources.
- `renders/state.md`, the ledger as a tracked file.
- One commit per repository released, with the message `release
  <intent version>: <one line>`, and the tag `v<major>` where you
  agreed to one.

## If something goes wrong

- **Another branch.** The release stops and names the branch. Save,
  then return with `python scripts/forge-branch.py <slug> main`.
  Merging a branch into `main` is done by hand or by merge request,
  never by this command.
- **Behind or diverged from the origin.** The release is refused and
  `/pull` is offered. The reason is that the renders a release makes
  are taken as `ours` at a merge, and that turns round in the rebase
  of the save.
- **A red test.** The release stops with the failures as `/test`
  reports them. Fix them and release again.
- **Pytest not installed.** Claude says the tests did not run. The
  release goes on only on your word, and with `--auto` it stops.
- **Findings you do not settle.** Ordering the release to go on parks
  them. The check is advisory, so you may order the release at any
  moment.
- **A missing recipe.** The project is released without that render,
  and the missing recipe is reported as a finding of the check.

## A worked example

You have finished a round of work on a project with the slug
`my-project` and want to release it.

1. You type `/release my-project`.
2. Claude finds the repository on `main` and level with its origin.
   It runs `light` and `project` and reports them clean. You see the
   checks passed.
3. Claude offers `critique essence` in one sentence. You say no, and
   nothing runs.
4. Claude reports that `docs/README.md` is one version behind the
   intent and offers `/document`. You say yes, and the pages are
   regenerated.
5. Claude regenerates the README and the release notes and reports a
   short summary of what changed. You accept it.
6. Claude writes `renders/state.md`.
7. Claude runs `/save --quick` with the message `release <intent
   version>: <one line>`. The intent version is an integer, so Claude
   proposes the tag `v<major>`. You agree, and the commit and the tag
   are made.

With `--auto` the same release asks only whether the documentation
runs, then stops once before the save with one proposition. It does
not offer `critique essence`, and it stops before the tag.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Run the tests](run-the-tests.md): the tests a release of the
  engine runs first.
- [Check conformance](check-conformance.md): the checks and how their
  findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the
  README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the
  command the release offers and, with `--auto`, asks about once.
- [Versioning and history](../about/versioning-and-history.md): what a
  major approves.
- [Persistence in git](../about/persistence-in-git.md): why there are
  two doors and two speeds, and why a release is made on `main` only.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  a release of the engine lands in two commits.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
