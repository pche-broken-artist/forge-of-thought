---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: dbd693ef63775f3d
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
  - projects/forge/10-intent.md#Elicitation
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/pull/SKILL.md
  - .claude/skills/work/SKILL.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - templates/ledger.md
  - templates/recipe-readme.md#Pinned facts (not rendered)
---

# Glossary

This page lists the terms of the forge, one line each, with the file that defines each. It is for every reader who meets a word on another page and wants its meaning at once. The forge is a workshop in which a thought travels a chain of versioned documents under isolated review.

The tables group the terms by topic. A path in the last column is a file of the engine, or a part of it named after a comma.

## People and conduct

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: it supplies ideas, answers and decisions and has the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those who receive an assignment: teams, colleagues or the principal's future self. | `CLAUDE.md`, What this workspace is |
| Claude as cognitive extension | Claude is the principal's cognitive extension: it owns structure, order, process discipline and document hygiene, and it proposes but never decides. | `CLAUDE.md`, Roles |
| session | One working sitting of the principal with Claude, which `/end` closes by saying what would be lost. | `CLAUDE.md`, Persistence (git) |
| session model | The one model the session runs on, which every subagent inherits. | `CLAUDE.md`, Isolated reviewers |
| harness | The program that runs Claude (Claude Code) and enforces the principal's word where it can, for instance by guarding commands. | `projects/forge/10-intent.md`, the position on the harness |
| subagent | A separate run of Claude, started for one job, that never sees the working conversation. | `.claude/skills/docs-contract/SKILL.md` |
| prime directive | One of the ten numbered rules at the head of the forge's core file, such as "when unsure, ask". | `CLAUDE.md`, Prime directives |
| working method | A named way a working conversation runs, applied whenever its situation arises and never a command. | `CLAUDE.md`, Working methods |
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds. | `projects/forge/10-intent.md`, Elicitation |
| Map | The part of a definition that names what must be found for an artefact to be complete; it is neither a questionnaire nor a list of headings. | `projects/forge/10-intent.md`, Elicitation |
| walkthrough | A list of items needing the principal's decision, worked one item per message, each closed with the verdict line. | `.claude/skills/walkthrough/SKILL.md` |
| verdict | The principal's answer to one item of a walkthrough: accept, modify, question, reject, park or obsolete. | `.claude/skills/walkthrough/SKILL.md` |
| round | One working conversation over an artefact or open items, written once at its end as one version. | `CLAUDE.md`, Prime directives |
| write | The principal's word that tells Claude to write what the round has agreed into the files. | `CLAUDE.md`, Working methods |
| guarded command | A command that changes files the moment it runs, which the harness keeps Claude from starting on its own judgement. | `projects/forge/10-intent.md`, the position on the harness |

## The chain and its documents

| Term | Meaning | Defined in |
|---|---|---|
| document | Any file of a project. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain, composed by the principal with Claude. | `CLAUDE.md`, Document kinds |
| layer | An artefact below the intent that a project takes when it needs it; a project may have none. | `CLAUDE.md`, What this workspace is |
| brief | The principal's idea put together, rough on purpose, in `00-brief.md` or `00-brief-<name>.md`. | `.claude/skills/forge/states/brief.md` |
| intent | The artefact `10-intent.md`, in which the briefs are chiselled into what the principal holds. | `.claude/skills/forge/states/intent.md` |
| mined | Taken from a brief into the intent; the Mined column of the ledger says how far a brief has been absorbed. | `.claude/skills/forge/states/brief.md` |
| position | What the principal holds or wants. | `projects/forge/10-intent.md`, the position on prefixes |
| fact | What is the case, on the principal's word or as a cited source states it. | `projects/forge/10-intent.md`, the position on prefixes |
| thread | An unresolved matter to be elicited next, kept in `threads.md` with its origin. | `projects/forge/10-intent.md`, the position on prefixes |
| rejected direction | A direction the principal dropped, kept in the intent with the reason. | `CLAUDE.md`, ID scheme |
| assignment | The artefact that carries the in-scope substance of the intent to the recipients, complete and precise. | `.claude/skills/forge/states/assignment.md` |
| solution design | The artefact that says how the things wanted are realised, part by part, with the choices they rest on. | `.claude/skills/forge/states/solution-design.md` |
| definition | The state file `.claude/skills/forge/states/<state>.md` that says what an artefact is and how it is found. | `CLAUDE.md`, Document chain |
| template | The canonical skeleton that says what comes out of a definition. | `CLAUDE.md`, Templates |
| work product | An output that is neither artefact nor render, made with work of its own and kept in `work/` as two files. | `.claude/skills/work/SKILL.md` |
| specification | The file `work/<name>.spec.md` of a work product, which holds the way and the why. | `.claude/skills/work/SKILL.md` |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | The append-only file `<file>.history.md` beside a versioned document, which holds what changed and why. | `CLAUDE.md`, Versioning & status |
| record | One entry of a history log, made for one change. | `CLAUDE.md`, Versioning & status |
| archive | The file `<file>.history.archive.md`, a history table kept as it stood before the log began, immutable. | `CLAUDE.md`, Versioning & status |
| ledger | The file `ledger.md`, the single source of truth for the state of a project, freely rewritten. | `CLAUDE.md`, Ledger |
| decision | An entry of `decisions.md`, the append-only record of the principal's decisions with reasons. | `CLAUDE.md`, Document kinds |
| immutable | Never edited after creation: a source from its registration, reviews, challenges and research notes from the day they are written. | `CLAUDE.md`, Versioning & status |
| major | An integer version of the forge intent that closes a set of features the principal names, after every check, both critic lenses and one challenge. | `projects/forge/10-intent.md`, the position on versioning |

## Sources and research

| Term | Meaning | Defined in |
|---|---|---|
| source | External input as it arrived, registered in `sources/` and never edited. | `CLAUDE.md`, Document chain |
| bundle | A set of related files kept as one subdirectory `sources/<slug>/`, counted as one source with its own index. | `CLAUDE.md`, Document chain |
| extract | The Markdown conversion of a binary source, made on the principal's word and then the source itself. | `CLAUDE.md`, Document chain |
| research | A durable, dated note that answers one question, kept in `research/` and immutable. | `CLAUDE.md`, Document kinds |
| resource index | The file `00-INDEX.md` that catalogues a `sources/` or `research/` directory. | `CLAUDE.md`, Document chain |
| Role | The free-text field of a resource index that says what an individual source is for. | `CLAUDE.md`, Document chain |

## Renders and their files

| Term | Meaning | Defined in |
|---|---|---|
| recipe | The versioned file in `recipes/` that holds inputs, audience, instructions and the output template of a render. | `CLAUDE.md`, Document chain |
| render | Audience-specific output generated from a recipe, never a source of truth and never edited by hand. | `.claude/skills/render/SKILL.md` |
| genre | A kind of recipe with its own skeleton `templates/recipe-<genre>.md`, composed through `/recipe <genre>`. | `CLAUDE.md`, Document chain |
| plain file | The file made from a render by `/render` through pandoc or `scripts/md2video.py`, beside the render. | `CLAUDE.md`, Document chain |
| published file | The designed file that `/publish` makes from a render through a model, kept in `published/`. | `CLAUDE.md`, Document chain |
| format file | The plain file in the format the recipe's Format section names. | `projects/forge/10-intent.md`, the position on the screenplay |
| screenplay | A genre of recipe that renders a terminal conversation as title card, scenes with captions and the text the terminal shows. | `projects/forge/10-intent.md`, the position on the screenplay |
| player page | The fixed page `docs/videos/index.html` of the engine, which plays the events of a screenplay's html-player file. | `projects/forge/10-intent.md`, the position on public hosting |
| public folder | The engine's folder `docs/videos/`, where a recipe's `output:` may send a format file and which the documentation leaves alone. | `projects/forge/10-intent.md`, the position on public hosting |
| primary render | The render in the first language that a recipe's `languages:` declares. | `projects/forge/10-intent.md`, the position on several languages |
| translation | A render in a further declared language, made from the primary render scene for scene and line for line. | `projects/forge/10-intent.md`, the position on several languages |
| provenance | The front-matter that opens every render and names its project, recipe and inputs with their versions. | `.claude/skills/render/SKILL.md` |
| stale | Said of a render when a version cited in its provenance differs from the file's current version or the cited file is gone. | `.claude/skills/render/SKILL.md` |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| critic | The reviewer of the quality of the documents, never of the substance. | `.claude/skills/critic-contract/SKILL.md` |
| lens | The angle through which one critic reads the chain. | `.claude/skills/critic-contract/SKILL.md` |
| challenger | The reviewer of the substance of the thinking, never of document quality. | `.claude/skills/challenger-contract/SKILL.md` |
| persona | The register in which one challenger works. | `.claude/skills/challenger-contract/SKILL.md` |
| check | A reviewer of mechanical conformance with the conventions, each owning one concern. | `.claude/skills/check-contract/SKILL.md` |
| finding | The result of a critic or of a check, ranked by severity and kept in the ledger. | `.claude/skills/critic-contract/SKILL.md` |
| challenge | The result of a challenger, with a severity and an epistemic status. | `.claude/skills/challenger-contract/SKILL.md` |
| contract | The skill that owns what every reviewer of one kind shares: subject, way of working and shape of the report. | `CLAUDE.md`, Isolated reviewers |
| Lens section | The part of a reviewer's agent file that is its own and specialises the contract without replacing any of it. | `CLAUDE.md`, Isolated reviewers |
| isolation | The rule that a reviewer runs as a subagent that never sees the working conversation. | `CLAUDE.md`, Isolated reviewers |

## Projects, the engine and git

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory under `projects/` that is a git repository of its own. | `CLAUDE.md`, Repository layout |
| thought project | A project of the kind `thought`, which carries the chain. | `CLAUDE.md`, Repository layout |
| library | A project of the kind `library`: material shared across projects, with no chain. | `CLAUDE.md`, Repository layout |
| dependency | A document of another repository, typically a library's, on which a project relies and which the ledger registers. | `templates/ledger.md` |
| engine | The one git repository that holds the forge itself: its core file, skills, agents, templates and scripts. | `CLAUDE.md`, Persistence (git) |
| instance | One installation of the forge. | `.claude/skills/docs-contract/SKILL.md` |
| instance fact | A fact of one installation, such as who the principal is or the conversation language, kept in a file outside the repository and never in the engine. | `projects/forge/10-intent.md`, the position on instance facts |
| save | The command `/save`, which runs its check and then commits and pushes on the branch that is checked out. | `CLAUDE.md`, Persistence (git) |
| release | The command `/release`, which runs from `main`, re-renders the README and the release notes and saves with a message and a tag. | `CLAUDE.md`, Persistence (git) |
| pull | The command `/pull`, which reports the state against the remote and pulls only a clean repository that is behind. | `.claude/skills/pull/SKILL.md` |
| tag | A git tag: the release that `/release` names receives `v<major>`, and any other tag is the principal's request. | `CLAUDE.md`, Persistence (git) |
| branch | A line of work in git; `main` is the released line and other branches are voluntary. | `CLAUDE.md`, Persistence (git) |

## Documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | The pages of one topic each in `docs/`, generated by `/document` and never composed by hand. | `CLAUDE.md`, Document chain |
| documentation map | The file `docs-map.md` beside the owning project's ledger, with one entry per page and everything the page is made from, never shown to the reader. | `.claude/agents/docs-planner.md` |
| page | One page of the documentation, of one topic and one kind: how-to, explanation or reference. | `.claude/agents/docs-writer.md` |
| index | The documentation's index `docs/README.md`, derived by a script from the documentation map. | `.claude/agents/docs-planner.md` |
| mirrored | Said of a page that restates what the files owning its topic say. | `.claude/agents/docs-writer.md` |
| derived | Said of a page put together from named evidence in several files. | `.claude/agents/docs-writer.md` |
| pinned fact | A fact that no file of the project owns yet, such as an install line, kept in the recipe of the README and read by the documentation. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports. | `.claude/agents/docs-planner.md` |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
