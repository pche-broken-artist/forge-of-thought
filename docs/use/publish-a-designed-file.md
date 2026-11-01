---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 422aedcf9e321c43
inputs:
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
  - projects/forge/10-intent.md#POS.1910
---

# Publish a designed file

This page shows how you make the designed Word or PowerPoint file of a render with `/publish`. It is for you as the principal, the person whose thinking is forged, once you have read a render and want it as a finished file.

## When to use it

Use it when the Markdown render of a recipe is the text you have read and you want it as a designed `.pptx` or `.docx`. The Markdown and the plain file come first, through `/render` (see [Render an output](render-an-output.md)).

Only you start this command. `/render`, `/release` and Claude's own judgement never run it, because it is expensive: a model works through its document skills and the run takes minutes.

Two recipes end before this command:

- A recipe without a `## Format` section ends at the Markdown. `/publish` says so and stops.
- A screenplay has no published file.

## The command

```
/publish <recipe> [slug]
```

`<recipe>` is the name of a file in the project's `recipes/`. The slug names the project; without it Claude infers the project from context and asks if that is ambiguous.

## What happens

1. Claude reads the recipe. It must be on the `main` branch, and the repository must not be behind or diverged from its origin. If it is, `/publish` refuses and offers `/pull`.
   You should now see the recipe accepted, or a refusal that names the branch or the state against origin.
2. Claude reads the recipe's `## Format` section and finds the render, `renders/<recipe>.md` or the path the recipe's `output:` names.
   You should now see no stop. If the recipe has no Format section, or the render does not exist, Claude says so and stops.
3. If the render is stale, Claude names which version differs and waits for your word: publish as it is, or stop so that you can run `/render` first. `/publish` never renders. What it publishes is the Markdown as it lies on disk, the text you have read. The definition of a stale render is on [Render provenance](../reference/render-provenance.md).
   You should now see either no remark, when the render is current, or the version that differs and a question to you.
4. Claude says in one line what runs and that it takes minutes. Then it runs the script of the format, `md2pptx.py` or `md2docx.py`, with `--engine claude`, the recipe, and the template or reference document and the model that the Format section names. What the scripts need installed is on [Scripts](../reference/scripts.md).
   You should now see the one line, and then the run in progress.
5. Claude checks that the file exists in `published/` and writes the companion `published/<recipe>.md`, then remakes the ledger.
   You should now see a report of what was published from what.

## What you have afterwards

- The designed file in `published/`, as `<recipe>.pptx` or `<recipe>.docx`.
- The companion `published/<recipe>.md`. It records which recipe and which render the file was made from, the model and the date. The shape is on [Render provenance](../reference/render-provenance.md).
- A row in the Published table of the ledger. The ledger reads the companion and shows the file `current`. It shows `stale` once its render is newer or missing. A stale file is only reported, never remade for you.

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The recipe has no `## Format` section: it ends at the Markdown, and Claude says so and stops. An older recipe with `## Build instructions` is read as its Format. Where it names no format, Claude asks once and offers to bring the recipe in line through `/recipe`.
- The render does not exist: Claude says so and stops. Run `/render <recipe>` first.
- The repository is not on `main`, or is behind or diverged from its origin: `/publish` refuses. Use `/pull` when it is offered.
- The run fails: no companion is written, so the ledger shows no new row for it. Run the command again.

## The designed file is not edited by hand

Do not edit the published file. If you want to change it, copy it first under a name of your own and work on the copy. That copy, or a PDF you save from Word or PowerPoint, is yours: keep it in `published/`, and the forge sets no companion, no ledger row and no check on it. Why the forge's own files stay untouched is on [Renders and recipes](../about/renders-and-recipes.md).

## A worked example

The project has the slug `my-project`, and its recipe `pitch` names a Word format. The render `renders/pitch.md` is current.

```
/publish pitch my-project
```

Claude is on `main`, in step with its origin. It says that a Word file is being made through a model and that this takes minutes. When the run ends, `projects/my-project/published/pitch.docx` and `projects/my-project/published/pitch.md` exist. The ledger shows the file as `current`.

Later you change the intent and run `/render pitch my-project`. The render is now newer than the companion records, so the ledger shows the file as `stale`. Nothing remakes it until you run `/publish pitch my-project` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Render provenance](../reference/render-provenance.md): the published companion and the definition of a stale render.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Renders and recipes](../about/renders-and-recipes.md): why the forge's files are never edited by hand and what the principal's own files beside them are.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
