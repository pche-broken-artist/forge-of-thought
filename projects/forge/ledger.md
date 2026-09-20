---
project: forge
kind: thought
language: en
terminal: intent
updated: 2026-09-20
---

# Ledger — Forge of Thought

<!-- Single source of truth for state. Freely rewritten (as are the resource indexes,
sources/00-INDEX.md and research/00-INDEX.md); every other document
is versioned or immutable. Keep current after every operation; /ledger
reads from here.
Version scheme: 0.x draft, 1.0 approved, 1.x change after approval, 2.0
next approved version. -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md). Status:
draft (being composed, editable) | approved (locked at 1.0, immutable).
Mined: pending | partial | mined | dropped — how far the intent has
absorbed it; Note says what remains (partial) or the REJ (dropped). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | — | placeholder: brief stage was skipped, intent is the earliest record | — | accepted under DEC.0010, not a check finding |
| 00-brief-public-engine.md | 1.0 | approved | mined | born in the forge 2026-08-29 (THR.0130, THR.0090), locked 2026-08-29 in English after the CTO challenge; mined into intent 2.21 (POS.0940–0980, REJ.0140–0150, THR.0190–0200). Instance work it records — the one-off migration steps 1–6, the first projects after the split — stays here and under Waiting on principal, not in the intent |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 4.17 | draft | 2026-09-20 |
| 20-assignment.md | — | not planned: the handover artefacts of this project are the core itself (CLAUDE.md, templates/, .claude/) and README.md | — |
| decisions.md | — | 13 records (DEC.0010–0130) | 2026-09-20 |

## Renders
<!-- Generated outputs, one row per recipe in recipes/. Never
hand-edited: iterate the recipe, re-run /render. Row mirrors the
render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.49 | CLAUDE.md, 10-intent.md v4.17 | 2026-09-20 |
| RELEASE-NOTES.md (repo root) | the user of the engine who takes upgrades through forge-pull | recipes/release-notes.md v0.10 | 10-intent.history.md, 10-intent.md v4.17, decisions.md, previous edition (released sections) | 2026-09-20 |
| renders/executive-pitch.md | C-level executives whose experience of AI is chatting with it | recipes/executive-pitch.md v0.4 | projects/forge/10-intent.md v4.4, CLAUDE.md | 2026-09-11 |
| renders/cto-pitch.md | technical leadership arriving at the repository - a CTO, a head of engineering or architecture | recipes/cto-pitch.md v0.3 | projects/forge/10-intent.md v4.15, CLAUDE.md | 2026-09-20 |
| renders/ceo-pitch.md | a CEO or another C-level executive whose experience of AI is chatting with it | recipes/ceo-pitch.md v0.3 | projects/forge/10-intent.md v4.15, CLAUDE.md | 2026-09-20 |

## Sources
<!-- Registration only; what a source is and is for lives in
sources/00-INDEX.md. -->
| File | Date | Date origin | Form |
|---|---|---|---|
| forge-run-record-health.md | 2026-09-13 | content | text |

## Dependencies
<!-- Registration only. Documents of other repositories this project
relies on — typically library documents (POS.1020): cited by path from
an index entry, a recipe or the chain. No version: library documents
are maintained by their owner. What the document is for lives where it
is used (the index entry, the recipe). /check verifies each path exists
on disk; /forge reports which libraries the project needs. -->
| Path | Library | Used by | Note |
|---|---|---|---|

## Research
<!-- Registration only; what a note answers lives in
research/00-INDEX.md. -->
| File | Date | Derived from |
|---|---|---|
| 2026-08-25-comparable-projects-landscape.md | 2026-08-25 | 10-intent.md v2.10 |
| 2026-08-29-framework-distribution-in-the-field.md | 2026-08-29 | 10-intent.md v2.17 (POS.0760, THR.0130); landscape research |
| 2026-08-29-claude-code-packaging.md | 2026-08-29 | 10-intent.md v2.17 (POS.0760, THR.0090, THR.0130) |
| 2026-08-29-git-engine-projects-separation.md | 2026-08-29 | 10-intent.md v2.17 (POS.0760, THR.0130) |
| 2026-08-29-split-migration-runbook.md | 2026-08-29 | 00-brief-public-engine.md v1.0; 10-intent.md v2.21 (POS.0940–0980); git research |
| 2026-09-03-version-history-placement.md | 2026-09-03 | 10-intent.md v3.13 (principal's question of 2026-09-03 on the cost of the Version History table); CLAUDE.md Versioning & status |
| 2026-09-05-good-release-notes.md | 2026-09-05 | 10-intent.md v3.34 (THR.0310; POS.0730, release-notes recipe 0.6); RELEASE-NOTES.md as rendered 2026-09-05 |
| 2026-09-07-brd-layer-fork-analysis.md | 2026-09-07 | 10-intent.md v4.0 (POS.0700 growth path; POS.0210, POS.0760, POS.0780, POS.1140); a colleague's fork of the engine at intent 2.8, read from a local clone |
| 2026-09-14-save-and-release-duration.md | 2026-09-14 | the ledger's Waiting section as of 2026-09-14; 10-intent.md v4.9 (POS.1100, POS.0810) |

## Findings
<!-- State: open | resolved | overruled | obsolete. Resolution: assignment
version for resolved, DEC.NNNN for overruled. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | medium | inconsistency | resolved | 2026-08-17-critique.md | README re-rendered, title at intent 2.7 (verified 2026-08-27) |
| FND.0020 | medium | inconsistency | resolved | 2026-08-17-critique.md | intent 2.7 (note under Open threads) (verified 2026-08-27) |
| FND.0030 | low | inconsistency | resolved | 2026-08-17-critique.md | decisions.md header comment updated (verified 2026-08-27) |
| FND.0040 | low | gap | resolved | 2026-08-17-critique.md | DEC.0050 (verified 2026-08-27) |
| FND.0050 | medium | gap | resolved | 2026-08-27-critique.md | intent 2.13 — CLAUDE.md Persistence (portability), script examples neutralised; instance facts left the scripts at 3.0 (verified 2026-09-03, clarity) |
| FND.0060 | low | contradiction | resolved | 2026-08-27-critique.md | intent 2.13 (Essence), CLAUDE.md heading "Two isolated reviewers" (verified 2026-09-03, clarity) |
| FND.0070 | low | divergence | resolved | 2026-08-27-critique.md | README re-rendered at intent 2.13 (2026-08-27, recipe 0.18) — regression belongs to the essence lens |
| FND.0080 | low | inconsistency | resolved | 2026-08-27-critique.md | ledger comments + templates/ledger.md (intent 2.13) (verified 2026-09-03, clarity) |
| FND.0090 | medium | contradiction | overruled | 2026-09-03-critique-clarity.md | DEC.0090; its condition (THR.0220 changing POS.0550) fell at 3.33 with POS.1110 — the contradiction dissolved with it, nothing returns |
| FND.0100 | medium | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0110 | medium | gap | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0120 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0130 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0140 | low | ambiguity | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0150 | low | ambiguity | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0160 | low | duplication | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0170 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | ledger rewritten (intent 3.17) (verified 2026-09-06, clarity) |
| FND.0180 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 (verified 2026-09-06, clarity) |
| FND.0190 | high | inconsistency | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0200 | high | gap | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0210 | high | gap | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0220 | medium | gap | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0230 | medium | ambiguity | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0240 | medium | ambiguity | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-05 (intent 3.30) |
| FND.0250 | medium | contradiction | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-06 (intent 3.41) — the cto persona a CTO in its own right, by the principal's counter-proposal |
| FND.0260 | medium | divergence | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-06 (intent 3.43, POS.1130) — all commands migrated to skills in one round |
| FND.0270 | medium | duplication | resolved | 2026-09-05-critique-harness.md | POS.1120, operating layer 2026-09-06 (intent 3.41) |
| FND.0280 | low | duplication | resolved | 2026-09-05-critique-harness.md | operating layer 2026-09-06 (intent 3.41) — clause deleted from thirteen commands, setup.md keeps its exception |
| FND.0290 | medium | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.0540 rewritten, no counts; CLAUDE.md heading; readme recipe 0.38) (verified 2026-09-06, clarity-2) |
| FND.0300 | medium | duplication | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.1100 owns the split) (verified 2026-09-06, clarity-2 — the owner went stale at 3.44, see FND.0350) |
| FND.0310 | low | ambiguity | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (the variants' word left to THR.0290) (verified 2026-09-06, clarity-2) |
| FND.0320 | low | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (verified 2026-09-06, clarity-2) |
| FND.0330 | low | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (verified 2026-09-06, clarity-2) |
| FND.0340 | low | duplication | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.0840 owns the index) (verified 2026-09-06, clarity-2) |
| FND.0350 | high | contradiction | resolved | 2026-09-06-critique-clarity-2.md | intent 3.45 (POS.1100 owns the current shape; POS.0570, POS.1110) (verified 2026-09-06, clarity-3 — POS.0570 drifting from the owner again, see FND.0420) |
| FND.0360 | medium | contradiction | resolved | 2026-09-06-critique-clarity-2.md | intent 3.45 (contracts renamed <kind>-contract; three contracts, no common skill) (verified 2026-09-06, clarity-3) |
| FND.0370 | low | ambiguity | resolved | 2026-09-06-critique-clarity-2.md | intent 3.45 (one sentence in POS.1140) (verified 2026-09-06, clarity-3) |
| FND.0380 | low | contradiction | resolved | 2026-09-06-critique-clarity-2.md | intent 3.45 (POS.1130) (verified 2026-09-06, clarity-3) |
| FND.0390 | low | duplication | resolved | 2026-09-06-critique-clarity-2.md | intent 3.45 (POS.1120 owns, POS.0400 and POS.0420 cite) (verified 2026-09-06, clarity-3) |
| FND.0400 | medium | ambiguity | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (POS.0120 clause on one date and no measurements; seven positions aligned) |
| FND.0410 | medium | contradiction | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 |
| FND.0420 | low | ambiguity | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (POS.0570 cites POS.1140) |
| FND.0430 | low | contradiction | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (THR.0240 dated) |

The two reviews `2026-08-17-critique.md` and `2026-08-27-critique.md`
carry no lens in their name: reports of the retired single critic,
written before lenses existed (POS.0410). Accepted as they are on
2026-09-11 at the release checks — legacy, not a finding. The two
reviews `2026-09-06-critique-clarity-2.md` and
`2026-09-06-critique-clarity-3.md` carry a run suffix the naming
convention does not have: three runs of one lens on one day. Accepted
as they are on 2026-09-20 — immutable and cited by the Findings rows.

## Challenges
<!-- State: open | accepted | rejected | parked | obsolete. Resolution:
intent version for accepted, DEC.NNNN for rejected. -->
| ID | State | Headline | Source review | Resolution |
|---|---|---|---|---|
| CHL.0010 | accepted | No evidence loop: the forge can improve the artefact forever without knowing whether it worked (dealbreaker) | 2026-08-17-challenge-cto.md | intent 2.8 (POS.0780, THR.0140) |
| CHL.0020 | accepted | The two reviewers are isolated but not independent, and the challenger has functioned as a content supplier (major) | 2026-08-17-challenge-cto.md | intent 2.8 (POS.0790, POS.0800) |
| CHL.0030 | rejected | The growth path contradicts the assignment boundary and displaces the functions that own BA and architecture (major) | 2026-08-17-challenge-cto.md | DEC.0060 |
| CHL.0040 | accepted | Outward-facing documents regenerated by a stochastic process on every save, with no gate and no reviewable diff (major) | 2026-08-17-challenge-cto.md | intent 2.8 (POS.0810) |
| CHL.0050 | accepted | The engine/projects split is decided in the wrong order, and there is no compatibility model at all (major) | 2026-08-17-challenge-cto.md | intent 2.8 (POS.0820, THR.0130 notes; the wrong-order claim rejected within the verdict) |
| CHL.0060 | rejected | Counter-case: the meta-work consumes the scarcest resource and the ceremony is already leaking (major) | 2026-08-17-challenge-cto.md | DEC.0070 |
| CHL.0070 | accepted | Nothing in the brief says the engine is yours to publish — employer IP/policy claim unexamined (dealbreaker, conditional on the contract) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — the engine is the principal's, built outside any work assignment; commit author moves to a private address) |
| CHL.0080 | accepted | Publication has no stated audience; the work is sized for a user the brief says will not come, while the exemplar stays open (major) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — audience stated (company rollout first, public project, showcase); the "drop plugin prep" part moot after CHL.0110) |
| CHL.0090 | accepted | The brief is the first file to fail its own pre-push grep; the leak surface is the immutable forge project, not the scripts (major) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — boundary: nothing company-specific by name in projects/forge; one-off rewrite of immutables before publication; brief locked in English) |
| CHL.0100 | accepted | Libraries are a real cross-repository dependency added with no mechanism, contradicting the research's own argument and loosening source immutability (major) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — library not a publication condition; cross-repo citation accepted knowingly as a visible unguarded pin; two kinds of material named. "Scope creep" part rejected: the library is a split question) |
| CHL.0110 | accepted | The "three free steps" are not free: the CLAUDE.md split moves half the engine's rules from always-on to on-demand, on an overstated 200-line claim (major) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — all plugin preparation dropped for now; git split only. Skills migration part not contested on substance, dropped with the rest) |
| CHL.0120 | rejected | Fresh history discards the git record the design relies on and leaves the only full copy on the employer's server; path-filtering not considered (major) | 2026-08-29-challenge-cto.md | DEC.0080 — fresh history kept; the company copy stays read-only |
| CHL.0130 | accepted | "Upgrade" is a fast-forward of an untagged branch, so the compatibility tool has nothing to compare against; a new project starts unbacked by default (minor) | 2026-08-29-challenge-cto.md | intent 2.21 (via brief 0.5 — git tag per approved major; "nothing to compare against" obsolete (condition 3 narrowed to /check against current conventions, no engine version in projects)) |
| CHL.0140 | accepted | The chain grows downward across principals and repositories, and every mechanism assumes it does not — POS.0700 and THR.0090 are one question (major) | 2026-09-06-challenge-cto.md | intent 3.46 (POS.0700: the chain is the principal's own layer in his own project; the handover case noted in THR.0090) |
| CHL.0150 | parked | THR.0230 is being decided by accretion: every position since 3.0 is the engine's, none the chain's, and the deferral makes the later split a rewrite (major) | 2026-09-06-challenge-cto.md | until after 4.0; noted in THR.0230 (intent 3.46) |
| CHL.0160 | rejected | The upgrade channel has one user, who never upgrades: convention migrations between 3.0 and 3.45 are paid by hand by every other instance (major) | 2026-09-06-challenge-cto.md | DEC.0100 (the migration path stated in POS.0940) |
| CHL.0170 | accepted | Every isolated reviewer receives the instance facts (CLAUDE.local.md, memory) and writes an immutable public file; THR.0210's parking premise is false today (major) | 2026-09-06-challenge-cto.md | intent 3.46 (POS.0950: identities out of the auto-loaded file into identities.local.md; the instance-fact sentence in all three contracts; THR.0210 noted) |
| CHL.0180 | accepted | The intent has become the chronicle it was designed not to be (positions as decision narratives, 1,779 lines) and CLAUDE.md grows with it, 435 → 636 lines in eight days (major) | 2026-09-06-challenge-cto.md | intent 3.46 (POS.0120: what a position carries; the sweep of the intent before 4.0, THR.0240) |
| CHL.0190 | accepted | Release 4.0 is queued and nothing says what an approved major of this intent means — a sign-off with no counterparty and no test (minor) | 2026-09-06-challenge-cto.md | intent 3.46 (POS.0300: what a major of the forge intent means and must pass) |

## Waiting on principal
- Order (2026-09-18, intent 4.12; unchanged since): 1. THR.0390 — the weekend of
  2026-09-19, its four steps in the thread's order; 2. THR.0350's
  leftovers; 3. the briefs `brd` and `layers` side by side.
- THR.0390 — the forge in front of the group; two public pitches
  made 2026-09-20, awaiting the principal's reading.
- THR.0400 — a gate in front of the tools; the reminder half done
  2026-09-20 (intent 4.14), the enforcing hook deferred until after
  THR.0390.
- THR.0350 — walked through (intent 4.9); left: the hook watched in
  the next walkthroughs (POS.1170). The ledger sweep done at 4.10.
- THR.0360 — a layer with an external audience, opened 2026-09-14;
  worked in the brief `brd`, to be born (`/forge brief brd`).
- THR.0370 — Mermaid diagrams in Word; deferred 2026-09-12, open.
- THR.0320 — a `harness` lens; decided in substance 2026-09-05,
  mechanism open, no priority.
- THR.0240 — the size of CLAUDE.md; first instance of the answer at
  4.9 (POS.1170), eight low restatements deferred 2026-09-20 until
  after THR.0390, the rest open.
- THR.0410 — the duration of `/save` and `/release`; the watch
  continues at the next releases.
- DEC.0120 — the force-push of 2026-09-04, recorded; a GitHub cache
  purge only on the principal's request.
- THR.0290 — what `/research` gains from kinds; deferred until a
  second way of researching appears.
- THR.0300 — a user's private layer; merges into the brief `layers`
  (THR.0230).
- THR.0250 — expander and essence manager; parked 2026-09-03.
- THR.0230 — a common engine beneath frameworks; worked as the brief
  `layers` (with THR.0190, THR.0300), after `brd`, research first;
  CHL.0150 parked with it.
- THR.0340 — the README split from the documentation; after
  THR.0230.
- THR.0380 — executive pitch loose ends (S03 counts, the deck build
  without the `pptx` skill); opened 2026-09-14.
- THR.0090 — multi-principal use; deliberately not worked on.
- THR.0140 — the delivery side; deferred until a subject project
  needs the linkage.
- THR.0150 — PowerShell scripts to POSIX sh; undecided, no priority.
- THR.0210 — the guard rail for the public boundary; at stake again
  2026-09-20, to be taken up.
- THR.0190 — a plugin as a distribution layer; merges into the brief
  `layers` (THR.0230).
- THR.0200 — the public face, narrowed to the README exemplar.
- THR.0170 — branch documents; deferred.
