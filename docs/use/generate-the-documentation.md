---
generated: 2026-10-09
made: mirrored
inputs-hash: fbe9bd203f09b571
inputs:
  - .claude/skills/document/SKILL.md
  - scripts/docs-state.py
  - scripts/docs-index.py
  - scripts/docs-check.py
---

# Generate the documentation

This page is for a user or an extender who wants to generate the
documentation of the engine or of a project, or to remake it after
something changed. The command is `/document [slug]`. It runs once,
from start to end, and asks nothing.

## Where it reads and where it writes

- Bare, `/document` documents the engine. The pages land in `docs/` at
  the engine root, and the map of the pages, `docs-map.md`, sits beside
  the ledger of `projects/forge`.
- With a slug, `/document <slug>` documents that project. The pages land
  in `projects/<slug>/docs/`, and the map sits beside that project's
  ledger.

The map is never kept in `docs/`.

## What happens

1. **Plan.** A planner agent reads the target on disk and writes the
   map: one entry per page, with the page's inputs. If a map already
   exists, the planner is shown the previous one.
2. **State.** A script computes what each page needs from the content of
   its inputs and of its entry in the map. A page is new, to be
   regenerated (its inputs or entry changed), kept (nothing changed), or
   to be removed (it exists in `docs/` but the map no longer names it).
   Only what changed is remade. The script also writes one task file per
   page to make, in the engine's gitignored `tmp/docs-tasks/`.
3. **Remove.** The pages that lost their entry are deleted, and the run
   says which.
4. **Write.** One writer agent per page is given its task file by path.
   It reads the task first and makes the page from its entry and its
   inputs alone. A mirrored page is made on a faster model, a derived
   page on the session model. Many writers run at once.
5. **Index.** A script derives the index, `docs/README.md`, from the
   map, stamped with the version of the intent.
6. **Check.** A script checks every page: it is present and named by the
   map, every link resolves, there is no long dash, it opens with a
   front-matter, and it carries no instance fact (the values kept in
   the instance's local file, e-mail addresses, paths of a machine). A
   page that fails is regenerated once with the failure named. A page
   that fails twice is left out of the documentation and said aloud.
7. **Record and report.** The ledger's Renders table of the owning
   project gets one row for the index.

## What you get at the end

- The counts: pages new, regenerated, kept and removed.
- The Unowned list: facts a page needs that no file owns. They wait for
  you to give them a home; nothing is invented to fill them.
- What did not fit in the map.
- What the writers left out because their inputs did not support it.
- The result of the check.
- The row for the index in the ledger's Renders table.

## When a page is wrong

Never mend the page by hand. Mend the file that owns the matter, then
run `/document` again: the changed input makes the page stale and only
that page is remade. See
[Change a documentation page](../extend/change-a-documentation-page.md).

## When it runs

Only when you command it. A release never runs it: it reports the age
of the index against the version of the intent and offers this command.

## See also

- [About the documentation](../about/the-documentation.md): what the documentation is, for whom, and why it is generated.
- [Change a documentation page](../extend/change-a-documentation-page.md): how a page is changed through the file that owns its matter.
- [Scripts](../reference/scripts.md): the three documentation scripts with their options.
