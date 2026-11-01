---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 990943fcd6c5828a
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Render provenance

This page is the reference for the provenance block every render opens with, the one definition of a stale render, the place of each file a render or a publication makes, and the companion of a published file. It is for the reader who runs `/render` or `/publish` and for the one who extends them.

## The provenance block

Every render opens with this YAML front-matter, written by the subagent (an isolated helper that sees only the recipe and its inputs) that generates it.

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
| `project` | the project's slug |
| `render` | the name of the recipe |
| `generated` | the date of the render |
| `recipe` | the recipe's path and its version |
| `inputs` | one line per input, path and version |

An input without a version of its own (such as `CLAUDE.md`) is cited by path alone.

### A render in several languages

Where a recipe declares several languages, each language is a render of its own, and its front-matter adds:

| Field | Holds | On |
|---|---|---|
| `language` | the language of this render | every render of the set |
| `translated_from` | `renders/<recipe>.<primary>.md`, the primary render it was made from | each translation |

## Stale

A render is stale when any version cited in its front-matter differs from the current version of that file, or when a cited file no longer exists. This is the one definition of a stale render.

## Where the files land

| File | Place |
|---|---|
| The render | `renders/<recipe>.md` |
| The render of one language, where the recipe declares languages | `renders/<recipe>.<lang>.md` |
| The render, where the recipe declares an `output:` path | that path (for example the repository README) |
| The plain file (`.docx`, `.pptx`), where the recipe has a `## Format` section | beside the render |
| The player file of a screenplay, where the format is `video` or `html-player` | beside the render, or at the recipe's `output:` |
| The designed file | `published/<recipe>.<ext>` |
| The companion of the designed file | `published/<recipe>.md` |

Further rules of place:

- An `output:` path may lie outside the project, in the engine's `docs/videos/`. That is the place of the plain file only. The Markdown render always stays in the project's `renders/`.
- In `docs/videos/` the script that makes the player file also renews the player page.
- A recipe without a `## Format` section ends at the Markdown render and has no plain file.
- A screenplay has no designed file.
- A render is overwritten freely on each run.

## The published companion

The companion `published/<recipe>.md` is the provenance of a published file. It is written after the file is verified to exist, and a failed run writes none. Its front-matter holds these fields and nothing else.

| Field | Holds |
|---|---|
| `project` | the project's slug |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publication |

## The state of a published file

The state is `current` or `stale`. It is never written in the companion. The ledger script computes it and shows it in the Published table, one row per designed file, with the columns File, Recipe, From render, Model, Published and State.

| State | When |
|---|---|
| `current` | the render's `generated` date is the one the companion names |
| `stale` | the render is newer than the companion names, or the render is missing |

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
