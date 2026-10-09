---
generated: 2026-10-09
made: derived
inputs-hash: fdee7c5700cada6b
inputs:
  - scripts/forge-pull.py
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/recipes/release-notes.md
---

# Upgrade the engine

This page is for the user who has cloned the engine and wants to
take the latest release. It says how the upgrade is pulled, what it
does and does not touch, and how a project is brought to the newer
conventions afterwards, step by step. It was put together from the
help header of `scripts/forge-pull.py`, the Persistence section of
`CLAUDE.md`, the forge intent and the recipe of the release notes.

## Before you pull

The pull is a fast-forward only, and it never touches a repository
with unsaved changes. Save first: a repository with uncommitted work
is reported and skipped in the bare form, and refused when you name
it by slug. This is deliberate, so that a pull can never create a
conflict in half-finished work. How to save is on
[Save your work](save-your-work.md).

What you need: Python 3.8 or newer, run as `python`, and `git` on
PATH.

## Step 1: pull

Run, from the engine root:

```
python scripts/forge-pull.py forge
```

This fast-forwards the engine from its remote. The engine's remote is
its upgrade channel; `main` is the released line.

The script has three forms:

- `python scripts/forge-pull.py`: bare, pulls the engine and then
  every project under `projects/` that has an origin configured. A
  project without a repository, or with a repository and no origin,
  is reported and skipped.
- `python scripts/forge-pull.py forge`: the engine alone. This is the
  upgrade.
- `python scripts/forge-pull.py <slug>`: one project,
  `projects/<slug>`.

What you see: one line per repository, `up to date` when the pull
succeeded, `no origin - skipped` or `has unsaved changes` followed by
the list of changed files when it was left alone. If the pull fails
because local and remote history have diverged, the script stops and
tells you to run `scripts/forge-save.py` or ask Claude.

Projects are untouched by an upgrade of the engine. Each project is
a repository of its own, which the engine does not know, and a
project records no engine version.

## Step 2: read the release notes

Open `RELEASE-NOTES.md` in the engine root. It has one section per
release, newest first, written for the user who takes upgrades
through `forge-pull`. In every section the group `Action required`
stands first: what changed, then "For you:" and what to do in your
projects after pulling. Read those lines first; the groups Added,
Changed, Removed, Fixed and Rejected follow.

## Step 3: check each project

Since a project records no engine version, the way to learn what the
new conventions mean for it is to measure it against them. For each
project you want to bring forward, run

```
/check light <slug>
/check project <slug>
```

Each check compares the project with the current conventions and
reports what no longer conforms. Running a check and settling what
it finds is on [Check conformance](check-conformance.md).

## Step 4: migrate on your word

The findings are walked one at a time, and Claude migrates the
project in the session, on your word. There is no migration tool;
this is a knowing choice. The whole migration path of any instance
is the same: pull, read the Action required lines, check each
project, decide.

## A project you leave as it is

Bringing a project to newer conventions is a decision made per
project, never assumed. A project left as it is remains valid under
the conventions it was written to: a check on a finished or dormant
project may report nonconformance, and that is a fact to report, not
a defect to chase.

## See also

- [Check conformance](check-conformance.md): running a check and settling its findings.
- [Save your work](save-your-work.md): saving before a pull.
