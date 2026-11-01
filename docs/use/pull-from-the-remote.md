---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 8c8942c29ac8aad3
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` brings the latest work from the remote into your copy of the
engine or of a project. It is for you, the principal (the person whose
thinking is forged), when you want to know whether the remote has moved
and to take what is safe to take. It looks first, says what it sees,
pulls only what is clean and behind, and merges nothing.

## When to use it

- You work on more than one machine, or with someone else, and the
  remote may hold commits you do not have.
- You keep the engine up to date: the remote of the engine is its
  upgrade channel.
- You want the state of every repository against its origin before you
  start to write.

## The command

```
/pull [slug]
```

- Bare, `/pull` takes the engine and every project that has an origin.
- `/pull forge` takes the engine only.
- `/pull my-project` takes that one project.

## What happens

1. Claude reads the state of each repository in scope against its
   origin, and says it as a fact. The words are: up to date, behind,
   ahead, diverged, no origin, not under git.

   You should now see one state for each repository in scope.

2. A repository with unsaved changes, or with a diverged history, stops
   here with one offer, and nothing is pulled from it. The offer is
   one of these:
   - `/save` first, to save the unsaved work (see
     [Save your work](save-your-work.md)).
   - A merge by hand.
   - `/save`, which rebases your commits onto the remote.

   You should now see the offer named against the repository it
   concerns. When the save of a diverged repository meets a conflict,
   see [Settle a conflict](settle-a-conflict.md).

3. For each repository that is clean and behind, Claude fast-forwards
   it, which only moves your copy forward to the remote's and never
   creates a merge. It reports where the repository moved from and to,
   and the subjects of the commits between.

   You should now see a line `pulled <from> -> <to>`, then the commit
   before and after, then the list of commits between.

4. After a pull of the engine, Claude reads the release notes and shows
   the "Action required" lines of every release whose commit the pull
   listed. It then offers two checks for each project you keep: the
   light check and the project check. It runs them only on your word.

   You should now see the "Action required" lines of the releases you
   crossed, and the offer of the two checks.

5. Where an "Action required" line names a migration, Claude offers
   `/migrate <slug>` for each project of the old shape. See
   [Migrate a project](migrate-a-project.md). What to do after a pull
   of the engine as a whole is told in
   [Upgrade the engine](upgrade-the-engine.md).

   You should now see a migration offered for each project that needs
   one.

6. After a pull of a project, Claude reports what the script printed.

   You should now see the same from-and-to report for the project.

## What you have afterwards

Every repository that was clean and behind is at the remote's latest
commit. Every other repository is as it was, with its state named and,
where it needs one, its offer. Nothing was merged, and no check ran
unless you said so. The forge never pulls or merges on its own
judgement. The reason it looks and offers is told in
[Persistence in git](../about/persistence-in-git.md).

## If something goes wrong

The pull script refuses in these cases. In every one, nothing is
pulled from that repository.

- Unsaved changes. The script prints `has unsaved changes:` and the
  changed files. Bare, it then says `skipped` and goes on to the next
  repository. With a slug, it stops with `Run scripts/forge-save.py
  first, then pull.` Save your work, then pull again.
- No origin. The script prints `no origin - skipped`. Bare, it goes
  on. With a slug, it stops. A project without a repository, or
  without an origin, has nothing to pull.
- Diverged history. Your commits and the remote's commits both exist
  and neither contains the other. The script stops with `Pull failed
  in <name> - local and remote history diverged; nothing pulled. Merge
  by hand, or scripts/forge-save.py rebases your commits onto the
  remote.` Save with `/save` to rebase your commits onto the remote, or
  merge by hand.

A repository that is ahead of its origin has nothing to pull: the
state is reported, and the commits wait for your next save.

## A worked example

You type:

```
/pull
```

Claude reports the states: the engine is behind, `my-project` is clean
and up to date, and `other-project` is diverged. It stops on
`other-project` with its offer and pulls nothing there. For the engine
it pulls and reports `pulled <from> -> <to>`, with the commits between.
Two of them read as releases. It shows their "Action required" lines;
one names a migration. It offers the two checks on `my-project` and
`/migrate my-project`, and waits for your word on each.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
