---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 0f43cd7ee7774256
inputs:
  - .claude/skills/publish/SKILL.md
  - .claude/skills/render/SKILL.md#7
---

# Publish a designed file

`/publish` makes the designed Word or PowerPoint file of a recipe from its render, through a model and its document skills. This page is for you, the one who has read a render and now wants the finished file. A render is the Markdown output generated from a recipe, and the plain file is the unstyled `.docx` or `.pptx` that `/render` makes beside it (see [Render an output](render-an-output.md)).

## When to use it

Use it when the render reads as you want it and you want the designed file made from it. Only you start it. `/render` never does, `/release` never does, and Claude never does on its own judgement. It is expensive and takes minutes, so it is not repeated freely.

## The command

```
/publish <recipe> [slug]
```

The recipe is the name of a file in the project's `recipes/` directory, and the slug names the project. Without a slug Claude infers the project from context and asks if it is ambiguous. For example, for a recipe called `executive-pitch` in a project `my-project`:

```
/publish executive-pitch my-project
```

## What happens

1. Claude reads the recipe. If it does not exist, Claude says so and stops.

   You should now see either a stop with that message, or the next step.

2. Claude reads the recipe's `## Format` section. A recipe without that section ends at the Markdown, so Claude says so and stops. A screenplay has no published file either. An older recipe that carries `## Build instructions` is read as its Format section. If that names no format, Claude asks once and offers to bring the recipe in line through `/recipe`.

   You should now see either a stop, or Claude going on with the format named.

3. Claude finds the render, `renders/<recipe>.md` or the path the recipe gives as `output:`. If it does not exist, Claude says so and stops. It never renders for you: what is published is the Markdown as it lies on disk, the text you have read.

   You should now see the render found, or a stop that names the missing file.

4. If the render is stale, Claude names which version differs before anything runs and waits for your word. A render is stale when a version cited in its front-matter differs from the current version of that file, or a cited file no longer exists. You answer in one of two ways: publish as it is, or stop so that you can `/render` first.

   You should now see Claude waiting for that word, or no pause at all when the render is current.

5. Claude says in one line what runs and that it takes minutes. It then runs `md2pptx.py` or `md2docx.py`, whichever the format asks for, with `--engine claude`. The file is written to `published/<recipe>.pptx` or `published/<recipe>.docx` in the project. What the scripts need installed is described in [Scripts](../reference/scripts.md).

   You should now see the one line, and after some minutes the run ends.

6. Claude checks that the file exists, writes its row in the ledger's Published table with state `current`, and reports what was published from what. The ledger is the project's single record of state.

   You should now see a report naming the published file and the render it came from.

## What you have afterwards

- The designed file in the project's `published/` directory.
- A row in the Published table of the ledger. It names the file, the recipe with its version, the render it was made from (its `generated` date and the input versions), the model, the date, and the state `current`.

Every later `/render` of that recipe sets the row to `stale` and says so. The published file is then older than its render. Nothing is remade: you run `/publish` again when you want a new file.

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The recipe has no `## Format` section: it ends at the Markdown, and Claude stops. There is no designed file for it.
- The render does not exist: Claude says so and stops. Run `/render` first.
- The render is stale: Claude waits for your word, as in step 4.
- The run fails: the ledger is left unchanged, so no row is written.

For a term you do not know, see the [Glossary](../reference/glossary.md).

## A worked example

A project `my-project` has a recipe `team-update` whose `## Format` section names a Word document. You have run `/render team-update my-project` and read the Markdown.

You type:

```
/publish team-update my-project
```

The render is current, so Claude does not pause. It says in one line that it is making the Word file through the model and that this takes minutes. When the run ends, `projects/my-project/published/team-update.docx` exists. The Published table has a new row for it with state `current`.

Later you edit the intent and run `/render team-update my-project`. The Markdown is regenerated, and Claude says the published file is now `stale`. The `.docx` stays as it is until you run `/publish team-update my-project` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
