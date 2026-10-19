---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: a75807f0209b1fc2
inputs:
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Publish a designed file

This page shows how to make the designed Word or PowerPoint file of a render with `/publish`. It is for you as the principal (the person whose thinking is being forged), when the Markdown render and its plain file are not enough and a designed file is wanted.

## When to use it

Use it when a render exists, you have read it, and you want the designed `.docx` or `.pptx` made from it. The plain file that `/render` produces comes first: see [Render an output](render-an-output.md).

Only you start it. `/render`, `/release` and Claude's own judgement never publish, because the run is expensive.

## The command

```
/publish <recipe> [slug]
```

The `<recipe>` is the name of a recipe of the project. The `[slug]` names the project and can be left out when the project is clear from context.

## What happens

1. Claude finds the project and reads the recipe. It checks that the repository is on `main` and is neither behind nor diverged from its origin. A published file is binary and is never merged, so a repository behind or diverged is refused and Claude offers `/pull`.
   You should now see no refusal, or the offer of `/pull` if the repository is out of step.
2. Claude reads the recipe's `## Format` section. A recipe without it ends at the Markdown, and Claude says so and stops. A screenplay has no published file.
   You should now see the format (Word or PowerPoint) the recipe names, or a message that the recipe stops at the Markdown.
3. Claude finds the render, `renders/<recipe>.md` or the path the recipe's `output:` gives. If it does not exist, Claude says so and stops. It never renders: the file is made from the Markdown as it lies on disk, the text you have read.
   You should now see no message about a missing render.
4. If the render is stale, Claude names which version differs before anything runs and waits for your word. You choose to publish as it is, or to stop and run `/render` first. How a stale render is defined is on [Render provenance](../reference/render-provenance.md).
   You should now see either no remark, or the differing version and a question to you.
5. Claude says in one line what runs and that it takes minutes. It then runs the script of the format (`md2pptx.py` or `md2docx.py`) with `--engine claude`, so that a model and its document skills design the file. What the scripts need installed is on [Scripts](../reference/scripts.md).
   You should now see the one line, then a wait of some minutes.
6. Claude checks that the file exists and writes its companion, `published/<recipe>.md`. It then remakes the ledger (the project's table of state) and reports what was published from what.
   You should now see the report naming the file and the render it was made from.

## What you have afterwards

- The designed file in the project's `published/` folder, as `<recipe>.pptx` or `<recipe>.docx`.
- A companion `published/<recipe>.md` that records what the file was made from: the project, the file, the recipe with its version, the render with the date it was generated and its input versions, the model, and the date of publishing. The companion is described on [Render provenance](../reference/render-provenance.md).
- A row in the ledger's Published table, read from the companion: file, recipe, the render it came from, model, date and state.

The state is `current` while the render's generated date is the one the companion names. It is `stale` once the render is newer or missing. The state is computed, never written by hand.

A stale published file is only reported. `/publish` never remakes it by itself; you run it again.

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The repository is not on `main`, or is behind or diverged from its origin: the run is refused and `/pull` is offered.
- The recipe has no `## Format` section: the recipe ends at the Markdown and nothing is published. An older recipe that carries `## Build instructions` is read as its Format. Where that names no format, Claude asks once and offers to bring the recipe in line through `/recipe`.
- The render does not exist: Claude says so and stops. Run `/render <recipe>` first (see [Render an output](render-an-output.md)).
- The run fails: no companion is written, so the Published table shows no new row.

## A worked example

You have a recipe `board-pitch` in a project `my-project`, and its render has been read and agreed.

```
/publish board-pitch my-project
```

Claude finds the repository on `main` and level with its origin, reads the Format section (PowerPoint), and finds `renders/board-pitch.md` up to date. It says that the designed deck is about to be made and takes minutes, and runs the PowerPoint script with `--engine claude`. When the file exists, Claude writes `published/board-pitch.md`, remakes the ledger and reports that `published/board-pitch.pptx` was made from the render of that date. The Published table shows the file as `current`. If you later change the intent and render again, the table shows it as `stale` until you publish again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Render provenance](../reference/render-provenance.md): the published companion and the definition of a stale render.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
