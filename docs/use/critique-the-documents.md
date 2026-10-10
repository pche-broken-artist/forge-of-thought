---
generated: 2026-10-10
made: mirrored
inputs-hash: 7b07137929379738
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
---

# Critique the documents

This page is for the person who wants a critic to read a project's
documents and say where they are weak as documents. It shows how to
start a critique, what comes back and how to settle it.

## What a critique is

A critique judges the quality of the documents, never the substance of
the thinking in them. Whether the idea is right is the job of the
challenger, not of the critic. A critic's findings are advice: you
decide, and rejecting a finding is a legitimate outcome.

One isolated agent does the reading. It sees the project's documents
and never the conversation you are having, so it judges only what the
documents say. Each agent looks through one lens, and the lens says
what it reads and what it goes after.

## See the lenses

Type `/critique` with nothing after it. You get the roster of
available lenses, with a recommendation of which fits the project's
state now. The recommendation is only that; nothing is gated by it.

## Run a critique

Type:

```
/critique <lens> [artefact] [slug]
```

- `<lens>` is the lens to run.
- `[artefact]` is optional. It narrows the run to one artefact, named
  as `/forge` names it. Without it the lens reads the whole chain.
- `[slug]` is the project. If it is left out, it is taken from the
  context, and you are asked if that is ambiguous.

Every run is your own word. No lens runs when you save, and what a
release offers is the release's own matter.

## What the critic leaves behind

The agent writes a dated report in the project's `reviews/` directory.
Reports are immutable: a later run writes a new one and never edits an
old one. Each finding carries an `FND` number, a severity and a
category, and the findings are entered as rows in the project's
ledger. The agent also re-tests the findings of its own lens that were
marked resolved earlier, and reports each as verified or reopened.
Findings you rejected before are not raised again unless the document
has changed materially.

When the agent returns, the command checks that the report file exists
and that the ledger is updated, and mends the ledger bookkeeping if
needed, without touching the findings.

## What you see afterwards

In the conversation you get a summary of what changed since the last
run of that lens:

- new findings, with their severity;
- findings verified as resolved;
- findings still open;
- findings that have become obsolete;
- what awaits your verdict.

For the `essence` lens the distillations come first, because the
findings rest on them.

The summary ends with an offer of a walkthrough of the open findings:
you settle them one by one, each with a verdict. If you decline, the
findings simply wait.

## What accepting means

In this walkthrough, `accept` means an iteration of the artefact the
finding concerns, run through `/forge`, and the finding is then marked
`resolved`. The other verdicts are the walkthrough's own.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today and what each goes after.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [About the critic](../about/the-critic.md): what the critic judges and why it is blind.
