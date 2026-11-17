---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 8a4ca8397a3e2f3b
inputs:
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
  - projects/forge/10-intent.md#POS.1910
---

# Publish a designed file

`/publish` makes the designed Word or PowerPoint file of a recipe from
its render, through a model, and puts it into `published/`. This page
is for you when the Markdown render has been read and approved and you
want the file to hand to others. Here the principal (the person whose
thinking is forged, you) is the only one who starts it.

## When to use it

Use it when a render exists, you have read it, and its recipe asks for
a `.pptx` or a `.docx`. The page [Render an output](render-an-output.md)
covers the Markdown and the plain file that come first.

Two cases end without a file:

- A recipe without a `## Format` section ends at the Markdown.
  `/publish` says so and stops.
- A screenplay has no published file.

## The command

```
/publish <recipe> [slug]
```

For example, `/publish my-pitch my-project` publishes the recipe
`my-pitch` of the project `my-project`. Without the slug, Claude takes
the current project from context and asks where that is ambiguous.

Only you start it. No other command runs it, and Claude never runs it
on its own judgement. A published file that has gone stale is reported
and never remade by itself.

## What happens

1. Claude reads the recipe `recipes/<recipe>.md` and checks the
   repository. The command runs on `main` only. A repository behind
   its origin or diverged from it is refused, because a published file
   is binary and is never merged. [Pull from the remote](pull-from-the-remote.md)
   says how to bring it current.
   You should now see no refusal and the recipe found. If the recipe
   does not exist, Claude says so and stops.

2. Claude reads the recipe's `## Format` section. An older recipe that
   still carries `## Build instructions` is read as its Format. Where
   it names no format, Claude asks once and offers to bring the recipe
   in line through `/recipe`.
   You should now see the format (`.pptx` or `.docx`) named, or the
   statement that the recipe ends at the Markdown.

3. Claude finds the render, `renders/<recipe>.md` or the path the
   recipe gives as `output:`. If it does not exist, Claude says so and
   stops. `/publish` never renders: what is published is the Markdown
   as it lies on disk, the text you have read.
   You should now see the render found.

4. Where the render is stale, Claude names which version differs before
   anything runs and waits for your word. You either publish as it is
   or stop and run `/render` first. [Render provenance](../reference/render-provenance.md)
   gives the definition of a stale render.
   You should now see either no remark, or the differing version named
   and Claude waiting.

5. Claude says in one line what runs and that it takes minutes. Then it
   runs `md2pptx.py` or `md2docx.py` with `--engine claude`, the
   recipe, the template or reference document and the model that the
   Format section names, and writes the file to
   `projects/<slug>/published/<recipe>.<ext>`. What each script needs
   installed is in [Scripts](../reference/scripts.md).
   You should now see the one-line notice, and after some minutes the
   run ends.

6. Claude verifies that the file exists, writes its companion
   `published/<recipe>.md`, and remakes the ledger (the file that
   holds the state of the project, made from the documents when read).
   It then reports what was published from what.
   You should now see the report naming the file and the render it
   was made from.

## What you have afterwards

- The designed file `published/<recipe>.pptx` or
  `published/<recipe>.docx`.
- The companion `published/<recipe>.md`. It records what the file was
  made from: the project, the file name, the recipe with its version,
  the render with its generated date and input versions, the model
  and the date of publishing.
- A row in the Published table of the ledger. The row shows the file,
  the recipe, the render it came from, the model, the date and a
  state. The state is `current` while the render is the one the
  companion names. It is `stale` once the render is newer or missing.
  The ledger computes the state; the companion does not hold it.

## If something goes wrong

- The recipe or the render does not exist: Claude says so and stops.
  Make the recipe, or run `/render` first.
- The recipe has no `## Format` section: the recipe ends at the
  Markdown, and nothing is published.
- The repository is behind or diverged: the command is refused. Bring
  it current as [Pull from the remote](pull-from-the-remote.md) says,
  then run `/publish` again.
- The run fails: no companion is written, so the ledger shows no row
  for a file that was not made. Run the command again once the cause
  is removed.

## Changing the designed file

The designed file is never edited by hand. What you want to change, you
copy first under a name of your own. That copy, or a PDF you save from
Word or PowerPoint, is yours. It is kept in `published/` with no
companion and no check. [Renders and recipes](../about/renders-and-recipes.md)
gives the reason.

## A worked example

You have read `renders/my-pitch.md` in the project `my-project`, and its
recipe has a `## Format` section for a `.pptx`.

1. You type `/publish my-pitch my-project`.
2. The repository is on `main` and current, so there is no refusal.
3. The render is as the recipe's last run made it, so Claude names no
   stale version.
4. Claude says that it will make the `.pptx` and that it takes minutes.
5. After the run, `projects/my-project/published/my-pitch.pptx` exists
   and `published/my-pitch.md` records what it was made from.
6. The Published table of the ledger shows the row as `current`. If you
   later change the render, the same row shows `stale`, and the file
   stays as it was until you run `/publish` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Pull from the remote](pull-from-the-remote.md): the pull that brings a repository behind its origin current.
- [Render provenance](../reference/render-provenance.md): the published companion and the definition of a stale render.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Renders and recipes](../about/renders-and-recipes.md): why the forge's files are never edited by hand and what the principal's own files beside them are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
