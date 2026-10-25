---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 2d4830f61bed532e
inputs:
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - .claude/skills/recipe/SKILL.md
---

# Recipe genres

This page lists the genres of `/recipe`: for each, what it is for, its
skeleton, its output and the elicitation checklist Claude works through
with the principal (the person whose thinking is being forged). It is
for the user who picks a genre and for the extender who adds one. Terms
such as recipe and render are in the [Glossary](glossary.md).

Each genre is one file, `.claude/skills/recipe/genres/<genre>.md`, with
its skeleton in `templates/recipe-<genre>.md`. Bare `/recipe` lists the
genres with their one-line descriptions, lists the project's existing
recipes with their versions and recommends a fit. A recipe outside any
genre stays legitimate: it is composed conversationally from
`templates/recipe.md`.

## The genres

| Genre | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `presentation` | a slide-by-slide deck definition, with a plain `.pptx` from `/render` and a designed one from `/publish` | a deck for a room | `.claude/skills/recipe/genres/presentation.md` |
| `readme` | the project's `README.md`, regenerated at every release | every project | `.claude/skills/recipe/genres/readme.md` |
| `release-notes` | one section per release in six fixed groups, derived from the records of the chain's history logs | every thought project | `.claude/skills/recipe/genres/release-notes.md` |
| `screenplay` | a teaching video of a terminal conversation cut from session records, made into a video or into the events of the player page by a script | a teaching video | `.claude/skills/recipe/genres/screenplay.md` |

## presentation

- **Description:** compose a presentation recipe, a slide-by-slide deck
  definition, with a plain `.pptx` from `/render` and a designed one
  from `/publish`.
- **Skeleton:** `templates/recipe-presentation.md`.
- **Output:** a recipe whose render is a slide-by-slide Markdown deck
  definition. It is source material for a presentation, never the
  presentation itself. The PowerPoint files are made from it in two
  steps, `/render` and `/publish`, and what each step needs is the
  recipe's Format section.
- **Role of Claude:** interviewer. It offers options and trade-offs; the
  decisions are the principal's.

Elicitation checklist:

1. **Audience and register.** Who sits in the room; technical or
   executive; how direct.
2. **Purpose and the one message.** What the audience must take away.
   The deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the
   intent). A picture may come from another render of the project: a
   slide references it as `render: <file>`, and that render is declared
   among Inputs so that provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda
   slide yes or no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all? If yes, whether they carry
   traceability citations (IDs of the intent and the assignment) back to
   the inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is
   banished to the notes.
7. **Diagram policy.** Which slides carry a diagram: inline Mermaid
   (valid standalone, simple enough to survive conversion into native
   slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined terms,
   house distinctions). The recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience:
   internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or none.
    For the published file, read by the model that designs the deck:
    the template, the model, overflow handling and diagram redraw
    expectations. These are the placeholders of the skeleton's Format
    section. How a template is named and what the model defaults to is
    given in the header of `scripts/md2pptx.py`.

## readme

- **Description:** compose or iterate a project's readme recipe. The
  render is the project's README, regenerated at every release.
- **Skeleton:** `templates/recipe-readme.md`.
- **Output:** `README.md` in the project root.
- **Role of Claude:** interviewer. When the principal asks for a first
  version without an interview, Claude drafts it from the inputs (the
  ledger, the brief, the essence of the intent) and presents it as a
  draft to iterate.

Elicitation checklist:

1. **Primary reader.** The recipients of the assignment, colleagues
   browsing the repository, or the principal returning. The README is
   written for the first of them.
2. **Inputs.** A thought project: ledger, brief, intent, and the layers
   below it once they exist. A library: ledger and the two `00-INDEX.md`
   catalogues. Its README is a catalogue of what the library holds, with
   Role and Use for each document, and how to use it (for example the
   path by which a deck template is named).
3. **What the essence must say** and how much of it: the problem, the
   direction, the recipients; one screen, not the intent.
4. **State.** Which ledger facts appear: chain versions and statuses,
   briefs and mining state, renders, what is waiting on the principal.
5. **What must not appear.** Confidentiality toward whoever can reach
   the repository; internal figures; nothing from other projects.

## release-notes

- **Description:** compose or iterate a thought project's release-notes
  recipe: one section per release in six fixed groups, derived from the
  records of the chain's history logs.
- **Skeleton:** `templates/recipe-release-notes.md`. The skeleton owns
  the shape of the notes.
- **Output:** `RELEASE-NOTES.md` in the project root. Thought projects
  only: a library has no intent and therefore no release notes, and its
  history is git.
- **Role of Claude:** interviewer, lightly, because this genre has few
  degrees of freedom.

Elicitation checklist:

1. **Which companions feed the notes.** The default is every chain
   artefact but the brief: the intent, the assignment, later layers as
   they appear. A project may narrow it.
2. **The reader.** The recipients tracking the project by default. A
   different reader changes what Action required means.

## screenplay

- **Description:** compose a screenplay recipe, a teaching video of a
  terminal conversation cut from session records, rendered as a
  screenplay and made into a video or into the events of the player
  page by a script.
- **Skeleton:** `templates/recipe-screenplay.md`.
- **Output:** a recipe whose render is a screenplay: a title card, a
  card of what the viewer will see, scenes with the real time of day,
  and an end card. Each scene has a caption of two parts (Now: what
  happens; Why: why the forge does it this way) and a fenced block of
  what the terminal shows. The caption is the teaching, the terminal the
  evidence. The render is never the video: the file is made from it by
  `scripts/md2video.py` in the format the recipe names, and the header
  of that script says what it needs.
- **Inputs of the recipe:** session records registered as sources (a
  transcript extract, by timestamps) and the brief that says what the
  videos are for.
- **Role of Claude:** interviewer.

Elicitation checklist:

1. **Audience and register.** Who watches; whether they have seen
   Claude Code; how the captions speak (plain, factual, no praise of
   the tool).
2. **Purpose and the one message.** What the viewer leaves with. The end
   card says it; which principle of the forge the video shows.
3. **Inputs.** The transcript source and the sessions in it; the brief
   of the videos; a document the video shows being born, as a
   dependency by path.
4. **The beats.** The scenes pinned by the time of their first line and
   the lines that must appear, so that every render is the same cut;
   what is left out (the hours of wording, the saves).
5. **The quotes.** The principal's lines as typed; what is corrected
   (gross errors only) and what is kept (no diacritics, the speed);
   which of Claude's answers are shown in full because the scene is
   about them, the rest cut to the sentences that carry the move; tool
   calls as one dim line, tool output and permission prompts not at all;
   the verdict line in today's form.
6. **Length.** Minutes of video, and what is shortened when there is too
   much: Claude's lines, never the principal's and never the captions.
7. **The title card.** The disclosure of the composition: real work, how
   many sessions, how many hours, times real, lines verbatim and
   shortened.
8. **What must not appear.** Names, companies, hosts, paths outside the
   forge; the instance's facts are never material.
9. **Languages.** The primary language (the language of the sessions)
   and the translations made from it in the same run. The render's
   notation stays English; the content is in the render's language.
10. **Pace and look.** The three reading rates in words a second (the
    principal's lines, Claude's answers, file reports; 4, 8, 16 unless
    the principal wants otherwise), the date shown in the tab bar, the
    labels of the captions by language.
11. **Format.** `video` or `html-player`, one of them, never both. For
    `html-player`: whether the file goes out to the engine's
    `docs/videos/` by `output:`, with its number for the order of the
    course, or stays in the project's `renders/` for the company; and
    the course on the player page: the section the video belongs to and
    its name per language, and what the viewer will learn, listed in
    place of the title card's title.

In this genre the language question is point 9. The composition from the
skeleton closes the genre as described below.

## The shared closing

Every genre runs in the same frame, and its checklist ends with the
same two parts.

- **The language question.** The render's language is what the recipe
  declares, or its languages where the genre allows a primary and its
  translations (`languages:`). Claude proposes the project's language
  from its project file (`project.md`) and asks. It never assumes.
- **The composition from the skeleton.** The recipe is composed from the
  genre's skeleton, with unused placeholders and all template comments
  deleted. It is composed with the principal: options and trade-offs
  are offered and the decisions are his. It is written once per round,
  on confirmation. A recipe carries a version and no status, and its
  history goes into `recipes/<recipe>.history.md`, created from
  `templates/history.md` with the recipe.

After writing, Claude offers `/render <recipe>` as the next step.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing through a genre.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the screenplay genre from recipe to played file.
- [Add a recipe genre](../extend/add-a-recipe-genre.md): adding a genre.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
