---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 3fc842cb455fbc73
inputs:
  - CLAUDE.md#The system's own project
  - CLAUDE.md#Versioning & status
  - projects/forge/10-intent.md#POS.0720
  - projects/forge/10-intent.md#POS.0900
  - projects/forge/10-intent.md#POS.1440
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - projects/forge/recipes/contributing.md#Instructions
---

# Make a change to the forge

A change to the forge is a change of how it behaves, and it is made
the way the forge makes every change: through its own chain of
documents before it is built, proved by its checks, recorded beside
the documents it touched and released from `main`. This page says
what you do, step by step, when you want the forge to behave
differently, whether in your own clone, where you decide everything,
or as a change you send to the public engine. It is written for the
extender: the person who changes a command, a rule, a convention or
what a reviewer looks for.

## When to use it

Use this page when your change alters what the forge does. The line
between the two kinds of change is drawn by what the change does,
never by its size:

- A change of how the forge behaves goes through the
  [chain](../reference/glossary.md): a command, a rule, a
  convention, what a reviewer looks for.
- A change that alters no behaviour is made directly: a wording, a
  broken path, a slip. Nothing of this page is needed for it. As a
  visitor, you send it as it is.

Three files of the engine are renders and are never edited by hand:
`README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md`. A render is a
file generated from a recipe, and a recipe is the versioned file that
says what the render is made from and how. A change to one of these
three goes into its recipe in `projects/forge/recipes/` or into what
the recipe reads; the file is regenerated at the next release. The
pages of `docs/` are generated the same way, by `/document`, from
the files that own each topic: a fix goes into the file the page
mirrors, and the page is regenerated (see
[Generate the documentation](../use/generate-the-documentation.md)).

The forge's own project is `projects/forge/`: the forge run through
its own process, with its brief, its intent, its solution design,
its decisions and its ledger (the single source of truth for the
project's state). Every step below works on that project. The slug
`forge` names it in every command.

## What you do

The commands, in the order you run them, with the one edit you make
by hand between them:

```
/forge intent forge
/forge solution-design forge
```

Then edit the file of the operating layer that carries the
behaviour: `CLAUDE.md`, a skill under `.claude/skills/`, an agent
under `.claude/agents/`, a template under `templates/` or a script
under `scripts/`. Then:

```
/check engine
/check single-source-of-truth
/release forge
```

`/check single-source-of-truth` is not run at every change: it fits
before a major or after a round on the operating layer. The rest
run every time.

## What happens

1. **You say what you want and why, and Claude writes the position.**
   Run `/forge intent forge`. Claude works the forge intent through
   its definition (see [Forge the intent](../use/forge-the-intent.md)):
   it asks, reflects back what it understood and asks whether to
   write. Before proposing a change to an existing position, it reads
   that position's history through `/history <ID>`. A change of
   substance goes into the intent first and propagates down the chain
   from there, whichever layer showed the need for it. On your word
   `write`, Claude writes the position and, in the same step, its
   record in the history companion beside the intent,
   `projects/forge/10-intent.history.md`: one record per change,
   `Was` included, its author the one who decided it. The reflection
   before the write shows you the new wording and the records.
   You should now see the position in `projects/forge/10-intent.md`,
   the intent's version bumped, its `last_change` derived from the
   new record, and the record in the companion.

2. **Claude writes the item of the solution design.** Run
   `/forge solution-design forge`. The solution design is the layer
   below the intent that says what realises what the intent wants.
   Claude writes the item where your change solves something, and its
   record in the companion beside it, in the same step.
   You should now see the item in `projects/forge/40-solution-design.md`
   and the record in `projects/forge/40-solution-design.history.md`.

3. **You change the operating layer.** Edit the file that carries the
   behaviour. Keep one rule in one place: a procedure, a rule set or a
   file shape that another file owns is cited by its path, never
   restated. A command table in `CLAUDE.md`, a skill, an agent and
   its front-matter, a template and a script's help header are all
   read by the checks of the next step. Where the operating layer and
   the intent differ after your edit, that difference is a finding of
   `/check engine`.
   You should now see the file changed and nothing of the old
   behaviour advertised anywhere else in the core.

4. **The checks prove the change.** Run `/check engine` (see
   [Check conformance](../use/check-conformance.md)). The check reads
   the core (`CLAUDE.md`, `templates/`, `.claude/skills/`,
   `.claude/agents/`, `scripts/`) and the forge intent with its
   threads and decisions, and verifies three things: the core agrees
   with itself (the commands table against the skills on disk, the
   agents against their files, every skill an agent names exists, the
   scripts on disk against `CLAUDE.md`, the templates against the
   conventions); every position is honoured by the core and nothing
   withdrawn is still advertised; and no old name from a recorded
   rename survives outside the historical records. Before a major, or
   after a round on the operating layer, also run
   `/check single-source-of-truth`: it reads the whole operating
   layer and verifies that every rule, procedure and file shape is
   written in one place and cited everywhere else, that a reviewer
   file carries only its front-matter and its Lens section, and that
   nothing operates directly where a mechanism exists. The result is
   reported to you always, even when clean. Findings are settled by
   walkthrough: one item per message, each closed with your verdict.
   You should now see either the statement that the check passed or
   its findings, one by one, waiting for your verdict.

5. **The release records and publishes the change.** Run
   `/release forge` (see
   [Release a version](../use/release-a-version.md)). It runs on
   `main` only. It runs the checks again: `engine` on the engine
   root, `light` and `project` on `projects/forge`, launched at once,
   settled by walkthrough. It offers `/critique essence` once, in one
   sentence, and runs it on your word only. Once the findings are
   settled it regenerates the README and the release notes from their
   recipes, always, and reports what materially changed in them: you
   rule on the delta before the commit. It then reports the age of
   the documentation, the `version` of `docs/README.md` against the
   intent's version, and offers `/document` in one sentence; on your
   word it runs it before the save, on your no, or silence, it runs
   nothing. A release never regenerates the documentation on its own.
   Then it saves with the commit message
   `release <intent version>: <one line>`, the line drawn from the
   records of the intent's history since the last release, and, when
   the intent's version is an integer, proposes the tag `v<major>`,
   taken on your word.
   You should now see the regenerated `README.md` and
   `RELEASE-NOTES.md`, the release commit on `main` and, at an
   approved major, its tag.

A process change is complete only once the intent is updated and the
README re-rendered. Until both are done, the change is not complete,
whatever the operating layer already says.

## What you have afterwards

In your own clone you have the whole change in one place each:

- the position in `projects/forge/10-intent.md`, saying what is
  wanted and why, with its record in the history companion;
- the item in `projects/forge/40-solution-design.md` where the change
  solves something, with its record;
- the changed file of the operating layer, in agreement with both;
- the check reports, where a check found something;
- the README and the release notes regenerated, the release saved
  and pushed from `main`.

The history log is the single primary record. The commit message of
the release and the release notes are derived from it, never the
other way round.

If you want the change in the public engine, `CONTRIBUTING.md` at
the engine root says how a visitor sends feedback, an idea or a
change. The easiest way is to open a discussion first. A pull request
for a change of behaviour carries:

- the position in `projects/forge/10-intent.md`, with its record in
  the history beside it;
- the item in `projects/forge/40-solution-design.md`;
- the change itself;
- one line on what you ran.

It does not carry a release, nor a regenerated README, release notes
or documentation: the author makes those at the next release. A
brief may come first and need not. Try your change yourself before
you send it. A change written with an AI is welcome on the same
rule, and the pull request says what was run. In your own clone you
decide everything, the forge there is yours. What is merged into the
public engine its author decides.

## If something goes wrong

- **`/release forge` stops before anything runs.** The repository is
  not on `main`. The release reports the branch it is on and how to
  get back: `python scripts/forge-branch.py forge main`, after
  saving. Merging a branch into `main` is git's business, by hand or
  by merge request, never the release's.
- **`/check engine` reports that a position is not honoured, or
  that something withdrawn is still advertised.** The operating layer
  and the intent differ. Settle the finding in the walkthrough and
  fix the side that is wrong: the intent first, where what is wanted
  changed; the operating layer, where the intent is right.
- **`/check engine` reports that the README contradicts `CLAUDE.md`
  or the intent.** That is a recipe defect. Fix it in
  `projects/forge/recipes/readme.md` or in what the recipe reads,
  never in `README.md`; the release regenerates the file.
- **`/check engine` reports a skill an agent names that does not
  exist.** Claude Code skips a missing skill silently, so the agent
  would run without its contract. Create the skill at
  `.claude/skills/<name>/SKILL.md` or correct the name in the
  agent's front-matter.
- **`/check single-source-of-truth` reports a restatement.** The
  same steps, rules or shape stand in two places, whatever the
  wording. The fix is a reference to the owner and the deletion of
  the copy. Where a shape has no owner at all, the finding proposes
  one, a skeleton or a section of `CLAUDE.md`, never a second
  description.
- **A finding you do not want to settle now.** A finding may be
  parked and the release proceeds. The check is advisory. A finding
  you have not settled when you order the release to go on is parked
  by that word, and the release says so aloud. Nothing is ever fixed
  silently.

## A worked example

The change is invented: you want `/end` to name the branch each
repository is on when it says what a shutdown would lose.

1. It changes what a command does, so it goes through the chain.
2. `/forge intent forge`. You say what you want and why. Claude
   reflects back one position: at the end of a session `/end` names
   the branch of every repository with changes. You answer `write`.
   Claude writes the position into `projects/forge/10-intent.md` and
   its record into `projects/forge/10-intent.history.md`; the
   intent's version bumps and `last_change` is derived from the
   record.
3. `/forge solution-design forge`. Claude writes the item that the
   `/end` command lists the branch beside each repository, reading it
   through `python scripts/forge-status.py`, the only door to git,
   and the record beside it in
   `projects/forge/40-solution-design.history.md`.
4. You edit `.claude/skills/end/SKILL.md` and add the branch to what
   it reports. You leave the commands table of `CLAUDE.md` as it is.
5. `/check engine`. One finding: the purpose of `/end` in the
   commands table of `CLAUDE.md` no longer matches what the skill
   does. In the walkthrough you accept it and bring the table line up
   to date. The check is clean on the next run.
6. `/release forge`. The repository is on `main`. The checks pass and
   Claude states so. You decline `/critique essence`. The README and
   the release notes are regenerated; Claude reports that the release
   notes gained one line on `/end`, and you accept the delta. Claude
   reports that the documentation is older than the intent and offers
   `/document`; you say yes, and the pages are regenerated before the
   save. The commit `release <version>: /end names the branch of each
   repository` lands on `main`. The version is not an integer, so no
   tag is proposed.

As a visitor, you stop after step 5 and open a pull request carrying
the position with its record, the item with its record, the changed
skill and the line `ran /check engine, clean`. The release and the
regenerated files are the author's, at the next release.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md): regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
