---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: b583797ec14bffc1
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/recipe.md
  - templates/ledger.md#Published
---

# Render provenance

This page lists the provenance block that every render opens with, the
one definition of a stale render, the companion file of a published
file, and the places where these files land. It is for the user who
reads or checks them and for the extender who builds on them. Terms of
the forge are in the [Glossary](glossary.md).

The ledger is the state report that a script makes from the documents
at read time. The principal is the person whose thinking is being
forged.

## The provenance block of a render

Every render opens with this YAML front-matter, written by the
subagent that generates it (see [Render an output](../use/render-an-output.md)).

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
| `recipe` | the recipe's path and version |
| `inputs` | one line per input, path and version |

An input without a version of its own is cited by path alone.

### A render in several languages

A render in one of several languages adds one field. A translation
adds a second.

| Field | On | Holds |
|---|---|---|
| `language: <lang>` | each render of a recipe that declares languages | the language of this file |
| `translated_from: renders/<recipe>.<primary>.md` | a translation | the primary render it was made from |

### A stale render

A render is stale when any version cited in its front-matter differs
from the current version of that file, or when a cited file no longer
exists. This is the one definition of a stale render.

## Where the files land

| File | Place |
|---|---|
| the render | `renders/<recipe>.md` |
| the render of a recipe with languages | `renders/<recipe>.<lang>.md`, one per language |
| the render of a recipe with `output:` | the path `output:` names |
| the plain file of a render | beside the render |
| the player file of a screenplay | the recipe's `output:` in the engine's `docs/videos/` |
| the designed file | `published/<recipe>.<ext>` |
| the companion of a designed file | `published/<recipe>.md` |

The two optional fields of a recipe's header that decide the place:

| Field | Meaning |
|---|---|
| `output: <path>` | overrides the default `renders/<recipe>.md`; the path is read relative to the project root, and a leading slash means the engine root |
| `languages: <cs, en>` | the first language is primary, the rest are its translations; one render per language, `renders/<recipe>.<lang>.md` |

Further rules of the places:

- A render is overwritten freely. Its history lives in git.
- An `output:` path may lie in the engine's `docs/videos/`. There it
  is the place of the plain file of a screenplay only. The Markdown
  render stays in the project's `renders/`.
- The plain file (`.docx`, `.pptx`, or the video or player file) is
  made only where the recipe has a `## Format` section.
- A screenplay has no designed file.

## The published companion

A designed file is made by the command in [Publish a designed file](../use/publish-a-designed-file.md).
It then writes the companion `published/<recipe>.md`. The companion
is the provenance of the designed file. Its front-matter holds these
fields and nothing else:

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publishing |

A failed run writes no companion.

### The state of a published file

The state is `current` or `stale`. It is never written into the
companion. The ledger computes it from the render's `generated` date.

| State | When |
|---|---|
| `current` | the render's `generated` date is the one the companion names |
| `stale` | the render is newer than the companion names, or the render is missing |

The ledger's table of published files has one row per designed file,
with the columns File, Recipe, From render, Model, Published and
State. The first five come from the companion.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
