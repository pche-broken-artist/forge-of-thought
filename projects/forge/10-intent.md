---
version: 3.19
date: 2026-09-03
status: draft
project: forge
audience: principal + Claude only
---

# Forge of Thought — Intent

## Version History
| Version | Modification | Author | Date |
|---|---|---|---|
| 3.19 | THR.0210 parked at the principal's decision: the risk of a content leak from a subject project into the public engine is small while he knows of it, and a rule with its checks would add weight the forge does not need now — not closed, only deferred. Claude's proposed solution recorded in the thread for the day it is taken up: a check item in `/check-forge` owning the rule (process facts admissible, content not; verified by reading, never by a term list) plus one citing sentence under Inputs in both reviewer skeletons, because their outputs are immutable and written by agents that read subject projects as evidence; not a critic lens (the leak surface lies outside the chain and a lens runs on request, not at every save), and no sentence in CLAUDE.md (THR.0240). | Claude | 2026-09-03 |
| 3.18 | Both reviewers take an optional target, at the principal's request: an artefact named as `/forge` names it, without one the whole chain — `clarity` reads that artefact alone, `essence` that artefact against its parent (a transition addressed by its downstream artefact, no arrow typed), a challenger the substance of that artefact; the challenger's default moves from the intent to the whole chain, each challenge naming the artefact it concerns. POS.0400, POS.0410 and POS.0420 extended; `/critique` and `/challenge`, both skeletons and the files carrying them, CLAUDE.md aligned. | Claude | 2026-09-03 |
| 3.17 | The first run of the `clarity` lens (reviews/2026-09-03-critique-clarity.md, ten findings) walked through, every verdict the principal's. FND.0090 overruled (DEC.0090): a position states the convention, the scripts' wider capability is no contradiction, and the manual tag is settled in THR.0220. Nine fixes: POS.0960 and `/check` report a project without a repository as a fact, never a finding, and POS.0940 names the local-only project — with or without a repository — as a legitimate shape for sensitive work (FND.0100); THR.0220 gains the question which reviewers run at a save or a release, and the fact that a two-speed save already exists in the principal's practice (FND.0110); POS.1000 cites POS.0720/0730 (FND.0120); POS.0970 lists a library's contents once, README and recipe included (FND.0130); POS.0950 opens with the per-repository identity and no longer narrates its own history (FND.0140); POS.0500 and POS.0600 name the repository `forge-of-thought` and keep `forge` for the project slug (FND.0150); POS.0560 folded into POS.1010 (FND.0160); POS.0005 calls the first principal the engine's author, keeping "instance fact" for `CLAUDE.local.md` (FND.0180); the ledger's migration entry reduced to one line and the executive-pitch entry rewritten to its present state (FND.0170). | Claude | 2026-09-03 |
| 3.16 | The critic split into two lenses at the principal's decision, after a user of the forge reported that the critic hunts formalities and does not guard the drift between the documents of the chain — a reading of the agent confirmed it: its mandate named one link (intent ↔ assignment) in one word, the brief was read but given no task, and formal checks filled four paragraphs of its prompt. POS.0400 rewritten: one shape for both reviewers — the critic has lenses and produces FND, the challenger has personas and produces CHL, both invoked by hand, both settled by walkthrough, each carrying its shared behaviour verbatim from one skeleton; which of them run at a save or a release is left to THR.0220. POS.0410 rewritten: `clarity` reads each artefact on its own, `essence` reads the chain — for every adjacent pair it distils the downstream essence blind, then the upstream's, and reports the difference of essences (lost without trace, added without provenance, shifted, provenance that does not hold). Names chosen by the principal from several pairs. THR.0250 extended with the essence manager's detail, which gave the `essence` lens its method. Operating layer: `templates/critic.md` new as the mirror of `templates/challenger.md`, `critic-clarity.md` and `critic-essence.md` replacing `critic.md`, `templates/critique.md` retired (the report shape lives in the skeleton), `/critique` rewritten as the mirror of `/challenge` (bare = roster), `/check-forge` verifies lenses like personas, CLAUDE.md reviewers section, layout and command row, readme recipe 0.33. | Claude | 2026-09-03 |
| 3.15 | POS.0850 extended at the principal's direction after a drift he named: one item per message — Claude puts one item with its recommendation in front of the principal and stops, the next message acknowledges the verdict in a line and carries the next item only, a check of understanding is an item of its own, an elicitation interview runs the same way one question at a time, a questionnaire being the table of verdicts in another coat. The drift: the interview of THR.0230 opened with six questions at once and every following message stacked the reflection of the last answer, a check and further questions. CLAUDE.md Walkthrough aligned. | Claude | 2026-09-03 |
| 3.14 | THR.0260 opened at the principal's direction: the Version History table out of the document — measured at 40 % of this intent and held three times over (row, commit message, release notes); research `2026-09-03-version-history-placement.md` run; proposed solution one rule without exceptions, every versioned chain document keeping its history in an append-only companion `<document>.history.md` with version, date, status and a machine-written `last_change` in front-matter; the research's split by kind rejected by the principal (two rules for one thing, and the forge's assignment-less chain distorts the picture). | Claude | 2026-09-03 |
| 3.13 | THR.0250 opened at the principal's direction: two functions suggested to him for the forge, an expander and an essence manager — names only, no detail yet; parked until more is known. | Claude | 2026-09-03 |
| 3.12 | Two threads opened at the principal's direction, by interview, no decision taken. THR.0230: a common engine beneath several frameworks — what every framework needs alike (git, ledger, versioning, IDs, isolated agents, recipes and renders, material indexes, `/save`, `/check`, `/setup`) lifted out of the forge so that a new framework is written as content only, the forge becoming the first framework on it; two further frameworks named as the cases that draw the boundary (a product framework rendering HTML prototypes per module, a project-management framework fed by the forge's assignments and later by meeting inputs sorted by an agent), the agent boundary (mechanism engine, personas and critic content the framework's), three paths by which the engine reaches a framework recorded without choice (THR.0190 read as part of that question), the second framework to exist in outline before the engine is built, the thread possibly the first to become a project of its own. THR.0240: the size of CLAUDE.md (523 lines), to be dealt with whatever becomes of THR.0230. | Claude | 2026-09-03 |
| 3.11 | THR.0220 extended with three candidate solutions, formulated at the principal's direction to be weighed with a fresh head: (A) stale-only regeneration plus the principal's word at save time; (B) `/save` and `/release` split — save commits and pushes on whatever branch is checked out with a light check and no renders, release on main only runs the full check, the renders, the release commit and the tag, branches being git's own affair; (C) B plus one forge command switching between a fixed working branch and main. Facts recorded with them: the scripts already operate on the current branch, and a colleague has worked in his own forge instance on a branch of a subject project and merged by merge request without any forge ceremony — the forge stays a single-user tool per instance, coordination is git's (bearing on THR.0090); the principal's constraint that the forge must not grow into a wrapper of git. | Claude | 2026-09-02 |
| 3.10 | The day's sweep for restated procedures walked through, fourteen findings and three observations, every verdict the principal's, all accepted. POS.1070 extended: the shared behaviour of the challenger personas gets one owner, `templates/challenger.md`, carried verbatim by every persona file with only its Lens section its own (the principal's choice over a runtime include — a persona file stands alone like every skeleton, and the copy is mechanically checkable); `/check-forge` gains the standing rule — a restated procedure, a persona diverging from its template, a direct operation where a mechanism exists — scoped to the operating-layer files changed in the save, the full sweep only on a bare `/check-forge`; two further shapes that had no owner get a skeleton (`templates/index-bundle.md` for the bundle catalogue, the library reduction of the ledger in `templates/ledger.md`'s header). POS.0930 extended at the principal's prompt (a save takes five minutes): `/check` and `/check-forge` execute their own definition in an isolated subagent, and `/save` launches a repository's two renders in parallel. CLAUDE.md gains prime directive 10 (one mechanism lives in one place) and the template sentence in the reviewers section. Twelve commands, two agents, four templates aligned: `/check-forge` runs `/check` on the forge project instead of copying it, `/challenge`, `/critique` and `/save` cite the walkthrough instead of restating it, `/forge assignment` and `/check` cite Requirement style, `/new-project` and `/spinoff` hand the brief to `/forge brief` and the intent to `/forge intent`, `/render` owns the definition of a stale render, `/save` leaves its script's behaviour to the script's help. Opened THR.0220 at the principal's direction: whether README and release notes must be regenerated at every save — expensive and slow — or only when stale, on his word, or at a major. The first isolated `/check-forge` of the same evening (twelve minutes for the whole save, renders in parallel and the check with a full `/check` of the forge project) found nine findings, all accepted: the conversation language had been hard-coded as Czech in thirteen commands and a template against POS.0950 — POS.0060 rewritten to point at `CLAUDE.local.md`, the commands now say "in the conversation language"; the isolation paragraph of `/check-forge` reduced to a reference to `/check`; CLAUDE.md cites `templates/index-bundle.md`; the readme recipe (0.32) pins the finding-state vocabulary the render had invented; `doc2md.ps1` examples no longer suggest `.extract`. | Claude | 2026-09-02 |
| 3.9 | POS.1070 (new): one mechanism lives in one place and is used from there — a command, skill, script or agent is invoked through its own definition whenever its situation arises, never re-described ad hoc; a restated procedure is a `/check-forge` finding. Raised by the principal after the README of 2026-09-02 was rendered at `/save` through an ad-hoc subagent prompt that missed the 72-column rule of `/render`; `/save` step 2 now routes the regeneration through `/render` explicitly. Sweep of every command and skill for the same escape pending. | Claude | 2026-09-02 |
| 3.8 | The commit identity returns to the project (POS.0950 rewritten): it is set locally in every repository at its creation or import, proposed by the command layer from the identity roster in `CLAUDE.local.md` — matched by the origin's host as an offer, never a rule — on the principal's word. The per-host `includeIf` model of 3.6–3.7 is dropped on the principal's decision: the host is only a correlate of the identity and fails exactly where one host serves two roles, and writing `~/.gitconfig-<host>` files reached beyond the engine's boundary. The one global guard, now `/setup`'s closing offer (POS.1050), is `user.useConfigOnly = true` with no global `user.name`/`user.email`, so a commit in a repository without a local identity fails aloud instead of silently taking a default. `/import-project` passes `-Name`/`-Email` by default (POS.1060); the scripts are unchanged. | Claude | 2026-09-02 |
| 3.7 | POS.1050 extended: `/setup` closes the git-identities interview by offering the per-host configuration of POS.0950 — it generates one `~/.gitconfig-<host>` file per identity and the `includeIf` block, and on the user's word writes the files and appends the block to the end of `~/.gitconfig` (never overwriting existing content; appended last, so a matching host overrides a global `[user]` default); declined, it prints them for the user to apply by hand. `/setup` still runs no git operation — the user's git identity configuration is the one thing it may write outside the engine, on his word. Raised by the principal's question how the per-host model reaches another user when the identity files cannot live in the repository: the engine carries the mechanism, `/setup` carries it to the user, the values stay the user's. | Claude | 2026-09-01 |
| 3.6 | The four open findings of the day's pre-save `/check-forge` walked through, every verdict the principal's. POS.0950 rewritten to the per-host identity model — the commit identity follows the host, not the project: git conditional includes (`includeIf "hasconfig:remote.*.url:…"`) in the user's own configuration resolve the right identity for every repository automatically, a per-repository local identity stays as an override; `forge-save`'s effective-identity check is correct in this model and stays (the finding had proposed `--local`; the principal's "one identity per host, independent of the project" won instead). POS.1000: the engine's own README exempted from the fixed closing sentence — it is the sentence's destination. POS.1060: `/import-project` runs the clone bare by default and the script reports the identity git resolves; `-Name`/`-Email` remains as the fallback for a machine without the per-host include. `forge-clone.ps1` reports the identity git actually resolves for the fresh clone, or truthfully that forge-save will report and skip. CLAUDE.md gains the POS.0710 authorship boundary sentence in the chain section and the per-host wording in Persistence. | Claude | 2026-09-01 |
| 3.5 | First run and project arrival made one command each, prompted by a newcomer observed struggling through the manual install steps. POS.1050 (new): `/setup` — after cloning the engine, one command copies `templates/CLAUDE.local.md` to the root and fills it by interview (principal, conversation language, git identities) and creates `.claude/settings.local.json` with the session model set to Fable without asking — the recommendation embodied as the default, one notice sentence naming the change path (`/model` or editing the file); existing files are reported, never overwritten; named `/setup`, not `/init`, over the collision with Claude Code's built-in. POS.1060 (new): `/import-project <git-url>` — an existing project arrives through the scripts-only git door: `scripts/forge-clone.ps1` (the fourth git script; POS.0550 extended) clones into `projects/<repository name>` — no slug parameter, the directory falls out of the repository's name — refuses to overwrite, and reports the last commit, the origin and whether a ledger with `kind:` is present; the script carries no identity — the command proposes the matching one from `CLAUDE.local.md` and passes `-Name`/`-Email` on the principal's word. POS.0950 aligned (CLAUDE.local.md is created and filled by `/setup`). Readme recipe 0.27: Quickstart rebuilt as a common head (clone, install Claude Code, `claude` from the root, `/setup`) plus two named paths — starting a new project and bringing an existing one, with selecting the project (`/forge <slug>`) visible as the first act of work; Setup sections aligned. In the same round, POS.0710 extended with the authorship boundary — a chain artefact is composed by the principal, a render is generated (an article the principal writes is a layer, its translation a render) — raised when the README's chain diagram was redrawn from a line into the star: solid what is built today, dashed a fixed set of illustrative future layers (business analysis, an RFP, an article with its translation render, strategy, solution design, an implementation deck), visibly marked as not existing yet. | Claude | 2026-09-01 |
| 3.4 | A source has one form (POS.1040): at `/ingest` every binary file gets one question — convert to Markdown? — and is then either a text extract `<slug>.md` (tracked, registered, indexed, immutable; the original not copied, or gitignored where it already lies in `sources/`) or a functional binary (a template, a graphic) kept as is; both only on the principal's explicit word. POS.0180 aligned: no `.extract.md` sibling by default, the ledger's Extract column becomes Form. Transition at the principal's decision: existing extracts keep their names, existing binaries with an extract leave git on his word. Raised on the reference-pack index finding of the day's `/check`. POS.1000 extended: every project README closes with the fixed sentence that reading needs nothing and maintaining needs Forge of Thought, linked. POS.0810 extended: renders are regenerated only by `/save` or an explicit `/render`, never on Claude's own judgement. | Claude | 2026-08-30 |
| 3.3 | What was living in Claude Code's private memory of this instance and belongs to the forge moved into the engine (POS.1030): the working method Step by step (one consent-needing action at a time, exact operation and reason stated, a seen plan is not consent), the walkthrough's rule that an accept recommendation carries the concrete text, and one-research-one-question in `/research`; instance facts that were in memory — the git identities per host — moved to `CLAUDE.local.md`. Memory is left with what is personal to the principal only. | Claude | 2026-08-30 |
| 3.2 | Cross-repository dependencies registered in the ledger (POS.1020): a Dependencies table — path, library, used by, note — for every document of another repository a project relies on, typically a library document cited by path; `/check` verifies the paths exist and `/forge` reports which libraries a project needs; no version pin, by POS.0970. Raised by the principal when the regulatory report moved from a project into the company library and the project's reliance on it and on the deck template became invisible. | Claude | 2026-08-30 |
| 3.1 | Every project gets a README and, for a thought project, release notes as renders of its own recipes, regenerated by every save that touches the project (POS.1000) — the engine's own README and release-notes mechanism generalised; the ledger's Renders table carries them. A project icon `logo.png` in the project root, supplied by the principal, optional (POS.1010). Genre skeletons `readme` and `release-notes` for `/recipe`, scaffolded by `/new-project`. | Claude | 2026-08-30 |
| 3.0 | Approved by the principal after the split was executed (2026-08-30, runbook phases 0–D): the engine is public at a repository of its own with a fresh one-commit history, the company projects and the library live in repositories of their own, the company monorepo is archived with a notice. New: POS.0990 the public face — repository `forge-of-thought`, licence CC BY 4.0, the author credited with a contact address in the README as a fixed text of the readme recipe; THR.0210 a guard rail so that `projects/forge` never carries the content of a subject project (the leak surface the rewrite found), opened for the next iteration. Extended: POS.0980 with the execution record — the boundary rewrite of the locked brief and both CTO challenges (immutability knowingly broken once, recorded in the ledger only), slugs kept as process facts, the forbidden-term list dropped, the archive and its `pre-split` tag; POS.0950 with the commit identity set per repository at its creation, never inherited from the global configuration. THR.0200 narrowed to the README exemplar. The operating layer (CLAUDE.md, .gitignore, scripts, templates, commands, readme recipe 0.25 with the author-and-licence section, LICENSE) was rebuilt to this intent in the same day; README and release notes re-rendered. | PCHe | 2026-08-30 |
| 2.21 | Brief `00-brief-public-engine.md` (1.0) mined at the principal's direction, every verdict his — the brief goes to `mined`. New positions: POS.0940 the mechanism of the engine/projects split (nested repositories in a gitignored `projects/*`, scripts recognising a project by its `.git`, no configured remotes, upgrade by `forge-pull`, a git tag per approved major, no engine version in projects; closes THR.0130); POS.0950 no instance facts in the engine (`CLAUDE.local.md`, `settings.local.json`, git identity from the user's configuration; the scripts part of THR.0090 resolved, the thread otherwise untouched by decision); POS.0960 project kind `thought | library`; POS.0970 the library project and its knowingly unguarded cross-repository citation; POS.0980 publication — ownership, audience, the boundary for the public forge project, fresh history (DEC.0080, the company copy read-only). Rewritten: POS.0500, POS.0550, POS.0740 (template by path), POS.0760 (decided), POS.0830, POS.0930 (model in `settings.local.json`), POS.0180 (a bare `/ingest` sweep reports changed sources with a question, universally — a breach in a thought project, the normal case in a library). Rejected: REJ.0140 `local/` (POS.0750 dropped), REJ.0150 submodules, subtree, template repository, copying the engine, plugin-only. Opened: THR.0190 plugin as a later distribution layer, THR.0200 exemplar, repository name, licence; THR.0180 notes the first Czech project. CHL.0070–0130 resolve to this version. Instance work (the one-off migration, the first projects after the split) stays in the brief and the ledger, not in the intent; the operating layer changes with the migration, and 3.0 follows its verification by a fresh clone. | Claude | 2026-08-29 |
| 2.20 | Brief `00-brief-public-engine.md` locked at 1.0 (2026-08-29), rewritten in English within the boundary it sets for the public forge project — the first CTO challenge of a brief (2026-08-29-challenge-cto.md, CHL.0070–0130) walked through beforehand: six accepted into the brief (the engine is the principal's, built outside any work assignment; the publication audience; nothing company-specific by name in the public forge project, with a one-off rewrite of immutables; the library taken as a knowing cross-repository dependency; all plugin preparation dropped — git split only; git tags per approved major), CHL.0120 rejected in its remedy (DEC.0080: fresh public history, the company copy read-only). Positions unchanged: the brief is mined by `/forge intent` next. Consistency fixes from the pre-save check: POS.0530 no longer lets reviewers pin a model (POS.0930), POS.0400 says "isolated", not "independent" (POS.0790). | Claude | 2026-08-29 |
| 2.19 | Brief redefined in form at the principal's direction (POS.0110): free-form means no *required* structure, not no structure — headings, tables and use cases are legitimate, thoughts to be processed rather than decisions, changeable until mined; a summary ordered into a brief is stored as shown, never re-narrated as prose. Prompted by brief public-engine 0.4, where a structured summary had been converted into imitated speech. CLAUDE.md (chain item 1) and `/forge brief` aligned; README re-render pending. | Claude | 2026-08-29 |
| 2.18 | New open thread THR.0180 at the principal's direction: the output language. English as the language of every artefact (POS.0060) is not a property of the forge but the principal's own rule for the company projects of this instance; a project with Czech output is conceivable, and the public engine (00-brief-public-engine.md, draft) must carry no instance rule. Left as is for now — more than one output language is to be solved when a project needs it. Recorded at the same time: the brief `00-brief-public-engine.md` born on 2026-08-29 (draft 0.3, pending) and three research notes on engine distribution registered. | Claude | 2026-08-29 |
| 2.17 | THR.0160 closed at the principal's decision (POS.0930, new): one model for the whole forge — every command, state and reviewer runs on the session model, and the two agents say so explicitly (`model: inherit`; the `opus` pin on `challenger-cto`, set on 2026-08-03 when opus was the strongest model, had silently come to mean a weaker reviewer than the author). Per-command pinning to a faster model rejected on the day's analysis: the routine commands are a small share of the work, their slowness comes from carrying the whole conversation as context rather than from the model, and the pins would add a convention to keep. The lever adopted instead is context, not model: `/render` now generates in an isolated subagent that sees only the recipe and its inputs — faster and cheaper on any model, and the gain lands where it is felt most, in `/save`'s re-renders. A per-recipe `model:` choice was tested the same day (README rendered from recipe 0.19 by fable, sonnet and opus in isolation): sonnet loosened pinned wording, dropped two prescribed elements and leaned on the previous render instead of the recipe — the drift POS.0810 exists to prevent — while opus was fully adequate; the choice is therefore deferred until a recipe exists that is genuinely mechanical. CLAUDE.md (Renders, Two isolated reviewers), `/render` and both agent files aligned. | Claude | 2026-08-27 |
| 2.16 | Consistency sweep after the brief redefinition, at the principal's direction — the `/check-forge` findings of the pre-save check all fixed: POS.0320 now says a brief is immutable from its lock, the other immutables from creation; POS.0060 names the briefs (`00-brief*.md`) as the language exception. The same wording carried into CLAUDE.md (Versioning, spin-off rule, `/new-project` row), `/spinoff` (a derived brief is written as a draft and locked on approval), `/new-project` and `templates/ledger.md` (brief row 0.1 draft, pending), the critic and challenger inputs and `templates/intent.md` (locked briefs), `/ledger` (Briefs first), `/check`, the readme recipe (diagram label "draft → locked", "the brief as dumped") and the README. | Claude | 2026-08-27 |
| 2.15 | The brief conversation's role settled at the principal's direction (POS.0110 extended): `/forge brief` runs under his moderation — he says what is explored and steers; Claude clarifies where he is terse or unclear, never adding content of its own, and keeps correlating the thought with reality — best practice, projects and standards solving the same thing, "are we reinventing the wheel?" — through `/research` and `/ingest`, proposed by Claude and timed by the principal. The aim is a thought clear enough to be checked against what exists or to draw inspiration from it; what a check contributes enters the brief only by his word. `.claude/commands/forge/brief.md` rewritten accordingly. | Claude | 2026-08-27 |
| 2.14 | Briefs redefined at the principal's decision — THR.0110 (open since 0.8) closed. A brief is an intent that is composed and then locked: draft while written, approved (1.0) at the lock, immutable from the lock rather than from creation (POS.0110 rewritten; the draft state had been invisible because every brief so far was composed outside the forge). Three origins equally legitimate — arrives finished, begun outside and finished with Claude, born in the forge — with `/forge brief [name]` as the door for the latter two. A project may carry more than one brief (`00-brief-<name>.md`), each the birthplace of one whole of thinking that would otherwise enter the intent as a batch of unproven positions; the ledger's new Briefs table tracks version, status and a mining state `pending \| partial \| mined \| dropped` with a free-text note; mined positions cite the brief, a dead whole leaves the brief locked and one REJ (POS.0920, new). Branch documents — a per-whole working space with positions before the merge — considered and deferred as heavy (THR.0170, new). CLAUDE.md (chain, directive 6, ledger, commands), `templates/ledger.md`, `/forge` map, `/forge intent`, `/new-project`, `/check` and the forge ledger aligned; `.claude/commands/forge/brief.md` created. | Claude | 2026-08-27 |
| 2.13 | The day's critique (2026-08-27-critique.md) walked through — the first walkthrough under POS.0850 — with three of four findings fixed at the principal's direction: the portability rule of POS.0830 carried into CLAUDE.md (Persistence) and the Windows-flavoured usage examples in `doc2md.ps1` and `md2pptx.ps1` neutralised, the instance facts in `forge-save.ps1` deliberately left to THR.0090 (FND.0050); "Two independent reviewers" renamed "Two isolated reviewers" in the Essence and the CLAUDE.md heading, as POS.0790 requires (FND.0060); the ledger header comment and its template now say the ledger is freely rewritten alongside the material indexes, not the only such file (FND.0080). FND.0070 (README stale at intent 2.8) left open by decision — resolved by the mechanised re-render at the next `/save`. | Claude | 2026-08-27 |
| 2.12 | Working methods codified at the principal's decision — a new subsection of the collaboration model naming the ways a working conversation runs, so that commands and the README can refer to them and the principal can invoke them in a word: Walkthrough (POS.0850, new — any decision list worked one item at a time, Claude's recommendation first, "leave open" legitimate, written once at the end; whatever produces a list ends by offering one), Propose never decide (POS.0860), Elicitation interview (POS.0870), Draft early (POS.0880), Reflect back (POS.0890), Intent-first (POS.0900), Recommend do not push (POS.0910) — the last six naming positions that already stood, gathered under one heading. Prompted by the principal's observation that the item-by-item method is one of the pillars of why the forge works for him and had been used beyond findings (comparing requirement sets) while living only as scattered wording in command definitions. `/resolve` retired without alias: a per-verdict door never used, since verdicts were always given inside a walkthrough; its write-up rules move into POS.0850. `/critique` and `/challenge` now end by offering a walkthrough; CLAUDE.md gains a Working methods section; the README recipe (0.17) gains a Working methods section so newcomers learn how the work feels, not only what the files are. The critique of the same day (FND.0050–0080) is left open by the principal's direction, to be walked through later. | Claude | 2026-08-27 |
| 2.11 | Material indexes adopted at the principal's decision (POS.0840): every `sources/` and `research/` directory carries a freely rewritten `00-INDEX.md` — a light catalogue for Claude and the principal so that material need not be re-read to be known about. Sources entries: What / Origin / Role / Use for; research entries: Question / Answer in short / Consult when; Role is free text (a standard to verify against, inspiration, a counter-example, a meeting record). The index tracks nothing — no processing state, no positions — and is no automatic input of any command: a contradiction between the intent and a material is not a finding, since the material may be there as a warning or a mere inspiration; Claude reaches for a file by its own judgement or on request. Bundles keep their own `00-INDEX.md` and appear as one entry in the top index — two levels, never deeper. Ledger reduced to registration: the Purpose column leaves the Sources table (content lives only in the index) and a Research table is added; POS.0180 and POS.0160 aligned, the bundle index reclassified from immutable to a rewritten catalogue. `/ingest` and `/research` write the entries, `/check` verifies index against directory, `/new-project` scaffolds both indexes from `templates/index.md`. Indexes created retroactively for agentic-platform, flow-ba and forge. | Claude | 2026-08-27 |
| 2.10 | New open thread THR.0160 at the principal's direction: model selection per command and per subagent (`model:` front-matter in `.claude/commands/*.md` and `.claude/agents/*.md`) so that routine commands run on a faster model without manual `/model` switching, which drops the prompt cache. To be thought through and settled later. | Claude | 2026-08-25 |
| 2.9 | Portability of the scripts settled by the principal (POS.0830): the forge runs beyond Windows; `scripts/` is the only platform-bound layer, kept in cross-platform PowerShell 7 and written with nothing Windows-only — usage examples included — instance facts to move out of the scripts (THR.0090), verified by a run on Linux. A review of the five scripts found them already conforming except for the hard-coded instance facts and Windows-flavoured usage examples. Replacing the set with POSIX `sh` under Git Bash recorded as an open thread the principal is still weighing (THR.0150); a dual set and a Python rewrite excluded within it. | Claude | 2026-08-25 |
| 2.8 | First peer review of the forge itself settled — six CTO challenges (2026-08-17-challenge-cto.md), four accepted, two rejected, every verdict the principal's. POS.0780: the forge is a general tool for forging thoughts, ending where its owner is satisfied; delivery, sponsorship and outcomes deliberately out of scope and sight, the door to a delivery chain open (new THR.0140), development at the principal's discretion and pace (CHL.0010 accepted). POS.0790: isolation is not independence — the shared model family named as a limit, reviewer agreement never treated as validation, external human review by experienced practitioners recorded as the calibration point; POS.0800: independent challengers on a different model family (Microsoft AI Foundry, invoked over a CLI link) will be built, mechanics when taken up (CHL.0020 accepted). POS.0810: regenerated renders pass under the principal's eyes — recipes pin load-bearing wording, `/save` reports the material delta of regenerated renders; `/save` step and CLAUDE.md aligned (CHL.0040 accepted). POS.0820: artefacts do not expire with the conventions, migration is an explicit per-project decision; THR.0130 extended with the destination-not-foreclosure and public-exemplar notes (CHL.0050 accepted in part). CHL.0030 rejected (DEC.0060 — the growth path names direction, not destination; a layer's boundary is defined when the layer is taken up); CHL.0060 rejected (DEC.0070 — the forge is a deliberately chosen pursuit, not a budgeted work stream). flow-ba recorded as sleeping by the principal's decision, its handover with the recipients. | Claude | 2026-08-18 |
| 2.7 | First critique round of the forge project settled, all four findings fixed at the principal's direction: README re-rendered with its title at the current intent version (FND.0010); a note added under Open threads recording the accidental double use of THR.0120 and fixing which thread its citations refer to (FND.0020); the stale decisions.md header comment updated — THR.0070 was resolved by DEC.0040 (FND.0030); DEC.0050 appended, recording the v1.20 generalisation of DEC.0020 that the append-only log had missed (FND.0040). | Claude | 2026-08-17 |
| 2.6 | Release notes made continuously current at the principal's decision: the majors-only regeneration left `RELEASE-NOTES.md` stale between approvals — the README's first line links to it while the intent moves on in minors, so the reader of a 2.5-titled README landed on notes ending at 2.0. POS.0730 rewritten: an Unreleased section on top summarises the changes since the last approved major and is regenerated by every `/save` touching the core or `projects/forge/`, alongside the README; released major sections stay carried over verbatim, and at a major approval the Unreleased head is recast as the new major's section. Recipe release-notes v0.2, `/save` step 2, CLAUDE.md and README aligned; RELEASE-NOTES.md re-rendered with its first Unreleased section. Recorded from the same day's recipe-only rounds: the README restructured for scannability at the principal's direction (readme recipe 0.12–0.15, structural inspiration from an external README he brought in) — masthead rebuilt as identity plus the principle's three bold forms, a challenge-headed opening section ("Better with AI, or replaced by it?") over the failure modes it removes, a "What you get" capability list, sections regrouped story → concepts → reference, two callouts in the chain section. | Claude | 2026-08-17 |
| 2.5 | The scripts-only door to git made exception-free at the principal's direction: the `/save` procedure itself had been reading git state directly (`git status` for scope, `git show` for verification) while the rule said scripts are the only door. A dedicated read-only script `forge-status.ps1` is added (reports unsaved changes and the last commit, changes nothing) — a status call does not belong in a script named save, so the trio reads by name: save, pull, status. `forge-save.ps1` additionally prints the committed file summary itself; the `/save` command now determines scope through `forge-status` and does no direct git verification. POS.0550 extended — three scripts, the door rule covers reading state too, with no exceptions. CLAUDE.md Persistence and README aligned. | Claude | 2026-08-17 |
| 2.4 | THR.0120 closed by the principal's decision: the enumerated delivery-stage ban (stakeholder matrices, RACI, impact analyses, MECE decompositions, tables of contents) originated in one early case and is not a universal principle. POS.0210 rewritten to the boundary of kind alone — an assignment assigns, it does not solve; any such apparatus may appear where the principal judges it part of setting direction. CLAUDE.md directive 8 and the `/forge assignment` drafting rule aligned; the critic's calibration needed no change (it already treats only solving-instead-of-assigning as the defect and never reports missing apparatus). README paragraph reduced to the boundary sentence (readme recipe 0.11). | Claude | 2026-08-17 |
| 2.3 | README recipe overhauled (v0.10) after an external critique round the principal brought in, all verdicts his: a Quickstart with the bootstrap step (clone this repository — the hardest gap: the README never said how to obtain the forge), an ontological sentence in the masthead (a git repository: slash commands, agent personas, templates, conventions), consolidated prerequisites naming PowerShell 7 on every platform, a real assignment excerpt (REQ.0430) illustrating the requirement style, slimmed command-table cells with mechanics moved below the table, `/forge` vs `/ledger` disambiguated, agent-rule dedup (only-door-to-git stated once), Naming folded into Conventions, first-definition bolding, a collaboration-model sentence; the render's visible YAML provenance kept by design (POS.0710). Language rule clarified at the principal's decision: the forge as a system dictates only the output language — all artefacts in English — while the working-conversation language is per-instance configuration that stays in the operating layer (CLAUDE.md directive 6 and the command definitions, currently Czech) and never appears in outward-facing renders: the README drops it entirely (POS.0060 rewritten). README re-rendered. | Claude | 2026-08-17 |
| 2.2 | Guided recipe composition adopted at the principal's decision: `/recipe <genre>` mirrors the `/forge` star — a thin dispatcher plus one definition file per genre carrying the elicitation checklist, the genre's canonical skeleton in `templates/recipe-<genre>.md` (POS.0770). First genre `presentation`, distilled from the agentic-platform IT-deck recipe: audience and register, the one message, dramaturgy, speaker notes and traceability citations, on-slide density, diagram policy, language, vocabulary discipline, confidentiality, and Build instructions copied verbatim into the render for the deck-builder LLM. "presentation" chosen over "deck" for company-wide legibility at rollout. A render may now serve as an input of another render — a slide citing an architecture picture as `render: <file>` — declared among the recipe's Inputs so provenance and staleness track it (POS.0710 extended). `md2pptx.ps1` gains `-Model`, default opus (POS.0740 extended). Render and check commands aligned; README re-rendered. | Claude | 2026-08-17 |
| 2.1 | Deck generation adopted at the principal's decision: `scripts/md2pptx.ps1` turns a Markdown deck render into a PowerPoint file through headless Claude Code with the official pptx skill — an LLM conversion by design, because deck definitions are free-form and carry instructions for the model (POS.0740; POS.0590 reworded: the forge still ends at content, with this one delivery tool at its edge). User-local files get a home: flat `local/` in the repository root, gitignored except its tracked README — first tenants are `.potx` deck templates, addressed by bare name with `default.potx` as the fallback (POS.0750); the generated `.pptx` lands beside its source render and is tracked. Course set for splitting the forge into a public engine and private user projects, the engine carrying no company-specific data and each user responsible for their own repository (POS.0760); the split mechanics are open as THR.0130. CLAUDE.md and README aligned; validated by generating a full deck from the agentic-platform IT-deck render. | Claude | 2026-08-17 |
| 2.0 | Approved by the principal: the second baseline of Forge of Thought, incorporating all changes since 1.0. The wave in synthesis: the chain is worked by target state (`/forge` map and states; `/clarify` and `/draft` retired); renders became a first-class concept (recipes iterated, outputs generated, README a render regenerated automatically on every core save); the challenger grew into a persona panel with hardened calibration, aimable at any chain artefact; ingest reduced to pure registration, with bundles and `doc2md` as the only conversion path; git persistence with `/save` and the visible pre-save check; and the paradigm shift from short-and-airy to complete-and-precise assignments. Release notes introduced with this approval (POS.0730): `RELEASE-NOTES.md` in the repository root, one section per major version, rendered from `recipes/release-notes.md` only at major approvals, released sections carried verbatim. Open by design: THR.0090, THR.0110, THR.0120. | Claude | 2026-08-15 |
| 1.24 | Brevity paradigm dropped at the principal's decision — the goal shifted with the widening project mix: the goal is to have it right, not short. An assignment carries the complete in-scope substance of the intent, written as precisely as it can be; a silent omission is a defect, explicit delegation (DEL/TBC) stays legitimate, length is whatever fidelity requires. Essence and POS.0130 rewritten; POS.0210 (delivery-stage apparatus stays out) kept as a boundary of kind, its final form opened as THR.0120. CLAUDE.md prime directive 8, critic calibration, critique template and the assignment state file aligned. | Claude | 2026-08-15 |
| 1.23 | `doc2md` adopted as the only document→Markdown conversion path at the principal's decision: his `scripts/doc2md.ps1` (engine: markitdown, installed separately) produces every text extract — `/ingest` runs it file by file with `-Suffix '.extract'` on binary formats; ad-hoc parsing (e.g. Python PDF libraries) is banned. The `-Suffix` option was added to the script for this. POS.0180 extended; ingest command, CLAUDE.md (layout + external-inputs rule) and the readme recipe (0.4 — Scripts purposes drawn from CLAUDE.md at large) aligned. | Claude | 2026-08-15 |
| 1.22 | `/save` re-renders the README at the principal's decision: a save touching the core or `projects/forge/` regenerates `README.md` from its recipe before the conformance check — unconditionally, no staleness test, the step reported. Staleness detection was considered and dropped: what matters is the content of the inputs, not cited versions, and an unconditional render is cheaper than the detection debate. Other renders stay ordinary check findings. POS.0570 extended; save command and CLAUDE.md aligned. | Claude | 2026-08-15 |
| 1.21 | `/render` argument relabelled from `<purpose>` to `<recipe>` at the principal's request: the argument selects the recipe, and the label now says so — the slug itself still names recipe, render and purpose alike, and the recipe's `purpose:` front-matter field is unchanged. Wording-only; command, CLAUDE.md, README and the recipe template aligned. | Claude | 2026-08-15 |
| 1.20 | Challenger opened to any chain artefact at the principal's request: `/challenge <persona> [artefact]`, default `intent`. The pre-assignment framing was an artefact of the version-1 world ending at the assignment, not a principle; the general rule is that a layer is best challenged before the next one is first derived from it, while accepted challenges are cheap. The challenger reads the whole chain for context and aims at the target. POS.0420 and POS.0450 updated; DEC.0020 ("before the first draft") generalised accordingly, its reasoning intact. Command, agent, CLAUDE.md and README updated in the same step. | Claude | 2026-08-15 |
| 1.19 | Challenger calibration hardened, inspired by the principal's own pre-forge CTO-challenger prompt (pasted in conversation, adopted selectively by his decision): challenges carry a severity (dealbreaker \| major \| minor) and are ordered by it; the epistemic scale widens to consensus \| active debate \| emerging practice \| my judgement; anti-fabrication discipline (a precise "I don't know" beats an invented figure, reconstructed numbers and citations are flagged); flawed assumptions in the material are corrected before anything is built on them; on technical trade-offs mechanism leads, not the analyst framework. Severity, the epistemic scale and anti-fabrication became shared invariants of all personas in `/challenge`; the rest lives in `challenger-cto`. Deliberately not adopted: proposing rewrites (collides with the critic split and the principal-composes rule), interactivity (collides with isolation), unbounded breadth (sharp-and-few stands). POS.0420 updated. | Claude | 2026-08-15 |
| 1.18 | Challenger generalised to personas at the principal's request (THR.0100 closed): `/challenge <persona>` selects the lens, one isolated agent per persona (`challenger-<persona>`), bare `/challenge` lists the roster and recommends a fit. The shared skeleton is invariant (blind context, substance only, 3–7 sharp challenges with falsifiable tests and epistemic status, CHL output); a persona defines only what it looks with. First persona `cto` carries the former challenger unchanged; further personas (a strategist, a business analyst) are created when first needed, and only where their blind spots genuinely differ — mechanics-when-taken-up, as with chain layers. Challenge files now carry the persona in their name. POS.0400 and POS.0420 rewritten; CLAUDE.md, `/challenge`, agent files and README updated in the same step. | Claude | 2026-08-15 |
| 1.17 | Conformance checks extended to recipes and renders at the principal's request: `/check-forge` gains a "Recipes and renders" section (recipe shape against `templates/recipe.md`, declared inputs exist, `output:` valid, render staleness by front-matter provenance, ledger Renders mirror) and `/check` an equivalent per-project check. Boundary held: shape and freshness only — whether a recipe's content still matches the principal's thinking is substance, for the principal and the reviewers, never for the mechanical check. POS.0540 unchanged in principle. In the same round the readme recipe moved to v0.2: "How it is used" split into the general flow and a worked example generated from the agentic-platform inputs (its ledger and intent added as recipe inputs), renders added to the chain diagram, and the README re-rendered. | Claude | 2026-08-15 |
| 1.16 | Recipe looseness made a property of the concept at the principal's request (POS.0710 extended): a template fixes the structure and what information appears where, never the wording — each rendering re-derives the words from the current inputs. First recipe created (`recipes/readme.md` v0.1) and README rendered for the first time — THR.0120 closed. The README gained a "How it is used" user-story section at the principal's request; the visible dated footer stays for now, pending the principal's further input. CLAUDE.md's README rule reworded recipe-first at the principal's request (POS.0720 aligned): the README is generated from its recipe, never edited by hand; a process change is complete only once the intent is updated and the README re-rendered. | Claude | 2026-08-15 |
| 1.15 | `/check-forge` findings settled: recipes exempted from the full versioning apparatus by the principal's decision (POS.0710 extended) — bare version and updated date in front-matter, no status, no Version History; change history lives in git, the full apparatus belongs to approved-and-handed-over documents. CLAUDE.md aligned (Renders paragraph, recipe template comment) and its Ledger section now enumerates all ledger tables (documents, renders, sources, findings, challenges). README staleness left standing by design (THR.0120). | Claude | 2026-08-15 |
| 1.14 | Chain commands renamed by target state at the principal's request: `/clarify` and `/draft` retired without aliases, replaced by `/forge` — bare, a state map; with a target (`/forge intent`, `/forge assignment`), work on that artefact. One definition file per state declares its own inputs, so the chain may branch into a star without new conventions (POS.0580). Derivatives reconceived as renders (POS.0710 rewritten): the iterated thing is the recipe (`recipes/<purpose>.md` — inputs, audience, instructions, template, one versioned file), the output generated by `/render <purpose>` into `renders/<purpose>.md`, undated and overwritten, YAML front-matter provenance, history in git. Everything the forge produces is Markdown; format conversion happens outside (POS.0590). README.md becomes a render of this project (POS.0720); its recipe is yet to be created (THR.0120) and the file stands unchanged until then. CLAUDE.md, templates (recipe added, ledger Renders table), command files and both project ledgers updated in the same step; agentic-platform's `derivatives/` migrated to `renders/`, dated editions kept as legacy history. | Claude | 2026-08-15 |
| 1.13 | Derivatives introduced at the principal's request (POS.0710): a project's intent may spawn audience-specific condensations — a pitch, an architecture picture, an executive summary — living in `projects/<slug>/derivatives/` as dated editions (`YYYY-MM-DD-<purpose>.md`). A derivative assigns nothing and is not part of the chain; the intent remains the source of truth. Editions may be polished in place while current and are superseded by a new dated file when the intent moves substantially; the project ledger lists them. First instance: the agentic-platform group pitch. CLAUDE.md, README and the ledger template updated in the same step. | Claude | 2026-08-09 |
| 1.12 | The fixed assignment size limit dropped at the principal's request (POS.0130): "page" is meaningless in Markdown and large subjects (first collision: agentic-platform) legitimately need more room. The defect remains excess detail — solving instead of assigning — never length as such; "short and airy" stays as the guiding style. CLAUDE.md directive 8, README chain table, `templates/critique.md` checklist and `/draft` updated in the same step; the two immutable flow-ba critique files retain the old checklist wording as history. | Claude | 2026-08-08 |
| 1.11 | Ingest reduced to registration at the principal's request (POS.0180): `/ingest` stores, registers and catalogues — it no longer processes anything into the intent. A source's role is individual — a standard to verify against, inspiration, a meeting record — so the principal alone directs how and when each source is used; sources may arrive at any stage, even before the brief. The ledger's `State: pending | processed` column, built on the pipeline just removed, replaced by free-text `Purpose` (flow-ba's "reference only" entries had already outgrown it). The no-silent-promotion principle stands: source content enters the intent only by the principal's explicit act, with provenance. `/ingest`, CLAUDE.md, README, ledger template and project ledgers updated in the same step. | Claude | 2026-08-08 |
| 1.10 | Bundle index adopted at the principal's request (POS.0180): every source bundle carries a `00-INDEX.md` — YAML header (bundle, project, date, origin) plus one paragraph on the whole, then a File / What it is / Origin / Date table. Created by `/ingest` at registration when missing, validated against contents when supplied; purely descriptive — processing state stays in the ledger only — and immutable with the bundle. `/ingest` and CLAUDE.md updated in the same step. | Claude | 2026-08-08 |
| 1.9 | Source bundles adopted at the principal's request (POS.0180): a set of related files (e.g. a downloaded site with its index) may live as a subdirectory `sources/<slug>/` — one source, one ledger entry, immutable as a whole from registration. Granularity settled after discussion: the ledger tracks the bundle, not its files, because its job is only existence and pending/processed state; file-level detail is preserved by intent provenance citing individual paths and by the bundle's index/extract. A file may be split out to its own row later if processing diverges. `/ingest`, CLAUDE.md and README updated in the same step. | Claude | 2026-08-08 |
| 1.8 | Brief scaffolding adopted at the principal's request (POS.0110): `/new-project` creates `00-brief.md` at scaffold time as an empty file with the YAML header pre-filled, instead of leaving the file absent until the brief arrives. The principal's verbatim text completes it; immutability starts from that moment. `.claude/commands/new-project.md` updated in the same step. | Claude | 2026-08-08 |
| 1.7 | `/save` extended at the principal's request: unless `-m` is given, Claude drafts the commit message and proposes it for confirmation before running the script. | Claude | 2026-08-04 |
| 1.6 | `/save` command adopted at the principal's request: the POS.0570 procedure gets its door — scope-routed check (core → `/check-forge`, project → `/check <slug>`), findings settled iteratively with the principal (acceptance may be a deferral, recorded in the ledger), script run only afterwards. Command file created; CLAUDE.md and README updated in the same step. | Claude | 2026-08-04 |
| 1.5 | Division of creative labour made explicit at the principal's request: POS.0070 — Claude criticises, challenges, inspires and lays out options; the principal composes. Nothing becomes content because Claude proposed it, only because the principal took it up. CLAUDE.md Roles and README §1 mirrored in the same step. | Claude | 2026-08-04 |
| 1.4 | POS.0520 rewritten to match reality after the sandbox experiment: OS-level sandboxing was configured, immediately blocked all shell execution on Windows (sandbox unavailable there), and was dropped by the principal's decision in favour of the permission system — prompts, allowlists, shared deny rules for sensitive paths, per-domain web approval. README §7 bullet reworded accordingly ("Sandbox" → "Permissions"). | Claude | 2026-08-04 |
| 1.3 | Pre-save check adopted at the principal's request (POS.0570): a save invoked through Claude is preceded by the relevant conformance check, with findings settled or explicitly accepted before the commit — recommended procedure, never a gate. Outcome of the first `/check-forge` run recorded: shared `.claude/settings.json` created (model pin, sandbox, permission policy), turning POS.0520 and POS.0530 from promise into configuration; CLAUDE.md layout now lists `.claude/`, command signatures aligned with README. CLAUDE.md (Persistence) and README (Saving and syncing) updated in the same step. | Claude | 2026-08-04 |
| 1.2 | Git persistence layer documented (built 2026-08-03, write deferred by the principal until this round): repository backed by GitLab, linear history on `main`, `forge-save.ps1` / `forge-pull.ps1` as the intended interface — recorded as POS.0550. Project avatar convention adopted: `logo.png` in the repository root via GitLab auto-detection, an `assets/` directory deferred until images beyond the logo exist — recorded as POS.0560. CLAUDE.md (layout + new Persistence section) and README.md (layout + Saving and syncing) updated in the same step. | Claude | 2026-08-04 |
| 1.1 | Self-description reframed at the principal's request: the forge is a place where thoughts are forged, not an engine defined by its current end product. README masthead reworked — subtitle "A workshop where thought is tempered and shaped." adopted and recorded as POS.0620, with the rule that no subtitle may name the assignment as the goal. Opening sentences of CLAUDE.md and of the Essence here aligned to the same framing. | Claude | 2026-08-03 |
| 1.0 | Approved by the principal: version 1 of Forge of Thought declared. The engine as designed — chain ending at the assignment, two independent reviewers, conformance commands, write-once-per-round cadence — is the approved baseline. Open threads THR.0090, THR.0100 and THR.0110 remain open by design. | Claude | 2026-08-02 |
| 0.11 | Write cadence generalised at the principal's request (POS.0190): once per iteration round for any working conversation over the intent or open items, not only `/clarify`; Claude asks at the round's end and writes on confirmation; the principal may order a write at any moment. Promoted to a prime directive in CLAUDE.md; `/clarify` step 4 and README aligned. | Claude | 2026-08-02 |
| 0.10 | Two conformance commands added at the principal's request (POS.0540): `/check-forge` — careful consistency check of the core and `projects/forge/` cross-checked against each other — and `/check [slug]` — conformance of a project against the current conventions, all projects except forge when run bare. Both advisory and read-only; they check conformance, never substance or document quality. CLAUDE.md and README updated in the same step. | Claude | 2026-08-02 |
| 0.9 | Wording at the principal's request: "chaotic" dropped from the tagline and essence everywhere — the engine forges thoughts, presuming nothing about their kind (README, CLAUDE.md, Essence, POS.0600). README title typo "Forge of Thought2" fixed. Consistency sweep: README "Planned extensions" rewritten to match POS.0700 (withdrawn `/elaborate` removed), heading level of "Structure and style of an assignment" fixed, REJ.0125 no longer cites a brief that no longer exists. | Claude | 2026-08-02 |
| 0.8 | New open thread THR.0110: additional briefs during a project's life — the principal's idea, with Claude's proposed mechanics (briefs as `00-brief-<slug>.md`, processed by `/clarify` into the single intent) recorded for his consideration. Principal thinking it over. | Claude | 2026-08-02 |
| 0.7 | Open-thread sweep by the principal. Expansion intent recorded as POS.0700 (BRD certain, solution architecture and integration intended, strategy possible; selection and order open) and the premature `/elaborate` mechanics withdrawn — THR.0020 and THR.0030 closed. `/status` renamed to `/ledger` over the real collision with the built-in command (THR.0050 → DEC.0030). THR.0060 closed: iteration is the normal mode, not a managed milestone, and the first configuration iteration in fact came from FLOW:BA. No back-fill of DEC records; kept from now on (THR.0070 → DEC.0040). THR.0090 reframed to the git-fork working assumption and left open for the future. | Claude | 2026-08-02 |
| 0.6 | THR.0040 resolved by the principal (→ DEC.0020): `/challenge` runs before the first draft; any further runs are at the solver's discretion (POS.0450). The challenger itself will be refined further and stays as-is for now (THR.0100). | Claude | 2026-08-02 |
| 0.5 | Write cadence of `/clarify` corrected at the principal's request during the first FLOW:BA interview: the intent is written once per iteration, not per answer (POS.0190). `.claude/commands/clarify.md` step 4 rewritten to match. | Claude | 2026-08-01 |
| 0.4 | Ingest friction removed at the principal's request: no dates in source filenames (plain slugs), origin dates recorded best-effort in the ledger (content | file | ingested) and never asked for, `/ingest` without arguments sweeps `sources/` for manually dropped files, `/status` reports unregistered and pending sources. | Claude | 2026-07-31 |
| 0.3 | External inputs approved and built: `sources/` per project plus `/ingest`, immutable dated originals with extracts, provenance-first processing into the intent (THR.0010 → POS.0180). Ledger gains a Sources table. | Claude | 2026-07-31 |
| 0.2 | Reframed per the principal's brief (see 00-brief.md): Forge of Thought is a general engine forging chaotic thoughts into assignments, usable by anyone; the CTO-to-heads framing is dropped as an instance fact, and the growth path toward BRD, architecture and a full realisation deck is promoted to the primary ambition, with version 1 scoped to end at the assignment. Audience terminology generalised (heads → recipients). | Claude | 2026-07-31 |
| 0.1 | Initial consolidation, written retrospectively from the design conversation that produced the core, the templates and the command set, including the adoption of the group BRD conventions and the Forge of Thought naming. | Claude | 2026-07-31 |

## Essence

**Forge of Thought** is a place for forging thoughts — a workshop
where thought is tempered and shaped. It began as one CTO's tool for
briefing his direct reports; that origin is now an instance fact, not the
system. Anyone can be the principal, the subject matter is deliberately
unconstrained — process redesign, platform initiatives, organisational
topics, anything — and the recipients of an assignment may be teams,
colleagues, or the principal's future self.

The primary ambition is the full chain: from a raw idea all the way to a
deck ready for realisation, growing layer by layer — assignment, then a
BRD, then solution architecture, up to implementation-ready specification
including integration. **Version 1 deliberately ends at the assignment.**
Every design decision below is made with that growth in mind, which is
why files and IDs are numbered with gaps and why the name says thought,
not assignment.

The engine runs in Claude Code. Claude acts as the principal's cognitive
extension: it owns structure, order and process discipline, while every
decision about content remains the principal's. Two isolated AI
reviewers, deliberately blind to the working conversation, provide
adversarial pressure from two different angles.

The design constraint that shapes almost everything: an assignment must
carry the complete in-scope substance of the intent, written as well and
as precisely as it can be. Nothing is omitted for brevity's sake; length
is whatever fidelity requires. What keeps it an assignment rather than a
solution is the kind of content, never the amount.

## Positions

### Collaboration model
- **POS.0005** Forge of Thought is a general-purpose engine, not bound
  to one person or one management relationship. "Principal" means
  whoever's thinking is being forged; "recipients" means whoever
  receives the assignment. PCHe (CTO) is the engine's author and its
  first principal (POS.0990); who the principal of an instance is lives
  in `CLAUDE.local.md` (POS.0950).
- **POS.0010** Claude is the principal's cognitive extension, not a
  supplier. Claude owns structure, order and document hygiene; the
  principal owns content and every decision.
- **POS.0020** Claude's default under uncertainty is to ask, never to
  assume. Beyond answering, Claude actively elicits: helping the
  principal extract what he has not yet articulated is part of the job.
- **POS.0030** Claude never introduces a new convention, prefix or
  section unilaterally: propose, wait for a decision, then write it down.
- **POS.0040** Many iterations are the normal mode. Intent and
  assignments may grow or change substantially between versions.
- **POS.0050** For key topics Claude researches current best practice
  rather than inventing. Outside inspiration is a legitimate input;
  durable findings are stored in `research/`, not left in chat.
- **POS.0060** The forge as a system dictates only the output
  language: all artefacts are written in English; the single
  exception is the briefs (`00-brief*.md`), stored verbatim in
  whatever language they were written. The working-conversation
  language is per-instance configuration, not a system rule: it is
  set in `CLAUDE.local.md` (POS.0950) and read from there by every
  command — never written into the operating layer, and never
  presented outward. The README and other outward-facing renders
  state only the output-language rule.
- **POS.0070** Claude's contribution to content is to criticise,
  challenge, inspire and lay out options; the composition is the
  principal's. He assembles what the forge offers into his own
  positions and decisions — nothing enters the content because
  Claude proposed it, only because the principal took it up.
  "Cognitive extension" (POS.0010) means an amplifier of the
  principal's thinking, never its substitute.

### Working methods
The named ways a working conversation runs. They are the forge's
vocabulary of collaboration: each has a name so that command
definitions and the README can refer to it and the principal can
invoke it in a word. None is a command — a command has one input and
starts on demand; a method applies whenever its situation arises,
whatever produced it. Some are new positions here; others name a
position that already stands elsewhere.

- **POS.0850 Walkthrough.** Any list of items that need the principal's
  decision — critique findings, challenges, the differences between two
  requirement sets, open threads, TBC items before a handover — is
  worked one item at a time, in order of weight. For each item Claude
  first gives its recommendation with a one-sentence reason; the
  principal decides in a word or with a counter-proposal; "leave it
  open" is a legitimate verdict, not a failure. A table asking for every
  verdict at once is never put in front of the principal. One item per
  message. Claude puts one item in front of the principal, with its
  recommendation and the reason, and stops. The principal gives his
  verdict. The next message opens with one line acknowledging that
  verdict and then carries the next item, nothing else. A check whether
  Claude has understood an item fully is an item of its own. An
  elicitation interview runs the same way: one question per message, the
  answer acknowledged before the next question is asked. A questionnaire
  of several questions at once is the table of verdicts in another coat
  and is never put in front of the principal. Verdicts are carried in
  the conversation and written once at the round's end (POS.0190):
  findings and challenges change state in the ledger, an overruled
  finding or rejected challenge becomes a DEC record with its reason, a
  fix becomes an iteration of the artefact it concerns, an accepted
  challenge must change the intent. Whatever produces a list ends by
  offering a walkthrough — `/critique`, `/challenge`, the `/forge` map,
  a comparison made on request — and the principal may call for one at
  any moment. The former `/resolve` command, a per-verdict door the
  principal never used because verdicts were always given inside a
  walkthrough, is retired without alias; its write-up rules live here.
- **POS.0860 Propose, never decide.** Claude criticises, challenges,
  inspires and lays out options; the principal composes (POS.0010,
  POS.0070). Nothing enters content because Claude proposed it.
- **POS.0870 Elicitation interview.** Claude draws out by questions
  what the principal has not yet articulated, rather than filling gaps
  by assumption (POS.0020); the heart of `/forge intent`.
- **POS.0880 Draft early.** An early draft is an elicitation tool,
  not an output: concrete text sharpens the principal's reaction
  (POS.0150).
- **POS.0890 Reflect back.** Before anything is written, Claude
  restates what it understood the principal to have said, so that the
  write is a confirmation and not a surprise; the companion of
  write-once-per-round (POS.0190).
- **POS.0900 Intent-first.** A change of substance goes into the
  intent and propagates from there; only wording is fixed downstream
  directly (POS.0140).
- **POS.0910 Recommend, do not push.** Every option Claude lays out
  comes with its recommendation and reason, stated once; a declined
  recommendation is not re-argued unless new facts appear.

### Document chain
- **POS.0100** Files in the chain are numbered in tens (`00-brief.md`,
  `10-intent.md`, `20-assignment.md`) so later layers — a BRD
  (`30-brd.md`), a solution design — can be added without renaming
  anything that exists.
- **POS.0110** A brief is an intent that is composed and then locked.
  It is the principal's own text — the birthplace of one whole of
  thinking — free-form: any structure the principal finds useful
  (prose, headings, tables, use cases), no required content and no
  IDs; only a minimal YAML header (project, title, date, author,
  version, status). It holds thoughts to be processed, not decisions:
  they may be changed, reworked or dropped when mined, and only the
  intent turns them into positions. No structure is *required*
  because a required one would force premature tidiness and destroy
  the diagnostic value of how the idea was actually dumped — but none
  is forbidden either, and a summary the principal orders into a
  brief is stored as shown, never re-narrated. A brief has two states:
  *draft* while it is being composed, and *approved* (version 1.0)
  once the principal locks it; immutability runs from the lock, not
  from the file's creation. Three origins are equally legitimate and
  the forge does not distinguish them: the brief arrives finished from
  outside and is locked on arrival (the founding case so far — every
  brief to date was composed outside the forge, which is why the draft
  state was invisible until 2026-08-27); it is begun outside and
  finished with Claude in the forge; or it is born in the forge from
  the first word. `/forge brief [name]` is the door for the latter two,
  and it runs under the principal's moderation: he says what is being
  explored and steers; Claude's role is to clarify where he is terse
  or unclear — never to add content of its own — and to correlate the
  thought with reality throughout, offering best practice, projects
  and standards that solve the same thing ("are we reinventing the
  wheel?") through `/research` and `/ingest`, which Claude proposes
  and the principal times. The aim of a brief is a thought clear
  enough to be checked against what exists or to draw inspiration
  from it; what such a check contributes enters the brief only by the
  principal's word — the brief stays his text, not a literature
  review. `/new-project` creates `00-brief.md` at scaffold time with the
  pre-filled header; the principal's verbatim text completes it. A
  locked brief is the provenance anchor of its whole: the record
  against which later drift is measured.
- **POS.0920** A project may have more than one brief, and the ledger
  tracks how far each is mined. The founding brief is `00-brief.md`;
  every later whole of thinking that would otherwise land in the
  intent as a batch of unproven positions is born as
  `00-brief-<name>.md` — same header, same states, same rules. A
  locked brief is mined into the single intent: positions cite the
  brief as provenance; a whole that dies on the way leaves the brief
  locked and one REJ in the intent with the reason, so the trace
  survives either way. The ledger's Briefs table carries one row per
  brief — version, status and a mining state `pending | partial |
  mined | dropped` with a free-text note (what remains for *partial*,
  the REJ for *dropped*); "how much" is a judgement recorded in that
  note and in the provenance of the positions, never a metric.
  `/forge` shows pending and partial briefs as next steps, `/forge
  intent` offers them for mining, `/check` compares the table with the
  directory. Rationale: a big new whole needs a place where the
  thought can be tempered before it enters the trunk — like a git
  branch — without a new document kind; THR was wrong for it (a
  thread is a question, not a body of work), and a working space with
  positions before the merge (a branch document) was judged heavy for
  now (THR.0170). Closes THR.0110 (opened 0.8, 2026-08-02).
- **POS.0120** `10-intent.md` is the working document: the consolidated
  *current* state of the principal's intent. Not an append-only log; it
  is rewritten for coherence each round, with changes recorded in its
  Version History. It exists because chat context dies and anything of
  value must live in a file: it is the document to read when returning to
  a project after weeks, instead of excavating old conversations.
- **POS.0130** `20-assignment.md` is the distilled handover document for
  the recipients: complete, precise, structured, self-contained,
  versioned. It carries the whole in-scope substance of the intent —
  nothing is left out for the sake of brevity, and a silent omission is
  a defect; leaving a matter out is legitimate only as an explicit
  delegation (a DEL or TBC item). There is no size target in either
  direction: length is whatever fidelity requires, and the defect is
  excess of the wrong kind (solving instead of assigning), never length
  as such. The earlier short-and-airy paradigm was dropped on
  2026-08-15 — the goal is to have it right, not short; the ≤ 3-page
  target had already been dropped on 2026-08-08. The name "assignment"
  was kept deliberately after considering alternatives; it does not
  preclude further layers below it.
- **POS.0140** Substance changes go intent-first and then propagate to
  the assignment; wording-only fixes may edit the assignment directly. If
  the principal dictates substance straight into the assignment, the
  corresponding intent update is proposed in the same step.
- **POS.0150** Drafting early is a legitimate elicitation tool, not a
  violation of sequence. Concrete text sharpens critique.
- **POS.0160** Supporting artefacts: `decisions.md` (append-only, DEC),
  `ledger.md` (single source of truth for state, freely rewritten),
  `reviews/`, `challenges/`, `research/` (all immutable, dated); the
  `00-INDEX.md` catalogues of `sources/` and `research/` are freely
  rewritten like the ledger (POS.0840).
- **POS.0170** Feedback from recipients has no channel of its own. The
  principal processes it and feeds conclusions back through
  `/forge intent`.
- **POS.0180** External inputs (transcripts, offers, documents,
  standards) live in `sources/` per project: immutable once registered,
  plain slug filenames, each in one form — text, or a functional
  binary (POS.1040).
  They may arrive at any stage of a project's life — before the brief
  as material for writing it, during intent work, or after. Origin
  dates are metadata, not ceremony: recorded best-effort in the ledger
  (content | file | ingested) and never demanded from the principal.
  The principal may drop files into `sources/` manually at any time;
  `/ingest` without arguments sweeps the directory: it registers new
  files and reports files changed since registration (modification
  time against the ledger date) with a question — what to do with
  each. The meaning depends on the project's kind (POS.0960): in a
  `thought` project a changed source is a breach of immutability to
  be settled (a new version beside it, or knowingly accepted); in a
  `library` project it is the normal case — the extract is
  regenerated, the ledger date moved, the index entry corrected.
  `/ingest`
  stores, registers and catalogues — nothing more. Registration does
  not imply intake: what a source is for is individual — a standard to
  verify against, inspiration, a meeting record, material to absorb —
  and is recorded as free-text Role in the directory's `00-INDEX.md`
  (POS.0840), taken from the principal in a sentence when he offers
  one, never demanded; the ledger row is registration only. The
  principal alone directs how and when a source is used, in whatever
  work he chooses. When source content does enter the intent, it is
  his explicit act, cited with provenance to the file; what someone
  said in a meeting is never silently promoted to the principal's own
  position. A set of related files — a downloaded site with its index,
  a document with attachments — may live as a subdirectory
  `sources/<slug>/`: one source, one ledger entry, immutable as a
  whole from registration. File-level detail is not lost: provenance
  in the intent cites individual files by path, and the bundle's index
  or extract lists its contents. If a bundle's files ever need
  separate fates, a file may be split out to its own ledger row — the
  ledger is freely rewritten. Isolated files stay directly in
  `sources/` as before. Every bundle carries a `00-INDEX.md`
  catalogue: a YAML header (bundle, project, date, origin), one
  paragraph saying what the whole is and why it entered sources, and a
  table of File / What it is / Origin / Date — origin dates best
  effort, never asked for. `/ingest` creates the index at registration
  when the bundle lacks one and validates a supplied one against the
  contents. The index is purely descriptive; unlike the files it
  catalogues it is a rewritten catalogue, not an immutable artefact
  (POS.0840). Text extracts are produced by
  `scripts/doc2md.ps1` (engine: markitdown, installed separately),
  never by ad-hoc parsing — no Python PDF reading, no manual
  transcription. `/ingest` runs the script file by file on every
  binary the principal chooses to convert (POS.1040), in bundles as
  well as for isolated files; the output is `sources/<slug>.md`, the
  source itself.
- **POS.0840** Material has an index. Every `sources/` and
  `research/` directory carries a `00-INDEX.md`: a light catalogue so
  that Claude — and the principal — know what material exists and what
  it is for without re-reading the files. It is a working aid, not a
  record of thinking: it tracks nothing (no processing state, no
  positions) and is an automatic input of no command. `/forge`,
  `/critique` and the challengers do not confront the chain with the
  material on their own; a contradiction between the intent and a
  source is not a finding, because the source may be a
  counter-example, a mere inspiration or a record of what someone else
  said. Claude reaches for a file by its own judgement or when the
  principal asks ("check the assessment against the requirements in
  file X"). Each entry has fixed fields in free text — for sources
  *What / Origin / Role / Use for*, for research *Question / Answer in
  short / Consult when*; Role is free text with recurring examples (a
  standard to verify against, inspiration, a counter-example, a
  meeting record), never a fixed vocabulary. The ledger holds
  registration only — a Sources table and a Research table, no content
  columns — so that nothing is described in two places. A bundle keeps
  its own `00-INDEX.md` inside and appears in the top index as one
  entry pointing into it: two levels, never deeper, and the top index
  never repeats the bundle's contents. The index is freely rewritten
  like the ledger while the files under it stay immutable. `/ingest`
  and `/research` write the entry when they place the file (the bare
  `/ingest` sweep fills gaps), `/new-project` scaffolds both indexes
  from `templates/index.md`, and `/check` verifies index against
  directory — a file without an entry or an entry without a file.
- **POS.0190** Artefacts are written once per iteration round, not once
  per answer — and this holds for any working conversation over the
  intent or open items (a `/forge intent` interview, a thread sweep,
  resolving findings), whatever the entry door. Answers are carried in
  the conversation and reflected back; at the round's natural end
  Claude asks whether to write and writes on the principal's
  confirmation — one version bump and one Version History row however
  many answers the round contained. The principal may at any moment
  order a write of whatever is agreed so far. Writing after every
  exchange buries the substantive change under changelog churn and
  makes the Version History unreadable.
- **POS.0710** A project may spawn renders: audience-specific outputs
  generated from the chain — a pitch for the group, an architecture
  picture, an executive summary, the repository README. A render is
  never edited by hand; the iterated thing is its **recipe**
  (`recipes/<recipe>.md`): inputs (one artefact or several), audience,
  instructions and the literal output template in one file, versioned
  by the house scheme and composed conversationally with the
  principal. `/render <recipe>` regenerates the output mechanically
  into `renders/<recipe>.md` — or the recipe's optional `output:`
  path — undated, overwritten freely, history in git. Every render
  opens with YAML front-matter provenance citing the recipe and every
  input with their versions; the ledger's Renders table mirrors it. A
  render assigns nothing and is not part of the chain: the artefacts
  remain the sole source of truth. The boundary between the two is
  authorship, not audience: a chain artefact is composed by the
  principal (Claude proposes, the principal composes), a render is
  generated from artefacts — an article the principal writes is a
  layer of the chain, its translation is a render. Visible YAML provenance was chosen
  over an invisible comment deliberately: provenance is control
  information, the audience rarely meets raw Markdown, and GitLab does
  not display front-matter. Dated hand-made editions of the earlier
  derivative convention remain in place as legacy history. Recipes are
  tools, not records of thinking: they carry a bare version and an
  updated date in front-matter — enough for a render to cite — with no
  status field and no Version History table; why a recipe changed
  lives in git, and the substantive turns live in the intent. The full
  versioning apparatus belongs to documents that are approved and
  handed over. Recipes are deliberately loose: the template fixes the
  structure and what information appears where, never the wording — a
  presentation recipe says what belongs on a slide, not its phrasing
  or its placement on a picture. Each rendering re-derives the words
  from the current inputs; fixing the text in the template would turn
  the recipe into the render and make the inputs meaningless. A
  render may also serve as an input of another render — a deck slide
  citing an architecture picture as `render: <file>` — provided the
  citing recipe declares it among its Inputs, so provenance and
  staleness track the dependency.
- **POS.0720** README.md is a render of the forge project — until now
  the only document produced by no governed process. Its recipe lives
  at `projects/forge/recipes/readme.md` with `output:` pointing at the
  repository root; the natural inputs are this intent and CLAUDE.md.
  README.md is never edited by hand: content fixes go into the recipe
  or the inputs, and the file is regenerated. The former rule "update
  README in the same step as a process change" becomes: a process
  change is complete only once the intent is updated and the README
  re-rendered.
- **POS.0730** Release notes stay continuously current. `RELEASE-NOTES.md`
  in the repository root is a render (`/render release-notes`, recipe
  `recipes/release-notes.md`): an Unreleased section on top
  summarising the changes since the last approved major, then one
  section per approved major version, newest first, synthesising what
  each era meant — the fine-grained log stays in this document's
  Version History. The Unreleased head is regenerated by every `/save`
  that touches the core or `projects/forge/`, alongside the README,
  and is recast as the new major's section at approval; sections of
  already-released majors are carried over verbatim from the previous
  edition, so published notes never change retroactively.
- **POS.0810** Regenerated renders pass under the principal's eyes.
  Regeneration is stochastic: the same inputs never guarantee the
  same words, so an unreviewed regeneration is an unreviewed edit of
  an outward-facing document. Two light defences, neither of them a
  gate (POS.0430): a recipe pins load-bearing wording as fixed
  text — what is pinned regenerates verbatim (a title, a claim, a
  fixed line) while everything else re-derives freely — and a
  `/save` that regenerated renders reports in its pre-save summary
  what materially changed in them, so the principal rules on the
  delta before the commit without reading a full diff. A render is
  regenerated only by `/save` or by the principal's explicit
  `/render`; Claude never regenerates on its own judgement — it
  reports staleness and offers (principal's direction 2026-08-30,
  after Claude re-ran renders unasked).
- **POS.0960** A project has a kind, `kind: thought | library`, declared
  in the YAML header of its ledger, default `thought` — today's projects
  unchanged. The rules of a kind live in the engine; the project carries
  only the data marker, and its optional `CLAUDE.md` stays polish, never
  kind rules (that would copy the engine into the project).
  `/new-project` scaffolds by kind, the `/forge` map reads a library as
  material rather than as a project waiting for a brief, `/check`
  requires no chain of a library and reports a project that is not a
  repository — with the one-line way to initialise it — as a fact, never
  as a defect (POS.0940). "Chain" was considered as a kind name and
  dropped: nothing could be pictured under it.
- **POS.0970** A library is a project of kind `library`: no chain: a
  ledger, `sources/` and `research/` with their indexes,
  `recipes/readme.md` and the README it renders (POS.1000) — a
  collection of documents used across projects, prefix `lib-`, its own
  repository and therefore its own visibility. Nothing is redefined:
  `/ingest` by file or link, or an upload and a sweep, registration and
  index as everywhere. Two kinds of material exist: a thought project's
  sources are inputs as of a date and immutable; a library's documents
  are maintained by an owner who is also their author — overwrite, or a
  new version beside, is the owner's choice (a deck template's previous
  version is irrelevant; a requirement-writing convention may usefully
  say "supports v1 and v2"). Another project cites a library document by
  path. The citation is a cross-repository dependency taken knowingly:
  only someone with both repositories can read it, the assignment is
  self-contained anyway, the version in the citation is a visible,
  unguarded pin, and a check is added when it hurts. The library is not
  a condition of publication: the intention is decided, the
  implementation comes with the first library.
### Structure and style of an assignment
- **POS.0200** Structured items with stable IDs beat prose, even at very
  high abstraction. Narrative is confined to Purpose & Context and
  Objective.
- **POS.0210** An assignment assigns; it does not solve. What keeps a
  document an assignment is the kind of content, never its amount.
  The formerly enumerated ban — stakeholder matrices, RACI, impact
  analyses, MECE decompositions, tables of contents — originated in
  one early case and is not a universal rule: any such apparatus may
  appear where the principal judges it part of setting direction; it
  is the recipients' machinery only when it belongs to executing
  delivery. (THR.0120 closed by this decision, 2026-08-17.)
- **POS.0220** IDs use the format `PREFIX.NNNN` with three-letter
  prefixes, numbered in tens, each new group starting at the next
  hundred. IDs are global and stable, never renumbered; items may move
  between groups freely. Groups are plain headings with no IDs, no
  metadata and no lifecycle; depth is capped at two levels.
- **POS.0230** Prefix vocabulary, aligned with the group BRD standard
  where an equivalent exists: REQ, OOS, CON, ASM, DEL, TBC, SCR in the
  assignment; POS, THR, REJ in the intent; FND, CHL, DEC internally. No
  universal standard for prefixes exists; this is a house convention
  derived from the group's own.
- **POS.0240** Every assignment carries a Terms section listing the
  prefixes and any domain terms it actually uses, so it can be forwarded
  without oral tradition. Defined Terms are capitalised in item text.
- **POS.0250** Requirements are written as shall / shall not, in full
  correct UK English sentences, one idea per item, each written once.
  Would, could, should, might, may and MoSCoW wording are not used.
- **POS.0260** No priorities and no priority column. Everything in an
  assignment is essential; an exception carries a note reading
  *optional*.
- **POS.0270** Testability is recommended, never required. Assignments
  are deliberately high-level; delegating concretisation through a DEL
  item is a legitimate outcome, and the critic reports untestable wording
  as a recommendation, not a finding.
- **POS.0280** Success criteria are wanted but not compulsory. Delegating
  them to the recipients as a deliverable ("define success criteria and
  return") is a legitimate outcome, not a defect.
- **POS.0290** An item must not depend on an external link to be
  understood, agreed or later tested. Negative mandates (out of scope,
  do-not) rank equally with positive ones. FR / NFR markers may appear in
  item text where they help; they are never part of the ID.

### Versioning and state
- **POS.0300** Versioning follows the group BRD convention: integers
  denote signed-off versions. Drafts run 0.1, 0.2 …; 1.0 is approved;
  1.1, 1.2 … are changes made after approval, not yet approved
  themselves; 2.0 is the next approved version. Status in front-matter
  (`draft | in_review | approved | superseded`) must agree with the
  number.
- **POS.0310** Every versioned document opens with a Version History
  table (Version | Modification | Author | Date), human-readable, stating
  what changed and why.
- **POS.0320** Immutable artefacts (a locked brief, reviews, challenges,
  research) are never edited — a brief from its lock, the others from
  creation; corrections happen downstream.
- **POS.0330** State lives in files, never only in conversation. A
  session can be ended at any point without loss; `/ledger` re-orients
  from the ledger. One project per session is the hygienic default.
- **POS.0820** Artefacts do not expire with the conventions.
  Conventions evolve continuously and `/check` measures against the
  current ones — but an artefact remains valid under the conventions
  it was written to: nonconformance of a finished or dormant project
  is a fact to report, never a defect to chase. Bringing a project
  to newer conventions is an explicit migration decision of the
  principal, made per project and never assumed.

### Review
- **POS.0400** Two isolated kinds of review of one shape: the critic
  (document quality, findings FND) and the challenger (substance of the
  thinking, challenges CHL). Both run as isolated subagents on the
  session model that never see the working conversation — that blindness
  is the source of their value; both are invoked by hand by the
  principal, `/critique <lens>` and `/challenge <persona>`; both produce
  an immutable dated report and ledger rows; both are settled by
  walkthrough (POS.0850). The challenger has personas, the critic has
  lenses: one agent file each, the shared behaviour carried verbatim
  from one skeleton (`templates/challenger.md`, `templates/critic.md`),
  only the Lens section its own; `/check-forge` verifies every file
  against its skeleton. Both take an optional target, an artefact named
  as `/forge` names it (`brief`, `brief-<name>`, `intent`, `assignment`,
  later layers as they come); without one, the whole chain — the
  principal's request of 2026-09-03, so that one file or one transition
  can be reviewed alone. Which of them run at a save or a release is not
  decided here (THR.0220).
- **POS.0410** The critic has two lenses, created 2026-09-03 after a
  user's report that the single critic hunted formalities and never
  guarded the chain — its mandate had named one link (intent ↔
  assignment) in one word while the brief, though read, had no task, and
  formal checks filled four paragraphs of its prompt. `clarity` reads
  each artefact on its own: ambiguity, internal contradiction,
  duplication, scope hygiene, Requirement style, the advisory checklist.
  `essence` reads the chain: for every adjacent pair (brief → intent,
  intent → assignment, every later layer) it first distils, blind, the
  essence of the downstream artefact in a few sentences, then the
  upstream's the same way, and compares — substance lost without a trace
  (REJ, DEC, DEL, TBC, the ledger's mining state), substance added
  without provenance, meaning shifted, provenance that does not hold; a
  finding is a difference of essences, not of texts, and the report
  carries both distillations. A target narrows `clarity` to that
  artefact and `essence` to that artefact against its parent — a
  transition is addressed by its downstream artefact, since every layer
  has exactly one parent, so no arrow is ever typed. Regression against
  resolved findings is every lens's first step over its own reports, the
  retired single critic's reports divided between them by category; FND
  IDs stay one global sequence; each run produces a delta report (new /
  verified resolved / still open / newly obsolete). Untestable wording
  and missing delivery-stage apparatus are findings of no lens.
- **POS.0420** `/challenge <persona> [artefact]` reviews the thinking
  through a chosen persona — one isolated agent per persona
  (`challenger-<persona>`), each defined by the blind spots it exists to
  find. The target may be any artefact of the chain, the whole chain
  when none is named — each challenge then names the artefact it
  concerns: the challenger reads the whole chain for context and
  challenges the substance of the target. The shared skeleton is
  invariant whatever the persona: no stake in the principal being right;
  unstated assumptions, whether the stated objective is the real
  problem, second-order effects, organisational reality, failure modes,
  missing dimensions, the serious counter-case; three to seven sharp
  challenges, each with a severity (dealbreaker | major | minor, ordered
  by it — a fatal flaw is never buried among cosmetics), a falsifiable
  "what would change my mind" and an epistemic status (consensus |
  active debate | emerging practice | my judgement); no fabrication — a
  precise "I don't know" beats an invented figure, and anything
  reconstructed from memory is flagged. The shared skeleton has one
  owner, `templates/challenger.md`: every persona file carries its fixed
  sections (Subject, How to work, Output) verbatim and writes only its
  own Lens — who it is to the principal and which blind spots it exists
  to find — and `/check-forge` verifies each persona against the
  template (POS.1070). The first persona is `cto` (peer-CTO register);
  further personas — a strategist, a business analyst — are created from
  the template by the principal's decision when first needed, and only
  where their blind spots genuinely differ: personas that would say the
  same things in different words are noise. Bare `/challenge` lists the
  roster and recommends a fit for the project's subject. Challenge files
  carry the persona in their name (`YYYY-MM-DD-challenge-<persona>.md`);
  the CHL sequence stays global per project.
- **POS.0430** Nothing blocks. There are no hard quality gates;
  checklists and findings are advisory and the principal alone decides
  what is published.
- **POS.0440** Every finding and challenge is either fixed or explicitly
  overruled with a recorded reason (DEC). Overruling and parking are
  legitimate outcomes; silently ignoring is not. An accepted challenge
  must change the intent, otherwise it was not accepted.
- **POS.0450** An artefact is best challenged before the next layer is
  first derived from it — the intent before the first assignment, one
  day a BRD before the solution design — while accepted challenges are
  still cheap to absorb. Whether it runs again later — after a draft,
  before approval — is left to the judgement of whoever is running the
  process; no rule prescribes it. (THR.0040 → DEC.0020, generalised
  from "before the first draft" when the challenger was opened to any
  artefact; the reasoning of the decision is unchanged.)
- **POS.0790** Isolation is not independence. The author, the critic
  and the challengers share one model family; what that family
  systematically cannot see, none of them will find, and agreement
  between the reviewers is therefore never treated as validation —
  it only means the artefact is consistent under one set of priors.
  The calibration point lies outside: review by humans or by a
  different model family, invited at the principal's discretion —
  independent different-family challengers are planned (POS.0800).
  External human review of the forge by experienced practitioners
  has already taken place and shaped it through the ordinary door,
  like any other input. A challenge may inspire, but supplied
  content follows POS.0070 — nothing enters the intent because a
  reviewer wrote it, only because the principal composed it — and an
  accepted challenge may change the intent by subtraction as readily
  as by addition (POS.0440 read accordingly).
- **POS.0800** Independent challengers will be built: challenger
  personas running on a different model family than the author's,
  composed by the principal in Microsoft AI Foundry and invoked from
  the forge over a CLI link, so that `/challenge` can send in a lens
  with genuinely different priors. The direction is decided; the
  mechanics are designed when taken up.

### Operating environment
- **POS.0500** The engine is one git repository, `forge-of-thought`
  (POS.0990), full name **Forge of Thought** in documents: the universal
  core in the root (`CLAUDE.md` for the agent, `README.md` for humans,
  `templates/`, `scripts/`, `.claude/`) together with `projects/forge`,
  the system's own project. User projects live under `projects/<slug>/`
  as git repositories of their own, ignored by the engine (POS.0940); a
  per-project `CLAUDE.md` is polish only where genuinely needed.
- **POS.0510** Commands are entry points into phases, not the only
  permitted door; the core rules apply in ordinary conversation too.
- **POS.0520** Protection relies on Claude Code's permission system,
  not an OS-level sandbox: commands and file operations run under
  permission prompts and allowlists, shared deny rules in
  `.claude/settings.json` block sensitive paths (`~/.ssh`, `~/.aws`),
  and web access is approved per domain on first use. OS-level
  sandboxing was tried on 2026-08-04 and deliberately dropped: it is
  unavailable on Windows, where enforcing it meant no shell at all.
- **POS.0530** This work is reasoning-heavy and token-light, so the
  strongest available model tier is the default — the session model,
  chosen once, with no per-agent pins (POS.0930).
- **POS.0540** Mechanical conformance has its own guard, distinct from
  the two reviewers: `/check-forge` cross-checks the core and
  `projects/forge/` for consistency with each other, and `/check`
  verifies a project against the current conventions — every project
  except forge when run without an argument. Both are read-only and
  advisory: they report and propose, the principal decides what is
  fixed. They check conformance, never substance or document quality —
  that remains the reviewers' territory.
- **POS.0550** The engine is persisted in git with a remote of its own,
  linear history on `main`, no branches; every user project is likewise
  a repository with whatever remote and visibility its owner gives it.
  Four PowerShell scripts are the only door to git — reading state
  included, no exceptions. Three of them serve the engine and every project
  that is a repository (`projects/<slug>/.git`): `forge-save.ps1`
  (stage–commit–push; bare, the engine and every project with changes,
  each its own commit; with a slug, that repository — `forge` meaning
  the engine; auto-generated commit message unless given; remote changes
  reconciled by rebase; without an origin, commit and a note; never `git
  add -f`, never `git clean`), `forge-pull.ps1` (fast-forward only,
  refuses over unsaved work; bare, the engine — which is the upgrade —
  and every project with a remote; with a slug, one), and
  `forge-status.ps1` (engine and every project: unsaved changes, last
  commit, origin or "not under git"; changes nothing). The fourth,
  `forge-clone.ps1`, brings an existing project in (POS.1060): it
  clones a repository into `projects/<repository name>`, never
  overwriting, and sets that repository's local commit identity only
  when given `-Name` and `-Email`. No remote is
  configured anywhere in the forge: git carries that information itself.
  Immutability of artefacts remains a process rule enforced by
  convention, not by git.
- **POS.0570** A save invoked through Claude is preceded by the
  relevant conformance check — `/check-forge` when core files are
  touched, `/check <slug>` for a project's changes — and its findings
  are settled before the commit: fixed, or explicitly accepted by the
  principal. This is the recommended procedure, never a gate: nothing
  blocks (POS.0430), and saves made directly from the shell are
  unaffected. The procedure is mechanised by the `/save` command,
  which routes the check by scope — `/check-forge` for core changes,
  `/check <slug>` per touched project — settles findings with the
  principal, proposes a commit message for the principal's
  confirmation, and only then runs the script; deferred findings are
  recorded in the ledger under "Waiting on principal". When a save
  touches the core or `projects/forge/`, `/save` re-renders
  `README.md` and the Unreleased head of `RELEASE-NOTES.md` from
  their recipes before the conformance check — unconditionally, with
  no staleness test — and reports the steps.
  Other renders remain ordinary check findings for the principal to
  settle or defer.
- **POS.0580** Work on the chain is invoked by target state, never by
  verb: `/forge <state>` (`/forge intent`, `/forge assignment`) —
  knowing the name of the target artefact is knowing the command, with
  nothing to memorise as layers are added. Bare `/forge` reports the
  map: which artefacts exist at what versions, which states can be
  worked from here, which renders are stale, and a recommended next
  step. Mechanics: a thin dispatcher (`.claude/commands/forge.md`)
  plus one definition file per state
  (`.claude/commands/forge/<state>.md`), each declaring its own
  inputs — so the chain is a star, not a fixed line: a future layer
  branches from any artefact by adding one file, the dispatcher
  untouched. `/clarify` and `/draft` were retired without aliases on
  2026-08-15.
- **POS.0590** Everything the forge produces is Markdown, renders
  included: a presentation is a `.md` saying what is on each slide
  (mermaid for pictures). The forge still ends at content, but it
  carries one delivery-format tool at its edge: `scripts/md2pptx.ps1`
  (POS.0740) turns a Markdown deck render into a `.pptx`. The
  Markdown render remains the sole source of truth; the `.pptx` is a
  generated output of second order — regenerated at will, never
  edited by hand. All other format conversion stays outside the
  forge, as git is for persistence.
- **POS.0740** `scripts/md2pptx.ps1` generates a PowerPoint file from
  a Markdown deck definition through headless Claude Code
  (`claude -p`) with Anthropic's official pptx skill (plugin
  `document-skills` from the `anthropics/skills` marketplace,
  installed separately per user, as markitdown is for `doc2md`). The
  conversion is done by a model, never by a deterministic converter,
  because deck definitions are deliberately free-form and may
  themselves contain instructions for the LLM — slide content,
  speaker notes, diagrams to redraw as native shapes, visual
  directions. Template handling: `-Template <path>` names a `.potx`
  file by path — typically a document of a library project
  (POS.0970), e.g. `projects/lib-<name>/sources/<name>.potx`; without
  the parameter Claude designs the visual style itself. There is no
  default template and no bare-name lookup. The output defaults to the input's directory
  and basename with a `.pptx` extension, so a deck generated from
  `renders/<recipe>.md` lands as `renders/<recipe>.pptx`, tracked in
  git like any render output; `-Out` overrides. The headless run's
  model is chosen by `-Model`, default opus; a presentation recipe
  may recommend one in its Build instructions.
- **POS.0770** Recipe composition may be guided by genre:
  `/recipe <genre>` mirrors the `/forge` star (POS.0580) — a thin
  dispatcher (`.claude/commands/recipe.md`) plus one definition file
  per genre (`.claude/commands/recipe/<genre>.md`) carrying the
  elicitation checklist, with the genre's canonical skeleton in
  `templates/recipe-<genre>.md` extending the base recipe shape,
  never replacing it. Bare `/recipe` lists the roster; a recipe
  outside any genre stays legitimate, composed conversationally from
  `templates/recipe.md`; naming an existing recipe iterates it
  through the same lens. The first genre is `presentation` — a
  slide-by-slide deck definition whose render `md2pptx.ps1` turns
  into a PowerPoint file — distilled from the first deck recipe;
  its interview covers audience and register, the one
  message, inputs (including renders as picture sources), dramaturgy,
  speaker notes and traceability citations, on-slide density, diagram
  policy, language, vocabulary discipline, confidentiality, and the
  Build instructions copied verbatim into the render for the
  deck-builder LLM. The genre is named "presentation" rather than
  "deck" for company-wide legibility at rollout.
- **POS.0830** The forge runs beyond Windows. `scripts/` is the only
  platform-bound layer, and its scripts are written to run unchanged
  on Linux and macOS: they are PowerShell 7, which is itself
  cross-platform (`pwsh`, one install on a non-Windows machine), and
  they use nothing Windows-only — paths composed with `Join-Path` or
  forward slashes, no `cmd`, registry or Windows-only cmdlets,
  `$IsWindows` only where the platform genuinely differs, external
  tools (`git`, `markitdown`, `claude`) resolved from PATH, and usage
  examples in the scripts' help free of Windows-specific paths and
  invocations. Instance facts are out of the scripts: no remote URL,
  no author identity, no first-run initialisation — git configuration
  is the user's (POS.0950). Portability is verified by running the set on Linux
  (WSL suffices); until then it is a writing rule, not a claim.
- **POS.0940** Mechanism of the engine/projects split. The engine is a
  clone; the projects are nested git repositories in a gitignored
  `projects/*` with `projects/forge` re-included (`!projects/forge`; the
  pattern must be `projects/*`, not `projects/`, or the re-include fails
  silently). The engine does not know the projects: the scripts
  recognise a project by the presence of `projects/<slug>/.git` —
  without it, status reports "not under git" and save and pull skip it;
  with it, they commit and push to its origin. `git init` and the remote
  are the user's one-off act: `/new-project` and `/spinoff` create files
  only and never touch git, and a project starting "not under git" is a
  property, not a defect. A project without a repository, or with a
  repository and no origin, is a legitimate shape — a sensitive project
  kept local; the second keeps the history the renders and recipes rely
  on, the first does not. Upgrade is `forge-pull` on the engine — a
  fast-forward of `main`; the engine receives a git tag at every
  approved major of this intent. A project records no engine version:
  `/check` measures it against the current conventions, and
  inconsistencies are fixed by the user with AI, as now. Verified by
  test on 2026-08-29 (research
  `2026-08-29-git-engine-projects-separation.md`); meets all six
  conditions of the brief with no mechanism at all. Shapes rejected:
  REJ.0150. Closes THR.0130 (opened 2.8, 2026-08-17).
- **POS.0950** The engine carries no instance facts. Who the principal
  is and what language the conversation runs in live in
  `CLAUDE.local.md` at the engine root — gitignored, created from
  `templates/CLAUDE.local.md` and filled by `/setup` on a new machine
  (POS.1050); the root is where Claude Code looks for it. The session
  model lives in `.claude/settings.local.json` (POS.0930). The commit
  identity is set locally per repository; the engine carries none
  (below). `CLAUDE.md` names the principal and the conversation language
  only as things that exist, never by value; the artefact language stays
  English (THR.0180). The scripts carry no URL and no identity
  (POS.0830). Resolves the scripts part of THR.0090; the thread is
  otherwise untouched. The commit identity is a property of the project,
  not of the host: it is set locally in every repository (`git config
  user.name` / `user.email`) at the repository's creation or import,
  proposed by the command layer from the identity roster in
  `CLAUDE.local.md` — matched by the origin's host, which is an offer,
  never a rule — and set on the principal's word. The per-host
  `includeIf` configuration adopted at 3.6 is dropped: the host is only
  a correlate of the identity and fails exactly where one host serves
  two roles (a personal and a company organisation on the same
  github.com), and writing `~/.gitconfig-<host>` files reached beyond
  the engine's boundary. The one global guard, offered by `/setup`
  (POS.1050), is `user.useConfigOnly = true` with no global
  `user.name`/`user.email`: a commit in a repository with no local
  identity then fails aloud instead of silently taking a default (a
  surviving global identity defeats the guard, and `/setup` says so). A
  user's own configuration — per-host includes included — remains his
  business and a legitimate way to resolve an identity. `forge-save`
  checks that git resolves an identity for the repository and, where it
  resolves none, reports it with the command to set one and commits
  nothing until it is. The identity follows the project, and the command
  layer manages it.
- **POS.0930** One model for the whole forge. Every command, chain
  state and reviewer runs on the session model; the reviewer agents
  declare `model: inherit` explicitly, so that the strongest model
  the forge runs on is a decision and never an accident of a pin
  that has aged (the `opus` pin on the challenger had done exactly
  that). Speed is bought with context, not with weaker models:
  `/render` generates in an isolated subagent that sees only the
  recipe and its inputs, never the working conversation — the same
  principle as the reviewers', applied to a mechanical job — and a
  command's `effort:` remains the lever for routine turns should one
  ever need it. Per-command pinning to a faster model is rejected
  for now: the routine commands are a small share of the work and
  slow for the size of the context they carry, not for the model,
  and every pin is a convention to keep. A per-recipe `model:` is
  deferred: tested on 2026-08-27 (README from recipe 0.19 rendered
  in isolation by three models), a smaller model loosened pinned
  wording, dropped prescribed elements and leaned on the previous
  render instead of the recipe — the drift POS.0810 guards against —
  so the choice waits for a recipe that is genuinely mechanical.
  The session model is chosen in one deliberate place,
  `.claude/settings.local.json` — an instance preference, gitignored
  (POS.0950).
  The one exception is `scripts/md2pptx.ps1`: a headless run has no
  session model, so the script needs a default of its own
  (`-Model`, POS.0740) — an explicit parameter, not an aged pin.
  The same lever carries the conformance checks: `/check` and
  `/check-forge` execute their own definition in an isolated subagent
  that sees only the files, returning the report for the walkthrough
  in the session, and `/save` launches a repository's README and
  release-notes renders in parallel; the working conversation is
  spent on verdicts, not on reading (2026-09-02, at the principal's
  prompt — a save had grown to five minutes).
  Closes THR.0160 (opened 2.10, 2026-08-25).
- **POS.1070** One mechanism lives in one place and is used from
  there. Whatever the forge already has a procedure for — a command,
  a skill, a script, an agent — is invoked through that procedure
  whenever its situation arises, never re-described ad hoc: `/save`
  regenerates renders through `/render`, git is touched through the
  four scripts (POS.0550), reviews run through the reviewer agents.
  A command that needs another's mechanism references it by path
  and adds nothing of its own to how it runs; the rules of a
  mechanism — isolation, wrapping, provenance, what may be read —
  are written once, in its own definition. Restating a procedure in
  a second place is a defect: the two copies drift, and the copy
  without a rule silently loses it (on 2026-09-02 the README,
  rendered at `/save` by an ad-hoc subagent prompt instead of
  `/render`, arrived unwrapped and with a foreign provenance shape).
  `/check-forge` carries the standing rule — a restated procedure, a
  persona file diverging from `templates/challenger.md`, a direct
  operation where a script, command or agent exists — over the
  operating-layer files changed in the save's scope, the full sweep
  only on an explicit bare `/check-forge`, so that the rule costs a
  save seconds, not minutes. Where a shape had no owner at all, it
  gets a skeleton rather than a second description: the bundle
  catalogue (`templates/index-bundle.md`), the library reduction of
  the ledger (`templates/ledger.md`'s header). Raised by the principal
  on 2026-09-02; the first sweep of the operating layer the same day
  found fourteen restatements, every one with a rule missing on one
  side.

### Naming
- **POS.0600** The system is named **Forge of Thought**: thoughts are
  the raw material — of whatever kind, nothing is presumed about them —
  and forged assignments are the product. Chosen with the full-chain
  vision in mind (assignment → BRD → architecture → full realisation
  deck); "Assignment Studio" was dropped because it named only the first
  segment and only the first audience. Repository `forge-of-thought`
  (POS.0990), slug `forge` for the system's own project under
  `projects/`, full name in documents; the short form "Forge" is
  expected in daily speech.
- **POS.0610** Project slugs are lowercase and hyphenated on disk;
  display names may differ. Programme naming is used where a family of
  initiatives is expected: FLOW (Future Lean Operating Way), first
  instance FLOW:BA → slug `flow-ba`. Names must be legible to the
  audience, not only to the principal.
- **POS.0620** The README subtitle is "*A workshop where thought is
  tempered and shaped.*" Any subtitle or one-line description must
  present the forge as a place and space where thoughts are forged; it
  must not name the assignment as the goal, because the assignment is
  only where version 1 of the chain happens to end. "Forging thoughts
  into assignments" was dropped for exactly that reason; "A forge for
  thought" was dropped as a tautology of the name.

### Growth path
- **POS.0700** The principal intends to keep extending the engine
  downward: thoughts are forged as far as he needs them taken. The BRD
  layer is certain to come; solution architecture and integration are
  intended; a strategy layer is possible if it proves to make sense.
  Which layers are added, and in what order, is open — possibly all of
  these, possibly none yet. Nothing is approved for construction: the
  mechanics of a layer (commands, agents, reviewer calibration) are
  designed when that layer is actually taken up, not in advance. An
  earlier `/elaborate` mechanics proposal was withdrawn as premature.
- **POS.0760** The forge is split into a public engine and user projects
  in repositories of their own. The engine — the core together with
  `projects/forge` — is public and contains nothing sensitive and no
  instance facts (POS.0950, POS.0980); users keep their projects
  wherever they choose and are themselves responsible for what those
  contain and where they live, generated decks carrying corporate
  branding included. Decided on 2026-08-29 from
  `00-brief-public-engine.md`; the mechanism is POS.0940.
- **POS.0780** The forge is a general tool for forging thoughts, and
  a forge run ends where its owner is satisfied: the outcome is an
  artefact the principal stands behind — nothing further. An intent
  may be immaterial and carry no delivery at all; the chain's
  mechanics are domain-agnostic — the same machinery that forges a
  platform assignment would forge a D&D campaign: an intent of the
  story, then materials rendered for the DM. Sponsorship, funding,
  adoption and delivery outcomes are outside the forge's scope and
  outside its sight. The door stays open, not closed: the forge may
  one day feed a delivery chain, and experience from use flows back
  through the ordinary door — the principal, via `/forge intent`
  (POS.0170) — as input like any other; whether a delivery side
  would be grown layers of the forge or a separate framework is
  deliberately undecided (THR.0140). The forge itself is developed
  at the principal's discretion and pace, by his needs and by the
  feedback its company rollout returns: direction may be named
  (POS.0700), destinations and deadlines are not.
- **POS.0980** Publication. The engine is the principal's to publish: it
  was built outside any work assignment and lived on the company's git
  only because it carried work information not yet separated. The
  audience, in order: rollout in the company first, at the same time a
  public project around which a community may form, and a showcase of
  the principal's work; the split also lets access be granted per
  project, where before a collaborator had to be on everything. The
  boundary for the public `projects/forge`: nothing company-specific by
  name — no company name, no URLs, no e-mail addresses, no content of
  the company projects. Before publication the forge project is gone
  through and rewritten within that boundary **including its immutable
  artefacts** (the brief, the challenges, the research notes, the intent
  history) — immutability knowingly broken, once; the brief was
  rewritten into English before its lock for the same reason, a one-time
  yield of POS.0060. The public repository starts with a fresh history
  (DEC.0080); the full record stays where it is today, on the company
  host, archived read-only. Until a public exemplar exists (THR.0200) the README carries no
  example project. Separating the company projects from the engine
  without publishing would have been a fallback only if publication
  were long and complicated; it is not.
  Executed 2026-08-30: the forge project was rewritten within the
  boundary — the company name, host, e-mail address, template file name
  and one personal project removed from the locked brief and the two CTO
  challenges, two sentences quoting a company project's substance
  neutralised — immutability of those three artefacts knowingly broken
  once, recorded in the ledger and nowhere in the files. The slugs of
  the company projects stay: that projects of those names exist and
  travelled the chain is a process fact, not content (THR.0210 draws the
  line). A forbidden-term list was considered and dropped as pointless —
  a grep catches names, not content. The fresh history is one commit;
  the company monorepo is archived read-only with a notice naming the
  new homes and the tag `pre-split` as its last complete state.
- **POS.0990** The public face. The engine lives at a public repository
  of the principal's, named `forge-of-thought` — the bare word "forge"
  is overloaded on every code host and says nothing in a search — under
  the licence **CC BY 4.0**: anyone may use and adapt the engine, and
  must credit the author and link to the repository. The README
  therefore names one person, the licence holder — the author with a
  contact address — as a fixed text of the readme recipe, and this is
  not an instance fact: it is who the work is by, whoever runs an
  instance. The `LICENSE` file carries the licence's verbatim legal
  code. Decided and executed 2026-08-30, with the first public commit.
- **POS.1000** Every project has a README and, if it is a thought
  project, release notes — both renders of the project's own recipes
  (`recipes/readme.md`, `recipes/release-notes.md`, `output:` in the
  project root), exactly as the engine has them (POS.0720, POS.0730;
  POS.0810 for the review of the regenerated output): the recipe is what
  is iterated, the render is never edited by hand, and every save that
  touches the project regenerates both before the check. A library has a
  README only — a catalogue of what it holds and how to use it, from its
  ledger and indexes — since release notes are distilled from an
  intent's Version History and decisions, which a library does not have;
  its history is git. The two recipes are genres of `/recipe` (skeletons
  `templates/recipe-readme.md`, `templates/recipe-release-notes.md`),
  scaffolded by `/new-project` and expected by `/check`; the ledger's
  Renders table carries them like any render. Every README closes with
  one fixed sentence, part of the readme genre: reading the repository
  needs nothing beyond a Markdown viewer, maintaining and evolving it
  needs Forge of Thought — the engine, linked
  (github.com/pche-broken-artist/forge-of-thought) — so that whoever
  finds the project knows what runs it (principal's decision
  2026-08-30). The engine's own README is the one exception: the
  sentence exists to point a visitor to the engine, and the engine's
  README is that destination (3.6).
- **POS.1010** A project may carry an icon: `logo.png` in the project
  root, supplied by the principal, picked up as the repository avatar by
  hosts that do so. Optional — a project without an icon is complete;
  `/check` does not report its absence. No `assets/` directory exists;
  one is introduced only when images beyond the logo appear.
- **POS.1020** A project registers what it relies on outside its own
  repository. The ledger carries a Dependencies table — path, library,
  used by, note — with one row per document of another repository the
  project cites: a deck template named in a recipe, a library document
  an index entry or a position refers to. Registration only, like
  sources: what the document is for lives where it is used. No version
  is recorded — a library document is maintained by its owner and cited
  as a moving target by design (POS.0970). `/check` verifies that every
  registered path exists on disk and reports a library that is not
  cloned alongside; an index entry or recipe pointing outside the
  project without a row is a finding. The `/forge` map says which
  libraries the project needs, and the project's README carries the same
  line. `/ingest` registers the row when the principal directs a project
  to a library document instead of copying it. Rationale: a
  cross-repository citation is a dependency taken knowingly (POS.0970) —
  knowingly means written down where state lives, not discovered when a
  render loses its template.

- **POS.1030** The forge's behaviour lives in the engine, never in the
  assistant's private memory. Claude Code keeps a per-directory memory
  outside the repository; whatever it learns there about how the forge
  should work — a working method, a rule of a command, a convention — is
  written into CLAUDE.md, the commands or the templates and removed from
  memory, so that every instance of the forge behaves the same and a new
  user meets the same forge as the principal. Memory is left with what
  is personal to one principal — his idiom, his private choices — and
  instance facts go to `CLAUDE.local.md` (POS.0950), which now also
  carries the git identities per host. Origin: the audit before the
  first fresh deployment, 2026-08-30, when most of the memory turned out
  to be engine rules already written or engine rules missing.
- **POS.1040** A source has one form. A file in `sources/` is either
  text or a functional binary, never both by default. At `/ingest`
  every binary file — isolated or inside a bundle — gets one question:
  convert to Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and
  that extract is the source — tracked in git, registered in the
  ledger, catalogued in the index with Origin "extract of `<original>`
  (markitdown)", immutable from registration; the original is not
  copied into the project, and where it already lies in `sources/` it
  is added to `sources/.gitignore` and stays local. No: the binary is
  the source as a functional thing — a deck template, a graphic, a
  logo — copied, registered and catalogued as is, with no extract.
  Text files get no question. Keeping both is the exception, on the
  principal's explicit word. The ledger's Sources column reads Form
  (`text | extract of <original> | binary`) instead of Extract; `/check`
  treats a binary without an extract and an extract without its
  original as the normal case. Reason: the repository carries what the
  forge works with — text — and a binary nobody reads from git is
  weight without use; a binary that is used as a thing is kept because
  it is used. Transition, the principal's decision 2026-08-30: the
  convention applies from now on; extracts made before keep their
  `.extract.md` names, and a binary already in git beside its extract
  leaves the index on his word, never automatically. Origin: the
  reference-pack index finding of the day's `/check`, where four PDFs
  sat in git beside the extracts that alone are ever cited.
- **POS.1050** First run is one command. After cloning the engine,
  `/setup` prepares the instance: it copies `templates/CLAUDE.local.md`
  to the engine root and fills it in an elicitation interview — who the
  principal is, the conversation language, the git identities per
  host — and it creates `.claude/settings.local.json` with the session
  model set to **Fable**, without asking: the strongest available model
  is the forge's default (POS.0530), the whole forge including the
  blind reviewers runs on it (POS.0930), and a newcomer's first minute
  is no place for a model decision. The command says in one sentence
  that Fable was set and that `/model` or editing the file changes it
  at any time. `/setup` never overwrites: an existing `CLAUDE.local.md`
  or `settings.local.json` is reported as it stands, not replaced.
  The git-identities interview closes with an offer: the global
  guard of POS.0950 — `user.useConfigOnly = true` appended to
  `~/.gitconfig`, read first, never overwriting existing content —
  written on the user's word; declined, printed for him to apply by
  hand. Where `~/.gitconfig` carries a global `user.name` or
  `user.email`, `/setup` says the guard only bites once that
  identity is removed and offers the removal, again only on his
  word. `/setup` runs no git operation — the user's git
  configuration file is the one thing it may edit outside the
  engine, on his word (3.7; narrowed from the per-host includes to
  the one guard line at 3.8).
  Named `/setup`, not `/init`: Claude Code's
  built-in `/init` generates a CLAUDE.md, and the collision would send
  a newcomer to exactly the wrong action at the most sensitive moment.
  Origin: a newcomer observed struggling through the manual first-run
  steps, 2026-09-01.
- **POS.1060** A project arrives through the scripts-only door.
  `/import-project <git-url>` brings an existing project into the
  forge: it calls `scripts/forge-clone.ps1` (POS.0550), which clones
  the repository into `projects/<repository name>` — no slug
  parameter: the directory falls out of the repository's name, and a
  nonconforming name is fixed by renaming the directory afterwards —
  refuses to overwrite an existing directory, and reports facts: the
  last commit, the origin, the commit identity git resolves for the
  fresh clone, and whether the project carries a ledger
  with a `kind:` header (its absence is a fact, not a defect). The
  script carries no identity (POS.0830): it accepts `-Name` and
  `-Email` and sets the repository's local commit identity only when
  given both. The command layer passes `-Name`/`-Email` by default:
  the identity is a property of the project (POS.0950), proposed
  from the identity roster in `CLAUDE.local.md` by the URL's host
  and confirmed or overridden on the principal's word. It runs the
  script bare only when the principal says his own git configuration
  resolves the identity, and the script reports which one the clone
  resolved; a clone left with no identity is caught by `forge-save`,
  which reports and commits nothing (POS.0950). Work then starts by
  selecting the project — `/forge <slug>` — because the engine does
  not track it and cannot guess it.
## Open threads

- **THR.0090** Multi-principal use. Current working assumption: a second
  principal receives Forge — including the `forge` project itself — via
  git and runs their own instance. How genuine multi-user operation
  would work is an open point for the future; deliberately not being
  worked on now.
- **THR.0140** The delivery side. Whether the forge's output one day
  feeds a delivery chain as grown layers of the forge or hands over
  to a separate delivery framework is open and deliberately not
  worked on now; it is taken up when a subject project first needs
  the linkage — flow-ba is a natural candidate.
- **THR.0150** Replacing the PowerShell scripts with POSIX `sh`.
  Considered: a single `scripts/*.sh` set (POSIX, no bashisms — macOS
  ships bash 3.2), run on Windows in Git Bash, which comes with Git
  for Windows and is required by Claude Code anyway — so no platform
  gains a dependency, unlike the `pwsh` install POS.0830 asks of
  non-Windows users; from PowerShell the call is
  `sh ./scripts/<name>.sh …`, Claude calls them directly. The
  principal is undecided whether to do it at all; no priority while
  PowerShell 7 suffices. If taken up: the set is replaced whole, never
  run side by side. Already excluded: a dual `.ps1` + `.sh` set (two
  truths drift apart) and a rewrite in Python (a dependency without
  benefit; Python stays only for markitdown).
- **THR.0170** Branch documents. Considered on 2026-08-27 alongside
  POS.0920 and deferred as too heavy for now: a working document per
  large whole (`branches/<name>.md` — a verbatim seed followed by
  positions and threads worked like the intent, states `open | merged
  | dropped`, merged into the intent with provenance or dropped to a
  REJ). To be taken up only if a brief in draft turns out to need
  structured, position-level work before it can be locked and mined;
  until then a draft brief is the branch.

- **THR.0180** The output language. POS.0060 makes English the
  language of every artefact as a rule of the forge; the principal
  stated on 2026-08-29 that it is not — it is his own rule, enforced
  by him, for the company projects of this instance, and a project
  with Czech output is conceivable. The rule therefore belongs to the
  instance or the project, not to the engine that is to become public
  (00-brief-public-engine.md). Deliberately left as is: more than one
  output language is to be solved when a project needs it — where the
  choice lives (instance default, per-project override), what stays
  English as notation (ID prefixes, `shall`, status words), how the
  reviewers and `/render` read it. The first project with Czech output
  opens it — planned as the first project after the split.
- **THR.0190** A plugin as a later distribution layer. Claude Code
  plugins would give the only real upgrade channel and project =
  repository, but a plugin carries no `CLAUDE.md`, and commands are
  discovered only up to the repository root — so it forces changes
  nobody needs yet: shortening the core to a bootstrap skill injected by
  a SessionStart hook (as Superpowers does; its repository `CLAUDE.md`
  is for contributors only), rewriting the commands from
  `projects/<slug>/` to the repository root, solving multi-project
  operations. A `CLAUDE.md` split is not a cheap step: 435 lines, and
  moving half the rules from always-on to on-demand is a behaviour
  change ("200 lines" is a recommendation, not a limit). `@import` of
  the forge `CLAUDE.md` into a user's works but carries only
  `CLAUDE.md`, not commands and agents. No preparation now; taken up
  when `forge-pull` proves an insufficient upgrade channel. Research:
  `2026-08-29-claude-code-packaging.md`,
  `2026-08-29-framework-distribution-in-the-field.md`.
- **THR.0200** The public face: an exemplar project for the README — the
  forge itself, or one created later; the company projects cannot
  travel. Until one exists the README carries a one-sentence placeholder
  (readme recipe 0.24). Repository name and licence settled in POS.0990.
- **THR.0210** A guard rail for the public boundary. The rewrite before
  publication (POS.0980) found the leak surface where the challenge
  predicted it: the forge project's own artefacts quoting the substance
  of subject projects — a sentence of a company intent in a CTO
  challenge, a deck's name in a position. A grep before a push is a net,
  not a rule. Wanted: a standing rule that `projects/forge` never
  carries the *content* of a subject project — only process facts: that
  a project exists, its versions, dates and counts — and a home for it:
  CLAUDE.md, the challenger and critic prompts (they read the subject
  projects as evidence), `/check-forge` as a sweep, or all three. Opened
  2026-08-30 at the principal's direction.
  **Parked 2026-09-03** by the principal: the risk is small while he
  knows of it, and a rule with its checks would add weight the forge
  does not need now; not closed, to be taken up when the boundary is
  next at stake (a publication of a further project, a reviewer run on
  `projects/forge` with subject projects in reach). Claude's proposed
  solution, recorded for that day: a check, not a critic lens, and
  not the check alone. Not a lens, because the critic reads the chain
  and the leak surface lies outside it — challenges, research notes,
  templates, recipes, README — and a lens runs on the principal's word
  while the boundary must hold before every push; the matter is a
  convention of the repository, which is `/check-forge`'s job at every
  `/save` that touches the engine. Not the check alone, because a check
  catches a leak after it is written, and challenges, reviews and
  research are immutable from creation and written by isolated agents
  that read subject projects as evidence — a leak there is repaired
  only by breaking immutability again. Hence two homes: a new check
  item in `/check-forge` owning the rule (the engine — core, operating
  layer, `projects/forge` with its immutable artefacts — carries no
  content of any subject project; a process fact is admissible:
  existence, slug, kind, versions, dates, states, counts, commands run;
  content is not: a position, a requirement, a quoted or paraphrased
  sentence, a deliverable's name, a person, an organisation, a host;
  verified by reading, never by a term list, POS.0980), and one
  sentence under Inputs in `templates/challenger.md` and
  `templates/critic.md` citing that item, carried into every agent.
  CLAUDE.md deliberately left out: the rule concerns one project, not
  every session, and THR.0240 argues against another sentence in the
  core. A position (POS.1080 was the number in hand) records the
  decision when it falls.
- **THR.0220** The cost of rendering README and release notes at every
  save. POS.1000 and POS.0730 regenerate both at every `/save` that
  touches a project or the engine, unconditionally; with the engine's
  README at 5,700 words and a recipe that pins wording, one render costs
  minutes and well over a hundred thousand tokens, and a save that
  changed one line of a command pays it twice. The parallel launch of
  POS.0930 halves the wait, not the cost. To think through: whether the
  unconditional regeneration is the right rule at all — regenerate only
  when an input's version moved (the stale test of `/render`), only on
  the principal's word at save time, only at an approved major, or by a
  cheaper mechanism for the release notes (the Unreleased head is a
  summary of Version History rows, close to mechanical) — and what each
  option does to POS.0810's guarantee that every regenerated render
  passes under the principal's eyes. And, since 2026-09-03, which of the
  two reviewers run where: whether `/release` (options B, C) or a save
  runs a critic lens or a challenger persona at all, and which — until
  decided every run is the principal's word (POS.0400). Opened
  2026-09-02 at the principal's direction. Three candidate solutions,
  formulated the same evening and left for a fresh head; facts first.
  The scripts already work on whatever branch is checked out
  (`forge-save` commits, rebases and pushes the current branch with its
  upstream, `forge-pull` fast-forwards it); only POS.0550's "main only"
  says otherwise. A colleague has already worked in his own forge
  instance on a branch of a subject project — sources, a walkthrough,
  intent, assignment and ledger — and merged by merge request, accepted
  by the principal without any forge ceremony because nobody else had
  touched the project; the forge stays a single-user tool per instance,
  more people means more instances and coordination by git (bearing on
  THR.0090), and a walkthrough of every merge request would not scale.
  The principal's constraint: the forge is developed by adding artefacts
  and challengers, not by wrapping git; the daily operation must stay
  understandable to a person who is not a developer. The principal has
  for weeks saved cosmetic changes directly through `forge-save.ps1` and
  reserved `/save` for changes that touch the README: the two-speed save
  of option B exists in practice and lacks only its names. **(A)
  Stale-only plus the principal's word.** One command as today. `/save`
  regenerates only a render whose recipe or input changed in that save
  (an unversioned input such as CLAUDE.md counts as changed when the
  save touches it); a fresh render is skipped without a question; the
  principal may order a save "without renders", and a skipped stale
  render leaves the trace `stale (skipped YYYY-MM-DD)` in the ledger's
  Renders table so that `/forge`, `/check` and the next save see it; at
  an approved major every render is regenerated. Saves perhaps a third
  of the engine's saves and little on projects, whose README inputs (the
  ledger) move at every operation. **(B) Save and release, branches left
  to git.** `/save` = commit and push on whatever branch is checked out,
  a light check (ledger bookkeeping, front-matter and version agreement
  — a "check-light" still to be defined), no renders; `/release` = on
  main only, refusing elsewhere: the full `/check` or `/check-forge`
  with its walkthrough, README and release notes, the release commit
  "release <intent version>" through `forge-save`, and at an approved
  major the tag through a new `forge-save -Tag` (the tag is today a
  manual git act outside the scripts). Two words a non-developer
  understands; the release number is the intent version, release notes
  stay as they are (Unreleased head plus one section per major). Whoever
  wants branches creates and switches them in git by hand (`git switch
  -c work`, one command) or through GitLab merge requests;
  `forge-status` reports the current branch. Main then carries only
  released state, so the README on main is never stale and the thread
  closes entirely. Known hole, left until it happens: two parallel
  branches taking the same next free ID — reported by `/check` at the
  release after the merge. **(C) B plus a switch.** As B, with a fixed
  working branch (`work`) per repository and one forge command (a fifth
  script) that creates it and switches between it and main, so that the
  principal never types git; `/release` merges `work` into main. More
  comfortable, and the first step towards the wrapper of git the
  principal does not want.
- **THR.0230** A common engine beneath several frameworks. Opened
  2026-09-03 at the principal's direction; a large rebuild if taken up,
  to be worked out first and decided later — the principal is not sure
  it is a good idea. The idea: whatever every framework needs alike is
  lifted out of the forge into an engine they share — git through the
  scripts, the ledger and its upkeep, versioning and Version History,
  the ID scheme, isolated agents on the session model, recipes and
  renders, sources and research with their indexes, `/save` and
  `/check`, `/setup` and the instance facts — so that a new framework is
  written as content only. Forge of Thought becomes the first framework
  on that engine, not the engine itself; the picture is several small
  cooperating frameworks on one engine, not one large one that absorbs
  everything (much could be pushed into the forge, but CLAUDE.md is
  already large — THR.0240 — and the separation helps there). Two
  further frameworks named as the concrete cases: a product framework (a
  screen described functionally per module, one artefact per module,
  HTML prototypes rendered from them) and a project-management framework
  (inputs from the forge's assignments; later meeting inputs over which
  an agent runs unattended, sorting tasks and new requirements into
  artefacts — Markdown or otherwise — or handing them on through MCP;
  verification of an implementation against its assignment; a high-level
  idea). What they show about the boundary: the chain is the framework's
  (its artefacts, their number, order and templates); "everything is
  Markdown" is a forge rule — the engine carries recipe and render, the
  framework names the output form; a dependency between frameworks is
  the Dependencies mechanism across a framework boundary; the ledger's
  tables are partly the framework's (tasks); agent types beyond the two
  (a verifier) are the framework's.
  *Agents.* Critic and challenger alike: the mechanism — isolated
  subagent, ledger record, states, walkthrough — is the engine's, the
  prompt content the framework's. Challenger personas are the
  framework's (a UX challenger, a challenger of a work plan). For the
  critic a nested point: what is generic (consistency, formal
  correctness) and what is the framework's — in the forge the drift
  brief → intent → assignment, perhaps further down.
  *How the engine reaches a framework at every session* — no decision
  now, every path recorded: one engine repository with the frameworks as
  directories in it (simplest, one `forge-pull` upgrades everything, but
  one CLAUDE.md and one command tree for all); the engine as a Claude
  Code plugin with each framework a repository of its own (the cleanest
  boundary; the finding of THR.0190 applies — a plugin carries no
  CLAUDE.md, so a bootstrap skill by SessionStart hook — the largest
  rebuild); engine and framework as two repositories joined by `@import`
  and a clone alongside (CLAUDE.md travels, commands and agents do not —
  copied or linked). THR.0190 is from now read as part of this question
  and stays a thread of its own.
  *Order of work.* The second framework must exist in outline before the
  boundary can be drawn; the engine is not built ahead of it. Where the
  engine is thought: here as a thread for now — it may become the first
  thread turned into a project of its own; the principal undecided.
  Whether THR.0220 and THR.0210 are settled on today's forge first or
  wait for the rebuild: open; Claude's recommendation is to settle both
  now as engine matters that carry over.
- **THR.0240** The size of CLAUDE.md. 523 lines on 2026-09-03 and
  growing with every iteration; THR.0190 already records that a split
  moves rules from always-on to on-demand and is a behaviour change, not
  a cut. To be dealt with sooner or later whatever becomes of THR.0230,
  which would help. Opened 2026-09-03 at the principal's direction. To
  think through: what must be always-on, what can live in commands,
  skills and templates and be read when its situation arises, and how
  the effect is measured — by behaviour, never by line count.
- **THR.0250** Two suggested functions: an expander and an essence
  manager. A tip the principal received on 2026-09-03 — where from not
  recorded. The essence manager got its detail the same day: at the end
  of the chain a blind agent, without context, distils the essence of
  the final document by itself, and that essence is checked against the
  brief to see how far the whole intent drifted. The `essence` lens of
  the critic (POS.0410) is that mechanism applied to every adjacent pair
  of the chain; whether an end-to-end distillation is a further thing or
  the same lens run brief-to-last-layer is open. The expander has a name
  only. Parked until more detail arrives.
- **THR.0260** The Version History out of the document. Measured on
  2026-09-03: the Version History table is 40 % of this intent (8,477 of
  21,265 words, 72 rows) and 11 % of a brief; every command and every
  isolated agent loads it whole, a human scrolls past it before reaching
  the substance, and the same information exists three times — the row,
  the commit message `forge-save` composes from it, and the Unreleased
  head of the release notes. Research
  `2026-09-03-version-history-placement.md`: the standards ask only for
  a revision notice at the head and allow separate volumes, records
  management names the separate file as the normal option for working
  documents, every wiki and every LLM-era spec framework keeps history
  out of the body; table-at-end saves nothing, git-only would invert the
  primary and collide with the four-scripts rule. Proposed solution, one
  rule without exceptions: every versioned chain document — brief
  included, however short its history — keeps its Version History in an
  append-only companion `<document>.history.md` beside it, and carries
  version, date, status and a machine-written `last_change` line in its
  front-matter; the row in the companion stays the single primary,
  commit message and release notes remain derivations by mechanism. The
  research's recommendation to keep the table in the head of the
  assignment and the briefs was rejected by the principal: two rules for
  one thing means nobody knows where the history is, and the forge
  project's own assignment-less chain distorts the picture — with an
  assignment present every critique would produce a corrective version
  of it too. Handover is unaffected: documents are handed over by a link
  into git, where the companion lies beside the document. Touches
  CLAUDE.md (Versioning & status, document chain), the templates (a
  `templates/history.md` skeleton), `/forge <state>` write steps,
  `forge-save.ps1`, the release-notes recipe, `/check`, and a one-off
  migration of the existing rows; best done together with THR.0220,
  which reaches into the same script and recipe. Opened 2026-09-03 at
  the principal's direction.

Note: the ID THR.0120 was inadvertently used twice — first for the
readme-recipe thread (opened 1.14, closed 1.16), then for the
assignment-apparatus boundary (opened 1.24, closed 2.4). Citations of
THR.0120 from POS.0210 and version 2.4 refer to the latter. Recorded
as-is; IDs are never renumbered.

## Rejected directions

- **REJ.0010** `clarifications.md` as an append-only Q&A log. Rejected
  because it left the current state of intent scattered across brief, log
  and assignment, with no single place answering "what do I want now".
  Replaced by `10-intent.md`.
- **REJ.0020** Workstreams as first-class entities with their own IDs and
  lifecycle. Rejected as structure for its own sake; plain heading groups
  plus stable global IDs achieve the same at lower cost.
- **REJ.0030** Hard quality gates blocking approval. Rejected: these are
  assignments for people, and the principal decides what ships.
- **REJ.0040** A templated brief with chapters (goal, high-level idea,
  and so on). Rejected; see POS.0110.
- **REJ.0050** Priority tags on items (`critical`, `important`,
  `nice-to-have`). Originally wanted as an optional attribute, dropped in
  favour of the group BRD convention: everything is essential, exceptions
  are noted as *optional*.
- **REJ.0060** Separate templates per genre of assignment. Rejected in
  favour of one universal skeleton with optional sections, so that
  everything arriving from the principal has a consistent shape.
- **REJ.0070** A dedicated feedback channel for comments coming back from
  the recipients. Rejected; see POS.0170.
- **REJ.0080** Merging document review and substantive challenge into one
  reviewer. Rejected: an agent doing both does neither properly, and the
  formal audit benefits from a clean context while the substantive
  challenge benefits from a different register entirely.
- **REJ.0090** Composite naming such as `BA-FLOW` for the BA initiative.
  Rejected because it destroys the word; `FLOW:BA` keeps both the
  programme and the instance legible.
- **REJ.0100** Single-letter and hyphenated ID prefixes (`R-001`,
  `P-01`). Replaced by three-letter dotted `PREFIX.NNNN` aligned with the
  group BRD standard.
- **REJ.0110** MAJOR.MINOR versioning with MAJOR meaning a scope change.
  Replaced by the group convention where integers denote approval; a
  scope change is a reason for re-approval anyway.
- **REJ.0120** "Mandate" and "charter" as the name of the handover
  document. Mandate rejected outright by the principal; charter carries
  project-management ceremony and implies a project, which many
  assignments are not. "Assignment" retained.
- **REJ.0125** The founding framing "a CTO's tool for briefing his direct
  reports (heads)" as the system's identity. Dropped by the principal on
  2026-07-31: it describes the first instance, not the engine.
  Superseded by the general-engine framing (POS.0005).
- **REJ.0130** "Cascade" as the system name: literally names the
  waterfall. "Foundry" rejected for collisions (Azure AI Foundry,
  Palantir Foundry). "Continuum", "Strata", "Idea Forge" and Czech
  "Kovárna" considered; **Forge of Thought** chosen.
- **REJ.0140** `local/` as the home of user-local files (POS.0750,
  adopted 2.1). Dropped on 2026-08-29: it existed only to keep company
  material out of the repository, which the gitignored `projects/*` now
  does; deck templates live in a library project (POS.0970) and are
  named by path (POS.0740).
- **REJ.0150** Shapes of the engine/projects relation rejected on
  2026-08-29 (research `2026-08-29-git-engine-projects-separation.md`,
  `2026-08-29-framework-distribution-in-the-field.md`): git submodules,
  subtree and worktrees — they model a dependency, which this relation
  is not; the engine as a template repository and copying the engine
  into projects — every comparable project that does so ends in
  manifests, override layers and migrations; a plugin as the only shape
  now (THR.0190).

## Candidate structure for assignment

Not applicable: this project's handover artefacts are the core itself
(`CLAUDE.md`, `templates/`, `.claude/`) and `README.md`. A
`20-assignment.md` would duplicate them for an audience that does not
exist; see the ledger.
