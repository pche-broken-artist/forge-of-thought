---
generated: 2026-10-10
made: mirrored
inputs-hash: f5b1b0bb95da1f9e
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - CLAUDE.md
---

# Save your work

This page is for the person who has finished a round of work and wants
it kept in git. It shows what `/save` does, in order, and what you are
asked along the way.

The command is `/save [slug] [-m "message"] [--tag name]`. It commits
and pushes on whatever branch is checked out. It makes no render.

## What you do

1. **Run `/save`.** Name a project by its slug (`<slug>`) to save that
   one repository, or use `forge` for the engine. Give no slug and
   every repository with changes is visited.
2. **See the scope.** The command first reads the state from the
   status script. It reports the engine and each project separately,
   each with the branch it is on. A project that is not under git is
   named in the report and left alone: that is a property of the
   project, not a defect.
3. **Let the light check run.** The `light` check runs on every
   repository in scope. Its findings are settled through `/check`. A
   save never waits on a finding you have not asked to fix.
4. **Confirm the commit message.** Unless you gave `-m`, a one-line
   English message is drafted from the records the round appended to
   the histories of the documents it touched. It is proposed to you,
   and the commit uses the wording you confirm or adjust. When more
   than one repository has changes, there is one message per
   repository, or you run the save once per slug. The script's own
   message, built from the list of files, is used only if you say so.
5. **Decide on a tag.** A tag is set only on your word: `--tag name`,
   or asked for in words. A tag needs one repository, so a slug.
   If you ask for a tag without a name, the version of that
   repository's intent is proposed as the name, and you may take it or
   give any name you like.
6. **The save runs.** Only now does the save script run.

## What the save script does

For each repository it stages everything and commits with the
confirmed message. When an origin is configured, it brings in remote
changes and pushes. It prints the commit's file summary and the tag.

What you may see instead:

- **Nothing to save.** The repository is reported as having nothing to
  save. If you asked for a tag, the current state is tagged instead,
  so a tag can mark a state before a large change.
- **No commit identity.** Where git resolves no identity for the host,
  nothing is committed in that repository. The report says to run
  `/setup` for the per-host identity or to set a local one.
- **A tag that exists.** An existing tag is refused and nothing is
  changed.
- **No origin.** The commit, and the tag if any, is kept locally and
  reported as not pushed.
- **A conflict with the remote.** Nothing is lost; the save stops and
  tells you to ask for help before doing anything else.
- **A project without a repository.** Bare, it is skipped with a note.
  Named by slug, it is refused, with the one-off step that makes it a
  repository.

The script never sets an identity or a remote, never initialises a
repository, and never forces a file into git or cleans anything.

## See also

- [Release a version](release-a-version.md): the other door, from
  `main`, with the renders.
- [About persistence in git](../about/persistence-in-git.md): why
  there are two doors and two speeds.
