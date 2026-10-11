---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 9bad241f4be2a2ac
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page is for the person who wants the documentation of the engine or of a project made or brought up to date. `/document` is the command that generates it: pages of one topic each, and their index, in one run that asks nothing. What the documentation is and why it is generated is said on [The documentation](../about/the-documentation.md).

## When to use it

Use it when the documentation does not exist yet, or when the files it is made from have changed and the pages should follow. A run remakes only the pages whose inputs changed, so running it again on an unchanged target changes nothing.

A release never runs it. A release reports how old the index is and offers the command; you decide whether to run it.

## The command

Bare, for the engine:

```
/document
```

With a project slug, for that project:

```
/document <slug>
```

Where the pages land:

- Bare: into `docs/` at the engine root. The documentation map, the list of pages and what each is made from, lies beside the ledger of `projects/forge`. The ledger is the file that holds a project's state ([Glossary](../reference/glossary.md)).
- With a slug: into `projects/<slug>/docs/`. The map lies beside that project's ledger.

The map is never shown to the reader and never lies in `docs/`.

## What happens

1. A planner reads the target on disk and writes the map, one entry per page.

   You should now see the map written beside the ledger, and the planner's counts.

2. A script computes the state of every page from the content of its inputs and of the rule the pages are made by. The state is one of four words:
   - `new`: no page exists at that path.
   - `regenerate`: a page exists, but an input or the rule changed since it was made.
   - `keep`: a page exists and nothing it is made from changed.
   - `remove`: a page lies in `docs/` that no entry names, or its entry was marked for removal.

   The script also writes one task per page to make, into the engine's `tmp/docs-tasks`. A page is remade when an input changed and also when the rule changed, so that no page stays made by an old rule.

   You should now see one summary line with the count of each state and the list of pages to remove.

3. Pages that lost their entry are deleted. Claude says which.

   You should now see the removed pages named, and no page left that the map does not name.

4. One writer per page makes it. A writer is a subagent, a separate Claude run that sees nothing of your conversation. It reads its task, then the inputs of its entry from disk, and writes the page. A mirrored page, one that restates its inputs, is made by a faster model. A derived page, one that puts its inputs together by reasoning, is made by the model of the session. Up to twenty writers run at once.

   You should now see one report per writer, and the pages in `docs/`.

5. A script derives the index `docs/README.md` from the map, with the version of the intent.

   You should now see `docs/README.md` with one line per page, grouped by section.

6. A script checks every page. A page that fails is regenerated once. A page that fails twice is left out of the documentation and said aloud; it is never mended by hand.

   You should now see the check's result: no failure, or each failure with its file and line.

7. Claude records the index's row in the Renders table of the owning project's ledger and gives you the closing report.

   You should now see the report described below.

## What you have afterwards

The pages and the index are in place. The closing report gives:

- The counts of pages new, regenerated, kept and removed.
- The Unowned list: facts a page needs and no file owns. Each waits for the principal, the person whose thinking is forged, to give it a home. Nothing is invented to fill it.
- What did not fit: matter the planner found and could place on no page.
- What the writers left out, because their inputs did not support it.
- Every place where a writer wanted a reason and none is recorded, as one list.
- The check's result.

The index has its row in the Renders table of the ledger.

## If something goes wrong

- The state script prints `missing input` for a file or part of a file that a map entry names and the disk does not have. The page is regenerated and its writer reports the gap. Fix the input or the entry, then run the command again.
- The check names a failure with its file and line. The page is regenerated once with the failure named. If it fails again, the page is deleted, its entry is marked `remove` in the map, and the report says so.
- A check failure for an instance fact (a name, an address or an absolute path of a machine) on a page means the page carried something it must not. The page is regenerated, not edited.
- A page is wrong in content: do not edit the page. Mend the file that owns the matter and run the command again; [Change a documentation page](../extend/change-a-documentation-page.md) shows how.

The check verifies these things, and nothing else:

- every entry of the map has its page, and no page lies in `docs/` that the map does not name;
- every relative link to a `.md` file resolves;
- no long dash in prose;
- every page opens with a front-matter;
- no instance fact on any page.

The three scripts, with their options, are on [Scripts](../reference/scripts.md).

## A worked example

A generic closing report of `/document <slug>`, where each `<n>` is a number:

```
Documentation of <slug>, into projects/<slug>/docs/
Pages: new <n>, regenerated <n>, kept <n>, removed <n>
Unowned: <fact a page needs and no file owns>
Did not fit: <matter placed on no page>
Writers left out: <what the inputs did not support>
Reason wanted, none recorded: <page and place>
Check: <n> files checked, no failure
Ledger: Renders row for docs/README.md added
```

Each Unowned fact and each place of a missing reason waits for the principal to give it a home in the file that owns the matter. After that, run `/document <slug>` again.

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through the file that owns its matter.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
