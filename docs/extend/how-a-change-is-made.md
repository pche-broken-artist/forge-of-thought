---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 8df92ee637fd5ef2
inputs:
  - CLAUDE.md#The system's own project
  - CLAUDE.md#Versioning & status
  - projects/README.md
  - projects/forge/10-intent.md#POS.0720
  - projects/forge/10-intent.md#POS.0900
  - projects/forge/10-intent.md#POS.1440
  - projects/forge/10-intent.md#POS.1780
  - projects/forge/10-intent.md#POS.1930
  - projects/forge/10-intent.md#POS.1980
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/test/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - projects/forge/recipes/contributing.md#Instructions
  - projects/forge/40-solution-design.md#SOL.0450
  - projects/forge/40-solution-design.md#SOL.0930
  - .claude/skills/render/SKILL.md
---

# Make a change to the forge

A change to the forge is a change of how the forge behaves, or of a
file it is made of, and it travels the forge's own chain before it is
built: a position in the forge intent, an item in the solution
design, then the files that do the work. This page is for you, the
extender: someone who wants the forge to do something differently,
in your own clone or in the public engine. It says where each kind of
change goes, what proves it, where it is recorded and how it is
released. The reasons behind this order are on the explanation pages
linked at the end; this page is the path.

## When to use it

Use this page when you want to change what the forge does: a
command, a rule, a convention, what a reviewer looks for. Such a
change goes through the chain before it is built.

The line between the two kinds of change is drawn by what the change
does, never by its size. A change that alters no behaviour, such as a
wording, a broken path or a slip, does not go through the chain. It
is made directly in the file and sent as it is; nothing else is
needed.

A fix of a generated file is a change of what generates it.
`README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md` are renders,
never edited by hand: the change goes into the recipe in
`projects/forge/recipes/` or into what the recipe reads. The pages of
`docs/` are generated the same way by `/document`: a fix goes into
the file the page mirrors ([Change a documentation
page](change-a-documentation-page.md)).

If you only want to say something, report a defect or bring an idea,
`CONTRIBUTING.md` in the engine root names the channel for each kind.
The easiest way to a change of behaviour is a discussion first.

## What you do

The commands, in the order a change meets them. `forge` is the slug
of the forge's own project; in a command over documents it names
that project, in a command of git it names the engine and the
project together.

```
/import-project <git-url>
python scripts/forge-branch.py forge <name>
/forge intent forge
/forge solution-design forge
/test
/check engine
/check single-source-of-truth
/render contributing
/release forge
```

- `/import-project <git-url>` clones the forge's own project beside
  the engine. Its address stands in `projects/README.md`.
- `python scripts/forge-branch.py forge <name>` makes a branch for a
  change of more than a few lines.
- `/forge intent forge` writes the position: what is wanted and why.
- `/forge solution-design forge` writes the item of the design: what
  the change solves and the choice it rests on.
- `/test` runs the engine's tests; `python -m pytest` from the engine
  root is the same thing.
- `/check engine` verifies the engine against itself and against the
  forge intent.
- `/check single-source-of-truth` verifies that every rule is written
  in one place; run it before a major or after a round on the
  operating layer.
- `/render contributing` regenerates `CONTRIBUTING.md`; a release
  does not.
- `/release forge` releases the engine and the project as two
  commits, the tests first.

## What happens

1. **Have both repositories.** The engine is one git repository. The
   thinking behind it, the forge intent and the solution design, lives
   in the forge's own project, `projects/forge`, a repository of its
   own that whoever develops the engine clones beside it; a user of
   the engine never needs it. Bring it in with
   `/import-project <git-url>`, the address taken from
   `projects/README.md`: the command asks for your word, clones
   through `scripts/forge-clone.py` into `projects/forge`, reports the
   commit identity git resolves and recommends `/forge forge` as the
   first act ([Bring in an existing
   project](../use/bring-in-an-existing-project.md)). The author's
   commands read that clone: `/check engine`, `/document`,
   `/release forge`, `/new-artefact` and the renders of the README,
   the release notes and CONTRIBUTING. You should now see
   `projects/forge/10-intent.md` and
   `projects/forge/40-solution-design.md` beside the engine.

2. **Decide the kind of change.** A change of behaviour takes the
   steps below. A change that alters no behaviour skips to step 6:
   make it in the file, try it, send it. You should now see which of
   the two ways your change takes.

3. **Make a branch for a larger change.** For a change of more than a
   few lines, run `python scripts/forge-branch.py forge <name>`, work
   and `/save` on that branch, and later send the pull request from
   it, so that your fork's `main` stays clean for the upgrades of the
   engine; the branch goes away with the merge ([Work on a
   branch](../use/work-on-a-branch.md)). You should now see the new
   branch as the one checked out in both repositories.

4. **Write the position first.** Run `/forge intent forge`. In your
   own clone you are the principal (the person whose thinking is
   being forged), so the working conversation is yours: Claude
   proposes and you decide. The round ends in one write on your
   confirmation: the position in `projects/forge/10-intent.md`, one
   version bump, and one record per change in the companion
   `projects/forge/10-intent.history.md`. The reason for the change,
   what was said and what turned it go into the record, never into
   the position ([Forge the intent](../use/forge-the-intent.md)).
   Where a change of the operating layer needs a test, the order
   differs: a brief first, in the principal's words, then the build
   and its test, then the rounds of the intent and the design right
   after it, never across a release. You should now see the intent at
   a new version and its record in the companion.

5. **Write the design item.** Run `/forge solution-design forge`. The
   item in `projects/forge/40-solution-design.md` says what the
   change solves, what it realises, the choice it rests on and where
   it lives; its record goes into
   `projects/forge/40-solution-design.history.md` in the same step.
   You should now see the item and its record.

6. **Change the operating layer.** The operating layer is `CLAUDE.md`,
   the skills under `.claude/skills/`, the agents under
   `.claude/agents/`, the templates under `templates/` and the scripts
   under `scripts/`, all in the engine. A script is changed with its
   test in `tests/`, beside the scripts it tests; a change of a render
   goes into its recipe; a fix of a documentation page goes into the
   file the page mirrors. You should now see the changed files and,
   for a script, a test beside it.

7. **Prove it.** Run `/test`: it runs `python -m pytest -q` from the
   engine root on copies of the fixture in a temporary directory,
   never on a repository of the forge, and reports the sum as pytest
   prints it; a red test is reported word for word and nothing is
   fixed on this command's word ([Run the
   tests](../use/run-the-tests.md)). Run `/check engine`: it verifies
   the commands table against the skills, the scripts on disk against
   `CLAUDE.md`, the README against `CLAUDE.md`, the templates against
   the conventions, and every position of the forge intent against
   the engine, with nothing withdrawn still advertised. Before a major
   or after a round on the operating layer, run
   `/check single-source-of-truth`: it reads the whole operating layer
   and finds every rule, procedure or file shape written in two
   places, and every direct operation where a mechanism exists. The
   checks are advisory: findings are settled by walkthrough, the
   forge's way of working a list one item per message ([Check
   conformance](../use/check-conformance.md)). You should now see the
   sum of the tests and either that the checks passed or a report of
   findings.

8. **Check the record.** Every versioned document you changed, the
   intent, the design and any recipe among them, keeps its history in
   an append-only companion `<file>.history.md` beside it, one record
   per change, written in the same step as the change. What the user
   must do after a change stands in the record's `Action` field. The
   log is the single primary: the commit messages and the release
   notes are derived from it. You should now see one record for each
   change you made, `Was` included.

9. **Save and send.** `/save` commits and pushes on the branch you are
   on; in your clone it pushes to your fork. A pull request for a
   change of behaviour carries the position with its record, the
   design item, the change itself and one line on what you ran, a
   script's test among it. Where the change touches both repositories
   it is two pull requests, one on the engine with the change itself
   and one on the forge's own project with the position and the
   design item, each naming the other. Everything that enters the
   forge's own project is English, a brief included; a brief sent in
   another language is translated at the merge and its original stays
   in git. Try your change yourself before you send it; a change
   written with an AI is welcome on the same rule. In your own clone
   you decide everything; what is merged into the public engine its
   author decides. You should now see your pull request, or two that
   name each other.

10. **Merge and release.** Two pull requests are merged both or
    neither, in one sitting, the project first and the engine second
    and no release between them, since git merges no two repositories
    as one; one of them declined means both closed with the reason.
    The release is `/release forge`, from `main` only ([Release a
    version](../use/release-a-version.md)). It runs the tests first,
    before any check, and a red test stops it. Then the checks:
    `engine` on the engine root, `light` and `project` on
    `projects/forge`. Then it reports the age of the documentation
    and offers `/document` in one sentence; it regenerates the pages
    only on the principal's word. Then it regenerates the README and
    the release notes from their recipes, always, and writes the
    state render. Then it saves with the message
    `release <intent version>: <one line>`, the engine and the
    project as two commits, and proposes the tag `v<major>` at an
    approved major. `CONTRIBUTING.md` is not regenerated by a release:
    that is `/render contributing`, on the principal's word ([Render
    an output](../use/render-an-output.md)). You should now see two
    commits, one in each repository, and a regenerated `README.md` and
    `RELEASE-NOTES.md` in the engine root.

## What you have afterwards

- The forge intent says what the forge now does and the record beside
  it says why.
- The solution design says what realises it and where.
- The operating layer does it; a changed script has its test, green.
- The history companions carry one record per change, and the
  release notes derive from them.
- The README is re-rendered. A process change is complete only once
  the intent is updated and the README re-rendered.
- The pull request carries no release and no regenerated README,
  release notes or documentation: the author makes those at the next
  release.

## If something goes wrong

- `/import-project` stops when `projects/<repository name>` already
  exists. When git resolves no identity on your host, it says so:
  `forge-save` commits nothing until git resolves one.
- `/test` says `No module named pytest` when pytest is missing;
  install it with `python -m pip install pytest`, the one thing a
  contributor installs beyond `python`. A red test is a round of its
  own: the script is changed with its test.
- `/release` on a branch other than `main` stops and names the way
  back, `python scripts/forge-branch.py forge main` after saving. A
  repository behind or diverged from its origin is refused with the
  offer of `/pull`.
- A red test stops the release; the failures come back as `/test`
  reports them, and the release does not run. Where pytest is not
  installed the release says the tests did not run and goes on only
  on the principal's word.
- A finding of a check at the release is settled by walkthrough; a
  finding the principal has not settled when he orders the release to
  go on is parked by that word, said aloud. A recipe that is missing
  is reported and the repository is released without that render.
- `/render` for a recipe that does not exist offers to compose it
  through `/recipe` and stops. After a render, a hit of the scan for
  instance facts is said aloud; an instance fact is regenerated out,
  never edited by hand.
- One of two pull requests declined means both are closed, with the
  reason.

## A worked example

An invented change, traced through. Suppose you want `/end` to name
the branch each repository is on when it reports unsaved changes.
That is a change of behaviour, so it goes through the chain. Nothing
of it is a script, so no test is needed and the order is the plain
one.

1. You have the engine and, beside it, `projects/forge`, brought in
   with `/import-project <git-url>` from the address in
   `projects/README.md`.
2. The change is a few lines in one skill, so you stay on `main`.
3. `/forge intent forge`: one round, one position saying that `/end`
   names the branch beside each unsaved repository, with its reason
   in the record of `projects/forge/10-intent.history.md`. You confirm
   the write; the intent moves one version.
4. `/forge solution-design forge`: one item saying that the `/end`
   skill reads the branch from the state script and names it, with
   the choice it was made against, and where it lives,
   `.claude/skills/end/SKILL.md`. Its record goes into
   `projects/forge/40-solution-design.history.md`.
5. You change `.claude/skills/end/SKILL.md` in the engine.
6. `/test` reports the sum of the suite as pytest prints it;
   `/check engine` reports that the checks passed.
7. You try `/end` yourself and see the branch named.
8. `/save forge` commits and pushes both repositories. Two pull
   requests, one on the engine with the skill, one on the forge's own
   project with the position and the item, each naming the other, and
   one line in each on what you ran.
9. The author merges the project first, then the engine, and runs
   `/release forge`: the tests, the checks, the offer of `/document`,
   the README and the release notes regenerated, two commits.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Bring in an existing project](../use/bring-in-an-existing-project.md):
  cloning the forge's own project beside the engine with
  `/import-project`.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Run the tests](../use/run-the-tests.md): running the tests.
- [Release a version](../use/release-a-version.md): the release.
- [Work on a branch](../use/work-on-a-branch.md): the branch a larger
  change is made on.
- [Render an output](../use/render-an-output.md): regenerating a
  render such as CONTRIBUTING from its recipe.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Change a documentation page](change-a-documentation-page.md): how a
  fix of a page is made through the file the page mirrors.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  the forge's own project is a repository of its own beside the
  engine.
- [The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md):
  the two fixed files the contributing file points at.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
