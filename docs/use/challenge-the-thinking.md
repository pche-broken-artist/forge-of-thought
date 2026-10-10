---
generated: 2026-10-10
made: mirrored
inputs-hash: 96975a3bcb4c39c2
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md
  - CLAUDE.md
---

# Challenge the thinking

This page is for the person who wants the substance of a document
attacked before more is built on it. It says how to run `/challenge`,
what comes back and what you do with it.

## What it does

A challenge is a peer review of the thinking, never of the document.
One isolated agent, a persona, reads the project's documents and
attacks what the target says: its assumptions, its gaps, what it
leaves silent. Wording, structure and traceability are not its job;
that belongs to the critic.

## Step 1: see the roster

Run the command bare:

```
/challenge
```

You see the personas that exist and a recommendation of which fits the
project's subject. The recommendation is advice, never a gate.

## Step 2: run a persona

```
/challenge <persona> [artefact] [slug]
```

- `persona` is the one you chose from the roster.
- `artefact` is the target, named as `/forge` names it. Without one,
  the persona takes the whole chain.
- `slug` is the project; Claude infers it from context and asks if it
  is ambiguous.

The agent sees only the project's documents, never your conversation.
It writes a dated report in the project's `challenges/` directory.
The report is immutable. It holds three to seven challenges, ordered
by severity. Each challenge is falsifiable (it says what would change
the agent's mind) and carries an epistemic status: consensus, active
debate, emerging practice or the agent's own judgement. The report
also says what is strong and lists the questions the agent cannot
answer from the documents. New challenges are entered in the ledger
as open.

## When to run it

Best before the next layer is first derived from the target. For the
intent, that means before the first layer below it, while an accepted
challenge is still cheap to absorb. Run it again after any major shift
of direction. On a near-final artefact it is late but not useless.

## What you see

When the agent returns, Claude first checks that the report and the
ledger entries exist. Then it shows you:

1. The overall read of the thinking.
2. Each challenge compressed to two or three sentences.
3. Claude's own disagreement with a challenge, where it has one,
   said plainly and separately, marked as its own view.
4. Answers to the agent's open questions where the answers exist in
   your conversation but not in the documents. Claude flags these,
   because they usually mean something true is missing from the
   documents.
5. An offer of a walkthrough of the challenges.

## Settling the challenges

Accept the walkthrough and the challenges are settled one by one with
the usual verdicts. `accept` means the challenge is mended through
`/forge` in the artefact it concerns, and its state becomes
`accepted`. If you decline the walkthrough, the challenges wait.

A rejected challenge is a healthy outcome, not a failure. So is one
that survives three rounds unresolved: park it and move on.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today and what each hunts.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [About the challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
