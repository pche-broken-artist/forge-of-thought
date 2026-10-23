---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 35ad5ba8a15d9745
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
  - projects/forge/10-intent.md#Elicitation
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/ingest/SKILL.md
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
  - templates/recipe-readme.md#Pinned facts (not rendered)
---

# Glossary

The glossary is the list of every term of the forge, each in one
line, with the file that defines it. It is for the user who works
with the forge, the extender who adds to it and the evaluator who
wants to understand it, whenever a page uses a word without
explaining it. The forge itself is described in prose on
[What the forge is and is not](../about/what-it-is-and-is-not.md).
The principal is the person whose thinking is forged; Claude is the
AI assistant that works with the principal. Terms stand in
alphabetical order; the "Defined in" column names the owning file as
a path, and "the forge intent" is `projects/forge/10-intent.md`.

## Terms

| Term | Meaning | Defined in |
|---|---|---|
| archive | A file that keeps an older shape as it stood, immutable: `<file>.history.archive.md` holds a history table written before the log, and `ledger.archive.md` the hand-kept ledger at the migration. | `CLAUDE.md` (Versioning & status, Repository layout); `templates/ledger.md` |
| artefact | A document of the chain (brief, intent, a layer below it), versioned, written by the principal with Claude and rewritten freely. | `CLAUDE.md` (Document kinds) |
| assignment | The layer `20-assignment.md` that carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| branch | A line of work in git beside `main` (the released line), voluntary and left to git, switched or created through `scripts/forge-branch.py`. | `CLAUDE.md` (Persistence) |
| brief | The principal's idea put together in free form, rough on purpose and without IDs, in `00-brief.md` or a later `00-brief-<name>.md`, mined into the intent when the principal says so. | `.claude/skills/forge/states/brief.md` |
| bundle | A set of related files kept as one subdirectory `sources/<slug>/`, counted as one source with its own `00-INDEX.md` catalogue. | `CLAUDE.md` (Document chain, External inputs); `.claude/skills/ingest/SKILL.md` |
| challenge | One result of a challenger, about the substance of the thinking, numbered `CHL` and settled by walkthrough. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/challenger-contract/SKILL.md` |
| challenger | The isolated reviewer that tests the substance of the thinking, never the quality of the documents, run as `/challenge <persona>`. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/challenger-contract/SKILL.md` |
| check | The isolated reviewer that verifies mechanical conformance with the conventions, one concern per check, run as `/check <check>`. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/check-contract/SKILL.md` |
| Claude | The AI assistant, the cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, and it proposes but never decides. | `CLAUDE.md` (Roles); `.claude/agents/docs-planner.md` |
| contract | The skill that owns what every member of one kind of reviewer (or the two documentation agents) shares: conduct and isolation, the subject and its boundary, the way of working and the shape of the output. | `CLAUDE.md` (Isolated reviewers); the three reviewer contracts; `.claude/skills/docs-contract/SKILL.md` |
| contributor | A person who works on a branch of a hosted project and saves it, leaving the merge to the integrator. | the forge intent |
| critic | The isolated reviewer that judges the quality of the documents, never the substance, run as `/critique <lens>`. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/critic-contract/SKILL.md` |
| decision | A record of the principal's decision with its reason, numbered `DEC` and appended to `decisions.md`, never edited and superseded only by a newer one. | `CLAUDE.md` (Document kinds); `templates/decisions.md` |
| definition | The state file `.claude/skills/forge/states/<state>.md` of one artefact, saying what the artefact is, how it is found and its rules, in seven blocks; it is paired with the artefact's template. | `CLAUDE.md` (Document chain); the forge intent (Elicitation) |
| dependency | A citation of another project's document (a library's or any other's), found in the project and shown in the ledger's Dependencies table without a version. | `templates/ledger.md`; `.claude/skills/ingest/SKILL.md` |
| derived (page) | A page that puts together what no single file says, from evidence in several files, by the reasoning its entry gives. | `.claude/skills/docs-contract/SKILL.md` |
| derived file | A file of the derived way of merging, made from other files: the ledger outside git, and in git the renders, the README, the release notes, the documentation, the state render and the published files, taken as `ours` at a merge and made again. | the forge intent; `CLAUDE.md` (Repository layout) |
| document | Every file of a project; each document has one kind that says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md` (Document kinds) |
| documentation | The pages of one topic each in `docs/` with their index, generated by `/document` and never composed by hand. | `CLAUDE.md` (Document chain, Documentation); the forge intent |
| documentation map | The file `docs-map.md` beside the owning project's ledger, one entry per page with everything that page is made from, never shown to the reader. | `CLAUDE.md` (Document kinds); `.claude/agents/docs-planner.md` |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, through questions, research and sources. | the forge intent (Elicitation) |
| engine | The repository of Forge of Thought itself: its operating layer (`CLAUDE.md`, skills, agents, templates, scripts) and its own project, carrying no instance facts. | `CLAUDE.md`; the forge intent |
| explanation | A kind of page that says what a thing is, how it works and why, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md` |
| extract | The Markdown conversion of a binary file made by `scripts/doc2md.py` on the principal's word, which then is the source. | `CLAUDE.md` (Document chain, External inputs); `.claude/skills/ingest/SKILL.md` |
| fact | What is the case, as the principal states it or as a source states it (citing its file), numbered `FCT` in the intent; not a stance. | `CLAUDE.md` (ID scheme); the forge intent |
| finding | One result of a critic (document quality) or of a check (conformance), numbered `FND` in one sequence per project. | `CLAUDE.md` (ID scheme, Isolated reviewers) |
| format file | The file a recipe's format makes from a render (a Word or PowerPoint file, a video or player events), named after its render; it alone may be sent to the public folder. | `.claude/skills/render/SKILL.md`; the forge intent |
| genre | A kind of recipe composed through its own interview, `/recipe <genre>`, from the skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md` (Document chain, Renders) |
| growing bundle | A bundle of one origin that keeps arriving (issues, minutes), grown file by file through `/ingest --bundle <name>`, each file immutable from its own registration. | `.claude/skills/ingest/SKILL.md` |
| guarded command | A command that changes files the moment it runs (such as `/save`, `/render`, `/document`), which the harness keeps Claude from starting on its own judgement. | the forge intent |
| harness | The program Claude runs in, which enforces the principal's word where it can: it keeps Claude from sensitive paths, asks for web access per domain and guards commands. | the forge intent; `.claude/skills/document/SKILL.md` |
| history companion | The append-only file `<file>.history.md` beside every versioned document that holds its history as a log, one record per change. | `CLAUDE.md` (Versioning & status); `templates/history.md` |
| hook's ask | The answer of the git hook `scripts/hook-git.py` to the few git commands that finish the step of a conflict: it puts them to the principal and runs them on his yes, while it denies every other git write. | `CLAUDE.md` (Persistence) |
| how-to | A kind of page that carries what the reader does, step by step, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md` |
| immutable | Never edited once made: reviews, challenges and research from creation, a source from its registration, a closed thread from its closing; a process rule, not a git mechanism. | `CLAUDE.md` (Versioning & status, Persistence) |
| index (of the documentation) | The page `docs/README.md`, derived by `scripts/docs-index.py` from the documentation map, that lists every page and names each reader's path. | the forge intent; `.claude/skills/document/SKILL.md`; `.claude/agents/docs-planner.md` |
| instance | One installation of the engine. | `.claude/skills/docs-contract/SKILL.md` |
| instance fact | A fact of one installation (who the principal is, the conversation language, the principal's handle), kept in the gitignored `CLAUDE.local.md` and never in the engine, a report or a page. | `CLAUDE.md`; the forge intent |
| integrator | The maintainer of a hosted project, typically the principal, who merges the contributors' branches. | the forge intent |
| intent | The working document `10-intent.md`: the consolidated current state of what the principal holds, rewritten for coherence each round. | the forge intent; `.claude/skills/forge/states/intent.md` |
| isolation | The rule that a reviewer or a documentation agent never sees the working conversation and reads every input from disk in its own run. | `CLAUDE.md` (Isolated reviewers); the contracts |
| kind (of a project) | The field `kind` of the project file, `thought` or `library`, that says which rules of the engine apply. | `templates/project.md`; the forge intent |
| layer | An artefact of the chain below the intent (an assignment, a solution design, others), taken by a project only where it needs one. | `CLAUDE.md` (What this workspace is, Document chain) |
| ledger | The single source of truth for the state of a project, `ledger.md`, built by `scripts/forge-ledger.py` from the documents and never kept in git. | `CLAUDE.md` (Ledger); `templates/ledger.md` |
| lens | One specialisation of the critic, an agent file `critic-<lens>`. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/critic-contract/SKILL.md` |
| Lens section | The part of a lens, persona or check agent file that is its own: a specialisation of its contract that may narrow or tighten it, never replace it. | `CLAUDE.md` (Isolated reviewers) |
| library | A project of kind `library`: no chain, only sources, research and a README that catalogues them, shared across projects. | `CLAUDE.md` (Repository layout); `templates/project.md` |
| made at read time | Built by a script from the documents whenever it is read, never written by hand and never kept in git, as the ledger is. | `CLAUDE.md` (Ledger); the forge intent |
| major | An integer version: the next approved version, incorporating all changes since the previous one. | `CLAUDE.md` (Versioning & status); the forge intent |
| Map | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area was consciously considered; not a questionnaire. | the forge intent (Elicitation) |
| merge driver `ours` | The git merge driver that keeps one's own side of a derived file at a merge, so that the file is made again afterwards. | `CLAUDE.md` (Persistence); the forge intent |
| migration | The one-off bringing of a project to the shape of a release that changed the shape of files, by `/migrate` through `scripts/forge-migrate.py`, on the principal's word and on one clone. | `CLAUDE.md` (Persistence); `.claude/skills/migrate/SKILL.md` |
| mined | Said of a brief whose substance the intent has absorbed; the ledger shows each brief as `pending`, `partial`, `mined` or `dropped`. | `.claude/skills/forge/states/brief.md`; `templates/ledger.md` |
| mirrored (page) | A page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md` |
| page | A page of the documentation, or its index: generated, never a source of truth, overwritten by the documentation run. | `CLAUDE.md` (Document kinds) |
| persona | One specialisation of the challenger, an agent file `challenger-<persona>`. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/challenger-contract/SKILL.md` |
| pinned fact | A fact of a project that no file owns yet (a prerequisite, an install line, the public home of the repository), kept in the readme recipe's section "Pinned facts (not rendered)" for the documentation to read. | `templates/recipe-readme.md` |
| plain file | The file `/render` makes from the Markdown render through the script its recipe's format names, deterministic and cheap. | `CLAUDE.md` (Document chain, Renders); `.claude/skills/render/SKILL.md` |
| player page | The page `docs/videos/index.html` of the engine, written anew by `scripts/md2video.py` from `templates/html-player.html`, that plays the player files in the public folder. | `CLAUDE.md` (Repository layout); the forge intent |
| position | What the principal holds or wants and why, numbered `POS` in the intent, naming what it comes from. | `CLAUDE.md` (ID scheme); the forge intent |
| primary render | The render in the first language a recipe declares, from which the other languages are translated. | `.claude/skills/render/SKILL.md`; the forge intent |
| prime directive | One of the ten standing rules of `CLAUDE.md` that govern how Claude works, such as "When unsure, ask". | `CLAUDE.md` (Prime directives) |
| principal | Whoever's thinking is being forged: the source of ideas, answers and decisions and the final authority on all content. | `CLAUDE.md` (Roles) |
| project | A directory `projects/<slug>/` that holds one chain (or one library), a git repository of its own unless it lies outside git. | `CLAUDE.md` (Repository layout, Persistence) |
| project file | The file `project.md` of a project, written once at its creation, holding its slug, kind and language. | `templates/project.md`; the forge intent |
| project outside git | A project whose directory is not the top of a git repository, on which the forge runs no git; a property, not a defect. | `CLAUDE.md` (Persistence) |
| provenance | The front-matter a render opens with, naming its recipe and every input with the versions it was made from. | `.claude/skills/render/SKILL.md` |
| published companion | The file `published/<recipe>.md` beside a published file, holding its provenance; its state is computed, never written. | `.claude/skills/publish/SKILL.md` |
| published file | The designed `.pptx` or `.docx` that `/publish` makes from a render through a model, only on the principal's command. | `CLAUDE.md` (Document chain, Renders); `.claude/skills/publish/SKILL.md` |
| public folder | The engine's `docs/videos/`, the one folder served in public by GitHub Pages, into which a recipe's `output:` may send a format file; the documentation run leaves it alone. | `CLAUDE.md` (Document chain, Renders); the forge intent |
| pull | The inward step `/pull`: it looks at the remote, says the state as a fact and pulls only a clean repository that is behind. | `CLAUDE.md` (Persistence); `.claude/skills/pull/SKILL.md` |
| recipe | The versioned file `recipes/<recipe>.md` that says how a render is made (inputs, audience, instructions, template); iterated, never approved. | `CLAUDE.md` (Document kinds, Document chain) |
| recipients | Those who receive an assignment: teams, colleagues, or the principal's future self. | `CLAUDE.md` (What this workspace is) |
| record | One line of a history companion: one change, with date, version, author, subject, kind and reason, appended and never rewritten. | `CLAUDE.md` (Versioning & status); `templates/history.md` |
| record of state | A record that changes only state (a mining, a finding or thread closed, a work product's state), carrying the current version without raising it. | `templates/history.md` |
| reference | A kind of page that states facts in the structure of what it mirrors, free of interpretation, a table where the input is a table. | `.claude/skills/docs-contract/SKILL.md` |
| registration of the merge driver | The one-off act of `/setup`, on the user's word, that writes the merge driver `ours` and the git settings it needs into the global git configuration through `scripts/forge-config.py`. | `CLAUDE.md` (Persistence) |
| rejected direction | A direction the principal dropped, numbered `REJ` in the intent with the reason it was dropped. | `CLAUDE.md` (ID scheme); the forge intent |
| release | The step `/release`, from `main` only: it runs its checks, re-renders the README and release notes, and saves with the release message and tag. | `CLAUDE.md` (Persistence) |
| render | An audience-specific output generated from the chain by `/render` from its recipe, never edited by hand and never a source of truth. | `CLAUDE.md` (Document chain, Renders); `.claude/skills/render/SKILL.md` |
| Reports | The section of the ledger that names what the merged files cannot say: an ID defined twice, a closed thread touched later, a thread cited without a file. | `templates/ledger.md` |
| research | A durable, immutable note in `research/` that answers one question, made by `/research`. | `CLAUDE.md` (Document kinds) |
| resource index | The `00-INDEX.md` of a `sources/` or `research/` directory: a light catalogue of what each resource is and is for, freely rewritten. | `CLAUDE.md` (Document chain, External inputs) |
| Role | The free-text field of a source's index entry that says what the source is for, asked of the principal before the entry is written. | `CLAUDE.md` (Document chain, External inputs); `.claude/skills/ingest/SKILL.md` |
| round | One working conversation over an artefact or open items, whose agreed changes are carried in the conversation and written once at its end, as one version. | `CLAUDE.md` (Prime directives, Working methods); `.claude/skills/walkthrough/SKILL.md` |
| save | The step `/save`: it runs its check and then commits and pushes on whatever branch is checked out; `--quick` leaves the check out. | `CLAUDE.md` (Persistence) |
| screenplay | A render of the genre `screenplay`: a terminal conversation in scenes with captions, turned into a video or player events by `scripts/md2video.py`. | the forge intent |
| session | The run of Claude in which the working conversation takes place, closed by `/end`. | `CLAUDE.md` (Commands); `.claude/skills/docs-contract/SKILL.md` |
| session model | The one model the whole forge runs on, chosen as an instance preference; every command and reviewer inherits it. | `CLAUDE.md` (Isolated reviewers, Repository layout) |
| shape of a project | The form of a project's files as a release defines it, recognised by the migration as a set of marks, one per step; a project without a project file is of the shape before the migration. | `.claude/skills/migrate/SKILL.md`; `templates/project.md`; the forge intent |
| solution design | The layer `40-solution-design.md` that says how the things wanted are realised, part by part, with the choices they rest on, numbered `SOL`. | `.claude/skills/forge/states/solution-design.md` |
| source | External input as it arrived, stored in `sources/` by `/ingest`, registered and immutable. | `CLAUDE.md` (Document kinds, Document chain) |
| specification | The versioned file `work/<name>.spec.md` of a work product, holding its way and its why: task, inputs, method, assumptions, open matters and how the file is made. | the forge intent; `.claude/skills/work/SKILL.md` |
| stale | Said of a render when a version its provenance cites differs from the current one or a cited file is gone; of a published file or a work product when what it was made from is newer. | `.claude/skills/render/SKILL.md`; `templates/ledger.md` |
| state render | The file `renders/state.md`, the ledger written as a render by `/release` on `main`, for where the state is wanted on the remote. | `CLAUDE.md` (Repository layout) |
| step of a conflict | The settling of a conflict `forge-save` meets and leaves standing: Claude lays both sides out as a walkthrough, the principal decides, Claude writes the wording, and git's finishing commands run on the hook's ask. | `CLAUDE.md` (Persistence) |
| subagent | An agent Claude launches with a context of its own that never sees the working conversation, as the reviewers, the render generator and the documentation agents are. | `CLAUDE.md` (Isolated reviewers); `.claude/skills/render/SKILL.md` |
| tag | A git name for one release: `v<major>` is given by `/release`, any other tag at the principal's request with a free name. | `CLAUDE.md` (Persistence) |
| template | A canonical skeleton in `templates/` that says what comes out when a document is created. | `CLAUDE.md` (Templates, Document chain) |
| thought project | A project of kind `thought`, the default, that carries a chain. | `CLAUDE.md` (Repository layout); `templates/project.md` |
| thread | One open matter of the intent, numbered `THR`, carrying its origin and the working debate until it is settled; it closes only on the principal's word. | `CLAUDE.md` (ID scheme); `.claude/skills/forge/states/intent.md` |
| thread file | The file `threads/THR.NNNN.md` of one thread, whose header (`id`, `concerns`, `origin`, `status`) is its state; freely rewritten while open, immutable once closed. | `.claude/skills/forge/states/intent.md`; `templates/thread.md` |
| translation | A render in a further language a recipe declares, translated from the primary render scene for scene and line for line, its provenance naming the primary. | `.claude/skills/render/SKILL.md`; the forge intent |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports; the writer leaves such a fact out. | `.claude/agents/docs-planner.md` |
| verdict | The principal's answer to one item of a walkthrough: `accept`, `modify`, `question`, `reject`, `park` or `obsolete`, offered by the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. | `.claude/skills/walkthrough/SKILL.md` |
| Verdict line | The line of a decision that rules on a finding or a challenge: `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`, one per ID. | `templates/decisions.md` |
| Waiting on principal | The section of the ledger that lists, by rule and not by hand, what waits on the principal: open threads, the TBCs he owns, open critic findings and challenges, and the parked ones. | `CLAUDE.md` (Ledger); `templates/ledger.md` |
| walkthrough | The working method by which a list of items needing the principal's decision is worked one item per message, in order of weight, each closed with the verdict line. | `CLAUDE.md` (Working methods); `.claude/skills/walkthrough/SKILL.md` |
| way of merging | One of three ways a file of a project merges, as the forge tells git: text, derived, or immutable and unique. | the forge intent |
| work product | An output of a project made with work of its own (a model, an analysis), two files in `work/`: the file with the content and its specification. | `CLAUDE.md` (Document kinds); the forge intent; `.claude/skills/work/SKILL.md` |
| working method | One of the named ways a working conversation runs (walkthrough, step by step, reflect back and others), applied whenever its situation arises; none is a command. | `CLAUDE.md` (Working methods) |
| write | The principal's word `write`, on which Claude reflects the round back and, on his yes, writes everything agreed as one round. | `CLAUDE.md` (Working methods); `.claude/skills/walkthrough/SKILL.md` |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
