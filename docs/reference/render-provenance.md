---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: ad318db974479f42
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
---

# Render provenance

This page states the provenance block that every render opens with, the one definition of a stale render, and the places where a render, its plain file and its published file land. It is for the reader who uses `/render` and for the extender who writes a recipe. The command itself is described in [Render an output](../use/render-an-output.md), and the terms of the forge are in the [Glossary](glossary.md).

## The provenance block

Every render opens with this YAML front-matter, written when the render is generated:

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

| Key | Value |
|---|---|
| `project` | The slug of the project. |
| `render` | The name of the recipe. |
| `generated` | The date of generation. |
| `recipe` | The path of the recipe and its version. |
| `inputs` | One line per input of the recipe: the path and its version. |

An input without a version of its own (`CLAUDE.md`, for one) is cited by path alone.

### A render in several languages

Where the recipe declares `languages:`, each language is a render of its own. Each adds one key:

| Key | Where | Value |
|---|---|---|
| `language` | A render in one of several languages | `<lang>` |
| `translated_from` | A translation | `renders/<recipe>.<primary>.md`, the primary render it was made from |

## Stale

A render is stale when any version cited in its front-matter differs from the current version of that file, or when a cited file no longer exists. This is the one definition of a stale render.

## Where the files land

| File | Place |
|---|---|
| The Markdown render | `renders/<recipe>.md` |
| The Markdown render of one language, where the recipe declares languages | `renders/<recipe>.<lang>.md` |
| The Markdown render, where the recipe declares `output:` | The `output:` path (the repository README is one) |
| The plain file, where the recipe has a `## Format` section | Beside the render, as `.docx` or `.pptx` made by pandoc, or as the file of the video format |
| The player file of a screenplay, where the recipe declares `output:` | The `output:` path in the engine's `docs/videos/`, where the script also renews the player page |
| The published file | `published/<recipe>.<ext>` in the project |

The Markdown render always stays in the project's `renders/`, even where `output:` points into the engine's `docs/videos/`. A recipe without a `## Format` section ends at the Markdown. A screenplay has no published file.

## The published file and its state

The published file is the designed `.pptx` or `.docx`, made by `/publish` from the Markdown render as it lies on disk. Its row in the ledger (the file that holds a project's state) records:

- the file
- the recipe with its version
- the render it was made from: its `generated` date and the input versions of its front-matter
- the model
- the date
- the state

The state is one of two values:

| State | Meaning |
|---|---|
| `current` | Set when the file is published. |
| `stale` | Set by `/render` when it regenerates the render of that recipe: the published file is then older than its render. |

A stale published file is reported and never remade by `/render`. `/publish` asks before it works from a stale render.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
