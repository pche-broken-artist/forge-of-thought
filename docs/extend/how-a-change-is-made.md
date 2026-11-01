---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: e991fdad90bbcf2d
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
  - projects/forge/40-solution-design.md#SOL.0450
  - .claude/skills/render/SKILL.md
---

# Make a change to the forge

A change to the forge is a change of how Claude behaves when it runs
the forge: a command, a rule, a convention, what a reviewer looks
for. Such a change goes through the forge's own chain of documents
before it is built, is proved by the checks, recorded in the history
companions and released from `main`. This page is for the extender
who wants to make one: it says which way a change takes, what you
type at each step and what you see when the step has worked.

## When to use it

Use this page when you want the forge to do something differently.
The forge runs itself through its own process: the engine's own
project, `projects/forge/`, carries its brief, its intent with the
design positions, its solution design, its decisions and its ledger.
A change of behaviour is first a change of that project, then a
change of the files that run the forge.

The line between the two kinds of change is drawn by what the change
does, never by its size:

- A change of how the forge behaves goes through the chain: a
  position in the forge intent, an item in the solution design, then
  the operating layer.
- A change that alters no behaviour (a wording, a broken path, a
  slip) does not go through the chain. It is made directly, in the
  file that owns the text.

The operating layer is the set of files Claude reads to run the
forge: `CLAUDE.md`, the skills under `.claude/skills/`, the agents
under `.claude/agents/`, the templates under `templates/` and the
scripts under `scripts/`.

In your own clone you are the principal, the one whose thinking is
forged and who alone decides what is written: you decide everything,
and the forge there is yours. What is merged into the public engine
its author decides. The way to send feedback, an idea or a finished
change to the public engine is told in `CONTRIBUTING.md` in the
repository root; the last step below says what it carries.

## What you do

A change of behaviour, in the order it is made:

```
/forge intent forge
/forge solution-design forge
/check engine
/check single-source-of-truth
/release forge
```

`forge` is the slug of the engine's own project. `engine` and
`single-source-of-truth` are entries of the check roster. The second
check is run before a major or after a round on the operating layer,
not at every release.

A change to a document that is a render takes one command:

```
/render contributing
```

## What happens

1. **Tell the two kinds apart.** Ask what the change does, not how
   large it is. A change of how the forge behaves goes on to step 2.
   A change that alters no behaviour is made in the file that owns
   the text and goes straight to step 7. A change to `README.md`,
   `RELEASE-NOTES.md` or `CONTRIBUTING.md` goes to step 8, since
   those files are generated. You should now see which way your
   change takes.

2. **Put the position into the forge intent.** Run
   `/forge intent forge`. The intent is the trunk of the chain; the
   working method is intent-first: a change of substance goes into
   the intent first and propagates down the chain from there,
   whichever layer showed the need for it. The position says what is
   wanted and why. How an intent is iterated is on
   [Forge the intent](../use/forge-the-intent.md). Before Claude
   proposes a change to an existing item it reads the item's history
   through `/history <ID>`. The round is written once, on your word,
   and the records of what changed are written in the same step as
   the change (step 6). You should now see the position in
   `projects/forge/10-intent.md`, its record in
   `projects/forge/10-intent.history.md` and the intent's version
   raised once for the round.

3. **Put the item into the solution design.** Run
   `/forge solution-design forge`. The
   [solution design](../reference/glossary.md) is the layer below the
   intent that says what is built or done, what it realises and the
   choice it rests on. The item names the position it realises and
   where the change lands. You should now see the item in
   `projects/forge/40-solution-design.md` with its record in the
   history companion beside it.

4. **Change the operating layer.** Edit the file that owns the
   mechanism: `CLAUDE.md`, the skill, the agent, the template or the
   script. A procedure, a rule set or a file shape lives in one place
   and is cited by path everywhere else; a copy of it in a second
   file is a finding of the `single-source-of-truth` check. Where the
   change needs a test, the order of the whole change is different:
   the brief first, in the principal's words, then the build and its
   test, then the rounds of the intent and the design right after it,
   never across a release. Until the intent is brought to the built
   state, the brief is the authority. You should now see the changed
   file, and the intent and the design brought to the built state
   before anything is released.

5. **Prove it.** Run `/check engine`. The check reads the engine
   (`CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`,
   `scripts/`) and the forge intent with its threads and decisions,
   and verifies three things:

   - the core against itself: the commands table of `CLAUDE.md`
     against the skills on disk, the described agents against
     `.claude/agents/`, every skill an agent names in its front-matter
     present on disk, every script in `scripts/` described in
     `CLAUDE.md` and nothing described there missing, the README
     against `CLAUDE.md` for the same chain, conventions and command
     set, the templates against the conventions of versioning and
     IDs;
   - the core against the forge intent: every position honoured,
     nothing withdrawn or rejected still advertised, every decision
     reflected in the intent where it applies;
   - a sweep for old names recorded in the decisions and for terms
     the principal has dropped, which only historical records may
     still carry.

   It costs minutes, so that a release can afford it every time.
   Before a major, or after a round on the operating layer, run
   `/check single-source-of-truth` as well, on the principal's word:
   it reads the whole operating layer, never a changed subset, and
   verifies that every rule, procedure and file shape has one owner
   and is cited everywhere else, that every lens, persona and check
   file carries only its front-matter and its Lens section, and that
   no skill or agent performs directly what a script, command or
   agent exists for. It is expensive by design and says in its
   report's first line how many files it read. How a check is run is
   on [Check conformance](../use/check-conformance.md). You should
   now see the report of each check: either that the check passed,
   or its findings, settled by walkthrough (one finding per message,
   each closed with your verdict).

6. **Record it.** Every versioned document, every artefact and every
   recipe alike, keeps its history in an append-only companion
   `<file>.history.md` beside it, never in its body: the body is the
   current state, the companion the record. The history is a log,
   one record per change; a round is one version and as many records
   as it made changes. The way to an item (why it changed, what was
   said, trials, which research turned it) goes into its record,
   never into the item. What the user must do after the change is
   written with it, in the record's `Action` field. The log is the
   single primary: the commit message a release drafts and the
   release notes are derived from it. You should now see one record
   per change in each companion, the former wording in `Was` and, where
   the user has something to do, an `Action`.

7. **Release it.** Run `/release forge` on `main`. The release runs
   its checks first (`engine` on the engine root, `light` and
   `project` on `projects/forge`), launched at once and awaited
   together, and reports the result even when clean; findings are
   settled by walkthrough. It offers `/critique essence` once and
   runs it only on your word. It reports the age of the
   documentation against the intent's version and offers
   `/document` in one sentence; a release by hand never regenerates
   the documentation on its own, so the pages are remade only on your
   word, as [Generate the
   documentation](../use/generate-the-documentation.md) says. Only
   then it regenerates the README and the release notes from their
   recipes, unconditionally, through `/render`, and reports what
   materially changed in them, so that you rule on the delta before
   the commit; then it writes the state render, the ledger (the
   project's state, made at read time) as a tracked render. Last it
   saves with the message `release <intent version>: <one line>`,
   the line drafted from the records of the intent's history since
   the last release, and proposes the tag `v<major>` when the
   intent's version is an integer. The whole run is on
   [Release a version](../use/release-a-version.md). A process change
   is complete only once the intent is updated and the README
   re-rendered. You should now see the regenerated `README.md` and
   `RELEASE-NOTES.md`, the release commit on `main` and the push to
   the remote.

8. **Where the document is a render.** `README.md`,
   `RELEASE-NOTES.md` and `CONTRIBUTING.md` are renders: generated
   files, never edited by hand. A change goes into the recipe in
   `projects/forge/recipes/` or into what the recipe reads, and the
   file is regenerated. The README and the release notes are
   regenerated by every release (step 7). `CONTRIBUTING.md` is a
   render of `projects/forge/recipes/contributing.md`, made on
   `/render contributing` and not by a release; a render is
   regenerated only on that command or by a release, never on
   Claude's own judgement, which reports a stale render and offers.
   How a render is regenerated is on
   [Render an output](../use/render-an-output.md). The pages of
   `docs/` are generated the same way, by `/document` from the files
   that own each topic: a fix goes into the file the page mirrors.
   You should now see the regenerated file opening with its
   provenance: the recipe and the inputs it was made from, with their
   versions.

9. **Send it to the public engine, if you are a visitor.**
   `CONTRIBUTING.md` names a channel for each kind of message: a
   discussion for feedback and an idea, which the forge wants most;
   an issue for a defect; a private way for what is not public.
   Everything posted on the public channels is public: no names, no
   company content, nothing of a project that is not yours to show. A
   finished change is welcome on the forge's own rule: a change of
   behaviour went through the chain before it was built, a document
   that is a render through its recipe, and nobody sends a change he
   has not tried himself; a change written with an AI is welcome on
   the same rule. The pull request carries the position in
   `projects/forge/10-intent.md` with its record in the history
   beside it, the item in `projects/forge/40-solution-design.md`, the
   change itself and one line on what you ran. It carries no release
   and no regenerated README, release notes or documentation; the
   author makes those at the next release. A brief may come first and
   need not. Whoever is unsure stops at a discussion and the author
   makes the change. You should now see the pull request with those
   four things in it and nothing generated.

## What you have afterwards

- A position in the forge intent saying what is wanted and why, and
  an item in the solution design saying what was built and the choice
  it rests on, each with its record in the history companion beside
  it.
- The changed file of the operating layer, with the mechanism in one
  place and cited by path elsewhere.
- A clean report of `/check engine`, and of
  `/check single-source-of-truth` where the round touched the
  operating layer.
- A release on `main`: the README and the release notes regenerated,
  the release notes carrying your change with its `Action` word for
  word, the state render written, the commit pushed.
- For a change that alters no behaviour: the fixed file, saved.
- For a render: the regenerated file with its provenance.

## If something goes wrong

- **The release stops at the branch.** A release runs on `main`
  only. On any other branch it stops and reports the branch the
  repository is on and how to get back:
  `python scripts/forge-branch.py <slug> main`, after saving.
- **The release refuses the repository.** A repository behind or
  diverged from its origin is refused with the offer of `/pull`.
- **A check finds something.** The findings are settled by
  walkthrough; a finding may be parked, and the release proceeds.
  Nothing is fixed silently. The check is advisory: you may order the
  release to go on regardless, and the findings you have not settled
  are parked by that word, said aloud.
- **The README says what `CLAUDE.md` or the intent no longer
  supports.** The `engine` check calls this a recipe defect: the fix
  goes into the recipe, never into the README.
- **The same rule stands in two files.** The
  `single-source-of-truth` check reports the restatement; the fix is
  a reference to the owner and the deletion of the copy. Where a
  shape has no owner at all, the finding proposes one, never a second
  description.
- **A recipe is missing at the release.** It is reported as a finding
  and the repository is released without that render.
- **A render carries an instance fact.** After every render the file
  is scanned mechanically, `python scripts/docs-check.py --file
  <render>`; a hit is said aloud and you judge it. An instance fact is
  regenerated out, never edited by hand.
- **The documentation is older than the intent.** The release reports
  the age and offers `/document`; it never runs it on its own. Run it
  on your word before the renders, so that the README reads the
  current index.

## A worked example

An invented change: you want the `engine` check to verify, beside
what it verifies today, that every script in `scripts/` opens with a
help header. That is a change of what a reviewer looks for, so it is
a change of behaviour and takes the chain.

1. You run `/forge intent forge` and say what you want and why.
   Claude reads the history of the positions on the checks through
   `/history <ID>`, reflects back what it understood and, on your
   word `write`, writes the position into
   `projects/forge/10-intent.md` with one record in
   `projects/forge/10-intent.history.md`; the intent's version rises
   once.
2. You run `/forge solution-design forge`. The item names the
   position it realises and where the change lands: the Lens section
   of `.claude/agents/check-engine.md`. It is written with its record
   in the design's history companion.
3. You add the clause to the Lens section of
   `.claude/agents/check-engine.md`, the one file that owns what the
   check verifies. Nothing of it is written anywhere else.
4. You run `/check engine`. The report says that the check passed:
   the agent is described in `CLAUDE.md`, the position is honoured,
   nothing withdrawn is advertised. Since the round touched the
   operating layer, you run `/check single-source-of-truth` as well;
   its first line says how many files it read, and it finds no
   restatement.
5. You run `/release forge` on `main`. The checks pass; you decline
   the offered critique; the release reports the age of the
   documentation and you accept `/document`, so that the pages carry
   the changed check; the README and the release notes are
   regenerated, the release notes carrying one sentence on the
   changed check; the state render is written; the save commits with
   `release <intent version>: <one line>` and pushes. The change is
   complete: the intent is updated and the README re-rendered.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an
  intent.
- [Check conformance](../use/check-conformance.md): running the
  checks.
- [Release a version](../use/release-a-version.md): the release.
- [Render an output](../use/render-an-output.md): regenerating a
  render such as CONTRIBUTING from its recipe.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
