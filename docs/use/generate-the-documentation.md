---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 3aae9aed805060b1
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page shows how to make the documentation of the engine or of a project with `/document`, and what you get at the end. It is for the user who wants the pages current and for the extender who changes what they are made from.

## When to use it

Use it when the documentation is missing, or when something it is made from has changed and you want the pages to follow. Run it only when you mean to: Claude never runs it on its own judgement. A release does not run it either. A release reports how old the index is and offers the command.

A page is never mended by hand. What is wrong on a page is mended in the file that owns the matter, and the page is regenerated. See [Change a documentation page](../extend/change-a-documentation-page.md). For what the documentation is and why it is generated, see [The documentation](../about/the-documentation.md).

## The command

```
/document
```

Bare, the target is the engine. The pages land in `docs/`, and the documentation map (the file that lists every page with the files it is made from) is kept beside the ledger of `projects/forge`. The ledger is the single file that holds the state of a project.

```
/document <slug>
```

With a slug, the target is that project. The pages land in `projects/<slug>/docs/`, and the map lies beside that project's ledger. The map is never shown to the reader and never lies in `docs/`.

The run asks you nothing. It happens on `main` only, and it refuses a repository that is behind its origin or has diverged from it. When it refuses, it offers `/pull`.

`docs/videos/` of the engine is not part of the documentation. The run leaves it alone.

## What happens

Two kinds of subagent (a helper Claude launches that sees only its own task) and three scripts do the work. A planner decides what pages there are. A writer makes one page each.

1. **The previous map is taken from git.** Claude asks a script for the map as last committed, so that the planner can compare. You should now see a path printed, or the word `none` when the map was never committed.
2. **A planner reads the target and writes the map.** It reads the target on disk and writes the documentation map. You should now see the planner's report: the counts, the Unowned list (facts that no page has a home for) and what did not fit.
3. **A script computes the state of every page.** It does not judge. It compares what each page was made from (its entry, the content of its input files, and the rules the pages are written by) with what the existing page records. The state of each page is one of these:
   - new: there is no page yet.
   - regenerate: the page exists, but an input or the rule changed.
   - keep: the page exists and nothing it is made from changed.
   
   Where an input is only a part of a file, a section or an item, a change elsewhere in that file leaves the page as it is. The script writes one task per page that is new or to be regenerated. You should now see a summary line with the counts, and a note for any input the map names and the disk does not have.
4. **Pages that lost their entry are deleted.** A page that no entry names, or whose entry the planner marked for removal, is removed, and Claude says which. You should now see those pages gone from `docs/`.
5. **One writer makes each page.** Each writer reads its task and its input files from disk and writes its page, and nothing else. Up to twenty writers run at once, and the rest follow as the first ones return. You should now see the new and regenerated pages in place.
6. **A script derives the index.** It writes `README.md` in the documentation folder from the map: the reading paths first, then one line per page, grouped by section. It is deterministic, and it is never edited by hand. You should now see the index listing every page.
7. **A script checks every page.** The check verifies these things:
   - every page the map names exists, and no page lies there that the map does not name;
   - every relative link to a Markdown file resolves;
   - no long dash stands in prose;
   - every page opens with front-matter;
   - no instance fact (a value private to one installation, such as a name or a machine path) and no e-mail address reached a page.

   A page that fails is regenerated once, with the failure named in its task. A page that fails twice is left out of the documentation: it is deleted, its entry is marked for removal in the map, and Claude says so aloud. You should now see the check report "no failure".
8. **The ledger is remade.** The Renders table of the ledger reads the index's front-matter, so nobody writes a row. You should now see the index among the renders of the ledger.

## What you have afterwards

The documentation is in `docs/` (or `projects/<slug>/docs/`) with its index. The closing report gives:

- the pages new, regenerated, kept and removed, as counts;
- the Unowned list: facts that wait for you to give them a home, and nothing is invented to fill it;
- what did not fit, from the planner;
- what the writers left out because their inputs did not support it;
- the places where a reason is wanted and none is recorded, as one list, so that you can decide whether the reason enters the intent;
- the result of the check;
- the ledger, remade.

## If something goes wrong

- **The run refuses to start.** The repository is behind or diverged from its origin, or the branch is not `main`. Switch to `main`, or run `/pull` as it offers, and run `/document` again.
- **The state summary names a missing input.** The map names a file or a part the disk does not have. The page is regenerated and its writer reports the gap. Mend the map's source by running `/document` again after the file is restored, or accept the gap as reported.
- **The check prints failures.** Each failure is printed with its file and line. The page is regenerated once. If it fails again, it is left out and reported. Never mend it by hand: mend the file that owns the matter, then run the command again.

## A worked example

A generic closing report of `/document <slug>` after one input changed:

```
Documentation of <slug>
  pages: <n> new, <n> regenerated, <n> kept, <n> removed
  removed: docs/<section>/<old-page>.md
  Unowned: <fact the planner could not place>
  did not fit: <what the planner could not plan>
  writers left out: <what the inputs did not support>
  reason not recorded: <page>, <place>
  check: <n> files checked, no failure
  ledger: remade, the Renders table carries the index
```

You read the Unowned list and the places where a reason is not recorded first. They are the only items that wait for you.

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
