---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/render/SKILL.md
  - CLAUDE.md
---

# Render an output

This page is for a user who has a render recipe and wants its output
made or made again: a README, a pitch, a summary. It says what
`/render` does and what you see when it has run.

## What a render is

A render is an output for one audience, generated from the documents
of a project. It is never edited by hand and is not a source of truth.
What you iterate is its recipe; to change the output, change the
recipe and render again.

## Run it

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/`. The slug
names the project; leave it out and the project is taken from context,
and if that is ambiguous you are asked.

1. The recipe is read. If it does not exist, you are offered to
   compose it through `/recipe` (by a genre where one fits, otherwise
   from the bare recipe skeleton), and the command stops there.
2. The inputs the recipe declares are read at their current versions.
3. The Markdown is generated in an isolated subagent. It sees only
   the recipe and its inputs, never your conversation, so the render
   is derived from the documents and not from what was said about
   them. It does not read the previous render unless the recipe
   declares it among its inputs.
4. The file is written to `renders/<recipe>.md`, or to the recipe's
   `output:` path if it declares one (the repository README is
   such a case). An existing file is overwritten; history lives in
   git.
5. Back in the session, the file and its provenance are checked, the
   ledger's Renders table is updated to mirror it, and you are told
   what was rendered from what.

## What you see

The render opens with front-matter that records the project, the
recipe and its version, the date and the inputs with their versions.
That block is what lets a render be called stale or current; its
shape and the one definition of stale are in
[Render provenance](../reference/render-provenance.md).

The render is content only, always Markdown. It carries no
instructions for a conversion; the recipe's `## Format` section is
never copied into it.

## The plain file

Where the recipe has a `## Format` section, the plain `.docx` or
`.pptx` is made beside the render through pandoc, using the reference
document and page size the section names. A recipe without that
section ends at the Markdown.

If pandoc is missing, the render stands, the plain file is not made,
and you are told so.

The designed file is not made here. That is a separate, deliberate
command: [Publish a designed file](publish-a-designed-file.md).

If the ledger's Published table has a row for the same recipe, it is
set to `stale` and you are told: the published file is now older than
its render. Nothing is remade.

## When a render is regenerated

Only when you give this command, or when `/release` runs. Claude never
regenerates a render on its own judgement. When a render is stale it
reports that and offers to render; the decision is yours.

## See also

- [Render provenance](../reference/render-provenance.md): the
  front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed
  file, made through a model.
- [About renders and recipes](../about/renders-and-recipes.md): why a
  render is generated and never a source of truth.
