---
project: forge
kind: thought
updated: 2026-09-03
---

# Ledger — Forge of Thought

<!-- Single source of truth for state. Freely rewritten (as are the material indexes,
sources/00-INDEX.md and research/00-INDEX.md); every other artefact
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
| 00-brief.md | — | placeholder: brief stage was skipped, intent is the earliest record | — | — |
| 00-brief-public-engine.md | 1.0 | approved | mined | born in the forge 2026-08-29 (THR.0130, THR.0090), locked 2026-08-29 in English after the CTO challenge; mined into intent 2.21 (POS.0940–0980, REJ.0140–0150, THR.0190–0200). Instance work it records — the one-off migration steps 1–6, the first projects after the split — stays here and under Waiting on principal, not in the intent |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 3.19 | draft | 2026-09-03 |
| 20-assignment.md | — | not planned: the handover artefacts of this project are the core itself (CLAUDE.md, templates/, .claude/) and README.md | — |
| decisions.md | — | 9 records (DEC.0010–0090) | 2026-09-03 |

## Renders
<!-- Generated outputs, one row per recipe in recipes/. Never
hand-edited: iterate the recipe, re-run /render. Row mirrors the
render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.33 | CLAUDE.md, 10-intent.md v3.19 | 2026-09-03 |
| RELEASE-NOTES.md (repo root) | humans tracking the system's evolution | recipes/release-notes.md v0.2 | 10-intent.md v3.19, decisions.md, previous edition (2026-09-02, released sections) | 2026-09-03 |
| renders/executive-pitch.md | C-level executives whose experience of AI is chatting with it | recipes/executive-pitch.md v0.1 | 10-intent.md, CLAUDE.md | — (not yet rendered) |

## Sources
<!-- Registration only; what a source is and is for lives in
sources/00-INDEX.md. -->
| File | Date | Date origin | Form |
|---|---|---|---|

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
| FND.0090 | medium | contradiction | overruled | 2026-09-03-critique-clarity.md | DEC.0090 |
| FND.0100 | medium | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0110 | medium | gap | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0120 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0130 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0140 | low | ambiguity | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0150 | low | ambiguity | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0160 | low | duplication | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |
| FND.0170 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | ledger rewritten (intent 3.17) |
| FND.0180 | low | contradiction | resolved | 2026-09-03-critique-clarity.md | intent 3.17 |

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

## Waiting on principal
- Save duration (watch): the first /save with parallel renders and
  the isolated /check-forge (2026-09-02) took twelve minutes — renders
  6:54 in parallel (README 6:54, release notes 2:45), the check 5:00
  with a full /check of the forge project folded in. THR.0220 (the
  cost of rendering at every save) is the lever. Second measurement
  (2026-09-03, save of 3.19): renders 8:18 in parallel (README 8:18,
  release notes 2:24), the check 4:19.
- README render deferred (2026-09-03): the readme recipe went to 0.34
  (the ontological sentence names challenger personas and critic
  lenses) after the README had been rendered from 0.33; the principal
  chose to save with the render stale rather than render again — the
  next /save or /render readme brings it current.
- THR.0260 the Version History out of the document into an append-only
  companion `<document>.history.md`, one rule for every chain document —
  opened 2026-09-03, research done; to be executed on the principal's
  decision, together with THR.0220
- THR.0250 two suggested functions — the expander (a name only) and the
  essence manager, whose detail became the `essence` lens (POS.0410);
  open whether an end-to-end distillation brief → last layer is the
  same lens or a further thing; opened 2026-09-03, parked
- THR.0230 a common engine beneath several frameworks (forge, product,
  project management) — opened 2026-09-03, to be worked out before any
  decision; the second framework in outline comes first; may become the
  first thread turned into a project of its own; the principal undecided
  whether at all
- THR.0240 the size of CLAUDE.md (523 lines) — opened 2026-09-03; to be
  dealt with whatever becomes of THR.0230
- THR.0220 the cost of rendering README and release notes at every
  save — opened 2026-09-02; three candidate solutions formulated in
  the intent (A stale-only plus the principal's word; B save/release
  split with branches left to git; C B plus a branch switch), to be
  weighed with a fresh head
- Executive pitch (since 2026-08-30): five-slide C-level deck of the
  forge, story agreed (S01–S05), recipe `recipes/executive-pitch.md`
  v0.1 with a Renders row. Decided direction, not yet written into the
  intent: the deck is for company management, so recipe and render move
  to `lib-allwyn`, template `sources/allwyn.potx` (to be ingested
  first); one sentence in POS.0970 (a library may carry recipes and
  renders for company audiences whose inputs are other repositories'
  artefacts, registered as Dependencies), one each in `/check` (paths
  out of the repository are cross-repo citations) and `/forge` (a
  library's renders reported with staleness), CLAUDE.md lib layout
  lines. Waits for a round of `/forge intent`.
- THR.0090 multi-principal use — deliberately not worked on
  (principal's direction 2026-08-29: principals not to be solved now); the scripts part resolved by POS.0950
- THR.0140 the delivery side — deliberately deferred until a subject
  project needs the linkage
- THR.0150 replacing the PowerShell scripts with POSIX sh — principal
  undecided whether at all; no priority while PowerShell 7 suffices
- Split migration: complete 2026-08-30 (intent 3.0, tag v3.0). The
  record of how it was done is
  research/2026-08-29-split-migration-runbook.md; the company host's
  main stays at the phase-B commit a717e52, archived read-only; the last
  monorepo state is tag pre-split (d600dda).
- THR.0210 the guard rail for the public boundary — `projects/forge` never carries the content of a subject project; parked 2026-09-03 by the principal, proposed solution recorded in the thread (a check item in `/check-forge` plus one sentence in both reviewer skeletons); taken up when the boundary is next at stake
- THR.0180 the output language — left as is; more than one output language solved when a project needs it
- THR.0190 a plugin as a later distribution layer — no preparation
  now; taken up when forge-pull proves an insufficient upgrade channel
- THR.0200 the public face, narrowed at 3.0 to the README exemplar (repository `forge-of-thought` and licence CC BY 4.0 settled in POS.0990)
- THR.0170 branch documents — deferred; taken up only if a draft brief needs position-level work before locking
- README footer (`_Last updated_`): kept for now; principal will give further input
