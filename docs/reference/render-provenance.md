---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Render provenance

This page is a reference for the person who uses `/render` and for the
one who extends the forge. It states the provenance block every render
opens with, the one definition of a stale render, and the places where
a render, its plain file and its published file are put.

## The front-matter of a render

Every render opens with this YAML block:

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
| `generated` | the date of the render |
| `recipe` | the path of the recipe, with its version |
| `inputs` | one line per declared input: its path and its version |

An input without a version of its own, such as `CLAUDE.md`, is cited
by path alone.

## Stale render

A render is stale when any version cited in its front-matter differs
from the current version of that file, or when a cited file no longer
exists. This is the one definition; `/forge` and `/check` cite it.

## Where the files are

| File | Place | Made by |
|---|---|---|
| the render | `renders/<recipe>.md`, or the path in the recipe's `output:` if it declares one | `/render` |
| the plain file | beside the render: `renders/<recipe>.docx` or `renders/<recipe>.pptx`, where the recipe carries a `## Format` section | `/render`, through pandoc |
| the published file | `published/<recipe>.docx` or `published/<recipe>.pptx` | `/publish`, through a model |

A render is overwritten at each run. The render carries content only,
and it is Markdown always. A recipe without a `## Format` section ends
at the Markdown. If pandoc is missing, the render stands and the plain
file is not made.

## The state of a published file

The ledger's Published table has a row for each published file. The
row holds the file, the recipe with its version, the render it was
made from (its `generated` date and the input versions of its
front-matter), the model, the date and a state:

| State | Meaning |
|---|---|
| `current` | set when `/publish` has made the file |
| `stale` | set by `/render` when it regenerates the render of that recipe: the published file is now older than its render |

Nothing is remade when a file turns `stale`. `/publish` takes the
Markdown as it lies on disk. If that render is stale by the definition
above, it says which version differs and waits for the principal's
word: publish as it is, or stop and render first.

## See also

- [Render an output](../use/render-an-output.md): the command.
