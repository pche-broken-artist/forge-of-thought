---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: ee3af12b81cdc1ef
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` looks at the remote of the engine and of your projects and
brings in what is clean and behind. It is for you, the principal (the
person whose thinking is forged), when you want the latest engine or
the latest of a project that someone else also saves to. Claude looks
and offers; it never pulls or merges on its own judgement.

## When to use it

- You want to upgrade the engine to its latest release.
- A project has a remote and you want what others saved there.
- You want to know where each repository stands against its origin
  (its remote), and what waits on GitHub, before you decide anything.

## The command

```
/pull [slug]
```

- Bare `/pull` covers the engine and every project that has an origin.
- `/pull forge` covers the engine and the forge's own project cloned
  beside it.
- `/pull my-project` covers that one project.

## What happens

1. Claude reports the state of each repository in scope against its
   origin, as a fact. The state is one of these:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin
   - not under git

   Beside it Claude reports what waits on GitHub outside git: the open
   pull requests and the unanswered discussions. Where it cannot read
   them, it says so in one line with the reason, for example that the
   GitHub tool is missing, that the origin is not on GitHub, that
   there is no login or no network. Nothing of this is pulled, merged
   or answered.

   You should now see one state per repository and one line on what
   waits on GitHub.

2. A repository with unsaved changes, or with a diverged history,
   stops here and nothing is pulled from it. It gets one offer:
   - `/save` first (see [Save your work](save-your-work.md)).
   - A merge by hand.
   - `/save`, which rebases your commits onto the remote. If that
     meets a conflict, see [Settle a conflict](settle-a-conflict.md).

   You should now see the offer for each repository that stopped.

3. For what is clean and behind, the pull script fast-forwards: it only
   moves the repository forward and never creates a merge. Claude
   reports where each repository moved from and to, and the commits
   between.

   You should now see a line per repository that moved, with a
   `before:` and an `after:` commit and the list of commits between.

4. After a pull of the engine, Claude reads the release notes and shows
   the Action required lines of every release the pull crossed. It then
   offers two checks for each project you keep, `/check light <slug>`
   and `/check project <slug>`, and runs them only on your word.

   You should now see the Action required lines and the two offers.

5. Where an Action required line names a migration, Claude offers
   `/migrate <slug>` for each project of the shape before the
   migration. See [Migrate a project](migrate-a-project.md).

   You should now see one `/migrate` offer per project of the old
   shape.

6. After a pull of a project, Claude reports what the script printed.

What to do after the engine has moved is told in
[Upgrade the engine](upgrade-the-engine.md).

## What you have afterwards

- Every clean repository that was behind stands at its origin.
- Repositories with unsaved or diverged work are untouched.
- Nothing on GitHub was merged or answered.
- No check ran and no migration was made unless you said so.

## If something goes wrong

- **No origin.** The repository is reported as "no origin - skipped".
  Bare, the pull goes on to the next repository. With a slug it
  stops with that message.
- **Unsaved changes.** The script lists the changed files. Bare, it
  reports "skipped" and goes on. With a slug it stops and tells you to
  run the save first, then pull.
- **Diverged history.** The script stops with "local and remote
  history diverged; nothing pulled". Merge by hand, or let the save
  rebase your commits onto the remote.
- **Projects without a repository.** They are reported and skipped.
- **GitHub cannot be read.** One line says why. The pull goes on.

## A worked example

You have the engine and a project `my-project` with an origin, and the
project has unsaved changes.

```
/pull
```

Claude reports the engine as behind and `my-project` as having unsaved
changes. It says nothing waits on GitHub for the engine, and one open
pull request waits for the project. It pulls the engine and prints the
moves:

```
pulled a1b2c3d -> e4f5a6b
   before: a1b2c3d <subject>
   after:  e4f5a6b <subject>
   commits between:
    <subject>
    <subject>
```

It shows the Action required lines of the releases crossed and offers
the two checks for `my-project`. It leaves `my-project` alone and
offers `/save` first. You answer, run the save, and then `/pull
my-project` if the project is behind.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
