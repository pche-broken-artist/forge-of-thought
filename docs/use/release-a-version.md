---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 0f62d93f65a9eec0
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

This page is for you when a repository, a project or the engine, has reached a point worth publishing. `/release` checks one repository, regenerates its README and release notes, and then saves it with a release message and, at an approved major version, a tag.

## When to use it

- Use it when the work on `main` is ready to be published as a version.
- A release is always one repository, never a sweep. Name the repository by its slug (its short name); `forge` means the engine. Without a slug, Claude asks which repository you mean.
- For a plain save with no checks and no renders, use [Save your work](save-your-work.md).

## The command

```
/release my-project -m "release 2.1: the scope is cut to two layers"
```

The slug, `-m` and `--tag` are all optional. Without `-m`, Claude drafts the message itself. A tag other than the one a major proposes is your own request through `--tag`.

## What happens

The release runs on `main` only. Each step below follows the one before it, and the order is fixed.

1. Claude reads the state of the repository. On any other branch it stops, names the branch and says how to get back to `main`.
   You should now see the repository on `main`, or a stop naming the branch you are on.
2. Claude runs the checks and reports the result, even when it is clean. For a project these are `light` and `project`. For the engine they are `engine` on the engine itself, and `light` and `project` on its own project. They are launched at once and awaited together. Findings are settled by walkthrough, that is one item per message with the verdicts accept, modify, reject or park. A finding may be parked and the release goes on. The checks run before the renders so that a fix made in the walkthrough is already in what the renders read. See [Check conformance](check-conformance.md).
   You should now see either the statement that the checks passed or each finding put to you in turn.
3. Claude offers the `critique essence` review once, in one sentence. It guards what a release publishes against drift of the chain. On your word it runs and its findings are settled by walkthrough. On your no, or your silence, nothing runs.
   You should now see either the review's findings or the next step, as you chose.
4. Claude regenerates the README and the release notes from their recipes, unconditionally and with no test of staleness, through `/render`. The two renders are launched at once and awaited together. A recipe that is missing is reported as a finding and the repository is released without that render. Other renders are not regenerated here. See [Renders and recipes](../about/renders-and-recipes.md).
   You should now see a short summary of what materially changed in the regenerated files. You rule on that change before anything is committed.
5. Claude reports the age of the documentation: the version in `docs/README.md` against the version of the intent. A repository without `docs/` has none, and that is no finding. Claude offers `/document` in one sentence. On your word it runs before the save, so that the release carries current pages. On your no, or silence, nothing runs. The release never regenerates the documentation on its own. See [Generate the documentation](generate-the-documentation.md).
   You should now see the documentation's version beside the intent's, or the statement that there is no documentation.
6. Claude runs `/save` for the repository. The commit message is `release <intent version>: <one line>`, where the line sums up the rounds since the last release, taken from the intent's history. Your `-m` replaces it. For a library, whose history is git, the version is left out and the line says what changed. When the intent's version is an integer, an approved major, Claude proposes the tag `v<major>` and takes it only on your word. If the repository is the engine, Claude first names what the forge's own intent asks a major to pass. That is a reminder on your word, never a gate. See [Versioning and history](../about/versioning-and-history.md) for what a major approves and what its test attests, and [Save your work](save-your-work.md) for the save itself.
   You should now see the commit and push reported, and the tag where you agreed to one.

## What you have afterwards

- The settled checks, with any parked findings recorded as parked.
- A README and release notes regenerated from the current sources.
- Documentation as current as you chose to make it.
- A commit on `main` with the release message, pushed, and the tag at an approved major.

## If something goes wrong

- Not on `main`: the release stops. Save your work, then switch back with `python scripts/forge-branch.py <slug> main`. Merging a branch into `main` is git's business, by hand or by merge request, never this command's.
- Findings you have not settled when you order the release to go on: they are parked by that word, said aloud. The check is advisory, so you may order the release at any moment.
- A recipe is missing: it is reported as a finding and the release goes on without that render.

For the terms used here, see the [Glossary](../reference/glossary.md).

## A worked example

You have finished a round of work on `my-project` and its intent stands at an integer version.

1. You type `/release my-project`.
2. Claude confirms the branch is `main`, runs `light` and `project`, and reports one finding. You park it.
3. Claude offers the `critique essence` review. You say no, and nothing runs.
4. Claude regenerates the README and the release notes and summarises the change. You accept it.
5. Claude reports that the documentation is one version behind the intent and offers `/document`. You say yes, and the pages are regenerated before the save.
6. Claude saves with `release <version>: <one line>`, proposes the tag `v<major>`, and you agree. The commit is pushed and tagged.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers for the documentation.
- [Versioning and history](../about/versioning-and-history.md): what a major approves and what its test attests.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
