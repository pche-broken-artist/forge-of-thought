---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 65c36cb67496605a
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` looks at the remote of the engine and of your projects and
brings in what is clean and behind it. It is for the principal (whoever's
thinking is being forged) who wants the latest engine or the latest
state of a project that others also work on. Terms of the forge are
explained in the [Glossary](../reference/glossary.md).

## When to use it

- You want the newest engine, which is how an upgrade arrives.
- A project has an origin and someone else may have saved to it.
- You want to know where each repository stands against its origin and
  what waits on GitHub, before you decide anything.

The forge never pulls or merges on its own. It looks, reports and
offers; the pull runs because you typed `/pull`. The reason the forge
looks at the remote and offers is explained in
[Persistence in git](../about/persistence-in-git.md).

## The command

```
/pull [slug]
```

- Bare `/pull`: the engine and every project that has an origin.
- `/pull forge`: the engine and the forge's own project cloned beside it.
- `/pull my-project`: that one project.

## What happens

1. Claude reads the state of each repository in scope against its
   origin and reports it as a fact. The states are:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin
   - not under git

   You should now see one state for every repository in scope.

2. Beside each state Claude reports what waits on GitHub outside git:
   the open pull requests and the discussions nobody of the repository
   has answered. Where it cannot read them (no `gh` tool, an origin that
   is not GitHub, no login, no network) it prints one line saying so and
   why. Nothing of this is pulled, merged or answered.
   You should now see a `github:` line under each remote state, either
   the waiting items one per line or the one line of the reason.

3. A repository with unsaved changes or a diverged history stops here
   with its one offer, and nothing is pulled from it:
   - `/save` first, when there are unsaved changes (see
     [Save your work](save-your-work.md));
   - or a merge by hand;
   - or `/save`, which rebases your commits onto the remote.

   If the save meets a conflict, see
   [Settle a conflict](settle-a-conflict.md).
   You should now see the repository named with the offer, and no change
   in it.

4. For every repository that is clean and behind, the pull script
   brings it forward, without ever merging, and reports where it moved
   from and to and the subjects of the commits between.
   You should now see `pulled <from> -> <to>`, a `before:` and an
   `after:` line and the list of commits between. A repository already
   level reports `up to date`.

5. After a pull of the engine, Claude reads the release notes and shows
   the Action required lines of every release the pull crossed. It then
   offers two checks on each project you keep, the light check and the
   project check, and runs them only on your word.
   You should now see the Action required lines and the two offers.

6. Where an Action required line names a migration, Claude offers
   `/migrate <slug>` for each project of the old shape (see
   [Migrate a project](migrate-a-project.md)).
   You should now see one offer per project that needs it.

7. After a pull of a project, Claude reports what the script printed.

What to do after the engine has moved is on
[Upgrade the engine](upgrade-the-engine.md).

## What you have afterwards

- Every clean repository that was behind is level with its origin.
- Repositories with unsaved or diverged work are untouched, each with
  its offer.
- You hold the Action required lines of the releases crossed, and you
  decide on the checks and migrations.

## If something goes wrong

- `no origin - skipped`: the repository has no origin. With a bare
  `/pull` it is skipped; with a slug the pull stops.
- `has unsaved changes:`: the changed files are listed. With a bare
  `/pull` the repository is skipped; with a slug the pull stops with
  "Run scripts/forge-save.py first, then pull." Use `/save` first.
- `Pull failed in <name> - local and remote history diverged; nothing
  pulled.`: merge by hand, or use `/save`, which rebases your commits
  onto the remote.
- A repository that is not under git, or has no repository of its own,
  is reported and skipped.
- A conflict that `/save` meets is left standing and is settled as
  described in [Settle a conflict](settle-a-conflict.md).

## A worked example

You type `/pull` with two projects, `my-project` and `other-project`.

Claude reports: the engine is behind, `my-project` is up to date, and
`other-project` has unsaved changes. The `github:` line under the
engine names one open pull request; under `my-project` it says it could
not read GitHub because no login was found. Nothing was pulled, merged
or answered.

Claude pulls the engine and reports where it moved from and to, with
the commits between. It shows the Action required line of one release
crossed, which names a migration, and offers `/migrate my-project`. It
also offers the light check and the project check on both projects.
For `other-project` it offers `/save` first. You answer the offers one
by one; nothing runs without your word.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
