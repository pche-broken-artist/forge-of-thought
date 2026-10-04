---
project: <slug>
purpose: Slide-by-slide source material for <the presentation>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/<recipe>.history.md>
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <presentation name>

<!-- Presentation-genre recipe, composed via /recipe presentation; the
render is a slide-by-slide deck definition, from which /render makes
a plain PowerPoint file and /publish the designed one. A recipe and
the two steps: CLAUDE.md, Document chain, Renders.
-->

## Inputs
<!-- Chain artefacts the deck is generated from. A picture may come
from another render of this project: declare that render here too, so
provenance and staleness track it. -->
- 10-intent.md

## Instructions
- The render is **source material for building a presentation**, not
  the presentation itself: one section per slide, carrying the exact
  on-slide text <and the speaker notes>. Slide count ~<N>; follow the
  Template's slide list.
- Audience: <audience>. Register: <register>. Language: <English>.
- The one message: <what the audience must take away>. Centre of
  gravity: <where the deck dwells>.
- Content comes from the Inputs only — no invention, no softening.
  <Speaker notes cite the underlying <POS/REQ> IDs so a slide can be
  traced back and checked when the input moves.>
- On-slide density: at most <N> bullets per slide, <N> words per
  bullet; everything beyond that belongs to the notes.
- Vocabulary discipline: <terms that must not blur>.
- Must not appear: <what this audience must not see>.
- Diagrams sit on the slides the Template assigns them to, in one of
  two forms: an inline Mermaid block — valid standalone, simple
  enough to survive conversion into native slide shapes — or a
  reference `render: <file>` to a render of this project declared in
  Inputs.
- Per-slide format:
  ```
  ## SNN — <slide title>
  **On slide:** <title line and bullets exactly as they should appear>
  **Diagram:** <mermaid block | render: <file> — only where the
  Template assigns one>
  **Speaker notes:** <what the presenter says>
  ```

## Format
<!-- The shape: templates/recipe.md. How a template is named, where
the file lands and the default model: the header of
scripts/md2pptx.ps1. Never copied into the render. -->
- Format: pptx
- Plain file, made by `/render` through pandoc: reference
  <path | none>.
- Published file, made by `/publish` through a model: template
  <path | none — design freely>, model <name>, <overflow handling,
  diagram redraw expectations, visual accents — anything else the
  model must know>.

## Template
Front-matter provenance per the render convention, then one section
per slide:

| # | Slide | Content | Diagram |
|---|---|---|---|
| S01 | <title & frame> | <content, with source IDs> | — |
| S02 | <slide> | <content, with source IDs> | <diagram subject \| render: <file>> |
| S<NN> | <closing> | <content> | — |
