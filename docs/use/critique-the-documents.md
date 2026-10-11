---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 3a67fe39395ccc39
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

`/critique` runs a critic lens on the quality of a project's documents. This page is for the principal (the person whose thinking is forged and who gives every command) who wants an independent reading of the documents and a list of what is wrong with them as documents.

## When to use it

- You want to know how the documents read, not whether the thinking is right. A critic judges document quality through one lens and never the substance.
- You want a reading that does not depend on the conversation you have had. The critic is an isolated agent (a subagent, a separate Claude run) that sees the project's documents and nothing of the conversation.

No lens runs at a save. A release offers the `essence` lens once. Every other run is your word.

## The command

```
/critique [lens] [artefact] [slug]
```

- `lens`: the lens to run. Left out, the command lists the lenses.
- `artefact`: optional. Narrows the run to one artefact, named as `/forge` names it, by its definition (for example `intent`). Left out, the run covers the whole chain.
- `slug`: the project. Left out, Claude infers it from the context and asks if it is ambiguous.

A line that can be typed as it stands:

```
/critique clarity intent my-project
```

## What happens

1. Bare `/critique` lists the lenses and recommends the one that fits the project's state. The recommendation follows the fit each lens states about itself. It is advice, never a gate.
   You should now see the roster and one recommended lens. The lenses are described on [Critic lenses](../reference/critic-lenses.md).
2. With a lens, Claude starts the isolated agent for that lens. It receives the project path and the target, nothing else.
   You should now see Claude waiting for the agent to return.
3. The agent reads the project's documents, judges them through its lens and writes a dated report in `reviews/`. The report is immutable. It lists findings (a finding is a critic's result about a document) and the agent records them as rows in the ledger.
   You should now see a new file in `reviews/` named with the date and the lens.
4. Claude checks that the report exists and that the ledger was updated. It repairs the ledger's bookkeeping where needed and leaves the findings as the agent wrote them.
   You should now see the ledger rows for the run.
5. Claude presents the delta summary in the conversation language:
   - the new findings, with their severity
   - the findings verified as resolved
   - the findings still open
   - the findings that became obsolete
   - what awaits your verdict

   For the `essence` lens the distillations come first, because the findings rest on them.
   You should now see the summary and the list of what awaits you.
6. Claude ends by offering a walkthrough of the open findings, one by one. See [Walk through a list](walk-through-a-list.md). Here `accept` means an iteration of the artefact concerned through `/forge`, and the finding becomes `resolved`. If you decline the walkthrough, the findings wait.
   You should now see the offer of the walkthrough.

Findings carry a severity and a category. Their vocabulary is the critic's, described on [The critic](../about/the-critic.md).

## What you have afterwards

- A dated report in `reviews/`, immutable. A second run on the same day gets a numbered suffix.
- The findings as rows in the ledger, open until you settle them.
- A decision for you: walk the findings now or leave them.

## If something goes wrong

- The project is ambiguous: Claude asks which project is meant. Name the slug.
- The report or the ledger update is missing after the agent returns: Claude fixes the ledger bookkeeping. It does not alter the findings.
- You decline the walkthrough: nothing is written, and the findings stay open.

## A worked example

You have worked on the intent of a project called `my-project` and want it read for clarity.

```
/critique clarity intent my-project
```

Claude starts the `clarity` lens on the intent of `my-project`. When it returns, you see a delta summary: on a first run all findings are new. Claude offers a walkthrough. You accept one finding, and Claude iterates the intent through `/forge` to mend it. Later you run the same command again. The summary now shows that finding as verified resolved, the others as still open, and any that no longer apply as obsolete.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today and what each goes after.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
