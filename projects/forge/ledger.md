---
project: forge
kind: thought
updated: 2026-09-06
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
| 00-brief.md | — | placeholder: brief stage was skipped, intent is the earliest record | — | — |
| 00-brief-public-engine.md | 1.0 | approved | mined | born in the forge 2026-08-29 (THR.0130, THR.0090), locked 2026-08-29 in English after the CTO challenge; mined into intent 2.21 (POS.0940–0980, REJ.0140–0150, THR.0190–0200). Instance work it records — the one-off migration steps 1–6, the first projects after the split — stays here and under Waiting on principal, not in the intent |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 3.43 | draft | 2026-09-06 |
| 20-assignment.md | — | not planned: the handover artefacts of this project are the core itself (CLAUDE.md, templates/, .claude/) and README.md | — |
| decisions.md | — | 9 records (DEC.0010–0090) | 2026-09-03 |

## Renders
<!-- Generated outputs, one row per recipe in recipes/. Never
hand-edited: iterate the recipe, re-run /render. Row mirrors the
render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|
| README.md (repo root) | humans arriving at the repository | recipes/readme.md v0.37 (recipe now 0.39, render stale) | CLAUDE.md, 10-intent.md v3.39 | 2026-09-06 |
| RELEASE-NOTES.md (repo root) | the user of the engine who takes upgrades through forge-pull | recipes/release-notes.md v0.10 | 10-intent.history.md, 10-intent.md v3.39, decisions.md, previous edition (released sections) | 2026-09-06 |
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
| 2026-09-05-good-release-notes.md | 2026-09-05 | 10-intent.md v3.34 (THR.0310; POS.0730, release-notes recipe 0.6); RELEASE-NOTES.md as rendered 2026-09-05 |

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
| FND.0290 | medium | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.0540 rewritten, no counts; CLAUDE.md heading; readme recipe 0.38) |
| FND.0300 | medium | duplication | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.1100 owns the split) |
| FND.0310 | low | ambiguity | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (the variants' word left to THR.0290) |
| FND.0320 | low | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 |
| FND.0330 | low | contradiction | resolved | 2026-09-06-critique-clarity.md | intent 3.42 |
| FND.0340 | low | duplication | resolved | 2026-09-06-critique-clarity.md | intent 3.42 (POS.0840 owns the index) |

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
- **Operating layer of POS.1120 built (2026-09-06, intent 3.41);
  the critic's first real run done, the challenger's pending:**
  `/critique clarity intent` on 2026-09-06 confirmed the contract on
  the live agent (its sections in the first user message after the
  task; report, regression and ledger by the contract; the running
  session picked up the edited agent without a restart); its six
  findings fixed at 3.42. Next, on the principal's word:
  `/challenge cto` on the new contract, the same one-sentence prompt
  check in the task. Trial outputs of 2026-09-06 kept only in the
  session's scratchpad, nothing filed. The README render is stale
  (CLAUDE.md and readme recipe 0.38 changed), regenerated at the next
  `/release`.
- **Commands migrated to skills (2026-09-06, intent 3.43, POS.1130):**
  THR.0330 closed, FND.0260 resolved; run before the check round on
  the principal's word so that `/check` is written once on its final
  place. One trial of `context: fork` on `/check` belongs to the check
  round. The bare `/check-forge` after the move: nine findings, all
  settled the same day (argument-hints quoted after the CRLF parse
  defect, eight small alignments, readme recipe 0.39). The README
  render is stale (CLAUDE.md changed again), regenerated at the next
  `/release`.
- **Harness critique settled (2026-09-06):** FND.0270 by POS.1120,
  FND.0250 and FND.0280 fixed, FND.0260 by POS.1130. The other six
  were fixed 2026-09-05 (intent 3.30, POS.1090).
- THR.0320 a `harness` lens — CLAUDE.md and the operating layer
  reviewed through the official plugins (plugin-dev,
  claude-md-management), output the classic critic's; opened
  2026-09-05 at the principal's direction, decided in substance;
  open: the mechanism (mapping in `.claude/skills/critique/SKILL.md` or an own agent with
  preloaded plugin skills), the plugin as an engine dependency, the
  fit of claude-md-improver's rubric, the regression step. No
  priority given yet; shares its mechanism with POS.1120.
- **Operating layer of POS.1100 and POS.1110 built 2026-09-05 with
  intent 3.33:** `release.md` new, `save.md` narrowed, `forge-save
  -Tag` and `forge-branch.ps1` (both tested on throwaway
  repositories), CLAUDE.md, templates, genre files and both recipes
  aligned. First real `/release forge` run the same evening: ten
  check-forge findings settled (intent 3.34), `critique essence`
  declined, README and release notes rendered from the settled
  sources. Until the light check exists (THR.0290), `/save` runs no
  check — accepted knowingly.
- **Release notes reshaped and the history migrated (2026-09-05,
  intent 3.35):** THR.0310 closed by walkthrough after the research
  `2026-09-05-good-release-notes.md` — one section per release in six
  fixed groups, compiled from a Notes block that closes every history
  row of the intent, the assignment and later layers (POS.0730,
  POS.0310). On the principal's word the Notes block was appended to
  all 93 rows of `10-intent.history.md` from 0.1 to 3.34, prose
  untouched, compiled from the prose by Claude — rows never rewritten,
  broken once, knowingly; marker row at the foot of the companion.
  `RELEASE-NOTES.md` re-rendered whole the same evening
  (`/render release-notes`, recipe 0.7, 94 sections) — the released
  sections of 3.0, 2.0 and 1.0 rewritten once in the new shape,
  knowingly. The principal's review of that render (a significant
  improvement; the lines described the system, not the change for
  its user; the majors claimed tags v1 and v2 that never existed):
  POS.0310 extended with the reader's-side rule (intent 3.36), every
  Notes line rewritten in a second pass the same evening (second
  marker row), recipe 0.8, and the notes re-rendered. His review of
  that second render: both views are needed in one line — the fact
  and what it means for the user (intent 3.37, POS.0310); every Notes
  line rewritten a second time (third marker row), recipe 0.9, the
  notes re-rendered again. Then his suggestion, decided at 3.38:
  at a major the minors fold into its section and their sections
  disappear (POS.0730, recipe 0.10); first applies at 4.0, no render. The README render is stale
  (CLAUDE.md changed), regenerated at the next `/release`. The
  release-notes recipes of agentic-platform and flow-ba keep the old
  shape until their next `/recipe release-notes`.
- **Priorities of the open threads (principal's order, 2026-09-04
  evening; item 1 closed 2026-09-05), the next rounds in this
  sequence:**
  1. ~~THR.0220~~ closed at 3.33 (POS.1100, POS.1110), operating
     layer built the same day (item above).
  2. ~~THR.0310~~ closed at 3.35–3.38 (POS.0730, POS.0310), research
     `2026-09-05-good-release-notes.md`, operating layer and history
     migrated the same evening (item below).
  3. ~~THR.0270~~ closed at 3.40 (POS.1120) after its trial run
     2026-09-06; the operating layer built at 3.41; the critic's real
     run done at 3.42; THR.0330 (all commands to skills) done at
     3.43. Next, in the principal's order of 2026-09-06: THR.0290 —
     check on the reviewer mechanism with its kinds (`project`,
     `engine`, `light` proposed), then `/challenge cto` on the new
     contract, then the settlement of that challenge and release 4.0.
     THR.0240 (the size of CLAUDE.md, the reviewer's context measured
     2026-09-06) after that.
  Then THR.0230 (after an outline of the second framework). Dormant
  by decision, trigger recorded in each: THR.0250, 0300, 0190, 0200,
  0210, 0170, 0180, 0150, 0140, 0090.
- Save duration (watch): the first /save with parallel renders and
  the isolated /check-forge (2026-09-02) took twelve minutes — renders
  6:54 in parallel (README 6:54, release notes 2:45), the check 5:00
  with a full /check of the forge project folded in. Second
  measurement (2026-09-03, save of 3.19): renders 8:18 in parallel
  (README 8:18, release notes 2:24), the check 4:19. Lever pulled
  2026-09-05: renders and check move to `/release` (POS.1100); the
  watch continues on the first releases. First `/release` (2026-09-05,
  release 3.34): the check 4:56, renders in parallel 7:07 (README
  3:44, release notes 7:07).
- Force-push of 2026-09-04, recorded: the save of intent 3.21–3.22
  (b717a67) carried the principal's private `tmp/` at the engine root
  into the public repository — the directory had never been added to
  `.gitignore` though the principal had asked for it the day before.
  On his word the commit was amended without `tmp/` and `main`
  rewritten (`git push --force-with-lease`, 1f7cc06), `/tmp/` added to
  `.gitignore`; direct git outside the scripts and a rewrite of `main`,
  knowingly, once. GitHub may still hold the objects of b717a67 in its
  cache; only GitHub support can purge them, if the principal wants
  certainty.
- THR.0290 check as a third kind of reviewer (fixed 2026-09-06), and
  research alike — opened 2026-09-04; kinds and the fate of
  /check-forge open; the save/release question answered at 3.33 (full
  check at `/release`, light check at `/save` once it exists)
- THR.0300 a user's private layer of local agents — opened 2026-09-04,
  no priority
- Migration to the history companion (POS.0310): the engine and the
  forge project done 2026-09-04 — CLAUDE.md, templates, commands, the
  80 rows of the intent moved to `10-intent.history.md`, one-row
  companions for the locked brief and the three recipes, "material
  index" renamed "resource index"; `last_change` written into the
  locked brief's front-matter on the principal's word at the
  check-forge walkthrough of 2026-09-04 — immutability knowingly
  broken once for one metadata line, the text untouched.
  The three local projects migrated and saved the same day, each
  through `/check` and its own `/save`: agentic-platform (acddf3d),
  flow-ba (2e262b8), lib-allwyn (c49c874). Left for their next save:
  the ledger and index comments of agentic-platform and flow-ba still
  say "material index" and "artefact" (comments only, not a finding).
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
- Tag v3.32 (2026-09-05, commit 30730c4): the state before the
  save/release round (THR.0220) — harness guard in place, `/save`
  reordered. Set by the principal from the shell, outside the
  forge's mechanism, since the scripts then carried no tag operation.
  Settled the same day (POS.1100): `forge-save -Tag <name>` for any
  tag on request, `v<major>` mandatory at every release of an
  approved major; the next such tag goes through `/save -Tag` or
  `/release -Tag`.
- THR.0210 the guard rail for the public boundary — `projects/forge` never carries the content of a subject project; parked 2026-09-03 by the principal, proposed solution recorded in the thread (a check item in `/check-forge` plus one sentence in both reviewer skeletons); taken up when the boundary is next at stake
- THR.0180 the output language — left as is; more than one output language solved when a project needs it
- THR.0190 a plugin as a later distribution layer — no preparation
  now; taken up when forge-pull proves an insufficient upgrade channel
- THR.0200 the public face, narrowed at 3.0 to the README exemplar (repository `forge-of-thought` and licence CC BY 4.0 settled in POS.0990)
- THR.0170 branch documents — deferred; taken up only if a draft brief needs position-level work before locking
- README footer (`_Last updated_`): kept for now; principal will give further input
