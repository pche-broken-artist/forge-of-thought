---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: ee6d3ac3033171e9
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository from its `main` branch: it runs the checks, regenerates the README and the release notes, reports the age of the documentation and then saves with a release message and, at an approved major version, a tag. This page is for you when a round of work is settled and you want to publish it.

The principal is whoever's thinking is being forged, and Claude is the machine that works with the principal. A render is an output generated from the documents of a project, never edited by hand. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the work on `main` is saved and you want the project's published state brought up to date. A release is always one repository, never a sweep. The repository is named by its slug, and `forge` means the engine itself. Without a slug, Claude asks which repository.

## The command

```
/release my-project -m "release 2.0: the first approved version" --tag v2
```

The full form is `/release [slug] [-m "message"] [--tag name]`. Both options are optional. Without `-m`, Claude writes the message itself.

## What happens

1. Claude reads the state of the repository. A release runs on `main` only. On any other branch it stops, says which branch the repository is on and how to get back (`python scripts/forge-branch.py <slug> main`, after saving). Merging a branch into `main` is not done by this command.

   You should now see the repository confirmed to be on `main`, or the stop with the branch named.

2. Claude runs the checks and reports the result, even when it is clean. For a project these are `light` and `project`. For the engine these are `engine` on the engine root, and `light` and `project` on its own project. They run together and Claude waits for all of them.

   You should now see either a statement that the checks passed, or a list of findings. Findings are settled one by one, as described in [Check conformance](check-conformance.md). A finding may be parked, and the release goes on. Claude never fixes a finding silently. The checks run before the renders so that a fix made while settling them is already in what the renders are made from.

3. Claude offers `/critique essence` once, in one sentence. That lens guards what a release publishes, which is the drift of the chain of documents. If you say yes, it runs and its findings are settled before the release goes on. If you say no, or say nothing, no reviewer runs.

   You should now see either the critique settled, or the release moving on without it.

4. Once the findings are settled, Claude regenerates the README and the release notes from their recipes, always, with no test of whether they are out of date. Both go through `/render` and are made together. Other renders are not regenerated here. A project whose recipe is missing is reported as a finding and released without that render. Why these two files are renders is explained in [Renders and recipes](../about/renders-and-recipes.md).

   You should now see the two files regenerated, with a short summary of what materially changed in them. You rule on that change before anything is committed.

5. Claude reports the age of the documentation. It compares the `version` in the front-matter of the repository's `docs/README.md` with the version of the intent. A repository without `docs/` has no age to report, and that is no finding. Claude then offers `/document` in one sentence. If you say yes, the documentation is regenerated before the save, as described in [Generate the documentation](generate-the-documentation.md), so that the release carries current pages. If you say no, or say nothing, nothing runs. The release never regenerates the documentation on its own.

   You should now see the age of the documentation, and the offer.

6. Claude saves the repository, as described in [Save your work](save-your-work.md). The commit message is `release <intent version>: <one line>`. The line summarises the rounds since the last release and is taken from the history of the intent. If you gave `-m`, your message is used. For a library, which has no intent, the version is left out and the line says what changed.

   You should now see the commit and push reported as `/save` reports them.

7. When the version of the intent is an integer, which is an approved major, Claude proposes the tag `v<major>`, and it is taken only on your word. Before proposing the tag of a major of the forge's own intent, Claude names what that intent asks a major to pass. That is a reminder, never a gate. What a major approves is in [Versioning and history](../about/versioning-and-history.md). Any other tag is created only when you ask for it.

   You should now see the tag proposed, or no tag at a version that is not an integer.

The check is advisory. You may order the release to go on at any moment, whatever the findings. Findings you have not settled are parked by that word, and Claude says so aloud.

## What you have afterwards

- The checks run and their findings settled or parked.
- The README and the release notes regenerated from the settled sources.
- The age of the documentation reported, and the documentation regenerated if you said yes.
- One commit with the release message, pushed, and the tag `v<major>` at an approved major if you took it.

## If something goes wrong

- On a branch other than `main` the release stops. Save, switch back with `python scripts/forge-branch.py <slug> main`, and run `/release` again.
- With no slug, Claude asks which repository. Give one.
- A missing recipe for the README or the release notes is reported as a finding, and the project is released without that render.
- Unsettled findings do not block the release. They are parked when you order it to go on.

## A worked example

You have finished a round on a project with the slug `my-project`, and its intent is at an integer version.

1. You type `/release my-project`.
2. Claude confirms the repository is on `main`, runs `light` and `project`, and reports that the checks passed.
3. Claude offers `/critique essence`. You say no, and nothing runs.
4. Claude regenerates the README and the release notes and summarises what changed in each. You accept the change.
5. Claude reports that the documentation is older than the intent and offers `/document`. You say yes, and the pages are regenerated.
6. Claude saves with a message of the form `release <intent version>: <one line>`, and proposes the tag `v<major>`. You say yes, and the commit and the tag are pushed.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
