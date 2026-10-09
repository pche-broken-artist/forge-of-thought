---
generated: 2026-10-09
made: derived
inputs-hash: 86a52a6428c1b6c3
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/document/SKILL.md
  - templates/ledger.md
---

# Glossary

The terms of the forge, one line each, with the file that defines
each: for the user who meets a word and wants to know what it means,
for the extender who must use the words as the engine uses them, and
for the evaluator reading the concept pages. This page was put
together from the files listed above: each term is taken from the
file that first defines it, and a term no file defines is not here.
The column "Defined in" names that file and, where it helps, the
section; a path is relative to the engine root.

## People and roles

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is carried to, teams, colleagues or the principal's future self, who act on it without the principal in the room. | `CLAUDE.md`, What this workspace is; `.claude/skills/forge/states/assignment.md`, Aim |
| Claude as cognitive extension | Claude's role: the principal's cognitive extension, owning structure, order, process discipline and document hygiene, proposing and never deciding. | `CLAUDE.md`, Roles |

## Documents and the chain

| Term | Meaning | Defined in |
|---|---|---|
| document | Every file of a project; each has one kind, and the kind says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain: composed by the principal with Claude, read by the reviewers, rendered from, versioned and rewritten freely. | `CLAUDE.md`, Document kinds |
| brief | `00-brief.md` or `00-brief-<name>.md`: the principal's own text of one whole of thinking, what he wants and why, free-form and without IDs, rough on purpose, mined into the intent. | `.claude/skills/forge/states/brief.md`, Target and Aim |
| intent | `10-intent.md`, the trunk of every project: the briefs chiselled into what the principal holds as positions, facts, threads and rejections, rewritten for coherence each round and never finished. | `.claude/skills/forge/states/intent.md`, Aim; `projects/forge/10-intent.md`, Document chain |
| position | An item of the intent, prefix `POS`: what the principal holds or wants and why, in as many words as it takes, naming what it comes from and dated once. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Document chain |
| fact | An item of the intent, prefix `FCT`: what is the case as the principal states it or as a source states it, not a stance; a source's fact cites its file, and verification is never demanded. | `CLAUDE.md`, ID scheme |
| thread | An open item, prefix `THR`, kept in the project's `threads.md`: an unresolved matter to elicit next, naming the artefact it concerns and carrying its origin, the principal's word, a document by path or Claude's synthesis. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | An item of the intent, prefix `REJ`: a direction that was dropped, with the reason it was dropped. | `CLAUDE.md`, ID scheme |
| assignment | `20-assignment.md`: the in-scope substance of the intent carried to the recipients, complete and precise, so that they can act on it without the principal in the room. | `.claude/skills/forge/states/assignment.md`, Target and Aim |
| solution design | `40-solution-design.md`: how the things wanted are realised, part by part, with the choices each rests on; it cites the layer above by ID, names what realises it by path and is kept current. | `.claude/skills/forge/states/solution-design.md`, Target and Aim |
| layer | An artefact below the intent that a project takes as it needs it, none a condition of another; a layer a project does not have is not missing. | `CLAUDE.md`, What this workspace is and Document chain |
| definition | The state file `.claude/skills/forge/states/<state>.md` of an artefact, worked through `/forge <state>`, saying what the artefact is, how it is found and its rules, in seven blocks: Target, Inputs, Aim, Partner, Map, Instruments and Course; also the file of a critic lens, a challenger persona or a check. | `CLAUDE.md`, Document chain and Templates; `projects/forge/10-intent.md`, Elicitation |
| template | The skeleton in `templates/` a document is created from; for an artefact it says what comes out, paired with the definition that says how it is found. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names, in the artefact's own vocabulary, what must be found for the artefact to be complete, walked as the question whether each area was consciously considered; neither headings nor a questionnaire. | `projects/forge/10-intent.md`, Elicitation; every definition, Map |

## Working together

| Term | Meaning | Defined in |
|---|---|---|
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds; the conversation is its medium, the interview one instrument, research and sources others. | `projects/forge/10-intent.md`, Elicitation |
| walkthrough | The working method for any list of items needing the principal's decision: one item per message, in order of weight, each closed with the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`, the verdicts carried to one write at the round's end. | `.claude/skills/walkthrough/SKILL.md`; `CLAUDE.md`, Working methods |
| round | One working conversation, whose answers and verdicts are carried in the conversation and written once at its end, as one version bump with as many history records as it made changes. | `CLAUDE.md`, prime directive 9 and Versioning & status |
| write | The principal's word on which Claude reflects the whole round back and, on his yes, writes everything carried in it as one version; until then what was agreed is nowhere yet. | `CLAUDE.md`, Working methods, One write per round; `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | `<file>.history.md` beside every versioned document: an append-only log of one record per change, carrying why it changed and what the wording was, never in the document's body. | `CLAUDE.md`, Versioning & status |
| archive | `<file>.history.archive.md`: a history table written before the log, moved there as it stands and immutable from then on; the history of an item is a search of both. | `CLAUDE.md`, Versioning & status |
| ledger | `ledger.md`: the single source of truth for a project's state, freely rewritten and kept current after every operation, its tables those of `templates/ledger.md`. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| decision | A record in `decisions.md`, prefix `DEC`: the principal's decision with its reason, rejected findings and challenges included; append-only. | `CLAUDE.md`, Document kinds and ID scheme |

## Resources

| Term | Meaning | Defined in |
|---|---|---|
| source | An external input as it arrived, stored in `sources/` by `/ingest`, immutable once registered, in one form: text, or a functional binary. | `CLAUDE.md`, Document kinds and Document chain, External inputs |
| bundle | A set of related files in `sources/<slug>/` that counts as one source with one ledger entry and carries its own `00-INDEX.md`. | `CLAUDE.md`, Document chain, External inputs |
| extract | The Markdown conversion of a binary source, produced by `scripts/doc2md.py` through `/ingest` on the principal's explicit word, which then is the source. | `CLAUDE.md`, Document chain, External inputs |
| research | A durable answer to one question: an immutable dated note in `research/`, written by `/research` and indexed. | `CLAUDE.md`, Document kinds and Repository layout |
| resource index | The `00-INDEX.md` of a `sources/` or `research/` directory: a light catalogue of what resources exist and what they are for, freely rewritten and an automatic input of no command. | `CLAUDE.md`, Document chain, Resource indexes |

## Rendering

| Term | Meaning | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`: how a render is made, with inputs, audience, instructions and the output template in one versioned file, iterated and never approved. | `CLAUDE.md`, Document kinds and Document chain, Renders |
| render | An audience-specific output generated from the chain by `/render` from its recipe, opening with its provenance, never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md` |
| plain file | The `.docx` or `.pptx` made beside a render by `/render` through pandoc where the recipe names a format: deterministic, cheap, repeated freely. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md`, step 7 |
| published file | The designed `.docx` or `.pptx` in `published/`, made from a render by `/publish` through a model, only on the principal's command. | `CLAUDE.md`, Document chain, Renders |
| genre | A kind of recipe with a definition and a skeleton of its own, `templates/recipe-<genre>.md`, composed through the interview of `/recipe <genre>`. | `CLAUDE.md`, Document chain, Renders; `projects/forge/10-intent.md`, Operating environment |
| stale | A render is stale when any version its provenance cites differs from the current version of that file, or a cited file no longer exists; a published file is stale once its render has been regenerated. | `.claude/skills/render/SKILL.md`, steps 5 and 8; `templates/ledger.md`, Published |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| critic | The isolated reviewer of document quality, never substance, run by `/critique <lens>`, producing findings in `reviews/`. | `CLAUDE.md`, Isolated reviewers |
| lens | One critic's specialisation: an agent file `critic-<lens>` whose Lens section says what it reads and goes after, under the shared contract. | `CLAUDE.md`, Isolated reviewers |
| challenger | The isolated reviewer of the substance of the thinking, never document quality, run by `/challenge <persona>`, producing challenges in `challenges/`. | `CLAUDE.md`, Isolated reviewers |
| persona | One challenger's specialisation: an agent file `challenger-<persona>` whose Lens section names the blind spots it hunts, under the shared contract. | `CLAUDE.md`, Isolated reviewers |
| check | The isolated reviewer of mechanical conformance with the conventions, one concern each, run by `/check <check>` on a project or on the engine; a run that finds nothing files nothing. | `CLAUDE.md`, Isolated reviewers |
| finding | Prefix `FND`: what a critic found about document quality or a check about conformance; its states open, resolved, rejected, parked and obsolete. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | Prefix `CHL`: a peer-review challenge of the substance; its states open, accepted, rejected, parked and obsolete, and an accepted one is mended wherever it needs to be. | `CLAUDE.md`, ID scheme and Isolated reviewers; `templates/ledger.md`, Challenges |
| contract | The skill holding the shared behaviour of one kind of reviewer, conduct and isolation, the subject and its boundary, the way of working and the shape of the output, preloaded by every agent of that kind. | `CLAUDE.md`, Isolated reviewers |

## Projects and the engine

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory `projects/<slug>` with a git repository of its own, of kind `thought` or `library` as its ledger header declares. | `CLAUDE.md`, Repository layout and Persistence; `templates/ledger.md` |
| thought project | A project of kind `thought`: it carries the chain, a brief, the intent and the layers it needs, with its records, ledger, resources and renders. | `CLAUDE.md`, Repository layout; `templates/ledger.md` |
| library | A project of kind `library`, prefix `lib-`: material shared across projects with no chain, only a ledger, sources, research and a README that catalogues what it holds. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Document chain |
| dependency | A document of another repository the project relies on, registered by path in the ledger's Dependencies table with no version, since its owner maintains it. | `templates/ledger.md`, Dependencies; `CLAUDE.md`, Ledger |
| engine | Forge of Thought itself: one git repository of `CLAUDE.md`, skills, agents, scripts and templates, which specifies and implements nothing, run through its own process as the project `projects/forge`. | `CLAUDE.md`, What this workspace is, Persistence and The system's own project |
| instance | One installed copy of the engine on a machine, with its instance facts in `CLAUDE.local.md` and its session model in `.claude/settings.local.json`, both kept out of the repository. | `CLAUDE.md`, What this workspace is and Repository layout |
| instance fact | Who the principal is and what language the conversation runs in: a fact of the instance, living in `CLAUDE.local.md`, never in the engine, in a reviewer's report or on a page. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, Operating environment |
| session model | The one model the whole forge runs on, chosen once as an instance preference: every command, chain state and reviewer inherits it, and speed is bought with context, never with a weaker model. | `CLAUDE.md`, Isolated reviewers; `projects/forge/10-intent.md`, Operating environment |

## Saving and releasing

| Term | Meaning | Defined in |
|---|---|---|
| save | `/save`: runs its check, then commits and pushes one repository, or every one with changes, on whatever branch is checked out, with no render. | `CLAUDE.md`, Persistence |
| release | `/release`, from `main` only: runs its checks, re-renders the README and the release notes, then saves with the release message and the tag. | `CLAUDE.md`, Persistence |
| major | An integer version, a signed-off one: its status is `approved`, and a release at an approved major carries the tag `v<major>`. | `CLAUDE.md`, Versioning & status and Persistence; `projects/forge/10-intent.md`, Operating environment |
| tag | A git mark on a release: `v<major>` at an approved major, set by `/release`; any other tag is the principal's request, with a free name. | `CLAUDE.md`, Persistence |
| immutable | Never edited after creation, or for a source after its registration: reviews, challenges, sources and research; a process rule, not a git mechanism, and corrections happen downstream. | `CLAUDE.md`, Versioning & status and Persistence |
| mined | How far the intent has absorbed a brief, `pending`, `partial`, `mined` or `dropped` in the ledger's Briefs table; a brief is mined on the principal's word, approved or not. | `templates/ledger.md`, Briefs; `.claude/skills/forge/states/brief.md`, Aim |

## Documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | The generated pages of one topic each in `docs/` with their index, for the user, the extender and the evaluator, in five sections filled only where the project has material, made by `/document` and never composed by hand. | `CLAUDE.md`, Document chain, Documentation; `.claude/skills/document/SKILL.md` |
| map | `docs-map.md` beside the owning project's ledger: one entry per page with everything the page is made from, written by the planner in a documentation run and never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/skills/document/SKILL.md` |
| page | A page of the documentation, or its index: generated, of one kind, how-to, explanation or reference, overwritten by the documentation run and never a source of truth. | `CLAUDE.md`, Document kinds; `projects/forge/10-intent.md`, Growth path |
| index | `docs/README.md`: derived from the map by `scripts/docs-index.py` with the version of the owning project's intent, listing every page and each reader's path through them. | `.claude/skills/document/SKILL.md`, step 5; `projects/forge/10-intent.md`, Growth path |
| mirrored | A page that restates the files that own its topic and cannot drift from them; it leaves the model no room, so it is written on a faster model. | `projects/forge/10-intent.md`, Growth path and Operating environment; `.claude/skills/document/SKILL.md`, step 4 |
| derived | A page put together from named evidence by the reasoning its entry gives, saying so in its opening; written on the session model. | `projects/forge/10-intent.md`, Growth path and Operating environment; `.claude/skills/document/SKILL.md`, step 4 |

## See also

- [About what the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.
