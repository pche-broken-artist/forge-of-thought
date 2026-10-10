---
generated: 2026-10-10
made: mirrored
inputs-hash: 5744109a01fa6b18
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
  - CLAUDE.md
---

# Research a topic

This page is for a user who wants the current best practice on one
question before deciding something in a project. It says what to type,
what comes back and where the result is kept.

## Run it

Type:

```
/research <topic> [slug]
```

The topic is the question you want looked into. The slug names the
project; if the last word you give names a project directory, it is
taken as the slug and the rest is the topic.

The aim is grounding for your own work: you do not reinvent what the
world has already solved.

## What happens

1. Claude searches the web for current best practice, established
   frameworks and notable recent developments. It prefers primary and
   high-quality sources and notes their publication dates. Each
   finding is marked as consensus, emerging or contested.
2. Claude writes a note in the project's `research/` directory, named
   `YYYY-MM-DD-<topic-slug>.md`, in English. It holds the question,
   the key findings with their sources, the options with their
   trade-offs, and a short section on relevance to this project with a
   concrete recommendation.
3. Claude adds the note to the research index, `research/00-INDEX.md`
   (creating the index if it is missing), and a row to the Research
   table of the project's ledger. The index entry has three fields:
   the question, the answer in short, and when to consult the note.
4. Claude tells you the result, leading with the recommendation and
   the trade-offs, not a literature review.

## One question, one note

A research answers one question. If your topic turns out to be several
questions, you get several notes, each answering one, never a single
combined document.

## The note does not change

The note is immutable once written. If the world moves on, a new
research is made rather than the old note being edited.

## When the findings point at a change

If the findings suggest a change to an artefact of the chain, Claude
proposes it explicitly, through `/forge <state>`. It never makes the
change silently: what to do with the recommendation stays yours.

## See also

- [About sources and research](../about/sources-and-research.md): what
  research is for and why it is immutable.
