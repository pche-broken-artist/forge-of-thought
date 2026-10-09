---
generated: 2026-10-09
made: derived
inputs-hash: afebd49817fed550
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the isolated reviewers

This page explains what the forge's reviewers are, how they run and
why they are built the way they are. It is for anyone who uses
the forge and wants to know what a review is worth, for anyone who
extends it with a new lens, persona or check, and for anyone judging
whether the design holds. It was put together from `CLAUDE.md`
(its section Isolated reviewers, which gives the mechanism) and
from the design positions and one rejected direction of the forge's
own intent, `projects/forge/10-intent.md`, which give the reasons.

## Three kinds, one shape

The forge has three kinds of reviewer. Each has one job, and none
does another's:

- The **critic** judges document quality, never substance. It runs
  as `/critique <lens> [artefact]`; a lens is one way of reading. It
  produces findings (`FND`) in `reviews/`, one dated file per run.
- The **challenger** judges the substance of the thinking, never
  document quality. It runs as `/challenge <persona> [artefact]`; a
  persona is defined by the blind spots it exists to find. It
  produces challenges (`CHL`) in `challenges/`, one dated file per
  run.
- The **check** verifies mechanical conformance with the
  conventions, never substance or quality. It runs as
  `/check <check> [slug]`; each check owns one concern and none
  another's. It produces findings (`FND`) in `reviews/`, and a run
  that finds nothing files nothing.

The critic and the challenger take an optional target: an artefact
of the chain, named as the state map names it (`brief`, `intent`,
`assignment`, a later layer). Without a target they read the whole
chain. A check takes a project by its slug, or the engine itself.
Bare `/critique`, `/challenge` and `/check` list what is available
and recommend a fit; that roster is not repeated here.

All three share one shape: an isolated agent, run by hand, a
report that is immutable and dated, rows in the ledger, and a
settlement by walkthrough. The check was deliberately built on the
same mechanism as the other two rather than on one of its own, so
that the mechanism takes further kinds as they come.

### Why review and challenge are two reviewers

Merging document review and substantive challenge into one reviewer
was considered and rejected. An agent doing both does neither
properly: the formal audit benefits from a clean context, while the
substantive challenge benefits from a different register entirely.
So the critic and the challenger are kept apart, with strictly
separate jobs and separate outputs.

## Isolation: why the reviewers are blind

Every reviewer runs as an isolated subagent. It sees the project's
documents only and never the working conversation in which the
documents were made. It cannot be told what was meant; it can only
read what was written. That blindness is the source of its value:
if a position is clear only to someone who sat in the conversation,
the reviewer will not understand it, and that is exactly the
finding wanted.

The reviewers run on the session model, the same model the whole
forge runs on. Speed is bought with context, never with a weaker
reviewer: the work is reasoning-heavy, so the strongest available
model is the default and no agent is pinned to a lesser one.

A reviewer's report is a public file, or may be quoted into one.
Instance facts, whatever the local configuration and the
assistant's memory carry (names, roles, addresses, hosts), never
enter a report, not even where they would explain a finding.

## By hand, advisory, settled by walkthrough

No reviewer runs on Claude's own judgement. Each is invoked by hand
by the principal. What a save and a release run is defined by those
commands themselves, not by the reviewers.

Nothing blocks. There are no hard quality gates: findings and
challenges are advisory, and the principal alone decides what is
published. But advisory is not ignorable. Every finding and every
challenge is either fixed or explicitly rejected with a recorded
reason in the project's decisions. Rejecting and parking are
legitimate outcomes; silently ignoring is not. The states in the
ledger carry the words of the walkthrough's verdicts; `open` means
only not yet judged, and `resolved` is the critic's word for a fix
that is in the document.

An accepted challenge is mended wherever it needs to be, and one
that mends nothing was not accepted. A challenge of a layer below
the intent is mended in that layer and changes nothing above it,
unless it shows that what is wanted cannot be realised, or only at
a price not worth paying: then a thread is opened in the intent,
citing the challenge, and what is wanted is decided there.

The best moment to challenge an artefact is before the next layer
is first derived from it, for example the intent before the first
assignment, while accepted challenges are still cheap to absorb.
Whether a reviewer runs again later, after a draft or before an
approval, is left to the judgement of whoever runs the process; no
rule prescribes it.

## Contract and lens

The shared behaviour of each kind of reviewer is written once, in a
contract: one skill per kind (`.claude/skills/critic-contract/`,
`.claude/skills/challenger-contract/`,
`.claude/skills/check-contract/`). Each lens, persona or check is
one agent file (`critic-<lens>`, `challenger-<persona>`,
`check-<name>`) that names its contract in its front-matter and
owns its Lens section and nothing else of the shared behaviour.

The contract owns conduct and isolation, the subject and its
boundary, the way of working, the shape of the report and the
ledger step. The lens file owns what it reads, what it goes after,
its categories and its own report sections. A lens is a
specialisation of its contract, never a replacement: it may narrow
what is read or make a shared rule stricter, but it never renames,
drops or duplicates a shared rule or field. The protocol changes in
the contract alone, and the contract never names a lens.

There is one contract per kind and no common one above them,
because the shared texts of the three kinds differ almost whole;
the few sentences common to all stay in each contract in its own
words. New lenses, personas and checks come only by the principal's
decision, and only where what they would find genuinely differs:
two personas that would say the same things in different words are
noise.

## Isolation is not independence

The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will
find. Agreement between the reviewers is therefore never treated as
validation: it only means the artefact is consistent under one set
of priors. The calibration point lies outside the forge, in review
by humans or by a different model family, invited at the
principal's discretion.

A challenge may inspire, but it supplies nothing. Nothing enters
the intent because a reviewer wrote it, only because the principal
composed it; and an accepted challenge may change the intent by
subtraction as readily as by addition.

## See also

- [About the critic](the-critic.md): what the critic judges.
- [About the challenger](the-challenger.md): what the challenger judges.
- [About the check](the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings are settled.
