---
generated: 2026-10-09
made: mirrored
inputs-hash: 54453441d9c35b4c
inputs:
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Publish a designed file

This page is for the person who has a render he has read and wants it
as a designed PowerPoint or Word file. It says how to run `/publish`,
what it checks first and what it leaves in the project.

## What `/publish` does

`/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from
the render of that recipe, as the render lies on disk, and puts it in
the project's `published/` directory. It works through a model and its
document skills, which is why it is expensive and takes minutes. The
slug is optional: without it the current project is used, and you are
asked if that is ambiguous.

Only you start it. `/render` never does, `/release` never does, and
Claude does not do it on his own judgement. Before it runs, Claude
says in one line what is about to run and that it takes minutes.

It makes a file and sends nothing anywhere.

## Before you publish

The Markdown render, and the plain file beside it where the recipe
names a format, come first: see [Render an output](render-an-output.md).
`/publish` does not render. What it publishes is the Markdown you have
already read.

It stops, and says so, in these cases:

- The recipe does not exist.
- The recipe has no `## Format` section. Such a recipe ends at the
  Markdown. An older recipe with a `## Build instructions` section is
  read as if it were Format; if it names no format, you are asked
  once, and offered to bring the recipe in line through `/recipe`.
- The render does not exist.

## If the render is stale

When the render is stale, Claude names which version differs before
anything runs and waits for your word. You choose one of two things:

- publish the render as it is, or
- stop, run `/render` yourself, and publish afterwards.

The decision is always yours. `/publish` never renders to catch up.

## What you get

1. The script for the format runs: `md2pptx.py` for a deck, `md2docx.py`
   for a Word document, with `--engine claude`. The recipe's Format
   section names the template or reference document and the model;
   what the scripts need installed is in [Scripts](../reference/scripts.md).
2. The file lands as `published/<recipe>.pptx` or
   `published/<recipe>.docx` in the project.
3. Claude checks that the file exists and writes a row in the ledger's
   Published table: the file, the recipe with its version, the render
   it was made from, the model, the date, and the state `current`.
4. Claude reports what was published from what.

If the run fails, the ledger is not changed.

## When the file goes stale

The Published table says whether each file is `current` or `stale`.
Every later `/render` of that recipe sets the published file to
`stale`. A stale published file is reported, never remade on its own:
to bring it up to date you run `/publish` again.

The published file is tracked in git like any render output and is
never edited by hand. The Markdown render stays the source of truth.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
