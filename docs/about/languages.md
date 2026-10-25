---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: e7772e671ad9f526
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The language rule of the forge says which language each kind of
document of a project is written in. The forge dictates one thing
only: that a project has one output language. This page is for the
user who runs a project and for the evaluator who wants to
understand how the forge handles language. It explains what is
written in which language, how that is decided and why.

## What it is

The principal is the person whose thinking is forged. Claude is the
machine that works with the principal. A project of the forge holds
documents of several kinds, and each kind carries a language by
rule:

- The artefacts of the chain (the intent, an assignment and every
  later layer): the language the project file declares.
- The briefs (`00-brief*.md`): whatever language they are written
  in.
- The records, the state, the research and the recipes: always
  English.
- A work specification: the language of the artefacts.
- The file of a work product: the language the `## Making` section
  of its specification says.
- A render: any language, or languages, its recipe declares.

English is also the notation throughout. That covers the ID
prefixes, the word `shall`, the status words and the front-matter
keys.

The README is English only. A translation of it is a render.

The language of the conversation with Claude is a separate matter.
It is not a rule of the forge. It is a fact of one instance (that is,
one installation of the forge), set where the instance is prepared.

## How it works

The project file (`project.md`) carries a field `language`. Its
value is an ISO 639-1 code. Where the field is absent, the project's
language is English. Every artefact of the chain is written in that
language.

The briefs are the one exception among the artefacts. A brief stays
in the language it was written in.

Records, state, research and recipes do not follow the project's
language. They are English in every project, whatever the project
file says.

A recipe may declare several languages: the first is the primary,
the rest are its translations, one render per language (see
[Renders and recipes](renders-and-recipes.md)).

The conversation language lives in `CLAUDE.local.md` at the root of
the engine. That file is the instance's own and is set during setup
(see [Set up the forge](../start/setup.md)). Every command reads the
conversation language from there. It is never written into the
operating layer of the forge. It never appears in an outward-facing
render, the README among them. Such a render states only the rule of
the output language.

Claude translates on write. The conversation may run in one language
while what is written into a document is in the language that
document carries.

## Why

Records, state, research and recipes are English because they are
read by Claude, the reviewers and the checks. They are never handed
to the recipients of the project. One operating language is what
lets Claude, the reviewers and the checks read every project the
same way.

The conversation language stays out of outward-facing renders
because it is a fact of one instance, not a property of the system.

Why the forge dictates exactly one output language per project, and
not several, is not recorded. Why the briefs are exempt from the
project's language is not recorded. Why translation happens on write
is not recorded.

## A worked example

A project with the placeholder slug `example-project` declares French
(`fr`) as the `language` of its project file. The principal and
Claude talk in whatever language the instance is set to, and Claude
translates on write. What the project holds then comes out like this:

| Kind of document | Language |
|---|---|
| a brief | the language the principal wrote it in |
| the intent and every layer below it | French |
| a record | English |
| the state | English |
| a research note | English |
| a recipe | English |
| a work specification | French |
| the file of a work product | the language the `## Making` section of its specification says |
| a render | each language its recipe declares, the first the primary |
| the README | English |

Every ID in the intent keeps its English prefix, and the
front-matter keys, the status words and `shall` stay English too.
Had the project file no `language` field, the intent would be in
English.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
