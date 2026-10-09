---
generated: 2026-10-09
made: mirrored
inputs-hash: 1a6f7bb083dbfd89
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
  - CLAUDE.md
---

# Research a topic

This page is for a user who wants the forge to look up what the world
already knows about a question before he decides something in his own
work. It says how to run `/research`, what comes back and what happens
to the findings.

## Run it

```
/research <topic> [slug]
```

The topic is the question you want grounded. The slug names the
project; if the last word you give is the name of a directory under
`projects/`, it is read as the slug and everything before it as the
topic.

## What the command does

1. It searches the web for current best practice, established
   frameworks and notable recent developments. It prefers primary and
   high-quality sources and notes their publication dates.
2. It marks the epistemic status of what it finds: consensus,
   emerging or contested.
3. It writes a note into the project's `research/` directory, named
   `YYYY-MM-DD-<topic-slug>.md`, in English. The note holds:
   - the question;
   - the key findings, with their sources;
   - options with their trade-offs;
   - a short section on relevance to this project, with a concrete
     recommendation.
4. It adds an entry for the note to `research/00-INDEX.md` (creating
   the index if it is missing) and a row to the Research table of the
   project's `ledger.md`.
5. It summarises for you, leading with the recommendation and the
   trade-offs, not a literature review.

## One question per note

A research answers one question. If your topic turns out to be
several questions, you get several notes, each answering one. You
never get one combined document.

## The index entry

Each note's entry in `research/00-INDEX.md` has three fields: the
question, the answer in short, and when to consult the note. The index
is a light catalogue, so that you and Claude know what research exists
and what it is for without opening every note.

## The note is immutable

Once written, a research note is not edited. If the world or your
view changes, a correction comes downstream, in a new note or in the
artefact itself, not in the old note.

## What follows from the findings

If the findings suggest a change to an artefact of the chain, Claude
proposes it explicitly, through `/forge <state>`. Nothing in the chain
is changed silently, and the decision stays yours.

## See also

- [About sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
