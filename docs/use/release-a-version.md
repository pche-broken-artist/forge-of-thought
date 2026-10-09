---
generated: 2026-10-09
made: mirrored
inputs-hash: d2b21ab7833df983
inputs:
  - .claude/skills/release/SKILL.md
  - CLAUDE.md
---

# Release a version

This page is for the person who wants to release one repository: the engine or a project. It says what `/release` does, in order, and where you decide.

```
/release [slug] [-m "message"] [--tag name]
```

A release is always one repository, never a sweep. Name it by its slug (`forge` means the engine). Without a slug you are asked which one.

## Before you start

A release runs from `main` only. On any other branch it stops, names the branch the repository is on and tells you how to get back (switch to `main` after saving). Merging a branch into `main` is not done by this command: that is git's business, by hand or by merge request.

## The steps

1. **Checks.** The checks run over the sources and the result is always reported, even when clean. For a project they are `light` and `project`. For the engine they are `light`, `engine` and `project`, the last two on the engine's own project. They are launched at once and awaited together. If they find something, you settle each finding by walkthrough. A finding may be parked, and the release goes on. Nothing is fixed silently, and the release does not go on with a finding left unsettled. The checks come first so that any fix from the walkthrough, such as a new intent version, is already in what the renders are made from.

2. **The essence critique.** You are offered `critique essence` once, in one sentence: it is the lens that guards what a release publishes against drift of the chain. It runs only on your word, and its findings are then settled by walkthrough. On your no, or silence, nothing is run. No reviewer runs at a release on its own judgement.

3. **README and release notes.** Once the findings are settled, the repository's README and release notes are regenerated from their recipes, unconditionally and with no test of whether they are stale, through `/render`. Both are launched at once. You get a report of the steps and a short summary of what materially changed in the regenerated files, and you rule on that change before anything is committed. If a project's recipe is missing, that is reported as a finding and the project is released without that render. Other renders are not regenerated here. Why these two are renders is explained in [About renders and recipes](../about/renders-and-recipes.md).

4. **Age of the documentation.** The release reports the `version` in the front-matter of the repository's `docs/README.md` against the intent's version. A repository without `docs/` has none, and that is no finding. `/document` is offered in one sentence. It runs before the save only on your word, so that the release carries current pages. On your no, or silence, nothing is run. The release never regenerates the documentation on its own. How to do it is on [Generate the documentation](generate-the-documentation.md).

5. **Save and tag.** `/save` runs for the repository, as described on [Save your work](save-your-work.md), with two things decided by the release:
   - The commit message is `release <intent version>: <one line>`. The line sums up the rounds since the last release, taken from the intent's history, unless you gave `-m`. For a library, whose history is git, the version is left out and the line says what changed.
   - When the intent's version is an integer, that is an approved major, the tag `v<major>` is proposed and taken on your word. Before the tag of a major of the forge intent is proposed, you are reminded of what the forge intent asks a major to pass. The reminder is never a gate. Any other tag is your own request.

## Advisory, not blocking

The check is advisory: you may order the release at any moment regardless of findings.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [About renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers for the documentation.
