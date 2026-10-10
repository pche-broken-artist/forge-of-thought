---
generated: 2026-10-10
made: derived
inputs-hash: 4c4c3d13b5c92161
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
  - templates/recipe-readme.md
---

# Glossary

The terms of the forge, one sentence each, with the file that
defines the term. For anyone who meets a word of the forge and wants
to know what it means and where that meaning is owned: the user, the
extender and the evaluator alike. The page was put together from the
files listed in its front-matter; each term is taken from the file
that first defines it, and a term no file defines is not here.

## Roles

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is for, teams, colleagues or the principal's future self, who must be able to act on it without the principal in the room. | `CLAUDE.md`, What this workspace is; `.claude/skills/forge/states/assignment.md`, Aim |
| Claude | The cognitive extension of the principal: owns structure, order, process discipline and document hygiene, proposes and never decides. | `CLAUDE.md`, Roles |

## Documents and the chain

| Term | Meaning | Defined in |
|---|---|---|
| document | Every file of a project; each has one kind, which says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain, composed by the principal with Claude, versioned and rewritten freely; what each one is, its definition says. | `CLAUDE.md`, Document kinds |
| brief | The principal's idea put together: what he wants, why and what he does not want, in free form and rough on purpose, mined into the intent when he says so. | `.claude/skills/forge/states/brief.md`, Aim |
| intent | The trunk of every project, `10-intent.md`: the briefs chiselled into what the principal holds, as positions, facts, threads and rejections, rewritten for coherence each round and never finished. | `.claude/skills/forge/states/intent.md`, Aim; `projects/forge/10-intent.md` |
| position | What the principal holds or wants and why, in as many words as it takes, naming the brief or source it comes from and dated once. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md` |
| fact | What is the case, on the principal's word or on a source's cited to its file; not a stance, and verification is never demanded. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md` |
| thread | An open, unresolved matter to elicit next, kept in the project's `threads.md`, naming the artefact it concerns and carrying its origin: the principal's word, a document by path, or Claude's synthesis. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | A direction the principal dropped, kept in the intent with the reason it was dropped. | `CLAUDE.md`, ID scheme |
| assignment | The layer that carries the in-scope substance of the intent to the recipients, complete and precise: who they are, what must be true at the end, what is theirs to decide, what they shall not do and what is left open on purpose. | `.claude/skills/forge/states/assignment.md`, Aim |
| solution design | The layer that says how the things wanted are realised, part by part, with the choices each rests on, kept current and read by whoever realises the solution. | `.claude/skills/forge/states/solution-design.md`, Aim |
| layer | An artefact of the chain below the intent, taken as the project needs it, none a condition of another; a layer a project does not have is not missing. | `CLAUDE.md`, What this workspace is; Document chain |
| definition | The state file of an artefact, `.claude/skills/forge/states/<state>.md`, which says what the artefact is, how it is found and owns its rules, in seven blocks: Target, Inputs, Aim, Partner, Map, Instruments, Course. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md` |
| template | The skeleton in `templates/` that says what comes out of a definition, and the canonical skeleton of every other new document. | `CLAUDE.md`, Document chain; Templates |
| Map | The block of a definition that names, in the artefact's own vocabulary, what must be found for the artefact to be complete, walked as the question whether each area has been consciously considered; neither headings nor a questionnaire. | `projects/forge/10-intent.md`; each definition's Map block |

## Working together

| Term | Meaning | Defined in |
|---|---|---|
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds; the conversation is its medium, the interview, research and sources its instruments. | `projects/forge/10-intent.md`; `CLAUDE.md`, Working methods |
| walkthrough | The way any list of items needing the principal's decision is worked: one item per message, in order of weight, each closed with the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`, the verdicts carried to one write at the round's end. | `.claude/skills/walkthrough/SKILL.md`; `CLAUDE.md`, Working methods |
| round | One working conversation over an artefact or open items, carried in the conversation and written once at its end, as one version bump with its changes recorded in the history. | `CLAUDE.md`, Prime directives (9); Working methods |
| write | The principal's word that ends a round: Claude reflects the whole round back and, on his yes, writes everything carried as one version. | `CLAUDE.md`, Working methods; `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write |

## Records and state

| Term | Meaning | Defined in |
|---|---|---|
| history companion | The append-only log `<file>.history.md` beside every versioned document, one record per change with its reason; the body is the current state, the companion the record. | `CLAUDE.md`, Versioning & status |
| archive | `<file>.history.archive.md`: a history table written before the log, moved as it stands and immutable from then on, searched together with the log. | `CLAUDE.md`, Versioning & status |
| ledger | `ledger.md`, the single source of truth for a project's state, freely rewritten and kept current after every operation; it cites and never copies. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| decision | A decision of the principal with its reason, rejected findings and challenges included, appended to `decisions.md`. | `CLAUDE.md`, Document kinds; ID scheme |
| immutable | Never edited once created, a source never once registered: a process rule of the forge, not a mechanism of git; corrections happen downstream. | `CLAUDE.md`, Versioning & status; Persistence |

## Resources

| Term | Meaning | Defined in |
|---|---|---|
| source | External input as it arrived, stored in `sources/` by `/ingest`, immutable once registered, in one form: text or a functional binary. | `CLAUDE.md`, Document chain, External inputs |
| bundle | A set of related files in `sources/<slug>/` that counts as one source with one ledger entry, catalogued by its own `00-INDEX.md`. | `CLAUDE.md`, Document chain, External inputs |
| extract | The Markdown conversion of a binary source, made by `scripts/doc2md.py` on the principal's explicit word, which then is the source. | `CLAUDE.md`, Document chain, External inputs |
| research | A durable answer to one question, written by `/research` into `research/` as a dated, immutable note. | `CLAUDE.md`, Document kinds; Prime directives (4) |
| resource index | The `00-INDEX.md` of a `sources/` or `research/` directory: a light, freely rewritten catalogue of what the resources are and are for, tracking nothing and an automatic input of no command. | `CLAUDE.md`, Document chain, Resource indexes |
| dependency | A document of another repository, typically a library document, that a project relies on, registered in the ledger by path without a version. | `templates/ledger.md`, Dependencies |

## Renders

| Term | Meaning | Defined in |
|---|---|---|
| recipe | The versioned file `recipes/<recipe>.md` that says how a render is made: inputs, audience, instructions and the output template; a tool, iterated and never approved. | `CLAUDE.md`, Document chain, Renders |
| render | An audience-specific output generated from the chain by `/render` from its recipe, in isolation, opening with its provenance; never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md` |
| plain file | The `.docx` or `.pptx` made beside a render by `/render` through pandoc where the recipe names a format: deterministic, cheap, repeated freely. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md` |
| published file | The designed file in `published/` made from a render by `/publish` through a model: expensive, only on the principal's command. | `CLAUDE.md`, Document chain, Renders |
| genre | A kind of recipe with a skeleton of its own, `templates/recipe-<genre>.md`, composed through the interview `/recipe <genre>`; the README and the release notes are genres. | `CLAUDE.md`, Document chain, Renders |
| stale | A render is stale when any version its provenance cites differs from the current version of that file, or a cited file no longer exists; a published file is stale once its render has been regenerated after it. | `.claude/skills/render/SKILL.md`, steps 5 and 8 |
| pinned fact | A fact of the project no file owns yet, kept in the readme recipe's section Pinned facts, not printed by the README but read by the documentation's planner as an owner, and dropped the day a file owns it. | `templates/recipe-readme.md`, Pinned facts |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| critic | The isolated reviewer of document quality, never substance, run by `/critique <lens>`; its report is a dated, immutable file of findings in `reviews/`. | `CLAUDE.md`, Isolated reviewers |
| lens | One critic's agent file: what that critic reads and goes after. | `CLAUDE.md`, Isolated reviewers |
| challenger | The isolated reviewer of the substance of the thinking, never document quality, run by `/challenge <persona>`; its report is a dated, immutable file of challenges in `challenges/`. | `CLAUDE.md`, Isolated reviewers |
| persona | One challenger's agent file: the blind spots that challenger hunts. | `CLAUDE.md`, Isolated reviewers |
| check | The reviewer of mechanical conformance with the conventions, never substance or quality, one concern per check, run by `/check <check>` on a project or on the engine; a run that finds nothing files nothing. | `CLAUDE.md`, Isolated reviewers |
| finding | What a critic or a check reports (prefix FND), kept in the ledger with a state: open, resolved, rejected, parked or obsolete. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | What a challenger reports on the substance (prefix CHL), kept in the ledger with a state: open, accepted, rejected, parked or obsolete; also the dated file of one challenger's run. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Challenges |
| contract | The one skill per kind of agent that owns the shared conduct, isolation, subject, way of working and output shape, preloaded into every agent of that kind; an agent's own file only specialises it. | `CLAUDE.md`, Isolated reviewers |

## Projects and the engine

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory `projects/<slug>` and a git repository of its own, of kind thought or library, which the engine does not know. | `CLAUDE.md`, Repository layout |
| thought project | A project of kind `thought`: the chain, with its briefs, intent, layers, records, resources, recipes and documentation. | `CLAUDE.md`, Repository layout |
| library | A project of kind `library`: material shared across projects, with no chain and no records, only the ledger, sources, research and a README that catalogues what it holds. | `CLAUDE.md`, Repository layout; Document kinds |
| engine | Forge of Thought itself: one git repository that holds the rules, skills, agents, scripts and templates every project is run under, and specifies rather than implements. | `CLAUDE.md`, What this workspace is; Persistence |
| instance | One installation of the engine on a machine, prepared by `/setup`, with its own `CLAUDE.local.md`. | `CLAUDE.md`, What this workspace is; Commands |
| instance fact | What belongs to an instance and not to the system, who the principal is and what language the conversation runs in, kept in `CLAUDE.local.md` and never in the engine or in any outward-facing file. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md` |
| session model | The one model a session runs on, set in `.claude/settings.local.json`, which every agent of the forge inherits; speed is bought with context, never with a weaker model. | `CLAUDE.md`, Isolated reviewers; Repository layout |

## Saving and releasing

| Term | Meaning | Defined in |
|---|---|---|
| save | `/save`: runs its check, then commits and pushes one repository, or every one with changes, on whatever branch is checked out, with no render. | `CLAUDE.md`, Persistence |
| release | `/release`: from `main` only, runs its checks, re-renders the README and the release notes, then saves with the release message and tag. | `CLAUDE.md`, Persistence |
| major | A signed-off, integer version; on the forge's own intent, one that closes a set of features the principal names and passes every check, both critic lenses and one challenge before its tag. | `CLAUDE.md`, Versioning & status; `projects/forge/10-intent.md` |
| tag | A git tag on a release: `v<major>` is `/release`'s to give, any other tag is the principal's request with a free name. | `CLAUDE.md`, Persistence |
| mined | The state of a brief whose substance the intent has absorbed, on the principal's word; the ledger records it as pending, partial, mined or dropped. | `.claude/skills/forge/states/brief.md`, Aim; `templates/ledger.md`, Briefs |

## The documentation

| Term | Meaning | Defined in |
|---|---|---|
| documentation | Pages of one topic each in `docs/` with an index, for the user, the extender and the evaluator, in a standard outline of five sections filled only where the project has material, generated by `/document` and never composed by hand. | `CLAUDE.md`, Document chain, Documentation; `projects/forge/10-intent.md` |
| map | `docs-map.md`, the documentation map beside the owning project's ledger: one entry per page and everything a page is made from, written by the planner and never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/skills/document/SKILL.md` |
| page | A page of the documentation, or its index: one topic, of one kind, generated from its entry in the map and the files the entry names, never a source of truth. | `CLAUDE.md`, Document kinds; `projects/forge/10-intent.md` |
| index | As a kind, the catalogue of a resource directory (see resource index); of the documentation, `docs/README.md`, derived from the map by `scripts/docs-index.py`, listing every page and naming each reader's path. | `CLAUDE.md`, Document kinds; `.claude/skills/document/SKILL.md`; `templates/recipe-readme.md` |
| mirrored | A page that restates what the files owning its topic say, so that it cannot drift from them. | `projects/forge/10-intent.md`; `.claude/skills/document/SKILL.md` |
| derived | A page put together from named evidence by the reasoning its map entry gives, saying in its opening that it was put together from those files. | `projects/forge/10-intent.md`; `.claude/skills/document/SKILL.md` |

## See also

- [About what the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.
