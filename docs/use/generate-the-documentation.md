---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 3eda1ce05a066f00
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page shows how the command `/document` makes the pages of the documentation and their index, and what report you get at the end. It is for the principal (the person whose thinking is forged) and for anyone who extends the forge.

## When to use it

Use it when the documentation is missing or out of date: a file that a page is made from has changed, or the rules the pages are made by have changed. The command regenerates only what changed. A release never runs it on its own: it reports how old the index is and offers the command.

## The command

```
/document [slug]
```

- Bare, the target is the engine. The pages land in `docs/`, and the documentation map lies beside the ledger of `projects/forge`. The ledger is the file that holds the state of a project, made when it is read.
- With a slug, the target is that project. The pages land in `projects/<slug>/docs/`, and the documentation map lies beside that project's ledger.

The documentation map is the list of pages with everything each page is made from. It is never shown to the reader and never lies in `docs/`.

The run asks you nothing. It runs on `main` only. It refuses a repository that is behind its origin or has diverged from it, and offers `/pull` instead.

## What happens

1. The previous documentation map is taken from git into the engine's working folder `tmp/`.
   You should now see the path of that copy, or the word `none` when there is no earlier map.
2. A planner reads the target on disk and writes the documentation map. The planner is an isolated subagent: it sees nothing of your conversation with Claude.
   You should now see the planner's counts, its list of Unowned facts and what did not fit.
3. A script computes the state of every page from the content of its inputs and of the rule the pages are made by, and writes one task per page. The state is one of four words:
   - `new`: no page exists at the path.
   - `regenerate`: the page exists, but an input, the entry or the rule changed.
   - `keep`: the page exists and nothing it is made from changed.
   - `remove`: the page has lost its entry in the map.

   The state is computed, never judged.
   You should now see a summary of these states.
4. Pages that lost their entry are deleted.
   You should now see which pages were removed.
5. Claude says how many pages it is about to make and on which models, then launches the writers. There is one writer per page, and each makes its page from its entry and its inputs alone. Several run at once; the rest start as the first ones finish.
   You should now see the writers return their reports.
6. A script derives the index, `README.md` in the documentation folder, from the documentation map. No model is involved.
   You should now see the index written.
7. A script checks every page. It verifies these things:
   - Every entry of the map has its page, and no page lies there that the map does not name.
   - Every relative link to a Markdown file resolves.
   - No long dash stands in the prose.
   - Every page opens with front-matter.
   - No instance fact appears, such as a value from the private instance file, an e-mail address or an absolute path of a machine.

   A page that fails is regenerated once, with the failure named in its task. A page that fails twice is left out of the documentation: it is deleted, its entry is marked `remove` in the map by hand, and Claude says so aloud. A failing page is never mended by hand.
   You should now see the check's result.
8. The ledger of the owning project is remade, so that its Renders table carries the index.
   You should now see Claude's closing report.

`docs/videos/` of the engine is not the documentation's. The planner never maps it, and the scripts read `docs/` without it.

## What you have afterwards

- The pages of the documentation, each made from its entry and its inputs.
- The index, derived from the documentation map.
- The documentation map, beside the owning project's ledger.
- The ledger, remade.

The closing report gives:

- the counts of pages new, regenerated, kept and removed;
- the Unowned list: facts the planner found that no owner holds, each waiting for you to give it a home (nothing is invented to fill it);
- what did not fit;
- what the writers left out because their inputs did not support it;
- every place where a writer wanted a reason and none is recorded, as one list (where you want such a reason, it enters the intent in its own round);
- the check's result.

## If something goes wrong

- The repository is behind or has diverged: the run is refused and `/pull` is offered. Pull, then run the command again.
- A page fails the check: it is regenerated once. If it fails again it is left out and reported.
- An input that the map names is missing on disk: the script reports it, the page is regenerated, and its writer reports the gap.
- A page is wrong in content: do not edit the page. Mend the file that owns the matter, then run the command again. See [Change a documentation page](../extend/change-a-documentation-page.md).

## A worked example

A run with the slug `my-project`, given as a generic shape, with counts as placeholders:

```
/document my-project

Pages: N new, N regenerated, N kept, N removed.
Unowned: <the facts no owner holds, one per line, or none>
Did not fit: <what the planner could not place, or none>
Left out by the writers: <what the inputs did not support, or none>
Reason not recorded: <one line per place, or none>
Check: all pages pass.
Ledger remade; its Renders table carries the index.
```

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
