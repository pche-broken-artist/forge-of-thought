---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: ff1cd5f4928a7717
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` looks at the remote of the engine and of your projects and brings in what is new, but only where that is safe. This page is for you, the principal (the person whose thinking is forged), when you want the latest engine or the latest work of a project that lives on another machine.

## When to use it

- You want the newest release of the engine. The engine's remote is its upgrade channel.
- You work on a project from more than one machine, or with someone else, and want what the remote holds.
- You want to know where each repository stands against its remote, without changing anything.

## The command

```
/pull [slug]
```

- Bare `/pull` covers the engine and every project that has an origin (a remote it was cloned from or pushed to).
- `/pull forge` covers the engine only.
- `/pull <slug>` covers one project, for example `/pull my-project`.

## What happens

1. Claude fetches each origin in scope and reports the state of each repository as a fact. The states are:
   - up to date
   - behind (the remote has commits you lack)
   - ahead (you have commits the remote lacks)
   - diverged (both sides have commits the other lacks)
   - no origin
   - not under git

   You should now see one state per repository in scope.

2. A repository with unsaved changes, or with a diverged history, stops here. Nothing is pulled from it. Claude gives you its one offer:
   - `/save` first, then pull again.
   - A merge by hand.
   - `/save`, which rebases your commits onto the remote.

   You should now see the offer next to each repository that stopped.

3. For each repository that is clean and behind, the pull script moves it forward to the remote's state. It never merges. It reports where the repository moved from and to, and the subject of each commit in between. You should now see a line such as "pulled <old> -> <new>", the two commits, and the list of commits between.

4. After a pull of the engine, Claude reads the release notes and shows the "Action required" lines of every release the pull crossed. You should now see those lines, or none if the releases asked nothing of you.

5. Claude then offers two checks for each project you keep, `/check light <slug>` and `/check project <slug>`. It runs them only on your word. You should now see the offer, and nothing run.

6. Where an "Action required" line names a migration, Claude offers `/migrate <slug>` for each project you keep that is still of the old shape. You should now see one offer per such project.

After a pull of a project, Claude reports what the script printed.

The forge never pulls or merges on its own. It looks, says what it sees and offers; every step that writes waits for you.

## What you have afterwards

- Each clean repository that was behind now stands at the remote's state, with the move reported.
- Repositories with unsaved changes or a diverged history are untouched.
- Nothing is merged and no check has run unless you asked for it.

## If something goes wrong

- **"has unsaved changes"**: the repository holds changes that are not saved. In a bare run it is skipped. When you named it, the pull is refused with the instruction to save first. Do that with `/save`, as [Save your work](save-your-work.md) describes, then pull again.
- **"Pull failed ... local and remote history diverged; nothing pulled"**: both sides have commits the other lacks. Merge by hand, or use `/save`, which rebases your commits onto the remote. If the save meets a conflict, [Settle a conflict](settle-a-conflict.md) says what to do.
- **"no origin - skipped"**: the repository has no remote. In a bare run it is reported and skipped. When you named it, the pull stops with this message.
- **"not under git"**: the project is not a git repository, so there is nothing to pull.

After a pull of the engine, [Upgrade the engine](upgrade-the-engine.md) says what to do next, and [Migrate a project](migrate-a-project.md) covers a migration that a release asks for. Why the forge only looks and offers is explained in [Persistence in git](../about/persistence-in-git.md).

## A worked example

You return to a machine after a few days and type:

```
/pull
```

Claude reports:

- the engine: behind
- `my-project`: up to date
- `other-project`: has unsaved changes

Claude offers `/save other-project` first for the last. It pulls the engine and prints a line like "pulled <old> -> <new>", the two commits and the subjects between them, one of which reads "release <version>". It then shows that release's "Action required" line, which names a migration. Claude offers `/check light my-project`, `/check project my-project` and `/migrate my-project`, and waits for your word on each.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
