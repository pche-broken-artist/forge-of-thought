---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: cd7d32e7ca6ca398
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/agents/docs-planner.md#What you read
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - .claude/skills/release/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

The command `/document` generates the documentation of the engine or of one project: pages of one topic each, and an index. This page is for you if you use the forge or extend it and want the documentation current. What the documentation is and why it is generated is explained in [The documentation](../about/the-documentation.md).

## When to use it

Use it when the documentation is missing or older than the intent. A release reports the index's age against the intent's version and offers this command; see [Release a version](release-a-version.md). Claude never runs it on its own judgement.

## The command

Bare, the command documents the engine:

```
/document
```

With a slug, it documents one project. The slug is a placeholder here:

```
/document my-project
```

The run asks you nothing. It works on `main` only. It refuses a repository that is behind or diverged from its origin and offers `/pull`.

Where the results land:

- Bare: the pages go into `docs/` at the engine root. The documentation map lies beside the ledger of `projects/forge`. The ledger is the state of a project, made from its documents at read time.
- With a slug: the pages go into `projects/<slug>/docs/`. The documentation map lies beside that project's ledger.

The documentation map is the file the pages are made from, with one entry per page. It is never shown to the reader.

For a project, the planner (the agent that writes the map) reads the project's briefs, intent, threads, the layers below the intent, its ledger, the indexes of `sources/` and `research/`, its recipes, and whatever its documents point to on disk. The pages are written in the project's language, as its artefacts are.

`docs/videos/` of the engine is not the documentation's. The run leaves it alone.

## What happens

1. The previous map is taken from git into the engine's working folder `tmp/`. You should now see the path of that copy, or `none` where no map was committed yet.
2. A planner reads the target on disk and writes the documentation map. Its task names the open findings of the last documentation report that concern the map, so that it brings those entries to their owners' wording. You should now see the planner's counts and what did not fit.
3. A script computes the state of every page from the content of its inputs and of the rule the pages are made by. The state is one of four words:
   - `new`: no page exists at the path.
   - `regenerate`: a page exists and an input or the entry changed.
   - `keep`: a page exists and nothing changed.
   - `remove`: no entry names the page any more.

   The script writes one task per page that is new or regenerated. You should now see a summary of the four states.
4. Pages that lost their entry are deleted. You should now see which ones.
5. Claude says how many pages it is about to make and on which models before it launches the writers. A writer is a subagent, an isolated run of Claude that sees nothing of your conversation. There is one writer per page, and each makes its page from its entry and its inputs alone. You should now see every writer report back.
6. A script derives the index `README.md` from the map. You should now see the index in the documentation folder.
7. A script checks every page. A page that fails is regenerated once. A page that fails twice is left out of the documentation, and Claude says so. You should now see the check's result.

## What you have afterwards

- The counts of pages made new, regenerated, kept and removed.
- The check's result.
- The ledger remade, so that its Renders table carries the index.
- A report of the run in `reviews/`, filed under the name of a check, if the run could not place something. It holds one finding per matter:
  - a fact that no file owns;
  - a matter on which the map and an owner disagree;
  - a claim the map asked for and no input carried;
  - every place where a writer wanted a reason and none is recorded.

A run that leaves nothing files nothing.

The report's findings are settled by walkthrough, as a check's are. A walkthrough takes one item per message and closes each with your verdict. How that goes is described in [Check conformance](check-conformance.md). A mend lands in the file that owns the matter and never on a page. How to change a page through its owners is described in [Change a documentation page](../extend/change-a-documentation-page.md).

## If something goes wrong

- The repository is not on `main`: the run stops. Get back to `main` after saving.
- The repository is behind or diverged from its origin: the run refuses and offers `/pull`.
- A page fails the check: it is regenerated once with the failure named. The check verifies that every entry has its page and no page lacks an entry, that every relative link to a page resolves, that no long dash stands in prose, that every page opens with a front-matter, and that no instance fact reached a page (a value of the instance file, an e-mail address, an absolute path of a machine).
- A page fails twice: it is deleted and its entry is marked `remove` in the map by hand, said aloud. It is never mended by hand.
- An input the map names is missing on disk: the page is regenerated and its writer reports the gap in the run's report.

## Inside a release

A release by hand reports the index's age and offers `/document`. Without your word it runs nothing. With `--auto`, the release asks once, before anything runs, whether the documentation runs. The default is yes. On yes the documentation runs as a part of the release, with the models and the number of pages said before the writers are launched.

## A worked example

A generic run of `/document my-project` ends with a report like this. The numbers and the findings are placeholders.

```
Pages: N new, N regenerated, N kept, N removed.
Check: passed.
Ledger: remade; the Renders table carries the index.
Report: reviews/YYYY-MM-DD-check-documentation-HHMM-<hash>.md
  FND.NNNN (medium): a fact the map asked for has no owner.
  FND.NNNN (medium): the map and an owner disagree on a command's options.
  FND.NNNN (low): the reason for a rule is not recorded.
```

You then settle the findings by walkthrough. For each one the mend lands in the file that owns the matter, and the next `/document` regenerates the pages that depend on it.

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Check conformance](check-conformance.md): how a report's findings are settled by walkthrough.
- [Release a version](release-a-version.md): the release that reports the documentation's age and offers the run.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
