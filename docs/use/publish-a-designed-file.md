---
generated: 2026-10-10
made: mirrored
inputs-hash: cabece33b82eb06c
inputs:
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Publish a designed file

This page is for the person who has a render he has read and wants it
as a designed PowerPoint or Word file. It says how to make that file
with `/publish`, what you will see, and what the command will not do.

## What it does

`/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from
the render of a recipe, as the render lies on disk. A model makes it,
through its document skills, and the file lands in the project's
`published/` directory as `published/<recipe>.pptx` or
`published/<recipe>.docx`. Without a slug the command infers the
project from context and asks if that is ambiguous.

It is a step of its own, never part of another. Only you start it:
`/render` does not, `/release` does not, and Claude never does on its
own judgement. It is expensive and takes minutes, which is why it
waits for your command.

It makes a file and sends nothing anywhere.

## Before you publish

The Markdown render and, where the recipe names a format, the plain
file come first. See the page Render an output. `/publish` never
renders: what it publishes is the Markdown as it is now, the text you
have read.

## Steps

1. Run `/publish <recipe> [slug]`.
2. If the recipe does not exist, the command says so and stops.
3. If the recipe has no `## Format` section, it ends at the Markdown:
   the command says so and stops. A recipe that still carries the
   older `## Build instructions` section is read as Format; if it
   names no format, the command asks once and offers to bring the
   recipe in line through `/recipe`.
4. If the render does not exist, the command says so and stops.
5. If the render is stale, the command names which version differs
   and waits for you. Your word is one of two: publish as it is, or
   stop so that you can run `/render` first.
6. The command says in one line what runs and that it takes minutes,
   then runs the script of the format (`md2pptx.py` or `md2docx.py`)
   with `--engine claude`, using the template or reference document
   and the model the recipe's Format section names.
7. When the run is back, the command checks that the file exists and
   reports what was published from what.

## What you see afterwards

The ledger's Published table has a new row for the file: the recipe
with its version, the render it was made from, the model, the date,
and the state `current`. Every later `/render` of that recipe sets the
row to `stale`. A stale published file is reported, never remade by
another command; to bring it up to date you run `/publish` again.

A failed run changes nothing in the ledger.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain
  file that come first.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`,
  the `claude` engine and what it needs.
