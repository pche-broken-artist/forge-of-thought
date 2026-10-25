---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 3db56ddf0bf1a171
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

This glossary lists the terms of Forge of Thought, each in one line
with the file that defines it. It is for the user who works with the
forge, the extender who adds to it and the evaluator who wants to
understand it. The principal (the person whose thinking is being
forged) and Claude (the AI assistant that works with him) are the two
roles most terms refer to. A term stands where it sorts by its first
word; a term with two senses has one row per sense. For the forge
told in prose, read the page linked under See also.

## Terms

| Term | Meaning | Defined in |
|---|---|---|
| archive | A file that keeps an older record as it stood, immutable and still read: `<file>.history.archive.md` holds a history table from before the log, `ledger.archive.md` the hand-kept ledger at the migration. | `CLAUDE.md`, Versioning & status; `templates/ledger.md` |
| artefact | A document of the chain, composed by the principal with Claude and versioned. | `CLAUDE.md`, Document kinds |
| assignment | `20-assignment.md`, the layer that carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| branch | A line of work in git, voluntary and left to git, on which a contributor saves his work for the integrator to merge. | `CLAUDE.md`, Persistence (git); `projects/forge/10-intent.md`, Operating environment |
| BRD | `30-brd.md`, the layer of business requirements that breaks its parent into rules, behaviour and qualities the stakeholders can review and the delivery can estimate. | `.claude/skills/forge/states/brd.md`; `templates/brd.md` |
| brief | `00-brief.md` or `00-brief-<name>.md`, the principal's own text of one whole of thinking (what he wants and why), rough on purpose and mined into the intent. | `.claude/skills/forge/states/brief.md` |
| bundle | A set of related files stored as `sources/<slug>/`, counted as one source with one ledger entry and catalogued by its own `00-INDEX.md`. | `CLAUDE.md`, Document chain |
| business requirement | An item of a BRD with the prefix `BR`: one testable rule of the business that cites the parent it carries. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/brd.md` |
| card | One question of a research plan, answered by one kind of evidence from one kind of source. | `.claude/skills/research/SKILL.md`; `templates/research-plan.md` |
| challenge | One result of a challenger about the substance of the thinking, with the prefix `CHL`. | `CLAUDE.md`, ID scheme; `.claude/skills/challenger-contract/SKILL.md` |
| challenger | The isolated reviewer that tests the substance of the thinking through one persona, never the quality of the documents. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md` |
| check | An isolated reviewer that verifies mechanical conformance with the conventions, one concern per check, never substance or quality. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/check-contract/SKILL.md` |
| citation check | The run of `scripts/forge-cite.py` that opens every URL a research note cites before the note is filed. | `scripts/forge-cite.py`, its header; `projects/forge/10-intent.md`, Research |
| Claude | The AI assistant that acts as the principal's cognitive extension: it owns structure, order, process discipline and document hygiene, and proposes but never decides. | `CLAUDE.md`, Roles |
| contract | The skill that owns what every member of one kind of agent shares: conduct, isolation, subject, way of working and the shape of the output. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| contributor | A person who works on a branch of a hosted project and saves it, leaving the merge to the integrator. | `projects/forge/10-intent.md`, Operating environment |
| critic | The isolated reviewer that judges the quality of the documents through one lens, never the substance of the thinking. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| decision | A record with the prefix `DEC` in the append-only `decisions.md`: one decision of the principal with its reason. | `templates/decisions.md` |
| definition | The state file `.claude/skills/forge/states/<state>.md` of an artefact, which says what the artefact is, how it is found and which rules it keeps, in seven blocks. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| dependency (of a BRD) | An item of a BRD with the prefix `DEP`: something the BRD relies on outside itself. | `.claude/skills/forge/states/brd.md`; `templates/brd.md` |
| dependency (of a project) | A citation of another project's document, a library's or any other's, registered in the ledger's Dependencies table without a version. | `templates/ledger.md` |
| derived (page) | A page that puts together what no single file says, from evidence in several files. | `.claude/skills/docs-contract/SKILL.md` |
| derived file | A file made for a reader (a render, the README, the documentation, a published file) that is kept in git, made only on `main`, taken as `ours` at a merge and made again. | `projects/forge/10-intent.md`, Operating environment |
| disconfirming query | One search per card, written to find the opposite of what is expected. | `templates/research-plan.md`; `.claude/skills/research/SKILL.md` |
| document | Every file of a project, each of one kind that says what it is, who writes it and how it behaves. | `CLAUDE.md`, Document kinds |
| documentation | The generated pages of one topic each in `docs/`, with their index, for the user, the extender and the evaluator. | `CLAUDE.md`, Document chain; `.claude/skills/document/SKILL.md` |
| documentation map | `docs-map.md` beside the owning project's ledger: one entry per page with everything the page is made from, never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md` |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, the conversation being only its medium. | `projects/forge/10-intent.md`, Elicitation |
| engine (of the forge) | The forge's own repository of commands, skills, agents, templates and scripts, which carries no instance fact and does not know the projects. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Operating environment |
| engine (of another model family) | A model of another family reached over its own command-line tool, one row of the engine table in `scripts/forge-engine.py`, such as `antigravity`. | `scripts/forge-engine.py`, its header |
| envelope | The JSON answer an engine returns for one run, saved beside the packet as `envelope.json` for inspection. | `scripts/forge-engine.py`, its header |
| explanation | A kind of page that says what a thing is, how it works and why, never a procedure or a listing. | `.claude/skills/docs-contract/SKILL.md` |
| extract | The Markdown conversion of a binary, made by `scripts/doc2md.py` on the principal's word, which then is the source. | `CLAUDE.md`, Document chain; `.claude/skills/ingest/SKILL.md` |
| fact | An item of the intent with the prefix `FCT`: what is the case, on the principal's word or on a source cited to its file, never a stance. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Structure and style of an assignment |
| finding | A result of a critic (document quality) or of a check (conformance), with the prefix `FND`; the word is used for a reviewer's result only. | `CLAUDE.md`, ID scheme; `.claude/skills/docs-contract/SKILL.md` |
| format file | The file made from a render in the format its recipe names, which follows the render's name and may be sent to the engine's public folder. | `.claude/skills/render/SKILL.md`; `projects/forge/10-intent.md`, Growth path |
| genre | A kind of recipe composed through an interview by `/recipe <genre>`, from the skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md`, Document chain |
| growing bundle | A bundle of one origin that keeps arriving, born at its first file by `/ingest --bundle <name>` and grown file by file. | `.claude/skills/ingest/SKILL.md` |
| guarded command | A command that changes files the moment it runs, which the harness keeps Claude from starting on its own judgement. | `projects/forge/10-intent.md`, Operating environment |
| harness | The program Claude runs in, which loads its skills and agents and enforces the principal's word where it can. | `projects/forge/10-intent.md`, Operating environment |
| history companion | `<file>.history.md`, the append-only log beside every versioned document, one record per change. | `CLAUDE.md`, Versioning & status; `templates/history.md` |
| hook's ask | The moment the git hook `scripts/hook-git.py` puts one of the few commands that finish the step of a conflict to the principal and runs it on his yes. | `CLAUDE.md`, Persistence (git) |
| how-to | A kind of page that carries what the reader does, step by step, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md` |
| immutable | Never edited once registered or created, as sources, reviews, challenges, research and closed threads are, by a process rule and not by git. | `CLAUDE.md`, Versioning & status |
| independence of engines | The measure, never an assumption, of how many URLs and sentences two engines' notes of one card share, counted by `scripts/forge-cite.py --independence`. | `scripts/forge-cite.py`, its header; `projects/forge/10-intent.md`, Research |
| index (of the documentation) | `docs/README.md`, derived by a script from the documentation map, listing every page and each reader's path through them. | `.claude/skills/document/SKILL.md`; `.claude/agents/docs-planner.md` |
| instance | One installation of the forge, whose facts live in `CLAUDE.local.md` at the engine root. | `CLAUDE.md`, What this workspace is; `.claude/skills/docs-contract/SKILL.md` |
| instance fact | Whatever `CLAUDE.local.md` and the assistant's memory carry (who the principal is, the conversation language, the author's handle), which never enters a report or a page. | `projects/forge/10-intent.md`, Operating environment; `CLAUDE.md`, Isolated reviewers |
| integrator | The maintainer of a hosted project, typically the principal, who merges the contributors' branches. | `projects/forge/10-intent.md`, Operating environment |
| intent | `10-intent.md`, the working document of the consolidated current state of what the principal holds: positions, facts, threads and rejections with their reasons. | `.claude/skills/forge/states/intent.md`; `projects/forge/10-intent.md`, Document chain |
| isolated subagent | A subagent that never sees the working conversation and reads every input from disk in its own run. | `CLAUDE.md`, Isolated reviewers |
| isolation | The rule that a reviewer or a documentation agent sees nothing of the conversation, reads its inputs from disk and puts no instance fact into what it writes. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/docs-contract/SKILL.md` |
| kind | Of a project, `thought` or `library` in its project file; of a document, one of the kinds the table of document kinds names. | `templates/project.md`; `CLAUDE.md`, Document kinds |
| layer | An artefact of the chain below the intent, taken by a project as it needs it; a layer the project does not have is not missing. | `CLAUDE.md`, Document chain |
| ledger | `ledger.md`, the single source of truth for state, made at read time by `scripts/forge-ledger.py` and never kept in git. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| lens | One specialisation of the critic, an agent file `critic-<lens>` of its own. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| Lens section | The one part of a reviewer's agent file that is its own, which specialises its contract and never replaces it. | `CLAUDE.md`, Isolated reviewers |
| library | A project of kind `library`: material shared across projects, with no chain, whose README is a catalogue of what it holds. | `CLAUDE.md`, Repository layout |
| made at read time | Built by a script from the documents whenever it is read and never kept in git, as the ledger is. | `projects/forge/10-intent.md`, Versioning and state |
| major | An integer version of the forge intent that closes a set of features the principal names and passes every check, both critic lenses and one challenge before its tag. | `projects/forge/10-intent.md`, Versioning and state |
| Map | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area was considered, never a questionnaire. | `projects/forge/10-intent.md`, Elicitation |
| merge driver `ours` | The git setting that keeps one's own side of a derived file at a merge, so that the file can be made again. | `CLAUDE.md`, Persistence (git); `projects/forge/10-intent.md`, Operating environment |
| migration | The run of `/migrate [slug]` through `scripts/forge-migrate.py` that brings a project, once and on one clone, to the shape of a release that changed the shape of files. | `.claude/skills/migrate/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |
| mined | Said of a brief whose substance has been carried into the intent, recorded as `pending`, `partial`, `mined` or `dropped`. | `.claude/skills/forge/states/brief.md`; `templates/ledger.md` |
| mirrored (page) | A page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md` |
| non-functional requirement | An item of a BRD with the prefix `NFR`: a quality by category, its value given by the stakeholders or held open as an open question. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/brd.md` |
| packet | A folder under `tmp/` whose `packet.md` is the whole context of one agent's run: the card, the agent's brief, the note's shape and the attached notes. | `.claude/skills/research/SKILL.md`; `scripts/forge-engine.py`, its header |
| page | One page of the documentation, of one topic and one kind, generated and never a source of truth. | `CLAUDE.md`, Document kinds; `.claude/skills/docs-contract/SKILL.md` |
| parent of an item | The requirement of the assignment (`REQ`) or the position of the intent (`POS`) that a business requirement or a use case carries and cites. | `.claude/skills/forge/states/brd.md` |
| persona | One specialisation of the challenger, an agent file `challenger-<persona>` of its own. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md` |
| perspective | A standpoint from which a research topic is looked at, listed in the plan with the cards that serve it. | `templates/research-plan.md` |
| pinned fact | A fact of a project that no file owns yet (a prerequisite, an install line, the public home), kept in the section "Pinned facts (not rendered)" of the readme recipe. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| plain file | The `.docx`, `.pptx`, video or player file a script makes from a render, deterministically, where the recipe names a format. | `CLAUDE.md`, Document chain; `.claude/skills/render/SKILL.md` |
| plan | The head of a research bundle, `00-plan.md`: purpose, perspectives, assumptions, what is left out, the cards and the agents, confirmed by the principal before anything is searched. | `.claude/skills/research/SKILL.md`; `templates/research-plan.md` |
| player page | `docs/videos/index.html`, written anew by `scripts/md2video.py` from `templates/html-player.html` whenever a file enters the public folder. | `projects/forge/10-intent.md`, Growth path |
| position | An item of the intent with the prefix `POS`: what the principal holds or wants, why, and what it comes from. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Document chain |
| prime directive | One of the ten numbered rules at the head of `CLAUDE.md` that hold for all of Claude's work. | `CLAUDE.md`, Prime directives |
| primary render | The render in the first language a recipe declares, from which the others are translated. | `.claude/skills/render/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| principal | Whoever's thinking is being forged, who supplies ideas, answers and decisions and has the final authority on all content. | `CLAUDE.md`, Roles |
| profile | A copy of the user's settings made for one run of another engine, with the forge's tree and the shell denied and the web allowed, kept in the run folder. | `scripts/forge-engine.py`, its header |
| project | A directory `projects/<slug>/` of kind `thought` or `library`, usually a git repository of its own that the engine does not know. | `CLAUDE.md`, Repository layout |
| project file | `project.md`, written once at a project's creation, holding its slug, its kind and its language. | `templates/project.md` |
| project outside git | A project whose directory is not the top of a git repository, on which the forge runs no git; a property, not a defect. | `CLAUDE.md`, Persistence (git) |
| provenance | The front-matter a render opens with: the project, the recipe with its version, the date and every input with its version. | `.claude/skills/render/SKILL.md` |
| provenance map | The tool of a joint pass that maps every group to its items and the items to what they came from, with what landed nowhere and what has no source; it is not part of the artefact. | `.claude/skills/forge/states/assignment.md` |
| published companion | `published/<recipe>.md`, the provenance of a published file, from which the ledger computes whether it is `current` or `stale`. | `.claude/skills/publish/SKILL.md` |
| published file | The designed `.pptx` or `.docx` made from a render through a model by `/publish`, only on the principal's command. | `.claude/skills/publish/SKILL.md` |
| pull | The command `/pull`, which says each repository's state against its origin (up to date, behind, ahead, diverged, no origin, not under git) and pulls only one that is clean and behind. | `.claude/skills/pull/SKILL.md` |
| quick and deep | The two depths of a research: `--quick` is one card on the session model filed as one note, `--deep` a plan of several cards filed as a bundle with a synthesis. | `.claude/skills/research/SKILL.md` |
| recipe | `recipes/<recipe>.md`, the versioned file of a render's inputs, audience, instructions and output template. | `CLAUDE.md`, Document chain |
| recipients | Those who receive an assignment: teams, colleagues or the principal's future self. | `CLAUDE.md`, What this workspace is |
| record | One line of a history companion: date, version, author, subject, kind, reason and, where it has them, `Action` and `Was`. | `templates/history.md` |
| record of state | A record that carries the current version without raising it and says a state: a brief mined, a finding or challenge settled, a work product's state. | `templates/history.md`; `projects/forge/10-intent.md`, Versioning and state |
| reference | A kind of page that states facts in the structure of what it mirrors, free of interpretation. | `.claude/skills/docs-contract/SKILL.md` |
| registration of the merge driver | The once-per-machine entry of the merge driver `ours` into the global git configuration, made by `/setup` through `scripts/forge-config.py`, without which a clone falls back to a conflict. | `CLAUDE.md`, Persistence (git) |
| rejected direction | An item of the intent with the prefix `REJ`: a direction dropped, with the reason. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md` |
| release | The command `/release`, which from `main` only runs its checks, re-renders the README and the release notes and saves with the release message and tag. | `CLAUDE.md`, Persistence (git) |
| render | An audience-specific output generated from the chain by `/render` from its recipe, never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain; `.claude/skills/render/SKILL.md` |
| Reports | The section of the ledger in which its script says what the merged files cannot, such as an ID defined twice. | `templates/ledger.md` |
| research | A document kind: a durable answer to one question, immutable, made by `/research`. | `CLAUDE.md`, Document kinds |
| research bundle | `research/YYYY-MM-DD-<topic>/`, with the plan and the synthesis in `00-plan.md` at its head and one note per card per engine. | `.claude/skills/research/SKILL.md` |
| research note | The answer of one engine to one card, in the shape of `templates/research.md`, immutable from its filing. | `templates/research.md` |
| resource index | The `00-INDEX.md` of every `sources/` and `research/` directory: a light catalogue in fixed free-text fields that tracks nothing. | `CLAUDE.md`, Document chain |
| Role | The free-text field of a source's index entry that says what the source is for, the principal's word, asked before the entry is written. | `.claude/skills/ingest/SKILL.md`; `CLAUDE.md`, Document chain |
| roster of areas | The instance's list of the areas of the enterprise a BRD must consider and which of them are mandatory, a library document cited by path, or `Roster: none`. | `.claude/skills/forge/states/brd.md`; `templates/brd.md` |
| round | One working conversation whose agreed answers are carried and written once at its end, on the principal's word, as one version. | `CLAUDE.md`, Prime directives; `.claude/skills/walkthrough/SKILL.md` |
| run folder | `tmp/research/YYYY-MM-DD-<topic>/`, which holds the packets, envelopes, profiles, held notes and citation reports of one research run, kept for inspection. | `.claude/skills/research/SKILL.md`; `scripts/forge-engine.py`, its header |
| save | The command `/save`, which runs its check and then commits and pushes on the branch checked out; `--quick` leaves the check out. | `CLAUDE.md`, Persistence (git) |
| screenplay | A recipe genre that renders a terminal conversation as a title card and timed scenes with captions, made into a video or player events by `scripts/md2video.py`. | `projects/forge/10-intent.md`, Document chain |
| second engine | An engine of another model family run beside the session model in a deep research, named by `--engine <name>`, which reviews the draft plan and takes every card. | `.claude/skills/research/SKILL.md`; `projects/forge/10-intent.md`, Research |
| session | One run of Claude with the principal, whose conversation lives only until it ends; `/end` closes it by saying what would be lost. | `CLAUDE.md`, Persistence (git); `.claude/skills/docs-contract/SKILL.md` |
| session model | The model of the session, on which the whole forge runs, the reviewers included. | `CLAUDE.md`, Isolated reviewers |
| shape of a project | The set of marks, one per migration step, by which the migration script recognises whether a project is in the shape of a release. | `.claude/skills/migrate/SKILL.md`; `templates/project.md`; `projects/forge/10-intent.md`, Operating environment |
| solution design | `40-solution-design.md`, the layer that says how the things wanted are realised, part by part, with the choices they rest on. | `.claude/skills/forge/states/solution-design.md` |
| source | External input as it arrived, kept in `sources/`, immutable from its registration and of one form. | `CLAUDE.md`, Document kinds and Document chain |
| specification | `work/<name>.spec.md`, the versioned way and why of a work product: its task, its inputs cited, its method, its assumptions, what is open and how the file is made. | `.claude/skills/work/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| stale | Said of a render whose provenance cites a version that differs from the file's current one or a file that no longer exists, and of a published file whose render is newer. | `.claude/skills/render/SKILL.md`; `templates/ledger.md` |
| state render | `renders/state.md`, the ledger as a render, written by `/release` on `main`. | `CLAUDE.md`, Repository layout |
| step of a conflict | The way a conflict left standing by `forge-save` is settled: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording and the finishing commands run on the hook's ask. | `CLAUDE.md`, Persistence (git) |
| stop rule | The rule of a card for when searching ends: nothing new from a differently-worded query and a primary source for every perspective of the card, or the opening budget spent. | `templates/research-plan.md`; `templates/research.md` |
| subagent | A separate agent Claude launches for one job, which returns its report and carries `CLAUDE.md` and the instance file. | `CLAUDE.md`, Isolated reviewers |
| synthesis | Claude's section of `00-plan.md`, made from the notes alone: completeness card by card, the engines' answers side by side, the unexpected and the not found gathered, and its own view last and apart. | `templates/research-plan.md`; `.claude/skills/research/SKILL.md` |
| tag | A name given to a commit; `/release` says which release receives `v<major>`, and any other tag is the principal's request. | `CLAUDE.md`, Persistence (git) |
| template | A canonical skeleton in `templates/` that says what comes out. | `CLAUDE.md`, Templates and Document chain |
| thought project | A project of kind `thought`, which carries the chain. | `CLAUDE.md`, Repository layout; `templates/project.md` |
| thread | An item of the intent with the prefix `THR`: one open matter, naming the artefact it concerns and its origin and carrying the working debate until it is settled. | `.claude/skills/forge/states/intent.md`; `projects/forge/10-intent.md`, Document chain |
| thread file | `threads/THR.NNNN.md`, one file per thread with `id`, `concerns`, `origin` and `status` in its header, freely rewritten while open and immutable once closed. | `templates/thread.md`; `.claude/skills/forge/states/intent.md` |
| touched area | An area of the roster that a BRD finds or knowingly finds not to apply, a mandatory one never left silent. | `.claude/skills/forge/states/brd.md` |
| translation | A render in a further language of a recipe's `languages:`, made from the primary render in the same run, scene for scene and line for line. | `.claude/skills/render/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports, which the writer leaves out. | `.claude/agents/docs-planner.md` |
| use case | An item of a BRD with the prefix `UC`: behaviour agreed as a sequence at user-goal level, its steps in the active voice. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/brd.md` |
| verdict | The principal's answer to one item: accept, modify, question, reject or park, offered by the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, with obsolete typed in full. | `.claude/skills/walkthrough/SKILL.md` |
| Verdict line | The line of a decision that records its ruling on a finding or a challenge: rejected, parked until a named matter, or obsolete. | `templates/decisions.md` |
| Waiting on principal | The section of the ledger that lists by rule what waits on the principal: open threads, open questions he owns, open findings and challenges, and the parked ones. | `templates/ledger.md` |
| walkthrough | The working method in which a list of items needing the principal's decision is worked one item per message, in order of weight, each closed with the verdict line. | `.claude/skills/walkthrough/SKILL.md`; `CLAUDE.md`, Working methods |
| way of merging | One of the three ways each file of a project is merged (text, derived, or immutable and unique), told to git by the project's `.gitattributes`. | `projects/forge/10-intent.md`, Operating environment |
| work product | An output of a project made with work of its own, neither artefact nor render: a file in `work/` with its specification beside it. | `.claude/skills/work/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| working folder | `tmp/` at the engine root, the forge's one working folder, in git with its README and `.gitignore` while its contents never are, and never a source of truth. | `tmp/README.md`; `projects/forge/10-intent.md`, Operating environment |
| working method | One of the named ways a working conversation runs, applied whenever its situation arises and never a command. | `CLAUDE.md`, Working methods |
| write | The principal's word that ends a round, on which Claude reflects the round back and writes it to files on his yes. | `.claude/skills/walkthrough/SKILL.md`; `CLAUDE.md`, Prime directives |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
