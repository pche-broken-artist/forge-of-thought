---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: cdbb706a00528acb
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/agents/docs-planner.md#What you read
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - .claude/skills/release/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
  - projects/forge/10-intent.md#REJ.0500
  - projects/forge/10-intent.md#POS.1980
---

# Generate the documentation

This page tells you how `/document` makes the pages of the
documentation and their index, and what you have at the end of a run.
It is for the user who documents a project and for the extender who
documents the engine. What the documentation is and why it is
generated is told in [The documentation](../about/the-documentation.md).

Three words are used here. The principal is whoever's thinking is
being forged. The ledger is the file that holds the state of a
project, made at read time from its documents. A subagent is a
helper that Claude launches to do one job in isolation: it sees
nothing of your conversation and reads its inputs from disk.

## When to use it

Use it when the pages are out of date with the files they are made
from, or when a project has none yet. Nothing is edited by hand on a
page: what is wrong on a page is mended in the file that owns the
matter, and the page is made again by this command. How such a mend is
made is told in
[Change a documentation page](../extend/change-a-documentation-page.md).

## The command

```
/document
```

Bare, the target is the engine. With a slug, the target is that
project:

```
/document <slug>
```

The run asks you nothing from start to end.

### What each target needs and gives

Bare, the pages land in `docs/` at the engine root. The map they are
made from lies beside the ledger of `projects/forge`, the forge's own
project. That project must therefore be cloned beside the engine, as
it is on the machine of whoever develops the engine and on no user's.
Why it is a repository of its own is told in
[Projects and the engine](../about/projects-and-the-engine.md).

With a slug, the pages land in `projects/<slug>/docs/` and the map
lies beside that project's ledger. The planner reads the project's:

- briefs
- intent
- threads
- layers below the intent
- ledger
- indexes of `sources/` and `research/`
- recipes
- whatever its documents point to on disk

Nothing else is read, and a project has no setting of its own to
document more. The pages are written in the project's language, as
its artefacts are.

`docs/videos/` of the engine is not the documentation's. The run
leaves it alone.

### Where it may run

It runs on `main` only. It refuses a repository that is behind its
origin or has diverged from it, and offers `/pull`.

## What happens

1. The previous map is taken from git into `tmp/`, the engine's
   working folder. A planner reads the target on disk and writes the
   map. Its task names the open findings of the last documentation
   report that concern the map, so that the planner brings those
   entries to their owners' wording. You should now see a map beside
   the owning project's ledger.
2. A script computes the state of every page from the content of its
   inputs and of the rule the pages are made by. A page is new,
   regenerate, keep or remove. A page whose inputs did not change is
   kept, never regenerated. The script writes one task per page that
   is made. You should now see a summary of the four states.
3. The pages that lost their entry are deleted. You should now see
   them named as removed.
4. Claude says how many pages it is about to make and on which models,
   before it launches the writers. One writer per page then makes it
   from its entry and inputs alone. You should now see the pages
   appear under the target's `docs/`.
5. A script derives the index from the map. You should now see
   `docs/README.md` with one line per page.
6. A script checks every page: that each entry has its page and no
   page lacks an entry, that every link to a page resolves, that no
   page holds a long dash in its prose, that each opens with
   front-matter, and that none carries an instance fact. A failing page
   is regenerated once. A page that fails twice is left out of the
   documentation and said aloud. You should now see the check's result
   with no failure.
7. The ledger is remade, so that its Renders table carries the index.
   The run is then reported. You should now see the counts, the check's
   result and, where the run left something, the report of the run.

## What you have afterwards

- The pages and the index under the target's `docs/`.
- The counts: pages new, regenerated, kept and removed.
- The check's result.
- The ledger remade, its Renders table carrying the index.
- What the run could not place, filed as a report of the run in
  `reviews/` under the name of a check, one finding per matter:
  - a fact that no file owns
  - a matter on which the map and an owner disagree
  - a claim the map asked for and no input carried
  - every place where a writer wanted a reason and none is recorded

A run that leaves nothing files nothing.

The findings of that report are settled by walkthrough, as a check's
are: one item per message, each closed with your verdict. How that
goes is told in [Check conformance](check-conformance.md). A mend
lands in the file that owns the matter, never on a page.

## If something goes wrong

- The repository is behind or has diverged: the run is refused and
  `/pull` is offered. Pull, then run again.
- A page fails the check: it is regenerated once with the failure
  named. If it fails again it is left out of the documentation and
  reported, never mended by hand.
- An input that the map names is missing on disk: the page is
  regenerated and its writer reports the gap in the run's report.

## In a release

A release never runs the documentation on its own judgement. A
release by hand reports the index's age against the intent's version
and offers the command. With `--auto` it asks once before anything
runs, and the default is yes. See
[Release a version](release-a-version.md).

## A worked example

A generic closing report of a run on a project with the placeholder
slug `<slug>`. The figures are placeholders.

```
Documentation of <slug>
  pages: <a> new, <b> regenerated, <c> kept, <d> removed
  check: no failure
  ledger: remade, Renders table carries docs/README.md

Filed: reviews/<date>-check-documentation-<time>-<hash>.md
  FND.<n>  medium  a matter the map and an owner disagree on
  FND.<n>  low     a page wanted a reason, none is recorded
```

You then settle the two findings by walkthrough. Each mend goes into
the file that owns the matter, and the next run regenerates the page.

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Check conformance](check-conformance.md): how a report's findings are settled by walkthrough.
- [Release a version](release-a-version.md): the release that reports the documentation's age and offers the run.
- [Projects and the engine](../about/projects-and-the-engine.md): why the forge's own project is a repository of its own that whoever develops the engine clones beside it.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
