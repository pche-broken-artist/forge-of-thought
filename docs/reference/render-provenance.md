---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 972d14c18f70ce72
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Render provenance

This page is the reference for the provenance block every render opens
with, the definition of a stale render, the companion file of a
published file and the places where these files land. It is for the
person who runs renders and publishes and for the one who extends the
forge. A render is an audience-specific output generated from the
chain; a recipe is the versioned file that says how it is made.

## The front-matter of a render

Every render opens with this YAML front-matter, written by the
subagent that generates it:

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

Inputs without a version of their own (for example `CLAUDE.md`) are
cited by path alone.

A render in one of several languages adds one field:

- `language: <lang>`

A translation adds a second field:

- `translated_from: renders/<recipe>.<primary>.md`

## A stale render

A render is stale when any version cited in its front-matter differs
from the current version of that file. It is also stale when a cited
file no longer exists. This is the one definition of the term.

## Where the files land

| File | Place |
|---|---|
| Markdown render | `renders/<recipe>.md` |
| Render in one of several languages | `renders/<recipe>.<lang>.md`, one file per language |
| Render with an `output:` in its recipe | the path the recipe's `output:` names |
| Plain file of a document format | beside the render |
| Player file of a screenplay | beside the render, or at the recipe's `output:` in the engine's `docs/videos/` |
| Designed file | `published/<recipe>.pptx` or `published/<recipe>.docx` |
| Companion of the designed file | `published/<recipe>.md` |

An `output:` path may lie outside the project, in the engine's
`docs/videos/`. That is the place of the plain format file only. The
Markdown render always stays in the project's `renders/`.

A screenplay has no designed file.

## The companion of a published file

`published/<recipe>.md` is the provenance of the published file. It
is written after the file exists, and a failed run writes none. Its
front-matter has these fields and nothing else:

| Field | Value |
|---|---|
| `project` | the project's slug |
| `file` | the published file's name |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publishing |

## The state of a published file

The ledger computes the state of each published file and nobody
writes it. The Published table has one row per designed file, with
the columns File, Recipe, From render, Model, Published and State.
The values of State are:

- `current`: the render's generated date is the one the companion
  names.
- `stale`: the render is newer than the companion's date, or the
  render is missing.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
