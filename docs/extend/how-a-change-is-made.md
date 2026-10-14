---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 27c465c73af5b36f
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

A change to the forge is one of two kinds: a change of how the forge
behaves, which goes through the forge's own chain before it is
built, or a change that leaves the behaviour as it is, which is made
directly. This page is for you, the extender, whether you change the
engine in your own clone or want to send a change to the public
engine: what you do in which order, what proves the change, where it
is recorded and how it is released. The forge runs its own
development as a project of its own, `projects/forge/`, with a brief,
an intent, a solution design, decisions and a ledger (the file that
holds the state of a project); that project is the chain this page
walks.

## When to use it

Use this page whenever you want to change what the engine is or
does. First decide which kind of change you have. The line between
the kinds is drawn by what the change does, never by its size.

- A change of behaviour: a command, a rule, a convention, what a
  reviewer looks for. It goes through the chain, as the steps below
  say.
- A change that alters no behaviour: a wording, a broken path, a
  slip. It is made directly, in the file that holds it, and nothing
  else is needed. For the public engine it is sent as it is.

Two things to know before you start.

- The README, the release notes and `CONTRIBUTING.md` are renders:
  files generated from a recipe, never edited by hand. A change to
  one of them goes into its recipe in `projects/forge/recipes/` or
  into what the recipe reads, and the file is regenerated. The
  pages of `docs/` are generated the same way, by `/document`, from
  the files that own each topic; a fix goes into the file the page
  mirrors, and the pages are regenerated as
  [Generate the documentation](../use/generate-the-documentation.md)
  says.
- In your own clone you decide everything: the forge there is
  yours. What is merged into the public engine its author decides.
  Nobody sends a change he has not tried himself; a change written
  with an AI is welcome on the same rule, and what was run is said
  with it.

## What you do

For a change of behaviour, the commands in order; `forge` is the
slug of the forge's own project and names the engine:

```
/forge intent forge
/forge solution-design forge
/check engine
/check single-source-of-truth
/release forge
```

Between the second and the third line you make the change itself,
in the operating layer. The operating layer is where the behaviour
lives:

- `CLAUDE.md`
- the skills under `.claude/skills/`
- the agents under `.claude/agents/`
- the templates under `templates/`
- the scripts in `scripts/`, with their help headers

For a change meant for the public engine, the last line is replaced
by a pull request, as "What happens" says.

## What happens

1. **The position.** `/forge intent forge` opens a round on the
   forge intent, `projects/forge/10-intent.md`. A change of
   substance goes into the intent first and propagates down the
   chain from there, whichever layer showed the need for it; this is
   the working method intent-first. The round runs as a conversation
   with Claude, as [Forge the intent](../use/forge-the-intent.md)
   says, and ends in one write on your word. The write puts a
   position into the intent, saying what is wanted and why, bumps
   the intent's version and appends one record per change to the
   history companion `projects/forge/10-intent.history.md`. The
   record holds the way to the item: why it changed, what was said,
   what was tried; the item itself holds only what holds now.
   `last_change` in the intent's front-matter is derived from the
   records by the write, never set by hand. You should now see the
   new position in the intent and its record in the history beside
   it.

2. **The item.** `/forge solution-design forge` opens a round on the
   solution design, `projects/forge/40-solution-design.md`, where
   the change solves something: the item says where in the operating
   layer the change lives. The write records it in the history
   companion beside the solution design in the same way. You should
   now see the item in the solution design and its record in the
   history beside it.

3. **The change.** You make the change in the operating layer, in
   the one file that owns the mechanism. Every command, agent,
   contract and template describes only its own job; a procedure, a
   rule set or a file shape that another file owns is cited by path,
   never restated. Where the change touches what the README says, it
   goes into `projects/forge/recipes/readme.md`, since the README is
   a render of the forge project. You should now see the changed
   files, and no second copy of the same rule anywhere.

4. **The proof.** `/check engine` runs the check of the core against
   itself and against the forge intent, as
   [Check conformance](../use/check-conformance.md) says. It verifies
   that the commands table of `CLAUDE.md` matches the skills on disk,
   that the agents described exist, that every skill an agent names
   exists, that every file in `scripts/` is described in `CLAUDE.md`
   and nothing described there is missing, that the README and
   `CLAUDE.md` do not contradict each other, that the templates agree
   with the conventions, that every position is honoured by the core,
   that nothing withdrawn is still advertised, and that every
   decision is reflected where it applies; and it sweeps the core for
   names that were renamed or dropped. The check reads the core files
   once and the intent's positions once, so that a release can afford
   it every time. You should now see Claude report that the check
   passed, or its findings.

   `/check single-source-of-truth` is the honest sweep: it reads the
   whole operating layer, always the whole and never a changed
   subset, and verifies that every rule, procedure and file shape is
   written in one place and cited everywhere else, that every
   reviewer file carries only its front-matter and its Lens section,
   and that no skill or agent performs directly what a script, a
   command or an agent exists for. It is expensive by design; it fits
   before a major or after a round on the operating layer, not at
   every release. You should now see a report whose first line says
   how many files it read, then that it passed or its findings.

5. **The release.** `/release forge` releases the engine from
   `main`, as [Release a version](../use/release-a-version.md) says.
   It runs the checks `engine` on the engine root and `light` and
   `project` on `projects/forge`, reports the result even when clean,
   and settles findings by walkthrough (the findings taken one by
   one, each settled or parked by your word). It offers
   `/critique essence` once, in one sentence, and runs it only on
   your word. It then regenerates the README and the release notes
   from their recipes, unconditionally, and reports what materially
   changed in them: you rule on the delta before the commit. It
   reports the age of the documentation, the `version` of
   `docs/README.md` against the intent's version, and offers
   `/document` in one sentence; it runs `/document` only on your
   word, never on its own. Then it saves with the message
   `release <intent version>: <one line>`, the line drawn from the
   records of the intent's history since the last release, and, when
   the intent's version is an integer, proposes the tag `v<major>`,
   taken on your word. A process change is complete only once the
   intent is updated and the README re-rendered. You should now see
   the release reported step by step, the regenerated README and
   release notes, and the commit pushed.

6. **The pull request**, for the public engine instead of step 5.
   `CONTRIBUTING.md` says the easiest way is to open a discussion
   first, and names a way for each kind of message: what you found,
   what is broken, an idea, a change. A pull request for a change of
   behaviour carries the position in `projects/forge/10-intent.md`
   with its record in the history beside it, the item in
   `projects/forge/40-solution-design.md`, the change itself and one
   line on what you ran. It carries no release and no regenerated
   README, release notes or documentation: the author makes those at
   the next release. A brief may come first and need not. You should
   now see the pull request open with those four things in it.

## What you have afterwards

- The position in the forge intent, with its record in
  `projects/forge/10-intent.history.md`: the one place that says
  what is wanted and why.
- The item in the solution design, with its record in the history
  beside it: where the change lives.
- The change in the one file of the operating layer that owns the
  mechanism, cited by path from wherever else it is needed.
- The check reports: `/check engine`, and
  `/check single-source-of-truth` where the round touched the
  operating layer.
- In your own clone: a release on `main` with the README and the
  release notes regenerated, the commit message derived from the
  intent's history, and the documentation regenerated if you took
  the offer of `/document`.
- For the public engine: a pull request with the position, the
  item, the change and one line on what was run.

## If something goes wrong

- **`/release` stops and names a branch.** A release runs on `main`
  only. On any other branch it stops, reports the branch the
  repository is on and how to get back:
  `python scripts/forge-branch.py forge main`, after saving.
- **A check finds something.** The findings are settled by
  walkthrough, never fixed silently. A finding may be parked and the
  release proceeds. The check is advisory: you may order the release
  to go on at any moment, and every finding you have not settled is
  parked by that word, said aloud.
- **`/check single-source-of-truth` reports a restatement.** The
  same steps, rules or shape stand in two places, whatever the
  wording. The fix is a reference to the owner and the deletion of
  the copy. Where a shape has no owner at all, the finding proposes
  one, a template or a section of `CLAUDE.md`, never a second
  description.
- **`/check engine` reports a claim in the README that `CLAUDE.md`
  or the intent no longer supports.** That is a recipe defect: fix
  `projects/forge/recipes/readme.md`, never the README. The README
  and the release notes are regenerated at the release after the
  check, so currency is never a finding.
- **`/check engine` reports a skill an agent names that does not
  exist.** Claude Code skips a missing skill silently, so the agent
  would run without its contract; add the skill or fix the name in
  the agent's front-matter.
- **`/release` reports a missing recipe.** A project whose recipe is
  missing is reported as a finding and released without that render.

## A worked example

The change is invented, to show the path only. Suppose you want
`/release`, after it has regenerated the README and the release
notes, to list the project's other renders that have grown stale,
without regenerating them.

1. You run `/forge intent forge`. In the conversation you say what
   you want and why: the release should show what it leaves stale,
   so that the delta is seen before the save. At the end of the
   round you say `write`. The intent gets a new position saying
   that, its version goes up by one minor, and
   `projects/forge/10-intent.history.md` gets one record naming the
   position, what changed and why.

2. You run `/forge solution-design forge`. The write adds an item to
   `projects/forge/40-solution-design.md` saying that the listing is
   a step of `.claude/skills/release/SKILL.md`, after the two renders
   are regenerated, and records it in the history beside the
   solution design.

3. You edit `.claude/skills/release/SKILL.md` and add the step. You
   leave `CLAUDE.md` as it is: it cites the release skill by path for
   what a release does, and the sentence it keeps on the release
   still holds.

4. You run `/check engine`. It reports that the check passed. Since
   the round touched the operating layer, you run
   `/check single-source-of-truth`. Its first line says how many
   files it read; it finds nothing, since the new step is described
   in the release skill alone.

5. In your own clone you run `/release forge` from `main`. The
   checks pass; you decline `/critique essence`; the README and the
   release notes are regenerated and Claude names what changed in
   them. Claude reports that the documentation is older than the
   intent and offers `/document`; you take the offer, so that the
   page on the release says what the release now does. The commit
   goes out as `release <intent version>: <one line>`.

   For the public engine you open a discussion first, then a pull
   request carrying the position with its record, the item, the
   changed skill and one line: the two checks run and clean, the
   change released once in your own clone. The README, the release
   notes and the pages of `docs/` stay as they are; the author
   regenerates them at the next release.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an
  intent.
- [Check conformance](../use/check-conformance.md): running the
  checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md):
  regenerating the pages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
