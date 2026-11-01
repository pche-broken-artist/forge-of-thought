---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 216cc6352a2bf91d
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1190
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.1520
  - projects/forge/10-intent.md#POS.1530
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#POS.1550
  - projects/forge/10-intent.md#POS.1560
  - projects/forge/10-intent.md#POS.1590
  - projects/forge/10-intent.md#POS.1600
  - projects/forge/10-intent.md#POS.1610
  - projects/forge/10-intent.md#POS.1740
  - projects/forge/10-intent.md#POS.1770
  - projects/forge/10-intent.md#POS.1800
  - projects/forge/10-intent.md#POS.1830
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.1870
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/10-intent.md#POS.1890
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/10-intent.md#POS.1910
  - projects/forge/10-intent.md#Elicitation
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/pull/SKILL.md
  - .claude/skills/work/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - templates/ledger.md
  - templates/history.md
  - templates/decisions.md
  - templates/project.md
  - templates/thread.md
  - templates/brd.md
  - templates/research.md
  - templates/research-plan.md
  - templates/recipe-readme.md#Pinned facts (not rendered)
  - scripts/forge-engine.py
  - scripts/forge-cite.py
  - tmp/README.md
---

# Glossary

The glossary is the list of every term of the forge, one line each,
with the file that defines it. It is for anyone who meets a word on
another page and wants its meaning in one sentence: the user, the
extender and the evaluator. The principal (whoever's thinking is
being forged) and Claude (the AI assistant working with him) are
defined in the table like every other term. For the forge described
in prose, see [What the forge is and is not](../about/what-it-is-and-is-not.md).

The terms stand in alphabetical order. Where one word has two
meanings, each meaning has its own row, with the sense in brackets.
"The forge intent" in the last column is the file
`projects/forge/10-intent.md`, cited by the section that holds the
term.

| Term | What it is | Defined in |
|---|---|---|
| archive | A history table written before the log, moved as it stands to `<file>.history.archive.md`, or the hand-kept ledger kept as `ledger.archive.md`; immutable, and searched together with the log. | `CLAUDE.md` (Versioning & status), `templates/ledger.md` |
| artefact | A document of the chain (a brief, the intent or a layer below it), composed by the principal with Claude and versioned. | `CLAUDE.md` (Document kinds) |
| assignment | The layer `20-assignment.md`, which carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| BRD | The layer `30-brd.md` below the assignment and above the solution design: the business requirements that break the parent into rules, behaviour and qualities the stakeholders can review and the delivery can estimate. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| branch | A voluntary line of work in git, created or switched to through `scripts/forge-branch.py`, its merge left to git by hand or by merge request. | `CLAUDE.md` (Persistence) |
| brief | The principal's free-form text of one whole of thinking (what he wants and why), rough on purpose and mined into the intent, kept as `00-brief.md` or `00-brief-<name>.md`. | `.claude/skills/forge/states/brief.md` |
| bundle | A set of related files kept as one source in `sources/<slug>/`, with one entry in the resource index and its own `00-INDEX.md`. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| business requirement (BR) | One rule of the business in a BRD, testable and worded with `shall`, citing the REQ or POS that is its parent. | `.claude/skills/forge/states/brd.md` |
| card | One question of a research plan, answered by one kind of evidence from one kind of source, with its disconfirming query and its stop rule. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| challenge (CHL) | One result of a challenger on the substance of the thinking, given its ID by the command and settled by walkthrough. | `CLAUDE.md` (ID scheme), `.claude/skills/challenger-contract/SKILL.md` |
| challenger | An isolated reviewer of the substance of the thinking, never of document quality, run as `/challenge <persona> [artefact]` with its reports filed in `challenges/`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/challenger-contract/SKILL.md` |
| check | An isolated reviewer of mechanical conformance with the conventions of the engine, run as `/check <check> [slug]`, filing a report in `reviews/` only when it finds something. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/check-contract/SKILL.md` |
| citation check | The run of `scripts/forge-cite.py` that opens every URL of a research note before the note is filed and classes each as ok, dead, unverifiable or mismatch. | `scripts/forge-cite.py`, the forge intent (Research) |
| Claude | The AI assistant that works as the cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, and it proposes but never decides. | `CLAUDE.md` (Roles) |
| contract | The skill that owns what every member of one kind of agent shares (the subject, the way of working, the shape of the output), preloaded into each agent of that kind. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/docs-contract/SKILL.md` |
| contributor | One who works on a branch of a hosted project and saves it there, leaving the merge to the integrator. | the forge intent (Operating environment) |
| critic | An isolated reviewer of the quality of the documents, never of their substance, run as `/critique <lens> [artefact]` with its reports filed in `reviews/`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/critic-contract/SKILL.md` |
| decision (DEC) | A record of one decision of the principal with its reason in the append-only `decisions.md`, never edited and superseded only by a newer record that names it. | `templates/decisions.md` |
| definition | The state file `.claude/skills/forge/states/<state>.md` of one artefact, in seven blocks (Target, Inputs, Aim, Partner, Map, Instruments, Course), by which `/forge <state>` works that artefact. | `CLAUDE.md` (Document chain), the forge intent (Elicitation) |
| dependency (DEP, in a BRD) | An item of a BRD naming what the BRD relies on outside itself, such as another system or a document that must be supplied from outside the forge. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| dependency (of a project) | A document of another repository that a project cites, a library's among them, registered in the ledger's Dependencies table without a version. | `templates/ledger.md` |
| derived (page) | A page that puts together what no single file says, from evidence in several. | `.claude/skills/docs-contract/SKILL.md` |
| derived file | A file made from others for a reader (a render, the README, the release notes, the documentation, the state render, a published file), made only on `main` and taken as `ours` at a merge. | `CLAUDE.md` (Persistence), the forge intent (Operating environment) |
| disconfirming query | One search of a card written to find the opposite of what is expected, its result reported even when it finds nothing. | `templates/research-plan.md`, `.claude/skills/research/SKILL.md` |
| document | Every file of a project, each of one kind that says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md` (Document kinds) |
| documentation | The pages of one topic each in `docs/` with their index, generated by `/document` for the user, the extender and the evaluator and never composed by hand. | `CLAUDE.md` (Document chain), `.claude/skills/document/SKILL.md` |
| documentation map | The file `docs-map.md` beside the owning project's ledger, with one entry per page holding everything that page is made from, never shown to the reader. | `CLAUDE.md` (Document kinds), `.claude/agents/docs-planner.md` |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, the conversation being its medium and the interview, research and sources its instruments. | the forge intent (Elicitation) |
| engine (of the forge) | The git repository of Forge of Thought itself, with its rules, skills, agents, scripts and templates, which carries no instance facts. | `CLAUDE.md` (Persistence), the forge intent (Operating environment) |
| engine (of another model family) | A model of another family reached by `scripts/forge-engine.py` over its own command-line tool, one row of the script's engine table each, `antigravity` the first. | `scripts/forge-engine.py`, the forge intent (Research) |
| envelope | The structured answer an engine's run returns (its status, its response and its usage), saved beside the packet as `envelope.json` for inspection. | `scripts/forge-engine.py` |
| explanation | A kind of page that carries what a thing is, how it works and why, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md` |
| extract | The Markdown text `scripts/doc2md.py` makes of a binary on the principal's word, which then is the source in place of the original. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| fact (FCT) | An item of the intent saying what is the case, on the principal's word or on a source's cited to its file, never a stance and never verified on demand. | the forge intent (Structure and style of an assignment) |
| finding (FND) | One result of a critic (document quality) or of a check (conformance), numbered in the project's one FND sequence. | `CLAUDE.md` (ID scheme), `.claude/skills/critic-contract/SKILL.md`, `.claude/skills/check-contract/SKILL.md` |
| format file | The file a recipe's Format makes from a render through the format's script (a `.docx`, a `.pptx`, a video or player events), landing beside the render or at the recipe's `output:` path. | `.claude/skills/render/SKILL.md`, the forge intent (Growth path) |
| genre | A kind of recipe composed through an interview with `/recipe <genre>`, from its skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md` (Document chain) |
| growing bundle | A bundle of one origin that keeps arriving (issues, minutes), grown file by file through `/ingest --bundle <name>`, each file immutable from its own registration. | `.claude/skills/ingest/SKILL.md` |
| guarded command | A command that changes files the moment it runs (such as `/save`, `/release`, `/render` or `/document`), which the harness keeps Claude from starting on its own judgement. | the forge intent (Operating environment) |
| harness | The program Claude runs in, which loads its agents and enforces the guards, hooks and permissions on the principal's behalf. | the forge intent (Operating environment), `.claude/skills/document/SKILL.md` |
| history companion | The append-only file `<file>.history.md` beside every versioned document, holding one record per change while the body holds the current state. | `CLAUDE.md` (Versioning & status), `templates/history.md` |
| hook's ask | The question `scripts/hook-git.py` puts to the principal for one of the few git commands that finish the step of a conflict, run on his yes, while every other write of git is denied with the name of the script to use. | `CLAUDE.md` (Persistence) |
| how-to | A kind of page that carries what the person does, step by step where there are steps, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md` |
| immutable | Said of a document never edited once written (a review, a challenge, a research note, a source from its registration, a closed thread), by a process rule and not by a mechanism of git. | `CLAUDE.md` (Versioning & status) |
| independence of engines | The measure, never the assumption, that a second engine's note was written from the web and not from the first engine's, counted over shared URLs and sentences by `scripts/forge-cite.py --independence`. | the forge intent (Research), `scripts/forge-cite.py` |
| index (of the documentation) | The file `docs/README.md`, derived by a script from the documentation map, listing every page by its line and each reader's path. | `.claude/skills/document/SKILL.md`, `.claude/agents/docs-planner.md` |
| instance | One installation of the forge, prepared by `/setup` after the engine is cloned. | `CLAUDE.md` (Commands), `.claude/skills/docs-contract/SKILL.md` |
| instance fact | A fact of one instance (who the principal is, the conversation language, the author's handle), kept in the gitignored `CLAUDE.local.md` and never let into a report, a render or a page. | `CLAUDE.md` (What this workspace is, Isolated reviewers), the forge intent (Operating environment) |
| integrator | The maintainer of a hosted project, typically the principal, who merges the contributors' branches: on the server where there is no conflict, on his clone through the step of a conflict where there is. | the forge intent (Operating environment) |
| intent | The working document `10-intent.md`: the principal's current positions, facts, threads and rejected directions, chiselled from the briefs and rewritten for coherence each round. | `.claude/skills/forge/states/intent.md`, the forge intent (Document chain) |
| isolated subagent | A subagent that sees nothing of the working conversation, reads every input from disk in its own run and lets no instance fact into what it returns. | `CLAUDE.md` (Isolated reviewers) |
| isolation | The rule that a reviewer judges only what the documents say and is never told what the drafter intended. | `.claude/skills/critic-contract/SKILL.md`, `CLAUDE.md` (Isolated reviewers) |
| kind (of a document) | The one class each document has (an artefact, a history, a ledger, a render and the others of the table), which says who writes it, whether it is versioned and how it behaves. | `CLAUDE.md` (Document kinds) |
| kind (of a project) | `thought` or `library`, declared in the project file, `thought` by default. | `templates/project.md`, the forge intent (Document chain) |
| layer | An artefact of the chain below the intent (the assignment, the BRD, the solution design), taken by a project only where it needs it. | `CLAUDE.md` (Document chain) |
| ledger | The file `ledger.md`, the single source of truth for a project's state, built from the documents by `scripts/forge-ledger.py` and never kept in git. | `CLAUDE.md` (Ledger), `templates/ledger.md` |
| lens | One specialisation of the critic, an agent file `critic-<lens>` of its own with its Lens section. | `CLAUDE.md` (Isolated reviewers) |
| Lens section | The one section of a critic, challenger or check agent file that is its own, which may narrow its contract or make a shared rule stricter but never renames, drops or duplicates one. | `CLAUDE.md` (Isolated reviewers) |
| library | A project of kind `library`, its name prefixed `lib-`, with no chain: material shared across projects, maintained by its owner and cited by path. | `CLAUDE.md` (Repository layout), `.claude/skills/ingest/SKILL.md` |
| made at read time | Said of the ledger: built by its script from the documents whenever it is needed, so that it never exists as a file to merge. | the forge intent (Versioning and state) |
| major | An approved integer version of the forge intent that closes a set of features the principal names, its release tagged `v<major>`. | the forge intent (Versioning and state), `CLAUDE.md` (Persistence) |
| manual | The command `/man` (alias `/manual`), which reads the forge's own definitions at the call and answers for a command, a working method or a need said in free words. | `.claude/skills/man/SKILL.md` |
| Map (of a definition) | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area was consciously considered, never a questionnaire. | the forge intent (Elicitation) |
| merge driver `ours` | The git setting by which a derived file keeps one side at a merge and is then made again instead of merged. | `CLAUDE.md` (Persistence), the forge intent (Operating environment) |
| migration | The run of `/migrate [slug]` through `scripts/forge-migrate.py` that brings a project to the shape of a release that changed the shape of files, once per project, on one clone, on the principal's word. | `.claude/skills/migrate/SKILL.md`, the forge intent (Operating environment) |
| mined | Said of a brief whose substance the intent has absorbed, recorded in the intent's history as pending, partial, mined or dropped. | `.claude/skills/forge/states/brief.md`, `templates/history.md`, `templates/ledger.md` |
| mirrored (page) | A page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md` |
| non-functional requirement (NFR) | A quality in a BRD by category, its value given by the stakeholders or left open as a TBC with an owner. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| packet | The folder holding `packet.md`, the whole context of one agent's run on a card or on a draft plan, the same for both engines and free of the conversation. | `.claude/skills/research/SKILL.md`, `scripts/forge-engine.py` |
| page | One page of the documentation, of one topic and one kind, or its index; never a source of truth. | `CLAUDE.md` (Document kinds), the forge intent (Growth path) |
| parent (of an item) | The item of the layer above that a BRD item carries and cites: a REQ of the assignment, or a POS where the project has no assignment. | `.claude/skills/forge/states/brd.md` |
| persona | One specialisation of the challenger, an agent file `challenger-<persona>` of its own with its Lens section. | `CLAUDE.md` (Isolated reviewers) |
| perspective | One standpoint from which a research plan looks at its topic, listed with the cards that serve it or with none. | `templates/research-plan.md` |
| pinned fact | A fact of a project that no file owns yet (a prerequisite, an install line, the public home of the repository), kept in the "Pinned facts" section of the README recipe for the documentation and never printed in the README. | `templates/recipe-readme.md` |
| plain file | The `.docx`, `.pptx`, video or player file that `/render` makes from a render through the script its format names, deterministic and cheap. | `CLAUDE.md` (Document chain), `.claude/skills/render/SKILL.md` |
| plan | The research plan shown and confirmed before anything is searched: its purpose, perspectives, assumptions, what is left out, its cards and its agents. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| player page | The page `docs/videos/index.html` that plays the player events of screenplays, written anew by `scripts/md2video.py` from `templates/html-player.html`. | the forge intent (Growth path) |
| position (POS) | An item of the intent saying what the principal holds or wants and why, naming the brief or source it comes from. | the forge intent (Document chain, Structure and style of an assignment) |
| primary render | The render in the first language a recipe declares, from which the renders in its other languages are translated. | the forge intent (Document chain) |
| prime directive | One of the ten rules at the head of `CLAUDE.md` that hold in every working conversation, such as "When unsure, ask". | `CLAUDE.md` (Prime directives) |
| principal | Whoever's thinking is being forged: the one who supplies ideas, answers and decisions, and the final authority on all content. | `CLAUDE.md` (Roles) |
| principal's own file | Any file in `renders/` or `published/` that no recipe names, made by hand from the forge's files and kept in git with no companion, no row and no check. | `CLAUDE.md` (Document chain), the forge intent (Document chain) |
| profile | A copy of the user's settings made for one run of another engine, with the forge's tree and the shell denied and the web allowed, kept in the run folder as its record. | the forge intent (Research), `scripts/forge-engine.py` |
| project | One body of work under `projects/<slug>/`, of kind thought or library, a git repository of its own unless it is outside git. | `CLAUDE.md` (Repository layout, Persistence) |
| project file | The file `project.md`, written once at a project's creation, holding its slug, its kind and its language. | `templates/project.md`, the forge intent (Document chain) |
| project outside git | A project whose directory is not the top of a git repository, on which the forge runs no git: a property, not a defect. | `CLAUDE.md` (Persistence) |
| provenance | The front-matter a render opens with, naming its recipe and every input with its version, and in the intent what a position names as its origin. | `.claude/skills/render/SKILL.md`, the forge intent (Document chain) |
| provenance map | The tool of a joint pass that maps every group to its items and to the parent items they came from, showing what landed nowhere and what has no parent, never part of the artefact. | `.claude/skills/forge/states/assignment.md` |
| public folder | The engine's `docs/videos/`, the one public place of an instance, into which a recipe's `output:` path may send a format file, left alone by `/document`. | `CLAUDE.md` (Document chain), the forge intent (Growth path) |
| published companion | The file `published/<recipe>.md` beside a published file, holding its provenance (recipe, render, model, date), its state current or stale computed by the ledger. | `.claude/skills/publish/SKILL.md` |
| published file | The designed `.pptx` or `.docx` that `/publish` makes from a render through a model, only on the principal's command. | `CLAUDE.md` (Document chain), `.claude/skills/publish/SKILL.md` |
| pull | The command `/pull`, which looks at the remote, says each repository's state against the origin and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| quick and deep | The two depths of `/research`: `--quick` is one card on the session model filed as one note, `--deep` a plan of several cards filed as a bundle with a synthesis. | `.claude/skills/research/SKILL.md`, the forge intent (Research) |
| recipe | The versioned file `recipes/<recipe>.md` that says how a render is made (its inputs, audience, instructions and output template), iterated and never approved. | `CLAUDE.md` (Document chain) |
| recipients | Those who receive an assignment: teams, colleagues or the principal's future self. | `CLAUDE.md` (What this workspace is) |
| record | One line of a history companion for one change, with its date, version, author, subject, kind and reason, and its Action and Was where it has them. | `templates/history.md` |
| record of state | A record that changes a state only (a mining, a finding closed, a thread closed, a work product's state), carrying the current version without raising it. | `templates/history.md`, the forge intent (Versioning and state) |
| reference (page) | A kind of page that states facts in the structure of what it mirrors, a table where the input is a table, and never explains. | `.claude/skills/docs-contract/SKILL.md` |
| registration of the merge driver | The once-per-machine write of the merge driver `ours` and the git settings it needs into the user's global git configuration, by `/setup` through `scripts/forge-config.py` on the user's word. | `CLAUDE.md` (Persistence) |
| rejected direction (REJ) | An item of the intent recording a direction the principal dropped, with the reason it was dropped. | `CLAUDE.md` (ID scheme), `.claude/skills/forge/states/intent.md` |
| release | The command `/release`, from `main` only, which runs its checks, renders the README and the release notes again and then saves with the release message and, at an approved major, the tag. | `CLAUDE.md` (Persistence) |
| render | An output for one audience generated from the chain by `/render <recipe>`, never edited by hand and never a source of truth. | `CLAUDE.md` (Document chain), `.claude/skills/render/SKILL.md` |
| Reports | The section of the ledger in which its script says what the merged files cannot, such as an ID defined twice, present only when there is something to say. | `templates/ledger.md` |
| research | A durable answer to a question about the world outside, made by `/research`, filed in `research/` and immutable. | `CLAUDE.md` (Document kinds), `.claude/skills/research/SKILL.md` |
| research bundle | The folder `research/YYYY-MM-DD-<topic>/` with the plan and the synthesis at its head in `00-plan.md` and one note per card per engine. | `.claude/skills/research/SKILL.md` |
| research note | One card answered by one engine in the shape of `templates/research.md`, immutable from its filing. | `templates/research.md` |
| resource index | The `00-INDEX.md` of `sources/` and of `research/`, a light catalogue of what each resource is and is for, which tracks no state. | `CLAUDE.md` (Document chain) |
| Role | The free-text field of a source's index entry that says what the source is for, the principal's word asked before the entry is written. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| roster of areas | The instance's list of the areas of the enterprise a BRD must consider and which of them are mandatory, a library document cited by path, or `Roster: none` where there is none. | `.claude/skills/forge/states/brd.md` |
| round | One working conversation over an artefact or open items, its answers carried in the conversation and written once at its end as one version. | `CLAUDE.md` (Prime directives), `.claude/skills/walkthrough/SKILL.md` |
| run folder | The folder `tmp/research/<run>/` holding the packets, envelopes, profiles and citation reports of one research run, kept for inspection. | `.claude/skills/research/SKILL.md`, `scripts/forge-engine.py` |
| save | The command `/save`, which runs its check and then commits and pushes on whatever branch is checked out, `--quick` leaving the check out. | `CLAUDE.md` (Persistence) |
| screenplay | A render of the genre `screenplay` that tells a terminal conversation in scenes with captions, made into a video or into player events by `scripts/md2video.py`. | the forge intent (Document chain) |
| second engine | An engine of another model family asked for by name with `/research --deep --engine <name>`, which reviews the draft plan and answers every card beside the session model. | `.claude/skills/research/SKILL.md`, the forge intent (Research) |
| session | One working conversation of Claude with the principal, whose context a subagent may see and which `/end` closes. | `CLAUDE.md` (Persistence), the forge intent (Operating environment) |
| session model | The one model on which every command, chain state and reviewer of the forge runs, set in the gitignored `.claude/settings.local.json` and inherited by the agents. | `CLAUDE.md` (Repository layout, Isolated reviewers) |
| shape of a project | The set of marks, one per step of a migration, by which `scripts/forge-migrate.py` recognises a project, a project without `project.md` being of the shape before the migration. | the forge intent (Operating environment), `templates/project.md` |
| solution design | The layer `40-solution-design.md`, which says how the things wanted are realised, part by part as SOL items, with the choices they rest on. | `.claude/skills/forge/states/solution-design.md` |
| source | An external input as it arrived (a transcript, an offer, a document), kept in `sources/` in one form, text or a functional binary, and immutable from its registration. | `CLAUDE.md` (Document chain) |
| specification | The versioned file `work/<name>.spec.md` of a work product, which holds the way and the why and from which the work file is made. | `.claude/skills/work/SKILL.md`, the forge intent (Document chain) |
| stale | Said of a render when a version its provenance cites differs from the current version of that file or the file is gone, and of a published file when its render is newer. | `.claude/skills/render/SKILL.md`, `templates/ledger.md` |
| state against the origin | A repository's standing as `/pull` reports it: up to date, behind, ahead, diverged, no origin or not under git. | `.claude/skills/pull/SKILL.md` |
| state map | What bare `/forge [slug]` shows: the state of a project's chain. | `CLAUDE.md` (Commands) |
| state render | The file `renders/state.md`, the ledger as a render, written by `/release` on `main`. | `CLAUDE.md` (Repository layout) |
| step of a conflict | The settling of a conflict that `scripts/forge-save.py` meets and leaves standing: Claude lays both sides out as a walkthrough, the principal decides and Claude writes the wording. | `CLAUDE.md` (Persistence) |
| stop rule | The condition on a card that ends its search: nothing new from a differently worded query and a primary source for every perspective, or the budget of openings spent. | `templates/research-plan.md`, `templates/research.md` |
| subagent | An agent Claude launches for one job in a context of its own, such as a reviewer, a renderer, a documentation agent or a research agent. | `CLAUDE.md` (Isolated reviewers) |
| synthesis | Claude's account of a research from its notes alone: completeness card by card, the engines' answers side by side, the unexpected, what was not found and its own view last and apart. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| tag | A named mark on one commit in git: `v<major>` on the release of an approved major, any other on the principal's request with a free name. | `CLAUDE.md` (Persistence) |
| template | A canonical skeleton in `templates/` from which a new document is created, a skeleton named `<type>-definition.md` being that of one member of a type the forge can be extended by. | `CLAUDE.md` (Templates) |
| thought project | A project of kind `thought`, whose chain starts at a brief and has the intent as its trunk. | `CLAUDE.md` (Repository layout, Document chain) |
| thread (THR) | One open matter of the intent, carrying its origin and, while it is unsettled, the working debate. | the forge intent (Document chain, Structure and style of an assignment), `.claude/skills/forge/states/intent.md` |
| thread file | The file `threads/THR.NNNN.md` of one thread, whose header says what it concerns, its origin and whether it is open, freely rewritten while open and immutable once closed. | `.claude/skills/forge/states/intent.md`, `templates/thread.md` |
| touched area | An area of the roster that a BRD must find or knowingly find not to apply, a mandatory area never left silent. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| translation | A render in a further language a recipe declares, made from the primary render in the same run, scene for scene and line for line. | the forge intent (Document chain), `.claude/skills/render/SKILL.md` |
| Unowned | The section of the documentation map listing every fact a page needs that no file supports, left off the page until a file gives it a home. | `.claude/agents/docs-planner.md` |
| use case (UC) | Behaviour in a BRD agreed as a sequence at user-goal level, its steps in the active voice, citing its parent. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| verdict | The principal's word on one item (accept, modify, question, reject, park or obsolete), given in answer to the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. | `.claude/skills/walkthrough/SKILL.md` |
| Verdict line (of a decision) | The line of a decision that rules on a finding or a challenge, one per ID, saying it is rejected, parked until an event, or obsolete. | `templates/decisions.md` |
| Waiting on principal | The section of the ledger that lists by rule what waits on the principal: the open threads, the TBCs he owns, the open findings of a critic and the open challenges, and the parked ones with their decision. | `templates/ledger.md` |
| walkthrough | The working method that puts a list of items needing the principal's decision before him one item per message, in order of weight, each closed with the verdict line. | `.claude/skills/walkthrough/SKILL.md` |
| way of merging | One of the three ways git is told to merge a file by its path: text, derived, or immutable and unique. | the forge intent (Operating environment) |
| work product | An output of a project made with work of its own (a model, an analysis), kept as two files in `work/`: the file with the content and its specification. | `.claude/skills/work/SKILL.md`, the forge intent (Document chain) |
| working folder | The folder `tmp/` at the engine's root, where runs leave their packets, tasks, dry ledgers and manifests, in git as a folder but never its contents, and no source of truth. | `tmp/README.md`, the forge intent (Operating environment) |
| working method | One of the named ways a working conversation runs, such as the walkthrough or one write per round, applied whenever its situation arises. | `CLAUDE.md` (Working methods) |
| write | The principal's word that closes a round, on which Claude reflects the round back and, on his yes, writes it as one version. | `.claude/skills/walkthrough/SKILL.md`, `CLAUDE.md` (Prime directives) |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
