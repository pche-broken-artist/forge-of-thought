---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: a410ebe921649e9d
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
---

# Add a recipe genre

A recipe genre is one kind of render recipe that `/recipe` can
compose by interview: a definition that carries the questions to ask
and a skeleton the recipe is composed from. This page is for the
extender who wants a genre the forge does not have yet. It says which
two files make a genre, what each holds, and how the addition is
proved, recorded and released. What a recipe is and how a render is
made from it is said on [Renders and recipes](../about/renders-and-recipes.md);
the genres that exist are listed on
[Recipe genres](../reference/recipe-genres.md); every term of the
forge is in the [Glossary](../reference/glossary.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md): a genre
is a change of the forge like any other, and it is recorded and
released by the steps that page gives.

Two facts set the frame of the work.

- A genre is two files and nothing else. The command `/recipe` is a
  dispatcher: it resolves the genre file by name and follows it. The
  dispatcher, `.claude/skills/recipe/SKILL.md`, never changes when a
  genre is added.
- A recipe outside any genre stays legitimate. Claude composes it in
  conversation with the principal (the person whose thinking is
  forged, who decides every content question) from the base
  skeleton `templates/recipe.md`. A genre is therefore not needed
  for a recipe that is made once. The inputs record no rule on when
  a kind of render deserves a genre of its own; that judgement is
  yours.

Every genre runs in the same frame, and the frame is the
dispatcher's, not the genre's:

- The checklist of the genre closes with the language question. The
  render's language, or its languages where the genre allows a
  primary and its translations, is what the recipe declares. Claude
  proposes the project's language from its ledger header and asks;
  it never assumes.
- The recipe is then composed from the genre's skeleton, with unused
  placeholders and all template comments deleted.
- The recipe is composed with the principal: options and trade-offs
  are offered, the decisions are his. It is written once per round,
  on confirmation, with a version and an updated date and no status,
  and its history companion `recipes/<recipe>.history.md` is created
  from `templates/history.md` with it.
- After the write, Claude offers `/render <recipe>` as the next step.

A genre file states none of this; it relies on it.

## The files

| File | What it is |
|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the definition: one line of description, the skeleton and the product named, the role, the numbered elicitation checklist |
| `templates/recipe-<genre>.md` | the skeleton: the base recipe shape with what the genre fixes filled in and what the interview decides left as placeholders |

### The definition

The definition is a short Markdown file in this shape, modelled on
`.claude/skills/recipe/genres/presentation.md`:

- Front-matter with one key, `description:`, in one line. Bare
  `/recipe` lists the directory `.claude/skills/recipe/genres/` and
  prints this line for each genre; it is how the genre appears in
  the roster.
- An opening line that names the genre and its skeleton:
  `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`
- A paragraph on the product: what the render of this genre is, and
  what it is not. Where the render has a file beside it, the
  paragraph says that the file is made from the render in the two
  steps of `/render` and `/publish` and that what each step needs is
  in the recipe's Format section.
- The role: Claude is the interviewer. It elicits the answers of the
  checklist from the principal, offers options and trade-offs,
  leaves the decisions to him, and then composes the recipe from the
  skeleton.
- The elicitation checklist, numbered. Each item is one question the
  recipe must have answered, in bold, followed by the alternatives
  the principal chooses between. The items are the genre's own; they
  are what makes one genre differ from another. Where the render has
  a file beside it, one item asks for the format and for what each
  of the two steps needs: these are the placeholders of the
  skeleton's Format section.
- A closing line that says the language question and the composition
  from the skeleton close every genre, as the dispatcher's step 2
  has it.

The arguments of a genre file are those that follow the genre name on
the command line.

### The skeleton

The skeleton extends the base recipe shape, `templates/recipe.md`.
The base owns these parts:

- Front-matter: `project`, `purpose`, `audience`, `version: 0.1`,
  `updated`, `last_change` (derived from the records of the newest
  version in the history companion, never written by hand), and two
  optional, commented keys: `output:` to override the default
  `renders/<recipe>.md`, and `languages:`.
- The title line `# Recipe — <purpose>`.
- `## Inputs`: the artefacts the render is generated from, by path,
  one per line; more than one is legitimate.
- `## Instructions`: audience, tone, what to emphasise, what to omit,
  target length, register; everything the renderer must know beyond
  the template.
- `## Format`, optional: a recipe without it ends at the Markdown.
  It names the format (`pptx`, `docx`, `video` or `html-player`),
  the plain file made by `/render` through pandoc with its reference
  and page size, and the published file made by `/publish` through a
  model with its template, model and anything else the model must
  know. A screenplay's `video` or `html-player` is made through
  `scripts/md2video.py` instead and has no published file. The
  section is never copied into the render.
- `## Template`: the literal skeleton of the render, with
  placeholders, always Markdown.

A genre's skeleton keeps every part of the base and fills in what the
genre fixes:

- The `purpose` line and the title carry the genre's wording with a
  placeholder for the one recipe.
- `## Instructions` carries the lines every recipe of this genre
  needs, each with a placeholder where the interview decides, so that
  the answers of the checklist have a place to land. The presentation
  skeleton, for instance, carries a line for the audience and
  register, one for the one message, one for the density of a slide,
  one for the vocabulary that must not blur, one for what must not
  appear, and the per-item format of the render.
- `## Format` is present where the render has a file beside it, with
  the format fixed and the rest as placeholders. The presentation
  skeleton fixes `Format: pptx` and leaves the reference of the plain
  file and the template and model of the published file open. A
  genre whose render ends at the Markdown leaves the section out.
- `languages:` stays in the front-matter where the genre allows a
  primary language and its translations. The base skeleton carries it
  as an optional line: the first language is the primary, the rest
  are its translations, and the render is one file per language,
  `renders/<recipe>.<lang>.md`. The presentation skeleton carries no
  `languages:` line. The inputs record no reason for that choice.
- `## Template` carries the shape of the render of this genre, with
  placeholders; the presentation skeleton gives a table of slides.

The comments of the base skeleton may stay in the genre's skeleton as
guidance for the composer. The composition deletes them from the
recipe.

## Steps

1. Write the definition `.claude/skills/recipe/genres/<genre>.md`
   in the shape above. Give it the one-line `description:` first:
   it is what the roster shows.
2. Write the skeleton `templates/recipe-<genre>.md`, starting from a
   copy of `templates/recipe.md`. Fix what the genre fixes, leave as
   a placeholder what the interview decides, drop `## Format` if the
   render ends at the Markdown, keep or drop `languages:` as the
   genre allows translations or not.
3. Make sure every item of the checklist has a place in the skeleton
   and every placeholder of the skeleton has an item in the
   checklist. The dispatcher composes the recipe from the skeleton
   with the checklist's answers; an answer without a place is lost,
   and a placeholder without a question stays unanswered.
4. Change nothing else. The dispatcher scans the directory; it is not
   told about the genre.

## Prove it

Run the check of the engine:

```
/check engine
```

Then compose one recipe of the new genre on a project, with the slug
of a project of yours in place of `<slug>`:

```
/recipe <genre> <slug>
```

What you should see, in order:

- Claude resolves `.claude/skills/recipe/genres/<genre>.md` and asks
  the questions of your checklist, offering the alternatives each
  item gives.
- The last question is the language question: Claude proposes the
  project's language from its ledger header and asks.
- Claude composes the recipe from your skeleton, with unused
  placeholders and template comments deleted, reflects it back and
  writes it on your confirmation to `recipes/<recipe>.md`, with
  `recipes/<recipe>.history.md` beside it.
- Claude offers `/render <recipe>`.

Two further signs that the genre is in place:

- Bare `/recipe` lists the new genre with its `description:` line
  among the others.
- `/recipe <name>` for a name that is neither a genre nor a recipe
  of the project lists the genres that do exist and stops; the new
  genre is in that list.

## Record and release

The two files are recorded and released as any change of the forge.
The steps are on [Make a change to the forge](how-a-change-is-made.md).

## A worked example

The genre is `<genre>` throughout; the project is `<slug>`.

The definition, `.claude/skills/recipe/genres/<genre>.md`:

```
---
description: Compose a <genre> recipe — <what the render is, in one line>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>, never
<what it is not>. <Where a file is made beside it: the file is made
from the render in the two steps of /render and /publish; what each
step needs is the recipe's Format section.>

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his (`/recipe`, step 2) —
then compose the recipe from the skeleton.

Elicitation checklist:
1. **<The first thing the recipe must know.>** <The alternatives.>
2. **<The second.>** <The alternatives.>
3. **Inputs.** <Which artefacts feed the render; the default.>
<...>
N. **Format.** <Where the render has a file beside it: the format,
   and what the plain and the published file each need.>

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

The skeleton, `templates/recipe-<genre>.md`:

```
---
project: <slug>
purpose: <The genre's purpose line> for <the one recipe>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/<recipe>.history.md>
# output: <path>   # optional — overrides the default renders/<recipe>.md
# languages: <cs, en>   # keep only where the genre allows a primary and its translations
---

# Recipe — <the one recipe>

## Inputs
- 10-intent.md

## Instructions
- <One line per item of the checklist, with a placeholder where the
  interview decides.>
- Audience: <audience>. Register: <register>. Language: <language>.
- Must not appear: <what this audience must not see>.

## Format
- Format: <pptx | docx | video | html-player>
- Plain file, made by `/render` through pandoc: reference
  <path | none>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must know>.

## Template
<The literal shape of the render, with placeholders.>
```

The run:

```
/recipe <genre> <slug>
```

Claude asks the N questions of the checklist, then the language
question, proposing the language of the project's ledger header. On
your confirmation it writes `projects/<slug>/recipes/<recipe>.md` at
version 0.1 with the day's date, creates
`projects/<slug>/recipes/<recipe>.history.md` from
`templates/history.md`, and offers `/render <recipe>`.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a recipe is.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
