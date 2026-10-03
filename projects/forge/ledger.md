---
project: forge
kind: thought
language: en
terminal: intent
updated: 2026-10-03
---

# Ledger — Forge of Thought

<!-- Single source of truth for state: CLAUDE.md, Ledger. Versions
per CLAUDE.md, Versioning & status. /ledger reads from here.
Kind: `thought` keeps every table below. `library` (POS.0960) keeps
only Renders, Sources, Dependencies, Research and Waiting on
principal; the Briefs, Documents, Published, Findings and Challenges
tables are deleted at scaffold time; the Findings table returns with
a check's first finding (`.claude/skills/check/SKILL.md`). This
comment is the one owner of that reduction (POS.1070). -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md). Status:
draft (being composed, editable) | approved (locked at 1.0, immutable).
Mined: pending | partial | mined | dropped — how far the intent has
absorbed it; Note says what remains (partial) or the REJ (dropped). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | — | placeholder: brief stage was skipped, intent is the earliest record | — | accepted under DEC.0010, not a check finding |
| 00-brief-public-engine.md | 1.0 | approved | mined | born in the forge 2026-08-29 (THR.0130, THR.0090), locked 2026-08-29 in English after the CTO challenge; mined into intent 2.21 (POS.0940–0980, REJ.0140–0150, THR.0190–0200). Instance work it records — the one-off migration steps 1–6, the first projects after the split — stays here and under Waiting on principal, not in the intent |
| 00-brief-elicitation.md | 1.0 | approved | mined | born in the forge and locked 2026-09-28; mined into intent 4.32 (POS.1300 to POS.1380, POS.0110, REJ.0180, REJ.0210, REJ.0220, THR.0440 to THR.0460; THR.0440 and THR.0450 closed at 4.46). The material for the briefs `brd` and `engine-split` is carried in THR.0230, THR.0300 and THR.0360. Not a model of a brief, see its opening note |
| 00-brief-next-gen.md | 0.2 | draft | pending | born in the forge 2026-10-03, written in English on the principal's word; the needs of the next generation gathered in one round, to be sifted; the eighteen researches of 2026-10-03 cited under its sections (0.2); THR.0520 opened from it |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 4.51 | draft | 2026-10-03 |
| 20-assignment.md | — | not planned: the handover artefacts of this project are the core itself (CLAUDE.md, templates/, .claude/) and README.md | — |
| decisions.md | — | 18 records (DEC.0010–0180) | 2026-10-02 |

## Renders
<!-- Generated outputs, one row per recipe in recipes/ (CLAUDE.md,
Document chain 7). Row mirrors the render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.54 | CLAUDE.md, 10-intent.md v4.49, .claude/agents/, .claude/skills/forge/states/, .claude/skills/, scripts/, templates/ledger.md | 2026-10-02 |
| RELEASE-NOTES.md (repo root) | the user of the engine who has cloned it and takes upgrades through forge-pull | recipes/release-notes.md v0.12 | 10-intent.history.md, 10-intent.history.archive.md, 10-intent.md v4.49, decisions.md, previous edition (released sections) | 2026-10-02 |
| renders/executive-pitch.md | C-level executives whose experience of AI is chatting with it | recipes/executive-pitch.md v0.6 | projects/forge/10-intent.md v4.30, CLAUDE.md | 2026-09-27 |
| renders/cto-pitch.md | technical leadership arriving at the repository - a CTO, a head of engineering or architecture | recipes/cto-pitch.md v0.5 | projects/forge/10-intent.md v4.28, CLAUDE.md | 2026-09-27 |
| renders/ceo-pitch.md | a CEO or another C-level executive whose experience of AI is chatting with it | recipes/ceo-pitch.md v0.5 | projects/forge/10-intent.md v4.28, CLAUDE.md | 2026-09-27 |

## Published
<!-- Designed files made by /publish, one row per file (CLAUDE.md,
Document chain 7). State: current | stale — set to current by
/publish, to stale by every /render of that recipe. -->
| File | Recipe | From render | Model | Published | State |
|---|---|---|---|---|---|
| published/executive-pitch.pptx | recipes/executive-pitch.md v0.4 | generated 2026-09-11, projects/forge/10-intent.md v4.4, CLAUDE.md | opus | 2026-09-11 | stale |
| published/cto-pitch.docx | recipes/cto-pitch.md v0.5 | generated 2026-09-20, projects/forge/10-intent.md v4.15, CLAUDE.md | opus | 2026-09-27 | stale |

## Sources
<!-- Registration only. External inputs, immutable once registered.
Date = best-effort origin date; origin: content | file | ingested. What
a source is and is for lives in sources/00-INDEX.md, never here
(CLAUDE.md, Document chain 5). Form (POS.1040): text | extract
of <original> | binary — one form per source. -->
| File | Date | Date origin | Form |
|---|---|---|---|
| forge-run-record-health.md | 2026-09-13 | content | text |
| word-default-a4.docx | 2026-09-20 | file | binary |
| forge-elicitation-brief-review.md | 2026-09-28 | ingested | text |
| forge-elicitation-brief-review-v0.4.md | 2026-09-28 | ingested | text |

## Dependencies
<!-- Registration only. Documents of other repositories this project
relies on — typically library documents (POS.1020): cited by path from
an index entry, a recipe or the chain. No version: library documents
are maintained by their owner. What the document is for lives where it
is used (the index entry, the recipe). -->
| Path | Library | Used by | Note |
|---|---|---|---|

## Research
<!-- Registration only. Immutable dated notes written by /research (or
recorded expert estimates). What a note answers lives in
research/00-INDEX.md, never here. -->
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
| 2026-09-28-artefact-layers-from-idea-to-handover.md | 2026-09-28 | 00-brief-elicitation.md v0.5 |
| 2026-09-28-human-ai-elicitation-over-artefacts.md | 2026-09-28 | 00-brief-elicitation.md v0.5 |
| 2026-09-29-change-history-of-document-items.md | 2026-09-29 | 10-intent.md v4.33 (THR.0470); the principal's questions of 2026-09-29 |
| 2026-09-29-change-record-file-format.md | 2026-09-29 | 10-intent.md v4.33 (THR.0470); the principal's questions of 2026-09-29 |
| 2026-09-30-how-everything-in-the-forge-is-born.md | 2026-09-30 | the engine's definitions at commit c95cffe; 10-intent.md v4.34 (POS.0120, POS.0700, POS.1130); the principal's question of 2026-09-30 |
| 2026-09-30-adding-a-new-type-to-the-engine.md | 2026-09-30 | the engine's definitions at commit c95cffe, every member of each type searched by name; 10-intent.md v4.34 (POS.0400-0420, POS.0700, POS.0960, POS.1000, POS.1070, POS.1120-1140); research/2026-09-07-brd-layer-fork-analysis.md; the principal's question of 2026-09-30 |
| 2026-10-01-what-of-the-intent-belongs-to-an-assignment.md | 2026-10-01 | 10-intent.md v4.41 read whole; 10-intent.threads.md (THR.0470, THR.0480); CLAUDE.md (prime directive 8, Document chain 2 and 3, Requirement style); research/2026-09-28-artefact-layers-from-idea-to-handover.md; the principal's question of 2026-10-01 |
| 2026-10-02-running-reviewers-without-the-conversation.md | 2026-10-02 | 10-intent.md v4.42 (POS.0400, POS.0540, POS.1120, POS.1140); the principal's question of 2026-10-02 |
| 2026-10-03-what-a-write-touches-and-where-two-authors-collide.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Several people on one project); the engine's definitions and the project `forge` as a sample; 10-intent.md v4.50 |
| 2026-10-03-where-requirements-meet-outside-git.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Several people on one project; Connection to the systems around) |
| 2026-10-03-showing-the-main-news-of-a-version-to-a-reader.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Documentation and news); research/2026-09-05-good-release-notes.md; RELEASE-NOTES.md as rendered 2026-10-02 |
| 2026-10-03-testing-the-behaviour-of-a-prompt-framework.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Testing how the engine behaves); CLAUDE.md and the listing of `.claude/` |
| 2026-10-03-agent-instruction-architecture-beyond-anthropic.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (A technical clean-up); CLAUDE.md and the listing of `.claude/` |
| 2026-10-03-several-authors-on-one-body-of-requirements.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Several people on one project) |
| 2026-10-03-anthropic-guidance-for-claude-code-and-where-the-forge-departs.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (A technical clean-up); research/2026-10-03-operating-layer-architecture-and-debt.md; the engine's operating layer; the researches of 2026-08-29 and 2026-10-02 on Claude Code |
| 2026-10-03-concurrent-work-on-structured-text-in-git.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Several people on one project); research/2026-10-03-what-a-write-touches-and-where-two-authors-collide.md |
| 2026-10-03-how-project-documentation-is-built.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Documentation and news); 10-intent.threads.md (THR.0340); README.md and recipes/readme.md v0.54 |
| 2026-10-03-one-tool-a-core-with-modules-or-several-tools.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (The shape of the whole); 10-intent.threads.md (THR.0230, THR.0420, THR.0300, THR.0140); the researches of 2026-08-25 and 2026-08-29 on the field |
| 2026-10-03-operating-claude-code-for-many-users-in-a-company.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Operation in a company); 10-intent.threads.md (THR.0210, THR.0400) |
| 2026-10-03-operating-layer-architecture-and-debt.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (A technical clean-up); the engine's operating layer as it stood on 2026-10-03; searches of the intent's history and its archive |
| 2026-10-03-the-threshold-of-entry-for-a-non-developer.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (The threshold of entry); the skills `setup` and `new-project`; CLAUDE.md, Persistence |
| 2026-10-03-user-extensions-kept-apart-from-the-core.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (User modifications); 10-intent.threads.md (THR.0300, THR.0480, THR.0190, THR.0230); the researches of 2026-08-29 and 2026-09-30 |
| 2026-10-03-versions-channels-and-migration-of-user-content.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Upgrade and compatibility); 10-intent.md v4.50 (POS.0940, POS.0820, POS.0300, POS.0730) |
| 2026-10-03-work-without-a-known-artefact-and-its-working-files.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Work without a known artefact; Further outputs and working files) |
| 2026-10-03-when-an-agent-may-decide-and-when-it-waits.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Automation); research/2026-10-03-where-the-forge-asks-for-the-principals-word.md; 10-intent.threads.md (THR.0400) |
| 2026-10-03-where-the-forge-asks-for-the-principals-word.md | 2026-10-03 | 00-brief-next-gen.md v0.1 (Automation); the engine's definitions; 10-intent.md v4.50 with its threads, decisions.md, searches of the history, its archive and `sources/forge-run-record-health.md` |

## Findings
<!-- Findings of the critic and of the checks, one sequence. State:
open | resolved | rejected | parked | obsolete. Resolution:
assignment version, or for a check's finding what fixed it, for
resolved; DEC.NNNN for rejected. `overruled` in an older record reads
as `rejected`. -->
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
| FND.0090 | medium | contradiction | rejected | 2026-09-03-critique-clarity.md | DEC.0090; its condition (THR.0220 changing POS.0550) fell at 3.33 with POS.1110 — the contradiction dissolved with it, nothing returns |
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
| FND.0400 | medium | ambiguity | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (POS.0120 clause on one date and no measurements; seven positions aligned) (verified 2026-10-02, clarity) |
| FND.0410 | medium | contradiction | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (verified 2026-10-02, clarity) |
| FND.0420 | low | ambiguity | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (POS.0570 cites POS.1140) (verified 2026-10-02, clarity; the restating half-sentence stays as a residue) |
| FND.0430 | low | contradiction | resolved | 2026-09-06-critique-clarity-3.md | intent 3.48 (THR.0240 dated) (verified 2026-10-02, clarity) |
| FND.0440 | medium | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 |
| FND.0450 | medium | conformance | rejected | 2026-10-02-check-history.md | DEC.0150 |
| FND.0460 | medium | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 |
| FND.0470 | low | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 |
| FND.0480 | low | conformance | rejected | 2026-10-02-check-history.md | DEC.0160 |
| FND.0490 | low | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 (the sentence on `-Model` kept in POS.0740, POS.0930 cites it) |
| FND.0500 | low | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 (the threads' closing note) |
| FND.0510 | low | conformance | resolved | 2026-10-02-check-history.md | intent 4.44 |
| FND.0520 | low | conformance | resolved | 2026-10-02-check-history.md | recipe release-notes 0.12 |
| FND.0530 | low | conformance | resolved | 2026-10-02-check-history.md | recipe executive-pitch 0.7 |
| FND.0540 | high | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the definition owns what a brief carries; CLAUDE.md, `/spinoff`, POS.0060) |
| FND.0550 | medium | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (`/spinoff` cites the Course of the state files) |
| FND.0560 | medium | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the walkthrough skill owns the shared verdicts) |
| FND.0570 | medium | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (CLAUDE.md, Document chain 7; who may start `/publish` kept) |
| FND.0580 | medium | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (`states/assignment.md`) |
| FND.0590 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (`templates/intent.md`) |
| FND.0600 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the skill `ingest`) |
| FND.0610 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (the Commands table of CLAUDE.md cut to the purpose of each command) |
| FND.0620 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (rules echoed inside CLAUDE.md cut to their owner) |
| FND.0630 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (CLAUDE.md, the skills `critique` and `man`, the descriptions of the two critic lenses) |
| FND.0640 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the skills `ingest` and `research`) |
| FND.0650 | low | conformance | parked | 2026-10-02-check-single-source-of-truth.md | needs a pass over the recipe genres and their skeletons |
| FND.0660 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (`templates/index-bundle.md`) |
| FND.0670 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (CLAUDE.md, `states/intent.md`) |
| FND.0680 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the critic contract; CLAUDE.md, Requirement style) |
| FND.0690 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (three agent files) |
| FND.0700 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (six reminders name their owner or left) |
| FND.0710 | low | conformance | rejected | 2026-10-02-check-single-source-of-truth.md | DEC.0170 |
| FND.0720 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (the three contracts cite the skeletons); the quoting caveat kept in the skeletons, DEC.0180 |
| FND.0730 | low | conformance | resolved | 2026-10-02-check-light.md | intent 4.48 (POS.0310, `templates/history.md`) |
| FND.0740 | low | conformance | resolved | 2026-10-02-check-project.md | intent 4.49 (four lines of Waiting on principal cut to a citation) |
| FND.0750 | low | conformance | parked | 2026-10-02-check-project.md | until the next iteration of the recipes `cto-pitch` and `ceo-pitch` |
| FND.0760 | medium | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, What this workspace is) |
| FND.0770 | medium | conformance | resolved | 2026-10-02-check-engine.md | recipe readme 0.52 |
| FND.0780 | medium | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, prime directive 1) |
| FND.0790 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, Document chain) |
| FND.0800 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, Versioning & status) |
| FND.0810 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (POS.0850) |
| FND.0820 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (`templates/recipe-readme.md`, `templates/recipe-release-notes.md`) |
| FND.0830 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0120, POS.1380) |
| FND.0840 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0740, POS.1150, POS.0930) |
| FND.0850 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0940) |
| FND.0860 | low | ambiguity | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.1080, POS.0710) |
| FND.0870 | low | duplication | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.1330, POS.1340, POS.1350, REJ.0220; the older positions own) |
| FND.0880 | low | gap | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (a Facts section saying why it is empty) |

Four review files are named outside the convention — accepted as they
are by DEC.0140.

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
<!-- What waits on the principal, one line per matter: cite, never
copy — CLAUDE.md, Ledger. -->
- THR.0520 — the intent carries the solution, a layer for the
  solution is missing; priority, opened 2026-10-03 (intent 4.51),
  the principal's stance saved, nothing decided.
- THR.0460 — `/recipe` and `/forge`, one dispatcher or two; small,
  open.
- THR.0470 — the intent too long to be read; the migration done and
  released at 4.49; whether large files are split open.
- THR.0400 — a gate in front of the tools; the soft half done, the
  hard half open, nothing scheduled.
- THR.0350 — walked through (intent 4.9); left: the hook watched in
  the next walkthroughs (POS.1170). The ledger sweep done at 4.10.
- THR.0360 — a layer with an external audience, opened 2026-09-14;
  worked in the brief `brd`, to be born (`/forge brief brd`).
- THR.0370 — Mermaid diagrams in Word; deferred 2026-09-12, open.
- THR.0320 — a `harness` lens; decided in substance 2026-09-05,
  mechanism open, no priority.
- THR.0240 — the size of CLAUDE.md; first instance of the answer at
  4.9 (POS.1170), the rules of particular artefacts moved out at
  4.49, the rest open.
- THR.0410 — the duration of `/save` and `/release`; the figures of
  the release of 2026-10-02 saved in the thread, the watch continues.
- DEC.0120 — the force-push of 2026-09-04, recorded; a GitHub cache
  purge only on the principal's request.
- THR.0290 — what `/research` gains from kinds; deferred until a
  second way of researching appears.
- THR.0300 — everything a user makes for himself, kept at his own
  place; widened and set on its own 2026-09-26, a matter of today's
  forge.
- THR.0250 — expander and essence manager; parked 2026-09-03.
- THR.0230 — can the forge be split into an engine and the rest;
  worked as the brief `engine-split` (with THR.0190), research
  first; after `brd` (POS.1380); CHL.0150 parked with it; THR.0480
  to be settled before it.
- THR.0480 — how a new type is added to the engine; opened
  2026-09-30 (intent 4.35), the principal's stance saved, nothing
  decided; any time, before THR.0230.
- THR.0490 — a stale clone goes unnoticed; `/forge` and
  `forge-status` to say the state against the remote and offer the
  pull; opened 2026-10-01 (intent 4.41), where it lives open.
- THR.0500 — the reviewers' mechanism out of the session; filing by
  a script kept for later, research of 2026-10-02; opened 2026-10-02.
- THR.0510 — live reference material by nightly export; the
  principal's thought, nothing decided; opened 2026-10-02.
- FND.0650 — parked finding of the `single-source-of-truth` check;
  needs a pass over the recipe genres and their skeletons.
- FND.0750 — parked finding of the `project` check; the Published
  line of the two pitch recipes, at their next iteration.
- THR.0420 — derivations of the forge for other jobs; nothing
  scheduled.
- THR.0430 — a command that ends a session; research of the
  transcript format first, nothing scheduled.
- THR.0340 — the README split from the documentation; after
  THR.0230.
- THR.0380 — executive pitch loose ends (S03 counts, the deck build
  without the `pptx` skill); opened 2026-09-14.
- THR.0090 — multi-principal use; deliberately not worked on.
- THR.0140 — the delivery side; deferred until a subject project
  needs the linkage.
- THR.0150 — the scripts in Python; decided 2026-10-02, the rewrite
  of the PowerShell scripts open.
- THR.0210 — the guard rail for the public boundary; at stake again
  2026-09-20, to be taken up.
- THR.0190 — a plugin as a distribution layer; merges into the brief
  `engine-split` (THR.0230).
- THR.0200 — the public face, narrowed to the README exemplar.
- THR.0170 — branch documents; deferred.
- How `shall` and the banned English words stand in an assignment
  written in another language; raised 2026-10-02, nothing decided.
- `check-project` names "assignment style" in its description and
  verifies no such part; noticed 2026-10-02.
- `essence` is not run on this project, the principal's word of
  2026-10-02; the release skill still offers it at every release.
- Three weakly founded places in the README of 2026-10-02 (the next
  step of `/forge`, when two scripts are run, the fifth verdict); the
  readme recipe, at its next iteration.
