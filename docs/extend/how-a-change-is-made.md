---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 14143ec641c97044
inputs:
  - CLAUDE.md#The system's own project
  - CLAUDE.md#Versioning & status
  - projects/forge/10-intent.md#POS.0720
  - projects/forge/10-intent.md#POS.0900
  - projects/forge/10-intent.md#POS.1440
  - projects/forge/10-intent.md#POS.1780
  - projects/forge/10-intent.md#POS.1930
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/test/SKILL.md
  - projects/forge/recipes/contributing.md#Instructions
  - projects/forge/40-solution-design.md#SOL.0450
  - .claude/skills/render/SKILL.md
---

# Make a change to the forge

A change to the forge is a change of how Claude is told to behave:
a command, a rule, a convention, what a reviewer looks for. This
page is for you, the extender, who wants to make such a change and
have it proved, recorded and released. It says the order the change
takes through the forge's own project (`projects/forge/`, the forge
run through its own process), which commands do the work, and what
a change meant for the public engine carries when it is sent. Every
term of the forge used here is in the [Glossary](../reference/glossary.md).

## When to use it

Use this page when the change alters how the forge behaves. The
line between the two kinds of change is drawn by what the change
does, never by its size:

- A change of behaviour goes through the chain before it is built:
  a command, a rule, a convention, what a reviewer looks for. This
  page is its way.
- A change that alters no behaviour is made directly, and nothing
  else is needed: a wording, a broken path, a slip.
- A change of a document that is a render goes into its recipe, or
  into what the recipe reads, and the render is regenerated. The
  README, the release notes and `CONTRIBUTING.md` are such renders
  and are never edited by hand. The pages of `docs/` are generated
  the same way, from the files that own each topic: a fix goes into
  the file the page mirrors, and the pages are regenerated as
  [Generate the documentation](../use/generate-the-documentation.md)
  says.

The change lands in the operating layer. That is `CLAUDE.md`, the
skills under `.claude/skills/`, the agents under `.claude/agents/`,
the templates under `templates/` and the scripts under `scripts/`.
Before it lands there, it goes through two artefacts of the forge's
own chain: the forge intent (`projects/forge/10-intent.md`) and the
solution design (`projects/forge/40-solution-design.md`).

## What you do

Each line can be typed as it stands. `forge` is the slug of the
forge's own project; to the commands it means the engine.

```
/forge intent forge
/forge solution-design forge
/test
/check engine
/check single-source-of-truth
/release forge
```

`/test` is for a change that touches a script. `/check
single-source-of-truth` fits before a major or after a round on the
operating layer, not at every release. `/release forge` runs the
tests first and then the checks the release composes, so the two
lines before it are the proof you make on your own before you
release.

## What happens

1. **The position in the forge intent.** You start with
   `/forge intent forge`, as [Forge the intent](../use/forge-the-intent.md)
   describes. A change of substance goes into the intent first and
   propagates down the chain, whichever layer showed the need for
   it. The position says what is wanted and why. Before Claude
   proposes a change to an item that exists, it reads the item's
   history through `/history <ID>`. The write happens on the word
   of the principal (the person whose thinking is being forged; in
   your own clone that is you). The record of the change is written
   in the same step, into the companion
   `projects/forge/10-intent.history.md`. What a user of the engine
   must do after the change stands in that record, in its `Action`
   field. You should now see the position in
   `projects/forge/10-intent.md`, its record in the companion beside
   it, and the intent's version raised by the round.

2. **The item in the solution design.** You go on with
   `/forge solution-design forge`. Where the change solves something,
   the item says what is built. It names the position it realises,
   the choice it rests on and what the choice was weighed against,
   and where the part lives. You should now see the item in
   `projects/forge/40-solution-design.md` and its record in
   `projects/forge/40-solution-design.history.md`.

3. **The operating layer.** Then the change itself: a sentence of
   `CLAUDE.md`, a skill, an agent, a template or a script. A script
   is changed with its test in `tests/`, beside the scripts the
   tests prove. Where the change of the operating layer needs a
   test, the order of the whole is different. The brief comes first,
   in the principal's words. The build and its test come next. The
   rounds of the intent and the design follow right after it, never
   across a release: the intent is brought to the built state before
   anything is released. You should now see the changed files, and
   for a script its test beside it.

4. **Prove it.** `/test` runs `python -m pytest -q` from the engine
   root over `tests/`, as [Run the tests](../use/run-the-tests.md)
   describes; nothing of the engine or of a project changes. The
   sum comes back as pytest prints it. A red test is reported word
   for word, the failing assertion included, and nothing is fixed
   on this command's word: the fix is a round of its own, the
   script changed with its test. `/check engine` verifies the core
   against itself and against the forge intent, as
   [Check conformance](../use/check-conformance.md) describes: the
   commands table of `CLAUDE.md` against the skills on disk, the
   agents against `.claude/agents/`, every file of `scripts/`
   described in `CLAUDE.md`, the templates against the conventions,
   every position honoured, nothing withdrawn still advertised,
   every decision reflected, and no old name of a renamed thing
   outside the historical records. `/check single-source-of-truth`
   reads the whole operating layer, never a changed subset, and
   verifies that every rule, procedure and file shape is written in
   one place and cited everywhere else; a restatement is a finding,
   and the fix is a reference to the owner and the deletion of the
   copy. It is long by design, so it is run before a major or after
   a round on the operating layer. Findings are settled by
   walkthrough (one item per message, each closed with your
   verdict). You should now see `<n> passed in <s>s` from the tests,
   and from each check a report with findings, or the word that the
   check passed.

5. **Record.** Every versioned document keeps its history in an
   append-only companion `<file>.history.md` beside it, never in
   its body: the body is the current state, the companion the
   record. A round is one version and as many records as it made
   changes. The log is the single primary: the commit messages that
   `/save` and `/release` draft and the release notes derive from
   it. You should now see one record for every change in the
   companion of every versioned document you touched.

6. **Release.** `/release forge` runs from `main` only, as
   [Release a version](../use/release-a-version.md) describes. It
   runs the engine's tests first, before any check or agent, so
   that a script that broke stops the release before it costs
   anything. It then runs the checks: `engine` on the engine root,
   and `light` and `project` on `projects/forge`. Findings are
   settled by walkthrough; a finding may be parked, and the release
   goes on. It offers `/critique essence` once and runs it only on
   your word. It reports the age of the documentation and offers
   `/document` once; a release by hand never regenerates the
   documentation on its own. Only then it regenerates the README and
   the release notes from their recipes, always through `/render`,
   and reports what materially changed in them: you rule on the
   delta before the commit. It writes the state render
   `projects/forge/renders/state.md`, the ledger (the state of the
   project, made at read time) as a tracked file. Then it saves
   with the message `release <intent version>: <one line>`, the line
   drawn from the records of the intent's history since the last
   release, and, when the intent's version is an integer, proposes
   the tag `v<major>`, taken on your word. A process change is
   complete only once the intent is updated and the README
   re-rendered. You should now see the README and the release notes
   regenerated, the state render written, and the release commit
   pushed.

7. **CONTRIBUTING, where you changed it.** `CONTRIBUTING.md` in the
   repository root is a render of
   `projects/forge/recipes/contributing.md`. It is made on
   `/render contributing`, as [Render an output](../use/render-an-output.md)
   describes, and not by a release. A change to what it says goes
   into the recipe, and you render it yourself. You should now see
   `CONTRIBUTING.md` regenerated, its front-matter citing the
   recipe's version.

8. **Send it to the public engine, where it is meant for it.** In
   your own clone you decide everything; the forge there is yours.
   What is merged into the public engine its author decides. The
   easiest way is to open a discussion first; whoever is unsure
   stops there, and the author makes the change. The way to a pull
   request, in the steps the forge and GitHub have: fork the
   repository on GitHub, clone your fork as your engine, work
   through the forge, `/save`, which pushes to your fork, and on
   your fork's page choose "Contribute", then "Open pull request".
   You try your change yourself before you send it; a change
   written with an AI is welcome on the same rule, and the pull
   request says what was run. You should now see your change on
   your fork, with a pull request opened against the public engine.

## What you have afterwards

- A position in the forge intent that says what is wanted and why,
  with its record.
- An item in the solution design that says where the change solves
  something, with its record.
- The change itself in the operating layer, and for a script its
  test in `tests/`.
- A green run of `/test` and the reports of the checks, settled.
- A release from `main` with the README and the release notes
  regenerated, where you released your own clone.

For the public engine, the pull request carries the first four:
the position with its record in the history beside it, the item,
the change itself, and one line on what you ran, the test of a
script among it. It does not carry a release, a regenerated README,
release notes or documentation: the author makes those at the next
release. A brief may come first and need not. Everything that
enters the forge's own project is written in English, a brief
included, because the project is public and read by everyone; a
brief sent in another language is translated at the merge, and its
original stays in git. The channels are named in `CONTRIBUTING.md`
by kind: a discussion for feedback and an idea, an issue for a
defect, and a private way for what is not public. Everything posted
there is public: no names, no company content, nothing of a project
that is not yours to show. The code of conduct holds everywhere the
forge is talked about, and a security problem never goes into an
issue; both are the fixed files that
[The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md)
describes.

## If something goes wrong

- **The release reports a branch other than `main` and stops.** It
  names the branch and the way back:
  `python scripts/forge-branch.py <slug> main`, after saving.
- **The release refuses a repository behind or diverged from its
  origin.** It offers `/pull`.
- **A red test.** `/test` prints the failure as pytest printed it.
  The release stops, the failures reported as `/test` reports them,
  and does not run: back to the fix, the script changed with its
  test.
- **`No module named pytest`.** The tests did not run. The one thing
  a contributor installs beyond `python` is pytest:
  `python -m pip install pytest`. The release goes on only on your
  word.
- **A check finds something.** The findings are settled by
  walkthrough, never fixed silently. A finding you have not settled
  when you order the release to go on is parked by that word, said
  aloud, since the check is advisory.
- **`/check single-source-of-truth` reports a restatement.** The
  same steps, rules or shape stand in two places. The fix is a
  reference to the owner and the deletion of the copy; where a
  shape has no owner at all, the finding proposes one.
- **A recipe is missing at the release.** It is reported as a check
  finding, and the repository is released without that render.
- **The scan of a regenerated render hits.** `/render` scans the
  written file for the instance's facts; a hit is said aloud and
  you judge it. An instance fact is regenerated out, never edited
  by hand.
- **`/render contributing` finds no recipe.** Claude offers to
  compose one through `/recipe` and stops.

## A worked example

An invented change: you want the state map that `/forge` shows to
name the render that has been stale longest. That alters behaviour,
so it goes through the chain.

You open `/forge intent forge`. Claude reads the history of the
positions on the state map and on stale renders, asks what you want
and why, and reflects it back. On your `write` the position lands in
`projects/forge/10-intent.md`, saying that the map names the oldest
stale render and why that is wanted, with its record in
`projects/forge/10-intent.history.md`. The intent's version is
raised by the round.

You go on with `/forge solution-design forge`. The item says what is
built: the map reads the age of each stale render and names the
oldest. It names the position it realises, the choice it rests on
(the age read from the provenance of the render against a date kept
elsewhere) and where it lives: the `/forge` skill and the script
that makes the ledger. Its record goes into the design's companion.

The change needs a test, so the order was different from the start:
you wrote a short brief in your own words first, built the change
in the skill and in the script with a test in `tests/` beside it,
and held the two rounds above right after the build, before any
release.

You run `/test` and see `<n> passed in <s>s`. You run
`/check engine`, which states that the check passed. Since this was
a round on the operating layer, you run
`/check single-source-of-truth`. It finds the rule of the oldest
render stated twice, in the skill and in the script's help header.
You settle the finding by walkthrough: the skill cites the script's
header, and the copy goes.

Every document you touched has its record. You run `/release forge`
on `main`: the tests run first, then the checks; you decline the
critique; the release reports the age of the documentation and you
run `/document`; the README and the release notes are regenerated,
and you rule on the delta; the state render is written; the release
is saved with the message `release <intent version>: <one line>`.

To send it to the public engine, you have pushed to your fork with
`/save` and open a pull request from your fork's page. It carries
the position with its record, the item, the change with its test,
and one line on what you ran: `/test`, `/check engine` and
`/check single-source-of-truth`. It carries no release and no
regenerated README; the author makes those at the next release.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an
  intent.
- [Check conformance](../use/check-conformance.md): running the
  checks.
- [Run the tests](../use/run-the-tests.md): running the tests.
- [Release a version](../use/release-a-version.md): the release.
- [Render an output](../use/render-an-output.md): regenerating a
  render such as CONTRIBUTING from its recipe.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [The security policy and the code of conduct](../about/the-security-policy-and-the-code-of-conduct.md):
  the two fixed files the contributing file points at.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
