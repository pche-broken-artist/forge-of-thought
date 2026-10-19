---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 377bef70c4133a05
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
---

# Research a topic

This page shows how to get a durable, indexed research note on one question with `/research`. It is for the principal, the person whose thinking is being forged, who wants current best practice behind an artefact instead of reinventing what others have solved.

## When to use it

Use it when a question in your project has probably been answered well elsewhere, and you want that answer, its sources and a recommendation on paper before you decide. Ask one question at a time. Why a note is kept unchanged and what research is for are explained in [Sources and research](../about/sources-and-research.md).

## The command

```
/research <topic> [slug]
```

The last word is read as the project slug if it names a project of yours. Everything before it is the topic.

```
/research how small teams run blameless post-incident reviews my-project
```

## What happens

1. Claude searches the web for current best practice, established frameworks and notable recent developments. It prefers primary and high-quality sources and notes their publication dates. It marks each finding as consensus, emerging or contested.

   You should now see Claude working through sources for your question.

2. Claude writes one note, `research/YYYY-MM-DD-<topic-slug>.md`, in English. The note holds the question, the key findings with their sources, the options with their trade-offs, and a short section on relevance to your project with a concrete recommendation.

   You should now see a new dated file in the `research/` folder of the project.

3. Claude adds an entry for the note to `research/00-INDEX.md`, and creates that index if it is missing. The entry has three fields: Question, Answer in short and Consult when. The ledger (the file that holds the state of the project) has a Research table that reads the note itself, so nobody writes a row there. Claude then remakes the ledger with `python scripts/forge-ledger.py <slug>`.

   You should now see the note's entry in `research/00-INDEX.md`.

4. Claude summarises the result for you. The summary leads with the recommendation and the trade-offs, not a literature review.

   You should now see the recommendation first in Claude's reply.

5. If the findings suggest a change to an artefact of the chain, Claude proposes it explicitly. The change is made through `/forge <state>`, never silently.

   You should now see a proposal, and no artefact changed.

## What you have afterwards

- One immutable dated note in `research/`, in English.
- Its entry in `research/00-INDEX.md`.
- A ledger that lists the note.
- A summary that leads with the recommendation.

A topic that turns out to hold several questions becomes several notes, each answering one. It is never one combined document.

## A worked example

You run `/research how small teams run blameless post-incident reviews my-project`. Claude finds that a written timeline and a focus on contributing conditions are consensus, that automated review tooling is emerging, and that publishing reviews outside the team is contested. It writes `research/2026-10-19-blameless-post-incident-reviews.md` with the question, the findings with sources, two options with trade-offs and a recommendation. It adds the index entry and remakes the ledger. Its reply opens with the recommendation. It then proposes that you take the recommendation into the intent through `/forge intent`, and waits for your decision.

## See also

- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
