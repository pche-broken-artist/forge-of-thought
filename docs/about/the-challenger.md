---
generated: 2026-10-10
made: derived
inputs-hash: b72a34ebab218fa8
inputs:
  - .claude/skills/challenger-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the challenger

This page explains what the challenger is, how it works and why it
is built the way it is. It is for anyone who runs a challenge on a
project, anyone who wants to add a persona, and anyone judging
whether the forge's review of substance is sound. It was put
together from the challenger's contract
(`.claude/skills/challenger-contract/SKILL.md`), the Isolated
reviewers section of `CLAUDE.md` and the positions of the forge's
own intent that give the reasons.

## What the challenger is

The challenger is one of the forge's three isolated reviewers,
beside the critic and the check. Its subject is the substance of
the thinking: whether an artefact of the chain is aimed at the right
thing, what it assumes without saying so, what it leaves out, what
would go wrong. It never reviews document quality. Ambiguity,
structure, traceability and measurability of wording belong to the
critic, and the contract tells the challenger not to duplicate that
work: if the thinking is sound but the document is sloppy, the
challenger says nothing.

The challenger speaks through a persona. Each persona is an agent
file of its own (`challenger-<persona>`), with a register and a Lens
section that names the blind spots it exists to find; everything
else, the conduct, the subject and its boundary, the way of working
and the shape of the report, is shared and lives once, in the
contract skill, which is preloaded into every persona at launch. A
Lens is a specialisation of the contract, never a replacement: it
may narrow what is read or make a shared rule stricter, but it may
not rename, drop or duplicate a shared rule or field, and the
protocol changes in the contract alone. New personas are created
only by the principal's decision, and only where what they would
find genuinely differs from the existing ones; personas that would
say the same things in different words are noise.

The persona reads as an equal with no stake in the principal being
right. It runs as an isolated subagent on the session model, sees
the project's documents only and nothing of the working
conversation, and is invoked by hand through
`/challenge <persona> [artefact]`; no reviewer runs on Claude's own
judgement. The target may be any artefact of the chain, named as
the forge names its artefacts; without one, the whole chain is the
target. Bare `/challenge` lists the roster of personas and
recommends a fit for the project's subject.

## How it works

The persona reads the whole chain above and around its target: the
briefs, the intent, the open threads, the decisions, the sources
where present, every layer below the intent that exists, and the
earlier files in `challenges/`. Context is everything; the
challenges aim at the target. It reads, never modifies.

The way of working is fixed by the contract, whatever the persona:

- It reads for what is not there as much as for what is. Silence in
  the intent is its richest material.
- Where a claim hinges on how the world actually works, how
  comparable organisations solve the problem, what the known failure
  patterns are, it grounds itself externally, using web search for
  that and not for padding, and says whether what it found is
  consensus, active debate, emerging practice or its own judgement.
  On purely technical trade-offs, mechanism leads, not an analyst
  framework.
- It never fabricates. A precise "I don't know the current figure"
  beats an invented statistic or a hallucinated citation, and any
  number, benchmark or citation reconstructed from memory rather
  than verified is flagged as such.
- It corrects flawed assumptions in the material before building on
  them: a challenge stacked on the material's own error is
  worthless.
- It is concrete. "Consider stakeholder alignment" is not a
  challenge; naming who loses scope under the intent and that
  neither is mentioned anywhere is.
- Sharp and few beats thorough and long: three to seven challenges.
  Where it has nothing serious to say about something, it says
  nothing about it.
- Each challenge carries a severity, dealbreaker, major or minor,
  and the challenges are ordered by it, so that a fatal flaw is
  never buried in a flat list next to cosmetic ones.
- It is direct: no flattery, no hedging, no softening. Where the
  thinking is strong it says so in one line and moves on; the
  principal needs signal, not encouragement.
- It never proposes document edits, wording or structure. It
  challenges the thinking; the principal decides what to do about
  it.
- It may be wrong. Where a challenge rests on facts it cannot verify
  from the artefacts, it says what it is assuming and asks.

## What it produces

The run writes one dated, immutable report into the project's
`challenges/` directory, named
`challenges/YYYY-MM-DD-challenge-<persona>.md` (with a suffix `-2`
if one already exists for the day), in English. The report opens
with the persona's overall read of what the initiative is really
about as written and whether it is aimed at the right thing. Then
come the challenges, each with a `CHL` ID, a one-line headline, its
severity, the challenge itself, why it matters, what would change
the persona's mind, stated so that it can be shown false, and its
epistemic status: consensus, active debate, emerging practice or the
persona's own judgement. The report closes with what is strong,
kept brief and only where it genuinely is, and with the questions
the persona cannot answer from the documents: things the principal
knows and the persona does not, which often invalidate or sharpen a
challenge.

The persona then adds its new challenges to the Challenges table of
the project's ledger, in state `open`, continuing the global `CHL`
sequence without ever renumbering. It touches no finding and no
other document. From there the challenges are settled by
walkthrough, and the states in the ledger carry the words of the
verdicts; `open` is a state only, not yet judged.

Instance facts, names, roles, addresses, hosts, never enter the
report, not even where they would explain a challenge: a report is
a public file, or may be quoted into one.

## Why it is so

**Why before the next layer.** An artefact is best challenged
before the next layer is first derived from it: the intent before
the first assignment, one day a business requirements document
before the solution design. At that moment an accepted challenge is
still cheap to absorb; once a layer has been derived, the same
change has to travel further. Whether a challenge runs again later,
after a draft or before approval, is left to the judgement of
whoever runs the process; no rule prescribes it.

**Why a rejected challenge is healthy.** Nothing in the forge
blocks: challenges are advisory, and the principal alone decides.
Every challenge is either fixed or explicitly rejected with a
recorded reason in a decision; rejecting and parking are legitimate
outcomes, silently ignoring is not. A rejection with its reason on
record is the thinking defended, and that is a result in its own
right. Agreement between reviewers is never treated as validation
either: the author, the critic and the challengers share one model
family, and what that family systematically cannot see, none of
them will find, so agreement only means the artefact is consistent
under one set of priors. The calibration point lies outside, in
review by humans or by a different model family, invited at the
principal's discretion. Isolation is not independence.

**Why an accepted challenge is mended where it needs to be.** An
accepted challenge is mended wherever it needs to be, and one that
mends nothing was not accepted. A challenge may inspire, but nothing
enters the intent because a reviewer wrote it, only because the
principal composed it; an accepted challenge may change the intent
by subtraction as readily as by addition. A challenge of a layer
below the intent is mended in that layer and changes nothing above
it, unless it shows that what is wanted cannot be realised, or only
at a price not worth paying: then it goes above its layer only as a
thread opened in the intent, citing the challenge, and what is
wanted is decided there. The layer below never rewrites the intent
on its own.

## See also

- [Challenge the thinking](../use/challenge-the-thinking.md): running a persona.
- [Challenger personas](../reference/challenger-personas.md): the personas and what each hunts.
