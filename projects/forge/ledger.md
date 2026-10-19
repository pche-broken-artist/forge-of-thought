---
project: forge
kind: thought
language: en
updated: 2026-10-19
---

# Ledger — Forge of Thought

<!-- Single source of truth for state: CLAUDE.md, Ledger. Versions
per CLAUDE.md, Versioning & status. /ledger reads from here.
kind: thought | library; a ledger without it reads as `thought`: at
an import that is a fact the command reports, at a check a finding
with the one-line fix (the one owner of this rule).
Kind: `thought` keeps every table below. `library` (POS.0960) keeps
only Renders, Sources, Dependencies, Research and Waiting on
principal; the Briefs, Documents, Published, Work, Findings and
Challenges tables are deleted at scaffold time; the Findings table returns with
a check's first finding (`.claude/skills/check/SKILL.md`). This
comment is the one owner of that reduction (POS.1070). -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md). Status:
draft (being composed) | approved (1.0 and on, changed after that as
any artefact is).
Mined: pending | partial | mined | dropped — how far the intent has
absorbed it; Note says what remains (partial) or the REJ (dropped). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | — | placeholder: brief stage was skipped, intent is the earliest record | — | accepted under DEC.0010, not a check finding |
| 00-brief-public-engine.md | 1.0 | approved | mined | born in the forge 2026-08-29 (THR.0130, THR.0090), locked 2026-08-29 in English after the CTO challenge; mined into intent 2.21 (POS.0940–0980, REJ.0140–0150, THR.0190–0200). Instance work it records — the one-off migration steps 1–6, the first projects after the split — stays here and under Waiting on principal, not in the intent |
| 00-brief-elicitation.md | 1.0 | approved | mined | born in the forge and locked 2026-09-28; mined into intent 4.32 (POS.1300 to POS.1380, POS.0110, REJ.0180, REJ.0210, REJ.0220, THR.0440 to THR.0460; THR.0440 and THR.0450 closed at 4.46). The material for the briefs `brd` and `engine-split` is carried in THR.0230, THR.0300 and THR.0360. Not a model of a brief, see its opening note |
| 00-brief-next-gen.md | 0.3 | draft | pending | born in the forge 2026-10-03, written in English on the principal's word; the needs of the next generation gathered in one round, to be sifted; the eighteen researches of 2026-10-03 cited under its sections (0.2); THR.0520 opened from it; the documentation moved out into the brief `documentation` (0.3) |
| 00-brief-brd.md | 0.2 | draft | pending | born 2026-10-16 handed over (THR.0360); 0.2 on the principal's judgement: the fork's BRD is the base, checked against the standards and improved; the IDs being decided one at a time, the first (BR, UC, DEP) without a verdict yet |
| 00-brief-documentation.md | 0.1 | draft | mined | born 2026-10-09 from THR.0340 (the rounds of 2026-10-05 and 2026-10-07) and the principal's word of 2026-10-09; the documentation part of `next-gen` moved into it; mined into intent 4.60 (POS.1450, POS.1080, POS.0930, POS.0950, REJ.0240 to REJ.0260, THR.0590) and solution design 0.4 (SOL.0460) the same day |
| 00-brief-collaboration.md | 0.8 | draft | mined | born 2026-10-17 from the principal's word of the day (the ledger as the file where every operation collides; two people, two branches, two windows on one project): the complete proposal of the merge mechanism stored as shown, from two researches of 2026-10-17, the evidence of agentic-platform and the reviews of another model (sources ledger-merge-review, merge-design-review); 0.2 to 0.8 the same day work in six critiques (merge-brief-critique, -2 to -6): B0 the project file, the header written on main only, land first, the driver's ordering rule, the reservation per prefix at the reflection, five digits recommended, both indexes mutable, the state render, the Waiting rule, M the migration; 0.7 the eleven open points decided in a walkthrough 2026-10-17, all accepted, and the path through git from the collision at the save of 0.6; 0.8 the worktree addressed by slug, IDs four-digit until 9999; mined into intent 5.13 (POS.1560 to POS.1750, REJ.0270 to REJ.0310, THR.0690; THR.0090, THR.0640, THR.0650, THR.0620 changed); the bare save narrowed against the brief's D on the mining (one window only); of the four reports B gives the light check, the THR cited without a file taken into POS.1640 at 5.24 and the finding resolved without a version left out, POS.1610 letting the intent's history settle one (FND.1810) |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 5.24 | draft | 2026-10-18 |
| 40-solution-design.md | 0.31 | draft | 2026-10-18 |
<!-- One row per layer below the intent, added when the layer is
born; a layer the project does not have gets no row (CLAUDE.md,
Ledger). -->

## Renders
<!-- Generated outputs (CLAUDE.md, Document chain, Renders): one row
per rendered recipe, written by /render step 6 at the first render
and kept by every later one, the row mirroring the render's
front-matter provenance. The documentation index has a row too,
written by /document: Recipe "none, derived by scripts/docs-index.py",
Inputs the map with its generated date and the intent's version. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.66 | CLAUDE.md, 10-intent.md v5.9, .claude/skills/forge/states/, docs/README.md v5.9, RELEASE-NOTES.md | 2026-10-14 |
| docs/README.md (the documentation index, kind page) | the three readers of the documentation | none: derived by scripts/docs-index.py (SOL.0460) | docs-map.md (generated 2026-10-14), 10-intent.md v5.9 | 2026-10-14 |
| RELEASE-NOTES.md (repo root) | the user of the engine who has cloned it and takes upgrades through forge-pull | recipes/release-notes.md v0.13 | 10-intent.history.md, 10-intent.history.archive.md, 40-solution-design.history.md, 10-intent.md v5.3, decisions.md, previous edition (released sections) | 2026-10-11 |
| CONTRIBUTING.md (repo root) | a visitor of the repository on GitHub who wants to say, ask or change something | recipes/contributing.md v0.3 | projects/forge/10-intent.md v5.3, CLAUDE.md, docs/README.md v5.3 | 2026-10-11 |
| renders/executive-pitch.md | C-level executives whose experience of AI is chatting with it | recipes/executive-pitch.md v0.6 | projects/forge/10-intent.md v4.30, CLAUDE.md | 2026-09-27 |
| renders/cto-pitch.md | technical leadership arriving at the repository - a CTO, a head of engineering or architecture | recipes/cto-pitch.md v0.6 | projects/forge/10-intent.md v4.58, CLAUDE.md | 2026-10-04 |
| renders/ceo-pitch.md | a CEO or another C-level executive whose experience of AI is chatting with it | recipes/ceo-pitch.md v0.6 | projects/forge/10-intent.md v4.58, CLAUDE.md | 2026-10-04 |
| renders/ba-intro.md (with renders/ba-intro.pptx, plain, pandoc) | business analysts meeting the forge for the first time, before a live demonstration | recipes/ba-intro.md v0.1 | CLAUDE.md, projects/forge/10-intent.md v5.5, .claude/skills/forge/states/, sixteen pages of docs/ v5.3, CONTRIBUTING.md | 2026-10-12 |

## Published
<!-- Designed files made by /publish, one row per file (CLAUDE.md,
Document chain, Renders). State: current | stale — set to current by
/publish, to stale by every /render of that recipe. -->
| File | Recipe | From render | Model | Published | State |
|---|---|---|---|---|---|
| published/executive-pitch.pptx | recipes/executive-pitch.md v0.4 | generated 2026-09-11, projects/forge/10-intent.md v4.4, CLAUDE.md | opus | 2026-09-11 | stale |
| published/cto-pitch.docx | recipes/cto-pitch.md v0.5 | generated 2026-09-20, projects/forge/10-intent.md v4.15, CLAUDE.md | opus | 2026-09-27 | stale |
| published/ba-intro.pptx | recipes/ba-intro.md v0.1 | generated 2026-10-12, CLAUDE.md, projects/forge/10-intent.md v5.5, .claude/skills/forge/states/, sixteen pages of docs/ v5.3, CONTRIBUTING.md | opus | 2026-10-12 | current |

## Work
<!-- Work products (CLAUDE.md, Document kinds; POS.1520): one row per
work product, written by /work at the specification's birth and kept
by every making. Specification = its version. State: current — set by
the making; stale — set by a write of the specification not followed
by a making; by hand — set on the principal's word when he has worked
the file and does not want it remade. -->
| File | Specification | Inputs | Made | State |
|---|---|---|---|---|
| work/collaboration-cutover.md | work/collaboration-cutover.spec.md v0.6 | 40-solution-design.md v0.24 (SOL.0670 to SOL.0830, SOL.0300, SOL.0330, SOL.0530, SOL.0150, SOL.0160, SOL.0420, SOL.0460, SOL.0500, TBC.0050, TBC.0060, TBC.0080), 10-intent.md v5.22 (POS.1560 to POS.1770, POS.1120, POS.1140, POS.0220), threads.md (THR.0620, THR.0650, THR.0690, THR.0700, THR.0710), decisions.md (DEC.0210 to DEC.0260), 00-brief-collaboration.md v0.8 (M), sources/cutover-plan-critique.md, sources/cutover-challenge-review.md, sources/cutover-challenge-review-2.md | 2026-10-17 | by hand |

## Sources
<!-- Registration only. External inputs, immutable once registered.
Date = best-effort origin date; origin: content | file | ingested. What
a source is and is for lives in sources/00-INDEX.md, never here
(CLAUDE.md, Document chain, External inputs). Form (POS.1040): text | extract
of <original> | binary — one form per source. -->
| File | Date | Date origin | Form |
|---|---|---|---|
| forge-run-record-health.md | 2026-09-13 | content | text |
| word-default-a4.docx | 2026-09-20 | file | binary |
| forge-elicitation-brief-review.md | 2026-09-28 | ingested | text |
| forge-elicitation-brief-review-v0.4.md | 2026-09-28 | ingested | text |
| docs-audit-2026-10-11.md | 2026-10-11 | content | text |
| ledger-merge-review.md | 2026-10-17 | ingested | text |
| merge-design-review.md | 2026-10-17 | ingested | text |
| merge-brief-critique.md | 2026-10-17 | ingested | text |
| merge-brief-critique-2.md | 2026-10-17 | ingested | text |
| merge-brief-critique-3.md | 2026-10-17 | ingested | text |
| merge-brief-critique-4.md | 2026-10-17 | ingested | text |
| merge-brief-critique-5.md | 2026-10-17 | ingested | text |
| merge-brief-critique-6.md | 2026-10-17 | ingested | text |
| mining-critique.md | 2026-10-17 | ingested | text |
| design-critique.md | 2026-10-17 | ingested | text |
| design-critique-2.md | 2026-10-17 | ingested | text |
| architect-challenge-review.md | 2026-10-17 | ingested | text |
| architect-challenge-review-2.md | 2026-10-17 | ingested | text |
| architect-challenge-review-3.md | 2026-10-17 | ingested | text |
| cutover-plan-critique.md | 2026-10-17 | ingested | text |
| cutover-challenge-review.md | 2026-10-17 | ingested | text |
| cutover-challenge-review-2.md | 2026-10-18 | ingested | text |
| cutover-challenge-review-3.md | 2026-10-18 | ingested | text |

## Dependencies
<!-- Registration only. Documents of other repositories this project
relies on — typically library documents (POS.1020): cited by path from
an index entry, a recipe or the chain. No version: library documents
are maintained by their owner. What the document is for lives where it
is used (the index entry, the recipe). -->
| Path | Library | Used by | Note |
|---|---|---|---|
| projects/lib-allwyn/sources/fork-brd/ (bundle, its 00-INDEX.md) | lib-allwyn | sources/00-INDEX.md; the research of the BRD layer of 2026-10-13; 00-brief-brd.md | private: names, company content, the group's internal standard |

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
| 2026-10-03-how-a-solution-design-is-built.md | 2026-10-03 | 10-intent.threads.md (THR.0520) and the working conversation over it; the three definitions of `.claude/skills/forge/states/`; research/2026-09-28-artefact-layers-from-idea-to-handover.md |
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
| 2026-10-04-deterministic-work-by-script-or-by-model.md | 2026-10-04 | the principal's question of 2026-10-04; the engine's operating layer read whole; 10-intent.md v4.53 read whole, its threads searched (THR.0150, THR.0400, THR.0410, THR.0500); the researches of 2026-10-02 and 2026-10-03 on the operating layer and on Claude Code |
| 2026-10-04-how-a-contributing-file-is-written-on-github.md | 2026-10-04 | the principal's word of 2026-10-04 on a CONTRIBUTING for the forge; the Community Standards page of the forge's repository; 10-intent.md v4.57 (POS.0170, POS.0720, POS.0980, POS.0990) |
| 2026-10-05-how-a-security-policy-is-written-on-github.md | 2026-10-05 | the principal's word of 2026-10-05 on a SECURITY.md for the forge; research/2026-10-04-how-a-contributing-file-is-written-on-github.md (finding 7); 10-intent.md v4.58 (POS.0760, POS.0950, POS.1440); 40-solution-design.md v0.3 (SOL.0030, SOL.0510, SOL.0520, SOL.0600) |
| 2026-10-10-a-user-only-distribution-of-the-engine.md | 2026-10-10 | the principal's question of 2026-10-10 after the release of 5.0; 10-intent.md v5.0 (POS.0940, POS.0950, THR.0190, THR.0230); the two distribution researches of 2026-08-29; the engine's tree measured on disk |
| 2026-10-13-what-an-it-or-ai-strategy-contains-light-but-complete.md | 2026-10-13 | the principal's word of 2026-10-13 in the project ai-strategy (a strategy artefact for the forge, research first); 00-brief-next-gen.md v0.3 (Work without a known artefact); 10-intent.md v5.6 (POS.0700, POS.1430); research/2026-10-03-work-without-a-known-artefact-and-its-working-files.md; web sources |
| 2026-10-13-ai-agents-and-tools-that-make-a-strategy.md | 2026-10-13 | the principal's word of 2026-10-13 in the project ai-strategy; research/2026-10-13-what-an-it-or-ai-strategy-contains-light-but-complete.md; research/2026-10-03-work-without-a-known-artefact-and-its-working-files.md; web sources |
| 2026-10-17-mergeable-shared-records-in-git.md | 2026-10-17 | the principal's word of 2026-10-17 (work of several people, branches or windows on one project collides in the ledger, the histories and the indexes); 10-intent.md v5.12 (POS.1110, POS.1490, REJ.0170); threads.md (THR.0090); CLAUDE.md (Ledger, Versioning & status); web sources |
| 2026-10-17-git-merge-drivers-and-their-limits.md | 2026-10-17 | the principal's word of 2026-10-17; research/2026-10-17-mergeable-shared-records-in-git.md; 10-intent.md v5.12 (POS.1110, POS.1490); web sources |
| 2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md | 2026-10-13 | the principal's word of 2026-10-13; projects/lib-allwyn/sources/fork-brd/ (cited by path); research/2026-09-07-brd-layer-fork-analysis.md; 10-intent.md v5.8 (POS.0700, POS.1310, POS.1320, POS.1350, POS.1360, POS.1430, POS.1520); threads.md THR.0360; decisions.md DEC.0060; the assignment's definition and the clarity lens |
| 2026-10-13-what-a-brd-contains-and-how-it-is-found-today.md | 2026-10-13 | the principal's word of 2026-10-13; research/2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md; research/2026-09-07-brd-layer-fork-analysis.md; research/2026-09-28-artefact-layers-from-idea-to-handover.md; the group's standard and tutorial in the library bundle; web sources |

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
| FND.0070 | low | divergence | resolved | 2026-08-27-critique.md | README re-rendered at intent 2.13 (2026-08-27, recipe 0.18) — regression belongs to the essence lens (verified 2026-10-09, essence) |
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
| FND.0620 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (rules echoed inside CLAUDE.md cut to their owner); reopened 2026-10-05 (`2026-10-05-check-single-source-of-truth.md`); named again (`2026-10-09-check-single-source-of-truth.md`); resolved: the layer rule in Ledger, the authorship boundary in Document chain 4, cited from the other places (operating layer 2026-10-09) |
| FND.0630 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (CLAUDE.md, the skills `critique` and `man`, the descriptions of the two critic lenses); reopened 2026-10-05 (`2026-10-05-check-single-source-of-truth.md`); named again (`2026-10-09-check-single-source-of-truth.md`); resolved: the parenthesis cut to "by its state file" (operating layer 2026-10-09) |
| FND.0640 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the skills `ingest` and `research`) |
| FND.0650 | low | conformance | parked | 2026-10-02-check-single-source-of-truth.md | needs a pass over the recipe genres and their skeletons; named again (`2026-10-09-check-single-source-of-truth.md`) |
| FND.0660 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (`templates/index-bundle.md`) |
| FND.0670 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (CLAUDE.md, `states/intent.md`) |
| FND.0680 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (the critic contract; CLAUDE.md, Requirement style) |
| FND.0690 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.48 (three agent files) |
| FND.0700 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (six reminders name their owner or left) |
| FND.0710 | low | conformance | rejected | 2026-10-02-check-single-source-of-truth.md | DEC.0170 |
| FND.0720 | low | conformance | resolved | 2026-10-02-check-single-source-of-truth.md | intent 4.49 (the three contracts cite the skeletons); the quoting caveat kept in the skeletons, DEC.0180 |
| FND.0730 | low | conformance | resolved | 2026-10-02-check-light.md | intent 4.48 (POS.0310, `templates/history.md`) |
| FND.0740 | low | conformance | resolved | 2026-10-02-check-project.md | intent 4.49 (four lines of Waiting on principal cut to a citation) |
| FND.0750 | low | conformance | resolved | 2026-10-02-check-project.md | recipes `cto-pitch` and `ceo-pitch` 0.6: the line written from the ledger's row in the one, dropped until a first publish in the other (reopened and settled 2026-10-04, `2026-10-04-check-project.md`) |
| FND.0760 | medium | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, What this workspace is) |
| FND.0770 | medium | conformance | resolved | 2026-10-02-check-engine.md | recipe readme 0.52 |
| FND.0780 | medium | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, prime directive 1) |
| FND.0790 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, Document chain) |
| FND.0800 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (CLAUDE.md, Versioning & status) |
| FND.0810 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (POS.0850) |
| FND.0820 | low | conformance | resolved | 2026-10-02-check-engine.md | intent 4.49 (`templates/recipe-readme.md`, `templates/recipe-release-notes.md`) |
| FND.0830 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0120, POS.1380) (verified 2026-10-09, clarity) |
| FND.0840 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0740, POS.1150, POS.0930) (verified 2026-10-09, clarity; a second exception has since grown in POS.0930, see FND.1240) |
| FND.0850 | medium | contradiction | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.0940) (verified 2026-10-09, clarity) |
| FND.0860 | low | ambiguity | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.1080, POS.0710) (verified 2026-10-09, clarity) |
| FND.0870 | low | duplication | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (POS.1330, POS.1340, POS.1350, REJ.0220; the older positions own) (verified 2026-10-09, clarity) |
| FND.0880 | low | gap | resolved | 2026-10-02-critique-clarity.md | intent 4.50 (a Facts section saying why it is empty) (verified 2026-10-09, clarity) |
| FND.0890 | low | conformance | resolved | 2026-10-03-check-light.md | the record of THR.0520 at 4.52 appended to the intent's history (2026-10-03) |
| FND.0900 | medium | conformance | resolved | 2026-10-04-check-light.md | the two companions moved untouched to their archives, the logs begin with the next version (2026-10-04) |
| FND.0910 | low | conformance | resolved | 2026-10-04-check-light.md | the rows of `20-assignment.md` and `decisions.md` deleted and the template's comment added (2026-10-04) |
| FND.0920 | low | conformance | resolved | 2026-10-04-check-light.md | the four comments replaced with the template's wording (2026-10-04) |
| FND.0930 | low | conformance | resolved | 2026-10-04-check-light.md | THR.0540, THR.0550 and THR.0560 opened, the ledger lines cut to a citation (intent 4.54) |
| FND.0940 | low | conformance | resolved | 2026-10-04-check-project.md | the line of THR.0520 under Waiting on principal cut to a citation (2026-10-04) |
| FND.0950 | medium | conformance | resolved | 2026-10-04-check-engine.md | recipe readme 0.56 (the brief no longer locked, its callout gone) |
| FND.0960 | medium | conformance | resolved | 2026-10-04-check-engine.md | recipe readme 0.56 (the artefacts from the definitions on disk, the diagram with the solution design as built) |
| FND.0970 | low | conformance | resolved | 2026-10-04-check-engine.md | the skills `ingest` and `render` and recipe readme 0.56 cite Document chain by the item's name (intent 4.58) |
| FND.0980 | medium | conformance | resolved | 2026-10-05-check-single-source-of-truth.md | named again (`2026-10-09-check-single-source-of-truth.md`); resolved: `templates/ledger.md` header owns the `kind:` rule (operating layer 2026-10-09) |
| FND.0990 | medium | conformance | resolved | 2026-10-05-check-single-source-of-truth.md | named again (`2026-10-09-check-single-source-of-truth.md`); resolved: `/spinoff` intent-first through the procedures (operating layer 2026-10-09) |
| FND.1000 | low | conformance | resolved | 2026-10-05-check-single-source-of-truth.md | named again (`2026-10-09-check-single-source-of-truth.md`); resolved: the Renders comment of `templates/ledger.md` owns the moment (operating layer 2026-10-09) |
| FND.1010 | low | conformance | resolved | 2026-10-05-check-single-source-of-truth.md | named again (`2026-10-09-check-single-source-of-truth.md`); resolved: both headers cite CLAUDE.md, Persistence (operating layer 2026-10-09) |
| FND.1020 | low | conformance | resolved | 2026-10-07-check-light.md | `proposal-documentation.md` deleted 2026-10-09 on the principal's word, its substance in the brief `documentation` and THR.0340 (named again in `2026-10-09-check-light.md`) |
| FND.1030 | low | conformance | resolved | 2026-10-09-check-light.md | named again (`2026-10-09-check-light-2.md`); the kind `map` in POS.1080 and CLAUDE.md, the map named in the Renders row of the index (intent 4.60, 2026-10-09) |
| FND.1050 | low | conformance | resolved | 2026-10-09-check-light-2.md | the stale line left with the closing of THR.0340 (intent 4.60, 2026-10-09) |
| FND.1060 | medium | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | the contract skill `docs-contract` (operating layer 2026-10-09, solution design 0.7) |
| FND.1070 | medium | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | the document skill cites its scripts' headers (operating layer 2026-10-09) |
| FND.1080 | medium | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | the release skill owns what a release does with the documentation; CLAUDE.md and the document skill cite it (operating layer 2026-10-09) |
| FND.1090 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | `templates/docs-map.md` (operating layer 2026-10-09, solution design 0.7) |
| FND.1100 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | `templates/ledger.md`, Renders comment owns the index's row (operating layer 2026-10-09) |
| FND.1110 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | `/render` step 3 the owner, the others cite or dropped the sentence (operating layer 2026-10-09) |
| FND.1120 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | `forge_tools.py` owns what the conversions need (operating layer 2026-10-09) |
| FND.1130 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | the readme skeleton the one owner, CLAUDE.md and POS.1450 cite it (intent 4.64, 2026-10-09) |
| FND.1140 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | the dispatcher cites Document chain (operating layer 2026-10-09) |
| FND.1150 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | three restating clauses dropped, one owner added (operating layer 2026-10-09) |
| FND.1160 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | owners named, the second sentence of `/new-project` dropped (operating layer 2026-10-09) |
| FND.1170 | low | conformance | resolved | 2026-10-09-check-single-source-of-truth.md | each rule once in its state file (operating layer 2026-10-09) |
| FND.1180 | low | conformance | resolved | 2026-10-09-check-light-3.md | the Waiting line says what is left (2026-10-09) |
| FND.1190 | low | conformance | resolved | 2026-10-09-check-light-3.md | the Inputs cell cut to the map and the version (2026-10-09) |
| FND.1200 | low | conformance | resolved | 2026-10-09-check-light-3.md | the template's comment in all nine companions (2026-10-09) |
| FND.1040 | low | conformance | resolved | 2026-10-09-check-light.md | `date: 2026-10-09` set in `00-brief-next-gen.md` (immediate fix, 2026-10-09) |
| FND.1210 | medium | contradiction | resolved | 2026-10-09-critique-clarity.md | intent 4.65: THR.0550 closed, `essence` ran on 2026-10-09 once the solution design stood; POS.0300 holds as written |
| FND.1220 | medium | contradiction | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.1380, THR.0170, THR.0230) |
| FND.1230 | medium | scope-creep | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.1050, POS.1060, POS.0180), solution design 0.8 (SOL.0150, SOL.0160, SOL.0230) |
| FND.1240 | low | contradiction | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.0930, POS.0530) |
| FND.1250 | low | contradiction | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.0100, POS.0600, POS.0620, POS.0700, POS.0970) |
| FND.1260 | low | contradiction | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.0550) |
| FND.1270 | low | ambiguity | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.1450 says the README; the pages' language open in THR.0590) |
| FND.1280 | low | gap | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.1090, POS.1450) |
| FND.1290 | low | gap | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.0930, REJ.0240, the closing section) |
| FND.1300 | low | duplication | resolved | 2026-10-09-critique-clarity.md | intent 4.65 (POS.0140 owns intent-first, POS.0900 names it; POS.1460 owns the birth step, POS.1090 cites; POS.0860) |
| FND.1310 | medium | lost | resolved | 2026-10-09-critique-essence.md | solution design 0.8 (SOL.0010) |
| FND.1320 | medium | shifted | resolved | 2026-10-09-critique-essence.md | solution design 0.8 (SOL.0500 cites the readme recipe's pinned facts, recipe 0.60 carries the address) |
| FND.1330 | low | lost | resolved | 2026-10-09-critique-essence.md | solution design 0.8 (SOL.0530) |
| FND.1340 | low | provenance | resolved | 2026-10-09-critique-essence.md | solution design 0.8 (head) |
| FND.1350 | low | lost | resolved | 2026-10-09-critique-essence.md | intent 4.65 (THR.0200) |
| FND.1360 | low | conformance | resolved | 2026-10-10-check-light.md | the header date set to 2026-10-10 |
| FND.1370 | low | conformance | resolved | 2026-10-10-check-light.md | the line says recipe 0.60 |
| FND.1380 | low | conformance | resolved | 2026-10-10-check-light.md | both comments replaced by the template's wording |
| FND.1390 | low | conformance | resolved | 2026-10-10-check-project.md | recipe release-notes 0.13: the solution design's history among the inputs |
| FND.1400 | low | conformance | resolved | 2026-10-10-check-project.md | templates/recipe-readme.md carries the optional section Pinned facts (not rendered) |
| FND.1410 | medium | conformance | resolved | 2026-10-10-check-engine.md | /render step 3 says instance facts are not material, step 6 scans the render with docs-check.py --file |
| FND.1420 | medium | conformance | resolved | 2026-10-10-check-engine.md | front-matter brought to the shape of the three reviewer contracts |
| FND.1430 | low | conformance | resolved | 2026-10-10-check-engine.md | the layout comment of CLAUDE.md names the documentation's contract and agents |
| FND.1440 | low | conformance | resolved | 2026-10-10-check-engine.md | intent 5.10: POS.1420 names the check as wanted (THR.0520) |
| FND.1450 | low | conformance | resolved | 2026-10-10-check-engine.md | the sentence of The system's own project says the threads stand beside the intent |
| FND.1460 | low | conformance | resolved | 2026-10-10-check-engine.md | the brief skeleton derives last_change as the other skeletons do |
| FND.1470 | low | conformance | resolved | 2026-10-10-check-light-2.md | the POS.1450 line deleted, both steps done 2026-10-10 |
| FND.1480 | low | conformance | resolved | 2026-10-10-check-light-3.md | the THR.0570 line says the release is made |
| FND.1490 | low | conformance | resolved | 2026-10-11-check-light.md | THR.0650 opened at intent 5.4, the line cut to the ID |
| FND.1500 | low | conformance | resolved | 2026-10-12-check-light.md | both cells say sixteen pages |
| FND.1510 | low | conformance | resolved | 2026-10-12-check-light.md | a line under Waiting on principal for the recipe ba-intro |
| FND.1520 | low | conformance | resolved | 2026-10-12-check-engine.md | intent 5.6 POS.1520 and CLAUDE.md prime directive 6 say the language of the specification and the file |
| FND.1530 | low | conformance | resolved | 2026-10-12-check-engine.md | CLAUDE.md Versioning & status and POS.0310 name the work specification |
| FND.1540 | low | conformance | resolved | 2026-10-12-check-engine.md | POS.1080 says six groups |
| FND.1550 | low | conformance | resolved | 2026-10-12-check-engine.md | readme recipe 0.64 cites POS.1450 and SOL.0500 |
| FND.1560 | low | conformance | resolved | 2026-10-12-check-engine.md | executive-pitch recipe 0.8, S02 idea approved |
| FND.1570 | low | conformance | resolved | 2026-10-12-check-engine.md | THR.0400 names scripts/hook-gate.py |
| FND.1580 | low | conformance | resolved | 2026-10-12-check-light-2.md | the Work table and the header comment from the template |
| FND.1590 | low | conformance | resolved | 2026-10-12-check-light-2.md | the comment of twelve history companions from the template |
| FND.1600 | low | conformance | resolved | 2026-10-13-check-light.md | a line under Waiting on principal |
| FND.1610 | medium | conformance | resolved | 2026-10-13-check-light-2.md | Documents rows 5.8 and 0.15 |
| FND.1620 | low | conformance | resolved | 2026-10-13-check-light-2.md | the line says the matter is tracked in the project ai-strategy |
| FND.1630 | low | conformance | resolved | 2026-10-13-check-light-2.md | the bare file name |
| FND.1640 | low | conformance | resolved | 2026-10-14-check-light.md | the Waiting line of POS.1530 names the operating layer only (2026-10-14) |
| FND.1650 | low | conformance | resolved | 2026-10-14-check-light.md | lines for TBC.0040 and TBC.0030 under Waiting on principal (2026-10-14) |
| FND.1660 | low | conformance | resolved | 2026-10-14-check-light-2.md | the Waiting line of POS.1530 says the operating layer is realised and the README re-rendered (2026-10-14) |
| FND.1670 | low | conformance | resolved | 2026-10-14-check-light-3.md | the Waiting line of POS.1530 names recipe 0.66 (2026-10-14) |
| FND.1690 | low | conformance | resolved | 2026-10-16-check-light.md | the Waiting line of THR.0360 says the brief `brd` was born and stands at 0.2 (2026-10-16) |
| FND.1700 | low | conformance | resolved | 2026-10-16-check-light.md | `updated: 2026-10-16` (2026-10-16) |
| FND.1710 | low | conformance | resolved | 2026-10-16-check-light.md | `00-brief-brd.md` added to the Used by of the `fork-brd` row (2026-10-16) |
| FND.1680 | low | conformance | resolved | 2026-10-15-check-light.md | the bundle saved and pushed from lib-allwyn 2026-10-15 (commit 3366304); the clone that lacked it pulls |
| FND.1720 | low | conformance | resolved | 2026-10-17-check-light.md | the brief collaboration 0.6 puts eleven points to the principal, Waiting on principal did not cite it; the line added |
| FND.1730 | low | conformance | resolved | 2026-10-17-check-light-2.md | TBC.0070 (the principal's, solution design 0.18) has no line under Waiting on principal; THR.0650's line does not carry the four tests of the brief collaboration (TBC.0050); both lines added |
| FND.1740 | low | conformance | resolved | 2026-10-18-check-light.md | TBC.0010 of work/collaboration-cutover.spec.md (the principal's) has no line under Waiting on principal; the line added |
| FND.1750 | low | conformance | resolved | 2026-10-18-check-light.md | the THR.0650 line says the four tests come after the first and the second release, the design at 0.22 says before the second, none after the first; the line brought to the design at 0.22 |
| FND.1760 | medium | conformance | resolved | 2026-10-18-check-light-2.md | the work file collaboration-cutover.md cites SOL.0150, SOL.0160, SOL.0420, SOL.0460, SOL.0500, SOL.0530 and POS.0220, which its specification's Inputs do not name; the specification 0.5: the seven items added to its Inputs, each with the step it serves |
| FND.1770 | low | conformance | resolved | 2026-10-18-check-light-2.md | the Work row's Inputs cell stands at the specification's 0.2 while the row says v0.4; the Inputs cell brought to the specification's Inputs |
| FND.1780 | low | conformance | resolved | 2026-10-18-check-light-2.md | 00-brief-brd.history.md carries the template's placeholder comment in its document field; the comment deleted from the field |
| FND.1790 | medium | shifted | resolved | 2026-10-18-critique-essence.md | POS.1750 still wants a throwaway clone, four tests after the releases and a fixture made by a script, which DEC.0240, TBC.0050 at design 0.22 and DEC.0250 have each replaced below without the position following; intent 5.24 (POS.1750) |
| FND.1800 | low | shifted | resolved | 2026-10-18-critique-essence.md | THR.0710's open form of the deferred releases would reverse POS.0550, POS.1200, POS.1490, POS.1760 and POS.1110, yet the thread is addressed to the design alone and the intent presents the mechanism as decided; intent 5.24 (THR.0710, POS.1760) |
| FND.1810 | low | lost | resolved | 2026-10-18-critique-essence.md | two of the four reports the brief `collaboration` gives the light check (a finding resolved without a version, a THR cited without a file) reach neither POS.1640, SOL.0680, SOL.0330 nor the Briefs row's note; intent 5.24 (POS.1640: the THR cited without a file taken; the finding resolved without a version left out, POS.1610 letting the intent's history settle one), design 0.26 (SOL.0680) |
| FND.1820 | low | provenance | resolved | 2026-10-18-critique-essence.md | POS.1580 cites the brief for a scope the brief's A2 does not have: the renders joined at 5.15 from sources/design-critique-2.md, which the position does not name; intent 5.24 (POS.1580) |
| FND.1830 | medium | contradiction | resolved | 2026-10-18-critique-clarity.md | at the state diverged POS.1490 offers `/merge`, POS.1760 has `/merge` refuse a diverged repository and POS.1690 gives a path of four steps starting with a branch; intent 5.24 (POS.1760, POS.1490, POS.1690), design 0.26 (SOL.0820) |
| FND.1840 | medium | contradiction | resolved | 2026-10-18-critique-clarity.md | POS.0180, POS.0920, POS.1520, POS.1140, POS.0400 and POS.0440 still have the ledger as the place where state is written, after POS.1600 to POS.1640 moved every state into records; intent 5.24 (POS.0180, POS.0920, POS.1520, POS.1140, POS.0400, POS.0440) |
| FND.1850 | medium | contradiction | resolved | 2026-10-18-critique-clarity.md | the role of a source is asked for after registration in POS.0180 and POS.1040 and before the entry is written in POS.1670; intent 5.24 (POS.0180, POS.1040) |
| FND.1860 | medium | contradiction | resolved | 2026-10-18-critique-clarity.md | POS.1750 verifies the promise on a throwaway clone and, in its own last sentence, on a fixture project of the forge; the moment of the four tests said only in the older wording; intent 5.24 (POS.1750) |
| FND.1870 | medium | ambiguity | resolved | 2026-10-18-critique-clarity.md | POS.1730 gives two rules for the next free number (over the local branches; from the author's block) without saying how they nest; POS.0220's "never from the block or the sequence" leaves no source where blocks exist; intent 5.24 (POS.1730, POS.0220), design 0.26 (SOL.0790) |
| FND.1880 | low | contradiction | resolved | 2026-10-18-critique-clarity.md | POS.1760 says every change of a thread is a record of the intent's history; POS.0120 records birth and closing only; intent 5.24 (POS.1760) |
| FND.1890 | low | contradiction | resolved | 2026-10-18-critique-clarity.md | POS.0110 and POS.0920 require a position to cite its brief with its version, and no position does; intent 5.24 (POS.0110, POS.0920: the version is the mining record's) |
| FND.1900 | low | style | resolved | 2026-10-18-critique-clarity.md | the closing note of threads.md on duplicated IDs stands between THR.0680 and THR.0690; threads.md, the note moved to the end (intent 5.24) |
| FND.1910 | medium | ambiguity | resolved | 2026-10-18-critique-clarity.md | the design marks Not built on SOL.0670 to SOL.0830 only; SOL.0120, SOL.0150, SOL.0160, SOL.0180, SOL.0210, SOL.0230, SOL.0400 and SOL.0640 describe unbuilt behaviour in the present with no mark, and SOL.0530's walk never reaches an item marked deferred; design 0.26 (head, SOL.0530) |
| FND.1920 | medium | contradiction | resolved | 2026-10-18-critique-clarity.md | the bare save skips the fixture by the flag in SOL.0510 and SOL.0670 and by the name `projects/fixture-*` in SOL.0830, and the interim `projects/fixture` matches neither; design 0.26 (SOL.0830, SOL.0510, SOL.0670) |
| FND.1930 | low | contradiction | resolved | 2026-10-18-critique-clarity.md | SOL.0510 names `forge-branch --reserve`, a reservation of IDs that SOL.0790 no longer has (REJ.0320); design 0.26 (SOL.0510) |
| FND.1940 | low | contradiction | resolved | 2026-10-18-critique-clarity.md | the design's head says no part answers POS.0700 while SOL.0170 realises it, and its list of items added since 0.1 names four of twenty-five; design 0.26 (head) |
| FND.1950 | low | conformance | resolved | 2026-10-18-check-engine-1746-9a79.md | the check skill still contrasts the check agent with a critic and a challenger that write, after both stopped writing (R1.01); the sentence says like, not unlike |
| FND.1960 | low | conformance | resolved | 2026-10-18-check-engine-1746-9a79.md | the readme recipe's pinned text of video 1 names "the lock" among the steps of a brief's birth, a mechanism withdrawn (POS.0110, THR.0520); recipe readme 0.67 says the approval, the README at the next render |
| FND.1970 | low | conformance | resolved | 2026-10-18-check-light-3-2114-fb83.md | TBC.0010 and TBC.0020 of the design, the principal's, have no line under Waiting on principal; the lines of THR.0370 and THR.0520 name them |
| FND.1980 | low | conformance | resolved | 2026-10-18-check-light-3-2114-fb83.md | the Waiting line of THR.0620 says nothing decided while its row 9 is decided and in building; the line says so |
| FND.1990 | low | conformance | resolved | 2026-10-19-check-engine-1237-204e.md | threads.md THR.0620 row 9, 2026-10-19: the preparation ships by its saves and the tag pre-r1 (DEC.0260) |
| FND.2000 | low | conformance | resolved | 2026-10-19-check-engine-1237-204e.md | CLAUDE.md layout, 2026-10-19: the three shared modules named together in the scripts/ comment |

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
| CHL.0200 | accepted | The major is for a date, and nothing named closes: the twenty-two-position pass of THR.0520 open, the solution design unjudged, the brief next-gen pending (major) | 2026-10-09-challenge-cto.md | intent 4.65 (POS.0300; the name of 5.0 in THR.0570), as modified: the major closes a package and the open stays open; that an approval signs the open matters over, declined |
| CHL.0210 | rejected | The first audience cannot, by the project's own research, run the shape 5.0 fixes: three managed locks switch the forge off silently and only a plugin passes, single-user by position, eleven steps to the first question, no cost lever (major; dealbreaker if the company locks customisation to plugins) | 2026-10-09-challenge-cto.md | DEC.0190 |
| CHL.0220 | accepted | The test of a major tests the paper against the paper: nothing runs the engine, no check keeps the design true to the files, essence declined at both majors (major) | 2026-10-09-challenge-cto.md | intent 4.65 (POS.0300, THR.0600), as modified: the test attests the documents, the behavioural test is a thread, not before 5.0 |
| CHL.0230 | rejected | The rules are written as walls and held as preferences, five exceptions on record, and a second user reading the documentation cannot tell which is which (major) | 2026-10-09-challenge-cto.md | DEC.0200 |
| CHL.0240 | accepted | The intent's own Map is not walked for the forge: no recipient, objective or success criterion, the layer-below section stale, the chain positions unused since 2026-09-04 (minor) | 2026-10-09-challenge-cto.md | intent 4.65 (the closing section; the Map walked at the write of 5.0), as modified: no success criteria before 5.0, open in the brief `next-gen` |
| CHL.0250 | accepted | The merge is the one step left outside the forge, and the design has just taken the server merge away: no door for the local merge into main, the fallback raw git the user types and Claude is denied (major; dealbreaker if the collaborators are analysts) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: `/merge <branch>` through the forge's door, the conflicts in a walkthrough (POS.1760, SOL.0820; THR.0700 for `/save`) |
| CHL.0260 | accepted | The reservation of IDs pushes to main, and main is protected by default on GitLab; TBC.0070 is the case, not a limit; a block per author assigned once was never weighed (major) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: one integrator and N contributors (POS.1770), ID blocks per author assigned by hand (POS.1730, SOL.0790), the plumbing rejected (REJ.0320); TBC.0070 closed |
| CHL.0270 | accepted | The migration reflows every line of prose and sees no branch, fork or clone in flight; --undo cannot undo the reflow; the release that carries it goes out before the four tests (major) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: the migration refuses while branches are in flight, the undo from the index (POS.1740, SOL.0800), the tests before the releases (POS.1750, TBC.0050), the branch tool TBC.0080 |
| CHL.0280 | accepted | The ledger script is a single point of failure for the map and the save, strict by rule, no degraded form, repair of a bad record a breach of append-only, and no word on what /save does when it fails (major) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: the ledger script degrades aloud and tolerates one release back, `/save` saves on (POS.1600, SOL.0680, SOL.0530), the dry run before the first release (TBC.0050) |
| CHL.0290 | accepted | merge=ours turns round in the rebase of /save: a release made on a clone that is behind tags the other person's older README silently (major) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: a release, the documentation and a publish refuse a repository behind or diverged (POS.1710, SOL.0530, SOL.0460, SOL.0420) |
| CHL.0300 | accepted | The design makes the migration a precondition of every write while POS.0820 says a migration is a per-project decision never assumed; the narrowing is not in the intent (minor) | 2026-10-17-challenge-architect.md | accepted 2026-10-17: POS.0820 narrowed with its reason, the old shape for reading until migrated |
| CHL.0310 | accepted | The merge has one direction and one source: nothing brings main into a branch though the driver's ordering rule and a test are designed for it; /merge reads origin/<branch> only, so a local worktree branch on a project without an origin cannot be merged; a branch and its worktree have a birth and no end (major) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: `/merge` in both directions, the source by where the branch lives, `forge-branch --done` (POS.1760, SOL.0820, SOL.0770) |
| CHL.0320 | accepted | The first release is the one-way door and realises the least of the evidenced pain: the reflow and the threads, justified by a conflict the evidence does not contain, ride in it with "land first" and the blame reset; the driver, which removes three of the five evidenced collisions, waits in the second; the unique report names sit a release behind the branches (major) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: the order of the releases reversed, the conversion last and on its own with a blame ignore-revs file, the unique names in the first (DEC.0210, POS.1580, THR.0620, SOL.0710, SOL.0810) |
| CHL.0330 | accepted | The resolution of a conflict at /merge is the one content change without a record in the history that is the single primary; a driver's conflict is by construction a breach, and what the driver leaves in the file at a conflict is unspecified while the walkthrough assumes text markers (minor) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: the verdict of a conflict as a `changed` record, the driver's conflict in standard markers with the base kept for an immutable unit (POS.1760, SOL.0820, SOL.0750) |
| CHL.0340 | accepted | rerere is called the load-bearing mechanism of /merge, but a rebase drops the merge commit and git says the resolution must be re-applied; it matches for a one-commit branch only; the guard that holds is the refusal, or /merge pushing as its last step (minor) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: rerere a convenience, `/merge` ending with the push and merging on refusal, `forge-save` pulling a merge commit by merge (POS.1760, POS.1690, SOL.0740, SOL.0530) |
| CHL.0350 | accepted | The engine's .gitattributes with the prefix projects/forge/ misses every way-3 file the engine actually has: README, release notes, CONTRIBUTING and docs/ at the root get the text merge (minor) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: the engine's own attribute list with its way-3 files at the root (POS.1690, SOL.0730) |
| CHL.0360 | accepted | The landing's place in the save is stated three ways (first; inside forge-save before committing; after the light check), and one order deadlocks: a closed record written by the check's settlement into a history with + records meets "land first: /save" from inside /save (minor) | 2026-10-17-challenge-architect-2.md | accepted 2026-10-17: joining the landing in place of land first, the landing the first act of the save (POS.1660, SOL.0760, SOL.0530) |
| CHL.0370 | accepted | The plan does not say where release 1 is built: on main the upgrade channel carries half-built states for the duration, on a branch there is one tree and the merge is raw git; the duration that decides is not priced (major) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the first release built on the engine's branch r1 in a second tree, six to eight sittings, one release (DEC.0220, THR.0620, the plan) |
| CHL.0380 | accepted | The fixture is placed in tmp/, where no forge script resolves a repository; nine closings "on the fixture" and the four tests of THR.0650 cannot run there without raw git (major) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the fixture two projects made by a script, skipped by a bare save (SOL.0830, POS.1590, POS.1750) |
| CHL.0390 | accepted | R1.19's refusal of the old shape lands four steps before R1.23 migrates the engine's own project, so Claude cannot write into it meanwhile; R1.22's checks cannot be clean by construction; ASM.0030 says first, the order says last (major) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the engine's project migrated right after the two scripts, the refusal the last code step, R1.22 dropped (the plan) |
| CHL.0400 | accepted | Between release 2 and 3 a branch round still bumps the header, so every merge of a worked branch conflicts on version and its records read as two boundaries later; R2.06 files a content change as a state record; the second interval has no sentence as the first has (major) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the version as a boundary in the second release with the driver and /merge, four releases (DEC.0220, SOL.0760) |
| CHL.0410 | accepted | Three closings cannot close as written: R1.09's diff against a hand-kept ledger known to differ, R5.01's byte-identical video, and the pre-release tests with no word for a red result (minor) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the pass of the dry run, the proof by the events file, the word for red (THR.0650, TBC.0050, POS.1750) |
| CHL.0420 | accepted | The way back is a tag, walked only by git in a person's hand; a project cannot go back alone once the engine refuses its old shape; R1.26 tags every project before only one migrates (minor) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the tag per project before its migration, the way back said truthfully (POS.1740, SOL.0800) |
| CHL.0430 | accepted | Release 4 realises nothing until a second author exists and release 5 waits behind it by ASM.0010, not by dependency; the plan marks no trigger and no dependency between releases (minor) | 2026-10-17-challenge-architect-3.md | accepted 2026-10-17: the blocks of IDs on the trigger of a second author, the dependencies marked (DEC.0220, POS.1730, the plan) |
| CHL.0440 | obsolete | The branch branches the forge's own project: the merge of r1 into main is a merge across the migration unless main is frozen, and nothing freezes it (major) | 2026-10-17-challenge-architect-4.md | obsolete 2026-10-18: the branch withdrawn, the first release on main in one stretch (DEC.0230) |
| CHL.0450 | obsolete | R1.24 runs /document and /release on the branch, where both refuse; merging first and releasing on main was not weighed (major) | 2026-10-17-challenge-architect-4.md | obsolete 2026-10-18: no release on a branch, the branch withdrawn (DEC.0230) |
| CHL.0460 | obsolete | The second tree holds only projects/forge: the throwaway clones of every project have no stated home, and the home they will get carries the real origins (major) | 2026-10-17-challenge-architect-4.md | obsolete 2026-10-18: no second tree; the throwaway clones live under projects/ of the one tree as fixture-flagged projects (DEC.0230) |
| CHL.0470 | accepted | The three gates that stop a release are placed before the parts they test, against the method's own rule (major) | 2026-10-17-challenge-architect-4.md | accepted 2026-10-18: each gate after what it tests, the fixture born in the old shape and migrated (the plan R1.00, R1.02, R2.01; SOL.0830, TBC.0050) |
| CHL.0480 | accepted | R1.23 closes with a command built sixteen rows later and checks whose agents learn the new shape afterwards; the window the review called one step is seven rows (minor) | 2026-10-17-challenge-architect-4.md | accepted 2026-10-18: the header-reading scripts before the migration, the migration by the script directly, the checks at the release (the plan R1.10, R1.11, R1.23) |
| CHL.0490 | accepted | Two parts of the design have no step (the state render, the Role before the write), and the tests disagree with TBC.0050 in both directions (minor) | 2026-10-17-challenge-architect-4.md | accepted 2026-10-18: the state render and the Role before the write as steps (R1.27, R1.28), the four tests before the second release, none after the first (R2.12, TBC.0050) |
| CHL.0500 | accepted | The throwaway clones of every project have no way into the one tree: forge-clone names by URL and has no target, the flag has no home before the migration makes it, and a bare save pushes a migrated clone to its real origin (major) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: the tests on the fixture alone, a real project dry in place, `forge-clone <url> <name>`, the skip of a bare save by name (SOL.0830, SOL.0800, DEC.0240; the plan R1.00, R1.09, R1.10, R1.13); `sources/cutover-challenge-review-2.md` |
| CHL.0510 | accepted | Two branches of one author take the same ID, the second release's own use case; the fourth release's trigger is the wrong event and its mechanism would not close the hole (major) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: the allocation over the local branches within one clone, the blocks between clones and authors, the trigger widened to a second clone, the one exception to never renumbered at a clash (POS.1730, POS.1110, POS.0220, POS.1680, SOL.0790, DEC.0240; the plan R2.13, R2.12, the heading of release 4; TBC.0020 of the specification for agentic-platform); `sources/cutover-challenge-review-2.md` |
| CHL.0520 | accepted | The fixture is born from the templates of the day, so after the stretch the migration has nothing to test; nothing tests one release back or the conversion step on it (minor) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: the fixture carries the old shape itself, a tag per shape on the bare remote (SOL.0830; the plan R1.00, R5.04) |
| CHL.0530 | accepted | Three mechanics of the third release cannot run as written: the ignore-revs hash of a commit the script never makes, no mark for the conversion, the blame configuration on one machine (minor) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: the sixth mark, the conversion's commit through forge-save and the hash by a second save, the blame file among the registrations of /setup on every machine (SOL.0800; the plan R5.04, R5.07) |
| CHL.0540 | accepted | The second machine is not in the plan: three /setup runs, the release notes' Action wrong for it, the freeze a habit without a mechanism (minor) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: the Action for every other machine in every release (SOL.0800; the plan R1.24, R2.11, R5.07, R4.06); the freeze by a refusal of forge-pull not built, DEC.0230 covers it today, on the principal's word |
| CHL.0550 | accepted | The engine's own 35 threads get their origin guessed with nobody judging, and the round that corrects them has no step (minor) | 2026-10-18-challenge-architect.md | accepted 2026-10-18: a walkthrough over the origins of the engine's threads, the plan R1.29 |
| CHL.0560 | accepted | R1.09's dry run in place overwrites the tracked hand-kept ledger it is diffed against and leaves a change a bare save pushes; its pass criterion was written for a migrated clone and cannot be graded over the old shape (major) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18: the ledger script writes only where the ledger is out of the index, else stdout or --out to tmp/, the old tables read as the archive (SOL.0680, TBC.0050, THR.0650; the plan R1.09) |
| CHL.0570 | accepted | The fourth release's trigger, a second clone of the same author writing into a project, has already fired on the brief's own evidence (the double FND.1690); the plan treats it as future and builds the blocks on the first release alone although R4.02 extends R2.13 (major) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18 as modified: the trigger narrowed to a second clone with a branch in flight, a pulling clone no trigger; the principal's word: the collision of 2026-10-17 was his own two clones, the second only pulls (POS.1730, DEC.0240, THR.0620; the plan's heading of release 4 and intro); the merge of the fourth release into the second declined |
| CHL.0580 | accepted | The remedy for a clash of IDs, the one exception to never renumbered, has no step, no owning command, and R2.13's test is written to avoid the race that would show it (major) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18: /merge runs the ledger script after the merge and settles a duplicate in its walkthrough, the light check reports one elsewhere (SOL.0820; the plan R2.14 with the race on the fixture) |
| CHL.0590 | accepted | The stretch is equated with the release, not with the shape change: nine rows change nothing the migration migrates and could ship in an ordinary release before it, shortening the freeze (minor) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18: a Preparation section, an ordinary release before the stretch, with R1.01, R1.18, R1.08, R1.12, R1.14, R1.28, R0.02, R1.00, R0.01; the stretch begins at the first commit of the shape, the tag before it (DEC.0240, THR.0620; the plan) |
| CHL.0600 | accepted | R1.00 uses forge-clone's target built in R1.10, the tag pre-r1 comes after two building commits, and R1.02 and R2.01 still say the clone the principal makes (minor) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18: the clone target as R0.02 before the fixture, R1.26 before R1.03, R1.02 and R2.01 on the fixture (the plan) |
| CHL.0610 | accepted | The fixture's shape tags live on a bare remote in the gitignored tmp/ of one machine, so the one-release-back bed accepted for CHL.0520 does not survive the machine (minor) | 2026-10-18-challenge-architect-2.md | accepted 2026-10-18: the shapes as the script's own data, `fixture.py --shape <version>`, no tag on the bare remote (SOL.0830; the plan R1.00, R1.24, R5.07) |

## Waiting on principal
<!-- What waits on the principal, one line per matter: cite, never
copy — CLAUDE.md, Ledger. -->
- THR.0660 — the course of the teaching videos; opened 2026-10-14.
- THR.0670 — a chain handed over whole; Claude's synthesis, nothing
  decided, not before the first such project; opened 2026-10-15.
- THR.0680 — a question put to the manual, `/man <free text>`;
  Claude's synthesis, to be built; opened 2026-10-15.
- TBC.0020 of `work/collaboration-cutover.spec.md` — whether
  `agentic-platform` already has a second author by handle; opened
  2026-10-18.
- THR.0690 — the conversion to one sentence per line (POS.1580),
  the third release of the brief collaboration (DEC.0220); opened
  2026-10-17.
- THR.0710 — the form of the deferred releases of the brief
  `collaboration`, the designed mechanism or git opened to Claude;
  after the first release (DEC.0250); opened 2026-10-18.
- THR.0700 — `/save` taking the conflict walkthrough of `/merge` in
  place of aborting a rebase; not now; opened 2026-10-17.
- TBC.0030 — the independent challengers of POS.0800, not built; open
  since solution design 0.1.
- a `strategy` artefact for the forge (`/new-artefact strategy`):
  tracked in the project ai-strategy (its work product
  `reconstruction`, TBC.0010) until the principal calls the command;
  the two researches of 2026-10-13 stand ready; no thread here.
- THR.0640 — when a thread that has become a plan is rather a brief,
  and whether large files are split; the `Was` question settled
  2026-10-17 (POS.1680); opened 2026-10-11.
- THR.0520 — a layer for the solution; priority; steps 1 to 5 done, step
  6 (the BRD) paused 2026-10-04; TBC.0020 of the design, which check
  keeps it true, decided here.
- THR.0570 — the presentation of the forge and what is to be ready
  for it; opened 2026-10-04; the major 5.0 approved and released
  2026-10-10; his verdict on the two pitch renders, his judgement
  of the recipe `ba-intro` 0.1 and the rest of the thread open.
- THR.0530 — what can be done deterministically is done by a script;
  the principal's stance of 2026-10-04, to be a prime directive;
  research of 2026-10-04; open.
- THR.0460 — `/recipe` and `/forge`, one dispatcher or two; small,
  open.
- THR.0400 — a gate in front of the tools; the soft half done, the
  hard half open, nothing scheduled.
- THR.0360 — a layer with an external audience, opened 2026-09-14;
  worked in the brief `brd`, born 2026-10-16 and at 0.2 draft (the
  Briefs row); its IDs being decided one at a time.
- THR.0370 — Mermaid diagrams in Word; deferred 2026-09-12, open;
  TBC.0010 of the design, the mermaid-cli dependency, his decision.
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
- THR.0500 — the reviewers' mechanism out of the session; filing by
  a script kept for later, research of 2026-10-02; opened 2026-10-02.
- THR.0510 — live reference material by nightly export; the
  principal's thought, nothing decided; opened 2026-10-02.
- FND.0650 — parked finding of the `single-source-of-truth` check;
  needs a pass over the recipe genres and their skeletons; named
  again 2026-10-05.
- THR.0420 — derivations of the forge for other jobs; nothing
  scheduled.
- THR.0430 — the measurement of a session, stored per user; where
  it lives open; `/end` decided (POS.1500, intent 5.1).
- THR.0650 — the test of forge-pull's new output and the states
  behind and diverged on a throwaway clone, deferred 2026-10-11; the
  four tests of the brief `collaboration` (TBC.0050) before the second
  release, none after the first.
- THR.0590 — what the documentation of a project other than the
  engine reads; opened 2026-10-09 (intent 4.60), after the first
  `/document <slug>` on a project.
- THR.0380 — executive pitch loose ends (S03 counts, the deck build
  without the `pptx` skill); opened 2026-09-14.
- THR.0090 — the multi-principal chain, an assignment handed to a
  colleague's instance; several people on one project answered
  2026-10-17 (POS.1560 to POS.1750); deliberately not worked on.
- THR.0140 — the delivery side; deferred until a subject project
  needs the linkage.
- THR.0210 — the guard rail for the public boundary; at stake again
  2026-09-20, to be taken up.
- THR.0190 — a plugin as a distribution layer; merges into the brief
  `engine-split` (THR.0230).
- THR.0200 — the public face, narrowed to the README exemplar.
- THR.0170 — branch documents; deferred.
- THR.0540 — `shall` in an assignment written in another language;
  raised 2026-10-02, nothing decided.
- THR.0600 — a test of the forge's behaviour; opened 2026-10-10 from
  CHL.0220, not before 5.0.
- THR.0610 — the horizon statement the intent lacks (POS.1360);
  opened 2026-10-10 at the approval of 5.0, for a 5.x round.
- THR.0620 — a plan for the forge after 5.0, Claude's synthesis; row 9
  decided in the brief `collaboration` and in building (DEC.0250, the
  plan `work/collaboration-cutover.md`), the other rows open, their
  questions to be asked one by one; opened 2026-10-10.
