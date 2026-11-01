---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: bfc8f86a2eb8c57b
inputs:
  - .claude/skills/release/SKILL.md
---

# Release a version

`/release` releases one repository from `main`: it runs the checks, regenerates the README and the release notes, writes the state render and then saves with a release message. This page is for the principal, the person whose thinking is forged, who wants to publish a settled state of a project or of the engine.

A release is always one repository, never a sweep. The repository is named by its slug, and `forge` means the engine. Without a slug, Claude asks which repository.

## When to use it

Use it when the sources are settled and you want the README, the release notes and the state on the remote as one named step. Use [Save your work](save-your-work.md) instead when you only want to commit and push on whatever branch is checked out.

A release is made on `main` only. The reason for the two doors and the two speeds is given in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/release [slug] [-m "message"] [--tag name] [--auto]
```

A line that can be typed as it stands:

```
/release my-project
```

- `-m "message"` gives the commit message yourself, so Claude does not draft one.
- `--tag name` asks for a tag with a free name of your own.
- `--auto` runs the release through and stops only at a serious thing (see below).

## What happens

1. **The state is read.** Claude reads the state of the repository and of its origin through a script.
   - On any branch but `main`, the release stops and tells you which branch the repository is on and how to get back.
   - A repository that is behind or diverged from its origin is refused, with the offer of `/pull`.
   - You should now see the repository on `main` and level with its origin, or a stop that names the way out.

2. **The checks run.** For a project, the checks are `light` and `project`. For the engine, `engine` runs on the engine root, and `light` and `project` run on the engine's own project. They are launched together and awaited together.
   - Claude reports the result even when it is clean.
   - Findings are settled by walkthrough, one item per message, each closed with a verdict. The page [Check conformance](check-conformance.md) says how.
   - A finding you have not settled when you order the release to go on is parked by that word, and Claude says so aloud. The check is advisory.
   - You should now see either the statement that the checks passed or every finding settled or parked.

3. **`critique essence` is offered once.** This lens guards what a release publishes. It runs only on your word. On your no, or on silence, nothing runs, because no reviewer runs at a release on Claude's own judgement.
   - You should now see one sentence of offer, and either its findings settled or nothing run.

4. **The age of the documentation is reported.** Claude compares the version in the front-matter of the repository's `docs/README.md` with the intent's version, and offers `/document` in one sentence. A repository without `docs/` has no age, and that is no finding.
   - On your word, `/document` runs before the renders, so that the README reads the current index. See [Generate the documentation](generate-the-documentation.md).
   - On your no, or on silence, nothing runs. A release started by hand never regenerates the documentation on its own.
   - You should now see the age reported and the documentation either regenerated or left as it was.

5. **The README and the release notes are regenerated.** Both are rendered unconditionally from their recipes, through `/render`, launched together and awaited together. Why they are renders is told in [Renders and recipes](../about/renders-and-recipes.md).
   - Claude reports a short summary of what materially changed in the regenerated files. You rule on that change before the commit.
   - Other renders are never regenerated here.
   - A project whose recipe is missing is reported and released without that render.
   - You should now see the summary of the change in the README and the release notes.

6. **The state render is written.** The ledger (the state of the project, made from its documents at read time) is written as the tracked file `renders/state.md`, so that the state is on the remote. For the engine the file is `projects/forge/renders/state.md`.
   - You should now see the state render among the changed files.

7. **The save runs.** Claude runs `/save --quick`, which is [Save your work](save-your-work.md) without the `light` check, because step 2 ran it already.
   - The message is `release <intent version>: <one line>`. The line sums up the rounds since the last release, taken from the history of the intent. Your `-m` replaces it.
   - For a library, whose history is git, the version is left out and the line says what changed.
   - At an integer version (an approved major) Claude proposes the tag `v<major>`, and it is taken on your word. Before it proposes the tag of a major of the engine, Claude names what the engine's own intent asks a major to pass. That is a reminder on your word, never a gate. What a major approves is told in [Versioning and history](../about/versioning-and-history.md).
   - Any other tag is your request, as `/save` has it.
   - You should now see the commit with the release message, pushed, and the tag where you agreed to it.

## With `--auto`

`--auto` runs the whole release through. The checks and every run of agents go without asking, and Claude says the model and the size of each run as information.

- **One question before anything runs.** Claude asks whether the documentation runs. The default is yes. On yes, it runs as a part of the release, and the models and the number of pages are said before the writers are launched.
- **Findings.** A finding whose fix lies in the operating layer or in bookkeeping, and changes no position and no rule's meaning, is fixed and recorded by Claude without a walkthrough.
- **What stops the release.** A finding of severity high stops it. So does a finding whose fix would change a position or a rule's meaning, and a finding the report calls a decision. Each is put to you. Nothing is parked on your behalf, so what `--auto` cannot settle stays open and the release waits for your word.
- **`critique essence`.** It is neither offered nor run.
- **The regenerated files.** They are taken as they came, with no summary put to you. The one stop is a hit of the instance-fact scan that the released version did not already carry. A hit that version carried stands as before.
- **The message.** The drafted message is used without confirmation and said aloud in the report.
- **The tag of a major.** `--auto` never takes it. The release stops before it and asks.

The branch and origin rule of step 1 holds under `--auto` as for any release.

## What you have afterwards

- The checks reported and their findings settled or parked.
- The documentation as current as you chose to make it.
- A regenerated README and release notes.
- The state render `renders/state.md`.
- One commit with the release message, pushed, and the tag `v<major>` where the version is a major and you agreed to it.

## If something goes wrong

- **The repository is on another branch.** The release stops and names the branch and the way back: save, then switch with `python scripts/forge-branch.py <slug> main`. Merging a branch into `main` is done with git, by hand or by merge request, and never by `/release`.
- **The repository is behind or diverged from its origin.** The release refuses and offers `/pull`.
- **A finding is not settled.** Order the release to go on and it is parked by that word. Under `--auto`, a finding that needs your decision stops the release instead.
- **A hit of the instance-fact scan under `--auto`.** The release stops when the hit is new to the released version.
- **The tag of a major.** Under `--auto` the release stops before it and asks. Answer, and the tag is taken on your word.

## A worked example

You have settled a round of work on a project with the slug `my-project` and are on `main`.

1. You type `/release my-project`.
2. Claude reports the repository on `main` and level with its origin, then runs `light` and `project` together. One finding comes back. You settle it by walkthrough.
3. Claude offers `critique essence` in one sentence. You answer no, and nothing runs.
4. Claude reports that the documentation is older than the intent and offers `/document`. You say yes, and the pages are regenerated.
5. Claude regenerates the README and the release notes and tells you what changed in them. You accept the change.
6. Claude writes `renders/state.md`, then runs `/save --quick` with the message `release <intent version>: <one line>`.
7. The version is not an integer, so no tag is proposed. The commit is pushed.

The same release with `/release my-project --auto` asks one question first, whether the documentation runs, and then goes through without further questions unless something serious stands in the way.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their findings are settled.
- [Renders and recipes](../about/renders-and-recipes.md): why the README and the release notes are renders.
- [Generate the documentation](generate-the-documentation.md): the command the release offers and, with `--auto`, asks about once.
- [Versioning and history](../about/versioning-and-history.md): what a major approves.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds, and why a release is made on `main` only.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
