---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: cf17dfe26672e58c
inputs:
  - .claude/skills/research/SKILL.md
  - templates/index.md
---

# Research a topic

`/research` looks up current best practice on one question and files the answer as a durable, indexed note in a project. This page is for the principal (the person whose thinking is being forged) who wants to ground a decision in what the world has already solved instead of reinventing it.

## When to use it

Use it when a question of your project has an answer that others have already worked out, and you want that answer with its sources before you decide. What research is for and why its notes never change is explained in [Sources and research](../about/sources-and-research.md).

## The command

```
/research <topic> [slug]
```

The last word is the project slug if it names a project; everything before it is the topic. Without a slug, Claude takes the project you are working in.

Example, with a placeholder slug:

```
/research release checklists for small teams my-project
```

## What happens

1. Claude searches the web for current best practice, established frameworks and notable recent developments. It prefers primary and high-quality sources and notes their publication dates. It marks each finding as consensus, emerging or contested.

   You should now see Claude working through sources on your one question.

2. Claude writes the note into the project's `research/` directory, as `research/YYYY-MM-DD-<topic-slug>.md`, in English. The note holds:
   - the question
   - the key findings, each with its sources
   - the options, with their trade-offs
   - a short section on relevance to this project, with a concrete recommendation

   You should now see a new dated file in `research/`.

3. Claude adds an entry to `research/00-INDEX.md`, creating the index if it is missing. The entry has three fields: Question, Answer in short and Consult when. Claude also adds a row to the Research table of the project's ledger (the single record of the project's state).

   You should now see the entry in the index and the row in the ledger.

4. Claude summarises the note for you. The summary leads with the recommendation and the trade-offs, not with a review of the literature.

   You should now see the recommendation first.

5. If the findings suggest a change to an artefact of the chain, Claude proposes it explicitly and points you to `/forge <state>`. It never changes the artefact silently.

   You should now see a proposal, or nothing if no change follows.

## What you have afterwards

- One immutable, dated note in `research/`. It is not edited later.
- An index entry that tells you, without re-reading the note, what it asked, what it concluded and when to open it.
- A registration row in the ledger.
- A recommendation you can accept, change or ignore. The decision stays yours.

## If something goes wrong

- A topic that turns out to be several questions becomes several notes, each answering one question. Claude never writes one combined document.
- No stop condition or error message is recorded for this command.

## A worked example

You run, in a project with the placeholder slug `my-project`:

```
/research how small teams keep a changelog my-project
```

Claude finds that keeping a changelog by hand is consensus, that generating it from commit messages is emerging, and that a single format for both is contested. It writes `research/2026-10-11-changelog-practice.md` with the question, the findings and their sources, the options with trade-offs, and a recommendation for `my-project`. It adds the index entry and the ledger row. It then tells you the recommendation first, with the trade-offs. If the recommendation would change an artefact, it proposes that through `/forge <state>` and waits for you.

## See also

- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
