---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 0d68526fa6849fb6
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
  - projects/forge/10-intent.md#POS.1910
---

# Render an output

`/render` regenerates a render, an audience-specific Markdown output, from its recipe, and makes the plain file beside it where the recipe names a format. This page is for you as the principal, the person whose thinking is being forged, when a render is out of date or has never been made.

## When to use it

Use it when a render has to be made or made again: the recipe changed, an input of the render changed, or the render does not exist yet. A render is regenerated only on this command or by `/release`. Claude never regenerates on its own judgement: it tells you that a render is stale and offers.

The recipe must exist in the project's `recipes/` folder. Where it does not, Claude offers to compose it and stops.

## The command

```
/render <recipe> [slug]
```

The recipe is the name of a file in `recipes/`, without the extension. The slug names the project; where the context makes it clear, you leave it out. For example:

```
/render pitch my-project
```

## What happens

1. Claude reads the recipe and every input it declares, at their current versions, from disk. Where the recipe reads the ledger (the file that is the single source of truth for state, made from the documents when it is read), Claude makes it first with its script.

   You should now see Claude naming the recipe and its inputs.

2. Claude hands the generation to a subagent, a helper run that sees none of your conversation. It sees only the recipe and its inputs, so the render comes from the documents and from nothing that was said about them.

   You should now see the render written to `renders/<recipe>.md`, or to the path the recipe gives in its `output:` field.

3. The render opens with provenance front-matter, which says what it was made from and at which versions. The block is described in [Render provenance](../reference/render-provenance.md).

   You should now see the front-matter at the top of the file.

4. Where the recipe declares `languages:`, the first language is the primary and the render of it is written first. Each other language is then a translation, a file of its own, `renders/<recipe>.<lang>.md`, made scene for scene from the primary. Nothing is re-cut.

   You should now see one file per language.

5. Back in the session (the one working conversation with Claude), Claude scans the written file mechanically for facts of your instance, with `python scripts/docs-check.py --file <render>`. A hit is said aloud and you judge it. An instance fact is never edited out by hand: the render is regenerated without it.

   You should now see either no hit or a hit named for your judgement.

6. Claude verifies that the file exists and that its provenance is correct. The ledger's Renders table reads the provenance, and nobody writes a row. Claude remakes the ledger and reports what was rendered from what.

   You should now see a report of the render and its inputs.

7. Where the recipe has a `## Format` section, Claude makes the plain file beside the render. A `.docx` or a `.pptx` is made through pandoc. For a screenplay, the video or the player file is made through `scripts/md2video.py`, beside the render or at the recipe's `output:`. The screenplay's formats are described in [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

   You should now see the plain file next to the render.

8. Where a published file of the recipe exists, Claude tells you that it is now older than its render. It remakes nothing. The designed file is made on your command through a model, as [Publish a designed file](publish-a-designed-file.md) describes. A screenplay has no published file.

   You should now see the notice, where a published file exists.

## What you have afterwards

- The Markdown render, in `renders/` or at the recipe's `output:`.
- One translation per further language, where the recipe declares them.
- The plain file, where the recipe has a `## Format` section.
- A ledger that lists the render with what it was made from.

The render and its plain file are never edited by hand. To change them, change the recipe or its inputs and render again, because a render is generated and never a source of truth; the reasons are on [Renders and recipes](../about/renders-and-recipes.md).

A file you make yourself from a render, such as an edited copy or a PDF saved by hand, is yours when you keep it in `renders/` under a name of its own. It is kept in git and left alone by the forge ([Renders and recipes](../about/renders-and-recipes.md) says more).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it and stops.
- A tool is missing (pandoc, or Pillow and ffmpeg for a video): Claude says so aloud, the render stands and the plain file is not made. Install the tool and render again.
- The scan finds an instance fact: Claude says so aloud. Where the hit is a public fixed text of the recipe, or a fact of the engine's own history, it stands; otherwise the render is regenerated without it.
- The render later reads as stale: a version cited in its provenance differs from the current version of that file, or a cited file no longer exists. [Render provenance](../reference/render-provenance.md) holds the one definition of stale.

## A worked example

A project with the slug `my-project` has a recipe `recipes/pitch.md` that declares two languages, the primary first, and has a `## Format` section naming a deck.

```
/render pitch my-project
```

Claude reads the recipe and its inputs, and the subagent writes the primary render and then the translation. Claude scans both files, finds nothing, verifies the provenance and remakes the ledger. It makes the deck beside each render through pandoc. A published file of the recipe exists, so Claude tells you that it is now older than its render. You decide whether to make the designed file again.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth, and what becomes of the principal's own files beside it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
