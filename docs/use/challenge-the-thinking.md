---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 8869f67bd5ee1500
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how to have a challenger persona attack the substance of your thinking with `/challenge`. It is for the principal (the person whose thinking is being forged), who wants the weak points of an artefact found before more is built on it.

## When to use it

Run it before the next layer is first derived from the target. For the intent, that means before the first layer below it. An accepted challenge is cheap to absorb at that point. Run it again after any major shift of direction. Running it on a near-final artefact is late but not useless.

A challenge judges the substance of the thinking, never the quality of the document.

## The command

```
/challenge <persona> [artefact|path] [slug]
```

Bare `/challenge` lists the personas and recommends the one that fits the project's subject. The recommendation is never a gate.

The target is an artefact, named as `/forge` names it, or any file of the project by its path. Without a target, the whole chain is attacked. The slug names the project; Claude infers it from context and asks when it is ambiguous. The personas of today are on [Challenger personas](../reference/challenger-personas.md).

## What happens

1. Claude makes the project's ledger first, so that the agent reads a current file. The ledger is the single source of truth for state, made from the documents when it is read.

   You should now see the ledger remade before the persona runs.

2. One isolated agent, a subagent that sees nothing of your conversation, attacks the substance of the target. It writes no file. It returns a report with three to seven challenges ordered by severity, what is strong in the target, and the questions it cannot answer from the documents.

   You should now see the agent's report come back to Claude.

3. Claude gives each challenge its `CHL` number and files the report word for word in `challenges/` under a unique dated name. Nothing is added, dropped or reworded but the numbers.

   You should now see a new file in `challenges/` named with the date and the persona.

4. Claude presents the report: the overall read first, then each challenge compressed to two or three sentences. If Claude disagrees with a challenge, it says so separately and marks the view as its own.

   You should now see the overall read, each challenge compressed and any disagreement of Claude marked as its own.

5. Where the answers to the agent's open questions exist in your conversation but not in the documents, Claude answers them and flags that to you. Such a gap usually means something true is missing from the intent.

   You should now see those answers flagged, if there are any.

6. Claude offers a walkthrough of the challenges, one item per message with a verdict line. See [Walk through a list](walk-through-a-list.md). If you decline, the challenges wait.

   You should now see the offer of a walkthrough.

## What you have afterwards

- A report in `challenges/`, immutable, with every challenge numbered.
- A refreshed ledger that carries the challenges as rows.
- For each challenge you settle, a verdict. `accept` means the challenge is mended through `/forge` in the artefact it concerns, and its state is `accepted`. The other verdicts are those of the walkthrough.

A rejected challenge is a normal, healthy outcome. So is a challenge that survives three rounds unresolved: park it and move on. For what the challenger judges and why it may be wrong, see [The challenger](../about/the-challenger.md).

## A worked example

The project is `my-project`, and its intent has just been written.

```
/challenge <persona> 10-intent my-project
```

Claude remakes the ledger and runs the persona. The report is filed in `challenges/`. Claude then says that the persona reads the intent as aimed at the right problem, but that it sees five challenges, the first a major one. Each follows in two or three sentences. Claude adds, marked as its own view, that it disagrees with the third. It offers a walkthrough.

You accept the first challenge, so the intent is mended through `/forge`. You reject the third, a healthy outcome. You park the fifth.

Terms of the forge are gathered in the [Glossary](../reference/glossary.md).

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
