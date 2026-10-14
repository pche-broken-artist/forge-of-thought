---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 09a435a8bb470b77
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
---

# Research a topic

`/research` gets you a durable, indexed research note on one question, grounded in current web sources. It is for the principal (whoever's thinking is being forged), who does not want to reinvent what the world has already solved. For what research is for and why a note is never edited, see [Sources and research](../about/sources-and-research.md).

## When to use it

Use it when an artefact you are working on rests on a question that others have already answered, and you want their best practice before you decide.

## The command

```
/research <topic> [slug]
```

The last word is the project slug if it names a directory under `projects/`. Everything before it is the topic. Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## What happens

1. Claude searches the web for current best practice, established frameworks and notable recent developments. It prefers primary and high-quality sources and notes their publication dates. It marks each finding as consensus, emerging or contested.

   You should now see Claude working through sources for your topic.

2. Claude writes one note, `research/YYYY-MM-DD-<topic-slug>.md`, in the project. The note is in English and is immutable. It holds:
   - the question
   - the key findings, with sources
   - the options, with their trade-offs
   - a short section on relevance to the project, with a concrete recommendation

   You should now see a new dated file in the project's `research/` directory.

3. Claude indexes the note and registers it. It adds an entry to `research/00-INDEX.md`, creating the index if it is missing. The entry names three fields: the question, the answer in short and when to consult the note. It also adds a row to the Research table of the ledger, the file that is the single source of truth for a project's state.

   You should now see the note in the index and a row for it in the ledger.

4. Claude summarises the result for you. The summary leads with the recommendation and the trade-offs, not with a literature review.

   You should now see the recommendation first.

5. If the findings suggest a change to an artefact of the chain, Claude proposes it explicitly. The change is made through `/forge <state>`, never silently.

   You should now see a proposal, and nothing changed in the artefact until you take it up.

## One question, one note

A research has one question. If your topic turns out to be several questions, Claude writes several notes, each answering one. It never writes one combined document.

## What you have afterwards

- One dated, immutable note per question in `research/`.
- An entry for each note in `research/00-INDEX.md`.
- A registration row for each note in the ledger.
- A summary that led with the recommendation.

## A worked example

You want to know how teams keep an onboarding checklist current. You type:

```
/research keeping an onboarding checklist current my-project
```

Claude finds the question has two parts: who owns the checklist, and how changes are detected. It writes two notes, for example `research/2026-10-14-checklist-ownership.md` and `research/2026-10-14-checklist-change-detection.md`. Each states its question, findings with sources marked consensus, emerging or contested, options with trade-offs, and a recommendation. Both appear in `research/00-INDEX.md` and in the ledger. Claude's summary opens with the recommendation of each note. It then proposes, if the findings call for it, a change to an artefact through `/forge <state>`, and waits for you.

## See also

- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
