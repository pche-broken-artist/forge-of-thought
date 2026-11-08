---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 6cf827ac22968970
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0330
  - projects/forge/10-intent.md#POS.0790
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1170
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
  - projects/forge/10-intent.md#POS.1920
  - projects/forge/10-intent.md#POS.1930
  - projects/forge/10-intent.md#POS.1940
  - projects/forge/10-intent.md#POS.1960
  - projects/forge/10-intent.md#POS.1970
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/10-intent.md#POS.1990
  - projects/forge/10-intent.md#POS.2010
  - projects/forge/10-intent.md#Elicitation
  - projects/forge/40-solution-design.md#SOL.0500
  - projects/forge/40-solution-design.md#SOL.0520
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/user-stories.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/pull/SKILL.md
  - .claude/skills/end/SKILL.md
  - .claude/skills/work/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/skills/test/SKILL.md
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
  - templates/user-stories.md
  - templates/research.md
  - templates/research-plan.md
  - templates/recipe-readme.md#Pinned facts (not rendered)
  - scripts/forge-engine.py
  - scripts/forge-cite.py
  - scripts/forge-status.py
  - scripts/md2video.py
  - scripts/hook-walkthrough.py
  - tmp/README.md
---

# Glossary

The glossary is the list of every term the forge uses, each in one
line, with the file that defines it. It is for the user who meets a
word on another page, for the extender who needs the exact name of a
thing before changing it, and for the evaluator who reads about the
forge without running it. The terms stand in groups by area, and
within a group in the order a reader usually meets them. The column
"Defined in" names the file that owns the term, with its section
where the file is long; a term that no file defines in one sentence is
marked "defined from use", and its line is drawn from the files named
beside it. What the forge is as a whole is told in prose on the page
[What the forge is and is not](../about/what-it-is-and-is-not.md).

## The people and the machine

| Term | In one line | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: he supplies ideas, answers and decisions and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is handed to, teams, colleagues or the principal's future self, who act on it without the principal in the room. | `CLAUDE.md`, What this workspace is; `.claude/skills/forge/states/assignment.md`, Aim |
| Claude as cognitive extension | Claude is the principal's cognitive extension: it owns structure, order, process discipline and document hygiene, and it proposes, never decides. | `CLAUDE.md`, Roles |
| Claude Code | The agent for the command line in which the forge runs; its slash commands, skills, agents and hooks are the mechanisms, and the forge is what they are told. | `CLAUDE.md`, What this workspace is |
| session | Defined from use: one conversation of the principal with Claude in the command line, which keeps nothing by itself, since what is in a file survives it and what lives only in the conversation does not, which `/end` says. | `projects/forge/10-intent.md`, Versioning and state; `.claude/skills/end/SKILL.md`; `.claude/skills/docs-contract/SKILL.md`, The voice |
| session model | The one model the whole forge runs on, `model: inherit` in every agent, set in `.claude/settings.local.json`; speed is bought with context, never with a weaker reviewer. | `CLAUDE.md`, Isolated reviewers and Repository layout |
| harness | Defined from use: the tool around Claude, Claude Code with its permission system and its hooks, which enforces the principal's word where it can; a hook is context, the nearest thing to a wall the harness offers. | `projects/forge/10-intent.md`, Working methods and Operating environment; `projects/forge/40-solution-design.md`, The wall; `.claude/skills/docs-contract/SKILL.md`, The voice |
| instance | One installation of the forge: a clone of the engine with its `CLAUDE.local.md`, its principal, its conversation language and the user's own git configuration. | `CLAUDE.md`, What this workspace is; `.claude/skills/docs-contract/SKILL.md`, The voice |
| instance fact | Who the principal is, the conversation language, the handle he signs with, and every name, address and host: what lives in `CLAUDE.local.md` or the user's own configuration and never in the engine or in a report. | `CLAUDE.md`, What this workspace is and Isolated reviewers; `projects/forge/10-intent.md`, Operating environment |
| integrator | The maintainer of a hosted project, typically the principal, who merges a contributor's branch: on the server where the merge request has no conflict, on his own clone through the step of a conflict where it has. | `projects/forge/10-intent.md`, Operating environment |
| contributor | One who works on a branch of a project and saves it with `/save`, the merge being the integrator's; of the engine, one who changes a script with its test and sends a pull request. | `projects/forge/10-intent.md`, Operating environment and Review; `CLAUDE.md`, Persistence |

## Documents and the chain

| Term | In one line | Defined in |
|---|---|---|
| document | The word for every file of a project; every document has one kind. | `CLAUDE.md`, Document kinds |
| kind | What a document is, who writes it, whether it is versioned and how it behaves, one kind per document; also the kind of a project, `thought` or `library`. | `CLAUDE.md`, Document kinds; `templates/project.md` |
| artefact | A document of the chain, composed by the principal with Claude, versioned and rewritten freely; the word is reserved for the chain. | `CLAUDE.md`, Document kinds |
| layer | One artefact of the chain below the intent, taken as the project needs it, none a condition of another; a layer a project does not have is not missing. | `CLAUDE.md`, Document chain and Ledger |
| definition | The state file of an artefact, `.claude/skills/forge/states/<state>.md`, which says what the artefact is, how it is found and owns its rules, in seven blocks: Target, Inputs, Aim, Partner, Map, Instruments, Course. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| template | A skeleton in `templates/`, which says what comes out; an artefact's template is paired with its definition. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area was consciously considered; neither the headings of the document nor a questionnaire. | `projects/forge/10-intent.md`, Elicitation |
| brief | `00-brief.md` or `00-brief-<name>.md`, the principal's text of one whole of thinking, rough on purpose, free of IDs, mined into the intent when he says so. | `.claude/skills/forge/states/brief.md` |
| intent | `10-intent.md`, the working document: the briefs chiselled into what the principal holds, as positions, facts, threads and rejections, rewritten for coherence each round and never finished. | `.claude/skills/forge/states/intent.md` |
| position | An item of the intent, prefix POS, saying what the principal holds and why, naming what it comes from, dated once. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Document chain |
| fact | An item of the intent, prefix FCT: what is the case, as the principal states it or as a source states it, not a stance; a source's fact cites its file, and verification is never demanded. | `CLAUDE.md`, ID scheme |
| thread | An item of the intent, prefix THR: one open matter, carrying its origin (the principal's word, a document by path or Claude's synthesis) and the working debate until it is settled. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| thread file | `threads/THR.NNNN.md`, one file per thread, its header `concerns`, `origin` and `status`, freely rewritten while open and immutable once closed. | `.claude/skills/forge/states/intent.md`, Threads and files; `templates/thread.md` |
| rejected direction | An item of the intent, prefix REJ: a direction dropped, with the reason it was dropped. | `CLAUDE.md`, ID scheme |
| assignment | `20-assignment.md`, the in-scope substance of the intent carried to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| obligation in the indicative | The form of every requirement: shall / shall not in English, in a full sentence, never a conditional, a permission or a wish in any language. | `.claude/skills/forge/states/assignment.md`, Requirement style; `projects/forge/10-intent.md`, Structure and style of an assignment |
| solution design | `40-solution-design.md`: how the things wanted are realised, part by part as SOL items with the choices they rest on, kept current and read by whoever realises the solution. | `.claude/skills/forge/states/solution-design.md` |
| prefix of two or three letters | The letters before the dot of an ID, `PREFIX.NNNN`, which say what an item is (POS, THR, REQ, BR, UC, US among them); a type is never told by a number. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Structure and style of an assignment |
| immutable | Never edited after it exists: a review, a challenge, a research note from its creation, a source from its registration, a closed thread; a process rule, not a git mechanism. | `CLAUDE.md`, Versioning & status and Persistence |
| mined | Of a brief: absorbed into the intent whole by whole, the ledger's Briefs table showing `pending`, `partial`, `mined` or `dropped` from the mining record. | `.claude/skills/forge/states/brief.md`, Aim; `templates/ledger.md`, Briefs |

## The BRD and the user stories

| Term | In one line | Defined in |
|---|---|---|
| BRD | `30-brd.md`, the business requirements: the parent broken into rules, behaviour and qualities that the stakeholders can review, the delivery can estimate and the solution design can start from. | `.claude/skills/forge/states/brd.md` |
| business requirement | An item of the BRD, prefix BR: one rule of the business, testable, one sentence, citing the REQ or POS it carries. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/brd.md`, Requirement style |
| use case | An item of the BRD, prefix UC: behaviour agreed as a sequence at user-goal level, its steps in the active voice and the present tense. | `CLAUDE.md`, ID scheme; `templates/brd.md`, Use cases |
| dependency (of a BRD) | An item of the BRD, prefix DEP: what the BRD relies on outside itself, a system, a project or a document, with the role that brings it. | `CLAUDE.md`, ID scheme; `templates/brd.md`, Dependencies |
| non-functional requirement | An item of the BRD, prefix NFR: a quality by category, its value the stakeholders' or a TBC with an owner, never a figure from the skeleton. | `CLAUDE.md`, ID scheme; `templates/brd.md`, Qualities |
| parent of an item | The item of the layer above that a BR, a UC or a story traces to: a REQ of the assignment, or a POS of the intent where the project has no assignment. | `.claude/skills/forge/states/brd.md`, Inputs; `.claude/skills/forge/states/user-stories.md`, Inputs |
| roster of areas | The areas of the enterprise a BRD must consider and which of them are mandatory, a library document of the instance cited by path; a project with no enterprise around it says `Roster: none`. | `.claude/skills/forge/states/brd.md`, Inputs; `templates/brd.md`, Touched areas of the enterprise |
| touched area | An area of the roster found in the BRD's items, or found not to apply with the reason; a mandatory area is never silent. | `.claude/skills/forge/states/brd.md`, Map; `templates/brd.md`, Touched areas of the enterprise |
| provenance map | A tool of the recast, not part of the artefact: group → items → the positions they came from, with the in-scope positions that landed nowhere and the items with no position. | `.claude/skills/forge/states/assignment.md`, Course |
| user story | An item of `35-user-stories.md`, prefix US: one function as the one who uses it meets it, behaviour seen from outside with its acceptance criteria, citing the BR, NFR, UC, DEP or POS it serves. | `.claude/skills/forge/states/user-stories.md`, Story style |
| acceptance criterion | What happens in the usual course of a story, in the indicative, present tense, one behaviour per bullet. | `.claude/skills/forge/states/user-stories.md`, Story style |
| edge case | A situation at the border of a story's behaviour, a failure, a missing datum, a change during use, written as "situation → what happens". | `.claude/skills/forge/states/user-stories.md`, Story style |
| Reference of a story | The one part every story has: the BR, NFR, UC or DEP it serves, or in a small change without a BRD the POS. | `.claude/skills/forge/states/user-stories.md`, Story style; `templates/user-stories.md` |
| Story style | The rules of wording of a story: a free sentence of who, what and why, criteria in the indicative, no vague word, no technical solution, priority or estimate, the labels fixed in English. | `.claude/skills/forge/states/user-stories.md`, Story style |
| the cut (of the stories) | What Claude returns first when the stories are handed over: the name of every story with a short description and the items of the parent no story serves, agreed before any story is drafted. | `.claude/skills/forge/states/user-stories.md`, Course |
| the cut (of the parent) | In the assignment's and the BRD's Map, what of the parent is carried now, what is expressly later and what is out of scope. | `.claude/skills/forge/states/assignment.md`, Map; `.claude/skills/forge/states/brd.md`, Map |
| the export of the stories | A render of the genre `user-stories-export`, one heading per story with its parts on lines of their own, leaving out every reference to a POS; a render, never the artefact. | `.claude/skills/forge/states/user-stories.md`, Instruments; `projects/forge/10-intent.md`, Document chain |

## Finding an artefact and deciding

| Term | In one line | Defined in |
|---|---|---|
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds; the conversation is its medium, the interview one instrument, research and sources others. | `projects/forge/10-intent.md`, Elicitation |
| working method | A named way a working conversation runs (Walkthrough, Step by step, In pieces, Reflect back among them), not a command, applying whenever its situation arises. | `CLAUDE.md`, Working methods |
| prime directive | One of the ten rules at the head of `CLAUDE.md` that hold over everything Claude does in the forge, such as asking when unsure and writing once per round. | `CLAUDE.md`, Prime directives |
| walkthrough | Any list of items needing the principal's decision worked one item per message, in order of weight, each item closed with the verdict line and the verdicts carried to one write at the round's end. | `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item, given on the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`: accept, modify, question, reject, park, or obsolete; a single letter is a whole message. | `.claude/skills/walkthrough/SKILL.md`, The verdict |
| round | One working conversation, in which what is agreed is carried and reflected back, written once at its end on the principal's word, one version bump for the whole. | `CLAUDE.md`, Prime directives and Working methods |
| write | The principal's word that ends a round: Claude reflects the whole round back and, on his yes, writes everything carried as one version with its records. | `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write; `CLAUDE.md`, Working methods |

## History, records and the ledger

| Term | In one line | Defined in |
|---|---|---|
| history companion | `<file>.history.md` beside every versioned document, an append-only log of one record per change; the body is the current state, the companion the record. | `CLAUDE.md`, Versioning & status; `templates/history.md` |
| record | One line of a history: date, version, author, subject, kind (`created`, `changed`, `closed`, `removed`, `approved`), reason, and `Action` and `Was` where the record has them. | `templates/history.md` |
| record of state | A record that carries the current version and does not raise it: the mining of a brief, a finding or a challenge settled, a work product's state. | `templates/history.md`; `projects/forge/10-intent.md`, Versioning and state |
| archive | `<file>.history.archive.md`, a history table written before the log, moved as it stands and immutable from then on; and `ledger.archive.md`, the hand-kept ledger as it stood at the migration. | `CLAUDE.md`, Versioning & status and Repository layout; `templates/ledger.md` |
| ledger | `ledger.md`, the single source of truth for state, made at read time by `scripts/forge-ledger.py` from the documents and never in git. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| made at read time | Built by a script from the records whenever it is read, so that nobody writes a row and the file is never a thing to merge. | `CLAUDE.md`, Ledger; `projects/forge/10-intent.md`, Versioning and state |
| Waiting on principal | The ledger's section of what waits on the principal, a rule and never a hand-kept list: the open threads, the TBCs he owns, the open findings and challenges, under Parked the parked ones. | `templates/ledger.md`, Waiting on principal |
| Reports | The ledger's section of what the merged files cannot say, found by the script: an ID defined twice, a closed thread touched by a later commit, a THR cited with neither a file nor a closed record. | `templates/ledger.md`, Reports |
| decision | A record of `decisions.md`, prefix DEC: the principal's decision with its reason, append-only, rejected findings and challenges among them. | `templates/decisions.md`; `CLAUDE.md`, ID scheme |
| Verdict line | The line of a decision that rules on a finding or a challenge, `<ID> rejected | parked until <what> | obsolete`, one line per ID; the ledger reads the state from it. | `templates/decisions.md` |

## Sources and research

| Term | In one line | Defined in |
|---|---|---|
| source | External input as it arrived, in `sources/`, immutable from its registration, one form each: text, or a functional binary. | `CLAUDE.md`, Document chain, External inputs |
| bundle | A set of related files in `sources/<slug>/`, counting as one source with one ledger entry and catalogued by its own `00-INDEX.md`. | `CLAUDE.md`, Document chain, External inputs; `.claude/skills/ingest/SKILL.md` |
| growing bundle | A bundle of one origin that keeps arriving, grown file by file through `/ingest --bundle <name>`, each file immutable from its own registration. | `.claude/skills/ingest/SKILL.md`, step 1 |
| extract | The Markdown made from a binary by `scripts/doc2md.py`, which then is the source, on the principal's explicit word. | `.claude/skills/ingest/SKILL.md`, step 3; `CLAUDE.md`, Document chain, External inputs |
| resource index | `00-INDEX.md` of `sources/` and of `research/`, a light catalogue of what exists and what it is for, freely rewritten, an automatic input of no command. | `CLAUDE.md`, Document chain, External inputs |
| Role | The free-text field of a source's index entry saying what the source is for, the principal's word, asked before the entry is written. | `.claude/skills/ingest/SKILL.md`, step 4; `CLAUDE.md`, Document chain, External inputs |
| research | A durable answer to one question about the world outside, in `research/`, immutable; a research of several questions is a bundle. | `CLAUDE.md`, Document kinds; `.claude/skills/research/SKILL.md` |
| research note | One card, one engine, one note, in the shape of `templates/research.md`, its answer in a few sentences placed first. | `templates/research.md` |
| research bundle | `research/YYYY-MM-DD-<topic>/`, with the plan and the synthesis at its head in `00-plan.md` and one note per card per engine, `<card>.<engine>.md`. | `.claude/skills/research/SKILL.md`, Target |
| plan | The Plan section of `00-plan.md`: purpose, perspectives, assumptions, what is left out, the cards and the agents, confirmed in a walkthrough before anything is searched. | `templates/research-plan.md`; `.claude/skills/research/SKILL.md`, steps 2 to 4 |
| card | One question answered by one kind of evidence from one kind of source, with why it matters, where to look, a disconfirming query and a stop rule. | `.claude/skills/research/SKILL.md`, step 2; `templates/research-plan.md`, Cards |
| perspective | A standpoint from which the topic is treated, one line of the plan, with the cards that serve it or "no card" where it is left empty on purpose. | `templates/research-plan.md`, Perspectives |
| disconfirming query | One search of a card written to find the opposite of what is expected, run by the agent and reported, including nothing found. | `templates/research-plan.md`, Cards |
| stop rule | When an agent stops searching: nothing new from a differently worded query and every perspective of the card has a primary source, or the budget of openings is spent. | `templates/research-plan.md`, Cards; `.claude/skills/research/SKILL.md`, The agent's brief |
| quick and deep | The two depths of `/research`: `--quick` is one card on the session model, filed as one note; `--deep` is a plan of several cards, one isolated agent per card, a bundle with a synthesis. | `.claude/skills/research/SKILL.md` |
| synthesis | Claude's reading of the notes alone, written into `00-plan.md` when every note has returned: completeness card by card, the answers side by side, the Unexpected gathered, what was not found, Claude's own view last and apart. | `.claude/skills/research/SKILL.md`, step 7; `templates/research-plan.md`, Synthesis |
| citation check | `scripts/forge-cite.py` opens every URL a note cites before the note is filed and reads the page behind a paper identifier for its title; a dead or mismatched citation sends the note back to its agent once. | `scripts/forge-cite.py`, header |
| independence of engines | Measured, never assumed: the URLs and the longer sentences two engines' notes share are counted (`forge-cite.py --independence`), and the first engine's notes are held out of the second's reach until it has returned. | `.claude/skills/research/SKILL.md`, steps 5 and 6; `scripts/forge-cite.py`, header; `scripts/forge-engine.py`, header |

## Engines, packets and the working folder

| Term | In one line | Defined in |
|---|---|---|
| engine (the forge's) | What a user clones: the universal core in the root (`CLAUDE.md`, `README.md`, `templates/`, `scripts/`, `.claude/`, `docs/`, `tests/`, `tmp/` and the root files) and no project. | `projects/forge/40-solution-design.md`, The repositories; `CLAUDE.md`, The system's own project |
| engine (another) | A model of another family reached through its own command-line tool by `scripts/forge-engine.py`, one row of its engine table (`antigravity` today); the login is the user's, and the forge carries no key or account. | `scripts/forge-engine.py`, header; `projects/forge/10-intent.md`, Research |
| engine and tier against model and version | The forge names engines and tiers (`claude`, `antigravity`; `opus`, `sonnet`), never versions, so that a name always means the newest of its kind, the version resolved by the tool at the call. | `projects/forge/10-intent.md`, Research |
| second engine | An engine run beside the session model in a deep research, `--engine <name>`: it reads the draft plan and says what it misses, then takes every card whole on the same packet. | `.claude/skills/research/SKILL.md`; `projects/forge/10-intent.md`, Research |
| packet | `packet.md` in its folder under `tmp/research/<run>/<card>/`, the whole context of a research agent: the card, the agent's brief, the note's shape, the attached notes; the same for both engines. | `.claude/skills/research/SKILL.md`, step 5; `scripts/forge-engine.py`, header |
| run folder | `tmp/research/YYYY-MM-DD-<topic>/`, holding the packets, envelopes, profile and held notes of one research, kept for inspection and never cleaned by a script. | `.claude/skills/research/SKILL.md`, step 3; `scripts/forge-engine.py`, header |
| profile | A copy of the user's settings made by `forge-engine.py` for one run of another engine, with the forge's tree and the shell denied and the web allowed, kept in the run folder as its record. | `scripts/forge-engine.py`, header, step 2a |
| envelope | The JSON answer of another engine's tool, with its status, response and usage, saved as `envelope.json` beside the packet; an empty answer is a failure. | `scripts/forge-engine.py`, header, step 4 |
| working folder | `tmp/` at the engine root, where the packets and envelopes, the tasks of a documentation run, a check's report before filing, a dry ledger and a migration's manifest lie; the folder in git, its contents never, nothing in it a source of truth. | `tmp/README.md`; `projects/forge/10-intent.md`, Operating environment |

## Projects and the engine

| Term | In one line | Defined in |
|---|---|---|
| project | A directory under `projects/`, the unit the forge works on, a git repository of its own or a project outside git, of kind `thought` or `library`. | `CLAUDE.md`, Repository layout and Persistence |
| project file | `project.md`, written once at a project's creation: `project`, `kind` and `language`; a fixture carries `fixture: true`; a project without it is of the shape before the migration. | `templates/project.md` |
| thought project | A project of kind `thought`: the chain, a brief and an intent and the layers below it as the project needs them. | `CLAUDE.md`, Repository layout; `templates/project.md` |
| library | A project of kind `library`: material shared across projects, no chain, only the project file, the ledger, sources and research, and a README that catalogues what it holds. | `CLAUDE.md`, Repository layout |
| dependency (of a project) | Another project's document cited by path, a library's among them, found by the ledger in the chain, the indexes, the recipes, the work and the research, registered with no version. | `templates/ledger.md`, Dependencies; `CLAUDE.md`, Ledger |
| project outside git | A project whose directory git does not report as the top of a repository, on which the forge runs no git whatever repository lies above it; a property, not a defect. | `CLAUDE.md`, Persistence |
| the forge's own project | `projects/forge`, Forge of Thought run through its own process: a repository of its own beside the engine, cloned by whoever develops the engine and needed by no user; its root renders land in the engine root. | `CLAUDE.md`, The system's own project; `projects/forge/10-intent.md`, Operating environment |
| `forge` in a command | In the commands of git, `/save`, `/pull`, `forge-branch` and `/release`, the whole: the engine's repository and the forge's own project beside it, each its own commit with the prefix `forge:`; in the commands over documents, the project. | `CLAUDE.md`, Persistence |
| shape of a project | The set of files a release expects of a project, recognised by the migration script as marks, one per step; until a project of an older shape is migrated nothing writes into it. | `templates/project.md`; `.claude/skills/migrate/SKILL.md`; `CLAUDE.md`, Persistence |
| migration | `/migrate [slug]` through `scripts/forge-migrate.py`: a project brought to the shape of a release that changed the shape of files, a dry run first, then once per project, on one clone, on `main`, on the principal's word. | `.claude/skills/migrate/SKILL.md` |
| fixture | `tests/fixture`, a synthetic thought project with a made-up subject and one of each kind of document the scripts read, never a copy of a real project; every test works on a copy of it. | `projects/forge/10-intent.md`, Operating environment; `.claude/skills/test/SKILL.md` |
| test | The engine's tests in `tests/`, run by `/test` as `python -m pytest`, enough to catch what a change of a script breaks; a script is changed with its test. | `.claude/skills/test/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |
| CI | The run of the tests at every push and pull request of the engine, on Linux and Windows, Python 3.8 and the newest, with an empty git configuration so that nothing of the machine is tested. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Operating environment |

## Git, saving and releasing

| Term | In one line | Defined in |
|---|---|---|
| save | `/save`: the `light` check, then a commit and a push of one repository on whatever branch is checked out, through `forge-save.py`, no render; `--quick` leaves the check out. | `CLAUDE.md`, Persistence; `projects/forge/10-intent.md`, Operating environment |
| release | `/release`, from `main` only: the tests where the repository is the engine, the checks with their walkthrough, the documentation, the README and release notes, the state render, then a save with the message `release <intent version>` and the tag at an approved major. | `.claude/skills/release/SKILL.md` |
| `--auto` | The flag that runs a release through without steps put to the principal, stopping only at a serious thing: a repository behind or diverged, a red test, a finding that would change a position or a rule, a new instance fact in a render, once before the save, and always at the tag of a major. | `.claude/skills/release/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |
| major | An integer version of the intent: the record of what the principal holds at that date, approved on his word after every check, both critic lenses and one challenge, and tagged at its release. | `CLAUDE.md`, Versioning & status; `projects/forge/10-intent.md`, Versioning and state |
| tag | `v<major>` at the release of an approved major, the one tag with a fixed name so that the checks and the release notes can rely on it; any other tag is the principal's request with a free name. | `CLAUDE.md`, Persistence; `.claude/skills/release/SKILL.md`, step 6 |
| branch | Voluntary and left to git: `forge-branch.py` creates or switches one, `/save` pushes whatever branch is checked out, and merging is git's, by hand or by merge request. | `CLAUDE.md`, Persistence |
| pull | `/pull`: the forge looks at the remote through `forge-status.py --remote`, says the state as a fact (up to date, behind, ahead, diverged, no origin, not under git) and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| what waits on GitHub | The open pull requests and the unanswered discussions of a repository's origin, read through `gh` by `forge-status.py --remote` and said as a fact beside the branch's state; the forge reads them and merges, answers and closes nothing. | `scripts/forge-status.py`, header; `projects/forge/10-intent.md`, Operating environment |
| way of merging | One of three for every file of a project, told to git in `.gitattributes`: text (artefacts, recipes, threads, records), derived (`ours` at a merge and made again), immutable and unique (never in conflict). | `projects/forge/10-intent.md`, Operating environment |
| derived file | A file made from others and made again on `main`: the ledger, never in git; the renders, the README, the release notes, the documentation, the state render and the published companions, in git and `ours` at a merge. | `projects/forge/10-intent.md`, Operating environment |
| merge driver `ours` | The git merge driver that keeps one side of a derived file at a merge, registered once per machine in the user's global configuration; an unregistered clone silently falls back to a conflict. | `CLAUDE.md`, Persistence; `scripts/forge-status.py`, header |
| registration of the merge driver | The writing of the driver `ours` and the settings it needs into the user's global git configuration by `/setup` through `scripts/forge-config.py`, on the user's word; `forge-status` says when it is missing. | `CLAUDE.md`, Persistence; `scripts/forge-status.py`, header |
| step of a conflict | How a conflict `forge-save` leaves standing is settled: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording, and the finishing commands of git run on the hook's ask. | `CLAUDE.md`, Persistence |
| the hook's ask | The few commands of git that finish the step of a conflict, which the hook `scripts/hook-git.py` puts to the principal instead of denying and runs on his yes. | `CLAUDE.md`, Persistence; `projects/forge/40-solution-design.md`, The wall |
| guarded command | A command that changes files the moment it runs and therefore starts on the principal's word and never on Claude's judgement: `/save`, `/release`, `/pull`, `/spinoff`, `/setup`, `/new-project`, `/new-artefact`, `/import-project`, `/ingest`, `/render`, `/publish`, `/document`, `/migrate`. | `projects/forge/10-intent.md`, Operating environment |
| manual | `/man [command | method | question]`, alias `/manual`: the forge's manual, a reader of its own definitions and never a text of its own; a need in free words gets the way the forge has for it. | `.claude/skills/man/SKILL.md` |

## Renders, published files and work products

| Term | In one line | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`: how a render is made, its inputs, audience, instructions, output template and Format in one versioned file, iterated with the principal. | `CLAUDE.md`, Document chain, Renders |
| genre | A kind of recipe with a skeleton `templates/recipe-<genre>.md` and an interview through `/recipe <genre>`; readme, release-notes, screenplay and user-stories-export among them. | `CLAUDE.md`, Document chain, Renders |
| render | An audience-specific Markdown output generated from the chain by `/render`, never edited by hand and never a source of truth, opening with its provenance. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md` |
| provenance | The YAML front-matter a render opens with: project, render, generated, the recipe with its version and every input with its version; the row the ledger's Renders table reads. | `.claude/skills/render/SKILL.md`, step 5 |
| stale | Of a render: any version cited in its provenance differs from the current version of that file, or a cited file no longer exists; of a published file or a work product: the render or the specification is newer than what was made from it. | `.claude/skills/render/SKILL.md`, step 5; `templates/ledger.md`, Published and Work |
| primary render | The render in the first language of a recipe's `languages:`, generated first, from which the translations are made. | `.claude/skills/render/SKILL.md`, step 3; `projects/forge/10-intent.md`, Document chain |
| translation | A render in a further language of the recipe, `renders/<recipe>.<lang>.md`, translated scene for scene and line for line from the primary in the same run and citing it in `translated_from`. | `.claude/skills/render/SKILL.md`, steps 3 to 5 |
| plain file | The file a script makes from a render where the recipe names a format, deterministic and cheap, landing beside the render: a `.pptx`, a `.docx`, or a screenplay's video or player events. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md`, step 7 |
| format file | The plain file of a screenplay render, an `.mp4` painted frame by frame or the timed events in `<name>.html-player.js`, made by `scripts/md2video.py` with no model in it. | `scripts/md2video.py`, header; `projects/forge/10-intent.md`, Document chain |
| published file | The designed `.pptx` or `.docx` in `published/`, made from the render as it lies on disk by `/publish` through a model, on the principal's command only. | `.claude/skills/publish/SKILL.md` |
| published companion | `published/<recipe>.md`, the provenance of a published file: project, file, recipe, render, model and the date published; the ledger computes `current` or `stale` from it. | `.claude/skills/publish/SKILL.md`, step 6; `templates/ledger.md`, Published |
| the principal's own file | Any file in `renders/` or `published/` that no recipe names, made by hand from the forge's files, a copy, a PDF, an HTML of a diagram: in git, no companion, no row, no check. | `projects/forge/10-intent.md`, Document chain; `CLAUDE.md`, Document chain, Renders |
| state render | `renders/state.md`, the ledger written as a tracked render by `/release` on `main`, so that the state stands on the remote; the Renders table does not list it. | `.claude/skills/release/SKILL.md`, step 5; `CLAUDE.md`, Repository layout |
| screenplay | A render of the genre `screenplay`: a title card, a card of what the viewer will see, scenes with the time of day, each with a caption of two parts (Now, Why) and a fenced block of what the terminal shows. | `projects/forge/10-intent.md`, Document chain; `scripts/md2video.py`, header |
| player page | `docs/videos/index.html`, written anew from `templates/html-player.html` by `md2video.py` whenever a file is written into the folder, playing the html-player files listed in it. | `scripts/md2video.py`, header; `CLAUDE.md`, Repository layout |
| public folder | `docs/videos/` of the engine, the one public place of an instance, served by GitHub Pages, flat, reached by a recipe's `output:` and left alone by `/document`. | `CLAUDE.md`, Document chain, Renders; `projects/forge/10-intent.md`, Growth path |
| work product | A document of kind `work`: an output of the project made with work of its own, two files in `work/`, the file `work/<name>.<ext>` holding the content and the specification beside it. | `.claude/skills/work/SKILL.md`; `CLAUDE.md`, Document kinds |
| specification | `work/<name>.spec.md`, the way and the why of a work product: the task, the inputs cited by ID and path, the method, ASM and TBC items, and `## Making`; versioned with its history companion. | `.claude/skills/work/SKILL.md`; `projects/forge/10-intent.md`, Document chain |

## Reviewers and agents

| Term | In one line | Defined in |
|---|---|---|
| subagent | An agent Claude launches for one task in a context of its own: a reviewer, a renderer, a documentation agent, a research agent. | `CLAUDE.md`, Isolated reviewers |
| isolated subagent | A subagent that sees nothing of the conversation, reads every input from disk in its own run and lets no instance fact into what it returns. | `CLAUDE.md`, Isolated reviewers |
| isolation | That property of a subagent; not independence, since the author and the reviewers share one model family, so that agreement between them is consistency and never validation. | `CLAUDE.md`, Isolated reviewers; `projects/forge/10-intent.md`, Review |
| critic | The reviewer of the quality of the documents, never of the substance, run as `/critique <lens> [artefact]`, returning findings filed in `reviews/`. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| lens | One critic's angle, one agent file `critic-<lens>` with a Lens section of its own; what each lens reads and goes after. | `CLAUDE.md`, Isolated reviewers |
| challenger | The reviewer of the substance of the thinking, never of document quality, run as `/challenge <persona> [artefact]`, allowed to search the web, returning challenges filed in `challenges/`. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md` |
| persona | One challenger's standpoint and register, one agent file `challenger-<persona>`; the blind spots each persona hunts. | `CLAUDE.md`, Isolated reviewers |
| check | The reviewer of mechanical conformance with the conventions, never substance or quality, run as `/check <name> [slug]`, one concern each; a run that finds nothing files nothing. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/check-contract/SKILL.md` |
| finding | Prefix FND: a result of a critic (quality) or of a check (conformance), severity high, medium or low, numbered by the command and settled by walkthrough as resolved, rejected, parked or obsolete. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | Prefix CHL: a result of a challenger on the substance, severity dealbreaker, major or minor, with its epistemic status, settled as accepted, rejected, parked or obsolete. | `.claude/skills/challenger-contract/SKILL.md`, Output; `templates/ledger.md`, Challenges |
| contract | The skill that owns what every member of one kind of agent shares, conduct, isolation, subject, way of working and the shape of the output, preloaded into each agent: the critic's, the challenger's, the check's and the documentation agents'. | `CLAUDE.md`, Isolated reviewers |
| Lens section | The one section an agent file owns beyond its contract, a specialisation that may narrow what is read or make a shared rule stricter, never rename, drop or duplicate one. | `CLAUDE.md`, Isolated reviewers |
| the documentation run's report | `reviews/YYYY-MM-DD-check-documentation.md`, filed by `/document` with what the run could not place as findings: facts without an owner, disagreements of map and owner, reasons no file records. | `.claude/skills/document/SKILL.md`, step 7 |

## The documentation

| Term | In one line | Defined in |
|---|---|---|
| documentation | Pages of one topic each in `docs/` with an index, generated by `/document` and never composed by hand, for the user, the extender and the evaluator, in five sections filled only where the project has material. | `CLAUDE.md`, Document chain, Documentation; `.claude/skills/document/SKILL.md` |
| documentation map | `docs-map.md` beside the owning project's ledger: one entry per page with everything the page is made from, written by the planner, read by the scripts and the writers, never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md`, The map |
| page | A document of kind `page`: one topic in one kind, how-to, explanation or reference, made alone from its entry in the map and the inputs the entry names, overwritten by the next run. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-writer.md` |
| index | `docs/README.md`, derived by `scripts/docs-index.py` from the map's one line per page and its reader paths; also the resource index of `sources/` and `research/`. | `.claude/skills/document/SKILL.md`, step 5; `.claude/agents/docs-planner.md` |
| mirrored | Of a page: it restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| derived | Of a page: it puts together what no single file says, from evidence in several, by the reasoning its entry's `evidence` gives; a page is never invented. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| how-to | A page that carries what the person does, step by step where there are steps, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| explanation | A page that carries what a thing is, how it works and why it is so, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| reference | A page that states facts in the structure of what it mirrors, free of interpretation, a table where the input is a table, never explaining. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| pinned fact | A fact of the project no file owns yet, a prerequisite, an install line, the public home of the repository, kept one bullet each in the readme recipe's section `## Pinned facts (not rendered)` and read by the planner as an owner. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports, with the page that needs it; the writer leaves it out, and the run reports it. | `.claude/agents/docs-planner.md`, The map |

## The fixed files of the root

| Term | In one line | Defined in |
|---|---|---|
| the security policy | `SECURITY.md`, the principal's own text: how a problem is reported privately, what the forge promises the reporter, what is supported and what is in and out of scope; no render, no companion, no row, no check. | `projects/forge/10-intent.md`, Growth path; `CLAUDE.md`, Repository layout |
| the code of conduct | `CODE_OF_CONDUCT.md`, the Contributor Covenant 3.0 word for word under its own licence, its reporting sentence pointing at the private way CONTRIBUTING names; no render. | `projects/forge/10-intent.md`, Growth path; `CLAUDE.md`, Repository layout |
| the fixed files of the root | The two files beside the root renders that are no render and derive from nothing in the chain, kept by hand and changed only on the principal's word. | `projects/forge/40-solution-design.md`, The repositories; `projects/forge/10-intent.md`, Growth path |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
