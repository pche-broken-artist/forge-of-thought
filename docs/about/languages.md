---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: f2176b5697c7e449
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The forge's language rule says which language each kind of document
in a project is written in. The forge sets one rule only: each
project has one output language. This page explains which documents
follow that language, which are always English, and why. It is for
the user who runs a project and for the evaluator who wants to
understand how the forge treats language.

## What it is

The forge as a system dictates one thing about language: a project
has one output language. The artefacts of the chain are written in
it. The artefacts are the versioned documents a project's thinking
travels through, such as the intent, the assignment and every later
layer. Everything else a project holds has a fixed language of its
own, or a language set somewhere else.

The language of the conversation is not part of this rule. The
conversation runs in the principal's language. The principal is the
person whose thinking is forged and who has the final word on its
content. That language is a fact of one instance (one installation
of the forge), not a property of the system. It is set in
`CLAUDE.local.md` at the engine root, which [Set up the
forge](../start/setup.md) fills on a new machine.

## How it works

Each kind of document in a project has its language set in one way:

- The artefacts of the chain (the intent, the assignment, later
  layers): the project's language.
- The briefs (`00-brief*.md`): whatever language they are written
  in. They are the one exception among the artefacts.
- A work specification: the project's language, as the artefacts
  are.
- The file of a work product: the language its specification's
  `## Making` section says.
- Records, state, research and recipes: always English.
- A render: any language, or languages, its recipe declares.
- The README: English only.

The project's language is the `language` field of the project file,
`project.md`, written as an ISO 639-1 code. Where the field is
absent, the project's language is English.

English is the notation throughout, whatever the project's language.
The ID prefixes, the word `shall`, the status words and the
front-matter keys stay English in every document, whatever language
its text is in.

A recipe may declare several languages: the first is the primary,
the others are translations of it, one render per language (see
[Renders and recipes](renders-and-recipes.md)). A translation of the
README is a render of its own.

Claude translates on write. The conversation may run in one
language while an artefact is written in another. Claude carries
what is agreed in the conversation and writes it into the artefact
in the artefact's language.

The conversation language never appears outward. It is not written
into the engine's operating layer, that is `CLAUDE.md`, the skills
and the templates. The README and every other render meant for
readers outside state only the rule of the output language.

For a one-line meaning of any term on this page, see the
[Glossary](../reference/glossary.md).

## Why

Records, state, research and recipes are always English. The reason
is that they are read by Claude, the reviewers and the checks, and
never handed to the recipients. One operating language is what lets
them read every project the same way.

The conversation language stays out of the system. The reason is
that it is configuration of one instance, not a rule of the forge.

Several reasons are not recorded:

- Why a project has exactly one output language, beyond the rule
  itself: the reason is not recorded.
- Why the briefs are exempt from the project's language: the reason
  is not recorded.
- Why English is the notation in every language: the reason is not
  recorded.
- Why a work product's file takes its language from its
  specification: the reason is not recorded.
- Why the README is English only: the reason is not recorded.

## A worked example

A project `my-project` has a project file with this line:

```
language: de
```

The principal talks with Claude in his own language, the one his
instance sets. When Claude writes the intent, it writes it in
German. The items keep their English ID prefixes and the
front-matter keys stay English. The assignment uses `shall` as its
keyword inside German sentences.

The principal's first brief was written in English, and it stays
English. The history companion of the intent, the ledger, the
research notes and every recipe are English.

A recipe for a pitch declares German first and English second. The
German render is the primary. The English render is a translation
of it. The project's README is English.

If the project file had no `language` field, every artefact but the
briefs would be English.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
