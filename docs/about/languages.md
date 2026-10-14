---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 345577e8a8f8ea2e
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The language rule of the forge says which language each kind of
document carries. This page is for the user who works a project and
for the evaluator who wants to know why a project speaks one language
outward and another inside. It says what the rule is, how it works
document by document, and the reasons that are recorded for it.

## What it is

The forge dictates one thing about language: a project has one
output language. The artefacts of the chain (the intent, the
assignment and every later layer) are written in that language.
Everything else a project holds is English. The conversation between
the principal (the person whose thinking is forged) and Claude runs in
whatever language the principal chooses, and that choice is a fact of
the installation, not a rule of the system.

## How it works

The output language of a project is declared in the header of its
ledger (the file that holds the project's state), under the key
`language`, as an ISO 639-1 code. When the header carries no
`language`, the output language is English.

Each kind of document carries its language as follows.

- The artefacts of the chain: the project's output language.
- The briefs (`00-brief*.md`): the one exception among the
  artefacts, kept in whatever language they are written in.
- The records (the histories and the decisions), the state (the
  ledger and the indexes), the research and the recipes: always
  English, whatever the project's language.
- A work specification: the project's output language, like the
  artefacts. The file of the work product is in the language its
  specification says under `## Making`.
- A render: any language its recipe declares. A recipe may declare
  several languages; the first is the primary and the rest are its
  translations, one render per language ([Renders and
  recipes](renders-and-recipes.md)). A translation is itself a
  render.
- The README of a project: English only. A translation of it is a
  render.

The notation is English throughout, in every document and in every
language: the ID prefixes, the word `shall`, the status words and the
front-matter keys are never translated.

The conversation language is set once per installation, in
`CLAUDE.local.md` ([Set up the forge](../start/setup.md)). Every
command reads it from there. It is never written into the operating
layer and never shown outward: the README and every other
outward-facing render state only the output-language rule.

Claude translates on write. The conversation may run in one language
and the document it produces in another; what is agreed in the
conversation is written into the document in the document's language.

## Why

The reasons recorded for the rule are these.

The records, the state, the research and the recipes are English
because they are read by Claude, the reviewers and the checks and
never handed to the recipients. One operating language is what lets
them read every project the same way.

The conversation language is a per-instance configuration and not a
system rule, so that the system dictates nothing about it. It is set
in one place and read by every command from there.

A translation of a render is a render, so that the artefacts stay the
source of truth in one language and every other language is
generated from them.

For the following parts of the rule the reason is not recorded: why
the briefs are the exception among the artefacts; why the notation
stays English in every language; why a work specification follows the
artefacts while its file may differ; why the conversation language is
never presented outward.

## A worked example

A principal creates a project with the placeholder slug `my-project`
and declares `language: fr` in its ledger header. The conversation
with Claude runs in the language set in `CLAUDE.local.md`, which may
be a third language again. What this means for the files:

- `10-intent.md` and every layer below it are written in French, and
  Claude translates what is agreed in the conversation as it writes.
- A position in the intent keeps its English ID (`POS.0010`) and its
  English front-matter keys (`version`, `status`), and a requirement
  of the assignment is still written with `shall`.
- `00-brief.md` stays in the language it was written in, French or
  not.
- `ledger.md`, `decisions.md`, every `.history.md` companion, every
  file of `research/` and every recipe in `recipes/` are English.
- A recipe that declares the languages `fr` and `en` yields two
  renders, the French one primary and the English one its
  translation.
- The project's README is English, and says of language only that
  the project's artefacts are in French.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
