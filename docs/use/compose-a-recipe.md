---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 2ddd11d52fbf5001
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - templates/recipe.md
  - CLAUDE.md#Versioning & status
---

# Compose a recipe

This page shows how to compose or iterate a render recipe with `/recipe`. A recipe is the one versioned file that says what a render is made from, for whom and in what shape. It is written for the principal (the person whose thinking is being forged) who wants a new render or a change to an existing one.

## When to use it

- You want a new render of the project, such as a deck, a README or a screenplay, and no recipe for it exists yet.
- You want to change a render. You change its recipe and never the render, which is overwritten at every run (see [Renders and recipes](../about/renders-and-recipes.md)).
- You do not know which genres exist or which recipes the project already has.

## The command

```
/recipe presentation <slug>
```

The command takes `/recipe [genre] [slug]`. The slug names the project and may be left out where the conversation makes it clear. Replace `presentation` with another genre, or with the name of an existing recipe.

- Bare `/recipe` lists the genres, each with a line on what it is for, and the project's existing recipes with their versions. Claude recommends a fit where the conversation suggests one.
- `/recipe <genre>` starts a guided composition through that genre.
- `/recipe <recipe-name>` iterates an existing recipe, through its genre where one fits and otherwise in conversation.
- If the name is neither a genre nor an existing recipe, Claude lists the genres and stops.

## The genres of today

- presentation: a slide-by-slide deck definition, from which a plain and a designed PowerPoint file are made.
- readme: the project's README, regenerated at every release.
- release-notes: the release notes of a thought project, one section per release.
- screenplay: a teaching video cut from session records, rendered as a screenplay.
- user-stories-export: the project's user stories as an export to paste elsewhere, one heading per story.

Each genre has its own checklist of questions. The checklists are in [Recipe genres](../reference/recipe-genres.md). A recipe that fits no genre is legitimate: Claude composes it in conversation from the base recipe skeleton.

## What happens

1. Claude reads the genre's definition and interviews you through its checklist. It offers options and trade-offs, and the decisions are yours. You should now see Claude asking one question after another about audience, inputs and what must not appear.
2. The checklist closes with the language question. You name one language, or several where the genre allows a primary and its translations, one render per language. Claude proposes the project's language from its project file and never assumes it. You should now see a proposed language that you confirm or change.
3. Claude composes the recipe from the genre's skeleton and deletes unused placeholders and template comments. You should now see the draft recipe laid out for your judgement.
4. On your confirmation Claude writes the recipe once for the round, together with its history companion, which it creates with the recipe. You should now see the recipe file and its history file named.
5. Claude offers `/render <recipe>` as the next step. See [Render an output](render-an-output.md).

An iteration runs the same way, with one write for the whole round.

## What you have afterwards

- `recipes/<recipe>.md`: the recipe, with the inputs, the instructions and the template of the render. It may also carry a Format section where the render becomes a file such as a deck.
- `recipes/<recipe>.history.md`: the record of its changes.
- A version that starts at 0.x and stays there. An integer version exists only where you name one, and Claude never proposes it. A recipe carries a version and no status.

## If something goes wrong

- The name you gave is neither a genre nor a recipe of the project: Claude lists the genres that exist and stops. Start again with a genre from the list, or compose a recipe outside any genre.
- The project is ambiguous: Claude asks which project is meant.

## A worked example

You want a short deck for a team of colleagues from the intent of a project called `<slug>`.

```
/recipe presentation <slug>
```

Claude asks who sits in the room, what they must take away, which artefacts feed the deck, how many slides it has and what must not appear. You answer, and Claude asks for the language of the deck, proposing the project's own. You confirm. Claude shows the draft recipe, and you say to write it. Claude writes `recipes/<recipe>.md` at version 0.1 with its history file and offers `/render <recipe>`. Later you run `/recipe <recipe>` to change the density of the slides, and Claude records the change in the history.

For the genre that ends in a video see [Make a teaching video from a recipe](make-a-video-from-a-recipe.md). For the stories the export genre renders see [Write user stories](write-user-stories.md). Terms of the forge are in the [Glossary](../reference/glossary.md).

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Write user stories](write-user-stories.md): the stories the export genre renders.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
