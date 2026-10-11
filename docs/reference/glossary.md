---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 5820bc4d2d90f396
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#Elicitation
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/skills/walkthrough/SKILL.md
  - .claude/skills/render/SKILL.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/pull/SKILL.md
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

A glossary is the list of the terms the forge uses, each explained
in one sentence with the file that defines it. This page is for the
user, the extender and the evaluator alike: whoever meets a word of
the forge on another page and wants its meaning finds it here, and
the file named beside it is where the full rule stands. The forge
itself, the engine that carries an idea through a chain of versioned
documents under isolated review, is explained in
[What the forge is and is not](../about/what-it-is-and-is-not.md).
The terms are grouped by what they belong to; within a group they
stand in the order a reader meets them.

## The people and the machine

| Term | In one sentence | Defined in |
|---|---|---|
| principal | Whoever's thinking is being forged: he supplies ideas, answers and decisions and is the final authority on all content. | `CLAUDE.md`, Roles |
| recipients | Those an assignment is carried to, such as teams, colleagues or the principal's future self, who act on it without the principal in the room. | `CLAUDE.md`, What this workspace is; `.claude/skills/forge/states/assignment.md`, Aim |
| Claude | The cognitive extension of the principal: it owns structure, order, process discipline and document hygiene, and it proposes, never decides. | `CLAUDE.md`, Roles |
| session | One conversation of Claude with the principal, from its opening to `/end`, together with the context it has read on the way; what lives only in it is lost when it ends. | `CLAUDE.md`, Commands (`/end`); `projects/forge/10-intent.md`, Operating environment |
| harness | The program Claude runs in, Claude Code, which enforces the principal's word where it can: it keeps Claude from sensitive paths, has web access approved per domain and guards the commands that write. | `projects/forge/10-intent.md`, Operating environment; `.claude/skills/document/SKILL.md`, Harness note |

## The documents of the chain

| Term | In one sentence | Defined in |
|---|---|---|
| document | The word for every file of a project; every document has one kind, which says what it is, who writes it, whether it is versioned and how it behaves. | `CLAUDE.md`, Document kinds |
| artefact | A document of the chain, composed by the principal with Claude, versioned and rewritten freely; what each one is, its definition says. | `CLAUDE.md`, Document kinds and Document chain |
| brief | The principal's idea put together, `00-brief.md` or `00-brief-<name>.md`: free form, rough on purpose, the place where thoughts are thrown in before they are sifted, and mined into the intent when the principal says so. | `.claude/skills/forge/states/brief.md`, Target and Aim |
| mined | Of a brief: absorbed into the intent by `/forge intent`; how far, the ledger's Mined column says (pending, partial, mined, dropped). | `.claude/skills/forge/states/brief.md`, Course; `templates/ledger.md`, Briefs |
| intent | `10-intent.md`, the trunk of the chain: the briefs chiselled into what the principal holds, as positions, facts, threads and rejections, rewritten for coherence each round and never finished. | `.claude/skills/forge/states/intent.md`, Aim; `projects/forge/10-intent.md`, Document chain |
| position | A POS item of the intent: what the principal holds or wants and why it holds, in as many words as it takes, naming the brief or source it comes from and dated once. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Document chain |
| fact | An FCT item of the intent: what is the case, stated by the principal on his word or by a source cited to its file, not a stance, and never required to be verified. | `CLAUDE.md`, ID scheme; `projects/forge/10-intent.md`, Structure and style of an assignment |
| thread | A THR item in the project's `threads.md`: an open matter to elicit next, naming in square brackets the artefact it concerns, carrying its origin (the principal's word, a document by path or Claude's synthesis) and the working debate until it is settled. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Threads and files |
| rejected direction | A REJ item of the intent: a direction the principal dropped, kept with the reason it was dropped. | `CLAUDE.md`, ID scheme; `.claude/skills/forge/states/intent.md`, Aim |
| assignment | `20-assignment.md`: the in-scope substance of the intent carried to the recipients, complete and precise enough for them to act on it without the principal in the room. | `.claude/skills/forge/states/assignment.md`, Target and Aim |
| solution design | `40-solution-design.md`: how the things wanted are realised, part by part, with the choice each part rests on, kept current and read by whoever realises the solution. | `.claude/skills/forge/states/solution-design.md`, Target and Aim |
| layer | An artefact below the intent, `NN-<layer>.md`, which a project takes as it needs it, none a condition of another; a layer a project does not have is not missing. | `CLAUDE.md`, Document chain and Ledger |
| definition | The state file `.claude/skills/forge/states/<state>.md` of an artefact: what the artefact is, how it is found and its rules, in seven blocks (Target, Inputs, Aim, Partner, Map, Instruments, Course), worked through `/forge <state>`. | `CLAUDE.md`, Document chain; `projects/forge/10-intent.md`, Elicitation |
| template | A skeleton in `templates/`, the canonical shape of a new document; for an artefact it says what comes out and stands beside the definition as a pair. | `CLAUDE.md`, Document chain and Templates |
| Map | The block of a definition that names, in the artefact's own vocabulary, what must be found for the artefact to be complete, walked as the question whether each area was consciously considered; neither a questionnaire nor a list of headings. | `projects/forge/10-intent.md`, Elicitation |

## The conversation

| Term | In one sentence | Defined in |
|---|---|---|
| elicitation | The process by which the principal and Claude find an artefact together and form the knowledge it holds; the conversation is its medium, and the interview, research and sources are its instruments. | `projects/forge/10-intent.md`, Elicitation |
| working method | A named way a working conversation runs, such as the walkthrough or Step by step: not a command, it applies whenever its situation arises, and the principal may invoke it in a word. | `CLAUDE.md`, Working methods |
| prime directive | One of the ten numbered rules of Claude's conduct at the head of `CLAUDE.md`, from "When unsure, ask" to "One mechanism lives in one place". | `CLAUDE.md`, Prime directives |
| walkthrough | The working method by which any list of items needing the principal's decision is worked one item per message, in order of weight, each item closed with a verdict and the verdicts carried to one write at the round's end. | `.claude/skills/walkthrough/SKILL.md`; `CLAUDE.md`, Working methods |
| verdict | The principal's answer to one item of a walkthrough, given on the line `(a)ccept / (m)odify / (r)eject / (p)ark`, with `obsolete` as the fifth word, typed in full. | `.claude/skills/walkthrough/SKILL.md`, The verdict |
| round | One working conversation whose agreed changes are carried in the conversation and written once at its end on the principal's word, as one version bump and as many history records as it made changes. | `CLAUDE.md`, Prime directives (9) and Versioning & status |
| write | The principal's word that closes a round: Claude reflects the whole round back and, on his yes, writes everything carried as one version. | `.claude/skills/walkthrough/SKILL.md`, From verdicts to the write; `CLAUDE.md`, Working methods |

## Records and state

| Term | In one sentence | Defined in |
|---|---|---|
| history companion | The append-only file `<file>.history.md` beside every versioned document, a log of one record per change in the shape of `templates/history.md`; the body is the current state, the companion the record. | `CLAUDE.md`, Versioning & status |
| record | One entry of a history log, written in the same step as the change by the one who decided it, carrying why it changed, what was said on the way and the previous wording in `Was`. | `CLAUDE.md`, Versioning & status |
| archive | `<file>.history.archive.md`: the table of a history companion written before the log, moved there as it stands and immutable from then on. | `CLAUDE.md`, Versioning & status |
| ledger | `ledger.md`, the single source of truth for the state of a project, freely rewritten and kept current after every operation; it cites and never copies. | `CLAUDE.md`, Ledger; `templates/ledger.md` |
| decision | A DEC record in the append-only `decisions.md`: a decision of the principal with its reason, rejected findings and challenges among them. | `CLAUDE.md`, Document kinds and ID scheme |
| immutable | Never edited after creation, or after registration for a source: reviews, challenges, sources, research and a history archive are immutable, as a process rule and not a git mechanism, and corrections happen downstream. | `CLAUDE.md`, Versioning & status and Persistence (git) |

## Resources

| Term | In one sentence | Defined in |
|---|---|---|
| source | An external input kept in `sources/` as it arrived, immutable once registered, in one form, text or a functional binary. | `CLAUDE.md`, Document chain, External inputs |
| bundle | A set of related files in `sources/<slug>/` that counts as one source with one ledger entry and carries its own `00-INDEX.md`. | `CLAUDE.md`, Document chain, External inputs |
| extract | The Markdown conversion of a binary source, made by `scripts/doc2md.py` through `/ingest` on the principal's explicit word, which then is the source. | `CLAUDE.md`, Document chain, External inputs |
| research | A durable answer to one question, written by `/research` into `research/` as a dated, immutable note and indexed. | `CLAUDE.md`, Document kinds and Prime directives (4) |
| resource index | The `00-INDEX.md` of a `sources/` or `research/` directory: a light, freely rewritten catalogue of what the resources are and are for, which tracks nothing and is an automatic input of no command. | `CLAUDE.md`, Document chain, External inputs |
| Role | The free-text field of a source's entry in the resource index that says what the source is for; registering a source does not imply intake, and the principal alone directs how and when it is used. | `CLAUDE.md`, Document chain, External inputs |

## Renders

| Term | In one sentence | Defined in |
|---|---|---|
| recipe | `recipes/<recipe>.md`, how a render is made: its inputs, audience, instructions and output template in one versioned file, iterated and never approved. | `CLAUDE.md`, Document chain, Renders |
| render | An audience-specific output generated from the chain by `/render` from its recipe, never edited by hand and never a source of truth. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md` |
| plain file | The `renders/<recipe>.docx` or `.pptx` made beside a render by `/render` through pandoc where the recipe's `## Format` section names a format. | `CLAUDE.md`, Document chain, Renders; `.claude/skills/render/SKILL.md`, step 7 |
| published file | The designed `published/<recipe>.docx` or `.pptx` made from a render by `/publish` through a model, only on the principal's command; the ledger's Published table says whether it is current or stale. | `CLAUDE.md`, Document chain, Renders; `templates/ledger.md`, Published |
| genre | A kind of recipe with a skeleton `templates/recipe-<genre>.md`, composed through a genre interview by `/recipe <genre>`; readme and release-notes are genres. | `CLAUDE.md`, Document chain, Renders |
| provenance | The YAML front-matter a render opens with, naming its project, its recipe with its version and every input with its version, mirrored in the ledger's Renders table. | `.claude/skills/render/SKILL.md`, step 5 |
| stale | The state of a render whose provenance cites a version that differs from the file's current version, or a file that no longer exists, and of a published file whose render was regenerated after it. | `.claude/skills/render/SKILL.md`, steps 5 and 8 |

## Reviewers

| Term | In one sentence | Defined in |
|---|---|---|
| critic | The isolated reviewer of document quality, never substance, run as `/critique <lens> [artefact]`; it writes findings into `reviews/`. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| lens | The specialisation of one critic: the agent file `critic-<lens>`, whose Lens section says what it reads and goes after. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md` |
| challenger | The isolated reviewer of the substance of the thinking, never document quality, run as `/challenge <persona> [artefact]` and allowed to search the web; it writes challenges into `challenges/`. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md` |
| persona | The specialisation of one challenger: the agent file `challenger-<persona>`, whose Lens section says the blind spots it hunts and its register. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/challenger-contract/SKILL.md` |
| check | The isolated reviewer of mechanical conformance with the conventions, never substance or quality, one concern each, run as `/check <check> [slug]`; it returns its report and the command files it. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/check-contract/SKILL.md` |
| finding | The result of a critic or of a check: an FND item with a severity, filed in `reviews/` and tracked in the ledger's Findings table in the states open, resolved, rejected, parked and obsolete. | `CLAUDE.md`, ID scheme; `templates/ledger.md`, Findings |
| challenge | The result of a challenger: a CHL item on the substance, with a severity of dealbreaker, major or minor and its epistemic status, filed in `challenges/` and tracked in the ledger's Challenges table in the states open, accepted, rejected, parked and obsolete. | `CLAUDE.md`, ID scheme; `.claude/skills/challenger-contract/SKILL.md`, Output; `templates/ledger.md`, Challenges |
| contract | The one skill that owns what every member of a reviewer kind shares, or what the two documentation agents share (conduct and isolation, the subject and its boundary, the way of working and the shape of the output), preloaded into each agent through the `skills` field of its front-matter. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/critic-contract/SKILL.md`; `.claude/skills/challenger-contract/SKILL.md`; `.claude/skills/check-contract/SKILL.md`; `.claude/skills/docs-contract/SKILL.md` |
| Lens section | The one section of a reviewer's agent file that is its own: a specialisation of its contract that may narrow what is read or make a shared rule stricter, never rename, drop or duplicate one. | `CLAUDE.md`, Isolated reviewers |
| subagent | An agent Claude launches to do one job apart from the working conversation (a reviewer, the renderer, the documentation's planner and writer); it carries what the session read, `CLAUDE.md` and the instance file among it, and never the conversation. | `CLAUDE.md`, Isolated reviewers; `projects/forge/10-intent.md`, Operating environment |
| isolation | The condition of a subagent: it sees nothing of the conversation that started it, reads every input from disk in its run, and lets no instance fact reach what it writes. | `CLAUDE.md`, Isolated reviewers; `.claude/skills/docs-contract/SKILL.md`, Conduct and isolation |

## Places

| Term | In one sentence | Defined in |
|---|---|---|
| project | A directory `projects/<slug>/` that is a git repository of its own, of the kind its ledger header says: thought or library. | `CLAUDE.md`, Repository layout; `templates/ledger.md`, header |
| thought project | A project of kind `thought`: it carries the chain from the brief to the intent and the layers below it, with its records, ledger, resources, recipes, renders and documentation. | `CLAUDE.md`, Repository layout |
| library | A project of kind `library`, `projects/lib-<name>/`: material shared across projects, with no chain, only a ledger, sources, research and a README that catalogues what it holds. | `CLAUDE.md`, Repository layout and Document chain, Renders |
| dependency | A document of another repository, typically of a library, that a project relies on, registered by path and without a version in the ledger's Dependencies table. | `templates/ledger.md`, Dependencies; `CLAUDE.md`, Ledger |
| engine | Forge of Thought itself: the one git repository that holds `CLAUDE.md`, the skills, the agents, the scripts and the templates, which specifies and implements nothing and runs itself as the project `projects/forge`. | `CLAUDE.md`, What this workspace is, Persistence (git) and The system's own project |
| instance | One installation of the engine on a machine, with its own `CLAUDE.local.md`. | `.claude/skills/docs-contract/SKILL.md`, The voice; `CLAUDE.md`, What this workspace is |
| instance fact | A fact of one installation and not of the system, such as who the principal is by role or the conversation language: it lives in `CLAUDE.local.md`, out of the repository, and never reaches a reviewer's report, a render or a page. | `CLAUDE.md`, What this workspace is; `projects/forge/10-intent.md`, Operating environment |
| session model | The one model the whole forge runs on in a session, inherited by every agent (`model: inherit`) and set in `.claude/settings.local.json`; speed is bought with context, never with a weaker reviewer. | `CLAUDE.md`, Isolated reviewers and Repository layout |

## Commands and persistence

| Term | In one sentence | Defined in |
|---|---|---|
| save | `/save`: the door that runs its check and then commits and pushes one repository, or every one with changes, on whatever branch is checked out, with no render. | `CLAUDE.md`, Persistence (git) |
| release | `/release`: from `main` only, it runs its checks, re-renders the README and the release notes and saves with the release message and the tag. | `CLAUDE.md`, Persistence (git) |
| pull | `/pull`: the door inward, which looks at the remote, says the state of each repository as a fact (up to date, behind, ahead, diverged, no origin, not under git), pulls only a clean repository that is behind and offers the rest. | `CLAUDE.md`, Persistence (git); `.claude/skills/pull/SKILL.md` |
| guarded command | A command that writes, scaffolds, commits or regenerates, which the harness keeps Claude from starting on its own judgement (`disable-model-invocation: true` in its skill's front-matter): the principal invokes it by slash or asks in words. | `projects/forge/10-intent.md`, Operating environment; `.claude/skills/document/SKILL.md`, front-matter |
| major | An integer version, that is an approved one; a major of the forge intent closes a set of features the principal names and passes every check, both critic lenses and one challenge before its tag. | `CLAUDE.md`, Versioning & status; `projects/forge/10-intent.md`, Versioning and state |
| tag | A git tag on a release: `v<major>` is given by `/release`, and any other tag is the principal's request with a free name. | `CLAUDE.md`, Persistence (git) |
| branch | A git branch, voluntary and left to git: `main` is the released line, `scripts/forge-branch.py` switches or creates one, and merging is done by hand or by merge request. | `CLAUDE.md`, Persistence (git) |

## The documentation

| Term | In one sentence | Defined in |
|---|---|---|
| documentation | The pages of one topic each in `docs/`, with their index, generated by `/document` from the documentation map for the user, the extender and the evaluator, in five sections by the reader's journey (`start/`, `use/`, `about/`, `extend/`, `reference/`). | `CLAUDE.md`, Document chain, Documentation; `.claude/skills/document/SKILL.md`; `projects/forge/10-intent.md`, Growth path |
| documentation map | `docs-map.md` beside the owning project's ledger, of kind `map`: one entry per page with everything a page is made from, written by the planner, read by the scripts and the writers and never shown to the reader. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-planner.md`, The map |
| page | One page of the documentation, or its index, of one topic and one kind (how-to, explanation or reference), generated, never a source of truth and overwritten by the documentation run. | `CLAUDE.md`, Document kinds; `.claude/agents/docs-writer.md`, What the page is |
| index | The documentation's `docs/README.md`, a page derived by `scripts/docs-index.py` from the map's one line per page and the readers' paths; the catalogue of a resource directory is the resource index. | `.claude/agents/docs-planner.md`, The outline; `.claude/skills/document/SKILL.md`, step 5 |
| mirrored | Of a page: it restates what its inputs say, in the reader's words. | `.claude/agents/docs-writer.md`, What the page is |
| derived | Of a page: it puts together what no single file says, from the evidence its entry names, by the reasoning the entry gives. | `.claude/agents/docs-planner.md`, The map; `.claude/agents/docs-writer.md`, What the page is |
| pinned fact | A fact of the project that no file owns yet, such as a prerequisite, how a tool is installed or the public home of the repository, kept one bullet each in the readme recipe's section `Pinned facts (not rendered)`, read by the documentation's planner as an owner and not printed in the README. | `templates/recipe-readme.md`, Pinned facts (not rendered) |
| Unowned | The section of the documentation map that lists every fact a page needs and no file supports, with the page that needs it; the writer leaves it out, and the owner of the documentation decides where it gets a home. | `.claude/agents/docs-planner.md`, The map |

## See also

- [What the forge is and is not](../about/what-it-is-and-is-not.md): the forge in prose.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
