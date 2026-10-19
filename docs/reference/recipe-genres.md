---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 7c13b5d71dabe0a1
inputs:
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - .claude/skills/recipe/SKILL.md
---

# Recipe genres

This page lists the genres of `/recipe`: the kinds of render recipe that Claude composes through an interview with the principal (the person whose thinking is forged). It is for the user who picks a genre and for the extender who needs to know what each genre asks and produces. Terms of the forge are explained in the [Glossary](glossary.md).

A genre is one file in `.claude/skills/recipe/genres/` with its skeleton in `templates/recipe-<genre>.md`. Bare `/recipe` lists these genres, each with its one-line description, and lists the project's existing recipes with their versions. A recipe outside any genre is legitimate: it is composed in conversation from `templates/recipe.md`.

## Overview

| Genre | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `presentation` | A slide-by-slide Markdown deck definition, with a plain `.pptx` from `/render` and a designed one from `/publish` | A talk or deck for a room | `.claude/skills/recipe/genres/presentation.md`, skeleton `templates/recipe-presentation.md` |
| `readme` | The project's `README.md`, regenerated at every release | Every project | `.claude/skills/recipe/genres/readme.md`, skeleton `templates/recipe-readme.md` |
| `release-notes` | `RELEASE-NOTES.md`, one section per release in six fixed groups, derived from the records of the chain's history logs | Every thought project (a library has none) | `.claude/skills/recipe/genres/release-notes.md`, skeleton `templates/recipe-release-notes.md` |
| `screenplay` | A teaching video of a terminal conversation cut from session records, made into a video or into the events of the player page by a script | A teaching video | `.claude/skills/recipe/genres/screenplay.md`, skeleton `templates/recipe-screenplay.md` |

## The frame every genre shares

Every genre runs in the same frame, which `/recipe` sets:

- Claude is the interviewer. It offers options and trade-offs, and the decisions are the principal's.
- The checklist closes with the language question. The render's language, or its languages where the genre allows a primary and its translations (`languages:`), is what the recipe declares. Claude proposes the project's language from its project file (`project.md`) and asks; it never assumes.
- The recipe is then composed from the genre's skeleton, with unused placeholders and all template comments deleted.
- The recipe is written once per round, on the principal's confirmation. A recipe has a version and no status, and its history goes into `recipes/<recipe>.history.md`, created from `templates/history.md` with the recipe.
- After writing, Claude offers `/render <recipe>` as the next step.

If the name given to `/recipe` is not a genre but an existing recipe of the project, Claude iterates that recipe, through its genre when one fits and otherwise in conversation. If neither exists, it lists the genres and stops.

## presentation

- **Description:** Compose a presentation recipe: a slide-by-slide deck definition, with a plain .pptx from /render and a designed one from /publish.
- **Skeleton:** `templates/recipe-presentation.md`.
- **Output:** a recipe whose render is a slide-by-slide Markdown deck definition. It is source material for a presentation, never the presentation itself. The PowerPoint files are made from it in two steps, `/render` for the plain file and `/publish` for the designed one. What each step needs is the recipe's Format section.

Elicitation checklist:

1. **Audience and register.** Who sits in the room; technical or executive; how direct.
2. **Purpose and the one message.** What the audience must take away. The deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the intent). A picture may come from another render of the project: a slide references it as `render: <file>`, and that render is declared among Inputs so that provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda slide yes or no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all. If yes, whether they carry traceability citations (position and requirement IDs) back to the inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is banished to the notes.
7. **Diagram policy.** Which slides carry a diagram; inline Mermaid (valid standalone, simple enough to survive conversion into native slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined terms, house distinctions); the recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience: internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or none. For the published file, read by the model that designs the deck: the template, the model, overflow handling, diagram redraw expectations (the placeholders of the skeleton's Format section). How a template is named and what the model defaults to is said in the header of `scripts/md2pptx.py`.

## readme

- **Description:** Compose or iterate a project's readme recipe: the render is the project's README.md, regenerated at every release.
- **Skeleton:** `templates/recipe-readme.md`.
- **Output:** `README.md` in the project root.

When the principal asks for a first version without an interview, Claude drafts it from the inputs (the ledger, which is the project's single record of state, the brief and the essence of the intent) and presents it as a draft to iterate.

Elicitation checklist:

1. **Primary reader.** The recipients of the assignment, colleagues browsing the repository, or the principal returning. The README is written for the first of them.
2. **Inputs.** A thought project: ledger, brief, intent, and the layers below it once they exist. A library: ledger and the two `00-INDEX.md` catalogues. Its README is a catalogue of what the library holds, with Role and Use for each document, and how to use it (for example the path a deck template is named by).
3. **What the essence must say** and how much of it: the problem, the direction, the recipients. One screen, not the intent.
4. **State.** Which ledger facts appear: chain versions and statuses, briefs and mining state, renders, what is waiting on the principal.
5. **What must not appear.** Confidentiality toward whoever can reach the repository; internal figures; nothing from other projects.

## release-notes

- **Description:** Compose or iterate a thought project's release-notes recipe: one section per release in six fixed groups, derived from the records of the chain's history logs.
- **Skeleton:** `templates/recipe-release-notes.md`. The skeleton owns the shape of the notes.
- **Output:** `RELEASE-NOTES.md` in the project root. Thought projects only: a library has no intent and therefore no release notes, and its history is git.

This genre has few degrees of freedom, so the interview is light.

Elicitation checklist:

1. **Which companions feed the notes.** The default is every chain artefact but the brief: the intent, the assignment, and later layers as they appear. A project may narrow it.
2. **The reader.** The recipients tracking the project by default. A different reader changes what Action required means.

## screenplay

- **Description:** Compose a screenplay recipe: a teaching video of a terminal conversation cut from session records, rendered as a screenplay and made into a video or into the events of the player page by a script.
- **Skeleton:** `templates/recipe-screenplay.md`.
- **Output:** a recipe whose render is a screenplay. The screenplay has a title card, a card of what the viewer will see, scenes with the real time of day, and an end card. Each scene has a caption of two parts (Now: what happens; Why: why the forge does it this way) and a fenced block of what the terminal shows. The caption is the teaching, the terminal the evidence.
- **Inputs of the recipe:** session records registered as sources (a transcript extract, by timestamps) and the brief that says what the videos are for.
- **Made into a file by:** `scripts/md2video.py`, in the format the recipe names. The render is never the video. The header of the script says what it needs.

See [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md) for the genre from recipe to played file.

Elicitation checklist:

1. **Audience and register.** Who watches; whether they have seen Claude Code; how the captions speak (plain, factual, no praise of the tool).
2. **Purpose and the one message.** What the viewer leaves with. The end card says it. Which principle of the forge the video shows.
3. **Inputs.** The transcript source and the sessions in it; the brief of the videos; a document the video shows being born, as a dependency by path.
4. **The beats.** The scenes pinned by the time of their first line and the lines that must appear, so that every render is the same cut. What is left out (the hours of wording, the saves).
5. **The quotes.** The principal's lines as typed; what is corrected (gross errors only) and what is kept (no diacritics, the speed). Which of Claude's answers are shown in full because the scene is about them; the rest are cut to the sentences that carry the move. Tool calls appear as one dim line; tool output and permission prompts do not appear at all. The verdict line is in today's form.
6. **Length.** Minutes of video, and what is shortened when there is too much: Claude's lines, never the principal's and never the captions.
7. **The title card.** The disclosure of the composition: real work, how many sessions, how many hours, times real, lines verbatim and shortened.
8. **What must not appear.** Names, companies, hosts, paths outside the forge. The instance's facts are never material.
9. **Languages.** The primary language (the language of the sessions) and the translations made from it in the same run. The render's notation stays English, the content is in the render's language. This point is the language question of the shared frame.
10. **Pace and look.** The three reading rates in words a second (the principal's lines, Claude's answers, file reports; 4, 8, 16 unless the principal wants otherwise), the date shown in the tab bar, the labels of the captions by language.
11. **Format.** `video` or `html-player`, one of them, never both. For `html-player`: whether the file goes out to the engine's `docs/videos/` by `output:`, with its number for the order of the course, or stays in the project's `renders/` for the company.

## The closing every genre shares

The language question and the composition from the skeleton close every genre. In the screenplay genre the language question is point 9, so only the composition from the skeleton follows it.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing through a genre.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the screenplay genre from recipe to played file.
- [Add a recipe genre](../extend/add-a-recipe-genre.md): adding a genre.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
