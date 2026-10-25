---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 48768bbb9f70813f
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
---

# Render an output

This page shows how you regenerate a render, and its plain file, with `/render`. It is for the principal, the person whose thinking is forged, who wants an audience-specific output made again from its recipe.

A render is a Markdown output generated from the documents of a project. A recipe is the versioned file that says how the render is made. The ledger is the file that holds the state of the project, made from the documents whenever it is read. A subagent is a helper that Claude starts for one job and that sees nothing of your conversation.

## When to use it

Use it when a render is stale, or when you have changed its recipe and want to see the result. A render is regenerated only on this command or by `/release`. Claude never regenerates one on its own judgement: it reports a stale render and offers.

## The command

```
/render <recipe> [slug]
```

The recipe is the name of a file in the project's `recipes/` folder. The slug names the project and may be left out when the project is clear from the context. Claude asks when it is not.

## What happens

1. Claude reads `recipes/<recipe>.md`. If the recipe does not exist, Claude offers to compose it with `/recipe` and stops.

   You should now see Claude go on to the inputs, or offer to compose the recipe.

2. Claude reads the inputs the recipe declares, at their current versions, from disk. Where an input is the ledger, Claude makes the ledger first with its script, so that the render reads the file as it stands now.

   You should now see the inputs read, the ledger made first where the recipe reads it.

3. Claude starts a subagent that sees only the recipe and its inputs, never your conversation. A render is derived from the documents, not from what was said about them. The subagent follows the recipe's instructions and template and writes the Markdown file. It does not read the previous render unless the recipe lists it among its inputs.

   You should now see the file at `renders/<recipe>.md`, or at the path the recipe gives under `output:`. The file is overwritten freely, because its history lives in git.

4. Where the recipe declares `languages:`, the subagent writes the primary render first. Then it writes one translation per language, each as a file of its own, `renders/<recipe>.<lang>.md`. A translation follows the primary scene for scene and line for line. Nothing is re-cut.

   You should now see one file per declared language.

5. Every render opens with a provenance block in its front-matter. The block names the project, the recipe and its version, and the inputs with their versions. A translation also names the primary render it was made from. The block is described in [Render provenance](../reference/render-provenance.md), which also gives the one definition of stale.

   You should now see the block at the top of each file.

6. Back in the conversation, Claude scans the written file mechanically for facts of the instance (the values of the local instance file) with `python scripts/docs-check.py --file <render>`. A hit is said aloud and you judge it. A fact of the instance is regenerated out, never edited by hand. A public fixed text of the recipe, or a fact of the engine's own history, stands.

   You should now see either no hit, or each hit said aloud for you to judge.

7. Claude verifies that the file exists and that its provenance is correct. The ledger's Renders table reads the provenance, and nobody writes a row. Claude remakes the ledger and reports what was rendered from what.

   You should now see a report of the render and its inputs.

8. Where the recipe has a `## Format` section, Claude makes the plain file beside the render:
   - a `.docx` or a `.pptx` through pandoc, with the reference document and page size the section names;
   - for a screenplay, the video or the player file through `scripts/md2video.py`, with the format, the pace and the date the section names.

   The plain file lands beside the render, or at the recipe's `output:` path. For a screenplay that path may lie in the engine's `docs/videos/`, where the script renews the player page. The Markdown render always stays in the project's `renders/`. The formats of a screenplay are given in full in [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

   You should now see the plain file next to the render.

9. Where a published file of the recipe exists, Claude tells you that it is now older than its render. It remakes nothing. The designed file is made only by `/publish`, never by `/render`: see [Publish a designed file](publish-a-designed-file.md).

   You should now see the notice that the published file is older than its render.

## What you have afterwards

- The Markdown render, with its provenance, at `renders/<recipe>.md` or at the recipe's `output:` path.
- One translation file per declared language, where the recipe declares languages.
- The plain file, where the recipe has a `## Format` section.
- A remade ledger, whose Renders table reads the new provenance.

The render is never a source of truth and is never edited by hand. What you iterate is the recipe. Why this is so is explained in [Renders and recipes](../about/renders-and-recipes.md).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it with `/recipe` and stops.
- The scan finds an instance fact: Claude says it aloud and you judge it. If it is an instance fact, the render is regenerated, not edited.
- A tool for the plain file is missing (pandoc, or Pillow and ffmpeg for a video): Claude says so aloud. The render stands and the plain file is not made. Install the tool and run the command again.
- A recipe without a `## Format` section ends at the Markdown. This is not a fault.

## A worked example

A project with the placeholder slug `my-project` has a recipe `summary` that declares no languages and has a `## Format` section naming `.docx`. You type:

```
/render summary my-project
```

Claude reads `recipes/summary.md` and its inputs, has the subagent write `renders/summary.md`, scans it for instance facts and finds none, and verifies the provenance. It remakes the ledger and runs pandoc on the render, so that `renders/summary.docx` lands beside it. A published file `published/summary.md` exists, so Claude tells you the published file is now older than its render. You decide whether to run `/publish`.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
