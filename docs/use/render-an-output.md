---
generated: 2026-10-10
made: mirrored
inputs-hash: a63c4b5d68138cbe
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
  - CLAUDE.md
---

# Render an output

This page is for the person who wants an output, such as a pitch, a
summary or the README, regenerated from its recipe. It says what
`/render` does, what you see, and what you are asked to judge.

## Run it

```
/render <recipe> [slug]
```

The recipe is the name of a file in the project's `recipes/` directory.
The slug names the project; without it the command takes the current
project from context, and asks if that is ambiguous.

A render is regenerated only on this command, or by `/release`.
Claude never regenerates one on its own judgement: when a render is
stale it reports that and offers to run the command.

If the recipe does not exist, the command offers to compose it through
`/recipe` and stops.

## What happens

1. The recipe is read, and so are the inputs it declares, at their
   current versions, from disk. This includes `CLAUDE.md`: the copy a
   subagent carries in its context may be older than the file.
2. The Markdown is generated in an isolated subagent. It sees only the
   recipe and its inputs, never your conversation, so a render is
   derived from the artefacts and not from what was said about them.
   It is told the shape of the provenance block and that nothing of
   the people who run the forge is material. It does not read the
   previous render unless the recipe declares it as an input (the
   release-notes genre does), and it does not touch the ledger.
3. The subagent writes the file to `renders/<recipe>.md`, or to the
   recipe's `output:` path if it declares one, as the repository README
   does. An existing file is overwritten; history lives in git. The
   file opens with provenance front-matter, which is described under
   "See also".

## What you check afterwards

Back in the session the written file is scanned mechanically for
instance facts, with `python scripts/docs-check.py --file <render>`.
The scan looks for the values recorded as instance facts in the
engine's local instance file, for the absolute path of a machine, and
for any extra pattern it is given.

- A hit is said aloud and you judge it.
- An instance fact is regenerated out of the render, never edited out
  by hand.
- A public fixed text of the recipe stands, and so does a fact of the
  engine's own history.

Then the file is verified to exist with correct provenance, the
render's row in the ledger's Renders table is written or updated, and
the command reports what was rendered from what.

## The plain file

Where the recipe has a `## Format` section, the plain Word or
PowerPoint file is made beside the render through pandoc, using the
reference document and page size the section names. If pandoc is
missing, the render stands, the plain file is not made, and this is
said aloud. A recipe without the section ends at the Markdown.

The designed file is never made here; that is the work of `/publish`.
Where the ledger's Published table has a row for the same recipe, its
state is set to `stale` and this is said, because the published file
is now older than its render. Nothing is remade.

## See also

- [Render provenance](../reference/render-provenance.md): the
  front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed
  file, made through a model.
- [About renders and recipes](../about/renders-and-recipes.md): why a
  render is generated and never a source of truth.
