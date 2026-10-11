---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: e68f16625297e1bc
inputs:
  - .claude/skills/pull/SKILL.md
  - scripts/forge-pull.py
  - scripts/forge-status.py
---

# Pull from the remote

`/pull` looks at the remote of the engine and of your projects, says the state of each as a fact, and brings in what is new only where that is safe. It is for you, the principal (the person whose thinking is forged), when you want the latest engine or the latest of a project that has an origin (the remote repository it was cloned from or pushes to). Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## When to use it

- You want the newest engine: it is upgraded by pulling it.
- You work on a project from more than one place and want what the other place saved.
- You want to know whether your repositories are behind, ahead or diverged, without changing anything.

## The command

```
/pull [slug]
```

- Bare: the engine and every project that has an origin.
- `forge`: the engine only.
- A slug: that one project.

## What happens

1. Claude reads the state of each repository in scope against its origin and says it in one of six words: up to date, behind, ahead, diverged, no origin, not under git. Looking fetches from the origin and changes nothing in your working files.

   You should now see one state per repository.

2. A repository with unsaved changes, or one whose history has diverged from its origin, stops here. Claude gives it one offer and pulls nothing from it:
   - unsaved changes: `/save` first, then pull (see [Save your work](save-your-work.md));
   - diverged: merge by hand, or let `/save` rebase your commits onto the remote.

   You should now see the offer in place of a pull for that repository.

3. For each repository that is clean and behind, the pull script fast-forwards it. It only moves the repository forward to what the origin has and never merges.

   You should now see, for each repository, where it moved from and to (the earlier and the later commit, each with its subject) and the subjects of the commits between.

4. After a pull of the engine, Claude reads `RELEASE-NOTES.md` and shows the "Action required" lines of every release the script listed among the commits between. Then it offers `/check light <slug>` and `/check project <slug>` on each project you keep. It runs them only on your word.

   You should now see the actions the new releases ask of you, and the offer of the two checks. What to do next, project by project, is on [Upgrade the engine](upgrade-the-engine.md).

5. After a pull of a project, Claude reports what the script printed.

   You should now see the same from-and-to report for that project.

## What you have afterwards

- The repositories that were clean and behind are at the state of their origin.
- Every other repository is as you left it, with its state said.
- Nothing is merged and no check has run unless you asked for it. The forge never pulls or merges on its own: it looks and offers. The reason is on [Persistence in git](../about/persistence-in-git.md).

## If something goes wrong

The pull script prints these. Bare, it reports a repository and goes on to the next. With a slug it stops.

| Message | Meaning | What you do |
|---|---|---|
| `<name>: no origin - skipped` | The repository has no origin. | Nothing to pull. With a slug this is a refusal. |
| `<name>: has unsaved changes:` followed by the list of changes, then `skipped` | A pull could create a conflict in half-finished work. | Run `/save`, then pull again. With a slug the script stops with "Run scripts/forge-save.py first, then pull." |
| `Pull failed in <name> - local and remote history diverged; nothing pulled.` | Your commits and the origin's have both moved. | Merge by hand, or let `/save` rebase your commits onto the remote. |

A project that has no repository is reported as not under git and skipped.

## A worked example

You have the engine and a project, `<slug>`, both with an origin. The project has unsaved edits.

1. You type `/pull`.
2. Claude says: the engine is behind, `<slug>` has unsaved changes. It offers `/save` for `<slug>`, pulls nothing there, and goes on with the engine.
3. The script fast-forwards the engine and prints the earlier commit, the later commit and the subjects between, among them one that names a release.
4. Claude shows that release's "Action required" lines from `RELEASE-NOTES.md` and offers `/check light <slug>` and `/check project <slug>` for `<slug>`.
5. You answer `/save`, then `/pull <slug>`. The project is up to date, and you say whether to run the checks.

## See also

- [Upgrade the engine](upgrade-the-engine.md): what to do after a pull of the engine, project by project.
- [Save your work](save-your-work.md): the save that must come first on unsaved work.
- [Persistence in git](../about/persistence-in-git.md): why the forge looks at the remote and offers, never pulls on its own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
