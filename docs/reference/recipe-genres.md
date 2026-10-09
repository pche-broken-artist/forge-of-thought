---
generated: 2026-10-09
made: mirrored
inputs-hash: f1232b8ec70f5104
inputs:
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/SKILL.md
---

# Recipe genres

This page lists the recipe genres the forge has, one entry each, as `/man recipe` prints them: the genre's description, its skeleton and output, and the questions the interview works through. It is for the person who composes a recipe and for the one who extends the forge with a genre. Each genre is one file in `.claude/skills/recipe/genres/`, with its skeleton in `templates/recipe-<genre>.md`.

## Shared by every genre

In every genre the interviewer elicits the answers from the principal, offering options and trade-offs; the decisions are the principal's. The checklist closes with the language question: the render's language is what the recipe declares. The project's language is proposed from its ledger header and the principal is asked, never assumed. The recipe is then composed from the genre's skeleton, with unused placeholders and all template comments deleted.

A recipe outside any genre is legitimate: it is composed conversationally from `templates/recipe.md`.

## presentation

- **Description:** Compose a presentation recipe - a slide-by-slide deck definition, with a plain .pptx from /render and a designed one from /publish.
- **Skeleton:** `templates/recipe-presentation.md`.
- **Output:** a recipe whose render is a slide-by-slide Markdown deck definition: source material for a presentation, never the presentation itself. The PowerPoint files are made from it in two steps, `/render` and `/publish`. What each step needs is in the recipe's Format section, and the render carries content only.
- **Role:** interviewer.

Elicitation checklist:

1. **Audience and register.** Who sits in the room; technical or executive; how direct.
2. **Purpose and the one message.** What the audience must take away; the deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the intent). A picture may come from another render of the project: a slide references it as `render: <file>`, and that render is declared among Inputs so provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda slide yes or no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all? If yes, whether they carry traceability citations (position and requirement IDs) back to the inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is banished to the notes.
7. **Diagram policy.** Which slides carry a diagram; inline Mermaid (valid standalone, simple enough to survive conversion into native slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined Terms, house distinctions); the recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience: internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or none. For the published file, read by the model that designs the deck: the template, the model, overflow handling, diagram redraw expectations (the placeholders of the skeleton's Format section). How a template is named and what the model defaults to is in the header of `scripts/md2pptx.py`. These stay in the recipe and are never copied into the render.

## readme

- **Description:** Compose or iterate a project's readme recipe - the render is the project's README.md, regenerated at every release.
- **Skeleton:** `templates/recipe-readme.md`.
- **Output:** `README.md` in the project root.
- **Role:** interviewer. When the principal asks for a first version without an interview, it is drafted from the inputs (the ledger, the brief, the intent's essence) and presented as a draft to iterate.

Elicitation checklist:

1. **Primary reader.** The recipients of the assignment, colleagues browsing the repository, or the principal returning. The README is written for the first of them.
2. **Inputs.** A thought project: ledger, brief, intent, and the layers below it once they exist. A library: ledger and the two `00-INDEX.md` catalogues. Its README is a catalogue of what the library holds, with Role / Use for each document, and how to use it (for example the path a deck template is named by).
3. **What the essence must say** and how much of it: the problem, the direction, the recipients; one screen, not the intent.
4. **State.** Which ledger facts appear: chain versions and statuses, briefs and mining state, renders, what is waiting on the principal.
5. **What must not appear.** Confidentiality toward whoever can reach the repository; internal figures; nothing from other projects.

## release-notes

- **Description:** Compose or iterate a thought project's release-notes recipe - one section per release in six fixed groups, derived from the records of the chain's history logs.
- **Skeleton:** `templates/recipe-release-notes.md`; the skeleton owns the shape of the notes.
- **Output:** `RELEASE-NOTES.md` in the project root. Thought projects only: a library has no intent and therefore no release notes; its history is git.
- **Role:** interviewer, lightly; this genre has few degrees of freedom.

Elicitation checklist:

1. **Which companions feed the notes.** The default is every chain artefact but the brief: the intent, the assignment, later layers as they appear. A project may narrow it (the forge itself reads the intent alone).
2. **The reader.** The recipients tracking the project by default; a different reader changes what "Action required" means.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing through a genre.
