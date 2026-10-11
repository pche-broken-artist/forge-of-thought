---
description: Look at the remote and pull a clean repository that is behind; after a pull of the engine, the Action required lines crossed and the offer of the checks
argument-hint: "[project-slug]"
disable-model-invocation: true
---

Pull the forge from its remotes through `scripts/forge-pull.py`
(POS.1490, SOL.0180): the scripts are the only door to git (CLAUDE.md,
Persistence). The forge looks and offers; it pulls only what is clean
and behind, merges nothing and runs no check unasked. `$0` is one
repository (`forge` = the engine, a slug = that project); bare = the
engine and every project with an origin.

1. Run `python scripts/forge-status.py --remote` and report the state
   of each repository in scope in the words of POS.1490: up to date,
   behind, ahead, diverged, no origin, not under git. A repository
   with unsaved changes or with a diverged history stops here, with
   its one offer: `/save` first, or a merge by hand or by `/save`
   (which rebases the user's commits onto the remote). Nothing is
   pulled from it.
2. For what is clean and behind, run `python scripts/forge-pull.py
   $ARGUMENTS` and relay its report: where each repository moved from
   and to, and the subjects of the commits between.
3. After a pull of the engine, read `RELEASE-NOTES.md` and show the
   Action required lines of every release whose commit the script
   listed (`release <version>`); then offer `/check light <slug>` and
   `/check project <slug>` on each project the user keeps (POS.0940),
   and run them only on his word.
4. After a pull of a project, report what the script printed.
