---
generated: 2026-10-09
made: mirrored
inputs-hash: 35a909fbea89b846
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - CLAUDE.md
---

# Save your work

This page is for a person who has worked on the engine or on a project and wants the work committed and pushed. `/save` is the quick door: a light check, a commit message you confirm, then the commit and the push, on whatever branch is checked out.

## The command

```
/save [slug] [-m "message"] [--tag name]
```

- `slug`: save one repository only. `forge` means the engine. Without a slug every repository with changes is saved.
- `-m "message"`: your own commit message. Without it, one is drafted for you.
- `--tag name`: tag the commit. A tag needs one repository, so a slug is required with it.

## What happens

1. **Scope.** The status script reports the engine and each project separately, with the branch each is on. A project that is not under git is named in the report and otherwise left alone. That is a property of the project, not a defect.
2. **The light check.** The `light` check runs on every repository in scope, and its findings are settled through `/check`. A save never waits on a finding you have not asked to fix.
3. **The commit message.** Unless you gave `-m`, a one-line English message is drafted from the records the round appended to the histories of the documents it touched, and proposed to you. The commit uses the wording you confirm or adjust. When more than one repository has changes you get one message per repository, or you run the save once per slug. The script's own message, a list of the changed files, is used only if you say so.
4. **A tag, only on your word.** A tag is set only if you give `--tag name` or ask for one in words. If you ask without naming it, a name is proposed from the version of that repository's intent, and you may take it or give any name you like. A tag that already exists is refused and nothing is changed.
5. **The save script.** It stages everything in the repository, commits, and pushes. If the remote has changes of its own, they are integrated first. No render is made.

## What you see

For each repository the script prints the commit and its file summary, and the tag if one was set. The outcome is one of these:

- saved and pushed to the remote;
- nothing to save, when the repository is clean;
- not pushed, when no remote is configured: the commit (and tag) stays local;
- a project named as not a repository, when you asked for it by slug: it is refused until the repository exists.

If the remote's changes conflict with yours, the script stops and says nothing was lost. Ask Claude for help before doing anything else. If the push fails, check the network and the access to the remote, then save again.

## When nothing is committed

The script commits nothing in a repository where git resolves no commit identity for this host. It says so and moves on. Run `/setup` for the per-host identity, or set a local one for that repository, then save again.

When there is nothing to commit but you gave a tag, the current state is tagged, so a tag can mark a state before a large change.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [About persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
