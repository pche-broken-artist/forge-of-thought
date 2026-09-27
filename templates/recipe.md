---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <one line from the newest row of recipes/<recipe>.history.md>
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <purpose>

<!-- A recipe: CLAUDE.md, Document chain 7 (what it is) and
Versioning & status (how it is versioned). This skeleton owns the
shape only. -->

## Inputs
<!-- Artefacts this render is generated from, by path, one per line.
More than one input is legitimate (e.g. intent + assignment). -->
- 10-intent.md

## Instructions
<!-- Audience, tone, what to emphasise, what to omit, target length,
register. Everything the renderer must know beyond the template. -->

## Format
<!-- Optional. A recipe without this section ends at the Markdown.
The two steps: CLAUDE.md, Document chain 7. Never copied into the
render. An older recipe's `## Build instructions` reads as this
section until its next iteration. -->
- Format: <pptx | docx>
- Plain file, made by `/render` through pandoc: reference
  <path | none>, page size <A4 | Letter>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must
  know>.

## Template
<!-- The literal skeleton of the render, with placeholders. Always
Markdown — the files made from it: CLAUDE.md, Document chain 7. -->
