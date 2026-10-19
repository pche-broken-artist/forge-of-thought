---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 949112cc470fa7f3
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` brings the latest work from a repository's remote (the copy
it was cloned from, called its origin) into your copy. This page is
for you as the principal (the person whose thinking is forged) when
you want the engine's newest release, or a project saved from
another machine. The command looks first, pulls only what is safe and
leaves everything else to you.

## When to use it

- You want to upgrade the engine to its newest release.
- A project was saved from another machine and this copy is behind.
- You want to know where each repository stands against its origin,
  with a pull only if one is safe.

Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## The command

```
/pull [slug]
```

- Bare `/pull` covers the engine and every project that has an
  origin.
- `/pull forge` covers the engine only.
- `/pull my-project` covers that one project (a placeholder slug,
  replaced by the slug of your own project).

## What happens

1. Claude looks at each repository in scope and reports its state
   against its origin as a fact. The states are:
   - up to date
   - behind
   - ahead
   - diverged (both sides have commits the other lacks)
   - no origin
   - not under git

   You should now see one state per repository.

2. A repository with unsaved changes, or with a diverged history,
   stops here. Nothing is pulled from it. Claude gives its one offer:
   `/save` first (see [Save your work](save-your-work.md)), or for a
   diverged history a merge by hand, or `/save`, which puts your
   commits on top of the remote's. You should now see the offer
   beside that repository, and its files unchanged.

3. For each repository that is clean and behind, Claude runs the pull
   script. It only fast-forwards, so it can never create a conflict
   in half-finished work. You should now see, per repository, where
   it moved from and to (the earlier and the later commit, each with
   its subject) and the subjects of the commits between.

4. After a pull of the engine, Claude reads the release notes and
   shows the "Action required" lines of every release the pull
   crossed. You should now see those lines, or none if the releases
   asked nothing of you.

5. Claude then offers two checks on each project you keep: the
   `light` check and the `project` check. It runs them only on your
   word. You should now see the offer, and no check running.

6. Where an "Action required" line names a migration, Claude offers
   `/migrate <slug>` for each of your projects that is still of the
   old shape. Each is migrated on one clone, then saved. A project
   migrated on another machine is brought in by `/pull`. It makes no
   difference whose machine the clone is: every user of the engine
   migrates his own projects. See
   [Migrate a project](migrate-a-project.md).

7. After a pull of a project, Claude reports what the script printed.

## What you have afterwards

- Every repository that was clean and behind is up to date.
- Every other repository is exactly as it was, with its offer.
- Nothing was merged, and no check was run unasked.

What to do next after an engine pull is on
[Upgrade the engine](upgrade-the-engine.md). The reason the forge
looks and offers instead of pulling on its own is on
[Persistence in git](../about/persistence-in-git.md).

## If something goes wrong

The script refuses in these cases. Each refusal changes nothing.

- **No origin.** A repository with no origin is reported as
  "no origin - skipped". Asked for by slug, the same case stops the
  run instead of being skipped.
- **Unsaved changes.** The repository is listed with its changes and
  skipped. Asked for by slug, the run stops with "Run
  scripts/forge-save.py first, then pull." Save first with `/save`,
  then pull again.
- **Diverged history.** The run stops with "local and remote history
  diverged; nothing pulled". Merge by hand, or use `/save`, which
  puts your commits on top of the remote's.
- **Not under git.** A project with no repository is reported and
  skipped.

## A worked example

You have just heard that the engine has a new release. You type:

```
/pull forge
```

Claude reports the engine as "behind", with the engine clean. It runs
the pull and prints where the engine moved from and to, and a short
list of commit subjects, one of them a release. It then shows that
release's "Action required" line, which names a migration. It offers
the `light` and `project` checks on `my-project` and offers
`/migrate my-project`. You say yes to the migration, then save the
project with `/save my-project`.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
