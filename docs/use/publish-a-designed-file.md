---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 496af30b8d8f1ea9
inputs:
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
  - projects/forge/10-intent.md#POS.1910
---

# Publish a designed file

This page shows how to make the designed Word or PowerPoint file of a
render with `/publish`. It is for you, the principal (the person whose
thinking is forged), once the Markdown render reads as you want it.

## When to use it

Use it when a render has a `## Format` section in its recipe and you
want the designed `.pptx` or `.docx` from it. The Markdown and the plain
file come first: see [Render an output](render-an-output.md).

Only you start it. `/render`, `/release` and Claude's own judgement
never publish, because the run is expensive.

A recipe without a `## Format` section ends at the Markdown, so there
is nothing to publish. A screenplay has no published file.

## The command

```
/publish <recipe> [slug]
```

For example, `/publish my-deck my-project` publishes the recipe
`my-deck` of the project `my-project`. Without a slug, Claude takes the
current project from the context, or asks when it is ambiguous.

## What happens

1. Claude reads the recipe and checks the repository. The repository
   must be on `main`, and a repository that is behind or diverged from
   its origin is refused, with `/pull` offered, because a published
   file is binary and is never merged. You should now see the recipe
   accepted, or the refusal with `/pull` offered.
2. Claude reads the recipe's `## Format` section. You should now see
   the format named, or a statement that the recipe ends at the
   Markdown.
3. Claude finds the render. It never renders: what is published is the
   Markdown as it lies on disk, the text you have read. You should now
   see the render found, or a statement that it does not exist.
4. Where the render is stale, Claude names which version differs and
   waits for your word: publish as it is, or stop so that you can
   `/render` first. What a stale render is, is defined in
   [Render provenance](../reference/render-provenance.md). You should
   now see the version named and the question put to you.
5. Claude says in one line what runs and that it takes minutes, because
   the file is made through a model and its document skills. It then
   runs `md2pptx.py` or `md2docx.py` with `--engine claude`; what the
   scripts need is in [Scripts](../reference/scripts.md). You should now
   see the file in `published/`.
6. Claude checks that the file exists and writes its companion,
   `published/<recipe>.md`. It then remakes the ledger (the state
   report made from the project's documents) and reports what was
   published from what. You should now see the companion beside the
   file and a report of the render it was made from.

## What you have afterwards

- The designed file, `published/<recipe>.pptx` or
  `published/<recipe>.docx`.
- Its companion, `published/<recipe>.md`, which records what the file
  was made from: the project, the file, the recipe with its version,
  the render with its date and input versions, the model and the date
  of publishing.
- A row in the Published table of the ledger. The ledger reads the
  companion and shows the file as `current`. Once the render is newer
  than the one the companion names, the row shows `stale`. A stale file
  is reported and never remade: you decide when to publish again.

## The designed file is never edited by hand

The designed file stays as the run made it. What you want to change,
you copy first under a name of your own. That copy, or a PDF you save
from Word or PowerPoint, is yours: it is kept in `published/` with no
companion and no check. See
[Renders and recipes](../about/renders-and-recipes.md).

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The recipe has no `## Format` section: Claude says so and stops. An
  older recipe that carries `## Build instructions` is read as its
  format; where it names none, Claude asks once and offers to bring the
  recipe in line through `/recipe`.
- The render does not exist: Claude says so and stops. Run `/render`
  first.
- The repository is not on `main`, or is behind or diverged from its
  origin: Claude refuses and offers `/pull`.
- The run fails: no companion is written, so the ledger shows no row
  for a file that was not made.

## A worked example

You have read the render of the recipe `my-deck` in the project
`my-project`, and its recipe names a PowerPoint format.

1. You type `/publish my-deck my-project`.
2. Claude finds the render current and says in one line that the
   PowerPoint file is being made through a model and takes minutes.
3. The run ends. Claude reports that
   `published/my-deck.pptx` was made from the render of `my-deck`, and
   `published/my-deck.md` lies beside it.
4. A week later you change the intent and run `/render my-deck`. The
   render is now newer, and the ledger shows the file as `stale`. The
   file itself is untouched until you run `/publish my-deck` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain
  file that come first.
- [Render provenance](../reference/render-provenance.md): the published
  companion and the definition of a stale render.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the
  `claude` engine and what it needs.
- [Renders and recipes](../about/renders-and-recipes.md): why the
  forge's files are never edited by hand and what the principal's own
  files beside them are.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
