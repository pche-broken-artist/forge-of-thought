---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <one line from the newest row of $1>
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <purpose>

<!-- A recipe is the iterated thing; its render is generated output.
Never polish a render by hand: change the recipe, run
/render <recipe>. Recipes are tools: version + updated date in
front-matter and no status (a recipe is never approved); its Version
History lives in the companion <recipe>.history.md, last_change
summarising the newest row. -->

## Inputs
<!-- Artefacts this render is generated from, by path, one per line.
More than one input is legitimate (e.g. intent + assignment). -->
- 10-intent.md

## Instructions
<!-- Audience, tone, what to emphasise, what to omit, target length,
register. Everything the renderer must know beyond the template. -->

## Template
<!-- The literal skeleton of the render, with placeholders. Always
Markdown — format conversion happens outside the forge. -->
