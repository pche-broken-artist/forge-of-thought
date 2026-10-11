---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: e7f48d10ecee17f4
inputs:
  - .claude/skills/render/SKILL.md
  - scripts/docs-check.py
---

# Render an output

`/render` regenerates a render, an audience-specific output such as a summary or a README, from its recipe, and makes its plain Word or PowerPoint file where the recipe asks for one. This page is for the user who wants a render brought up to date. A render is never a source of truth and is never edited by hand; the reason is on [Renders and recipes](../about/renders-and-recipes.md).

## When to use it

- A render is stale, that is, an input it cites has changed since it was generated. The definition of stale is on [Render provenance](../reference/render-provenance.md).
- You have changed a recipe and want to see the output.

Claude never regenerates a render on its own judgement. It reports a stale render and offers. A render is regenerated only on this command, or by `/release`.

## The command

```
/render <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/` directory, without the extension. `[slug]` names the project and may be left out where the current project is clear from context.

## What happens

1. Claude reads `recipes/<recipe>.md` of the project. If the recipe does not exist, Claude offers to compose it through `/recipe` and stops.

   You should now see either the recipe read or the offer to compose it.

2. Claude reads the inputs the recipe declares, from disk, at their current versions.

   You should now see no message of its own: the next step starts.

3. The Markdown is generated in isolation. Claude starts a subagent (a helper that sees only what it is given, never the conversation) that reads the recipe and its inputs alone. It writes the file to `renders/<recipe>.md`, or to the recipe's `output:` path where the recipe declares one, overwriting the old file. The file opens with provenance front-matter that names the project, the recipe, the date, the recipe version and each input with its version.

   You should now see the render written at its path.

4. Back in the main conversation, Claude scans the file mechanically for facts of this installation (names, hosts and the like) with this command:

   ```
   python scripts/docs-check.py --file <render>
   ```

   A hit is said aloud and you judge it. If it is an instance fact, the render is regenerated without it; it is never edited by hand. A fixed public text of the recipe, or a fact of the engine's own history, stands.

   You should now see either no hit or the hits named with their lines.

5. Claude verifies that the file exists and its provenance is correct, writes or updates the render's row in the Renders table of the ledger (the file that records the state of the project), and reports what was rendered from what.

   You should now see the report of the render and its inputs.

6. Where the recipe has a `## Format` section, Claude makes the plain `.docx` or `.pptx` file beside the render through pandoc, with the reference document and page size the section names. Where pandoc is missing, the render stands, the plain file is not made, and Claude says so. A recipe without the section ends at the Markdown.

   You should now see the plain file beside the render, or the statement that pandoc is missing.

7. Where the Published table of the ledger has a row for this recipe, Claude sets it to `stale` and says so. It remakes nothing: the designed file is made on request, as [Publish a designed file](publish-a-designed-file.md) describes.

   You should now see the published file marked stale, if there was one.

## What you have afterwards

- The render, overwritten with the current state of its inputs.
- The plain file beside it, where the recipe names a format and pandoc is present.
- A Renders row in the ledger that mirrors the provenance.
- A published file of the same recipe marked stale, if one existed.

## If something goes wrong

- The recipe does not exist: Claude stops and offers to compose it through `/recipe`.
- The scan names an instance fact: Claude says so and you judge it. The render is regenerated without the fact.
- Pandoc is missing: the render stands and no plain file is made. Claude says so.

## A worked example

You have a recipe `summary` in a project `my-project`, and its intent has changed since the last render.

```
/render summary my-project
```

Claude reads `recipes/summary.md` and its inputs, has the render generated, and writes `renders/summary.md`. It scans the file, finds no instance fact, updates the Renders row of `my-project` and reports the inputs with their versions. The recipe has a `## Format` section naming Word, so `renders/summary.docx` appears beside the render. A published `summary.docx` existed, so Claude marks it stale and tells you.

## See also

- [Render provenance](../reference/render-provenance.md): the front-matter block and the one definition of stale.
- [Publish a designed file](publish-a-designed-file.md): the designed file, made through a model.
- [Renders and recipes](../about/renders-and-recipes.md): why a render is generated and never a source of truth.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
