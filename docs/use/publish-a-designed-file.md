---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Publish a designed file

This page is for a user who has a render and wants the designed
PowerPoint or Word file made from it. `/publish` does that, through a
model and its document skills, and puts the file in `published/`.

## What it is for

A render comes first as Markdown, and where the recipe names a format
as a plain file beside it. `/publish` makes the designed file: slower
and dearer than the plain one, so it runs only when you ask.

- Only you start it. `/render` never does, `/release` never does, and
  Claude does not do it on its own judgement.
- It is expensive and takes minutes. Before it runs, it says so in one
  line.
- It makes a file and sends nothing anywhere.

## Steps

1. Run `/publish <recipe> [slug]`. The slug names the project; leave it
   out when the project is clear from context, and you are asked if it
   is not.
2. The command reads the recipe. If the recipe does not exist, it says
   so and stops.
3. It reads the recipe's `## Format` section. A recipe without one ends
   at the Markdown: the command says so and stops. An older recipe with
   a `## Build instructions` section is read as its Format; if it names
   no format, you are asked once, and offered to bring the recipe in
   line through `/recipe`.
4. It looks for the render, `renders/<recipe>.md` or the path the
   recipe gives as its `output:`. If there is none, it says so and
   stops. It never renders: what is published is the Markdown as it lies
   on disk, the text you have read.
5. If the render is stale, the command first says which version
   differs and waits for your word: publish it as it is, or stop so that
   you can run `/render` first.
6. It says in one line what runs and that it takes minutes, then runs
   the conversion for the format, `md2pptx.ps1` or `md2docx.ps1`, with
   the `claude` engine (`-Engine claude`). The template or reference
   document comes from the recipe's Format section.

## What you see

The file lands at `published/<recipe>.pptx` or `published/<recipe>.docx`
in the project. The command checks that it exists and reports what was
published from what.

It also writes a row in the ledger's Published table: the file, the
recipe and its version, the render it was made from, the model, the
date, and the state `current`. Every later `/render` of that recipe
sets the row to `stale`, which tells you the published file no longer
matches the render. A stale published file is reported, never remade on
its own; to refresh it you run `/publish` again.

If the run fails, the ledger is left as it was.

The published file is tracked in git like any render output and is
never edited by hand; the Markdown render stays the source of truth.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain
  file that come first.
- [Scripts](../reference/scripts.md): `md2pptx.ps1` and `md2docx.ps1`,
  the `claude` engine and what it needs.
