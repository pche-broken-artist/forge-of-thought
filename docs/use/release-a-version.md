---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: f892a2272961ed75
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` publishes one repository from its `main` branch: it runs the checks, regenerates the README and the release notes, writes the state render and then saves with a release message. This page is for you when a project, or the engine, is ready to go out. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the work on `main` is settled and you want it on the remote as a release. A release is always one repository, never a sweep. The principal (whoever's thinking is being forged) orders it, and Claude does not start it on its own.

## The command

```
/release my-project -m "release 2.0: the first approved version" --tag v2
```

The slug names the repository, and `forge` means the engine. Without a slug, Claude asks which repository. `-m` and `--tag` are optional: without `-m` Claude drafts the message, and without `--tag` it proposes the tag only where the rule below says so.

## What happens

1. Claude reads the state of the repository and of its origin.
   - A release runs on `main` only. On any other branch Claude stops and says which branch the repository is on and how to get back to `main`: save, then switch with `python scripts/forge-branch.py my-project main`.
   - A repository that is behind its origin, or has diverged from it, is refused with the offer of `/pull`.
   - You should now see the repository named as being on `main` and level with its origin, or a refusal that says which of these is not so.
2. Claude runs the checks and reports the result, even when it is clean.
   - A project gets the `light` and `project` checks.
   - The engine gets `engine` on the engine root, and `light` and `project` on its own project.
   - The checks are launched at once and awaited together. Their findings are settled by walkthrough, that is, one finding per message, each closed with your verdict. How a check works and how a finding is settled is on [Check conformance](check-conformance.md).
   - You should now see either the statement that the checks passed or the first finding, put to you.
3. Claude offers `/critique essence` once, in one sentence. It is the lens that guards what a release publishes. On your word Claude runs it and the findings are settled by walkthrough. On your no, or silence, nothing runs.
   - You should now see the offer, and, if you accepted, its findings.
4. Claude regenerates the README and the release notes through `/render`, always and without testing whether they are stale. The two renders are launched at once and awaited together. Why these two files are renders is on [Renders and recipes](../about/renders-and-recipes.md).
   - Claude reports the steps with a short summary of what materially changed in the regenerated files. You rule on that change before the commit.
   - Other renders are never regenerated here.
   - A project whose recipe is missing is reported and released without that render.
   - You should now see the summary of what changed in the README and the release notes.
5. Claude writes the state render: the ledger (the single record of state, made at read time from the documents) is written as the tracked file `renders/state.md`. For the engine the file is `projects/forge/renders/state.md`. The command is `python scripts/forge-ledger.py my-project --out renders/state.md`.
   - You should now see `renders/state.md` made, so that the state is on the remote.
6. Claude reports the age of the documentation: the version in the front-matter of `docs/README.md` against the version of the intent. A repository without `docs/` has none, and that is no finding. Claude then offers `/document` in one sentence.
   - On your word Claude runs it before the save, so that the release carries current pages. See [Generate the documentation](generate-the-documentation.md).
   - On your no, or silence, nothing runs. A release never regenerates the documentation on its own.
   - You should now see the age of the pages and the offer.
7. Claude runs `/save` for the repository, as described on [Save your work](save-your-work.md), with two things decided by the release.
   - The commit message is `release <intent version>: <one line>`, unless you gave `-m`. The line sums up the rounds since the last release, taken from the history of the intent. For a library, whose history is git, the version is left out and the line says what changed.
   - When the intent's version is an integer, which means an approved major, Claude proposes the tag `v<major>` and takes it on your word. For the forge's own intent Claude first names what that intent asks a major to pass. That is a reminder, not a gate. What a major approves is on [Versioning and history](../about/versioning-and-history.md).
   - Any other tag is your request, as `/save` has it.
   - You should now see the commit made and pushed with the release message, and the tag where you accepted it.

## What you have afterwards

- A commit on `main`, pushed, whose message begins `release`.
- The README and the release notes regenerated from the settled sources.
- `renders/state.md` current in the repository.
- Pages of the documentation current, if you asked for `/document`.
- The tag `v<major>`, if the version was an integer and you accepted it.

## If something goes wrong

- The repository is not on `main`: Claude stops and names the branch and the way back. Merging a branch into `main` is done with git, by hand or by merge request, never by this command.
- The repository is behind or has diverged from its origin: the release is refused, and Claude offers `/pull`. The reason given is that the renders a release makes are taken as `ours` at a merge, which turns round in the rebase of the save.
- The checks find something you do not want to settle now: the check is advisory, so you may order the release to go on at any moment. Findings you have not settled are parked by that word, said aloud. Claude never fixes a finding silently.
- A recipe is missing: the gap is reported as a finding and the release goes on without that render.

## A worked example

You have a project `my-project` on `main`, its intent at an approved integer version, and a clean working state.

1. You type `/release my-project`.
2. Claude reports that the repository is on `main` and level with its origin, runs `light` and `project`, and says both passed.
3. Claude offers `/critique essence`. You answer no.
4. Claude regenerates the README and the release notes and tells you that the README gained a paragraph on the new layer. You accept.
5. Claude writes `renders/state.md`, reports that the documentation is one version behind and offers `/document`. You say yes, and the pages are regenerated.
6. Claude saves with the message `release 2.0: first approved version, the layer below the intent added`, proposes the tag `v2`, and on your yes the commit and the tag are pushed.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
