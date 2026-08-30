---
project: forge
kind: thought
updated: 2026-08-30
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
| 10-intent.md | 3.0 | approved | 2026-08-30 |
| 20-assignment.md | — | not planned: the handover artefacts of this project are the core itself (CLAUDE.md, templates/, .claude/) and README.md | — |
| decisions.md | — | 8 records (DEC.0010–0080) | 2026-08-29 |

## Renders
<!-- Generated outputs, one row per recipe in recipes/. Never
hand-edited: iterate the recipe, re-run /render. Row mirrors the
render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.25 | CLAUDE.md, 10-intent.md v3.0 | 2026-08-30 |
| RELEASE-NOTES.md (repo root) | humans tracking the system's evolution | recipes/release-notes.md v0.2 | 10-intent.md v3.0, decisions.md, previous edition (2026-08-30) | 2026-08-30 |

## Sources
<!-- Registration only; what a source is and is for lives in
sources/00-INDEX.md. -->
| File | Date | Date origin | Extract |
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

## Findings
<!-- State: open | resolved | overruled | obsolete. Resolution: assignment
version for resolved, DEC.NNNN for overruled. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | medium | inconsistency | resolved | 2026-08-17-critique.md | README re-rendered, title at intent 2.7 (verified 2026-08-27) |
| FND.0020 | medium | inconsistency | resolved | 2026-08-17-critique.md | intent 2.7 (note under Open threads) (verified 2026-08-27) |
| FND.0030 | low | inconsistency | resolved | 2026-08-17-critique.md | decisions.md header comment updated (verified 2026-08-27) |
| FND.0040 | low | gap | resolved | 2026-08-17-critique.md | DEC.0050 (verified 2026-08-27) |
| FND.0050 | medium | gap | resolved | 2026-08-27-critique.md | intent 2.13 — CLAUDE.md Persistence (portability), script examples neutralised; forge-save instance facts deferred to THR.0090 by decision |
| FND.0060 | low | contradiction | resolved | 2026-08-27-critique.md | intent 2.13 (Essence), CLAUDE.md heading "Two isolated reviewers" |
| FND.0070 | low | divergence | resolved | 2026-08-27-critique.md | README re-rendered at intent 2.13 (2026-08-27, recipe 0.18) |
| FND.0080 | low | inconsistency | resolved | 2026-08-27-critique.md | ledger comments + templates/ledger.md (intent 2.13) |

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
- THR.0090 multi-principal use — deliberately not worked on
  (principal's direction 2026-08-29: principals not to be solved now); the scripts part resolved by POS.0950
- THR.0140 the delivery side — deliberately deferred until a subject
  project needs the linkage
- THR.0150 replacing the PowerShell scripts with POSIX sh — principal
  undecided whether at all; no priority while PowerShell 7 suffices
- One-off migration to the split engine (runbook: research/2026-08-29-split-migration-runbook.md, phases 0 + A–D with rollback; brief steps 1–6: company library, project repositories, CLAUDE.local.md, rewrite of projects/forge within the boundary, public repository with fresh history, verification by a fresh clone) — the operating layer (CLAUDE.md, .gitignore, scripts, templates, commands, readme recipe) changes with it — including removing the TEMPORARY relocation notice from recipes/readme.md (0.23), which is for the last edition on the company host only; then intent 3.0 + git tag. Progress (2026-08-30): phase 0 done (tag pre-split = d600dda, the last edition with the relocation notice, pushed); phase A done (library and both company projects in repositories of their own on the company host, dropped from the engine's index at b4ea967); phase B done on the old history (gitignore, CLAUDE.local.md + template, settings split, local/ removed, four scripts rewritten and tested, templates and commands by kind, CLAUDE.md, readme recipe 0.24) and saved with this commit. C1 done 2026-08-30: projects/forge rewritten within the boundary (POS.0980) — company name, host, e-mail, template file name and one personal project removed from the 2026-08-29 CTO challenge and the public-engine brief, two sentences of company-project content neutralised in the 2026-08-17 CTO challenge and POS.0710; immutability of the two challenges and the locked brief knowingly broken once, here recorded and nowhere in the files; the company project slugs stay by decision. C2 grep (name, host, identity, the removed project, the neutralised phrases) over the tracked tree and file names: clean. C3-prep done 2026-08-30: LICENSE (CC BY 4.0, verbatim legal code), readme recipe 0.25 (Author and licence section — the principal's decision: credit as Petr Chlumsky (PCHe) with the contact address; the one person the README names), LICENSE in the CLAUDE.md layout, README re-rendered. Decisions of the day for THR.0200, to be written into the intent at 3.0: public repository github.com/pche-broken-artist/forge-of-thought (created empty, public), licence CC BY 4.0, exemplar still open; the forbidden-term list dropped as pointless for now (C2 was run with an ad-hoc list; the durable answer is the content guard rail below). C3 done 2026-08-30: private identity set locally, orphan commit 3507545 (62 files), renamed main. C4.1 done: origin = github.com/pche-broken-artist/forge-of-thought (pushed), the company host kept as remote `company`. C4.3 done: the company project archived (read-only, description pointing to the new homes). D1–D4 done 2026-08-30: fresh clone from GitHub (1 commit, 62 files, boundary grep clean, only projects/forge tracked); CLAUDE.local.md and settings.local.json ignored; forge-status engine-only, then a hand-scaffolded projects/test reported "not under git", after git init "no origin"; forge-pull fast-forwarded the engine and skipped test; forge-save test committed with the "not pushed — no origin" note; bare save reported nothing to save in both; clone deleted. D5 done: /forge agentic-platform from its own repository — the map, renders and threads read as before (brief condition 4). D6: intent 3.0 approved 2026-08-30; saved and tagged v3.0 on the public engine. Migration complete; the runbook stays as the record of how it was done. The company host's main is left at the phase-B commit (a717e52) and archived as is — the principal's decision 2026-08-30 after weighing a force push, a default-branch switch and a revert; the last complete monorepo state is the tag pre-split (d600dda, README with the relocation notice). Inputs still to come from the principal: the forbidden-term list, kept outside the repository, for C2; the licence and the public repository for C4; the README exemplar (THR.0200) may wait until after 3.0.
- THR.0210 the guard rail for the public boundary — a standing rule that `projects/forge` never carries the content of a subject project, and where it lives (CLAUDE.md, the reviewer prompts, `/check-forge`); opened 2026-08-30, to be settled at the next iteration
- THR.0180 the output language — left as is; more than one output language solved when a project needs it
- THR.0190 a plugin as a later distribution layer — no preparation
  now; taken up when forge-pull proves an insufficient upgrade channel
- THR.0200 the public face, narrowed at 3.0 to the README exemplar (repository `forge-of-thought` and licence CC BY 4.0 settled in POS.0990)
  name, licence — open, nothing blocks the split
- THR.0170 branch documents — deferred; taken up only if a draft brief needs position-level work before locking
- README footer (`_Last updated_`): kept for now; principal will give further input
