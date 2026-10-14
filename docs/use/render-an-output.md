---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 3bda1237102ab0fc
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
---

# Render an output

This page shows how you regenerate a render, and the plain file beside it, with `/render`. A render is an audience-specific output (a pitch, a summary, a README) that Claude generates from a recipe and never edits by hand. The page is for anyone who owns a project and wants its output made again.

The principal is whoever's thinking is being forged. A ledger is the project's single record of state. A subagent is a helper that Claude starts to do one job in isolation, without seeing the conversation.

## When to use it

- You changed a recipe, or an input of a recipe, and you want the output made again.
- Claude told you a render is stale and offered to regenerate it.

A render is regenerated only on this command or by `/release`. Claude never regenerates one on its own judgement: it reports a stale render and offers.

## The command

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/` directory, without the extension. `[slug]` names the project; leave it out where the project is clear from context.

## What happens

1. Claude reads `recipes/<recipe>.md`.
   If the recipe does not exist, Claude offers to compose it with `/recipe` and stops.
   You should now see either the next step starting or the offer to compose the recipe.

2. Claude reads the inputs the recipe declares, at their current versions, from disk.
   You should now see no output yet: this step only reads.

3. A subagent generates the Markdown.
   It works from the recipe and its inputs alone, never from your conversation, so the render is derived from the documents and not from what was said about them.
   It writes to `renders/<recipe>.md`, or to the recipe's `output:` path where the recipe names one.
   The file opens with provenance front-matter, which lists the recipe and the inputs with their versions (the block is described in [Render provenance](../reference/render-provenance.md)).
   An existing file is overwritten; its history lives in git.
   You should now see the render file at its path, opening with front-matter.

4. Where the recipe declares `languages:`, the subagent writes the primary render first.
   It then writes one translation per language, each as a file of its own, `renders/<recipe>.<lang>.md`.
   A translation follows the primary scene for scene; nothing is re-cut.
   You should now see one file per language.

5. Back in the conversation, Claude scans each written file mechanically for facts of the instance (names, addresses, paths of a machine) with this command:
   ```
   python scripts/docs-check.py --file <render>
   ```
   The scan reads the values in `CLAUDE.local.md` and the patterns of an absolute path on a machine.
   You should now see `1 file checked, no failure`.

6. Claude verifies that the file exists and that its provenance is correct.
   It then writes or updates the render's row in the ledger's Renders table, one row per file, a translation citing its primary render.
   You should now see a report of what was rendered from what.

7. Where the recipe has a `## Format` section, Claude makes the plain file.
   For a Word or PowerPoint format it runs `python scripts/md2docx.py` or `python scripts/md2pptx.py` through pandoc, and the `.docx` or `.pptx` lands beside the render.
   For a screenplay, whose format is a video or a player page, it runs `python scripts/md2video.py` on each language's render, and the file lands beside the render or at the recipe's `output:`.
   Both ways are described in [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).
   A recipe without a `## Format` section ends at the Markdown.
   You should now see the plain file beside the render, or at the recipe's `output:` path.

8. Where the ledger's Published table has a row for this recipe, Claude sets it to `stale` and says so.
   The published file is now older than its render, and Claude remakes nothing.
   A screenplay has no published file, so this step does not apply to it.
   You should now see the row marked `stale`.

## What you have afterwards

- The Markdown render at `renders/<recipe>.md`, or at the recipe's `output:` path, or one file per language.
- A row in the ledger's Renders table for every file written.
- Where the recipe has a `## Format` section, the plain file beside the render.
- Where a published file of the recipe existed, its row marked `stale`.

The designed file, made through a model, is not made here. It is made by [Publish a designed file](publish-a-designed-file.md).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it and stops.
- The scan finds an instance fact: Claude says so aloud, with the line, and you judge it. An instance fact is regenerated out, never edited by hand. A public text fixed by the recipe, or a fact of the engine's own history, stands.
- A scan failure reads `1 file checked, N failures` and lists each file with its line.
- A tool for the plain file is missing (pandoc, or Pillow and ffmpeg for a video): the render stands, the plain file is not made, and Claude says so aloud. Install the tool and run `/render` again.

## A worked example

A project has a recipe `recipes/summary.md` that declares no languages and has a `## Format` section naming Word.

```
/render summary my-project
```

Claude reads the recipe and its inputs, and a subagent writes `renders/summary.md`. The scan prints `1 file checked, no failure`. Claude adds a row for `renders/summary.md` to the Renders table. It then runs pandoc, and `renders/summary.docx` appears beside the render. A row for `summary` in the Published table, if there is one, is set to `stale`, and Claude reports what was rendered from what.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
