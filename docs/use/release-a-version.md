---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: bb4bcfe3c39afdb9
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository: it runs the checks, regenerates the README and the release notes, writes the state render and saves with a release message. This page is for you as the principal (the person whose thinking is forged and who decides what is published) when a repository is ready to be cut.

## When to use it

Use it when the repository stands on `main` and you want to publish its current state. A release is always one repository, never a sweep. Without a slug, Claude asks which repository is meant. The slug `forge` means the engine.

Use [Save your work](save-your-work.md) instead for a commit on any branch without the release steps. The reason for two doors and two speeds, and for releasing on `main` only, is given in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/release [slug] [-m "message"] [--tag name] [--auto]
```

For example, `/release my-project`.

- `-m "message"`: your own commit message instead of the drafted one.
- `--tag name`: a tag of your own choosing, as `/save` has it.
- `--auto`: run the release through and stop only at a serious thing (below).

## What happens

1. Claude reads the state of the repository through `scripts/forge-status.py --remote`.
   - A release runs on `main` only. On any other branch Claude stops and reports the branch the repository is on and the way back (`python scripts/forge-branch.py <slug> main`, after saving).
   - A repository behind its origin, or diverged from it, is refused with the offer of `/pull`. The reason is that the renders a release makes are taken as `ours` at a merge, and that turns round in the rebase of the save.
   - Merging a branch into `main` is never done by `/release`.
   - `--auto` stops here as any release does.

   You should now see the branch confirmed as `main` and the repository level with its origin, or a stop that names the way back.

2. For the engine only, Claude runs the tests through `/test` before any check or agent runs, so that a broken script stops the release before it costs anything. See [Run the tests](run-the-tests.md). A project's release runs no tests.
   - A red test stops the release. The failures are reported as `/test` reports them, and the release goes back to the fix.
   - If pytest is not installed, Claude says the tests did not run and goes on only on your word.

   You should now see the tests pass, or the failures listed and the release stopped.

3. Claude runs the checks and reports the result, even when clean.
   - A project: `light` and `project`.
   - The engine: `engine` on the engine root, and `light` and `project` on its own project.

   The checks are launched at once and awaited together. Findings are settled by walkthrough (one item per message, each closed with the verdict line) as described in [Check conformance](check-conformance.md). Nothing is fixed silently. The check is advisory: you may order the release to go on at any moment, and a finding you have not settled when you do is parked by that word, said aloud. The checks run before the renders so that a fix from the walkthrough is already in what the renders are made from.

   You should now see a statement that the checks passed, or each finding settled or parked.

4. Claude offers `/critique essence` once, in one sentence. The lens guards what a release publishes: the drift of the chain. On your word it runs and its findings are settled by walkthrough. On your no, or silence, nothing runs, because no reviewer runs at a release on Claude's own judgement.

   You should now see either the critique settled or the release going on without it.

5. Claude reports the age of the documentation: the `version` in the front-matter of the repository's `docs/README.md` against the intent's version. A repository without `docs/` has none, and that is no finding. Claude then offers `/document` in one sentence. On your word it runs before the renders, so that the release carries current pages and the README reads the current index. On your no, or silence, nothing runs. A release by hand never regenerates the documentation on its own judgement. See [Generate the documentation](generate-the-documentation.md).

   You should now see the age of the documentation stated and, if you agreed, the pages regenerated.

6. Once the findings are settled and the documentation stands, Claude regenerates the README and the release notes from their recipes, always through the `/render` procedure and without a staleness test. Both are launched at once and awaited together. They are renders, never edited by hand: see [Renders and recipes](../about/renders-and-recipes.md). Claude reports the steps with a short summary of what materially changed in the regenerated files, and you rule on that change before the commit. A project whose recipe is missing is reported and released without that render. Other renders are never regenerated here.

   You should now see the README and the release notes regenerated, with the summary of what changed.

7. Claude writes the state render: the ledger (the single source of truth for state, made at read time) written as the tracked file `renders/state.md`, for the engine `projects/forge/renders/state.md`. It is made only on `main`, so that the state is on the remote where it is wanted.

   You should now see `renders/state.md` written.

8. Claude runs `/save --quick` for this repository: the same save as in [Save your work](save-your-work.md), without a second `light` check, since step 3 ran it and nothing made since is read by it.
   - The commit message is `release <intent version>: <one line>`. The line summarises the rounds since the last release, from the history of the intent. A message given with `-m` is used instead. For a library the version is omitted and the line describes what changed.
   - When the intent's version is an integer (an approved major, see [Versioning and history](../about/versioning-and-history.md)), Claude proposes the tag `v<major>` and takes it on your word. Before proposing the tag of a major of the forge's own intent, Claude names what that intent asks a major to pass, as a reminder and never as a gate.
   - Any other tag is your request, as `/save` has it.

   You should now see the commit made and pushed with the release message and, at a major you approved, the tag.

## What you have afterwards

- The checks run, their findings settled or parked.
- The documentation current if you chose to regenerate it.
- The README, the release notes and `renders/state.md` regenerated from the settled sources.
- One commit with the release message, pushed, and the tag `v<major>` at an approved major.

## With `--auto`

`--auto` runs the whole release through and stops only at a serious thing. Nothing is parked on your behalf: what `--auto` cannot settle stays open, and the release waits for your word.

- Before anything runs, Claude asks once whether the documentation runs. The default is yes. On yes it runs as a part of the release, and the models and the number of pages are said before the writers are launched.
- It stops at a red test and at a missing pytest alike, since each is yours to decide.
- The checks and every run of agents run without asking. The model and the size of each run are said as information.
- A finding whose fix lies in the operating layer or in bookkeeping, and changes no position and no rule's meaning, is fixed and recorded by Claude without a walkthrough.
- A finding of severity high, one that would change a position or a rule's meaning, or one the report calls a decision, stops the release and is put to you.
- `critique essence` is neither offered nor run.
- The regenerated files are taken as they came, with no summary put to you. The one stop is a hit of the instance-fact scan that the released version did not already carry. A hit it already carried stands as before.
- The drafted message is used without confirmation and said aloud in the report.
- The tag of a major is never taken by `--auto`. The release stops before it and asks.

## If something goes wrong

- Another branch than `main`: the release stops and names the branch and the way back, `python scripts/forge-branch.py <slug> main`, after saving.
- Behind or diverged from the origin: the release is refused and `/pull` is offered.
- A red test (engine): the release stops with the failures as `/test` reports them. Fix them and release again.
- pytest missing (engine): Claude says the tests did not run. The release goes on only on your word, and with `--auto` it stops.
- Findings you do not want to settle now: order the release to go on, and they are parked by that word.
- A project whose recipe for the README or the release notes is missing: this is reported as a finding and the release goes on without that render.

## A worked example

You have finished a round of work on `my-project`, and the repository is on `main` and level with its origin.

```
/release my-project
```

1. Claude confirms `main` and a repository level with its origin.
2. It runs `light` and `project` and reports that the checks passed.
3. It offers `/critique essence` in one sentence. You answer no, and nothing runs.
4. It reports the documentation as older than the intent and offers `/document`. You say yes, and the pages are regenerated.
5. It regenerates the README and the release notes and summarises what changed. You accept the change.
6. It writes `renders/state.md`.
7. It runs `/save --quick` with the message `release <intent version>: <one line>`. The intent's version is an integer, so it proposes the tag `v<major>`. You agree, and the commit is pushed with the tag.

The same release with `--auto` asks the one question about the documentation, then runs through without the offer of the critique or the summary, and stops before the tag to ask.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Run the tests](run-the-tests.md): the tests a release of the engine runs first.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers and, with `--auto`, asks about once.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds, and why a release is made on `main` only.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
