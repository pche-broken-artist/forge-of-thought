---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - projects/forge/recipes/contributing.md
---

# Make a change to the forge

This page is for someone who wants to change how the forge itself
works: a command, a rule, a convention, what a reviewer looks for. It
gives the order of one change, from the reason to the release. It was
put together from `CLAUDE.md`, the forge intent
(`projects/forge/10-intent.md`), the two check agents
`.claude/agents/check-engine.md` and
`.claude/agents/check-single-source-of-truth.md`, the release skill
`.claude/skills/release/SKILL.md` and the contributing recipe
`projects/forge/recipes/contributing.md`. None of them states the
whole order in one place; the page joins what each says.

## First decide which kind of change it is

The line is drawn by what the change does, never by its size.

- **A change of behaviour** alters how the forge behaves: a command,
  a rule, a convention, what a reviewer looks for. It goes through
  the chain before it is built (below).
- **A change that alters no behaviour**, such as a wording, a broken
  path or a slip, does not go through the chain. You make it
  directly.

The reason: the forge is run through its own process. A change of
substance goes into the intent and propagates from there down the
chain; only wording is fixed downstream directly.

## Make a change of behaviour

1. **Write the position in the forge intent.** Run
   `/forge intent forge`. The change becomes a position in
   `projects/forge/10-intent.md` saying what is wanted and why. The
   write adds its record to the history companion beside the intent,
   `projects/forge/10-intent.history.md`. A brief may come first, but
   need not.
2. **Write the item of the solution design, where the change solves
   something.** Run `/forge solution-design forge`. The item goes into
   `projects/forge/40-solution-design.md`.
3. **Change the operating layer.** This is the engine itself:
   `CLAUDE.md`, the skills in `.claude/skills/`, the agents in
   `.claude/agents/`, the templates in `templates/` and the scripts in
   `scripts/`. Where the operating layer and the intent differ, that
   is a finding, not a choice of which one to follow.
4. **Record it.** Every versioned document keeps its history in its
   companion `<file>.history.md`, one record per change. A change of
   the operating layer that touches no item of the intent is recorded
   in the forge's own project under the subject `operating layer`,
   one record a round, so that the release notes can be derived from
   it. What the user must do after the change is written with it, in
   the record's `Action` field.
5. **Prove it with the checks.**
   - `/check engine` verifies the core (`CLAUDE.md`, templates,
     skills, agents, scripts) against itself and against the forge
     intent: every position honoured, nothing withdrawn or rejected
     still advertised, every decision reflected. It is cheap enough to
     run at every release.
   - `/check single-source-of-truth` verifies that every rule,
     procedure and file shape is written in one place and cited
     everywhere else, and that no skill or agent does directly what a
     script, command or agent exists for. It reads the whole operating
     layer and is expensive by design: run it before a major or after
     a round on the operating layer, not at every release. A release
     does not run it for you.
6. **Release it.** Run `/release forge` from `main`. It runs the
   checks `light`, `engine` and `project`, settles their findings by
   walkthrough, and only then re-renders the README and the release
   notes from their recipes. You see a summary of what changed in the
   regenerated files and rule on it before the commit.

A process change is complete only once the intent is updated and the
README re-rendered.

## Change a generated document

`README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md` in the root are
renders: they are generated and never edited by hand. A change to one
of them goes into its recipe in `projects/forge/recipes/`, or into
what the recipe reads, and the file is regenerated.

## If you are a visitor

`CONTRIBUTING.md` in the repository root is the way a visitor sends
feedback, an idea or a change. Feedback and ideas are what the forge
wants most; a finished change is welcome on the same rule as above,
and nobody sends a change he has not tried himself. For a change of
behaviour the pull request carries the position in the intent with
its history record, the item of the solution design where the change
solves something, and the change itself; the easiest way is to open a
discussion first. A change that alters no behaviour needs nothing but
the pull request. What enters the forge stays the principal's
decision.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
