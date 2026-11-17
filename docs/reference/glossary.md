---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 272ceb2400bd0f6e
inputs:
  - CLAUDE.md
  - .claude/reference/id-prefixes.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0590
  - projects/forge/10-intent.md#POS.0790
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
  - projects/forge/10-intent.md#POS.1680
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
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/user-stories.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/thread/SKILL.md
  - .claude/skills/ingest/SKILL.md
  - .claude/skills/research/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/publish/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/pull/SKILL.md
  - .claude/skills/setup/SKILL.md
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
  - templates/recipe.md
  - templates/brd.md
  - templates/user-stories.md
  - templates/research.md
  - templates/research-plan.md
  - templates/recipe-readme.md#Pinned facts (not rendered)
  - scripts/forge-engine.py
  - scripts/forge-cite.py
  - scripts/forge-status.py
  - scripts/md2video.py
  - tmp/README.md
---

# Glossary

The glossary states every term of Forge of Thought in one line, with
the file that defines the term. It is for the user, the extender and
the evaluator alike: whoever meets a word of the forge and wants its
meaning and its owner. Each line gives the term, its meaning in one
sentence and the defining file by path and section. A term with two
senses has two lines.

The terms are stated here, not explained.
[What the forge is and is not](../about/what-it-is-and-is-not.md)
tells the forge in prose.

## Roles and where the forge runs

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: the principal supplies ideas, answers and decisions and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is carried to: teams, colleagues or the principal's future self. | `CLAUDE.md`, What this workspace is |
| Claude | The cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, and it proposes and never decides. | `CLAUDE.md`, Roles |
| Claude Code | The agent for the command line in which the forge runs: its slash commands, skills, agents and hooks are the mechanisms, and the forge is what they are told. | `CLAUDE.md`, What this workspace is |

## Documents and the chain

| Term | Meaning | Defined in |
|---|---|---|
| document | Every file of a project: each document has one kind, which says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain: composed by the principal with Claude, versioned and rewritten freely. | `CLAUDE.md`, Document kinds |
| layer | One numbered artefact of the chain: below the intent a project takes the layers it needs, and none is a condition of another. | `CLAUDE.md`, Document chain |
| definition | The state file of an artefact (`.claude/skills/forge/states/<state>.md`), worked through `/forge <state>`: it says what the artefact is and how it is found, and it owns the artefact's rules. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| template | A canonical file of `templates/` from which a new file is made: paired with a definition, it says what comes out. | `CLAUDE.md`, Templates and Document chain |
| the line that names a template | The comment `<!-- Shape: templates/<name>.md -->`: the one comment of its template that a file made from it keeps. | `CLAUDE.md`, Templates |
| Map (of a definition) | The block of a definition that names what must be found for the artefact to be complete: neither a questionnaire nor the headings of the document. | `projects/forge/10-intent.md`, Elicitation |
| brief | The artefact `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking: the principal's idea put together, what is wanted and why, in free form without IDs and rough on purpose. | `.claude/skills/forge/states/brief.md`, Target and Aim |
| intent | The artefact `10-intent.md`, present in every chain: the consolidated current state of what the principal holds, rewritten for coherence each round and never finished. | `.claude/skills/forge/states/intent.md`, Aim; `projects/forge/10-intent.md`, Document chain |
| assignment | The artefact `20-assignment.md`: the in-scope substance of the intent carried to the recipients, complete and precise enough for them to act without the principal in the room. | `.claude/skills/forge/states/assignment.md`, Aim |
| BRD | The artefact `30-brd.md` (the business requirements, below the assignment and above the solution design): the parent broken into rules, behaviour and qualities that the stakeholders can review and the delivery teams can estimate. | `.claude/skills/forge/states/brd.md`, Aim |
| solution design | The artefact `40-solution-design.md`: how the things wanted are realised, part by part, with the choices the parts rest on, kept current. | `.claude/skills/forge/states/solution-design.md`, Aim |
| prefix of two or three letters | The letters before the dot of an ID in the format `PREFIX.NNNN`: the prefix says what an item is, and the table of prefixes gives each prefix its meaning and the place its items live in. | `CLAUDE.md`, ID scheme; `.claude/reference/id-prefixes.md` |

## The intent and its threads

| Term | Meaning | Defined in |
|---|---|---|
| position | An item with the prefix `POS`: what the principal currently holds or wants and why, with the brief or the source it comes from, dated once. | `.claude/reference/id-prefixes.md`; `projects/forge/10-intent.md`, Document chain |
| fact | An item with the prefix `FCT`: what is the case, as the principal states it or as a source cited to its file states it; a fact is not a stance, and verification is never demanded. | `.claude/reference/id-prefixes.md`; `projects/forge/10-intent.md`, Structure and style of an assignment |
| rejected direction | An item with the prefix `REJ`: a direction that was dropped, kept in the intent with the reason it was dropped. | `.claude/reference/id-prefixes.md` |
| thread | One matter of a project set aside to be taken up later (a task, a question, a decision to make or an idea), with the prefix `THR` and born only on the principal's command. | `.claude/skills/thread/SKILL.md` |
| thread file | The one file a thread lives in, in the project's `threads/` and named by the thread's ID: its header is the thread's state, and it is freely rewritten while open and immutable once closed. | `templates/thread.md`; `projects/forge/10-intent.md`, Document chain |
| priority of a thread | The header field `priority` of a thread (`high`, `medium` or `low`): it says when the matter is taken up, not how much it binds, and a thread without it is read as medium. | `.claude/skills/thread/SKILL.md`, The header |
| mined | Said of a brief that has been worked into the intent on the principal's word: the ledger shows how far as `pending`, `partial`, `mined` or `dropped`. | `.claude/skills/forge/states/brief.md`, Aim; `templates/ledger.md`, Briefs |

## Requirements: the assignment and the BRD

| Term | Meaning | Defined in |
|---|---|---|
| obligation in the indicative | The wording of a requirement as a full sentence in the indicative, in English `shall` or `shall not`: never a conditional, a permission, a wish or MoSCoW wording. | `.claude/skills/forge/states/assignment.md`, Requirement style; `projects/forge/10-intent.md`, Structure and style of an assignment |
| provenance map | A tool of the pass in which Claude drafts an artefact whole from its parent: every group with its items and the items of the parent they came from, with what of the parent landed nowhere and which items have no parent; it is not part of the artefact. | `.claude/skills/forge/states/assignment.md`, Course |
| business requirement | An item of a BRD with the prefix `BR`: one rule of the business, testable, citing the item of the parent it carries. | `.claude/reference/id-prefixes.md` |
| use case | An item of a BRD with the prefix `UC`: behaviour agreed as a sequence, at user-goal level. | `.claude/reference/id-prefixes.md` |
| dependency (of a BRD) | An item of a BRD with the prefix `DEP`: what the BRD relies on outside itself, such as another system, project or document. | `.claude/reference/id-prefixes.md`; `templates/brd.md`, Dependencies |
| non-functional requirement | An item of a BRD with the prefix `NFR`: a quality by category, its value given by the stakeholders or left as an open question. | `.claude/reference/id-prefixes.md` |
| parent of an item | The item of the layer above that a BR or a UC cites: a `REQ` of the assignment, or a `POS` of the intent where the project has no assignment; an NFR without a parent cites its category. | `.claude/skills/forge/states/brd.md`, Inputs and Requirement style |
| roster of areas | The areas of the enterprise a BRD must consider, with which of them are mandatory: a library document of the instance, cited by path, and `Roster: none` in a project with no enterprise around it. | `.claude/skills/forge/states/brd.md`, Inputs |
| touched area | An area of the roster as a BRD records it: found, with the items that carry it, or not applicable, with the reason. | `templates/brd.md`, Touched areas of the enterprise |

## User stories

| Term | Meaning | Defined in |
|---|---|---|
| user story | An item with the prefix `US` in the artefact `35-user-stories.md`: behaviour seen from outside, one function as the one who uses it meets it, with its acceptance criteria. | `.claude/skills/forge/states/user-stories.md`, Aim and Story style |
| acceptance criterion | A bullet of a story in the indicative, present tense, one behaviour per bullet: what happens in the usual course, worded in a form that can be tested. | `.claude/skills/forge/states/user-stories.md`, Story style |
| edge case | A situation at the border of a story's behaviour, such as a failure, a missing datum or a change during use, written as `situation → what happens`. | `.claude/skills/forge/states/user-stories.md`, Story style |
| Reference (of a story) | The one part every story has: the BR, NFR, UC or DEP the story serves, or the `POS` in a small change without a BRD. | `.claude/skills/forge/states/user-stories.md`, Story style |
| Story style | The rules of wording that close the definition of the user stories: one function per story, criteria in the indicative, no vague word, fixed English labels and no technical solution, priority or estimate. | `.claude/skills/forge/states/user-stories.md`, Story style |
| the cut | What Claude returns first when the stories are handed over: the name of every story with a short description of what it covers, and the items of the parent no story serves; the stories are drafted once the principal has agreed it. | `.claude/skills/forge/states/user-stories.md`, Course |
| the export of the stories | A render of the genre `user-stories-export` that the instance hands over: one heading per story with its parts on lines of their own and no reference to a position of the intent. | `projects/forge/10-intent.md`, Document chain; `.claude/skills/forge/states/user-stories.md`, Instruments |

## The working conversation

| Term | Meaning | Defined in |
|---|---|---|
| working method | One of the named ways a working conversation runs, such as the walkthrough or handing over: none is a command, and a method applies whenever its situation arises. | `CLAUDE.md`, Working methods |
| prime directive | One of the numbered rules that `CLAUDE.md` lists under Prime directives, from "When unsure, ask" to "One mechanism lives in one place". | `CLAUDE.md`, Prime directives |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds: the conversation is its medium, and the interview, research and sources are its instruments. | `projects/forge/10-intent.md`, Elicitation |
| walkthrough | The working method for any list of items that needs the principal's decision: one item per message, in order of weight, each closed with the verdict line, the verdicts carried to one write at the end of the round. | `CLAUDE.md`, Working methods; `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item of a walkthrough or to a step that needs consent, given on the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`; `obsolete` is a further verdict, typed in full. | `.claude/skills/walkthrough/SKILL.md`, The verdict |
| round | One working conversation as a whole iteration: what is agreed is carried in the conversation and written once at its end, as one version bump. | `CLAUDE.md`, Working methods and Prime directives |
| write | The word `write`: on it Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round; written always means a file. | `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write; `CLAUDE.md`, Prime directives |
| guarded command | A command that changes files the moment it runs, with no round and no `write` in between, such as `/save`, `/release`, `/render` or `/document`: it starts on the principal's word and never on Claude's judgement. | `projects/forge/10-intent.md`, Operating environment |
| manual | `/man` (alias `/manual`): a reader of the forge's own definitions and never a text of its own, which prints the overview, one command, one working method or the way the forge has for a need said in free words. | `.claude/skills/man/SKILL.md` |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | `<file>.history.md`: the append-only file beside every versioned document that keeps its history, the body of the document being the current state and the companion the record. | `CLAUDE.md`, Versioning & status |
| record | One line of a history companion for one change, appended and never rewritten: the date, the version, the author, the subject, the kind and the reason. | `templates/history.md` |
| record of state | A record that carries the current version and does not raise it: the mining of a brief, a finding or a challenge settled, the state of a work product. | `templates/history.md` |
| archive | A file kept as it stood and immutable: `ledger.archive.md`, the hand-kept ledger at the migration, and `<file>.history.archive.md`, a history table from before the log. | `CLAUDE.md`, Repository layout; `templates/ledger.md` |
| decision | A record of the append-only `decisions.md` with the prefix `DEC`: what the principal decided and why; a later decision supersedes it by a new record that names it. | `templates/decisions.md` |
| Verdict line (of a decision) | The line of a decision that rules on a finding or a challenge, one per ID: rejected, parked until a named condition, or obsolete. | `templates/decisions.md` |
| ledger | `ledger.md`: the single source of truth for the state of a project, built from the documents by `python scripts/forge-ledger.py <slug>`, with no row written by anybody. | `CLAUDE.md`, Ledger |
| made at read time | Said of the ledger: it is built from the documents whenever it is read and is never kept in git. | `projects/forge/10-intent.md`, Versioning and state; `CLAUDE.md`, Ledger |
| Waiting on principal | The section of the ledger that lists what waits on the principal, one line per matter: the open threads, the open questions the principal owns, the open findings of a critic, the open challenges and the parked ones with their decision. | `templates/ledger.md`, Waiting on principal |
| Reports | The section of the ledger for what the merged files cannot say, found by the ledger script and present only when there is something: an ID defined twice, a closed thread touched by a later commit, a thread cited that has neither a file nor a closed record. | `templates/ledger.md`, Reports |
| immutable | Never edited once it stands: a review, a challenge and a research from their creation, a source from its registration and a thread from its closing; corrections happen downstream. | `CLAUDE.md`, Versioning & status and Document kinds |
| major | An approved integer version: a major of the forge intent closes a set of features the principal names and passes more than a minor before its tag. | `projects/forge/10-intent.md`, Versioning and state |
| tag | A git tag taken at a save or a release: `v<major>` at an approved major is the one fixed name, and any other tag is taken on request with `/save --tag` or `/release --tag`. | `projects/forge/10-intent.md`, Operating environment; `.claude/skills/release/SKILL.md`, step 6 |

## Sources and research

| Term | Meaning | Defined in |
|---|---|---|
| source | An external input as it arrived, such as a transcript, an offer, a document or a standard: kept in `sources/` and immutable once registered. | `CLAUDE.md`, Document kinds and Document chain |
| bundle | A set of related files stored as `sources/<slug>/`: one source with one index entry, which points to the bundle's own index. | `.claude/skills/ingest/SKILL.md`, step 1 |
| growing bundle | A bundle of one origin that keeps arriving, named with `--bundle <name>`: each new file is stored inside it with its own entry in the bundle's index and is immutable from its own registration. | `.claude/skills/ingest/SKILL.md`, step 1 |
| extract | The Markdown that `scripts/doc2md.py` makes from a binary file: the extract is then the source, registered, indexed and immutable. | `.claude/skills/ingest/SKILL.md`, step 3 |
| resource index | `00-INDEX.md` in every `sources/` and `research/` directory: a light catalogue of what resources exist and what they are for, which tracks no state and is an automatic input of no command. | `CLAUDE.md`, Document chain |
| Role | The free-text field of a source's index entry that says what the source is for: the principal's word, asked before the entry is written. | `.claude/skills/ingest/SKILL.md`, step 4 |
| research | A durable answer to one question, made by `/research` and kept immutable in `research/`: one question is a research note, several questions are a research bundle. | `CLAUDE.md`, Document kinds |
| research note | The file that answers one card on one engine, in English and immutable from its filing: `<card>.<engine>.md` in a bundle, or `research/YYYY-MM-DD-<topic>.md` where the research is one card on one engine. | `templates/research.md`; `.claude/skills/research/SKILL.md`, Target |
| research bundle | The directory `research/YYYY-MM-DD-<topic>/` of a research of several cards: `00-plan.md` at its head with the plan as confirmed and the synthesis, and one note per card per engine. | `.claude/skills/research/SKILL.md`, Target |
| plan (of a research) | What `/research` shows before anything is searched and the principal confirms in a walkthrough: the purpose, the perspectives, the assumptions, what is left out, the cards and the agents. | `templates/research-plan.md`, Plan; `projects/forge/10-intent.md`, Research |
| card | One question of a research plan, answered by one kind of evidence from one kind of source. | `.claude/skills/research/SKILL.md`, Course, step 2 |
| perspective | A standpoint from which the topic of a research is treated, listed in the plan with the cards that serve it or with "no card". | `templates/research-plan.md`, Perspectives |
| disconfirming query | The field of a card that holds one search written to find the opposite of what is expected: the note reports what it found, including nothing. | `templates/research-plan.md`, Cards |
| stop rule | The field of a card that says when searching ends: nothing new from a differently worded query, a primary source for every perspective of the card, and the opening budget. | `templates/research-plan.md`, Cards |
| quick and deep | The two depths of a research: `--quick` is one card on the session model, filed as a single note; `--deep` is a plan of several cards, one isolated agent per card and a bundle with a synthesis. | `.claude/skills/research/SKILL.md`; `projects/forge/10-intent.md`, Research |
| synthesis | Claude's reading of a deep research, made from the notes alone when every note has returned: completeness card by card, the engines' answers side by side, the unexpected and the not found gathered, and Claude's own view last and apart. | `.claude/skills/research/SKILL.md`, Course, step 7; `templates/research-plan.md`, Synthesis |
| citation check | The check before a research note is filed: `scripts/forge-cite.py` opens every URL the note cites and compares every paper identifier with the title the note gives it. | `scripts/forge-cite.py`, header; `projects/forge/10-intent.md`, Research |

## Engines

| Term | Meaning | Defined in |
|---|---|---|
| engine (the forge's) | The one git repository a user clones: the universal core in its root and no project. | `projects/forge/40-solution-design.md`, Persistence; `CLAUDE.md`, The system's own project |
| engine (of another model family) | A model of another family, reached over that engine's own command-line tool: each engine is one row of the engine table of `scripts/forge-engine.py`, which holds `antigravity` today. | `scripts/forge-engine.py`, header; `projects/forge/10-intent.md`, Research |
| engine and tier, model and version | The forge names engines and tiers and never models or versions: a name always means the newest of its kind, and the version is resolved by the engine's own tool at the call. | `projects/forge/10-intent.md`, Research |
| second engine | An engine named with `/research --deep --engine <name>`: it reads the draft plan before the walkthrough and then takes every card, on the same packet as the agent of the session model. | `.claude/skills/research/SKILL.md`; `projects/forge/10-intent.md`, Research |
| independence of engines | That two engines' notes on one card were each written from the web and not from each other: measured before filing by the URLs and the sentences the notes share, never assumed. | `scripts/forge-cite.py`, header; `projects/forge/10-intent.md`, Research |
| packet | `packet.md` in a folder of its own, the whole context of one research agent and the same for every engine: the card, the agent's brief, the shape of the note and the list of the attached notes, with nothing of the conversation. | `.claude/skills/research/SKILL.md`, Course, step 5 |
| run folder | `tmp/research/YYYY-MM-DD-<topic>/`: the folder of one research run, with its packets, envelopes and profiles, kept for inspection. | `.claude/skills/research/SKILL.md`, Course, steps 3 and 8 |
| profile | The settings `scripts/forge-engine.py` gives another engine for one run: a copy of the machine's own settings for that tool with what the engine may read and do denied, kept in the run folder while the settings themselves stay untouched. | `scripts/forge-engine.py`, header |
| envelope | The JSON answer of one run of another engine, with its status, its response and its usage, saved beside the packet as `envelope.json`. | `scripts/forge-engine.py`, header |
| working folder | `tmp/` at the engine root: the one working folder of the forge; the folder is in git, its contents never are, and nothing in it is a source of truth. | `tmp/README.md`; `projects/forge/10-intent.md`, Operating environment |

## Renders, published files and work products

| Term | Meaning | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`: the one versioned file that says how a render is made, with its inputs, audience, instructions and output template. | `CLAUDE.md`, Document chain |
| genre | A kind of recipe that `/recipe` has a genre file for, such as `screenplay` or `user-stories-export`: a recipe of no genre is composed bare from `templates/recipe.md`. | `.claude/skills/render/SKILL.md`, step 1; `projects/forge/10-intent.md`, Elicitation |
| render | An audience-specific output generated from the chain by `/render <recipe>`: never a source of truth, never edited by hand and overwritten at the next run. | `CLAUDE.md`, Document chain |
| provenance | The YAML front-matter a render opens with: the project, the recipe with its version, the date and every input with its version. | `.claude/skills/render/SKILL.md`, step 5 |
| stale | Said of a render when a version cited in its provenance differs from the current version of that file, or a cited file no longer exists. | `.claude/skills/render/SKILL.md`, step 5 |
| primary render | The render in the first language a recipe declares under `languages:`: the other languages are translated from it. | `projects/forge/10-intent.md`, Document chain; `templates/recipe.md` |
| translation | A render in a further language of the recipe, made from the primary render scene for scene and line for line, with a provenance of its own that names the primary render. | `.claude/skills/render/SKILL.md`, steps 3 and 5 |
| plain file | The file `/render` makes beside the Markdown render where the recipe names a format, by a script: deterministic, cheap, repeated freely and never edited by hand. | `.claude/skills/render/SKILL.md`, step 7; `templates/recipe.md`, Format |
| format file | The plain file of a screenplay render, in the format its recipe names: a video, or the timed events the player page plays. | `scripts/md2video.py`, header; `projects/forge/10-intent.md`, Document chain |
| picture | A render that is a picture, in the format its recipe names: where that is `png`, the renderer draws `renders/<recipe>.png` in the render's run, and the Markdown render carries only the provenance and a link to the picture. | `templates/recipe.md`, Format; `.claude/skills/render/SKILL.md`, step 3 |
| published file | The designed `.pptx` or `.docx` that `/publish` makes into `published/` from the render as it lies on disk, through a model: only on the principal's command. | `.claude/skills/publish/SKILL.md`; `CLAUDE.md`, Document chain |
| published companion | `published/<recipe>.md`: the provenance of a published file, that is its project, file, recipe, render, model and date of publishing. | `.claude/skills/publish/SKILL.md`, step 6 |
| the principal's own file | Any file in `renders/` or `published/` that no recipe names: made by hand from the forge's files and kept in git beside them, it has no kind, and the forge never reads, overwrites or raises it. | `projects/forge/10-intent.md`, Document chain; `CLAUDE.md`, Document kinds |
| screenplay | The render of a recipe of the genre `screenplay`: a terminal conversation as a title card, a card of what the viewer will see and scenes, each with a caption and a block of what the terminal shows. | `projects/forge/10-intent.md`, Document chain |
| player page | The one page of the engine's `docs/videos/` that plays the files of the folder: kept current with the folder by the forge and never by hand. | `projects/forge/10-intent.md`, Growth path; `scripts/md2video.py`, header |
| public folder | The engine's `docs/videos/`: the one public place, to which a project's recipe may send its format file by its `output:` path and which `/document` leaves alone. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Growth path |
| state render | `renders/state.md`: the ledger as a tracked render, written by `/release` on `main`. | `.claude/skills/release/SKILL.md`, step 5; `CLAUDE.md`, Repository layout |
| work product | An output of a project made with work of its own, neither an artefact nor a render: two files in `work/`, the file that holds the content and the specification beside it. | `.claude/skills/work/SKILL.md`; `CLAUDE.md`, Document kinds |
| specification | `work/<name>.spec.md`: the versioned file of a work product that holds the way and the why, that is the task, the inputs, the method, the assumptions, what is open and how the file is made. | `.claude/skills/work/SKILL.md`; `projects/forge/10-intent.md`, Document chain |

## Reviewers and isolation

| Term | Meaning | Defined in |
|---|---|---|
| subagent | An agent that a command launches for one job, such as a reviewer for `/critique`, a renderer for `/render` or a writer for `/document`. | `CLAUDE.md`, Isolated reviewers |
| isolated subagent | A subagent that works under isolation: a reviewer, a renderer, a documentation agent or a research agent alike. | `CLAUDE.md`, Isolated reviewers |
| isolation | What holds for every isolated subagent: it sees nothing of the conversation, reads every input from disk in its own run and lets no instance fact into what it returns. | `CLAUDE.md`, Isolated reviewers |
| critic | The reviewer behind `/critique`: it reads the quality of the documents and never the substance of the thinking. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md`, Subject |
| lens | One member of the critic: an agent file `critic-<lens>` that shares the critic's contract and owns its Lens section alone. | `.claude/skills/critic-contract/SKILL.md` |
| challenger | The reviewer behind `/challenge`: it reads the substance of the thinking and never the quality of a document. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md`, Subject |
| persona | One member of the challenger: an agent file `challenger-<persona>` with a register of its own, which shares the challenger's contract and owns its Lens section alone. | `.claude/skills/challenger-contract/SKILL.md` |
| check | The reviewer behind `/check` and each of its members (`check-<name>`): it reads mechanical conformance with the conventions of the engine, and each check owns one concern. | `.claude/skills/check-contract/SKILL.md`, Subject |
| contract | The skill that owns what every member of one kind of agent shares, preloaded into each agent: conduct and isolation, the subject and its boundary, the way of working and the shape of the output. | `CLAUDE.md`, Isolated reviewers |
| Lens section | The one section an agent file owns beside its contract: a specialisation that may narrow what is read or make a shared rule stricter and never renames, drops or duplicates a shared rule. | `CLAUDE.md`, Isolated reviewers |
| finding | A result of a critic on the quality of a document or of a check on conformance, with the prefix `FND`, given its ID when the report is filed. | `.claude/reference/id-prefixes.md`; `.claude/skills/critic-contract/SKILL.md`, Output |
| challenge | A result of a challenger on the substance of the thinking, with the prefix `CHL` and a severity of dealbreaker, major or minor. | `.claude/reference/id-prefixes.md`; `.claude/skills/challenger-contract/SKILL.md`, Output |
| the documentation run's report | What a run of `/document` could not place, filed in `reviews/` as a check's report and settled by walkthrough: a fact with no owner, a matter on which the documentation map and its owner disagree, a reason a page wants and no file records. | `.claude/skills/document/SKILL.md`, step 7; `projects/forge/10-intent.md`, Growth path |

## Projects and instances

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory `projects/<slug>/` with its project file, of the kind `thought` or `library`: under git it is a repository of its own, which the engine's repository ignores. | `CLAUDE.md`, Repository layout and Persistence (git) |
| project file | `project.md`: written once at the creation of a project, it holds the slug, the kind and the language of the project. | `templates/project.md`; `projects/forge/10-intent.md`, Document chain |
| kind (of a project) | The field `kind` of the project file: `thought` or `library`. | `templates/project.md` |
| thought project | A project of the kind `thought`: it carries the chain, from the brief and the intent down. | `CLAUDE.md`, Repository layout |
| library | A project of the kind `library` (`projects/lib-<name>/`): material shared across projects, with no chain and with documents maintained by their owner. | `CLAUDE.md`, Repository layout |
| dependency (of a project) | A citation of a document that lives in another project, a library or any other: the document is cited by path and never copied, and the ledger's Dependencies table lists the citation. | `.claude/skills/ingest/SKILL.md`, step 6; `templates/ledger.md`, Dependencies |
| project outside git | A project that is not under git: a property and not a defect; it is migrated as any other, and none of the refusals of git applies to it. | `projects/forge/10-intent.md`, Operating environment |
| the forge's own project | `projects/forge/`: Forge of Thought itself run through its own process, kept as a repository of its own beside the engine, cloned by whoever develops the engine and needed by no user. | `CLAUDE.md`, The system's own project |
| `forge` (in a command) | In the commands of git (`/save`, `/pull`, `forge-branch` and `/release`) the word names the whole, that is the engine's repository and the forge's own project beside it; in the commands over documents it names the project. | `projects/forge/10-intent.md`, Operating environment |
| instance | One installation of the forge: its facts live in `CLAUDE.local.md` at the engine root, a file kept out of the repository. | `.claude/skills/docs-contract/SKILL.md`, The voice; `CLAUDE.md`, What this workspace is |
| instance fact | A fact of one instance and not of the system, such as who the principal is, the conversation language or the handle that signs records: the engine carries none, and none reaches a report, a render or a page. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, Operating environment |
| session model | The model named in `.claude/settings.local.json`, set by `/setup`: the whole forge runs on it, the isolated reviewers included, but for the exceptions the owners name. | `.claude/skills/setup/SKILL.md`, step 2; `CLAUDE.md`, Isolated reviewers |
| shape of a project | What the migration recognises from the project itself and never from an engine version in it: a project without a project file is of the shape before the migration. | `templates/project.md`; `projects/forge/10-intent.md`, Operating environment |
| migration | The bringing of a project to the shape of a release that changed the shape of files, through `/migrate [slug]`: a dry run first, then only the missing steps on the principal's word, once per project and on one clone, with nothing committed. | `.claude/skills/migrate/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |

## Saving, releasing and merging

| Term | Meaning | Defined in |
|---|---|---|
| save | `/save` runs the `light` check and then commits and pushes on whatever branch is checked out, with no render; `/save --quick` leaves the check out. | `projects/forge/10-intent.md`, Operating environment |
| release | `/release` releases one repository from `main`: its checks with their walkthrough, the documentation, the README and the release notes, the state render, then the save with the release message and, at an approved major, the tag. | `.claude/skills/release/SKILL.md` |
| `--auto` | The option of `/release` that runs the whole release through: it asks once whether the documentation runs, stops where a thing is serious, stops once before the save and always stops at the tag of a major. | `.claude/skills/release/SKILL.md` |
| pull | `/pull` reports each repository against its origin (up to date, behind, ahead, diverged, no origin, not under git) and pulls only what is clean and behind, merging nothing. | `.claude/skills/pull/SKILL.md` |
| branch | A line of work beside `main`, which is the released line: branches are voluntary and left to git, and `/save` commits and pushes on whatever branch is checked out. | `CLAUDE.md`, Persistence (git) |
| integrator | The maintainer (typically the principal) who merges a contributor's branch: on the server where the merge has no conflict, on the integrator's own clone through the step of a conflict where it has. | `projects/forge/10-intent.md`, Operating environment; `CLAUDE.md`, Persistence (git) |
| contributor | One of several people on one project who works on a branch and saves it: `/save` pushes the branch, and the integrator merges it. | `projects/forge/10-intent.md`, Operating environment |
| way of merging | One of the three ways in which a file of a project is merged, which the forge tells git by path: text, derived, or immutable and unique. | `projects/forge/10-intent.md`, Operating environment |
| derived file | A file made from other files and never merged by hand: the ledger, which is made at read time and never in git, and the documents for a reader, which are made only on `main`, taken as `ours` at a merge and made again. | `projects/forge/10-intent.md`, Operating environment; `CLAUDE.md`, Persistence (git) |
| merge driver `ours` | The merge driver of git by which a derived file is taken as `ours` at a merge: a clone without its registration falls back to a conflict on the derived files. | `.claude/skills/setup/SKILL.md`, step 1; `scripts/forge-status.py`, header |
| registration of the merge driver | The entry of the merge driver `ours` in the global git configuration, written by `python scripts/forge-config.py --register`: offered by `/setup` once per machine, and reported by `forge-status` as ok or with the keys missing. | `.claude/skills/setup/SKILL.md`, step 1 |
| step of a conflict | The way a conflict that git leaves standing is settled: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording, and the finishing commands of git run on the hook's ask. | `CLAUDE.md`, Persistence (git) |
| the hook's ask | The question the hook `scripts/hook-git.py` puts to the principal before the few git commands that finish the step of a conflict, which run on a yes; every other write of git by Claude is denied with the name of the script to use. | `CLAUDE.md`, Persistence (git) |
| what waits on GitHub | What lies at a repository's origin outside git: the open pull requests and the discussions nobody of the repository has answered, read with `forge-status.py --remote` and said as a fact by the state map of `/forge` and by `/pull`. | `scripts/forge-status.py`, header; `projects/forge/10-intent.md`, Operating environment |

## The documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | Pages of one topic each in `docs/` with an index, generated by `/document` for the user, the extender and the evaluator and never composed by hand. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Growth path |
| documentation map | `docs-map.md`, beside the owning project's ledger: one entry per page with everything the page is made from, written by the planner and never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md`, The map |
| page | One file of the documentation: one topic and one kind, standing on its own, overwritten by the documentation run and never a source of truth. | `CLAUDE.md`, Document kinds; `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| index (of the documentation) | `docs/README.md`: every page with its one line and each reader's path through the pages, derived by a script from the documentation map. | `.claude/agents/docs-planner.md`, The outline; `.claude/skills/document/SKILL.md`, step 5 |
| mirrored | Said of a page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| derived | Said of a page that puts together what no single file says, from evidence in several files, by the reasoning its entry in the documentation map gives. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| how-to | A page that carries what the reader does, step by step where there are steps, and what the reader sees: practical, not complete, never the reasons. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| explanation | A page that carries what a thing is, how it works and why it is so: never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| reference | A page that states facts in the structure of what it mirrors, free of interpretation: it never explains. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| pinned fact | A fact of the project that no file of the project owns yet, such as a prerequisite, how a tool is installed or the public home of the repository: kept in the readme recipe's section "Pinned facts (not rendered)" and read there by the documentation's planner. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports, with the page that needs it: the writer leaves the fact out. | `.claude/agents/docs-planner.md`, The map |
| reference file read on demand | A file under `.claude/reference/` that `CLAUDE.md` names and that is read when its matter is looked for: the table of the commands, the table of the ID prefixes, the layout of the engine's root. | `CLAUDE.md`, Commands, ID scheme and Repository layout |

## The engine's own files

| Term | Meaning | Defined in |
|---|---|---|
| test | A test of the engine's scripts, kept in `tests/` beside them and run through `/test`: a project has none, and a user of the engine never runs them. | `.claude/skills/test/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |
| fixture | `tests/fixture`: a synthetic thought project of the current shape, marked `fixture: true` in its project file, on a copy of which every test works. | `projects/forge/10-intent.md`, Operating environment; `templates/project.md` |
| CI | The run of the engine's tests at every push and pull request of the engine, on Linux and Windows; a test reads nothing of the git configuration of the machine it runs on. | `projects/forge/10-intent.md`, Operating environment; `CLAUDE.md`, Persistence (git) |
| the security policy | `SECURITY.md` at the engine root: the principal's own text and no render. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Growth path |
| the code of conduct | `CODE_OF_CONDUCT.md` at the engine root: the Contributor Covenant 3.0 word for word and no render. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Growth path |
| the fixed files of the root | The two files of the engine root that are no render and derive from nothing in the chain (the security policy and the code of conduct): neither has a companion, a row or a check, and a change to either is the principal's word. | `projects/forge/10-intent.md`, Growth path |

## Words without a line

Two words the owners use have no line in this glossary: session and
harness. No file defines either, and a reference states what its
owners state. A page that needs one of the two glosses it there.

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
