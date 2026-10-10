---
generated: 2026-10-10
made: mirrored
inputs-hash: e44842f45035e7b2
inputs:
  - .claude/skills/release/SKILL.md
  - CLAUDE.md
---

# Release a version

This page is for the person who wants to release a repository: a
project, or the engine itself. It says what `/release` does, in what
order, and where it waits for your word.

```
/release [slug] [-m "message"] [--tag name]
```

A release is always one repository, never a sweep. Name it by its
slug (`forge` means the engine); without a slug you are asked which
repository.

## Before anything: the branch

A release runs on `main` only. On any other branch it stops, names the
branch the repository is on and tells you how to get back
(`python scripts/forge-branch.py <slug> main`, after saving).
Merging a branch into `main` is git's business, by hand or by merge
request, never this command's.

## The steps, in order

1. **The checks.** For a project they are `light` and `project`; for
   the engine, `light`, `engine` and `project`, the last two on the
   forge's own project. They are launched at once and awaited
   together. The result is reported to you always, even when clean.
   Findings are settled by walkthrough, one at a time, and a finding
   may be parked: the release then goes on. Nothing is fixed silently,
   and the release does not go on with an unsettled finding. The checks
   run before the renders so that a fix made in the walkthrough is
   already in what the renders are made from.
2. **The essence critique, offered.** One sentence offers
   `critique essence`, the lens that guards what a release publishes.
   It runs only on your word, and its findings are settled by
   walkthrough before the release goes on. On your no, or silence,
   nothing runs: no reviewer runs at a release on Claude's own
   judgement.
3. **The README and the release notes.** Once the findings are
   settled, both are regenerated from their recipes, unconditionally,
   with no test of whether they are stale, each through `/render`. The
   two are launched at once. You get a short summary of what
   materially changed in the regenerated files and rule on it before
   the commit. Other renders are never regenerated here. A project
   whose recipe is missing is reported and released without that
   render.
4. **The age of the documentation.** The release reports the
   `version` in the front-matter of the repository's `docs/README.md`
   against the intent's version. A repository without `docs/` has no
   such age, and that is no finding. `/document` is offered in one
   sentence. On your word it runs before the save, so that the release
   carries current pages; on your no, or silence, nothing runs. The
   release never regenerates the documentation on its own.
5. **The save.** `/save` runs for this repository with two things
   decided here:
   - The commit message is `release <intent version>: <one line>`,
     the line summarising the rounds since the last release, taken
     from the intent's history. Your `-m` replaces it. For a library,
     whose history is git, the version is left out and the line says
     what changed.
   - When the intent's version is an integer, an approved major, the tag
     `v<major>` is proposed and taken on your word. Where the
     repository is the engine, Claude first names what the forge's own
     intent asks a major to pass: a reminder, never a gate. Any other
     tag is your request, as `/save` has it (`--tag name`).

## The check is advisory

You may order the release at any moment regardless of findings. The
checks and the critique inform; only you publish.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [About renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers for the documentation.
- [About versioning and history](../about/versioning-and-history.md): what a major approves and what its test attests.
