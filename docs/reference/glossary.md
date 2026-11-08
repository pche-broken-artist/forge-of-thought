---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: bc7ddca38f633bab
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1100
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
  - projects/forge/10-intent.md#POS.1990
  - projects/forge/10-intent.md#POS.2010
  - projects/forge/10-intent.md#Elicitation
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
  - tmp/README.md
---

# Glossary

The glossary is the vocabulary of the forge: every term in one line,
with the file that defines it. It is for the user who meets a word on
another page, the extender who must use the owners' words, and the
evaluator who reads without running anything. Each line says what the
term means and nothing of why; the column "Defined in" names the file
to open for the whole rule, a path in backticks being a file of the
engine. The forge itself, as a whole, is described on
[What the forge is and is not](../about/what-it-is-and-is-not.md).
The terms are grouped by the part of the forge they belong to, and
within a group they stand in the order a reader meets them.

## The people and the machine

| Term | In one line | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is addressed to: teams, colleagues, or the principal's future self. | `CLAUDE.md`, What this workspace is |
| Claude as cognitive extension | Claude is the cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, proposes and never decides. | `CLAUDE.md`, Roles |
| Claude Code | The agent for the command line in which the forge runs; its slash commands, skills, agents and hooks are the mechanisms, and the forge is what they are told. | `CLAUDE.md`, What this workspace is |
| session | One working conversation of Claude Code, from its start to `/end`, whose context no isolated subagent sees. | `CLAUDE.md`, Isolated reviewers and Commands |
| harness | Claude Code seen as the machinery around Claude, the hooks among it, which enforces the principal's word where it can: Claude is kept from sensitive paths and web access is approved per domain. | `projects/forge/10-intent.md`, the item "The harness enforces the principal's word where it can" |
| instance | One installation of the forge on one machine, with its own instance file `CLAUDE.local.md`. | `CLAUDE.md`, What this workspace is; `.claude/skills/docs-contract/SKILL.md`, The voice |
| instance fact | Who the principal is, what language the conversation runs in and the handle he signs records with: kept in `CLAUDE.local.md`, never in the engine, never in a report or a page. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, the item "The engine carries no instance facts" |
| session model | The one model the whole forge runs on, chosen once, `model: inherit` in every agent and set in `.claude/settings.local.json`. | `CLAUDE.md`, Isolated reviewers and Repository layout |
| working method | A named way a working conversation runs, such as the walkthrough or intent-first; none is a command, each applies whenever its situation arises. | `CLAUDE.md`, Working methods |
| prime directive | One of the ten rules at the head of `CLAUDE.md` that hold over all of the forge's work. | `CLAUDE.md`, Prime directives |
| guarded command | A command that writes, scaffolds, commits or regenerates, started only on the principal's word and never on Claude's judgement. | `projects/forge/10-intent.md`, the item "The harness enforces the principal's word where it can" |
| manual | `/man`, alias `/manual`: the forge's manual, read at the call from the files that own each thing, never a text of its own; a need said in free words gets the way the forge has for it. | `.claude/skills/man/SKILL.md` |

## Documents and the chain

| Term | In one line | Defined in |
|---|---|---|
| document | The word for every file of a project; every document has one kind. | `CLAUDE.md`, Document kinds |
| kind (of a document) | What a document is, who writes it, whether it is versioned and how it behaves, one per document. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain, composed by the principal with Claude, versioned and rewritten freely; what each is, its definition says. | `CLAUDE.md`, Document kinds and Document chain |
| layer | An artefact below the intent, taken as the project needs it, none a condition of another; a layer a project does not have is not missing. | `CLAUDE.md`, Document chain |
| definition | The state file of one artefact, `.claude/skills/forge/states/<state>.md`, worked through `/forge <state>`: what the artefact is, how it is found and its rules, in seven blocks. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, the item "The shape of a definition" |
| template | The skeleton in `templates/` paired with a definition: where the result lands and what comes out. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names, in the artefact's own vocabulary, what must be found; walked at the moments the definition names, neither a questionnaire nor a list of criteria. | `projects/forge/10-intent.md`, the item "A Map is a map of what must be found" |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds; the conversation is its medium, the interview one instrument, research and sources others. | `projects/forge/10-intent.md`, the item "What elicitation is" |
| brief | `00-brief.md`, or `00-brief-<name>.md` for a later whole: the principal's idea put together, rough on purpose, in free form, approved when he says so and then mined. | `.claude/skills/forge/states/brief.md` |
| mined | Said of a brief whose substance has been sifted into the intent on the principal's word; the mining record of the intent's history says `pending`, `partial`, `mined` or `dropped`. | `.claude/skills/forge/states/brief.md`; `templates/history.md` |
| intent | `10-intent.md`, the working document: the consolidated current state of what the principal holds, as positions, facts, threads and rejections, rewritten for coherence each round. | `.claude/skills/forge/states/intent.md`; `projects/forge/10-intent.md`, the item on the working document |
| position | What the principal holds or wants, and why, with what it comes from; prefix POS. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, the item on the prefix vocabulary |
| fact | What is the case, as the principal states it on his word or as a source states it cited to its file; not a stance, and verification is never demanded; prefix FCT. | `CLAUDE.md`, ID scheme |
| thread | One open matter of the intent: an unresolved matter to elicit next, naming the artefact it concerns and carrying its origin; prefix THR. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| thread file | `threads/THR.NNNN.md`, one file per thread, its header its state (what it concerns, its origin, open or closed), freely rewritten while open and immutable once closed. | `templates/thread.md`; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | A direction the principal dropped, kept with the reason it was dropped; prefix REJ. | `CLAUDE.md`, ID scheme |
| assignment | `20-assignment.md`: the in-scope substance of the intent carried to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| obligation in the indicative | The form of every requirement: `shall` / `shall not` in English, strictly, never a conditional, a permission or a wish; in another language that language's own verb of obligation. | `.claude/skills/forge/states/assignment.md`, Requirement style |
| provenance map | A tool of the recast of an assignment or a BRD: group, then items, then the positions or parent items they came from, with the in-scope items that landed nowhere and the items with no parent. | `.claude/skills/forge/states/assignment.md`, Course |
| solution design | `40-solution-design.md`: how the things wanted are realised, part by part, with the choices each rests on, kept current and never finished. | `.claude/skills/forge/states/solution-design.md` |
| prefix of two or three letters | The head of every ID, `PREFIX.NNNN`: two or three letters, numbered in tens, each new group at the next hundred, four digits as long as the number fits. | `CLAUDE.md`, ID scheme |

## The BRD

| Term | In one line | Defined in |
|---|---|---|
| BRD | `30-brd.md`, the business requirements: the parent broken into rules, behaviour and qualities that the stakeholders can review and the delivery can estimate. | `.claude/skills/forge/states/brd.md` |
| parent of an item | The item of the layer above that an item is traced to: a REQ of the assignment, or a POS of the intent where the project has no assignment; for a story a BR, NFR, UC or DEP of the BRD. | `.claude/skills/forge/states/brd.md`, Inputs; `.claude/skills/forge/states/user-stories.md`, Inputs |
| business requirement | One rule of the business, testable, citing the REQ or POS it carries; prefix BR. | `CLAUDE.md`, ID scheme |
| use case | Behaviour agreed as a sequence, at user-goal level, its steps in the active voice; prefix UC. | `CLAUDE.md`, ID scheme; `templates/brd.md`, Use cases |
| dependency (of a BRD) | What the BRD relies on outside itself, a system, a project or a document; prefix DEP. | `CLAUDE.md`, ID scheme |
| non-functional requirement | A quality by category, its value the stakeholders' or a TBC with an owner; prefix NFR. | `CLAUDE.md`, ID scheme; `templates/brd.md`, Qualities |
| roster of areas | The areas of the enterprise a BRD must consider and which of them are mandatory: a library document of the instance cited by path, or `Roster: none` where the project has no enterprise around it. | `.claude/skills/forge/states/brd.md`, Inputs |
| touched area | An area of the roster as the BRD walks it: found in named items, or not applicable with the reason; a mandatory area is never silent. | `templates/brd.md`, Touched areas of the enterprise |

## The user stories

| Term | In one line | Defined in |
|---|---|---|
| user story | Behaviour seen from outside, with its acceptance criteria, citing the BR, NFR, UC, DEP or POS it serves; prefix US, in `35-user-stories.md`. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/user-stories.md` |
| acceptance criterion | What happens in the usual course of a story: one bullet in the indicative, present tense, one behaviour each, testable. | `.claude/skills/forge/states/user-stories.md`, Story style |
| edge case | A situation at the border of a behaviour, a failure, a missing datum or a change during use, written as `situation → what happens`. | `.claude/skills/forge/states/user-stories.md`, Story style |
| Reference of a story | The one part every story has: the BR, NFR, UC or DEP it serves, or in a small change without a BRD the POS. | `.claude/skills/forge/states/user-stories.md`, Story style |
| Story style | The rules of wording a story: one function as the one who uses it meets it, criteria in the indicative, no vague word, no technical solution, priority or estimate, fixed English labels. | `.claude/skills/forge/states/user-stories.md`, Story style |
| the cut | What Claude returns first when the stories are handed over: the name of every story with a short description, and the items of the parent no story serves. | `.claude/skills/forge/states/user-stories.md`, Course |
| the export of the stories | A render of the genre `user-stories-export`, one heading per story with its parts on lines of their own, leaving out every reference to a POS. | `.claude/skills/forge/states/user-stories.md`, Instruments; `projects/forge/10-intent.md`, the item "The user stories" |

## The walkthrough and the round

| Term | In one line | Defined in |
|---|---|---|
| walkthrough | A list of items needing the principal's decision, worked one item per message in order of weight, each closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. | `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item: `accept`, `modify`, `question`, `reject`, `park` or `obsolete`, a single letter allowed for the first five. | `.claude/skills/walkthrough/SKILL.md`, The verdict |
| round | One working conversation, its answers carried in the conversation and written once at its end, one version bump for the whole. | `CLAUDE.md`, Prime directives (9) and Working methods |
| write | The principal's word that closes a round: Claude reflects the whole round back and, on his yes, writes everything carried as one round. | `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write |

## Records and state

| Term | In one line | Defined in |
|---|---|---|
| history companion | `<file>.history.md` beside every versioned document: the append-only log of its changes, one record per change, never in the body. | `CLAUDE.md`, Versioning & status; `templates/history.md` |
| record | One line of a history: date, version, author, subject, kind (`created`, `changed`, `closed`, `removed`, `approved`), reason, and where it has them `Action` and `Was`. | `templates/history.md` |
| record of state | A record that carries the current version without raising it: the mining of a brief, a finding or a challenge settled, the state of a work product. | `templates/history.md` |
| archive | A history table written before the log, moved as it stands to `<file>.history.archive.md`, or the hand-kept ledger moved to `ledger.archive.md` at the migration; immutable from then on. | `CLAUDE.md`, Versioning & status; `templates/ledger.md` |
| decision | A record of the principal's decision with its reason, numbered DEC, appended to `decisions.md` and never edited. | `templates/decisions.md` |
| Verdict line | The line of a decision that rules on a finding or a challenge: `<ID> rejected`, `parked until <what>` or `obsolete`, one line per ID. | `templates/decisions.md` |
| ledger | `ledger.md`, the single source of truth for state, built by `python scripts/forge-ledger.py <slug>` from the documents and never in git. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| made at read time | Said of the ledger: a script builds it from the documents whenever it is read, nobody writes a row, so it is not a thing to merge. | `projects/forge/10-intent.md`, the item "The ledger is made at read time"; `CLAUDE.md`, Ledger |
| Waiting on principal | The ledger's section of what waits on him, by rule and not by a hand-kept list: the open threads, the TBCs he owns, the open findings of a critic, the open challenges, the parked ones under Parked. | `templates/ledger.md`, Waiting on principal |
| Reports | The ledger's section of what the merged files cannot say, found by the script: an ID defined twice, a closed thread touched later, a thread cited with neither a file nor a closed record. | `templates/ledger.md`, Reports |
| immutable | Never edited after its birth: a review, a challenge, a research note, a closed thread, a source from its registration; a process rule, not a git mechanism. | `CLAUDE.md`, Versioning & status and Persistence |
| stale | A render whose provenance cites a version that differs from the file's current one or a file that is gone; a published file whose render is newer; a work product's file after its specification changed. | `.claude/skills/render/SKILL.md`, step 5; `templates/ledger.md` |

## Sources and research

| Term | In one line | Defined in |
|---|---|---|
| source | External input as it arrived, in `sources/`, immutable from registration, one form each: text or a functional binary. | `CLAUDE.md`, Document kinds and Document chain (External inputs) |
| bundle | A set of related files in `sources/<slug>/`, one source with one ledger entry, catalogued by its own `00-INDEX.md`. | `CLAUDE.md`, Document chain (External inputs) |
| growing bundle | A bundle of one origin that keeps arriving, grown file by file through `/ingest --bundle <name>`, each file immutable from its own registration. | `.claude/skills/ingest/SKILL.md`, step 1 |
| extract | The Markdown made from a binary by `python scripts/doc2md.py` on the principal's word, which then is the source. | `.claude/skills/ingest/SKILL.md`, step 3 |
| resource index | The `00-INDEX.md` of every `sources/` and `research/` directory: a light catalogue of what exists and what it is for, freely rewritten, an automatic input of no command. | `CLAUDE.md`, Document chain (Resource indexes) |
| Role | The free-text field of a source's index entry saying what the source is for, the principal's word, asked before the entry is written. | `.claude/skills/ingest/SKILL.md`, step 4 |
| research | A durable answer to one question about the world outside, immutable, in `research/`, indexed. | `CLAUDE.md`, Document kinds |
| research note | One card, one engine, one note, in the shape of `templates/research.md`, immutable from its filing. | `templates/research.md` |
| research bundle | `research/YYYY-MM-DD-<topic>/`: the plan and the synthesis at its head in `00-plan.md`, and one note per card per engine, `<card>.<engine>.md`. | `.claude/skills/research/SKILL.md`, Target |
| plan | The Plan section of `00-plan.md`: purpose, perspectives, assumptions, what is left out, the cards and the agents, confirmed in a walkthrough before anything is searched. | `templates/research-plan.md`; `.claude/skills/research/SKILL.md`, step 4 |
| card | One question answered by one kind of evidence from one kind of source; a card that needs two kinds is two cards. | `.claude/skills/research/SKILL.md`, step 2 |
| perspective | A standpoint from which the topic is treated, with the cards that serve it or `no card` where the plan leaves it empty on purpose. | `templates/research-plan.md`, Perspectives |
| disconfirming query | One search of a card written to find the opposite of what is expected, run by the agent and reported with what it found, including nothing. | `templates/research-plan.md`, Cards |
| stop rule | When a card's search ends: nothing new from a differently-worded query and every perspective of the card has a primary source, or the opening budget is spent. | `templates/research-plan.md`, Cards |
| quick and deep | The two depths of a research: `--quick` is one card on the session model, filed as one note; `--deep` is a plan of several cards, one isolated agent per card, a bundle with a synthesis. | `.claude/skills/research/SKILL.md` |
| synthesis | Claude's reading of the notes alone, written into `00-plan.md` when every note has returned: completeness card by card, the engines' answers side by side, the Unexpected gathered, what was not found, Claude's view last and apart. | `templates/research-plan.md`, Synthesis |
| citation check | `python scripts/forge-cite.py <note>` opens every URL a note cites before it is filed and reads an arXiv page for its title; a dead page or a mismatched title sends the note back to its agent. | `scripts/forge-cite.py`, its header |
| independence of engines | Measured, never assumed: the URLs and sentences two engines' notes of one card share are counted by `forge-cite.py --independence`, and the first engine's notes are held out of the second's reach until its note has returned. | `projects/forge/10-intent.md`, the item "Two model families on one plan"; `scripts/forge-cite.py`, its header |

## Engines

| Term | In one line | Defined in |
|---|---|---|
| engine (the forge's) | The forge's own repository: `CLAUDE.md`, the skills, the agents, the scripts and the templates, with its own project `projects/forge`, as against the projects run in it. | `CLAUDE.md`, Persistence and Repository layout |
| engine (of a model family) | A model of another family reached over its own command line through `python scripts/forge-engine.py <engine>`, one row of the script's engine table, `antigravity` the row today. | `scripts/forge-engine.py`, its header |
| engine and tier against model and version | The forge names engines and tiers, never models or versions, so that a name always means the newest of its kind: `claude` or `antigravity` in the engine table, `opus` or `sonnet` in a model override. | `projects/forge/10-intent.md`, the item "The link to another engine" |
| second engine | An engine run beside the session model in a deep research, asked for by name with `--deep --engine <name>`: it reads the draft plan and then takes every card whole on the same packet. | `.claude/skills/research/SKILL.md`; `projects/forge/10-intent.md`, the item "Two model families on one plan" |
| packet | The folder `tmp/research/<run>/<card>/` with `packet.md`, the whole context of one agent: the card, the agent's brief, the note's shape and the attached notes, nothing of the conversation. | `.claude/skills/research/SKILL.md`, step 5 |
| run folder | `tmp/research/YYYY-MM-DD-<topic>/`, where the packets, envelopes, profiles and reports of one research run lie, kept for inspection and never cleaned by a script. | `.claude/skills/research/SKILL.md`, steps 3 and 8 |
| profile | A copy of the user's settings made for one run of another engine, with the forge's tree and the shell denied and the web allowed, kept in the run folder as its record. | `scripts/forge-engine.py`, its header (2a) |
| envelope | The JSON answer of an engine's run, its status, response and usage, saved as `envelope.json` beside the packet. | `scripts/forge-engine.py`, its header |
| working folder | `tmp/` at the engine's root: packets, envelopes and profiles, the tasks of a documentation run, a check's report before filing, a dry ledger, the manifest of a migration; in git with its README, its contents never, a source of truth for nothing. | `tmp/README.md`; `projects/forge/10-intent.md`, the item "The engine's working folder" |

## Renders

| Term | In one line | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`: how a render is made, its inputs, audience, instructions and output template in one versioned file. | `CLAUDE.md`, Document chain (Renders) |
| genre | A kind of recipe composed through an interview, `/recipe <genre>`, from the skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md`, Document chain (Renders) |
| render | An audience-specific output generated from the chain by `/render`, never edited by hand and never a source of truth, opening with its provenance. | `CLAUDE.md`, Document chain (Renders); `.claude/skills/render/SKILL.md` |
| provenance | The YAML front-matter a render opens with: project, render, date generated, the recipe with its version and every input with its version. | `.claude/skills/render/SKILL.md`, step 5 |
| primary render | The render in the first language a recipe declares in `languages:`, from which the translations are made. | `.claude/skills/render/SKILL.md`, step 3; `projects/forge/10-intent.md`, the item "A recipe may render in several languages" |
| translation | A render in another declared language, `renders/<recipe>.<lang>.md`, made from the primary render in the same run scene for scene and line for line, citing it in `translated_from`. | `.claude/skills/render/SKILL.md`, steps 3 and 5 |
| plain file | The file `/render` makes from the render through the script of the recipe's format, with pandoc for a deck or a document and with `md2video.py` for a screenplay, deterministic, beside the render. | `.claude/skills/render/SKILL.md`, step 7 |
| format file | The file the recipe's `## Format` section names beside the Markdown render, the plain file of its format; its name follows the render's language, and its `output:` may send it into the public folder. | `projects/forge/10-intent.md`, the items "A recipe may render in several languages" and "The engine hosts what a project shows in public" |
| published file | The designed `.pptx` or `.docx` made from the render by `/publish` through a model, in `published/`, on the principal's command only. | `.claude/skills/publish/SKILL.md` |
| published companion | `published/<recipe>.md`: the provenance of the published file, its project, file, recipe, render, model and date published, from which the ledger computes `current` or `stale`. | `.claude/skills/publish/SKILL.md`, step 6 |
| the principal's own file | Any file in `renders/` or `published/` that no recipe names, made by hand from the forge's: in git beside them, no companion, no row, no check, never read or overwritten by the forge. | `projects/forge/10-intent.md`, the item "The principal's own files beside the forge's"; `CLAUDE.md`, Document chain (Renders) |
| screenplay | A render of the genre `screenplay`: a terminal conversation as a title card, a card of what the viewer will see and scenes with captions and fenced blocks of what the terminal shows; its format `video` or `html-player`, no published file. | `projects/forge/10-intent.md`, the item "A screenplay and its player" |
| public folder | `docs/videos/` of the engine, the one public folder, served by GitHub Pages, flat, and left alone by `/document`. | `CLAUDE.md`, Document chain (Renders) and Repository layout |
| player page | `docs/videos/index.html`, written anew by `md2video.py` from `templates/html-player.html` with the folder's files whenever a file is written into the folder. | `projects/forge/10-intent.md`, the item "The engine hosts what a project shows in public"; `CLAUDE.md`, Repository layout |
| state render | `renders/state.md`, the ledger written as a tracked render by `/release` on `main`, so that the state is on the remote. | `.claude/skills/release/SKILL.md`, step 5 |

## Work products

| Term | In one line | Defined in |
|---|---|---|
| work product | An output of the project made with work of its own, neither artefact nor render: two files in `work/`, the file that holds the content and the specification beside it. | `.claude/skills/work/SKILL.md`; `CLAUDE.md`, Document kinds |
| specification | `work/<name>.spec.md`: the way and the why of a work product, versioned with its history, citing its inputs and never copying them, its `## Making` saying how the file is made. | `.claude/skills/work/SKILL.md` |

## The reviewers

| Term | In one line | Defined in |
|---|---|---|
| subagent | An agent Claude launches for one job in a context of its own: a reviewer, a renderer, a documentation agent or a research agent. | `CLAUDE.md`, Isolated reviewers |
| isolated subagent | A subagent that sees nothing of the conversation, reads every input from disk in its own run and lets no instance fact into what it returns. | `CLAUDE.md`, Isolated reviewers |
| isolation | That rule of every subagent: the conversation unseen, the inputs from disk, no instance fact out. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/docs-contract/SKILL.md`, Conduct and isolation |
| contract | The skill that owns what every agent of one kind shares, conduct, isolation, subject, way of working and the shape of the output, preloaded into each agent of that kind. | `CLAUDE.md`, Isolated reviewers |
| Lens section | The one section an agent file owns beyond its contract: a specialisation that may narrow what is read or make a shared rule stricter, never rename, drop or duplicate one. | `CLAUDE.md`, Isolated reviewers |
| critic | The reviewer of document quality, never of substance, run as `/critique <lens> [artefact]`, whose findings are filed in `reviews/`. | `.claude/skills/critic-contract/SKILL.md` |
| lens | One critic's angle, one agent file `critic-<lens>`, its Lens section its own. | `.claude/skills/critic-contract/SKILL.md`; `CLAUDE.md`, Isolated reviewers |
| challenger | The reviewer of the substance of the thinking, never of document quality, run as `/challenge <persona> [artefact]`, whose challenges are filed in `challenges/`. | `.claude/skills/challenger-contract/SKILL.md` |
| persona | One challenger's standpoint and register, one agent file `challenger-<persona>`. | `.claude/skills/challenger-contract/SKILL.md` |
| check | The reviewer of mechanical conformance with the conventions, never of substance or quality, run as `/check <check> [slug]`, each check owning one concern. | `.claude/skills/check-contract/SKILL.md` |
| finding | The result of a critic or a check, prefix FND, with severity and category, filed in `reviews/` and settled by walkthrough. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | The result of a challenger, prefix CHL, with severity (`dealbreaker`, `major`, `minor`) and epistemic status, filed in `challenges/`. | `.claude/skills/challenger-contract/SKILL.md`, Output |
| the documentation run's report | The check's report `reviews/YYYY-MM-DD-check-documentation.md` that `/document` files with what the run could not place: the Unowned list, what did not fit, what the writers left out and every reason none recorded. | `.claude/skills/document/SKILL.md`, step 7 |

## Projects and the instance

| Term | In one line | Defined in |
|---|---|---|
| project | A directory under `projects/`, a git repository of its own that the engine does not know, of kind thought or library. | `CLAUDE.md`, Repository layout and Persistence |
| thought project | A project of kind `thought`: the chain, from a brief and an intent down to the layers it needs. | `CLAUDE.md`, Repository layout |
| library | A project of kind `library`, prefix `lib-`: material shared across projects, no chain, its documents maintained by their owner, its README a catalogue of what it holds. | `CLAUDE.md`, Repository layout and Document chain (Renders) |
| dependency (of a project) | A citation by path of another project's document, a library's among them, found by the ledger in the chain, the indexes, the recipes, the work and the research; it carries no version. | `templates/ledger.md`, Dependencies |
| project file | `project.md`: the slug, the `kind` and the `language` of a project, written once at its creation and merged as text; a fixture carries `fixture: true`. | `templates/project.md` |
| kind (of a project) | `thought`, the chain, or `library`, shared material without a chain; the `kind` field of the project file. | `templates/project.md`; `CLAUDE.md`, Repository layout |
| project outside git | A project whose directory is not the top of a repository: the forge runs no git on it, whatever repository lies above it; a property, not a defect. | `CLAUDE.md`, Persistence |
| shape of a project | The set of files a release expects, recognised by the migration script as a set of marks, one per step; a project without a project file is of the shape before the migration. | `templates/project.md`; `projects/forge/10-intent.md`, the item "A release that changes the shape of files comes with a migration" |
| migration | `/migrate [slug]` through `python scripts/forge-migrate.py`: brings a project to the shape of a release that changed the shape of files, once per project, on one clone, on the principal's word. | `.claude/skills/migrate/SKILL.md` |
| pinned fact | A fact of the project no file owns yet, a prerequisite, an install line or the public home of the repository: a bullet of the readme recipe's "Pinned facts (not rendered)" section, read by the documentation's planner and never printed. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| the security policy | `SECURITY.md`, the principal's own text, no render, no companion, no row, no check. | `projects/forge/10-intent.md`, the item "The two fixed files of the root"; `CLAUDE.md`, Repository layout |
| the code of conduct | `CODE_OF_CONDUCT.md`, the Contributor Covenant 3.0 word for word, no render. | `projects/forge/10-intent.md`, the item "The two fixed files of the root"; `CLAUDE.md`, Repository layout |
| the fixed files of the root | The security policy and the code of conduct: two files beside the renders of the root that are no render and derive from nothing in the chain. | `projects/forge/10-intent.md`, the item "The two fixed files of the root" |

## Git

| Term | In one line | Defined in |
|---|---|---|
| save | `/save`: the `light` check, then a commit and a push on whatever branch is checked out, through `forge-save.py`, no render; `--quick` leaves the check out. | `CLAUDE.md`, Persistence; `projects/forge/10-intent.md`, the item "Save and release are two commands" |
| release | `/release`: from `main` only, the engine's tests, the checks with their walkthrough, the documentation, the README and release notes, the state render, then a save with the release message and at an approved major the tag. | `.claude/skills/release/SKILL.md` |
| `--auto` | The way of `/release` that runs through without a step put to the principal and stops only at a serious thing: a repository behind or diverged, a red test, a finding that would change a position or a rule, a new instance fact in a render, and always at the tag of a major. | `.claude/skills/release/SKILL.md` |
| pull | `/pull`: looks at the remote, says the state as a fact and pulls only a clean repository that is behind; the forge never pulls or merges on its own judgement. | `.claude/skills/pull/SKILL.md` |
| major | An integer version of the forge intent, closed by the principal's word after every check, both critic lenses and one challenge have passed; tagged at its release. | `projects/forge/10-intent.md`, the item "Versioning follows the group BRD convention" |
| tag | `v<major>` at the release of an approved major, the one fixed name; any other tag is the principal's request with a free name, `/save --tag` or `/release --tag`. | `CLAUDE.md`, Persistence; `.claude/skills/release/SKILL.md`, step 6 |
| branch | Voluntary and left to git: `main` is the released line, any other is created or switched to through `forge-branch.py`, and merging is git's, by hand or by merge request. | `CLAUDE.md`, Persistence |
| way of merging | One of three ways every file of a project has, told to git by `.gitattributes`: text, merged by git and settled by a person where it conflicts; derived, `ours` at a merge and made again; immutable and unique, never in conflict. | `projects/forge/10-intent.md`, the item "Every file of a project has one of three ways of merging" |
| derived file | A file made from others and taken as `ours` at a merge and made again on `main`: the renders, the README, the release notes, CONTRIBUTING, the documentation, the state render and the published companions; the ledger among them, never in git. | `projects/forge/10-intent.md`, the item "Every file of a project has one of three ways of merging" |
| merge driver `ours` | The driver of git that keeps the local side of a derived file at a merge; unregistered, a clone falls back silently to a conflict. | `CLAUDE.md`, Persistence |
| registration of the merge driver | Done once per machine by `/setup` on the user's word, through `python scripts/forge-config.py`, in the user's global git configuration; `forge-status.py` says when it is missing. | `CLAUDE.md`, Persistence; `scripts/forge-status.py`, its header |
| step of a conflict | What follows a conflict `forge-save.py` meets and leaves standing: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording, and the finishing commands of git run on the hook's ask. | `CLAUDE.md`, Persistence |
| the hook's ask | The hook `scripts/hook-git.py` denies every write of git and names the script to use, except the few commands that finish the step of a conflict, which it puts to the principal and runs on his yes. | `CLAUDE.md`, Persistence |
| integrator | The maintainer of a hosted project, typically the principal, who merges a contributor's branch: on the server where the merge request has no conflict, on his own clone through the step of a conflict where it has. | `projects/forge/10-intent.md`, the item "One integrator and N contributors" |
| contributor | One who works on a branch of a hosted project and saves it, `/save` pushing the branch, and never writes into the integrator's clone. | `projects/forge/10-intent.md`, the item "One integrator and N contributors" |
| what waits on GitHub | The open pull requests and the unanswered discussions of a repository's origin, read through `gh` by `forge-status.py --remote` and said by the `/forge` map and `/pull` as a fact; the forge reads it only. | `scripts/forge-status.py`, its header; `projects/forge/10-intent.md`, the item "The map says what waits on the remote" |

## The tests

| Term | In one line | Defined in |
|---|---|---|
| test | One of the engine's tests in `tests/`, run with pytest through `/test` on a copy of the fixture; a project has none. | `.claude/skills/test/SKILL.md` |
| fixture | `tests/fixture`: a synthetic thought project of the current shape with a made-up subject, `fixture: true` in its project file, copied by every test and never changed by one. | `projects/forge/10-intent.md`, the item "The fixture is synthetic"; `CLAUDE.md`, Repository layout |
| CI | `.github/workflows/tests.yml`: the tests run at every push and pull request of the engine, on Linux and Windows, Python 3.8 and the newest. | `CLAUDE.md`, Repository layout |

## The documentation

| Term | In one line | Defined in |
|---|---|---|
| documentation | The pages of one topic each in `docs/`, with an index, for the user, the extender and the evaluator, generated by `/document` and never composed by hand. | `CLAUDE.md`, Document chain (Documentation) |
| documentation map | `docs-map.md` beside the owning project's ledger: one entry per page with everything the page is made from, written by the planner and never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md`, The map |
| page | A page of the documentation, or its index: one topic and one kind, generated, never a source of truth, overwritten by the documentation run. | `CLAUDE.md`, Document kinds |
| index | `docs/README.md`, derived by `python scripts/docs-index.py` from the map: every page with its line and each reader's path through them. | `.claude/skills/document/SKILL.md`, step 5; `.claude/agents/docs-planner.md` |
| how-to | A kind of page that carries what the person does, step by step, and what he sees; practical, never the reasons. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| explanation | A kind of page that carries what a thing is, how it works and why it is so, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| reference | A kind of page that states facts in the structure of what it mirrors, free of interpretation, and never explains. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| mirrored | Said of a page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| derived | Said of a page that puts together what no single file says, from evidence in several, by the reasoning its entry gives. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| Unowned | The section of the documentation map listing every fact a page needs and no file supports, with the page that needs it. | `.claude/agents/docs-planner.md`, The map |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
