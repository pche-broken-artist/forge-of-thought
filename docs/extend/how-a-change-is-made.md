---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 86e1155b7a7e7db4
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

A change of the forge is made in a fixed order: it is written down
in the forge's own project first, then built, then proved by the
checks, recorded in the histories and released. This page is for the
extender: whoever changes how the forge behaves in a clone of the
engine, or sends such a change to the public engine.

## When to use it

Use this page when a change alters how the forge behaves. Such a
change is, for example:

- a command
- a rule
- a convention
- what a reviewer looks for

The line between the two kinds of change is drawn by what the change
does, never by its size. A change that alters no behaviour does not
go through the chain. Such a change is, for example:

- a wording
- a broken path
- a slip

You make it directly, and nothing else is needed.

The README, the release notes and `CONTRIBUTING.md` are renders: files
generated from a recipe, never edited by hand. A change to one of them
goes into its recipe in `projects/forge/recipes/` or into what the
recipe reads, and the file is regenerated.

## The command

A change of behaviour starts in the forge's own intent:

```
/forge intent forge
```

The intent is the document of the forge's own project
(`projects/forge/10-intent.md`) that holds the positions: what the
principal (the person whose thinking is forged, the final authority
on all content) wants and why. How a round on an intent runs is the
page [Forge the intent](../use/forge-the-intent.md). The terms of the
forge are listed one line each in the [Glossary](../reference/glossary.md).

## What happens

1. **The position.** Through `/forge intent forge` you write the
   position that says what is wanted and why. A change of substance
   goes into the intent first and propagates down the chain from
   there, whichever layer showed the need for it.
   You should now see the position in `projects/forge/10-intent.md`
   and its record in the history beside it,
   `projects/forge/10-intent.history.md`.
2. **The item of the solution design.** Where the change solves
   something, you write the item that says what is built or done,
   through `/forge solution-design forge`.
   You should now see the item in
   `projects/forge/40-solution-design.md` and its record in the
   history beside it.
3. **The operating layer.** You build the change in the operating
   layer of the engine. The operating layer is these files:
   - `CLAUDE.md`
   - the skills under `.claude/skills/`
   - the agents under `.claude/agents/`
   - the templates under `templates/`
   - the scripts under `scripts/`

   You should now see the change in the files it concerns, and no
   rule or procedure written in a second place.
4. **Prove it.** You run the engine's check, as the page
   [Check conformance](../use/check-conformance.md) says:

   ```
   /check engine
   ```

   It verifies the core against itself and against the forge intent:
   every position honoured, nothing withdrawn still advertised, every
   decision reflected. Before a major version, or after a round on
   the operating layer, you also run:

   ```
   /check single-source-of-truth
   ```

   It verifies that every rule, procedure and file shape is written in
   one place and cited everywhere else. It reads the whole operating
   layer every time and is long by design. It is not meant for every
   release.
   You should now see the result of each check: a clean run, or
   findings to settle.
5. **Record it.** Every versioned document keeps its history in a
   companion file beside it, `<file>.history.md`, never in its body.
   The record is written in the same step as the change. The way to
   an item (why it changed, what was said, trials, which research
   turned it) goes into its record, never into the item. What the
   user must do after the change is written with it, in the record's
   `Action` field.
   You should now see one record per change in the companion of each
   document the change touched.
6. **Release it.** You release the engine from `main`, as the page
   [Release a version](../use/release-a-version.md) says:

   ```
   /release forge
   ```

   The release runs the checks first: `engine` on the engine, and
   `light` and `project` on the forge's own project. Their findings
   are settled by walkthrough, that is one finding at a time, each
   with the principal's verdict. Then it regenerates the README and
   the release notes from their recipes, unconditionally. It reports
   the age of the documentation and offers `/document`. It never
   regenerates the documentation on its own. Regenerating the pages
   is the page [Generate the documentation](../use/generate-the-documentation.md).
   You should now see the report of the checks, a short summary of
   what changed in the regenerated README and release notes, and then
   the save with the release message.

## The order when the change needs a test

Where a change of the operating layer needs a test, the order is
different:

1. The brief first, in the principal's words.
2. Then the build and its test.
3. Then the rounds of the intent and of the solution design, right
   after it.

These rounds never wait across a release. Until they are written,
the brief and the plan of the work are the authority.

## What you have afterwards

A process change is complete only once the intent is updated and the
README re-rendered. Afterwards you have:

- the position in the intent, with its record
- the item of the solution design where the change solves something,
  with its record
- the change in the operating layer
- a release whose README and release notes are regenerated from the
  updated sources

## Sending a change to the public engine

In your own clone you decide everything: the forge there is yours.
What is merged into the public engine its author decides.

What the forge wants from visitors most is feedback and ideas. A
finished change is welcome too, on the same rule as above. The way
to send feedback, an idea or a change is said in `CONTRIBUTING.md`,
with the channel for each kind. The easiest way is to open a
discussion first.

A pull request for a change of behaviour carries:

- the position in `projects/forge/10-intent.md` saying what is wanted
  and why, with its record in the history beside it
- the item in `projects/forge/40-solution-design.md`, where the
  change solves something
- the change itself
- one line on what you ran

It carries no release and no regenerated README, release notes or
documentation. The author makes them at the next release. A brief may
come first and need not. Nobody sends a change he has not tried
himself. A change written with an AI is welcome on the same rule.

## If something goes wrong

- **The release stops because the engine is not on `main`.** A
  release runs on `main` only. It reports the branch the engine is on
  and how to get back, after saving:
  `python scripts/forge-branch.py forge main`.
- **The release is refused because the engine is behind or diverged
  from its origin.** It offers `/pull`. Pull first, then release.
- **A check finds something.** The findings are settled by
  walkthrough. A finding may be parked and the release goes on. A
  finding the principal has not settled when he orders the release to
  go on is parked by that word.
- **The README claims what `CLAUDE.md` or the intent no longer
  supports.** That is a defect of the recipe. It is fixed in the
  recipe, never in the README.
- **A rule now stands in two places.** The single-source-of-truth
  check reports it. The fix is a reference to the owner and the
  deletion of the copy.

## A worked example

An invented change: a command of the engine should print one more
line of state. This is a change of behaviour, so it goes through the
chain.

1. `/forge intent forge`: a round on the intent writes a position
   saying the command prints that line and why. Its record lands in
   `projects/forge/10-intent.history.md`.
2. `/forge solution-design forge`: a round on the design writes the
   item saying which skill or script prints the line. Its record lands
   in the design's history.
3. The skill `.claude/skills/<command>/SKILL.md` is changed, and
   nothing else restates what it now does.
4. `/check engine` runs clean: the command still matches its row in
   `CLAUDE.md`, and the position is honoured.
5. `/release forge` runs its checks, regenerates the README and the
   release notes, and saves with the release message.

Had the change been the fix of a misspelt word in a skill, it would
have been made directly, with none of these steps.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
