---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 902614c6336b766f
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

`/challenge` has one isolated reviewer, a persona, attack the substance of an artefact, so that you hear the objections before the next layer is built on it. It is for the principal, the person whose thinking is being forged. The persona judges the thinking, never the quality of the document.

A persona is a reviewer that exists to find one kind of blind spot. It runs as a subagent, a separate Claude run that never sees your conversation with Claude. An artefact is a document of the chain, such as the intent.

## When to use it

- Run it before the next layer is first derived from the artefact. For the intent that means before the first layer below it, while an accepted challenge is still cheap to absorb.
- Run it again after any major shift of direction.
- Running it on a near-final artefact is late but not useless.

## The command

```
/challenge [persona] [artefact] [slug]
```

All three parts are optional.

- Bare `/challenge` shows the roster of personas and recommends the one that fits your project's subject. The recommendation is never a gate.
- `/challenge <persona> [artefact] [slug]` runs the persona. The artefact is named as `/forge` names it. Without one, the persona reads the whole chain. The slug names the project; Claude infers it from context and asks if it is ambiguous.

The personas of today are listed in [Challenger personas](../reference/challenger-personas.md).

## What happens

1. Claude starts the chosen persona on your project and names the target artefact. It passes nothing else, so the persona forms its view from the documents alone.

   You should now see Claude waiting while the persona works.

2. The persona writes a dated report in the project's `challenges/` folder. The report is immutable: it is never edited afterwards. It holds three to seven challenges, ordered by severity, what is strong in the artefact, and the questions the persona cannot answer from the documents. Each new challenge is entered in the ledger, the project's table of state, as `open`.

   You should now see a new file in `challenges/` named with today's date and the persona.

3. Claude checks that the file exists and that the ledger is updated. It fixes the bookkeeping only, never the challenges.

4. Claude presents the result to you.

   You should now see the overall read first, then each challenge compressed to two or three sentences. If Claude disagrees with a challenge, it says so plainly and separately, marked as its own view. It does not defend earlier drafting choices.

5. Where the answer to a persona's open question exists in your conversation with Claude but not in the documents, Claude answers it and flags it to you. Such a question usually means something true is missing from the artefact.

6. Claude offers a walkthrough of the challenges. A walkthrough settles a list one item per message, each closed by the verdict line, as described in [Walk through a list](walk-through-a-list.md).

   You should now see the offer. If you decline it, the challenges wait.

## What `accept` does

Accepting a challenge means it is mended through `/forge` in the artefact it concerns. The challenge is then in state `accepted`. The other verdicts are those of the walkthrough.

## What you have afterwards

- One immutable report in `challenges/`.
- New challenges in the ledger, `open` until you settle them.
- Challenges that you settle by walkthrough, with the accepted ones mended in the artefact.

A rejected challenge is a normal, healthy outcome. So is a challenge that survives three rounds unresolved: park it and move on. The persona can be wrong, as [The challenger](../about/the-challenger.md) explains.

## A worked example

You have a project `my-project` with a finished intent and have not yet written the layer below it.

```
/challenge
```

Claude lists the personas and recommends one for the subject, say `<persona>`.

```
/challenge <persona> intent my-project
```

Claude runs the persona on the intent. It then tells you the overall read, for instance that the intent is aimed at the right goal but rests on an unstated assumption. It gives four challenges in order of severity, each in a few sentences, and adds a line marked as its own: it thinks the third challenge misreads the intent. It closes by offering a walkthrough.

You accept the walkthrough. You accept the first challenge, so Claude mends it in the intent through `/forge`. You reject the third, which is a healthy outcome, and park the fourth.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
