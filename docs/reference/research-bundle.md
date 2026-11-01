---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 44e8034c026485c1
inputs:
  - .claude/skills/research/SKILL.md#Target
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
---

# Research note and bundle

This page lists the places, the front-matter and the sections of a research note, of a research bundle and of its plan, exactly as the forge shapes them. It is for the user who reads a finished research and for the extender who checks or changes its shape. The principal is whoever's thinking is being forged.

## Where a research lands

A research lands in the `research/` directory of the project, in one of two forms.

| Form | Path | Holds |
|---|---|---|
| Bundle | `research/YYYY-MM-DD-<topic>/` | `00-plan.md` at its head, and one note per card per engine, `<card>.<engine>.md` |
| Single note | `research/YYYY-MM-DD-<topic>.md` | one card on one engine, in the shape of a note |

- A bundle has one entry in `research/00-INDEX.md`, named by its directory.
- A research of one card on one engine stays a single note.
- A bundle is immutable from the filing of the synthesis.
- A note is immutable from its filing.
- Everything is written in English.

## The working files of a run

The files of a run are made under `tmp/research/<run>/`. They are no source of truth. The folder stays as it is after the run, for inspection.

## The plan (`00-plan.md`)

### Front-matter

| Key | Value |
|---|---|
| `date` | the date, `YYYY-MM-DD` |
| `project` | the project slug |
| `topic` | the topic in a few words |
| `status` | `draft` from the plan's confirmation, `immutable` from the filing of the synthesis |
| `engines` | the engines the plan went to |
| `derived_from` | the principal's word and its date, the notes and sources the plan names, the second engine's review of the draft plan |

### Sections, in order

1. **Summary.** Written at the synthesis, placed first. It is empty until then. The index entry's "Answer in short" is drawn from it.
2. **Plan (confirmed `YYYY-MM-DD`).** The plan word for word as confirmed, in these subsections:
   - **Purpose:** what the research serves, and the notes and sources already known.
   - **Perspectives:** the standpoints, one line each, with the cards that serve them, or "no card".
   - **Assumptions:** what the plan takes for granted about where the answer lives, then the premortem.
   - **Left out:** the fields and questions deliberately not pursued.
   - **Cards:** one subsection per card.
   - **Agents:** how many, the rule that fixed the count, the engines, and whether a second round is allowed.
   - **The second engine's review of the draft:** what it said the draft missed, and what the principal took in.
3. **Deviations from the plan.** Every difference between the plan and the run, with its reason. "None" is a legitimate entry.
4. **Synthesis (`YYYY-MM-DD`).** In these subsections:
   - **Completeness, card by card:** per card, answered or not found, the stop rule met or why searching ended, and what the disconfirming query found.
   - **Answers side by side:** the engines' answers beside each other, with the differences spelled out.
   - **Unexpected, gathered:** the Unexpected sections of every note.
   - **Not found, gathered:** what every note reported not finding.
   - **Claude's view:** last and apart, marked as Claude's own.
5. **Notes.** The files of the bundle, one line each, with the packet folder under `tmp/research/<run>/` each was made from.

### The six fields of a card

A card is headed `Card N: <the question in a few words>`.

| Field | Content |
|---|---|
| Question | what is asked, about what, in what context, against what alternative |
| Why it matters | the decision or artefact it serves, one sentence |
| What would answer it | one kind of evidence, and the kind of source it lives in |
| Where to look | source kinds, more than one route, and the known items that must turn up |
| Disconfirming query | one search written to find the opposite of what is expected, and what is expected |
| Stop rule | nothing new from a differently-worded query, and every perspective of the card has a primary source; the opening budget |

## The note (`<card>.<engine>.md`)

### Front-matter

| Key | Value |
|---|---|
| `date` | the date, `YYYY-MM-DD` |
| `project` | the project slug |
| `topic` | the card's question in a few words |
| `status` | `immutable` |
| `engine` | the engine that made the note (`claude`, `antigravity`, and so on); the forge names engines, never models |
| `model` | as the engine's envelope reports it, or "engine default" |
| `usage` | the envelope's usage, compact; `—` for a session agent |
| `run` | the packet folder the note was made from, `tmp/research/<run>/<card>` |
| `derived_from` | the plan and the card, the known notes the card named, the web sources |

A single note of one card on one engine uses the same front-matter.

### Sections, in order

1. **In short.** The answer in a few sentences: what was found, how sure it is, what the disconfirming query did to it, the one unexpected thing if there is one. Written last, placed first.
2. **Question.** The card verbatim, then one paragraph on the baseline the note must beat.
3. **Key findings.** Numbered F1, F2 and on. Each is a statement in bold, then its epistemic status in brackets, then the substance with sources cited inline as [n].
4. **Unexpected.** Leads, never conclusions, one paragraph each with its source [n]. "None" is a legitimate entry.
5. **Not found.** What was looked for and not found, and where it was looked.
6. **Options.** The distinct ways the project could act, each with trade-offs. Left out when the card asked for a fact, not a choice.
7. **Relevance to this project.** The recommendation, what it rests on, what it is chosen against, ending with "Consult when:".
8. **Sources.** Numbered as cited.
9. **Opened and not used.** One line per source opened and left out, with the reason.
10. **Search record.** The queries in order, the pages opened, what the disconfirming query found, and which part of the stop rule or the opening budget ended the run.

### Epistemic status words

A finding carries one of these words in brackets, with the kind of evidence named (controlled study, audit, standard, vendor report, practitioner claim).

- consensus
- emerging
- contested
- single source
- vendor claim

### The fields of a source

Each entry of Sources has these fields.

| Field | Content |
|---|---|
| Title | the title of the source |
| Author or organisation | who published it |
| Date | the date and how it was dated: byline, structured data, archive snapshot or undated |
| URL | the address |
| Kind | primary, secondary or tertiary |
| How read | in full; partially, with which part; summarised fetch; or not opened, with the reason |
| Original or copy | and of what it is a copy |

A source that could not be opened is listed as not opened and is never cited for content.

## The research entry of the resource index

`research/00-INDEX.md` has one entry per bundle or single note. Its heading is the bundle's directory name, or the note's file name `YYYY-MM-DD-<topic>.md`. The entry has three fields.

| Field | Content |
|---|---|
| Question | what the note set out to answer |
| Answer in short | two or three lines of the conclusion |
| Consult when | the situations in which the note is worth opening |

For a bundle the entry is written from the synthesis, and it waits for the synthesis.

## See also

- [Research a topic](../use/research-a-topic.md): the command that makes them.
- [How a research is made](../about/the-research.md): why a plan comes first and what the sections are for.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
