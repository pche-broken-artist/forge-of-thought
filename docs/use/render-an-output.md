---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: f21f361007c20755
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
  - projects/forge/10-intent.md#POS.1910
---

# Render an output

This page is for you, the principal (the person whose thinking is forged), when you want to regenerate a render from its recipe with `/render`, and its plain file with it. A render is an audience-specific output made from the documents of a project; a recipe is the versioned file that says how it is made.

## When to use it

- A recipe has changed and its render must follow.
- Claude has reported a render as stale (an input has a new version since the render was made) and you want it regenerated.
- A recipe is new and has no render yet.

A render is regenerated only on this command or by `/release`. Claude never regenerates one on its own judgement: it reports a stale render and offers.

## The command

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/` folder, without the extension. `[slug]` names the project; leave it out when the project is clear from the conversation.

## What happens

1. Claude reads `recipes/<recipe>.md`.
   You should now see the recipe found. If it does not exist, Claude offers to compose it through `/recipe` and stops.

2. Claude reads the inputs the recipe declares, at their current versions, from disk. Where the recipe reads the ledger, Claude makes the ledger first with its script, because a render reads the file on disk.
   You should now see no message, or the ledger made when the recipe needs it.

3. Claude generates the Markdown in isolation. It hands the recipe and its inputs to a subagent (a helper run that sees nothing of your conversation), so the render is derived from the documents and not from what was said about them. The file is written to `renders/<recipe>.md`, or to the recipe's `output:` path where the recipe declares one, and overwrites the earlier one. The render opens with a provenance block in its front-matter (see [Render provenance](../reference/render-provenance.md)).
   You should now see the render file written, opening with its provenance.

4. Where the recipe declares `languages:`, the first language is the primary render. Each further language is translated from it in the same run, scene for scene and line for line, as a file of its own, `renders/<recipe>.<lang>.md`. Nothing is re-cut.
   You should now see one file per language.

5. Back in the session, Claude scans the written file mechanically for facts of the instance (`python scripts/docs-check.py --file <render>`). A hit is said aloud and you judge it. An instance fact is regenerated out, never edited by hand.
   You should now see either no hit or the hit named for your judgement.

6. Claude verifies that the file exists and that its provenance is correct. The ledger's Renders table reads the provenance, so nobody writes a row. Claude remakes the ledger and reports what was rendered from what.
   You should now see a report of the render and its inputs.

7. Where the recipe has a `## Format` section, Claude makes the plain file beside the render. A Word or PowerPoint file is made through pandoc. For a screenplay, the video or the player file is made through `scripts/md2video.py`, beside the render or at the recipe's `output:`. The screenplay's formats are on [Make a teaching video from a recipe](make-a-video-from-a-recipe.md). A recipe without the section ends at the Markdown.
   You should now see the plain file next to the render.

8. Where a published file of the recipe exists, Claude tells you it is now older than its render. It remakes nothing. The designed file is made only by `/publish` (see [Publish a designed file](publish-a-designed-file.md)).
   You should now see the remark that the published file is older.

## What you have afterwards

- The Markdown render, in `renders/` or at the recipe's `output:` path.
- One render per language where the recipe declares languages.
- The plain file, where the recipe has a `## Format` section.
- A ledger that reads the new provenance.

The render and its plain file are never edited by hand. To change them, change the recipe or its inputs and render again, because the Markdown render stays the source of truth for its plain file.

A file you make yourself from them, such as an edited copy or a PDF saved by hand, and keep in `renders/` under a name of its own, is yours. It is kept in git and left alone by the forge ([Renders and recipes](../about/renders-and-recipes.md)).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it through `/recipe` and stops.
- The scan finds an instance fact: Claude says it aloud and you judge it. A public fixed text of the recipe, or a fact of the engine's own history, stands. Anything else is regenerated out.
- A tool of the plain file is missing (pandoc, or Pillow and ffmpeg for a video): the render stands, the plain file is not made, and Claude says so aloud. Install the tool and run the command again.

## A worked example

You have a recipe `summary` in a project `my-project`, with no `languages:` and a `## Format` section naming a Word file.

```
/render summary my-project
```

Claude reads `recipes/summary.md` and its inputs, generates `renders/summary.md` with its provenance, scans it and finds no hit, and remakes the ledger. It then makes `renders/summary.docx` through pandoc. No published file of `summary` exists, so Claude says nothing of one. It reports the render, the plain file and the inputs they came from.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth, and what becomes of the principal's own files beside it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
