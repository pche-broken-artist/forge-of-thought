---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 92de38b172b2c628
inputs:
  - CLAUDE.md#Prime directives
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.2010
---

# Languages

The language rule of the forge says which language each kind of
document carries: one output language per project for what is
handed on, English for everything the forge keeps for itself. This
page is for the user who works a project in a language other than
English and wants to know what will come out in which language, and
for the evaluator who wants to understand why the forge splits the
languages the way it does.

## What it is

The forge dictates one thing about language: a project has one
output language. That language is declared in the project file, in
its `language` field. When the project file declares none, the
output language is English.

The output language governs what is handed on. Everything the forge
keeps for its own working stays English. Between the two stands the
language of the conversation, which is a fact of one installation
and no rule of the system at all.

Three languages can therefore be in play around one project:

- the project's language: the language of its artefacts, the
  documents of the chain, from the intent down to every layer below
  it, and of its documentation
- English: the language of its records, its state, its research and
  its recipes, and the notation throughout
- the conversation language: the language the principal (the person
  whose thinking is being forged) and Claude speak in, set in
  `CLAUDE.local.md` and nowhere else

Every term of the forge used on this page is defined in one line in
the [Glossary](../reference/glossary.md).

## How it works

### What is written in the project's language

The artefacts of the chain are written in the project's language:
the intent, the assignment and every later layer. The pages of the
documentation are written in the project's language as well, as its
artefacts are; how they are made is said on
[The documentation](the-documentation.md).

A work specification follows the artefacts. The file it specifies
is in the language its `## Making` section says.

The one exception among the artefacts is the briefs, the files
`00-brief*.md`. A brief is kept in whatever language it is written
in.

### What is always English

Everything else a project holds is English, whatever the project's
language:

- its records
- its state
- its research
- its recipes

English is also the notation throughout. The notation is what the
forge itself names, in every project alike:

- the ID prefixes
- the status words
- the front-matter keys
- the fixed labels of a story: `Edge cases`, `Risks`, `Note`,
  `Questions`, `Reference`

The README is English only. A translation of it is a render.

### The verb of a requirement

A requirement is an obligation in the indicative. In English the
obligation is written as shall or shall not. An artefact in another
language uses that language's own verb of obligation under the same
rule, and the forge names no word of any other language. Why the
verb follows the language of the artefact is said on
[The assignment](the-assignment.md).

### Renders

A render may be in any language its recipe declares, or in several:
the first is the primary language, the rest are its translations,
and each language gets one render; how a recipe declares them is
said on [Renders and recipes](renders-and-recipes.md).

### The conversation language

The conversation runs in the principal's language. That language is
set in `CLAUDE.local.md`, the instance file of one installation, and
every command reads it from there; where it is set is said on
[Set up the forge](../start/setup.md). It is never written into the
operating layer of the forge. It is never presented outward: the
README and every other outward-facing render state only the
output-language rule.

### Translate on write

The rule that joins the conversation to the documents is "translate
on write". What is talked through in the conversation language is
written into a document in that document's language. A document
never takes the language of the conversation that produced it.

## Why

The records, the state, the research and the recipes are English
because they are read by Claude, the reviewers and the checks, and
never handed to the recipients, those the artefacts are written for.
One operating language is what lets Claude, the reviewers and the
checks read every project the same way.

The conversation language is no rule of the system because it is
per-instance configuration. It belongs to one installation, not to
the forge, and so it has no place in anything the forge shows
outward.

For the other rules on this page no reason is recorded: why the
artefacts take exactly one output language and not several, why the
notation is English, why the briefs are exempt from the project's
language, and why the README stays English while a translation is a
render.

## A worked example

The example is generic and taken from no project. Take a project
whose project file declares `language: de`.

- Its intent and its assignment are written in that language. Their
  requirements use that language's own verb of obligation, not
  shall; which verb that is, the forge does not say.
- Its item IDs keep their English prefixes, its front-matter keeps
  its English keys, and its status words stay English, in the middle
  of text in the project's language.
- Its records, its state and its research are English.
- Its recipes are English, while the renders they produce may be in
  the project's language, in English or in both, one render per
  language, as each recipe declares.
- Its documentation pages are in the project's language. Its README
  is English; a README in the project's language would be a further
  render.
- Its brief stays in whatever language it was written in, whether
  that is the project's language or another.
- Nothing in any of these files says which language the principal
  and Claude spoke while making them.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [The documentation](the-documentation.md): the pages, generated in
  the project's language.
- [The assignment](the-assignment.md): the obligation of a
  requirement and why its verb follows the artefact's language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
