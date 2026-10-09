---
description: Generate the documentation of the engine or of a project into docs/ - pages of one topic each and their index, from a map
argument-hint: "[project-slug]"
disable-model-invocation: true
---

Role: the documentation command (what the documentation is and for
whom: POS.1450 of the forge intent; how it is built: SOL.0460 of the
forge solution design). Two agents and three scripts, one run, no
question asked: the planner writes the map, the scripts compute what
is stale, the writers make those pages, the scripts derive the index
and check the pages. Nothing here is composed by hand; what is wrong
on a page is mended in the file that owns the matter, and the page is
regenerated.

Target and places. Bare, the target is the engine: its root is the
engine root, the owning project is `projects/forge`, the pages land in
`docs/` at the engine root. With a slug, the target is that project:
its root and the owning project are `projects/<slug>`, the pages land
in `projects/<slug>/docs/`. The map is `docs-map.md` beside the
owning project's ledger, never in `docs/`. The date is today's.

1. **Plan.** Launch the agent `docs-planner` (Agent tool, type
   `docs-planner`, session model, never a model override). The task
   names the target's root, the owning project, the path of the map
   to write, the date, and the previous map where one exists: copy
   the current map to the engine's `tmp/docs-map.previous.md` first
   and name that copy; without one say `none`. The planner reads the
   target on disk and writes the map. Its report gives the counts,
   the Unowned list and what did not fit: keep them for step 7.
2. **State.** Run `python scripts/docs-state.py <map> <docs-dir>
   --tasks tmp/docs-tasks` (the engine's gitignored `tmp/`): what it
   computes and writes is its header's. Read its summary; the state
   is the script's, never a judgement.
3. **Remove.** Delete the pages listed as `remove`. Say which.
4. **Write the pages.** For every task file launch one agent
   `docs-writer` (Agent tool, type `docs-writer`) whose prompt names
   the task file by path and nothing else; the writer reads it from
   disk first, as its definition says, so that the session carries no
   page's material: a mirrored page (`made:
   mirrored` in its entry) with the model override `sonnet`, a
   derived page without an override, on the session model (POS.0930).
   Up to twenty run at once; launch the rest as the first return.
   Every writer reads its inputs from disk and writes its page with
   the `inputs-hash` its task gives it. Collect the reports: what the
   inputs did not support goes to step 7.
5. **Index.** Run `python scripts/docs-index.py <map> <docs-dir>`;
   what it derives is its header's.
6. **Check.** Run `python scripts/docs-check.py <map> <docs-dir>`;
   what it verifies is its header's. A page that fails is regenerated
   once with the failure named in its task; a page that fails twice
   is reported and left out of the documentation (deleted, its entry
   marked `remove` in the map by hand, said aloud), never mended by
   hand.
7. **Record and report.** The ledger's Renders table of the owning
   project gets the index's row (its shape: `templates/ledger.md`,
   Renders). Report:
   pages new, regenerated, kept and removed; the Unowned list and what
   did not fit, from the planner; what the writers left out; the
   check's result. Every fact in Unowned waits for the principal to
   give it a home; nothing is invented to fill it.

What a run never does: read the renders or the README as owners;
touch a page by hand; run on Claude's own judgement (the command is
guarded, POS.1090). What a release does with the documentation is
the release's (`.claude/skills/release/SKILL.md`).

Harness note. Claude Code loads an agent's definition once per
session: a change to `docs-planner.md` or `docs-writer.md` reaches the
agents only in a new session. Within the session that changed one,
pass the changed rule in the task and say so in the report.
