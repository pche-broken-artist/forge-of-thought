---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 4b493afee0d6bc47
inputs:
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - .claude/skills/recipe/SKILL.md
---

# Recipe genres

This page lists the genres of `/recipe`, the command that composes a
render recipe with the principal (the person whose thinking is forged).
A genre is one kind of render with its own skeleton, its own output
and its own elicitation checklist, that is, the questions Claude asks
the principal before it composes the recipe. Terms of the forge are
explained in the [Glossary](glossary.md).

Bare `/recipe` lists the genres, each with its one-line description,
and the recipes the current project already has. `/recipe <genre>`
composes or iterates a recipe through that genre. A recipe that fits
no genre stays legitimate and is composed in conversation from
`templates/recipe.md`.

## Overview

| Genre | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `presentation` | A slide-by-slide deck definition, with a plain `.pptx` from `/render` and a designed one from `/publish` | A talk or a deck for a room | `.claude/skills/recipe/genres/presentation.md`, skeleton `templates/recipe-presentation.md` |
| `readme` | The project's `README.md`, regenerated at every release | Every project carries it | `.claude/skills/recipe/genres/readme.md`, skeleton `templates/recipe-readme.md` |
| `release-notes` | One section per release in six fixed groups, derived from the records of the chain's history logs | Every thought project carries it | `.claude/skills/recipe/genres/release-notes.md`, skeleton `templates/recipe-release-notes.md` |
| `screenplay` | A teaching video of a terminal conversation cut from session records | A video, or the events of the player page | `.claude/skills/recipe/genres/screenplay.md`, skeleton `templates/recipe-screenplay.md` |
| `user-stories-export` | The user stories as an export for a wiki or a tracker, one heading per story | A thought project that has user stories | `.claude/skills/recipe/genres/user-stories-export.md`, skeleton `templates/recipe-user-stories-export.md` |

## presentation

- **Description:** compose a presentation recipe, a slide-by-slide deck
  definition, with a plain `.pptx` from `/render` and a designed one
  from `/publish`.
- **Skeleton:** `templates/recipe-presentation.md`.
- **Output:** a Markdown deck definition, source material for a
  presentation and never the presentation itself. The PowerPoint files
  are made from it in two steps, `/render` and `/publish`. What each
  step needs is stated in the recipe's Format section.
- **Role:** interviewer. Claude elicits the answers below, offers
  options and trade-offs, and the decisions are the principal's. Then
  it composes the recipe from the skeleton.

Elicitation checklist:

1. **Audience and register.** Who sits in the room, whether it is
   technical or executive, and how direct the deck is.
2. **Purpose and the one message.** What the audience must take away.
   The deck is built around it.
3. **Inputs.** Which chain artefacts feed the deck, by default the
   intent. A picture may come from another render of the project: a
   slide references it as `render: <file>`, and that render is
   declared among the inputs so that provenance and staleness track it.
4. **Dramaturgy.** The slide count, the opening and closing slides,
   whether there is an agenda slide, the section dividers and the arc
   from the first slide to the last.
5. **Speaker notes.** Whether they are wanted at all. If they are,
   whether they carry traceability citations back to the inputs.
6. **On-slide density.** The maximum of bullets and words per slide,
   and what is banished to the notes.
7. **Diagram policy.** Which slides carry a diagram, either inline
   Mermaid (valid standalone and simple enough to survive conversion
   into native slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** The terms that must not blur, defined
   terms and house distinctions. The recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience:
   internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or none.
    For the published file, which the model that designs the deck
    reads: the template, the model, the handling of overflow and the
    expectations for redrawn diagrams. How a template is named and
    which model is the default is stated in the header of
    `scripts/md2pptx.py`.

## readme

- **Description:** compose or iterate a project's readme recipe. The
  render is the project's `README.md`, regenerated at every release.
- **Skeleton:** `templates/recipe-readme.md`.
- **Output:** `README.md` in the project root.
- **Where it is owned:** every project carries this recipe, as
  `CLAUDE.md` says under Repository layout. When its render is made is
  said by `.claude/skills/release/SKILL.md`.
- **Role:** interviewer. Claude elicits the answers below, offers
  options and trade-offs, and the decisions are the principal's. Then
  it composes or iterates the recipe from the skeleton. When the
  principal asks for a first version without an interview, Claude
  drafts it from the inputs (the ledger, the brief, the essence of the
  intent) and presents it as a draft to iterate.

Elicitation checklist:

1. **Primary reader.** The recipients of the assignment, colleagues
   browsing the repository, or the principal returning. The README is
   written for the first of them.
2. **Inputs.** For a thought project: the ledger, the brief, the
   intent and the layers below it once they exist. For a library: the
   ledger and the two `00-INDEX.md` catalogues. Its README is a
   catalogue of what the library holds, with Role and Use for each
   document and how to use it, for example the path by which a deck
   template is named.
3. **What the essence must say** and how much of it: the problem, the
   direction and the recipients, on one screen and not the whole
   intent.
4. **State.** Which ledger facts appear: chain versions and statuses,
   briefs and mining state, renders, and what is waiting on the
   principal.
5. **What must not appear.** Confidentiality toward whoever can reach
   the repository, internal figures, and anything from other projects.

## release-notes

- **Description:** compose or iterate a thought project's
  release-notes recipe. It has one section per release in six fixed
  groups, derived from the records of the chain's history logs.
- **Skeleton:** `templates/recipe-release-notes.md`.
- **Output:** `RELEASE-NOTES.md` in the project root.
- **Scope:** thought projects only. A library has no intent and so no
  release notes, and its history is git.
- **Where it is owned:** every thought project carries this recipe, as
  `CLAUDE.md` says under Repository layout. When its render is made is
  said by `.claude/skills/release/SKILL.md`. The skeleton owns the
  shape.
- **Role:** interviewer, lightly, because this genre has few degrees
  of freedom.

Elicitation checklist:

1. **Which companions feed the notes.** The default is every chain
   artefact but the brief: the intent, the assignment and later layers
   as they appear. A project may narrow it.
2. **The reader.** By default the recipients tracking the project. A
   different reader changes what Action required means.

## screenplay

- **Description:** compose a screenplay recipe, a teaching video of a
  terminal conversation cut from session records. It is rendered as a
  screenplay and made into a video, or into the events of the player
  page, by a script.
- **Skeleton:** `templates/recipe-screenplay.md`.
- **Output:** a screenplay, never the video itself. It holds a title
  card, a card of what the viewer will see, scenes with the real time
  of day and an end card. Each scene has a caption of two parts (Now:
  what happens, Why: why the forge does it this way) and a fenced
  block of what the terminal shows. The caption is the teaching and
  the terminal is the evidence. The video file is made from the
  screenplay by `scripts/md2video.py`, in the format the recipe names.
  The header of the script says what it needs.
- **Inputs:** session records registered as sources (a transcript
  extract, by timestamps) and the brief that says what the videos are
  for.
- **Role:** interviewer. Claude elicits the answers below, offers
  options and trade-offs, and the decisions are the principal's. Then
  it composes the recipe from the skeleton.
- **Language question:** it is point 9 of this checklist, not a
  closing question.

Elicitation checklist:

1. **Audience and register.** Who watches, whether they have seen
   Claude Code, and how the captions speak: plain, factual, with no
   praise of the tool.
2. **Purpose and the one message.** What the viewer leaves with. The
   end card says it. Also which principle of the forge the video
   shows.
3. **Inputs.** The transcript source and the sessions in it, the brief
   of the videos, and a document the video shows being born, as a
   dependency by path.
4. **The beats.** The scenes are pinned by the time of their first
   line and by the lines that must appear, so that every render is the
   same cut. Also what is left out, such as the hours of wording and
   the saves.
5. **The quotes.** The principal's lines are shown as typed. Gross
   errors only are corrected, and what is kept is the missing
   diacritics and the speed. Some of Claude's answers are shown in
   full because the scene is about them, and the rest are cut to the
   sentences that carry the move. Tool calls appear as one dim line,
   and tool output and permission prompts do not appear at all. The
   verdict line is shown in today's form.
6. **Length.** Minutes of video, and what is shortened when there is
   too much: Claude's lines, never the principal's and never the
   captions.
7. **The title card.** The disclosure of the composition: real work,
   how many sessions, how many hours, times real, and lines verbatim
   and shortened.
8. **What must not appear.** Names, companies, hosts, and paths
   outside the forge. The facts of the instance are never material.
9. **Languages.** The language of the sessions as the primary one, and
   which translations (`languages:` in `templates/recipe.md`). The
   notation of the render stays English and the content is in the
   language of the render.
10. **Pace and look.** The three reading rates in words a second: the
    principal's lines, Claude's answers and file reports, at 4, 8 and
    16 unless the principal wants otherwise. Also the date shown in
    the tab bar and the labels of the captions by language.
11. **Format.** `video` or `html-player`, one of them and never both.
    For `html-player`, whether the file goes out to the engine's
    `docs/videos/` by `output:`, with its number for the order of the
    course, or stays in the project's `renders/` for the company. Also
    the course on the player page: the section the video belongs to
    and its name per language, and what the viewer will learn, listed
    in place of the title of the title card.

## user-stories-export

- **Description:** compose or iterate the recipe that renders a
  project's user stories as the export the instance hands over, with
  one heading per story and its parts on lines of their own, to be
  pasted into a wiki or a tracker.
- **Skeleton:** `templates/recipe-user-stories-export.md`.
- **Output:** by default `renders/user-stories-export.md`.
- **Scope:** thought projects that have `35-user-stories.md`. The
  export is a render and never the artefact.
- **Shape:** the skeleton owns the shape of the export. It has no
  table, because a Markdown table cannot break a line inside a cell
  and a paste into a wiki or a tracker would run a story into one
  paragraph. A recipe keeps the shape and changes only what the
  elicitation below opens.
- **Role:** interviewer, lightly, because this genre has few degrees
  of freedom.
- **Labels:** the labels of a story stay in English whatever the
  language.

Elicitation checklist:

1. **The input.** `35-user-stories.md` by default, or a work product
   in `work/` where the stories were made from a source.
2. **The section heading and the purpose line.** The skeleton holds
   placeholders for the second heading and the sentence under it.
   They are filled with the words of the export the instance hands
   over, as the principal gives them, in the language of the render.

## The shared closing

Every genre closes in the same way, except that the screenplay genre
asks the language question as point 9.

- **The language question.** The checklist closes with the language of
  the render, or the languages where the genre allows them
  (`languages:` in `templates/recipe.md`). Claude proposes the
  project's language from its project file (`project.md`) and asks. It
  never assumes.
- **The composition.** The recipe is then composed from the skeleton
  of the genre. Unused placeholders and the comments of the template
  are deleted, but the line that names the skeleton stays.
- **The write.** The recipe is composed with the principal, who
  decides. It is written once per round, on confirmation, with a
  version and no status. Its history goes into
  `recipes/<recipe>.history.md`, created from `templates/history.md`
  with the recipe.
- **The next step.** After the write, Claude offers `/render <recipe>`.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing through a genre.
- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the screenplay genre from recipe to played file.
- [Write user stories](../use/write-user-stories.md): the stories the export genre renders.
- [Add a recipe genre](../extend/add-a-recipe-genre.md): adding a genre.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
