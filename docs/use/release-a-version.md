---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 099077394d97f224
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

This page shows what `/release` does when you release one repository, and in what order. It is for you as the person who runs it: the principal (whoever's thinking is being forged), who alone decides what is published.

A release is always one repository, never a sweep. It runs the checks, regenerates the README and the release notes, writes the state render, offers the documentation and then saves with a release message and, at an approved major version, a tag.

## When to use it

Use it when the repository's sources are settled and you want a released state on `main`, with a current README, release notes and state render. Use [Save your work](save-your-work.md) instead for an ordinary save on any branch.

## The command

```
/release [slug] [-m "message"] [--tag name]
```

For example, to release a project called `my-project`:

```
/release my-project
```

The slug names the repository. The slug `forge` means the engine itself. Without a slug, Claude asks which repository. With `-m`, the message you give replaces the one Claude would draft. With `--tag`, you name a tag of your own.

## What happens

1. Claude reads the state of the repository with its status script. A release runs on `main` only.
   - On any other branch, Claude stops, names the branch and tells you the way back: save, then switch to `main` with the branch script.
   - A repository behind or diverged from its origin is refused, with the offer of `/pull`.

   You should now see either the state of a repository on `main` that is level with its origin, or a refusal that names what to do.

2. Claude runs the checks over the sources, always, even when they are clean.
   - A project gets the `light` and `project` checks.
   - The engine gets the `engine` check on the engine root, and `light` and `project` on its own project.

   The checks run at once and are awaited together. Findings are settled by a walkthrough: one item per message, each closed with the verdict line. A finding may be parked, and the release goes on. Nothing is fixed silently. You should now see either the statement that the checks passed or each finding put to you. How the checks work and how a finding is settled is on [Check conformance](check-conformance.md).

3. Claude offers `/critique essence` once, in one sentence. It is the lens that guards what a release publishes. On your word it runs and its findings are settled by walkthrough. On your no, or your silence, nothing runs. You should now see the offer, and a report only if you accepted.

4. Once the findings are settled, Claude regenerates the README and the release notes from their recipes through `/render`. This is unconditional, with no test whether they are stale. The two renders run at once. Why these files are renders is on [Renders and recipes](../about/renders-and-recipes.md). You should now see a report of the steps with a short summary of what materially changed in the two files. You rule on that change before the commit.

   Other renders are not regenerated here. A project whose recipe is missing is reported, and released without that render.

5. Claude then writes the state render: the ledger (the single record of state, made when it is read) as the tracked file `renders/state.md`. For the engine it is the file in its own project. It is made only on `main`, so that the state is on the remote. You should now see `renders/state.md` written.

6. Claude reports the age of the documentation: the version in the front-matter of the repository's `docs/README.md` against the intent's version. A repository without `docs/` has none, and that is no finding. Claude offers `/document` in one sentence. On your word it runs before the save, so that the release carries current pages. On your no, or silence, nothing runs. A release never regenerates the documentation on its own. The command is on [Generate the documentation](generate-the-documentation.md). You should now see the age reported and the offer made.

7. Claude runs `/save` for the repository. The save itself is on [Save your work](save-your-work.md). Two things are decided by the release:
   - The commit message is `release <intent version>: <one line>`. The line sums up the rounds since the last release, from the records of the intent's history, unless you gave `-m`. For a library the version is left out, and the line says what changed.
   - When the intent's version is an integer, an approved major, Claude proposes the tag `v<major>` and takes it on your word. For the engine's own intent, Claude first names what that intent asks a major to pass. This is a reminder, never a gate. What a major approves is on [Versioning and history](../about/versioning-and-history.md). Any other tag is your own request.

   You should now see the commit and push reported, and the tag if you agreed to it.

The check is advisory. You may order the release at any moment regardless of findings. A finding you have not settled when you say so is parked by that word, said aloud.

## What you have afterwards

- the checks run and their findings settled or parked
- the README and the release notes regenerated, with the change summarised to you
- `renders/state.md` written
- the documentation current, if you accepted `/document`
- a commit with the release message, pushed
- the tag `v<major>`, if the version is an integer and you agreed

## If something goes wrong

- Not on `main`: the release stops. Save your work, switch back with `python scripts/forge-branch.py <slug> main`, then run it again.
- Behind or diverged from the origin: the release is refused and Claude offers `/pull`. The renders a release makes are taken as `ours` at a merge, which is why the release will not run on a repository that has not caught up.
- Merging a branch into `main` is not done by `/release`. That is git's business, by hand or by merge request.
- A recipe is missing in a project: the gap is reported as a finding, and the release goes on without that render.
- Findings you do not want to settle now: park them, or order the release to go on.

## A worked example

You have a project `my-project` on `main`, level with its origin.

1. You type `/release my-project`.
2. Claude reports the repository is on `main` and current with its origin.
3. Claude runs `light` and `project`, and reports one finding. You settle it in a walkthrough with `accept`, and park nothing.
4. Claude offers `/critique essence`. You answer no, and nothing runs.
5. Claude regenerates the README and the release notes and tells you that the README gained a section and the release notes one entry. You accept the change.
6. Claude writes `renders/state.md`, reports that the documentation is one version behind the intent, and offers `/document`. You say no.
7. The intent stands at an integer version. Claude drafts `release <version>: <one line>`, proposes the tag `v<major>`, and you agree. Claude saves, pushes and tags.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
