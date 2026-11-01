---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: f0e9d81c0218f37c
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
  - projects/forge/10-intent.md#POS.1910
---

# Render an output

This page shows how you regenerate a render, and its plain file, with `/render`. A render is an output made from the documents of a project for one audience, such as a pitch, a summary or a README. It is written for the principal (the person whose thinking is forged) who wants an output made again from its recipe, the file that says how the render is made. Terms are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use it when a recipe has changed, when the documents it reads have changed, or when a render is reported stale and you want it made again. Claude never regenerates a render on its own judgement. A render is regenerated only on this command or by `/release`.

## The command

```
/render <recipe> [slug]
```

The slug names the project. Without it, Claude infers the project from context and asks if it is ambiguous. If the recipe does not exist, Claude offers to compose it with `/recipe` and stops.

## What happens

1. Claude reads the recipe and the inputs it declares, from disk, at their current versions. Where the recipe reads the ledger, Claude makes it first with its script, because the ledger is made at read time. You should now see the recipe's inputs named in Claude's report.
2. Claude generates the Markdown in isolation. A subagent (a helper that sees nothing of the conversation) reads the recipe and its inputs alone and writes the file. You should now see the file written to `renders/<recipe>.md`, or to the recipe's `output:` path where the recipe declares one.
3. The render opens with provenance front-matter, which records the recipe and the inputs it was made from, each with its version. The page [Render provenance](../reference/render-provenance.md) gives the block and the one definition of stale. You should now see that block at the head of the file.
4. Where the recipe declares `languages:`, the subagent writes the primary render first. It then writes one translation per language as a file of its own, `renders/<recipe>.<lang>.md`. A translation follows the primary scene for scene, and nothing is re-cut. You should now see one file per language.
5. Back in the conversation, Claude scans the file mechanically for facts of the instance (the one installation of the forge), with `python scripts/docs-check.py --file <render>`. A hit is said aloud and you judge it. You should now see either no hit or the hit named for your judgement.
6. Claude verifies that the file exists and that its provenance is correct. The ledger's Renders table reads the provenance, and nobody writes a row. You should now see a report of what was rendered from what.
7. Where the recipe has a `## Format` section, Claude makes the plain file beside the render. A `.docx` or `.pptx` is made through pandoc. For a screenplay, `scripts/md2video.py` makes the video or the player file, at the render or at the recipe's `output:`. The page [Make a teaching video from a recipe](make-a-video-from-a-recipe.md) gives the screenplay's formats in full. You should now see the plain file next to the render.
8. Where a published file of the recipe exists, Claude tells you it is now older than its render. It remakes nothing. The designed file is made through a model by a command of its own, described in [Publish a designed file](publish-a-designed-file.md). You should now see that notice.

## What you have afterwards

- The render in Markdown, with its provenance, in `renders/` or at the recipe's `output:` path.
- One translation file per further language, where the recipe declares languages.
- The plain file, where the recipe has a `## Format` section.
- A ledger whose Renders table reads the provenance of the render.

The render and its plain file are never edited by hand. To change them, change the recipe and render again. A file you make yourself from them and keep in `renders/` under a name of its own, such as an edited copy or a PDF saved by hand, is yours. It is kept in git and left alone by the forge. The reasons are in [Renders and recipes](../about/renders-and-recipes.md).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it and stops.
- The scan finds an instance fact in the render: Claude says it aloud and you judge it. A fact that does not belong is regenerated out, never edited by hand. A public fixed text of the recipe, or a fact of the engine's own history, stands.
- A tool is missing (pandoc, or Pillow and ffmpeg for video): Claude says so aloud, the render stands, and the plain file is not made.

## A worked example

You have a project `my-project` with a recipe `recipes/summary.md` that declares one format and no extra languages.

```
/render summary my-project
```

Claude reads the recipe and its inputs, and the subagent writes `renders/summary.md` with its provenance. The scan finds no instance fact. Claude verifies the provenance and remakes the ledger. The recipe has a `## Format` section naming Word, so `renders/summary.docx` appears beside the render. No `published/summary.md` exists, so no notice of an older published file is given. Claude reports that `summary` was rendered from the recipe and its inputs.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth, and what becomes of the principal's own files beside it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
