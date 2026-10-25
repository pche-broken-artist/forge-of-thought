---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 6433be71e3a7bfa3
inputs:
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Publish a designed file

`/publish` makes the designed Word or PowerPoint file of a render, through a model and its document skills. This page is for you, the principal (the person whose thinking is forged), when a render is read and approved and you want the designed file to hand on.

## When to use it

Use it when the Markdown render is as you want it and you want the designed `.pptx` or `.docx`. Nothing else makes this file: `/render` never does, `/release` never does and Claude does not do it on its own judgement. It starts only when you type the command. The command makes a file and sends it nowhere.

The recipe must have a `## Format` section that names the format. A recipe without one ends at the Markdown, and `/publish` says so and stops. A screenplay has no published file.

## The command

```
/publish <recipe> [slug]
```

The slug names the project. Without it Claude infers the project from context and asks if that is ambiguous. The Markdown and the plain file that come before this step are made by `/render`; see [Render an output](render-an-output.md).

## What happens

1. Claude reads the recipe `recipes/<recipe>.md`. It stops, saying so, if the recipe does not exist. It also refuses unless the repository is on `main` and level with its origin, because a published file is binary and is never merged. A repository that is behind or has diverged is refused, and `/pull` is offered.

   You should now see either the next step starting or a refusal that names the reason.

2. Claude reads the `## Format` section. A recipe without it ends at the Markdown, and Claude says so and stops. An older recipe that still has a `## Build instructions` section is read as its Format section. Where that names no format, Claude asks once, and offers to bring the recipe in line through `/recipe`.

   You should now see the format (Word or PowerPoint) settled, or a plain statement that the recipe ends at the Markdown.

3. Claude finds the render, `renders/<recipe>.md` or the path the recipe's `output:` gives. It stops, saying so, if there is none. It never renders: what is published is the Markdown as it lies on disk, the text you have read.

   You should now see no message about a missing render.

4. If the render is stale, Claude names which version differs before anything runs, and waits for your word. You either publish as it is, or stop and run `/render` first. What makes a render stale is on [Render provenance](../reference/render-provenance.md).

   You should now see the question only if the render is stale, and nothing runs until you answer.

5. Claude says in one line what runs and that it takes minutes, because the run is expensive. Then it runs the script of the format (`md2pptx.py` or `md2docx.py`) with `--engine claude`, naming the recipe, the template or reference document and the model that the Format section gives. The file is written into `published/`. What each script needs installed is on [Scripts](../reference/scripts.md).

   You should now see the one-line notice, then the designed file `published/<recipe>.pptx` or `published/<recipe>.docx` once the run ends.

6. Claude checks that the file exists and writes its companion `published/<recipe>.md`. Then it remakes the ledger and reports what was published from what.

   You should now see the report naming the file and the render it was made from.

## What you have afterwards

- The designed file in `published/`.
- The companion `published/<recipe>.md`, which records what the file was made from: the project, the file name, the recipe with its version, the render (its generated date and the input versions of its front-matter), the model and the date of publishing. Its fields are described on [Render provenance](../reference/render-provenance.md).
- A row in the Published table of the ledger. The row is read from the companion and shows the file, the recipe, the render it came from, the model, the date and the state. The state is `current` while the render's generated date is the one the companion names. It is `stale` once the render is newer or missing. The state is computed when the ledger is made and is never written into the companion.

A stale published file is only reported. `/publish` never remakes it by itself.

## If something goes wrong

- The recipe does not exist: Claude says so and stops.
- The repository is not on `main`, or is behind or diverged from its origin: Claude refuses and offers `/pull`.
- The recipe has no `## Format` section: it ends at the Markdown, and Claude says so and stops.
- The render does not exist: Claude says so and stops. Run `/render` first.
- The render is stale: Claude waits for your word, to publish as it is or to stop.
- The run fails: no companion is written, so the ledger shows no new published file. The reason for a failure is the script's output; what each script needs installed is on [Scripts](../reference/scripts.md).

## A worked example

The recipe is `<recipe>` in the project `<slug>`, with a `## Format` section that names Word.

```
/publish <recipe> <slug>
```

The repository is on `main` and level with its origin. The render `renders/<recipe>.md` is older than none of its inputs, so Claude raises no stale warning. It prints one line saying that the Word file is being made through a model and takes minutes. When the run ends, `projects/<slug>/published/<recipe>.docx` exists and so does `published/<recipe>.md`. Claude reports that the file was published from the render of the recipe, and the Published table of the ledger shows the file as `current`.

Later you change the intent and run `/render <recipe>`. The render is now newer than the companion names, and the table shows the file as `stale`. Nothing remakes it until you run `/publish <recipe> <slug>` again.

## See also

- [Render an output](render-an-output.md): the Markdown and the plain file that come first.
- [Render provenance](../reference/render-provenance.md): the published companion and the definition of a stale render.
- [Scripts](../reference/scripts.md): `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
