---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: f277f9d4dd17a46b
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how you have a challenger persona attack the substance of your work with `/challenge`. It is for the principal, the person whose thinking is being forged. The command asks one isolated agent to look for blind spots in what you have written and hands you its objections to settle. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Run it before the next layer is first derived from the artefact you want attacked. For the intent, that means before the first layer below it. An accepted challenge is cheap to absorb at that point.

Run it again after any major shift of direction. Running it on a near-final artefact is late but not useless.

The challenge goes at substance, the thinking itself. It never judges the quality of the document.

## The command

```
/challenge [persona] [artefact|path] [slug]
```

All three arguments are optional.

- `persona`: the persona that attacks. The personas of today are listed in [Challenger personas](../reference/challenger-personas.md).
- `artefact|path`: the target. It is an artefact named as `/forge` names it, or any file of the project by its path. Without a target, the whole chain is attacked.
- `slug`: the project. When it is left out, Claude infers it from context and asks if that is ambiguous.

Typed as it stands:

```
/challenge <persona> 10-intent <slug>
```

Bare `/challenge` lists the roster of personas and recommends the one that fits the project's subject. The recommendation is never a gate.

## What happens

1. Claude remakes the project's ledger, the single file of state that every reader of the project works from. You should now see the ledger rebuilt, so that the agent reads a current file.
2. Claude invokes the persona as an isolated subagent, a helper that cannot see your conversation. It is given only the project and the target. You should now see Claude waiting while the agent reads the documents.
3. The agent returns a report and writes no file. The report holds an overall read, the challenges, what is strong and the questions the agent cannot answer from the documents.
4. Claude gives each challenge its number and files the report word for word in the project's `challenges/` folder under a unique dated name. You should now see the report filed, and the ledger remade to include it.
5. Claude presents the report to you. You should now see:
   - the overall read first;
   - each challenge compressed to two or three sentences;
   - any disagreement of Claude's own, said plainly and marked as its own view, never mixed into the challenge;
   - the open questions of the agent, answered by Claude where the answer exists in your conversation but not in the documents, and flagged, because such an answer usually means something true is missing from the intent;
   - the offer of a walkthrough.

## What you have afterwards

You have a filed report that is never edited, and the challenges as entries in the ledger.

If you take the walkthrough, you give each challenge a verdict. Settling them one by one is described in [Walk through a list](walk-through-a-list.md). Here `accept` means the challenge is mended through `/forge` in the artefact it concerns, and the challenge is then in the state `accepted`. The other verdicts are the walkthrough's.

If you decline the walkthrough, the challenges wait.

A rejected challenge is a normal, healthy outcome. A challenge that survives three rounds unresolved is parked, and you move on.

## If something goes wrong

- The project is ambiguous: Claude asks which one is meant. Name the slug.
- The agent cannot answer something from the documents: that appears as a question in the report. It is not a failure. It marks something you know and the documents do not say.
- You disagree with a challenge: say so. Reject it. The agent may be wrong, as [The challenger](../about/the-challenger.md) explains.

## A worked example

You have an intent for a project with the slug `demo`, and nothing yet below it. You type:

```
/challenge <persona> 10-intent demo
```

Claude remakes the ledger, runs the persona and files the report in `challenges/` under a dated name. It then tells you the overall read, for instance that the intent aims at the right problem but leaves one assumption unargued. Each challenge follows in two or three sentences. Claude adds one line marked as its own, saying it thinks the second challenge misreads a position. It offers a walkthrough.

You take it. You accept the first challenge, so Claude mends the intent through `/forge`. You reject the second with your reason. You park the third. The report stays as filed.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
