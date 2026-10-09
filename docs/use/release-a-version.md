---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/release/SKILL.md
  - CLAUDE.md
---

# Release a version

This page is for a user who wants to release a repository: the engine
or one of its projects. It says what `/release` does, in order, and
where you decide.

```
/release [slug] [-m "message"] [-Tag name]
```

A release is always one repository, named by its slug (`forge` means
the engine). Without a slug the command asks which repository you
mean; it never sweeps all of them. A release differs from a save in
that it runs the checks and regenerates the README and the release
notes first; a save does neither.

## Steps

1. **Branch.** A release runs from `main` only. On any other branch
   the command stops, names the branch the repository is on and tells
   you how to get back (`./scripts/forge-branch.ps1 <slug> main`,
   after saving). Merging a branch into `main` is git's business, by
   hand or by merge request, never this command's.

2. **Checks.** The checks are launched at once and awaited together:
   `light` and `project` for a project; `light`, `engine` and
   `project` for the engine, the two project checks run on
   `projects/forge`. The result is always reported to you, even when
   clean. If there are findings, you settle them by walkthrough, one
   at a time. A finding may be parked and the release then goes on.
   Nothing is fixed silently, and the release does not proceed with a
   finding left unsettled. The checks come before the renders so that
   a fix made in the walkthrough is already in the inputs the renders
   draw on.

3. **Essence critique, offered once.** In one sentence the command
   offers `/critique essence`, the lens that guards what a release
   publishes against drift of the chain. If you say yes, it runs and
   its findings are settled by walkthrough before the release goes
   on. If you say no, or say nothing, no reviewer runs.

4. **README and release notes.** Once the findings are settled, both
   are regenerated from their recipes, every time, with no test of
   whether they are stale, through `/render`. The two renders are
   launched at once and awaited together. The command then reports
   the steps with a short summary of what materially changed in the
   regenerated files, and you rule on that change before anything is
   committed. If a project has no recipe for one of them, that is
   reported as a finding and the project is released without that
   render. Other renders are not regenerated here; their staleness
   shows on the `/forge` map and is yours to attend to.

5. **Save.** The command then runs `/save` for the repository. The
   commit message is

   ```
   release <intent version>: <one line>
   ```

   where the line sums up the rounds since the last release, taken
   from the intent's history. With `-m` your own message is used
   instead. For a library, whose history is git, the version is left
   out and the line describes what changed.

6. **Tag.** When the intent's version is an integer, an approved
   major, the tag `v<major>` is proposed and taken on your word. Any
   other tag is your own request, given with `-Tag name`. For a
   major of the forge intent the command first names what the intent
   asks a major to pass; this is a reminder on your word, not a gate.

## The check is advisory

The checks inform; they do not block. You may order the release at any
moment, whatever the findings.

## See also

- [Save your work](save-your-work.md): the save the release ends with.
- [Check conformance](check-conformance.md): the checks and how their
  findings are settled.
- [About renders and recipes](../about/renders-and-recipes.md): why
  the README and the release notes are renders.
