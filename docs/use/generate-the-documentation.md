---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 67a37de284f3c4e7
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page shows how to make the documentation of the engine or of a project with `/document`, and what you have at the end of the run. It is for you as the principal (the person whose thinking is forged) and for anyone who extends the forge. What the documentation is and why it is generated is on [The documentation](../about/the-documentation.md).

## When to use it

Use it when the documentation is missing, or when something it is made from has changed: a document of the chain, a rule, a script. The run regenerates only the pages that changed, so it is cheap to repeat. A page that is wrong is not mended by hand. The matter is mended in the file that owns it, and the page is regenerated (see [Change a documentation page](../extend/change-a-documentation-page.md)).

## The command

```
/document [slug]
```

- Bare, the target is the engine. The pages land in `docs/` at the engine root. The documentation map (the list of pages and everything each is made from) lies beside the ledger of `projects/forge`.
- With a slug, the target is that project. The pages land in `projects/<slug>/docs/`.

The run asks you nothing. It runs on `main` only. It refuses a repository that is behind its origin or has diverged from it, and offers `/pull`. The folder `docs/videos/` of the engine is not the documentation's and is left alone.

## What happens

1. The previous map is taken from git into the engine's working folder `tmp/`. You should now see a path printed, or `none` when there is no previous map.
2. A planner (an isolated subagent) reads the target on disk and writes the map. You should now see its counts, its Unowned list (facts that no page has a home for) and what did not fit.
3. A script computes the state of every page from the content of its inputs and of the rule the pages are made by. Each page is `new`, `regenerate`, `keep` or `remove`. It writes one task per page that is new or to regenerate. You should now see a summary of the four states.
4. Pages that lost their entry in the map are deleted. You should now see which pages were removed.
5. Claude says how many pages it is about to make and on which models, before it launches the writers. You should now see that statement, with the count and the models.
6. One writer per page makes it from its entry and its inputs alone. You should now see the writers return, each with a report of what its inputs did not support.
7. A script derives the index `README.md` of the documentation from the map. You should now see the index written in the docs folder.
8. A script checks every page. A page that fails is regenerated once, with the failure named. A page that fails twice is left out of the documentation, its entry marked `remove` in the map, and this is said aloud. You should now see the check pass, or the pages left out named.
9. The ledger of the owning project is remade, so that its Renders table carries the index. You should now see the report.

## What you have afterwards

The report names:

- the pages new, regenerated, kept and removed
- the Unowned list and what did not fit, from the planner
- what the writers left out
- the places where a reason was wanted and none is recorded, as one list
- the result of the check

Every fact in Unowned waits for you to give it a home. Nothing is invented to fill it. A reason that is not recorded enters the intent in a round of its own.

A release never runs `/document`. It reports the age of the index and offers the command.

## If something goes wrong

- The repository is not on `main`: the run refuses. Switch to `main` and run it again.
- The repository is behind or has diverged from its origin: the run refuses and offers `/pull`.
- A page fails the check twice: it is left out and said aloud. Mend the file that owns the matter, then run `/document` again. The page is never edited by hand.
- A script cannot find an input the map names: the page is regenerated and its writer reports the gap.

The three scripts and their options are on [Scripts](../reference/scripts.md). Terms of the forge are in the [Glossary](../reference/glossary.md).

## A worked example

A closing report of a run on a project with the placeholder slug `my-project`:

```
/document my-project

Pages: <n> new, <n> regenerated, <n> kept, <n> removed.
Unowned: <n> facts, each waiting for a home.
Did not fit: <n> items, named.
Writers left out: <n> items, named.
Reasons not recorded: <n> places, listed.
Check: passed.
Ledger remade; its Renders table carries the index.
```

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
