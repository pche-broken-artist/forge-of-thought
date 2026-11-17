---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: d8e9f5b8122c32c0
inputs:
  - .claude/skills/research/SKILL.md#Target
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
---

# Research note and bundle

This page states where a research lands, and the front-matter and the
sections of its files: the single note, the bundle, the plan at the
head of a bundle and the research entry of the resource index. It is
for the user who reads a research and for the extender who changes its
shape. The command that makes these files is described in
[Research a topic](../use/research-a-topic.md), the reasons for the
plan and its sections in [How a research is made](../about/the-research.md),
and the terms in the [Glossary](glossary.md).

## Where a research lands

| Research | Where it lands |
|---|---|
| Several cards, or several engines | A bundle, the folder `research/YYYY-MM-DD-<topic>/` |
| One card on one engine | A single note, `research/YYYY-MM-DD-<topic>.md` |

A bundle holds these files:

| File | Content |
|---|---|
| `00-plan.md` | The plan as confirmed, then the synthesis; at the head of the bundle |
| `<card>.<engine>.md` | One note per card per engine |

- A bundle has one entry in `research/00-INDEX.md`.
- A single note has one entry there as well, named by its file.
- Every file is written in English.
- The plan is `draft` from its confirmation and `immutable` from the
  filing of the synthesis. After that nothing in the bundle changes.
- A note is `immutable` from its filing.
- The working files of a run lie under `tmp/research/<run>/`. They are
  no source of truth.

## The plan: `00-plan.md`

### Front-matter

| Key | Holds |
|---|---|
| `date` | The date of the research |
| `project` | The slug of the project |
| `topic` | The topic in a few words |
| `status` | `draft`, then `immutable` |
| `engines` | The engines the plan went to, such as `claude` or `antigravity` |
| `derived_from` | The principal's word, the notes and sources the plan names, and the second engine's review of the draft plan |

The principal is the person whose thinking is forged.

### Sections, in order

| Section | Holds |
|---|---|
| Summary | Written at the synthesis, placed first: the result, where the engines differ, what it suggests for the project, what was unexpected. The "Answer in short" of the index entry is drawn from it. Empty until the synthesis |
| Plan (confirmed on a date) | The plan, with the subsections below |
| Deviations from the plan | Every difference between the plan as confirmed and the run, each with its reason; "None" is a legitimate entry |
| Synthesis (with its date) | Made when every note has returned, with the subsections below |
| Notes | The files of the bundle, one line each, with the packet folder under `tmp/research/<run>/` it was made from |

Subsections of Plan, in order:

| Subsection | Holds |
|---|---|
| Purpose | What the research serves in the project, and what is already known from `research/` and `sources/` |
| Perspectives | The standpoints from which the topic is treated, one line each, with the cards that serve it, or "no card" where a perspective is left empty on purpose |
| Assumptions | What the plan takes for granted about where the answer lives, what would make it rethink, and the premortem answered once by Claude |
| Left out | The fields and questions considered and deliberately not pursued |
| Cards | One card per question |
| Agents | The number of agents and the rule that fixed it, the engines, and whether a second round is allowed and for what |
| The second engine's review of the draft | What the second engine said the draft missed or assumed, and what of it the principal took into the plan |

Subsections of Synthesis, in order:

| Subsection | Holds |
|---|---|
| Completeness, card by card | Per card: answered, or not found and where it was looked; whether the stop rule was met; what the disconfirming query found |
| Answers side by side | Per card, the engines' answers laid beside each other; differences spelled out; two engines citing one copy counted as one source |
| Unexpected, gathered | The Unexpected sections of every note, sorted into finds that reconfigured a question and finds that only add a source |
| Not found, gathered | What every note reported not finding |
| Claude's view | Last and apart: what Claude makes of it, marked as its own, and what it proposes to change in the chain |

### The card

A card has a heading `Card N: <the question in a few words>` and six
fields:

| Field | Holds |
|---|---|
| Question | What is asked, about what, in what context, against what alternative |
| Why it matters | The decision or artefact it serves, in one sentence |
| What would answer it | One kind of evidence, and the kind of source it lives in |
| Where to look | Source kinds, more than one route, and the known items that must turn up |
| Disconfirming query | One search written to find the opposite of what is expected, and what is expected |
| Stop rule | Nothing new from a differently worded query, every perspective of the card with a primary source, and the opening budget |

## The note: `<card>.<engine>.md`

### Front-matter

| Key | Holds |
|---|---|
| `date` | The date of the note |
| `project` | The slug of the project |
| `topic` | The card's question in a few words |
| `status` | `immutable` |
| `engine` | The engine that made the note, such as `claude` or `antigravity`; engines are named, never models |
| `model` | The model as the engine's envelope reports it, or "engine default" |
| `usage` | The envelope's usage, compact; a long-dash placeholder for a session agent, that is an agent run inside the conversation |
| `run` | The packet folder the note was made from, `tmp/research/<run>/<card>` |
| `derived_from` | The plan and the card number, the known notes the card named, and the web sources |

### Sections, in order

| Section | Holds |
|---|---|
| In short | The answer to the card in a few sentences: what was found, how sure it is, what the disconfirming query did to it, the one unexpected thing if there is one |
| Question | The card verbatim, then one paragraph on what the note must beat, the baseline |
| Key findings | See below |
| Unexpected | Leads, never conclusions, one paragraph each with its provenance; "None" is a legitimate entry |
| Not found | What was looked for and not found, with where it was looked |
| Options | The distinct ways the project could act on the findings, each with its trade-offs; left out when the card asked for a fact |
| Relevance to this project | The recommendation, what it rests on and what it is chosen against, the agent's own inferences marked; it ends with "Consult when:" and the situations in which the note is worth opening |
| Sources | Numbered as cited, with the fields below |
| Opened and not used | One line per source opened and left out, with the reason |
| Search record | The queries run in order, the pages opened, what the disconfirming query found, and the reason the run ended |

### Key findings

Findings are numbered F1, F2 and so on. Each is a statement in bold,
then its epistemic status in brackets, then the substance with sources
cited inline as [n].

| Status word | Meaning in the template |
|---|---|
| `consensus` | Status word of a finding |
| `emerging` | Status word of a finding |
| `contested` | Status word of a finding |
| `single source` | Status word of a finding |
| `vendor claim` | Status word of a finding |

The kind of evidence is named beside the status, for example a
controlled study, an audit, a standard, a vendor report or a
practitioner claim.

### The fields of a source

| Field | Holds |
|---|---|
| Title, author or organisation | As the source gives them |
| Date and how it was dated | `byline`, `structured data`, `archive snapshot` or `undated`; the URL |
| Kind | `primary`, `secondary` or `tertiary` |
| How read | `in full`, `partially` with which part, `summarised fetch`, or `not opened` with why |
| Original or copy | And of what it is a copy |

A source that could not be opened is listed as not opened and never
cited for content.

## The research entry of the index

Each research has one entry in `research/00-INDEX.md`, under the
heading of its file name `YYYY-MM-DD-<topic>.md`. A bundle takes one
entry.

| Field | Holds |
|---|---|
| Question | What the note set out to answer |
| Answer in short | Two or three lines of the conclusion |
| Consult when | The situations in which the note is worth opening |

## See also

- [Research a topic](../use/research-a-topic.md): the command that makes them.
- [How a research is made](../about/the-research.md): why a plan comes first and what the sections are for.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
