---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: de69471c32990efd
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page shows how the command `/document` makes the pages of the documentation and their index, and what you have at the end of a run. It is for the person who runs the command, whether a user of the forge or an extender. The principal (the person whose thinking is forged) gives the command; Claude runs it.

## When to use it

Run it when the documentation should match the target as it stands now: after the engine or a project has changed, or when no documentation exists yet. The run regenerates only the pages whose material changed, so it is cheap to repeat. What the documentation is and why it is generated is on [The documentation](../about/the-documentation.md).

## The command

```
/document
```

Bare, the target is the engine. The pages land in `docs/` at the engine root, and the documentation map (the plan that lists every page and what it is made from) lies beside the ledger of `projects/forge`. The ledger is the file that holds a project's state.

```
/document <slug>
```

With a slug, the target is that project. Its pages land in `projects/<slug>/docs/`, and its documentation map lies beside its own ledger.

The run asks you nothing. Where something is unclear, Claude decides and says so in the report.

## What happens

1. **Plan.** A planner (a subagent: a helper that Claude starts and that sees only its own task) reads the target on disk and writes the documentation map. If a map exists, the planner is given the previous one to compare against.

   You should now see the planner's report: the counts, the list of what is unowned, and what did not fit.

2. **State.** A script computes the state of every page from the content of the page's inputs and of the rule the pages are made by. The state is one of four words:
   - `new`: no page exists yet.
   - `regenerate`: a page exists, but an input or the rule changed.
   - `keep`: a page exists and nothing it is made from changed.
   - `remove`: a page exists that no entry of the map names, or its entry was marked for removal.

   The script also writes one task for every page that is new or to be regenerated. The state is computed, never judged.

   You should now see a summary line with the number of entries, the pages per state and the folder the tasks were written to, followed by the pages to remove and any input that the map names and the disk does not have.

3. **Remove.** The pages that lost their entry are deleted.

   You should now see Claude name each page it deleted.

4. **Write the pages.** One writer (a subagent) makes each page from its task alone. It reads its entry and its inputs from disk and nothing else, and writes the page. Several writers run at once.

   You should now see each page that was new or to be regenerated written, and a short report from each writer of what its inputs did not support.

5. **Index.** A script derives the index, `README.md` in the documentation folder. It lists every page by section with its title and one line, and it needs no model: the same map gives the same index.

   You should now see a line saying the index was written.

6. **Check.** A script checks every page against the map and the rules of a page: the page exists, every link resolves, no long dash stands in the prose, the front-matter is there, and no fact of the instance (a name, an address, a path of a machine) has reached the text. A page that fails is regenerated once with the failure named. A page that fails twice is left out of the documentation: it is deleted and its entry is marked for removal in the map, and Claude says so aloud. It is never mended by hand.

   You should now see a result line saying how many files were checked and that none failed.

7. **Record and report.** The index gets its row in the Renders table of the ledger of the owning project. Then Claude gives you the closing report below.

   You should now see the report.

Two things lie outside the run. The folder `docs/videos/` of the engine is not part of the documentation: the planner never maps it, and the scripts read `docs/` without it. A release never runs `/document`: it reports the age of the index and offers the command.

What is wrong on a page is not mended on the page. It is mended in the file that owns the matter, and the page is regenerated. How that is done is on [Change a documentation page](../extend/change-a-documentation-page.md). The three scripts and their options are on [Scripts](../reference/scripts.md).

## What you have afterwards

- The pages under `docs/`, one topic each, and their index `README.md`.
- The documentation map beside the ledger of the owning project. It is not shown to a reader of the documentation.
- A row for the index in the Renders table of the ledger.
- The closing report:
  - the pages new, regenerated, kept and removed;
  - the Unowned list: facts the planner found that no page owns, each waiting for you to give it a home, since nothing is invented to fill it;
  - what did not fit the outline;
  - what the writers left out because their inputs did not support it;
  - every place where a writer wanted a reason and none is recorded, as one list, so that you can enter the reason where it belongs;
  - the result of the check.

## If something goes wrong

- The state summary lists a missing input: the map names a file or a part of a file that the disk does not have. The page is regenerated and its writer reports the gap.
- The check names a page and a line: that page is regenerated once with the failure named. If it fails again, it is left out and reported.
- A page is wrong in substance: do not edit it. Change the file that owns the matter and run the command again.

## A worked example

A generic closing report of a run on a project with the placeholder slug `my-project`:

```
/document my-project

Pages: <n> new, <n> regenerated, <n> kept, <n> removed.
Removed: docs/about/old-topic.md.

Unowned: <n> facts with no page.
  - <a fact the planner found, with the file it came from>
Did not fit: <n> items.
  - <an item the outline had no section for>

Writers left out:
  - docs/use/some-job.md: <what its inputs did not support>
Reason not recorded:
  - docs/about/some-concept.md: why <a rule> holds

Check: <n> files checked, no failure.
Ledger: the index row of projects/my-project/docs/README.md recorded.
```

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
