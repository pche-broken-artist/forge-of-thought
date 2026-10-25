---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 6976043c9b39cf04
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1090
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

This glossary gives every term of Forge of Thought in one line, with
the file that defines it. It is for the user, the extender and the
evaluator who meet a word on another page and want its meaning
without reading the owner. The principal (whoever's thinking is being
forged) and Claude (the AI assistant working beside him) appear in
most lines. For the forge told in prose, read
[What the forge is and is not](../about/what-it-is-and-is-not.md).

The terms stand in alphabetical order. A path in the last column is
the file that defines the term; where a section of `CLAUDE.md` owns
it, the section is named in brackets.

| Term | Meaning | Defined in |
|---|---|---|
| **archive** | A history table or a hand-kept ledger from before the log, kept immutable as `<file>.history.archive.md` or `ledger.archive.md` and read beside the newer records. | `CLAUDE.md` (Versioning & status), `templates/ledger.md` |
| **artefact** | A document of the chain, such as the brief, the intent or the assignment, composed by the principal with Claude, versioned, and found through a definition of its own. | `CLAUDE.md` (Document kinds, Document chain) |
| **assignment** | The layer `20-assignment.md` that carries the in-scope substance of the intent to the recipients, complete and precise, for them to act on without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| **branch** | A line of work in git beside `main` (the released line), voluntary, switched to or created by `scripts/forge-branch.py` and merged by git, by hand or by merge request. | `CLAUDE.md` (Persistence) |
| **BRD** | The business requirements document `30-brd.md`, the layer below the assignment and above the solution design that breaks its parent into rules, behaviour and qualities the stakeholders can review and the delivery can estimate. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| **brief** | The principal's idea put together in free form and without IDs (`00-brief.md` or `00-brief-<name>.md`), where a chain starts and which is later mined into the intent. | `.claude/skills/forge/states/brief.md` |
| **bundle** | A set of related files of one origin, stored as `sources/<slug>/` with its own `00-INDEX.md` and counted as one source. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| **business requirement** | An item of a BRD (prefix BR) that states one testable rule of the business with `shall` and cites its parent. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| **card** | One question of a research plan, answered by one kind of evidence from one kind of source, with its disconfirming query and its stop rule. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| **challenge** | A result of a challenger (prefix CHL): a point against the substance of the thinking with its severity, filed in `challenges/` and settled by walkthrough. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/challenger-contract/SKILL.md` |
| **challenger** | An isolated reviewer of the substance of the thinking, never of document quality, run as `/challenge <persona> [artefact]`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/challenger-contract/SKILL.md` |
| **check** | An isolated reviewer of mechanical conformance with the conventions of the engine, never of substance or quality, run as `/check <check> [slug]`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/check-contract/SKILL.md` |
| **citation check** | The opening of every URL a research note cites, by `scripts/forge-cite.py`, before the note is filed, a dead page or a mismatched arXiv title being the mark of a fabricated citation. | `scripts/forge-cite.py`, `projects/forge/10-intent.md` |
| **Claude** | The AI assistant that works as the cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, and it proposes but never decides. | `CLAUDE.md` (Roles) |
| **contract** | The skill that holds what every member of one kind of agent shares (conduct and isolation, the subject and its boundary, the way of working, the shape of the output), preloaded into each agent of that kind. | `.claude/skills/critic-contract/SKILL.md`, `.claude/skills/challenger-contract/SKILL.md`, `.claude/skills/check-contract/SKILL.md`, `.claude/skills/docs-contract/SKILL.md` |
| **contributor** | A person who works on a branch of a hosted project and saves it, leaving the merge to the integrator. | `projects/forge/10-intent.md` |
| **critic** | An isolated reviewer of document quality, never of substance, run as `/critique <lens> [artefact]`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/critic-contract/SKILL.md` |
| **decision** | A record of `decisions.md` (prefix DEC) that holds one decision of the principal with its reason and is never edited. | `templates/decisions.md` |
| **definition** | The state file `.claude/skills/forge/states/<state>.md` of one artefact, which says in seven blocks what the artefact is, how it is found and its rules, paired with the artefact's template. | `CLAUDE.md` (Document chain), `projects/forge/10-intent.md` (Elicitation) |
| **dependency (of a BRD)** | An item of a BRD (prefix DEP) that names what the BRD relies on outside itself, such as another system or a document to be supplied from outside the forge. | `templates/brd.md` |
| **dependency (of a project)** | A document of another repository, a library's among them, that a project cites by path and the ledger registers without a version. | `templates/ledger.md` |
| **derived (page)** | Said of a page put together from evidence in several files, by the reasoning its entry in the documentation map gives. | `.claude/skills/docs-contract/SKILL.md` |
| **derived file** | A document for a reader that lives in git and is made only on `main`, such as a render, the README or the documentation, taken as `ours` at a merge and then made again. | `projects/forge/10-intent.md` |
| **disconfirming query** | The one search of a card written to find the opposite of what is expected, run and reported whatever it finds. | `templates/research-plan.md`, `.claude/skills/research/SKILL.md` |
| **document** | Every file of a project, each of one kind that says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md` (Document kinds) |
| **documentation** | The pages of one topic each in `docs/` with their index, generated by `/document [slug]` from the documentation map and never composed by hand. | `CLAUDE.md` (Document chain), `.claude/skills/document/SKILL.md` |
| **documentation map** | The file `docs-map.md` beside the owning project's ledger: one entry per page with everything the page is made from, never shown to the reader. | `CLAUDE.md` (Document kinds), `.claude/agents/docs-planner.md` |
| **elicitation** | The process by which the principal and Claude find an artefact together and form the knowledge it holds, with the conversation as its medium and the interview, research and sources as its instruments. | `projects/forge/10-intent.md` (Elicitation) |
| **engine (the forge's)** | The forge's own repository of skills, agents, templates and scripts, as against the projects it works on, carrying no instance fact. | `CLAUDE.md` (Repository layout), `projects/forge/10-intent.md` |
| **engine (of another model family)** | A model of another family reached over its own command-line tool through `scripts/forge-engine.py`, one row of that script's engine table, such as `antigravity`. | `scripts/forge-engine.py`, `.claude/skills/research/SKILL.md` |
| **envelope** | The JSON answer an engine returns from one run, checked for success and a non-empty response and kept as `envelope.json` beside the packet. | `scripts/forge-engine.py` |
| **explanation** | A page that says what a thing is, how it works and why, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md` |
| **extract** | The Markdown conversion of a binary source, made by `scripts/doc2md.py` on the principal's word, which then is the source. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| **fact** | An item of the intent (prefix FCT) that states what is the case, on the principal's word or citing the source that states it, and is not a stance. | `CLAUDE.md` (ID scheme), `projects/forge/10-intent.md` |
| **finding** | A result of a critic or a check (prefix FND), filed in `reviews/` and settled by walkthrough; the word names a reviewer's result only. | `CLAUDE.md` (Isolated reviewers), `templates/ledger.md` |
| **format file** | The file a script makes from a render in the format the recipe's `## Format` section names, landing beside the render or at the recipe's `output:` path. | `.claude/skills/render/SKILL.md`, `projects/forge/10-intent.md` |
| **genre** | A kind of recipe with its own interview and skeleton `templates/recipe-<genre>.md`, composed through `/recipe <genre>`. | `CLAUDE.md` (Document chain) |
| **growing bundle** | A bundle of one origin that keeps arriving, such as issues or minutes, grown file by file through `/ingest --bundle <name>`, each file immutable from its own registration. | `.claude/skills/ingest/SKILL.md` |
| **guarded command** | A command that changes files the moment it runs, such as `/save`, `/render` or `/document`, which the harness keeps Claude from starting on its own judgement. | `projects/forge/10-intent.md` |
| **harness** | The program Claude runs in, which loads the skills and agents, runs the hooks and guards the commands that write. | `projects/forge/10-intent.md`, `.claude/skills/document/SKILL.md` |
| **history companion** | The append-only file `<file>.history.md` beside every versioned document, with one record per change. | `CLAUDE.md` (Versioning & status), `templates/history.md` |
| **the hook's ask** | The question the git hook `scripts/hook-git.py` puts to the principal before one of the few git commands that finish the step of a conflict, which then runs on his yes. | `CLAUDE.md` (Persistence) |
| **how-to** | A page that carries what the person does, step by step, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md` |
| **immutable** | Never edited once filed: reviews, challenges and research from their creation, sources from their registration, by a rule of the process and not a lock of git. | `CLAUDE.md` (Versioning & status) |
| **independence of engines** | The measure, by `scripts/forge-cite.py --independence`, of the URLs and sentences two engines' notes of one card share, which shows a note written from the other note rather than from the web. | `scripts/forge-cite.py`, `projects/forge/10-intent.md` |
| **index** | The page `docs/README.md`, which lists every page of the documentation and each reader's path through it, derived by a script from the documentation map. | `.claude/agents/docs-planner.md`, `.claude/skills/document/SKILL.md` |
| **instance** | One installation of the forge, whose own facts live in `CLAUDE.local.md` at the engine root, outside the repository. | `CLAUDE.md` (What this workspace is), `projects/forge/10-intent.md` |
| **instance fact** | A fact of one installation, such as a name, a role, an address or a host, which never enters the engine, a reviewer's report or a page. | `projects/forge/10-intent.md`, `CLAUDE.md` (Isolated reviewers) |
| **integrator** | The maintainer of a hosted project, typically the principal, who merges the contributors' branches on the server where there is no conflict and on his clone through the step of a conflict where there is. | `projects/forge/10-intent.md` |
| **intent** | The trunk of every chain, `10-intent.md`: the briefs chiselled into what the principal holds, as positions, facts, threads and rejected directions with their reasons. | `.claude/skills/forge/states/intent.md` |
| **isolation** | The rule that a reviewer or a documentation agent never sees the working conversation and reads every input from disk in its own run. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/docs-contract/SKILL.md` |
| **kind (of a project)** | The field `kind` of the project file, `thought` or `library`, which says which rules of the engine apply to the project. | `templates/project.md`, `projects/forge/10-intent.md` |
| **layer** | An artefact of the chain below the intent, such as the assignment, the BRD or the solution design, which a project takes only where it needs it. | `CLAUDE.md` (Document chain) |
| **ledger** | The file `ledger.md`, the single source of truth for a project's state, built from the documents by `scripts/forge-ledger.py` and never kept in git. | `CLAUDE.md` (Ledger), `templates/ledger.md` |
| **lens** | One critic's angle on document quality, defined in an agent file `critic-<lens>`. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/critic-contract/SKILL.md` |
| **Lens section** | The one section of a critic, challenger or check agent file that is its own, a specialisation of its contract and never a replacement. | `CLAUDE.md` (Isolated reviewers) |
| **library** | A project of kind `library` (directory `lib-<name>`) with no chain, holding sources, research and a README catalogue of material shared across projects. | `CLAUDE.md` (Repository layout) |
| **made at read time** | Built by a script from the documents whenever it is read, never written by hand and never in git, as the ledger is. | `projects/forge/10-intent.md`, `templates/ledger.md` |
| **major** | A version of the forge's intent that closes a set of features the principal names and, before its tag, passes every check, both critic lenses and one challenge. | `projects/forge/10-intent.md` |
| **Map** | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area was consciously considered, and never a questionnaire. | `projects/forge/10-intent.md` (Elicitation) |
| **merge driver `ours`** | The git setting that keeps one side of a derived file at a merge, the file being made again afterwards. | `CLAUDE.md` (Persistence), `projects/forge/10-intent.md` |
| **migration** | The one-off bringing of a project to the shape of a release that changed the shape of files, by `/migrate [slug]` through `scripts/forge-migrate.py`, on one clone and on the principal's word. | `.claude/skills/migrate/SKILL.md`, `projects/forge/10-intent.md` |
| **mined** | Said of a brief whose substance the intent has absorbed, its state being pending, partial, mined or dropped. | `templates/history.md`, `templates/ledger.md` |
| **mirrored (page)** | Said of a page that restates what its input files say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md` |
| **non-functional requirement** | An item of a BRD (prefix NFR) that names a quality by category, such as reliability or security, with a value from the stakeholders or an open question in its place. | `templates/brd.md`, `.claude/skills/forge/states/brd.md` |
| **packet** | The folder of one research agent's run under `tmp/research/<run>/`, whose `packet.md` (the card, the agent's brief and the note's shape) is the agent's whole context. | `.claude/skills/research/SKILL.md`, `scripts/forge-engine.py` |
| **page** | One file of the documentation, of one topic and one kind, generated from its entry in the documentation map and never edited by hand. | `CLAUDE.md` (Document kinds), `projects/forge/10-intent.md` |
| **parent of an item** | The item of the layer above that a BRD item carries: a requirement of the assignment, or a position of the intent where the project has no assignment. | `.claude/skills/forge/states/brd.md` |
| **persona** | One challenger's standpoint, defined in an agent file `challenger-<persona>` that names the blind spots it hunts. | `CLAUDE.md` (Isolated reviewers), `.claude/skills/challenger-contract/SKILL.md` |
| **perspective** | A standpoint from which a research topic is looked at, listed in the plan with the cards that serve it or with none. | `templates/research-plan.md` |
| **pinned fact** | A fact no file of a project owns yet, such as a prerequisite or the public home of the repository, kept in the readme recipe's section `## Pinned facts (not rendered)` for the documentation to read. | `templates/recipe-readme.md` |
| **plain file** | The file `/render` makes from a render through a script where the recipe names a format, deterministic and landing beside the render. | `CLAUDE.md` (Document chain), `.claude/skills/render/SKILL.md` |
| **plan** | The head of a research, `00-plan.md`, with its purpose, perspectives, assumptions, what is left out, cards and agents, confirmed by the principal before anything is searched. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| **player page** | The page `docs/videos/index.html` that plays the screenplays sent to the public folder, written anew by `scripts/md2video.py` from `templates/html-player.html`. | `projects/forge/10-intent.md`, `CLAUDE.md` (Repository layout) |
| **position** | An item of the intent (prefix POS) that says what the principal holds or wants and why, naming what it comes from. | `projects/forge/10-intent.md`, `CLAUDE.md` (ID scheme) |
| **primary render** | The render in the first language a recipe declares in `languages:`, made first and the one the other languages are translated from. | `projects/forge/10-intent.md`, `.claude/skills/render/SKILL.md` |
| **prime directive** | One of the ten standing rules at the head of `CLAUDE.md`, such as "When unsure, ask". | `CLAUDE.md` (Prime directives) |
| **principal** | Whoever's thinking is being forged: the one who supplies ideas, answers and decisions and has final authority on all content. | `CLAUDE.md` (Roles) |
| **profile** | The copy of the user's settings that `scripts/forge-engine.py` gives another engine for one run, with the forge's tree and the shell denied and the web allowed, kept in the run folder as its record. | `scripts/forge-engine.py`, `projects/forge/10-intent.md` |
| **project** | A directory under `projects/` holding one chain of thought or a library, a git repository of its own where it is under git. | `CLAUDE.md` (Repository layout) |
| **project file** | The file `project.md`, written once at a project's creation, holding its slug, kind and language. | `templates/project.md`, `projects/forge/10-intent.md` |
| **project outside git** | A project whose directory is not the top of a git repository, on which the forge runs no git, a property and not a defect. | `CLAUDE.md` (Persistence) |
| **provenance** | The front-matter a render opens with, naming its recipe and every input with its version, which the ledger's Renders table reads. | `.claude/skills/render/SKILL.md` |
| **provenance map** | A tool of the recast of an assignment or a BRD that lists each group with its items and the parent items they came from, with the parent items that landed nowhere and the items with no parent. | `.claude/skills/forge/states/assignment.md`, `.claude/skills/forge/states/brd.md` |
| **published companion** | The file `published/<recipe>.md` beside a published file, the one record of the recipe, render, model and date it was made from. | `.claude/skills/publish/SKILL.md` |
| **published file** | The designed `.pptx` or `.docx` that `/publish` makes from a render through a model, only on the principal's command. | `.claude/skills/publish/SKILL.md`, `CLAUDE.md` (Document chain) |
| **pull** | The way inward, `/pull`, which states each repository's standing against its origin (up to date, behind, ahead, diverged, no origin, not under git) and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| **quick and deep** | The two depths of `/research`: `--quick` is one card on the session model filed as one note, and `--deep` is a plan of several cards filed as a bundle with a synthesis. | `.claude/skills/research/SKILL.md` |
| **recipe** | The versioned file `recipes/<recipe>.md` that says how a render is made: its inputs, audience, instructions and output template. | `CLAUDE.md` (Document chain) |
| **recipients** | Those an assignment is addressed to, such as teams, colleagues or the principal's future self. | `CLAUDE.md` (What this workspace is) |
| **record** | One line of a history companion, giving date, version, author, subject, kind and reason, with `Action` and `Was` where they apply. | `templates/history.md` |
| **record of state** | A record that changes only a state, such as a brief mined, a finding closed, a thread closed or a work product's state, and carries the current version without raising it. | `templates/history.md` |
| **reference** | A page that states facts in the structure of what it mirrors, free of interpretation, and never explains. | `.claude/skills/docs-contract/SKILL.md` |
| **registration of the merge driver** | The one-off entry in the user's global git configuration, offered by `/setup` and written through `scripts/forge-config.py`, that makes the merge driver `ours` known on a machine. | `CLAUDE.md` (Persistence) |
| **rejected direction** | An item of the intent (prefix REJ) that records a direction dropped, with the reason. | `CLAUDE.md` (ID scheme), `projects/forge/10-intent.md` |
| **release** | The command `/release`, run from `main` only, which runs its checks, re-renders the README and the release notes and saves with the release message and tag. | `CLAUDE.md` (Persistence) |
| **render** | An output for one audience generated from the chain by `/render <recipe>`, never edited by hand and never a source of truth. | `CLAUDE.md` (Document chain), `.claude/skills/render/SKILL.md` |
| **Reports** | The ledger's section of what the merged files cannot say: an ID defined twice, a closed thread touched by a later commit, a thread cited with neither a file nor a closed record. | `templates/ledger.md` |
| **research** | A durable answer to a question about the world outside, made by `/research`, filed in `research/` and indexed, immutable from its filing. | `CLAUDE.md` (Document kinds), `.claude/skills/research/SKILL.md` |
| **research bundle** | A research of several cards, `research/YYYY-MM-DD-<topic>/`, with the plan and the synthesis at its head and one note per card per engine. | `.claude/skills/research/SKILL.md` |
| **research note** | The answer to one card from one engine, as `<card>.<engine>.md` in a bundle or as a single note, in the shape of `templates/research.md`. | `templates/research.md`, `.claude/skills/research/SKILL.md` |
| **resource index** | The `00-INDEX.md` of `sources/`, of `research/` and of each bundle: a light catalogue of what each resource is and is for, freely rewritten. | `CLAUDE.md` (Document chain) |
| **Role** | The free-text field of a source's index entry that says what the source is for, the principal's word asked before the entry is written. | `.claude/skills/ingest/SKILL.md`, `CLAUDE.md` (Document chain) |
| **roster of areas** | The instance's list of the areas of the enterprise a BRD must consider and which of them are mandatory, kept as a library document and cited by path. | `.claude/skills/forge/states/brd.md` |
| **round** | One working conversation over an artefact or open items, whose answers are carried in the conversation and written once at its end as one version. | `CLAUDE.md` (Prime directives), `.claude/skills/walkthrough/SKILL.md` |
| **run folder** | The folder `tmp/research/<run>/` that holds the packets, envelopes, profile, held notes and citation reports of one research run, kept for inspection. | `.claude/skills/research/SKILL.md`, `scripts/forge-engine.py` |
| **save** | The command `/save`, which runs its check and then commits and pushes on whatever branch is checked out, `--quick` leaving the check out. | `CLAUDE.md` (Persistence) |
| **screenplay** | A render of the genre `screenplay`: a terminal conversation as a title card and timed scenes with captions, turned by `scripts/md2video.py` into a video or the events of the player page. | `projects/forge/10-intent.md` |
| **second engine** | An engine of another model family added to a deep research by `--engine <name>`, which reviews the draft plan and answers every card on the same packet as the session's agents. | `.claude/skills/research/SKILL.md`, `projects/forge/10-intent.md` |
| **session** | One run of Claude in the harness with its working conversation, which no isolated agent sees. | `CLAUDE.md` (Commands, Isolated reviewers) |
| **session model** | The one model the whole forge runs on, inherited by every reviewer and agent (`model: inherit`). | `CLAUDE.md` (Isolated reviewers) |
| **shape of a project** | The form of a project's files a release expects, recognised by `scripts/forge-migrate.py` as a set of marks, one per step of the migration. | `.claude/skills/migrate/SKILL.md`, `templates/project.md` |
| **solution design** | The layer `40-solution-design.md` that says how the things wanted are realised, part by part (prefix SOL), with the choices they rest on. | `.claude/skills/forge/states/solution-design.md` |
| **source** | An external input as it arrived, such as a transcript, an offer or a document, stored in `sources/` by `/ingest` and immutable from its registration. | `CLAUDE.md` (Document chain), `.claude/skills/ingest/SKILL.md` |
| **specification** | The versioned file `work/<name>.spec.md` of a work product, holding the way and the why: the task, its inputs, the method, the assumptions, the open questions and how the file is made. | `.claude/skills/work/SKILL.md`, `projects/forge/10-intent.md` |
| **stale** | Said of a render when a version its provenance cites differs from the file's current version or the cited file is gone, and of a published file or a work product when what it was made from is newer. | `.claude/skills/render/SKILL.md`, `templates/ledger.md` |
| **state render** | The file `renders/state.md`, the ledger written as a tracked render by `/release` on `main`. | `CLAUDE.md` (Repository layout) |
| **step of a conflict** | The settling of a conflict `forge-save` met: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording, and git's finishing commands run on the hook's ask. | `CLAUDE.md` (Persistence) |
| **stop rule** | The rule that ends the search of a card: nothing new from a differently-worded query and a primary source for every perspective of the card, or the budget of openings spent. | `templates/research-plan.md`, `templates/research.md` |
| **subagent** | A separate run of Claude launched for one task in a context of its own, such as a reviewer or a documentation writer, which never sees the working conversation. | `CLAUDE.md` (Isolated reviewers) |
| **synthesis** | Claude's account of a deep research from its notes alone: completeness card by card, the engines' answers side by side, the unexpected and the not found gathered, and Claude's own view last and apart. | `.claude/skills/research/SKILL.md`, `templates/research-plan.md` |
| **tag** | A name git gives a commit: `/release` says which release receives `v<major>`, and any other tag is the principal's request with a free name. | `CLAUDE.md` (Persistence) |
| **template** | A canonical skeleton in `templates/` from which a new document is made, the one beside a definition saying what the artefact comes out as. | `CLAUDE.md` (Templates, Document chain) |
| **thought project** | A project of kind `thought`: one chain from a brief onward, with its records, renders and resources. | `CLAUDE.md` (Repository layout), `templates/project.md` |
| **thread** | An open matter of the intent (prefix THR) to elicit next, naming the artefact it concerns and carrying its origin. | `CLAUDE.md` (ID scheme), `projects/forge/10-intent.md` |
| **thread file** | One file per thread in `threads/`, whose header (`concerns`, `origin`, `status`) is its state, freely rewritten while open and immutable once closed. | `.claude/skills/forge/states/intent.md`, `templates/thread.md` |
| **touched area** | An area of the roster that a BRD walks, found in its items or found not to apply with the reason, a mandatory one never left silent. | `.claude/skills/forge/states/brd.md`, `templates/brd.md` |
| **translation** | A render in a further language of the recipe, translated from the primary render scene for scene and line for line and citing it in `translated_from`. | `.claude/skills/render/SKILL.md`, `projects/forge/10-intent.md` |
| **Unowned** | The documentation map's list of facts a page needs and no file supports, left out of the pages until the owner gives them a home. | `.claude/agents/docs-planner.md`, `.claude/skills/document/SKILL.md` |
| **use case** | An item of a BRD (prefix UC) that describes behaviour to be agreed as a sequence, at user-goal level, its steps in the active voice. | `templates/brd.md`, `.claude/skills/forge/states/brd.md` |
| **verdict** | The principal's answer to one item of a walkthrough or one step that needs his consent (accept, modify, question, reject or park), asked for by the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. | `.claude/skills/walkthrough/SKILL.md` |
| **Verdict line** | The line of a decision record that rules on a finding or a challenge: `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`. | `templates/decisions.md` |
| **Waiting on principal** | The ledger's section of what waits on the principal, made by rule from the open threads, the open questions he owns, the open critic findings and challenges, and the parked ones under a heading of their own. | `templates/ledger.md`, `CLAUDE.md` (Ledger) |
| **walkthrough** | The working method by which a list of items that need the principal's decision is worked one item per message, in order of weight, each closed with the verdict line. | `.claude/skills/walkthrough/SKILL.md`, `CLAUDE.md` (Working methods) |
| **way of merging** | One of the three ways a file of a project merges (text, derived, or immutable and unique), which the forge tells git through `.gitattributes`. | `projects/forge/10-intent.md` |
| **work product** | An output of a project made with work of its own, such as a model or an analysis, kept in `work/` as its file with its specification beside it. | `.claude/skills/work/SKILL.md`, `projects/forge/10-intent.md` |
| **working folder** | The folder `tmp/` at the engine root, in git with its own README while its contents never are, holding the working files of runs and never a source of truth. | `tmp/README.md`, `projects/forge/10-intent.md` |
| **working method** | One of the named ways a working conversation runs, such as the walkthrough or step by step, applying whenever its situation arises. | `CLAUDE.md` (Working methods) |
| **write** | The principal's word that ends a round, on which Claude reflects the round back and, on his yes, writes everything agreed as one version. | `.claude/skills/walkthrough/SKILL.md`, `CLAUDE.md` (Prime directives) |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
