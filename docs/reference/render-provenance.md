---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 4989459bfc7ea01f
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
---

# Render provenance

This page states the provenance block every render opens with, the one
definition of a stale render and the places where a render, its plain
file and its published file land. It is for the user and the extender
who read or check renders. A render is an audience-specific output
generated from the documents of a project, never a source of truth.

## The provenance block

Every render opens with this YAML front-matter, written when the render
is generated:

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

| Key | Holds |
|---|---|
| `project` | the slug of the project |
| `render` | the name of the recipe |
| `generated` | the date of generation |
| `recipe` | the path of the recipe and its version |
| `inputs` | one line per input: its path and its version |

An input without a version of its own (`CLAUDE.md`, for example) is
cited by its path alone.

## Stale

A render is stale when any version cited in its front-matter differs
from the current version of that file, or when a cited file no longer
exists. This is the one definition.

## Where the files land

| File | Place | Made by |
|---|---|---|
| The render | `renders/<recipe>.md`, or the path the recipe gives under `output:` | `/render` |
| The plain file | beside the render, in the format the recipe's `## Format` section names (`.docx` or `.pptx`) | `/render`, through pandoc |
| The designed file | `published/<recipe>.<ext>` in the project | `/publish`, through a model |

- A recipe without a `## Format` section ends at the Markdown: no
  plain file is made.
- Where pandoc is missing, the render stands and the plain file is not
  made.
- The render is always Markdown, content only. The recipe's `## Format`
  section is never copied into it.

## The published state

The ledger's Published table has one row per published file: the file,
the recipe with its version, the render it was made from (its
`generated` date and the input versions of its front-matter), the
model, the date and a state.

| State | Meaning |
|---|---|
| `current` | set when the file is published |
| `stale` | set by `/render` when it regenerates the render of that recipe: the published file is older than its render |

A stale published file is reported and never remade. Only `/publish`,
on the principal's command, makes a new one.

## See also

- [Render an output](../use/render-an-output.md): the command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
