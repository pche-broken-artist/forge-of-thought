---
generated: 2026-10-09
made: mirrored
inputs-hash: 1bfeff3044e683d3
inputs:
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - CLAUDE.md
---

# Render provenance

This page is a reference for the front-matter every render opens with,
the one definition of a stale render, and the places where a render, its
plain file and its published file are kept. It is for the user who reads
a render and for the extender who changes how renders are made.

## The front-matter

Every render opens with this YAML block, written when `/render`
generates the file:

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
| `recipe` | the path of the recipe and its version |
| `inputs` | one line per input: its path and its version |

An input without a version of its own, `CLAUDE.md` for example, is cited
by path alone.

## Stale

A render is stale when any version cited in this front-matter differs
from the current version of that file, or when a cited file no longer
exists. This is the one definition of a stale render. `/forge`, `/check`
and `/publish` use it.

## Where the files are

| File | Place | Made by |
|---|---|---|
| the render (Markdown) | `renders/<recipe>.md`, or the recipe's `output:` path where it declares one (for example the repository README) | `/render` |
| the plain file | beside the render: `renders/<recipe>.docx` or `renders/<recipe>.pptx`, where the recipe has a `## Format` section | `/render`, through pandoc |
| the published file | `published/<recipe>.docx` or `published/<recipe>.pptx` | `/publish`, through a model, on the principal's command only |

A render is overwritten on every `/render`; its history lives in git.
Where pandoc is missing, the render stands and the plain file is not
made. A recipe without a `## Format` section ends at the Markdown.

## The published state

The ledger's Published table has a row for each published file: the
file, the recipe with its version, the render it was made from (its
`generated` date and the input versions of its front-matter), the model,
the date and a state, `current` or `stale`.

- `/publish` writes the row with the state `current`.
- `/render` sets the row of its recipe to `stale`: the published file is
  now older than its render. It remakes nothing.
- `/publish` on a stale render says which version differs and waits for
  the principal: publish as it is, or stop and `/render` first.

The ledger's Renders table mirrors the front-matter of each render.

## See also

- [Render an output](../use/render-an-output.md): the command.
