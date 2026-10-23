---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: cfe47fd481e141ce
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page tells you how to make the documentation with `/document`, one command that writes the pages of the engine or of a project and their index. It is for the user who wants the pages brought up to date and for the extender who has changed a source and wants to see its page follow. The principal (whoever's thinking is being forged) runs it; it asks nothing during the run.

## When to use it

- You have changed a file that a page is made from, and you want the page to follow.
- You have changed the rule the pages are made by, and every page made by the old rule must be made again.
- A release has told you that the index is old and offered this command.

A release never runs `/document` itself. It reports how old the index is and offers the command.

## The command

```
/document [slug]
```

Bare, the target is the engine. Its pages land in `docs/`, and the documentation map (the list of every page with what it is made from) lies beside the ledger of `projects/forge`. The ledger is the state report that a script makes from the documents at read time.

With a slug, the target is that project. Its pages land in `projects/<slug>/docs/`, and its documentation map lies beside its own ledger.

```
/document <slug>
```

The run happens on `main` only. It refuses a repository that is behind its origin or has diverged from it, and it offers `/pull`.

`docs/videos/` of the engine is not part of the documentation. The run does not map it, and the scripts read `docs/` without it.

## What happens

1. **The previous map is taken from git.** Claude fetches the documentation map as it was last committed, so that the planner can see what the pages were made from before. You should now see a path to that copy, or `none` where the map was never committed.
2. **A planner writes the documentation map.** A planner (a subagent: an agent that runs on its own and sees nothing of your conversation) reads the target as it is on disk and writes the map. You should now see its counts, the Unowned list (facts no page has a home for) and what did not fit.
3. **A script computes every page's state.** `scripts/docs-state.py` hashes each entry together with the content of every input it names, and with the rule the pages are made by. It compares the result with the hash the existing page carries. You should now see one of four states for each page:
   - `new`: no page exists yet.
   - `regenerate`: a page exists, but an input, the entry or the rule changed.
   - `keep`: a page exists with the same hash, so it is left as it is.
   - `remove`: the page belongs to no entry, or its entry was marked for removal.

   An input is a whole file or a named part of one, and only that part is hashed, so a change elsewhere in the file leaves the page alone. The script writes one task file for each `new` or `regenerate` page. If an input named by the map is missing on disk, the script lists it as a missing input.
4. **Pages that lost their entry are deleted.** Claude removes every page listed as `remove` and says which. You should now see those files gone.
5. **One writer makes each page.** For each task file Claude launches one writer, a subagent that makes the page from its entry and its inputs alone and carries nothing of any other page. Up to twenty run at once, and the rest follow as the first ones return. You should now see every `new` and `regenerate` page written, and each writer's short report.
6. **A script derives the index.** `scripts/docs-index.py` writes `README.md` in the documentation directory from the map: one line per page, grouped by section in the order start, use, about, extend, reference, preceded by the reading paths of the map. The same map always gives the same index. You should now see the line stating how many entries it wrote and where.
7. **A script checks every page.** `scripts/docs-check.py` verifies that:
   - every entry that is not marked `remove` has its page, and no page exists that the map does not name;
   - every relative link to a Markdown file resolves;
   - no page carries a long dash in its prose;
   - every page opens with front-matter;
   - no page carries an instance fact, that is, a value private to this installation, an e-mail address other than a placeholder, or the absolute path of a machine.

   A page that fails is regenerated once with the failure named to its writer. A page that fails twice is deleted and left out of the documentation, and Claude says so aloud. It is never mended by hand. You should now see a line saying how many files were checked and that none failed.
8. **The ledger is remade.** Claude runs `scripts/forge-ledger.py` for the owning project, so that the Renders table of the ledger carries the index. Nobody writes that row by hand.

## What you have afterwards

- The pages under `docs/` (or `projects/<slug>/docs/`) and their index, `README.md`.
- The documentation map beside the ledger of the owning project.
- A closing report with:
  - the pages new, regenerated, kept and removed, as counts;
  - the Unowned list, each fact waiting for you to give it a home, and what did not fit;
  - what the writers left out because the inputs did not support it;
  - one list of the places where a writer wanted a reason and none is recorded;
  - the check's result.

Nothing is invented to fill the Unowned list. A reason that is not recorded enters the intent in a round of its own, when you want one.

## If something goes wrong

- **The repository is behind or diverged from its origin.** The run stops and offers `/pull`. Pull, then run `/document` again.
- **You are not on `main`.** The run does not go ahead on another branch.
- **An input is reported as missing.** The page is regenerated anyway, and its writer reports the gap. Fix the map's entry or restore the file through the owner of the matter.
- **A page fails the check.** It is regenerated once. If it fails again it is deleted and named in the report.
- **A page is wrong.** Do not edit it. Mend the file that owns the matter, then run `/document` again. How a change reaches a page is described in [Change a documentation page](../extend/change-a-documentation-page.md).

## A worked example

A run on a project, shown as the closing report might read. The numbers are placeholders.

```
/document example-project

Pages: new N1, regenerated N2, kept N3, removed N4.
Removed: docs/about/old-topic.md
Unowned: <a fact no page has a home for>
Did not fit: <a matter the outline has no section for>
Writers left out: <what the inputs did not support>
Reason not recorded: docs/about/some-topic.md, <the place that wanted a reason>
Check: N files checked, no failure.
Ledger remade; its Renders table carries the index.
```

## See also

- [The documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through its owners.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
