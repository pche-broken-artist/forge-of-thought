---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f6f802d4a1e9d04b
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
  - projects/forge/10-intent.md#POS.1910
---

# Render an output

This page shows how you regenerate a render, and its plain file, with
`/render`. It is for the principal, the person whose thinking is
forged, who wants an output such as a pitch, a summary or a README
made again from its recipe.

A render is an audience-specific output generated from the documents
of a project. A recipe is the versioned file that says how it is made.
Both are explained in [Renders and recipes](../about/renders-and-recipes.md).

## When to use it

- You changed a recipe or one of its inputs and want the output made
  again.
- A render is stale, that is, a version cited in its provenance
  differs from the current version of that file, or a cited file no
  longer exists. The definition is in
  [Render provenance](../reference/render-provenance.md).

A render is regenerated only on this command or by `/release`. Claude
never regenerates one on its own judgement: it reports a stale render
and offers.

## The command

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/` folder,
without `.md`. The slug names the project; where it is left out,
Claude infers the project from context and asks if it is ambiguous.

## What happens

1. Claude reads `recipes/<recipe>.md`. If the recipe does not exist,
   it offers to compose one with `/recipe` and stops.

   You should now see either the recipe read or the offer to compose
   it.

2. Claude reads the inputs the recipe declares, at their current
   versions, from disk. Where the recipe reads the ledger (the single
   source of truth for state, made at read time), Claude makes it
   first with its script.

   You should now see the inputs read and, where needed, the ledger
   freshly made.

3. A subagent (an isolated Claude run that sees nothing of your
   conversation) generates the Markdown from the recipe and its inputs
   alone. It writes to `renders/<recipe>.md`, or to the recipe's
   `output:` path where the recipe declares one. The file opens with
   provenance front-matter.

   You should now see the render written at that path.

4. Where the recipe declares `languages:`, the subagent writes the
   primary render first. It then writes one translation per language
   as a file of its own, `renders/<recipe>.<lang>.md`, scene for scene,
   with nothing re-cut.

   You should now see one file per declared language.

5. Back in the session, Claude scans the file mechanically for facts
   of the instance (`python scripts/docs-check.py --file <render>`).
   A hit is said aloud and you judge it.

   You should now see either no hit or a hit named for your judgement.

6. Claude verifies that the file exists and that its provenance is
   correct. The ledger's Renders table reads that provenance; nobody
   writes a row. Claude then reports what was rendered from what.

   You should now see a report of the render and its inputs.

7. Where the recipe has a `## Format` section, Claude makes the plain
   file beside the render:
   - a `.docx` or `.pptx` through pandoc;
   - for a screenplay, the video or the player file through
     `scripts/md2video.py`, at the render or at the recipe's
     `output:`. The screenplay's formats are described in
     [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

   You should now see the plain file beside the render.

8. Where the Format names `png`, the render's own run draws the
   picture and writes it to `renders/<recipe>.png`. The Markdown
   render then carries the provenance and a link to the picture and
   nothing else. Nothing is converted afterwards.

   You should now see the picture file and a short Markdown render
   linking it.

9. Where a published file of the recipe exists, Claude tells you it is
   now older than its render. It remakes nothing: the designed file is
   made through a model, as
   [Publish a designed file](publish-a-designed-file.md) describes.

   You should now see that remark.

## What you have afterwards

- The render at `renders/<recipe>.md` or the recipe's `output:` path,
  with provenance front-matter.
- One file per language where the recipe declares languages.
- The plain file beside the render, where the recipe has a Format.
- A report of what was rendered from what.

The render and its plain file are never edited by hand. To change
them, change the recipe or its inputs and run `/render` again.

A file you make yourself from them and keep in `renders/` under a name
of its own, such as an edited copy or a PDF saved by hand, is yours.
It is kept in git and left alone by the forge; see
[Renders and recipes](../about/renders-and-recipes.md).

## If something goes wrong

- The recipe does not exist: Claude offers to compose it with
  `/recipe` and stops.
- The scan finds an instance fact: it is said aloud and you judge it.
  A fact is regenerated out, never edited by hand. A public fixed text
  of the recipe, or a fact of the engine's own history, stands.
- A tool for the plain file is missing (pandoc, or Pillow and ffmpeg
  for a video): the render stands, the plain file is not made, and
  Claude says so aloud.

## A worked example

A project `my-project` has `recipes/summary.md` with no `languages:`
and no `## Format` section.

```
/render summary my-project
```

Claude reads the recipe and its inputs, and the subagent writes
`renders/summary.md` with provenance front-matter. The scan finds no
instance fact, the provenance is verified, and Claude reports the
render and the inputs it was made from. The recipe has no Format, so
the work ends at the Markdown.

## See also

- [Render provenance](../reference/render-provenance.md): the
  front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed
  file, made through a model.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md):
  the screenplay's formats in full.
- [Renders and recipes](../about/renders-and-recipes.md): why a render
  is generated and never a source of truth, and what becomes of the
  principal's own files beside it.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
