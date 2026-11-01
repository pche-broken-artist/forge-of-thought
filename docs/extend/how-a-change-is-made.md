---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: b0986c746b8c0f06
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

A change to the forge is a change to the engine (the forge's own
repository), made with the forge's own commands. This page is for the
extender who wants to change how the forge behaves, or to fix
something that changes no behaviour. It says which way each kind of
change takes, how it is proved, recorded and released, and how a
visitor sends a change to the public engine.

## When to use it

Use this page when you want to change a command, a rule, a convention
or what a reviewer looks for. Use it too for a change that alters no
behaviour, such as a wording, a broken path or a slip.

The line between the two kinds is drawn by what the change does,
never by its size:

- A change of how the forge behaves goes through the chain before it
  is built.
- A change that alters no behaviour is made directly.

The chain here is the forge's own project, `projects/forge/`: its
intent (the positions the principal holds, in
`projects/forge/10-intent.md`) and its solution design (what is built
and the choice it rests on, in `projects/forge/40-solution-design.md`).
The principal is the person whose thinking is forged and who has the
final word on what enters it.

## The command

A change of behaviour starts here:

```
/forge intent forge
```

The second word names the definition to work (here the intent); the
third names the project (`forge` is the engine's own project). How a
round of the intent runs is on [Forge the intent](../use/forge-the-intent.md).

## What happens

1. **Write the position.** Run `/forge intent forge` and state, as a
   position of the intent, what is wanted and why. A change of
   substance goes into the intent first and propagates down the chain,
   whichever layer showed the need for it.
   You should now see the new or changed position in
   `projects/forge/10-intent.md`, and its record in
   `projects/forge/10-intent.history.md`.

2. **Write the item of the solution design.** Where the change solves
   something, run `/forge solution-design forge` and write the item
   that says what is built and what it realises.
   You should now see the item in
   `projects/forge/40-solution-design.md`, and its record in the
   history companion beside it.

3. **Change the operating layer.** Build the change in the operating
   layer of the engine:
   - `CLAUDE.md`
   - the skills under `.claude/skills/`
   - the agents under `.claude/agents/`
   - the templates under `templates/`
   - the help headers of the scripts in `scripts/`

   Where a document you would change is a render (`README.md`,
   `RELEASE-NOTES.md`, `CONTRIBUTING.md`), change its recipe in
   `projects/forge/recipes/` or what the recipe reads, never the file.
   The pages of `docs/` are generated the same way: a fix goes into the
   file the page mirrors.
   You should now see the change in the files of the operating layer,
   and no render edited by hand.

4. **Prove it.** Run the engine check:

   ```
   /check engine
   ```

   It verifies the core against itself and against the forge intent:
   every position honoured, nothing withdrawn still advertised, every
   decision reflected. Before a major version, or after a round on the
   operating layer, run also:

   ```
   /check single-source-of-truth
   ```

   It verifies that every rule, procedure and file shape is written in
   one place and cited everywhere else. It reads the whole operating
   layer, so it is long by design and does not fit every release. How
   the checks run and how their findings are settled is on
   [Check conformance](../use/check-conformance.md).
   You should now see the result of each check: a clean run, or
   findings to settle by walkthrough (one item at a time, each closed
   by the principal's verdict).

5. **Release it.** Run the release of the engine:

   ```
   /release forge
   ```

   The release runs its checks (`engine` on the engine, `light` and
   `project` on `projects/forge`), then regenerates the README and the
   release notes from their recipes, then the state render, and then
   saves with the release message. It offers to regenerate the
   documentation in one sentence and runs `/document` only on the
   principal's word: a release never regenerates the documentation on
   its own. How a release runs in full is on
   [Release a version](../use/release-a-version.md), and how the pages
   are regenerated is on
   [Generate the documentation](../use/generate-the-documentation.md).
   You should now see a commit whose message opens with
   `release <intent version>:`, with the README and the release notes
   regenerated.

A process change is complete only once the intent is updated and the
README re-rendered.

### A change that needs a test

Where a change of the operating layer needs a test, the order is
different:

1. The brief first, in the principal's words.
2. Then the build and its test.
3. Then the rounds of the intent and of the solution design, right
   after the test.

The rounds of the intent and the design are never left across a
release. Until they are written, the brief is the authority on what
is wanted.

### A change that alters no behaviour

Make it directly in the file that owns it, or in the recipe where the
file is a render. It needs no position and no item of the solution
design.

## What you have afterwards

- The position in the intent and, where the change solves something,
  the item in the solution design.
- A record for each change in the history companion
  (`<file>.history.md`) beside each versioned document you changed.
  The companion is append-only: one record per change, written in the
  same step as the change, in the shape `templates/history.md` defines.
  The way to an item (why it changed, what was tried, which research
  turned it) goes into its record, never into the item. What a user
  must do after the change is written with it, in the `Action` field.
- The changed operating layer.
- After the release: the README and the release notes regenerated,
  and a commit with the release message.

Before you propose a change to an item, read its history with
`/history <ID>`.

## Sending a change to the public engine

A visitor finds the way to send feedback, an idea or a change in
`CONTRIBUTING.md`. It gives the channels by kind: something to say,
something broken, an idea, a change. Feedback and ideas are what is
wanted most.

In your own clone you decide everything: the forge there is yours.
What is merged into the public engine its author decides.

The way to a pull request has these steps:

1. Fork the repository on GitHub.
2. Clone your fork as your engine.
3. Work through the forge (`/forge intent forge` for a change of
   behaviour).
4. Run `/save`, which pushes to your fork.
5. On your fork's page on GitHub, choose "Contribute", then "Open pull
   request".

A pull request for a change of behaviour carries:

- the position in `projects/forge/10-intent.md` saying what is wanted
  and why, with its record in the history beside it;
- the item in `projects/forge/40-solution-design.md`, where the change
  solves something;
- the change itself;
- one line on what you ran.

It carries no release and no regenerated README, release notes or
documentation: the author makes those at the next release. A brief may
come first and need not. A change that alters no behaviour is sent as
a pull request as it is, and nothing else is needed.

Try your change yourself before you send it. A change written with an
AI is welcome on the same rule, and the pull request says what was
run. Whoever is unsure stops at a discussion, and the author makes
the change.

## If something goes wrong

- **The release stops because the engine is not on `main`.** A
  release runs on `main` only. Save your work, then go back with
  `python scripts/forge-branch.py forge main`.
- **The release refuses because the engine is behind or diverged from
  its origin.** It offers `/pull`; pull first, then release.
- **A check reports findings.** Settle them by walkthrough. A finding
  may be parked, and the release goes on. The check is advisory: the
  principal may order the release regardless, and the findings he has
  not settled are parked by that word.
- **The engine check says the README claims something the intent no
  longer supports.** That is a defect of the recipe, fixed in the
  recipe, never in the README.
- **The single-source-of-truth check finds a rule stated in two
  places.** The fix is a reference to the file that owns the rule and
  the deletion of the copy.

## A worked example

This change is invented, to show the path. Suppose you want the
engine check to verify one thing more.

1. You run `/forge intent forge` and, in one round, write a new
   position: what the check is to verify, and why. The round writes
   its record into `projects/forge/10-intent.history.md`.
2. The change solves something, so you run
   `/forge solution-design forge` and write the item that says what is
   changed in the check and what it realises, with its record.
3. You change the check's agent file, `.claude/agents/check-engine.md`.
   The file carries only its own front-matter and its Lens section, so
   the new point goes into the Lens.
4. You run `/check engine`. A round on the operating layer is done, so
   you also run `/check single-source-of-truth`. You settle what they
   find by walkthrough.
5. You run `/release forge`. The README and the release notes are
   regenerated from their recipes, and the release is saved. You
   accept the offer of `/document`, so the pages carry the change too.

Had you sent the same change from a fork, your pull request would
carry steps 1 to 3 and one line saying that you ran `/check engine`;
step 5 would be the author's.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
