---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: b527e948e2757767
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

A change to the forge is a change to the engine itself: a command, a
rule, a convention or what a reviewer looks for. This page is for the
extender who wants to make such a change in a clone, prove it,
record it and release it, or send it to the public engine. It walks
the change from the forge's own intent down to the release.

## When to use it

Use this page when your change alters how the forge behaves.
A change of behaviour is, for example, a new or changed command, a
rule, a convention, or what a reviewer looks for.
The line between the two kinds of change is drawn by what the change
does, never by its size.

A change that alters no behaviour is made directly.
Such a change is a wording, a broken path or a slip.
You make it in the file where it stands, and nothing else is needed.

Three files of the engine are generated and are never edited by
hand:

- `README.md`
- `RELEASE-NOTES.md`
- `CONTRIBUTING.md`

A change to one of them goes into its recipe in
`projects/forge/recipes/`, or into what the recipe reads.
A recipe is the versioned file that says how a generated output (a
render) is made.

In your own clone you decide everything: the forge there is yours.
What is merged into the public engine its author decides.

## What you do

The change goes through the forge's own chain of documents before it
is built. You start at the forge intent, the document of the
positions the forge holds:

```
/forge intent forge
```

From there it travels down, in this order:

1. A position in the forge intent (`projects/forge/10-intent.md`).
2. The item of the solution design
   (`projects/forge/40-solution-design.md`), where the change solves
   something.
3. The operating layer: `CLAUDE.md`, the skills under
   `.claude/skills/`, the agents under `.claude/agents/`, the
   templates under `templates/` and the scripts under `scripts/`.
4. The checks that prove it.
5. The release.

This order is the working method called intent-first.
A change of substance goes into the intent first and propagates down
the chain, whichever layer showed the need for it.

## What happens

1. **Write the position.** Run `/forge intent forge` and work the
   change with Claude as a position of the forge intent: what is
   wanted and why. You are the principal here (the person whose
   thinking is forged, with final authority over the content). The
   round ends in one write, on your word. How the intent is iterated
   is on [Forge the intent](../use/forge-the-intent.md).
   You should now see the new or changed position in
   `projects/forge/10-intent.md` and its record in
   `projects/forge/10-intent.history.md`.

2. **Write the item of the solution design.** Where the change solves
   something, run `/forge solution-design forge` and work the item
   that says what is built or done.
   You should now see the item in
   `projects/forge/40-solution-design.md` and its record in
   `projects/forge/40-solution-design.history.md`.

3. **Build it in the operating layer.** Change `CLAUDE.md`, the
   skills, the agents, the templates or the scripts that the change
   touches.
   Where your change touches the README, the release notes or
   `CONTRIBUTING.md`, change their recipe, not the file.
   Every versioned document you change keeps its history in its
   companion `<file>.history.md` beside it: one record per change,
   written in the same step as the change.
   What the user of the engine must do after the change is written
   with it, in the record's `Action` field.
   You should now see the changed files of the operating layer, and
   one new record in the history companion of every versioned
   document you changed.

4. **Prove it.** Run the engine check:

   ```
   /check engine
   ```

   It verifies the engine against itself and against the forge
   intent. It covers the commands table against the skills, the
   scripts against `CLAUDE.md`, the README against `CLAUDE.md`, and
   the templates against the conventions. It also verifies that every
   position is honoured and that nothing withdrawn is still
   advertised.
   Before a major version, or after a round on the operating layer,
   also run:

   ```
   /check single-source-of-truth
   ```

   It verifies that every rule, procedure and file shape is written in
   one place and cited everywhere else.
   It reads the whole operating layer every time and is long by
   design.
   How the checks run and how their findings are settled is on
   [Check conformance](../use/check-conformance.md).
   You should now see the result of each check: its findings, or the
   word that it passed.

5. **Release it.** From `main`, run:

   ```
   /release forge
   ```

   The release runs the `engine` check on the engine root, and the
   `light` and `project` checks on `projects/forge`. Its findings are
   settled by walkthrough (Claude puts each finding to you for your
   verdict). It offers the `essence` critique once.
   It then regenerates the README and the release notes from their
   recipes, and reports what materially changed in them.
   It reports the age of the documentation and offers `/document`.
   Finally it saves with the release message and, at an approved
   major, the tag. The release in full is on
   [Release a version](../use/release-a-version.md).
   You should now see a commit whose message opens with
   `release <intent version>:`.

A process change is complete only once the intent is updated and the
README re-rendered.

A release never regenerates the documentation on its own.
The pages of `docs/` are regenerated by `/document`, on your word when
the release offers it, or at any time
([Generate the documentation](../use/generate-the-documentation.md)).

## What you have afterwards

- A position in the forge intent that says what is wanted and why,
  with its record in the history beside it.
- Where the change solves something, an item in the solution design.
- The change itself in the operating layer, with a record in every
  history companion it touched.
- A regenerated README and release notes, and a release commit.
- At an approved major (an integer version of the intent), the tag
  `v<major>`, proposed and taken on your word.

## If something goes wrong

- **The repository is not on `main`.** The release stops and reports
  the branch it is on. You get back by saving and then running
  `python scripts/forge-branch.py forge main`.
- **The repository is behind or diverged from its origin.** The
  release is refused, with the offer of `/pull`.
- **A check finds something.** The findings are settled by
  walkthrough. A finding may be parked, and the release proceeds.
  The check is advisory: you may order the release to go on at any
  moment, and the findings not yet settled are parked by that word.
- **A recipe is missing.** The release reports it as a finding and
  goes on without that render.
- **The README says something `CLAUDE.md` or the intent no longer
  supports.** This is a defect of the recipe, and it is fixed in the
  recipe.

## Sending a change to the public engine

`CONTRIBUTING.md` is the visitor's way in. It lists the ways to send
feedback, an idea or a change, by kind. Feedback and ideas are what
is wanted most. The easiest way to a change is to open a discussion
first.

A pull request for a change of behaviour carries:

- the position in `projects/forge/10-intent.md`, with its record in
  the history beside it;
- the item in `projects/forge/40-solution-design.md`, where the change
  solves something;
- the change itself;
- one line on what you ran.

It carries no release and no regenerated README, release notes or
documentation. The author makes those at the next release.
A brief may come first, and need not.
Try your change yourself before you send it.
A change written with an AI is welcome on the same rule, and the pull
request says what was run.

A change that alters no behaviour is sent as a pull request as it
is.

## A worked example

This change is invented for the example. Suppose you want every
critic report to open with the version of the document it read.

1. You run `/forge intent forge` and, with Claude, word a position:
   a critic report opens with the version of what it read, and why
   you want it. On your word to write, the position lands in
   `projects/forge/10-intent.md` and its record in
   `projects/forge/10-intent.history.md`.
2. You run `/forge solution-design forge` and add the item that says
   where the version is read and where the report shows it.
3. You change the file of the operating layer that owns the shape of
   a critic report. You write its record, with an `Action` line if
   users must do anything after it.
4. You run `/check engine`. Since the round touched the operating
   layer, you also run `/check single-source-of-truth`, and settle
   what they find.
5. On `main`, you run `/release forge`. The checks run again, the
   README and the release notes are regenerated, and you accept the
   offer of `/document` so that the pages carry the new rule. The
   save commits with `release <intent version>: <one line>`.

Sent to the public engine instead, the pull request carries steps 1
to 3 and one line on what you ran in step 4.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the
  checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
