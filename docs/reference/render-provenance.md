---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a80f8f74677b3da6
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/recipe.md
  - templates/ledger.md#Published
---

# Render provenance

This page lists what every render opens with, when a render counts as stale, where the files of a render and of a published file land, and what the companion of a published file holds. It is for the reader who makes or checks renders and for the one who extends the forge. A render is an audience-specific output generated from the documents of a project, and a recipe is the versioned file that says how it is made. A published file is the designed `.pptx` or `.docx` that `/publish` makes from a render.

## The provenance block of a render

Every render opens with this YAML front-matter, written by the subagent that generates it (an isolated agent that sees only the recipe and its inputs):

```yaml
---
project: <slug>
render: <recipe>
generated: YYYY-MM-DD
recipe: recipes/<recipe>.md v<version>
inputs:
  - <path> v<version>
---
```

An input without a version of its own is cited by path alone.

A render in several languages adds one field, and a translation adds a second:

| Field | Where | Value |
|---|---|---|
| `language` | every render of a recipe that declares several languages | `<lang>` |
| `translated_from` | a translation only | `renders/<recipe>.<primary>.md`, the primary render it was made from |

## Stale

A render is stale when any version cited in its front-matter differs from the current version of that file, or when a cited file no longer exists.

## Where the files land

| File | Place |
|---|---|
| Render | `renders/<recipe>.md` |
| Render in one of several languages | `renders/<recipe>.<lang>.md`, one per language |
| Render with an `output:` path | the recipe's `output:`, read from the project root; a leading slash means the engine root |
| Plain file of a render | beside the render |
| Player file of a screenplay | the recipe's `output:` in the engine's `docs/videos/`, where the Markdown render still stays in the project's `renders/` |
| Picture (format `png`) | `renders/<recipe>.png`, beside a Markdown render that carries the provenance and a link to the picture |
| Published file | `published/<recipe>.<ext>` |
| Companion of a published file | `published/<recipe>.md` |

The formats a recipe's Format section names are `pptx`, `docx`, `video`, `html-player` and `png`. A recipe without a Format section ends at the Markdown. A screenplay and a `png` have no published file.

## The companion of a published file

`/publish` writes `published/<recipe>.md` after the published file exists. Its front-matter holds these fields and nothing else:

| Field | Value |
|---|---|
| `project` | the project slug |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date |

A failed run writes no companion.

## The state of a published file

The ledger computes the state of each published file and nobody writes it. The ledger's Published table has one row per published file with the columns File, Recipe, From render, Model, Published and State.

| State | Meaning |
|---|---|
| `current` | the render's generated date is the one the companion names |
| `stale` | the render is newer than the companion names, or the render is missing |

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
