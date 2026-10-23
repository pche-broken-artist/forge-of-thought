---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 01fcdfa71b86df56
inputs:
  - CLAUDE.md#The system's own project
  - CLAUDE.md#Versioning & status
  - projects/forge/10-intent.md#POS.0720
  - projects/forge/10-intent.md#POS.0900
  - projects/forge/10-intent.md#POS.1440
  - projects/forge/10-intent.md#POS.1780
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - projects/forge/recipes/contributing.md#Instructions
---

# Make a change to the forge

A change to the forge is a change of the engine itself: of a command,
a rule, a convention or what a reviewer looks for. This page is for
the extender who wants to make such a change, prove it, record it and
release it, in his own clone or as a contribution to the public
engine. It also says which changes skip the chain and how a visitor
sends one.

## When to use it

Use it when you want the forge to behave differently. The forge runs
its own design as a project of its own, `projects/forge/`. A change
of behaviour therefore goes through that project's chain before
anything is built.

The line between the two kinds of change is drawn by what the change
does, never by its size:

- A change of how the forge behaves goes through the chain. Examples
  are a command, a rule, a convention, or what a reviewer looks for.
- A change that alters no behaviour is made directly. Examples are a
  wording, a broken path or a slip.

Some files are renders, that is outputs generated from a recipe and
never edited by hand:

- `README.md`
- `RELEASE-NOTES.md`
- `CONTRIBUTING.md`

A change to one of them goes into its recipe in
`projects/forge/recipes/`, or into what the recipe reads. The pages
of `docs/` are generated the same way and are never edited by hand
either.

## The command

```
/forge intent forge
```

This opens a round on the forge intent, the document of the
positions the forge holds. How such a round runs is on
[Forge the intent](../use/forge-the-intent.md).

## What happens

The person whose thinking is forged is the principal: in your own
clone that is you. What enters the forge stays the principal's
decision.

1. **The position in the intent.** You run `/forge intent forge` and
   work out, with Claude, the position that says what is wanted and
   why. This is the intent-first rule: a change of substance goes
   into the intent first and propagates down the chain from there,
   whichever layer showed the need for it. A round is one version of
   the intent.
   You should now see the new or changed position in
   `projects/forge/10-intent.md` and its record in
   `projects/forge/10-intent.history.md`.
2. **The item of the solution design.** Where the change solves
   something, you run `/forge solution-design forge` and write the
   item that says what is built or done.
   You should now see the item in
   `projects/forge/40-solution-design.md` and its record in the
   history companion beside it.
3. **The operating layer.** You make the change itself in the
   operating layer. The operating layer is `CLAUDE.md`, the skills,
   the agents, the templates and the scripts.
   You should now see the changed files in the engine, saying what
   the position and the item say.
4. **Proof.** You run `/check engine`. It verifies the core against
   itself and against the forge intent: every position honoured,
   nothing withdrawn still advertised, every decision reflected. How
   checks are run and settled is on
   [Check conformance](../use/check-conformance.md).
   You should now see a check that passed, or findings to settle.
5. **The honest sweep, where it fits.** Before a major version, or
   after a round on the operating layer, you also run
   `/check single-source-of-truth`. It reads the whole operating
   layer and verifies that every rule, procedure and file shape is
   written in one place and cited everywhere else. It is expensive by
   design and runs on the principal's word, when there is time for
   it.
   You should now see a report whose first line says how many files
   it read.
6. **The release.** You run `/release forge`, described on
   [Release a version](../use/release-a-version.md).
   You should now see the regenerated `README.md` and
   `RELEASE-NOTES.md` and a summary of what changed in them, before
   the commit.

A process change is complete only once the forge intent is updated
and the README re-rendered.

### Where the change needs a test

Some changes of the operating layer need a test before their design
can be trusted. These go in a different order:

1. The brief first, in the principal's words.
2. The build and its test.
3. The rounds of the intent and the solution design, right after the
   test.

The rounds of the intent and the design are never left across a
release. Until they are written, the brief is the authority on what
is being built.

### How the change is recorded

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it, never in its body:

- The body is the current state.
- The companion holds one record per change.
- A round is one version, with as many records as it made changes.
- The record is written in the same step as the change.
- Why an item changed, what was said, trials and measurements go into
  its record, never into the item.
- What the user must do after the change is written with it, in the
  record's `Action` field.

The release notes and the commit messages of a release are derived
from these records. `Action` is carried into the release notes word
for word.

## What you have afterwards

- A position in the forge intent that says what is wanted and why.
- An item of the solution design where the change solves something.
- The change in the operating layer.
- Records in the history companions of every document the round
  changed.
- After `/release forge`, a commit with the message
  `release <intent version>: <one line>`, a regenerated README and
  regenerated release notes. When the intent's version is an integer
  (an approved major), the tag `v<major>` is proposed and taken on
  the principal's word.

A release never regenerates the documentation on its own. It reports
the age of `docs/` and offers `/document`; the pages are regenerated
only on the principal's word, as
[Generate the documentation](../use/generate-the-documentation.md)
says.

## Sending a change to the public engine

In your own clone you decide everything: the forge there is yours.
What is merged into the public engine its author decides. The forge
wants feedback and ideas most; a finished change is welcome too, on
the same rules as above.

`CONTRIBUTING.md` at the root of the engine is the visitor's way in.
It names where to send feedback, an idea or a change, by kind. The
easiest way is to open a discussion first.

A pull request for a change of behaviour carries:

- the position in `projects/forge/10-intent.md`, saying what is
  wanted and why, with its record in the history beside it;
- the item in `projects/forge/40-solution-design.md`, where the
  change solves something;
- the change itself;
- one line on what you ran.

It does not carry a release, nor a regenerated README, release notes
or documentation. The author makes those at the next release. A
brief may come first, and need not.

A change that alters no behaviour is sent as a pull request as it
stands. Nothing else is needed.

Try your change yourself before you send it. A change written with
an AI is welcome on the same rule, and the pull request says what was
run.

## If something goes wrong

- **The release stops on another branch.** A release runs on `main`
  only. Save, then go back with
  `python scripts/forge-branch.py forge main`.
- **The release is refused because the repository is behind or
  diverged.** The release offers `/pull`; pull first, then release.
- **A check finds something.** The findings are settled by
  walkthrough, that is one finding per message, each with its verdict
  from the principal. A finding may be parked and the release goes
  on, because a check is advisory and never blocks.
- **The engine check reports a claim in the README that the forge no
  longer supports.** The fix goes into the recipe in
  `projects/forge/recipes/`, never into `README.md`.
- **A recipe is missing.** The release reports it as a check finding
  and releases without that render.

## A worked example

This example is invented. Say you want a command to print one more
line in its report.

1. You run `/forge intent forge`. With Claude you write a new
   position: the command prints the line, and why the reader needs
   it. On the principal's word the position lands in
   `projects/forge/10-intent.md`, with its record in
   `projects/forge/10-intent.history.md`. The record's `Action` says
   whether the user must do anything.
2. The change solves something, so you run
   `/forge solution-design forge` and write an item that says how the
   command produces the line.
3. You change the command's skill under `.claude/skills/` and, if the
   line comes from a script, that script under `scripts/`.
4. You run `/check engine`. It finds the position honoured by the
   skill, and nothing to settle.
5. The round touched the operating layer, so you run
   `/check single-source-of-truth`. It confirms that the shape of the
   new line is written in one place only.
6. In your clone, you run `/release forge`: the checks run, the README
   and the release notes are regenerated, and the release is saved.
   To offer the change to the public engine instead, you open a pull
   request with the position, the item, the changed skill and one
   line saying you ran the two checks.

Every term used here has one line in the [Glossary](../reference/glossary.md).

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
