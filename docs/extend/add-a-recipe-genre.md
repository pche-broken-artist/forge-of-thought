---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: e8c9d4f62c6ac756
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
---

# Add a recipe genre

A recipe genre is one kind of render that `/recipe` can compose a
recipe for by interview. You add one as two files: a genre
definition and a template of the recipe. This page is for the
extender who wants a new genre beside the ones that exist. A
recipe is the versioned file that says how a render is made; what
it is, is said in [Renders and recipes](../about/renders-and-recipes.md).
The genres that exist are listed in [Recipe genres](../reference/recipe-genres.md).

## Before you start

How a change to the forge is proven, recorded and released is said
in [Make a change to the forge](how-a-change-is-made.md). A new
genre is recorded and released as any change of the forge.

Every genre runs in the same frame, which `/recipe` supplies:

- The genre's checklist closes with the language question. The
  render's language, or languages where the genre allows a primary
  and its translations, is what the recipe declares. Claude
  proposes the project's language from its project file and asks
  the principal (the person whose thinking is forged), never
  assuming it.
- The recipe is then composed from the genre's template, with the
  unused placeholders and all template comments deleted.
- The recipe is written once per round on the principal's
  confirmation, with a history companion beside it.

Your genre file does not repeat this frame. It only points at it.

The `/recipe` command itself never changes when a genre is added.
Bare `/recipe` lists the genre directory, each genre with its
one-line description, so the new genre appears there by its file
alone.

## The files

- `.claude/skills/recipe/genres/<genre>.md`: the genre definition.
  It carries the one-line description, names the template, says
  what the render is, gives Claude its role and holds the numbered
  elicitation checklist.
- `templates/recipe-<genre>.md`: the template of the recipe. It
  extends the base shape of `templates/recipe.md`.

## Steps

1. Write the genre definition at
   `.claude/skills/recipe/genres/<genre>.md`, in the shape of
   `.claude/skills/recipe/genres/presentation.md`:
   - front-matter with a `description:` of one line, which is what
     bare `/recipe` shows;
   - a line naming the genre and its template, such as
     `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`;
   - a paragraph on what the render of such a recipe is, and where a
     file is made from it, which step makes it;
   - the role Claude takes, an interviewer that offers options and
     trade-offs while the decisions stay the principal's;
   - the numbered elicitation checklist, one question per item,
     written for your genre;
   - a closing line saying that the language question and the
     composition from the template close every genre.

   Arguments given after the genre name on the command line are the
   genre file's own.

   You should now see the file in `.claude/skills/recipe/genres/`
   beside the existing genres.

2. Write the template at `templates/recipe-<genre>.md`, in the shape
   of `templates/recipe-presentation.md`. Keep the base shape of
   `templates/recipe.md`:
   - front-matter with `project`, `purpose`, `audience` and
     `version: 0.1`, and the optional `output:` line;
   - `## Inputs`, the artefacts the render is generated from, by
     path;
   - `## Instructions`, everything the renderer must know beyond the
     template, filled in with placeholders for your genre;
   - `## Template`, the literal skeleton of the render, always
     Markdown.

   Add `## Format` where the render has a file beside it (a
   PowerPoint file, a Word file, a video or a player). A recipe
   without that section ends at the Markdown. Add the optional
   `languages:` line to the front-matter where the genre allows
   translations: the first language is primary, the rest are its
   translations, one render per language.

   You should now see the template in `templates/` under the name
   the genre definition gives for it.

## Prove it

Type bare `/recipe` and see the new genre in the roster with its
one-line description:

```
/recipe
```

Then compose one recipe through it on a project:

```
/recipe <genre> <slug>
```

The interview runs your checklist, closes with the language
question and composes the recipe from your template. The general
proofs of a change are on [Make a change to the forge](how-a-change-is-made.md).

## Record and release

The two files are recorded and released as any change of the forge,
as [Make a change to the forge](how-a-change-is-made.md) says.

## A worked example

A genre `<genre>` whose render is a Markdown document only, with no
file beside it and one language. The genre definition:

```markdown
---
description: Compose a <genre> recipe: <what the render is, in one line>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>.

Role: interviewer. Elicit the answers below from the principal,
options and trade-offs offered, decisions his (`/recipe`, step 2),
then compose the recipe from the skeleton.

Elicitation checklist:
1. **<First question>.** <What it asks.>
2. **<Second question>.** <What it asks.>

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

The template:

```markdown
---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
---

# Recipe: <name>

## Inputs
- 10-intent.md

## Instructions
- Audience: <audience>. Register: <register>.
- <What the renderer must know for this genre.>

## Template
<The literal skeleton of the render, with placeholders.>
```

Had the render a file beside it, the template would carry a
`## Format` section. Had the genre allowed translations, its
front-matter would carry `languages:`.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a
  recipe is.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
