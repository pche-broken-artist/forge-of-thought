---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 99de84a6e1948992
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository from `main`: it runs the checks, regenerates the README and the release notes, renders the state, offers the documentation and then saves with a release message and, at an approved major version, a tag. This page is for you, the user who has decided a repository is ready to go out and wants to know what the command does, in what order.

Two words are used throughout. The principal is the person whose thinking is being forged, that is you, who alone decides. The ledger is the file that holds the state of a project (its documents, renders, findings and so on). A walkthrough is the way Claude works through a list that needs your decision: one item per message, each closed with a verdict line.

## When to use it

Use it when a repository is on `main`, its work is saved and you want the release to carry fresh renders and a release commit. A release is always one repository, never a sweep. Use [Save your work](save-your-work.md) instead when you only want to commit and push without renders.

## The command

```
/release [slug] [-m "message"] [--tag name]
```

A real example: `/release forge` releases the engine itself. The slug is the repository's name, and without one Claude asks which repository you mean. `-m` supplies the commit message yourself. `--tag` asks for a tag of your own naming.

## What happens

1. Claude reads the state of the repository against its origin.
   A release runs on `main` only. On any other branch it stops and tells you which branch the repository is on and how to get back.
   A repository that is behind its origin, or has diverged from it, is refused with the offer of `/pull`.
   You should now see either the release going on, or a refusal naming the branch or the state against the origin.

2. Claude runs the checks and reports the result, even when it is clean.
   For a project the checks are `light` and `project`. For the engine they are `engine` on the engine itself, and `light` and `project` on its own project. They are launched together and awaited together.
   Findings are settled by walkthrough, as described in [Check conformance](check-conformance.md). A finding may be parked and the release goes on. Claude fixes nothing silently.
   The checks come before the renders so that any fix made in the walkthrough is already in what the renders are made from.
   You should now see "the checks passed", or a list of findings offered for walkthrough.

3. Claude offers `/critique essence` once, in one sentence.
   It is the lens that guards what a release publishes. On your word it runs and its findings are settled by walkthrough. On your no, or silence, nothing runs: no reviewer runs at a release on Claude's own judgement.
   You should now see the offer, and after your answer either the findings or the next step.

4. Once the findings are settled, Claude regenerates the README and the release notes.
   Both are regenerated every time, with no test of whether they are stale, each through `/render` (see [Renders and recipes](../about/renders-and-recipes.md) for why they are renders). They are launched together and awaited together.
   Claude reports the steps with a short summary of what materially changed in the regenerated files, and you rule on that change before the commit.
   Other renders of the repository are never regenerated here.
   Then Claude renders the state: the ledger is written as the tracked file `renders/state.md` (for the engine, in its own project's `renders/` folder), so that the state is on the remote.
   You should now see the README, the release notes and `renders/state.md` regenerated, and the summary of what changed.

5. Claude reports the age of the documentation and offers `/document`.
   It compares the version in `docs/README.md` with the version of the intent. A repository without `docs/` has no age to report, and that is no finding.
   On your word it runs `/document` before the save, so that the release carries current pages (see [Generate the documentation](generate-the-documentation.md)). On your no, or silence, nothing runs. A release never regenerates the documentation on its own.
   You should now see the age of the documentation, and the offer.

6. Claude runs `/save` for the repository (see [Save your work](save-your-work.md)).
   The commit message is `release <intent version>: <one line>`, the line summarising the rounds since the last release. Supplying `-m` replaces it. For a library, which has no intent version, the version is left out and the line says what changed.
   When the intent's version is an integer, an approved major, Claude proposes the tag `v<major>` and takes it on your word only. For the forge's own intent, Claude first names what that intent asks a major to pass, as a reminder and never as a gate. [Versioning and history](../about/versioning-and-history.md) says what a major approves. Any other tag is your request, as `/save` has it.
   You should now see the commit and push done, and the tag if you agreed to it.

## What you have afterwards

- A release commit on `main`, pushed, with a message that names the intent version.
- The README and the release notes regenerated from the settled sources.
- The ledger as the tracked file `renders/state.md`.
- Current documentation, if you agreed to `/document`.
- At an integer version, the tag `v<major>`, if you agreed to it.

The check is advisory. You may order the release at any moment regardless of findings, and the findings you have not settled are parked by that word, said aloud.

## If something goes wrong

- The repository is on another branch: the release stops and names the branch. Save your work there, then go back with `python scripts/forge-branch.py <slug> main`. Merging a branch into `main` is git's business, by hand or by merge request, never this command's.
- The repository is behind or diverged from its origin: the release is refused and `/pull` is offered. The reason is that the renders a release makes are taken as ours at a merge, and that turns round in the rebase of the save.
- A project has no recipe for the README or the release notes: the gap is reported as a check finding and the project is released without that render.
- Findings you do not want to settle now: say so, and they are parked by that word.

## A worked example

```
/release my-project
```

1. Claude reports the repository is on `main` and level with its origin.
2. The checks `light` and `project` come back with one finding; you settle it in a walkthrough with `(a)ccept`.
3. Claude offers `/critique essence`; you answer no, and nothing runs.
4. The README and the release notes are regenerated, with a summary of what changed; `renders/state.md` is written. You rule that the summary is as expected.
5. Claude reports the documentation is one version behind and offers `/document`; you say yes and it runs.
6. The commit is made with the message `release 2.0: <one line of the rounds since the last release>`. The version is an integer, so Claude proposes the tag `v2` and you agree.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
