---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 364e5415ce116c64
inputs:
  - .claude/skills/publish/SKILL.md
---

# Publish a designed file

This page shows how the principal (the person whose thinking is forged) makes the designed Word or PowerPoint file of a render with `/publish`. It is for the user who has a render and wants the finished file.

## When to use it

Use it when a render has been read and approved, and the recipe names a format. A recipe without a `## Format` section ends at the Markdown, and `/publish` says so and stops.

Publishing is expensive and takes minutes, because a model and its document skills build the file. Only you start it. `/render`, `/release` and Claude's own judgement never publish. The Markdown and the plain file that come first are made by `/render`: see [Render an output](render-an-output.md).

## The command

```
/publish <recipe> [slug]
```

`<recipe>` is the name of a recipe of the project. `[slug]` names the project and may be left out where the current project is clear.

## What happens

1. Claude reads the recipe and its `## Format` section.

   You should now see either the format it will make, or a plain statement that the recipe has no Format section and ends at the Markdown.

2. Claude looks for the render, `renders/<recipe>.md` or the path the recipe names as its output.

   You should now see no message, or a statement that the render does not exist and the run stops. `/publish` never renders: it publishes the Markdown as it lies on disk, the text you have read.

3. Where the render is stale, Claude names which version differs before anything runs and waits for your word.

   You should now see the question: publish as it is, or stop so that you can run `/render` first. The word is yours.

4. Claude says in one line what runs and that it takes minutes. It then runs the conversion script of the format with the `claude` engine, which makes the file in `published/`. The scripts and what they need installed are on the page [Scripts](../reference/scripts.md).

   You should now see that one line, and then the run.

5. Claude checks that the file exists and writes its row in the ledger (the project's table of state) under Published.

   You should now see a report of what was published from what.

## What you have afterwards

- The designed file `published/<recipe>.pptx` or `published/<recipe>.docx`.
- A row in the ledger's Published table with the state `current`. Every later `/render` of that recipe sets the row to `stale`. A stale file is reported and never remade by another command: you run `/publish` again.

The command makes a file and sends nothing anywhere.

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The recipe has no `## Format` section: Claude says it ends at the Markdown and stops. An older recipe with `## Build instructions` is read as its Format. Where that names no format, Claude asks once and offers to bring the recipe in line through `/recipe`.
- The render does not exist: Claude says so and stops. Run `/render` first.
- The render is stale: Claude waits for your word, as in step 3.
- The run fails: the ledger is left unchanged. What each script needs installed is described in its own header, and the page [Scripts](../reference/scripts.md) says it.

## A worked example

You have a recipe `<recipe>` with a Format section that names a presentation. You type:

```
/publish <recipe>
```

Claude finds the render and sees that it is current. It says that it will make the designed file through a model and that this takes minutes. It runs, and reports that `published/<recipe>.pptx` was made from the render of that recipe. The ledger now has a Published row for the file with the state `current`.

Later you change the recipe and run `/render <recipe>`. The row becomes `stale`. When you want the new file, you run `/publish <recipe>` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
