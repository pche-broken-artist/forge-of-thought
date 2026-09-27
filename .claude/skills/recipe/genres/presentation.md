---
description: Compose a presentation recipe — a slide-by-slide deck definition, with a plain .pptx from /render and a designed one from /publish
---

Genre: presentation. Skeleton: `templates/recipe-presentation.md`.

The product is a recipe whose render is a slide-by-slide Markdown deck
definition — source material for a presentation, never the
presentation itself. The PowerPoint files are made from it in the
two steps of CLAUDE.md, Document chain 7; what each step needs is
the recipe's Format section, and the render carries content only.

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his (`/recipe`, step 2) —
then compose the recipe from the skeleton.

Elicitation checklist:
1. **Audience and register.** Who sits in the room; technical or
   executive; how direct.
2. **Purpose and the one message.** What the audience must take away —
   the deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the
   intent). A picture may come from another render of the project: a
   slide references it as `render: <file>`, and that render is
   declared among Inputs so provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda
   slide yes/no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all? If yes, whether they carry
   traceability citations (POS/REQ IDs) back to the inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is
   banished to the notes.
7. **Diagram policy.** Which slides carry a diagram; inline Mermaid
   (valid standalone, simple enough to survive conversion into native
   slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined
   Terms, house distinctions); the recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience:
   internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or
    none. For the published file, read by the model that designs the
    deck: the template, the model, overflow handling, diagram redraw
    expectations — the placeholders of the skeleton's Format
    section; how a template is named and what the model defaults to
    is the header of `scripts/md2pptx.ps1`. They stay in the recipe
    and are never copied into the render.

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
