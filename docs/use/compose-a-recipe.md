---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 43d4908167c22e7a
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe.md
---

# Compose a recipe

This page shows how to compose a render recipe, or iterate one that exists, with `/recipe`. A recipe is the versioned file that says what a render is made from, for whom and in what shape. It is written for the principal (the person whose thinking is being forged), who decides what the recipe says while Claude asks the questions and writes the file.

## When to use it

Use `/recipe` when you want a new render of your project, such as a deck, a README, release notes or a teaching video. Use it again when a render is not what you wanted: you change the recipe, never the render. The reason is given in [Renders and recipes](../about/renders-and-recipes.md).

Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## The command

```
/recipe presentation my-project
```

The command takes two optional arguments:

- `genre`: the kind of render to compose, or the name of an existing recipe to iterate.
- `slug`: the project. When you leave it out, Claude infers the project from the conversation and asks only if that is ambiguous.

Bare `/recipe` composes nothing. It reports the roster.

## What happens

1. Run bare `/recipe` to see what is available. Claude lists the genres, each with a one-line description, and the recipes your project already has with their versions. Where the conversation suggests a fit, it recommends one.

   You should now see the genres and your project's recipes, with a recommendation where one fits.

2. Run `/recipe <genre>` with one of the genres. Claude reads the genre's definition and interviews you through its checklist. It offers options and trade-offs, and the decisions are yours.

   You should now see questions one topic at a time, each with options where there are any.

3. Answer the last question, which is always the language. The render is in one language, or in several where the genre allows a primary language and translations made from it. Claude proposes the project's language, read from its project file, and asks. It never assumes.

   You should now see the language proposed and a question waiting for your answer.

4. Confirm the write. Claude composes the recipe from the genre's skeleton (the template that fixes the recipe's shape), deletes the placeholders and comments that are not used, and writes the file once, when you confirm.

   You should now see the recipe in the project's `recipes/` folder and its history file beside it.

5. Take the offer of `/render <recipe>`, which Claude makes as the natural next step. Generating the render is described in [Render an output](render-an-output.md).

   You should now see Claude offering `/render` for the recipe you wrote.

## The genres of today

- `presentation`: a slide-by-slide deck definition, from which a plain PowerPoint file and a designed one are made.
- `readme`: the project's README, regenerated at every release.
- `release-notes`: one section per release, derived from the history of the chain's documents.
- `screenplay`: a teaching video cut from session records, made into a video file or into the events of the player page. The whole path is in [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

Each genre's checklist is set out in full in [Recipe genres](../reference/recipe-genres.md).

## Other cases

- To iterate a recipe that exists, give its name in place of a genre: `/recipe my-deck my-project`. Claude iterates it through its genre when one fits, and conversationally otherwise.
- A recipe that fits no genre is legitimate. Claude composes it conversationally from the base skeleton, which has a front matter, the sections Inputs and Instructions, an optional Format section for a recipe that is to end in a file, and the Template.

## What you have afterwards

- A recipe in `recipes/`, with a version that starts at 0.1.
- A history file, `recipes/<recipe>.history.md`, created with the recipe.

A recipe stays at a 0.x version for life and carries no status. It is iterated, never approved, and every change you confirm becomes one version.

## If something goes wrong

- If the name you gave is neither a genre nor an existing recipe of the project, Claude lists the genres that exist and stops. Run the command again with one of them.
- If the project cannot be inferred, Claude asks for the slug.

## A worked example

You want a deck for the colleagues who will review the project, and the project is `my-project`.

1. You type `/recipe presentation my-project`.
2. Claude asks about the audience, the one message the deck must carry, the inputs, the arc of the slides and what must not appear. You answer; where you are unsure, Claude lays out options and recommends one.
3. Claude asks which language the deck is in. It proposes the project's language, and you confirm it or name another.
4. Claude shows the recipe it has composed. You confirm, and it writes `recipes/my-deck.md` at version 0.1 with its history file beside it.
5. Claude offers `/render my-deck`. You accept, and the deck definition appears in `renders/`.

If the deck is wrong, you do not edit the render. You run `/recipe my-deck my-project`, change the answer that caused it, confirm, and render again.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
