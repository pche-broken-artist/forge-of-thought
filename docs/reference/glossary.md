---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/render/SKILL.md
  - templates/ledger.md
---

# Glossary

The terms of Forge of Thought, one sentence each, with the file that
defines each, for anyone who uses the forge, extends it or weighs
whether to adopt it. The page was put together from the files listed
above: each term is taken from the file that first defines it and
said in one sentence; a term no file defines is left out. Where a
definition is longer, the file named beside it holds the whole.

## People and roles

| Term | Meaning | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged, who supplies ideas, answers and decisions and has final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Whoever receives an assignment: teams, colleagues or the principal's future self. | `CLAUDE.md`, What this workspace is |
| Claude, cognitive extension | The principal's cognitive extension, which owns structure, order, process discipline and document hygiene, and proposes but never decides. | `CLAUDE.md`, Roles |

## Documents and the chain

| Term | Meaning | Defined in |
|---|---|---|
| document | The word for every file of a project, each with one kind that says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain: one the principal composes, the reviewers read and the renders are generated from. | `CLAUDE.md`, Document kinds |
| brief | The principal's idea put together, what he wants and why, rough on purpose, where a chain starts (`00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking). | `.claude/skills/forge/states/brief.md`, Target and Aim |
| intent | The trunk of the chain, `10-intent.md`, which chisels the briefs into what the principal holds as positions, facts, threads and rejected directions. | `.claude/skills/forge/states/intent.md`, Target and Aim |
| position | An item of the intent saying what the principal currently holds or wants and why, naming what it comes from. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Document chain and Structure and style of an assignment |
| fact | What is the case, as the principal states it or as a source states it with its file cited; not a stance, and verification is never demanded. | `CLAUDE.md`, ID scheme |
| thread | An unresolved matter to elicit next, kept in the project's `threads.md`, naming the artefact it concerns and carrying its origin: the principal's word, a document, or Claude's synthesis. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | A direction the principal dropped, kept in the intent with the reason it was dropped. | `CLAUDE.md`, ID scheme |
| assignment | `20-assignment.md`, which carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act on it without the principal in the room. | `.claude/skills/forge/states/assignment.md`, Target and Aim |
| solution design | `40-solution-design.md`, which says how the things wanted are realised, part by part, with the choices they rest on, for whoever realises the solution. | `.claude/skills/forge/states/solution-design.md`, Target and Aim |
| layer | An artefact of the chain below the intent, which a project takes only where it needs it, so that a layer it does not have is not missing. | `CLAUDE.md`, Document chain |
| definition | The state file of an artefact, `.claude/skills/forge/states/<state>.md`, which says what the artefact is and how it is found and owns its rules, in seven blocks: Target, Inputs, Aim, Partner, Map, Instruments and Course. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| template | The canonical skeleton in `templates/` that says what comes out, paired with an artefact's definition. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names what must be found for the artefact to be complete, walked as the question whether each area has been consciously considered, and never a questionnaire. | `projects/forge/10-intent.md`, Elicitation |
| mined | How far the intent has absorbed a brief, kept in the ledger's Briefs table as `pending`, `partial`, `mined` or `dropped`. | `.claude/skills/forge/states/brief.md`, Aim; `templates/ledger.md`, Briefs |
| history companion | The append-only `<file>.history.md` beside every versioned document, a log of one record per change, so that the body holds only the current state. | `CLAUDE.md`, Versioning & status |
| archive | `<file>.history.archive.md`, the history table a companion held before the log began, moved as it stood and immutable from then on. | `CLAUDE.md`, Versioning & status |
| ledger | `ledger.md`, the single source of truth for a project's state, freely rewritten and kept current after every operation. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| decision | A record in the append-only `decisions.md` of a decision of the principal with its reason, rejected findings and challenges included. | `CLAUDE.md`, Document kinds and ID scheme |
| immutable | Never edited once created, or for a source once registered, with corrections made downstream; reviews, challenges, sources and research are immutable. | `CLAUDE.md`, Versioning & status |

## Working together

| Term | Meaning | Defined in |
|---|---|---|
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds, with the conversation as its medium and the interview, research and sources as its instruments. | `projects/forge/10-intent.md`, Elicitation |
| walkthrough | The way any list needing the principal's decision is worked: one item per message, in order of weight, each closed with the line `(a)ccept / (m)odify / (r)eject / (p)ark`. | `CLAUDE.md`, Working methods; `.claude/skills/walkthrough/SKILL.md` |
| round | One working conversation, whose agreed answers are carried in the conversation and written once at its end as one version. | `CLAUDE.md`, prime directive 9 and Working methods |
| write | The principal's word, typed in full, on which Claude reflects the whole round back and, on his yes, writes it to file; until then nothing agreed is written anywhere. | `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write; `CLAUDE.md`, prime directive 9 |

## Resources

| Term | Meaning | Defined in |
|---|---|---|
| source | An external input as it arrived, kept in `sources/` and immutable once registered. | `CLAUDE.md`, Document kinds and Document chain |
| bundle | A set of related files kept as a subdirectory `sources/<slug>/`, which counts as one source with one ledger entry and carries its own `00-INDEX.md`. | `CLAUDE.md`, Document chain |
| extract | The Markdown made from a binary through `/ingest` on the principal's explicit word, which then is the source in place of the binary. | `CLAUDE.md`, Document chain |
| research | A durable, immutable answer to one question, written by `/research` into `research/`. | `CLAUDE.md`, Document kinds |
| resource index | The `00-INDEX.md` of `sources/` or `research/`, a light catalogue of what each resource is and is for, freely rewritten and tracking nothing. | `CLAUDE.md`, Document chain |
| dependency | A document of another repository that a project cites, typically a library document, registered in the ledger's Dependencies table without a version. | `templates/ledger.md`, Dependencies; `CLAUDE.md`, Ledger |

## Renders

| Term | Meaning | Defined in |
|---|---|---|
| recipe | The versioned file `recipes/<recipe>.md` holding a render's inputs, audience, instructions and output template, iterated and never approved. | `CLAUDE.md`, Document chain and Document kinds |
| render | An audience-specific output generated from the chain by `/render`, never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain and Document kinds |
| genre | A kind of recipe composed through its own interview by `/recipe <genre>`, from the skeleton `templates/recipe-<genre>.md`. | `CLAUDE.md`, Document chain |
| plain file | The `.docx` or `.pptx` that `/render` makes beside a render through pandoc where the recipe names a format. | `CLAUDE.md`, Document chain; `.claude/skills/render/SKILL.md`, step 7 |
| published file | The designed file that `/publish` makes from a render through a model, only on the principal's command, into `published/`. | `CLAUDE.md`, Document chain |
| stale | A render is stale when any version cited in its provenance differs from the current version of that file or a cited file no longer exists, and a published file is stale once its recipe is rendered again. | `.claude/skills/render/SKILL.md`, steps 5 and 8; `templates/ledger.md`, Published |

## Reviewers

| Term | Meaning | Defined in |
|---|---|---|
| critic | An isolated reviewer of document quality, never of substance, whose findings are filed in `reviews/`. | `CLAUDE.md`, Isolated reviewers |
| lens | One kind of critic, with what it reads and goes after in its own agent file `critic-<lens>`. | `CLAUDE.md`, Isolated reviewers |
| challenger | An isolated reviewer of the substance of the thinking, never of document quality, whose challenges are filed in `challenges/`. | `CLAUDE.md`, Isolated reviewers |
| persona | One kind of challenger, with the blind spots it hunts in its own agent file `challenger-<persona>`. | `CLAUDE.md`, Isolated reviewers |
| check | An isolated reviewer of mechanical conformance with the conventions, owning one concern, whose report is filed only when it finds something. | `CLAUDE.md`, Isolated reviewers |
| finding | An item raised by a critic on document quality or by a check on conformance, kept in the ledger as `open`, `resolved`, `rejected`, `parked` or `obsolete`. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | An item raised by a challenger on the substance, kept in the ledger as `open`, `accepted`, `rejected`, `parked` or `obsolete`. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Challenges |
| contract | The skill holding the shared behaviour of one kind of reviewer (conduct and isolation, the subject and its boundary, the way of working and the shape of the output), of which each agent's Lens section is only a specialisation. | `CLAUDE.md`, Isolated reviewers |

## Projects, engine and git

| Term | Meaning | Defined in |
|---|---|---|
| project | A directory `projects/<slug>/` that is a git repository of its own, with its kind declared in the header of its ledger. | `CLAUDE.md`, Repository layout and Persistence; `templates/ledger.md` |
| thought project | A project of kind `thought`, the default, which holds a chain. | `CLAUDE.md`, Repository layout; `templates/ledger.md` |
| library | A project of kind `library`, named `lib-<name>`, with no chain: material shared across projects, held as a ledger, sources, research and a README that catalogues them. | `CLAUDE.md`, Repository layout; `projects/forge/10-intent.md`, Document chain |
| engine | Forge of Thought's own git repository, holding `CLAUDE.md`, `.claude/`, `templates/` and `scripts/`, kept apart from the projects, each of which is a repository of its own. | `CLAUDE.md`, Repository layout and Persistence |
| instance | One copy of the engine prepared by `/setup` after cloning, with its own `CLAUDE.local.md` kept out of the repository. | `CLAUDE.md`, What this workspace is and Commands; `projects/forge/10-intent.md`, Operating environment |
| instance fact | A fact of one instance and not of the system, such as who the principal is and what language the conversation runs in, kept in `CLAUDE.local.md` and never in the engine or a reviewer's report. | `CLAUDE.md`, What this workspace is and Isolated reviewers; `projects/forge/10-intent.md`, Operating environment |
| session model | The one model the whole forge runs on, every command and reviewer included, chosen once as an instance preference with no per-agent pins. | `CLAUDE.md`, Isolated reviewers; `projects/forge/10-intent.md`, Operating environment |
| save | `/save`, which runs its check and then commits and pushes on whatever branch is checked out, with no render. | `CLAUDE.md`, Persistence |
| release | `/release`, which from `main` only runs its checks, re-renders the README and release notes and then saves with the release message and tag. | `CLAUDE.md`, Persistence |
| major | An integer version, which denotes a signed-off version, such as 1.0 or 2.0. | `CLAUDE.md`, Versioning & status; `projects/forge/10-intent.md`, Versioning and state |
| tag | A git tag set at a save or a release: `v<major>` where `/release` says so, any other tag a free name on the principal's request. | `CLAUDE.md`, Persistence |

## See also

- [About what the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.
