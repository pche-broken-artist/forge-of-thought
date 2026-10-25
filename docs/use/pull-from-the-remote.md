---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 7070c13547e994e6
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` brings the latest work from the remote into your copy of the engine and of your projects. It is for you, the principal (the person whose thinking is forged), whenever you want to know where your repositories stand against their remotes, or to take in an upgrade of the engine. It looks first, pulls only what is clean and behind, and never merges.

## When to use it

- You want to upgrade the engine. The engine's remote is its upgrade channel.
- A colleague works on the same project and you want to take in what they saved.
- You want to know whether a repository is behind, ahead or diverged, before you decide anything.

## The command

```
/pull [slug]
```

- Bare `/pull` covers the engine and every project that has an origin (the remote a repository was cloned from or linked to).
- `/pull forge` covers the engine only.
- `/pull my-project` covers that one project.

## What happens

1. Claude reports the state of each repository in scope against its origin, as a fact. It fetches the origin to do so, which changes nothing in your files. The states are:
   - up to date
   - behind
   - ahead
   - diverged
   - no origin
   - not under git

   You should now see one state for every repository in scope.

2. A repository with unsaved changes, or one whose history has diverged from its origin, stops here with one offer. Nothing is pulled from it. The offer is one of these:
   - `/save` first, so that the work is saved and the repository is clean.
   - A merge by hand.
   - `/save`, which rebases your commits onto the remote.

   You should now see the repository named with its offer, and your files untouched.

3. For every repository that is clean and behind, Claude pulls by fast-forward, which only moves your copy forward to what the remote already has. It reports where each repository moved from and to, with the commit before and after, and the subjects of the commits between. You should now see a line of the form "pulled <old> -> <new>" for each repository that moved, and "up to date" for one that had nothing new.

4. After a pull of the engine, Claude reads the release notes and shows the Action required lines of every release the pull crossed. It then offers two checks on each project you keep: the light check and the project check. It runs them only on your word. You should now see the Action required lines, and the offer of the checks.

5. Where an Action required line names a migration, Claude offers `/migrate my-project` for each project you keep that is still of the old shape. You should now see one such offer per project that needs it. The migration itself is described in [Migrate a project](migrate-a-project.md).

6. After a pull of a project, Claude reports what the script printed. You should now see the same "pulled" report as for the engine, without the release steps.

The forge never pulls or merges on its own judgement. It looks and offers, and you decide.

## What you have afterwards

- Every clean repository that was behind is level with its origin.
- Every other repository is as it was, with its state named and one offer made.
- After an engine pull, you know which releases you crossed and what each asks of you. [Upgrade the engine](upgrade-the-engine.md) says what to do next.

## If something goes wrong

The script refuses in these cases. Each time nothing is pulled.

- **Unsaved changes.** A bare pull lists the changed files and skips that repository. A pull of one named repository stops with: "Run scripts/forge-save.py first, then pull." Save first, as [Save your work](save-your-work.md) describes, then pull again. This is so that a pull can never create a conflict in half-finished work.
- **No origin.** A bare pull says "no origin - skipped" and goes on. A pull of one named repository stops with the same message. The repository has no remote to pull from.
- **Diverged history.** The script stops with: "Pull failed ... local and remote history diverged; nothing pulled." Either merge by hand, or save, which rebases your commits onto the remote. If that save meets a conflict, [Settle a conflict](settle-a-conflict.md) says how to go on.
- **Not under git.** A project outside git is reported as such and is left alone.

## A worked example

You run `/pull` bare. Claude reports three repositories: the engine is behind, `my-project` is up to date, and `other-project` has unsaved changes.

Claude pulls the engine and prints:

```
forge: pulled 1a2b3c4 -> 5d6e7f8
   before: 1a2b3c4 <subject>
   after:  5d6e7f8 <subject>
   commits between:
  <subject of a commit>
  release <version>
```

It leaves `other-project` alone, with the offer to save first. It shows the Action required line of the release it crossed, and that line names a migration. Claude offers the light check and the project check on `my-project`, and `/migrate my-project`, and waits for your word on each.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine.
- [Migrate a project](migrate-a-project.md): the migration a release may ask for.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Settle a conflict](settle-a-conflict.md): what to do when the save of a diverged repository meets a conflict.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
