---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 91a9437c4b45fcc5
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Render provenance

This page is the reference for the provenance of a render: the front-matter every render opens with, the one definition of a stale render, the places the files land and the companion of a published file. It is for the reader who uses `/render` and `/publish` and for the one who extends them.

## The front-matter of a render

Every render opens with this block, written by the subagent that generates it (a subagent is an isolated Claude run that sees only the recipe and its inputs).

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

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `render` | the name of the recipe |
| `generated` | the date of the render |
| `recipe` | the path of the recipe and its version |
| `inputs` | one line per input: its path and its version |

An input without a version of its own is cited by path alone.

A render in one of several languages adds one field:

- `language: <lang>`

A translation adds a second one:

- `translated_from: renders/<recipe>.<primary>.md`

The translation names the primary render it was made from.

## Stale

A render is stale when any version cited in its front-matter differs from the current version of that file, or when a cited file no longer exists. This is the one definition of a stale render.

## Where the files land

| File | Place |
|---|---|
| the render | `renders/<recipe>.md` |
| the render in a language, where the recipe declares languages | `renders/<recipe>.<lang>.md`, one per language |
| the render where the recipe declares `output:` | the path `output:` names |
| the plain file (a `.docx` or `.pptx`, or a video) | beside the render |
| the plain file where `output:` names the engine's `docs/videos/` | `docs/videos/` |
| the designed file | `published/<recipe>.<ext>` |
| the companion of the designed file | `published/<recipe>.md` |

The Markdown render always stays in the project's `renders/`, even when `output:` sends the plain file to `docs/videos/`. A recipe without a `## Format` section ends at the Markdown. A screenplay has a plain file (a video, or the events of the player) and no designed file.

## The companion of a published file

`/publish` writes `published/<recipe>.md` after the designed file exists. A run that fails writes no companion. The front-matter holds these fields and nothing else:

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions from the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publishing |

## The state of a published file

The ledger lists each published file in its Published table: File, Recipe, From render, Model, Published and State. The row is read from the companion.

| State | Meaning |
|---|---|
| `current` | the render's generated date is the one the companion names |
| `stale` | the render is newer than that date, or is missing |

The ledger script computes the state from the render's `generated` date. Nobody writes it, and a stale published file is reported, never remade.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
