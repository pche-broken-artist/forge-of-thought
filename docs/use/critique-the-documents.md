---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
---

# Critique the documents

This page is for the person who wants a project's documents read for
quality by an independent reviewer. It says how to run `/critique`,
what happens during the run and what you see when it ends.

## The command

```
/critique [lens] [artefact] [slug]
```

All three arguments are optional. The command only chooses the lens,
passes the project to the reviewer and checks the bookkeeping
afterwards. What each lens looks for is not set by the command.

## See the lenses first

Run `/critique` with no arguments. It lists the available lenses and
recommends the one that fits the project's state, going by the fit
each lens states about itself. The recommendation is advice, not a
gate: you choose.

## Run a lens

Run `/critique <lens>`. The project is taken from context; if that is
ambiguous, you are asked which one.

One isolated reviewer reads the project's documents and nothing else.
It never sees your working conversation, and it is not told what the
author meant. It judges only what the documents say. It judges their
quality as documents, read through the lens you chose. It never judges
the substance of your thinking: whether the objective is the right one
or the plan is wise is a different review, the challenge. If a
document is sound but the thinking behind it is wrong, the critic says
nothing.

The reviewer writes a dated report in the project's `reviews/`
directory. The report is immutable once written. It holds the
findings, each numbered `FND.NNNN`, and the project's ledger gets a
row for each new finding. Findings have a severity and a category;
the reference and the explanation page below say what they are.

### Narrow the run to one artefact

Add a target to run the lens on one artefact only, named as `/forge`
names it: `brief`, `brief-<name>`, `intent`, `assignment`, or a later
layer the project has. Without a target the lens reads the whole
chain. How a target narrows a lens is stated by the lens itself.

### Pick the project

Add the project's slug as the last argument, for example
`/critique <lens> intent <slug>`.

## What you see afterwards

When the reviewer returns, the command first checks that the review
file exists and that the ledger is updated, and mends the ledger
bookkeeping if needed. It never alters the findings. Then it tells you,
in your conversation language, the delta against the previous runs of
that lens:

- new findings, with their severity;
- findings that were marked resolved and have now been verified as
  resolved;
- findings still open;
- findings that have become obsolete;
- what awaits your verdict.

For the `essence` lens, the distillations come first, because the
findings rest on them.

It ends with an offer to settle the open findings in a walkthrough,
one finding at a time. If you accept the offer, the walkthrough runs
as described on the walkthrough page. If you decline it, the findings
wait. When you give the verdict `accept` on a finding, the artefact
concerned is iterated through `/forge` and the finding is marked
`resolved`. The other verdicts are the walkthrough's.

## When a lens runs

A critic is never run on Claude's own judgement; every run is your
word. A save runs no lens. What a release offers is the release
command's to say.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of
  today and what each goes after.
- [Walk through a list](walk-through-a-list.md): settling the
  findings one by one.
- [About the critic](../about/the-critic.md): what the critic judges
  and why it is blind.
