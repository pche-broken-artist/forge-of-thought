---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: fc759b426a8f2462
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
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
  - .claude/skills/release/SKILL.md
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

This page gives every term of the forge in one line, with the file that defines it, for the user, the extender and the evaluator. The forge is the workshop described in [What the forge is and is not](../about/what-it-is-and-is-not.md). A term that is a command or a path is written as the owner writes it.

## People, tool and installation

| Term | Meaning | Defined in |
|---|---|---|
| principal | The person whose thinking is being forged, who supplies ideas, answers and decisions and has final authority on all content. | `CLAUDE.md` |
| recipients | Those who receive an assignment: teams, colleagues or the principal's future self. | `CLAUDE.md` |
| Claude | The cognitive extension of the principal, which owns structure, order, process discipline and document hygiene, and proposes but never decides. | `CLAUDE.md` |
| Claude Code | The agent for the command line in which the forge runs, whose slash commands, skills, agents and hooks are the forge's mechanisms. | `CLAUDE.md` |
| session | One run of Claude Code from its start to its end, whose conversation is lost when it ends unless it was written to a file. | `CLAUDE.md` |
| harness | The part of Claude Code around Claude that enforces the principal's word where it can, for instance by guarding commands and sensitive paths. | `projects/forge/10-intent.md` (the position on the harness) |
| session model | The one model the whole forge runs on, chosen once and inherited by every subagent, so that speed is bought with context and never with a weaker reviewer. | `CLAUDE.md` |
| instance | One installation of the forge. | `.claude/skills/docs-contract/SKILL.md` |
| instance fact | A fact of one installation, such as who the principal is, the conversation language or the handle records are signed with, kept in `CLAUDE.local.md` and never in the engine. | `projects/forge/10-intent.md` (the position on instance facts) |
| engine (the forge's) | The repository of the forge itself, with its rules, skills, agents, templates and scripts, as against the projects under `projects/`. | `projects/forge/10-intent.md` (the position on instance facts) |
| engine (of a model family) | A model of another family reached through one row of the engine table of `scripts/forge-engine.py`, of which `antigravity` is the one row today. | `scripts/forge-engine.py` |
| engine and tier against model and version | The forge names engines and tiers and never models or versions, so that a name always means the newest of its kind and nothing changes when a new version arrives. | `projects/forge/10-intent.md` (the position on the link to another engine) |
| second engine | An engine of another family that reads the draft plan of a deep research and then takes every card beside the session model, asked for by name with `--engine`. | `.claude/skills/research/SKILL.md` |
| prime directive | One of the ten rules at the head of `CLAUDE.md` that hold in every conversation. | `CLAUDE.md` |
| working method | A named way a working conversation runs, none of them a command, each applying whenever its situation arises. | `CLAUDE.md` |
| manual | The forge's own help, `/man` or `/manual`, which reads its answers from the files that own them and has no text of its own. | `.claude/skills/man/SKILL.md` |

## Documents and the chain

| Term | Meaning | Defined in |
|---|---|---|
| document | Every file of a project, each having one kind that says who writes it, whether it is versioned and how it behaves. | `CLAUDE.md` |
| artefact | A document of the chain, composed by the principal with Claude and rewritten freely. | `CLAUDE.md` |
| layer | One kind of artefact in the chain, which a project takes only if it needs it and which is added without reworking what exists. | `CLAUDE.md` |
| brief | The principal's idea put together, rough on purpose, `00-brief.md` or a later `00-brief-<name>.md`, in which nothing is yet a position. | `.claude/skills/forge/states/brief.md` |
| intent | `10-intent.md`, the working document that holds the consolidated current state of what the principal holds, rewritten for coherence each round. | `.claude/skills/forge/states/intent.md` |
| position | What the principal currently holds or wants, an item of the intent. | `projects/forge/10-intent.md` (the position on the prefix vocabulary) |
| fact | What is the case, as the principal states it or as a source states it and cites to its file, which is not a stance and is never demanded to be verified. | `projects/forge/10-intent.md` (the position on the prefix vocabulary) |
| thread | One open matter of the intent, which names the artefact it concerns and carries its origin. | `templates/thread.md` |
| thread file | The one file in `threads/` that holds a thread, whose header gives what it concerns, its origin and whether it is open, freely rewritten while open and immutable once closed. | `.claude/skills/forge/states/intent.md` |
| rejected direction | A direction the principal dropped, kept in the intent with the reason it was dropped. | `.claude/skills/forge/states/intent.md` |
| assignment | `20-assignment.md`, which carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| BRD | `30-brd.md`, which breaks the parent into business requirements, use cases and qualities that stakeholders can review and the delivery can estimate. | `.claude/skills/forge/states/brd.md` |
| business requirement | One rule of the business in a BRD, written with `shall`, testable and tracing to its parent (prefix BR). | `.claude/skills/forge/states/brd.md` |
| use case | Behaviour agreed as a sequence at user-goal level, with its actor, trigger, steps and exceptions (prefix UC). | `templates/brd.md` |
| dependency (of a BRD) | An item that names what the BRD relies on outside itself, such as a system, a project or a document (prefix DEP). | `templates/brd.md` |
| non-functional requirement | A quality of the thing named by category, whose value is the stakeholders' or an open question with an owner (prefix NFR). | `templates/brd.md` |
| parent of an item | The assignment item or the position from which a BRD item descends, cited at the end of the item. | `.claude/skills/forge/states/brd.md` |
| roster of areas | The list, kept in a library document of the instance, of the areas of the enterprise a BRD must consider and which of them are mandatory, or `Roster: none`. | `.claude/skills/forge/states/brd.md` |
| touched area | An area of the roster that a BRD either finds items for or knowingly finds not to apply, with the reason. | `templates/brd.md` |
| provenance map | The map from every item of the parent to the items that carry it, made before the items are written so that nothing of the parent is lost in silence. | `.claude/skills/forge/states/brd.md` |
| solution design | `40-solution-design.md`, which says how the things wanted are realised, part by part, with the choices they rest on and what they cost. | `.claude/skills/forge/states/solution-design.md` |
| definition | The state file of one artefact in `.claude/skills/forge/states/`, worked through `/forge <state>`, which says what the artefact is, how it is found and when it is complete. | `CLAUDE.md` |
| template | A skeleton in `templates/` that says what comes out, paired with the definition that says how to get there. | `CLAUDE.md` |
| Map (of a definition) | The block of a definition that names what must be found for the artefact to be complete, which is neither a questionnaire nor a list of headings. | `projects/forge/10-intent.md` (the Elicitation group) |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, the conversation being its medium. | `projects/forge/10-intent.md` (the Elicitation group) |
| work product | An output of the project made with work of its own, held in two files in `work/`, the content and beside it the specification. | `.claude/skills/work/SKILL.md` |
| specification | The file `work/<name>.spec.md` of a work product, which holds the way and the why: the task, its inputs, the method, the assumptions and what is open. | `.claude/skills/work/SKILL.md` |
| mined | Said of a brief whose substance the principal has carried into the intent, recorded as pending, partial, mined or dropped. | `templates/history.md` |
| immutable | Never edited after creation or registration, as reviews, challenges, sources, research and closed threads are. | `CLAUDE.md` |

## Working methods

| Term | Meaning | Defined in |
|---|---|---|
| walkthrough | A list of items needing the principal's decision worked one item per message, in order of weight, each item closed with the verdict line. | `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item: accept, modify, question, reject or park, and where an item no longer applies, obsolete. | `.claude/skills/walkthrough/SKILL.md` |
| verdict line | The line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark` that closes every proposition put to the principal for a decision. | `.claude/skills/walkthrough/SKILL.md` |
| round | One working conversation over the intent or open items, carried in the conversation and written once at its end as one version bump. | `CLAUDE.md` |
| write | The principal's word that ends a round, on which Claude reflects the round back and writes everything agreed once. | `.claude/skills/walkthrough/SKILL.md` |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | The append-only file `<file>.history.md` beside a versioned document, which holds what changed in it and why. | `templates/history.md` |
| record | One line of a history: date, version, author, subject, kind, and where it applies the reason, the action and the wording that ceased to hold. | `templates/history.md` |
| record of state | A record that carries the current state of something, such as the mining of a brief, a settled finding or the state of a work product, without raising the version. | `templates/history.md` |
| archive | A file kept immutable from the day it was made: a history table from before the log in `<file>.history.archive.md`, or the hand-kept ledger in `ledger.archive.md`. | `templates/history.md` |
| ledger | The single source of truth for the state of a project, built from the documents and never kept in git. | `templates/ledger.md` |
| made at read time | Said of the ledger, which `scripts/forge-ledger.py` builds whenever it is read, so that no one writes a row and no two people merge it. | `projects/forge/10-intent.md` (the position on the ledger) |
| Waiting on principal | The section of the ledger that lists by rule what waits for the principal: open threads, open questions he owns, open findings of a critic, open challenges and parked matters. | `templates/ledger.md` |
| Reports | The section of the ledger, present only when needed, that lists what merged files cannot say, such as an ID defined twice or a closed thread touched by a later commit. | `templates/ledger.md` |
| decision | One record of the principal's decision in `decisions.md`, append-only, with its reason, its date and where it rules on a finding or a challenge its verdict. | `templates/decisions.md` |
| Verdict line (of a decision) | The line of a decision record that rules on a finding or a challenge, reading that the item is rejected, parked until something, or obsolete. | `templates/decisions.md` |

## Sources and research

| Term | Meaning | Defined in |
|---|---|---|
| source | External input as it arrived, kept in `sources/`, immutable, in one form: text, or a functional binary. | `CLAUDE.md` |
| bundle | A set of related files in `sources/<slug>/` that counts as one source with one ledger entry and an index of its own. | `CLAUDE.md` |
| growing bundle | A bundle of one origin that keeps arriving, to which `/ingest --bundle <name>` adds files one by one, each immutable from its own registration. | `.claude/skills/ingest/SKILL.md` |
| extract | The Markdown that `scripts/doc2md.py` makes from a binary on the principal's word, which then is the source. | `.claude/skills/ingest/SKILL.md` |
| resource index | The file `00-INDEX.md` in every `sources/` and `research/` directory, a light catalogue that is freely rewritten and tracks nothing. | `CLAUDE.md` |
| Role | The field of a source's index entry that says what the source is for, asked of the principal before the entry is written. | `.claude/skills/ingest/SKILL.md` |
| research | A durable answer to a question about the world outside, kept in `research/`, either one note or a bundle. | `.claude/skills/research/SKILL.md` |
| research note | The answer to one card from one engine, filed as `<card>.<engine>.md` in English and immutable from its filing. | `templates/research.md` |
| research bundle | The directory `research/YYYY-MM-DD-<topic>/` that holds one research of several cards, with the plan and the synthesis at its head and one note per card per engine. | `.claude/skills/research/SKILL.md` |
| plan (of a research) | The purpose, perspectives, assumptions, exclusions, cards and agents of a research, shown and confirmed by walkthrough before anything is searched. | `templates/research-plan.md` |
| card | One question answered by one kind of evidence from one kind of source. | `.claude/skills/research/SKILL.md` |
| perspective | A standpoint from which the topic of a research is looked at, with the cards that serve it or none. | `templates/research-plan.md` |
| disconfirming query | One search written to find the opposite of what the card expects, whose result is reported even when it is nothing. | `templates/research-plan.md` |
| stop rule | The condition that ends a card's search: nothing new from a differently worded query and a primary source for every perspective, within an opening budget. | `templates/research-plan.md` |
| quick and deep | The two depths of a research: quick is one card on the session model alone, filed as one note, and deep is the confirmed plan with one isolated agent per card, filed as a bundle. | `.claude/skills/research/SKILL.md` |
| synthesis | Claude's account made from the notes alone, with completeness card by card, the engines' answers side by side, what was unexpected, what was not found and its own view last and apart. | `templates/research-plan.md` |
| citation check | The opening of every URL of a note by `scripts/forge-cite.py` before it is filed, which sends back a note with a dead or mismatched citation and never counts a refused page as a failure. | `scripts/forge-cite.py` |
| independence of engines | The measure, by the URLs and sentences two engines' notes share, of whether a second note was written from the web and not from the first. | `scripts/forge-cite.py` |
| packet | The folder with `packet.md`, the whole context of one run on an engine, composed from the forge's own definition. | `scripts/forge-engine.py` |
| run folder | The folder `tmp/research/<run>/` that keeps the packets, envelopes and profile of one research run for inspection. | `scripts/forge-engine.py` |
| profile | The copy of the user's settings that `scripts/forge-engine.py` gives an engine for one run, with the forge's tree and the shell denied and the web allowed. | `scripts/forge-engine.py` |
| envelope | The structured answer of an engine's run, saved beside its packet as `envelope.json`. | `scripts/forge-engine.py` |
| working folder | `tmp/`, the engine's one folder for packets, task files and dry results, in git without its contents, and no source of truth. | `tmp/README.md` |

## Projects and their files

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory under `projects/` that is a repository of its own, of kind thought or library. | `CLAUDE.md` |
| project file | The file `project.md`, written once at the creation of a project, which holds its slug, kind and language. | `templates/project.md` |
| kind (of a project) | Whether a project is a thought project with a chain or a library without one, said by the project file. | `templates/project.md` |
| thought project | A project of kind thought, which holds the chain from the brief on. | `CLAUDE.md` |
| library | A project of kind library, named with the prefix `lib-`, that has no chain and holds documents maintained by their owner for use across projects. | `CLAUDE.md` |
| dependency (of a project) | A citation of another project's document, such as a library's, which the ledger registers without a version. | `templates/ledger.md` |
| project outside git | A project in `projects/` that is not the top of a repository, on which the forge runs no git, which is a property and not a defect. | `CLAUDE.md` |

## Renders and recipes

| Term | Meaning | Defined in |
|---|---|---|
| recipe | The versioned file in `recipes/` that says how a render is made: its inputs, audience, instructions and output template. | `CLAUDE.md` |
| render | An audience-specific output generated from the chain by `/render`, never a source of truth and never edited by hand. | `.claude/skills/render/SKILL.md` |
| plain file | The file `/render` makes beside a render through the script of the format its recipe names, deterministic and cheap. | `CLAUDE.md` |
| format file | The plain file a recipe's Format section names, such as a deck, a document, a video or the events of a player. | `projects/forge/10-intent.md` (the position on the engine hosting what a project shows) |
| published file | The designed `.pptx` or `.docx` that `/publish` makes from a render through a model, only on the principal's command. | `.claude/skills/publish/SKILL.md` |
| published companion | The file `published/<recipe>.md` that records the provenance of a published file, whose state of current or stale is computed and never written. | `.claude/skills/publish/SKILL.md` |
| principal's own file | A file in `renders/` or `published/` that no recipe names, made by hand from the forge's files and kept in git with no companion, row or check. | `projects/forge/10-intent.md` (the position on the principal's own files) |
| genre | A kind of recipe that `/recipe <genre>` composes through an interview from a skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md` |
| screenplay | A genre that renders a terminal conversation as scenes with captions, made into a video or into the events of a player. | `projects/forge/10-intent.md` (the position on the screenplay and its player) |
| player page | The page `docs/videos/index.html`, written anew by `scripts/md2video.py` from `templates/html-player.html` whenever a file is written into the folder. | `projects/forge/10-intent.md` (the position on the engine hosting what a project shows) |
| public folder | `docs/videos/` of the engine, the one public place of an instance, flat and left alone by `/document`. | `projects/forge/10-intent.md` (the position on the engine hosting what a project shows) |
| primary render | The render in the first language that a recipe's `languages:` declares, from which the others are translated. | `projects/forge/10-intent.md` (the position on rendering in several languages) |
| translation | A render in another declared language, made from the primary render scene for scene and line for line, citing it. | `.claude/skills/render/SKILL.md` |
| provenance | The front-matter a render opens with: its project, recipe and version, date and the inputs with their versions. | `.claude/skills/render/SKILL.md` |
| stale | Said of a render when a version its provenance cites differs from the current one or a cited file is gone, and of a published file when its render is newer or missing. | `.claude/skills/render/SKILL.md` |
| state render | The ledger as a tracked render, `renders/state.md`, written by `/release` on `main`. | `.claude/skills/release/SKILL.md` |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| critic | The reviewer of the quality of the documents as documents and never of the substance, run by `/critique`. | `.claude/skills/critic-contract/SKILL.md` |
| lens | The angle of one critic, held in one agent file named `critic-<lens>`. | `.claude/skills/critic-contract/SKILL.md` |
| challenger | The reviewer of the substance of the thinking and never of the quality of the documents, run by `/challenge`. | `.claude/skills/challenger-contract/SKILL.md` |
| persona | The register of one challenger, held in one agent file named `challenger-<persona>`. | `.claude/skills/challenger-contract/SKILL.md` |
| check | The reviewer of mechanical conformance with the conventions and never of substance or quality, run by `/check`. | `.claude/skills/check-contract/SKILL.md` |
| finding | The result of a critic or a check, with a severity, which is advisory and settled by walkthrough. | `.claude/skills/check-contract/SKILL.md` |
| challenge | The result of a challenger, with a severity and an epistemic status, settled by walkthrough. | `.claude/skills/challenger-contract/SKILL.md` |
| documentation run's report | The check's report filed in `reviews/` by `/document` for what the run could not place, such as a fact with no owner or a reason no file records. | `.claude/skills/document/SKILL.md` |
| contract | The skill that owns what every member of one kind of reviewer or documentation agent shares, preloaded into each agent file. | `.claude/skills/check-contract/SKILL.md` |
| Lens section | The one part of an agent file that is its own, a specialisation of its contract that never replaces a shared rule. | `.claude/skills/check-contract/SKILL.md` |
| subagent | A helper that Claude launches for one task, with a context of its own. | `CLAUDE.md` |
| isolated subagent | A subagent that sees nothing of the conversation, reads every input from disk in its own run and lets no instance fact into what it returns. | `CLAUDE.md` |
| isolation | The condition under which an isolated subagent works, so that its result is derived from the documents and not from what was said about them. | `CLAUDE.md` |

## Git and releases

| Term | Meaning | Defined in |
|---|---|---|
| save | `/save`, which runs the light check and then commits and pushes on the branch checked out, with no render, and with `--quick` leaves the light check out. | `CLAUDE.md` |
| release | `/release`, run from `main` only: checks, documentation, README and release notes, state render and then a save with the release message. | `.claude/skills/release/SKILL.md` |
| `--auto` | The option of `/release` that runs the whole release through, stopping only at a serious thing and always at the tag of a major. | `.claude/skills/release/SKILL.md` |
| pull | `/pull`, which looks at the remote and says the state as a fact, and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| migration | `/migrate`, run once per project on one clone and on the principal's word, which brings a project to the shape of a release that changed the shape of files. | `.claude/skills/migrate/SKILL.md` |
| shape of a project | The set of marks, one per migration step, by which the migration script recognises how far a project is brought. | `.claude/skills/migrate/SKILL.md` |
| major | An approved intent version that is an integer, whose release takes the tag `v<major>` on the principal's word. | `.claude/skills/release/SKILL.md` |
| tag | A name on a commit: `v<major>` at a major, and any other only on the principal's request. | `.claude/skills/release/SKILL.md` |
| branch | A line of work beside `main`, which a contributor saves and which is switched or created through `scripts/forge-branch.py`. | `CLAUDE.md` |
| way of merging | One of the three ways every file of a project is merged, text, derived, or immutable and unique, as the forge tells git. | `projects/forge/10-intent.md` (the position on the ways of merging) |
| derived file | A document for a reader made from other files, such as a render, the README, the documentation or a published file, kept in git, made only on `main` and taken as `ours` at a merge. | `projects/forge/10-intent.md` (the position on the ways of merging) |
| merge driver `ours` | The git setting that keeps this side's version of a derived file at a merge, so that the file is made again afterwards. | `CLAUDE.md` |
| registration of the merge driver | The step by which `/setup` registers `ours` once per machine, on the user's word, in the global git configuration. | `CLAUDE.md` |
| step of a conflict | The settling of a conflict `forge-save` leaves standing, in which Claude lays both sides out as a walkthrough, the principal decides and the finishing git commands run on the hook's ask. | `CLAUDE.md` |
| the hook's ask | The question the hook `scripts/hook-git.py` puts to the principal for the few git commands that finish a step of a conflict, which run on his yes. | `CLAUDE.md` |
| integrator | The maintainer, typically the principal, who merges contributors' branches, on the server where there is no conflict and on his own clone where there is. | `projects/forge/10-intent.md` (the position on one integrator and N contributors) |
| contributor | A person who works on a branch and saves it, and never writes into the integrator's clone. | `projects/forge/10-intent.md` (the position on one integrator and N contributors) |
| guarded command | A command that writes, scaffolds, commits or regenerates, which the harness keeps Claude from starting on its own judgement so that the principal invokes it by slash. | `projects/forge/10-intent.md` (the position on the harness) |

## Documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | The set of pages in `docs/`, one topic each, with an index, generated by `/document` and never composed or maintained by hand. | `.claude/skills/document/SKILL.md` |
| documentation map | The file `docs-map.md` beside the owning project's ledger, with one entry per page and everything a page is made from, never shown to the reader. | `CLAUDE.md` |
| page | One page of the documentation, with one topic and one kind, generated and never mended by hand. | `.claude/skills/docs-contract/SKILL.md` |
| index (of the documentation) | The page `docs/README.md`, derived by script from the documentation map, which lists every page and each reader's path. | `.claude/agents/docs-planner.md` |
| mirrored | Said of a page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md` |
| derived | Said of a page that puts together what no single file says, from evidence in several. | `.claude/skills/docs-contract/SKILL.md` |
| how-to | The kind of page that carries what the person does, step by step, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md` |
| explanation | The kind of page that carries what a thing is, how it works and why, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md` |
| reference | The kind of page that states facts in the structure of what it mirrors, free of interpretation. | `.claude/skills/docs-contract/SKILL.md` |
| pinned fact | A fact of a project that no file owns yet, kept in the recipe's section `Pinned facts (not rendered)` for the documentation to read and dropped the day a file owns it. | `templates/recipe-readme.md` |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports. | `.claude/agents/docs-planner.md` |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
