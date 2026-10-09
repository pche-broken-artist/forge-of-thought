---
generated: 2026-10-09
made: mirrored
inputs-hash: 0bc4f249578f167f
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md
  - CLAUDE.md
---

# Challenge the thinking

This page is for the person who wants the substance of a project's
thinking attacked before more is built on it. It shows how to run
`/challenge`, what comes back and how to settle it.

## What the command does

`/challenge [persona] [artefact] [slug]` runs one isolated agent, a
challenger persona, against the substance of your thinking. It judges
whether the thinking is sound, never whether the document is well
written; that belongs to the critic. It sees the project's documents
only, never your conversation with Claude.

## Steps

1. **See who is available.** Run `/challenge` bare. You get the roster
   of personas and a recommendation of which fits the project's
   subject. The recommendation is advice, never a gate.
2. **Run a persona.** Run `/challenge <persona>`. Add an artefact
   (`brief`, `brief-<name>`, `intent`, `assignment` or a later layer,
   named as `/forge` names it) to aim the challenges at it; without
   one, the whole chain is the target. Add the project slug if it
   cannot be inferred from context.
3. **Read what comes back.** Claude presents the result in this
   order:
   - the overall read first;
   - then each challenge compressed to two or three sentences;
   - Claude's own disagreement with a challenge, if any, stated
     plainly and separately, marked as his view;
   - the challenger's open questions that Claude can answer from your
     conversation but which the documents do not hold. These are
     flagged, because they usually mean something true is missing
     from the intent.
4. **Settle the challenges.** Claude offers a walkthrough, one
   challenge at a time (see [Walk through a list](walk-through-a-list.md)).
   If you decline, the challenges wait.

## What the report holds

The agent writes a dated report in the project's `challenges/`
directory. It is immutable once written. It holds:

- three to seven challenges, ordered by severity (dealbreaker, major,
  minor);
- for each challenge, a statement of what would change the
  challenger's mind, so it can be shown wrong, and its epistemic
  status: consensus, active debate, emerging practice or the
  challenger's own judgement;
- a short note of what is strong;
- the questions it cannot answer from the documents.

The challenges are also entered in the project's ledger as open. The
challenger never proposes wording or structure for the documents; you
decide what to do about a challenge. It may also be wrong, and says
what it is assuming where it cannot verify a fact. For why it may be
wrong and what it judges, see [About the challenger](../about/the-challenger.md).

## What each verdict does

`accept` means the challenge is mended through `/forge` in the
artefact it concerns, and its state becomes `accepted`. The other
verdicts are the walkthrough's. A rejected challenge is a normal,
healthy outcome. So is a challenge that survives three rounds
unresolved: park it and move on.

## When to run it

Best before the next layer is first derived from the target. For the
intent, that means before the first layer below it, while an accepted
challenge is still cheap to absorb. Run it again after any major shift
of direction. On a near-final artefact it is late but not useless.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today and what each hunts.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [About the challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
