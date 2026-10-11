---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: f2396183dc7b7788
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how you have a challenger persona attack the substance of your work with `/challenge`. It is for the principal (the person whose thinking is being forged) who wants the thinking tested before more is built on it.

## When to use it

Use it before the next layer is first derived from the artefact you want tested. For the intent, that means before the first layer below it, while an accepted challenge is still cheap to absorb. Run it again after any major shift of direction. Running it on a near-final artefact is late but not useless.

A challenge judges the substance of the thinking, never the quality of the document. For the quality of the writing, see [The challenger](../about/the-challenger.md), which also says why a challenger may be wrong.

## The command

To see the personas and a recommendation of which one fits your project, type the command bare:

```
/challenge
```

To run one persona against one artefact of one project:

```
/challenge cto intent my-project
```

The persona and the artefact are both optional after the first word. The artefact is named as `/forge` names it. Without one, the whole chain is challenged. Without a project slug, Claude infers the project from the context and asks if it is ambiguous. The personas of today and what each hunts are listed in [Challenger personas](../reference/challenger-personas.md).

## What happens

1. Claude lists the personas, or, with a persona named, hands the project path and the target to one isolated agent (a subagent that never sees your conversation).

   You should now see, for the bare command, the roster with a recommended fit. The recommendation is never a gate.

2. The agent reads the project's documents and attacks the substance. It writes a dated report in the project's `challenges/` directory. The report is immutable. It holds three to seven challenges ordered by severity. Each challenge is falsifiable and carries its epistemic status. The report also says what is strong and which questions the agent cannot answer from the documents.

   You should now see a new file in `challenges/` and the new challenges recorded as open in the project's ledger (the single record of state). Claude checks both and repairs only the bookkeeping, never the challenges.

3. Claude presents the result to you.

   You should now see the overall read first, then each challenge compressed to two or three sentences. If Claude disagrees with a challenge, it says so plainly and separately, marked as its own view. It does not defend earlier drafting choices.

4. Claude answers the agent's open questions where the answer exists in the conversation but not in the documents, and flags those answers to you. They usually mean that something true is missing from the artefact.

   You should now see which questions were answered from the conversation.

5. Claude offers a walkthrough of the challenges. A walkthrough settles the items one per message, each closed with a verdict. The shape is described in [Walk through a list](walk-through-a-list.md).

   You should now see the offer. If you decline it, the challenges wait.

## What you have afterwards

- A dated report in `challenges/` that is never edited.
- The challenges listed in the ledger, open until you settle them.
- For each challenge you accept, a mend: `accept` means the challenge is mended through `/forge` in the artefact it concerns, and its state becomes `accepted`. The other verdicts are those of the walkthrough.

## If something goes wrong

- If the project is ambiguous, Claude asks which one you mean.
- If you decline the walkthrough, nothing is lost: the challenges stay open in the ledger and wait.
- If a challenge survives three rounds unresolved, park it and move on.
- A rejected challenge is a normal, healthy outcome. It is not a failure of the run.

## A worked example

You have an intent for a project called `my-project` and have not yet derived anything below it.

```
/challenge architect intent my-project
```

Claude reports that the agent has written `challenges/<date>-challenge-architect.md` with, say, four challenges, and opens with the overall read: what the intent is really about as written and whether it aims at the right thing. The first challenge, a major one, says that two positions in the intent cannot both hold. Claude compresses it to three sentences. The agent states what would change its mind: a stated priority between the two positions. Its epistemic status is "my judgement".

Claude adds: "My own view: I disagree with the third challenge, because the intent already rules that case out." It also notes that one open question, about who will run the result, is answered in your conversation but not in the intent, so a fact is missing from the intent. It then offers a walkthrough.

You accept the first challenge and reject the third. The first is mended through `/forge intent my-project`. The third stays in the ledger as rejected.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today and what each hunts.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
