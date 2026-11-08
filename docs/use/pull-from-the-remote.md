---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: f776cfd40bc8d6b2
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` is the command that looks at the remote copy of the engine and of your projects, says how each stands against it, and brings in what is clean and behind. It is for you, the person who keeps the engine and projects on a machine and wants the latest of them. Claude is the agent that runs it for you. The remote copy is called the origin below.

## When to use it

- You want the latest engine, the way the engine is upgraded.
- You work on a project with someone else and want what they saved.
- You want to know where a repository stands against its origin before you save or release.

## The command

```
/pull [slug]
```

- Bare `/pull` takes the engine and every project that has an origin.
- `/pull forge` takes the engine only.
- `/pull <slug>` takes that one project, for example `/pull my-project`.

## What happens

1. Claude reads the state of each repository in scope against its origin. It reports one of these facts for each:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin
   - not under git

   You should now see one state per repository, in those words.

2. Beside that, Claude reports what waits on GitHub outside git: the open pull requests and the discussions nobody of the repository has answered. If it cannot read them (no `gh` tool, an origin that is not on GitHub, no login, no network), you see one line saying so and why. Nothing of it is pulled, merged or answered. You should now see a `github:` line under each repository that has an origin.

3. A repository with unsaved changes, or with a diverged history, stops here with one offer, and nothing is pulled from it. The offer is one of these:
   - `/save` first, see [Save your work](save-your-work.md).
   - a merge by hand.
   - `/save`, which rebases your commits onto the remote. If the save meets a conflict, see [Settle a conflict](settle-a-conflict.md).

   You should now see the offer under the repository that stopped.

4. For what is clean and behind, Claude runs the pull script. It fast-forwards only, so it never merges. For each repository it reports where it moved from and to, and the subjects of the commits between. You should now see a line `pulled <from> -> <to>`, the first and last commit of the move, and the list of commits between.

5. After a pull of the engine, Claude reads the release notes and shows the Action required lines of every release the pull crossed. Then it offers two checks on each project you keep, `/check light <slug>` and `/check project <slug>`, and runs them only on your word. Where an Action required line names a migration, Claude offers `/migrate <slug>` for each project of the old shape; see [Migrate a project](migrate-a-project.md). You should now see the Action required lines and the offers. What to do next is in [Upgrade the engine](upgrade-the-engine.md).

6. After a pull of a project, Claude reports what the script printed.

The forge never pulls or merges on its own. It looks and offers, and it pulls only what is clean and behind. The reasons are in [Persistence in git](../about/persistence-in-git.md).

## What you have afterwards

- Each clean repository that was behind is at the commit of its origin.
- Each repository that was up to date is unchanged.
- Each repository with unsaved changes or a diverged history is untouched, with an offer for it.

## If something goes wrong

- "no origin - skipped": the repository has no origin. Bare, the pull skips it. With a slug, it stops with this message.
- "has unsaved changes": the repository is not touched, so that a pull cannot create a conflict in half-finished work. Bare, it is skipped. With a slug, the script stops and says to save first, then pull.
- "Pull failed ... local and remote history diverged; nothing pulled": the script stops for that repository. Merge by hand, or save, which rebases your commits onto the remote.
- The `github:` line says it could not read what waits on GitHub: the pull itself is not affected. Install and log in to `gh` if you want that line filled.

Terms of the forge are in the [Glossary](../reference/glossary.md).

## A worked example

You have the engine and one project, `my-project`, with an origin. You run:

```
/pull
```

Claude reports the engine as behind and `my-project` as clean and up to date. Under each, the `github:` line shows one open pull request for the engine and nothing waiting for the project. Claude runs the pull script. For the engine it prints `pulled <from> -> <to>`, the two commits, and the subjects between them, one of which names a release. Claude reads the release notes, shows that release's Action required line, which names no migration, and offers `/check light my-project` and `/check project my-project`. You answer yes to the first. Nothing else was pulled, merged or answered.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
