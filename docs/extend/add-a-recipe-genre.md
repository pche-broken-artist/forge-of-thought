---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 403e30495efd7bb8
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
---

# Add a recipe genre

A recipe genre is one kind of render that `/recipe` can compose
through a guided interview, such as a presentation. A render is an
output generated for one audience, and its recipe is the versioned
file that says how it is made (see
[Renders and recipes](../about/renders-and-recipes.md)). This page
is for an extender who wants `/recipe` to offer a new genre. It
shows the two files a genre consists of, how to write them and how
to prove that the new genre works.

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md): it
  says how a change is proved, recorded and released.
- A new genre is recorded and released as any change of the forge.
- Look at [Recipe genres](../reference/recipe-genres.md) for the
  genres that exist, so that the new one does not duplicate one.
- The terms used here are each explained in one line in the
  [Glossary](../reference/glossary.md).

## The files

A genre is exactly two files:

- `.claude/skills/recipe/genres/<genre>.md`: the genre definition.
  It tells Claude how to interview the principal (the person whose
  thinking is forged) and which skeleton to compose the recipe from.
- `templates/recipe-<genre>.md`: the skeleton of a recipe of this
  genre. It extends the base recipe shape that `templates/recipe.md`
  owns.

Nothing else changes. The `/recipe` command itself (its dispatcher,
`.claude/skills/recipe/SKILL.md`) never changes when a genre is
added. Bare `/recipe` lists the `genres/` directory and shows each
genre with its one-line description, so the new file appears there
by being present.

## Steps

1. **Write the genre definition** in
   `.claude/skills/recipe/genres/<genre>.md`, in the shape the
   presentation genre (`.claude/skills/recipe/genres/presentation.md`)
   models:
   - front-matter with a `description:`: one line saying what recipe
     the genre composes. This is the line bare `/recipe` shows.
   - a first line naming the genre and its skeleton, in the form
     `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`
   - a paragraph on the product: what the render of such a recipe
     is, and which files are made from it where there are any.
   - the role Claude takes, for example interviewer: it elicits the
     answers from the principal, offers options and trade-offs, and
     leaves the decisions to him.
   - a numbered elicitation checklist: the questions this kind of
     render needs answered. They are the genre's own and are written
     for it, not copied from another genre.
   - a closing line saying that the language question and the
     composition from the skeleton close every genre, as `/recipe`
     step 2 says.

   You should now see the new genre, with its description, when you
   run bare `/recipe`.

2. **Leave the shared frame out of the checklist.** Every genre runs
   in the same frame, and `/recipe` supplies it:
   - the checklist closes with the language question. The language
     of the render, or its languages where the genre allows a
     primary language and its translations, is what the recipe
     declares. Claude proposes the project's language from the
     project file (`project.md`) and asks.
   - the recipe is then composed from the genre's skeleton, with
     unused placeholders and all template comments deleted.
   - the recipe is written once per round on the principal's
     confirmation, with its history companion beside it.

   The genre definition therefore does not repeat these steps; it
   only points to them in its closing line.

   You should now see a checklist that holds only the questions
   particular to the genre.

3. **Write the skeleton** in `templates/recipe-<genre>.md`. Start
   from the base shape of `templates/recipe.md` and keep its parts:
   - front-matter with `project`, `purpose`, `audience` and
     `version: 0.1`, and the optional `output:` line.
   - `## Inputs`: the artefacts the render is generated from, by
     path.
   - `## Instructions`: what the renderer must know beyond the
     template, filled with the placeholders the checklist answers.
   - `## Template`: the literal skeleton of the render, always
     Markdown.

   Add the two optional parts where the genre needs them:
   - a `## Format` section where the render has a file beside the
     Markdown (such as a `pptx` or a `docx`). It names the format,
     what the plain file made by `/render` needs, and what the
     published file made by `/publish` through a model needs. A
     recipe without this section ends at the Markdown.
   - a `languages:` line in the front-matter where the genre allows
     translations: the first language is primary, the rest are its
     translations, one render per language.

   You should now see a skeleton whose placeholders match the
   questions of your checklist.

## Prove it

Run the engine check:

```
/check engine
```

Then compose one recipe through the new genre on a project:

```
/recipe <genre> <slug>
```

You should now see the interview run through your checklist, close
with the language question, and end with a recipe composed from your
skeleton, offered to be rendered with `/render <recipe>`.

## Record and release

Record and release the two new files as any change of the forge, in
the way [Make a change to the forge](how-a-change-is-made.md)
describes.

## A worked example

A genre named `<genre>` whose render is a Word document, with
translations allowed.

`.claude/skills/recipe/genres/<genre>.md`:

```
---
description: Compose a <genre> recipe - <what the render is>, with a plain .docx from /render
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>.
The Word files are made from it in the two steps of /render and
/publish; what each step needs is the recipe's Format section.

Role: interviewer. Elicit the answers below from the principal -
options and trade-offs offered, decisions his (`/recipe`, step 2) -
then compose the recipe from the skeleton.

Elicitation checklist:
1. **<first question>.** <what it settles>.
2. **<second question>.** <what it settles>.
3. **Format.** <the format and what each step needs>.

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

`templates/recipe-<genre>.md`:

```
---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
# output: <path>
# languages: <primary, translation>
---

# Recipe - <name>

## Inputs
- 10-intent.md

## Instructions
- Audience: <audience>. Register: <register>.
- <one line per answer of the checklist>

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference
  <path | none>, page size <A4 | Letter>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must know>.

## Template
<the literal skeleton of the render, with placeholders>
```

With both files in place, bare `/recipe` lists `<genre>`, and
`/recipe <genre> <slug>` composes a recipe from them.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a
  recipe is.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
