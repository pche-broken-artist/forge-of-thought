---
generated: 2026-10-09
made: mirrored
inputs-hash: 3dc732faeff5dda8
inputs:
  - .claude/skills/render/SKILL.md
  - CLAUDE.md
---

# Render an output

This page is for a user who has a recipe and wants its output made
again from the current documents of the project. It says what
`/render` does, what you see afterwards and when a render is
regenerated at all.

## Run the command

Type `/render <recipe> [slug]`. The recipe is the name of a file in
the project's `recipes/` directory. The project slug is optional when
the project is clear from context; otherwise you are asked.

If the recipe does not exist, nothing is rendered. You are offered to
compose it through `/recipe`, from a genre where one fits, otherwise
from the plain recipe skeleton.

## What happens

1. The recipe is read, and then every input it declares, at its
   current version, from disk. `CLAUDE.md` is read from disk too, so
   a render never works from an older copy held in the session.
2. The Markdown is generated in an isolated subagent. It sees only the
   recipe and its inputs, never the conversation: a render is derived
   from the documents, not from what was said about them. It does not
   read the previous render unless the recipe lists it as an input
   (the release notes do, for the sections already released), and it
   does not touch the ledger.
3. The file is written to `renders/<recipe>.md`, or to the path the
   recipe gives in its `output:` field (the repository README is
   one). An existing file is overwritten; the history is in git.
4. The render opens with provenance front-matter: the project, the
   recipe, the date, and the recipe and inputs with the versions they
   were read at. Its exact shape, and the one definition of when a
   render is stale, are on [Render provenance](../reference/render-provenance.md).
5. Back in the session the file and its provenance are checked, the
   ledger's Renders table is updated to mirror them, and you are told
   what was rendered from what.

The render is content only, always Markdown. Instructions for a
conversion stay in the recipe and are never copied into the render.

## The plain Word or PowerPoint file

Where the recipe has a `## Format` section, the plain `.docx` or
`.pptx` is made beside the render through pandoc, with the reference
document and page size the section names. If pandoc is missing, the
render stands, the plain file is not made, and this is said aloud. A
recipe without the section ends at the Markdown.

The designed file is not made here. That is a separate and costlier
step, described on [Publish a designed file](publish-a-designed-file.md).
If the ledger's Published table has a row for this recipe, its state
is set to `stale` and you are told: the published file is now older
than its render. Nothing is remade.

## When a render is regenerated

Only on `/render`, or by `/release`. Claude never regenerates a render
on its own judgement. When a render is stale, Claude reports it and
offers to regenerate; you decide.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [About renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth.
