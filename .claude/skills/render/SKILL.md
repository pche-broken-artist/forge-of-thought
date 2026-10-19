---
description: Regenerate a render from its recipe in recipes/
argument-hint: "<recipe> [project-slug]"
disable-model-invocation: true
---

Role: renderer (what a render and a recipe are: CLAUDE.md, Document
chain, Renders). A render is regenerated only here, on the principal's
explicit command, or by `/release` (POS.0810); Claude never regenerates
on its own judgement — it reports a stale render and offers. Iterating the recipe is working conversation like any
other; generating the render is mechanical.

1. Infer the current project from context ($1, or ask if ambiguous) and
   read `recipes/$0.md`. If it does not exist, offer to compose it
   through `/recipe` (a genre where one fits, else bare from
   `templates/recipe.md`) and stop.
2. Read the recipe's declared inputs at their current versions.
   Where the inputs name `ledger.md`, make it first, `python
   scripts/forge-ledger.py <slug>`: the ledger is made at read time
   (CLAUDE.md, Ledger) and a render reads the file on disk.
   Every input, CLAUDE.md included, is read from disk in the run:
   the copy of CLAUDE.md a subagent carries in its context is the
   session's and may be older than the file (POS.0950).
3. Generate in isolation: spawn one subagent (Agent tool, type
   `general-purpose`, session model — never a model override) whose
   prompt names the project, the recipe path, the output path and the
   render date, and instructs it to read the recipe and its declared
   inputs, follow the Instructions and Template exactly, and write the
   file — nothing else. The prompt carries the front-matter block of
   step 5 verbatim, so the subagent never derives the provenance shape
   from a previous render. The subagent sees only the recipe and its
   inputs, never this conversation: a render is derived from the
   artefacts, not from what was said about them. Its prompt says, in
   the words of the docs contract, that whatever its context carries
   about the people who run this forge, their company, hosts,
   addresses or preferences is not material and must not reach the
   render (POS.0950). It must not read the
   previous render unless the recipe declares it among its inputs
   (the release-notes genre does, for the released sections), and
   must not touch the ledger. Prose is hard-wrapped as CLAUDE.md,
   Document kinds, says for every document. Where the recipe
   declares `languages:`, the subagent writes the primary render
   first and then each translation as a file of its own, scene for
   scene and line for line, its provenance naming the primary
   render it was made from; nothing is re-cut.
   Content only, always Markdown: the render carries no instructions
   for a conversion — the recipe's `## Format` section is never
   copied into it.
4. The subagent writes to `renders/$0.md`, or, where the recipe
   declares languages, to `renders/$0.<lang>.md` per language, or
   to the recipe's `output:` path if it declares one (e.g. the
   repository README). An `output:` path may lie outside the
   project, in the engine's `docs/videos/` (POS.1540): that is the
   place of the format file of step 7 only, and the Markdown render
   always stays in the project's `renders/`. Overwrite freely;
   history lives in git.
5. The render opens with YAML front-matter provenance, written by the
   subagent:
   ```yaml
   ---
   project: <slug>
   render: <recipe>
   generated: YYYY-MM-DD
   recipe: recipes/<recipe>.md v<version>
   inputs:
     - <path> v<version>
   ---
   ```
   A render in one of several languages adds `language: <lang>`,
   and a translation `translated_from: renders/<recipe>.<primary>.md`.
   Inputs without a version of their own (e.g. CLAUDE.md) are cited by
   path alone. A render is **stale** when any version cited in this
   front-matter differs from the current version of that file, or a
   cited file no longer exists. This is the one definition; `/forge`
   and `/check` cite it (POS.1070).
6. Back in the session: scan the written file mechanically for the
   instance's facts, `python scripts/docs-check.py --file <render>`;
   a hit is said aloud and the principal judges it: an instance fact
   is regenerated out, never edited by hand; a public fixed text of
   the recipe (POS.0990) or a fact of the engine's own history stands
   (POS.0950). Verify the file exists and its provenance is
   correct — the provenance is the row the ledger's Renders table
   reads, a translation citing the primary render; nobody writes a
   row — remake the ledger, `python scripts/forge-ledger.py <slug>`,
   and report what was rendered from what.
7. The plain file (CLAUDE.md, Document chain, Renders). Where the recipe
   carries a `## Format` section, run the script of its format —
   `python scripts/md2docx.py` or `python scripts/md2pptx.py` — on the
   render with `--engine pandoc` and the reference document and page size
   the section names; the file lands beside the render. Where the
   format is `video` or `html-player`, run `python
   scripts/md2video.py` on each language's render with the format,
   the pace and the date the section names, the file beside the
   render or at the recipe's `output:` (`docs/videos/`, where the
   script renews the player page). Where pandoc, or Pillow and
   ffmpeg, is missing, the render stands, the plain file is not
   made, and that is said aloud. A recipe without the section ends
   at the Markdown. The designed file is `/publish`'s, never made
   here; a screenplay has none, and step 8 does not apply to it.
8. Where `published/<recipe>.md` exists, say that the published file
   is now older than its render: the ledger computes its state
   `stale` from the dates (SOL.0680), nobody sets it. Remake nothing.
