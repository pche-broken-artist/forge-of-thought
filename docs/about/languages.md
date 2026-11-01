---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 43ea09b9072b17f3
inputs:
  - CLAUDE.md#Prime directives
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The language rule of the forge says which language each kind of
document carries: the documents of a project that reach its
recipients are written in one language, the project's own, and
everything the forge keeps for its own reading is English. This page
is for the user who wants to know what language a file will be in
before it is written, and for the evaluator who wants to understand
why a project may hold two languages side by side without
contradiction.

## What it is

The forge dictates one thing about language: a project has one
output language. That language is declared in the project file
(`project.md`, its `language` field). Where the project file declares
none, the output language is English.

Every document of a project falls on one of two sides of this rule.

- The artefacts of the chain (the intent, the assignment and every
  later layer) are written in the project's language.
- The pages of the documentation are written in the project's
  language, as its artefacts are. The page you are reading follows
  the same rule; what the pages are and how they are made is said on
  [The documentation](the-documentation.md).
- The records (the histories and the decisions), the state (the
  ledger, that is the one file that states where a project stands,
  and the project's threads), the research and the recipes are
  always English, whatever the project's language.
- The notation is English throughout: the ID prefixes, the word
  `shall`, the status words and the front-matter keys.

Three cases complete the rule.

- The briefs (`00-brief*.md`) are the one exception among the
  artefacts: a brief is kept in whatever language it was written in.
- A work specification follows the artefacts and is in the project's
  language; the work file beside it is in the language the
  specification's `## Making` section says.
- A render may be in any language, or languages, its recipe
  declares, the first primary and the rest its translations, one
  render per language; how a recipe declares them is said on
  [Renders and recipes](renders-and-recipes.md).

The README is English only. A README in another language is a
translation, and a translation is a render.

## How it works

The project file is the one source of the output language. Claude
reads the `language` field there and writes every artefact and every
page of the documentation in that language, English when the field is
absent. Nothing else in the project says what language a document is
in: a document's language follows from its kind and from that one
field.

The conversation is a different matter. The language Claude speaks
with the principal (the person whose thinking is being forged) is not
a rule of the system but a setting of the instance, that is of one
installation of the forge. It is set in `CLAUDE.local.md` at the
engine root and read from there by every command. How it is set is
said on [Set up the forge](../start/setup.md). It is never written
into the operating layer, and it is never presented outward: the
README and every other outward-facing render state only the
output-language rule and say nothing of the language the conversation
runs in.

So a conversation may run in one language while the artefacts it
produces are written in another. The forge translates on write: what
is agreed in the conversation is written into each document in the
language that document carries. A position found in the conversation
lands in the intent in the project's language, and the record of how
it changed lands in the history in English, in the same write.

The pages of the documentation take the project's language from the
same project file, and their words keep the spelling the project's
documents use. The README stays English even where the pages are not.

## Why

The reason the records, the state, the research and the recipes are
always English is recorded: they are read by Claude, by the reviewers
(the isolated agents that critique, challenge and check a project)
and by the checks, and they are never handed to the recipients. One
operating language is what lets Claude and the reviewers read every
project the same way, whatever language the project itself is written
in.

Why the artefacts and the pages carry the project's language rather
than a fixed one is not recorded beyond the rule itself: the forge
dictates one output language per project, and the project file
declares it.

Why the conversation language is a setting of the instance and not a
rule of the system, and why it is kept out of every outward-facing
render, is not recorded.

Why the briefs are kept in whatever language they are written in, the
one exception among the artefacts, is not recorded.

Why the README is English only, a translation being a render, is not
recorded.

## A worked example

Take a project under the placeholder slug `<slug>` whose project file
declares a language other than English, written here as `xx`. The
table shows what language each file of that project carries; the
instance's conversation language does not appear in it, because no
file of the project depends on it.

| File | Language | Because |
|---|---|---|
| `project.md` | `language: xx` | the one source of the output language |
| `00-brief.md` | as written | the one exception among the artefacts |
| `10-intent.md` | `xx` | an artefact of the chain |
| `20-assignment.md` | `xx` | an artefact of the chain |
| `10-intent.history.md` | English | a record |
| `decisions.md` | English | a record |
| `ledger.md`, `threads/THR.NNNN.md` | English | state |
| `research/…` | English | research |
| `recipes/<recipe>.md` | English | a recipe |
| `work/<name>.spec.md` | `xx` | a work specification follows the artefacts |
| `work/<name>.<ext>` | as its `## Making` says | the work file |
| `renders/<recipe>.md` | as the recipe declares | a render, one per declared language |
| `README.md` | English | English only; a translation is a render |
| `docs/…` | `xx` | the pages, as the artefacts are |

The IDs inside every file, `POS.NNNN` or `REQ.NNNN`, the word `shall`
in the assignment, the status `draft` or `approved` in a header and
every front-matter key stay English in each of them, because the
notation is English throughout.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [The documentation](the-documentation.md): the pages, generated in
  the project's language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
