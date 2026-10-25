---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 50d3deeccab14608
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository from `main`: it runs the checks, regenerates the README and the release notes, writes the state render, offers the documentation, and then saves with a release message and, at an approved major, a tag. This page is for you, the principal (the person whose thinking is being forged), when a round of work is settled and you want it published.

## When to use it

Use it when the repository is on `main`, its work is saved, and you want the README, the release notes and the state published together with a release commit. A release is always one repository, never a sweep over several. Without a slug, Claude asks which repository you mean.

## The command

```
/release [slug] [-m "message"] [--tag name]
```

For example, for a project called `my-project`:

```
/release my-project -m "release 2.0: the first approved version"
```

The slug `forge` means the engine itself. Without `-m`, Claude drafts the message. `--tag` names a tag of your own choice; it is not needed for the tag of a major (see step 7).

## What happens

1. **The state is read.** Claude reads the state of the repository against its origin (the remote copy) through its script.
   - A release runs on `main` only. On any other branch Claude stops, names the branch the repository is on and gives the way back: save, then switch with `python scripts/forge-branch.py <slug> main`.
   - A repository that is behind its origin, or has diverged from it, is refused with the offer of `/pull`. The renders a release makes would otherwise be taken from your side at a merge and the next save would turn that round.
   - Merging a branch into `main` is not done by this command. It is done in git, by hand or by merge request.

   You should now see the repository named as being on `main` and in step with its origin, or a stop that says why not.

2. **The checks run.** A project gets the checks `light` and `project`. The engine gets `engine` on the engine root, and `light` and `project` on its own project. They are launched together and awaited together.
   - Claude reports the result always, even when it is clean.
   - Findings are settled by walkthrough (one item at a time, each closed with a verdict of accept, modify, question, reject or park). A finding may be parked and the release goes on. Claude fixes nothing silently.
   - The checks run before the renders so that a fix made in the walkthrough is already in what the renders are made from.

   You should now see "the checks passed", or every finding settled or parked. The details are on [Check conformance](check-conformance.md).

3. **`critique essence` is offered once.** Claude offers it in one sentence as the lens that guards what a release publishes. On your word it runs and its findings are settled by walkthrough before the release goes on. On your no, or on silence, nothing runs. No reviewer runs at a release on Claude's own judgement.

   You should now see either the critique's findings settled or the release moving on without it.

4. **The README and the release notes are regenerated.** This happens always, with no test of whether they are stale, and only once the findings are settled. Both go through `/render`, are launched together and are awaited together. Claude reports the steps and a short summary of what materially changed in the two files. You rule on that change before the commit.
   - Other renders are not regenerated here. Whether they are stale is shown by the state map of `/forge`.
   - A project whose recipe for either file is missing has that reported and is released without that render.
   - Why the README and the release notes are renders is explained on [Renders and recipes](../about/renders-and-recipes.md).

   You should now see the two files regenerated and a summary of what changed in them.

5. **The state render is written.** Claude writes the ledger (the table of what the repository holds and the state of each item, made at read time) as the tracked file `renders/state.md`. For the engine, this is `projects/forge/renders/state.md`. It is made on `main` only, so that the state is on the remote where it is wanted.

   You should now see `renders/state.md` written.

6. **The age of the documentation is reported.** Claude compares the `version` in the front-matter of the repository's `docs/README.md` with the version of the intent and offers `/document` in one sentence. A repository without `docs/` has no age to report, and that is no finding.
   - On your word `/document` runs before the save, so that the release carries current pages. See [Generate the documentation](generate-the-documentation.md).
   - On your no, or on silence, nothing runs. The release never regenerates the documentation on its own.

   You should now see the documentation's age stated against the intent's version.

7. **`/save` runs.** The release ends with the save of this repository, described on [Save your work](save-your-work.md), with two things decided here.
   - The commit message is `release <intent version>: <one line>`. The line summarises the rounds since the last release, taken from the intent's history. If you gave `-m`, your message is used. For a library, whose history is git, the version is left out and the line says what changed.
   - When the intent's version is an integer (an approved major), Claude proposes the tag `v<major>` and takes it on your word. For the forge's own intent, Claude first names what that intent asks a major to pass. This is a reminder, never a gate. What a major approves is explained on [Versioning and history](../about/versioning-and-history.md). Any other tag is your request, as `/save` has it.

   You should now see the release commit saved and, if you agreed, the tag.

## What you have afterwards

- The checks reported, and every finding settled or parked.
- The README and the release notes regenerated from the settled sources.
- The state render `renders/state.md` written and tracked.
- The documentation current, if you asked for `/document`.
- A release commit with the message `release <intent version>: <one line>`, and the tag `v<major>` at an approved major if you agreed to it.

## If something goes wrong

- **The repository is on another branch.** The release stops. Save, then switch back with `python scripts/forge-branch.py <slug> main`.
- **The repository is behind or has diverged from its origin.** The release is refused and `/pull` is offered.
- **A finding is not settled when you order the release to go on.** Your word parks it, and Claude says so aloud. The check is advisory: you may order the release at any moment, whatever the findings.
- **A recipe for the README or the release notes is missing.** Claude reports it, and the release goes on without that render.

## A worked example

A project `my-project` has settled its intent at an integer version and is on `main`.

1. You type `/release my-project`.
2. Claude reads the state: on `main`, level with its origin.
3. `light` and `project` run together and report two findings. You settle one by accepting it and park the other. Claude says that the checks are settled.
4. Claude offers `critique essence` in one sentence. You say no, and nothing runs.
5. The README and the release notes are regenerated through `/render`. Claude summarises what changed and you accept the change.
6. Claude writes `renders/state.md`.
7. Claude reports that the documentation is one version behind the intent and offers `/document`. You say yes, and it runs.
8. Claude saves with the message `release 2.0: <one line>` and proposes the tag `v2`. You agree, and the tag is made.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
