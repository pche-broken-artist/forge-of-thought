---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a4808bd30c294cb7
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
documentation and their index, and what you have at the end of the
run. It is for the user and for the extender. The principal is the
person whose thinking is forged; the run is his to start, and it asks
him nothing once it has begun. A subagent is an agent Claude launches
for one job, which sees nothing of the conversation. The ledger is the
state of a project, made from its documents each time it is read.

## When to use it

Use it when the pages are older than what they describe, or when a
project has no documentation yet. What the documentation is, for whom
and why it is generated is the page [The
documentation](../about/the-documentation.md).

A release by hand never runs it on its own judgement. It reports the
age of the index against the version of the intent and offers the
command; you decide. With `--auto` the release asks once, before
anything runs, whether the documentation runs, and the default is yes
(see [Release a version](release-a-version.md)).

## The command

```
/document [slug]
```

Bare, the target is the engine. The pages land in `docs/`. The map is
kept beside the ledger of `projects/forge`, the forge's own project.
That project must therefore be cloned beside the engine, as it is on
the machine of whoever develops the engine and on no user's machine
(why: [Projects and the engine](../about/projects-and-the-engine.md)).

With a slug, the target is that project. The pages land in
`projects/<slug>/docs/` and the map lies beside the project's ledger.
The planner reads the following, and nothing a project would set for
itself:

- the project's briefs
- its intent
- its threads
- the layers below the intent
- its ledger
- the indexes of `sources/` and `research/`
- its recipes
- whatever its documents point to on disk

The pages are written in the project's language, as its artefacts are.

The command runs on `main` only. It refuses a repository that is
behind its origin or has diverged from it, and it offers `/pull`.

## What happens

1. The previous map is taken from git into `tmp/`, the engine's working
   folder. You should now see its path printed, or `none` where there
   is no earlier map.
2. A planner, one subagent, reads the target on disk and writes the
   map: one entry per page. Its task names the open findings of the
   last documentation report that concern the map, so that the planner
   brings those entries to their owners' wording. You should now see
   the map beside the ledger.
3. A script computes the state of every page from the content of its
   inputs and of the rule the pages are made by. A page is `new` where
   none exists, `regenerate` where its inputs or the rule changed, and
   `keep` where nothing changed. A page that no entry names, or whose
   entry was marked for removal, is `remove`. The script writes one
   task per page to be made. You should now see a summary of the four
   states.
4. Pages that lost their entry are deleted. You should now see Claude
   say which.
5. Claude says how many pages it is about to make and on which models,
   and then launches the writers. One writer makes each page, from its
   entry and its inputs alone. You should now see the writers return,
   each with a report of what its inputs did not support.
6. A script derives the index, `docs/README.md`, from the map. No model
   is involved. You should now see the index written.
7. A script checks every page: that every page of the map exists and no
   other page lies in the folder, that every relative link to a page
   resolves, that no prose carries a long dash, that every page opens
   with a front-matter, and that no fact of the instance reaches a
   page. A failing page is regenerated once. A page that fails twice
   is left out of the documentation, and Claude says so aloud. You
   should now see the check's result.
8. Claude remakes the ledger of the owning project, and files what the
   run could not place. You should now see the closing report.

`docs/videos/` of the engine is not the documentation's. The run leaves
it alone.

## What you have afterwards

- The counts of pages new, regenerated, kept and removed.
- The check's result.
- The ledger remade, so that its Renders table carries the index.
- A report of the run in `reviews/`, filed under the name of a check,
  `YYYY-MM-DD-check-documentation.md`. It holds one finding per matter
  the run could not place:
  - a fact that no file owns
  - a matter on which the map and an owner disagree
  - a claim the map asked for and no input carried
  - every place where a writer wanted a reason and none is recorded

A run that leaves nothing files nothing.

The findings are settled by walkthrough, as a check's are (see [Check
conformance](check-conformance.md)). A mend lands in the file that owns
the matter and never on a page, and the page is then regenerated. How
that is done: [Change a documentation
page](../extend/change-a-documentation-page.md).

## If something goes wrong

- The repository is behind its origin or has diverged: the command
  refuses and offers `/pull`. Run it, then run `/document` again.
- A bare run finds no `projects/forge`: the forge's own project is
  cloned beside the engine only by whoever develops it, so a user runs
  the command with a slug.
- A page fails the check twice: it is deleted and left out, and the run
  says so. It is never mended by hand. Mend the owner of the matter and
  run the command again.
- An input that the map names is missing on disk: the page is
  regenerated, and its writer reports the gap in the run's report.

The three scripts of the run and their options are in
[Scripts](../reference/scripts.md). A term you do not know is in the
[Glossary](../reference/glossary.md).

## A worked example

A closing report of a run for a project with the placeholder slug
`example-project`. The numbers are placeholders.

```
/document example-project

Pages: <n> new, <n> regenerated, <n> kept, <n> removed.
Check: every page passes.
Ledger remade; its Renders table carries docs/README.md.

Filed: reviews/<date>-check-documentation.md, three findings
  1. medium  a fact no file owns: <the fact, as the planner found it>
  2. medium  the map and an owner disagree on <the matter>
  3. low     a writer wanted a reason for <the matter>; none is
             recorded

Next: walk the three findings; a mend lands in the owning file, then
run /document again.
```

## See also

- [The documentation](../about/the-documentation.md): what the
  documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md):
  how a page is changed through its owners.
- [Check conformance](check-conformance.md): how a report's findings
  are settled by walkthrough.
- [Release a version](release-a-version.md): the release that reports
  the documentation's age and offers the run.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  the forge's own project is a repository of its own that whoever
  develops the engine clones beside it.
- [Scripts](../reference/scripts.md): the three documentation scripts
  with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
