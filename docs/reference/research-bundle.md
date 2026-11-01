---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 7d5181fe3f02c9da
inputs:
  - .claude/skills/research/SKILL.md#Target
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
---

# Research note and bundle

This page states where a research lands and the exact shape of what
it leaves: the bundle, its plan, its notes and its entry in the
research index. It is for the reader who looks up a field or a
section, and for the extender who changes one. The principal is the
person whose thinking is being forged.

## Where a research lands

| Research | Lands as |
|---|---|
| Several cards, or more than one engine | a bundle, the directory `research/YYYY-MM-DD-<topic>/` |
| One card on one engine | a single note, `research/YYYY-MM-DD-<topic>.md` |

A bundle holds:

- `00-plan.md` at its head: the plan as confirmed, then the synthesis.
- One note per card per engine, named `<card>.<engine>.md`.

Rules that hold for both:

- The bundle has one entry in `research/00-INDEX.md`.
- A bundle is immutable from the filing of the synthesis.
- A note is immutable from its filing.
- Everything is written in English.

The command that makes them is described in
[Research a topic](../use/research-a-topic.md).

## The plan, `00-plan.md`

### Front-matter

| Key | Holds |
|---|---|
| `date` | the date of the research |
| `project` | the project's slug |
| `topic` | the topic in a few words |
| `status` | `draft` from the plan's confirmation, then `immutable` from the filing of the synthesis |
| `engines` | the engines the plan went to |
| `derived_from` | the principal's word, the notes and sources the plan names, and the second engine's review of the draft plan |

### Sections, in order

1. Summary
2. Plan (confirmed on a date), with these subsections in order:
   - Purpose
   - Perspectives
   - Assumptions
   - Left out
   - Cards
   - Agents
   - The second engine's review of the draft
3. Deviations from the plan
4. Synthesis (with a date), with these subsections in order:
   - Completeness, card by card
   - Answers side by side
   - Unexpected, gathered
   - Not found, gathered
   - Claude's view
5. Notes

| Section | Holds |
|---|---|
| Summary | what the research says, where the engines differ, what it suggests for the project, what was unexpected; written at the synthesis and placed first |
| Purpose | what the research serves, and the notes and sources already known that the plan builds on |
| Perspectives | the standpoints the topic is treated from, one line each, with the cards that serve it, or "no card" |
| Assumptions | what the plan takes for granted about where the answer lives, and the premortem |
| Left out | the fields and questions considered and deliberately not pursued |
| Cards | the cards, numbered |
| Agents | how many agents and the rule that fixed the count, the engines, whether a second round is allowed and for what |
| The second engine's review of the draft | what the second engine said the draft missed or assumed, and what of it the principal took into the plan |
| Deviations from the plan | every difference between the plan as confirmed and the run, with its reason; "None" is a legitimate entry |
| Completeness, card by card | per card: answered or not found, the stop rule met or why searching ended, what the disconfirming query found |
| Answers side by side | per card, the engines' answers beside each other, the differences spelled out |
| Unexpected, gathered | the Unexpected sections of every note, sorted into finds that reconfigured a question and finds that add a source to a point already made |
| Not found, gathered | what every note reported not finding |
| Claude's view | Claude's own reading, marked as its own, last and apart |
| Notes | the files of the bundle, one line each, with the packet folder it was made from |

### A card

A card has six fields:

| Field | Holds |
|---|---|
| Question | what is asked, about what, in what context, against what alternative |
| Why it matters | the decision or artefact it serves, in one sentence |
| What would answer it | one kind of evidence, and the kind of source it lives in |
| Where to look | source kinds, more than one route, and the known items that must turn up |
| Disconfirming query | one search written to find the opposite of what is expected, and what is expected |
| Stop rule | nothing new from a differently-worded query, every perspective of the card has a primary source, and the opening budget |

## The note, `<card>.<engine>.md`

### Front-matter

| Key | Holds |
|---|---|
| `date` | the date of the note |
| `project` | the project's slug |
| `topic` | the card's question in a few words |
| `status` | `immutable` |
| `engine` | the engine that made the note, such as `claude` or `antigravity` |
| `model` | the model as the engine's envelope reports it, or "engine default" |
| `usage` | the envelope's usage, compact; `—` for a session agent |
| `run` | the packet folder the note was made from, `tmp/research/<run>/<card>` |
| `derived_from` | the plan and its card number, the known notes the card named, and the web sources |

A single note of one card on one engine uses the same front-matter.

### Sections, in order

| Section | Holds |
|---|---|
| In short | the answer to the card in a few sentences: what was found, how sure it is, what the disconfirming query did to it |
| Question | the card verbatim, then one paragraph on the baseline the note must beat |
| Key findings | findings numbered F1, F2 and so on |
| Unexpected | leads, never conclusions; "None" is a legitimate entry |
| Not found | what was looked for and not found, and where it was looked |
| Options | the distinct ways the project could act, each with its trade-offs; left out when the card asked for a fact |
| Relevance to this project | the recommendation and what it rests on, ending with "Consult when:" |
| Sources | the sources, numbered as cited |
| Opened and not used | one line per source opened and left out, with the reason |
| Search record | the queries in order, the pages opened, what the disconfirming query found, and the reason the run ended |

### A finding

A finding is a statement in bold, followed by its epistemic status in
brackets and the kind of evidence named, then the substance with its
sources cited inline as [n].

The epistemic status is one of:

- `consensus`
- `emerging`
- `contested`
- `single source`
- `vendor claim`

The kind of evidence is named beside it, such as controlled study,
audit, standard, vendor report or practitioner claim.

### A source

Each entry of Sources carries:

| Field | Values |
|---|---|
| Title, author or organisation | as published |
| Date | and how it was dated: `byline`, `structured data`, `archive snapshot` or `undated` |
| URL | the address |
| Kind | `primary`, `secondary` or `tertiary` |
| How read | `in full`, `partially` with which part, `summarised fetch`, or `not opened` with why |
| Original or copy | and of what |

## The entry in the research index

The research entry of `research/00-INDEX.md` is one block with a
heading and three fields. The heading is the bundle's directory name,
or the file name for a single note.

| Field | Holds |
|---|---|
| Question | what the research set out to answer |
| Answer in short | two or three lines of the conclusion |
| Consult when | the situations in which the research is worth opening |

## The working files of a run

The working files of a run live under `tmp/research/<run>/`: packets,
plan review, held notes and citation reports. They are no source of
truth, and nothing reads them as a document.

## See also

- [Research a topic](../use/research-a-topic.md): the command that makes them.
- [How a research is made](../about/the-research.md): why a plan comes first and what the sections are for.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
