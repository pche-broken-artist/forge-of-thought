---
generated: 2026-10-09
made: derived
inputs-hash: 6dbb0aa8d471b5f2
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/document/SKILL.md
  - projects/forge/recipes/contributing.md
---

# Make a change to the forge

This page is for the extender who wants to change how the forge
behaves: add a rule, alter a command, change what a reviewer looks
for. It puts together, from `CLAUDE.md`, the forge's own intent, the
two check agents `check-engine` and `check-single-source-of-truth`,
the `/release` and `/document` skills and the recipe of
`CONTRIBUTING.md`, the order in which one change travels from the
idea to the released engine.

## Two kinds of change

The forge draws one line between changes, by what a change does,
never by its size.

- A change of how the forge behaves: a command, a rule, a
  convention, what a reviewer looks for. It goes through the chain
  before it is built, in the order this page gives.
- A change that alters no behaviour: a wording, a broken path, a
  slip. It is made directly, where it stands, and nothing else is
  needed.

The reason is the forge's own rule for every project: a change of
substance goes into the intent first and propagates from there down
the chain. The forge is run through its own process, so the rule
holds for the forge itself.

## The order of one change of behaviour

### 1. The position in the forge intent

Open the forge intent with `/forge intent forge`. The change becomes a
position there: what is wanted and why. The write of the round
appends a record to the intent's history companion beside it, in the
same step as the change; the record names the item it touches and
carries what ceased to hold.

The change may come from below. When building shows that what is
wanted cannot be had, or must be wanted differently, the intent still
changes first and the layers follow. Only wording is fixed downstream
directly.

### 2. The item in the solution design

Where the change solves something, it gets its item in the forge's
solution design, `projects/forge/40-solution-design.md`, through
`/forge solution-design forge`. The intent holds what is wanted and
why; the solution design holds what is built or done and what it
realises.

### 3. The operating layer

Only then is the operating layer changed: `CLAUDE.md`, the skills
under `.claude/skills/`, the agents under `.claude/agents/`, the
templates and the scripts. Where the operating layer and the intent
differ after this step, that is a finding: the `engine` check
verifies that every position of the intent is honoured by the core
and that nothing withdrawn or rejected is still advertised.

A change of the operating layer that touches no item of the intent is
still recorded: in the forge project it goes into the history under
the subject `operating layer`, one record a round, so that the release
notes can be derived from it.

### 4. Proving it

Two checks prove a change of the forge; both are run by hand with
`/check`, and their findings are settled by walkthrough.

- `/check engine` reads the core, `CLAUDE.md`, the templates, the
  skills, the agents and the scripts, against itself and against the
  forge intent: the commands table against the skills on disk, the
  scripts on disk against the layout, the templates against the
  conventions; every position honoured, every decision reflected; a
  sweep for names that were renamed or dropped. It is cheap enough
  that every release runs it.
- `/check single-source-of-truth` reads the whole operating layer,
  always the whole and never a changed subset, and verifies that
  every rule, procedure and file shape is written in one place and
  cited everywhere else: one owner per rule, reviewer files carrying
  only their own Lens section, no direct operation where a script,
  command or agent exists for it. It is expensive by design and is
  not run at a release: its fit is before a major or after a round on
  the operating layer, on the principal's word, when there is time
  for it.

A restatement found by the second check is fixed by a reference to
the owner and the deletion of the copy, never by a third description.

### 5. Releasing

`/release forge` releases the engine from `main`. It runs the `light`,
`engine` and `project` checks, settles their findings by walkthrough,
and then regenerates the README and the release notes from their
recipes, unconditionally, with a short summary of what materially
changed in them so that the principal rules on the delta before the
commit. Then it saves with the release message, drawn from the
records of the intent's history since the last release, and at an
approved major the tag.

Between the renders and the save, the release reports the age of the
documentation: the version in the front-matter of `docs/README.md`
against the intent's version, and offers `/document` in one sentence.
On the principal's word it runs; on his no, or silence, nothing runs.
A release never regenerates the documentation on its own.

### 6. The documentation

`/document` regenerates the documentation in `docs/`: the planner
rewrites the map, a script compares every entry's inputs with the
hash the existing page carries, and only the pages whose inputs
changed are remade; the index is derived from the map. The run asks
nothing, and no page is touched by hand: what is wrong on a page is
mended in the file that owns the matter, and the page is regenerated.

### When the change is complete

A process change is complete only once the forge intent is updated
and the README re-rendered. Until both are done the change is
somewhere between the files, and the next `engine` check will say so.

## Changing a document that is a render

`README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md` in the
repository root are renders: generated from a recipe, never edited by
hand. A change to one of them goes into its recipe in
`projects/forge/recipes/` or into what the recipe reads, and the file
is regenerated with `/render`. A claim in the README that `CLAUDE.md`
or the intent no longer supports is a defect of the recipe, fixed
there.

## Sending a change from outside

A visitor who has used the forge and wants to say, ask or change
something reads `CONTRIBUTING.md` in the repository root. It names
one channel by kind for each case: a discussion for feedback and for
an idea, which is what the forge wants most; an issue for a defect,
when a command does something other than it says, a file is missing
or a link is dead.

For a change of behaviour the file says what a pull request carries:
the position in `projects/forge/10-intent.md` saying what is wanted
and why, with its record in the history beside it; the item in
`projects/forge/40-solution-design.md` where the change solves
something; and the change itself. A brief may come first and need
not. The easiest way is to open a discussion first, and the forge's
own commands do this work. A change that alters no behaviour is sent
as it is.

Two rules hold for every change sent: nobody sends a change he has
not tried himself, and a change written with an AI is welcome on the
same rule, the pull request saying what was run. What enters the
forge stays the principal's decision.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md): regenerating the pages.
