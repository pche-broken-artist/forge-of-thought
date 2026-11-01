---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: f1bc8b79c49dcc45
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Render provenance

This page is the reference for the provenance every render opens with, the one definition of a stale render, the places where renders and their plain files land, and the companion that records a published file. It is for the user who reads a render's header and for the extender who writes a recipe or a script that reads it.

A render is an audience-specific output generated from the documents of a project by a recipe. A recipe is the versioned file that says how a render is made. A published file is the designed `.pptx` or `.docx` made from a render.

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

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `render` | the name of the recipe |
| `generated` | the date the render was made |
| `recipe` | the path of the recipe and its version |
| `inputs` | one line per input: the path and its version |

An input without a version of its own (for example `CLAUDE.md`) is cited by its path alone.

### A render in several languages

A recipe may declare several languages. The first is the primary and the rest are translations, one render file per language.

| Field | Where | Holds |
|---|---|---|
| `language` | every render of such a recipe | the language of this render |
| `translated_from` | a translation only | `renders/<recipe>.<primary>.md`, the primary render it was made from |

## Stale

A render is stale when any version cited in its front-matter differs from the current version of that file, or when a cited file no longer exists. This is the one definition. The state map and the checks cite it.

## Where the files land

| File | Place |
|---|---|
| the render | `renders/<recipe>.md` |
| the render of one language | `renders/<recipe>.<lang>.md` |
| the render when the recipe declares `output:` | the path `output:` names (for example the repository README) |
| the plain file of a render (`.docx`, `.pptx`) | beside the render |
| the player file of a screenplay | beside the render, or at the recipe's `output:` in the engine's `docs/videos/` |
| the designed file | `published/<recipe>.<ext>` |
| the companion of a published file | `published/<recipe>.md` |

An `output:` path may lie outside the project only in the engine's `docs/videos/`, and then it is the place of the plain file alone. The Markdown render always stays in the project's `renders/`. A render is overwritten on every generation. A screenplay has no designed file.

## The published companion

The companion `published/<recipe>.md` is the provenance of the published file. It is written when the file has been made, and a failed run writes none. Its front-matter holds these fields and nothing else:

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publication |

The state of the published file is not written in the companion.

## The state of a published file

The ledger computes the state of each published file when it is made. It has one row per companion, with the columns File, Recipe, From render, Model, Published and State.

| State | Holds when |
|---|---|
| `current` | the render's `generated` date is the one the companion names |
| `stale` | the render is newer than the companion names, or is missing |

When a render is regenerated and a companion exists, the published file is older than its render. Nothing remakes it: a stale published file is reported only.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
