---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: c8bbb31224949f23
inputs:
  - .claude/skills/research/SKILL.md#Target
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
---

# Research note and bundle

This page lists exactly where a research lands and what its files hold: the folder of a bundle, its plan, a research note, and the entry in the resource index. It is for the reader who looks up a field or a section, whether the person who runs a research or the one who extends how it is made. The principal is the person whose thinking is being forged.

## Where a research lands

| Research | Lands as | Index entry |
|---|---|---|
| Several cards, or more than one engine | A bundle folder `research/YYYY-MM-DD-<topic>/` | One entry for the whole bundle in `research/00-INDEX.md` |
| One card on one engine | A single note `research/YYYY-MM-DD-<topic>.md` | One entry in `research/00-INDEX.md` |

A bundle holds these files:

| File | Content |
|---|---|
| `00-plan.md` | At the head of the bundle: the plan as confirmed, then the synthesis |
| `<card>.<engine>.md` | One note per card per engine |

Rules that hold for both shapes:

- A bundle is immutable from the filing of the synthesis. After that nothing in it changes.
- A single note is immutable from its filing.
- Everything is written in English.
- The working files of a run live under `tmp/research/<run>/`. They are no source of truth, and no note, check or ledger reads them as one.

## The plan: `00-plan.md`

### Front-matter

| Field | Holds |
|---|---|
| `date` | The date of the plan |
| `project` | The project's slug |
| `topic` | The research's topic in a few words |
| `status` | `draft` from the plan's confirmation, `immutable` from the synthesis's filing |
| `engines` | The engines the plan went to |
| `derived_from` | The principal's word, the notes and sources the plan names, and the second engine's review of the draft plan |

### Sections, in order

| Section | Holds |
|---|---|
| Summary | Written at the synthesis but placed first: what the research says, where the engines differ and what that means, what it suggests for the project, what was unexpected. Empty until the synthesis. The index entry's "Answer in short" is drawn from it |
| Plan (confirmed on a date) | The plan word for word as confirmed, in the subsections below |
| Deviations from the plan | Every difference between the plan and the run, with its reason. "None" is a legitimate entry |
| Synthesis (on a date) | Made when every note has returned, in the subsections below |
| Notes | The files of the bundle, one line each, with the packet folder under `tmp/research/<run>/` each was made from |

The subsections of Plan, in order:

| Subsection | Holds |
|---|---|
| Purpose | What the research serves in the project, and the notes and sources already known that the plan builds on |
| Perspectives | The standpoints from which the topic is treated, one line each, with the cards that serve them or "no card" |
| Assumptions | What the plan takes for granted about where the answer lives, what would make it rethink, and a premortem answered once by Claude and marked as its own |
| Left out | The fields and questions considered and deliberately not pursued |
| Cards | One card per question, with the six fields below |
| Agents | How many agents, the rule that fixed the count (one per card per engine, none for a question another card answers), the engines, and whether a second round is allowed and for what |
| The second engine's review of the draft | What the second engine said the draft missed or assumed, and what of it the principal took into the plan, item by item |

The six fields of a card:

| Field | Holds |
|---|---|
| Question | What is asked, about what, in what context, against what alternative |
| Why it matters | The decision or artefact it serves, in one sentence |
| What would answer it | One kind of evidence, and the kind of source it lives in |
| Where to look | Source kinds, more than one route, and the known items that must turn up |
| Disconfirming query | One search written to find the opposite of what is expected, and what is expected |
| Stop rule | Nothing new from a differently-worded query, every perspective of the card has a primary source, and the opening budget |

The subsections of Synthesis, in order:

| Subsection | Holds |
|---|---|
| Completeness, card by card | Per card: answered, or not found and where it was looked; the stop rule met, or why searching ended; what the disconfirming query found, including nothing |
| Answers side by side | Per card, the engines' answers beside each other, the engine named. Agreement is reported as consistency, never as validation. Differences are spelled out. Two engines citing the same copy count as one source |
| Unexpected, gathered | The Unexpected sections of every note, sorted into finds that reconfigured a question or brought a mechanism from elsewhere, and finds that only add a source to a point already made |
| Not found, gathered | What every note reported not finding, put together |
| Claude's view | Last and apart: what Claude makes of it, marked as its own, verified or hypothesis said in plain words, and what it proposes to change in the chain |

## The note: `<card>.<engine>.md`

A note holds one card on one engine. A single research of one card on one engine uses the same shape, `engine` and `run` as they are.

### Front-matter

| Field | Holds |
|---|---|
| `date` | The date of the note |
| `project` | The project's slug |
| `topic` | The card's question in a few words |
| `status` | `immutable` |
| `engine` | The engine that made the note. The forge names engines, never models |
| `model` | The model as the engine's envelope reports it, or "engine default" |
| `usage` | The envelope's usage, compact; a single hyphen for a session agent |
| `run` | The packet folder the note was made from, `tmp/research/<run>/<card>` |
| `derived_from` | The plan and card number, the known notes the card named, and the web sources |

### Sections, in order

| Section | Holds |
|---|---|
| In short | The answer to the card in a few sentences, written last and placed first: what was found, how sure it is, what the disconfirming query did to it, and the one unexpected thing if there is one |
| Question | The card verbatim, then one paragraph on what the note must beat (the baseline) |
| Key findings | Numbered F1, F2 and so on; see below |
| Unexpected | Leads, never conclusions, one paragraph each with its source. A find that reconfigures the question is said in plain words while the question is still answered as put. "None" is a legitimate entry |
| Not found | What was looked for and not found, with where it was looked. A figure with no source is a gap here, never an estimate above |
| Options | The distinct ways the project could act on the findings, each with its trade-offs. Left out when the card asked for a fact, not a choice |
| Relevance to this project | The recommendation in plain words, what it rests on and what it is chosen against, the agent's own inferences marked as its own. It ends with "Consult when:" and the situations in which the note is worth opening |
| Sources | Numbered as cited; the fields below |
| Opened and not used | One line per source opened and left out, with the reason: off the question, a copy, below the bar, or superseded by another |
| Search record | The queries run, in order; the pages opened, an opening being a fetch of a page; what the disconfirming query found; the reason the run ended |

### A key finding

Each finding is a statement in bold, then its epistemic status in brackets, then the substance with its sources cited inline as [n].

The status is one of these words:

- consensus
- emerging
- contested
- single source
- vendor claim

The kind of evidence is named beside the status: controlled study, audit, standard, vendor report or practitioner claim. These further rules hold:

- A finding that rests on a summarised fetch or a snippet alone says so.
- Two sources that disagree are both named, with "contradicted by [n]" where it applies.
- A time-sensitive figure carries the date of its youngest source.
- Fact and speculation are kept apart: future tense and "could" are speculation.

### A source

| Field | Holds |
|---|---|
| Title, author or organisation | As the source gives them |
| Date | With how it was dated: byline, structured data, archive snapshot or undated |
| URL | The address |
| Kind | primary, secondary or tertiary |
| How read | in full; partially, with which part (the word "partially" alone is no answer); summarised fetch; or not opened, with why |
| Original or copy | And of what, if a copy |

A source the agent could not open is listed as not opened and is never cited for content.

## The research entry of the resource index

Each research has one entry in `research/00-INDEX.md`, headed by the file or folder name `YYYY-MM-DD-<topic>.md`. A bundle appears as one entry. The index is freely rewritten, tracks nothing, and catalogues the files without being a source of truth.

| Field | Holds |
|---|---|
| Question | What the note set out to answer |
| Answer in short | Two or three lines of the conclusion |
| Consult when | The situations in which the note is worth opening |

## See also

- [Research a topic](../use/research-a-topic.md): the command that makes them.
- [How a research is made](../about/the-research.md): why a plan comes first and what the sections are for.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
