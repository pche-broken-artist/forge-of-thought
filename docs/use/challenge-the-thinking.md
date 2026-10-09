---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md
  - CLAUDE.md
---

# Challenge the thinking

This page is for the person who wants an isolated reviewer to attack
the substance of a project's thinking before building more on it. It
shows how to run `/challenge`, what comes back and how to settle it.

## What the command does

`/challenge [persona] [artefact] [slug]` sends one isolated agent, a
persona, at the substance of the thinking: whether the ideas hold,
not whether the documents are well written. Document quality belongs
to `/critique`, a different command. The agent sees the project's
documents only, never your conversation with Claude.

The three arguments are all optional:

- `persona` chooses which challenger runs.
- `artefact` narrows the run to one artefact, named as `/forge`
  names it: `brief`, `brief-<name>`, `intent`, `assignment`, or a
  later layer. Without it the whole chain is the target.
- `slug` names the project. If it is not clear from context, Claude
  asks.

## See which personas there are

Run `/challenge` bare. You get the list of personas available, each
with the blind spots it hunts, and a recommendation of which one
fits the subject of your project. The recommendation is advice, not
a gate; any persona may be run.

## Run a persona

1. Run `/challenge <persona>`, adding the artefact and the project
   slug when you want to name them.
   For example: `/challenge <persona> intent <project-slug>`.
2. The agent reads the chain above and around the target, and
   looks for what is missing as much as for what is written. Where a
   claim depends on how the world works, it may check outside
   sources, and it says how sure it is. It does not invent figures
   or citations, and it does not propose edits to your documents.
3. It writes a dated report in the project's `challenges/` folder.
   Reports are immutable; a second run on the same day gets its own
   file. The new challenges are entered in the project's ledger as
   open.

The report holds three to seven challenges, ordered by severity so
that a fatal flaw is never buried among small ones. Each challenge
can be proved wrong: it says what would change the agent's mind, and
it states how well founded it is, from consensus to the agent's own
judgement. The report also says what is strong in the thinking and
lists questions the agent cannot answer from the documents.

### When to run it

Run it before the next layer is first derived from the target. For
the intent, that means before the first layer below it, while an
accepted challenge is still cheap to absorb. Run it again after any
major shift of direction. Running it on a near-final artefact is
late but not useless.

## What you see

When the agent returns, Claude first checks that the report exists
and that the ledger is updated, then shows you:

1. The overall read of the project's thinking.
2. Each challenge compressed to two or three sentences.
3. Claude's own disagreement, where it has any, stated plainly and
   marked as its own view, separate from the challenges. Claude does
   not defend earlier drafting choices.
4. Answers to the agent's open questions where the answer exists in
   your conversation but not in the documents. Claude flags these to
   you, because they usually mean something true is missing from the
   intent.
5. An offer to settle the challenges in a walkthrough.

## Settle the challenges

Accept the offer and the challenges are worked one by one; how that
runs is described in [Walk through a list](walk-through-a-list.md).
The verdicts are the walkthrough's. In this setting, `accept` means
the challenge is mended through `/forge` in the artefact it
concerns, and its state becomes accepted. If you decline the
walkthrough, the challenges wait.

A rejected challenge is a normal, healthy outcome: the challenger
may be wrong, and you decide. A challenge that survives three rounds
unresolved can be parked so that you move on.

## See also

- [Challenger personas](../reference/challenger-personas.md): the
  personas of today and what each hunts.
- [Walk through a list](walk-through-a-list.md): settling the
  challenges one by one.
- [About the challenger](../about/the-challenger.md): what the
  challenger judges and why it may be wrong.
