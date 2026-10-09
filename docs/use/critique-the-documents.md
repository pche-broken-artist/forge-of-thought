---
generated: 2026-10-09
made: mirrored
inputs-hash: 376c3dfb0b76bf0d
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
---

# Critique the documents

This page is for the person who wants an independent reader to judge
how well a project's documents are written. It shows how to run
`/critique`, what happens during the run and what you are given at
the end.

## What a critique is

A critique judges the quality of your documents as documents, read
through one lens. It never judges the substance of your thinking:
whether the objective is the real problem or the plan rests on sound
assumptions is the work of the challenger, not the critic.

The critic runs as one isolated agent. It sees the project's
documents only and never the conversation, so it cannot be told what
you meant: it judges what the documents say. Its findings are
advice. You decide, and rejecting a finding is a legitimate outcome.

## See the lenses

Run the command bare:

```
/critique
```

You get the roster of lenses, one per critic agent, each with the
fit it states for itself, and a recommendation of which lens suits
the project's state. The recommendation is never a gate. The lenses
of today and what each goes after are on the page
[Critic lenses](../reference/critic-lenses.md).

## Run a lens

```
/critique <lens> [artefact] [slug]
```

- `<lens>` is the lens you chose from the roster.
- `[artefact]` is optional. It narrows the run to one artefact,
  named as `/forge` names it: `brief`, `brief-<name>`, `intent`,
  `assignment` or a later layer. How a lens narrows its work is the
  lens's own. Without a target the lens reads the whole chain.
- `[slug]` is the project. If it is not given, it is taken from
  context, and if that is ambiguous you are asked.

Every run is your word. No lens runs at a save. What a release
offers is the release's own matter.

## What the critic does

Before it looks for anything new, the critic re-tests every earlier
finding of its own lens that was marked resolved, and reports each
as verified or reopened. It respects findings you rejected and does
not raise them again unless the document changed in a way that
materially alters the situation. It prefers a few sharp findings to
many trivial ones.

It then writes a dated report in the project's `reviews/` directory.
The report is immutable: it is never edited afterwards, and
corrections happen downstream. The findings, numbered FND, are also
entered in the project's ledger. The report's shape and the
vocabulary of its findings are described in the pages on the
critic.

## What you see afterwards

When the critic returns, the command checks that the review file
exists and that the ledger is up to date, and mends only the ledger
bookkeeping, never the findings. Then it tells you, in the
conversation:

- the new findings, with their severity;
- the findings verified resolved;
- the findings still open;
- the findings that became obsolete;
- what awaits your verdict.

Some lenses first show the distillations their findings rest on.

The command ends by offering a walkthrough of the open findings. In
a walkthrough you settle them one at a time; see
[Walk through a list](walk-through-a-list.md). Choosing `accept` on
a finding means an iteration of the artefact concerned through
`/forge`, after which the finding is marked resolved. The other
verdicts are the walkthrough's. If you decline the walkthrough, the
findings simply wait.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today and what each goes after.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [About the critic](../about/the-critic.md): what the critic judges and why it is blind.
