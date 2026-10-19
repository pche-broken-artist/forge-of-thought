---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 2104a50a62489510
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - templates/ledger.md#Published
---

# Render provenance

This page states the provenance block every render opens with, the
one definition of a stale render, the places where render files land
and the companion that records a published file. It is for the user
who reads a render's front-matter and for the extender who writes
anything that reads it. A render is an audience-specific output
generated from the documents of a project; a recipe says how it is
made. The ledger is the state file of a project, made by a script
at read time.

## The provenance block of a render

A render opens with this YAML front-matter, written by the
[subagent](../reference/glossary.md) that generates it (a subagent
is an isolated Claude run that sees only what its prompt names).

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
| `generated` | the date of the run |
| `recipe` | the recipe's path and version |
| `inputs` | one line per input, its path and version |

An input without a version of its own is cited by path alone.

### A render in several languages

| Field | Added to | Holds |
|---|---|---|
| `language: <lang>` | each render of the set | the language of this render |
| `translated_from: renders/<recipe>.<primary>.md` | each translation | the primary render it was made from |

The first language the recipe declares is the primary. Each
translation is a file of its own.

## Stale

A render is stale when any version cited in its front-matter differs
from the current version of that file, or when a cited file no
longer exists. This is the one definition of a stale render.

## Where the files land

| File | Place |
|---|---|
| the render, one language | `renders/<recipe>.md` |
| the render, one file per language | `renders/<recipe>.<lang>.md` |
| the render, where the recipe declares `output:` | the path `output:` names |
| the plain file (`.docx`, `.pptx`, `.mp4`) | beside the render, or at the recipe's `output:` |
| a screenplay's player file | the recipe's `output:` in the engine's `docs/videos/` |
| the designed file | `published/<recipe>.<ext>` |
| the companion of a designed file | `published/<recipe>.md` |

The Markdown render always stays in the project's `renders/`, even
where `output:` sends the format file into the engine's
`docs/videos/`. A screenplay has no designed file.

## The companion of a published file

`published/<recipe>.md` records where a designed file came from. It
is written when the file has been made, and a failed run writes no
companion. Its front-matter holds these fields and nothing else.

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `file` | the name of the published file |
| `recipe` | the recipe, with its version |
| `render` | `generated <date>` and the input versions of the render's front-matter |
| `model` | the model that made the file |
| `published` | the date of publication |

## The state of a published file

The state is `current` or `stale`. It is never written into the
companion: the ledger script computes it for the Published table.

| State | When |
|---|---|
| `current` | the render's `generated` date is the one the companion names |
| `stale` | the render is newer than the companion names, or the render is missing |

The Published table of the ledger has one row per designed file,
with the columns File, Recipe, From render, Model, Published and
State.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Publish a designed file](../use/publish-a-designed-file.md): the command that writes the companion.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
