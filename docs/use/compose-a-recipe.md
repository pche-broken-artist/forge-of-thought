---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 2f269dac720a2776
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

This page shows how you compose a new render recipe, or iterate an
existing one, with `/recipe`. A recipe is the versioned file that says
how one render is made: its inputs, its audience, its instructions and
the template of its output. It is written for the principal, the person
whose thinking is forged and who decides every choice in the
composition.

## When to use it

Use it when you want a new output made from your project, such as a
deck, a README or a video script. Use it as well when an existing
recipe needs to change. The render is never edited by hand; the recipe
is what you iterate (see [Renders and recipes](../about/renders-and-recipes.md)).

## The command

```
/recipe [genre] [slug]
```

The genre and the project slug are both optional. The forms are:

- `/recipe` alone lists the genres and the project's existing recipes.
- `/recipe <genre>` composes a recipe through that genre.
- `/recipe <recipe-name>` iterates the existing recipe of that name.

The genres of today are:

- `presentation`: a slide-by-slide deck definition, with a plain file
  from `/render` and a designed one from `/publish`.
- `readme`: the project's README, regenerated at every release.
- `release-notes`: one section per release, derived from the history
  logs of the chain.
- `screenplay`: a teaching video of a terminal conversation, made into
  a video or into the events of a player page.
- `user-stories-export`: the project's user stories as an export, one
  heading per story, ready to paste into a wiki or a tracker.

The checklist of each genre is on [Recipe genres](../reference/recipe-genres.md).

## What happens

1. Bare `/recipe` reports the roster. Claude lists each genre with its
   one-line description, then lists the recipes already in the
   project's `recipes/` folder with their versions, and recommends a
   fit where the conversation suggests one.

   You should now see the genres and your project's recipes with
   their versions.

2. With a genre, Claude reads that genre's definition and walks you
   through its checklist. It offers options and trade-offs; the
   decisions are yours.

   You should now see Claude asking the checklist's questions, one
   at a time.

3. The checklist closes with the language question. The render has
   one language, or, where the genre allows it, a primary language
   and its translations, one render per language. Claude proposes the
   language of your project from its project file and asks. It never
   assumes.

   You should now see Claude naming your project's language and
   asking whether the render follows it.

4. Claude composes the recipe from the genre's skeleton. Unused
   placeholders and all template comments are deleted. The recipe is
   written once per round, when you confirm.

   You should now see Claude asking whether to write the recipe.

5. With the name of an existing recipe, Claude iterates that recipe
   instead, through its genre where one fits and otherwise as a
   conversation.

   You should now see Claude working from the recipe as it stands.

6. After the write, Claude offers `/render <recipe>` as the next step.
   Generating the render is on [Render an output](render-an-output.md).

   You should now see the offer of `/render` with your recipe's name.

A recipe that fits no genre is still legitimate. Claude composes it in
conversation from the base recipe template, which has four sections:
the inputs, the instructions, an optional format and the template of
the output. The format section exists only where the recipe names a
file format beyond the Markdown.

## What you have afterwards

- The recipe in the project's `recipes/` folder.
- Its history companion beside it, the append-only file that records
  each change of the recipe, created together with the recipe.
- A version of 0.x. A recipe stays 0.x and moves to an integer only
  where you name one. Claude never proposes it.

## If something goes wrong

- A name that is neither a genre nor an existing recipe: Claude lists
  the genres that exist and stops. Check the spelling, or choose from
  the list.
- A slug that is ambiguous: Claude asks which project is meant.

## Genres with their own page

- The screenplay genre is followed from recipe to played video on
  [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).
- The stories the export genre renders are written as described on
  [Write user stories](write-user-stories.md).

## A worked example

You want a deck from the project `my-project`.

1. You type `/recipe presentation my-project`.
2. Claude asks the checklist's questions about the deck. You answer
   them, and Claude reflects back what it understood.
3. Claude asks for the render's language. It proposes the language of
   `my-project` from its project file. You confirm it, and you
   decline a translation.
4. Claude shows the composed recipe and asks whether to write. You say
   write.
5. Claude writes `recipes/<recipe>.md` at version 0.1 with its history
   companion, and offers `/render <recipe>`.

You should now see the new recipe and its history companion in the
`recipes/` folder of `my-project`.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Write user stories](write-user-stories.md): the stories the export genre renders.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
