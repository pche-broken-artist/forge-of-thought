---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/<recipe>.history.md>
# output: <path>   # optional — overrides the default renders/<recipe>.md
# languages: <cs, en>   # optional — the first primary, the rest its translations, one render per language renders/<recipe>.<lang>.md (POS.1550)
---

# Recipe — <purpose>

<!-- A recipe: CLAUDE.md, Document chain, Renders (what it is) and
Versioning & status (how it is versioned). This skeleton owns the
shape only. -->

## Inputs
<!-- Artefacts this render is generated from, by path, one per line.
More than one input is legitimate (CLAUDE.md, Document chain, Renders),
e.g. intent + assignment. -->
- 10-intent.md

## Instructions
<!-- Audience, tone, what to emphasise, what to omit, target length,
register. Everything the renderer must know beyond the template. -->

## Format
<!-- Optional. A recipe without this section ends at the Markdown.
The two steps: CLAUDE.md, Document chain, Renders. Never copied into the
render (/render step 3). An older recipe's `## Build instructions` reads as this
section until its next iteration. -->
- Format: <pptx | docx | video | html-player>
- Plain file, made by `/render` through pandoc: reference
  <path | none>, page size <A4 | Letter>. <A screenplay's `video` or
  `html-player` is made through `scripts/md2video.py` instead, with
  the pace, the date and the look stated here; it has no published
  file (POS.1530).>
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must
  know>.

## Template
<!-- The literal skeleton of the render, with placeholders. Always
Markdown — the files made from it: CLAUDE.md, Document chain, Renders. -->
