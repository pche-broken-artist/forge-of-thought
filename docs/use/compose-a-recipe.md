---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 3f22f42804d45ec3
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe.md
  - CLAUDE.md#Versioning & status
---

# Compose a recipe

`/recipe` is the command that composes or iterates a render recipe, the file that says how one audience-specific output is made. It is for you when you want a new render, or want to change how an existing one is made. You are the principal, the person whose thinking is being forged, and Claude interviews you and writes the recipe with you.

## When to use it

- You want a new render, such as a deck, a README or a teaching video, and no recipe for it exists yet.
- A render comes out wrong and you want to change its recipe. The render is never edited by hand; the recipe is what you iterate, as [Renders and recipes](../about/renders-and-recipes.md) explains.
- You are not sure which kinds of recipe exist. Run the command bare.

## The command

```
/recipe [genre-or-recipe] [slug]
```

Typed as it stands, for a presentation recipe in a project:

```
/recipe presentation my-project
```

The slug names the project. When it is left out, Claude infers the project from the conversation and asks if that is ambiguous.

The first argument takes one of three forms:

- Nothing. Claude prints the roster of genres, each with its one-line description, and the recipes the project already has, with their versions.
- The name of a genre. Claude guides a composition through that genre.
- The name of an existing recipe of the project. Claude iterates it, through its genre where one fits, otherwise in conversation.

If the name is neither a genre nor an existing recipe, Claude lists the genres and stops.

## The genres

A genre is a definition of one kind of recipe: a checklist of questions and a skeleton to compose from. Today there are four:

- `presentation`: a slide-by-slide deck definition, with a plain PowerPoint file from `/render` and a designed one from `/publish`.
- `readme`: a project's README, regenerated at every release.
- `release-notes`: a thought project's release notes, one section per release in six fixed groups.
- `screenplay`: a teaching video of a terminal conversation cut from session records.

Each genre's checklist is in [Recipe genres](../reference/recipe-genres.md). A recipe that fits no genre is legitimate. Claude then composes it in conversation from the base skeleton for recipes.

## What happens

1. Claude finds the genre and reads its checklist. You should now see Claude put the first question of the genre to you.
2. Claude asks the questions one after another. It offers options and trade-offs, and the decisions are yours. You should now see your answers reflected back before anything is written.
3. The last question of every genre is the language. A render has one language, or several where the genre allows a primary and its translations. Claude proposes the language of the project, taken from its project file, and asks. It never assumes. You should now see the language you chose named in what Claude is about to write.
4. Claude composes the recipe from the genre's skeleton, with unused placeholders and template comments deleted. It writes once per round, when you confirm. You should now see the recipe file named, and its history companion beside it.
5. Claude offers `/render <recipe>` as the next step. You should now see that offer, which you may take or leave.

For an existing recipe the steps are the same, with the questions limited to what you want to change.

## What you have afterwards

- `recipes/<recipe>.md` in the project: the recipe, with its inputs, its instructions and the template of its render. A recipe may also carry a Format section, for the genres that make a file beyond the Markdown.
- `recipes/<recipe>.history.md`: its history companion, created with the recipe from the history template.
- A version of `0.x`. A recipe carries a version and no status. It stays at `0.x` unless you name an integer, and Claude never proposes one.

To generate the output, go on to [Render an output](render-an-output.md). For the screenplay genre, [Make a teaching video from a recipe](make-a-video-from-a-recipe.md) follows the recipe through to the played video.

## If something goes wrong

- The name you gave is neither a genre nor a recipe of the project. Claude lists the genres that exist and stops. Run `/recipe` bare and pick from the roster.
- The slug is ambiguous. Claude asks which project you mean.

## A worked example

You want a deck for a group of colleagues, and the project is called `my-project`.

```
/recipe presentation my-project
```

Claude asks who will sit in the room, what they must take away and which documents of the project feed the deck. It asks the remaining questions of the genre in the same way, and offers choices where there are any. Last it asks for the language of the deck and proposes the language of `my-project`. You confirm. Claude writes `recipes/presentation.md` at version `0.1` with `recipes/presentation.history.md` beside it, and offers `/render presentation`.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
