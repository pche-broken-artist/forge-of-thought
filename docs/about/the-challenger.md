---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: c8eba0d7e0f313ff
inputs:
  - .claude/skills/challenger-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0420
  - projects/forge/10-intent.md#POS.0440
  - projects/forge/10-intent.md#POS.0450
  - projects/forge/10-intent.md#POS.0790
---

# The challenger

The challenger is a reviewer that attacks the substance of the
thinking in a project, never the quality of its documents. This page
says what a challenger persona goes after, how it works, what it
produces and why it is allowed to be wrong. It is for anyone who runs
one, judges its report or wants to add a persona: the user, the
extender and the evaluator alike. How a run is started is the page
[Challenge the thinking](../use/challenge-the-thinking.md); which
personas exist is the page
[Challenger personas](../reference/challenger-personas.md).

## What it is

A challenger is one isolated agent per persona, named
`challenger-<persona>`. Isolated means it runs as a subagent (an agent
launched apart from the working conversation) and sees nothing of what
the principal (the person whose thinking is being forged) and Claude
have said to each other. Its task is its whole brief.

A persona is defined by the blind spots it exists to find. Each
persona carries a register of its own, the voice and standpoint it
reads from, and a list of what it hunts. The challenger speaks as a
peer: its report is headed "Peer review", and it has no stake in the
principal being right.

Its subject is the substance of the target: the whole chain of
artefacts (the versioned documents of a project, brief, intent and
the layers below) when no artefact is named, or one artefact of the
chain when one is. When the whole chain is the target, each challenge
names the artefact it concerns.

Its subject is never document quality. Ambiguity, structure,
traceability and the measurability of wording belong to the critic
lenses. If the thinking is sound but the document is sloppy, the
challenger says nothing.

What every persona shares, that is its subject, its way of working,
the shape of its report and its step in the ledger, is written once,
in one contract (`.claude/skills/challenger-contract/SKILL.md`). A
persona file owns only its Lens section: what it reads, what it goes
after, its categories and its own report sections. A persona may make
a shared rule stricter. It may never rename, drop or duplicate one.
How a persona is added is the page
[Add a challenger persona](../extend/add-a-challenger-persona.md).

## How it works

### What it reads

The challenger reads the whole chain above and around the target:

- the briefs (`00-brief*.md`)
- the intent (`10-intent.md`) and the project's threads
  (`threads.md`)
- the decisions (`decisions.md`)
- `sources/`, where present
- every layer below the intent that exists
- the previous reports in `challenges/`

It reads and never modifies. Context is everything; the challenges
aim at the target. Every file it cites is read from disk in its own
run, so that it judges the documents as they stand, not as a copy in
its context remembers them.

### How it challenges

- It reads for what is not there as much as for what is. Silence in
  the intent is its richest material.
- It grounds itself externally when a claim hinges on how the world
  actually works: how comparable organisations solve the matter, what
  the known failure rates and patterns are. It may search the web for
  that, never for padding. On a purely technical trade-off it lets
  the mechanism lead, not an analyst's framework.
- It never fabricates. A precise "I don't know the current figure"
  beats an invented statistic or a hallucinated citation. Any number,
  benchmark or citation it reconstructs from memory rather than
  verifies is flagged as such.
- It corrects a flawed assumption in the material before building on
  it. A challenge stacked on the material's own error is worthless.
- It is concrete. "Consider stakeholder alignment" is worthless. "The
  owners of X and Y both lose scope under this and neither is named
  anywhere in the intent" is a challenge.
- It is sharp and few rather than thorough and long: three to seven
  challenges. Where it has nothing serious to say, it says nothing.
- It marks the severity of each challenge (dealbreaker, major or
  minor) and orders the challenges by it. A fatal flaw is never
  buried in a flat list next to cosmetic ones.
- It is direct: no flattery, no hedging, no softening. Where the
  thinking is strong it says so in one line and moves on.
- It never proposes a document edit, a wording or a structure. It
  challenges the thinking; the principal decides what to do about it.
- It may be wrong. Where a challenge rests on facts it cannot verify
  from the artefacts, it says what it assumes and asks.

Each challenge carries:

- a severity: dealbreaker, major or minor
- the challenge itself and why it matters
- what would change its mind: falsifiable and concrete
- an epistemic status: consensus, active debate, emerging practice,
  or its own judgement

### What it produces

The challenger writes one dated report into the project's
`challenges/` directory, named `YYYY-MM-DD-challenge-<persona>.md`,
in English. The report is immutable from the moment it is written. A
second run of the same persona on the same day takes the suffix `-2`.
The report names its target, every file read with its version where
one exists, and the persona with its register. It holds:

- an overall read: what the initiative is really about as written,
  and whether it is aimed at the right thing
- the challenges, each with the ID `CHL.NNNN`, continuing the
  project's global sequence, never renumbered
- what is strong, briefly, and only what genuinely is
- the questions it cannot answer from the documents: things the
  principal knows and the challenger does not, which often invalidate
  or sharpen a challenge

Then it adds one row per new challenge to the Challenges table of the
ledger (the project's one file of state, `ledger.md`), in the state
`open`. It touches no finding of a critic and no other document.

A challenge in the state `open` is not yet judged. The principal
judges each one, and the state in the ledger then carries the word of
his verdict. Every challenge ends either fixed or explicitly rejected
with a recorded reason, as a decision record (`DEC`). Rejecting and
parking are legitimate outcomes. Silently ignoring is not.

## Why

**Why substance and never document quality.** Formal document review
belongs to the critic lenses. The challenger does not duplicate it,
so that each reviewer has one job and the principal gets one kind of
result from each.

**Why personas, and why each is defined by its blind spots.** What a
persona goes after is its own Lens; the contract is invariant whatever
the persona. A new persona is created only by the principal's
decision, when first needed, and only where its blind spots genuinely
differ from the existing ones. Personas that would say the same things
in different words are noise.

**Why the contract is written once.** The shared behaviour of a kind
of reviewer is a contract, never a copy. One owner means the protocol
changes in one place, and a persona cannot drift from it.

**Why no fabrication and an epistemic status on every challenge.** The
principal needs signal. A challenge that rests on an invented figure
or a reconstructed citation is worse than none, because the principal
cannot tell it from a grounded one. The status says how far the
challenger's claim is shared knowledge and how far it is only its own
judgement.

**Why the challenger may be wrong.** Isolation is not independence.
The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation: it only means the artefact is consistent under one set of
priors. The calibration point lies outside, in review by humans or by
a different model family, invited at the principal's discretion. This
is why a challenge says what it assumes, and why it asks what it
cannot answer.

**Why it is best run before the next layer is derived.** An artefact
is best challenged before the next layer is first derived from it:
the intent before the first assignment, for instance. At that point
an accepted challenge is still cheap to absorb; once a layer below
has been built on the artefact, mending it costs more. Whether the
challenger runs again later, after a draft or before approval, is left
to the judgement of whoever is running the process. No rule prescribes
it.

**Why a rejected challenge is healthy.** The challenger challenges;
the principal decides. Nothing enters the intent because a reviewer
wrote it, only because the principal composed it. A challenge may
inspire, but it is one reading under one set of priors, and it may be
wrong. A rejection with a recorded reason is therefore a decision
taken, not a review wasted. What is not allowed is silence: a
challenge that is neither fixed nor rejected has not been judged.

**Why an accepted challenge is mended where it needs to be.** An
accepted challenge is mended wherever it needs to be, and one that
mends nothing was not accepted. It may change the intent by
subtraction as readily as by addition. A challenge of a layer below
the intent is mended in that layer and changes nothing above it. The
one exception is a challenge that shows that what is wanted cannot be
realised, or only at a price not worth paying. Then a thread is opened
in the intent, citing the challenge, and what is wanted is decided
there. So a challenge goes above its layer only as a thread, never as
an edit, because what is wanted is decided in the intent and nowhere
else.

## A worked example

One challenge, as a persona would write it, for a made-up intent that
proposes to merge three internal help desks into one service desk.
The project, the persona and the figures are placeholders; nothing of
it comes from a real project.

```markdown
### CHL.0030 — The three desks are merged, their three escalation paths are not
- **Severity:** major
- **Challenge:** The intent treats the three help desks as one
  service with three entrances. Each desk today escalates to a
  different line organisation, and the intent is silent on where a
  ticket goes after first-line in the merged desk. Silence here is
  not a detail left to the recipients: it decides who owns the
  outcome.
- **Why it matters:** The merged desk will route escalations by
  whichever rule its first team writes down. The three line owners
  then discover the routing after it is live, and the merger is
  relitigated in the first quarter.
- **What would change my mind:** A position in the intent that names
  the owner of second-line for each of the three ticket classes, or
  a deliverable that assigns that decision to a named recipient with
  a date.
- **Epistemic status:** my judgement; the pattern of post-merger
  escalation conflicts is widely reported, the figures I would
  attach to it I cannot verify from the documents.
```

What the example shows: the challenge is about what is not there, not
about wording; it names a second-order effect; it says what would
falsify it; it marks that the pattern is the challenger's judgement
and that it has no verified figure. It proposes no text for the
intent. What becomes of it is the principal's verdict, recorded in the
ledger and, if rejected, in a decision record with the reason.

## See also

- [Challenge the thinking](../use/challenge-the-thinking.md): running
  a persona.
- [Challenger personas](../reference/challenger-personas.md): the
  personas and what each hunts.
- [Add a challenger persona](../extend/add-a-challenger-persona.md):
  adding a persona of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
