---
generated: 2026-10-10
made: derived
inputs-hash: 9ff5be31c11f88cb
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

This page is for the extender: someone who wants to change how the
forge behaves, a command, a rule, a convention, what a reviewer looks
for, and wants to know the order in which that change is thought
through, built, proved, recorded and released. It was put together
from `CLAUDE.md`, the forge intent, the two check agents `engine` and
`single-source-of-truth`, the `/release` and `/document` skills and
the recipe of `CONTRIBUTING.md`; it joins what they say into the
order of one change.

## Two kinds of change

The forge draws one line between changes, and it is drawn by what a
change does, never by its size.

- **A change of how the forge behaves** goes through the chain before
  it is built. The forge is run through its own process: it has a
  project of its own, `projects/forge/`, with a brief, an intent, a
  solution design, decisions and a ledger, and a change of behaviour
  begins there, not in the files that implement it.
- **A change that alters no behaviour**, a wording, a broken path, a
  slip, is made directly in the file where it stands, and nothing
  else is needed.

The rest of this page is the first kind, with one section at the end
for a document that is a render and one for a visitor who sends a
change from outside.

## The order of a change of behaviour

### 1. Say what is wanted, in the intent

Substance goes into the intent first and propagates down the chain
from there; this is the forge's working method called intent-first.
Even when a need shows up below, in the solution design or in a
skill, the intent changes first and the layers follow.

Run `/forge intent forge` and work the change as a position of the
forge intent, `projects/forge/10-intent.md`: an item saying what is
wanted and why, with the reason in it. A brief may come before the
intent and need not. The work runs as one round: what is agreed is
carried in the conversation, reflected back, and written once at the
round's end on your word, one version bump for the whole round. The
write appends a record to the intent's history companion,
`10-intent.history.md`, in the same step as the change, with `Was`
holding the wording that ceased to hold. Before a change to an
existing item is proposed, its history is searched for the item's ID,
so that a direction once tried and dropped is seen before it is
tried again.

### 2. Solve it, in the solution design

Run `/forge solution-design forge` and bring the solution design,
`projects/forge/40-solution-design.md`, to the new position: the item
where the change solves something, what is built or done, what it
realises and the choice it rests on. Its history companion receives
its record the same way.

### 3. Change the operating layer

Only now does the change reach the files that make the forge run:
`CLAUDE.md`, the skills under `.claude/skills/`, the agents under
`.claude/agents/`, the templates under `templates/` and the scripts
under `scripts/`. Together these are the operating layer.

Two rules govern how it is written:

- **One mechanism lives in one place.** Whatever the forge has a
  procedure for is used through its own definition and cited by path
  from anywhere else; a procedure stated in two places is a defect,
  because the two copies drift and the copy without a rule silently
  loses it. A rule that is new and has no owner gets one, a skeleton
  or a section, never a second description.
- **The operating layer honours the intent.** Every position of the
  forge intent is to be honoured by the core documents, and nothing
  withdrawn or rejected may still be advertised there. Where the
  operating layer and the intent differ, that difference is a
  finding, found by the check in step 5.

### 4. Record it

Every versioned document keeps its history in an append-only
companion beside it, and the record is written in the same step as
the change. A round that touched the intent or the solution design
already has its records from steps 1 and 2.

A change of the operating layer that touches no item of the intent
still gets a record: in the forge's own project it is written under
the subject `operating layer`, one record a round, so that the
release notes can be derived from it. What the user must do after
the change, if anything, is written with the record in its `Action`
field; the release notes carry it word for word into their
*Action required*.

The ledger, `projects/forge/ledger.md`, is kept current after every
operation.

### 5. Prove it

Two checks verify a change of the operating layer. Both are
mechanical conformance checks, never a critic of the documents and
never a challenger of the thinking, and each owns one concern and
none of the other's.

- `/check engine` is run at every release and whenever you want it.
  It reads the core, `CLAUDE.md`, the templates, the skills, the
  agents and the scripts, and the forge intent with its threads and
  decisions, and verifies the core against itself and against the
  intent: the commands table against the skills on disk, the agents
  described against the agents present, every skill an agent names in
  its front-matter present, every script on disk described in
  `CLAUDE.md`, the templates in agreement with the conventions; every
  position honoured and nothing withdrawn still advertised; every
  decision reflected in the intent; and a sweep for names that were
  renamed or dropped. It costs minutes, so a release can afford it
  every time.
- `/check single-source-of-truth` is the honest sweep, expensive by
  design. It reads the whole operating layer, always the whole and
  never a changed subset, and verifies that every rule, procedure and
  file shape is written in one place and cited everywhere else, that
  a reviewer file carries only its own front-matter and Lens section,
  and that no skill or agent performs directly what a script, a
  command or an agent exists for. It is fit before a major or after a
  round on the operating layer, run on your word; a release never runs
  it on its own, so that the rule costs a release nothing.

A check that finds nothing files nothing. Findings are filed as an
immutable, dated report in `projects/forge/reviews/` and settled by
walkthrough, one item per message; a finding may be parked. The
check is advisory: nothing blocks, only you publish.

### 6. Release it

Run `/release forge`. The release runs from `main` only; on another
branch it stops and says how to get back. It then:

1. runs the checks `light`, `engine` and `project` over the sources,
   launched at once, and reports the result even when clean; findings
   are settled by walkthrough before anything is rendered, so that a
   fix of the walkthrough is already in what the renders derive from;
2. offers the critic lens `essence` once, in one sentence, and runs
   it only on your word;
3. regenerates `README.md` and `RELEASE-NOTES.md` from their recipes
   through `/render`, unconditionally, and reports what materially
   changed in them, because a regeneration is stochastic and passes
   under your eyes before the commit; no other render is regenerated
   here;
4. reports the age of the documentation, the `version` in the
   front-matter of `docs/README.md` against the intent's version, and
   offers `/document` in one sentence; it runs only on your word,
   before the save, so that the release carries current pages. A
   release never regenerates the documentation on its own;
5. saves through `/save` with the message `release <intent version>:
   <one line>`, the line drawn from the records of the intent's
   history since the last release, and, when the intent's version is
   an integer, proposes the tag `v<major>`, taken on your word.

A process change is complete only once the forge intent is updated
and the README re-rendered.

### 7. Regenerate the documentation

The documentation in `docs/` is generated, never composed by hand.
`/document` runs as one run that asks nothing: a planner writes the
map, `projects/forge/docs-map.md`, a script computes which pages are
stale from the hashes of each page's inputs, one writer per stale
page remakes it, and scripts derive the index and check the pages.
Only the pages whose inputs changed are regenerated; the rest are
kept. What is wrong on a page is mended in the file that owns the
matter, and the page is regenerated; a page is never touched by hand.
The run is a guarded command: it starts on your word, by slash or by
asking in words, never on Claude's own judgement.

## A change of a document that is a render

`README.md`, `RELEASE-NOTES.md` and `CONTRIBUTING.md` in the
repository root are renders: generated from recipes, never edited by
hand. A change to one of them goes into its recipe in
`projects/forge/recipes/` (`readme.md`, `release-notes.md`,
`contributing.md`) or into what the recipe reads, and the file is
regenerated with `/render <recipe>`. The README and the release notes
are regenerated at every release; `CONTRIBUTING.md` is not, so after
a change to its recipe you run `/render contributing` yourself. A
recipe is versioned and keeps a history companion like any artefact,
but it stays at 0.x and is never approved.

## Sending a change from outside

A visitor to the repository finds the way in `CONTRIBUTING.md` in the
root. It names three channels by kind: a discussion for what you
found and for an idea, an issue for something broken, and a pull
request for a change. Feedback and ideas are what is wanted most, and
for a change of behaviour the easiest way is to open a discussion
first.

A pull request for a change of behaviour carries the same things as
the order above: the position in `projects/forge/10-intent.md` saying
what is wanted and why, with its record in the history beside it; the
item in `projects/forge/40-solution-design.md` where the change
solves something; and the change itself. The forge's own commands do
this work. A pull request for a change that alters no behaviour
carries the change alone. Whatever the kind, try your change yourself
before you send it; a change written with an AI is welcome on the
same rule, and the pull request says what was run. What enters the
forge stays the principal's decision.

## See also

- [Forge the intent](../use/forge-the-intent.md): iterating an intent.
- [Check conformance](../use/check-conformance.md): running the checks.
- [Release a version](../use/release-a-version.md): the release.
- [Generate the documentation](../use/generate-the-documentation.md): regenerating the pages.
