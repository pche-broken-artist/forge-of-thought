---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
  - CLAUDE.md
---

# Research a topic

This page is for a user who wants to ground a decision in what the
world already knows about it. It says what `/research` does, what
comes out and what happens to the findings afterwards.

## Run it

```
/research <topic> [slug]
```

The topic is a question you want answered, for example how some kind
of document is usually written. If the last word names a project
under `projects/`, it is taken as the project's slug and the rest is
the topic. The purpose is inspiration and grounding for your
artefacts, so that you do not reinvent what has already been solved.

## What it does

1. It looks up current best practice with web sources: established
   frameworks and notable recent developments. It prefers primary and
   high-quality sources and notes their publication dates.
2. It marks the epistemic status of what it finds: **consensus**,
   **emerging** or **contested**.
3. It writes a dated note into the project's `research/` directory,
   named `YYYY-MM-DD-<topic-slug>.md`, in English. The note holds:
   - the question;
   - the key findings, each with its sources;
   - the options, with their trade-offs;
   - a short section on relevance to this project, with a concrete
     recommendation.
4. It indexes the note in `research/00-INDEX.md` (creating the index
   if it is missing) and registers it in the Research table of the
   project's `ledger.md`.
5. It summarises for you in the conversation. The summary leads with
   the recommendation and the trade-offs, not with a literature
   review.

## One question, one note

A research answers one question. If your topic turns out to be several
questions, you get several notes, each answering one. You never get
one combined document.

## What you see in the index

The entry for a note in `research/00-INDEX.md` has three fields:
**Question**, **Answer in short** and **Consult when**. They let you
and Claude know what research exists, and when it is worth opening,
without re-reading the notes.

## The note is immutable

Once written, the note is never edited. If the world moves on or you
want a different angle, a new note is made; corrections happen
downstream, not in the old note. The index, unlike the notes it lists,
is rewritten freely.

## When the findings point at a change

If the findings suggest changing an artefact of the chain, Claude
proposes the change explicitly, through `/forge <state>`. It never
makes the change silently, and the research itself changes nothing in
the chain.

## See also

- [About sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
