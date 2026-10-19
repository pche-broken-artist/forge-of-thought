---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 5d1fe175df5acb62
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
  - projects/forge/10-intent.md#POS.1590
  - projects/forge/10-intent.md#POS.1600
  - projects/forge/10-intent.md#POS.1610
  - projects/forge/10-intent.md#POS.1740
  - projects/forge/10-intent.md#Elicitation
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
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

This glossary gives every term of the forge in one line each, with
the file that defines it. It is for the user, the extender and the
evaluator alike: anyone who meets a word of the forge on another page
and wants its meaning in one sentence. The terms stand in groups by
theme, in the order a reader meets them. For the forge in prose, read
[What the forge is and is not](../about/what-it-is-and-is-not.md).
"Defined in" names the file, and the section where the file is long;
a section of the forge's intent is named by its group heading.

## People, roles and the conversation

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: the one who supplies ideas, answers and decisions and has final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is handed to: teams, colleagues or the principal's future self. | `CLAUDE.md`, What this workspace is |
| Claude (cognitive extension) | The AI assistant that works as the principal's cognitive extension: it owns structure, order, process discipline and document hygiene, and it proposes but never decides. | `CLAUDE.md`, Roles; `.claude/agents/docs-planner.md` |
| session | One sitting of work with Claude, closed by `/end`, which says what lives only in the conversation and would be lost. | `CLAUDE.md`, Commands |
| harness | The program Claude runs in (Claude Code), which enforces the principal's word where it can: it keeps Claude from sensitive paths, asks approval of web access per domain and guards the commands that write. | `projects/forge/10-intent.md`, Operating environment; `.claude/skills/document/SKILL.md` |
| working method | A named way a working conversation runs; none is a command, each applies whenever its situation arises, and the principal may invoke any of them in a word. | `CLAUDE.md`, Working methods |
| prime directive | One of the ten numbered ground rules of Claude's conduct in `CLAUDE.md`, such as "When unsure, ask" and "One mechanism lives in one place". | `CLAUDE.md`, Prime directives |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, with the conversation as its medium and the interview, research and sources as its instruments. | `projects/forge/10-intent.md`, Elicitation |
| walkthrough | The working method for any list of items needing the principal's decision: one item per message, in order of weight, each closed with the verdict line. | `CLAUDE.md`, Working methods; `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item of a walkthrough: `accept`, `modify`, `question`, `reject`, `park` or `obsolete`. | `.claude/skills/walkthrough/SKILL.md`, The verdict |
| round | One working conversation, whose agreed changes are carried in the conversation and written once at its end as one version. | `CLAUDE.md`, Prime directives (9) |
| write | The principal's word that ends a round: Claude reflects the whole round back and, on his yes, writes everything carried as one round. | `CLAUDE.md`, Working methods; `.claude/skills/walkthrough/SKILL.md` |
| guarded command | A command that changes files the moment it runs, with no round and no `write` in between, such as `/save`, `/render` or `/document`, which the harness keeps Claude from starting on its own judgement. | `projects/forge/10-intent.md`, Operating environment |

## The chain and its artefacts

| Term | Meaning | Defined in |
|---|---|---|
| document | Every file of a project. | `CLAUDE.md`, Document kinds |
| kind (of a document) | The class that says what a document is, who writes it, whether it is versioned and how it behaves, such as artefact, history, ledger, render or source. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain, composed by the principal with Claude, versioned and found through its definition. | `CLAUDE.md`, Document kinds |
| brief | The principal's idea put together, `00-brief.md` or `00-brief-<name>.md`: what he wants and why, in free form and rough on purpose, before it is mined into the intent. | `.claude/skills/forge/states/brief.md` |
| mined | How far the intent has absorbed a brief (`pending`, `partial`, `mined` or `dropped`), said by a mining record in the intent's history. | `templates/history.md`; `templates/ledger.md`, Briefs |
| intent | `10-intent.md`, the trunk of every chain: the briefs chiselled into what the principal holds as positions, facts, threads and rejected directions, saying what is wanted and never how it is realised. | `.claude/skills/forge/states/intent.md` |
| position | An item of the intent (prefix `POS`) that says what the principal holds or wants and why, and names what it comes from. | `projects/forge/10-intent.md`, Document chain and Structure and style of an assignment |
| fact | An item of the intent (prefix `FCT`) that says what is the case, on the principal's word or on a source cited to its file, never a stance and never demanded to be verified. | `projects/forge/10-intent.md`, Structure and style of an assignment; `CLAUDE.md`, ID scheme |
| thread | An open matter (prefix `THR`) still to be elicited, which names the artefact it concerns, carries its origin and holds the working debate until it is settled. | `projects/forge/10-intent.md`, Document chain; `.claude/skills/forge/states/intent.md`, Threads and files |
| thread file | The file of one thread in `threads/`, named by its ID, whose header (`id`, `concerns`, `origin`, `status`) is its state; it is freely rewritten while open and immutable once closed. | `templates/thread.md`; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | An item of the intent (prefix `REJ`) that records a direction the principal dropped, with the reason it was dropped. | `CLAUDE.md`, ID scheme |
| assignment | `20-assignment.md`, which carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. | `.claude/skills/forge/states/assignment.md` |
| solution design | `40-solution-design.md`, which says how the things wanted are realised, part by part, with the choices they rest on, and is kept current. | `.claude/skills/forge/states/solution-design.md` |
| layer | An artefact of the chain below the intent, taken by a project only as it needs it; a layer a project does not have is not missing. | `CLAUDE.md`, What this workspace is and Document chain |
| definition | The state file of an artefact, `.claude/skills/forge/states/<state>.md`, which says what the artefact is, how it is found and what its rules are, in seven blocks. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| template | A canonical skeleton in `templates/`, which says what comes out where the definition says how it is found. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names what must be found for the artefact to be complete, walked at the moments the definition names, neither a questionnaire nor a list of headings. | `projects/forge/10-intent.md`, Elicitation |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | `<file>.history.md`, the append-only log beside every versioned document, which holds what changed and why while the body holds the current state. | `CLAUDE.md`, Versioning & status; `templates/history.md` |
| record | One line of a history companion, one per change, carrying date, version, author, subject, kind and reason, with `Action` and `Was` where it has them. | `templates/history.md` |
| record of state | A record that carries the current version without raising it and says a state, such as the mining of a brief, a settled finding or a work product's state. | `templates/history.md` |
| archive | An immutable file of what stood before the present shape: `<file>.history.archive.md` for a history table before the log, `ledger.archive.md` for the hand-kept ledger at the migration. | `CLAUDE.md`, Versioning & status; `templates/ledger.md` |
| ledger | `ledger.md`, the single source of truth for a project's state, built from the documents by `scripts/forge-ledger.py` and never kept in git. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| made at read time | Built by a script from the documents whenever it is needed, instead of being kept and written by hand, as the ledger is. | `projects/forge/10-intent.md`, Versioning and state |
| Waiting on principal | The ledger's section of what waits on the principal, computed by a rule from the open threads, the TBCs he owns, the open findings of a critic, the open challenges and, under Parked, the parked ones. | `templates/ledger.md`, Waiting on principal |
| Reports | The ledger's section of what the merged files cannot say, found by the ledger script, such as an ID defined twice. | `templates/ledger.md`, Reports |
| decision | A record of `decisions.md` (prefix `DEC`) that holds one decision of the principal with its reason, append-only and superseded only by a newer record. | `templates/decisions.md`; `CLAUDE.md`, Document kinds |
| Verdict line | The line of a decision that rules on one finding or challenge: `<ID> rejected`, `<ID> parked until <what>` or `<ID> obsolete`. | `templates/decisions.md`; `.claude/skills/walkthrough/SKILL.md` |
| immutable | Never edited: a source from its registration, a review, a challenge or a research note from its creation, corrections made downstream, as a process rule and not a git mechanism. | `CLAUDE.md`, Versioning & status and Persistence (git) |

## Resources

| Term | Meaning | Defined in |
|---|---|---|
| source | External input as it arrived, stored in `sources/` and immutable once registered. | `CLAUDE.md`, Document chain (External inputs) |
| bundle | A set of related files in `sources/<slug>/`, which counts as one source and carries its own `00-INDEX.md`. | `CLAUDE.md`, Document chain (External inputs) |
| extract | The Markdown made from a functional binary by `scripts/doc2md.py`, on the principal's explicit word through `/ingest`, which from then on is the source. | `CLAUDE.md`, Document chain (External inputs) |
| research | A durable answer to one question in `research/`, written by `/research` and immutable. | `CLAUDE.md`, Document kinds |
| resource index | The `00-INDEX.md` of `sources/` or `research/`, a light catalogue of what the resources are and are for, freely rewritten and tracking nothing. | `CLAUDE.md`, Document chain (Resource indexes) |
| Role | The free-text field of a source's entry in the resource index that says what that source is for, asked before the entry is written. | `CLAUDE.md`, Document chain (External inputs) |
| dependency | A citation of a document of another repository, typically a library's, registered in the ledger's Dependencies table without a version. | `templates/ledger.md`, Dependencies |

## Renders and published files

| Term | Meaning | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`, the one versioned file of a render's inputs, audience, instructions and output template, iterated and never approved. | `CLAUDE.md`, Document chain (Renders) and Versioning & status |
| genre | A kind of recipe composed through an interview by `/recipe <genre>`, with its skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md`, Document chain (Renders) |
| render | An audience-specific output generated from the chain by `/render`, never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain (Renders); `.claude/skills/render/SKILL.md` |
| provenance | The YAML front-matter every render opens with, naming the project, the recipe with its version, the generation date and every input with its version. | `.claude/skills/render/SKILL.md`, step 5 |
| stale (render) | Said of a render when any version its provenance cites differs from the current version of that file, or a cited file no longer exists. | `.claude/skills/render/SKILL.md`, step 5 |
| primary render | The render in the first language a recipe declares in `languages:`, from which the others are translated. | `.claude/skills/render/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| translation | A render in a further declared language, made from the primary render in the same run, scene for scene and line for line, and citing it in `translated_from`. | `.claude/skills/render/SKILL.md`; `projects/forge/10-intent.md`, Document chain |
| plain file | The file `/render` makes beside a render through a script where the recipe names a format, such as a `.docx`, a `.pptx`, a video or a player's events, deterministic and repeated freely. | `CLAUDE.md`, Document chain (Renders); `.claude/skills/render/SKILL.md`, step 7 |
| format file | The file made from a render in the format its recipe's `## Format` section names, which the recipe's `output:` may send into the engine's public folder. | `projects/forge/10-intent.md`, Growth path; `.claude/skills/render/SKILL.md`, steps 4 and 7 |
| screenplay | A render of the genre `screenplay`: a terminal conversation shown as a title card, a card of what the viewer will see and timed scenes, each with a two-part caption and a block of what the terminal shows. | `projects/forge/10-intent.md`, Document chain |
| player page | `docs/videos/index.html`, written anew by `scripts/md2video.py` from `templates/html-player.html` whenever a file enters the public folder, which plays a screenplay's timed events. | `projects/forge/10-intent.md`, Growth path |
| public folder | The engine's `docs/videos/`, the one public folder, served by GitHub Pages and left alone by `/document`. | `CLAUDE.md`, Document chain (Renders); `projects/forge/10-intent.md`, Growth path |
| published file | The designed `.pptx` or `.docx` in `published/`, made from a render through a model by `/publish`, only on the principal's command. | `.claude/skills/publish/SKILL.md` |
| published companion | `published/<recipe>.md`, the provenance of a published file, from which the ledger computes whether it is current or stale. | `.claude/skills/publish/SKILL.md`, step 6 |
| stale (published file) | Said of a published file when its render is newer than the one its companion names, or missing. | `templates/ledger.md`, Published |
| state render | `renders/state.md`, the ledger as a render, written by `/release` on `main`. | `CLAUDE.md`, Repository layout |

## Work products

| Term | Meaning | Defined in |
|---|---|---|
| work product | An output of a project made with work of its own, neither an artefact nor a render (a model, an analysis, a worked task), kept as two files in `work/`. | `projects/forge/10-intent.md`, Document chain; `.claude/skills/work/SKILL.md` |
| specification | `work/<name>.spec.md`, the versioned file of a work product's way and why: its task, its inputs cited by ID and path, its method, its assumptions, what is open and, in `## Making`, how the file is made. | `projects/forge/10-intent.md`, Document chain; `.claude/skills/work/SKILL.md` |
| stale (work product) | The state of a work product's file after its specification was written anew since the last making, said by a record of state in the specification's history. | `templates/history.md`; `templates/ledger.md`, Work |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| subagent | An agent Claude launches in a context of its own, which never sees the working conversation and reads its inputs from disk. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/render/SKILL.md`, step 3 |
| isolation | The rule that a reviewer or a generating agent sees nothing of the working conversation and judges only what the files say. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/docs-contract/SKILL.md` |
| contract | The skill that owns what every member of one kind of agent shares (conduct and isolation, subject and boundary, way of working, shape of the output), preloaded into each agent. | `CLAUDE.md`, Isolated reviewers |
| Lens section | The one section of a lens, persona or check file that is its own, a specialisation of its contract that may narrow what is read or make a shared rule stricter but never replace it. | `CLAUDE.md`, Isolated reviewers |
| critic | The isolated reviewer of the documents' quality, never their substance, run by `/critique <lens>` and filing its findings in `reviews/`. | `.claude/skills/critic-contract/SKILL.md` |
| lens | One specialisation of the critic, one agent file `critic-<lens>`, with its own Lens section. | `.claude/skills/critic-contract/SKILL.md`; `CLAUDE.md`, Isolated reviewers |
| challenger | The isolated reviewer of the substance of the thinking, never the documents' quality, run by `/challenge <persona>` and filing its challenges in `challenges/`. | `.claude/skills/challenger-contract/SKILL.md` |
| persona | One specialisation of the challenger, one agent file `challenger-<persona>`, with its own Lens section and register. | `.claude/skills/challenger-contract/SKILL.md`; `CLAUDE.md`, Isolated reviewers |
| check | The isolated reviewer of mechanical conformance with the engine's conventions, never substance or quality, run by `/check <check>`, each check owning one concern. | `.claude/skills/check-contract/SKILL.md` |
| finding | The result of a critic (document quality) or of a check (conformance), prefix `FND`, in one sequence whose state the ledger reads from records and Verdict lines. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | The result of a challenger on the substance of the thinking, prefix `CHL`, with its severity (dealbreaker, major or minor) and its epistemic status. | `.claude/skills/challenger-contract/SKILL.md`; `templates/ledger.md`, Challenges |

## Projects, the engine and git

| Term | Meaning | Defined in |
|---|---|---|
| engine | The repository of the forge itself (`CLAUDE.md`, the skills, the agents, the templates and the scripts), which specifies, implements nothing and carries no instance facts. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, Operating environment |
| instance | One installation of the engine. | `.claude/skills/docs-contract/SKILL.md`, The voice |
| instance fact | A fact of one instance (who the principal is, the conversation language, the handle he signs records with), kept in the gitignored `CLAUDE.local.md` and never in the engine, a report or a page. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, Operating environment |
| session model | The one model the whole forge runs on, set in `.claude/settings.local.json` and inherited by every reviewer. | `CLAUDE.md`, Isolated reviewers and Repository layout |
| project | A directory `projects/<slug>/` that is a git repository of its own, of kind `thought` or `library`. | `CLAUDE.md`, Repository layout and Persistence (git) |
| kind (of a project) | `thought` or `library`, declared in the project file, with the rules of each kind kept in the engine. | `templates/project.md`; `projects/forge/10-intent.md`, Document chain |
| project file | `project.md`, written once at a project's creation, which holds the project's slug, kind and language. | `templates/project.md`; `projects/forge/10-intent.md`, Document chain |
| thought project | A project of kind `thought`, which carries a chain from a brief to the intent and the layers it needs. | `CLAUDE.md`, Repository layout |
| library | A project of kind `library`, named `lib-<name>`, with no chain: material shared across projects in its sources and research, catalogued by its README. | `CLAUDE.md`, Repository layout |
| save | `/save`, which runs its check and then commits and pushes on the checked-out branch without rendering; `--quick` leaves the check out. | `CLAUDE.md`, Persistence (git) |
| release | `/release`, run from `main` only, which runs its checks, renders the README and release notes again and saves with the release message and tag. | `CLAUDE.md`, Persistence (git) |
| pull | `/pull`, which states each repository's state against its origin (up to date, behind, ahead, diverged, no origin or not under git) and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| migration | `/migrate [slug]` through `scripts/forge-migrate.py`, which brings a project to the shape of a release that changed the shape of files, once per project, on one clone, on the principal's word. | `.claude/skills/migrate/SKILL.md`; `projects/forge/10-intent.md`, Operating environment |
| shape of a project | The set of marks, one per step of the migration, by which the migration script recognises how far a project is, never by an engine version. | `projects/forge/10-intent.md`, Operating environment; `templates/project.md` |
| major | An integer version, which is a signed-off one; a major of the forge's intent closes a set of features the principal names and passes every check, both critic lenses and one challenge before its tag. | `CLAUDE.md`, Versioning & status; `projects/forge/10-intent.md`, Versioning and state |
| tag | A name git gives a commit: `v<major>` on the release `/release` says, any other only at the principal's request, with a free name. | `CLAUDE.md`, Persistence (git) |
| branch | A line of work beside `main`, voluntary and left to git, switched or created by `scripts/forge-branch.py` and merged by hand or by merge request. | `CLAUDE.md`, Persistence (git) |

## The documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | The pages in `docs/`, one topic each, with an index, generated by `/document` and never written by hand, for the user, the extender and the evaluator. | `CLAUDE.md`, Document chain (Documentation); `projects/forge/10-intent.md`, Growth path |
| documentation map | `docs-map.md` beside the owning project's ledger, one entry per page with everything a page is made from, never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md`, The map |
| page | A page of the documentation, or its index, overwritten by the documentation run and never a source of truth. | `CLAUDE.md`, Document kinds |
| index (of the documentation) | `docs/README.md`, derived by `scripts/docs-index.py` from the documentation map, listing every page and each reader's path through them. | `.claude/agents/docs-planner.md`, The outline; `projects/forge/10-intent.md`, Growth path |
| how-to | A page that carries what the person does, step by step where there are steps, and what he sees, never the reasons. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| explanation | A page that carries what a thing is, how it works and why it is so, never a procedure and never a listing. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| reference | A page that states facts in the structure of what it mirrors, free of interpretation, and never explains. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| mirrored | Said of a page that restates what its inputs say, in the reader's words. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| derived | Said of a page that puts together what no single file says, from evidence in several, by the reasoning its entry gives. | `.claude/skills/docs-contract/SKILL.md`, The kinds of a page |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports, left off the page until the owner of the documentation gives it a home. | `.claude/agents/docs-planner.md`, The map; `.claude/skills/document/SKILL.md` |
| pinned fact | A fact of a project that no file owns yet (a prerequisite, how a tool is installed, the public home of the repository), kept in the readme recipe's `## Pinned facts (not rendered)` section and read by the documentation planner. | `templates/recipe-readme.md`, Pinned facts (not rendered) |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the forge in prose.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
