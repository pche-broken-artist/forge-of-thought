---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 64b1f091b7c6a57c
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` is the command that brings the latest work from a remote into the engine or into a project, and only when that is safe. It is for you, the principal (the person whose thinking is forged), when you want to take in what others pushed or to upgrade the engine. It first looks and says what it sees. It pulls only a repository that is clean and behind its remote, and it never merges.

## When to use it

- You want the newest engine, which is how the engine is upgraded.
- A colleague or another machine pushed to a project and you want it here.
- You want to know where each repository stands against its remote, with the offer that fits.

For the reasons the forge looks at the remote and offers instead of acting, see [Persistence in git](../about/persistence-in-git.md).

## The command

```
/pull [slug]
```

- Bare, `/pull` covers the engine and every project that has an origin (the remote the repository was set up with).
- `/pull forge` covers the engine only.
- `/pull <slug>` covers that one project.

## What happens

1. Claude looks at each repository in scope against its origin and reports the state as a fact. The state is one of these:
   - up to date
   - behind
   - ahead
   - diverged (both sides have commits the other lacks)
   - no origin
   - not under git

   You should now see one state for each repository.

2. A repository with unsaved changes, or with a diverged history, stops here and nothing is pulled from it. It gets one offer:
   - for unsaved changes, `/save` first, as described in [Save your work](save-your-work.md);
   - for a diverged history, a merge by hand, or `/save`, which rebases your commits onto the remote.

   If the save of a diverged repository meets a conflict, [Settle a conflict](settle-a-conflict.md) says what to do. You should now see the stopped repository named with its offer.

3. For every repository that is clean and behind, the pull script fast-forwards it: the repository moves forward to the remote's newest commit without any merge. You should now see, for each one, where it moved from and to, and the subjects of the commits between.

4. After a pull of the engine, Claude reads the release notes and shows the Action required lines of every release the pull crossed. You should now see those lines, or none if the releases asked for nothing.

5. Claude then offers two checks, a light check and a project check, on each project you keep. It runs them only on your word.

6. Where an Action required line names a migration, Claude offers `/migrate <slug>` for each project of the old shape. Each project is migrated on one clone and then saved. A project migrated elsewhere reaches you by `/pull`. Every user of the engine migrates their own projects. See [Migrate a project](migrate-a-project.md).

   You should now see one offer for each project that still has the old shape.

After a pull of a project, Claude reports what the script printed.

## What you have afterwards

- Every clean repository that was behind is at its remote's newest commit.
- Repositories that were up to date, ahead, diverged, unsaved, without origin or not under git are as they were.
- After an engine pull, you know which releases were crossed and what each asked of you. [Upgrade the engine](upgrade-the-engine.md) says what to do next.

## If something goes wrong

The scripts refuse in these cases. With a slug the refusal stops the run. Bare, the repository is reported and skipped, and the run goes on to the next.

- **No origin:** the script prints "no origin - skipped". Set up a remote first, or leave the repository alone.
- **Unsaved changes:** the script lists the changes and, with a slug, tells you "Run scripts/forge-save.py first, then pull." Bare, it prints "skipped". Save first, so that a pull cannot create a conflict in half-finished work.
- **Diverged history:** the script prints "Pull failed ... local and remote history diverged; nothing pulled. Merge by hand, or scripts/forge-save.py rebases your commits onto the remote." Choose one of the two as the message says.
- **Not under git:** the repository is reported as such and nothing is pulled.

The forge never pulls or merges on its own. Anything beyond a fast-forward is yours to decide.

## A worked example

You run `/pull` with a project `<slug>` that has unsaved changes and the engine that is behind.

```
/pull
```

Claude reports the engine as behind and `<slug>` as having unsaved changes, with the offer to `/save` it first. You decide to take the engine now. The script prints the engine's before and after commits and the subjects between them, one of which reads `release <version>`. Claude shows that release's Action required line, which names a migration. It offers the two checks on `<slug>` and offers `/migrate <slug>` because `<slug>` is of the old shape. You save `<slug>` first, then accept the migration.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
