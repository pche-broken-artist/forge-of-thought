---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 418aeb18aae512a0
inputs:
  - .claude/skills/document/SKILL.md
  - .claude/agents/docs-planner.md#What you read
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - .claude/skills/release/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
  - projects/forge/10-intent.md#REJ.0500
---

# Generate the documentation

`/document` is the command that makes the documentation of the engine or of a project: one page per topic and an index, in one run that asks you nothing. This page is for the user who wants to run it and for the extender who wants to know what it did. It says what you type, what happens in what order and what you have at the end. What the documentation is and why it is generated is on [The documentation](../about/the-documentation.md).

The words used here: the principal is the person whose thinking is forged and who gives the command. The ledger is the file of a project that holds its state, made at read time by a script. A subagent is a Claude run that sees nothing of your conversation and reads its inputs from disk. The documentation map is the plan of the pages, one entry for each, never shown to the reader.

## When to use it

- The documentation does not exist yet.
- The sources of the pages (the intent, the definitions, the templates, the scripts) have changed and the pages are stale.
- A release has reported that the index is older than the intent and offered the run.

## The command

```
/document [slug]
```

Bare, the target is the engine. With a slug, the target is that project. Which one a run makes:

- Bare: the pages land in `docs/` of the engine. The map lies beside the ledger of `projects/forge`.
- With a slug: the pages land in `projects/<slug>/docs/`. The map lies beside the project's ledger.

For a project, the planner (the subagent that writes the map) reads these and nothing else:

- its briefs
- its intent
- its threads
- the layers below the intent
- its ledger
- the indexes of `sources/` and `research/`
- its recipes
- whatever its documents point to on disk

A project sets nothing for itself about what is documented beyond that. The pages are written in the project's language, as its artefacts are.

The command runs on `main` only. It refuses a repository that is behind or diverged from its origin and offers `/pull`.

`docs/videos/` of the engine is not the documentation's. The run leaves it alone.

## What happens

1. The previous map is taken from git into `tmp/`, the engine's working folder. You should now see the path of the copy printed, or `none` where there is no earlier map.
2. The planner reads the target on disk and writes the map. Its task names the open findings of the last documentation report that concern the map, so that it brings those entries to their owners' wording. You should now see the map written beside the ledger, with the planner's counts and the list of what it could not place.
3. A script computes the state of every page from the content of its inputs and of the rule the pages are made by. A page is `new`, to be `regenerate`d, to be `keep`t or to be `remove`d. The script writes one task for every page that is new or to be regenerated. You should now see a summary of the four counts. A change elsewhere in a file leaves a page as it is when the page uses only a part of it.
4. Pages that lost their entry are deleted. You should now see their names listed.
5. Claude says how many pages it is about to make and on which models, and then launches the writers. You should now see that statement before any writer starts.
6. One writer per page makes it from its entry and its inputs alone. You should now see the pages appear in the documentation directory.
7. A script derives the index (`README.md` of the documentation) from the map. Nobody edits it by hand.
8. A script checks every page:
   - every page the map names exists, and no other page lies in the directory
   - every relative link to a Markdown file resolves
   - no long dash in the prose
   - every page opens with its front-matter
   - no instance fact (a value of the instance file, an e-mail address, an absolute path of a machine) is on a page

   A page that fails is regenerated once with the failure named. A page that fails twice is left out of the documentation, deleted and reported, and never mended by hand. You should now see the check's result.
9. The ledger is remade, so that its Renders table carries the index. Then Claude files what the run could not place as a report of the run. You should now see the closing report.

## What you have afterwards

- The pages and the index in the documentation directory.
- The counts of pages new, regenerated, kept and removed.
- The check's result.
- The ledger, remade.
- A report of the run in `reviews/`, filed under the name of a check, when the run could not place something. A run that leaves nothing files nothing.

The report has one finding for each matter:

- a fact that no file owns
- a matter on which the map and an owner disagree
- a claim the map asked for and no input carried
- every place where a writer wanted a reason and none is recorded

The findings are settled by walkthrough, one item per message, as the findings of a check are. See [Check conformance](check-conformance.md). A mend lands in the file that owns the matter, never on a page, and the page is regenerated afterwards. See [Change a documentation page](../extend/change-a-documentation-page.md).

## Where a release comes in

A release never runs the documentation on its own judgement. A release by hand reports the age of the index against the version of the intent and offers the command, and runs it on your word. A release with `--auto` asks once before anything runs, whether the documentation runs, and the default is yes. See [Release a version](release-a-version.md).

## If something goes wrong

- The repository is not on `main`: the command stops. Switch to `main` and run it again.
- The repository is behind or diverged from its origin: the command refuses and offers `/pull`.
- A page fails the check twice: it is left out, deleted, and said aloud. Mend the matter in the file that owns it and run the command again.
- An input that an entry names is missing on disk: the page is regenerated and its writer reports the gap in the closing report.

The three scripts and their options are on [Scripts](../reference/scripts.md). Unknown terms are in the [Glossary](../reference/glossary.md).

## A worked example

A run for a project with the placeholder slug `acme-pilot` ends with a report like this, filed as `projects/acme-pilot/reviews/YYYY-MM-DD-check-documentation-HHMM-<hash>.md`. The shape of a finding is the shape of any check's report.

```
Pages: new 3, regenerated 2, kept 11, removed 1.
Check: passed.

Findings
1. medium - no file owns the delivery date the intent's
   summary refers to; it waits for the principal to give it a home.
2. medium - the map says the page "Roles" explains who approves,
   and the intent names the approver differently; the owner's
   wording was taken.
3. low - the page "Hand-over" wanted the reason for the order of
   the steps; the reason is not recorded.
```

You settle the three by walkthrough. Each mend goes into the intent, never into a page, and the next run regenerates the page that used it.

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Check conformance](check-conformance.md): how a report's findings are settled by walkthrough.
- [Release a version](release-a-version.md): the release that reports the documentation's age and offers the run.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
