---
generated: 2026-10-10
made: mirrored
inputs-hash: d8433cf286de3628
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Render provenance

This page is for the user and the extender. It states the front-matter
every render opens with, when a render is stale, and where a render, its
plain file and its published file lie.

## The front-matter

Every render opens with this YAML block, written when the render is
generated:

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

| Key | Content |
|---|---|
| `project` | the slug of the project |
| `render` | the name of the recipe |
| `generated` | the date of generation |
| `recipe` | the recipe's path with its version |
| `inputs` | one line per input, the path with its version |

An input without a version of its own, `CLAUDE.md` for one, is cited by
its path alone.

## A stale render

A render is stale when any version cited in its front-matter differs
from the current version of that file, or when a cited file no longer
exists. This is the one definition of the term. Where a render is
stale, the forge's state map and its checks report it, and `/publish`
names the differing version before it runs.

## Where the files lie

| File | Place |
|---|---|
| the render | `renders/<recipe>.md`, or the path the recipe's `output:` gives (the repository README is one) |
| the plain file | beside the render: `renders/<recipe>.docx` or `renders/<recipe>.pptx`, made through pandoc where the recipe has a `## Format` section |
| the published file | `published/<recipe>.docx` or `published/<recipe>.pptx`, made by `/publish` through a model |

A recipe without a `## Format` section ends at the Markdown: no plain
file and no published file.

## The state of a published file

The ledger's Published table has one row per published file: the file,
the recipe with its version, the render it was made from (its
`generated` date and the input versions of its front-matter), the model,
the date and a state, `current` or `stale`.

A new row is `current`. When the render of that recipe is generated
again, the row becomes `stale`: the published file is older than its
render. Nothing remakes it; a published file is made only by
`/publish`, on the principal's command.

## See also

- [Render an output](../use/render-an-output.md): the command.
