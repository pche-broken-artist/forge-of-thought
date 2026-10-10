---
generated: 2026-10-10
made: derived
inputs-hash: b455ca11ddf32f34
inputs:
  - scripts/forge-pull.py
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/recipes/release-notes.md
---

# Upgrade the engine

This page is for the user who has cloned the engine and wants to
bring it to its latest release, and then wants to know what that
means for the projects he keeps. It was put together from the help
header of `scripts/forge-pull.py`, the Persistence section of
`CLAUDE.md`, the engine's intent and the release-notes recipe.

## What an upgrade is

The engine is one git repository with a remote, and its `main`
branch is the released line. Upgrading means fast-forwarding your
copy of the engine to that line with `scripts/forge-pull.py`: the
engine's own remote is its upgrade channel. Nothing else is
involved: there is no installer and no migration tool, and that is
by design.

Your projects are repositories of their own, which the engine does
not know. A pull of the engine does not touch them, and a project
records no engine version anywhere. What ties a project to the
engine is only the conventions it was written to, and those are
measured, not stored (see "After the pull").

## Step 1: save first

The pull refuses to touch a repository that has unsaved changes, so
that a pull can never land in half-finished work. Save what you have
first, in the engine and in any project you want pulled: how is
[Save your work](save-your-work.md).

## Step 2: pull

Run, from the engine root:

```
python scripts/forge-pull.py forge
```

`forge` names the engine alone: this is the plain upgrade. The pull
is fast-forward only, on whatever branch is checked out. You see
one line per repository: `up to date` in green when it went through.

The bare form pulls the engine and then every project under
`projects/` that has an origin configured:

```
python scripts/forge-pull.py
```

With a project's slug it pulls that one project:

```
python scripts/forge-pull.py <slug>
```

What happens when a repository is not clean depends on the form:

- Bare: a repository with unsaved changes is reported, its changed
  files listed, and skipped; the run goes on with the next one. A
  project without a repository, or without an origin, is reported
  and skipped as well.
- With a slug (`forge` included): the same situation is a refusal.
  The script stops and tells you to run `scripts/forge-save.py`
  first, then pull again.

If the pull fails because your local history and the remote's have
diverged, the script says so and points you to `forge-save.py`,
which reconciles both, or to asking Claude.

The script needs Python 3.8 or newer, `git` on PATH and
`forge_repos.py` beside it; it carries no address and no identity of
its own.

## Step 3: read the release notes

After the pull, open `RELEASE-NOTES.md` in the engine root. It is
written for exactly this moment: one section per release of the
engine, newest first, for the user who takes upgrades through
`forge-pull`. In every section the Action required lines stand
first: each one says what changed and, after "For you:", what to do
in your projects now that you have pulled. Read those first; the
rest of a section tells you what was added, changed, removed, fixed
or rejected, and what each means for you.

## After the pull: project by project

Because a project records no engine version, the way to learn what
the new conventions mean for it is to measure it. For each project
you want to bring along, run in the session:

```
/check light <slug>
/check project <slug>
```

Each check compares the project against the current conventions
and reports what no longer conforms. The two checks own different
concerns, so run both. What a check is and how its report is
settled is [Check conformance](check-conformance.md).

The findings are then walked one at a time: Claude presents each
one, you give the verdict, and on your word Claude makes the
change in the session. That is the whole migration path, for every
instance alike. There is no migration tool, knowingly: the release
notes say what to do, the checks say where, and Claude does it on
your word.

## A project you leave as it is

You do not have to migrate. Conventions evolve continuously and the
checks always measure against the current ones, but a project stays
valid under the conventions it was written to. Nonconformance of a
finished or dormant project is a fact the check reports, never a
defect to chase. Bringing a project to newer conventions is an
explicit decision, made per project and never assumed.

## See also

- [Check conformance](check-conformance.md): running a check and settling its findings.
- [Save your work](save-your-work.md): saving before a pull.
