---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 96ae051943d12642
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` is the command that looks at the remote of the engine and of each project and brings in what is clean and behind. This page is for you when you want the latest engine, or the latest of a project that is also kept elsewhere. The terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## When to use it

- You want the latest engine. The engine's remote is its upgrade channel.
- You work on a project from more than one place and want the work done elsewhere.
- You want to know where each repository stands against its remote, before you decide anything.

## The command

```
/pull [slug]
```

- Bare, `/pull` covers the engine and every project that has an origin (a remote the repository was given).
- `/pull forge` covers the engine only.
- `/pull <slug>` covers that one project.

Claude runs the scripts for you. Nothing is pulled without this command: the forge never pulls or merges on its own judgement. The reason it looks and offers is explained in [Persistence in git](../about/persistence-in-git.md).

## What happens

1. Claude fetches each repository in scope from its origin and reports its state as a fact. The words are:
   - up to date
   - behind
   - ahead
   - diverged (your history and the remote's each hold commits the other lacks)
   - no origin
   - not under git

   You should now see one state per repository, and nothing has changed in your files.

2. A repository with unsaved changes, or with a diverged history, stops here with one offer, and nothing is pulled from it.
   - With unsaved changes the offer is to save first. See [Save your work](save-your-work.md).
   - With a diverged history the offer is a merge by hand, or a save, which rebases your commits onto the remote.

   You should now see the offer next to that repository, and the other repositories carry on.

3. For each repository that is clean and behind, the pull script brings it forward. It moves forward only: it never merges. Claude relays its report.
   - Where the repository moved from and to, each with its short hash and subject.
   - The subjects of the commits in between.

   You should now see "pulled" with two hashes for each repository that moved, and "up to date" for one that did not.

4. After a pull of the engine, Claude reads `RELEASE-NOTES.md` and shows the Action required lines of every release among the commits the script listed. Those are the things you must do because of the release.

   You should now see the Action required lines, release by release.

5. Claude then offers two checks on each project you keep, the light check and the project check. It runs them only when you say so.

   You should now see the offer, and no check has run. What to do next is on [Upgrade the engine](upgrade-the-engine.md).

6. After a pull of a project, Claude reports what the script printed, and nothing more.

## What you have afterwards

- Each repository that was clean and behind is at the remote's latest commit.
- Every other repository is as it was, with its state and its offer reported.
- The Action required lines of the crossed releases are in front of you after an engine pull.
- No merge has been made and no check has run.

## If something goes wrong

The scripts stop with these messages and refusals.

| What you see | What it means | What to do |
|---|---|---|
| `has unsaved changes:` followed by the changed files, then `skipped` | The repository has unsaved work. A bare `/pull` skips it and goes on. | Save first, then pull again. |
| `Run scripts/forge-save.py first, then pull.` | The same, for a repository you named: the pull is refused. | Save first, then pull again. |
| `no origin - skipped` | The repository has no remote. A bare `/pull` skips it. | Nothing to pull. Add a remote if you want one. |
| `no origin - skipped` for a named project | The pull is refused. | The same. |
| `Pull failed in <name> - local and remote history diverged; nothing pulled.` | Your history and the remote's have parted. | Merge by hand, or save: the save rebases your commits onto the remote. Then pull again. |
| A project reported as not under git | The project has no repository of its own. | Nothing to pull. This is a property of the project, not a defect. |

## A worked example

You want the latest engine and have one project, `my-project`, that is kept on a remote too.

You type:

```
/pull
```

Claude reports the state of each repository. The engine is behind. `my-project` is up to date. Claude runs the pull, and the report reads like this:

```
forge (engine): pulled a1b2c3d -> e4f5a6b
   before: a1b2c3d <subject of the old last commit>
   after:  e4f5a6b <subject of the new last commit>
   commits between:
  <subject of a commit>
  <subject of the release commit>
my-project: up to date
```

The listed commits include a release, so Claude shows that release's Action required lines from `RELEASE-NOTES.md`. Then it offers the light check and the project check on `my-project`. You say yes to the light check and no to the other. Only the light check runs.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
