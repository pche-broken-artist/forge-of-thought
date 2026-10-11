---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 235cc6a7c6b86ffb
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The language rule of the forge says which language each kind of
document carries: one output language per project for the documents
of the chain, English for everything the machinery reads, and a
conversation language that belongs to the installation alone. This
page is for the user who works a project in a language other than
English and for the evaluator who wants to know why a project is not
simply written in one language throughout.

## What it is

The forge dictates one thing about language: a project has one
output language. The output language is the language of the
[artefacts](../reference/glossary.md) of the chain, that is, of the
intent, the assignment and every later layer. A project declares it
in the `language` field of its ledger header, the ledger being the
one file that holds the project's state. The value is an ISO 639-1
code. A project that declares nothing is in English.

Everything else a project holds is always English, whatever the
project's output language:

- records, such as the histories, the decisions and the reports of
  the reviewers;
- state, that is, the ledger;
- research;
- recipes, the files a render is made from.

English is also the notation throughout, in every document of every
project:

- the ID prefixes;
- the word `shall` in the items of an assignment;
- the status words;
- the keys of the front-matter.

There is one exception among the artefacts: the briefs
(`00-brief*.md`) are kept in whatever language they are written in.

A render, an output generated from the chain for one audience, may be
in any language its recipe declares. A translation of an artefact is
such a render: it is not a layer of the chain. The README of a
project is English only; a translation of it is a render.

The conversation language, the language in which the principal (the
person whose thinking is forged) and Claude talk, is not a rule of the
system. It is a fact of one installation, set in `CLAUDE.local.md`
when the forge is set up ([Set up the forge](../start/setup.md)) and
read from there by every command. It is never written into the
operating layer and never shown outward: the README and the other
outward-facing renders state only the output-language rule.

## How it works

Claude translates on write. The principal says what he says in the
conversation language. When a round of work is written, the matter
lands in the artefact in the project's output language, and the
records of the round land beside it in English. The principal does
not translate anything himself.

The one output language holds down the whole chain of a project. The
intent, the assignment and every later layer share it, so that what
the recipients receive reads as one.

A brief is not translated. It stays as it was written, and the
intent made from it is written in the project's output language.

Where the principal wants an artefact in another language, he does
not write a second artefact. He writes a recipe that declares the
language, and the translation is generated as a render from the
artefact. The artefact stays the source of truth; the render is never
edited by hand.

## Why

Records, state, research and recipes are English because they are
read by Claude, the reviewers and the checks and never handed to the
recipients. One operating language is what lets Claude, the reviewers
and the checks read every project the same way, whatever language its
chain is written in.

The conversation language is kept out of the operating layer and out
of every outward-facing render because it is per-instance
configuration, not a system rule: two installations may run the same
project in different conversation languages, and nothing of the
project should depend on which.

Why the briefs keep the language they are written in is not recorded.
Why English is the notation throughout is not recorded. Why the README
is English only, rather than in the project's output language, is not
recorded.

## A worked example

A project `<slug>` is worked by a principal whose conversation
language is not English, and its recipients read French. Its ledger
header declares:

```
language: fr
```

What the project then holds:

| Document | Language |
|---|---|
| the brief, `00-brief.md` | as it was written, whatever that is |
| the intent, `10-intent.md` | French |
| the assignment and every later layer | French |
| the histories and the decisions | English |
| the ledger | English |
| the research | English |
| the recipes | English |
| a render | the language its recipe declares |
| the README | English |

Inside the French intent, the notation stays English: an item is
`POS.0010`, its status is `draft` or `approved`, and the front-matter
keys are `version`, `date`, `status` and `last_change`. Inside the
French assignment, each requirement is written with `shall`.

When the principal wants an English version of the assignment for a
colleague, he does not write one: a recipe declares English as its
language, and the translation is generated as a render beside the
chain.

## See also

- [Set up the forge](../start/setup.md): where the conversation language is set.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
