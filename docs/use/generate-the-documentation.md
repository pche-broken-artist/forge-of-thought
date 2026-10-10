---
generated: 2026-10-10
made: mirrored
inputs-hash: fb3963d2fec37c39
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page is for the person who wants the documentation of the engine
or of a project made or brought up to date, and for the one who
extends the forge and wants to know what the command does. One
command makes it, in one run that asks nothing.

## Run it

- `/document` bare generates the engine's documentation into `docs/`
  at the engine root. The map it is made from, `docs-map.md`, lies
  beside the ledger of `projects/forge`, never in `docs/`.
- `/document <slug>` generates that project's documentation into
  `projects/<slug>/docs/`. Its map lies beside that project's ledger.

Nothing is composed by hand: the run regenerates only the pages whose
inputs changed.

## What happens

1. **Plan.** A planner agent reads the target on disk and writes the
   map. If a map already exists, a copy of it is kept for the planner
   to compare against.
2. **State.** A script computes the state of every page from the
   content of its inputs: `new` (no page yet), `regenerate` (the page
   exists but an input or the entry changed), `keep` (nothing changed)
   or `remove` (a page that no entry names any more). The state is
   computed, never judged, so only what changed is remade. The script
   writes one task file for every page to make. An input the map names
   and the disk does not have is reported, and the page is
   regenerated.
3. **Remove.** The pages that lost their entry are deleted, and the
   run says which.
4. **Write.** One writer agent per page is handed its task file by
   path. It reads the file first and makes the page from its entry and
   its inputs alone. A mirrored page, which restates its inputs, is
   made on a faster model; a derived page, which puts several files
   together, is made on the session model. Many writers run at once.
5. **Index.** A script derives the index `docs/README.md` from the
   map. The index names the version of the owning project's intent,
   which for the engine is its version. The same map always gives the
   same index.
6. **Check.** A script checks every page:
   - the page is present and named by the map, and no page lies in
     `docs/` that the map does not name;
   - every relative link to a Markdown file resolves;
   - no long dash;
   - the page opens with a front-matter;
   - no instance fact: no value of the instance's private settings, no
     e-mail address but a placeholder, no absolute path of a machine.

   A page that fails is regenerated once with the failure named in its
   task. A page that fails twice is left out of the documentation and
   said aloud, never mended by hand.
7. **Record and report.** The index gets a row in the Renders table of
   the owning project's ledger.

## What you get at the end

- The counts of pages new, regenerated, kept and removed.
- The Unowned list: facts a page needs and no file owns. Each waits
  for you to give it a home; nothing is invented to fill it.
- What did not fit the outline.
- What the writers left out because their inputs did not support it.
- The check's result.

## When a page is wrong

Never edit the page. Mend the file that owns the matter, then run
`/document` again: the page's inputs changed, so it is regenerated.
[Change a documentation page](../extend/change-a-documentation-page.md)
says how.

## Releases

A release never runs the command. It reports the index's age against
the intent's version and offers `/document`.

## See also

- [About the documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through the file that owns its matter.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
