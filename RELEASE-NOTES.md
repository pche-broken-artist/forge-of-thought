---
project: forge
render: release-notes
generated: 2026-09-01
recipe: projects/forge/recipes/release-notes.md v0.2
inputs:
  - projects/forge/10-intent.md v3.6
  - projects/forge/decisions.md
  - RELEASE-NOTES.md (2026-08-30 edition — released sections)
---

# Forge of Thought — Release Notes

An Unreleased section covering the changes since the last approved
major, then one section per approved major version of the system,
newest first. The fine-grained change log lives in
`projects/forge/10-intent.md` (Version History).

## Unreleased — 3.x since 3.0

These changes are not yet approved; they cover intent versions 3.1 to
3.6 — the first four made on the day of the 3.0 approval while the
first fresh deployment of the public engine was being prepared, the
last two prompted by the first newcomer meeting it and by the day's
check findings.

**Every project gets a README and release notes.** The engine's own
mechanism is generalised: every project has a README and, if it is a
thought project, release notes — both renders of the project's own
recipes (`recipes/readme.md`, `recipes/release-notes.md`, with
`output:` in the project root), exactly as the engine has them. The
recipe is what is iterated, the render is never edited by hand, and
every save that touches the project regenerates both before the
check; the ledger's Renders table carries them like any render. A
library has a README only — a catalogue of what it holds — since
release notes are distilled from an intent's Version History and
decisions, which a library does not have. Every project README closes
with the fixed sentence that reading it needs nothing and maintaining
it needs Forge of Thought, linked — the engine's own README excepted,
being that sentence's destination (POS.1000).

**Genre skeletons scaffolded from the start.** `readme` and
`release-notes` are genres of `/recipe`, with skeletons
`templates/recipe-readme.md` and `templates/recipe-release-notes.md`;
`/new-project` scaffolds them and `/check` expects them.

**An optional project icon.** A project may carry `logo.png` in its
root, supplied by the principal and picked up as the repository
avatar by hosts that do so. A project without an icon is complete,
and `/check` never reports its absence (POS.1010).

**Cross-repository dependencies registered in the ledger.** A project
writes down what it relies on outside its own repository: the ledger
carries a Dependencies table — path, library, used by, note — with one
row per document of another repository the project cites, typically a
library document referred to by path or a deck template named in a
recipe. Registration only, like sources; no version is pinned, by
design, because a library document is maintained by its owner and
cited as a moving target. `/check` verifies that every registered
path exists on disk, the `/forge` map names which libraries the
project needs, and `/ingest` registers the row when the principal
directs a project to a library document instead of copying it. The
position was raised when a document moved from a project into a
library and the project's reliance on it and on its deck template
became invisible (POS.1020).

**The forge's behaviour lives in the engine, never in the assistant's
private memory.** The assistant keeps a per-directory memory outside
the repository; whatever it learns there about how the forge should
work — a working method, a rule of a command, a convention — is
written into `CLAUDE.md`, the commands or the templates and removed
from memory, so that every instance behaves the same and a new user
meets the same forge as the principal. The audit before the first
fresh deployment found most of that memory to be engine rules already
written or engine rules missing, and the missing ones moved in: the
working method Step by step (one consent-needing action at a time,
the exact operation and its reason stated, a seen plan is not
consent), the walkthrough's rule that an accept recommendation carries
the concrete text the artefact would receive, and one research per
question in `/research`. Instance facts that had lived in memory —
the git identities per host — moved to `CLAUDE.local.md`. Memory is
left with what is personal to one principal only (POS.1030).

**A source has one form.** A file in `sources/` is either text or a
functional binary, never both by default. At `/ingest` every binary
file — isolated or inside a bundle — gets one question: convert to
Markdown? Yes: `doc2md` writes `sources/<slug>.md`, and that extract
is the source — tracked, registered, indexed, immutable — while the
original is not copied into the project, or is gitignored where it
already lies in `sources/`. No: the binary is the source as a
functional thing — a deck template, a graphic, a logo — kept as is
with no extract. Text files get no question; keeping both is the
exception, on the principal's explicit word. The ledger's Sources
table records the form (`text | extract of <original> | binary`)
instead of an extract flag, and `/check` treats a binary without an
extract, or an extract without its original, as the normal case. The
reason: the repository carries what the forge works with — text — and
a binary nobody reads from git is weight without use. The convention
applies from now on: earlier extracts keep their `.extract.md` names,
and a binary already in git beside its extract leaves the index only
on the principal's word, never automatically. Raised by the day's
`/check`, where four PDFs sat in git beside the extracts that alone
are ever cited (POS.1040).

**First run is one command.** After cloning the engine, `/setup`
copies `templates/CLAUDE.local.md` to the root and fills it by
interview — principal, conversation language, git identities — and
creates `.claude/settings.local.json` with the session model set to
Fable without asking: the recommendation embodied as the default,
with one notice sentence naming the change path (`/model` or editing
the file). Existing files are reported, never overwritten. The
command is named `/setup`, not `/init`, over the collision with
Claude Code's built-in command. Prompted by a newcomer observed
struggling through the manual install steps (POS.1050).

**An existing project arrives through one command too.**
`/import-project <git-url>` brings an existing project in through the
scripts-only git door: `scripts/forge-clone.ps1` — the fourth git
script — clones into `projects/<repository name>`, with no slug
parameter because the directory falls out of the repository's name,
refuses to overwrite, and reports the last commit, the origin and
whether a ledger with `kind:` is present. The clone runs bare by
default and the script reports the commit identity git resolves for
the fresh clone — or, truthfully, that `forge-save` will report and
skip; passing an identity from `CLAUDE.local.md` (`-Name`/`-Email`)
remains as the fallback for a machine without the per-host include
(POS.1060).

**The chain drawn as a star, and an authorship boundary.** The
README's Quickstart was rebuilt as a common head — clone, install
Claude Code, `claude` from the root, `/setup` — plus two named paths,
starting a new project and bringing an existing one, with selecting
the project (`/forge <slug>`) visible as the first act of work. The
chain diagram was redrawn from a line into the star: solid what is
built today, dashed a fixed set of illustrative future layers —
business analysis, an RFP, an article with its translation render,
strategy, solution design, an implementation deck — visibly marked as
not existing yet. Raised on the way, the render concept gained its
authorship boundary: a chain artefact is composed by the principal, a
render is generated — an article the principal writes is a layer, its
translation a render (POS.0710 extended); the sentence was carried
into CLAUDE.md's chain section in the round that followed.

**The commit identity follows the host, not the project.** POS.0950
was rewritten to the per-host identity model in the walkthrough of the
day's four open check findings, every verdict the principal's: git
conditional includes (`includeIf "hasconfig:remote.*.url:…"`) in the
user's own configuration resolve the right identity for every
repository automatically, and a per-repository local identity stays
as an override. `forge-save`'s effective-identity check is correct in
this model and stays — the finding had proposed checking `--local`,
and the principal's "one identity per host, independent of the
project" won instead. CLAUDE.md's Persistence section carries the
per-host wording.

## 3.0 — 2026-08-30

Version 2 made the forge a workshop; version 3 sets it free. The
engine parted ways with the projects it serves and became a public
repository under an open licence, carrying no instance facts and no
content of anyone's projects, while each project lives in a
repository of its own. On the way the brief was redefined and born in
the forge for the first time, the whole forge settled on one model
with renders in isolation, the working methods got names, material
got an index and projects got a kind.

**The engine and the projects part ways.** The course set early in the
era — a public engine carrying no company-specific data, each user
responsible for their own project repositories — became a mechanism
and was then executed. The engine is a clone; the projects are nested
git repositories in a gitignored `projects/*`, with `projects/forge`
re-included. The engine does not know the projects: the scripts
recognise one by the presence of its `.git`, commit and push to its
own origin, and skip a directory without one; `git init` and the
remote are the user's one-off act; the engine is upgraded by
`forge-pull`, carries a git tag per approved major, and stamps no
engine version into projects. Submodules, subtree, a template
repository, copying the engine into projects and a plugin-only shape
were rejected on the research of the day — they model a dependency
this relation is not, or end in manifests, override layers and
migrations. A plugin remains a possible later distribution layer, its
cost (a `CLAUDE.md` split, commands rewritten to the repository root)
not worth paying yet (THR.0190). On 2026-08-30 the split was run to
its end along a runbook: the engine is public at a repository of its
own with a fresh one-commit history, the subject projects and the
library live in repositories of their own, and the former monorepo is
archived read-only with a notice naming the new homes and a
`pre-split` tag as its last complete state. The operating layer —
`CLAUDE.md`, `.gitignore`, the scripts, templates and commands — was
rebuilt to this intent the same day.

**No instance facts in the engine; identity per repository.** Who the
principal is and what language the conversation runs in move to a
gitignored `CLAUDE.local.md` at the engine root, the session model to
`.claude/settings.local.json`, the commit author to the user's git
configuration; the core names these things only as things that exist,
never by value, and the scripts carry no URL or identity. The commit
identity is set per repository, locally, as part of the one-off act
that creates it — never inherited from the global configuration by
default, since one machine serves hosts with different identities; a
repository whose identity is missing is reported by `forge-save` with
the command to set it, and nothing is committed until it is. `local/`
is dropped: it existed only to keep company material out of the
repository, which the gitignored `projects/*` now does, and deck
templates are named by path instead. The output language was
recognised on the way as an instance rule: English for every artefact
is the principal's own rule for the projects of this instance, a
project with Czech output is conceivable and the first such project
has been noted, and more than one output language is to be solved when
a project needs it (THR.0180).

**Publication and the public face.** The engine is the principal's to
publish, built outside any work assignment and on the company's git
only because it carried work information not yet separated. The
audience, in order: rollout in the company, at the same time a public
project around which a community may form, and a showcase of the
principal's work; the split also lets access be granted per project.
The boundary for the public forge project is nothing company-specific
by name, and before publication the project was gone through and
rewritten within it, immutable artefacts included — the locked brief
and both CTO challenges had a name, a host, an address, a template
file name and two sentences quoting a subject project's substance
removed, immutability knowingly broken once and recorded in the
ledger only. The slugs of the subject projects stay: that projects of
those names exist and travelled the chain is a process fact, not
content. A forbidden-term list was considered and dropped — a grep
catches names, not content. The public engine starts with a fresh git
history rather than one filtered by path (DEC.0080): the company lives
in the text — commit messages, every version of the forge intent, a
challenge, the research notes — so a filtered history would need text
filtering as well, work comparable to a fresh start with a residual
risk of a leak made public for good; "history lives in git" is not
voided but starts on the day of publication. The one true point of
the challenge, that the only complete record lives on the employer's
server, is accepted as it is, the company copy kept read-only while it
exists. The public face itself is settled (POS.0990): the repository
is named `forge-of-thought` — the bare word "forge" is overloaded on
every code host — under the licence CC BY 4.0, anyone free to use and
adapt the engine with credit to the author and a link to the
repository; the README names the author with a contact address as a
fixed text of its recipe, which is not an instance fact but who the
work is by, whoever runs an instance; the `LICENSE` file carries the
verbatim legal code.

**A guard rail for the boundary.** The rewrite before publication
found the leak surface where the challenge predicted it: the forge
project's own artefacts quoting the substance of subject projects — a
sentence of a subject intent in a CTO challenge, a deck's name in a
position. Wanted is a standing rule that `projects/forge` never
carries the content of a subject project, only process facts — that a
project exists, its versions, dates and counts — and a home for it in
`CLAUDE.md`, the reviewer prompts, `/check-forge` as a sweep, or all
three. Opened at approval for the next iteration (THR.0210).

**Projects have a kind.** A project is a `thought` — a chain from brief
to assignment — or a `library`: only `sources/` with its index, a
ledger and `research/`, prefix `lib-`, its own repository and therefore
its own visibility, a collection of documents used across projects
whose owner is also their author and may overwrite or version beside.
Nothing is redefined for it — `/ingest`, registration and the index
work as everywhere — and a citation of a library from another project
is a knowingly unguarded cross-repository dependency. A bare `/ingest`
sweep now reports changed sources with a question universally: a
breach in a thought project, the normal case in a library.

**Briefs redefined, and the first brief born in the forge.** A brief
is an intent that is composed and then locked: draft while written,
approved at the lock, immutable from the lock rather than from the
file's creation. Three origins are equally legitimate — it arrives
finished, is begun outside and finished with the forge, or is born in
the forge from the first word — with `/forge brief` as the door: the
principal moderates and says what is explored, Claude clarifies where
he is terse without adding content of its own and keeps asking
whether what exists already solves it, reaching for `/research` and
`/ingest` at his timing. Free-form means no *required* structure, not
no structure — headings, tables and use cases are legitimate, a brief
holds thoughts to be processed rather than decisions, changeable until
mined, and a summary ordered into a brief is stored as shown, never
re-narrated as prose. A project may carry more than one brief
(`00-brief-<name>.md`), each the birthplace of one whole of thinking
that would otherwise enter the intent as a batch of unproven
positions; the ledger's Briefs table tracks how far each has been
mined, and a whole that dies leaves its brief locked and one rejected
direction. Branch documents proper were considered and deferred as
heavy (THR.0170); the long-open thread on additional briefs closed.
`00-brief-public-engine.md` was the first brief composed inside the
forge, with three research notes on engine distribution beside it,
and the first brief challenged: seven CTO challenges before the lock,
six accepted into it, the seventh rejected in its remedy and accepted
in its risk (DEC.0080). Locked at 1.0 and mined at the principal's
direction, every verdict his — the whole cycle brief → challenge →
lock → mine run end to end for the first time.

**One model for the whole forge, and renders in isolation.** Every
command, state and reviewer runs on the session model, both agents
saying so explicitly (`model: inherit`); the `opus` pin on the CTO
challenger, set when opus was the strongest model, had silently come
to mean a weaker reviewer than the author, and reviewers may no longer
pin a model. Per-command pinning to a faster model was rejected:
routine commands are a small share of the work, their slowness comes
from carrying the whole conversation as context, and the pins would
add a convention to keep. The lever adopted instead is context:
`/render` generates in an isolated subagent that sees only the recipe
and its inputs — faster and cheaper on any model, the gain landing in
`/save`'s re-renders. A per-recipe model choice was tested and
deferred: a smaller model loosened pinned wording, dropped prescribed
elements and leaned on the previous render instead of the recipe —
the drift the delta-reporting position exists to prevent.

**Working methods named.** The ways a working conversation runs now
have names, so that commands and the README can refer to them and the
principal can invoke one in a word: Walkthrough, Propose never decide,
Elicitation interview, Draft early, Reflect back, Intent-first,
Recommend do not push. The Walkthrough is the one new position — any
list needing the principal's decision is worked one item at a time,
Claude's recommendation and reason first, "leave it open" a
legitimate verdict, everything written once at the round's end;
whatever produces a list ends by offering one. `/resolve` was retired
without alias, a per-verdict door never used.

**Material has an index.** Every `sources/` and `research/` directory
carries a freely rewritten `00-INDEX.md` — what a material is, where
it came from, its role, when to consult it — so that material need
not be re-read to be known about. The index tracks nothing and is no
automatic input of any command: a contradiction between the intent
and a material is not a finding. Bundles keep their own index and
appear as one entry above — two levels, never deeper. The ledger was
reduced to registration, and `/ingest`, `/research`, `/check` and
`/new-project` write, verify and scaffold the indexes.

**Decks become real PowerPoints; recipes composed by genre.**
`scripts/md2pptx.ps1` turns a Markdown deck render into a `.pptx`
through headless Claude Code with the official pptx skill — an LLM
conversion by design, deck definitions being free-form and carrying
instructions for the model; the generated file lands beside its
source render, tracked like any render output. `/recipe <genre>`
mirrors the `/forge` star: a guided interview composes a render
recipe from the genre's elicitation checklist and skeleton, the first
genre `presentation`. A render may cite another render as an input,
with provenance and staleness tracked.

**The README rebuilt as an onboarding pitch.** A bootstrap Quickstart,
a masthead leading with the forge's identity as an AI cognitive
extension of the principal, a challenge-headed opening section over
the failure modes the forge removes, a "What you get" list, sections
regrouped story → concepts → reference, a Working methods section so
that newcomers learn how the work feels, and at the end an
author-and-licence section. The forge dictates only the output
language; the conversation language is per-instance configuration
that never appears in outward-facing renders. Until a public exemplar
project exists the README carries a one-sentence placeholder.

**The forge runs beyond Windows.** `scripts/` is the only
platform-bound layer, kept in cross-platform PowerShell 7 with
nothing Windows-only, usage examples included, verified by a run on
Linux; the instance facts once hard-coded in the scripts left them
under the positions above. Replacing the set with POSIX `sh` under
Git Bash is still being weighed (THR.0150); a dual set and a Python
rewrite are excluded.

**Housekeeping of the door and the boundary.** A third script,
`forge-status.ps1`, reads repository state without changing anything,
so the scripts are the only door to git, reading included. The
enumerated ban on delivery-stage apparatus fell: what keeps an
assignment an assignment is the kind of content — it assigns, it does
not solve. These release notes gained an Unreleased head, regenerated
by every save that touches the core and recast as the new major's
section at approval — as here.

**The forge turned its reviewers on itself.** Two critique rounds of
the forge project, seven of eight findings fixed and one left open by
decision; the first CTO challenge of the forge intent returned six,
four accepted and two rejected with recorded reasons (DEC.0060,
DEC.0070). The round produced the scope positions: the forge is a
general tool for forging thoughts and ends where its owner is
satisfied, delivery deliberately outside its sight; reviewer isolation
is not independence, with independent challengers on a different
model family planned; regenerated renders pass under the principal's
eyes; and artefacts do not expire with the conventions they were
written to.

**Open by design:** THR.0090 (genuine multi-principal operation beyond
one instance per person via git), THR.0140 (whether the forge's output
one day feeds a delivery chain as grown layers or hands over to a
separate framework), THR.0150 (replacing the PowerShell scripts whole
with POSIX `sh`), THR.0170 (branch documents as a per-whole working
space before the merge), THR.0180 (more than one output language,
opened by the first project with Czech output), THR.0190 (a plugin as
a later distribution layer, taken up when `forge-pull` proves an
insufficient upgrade channel), THR.0200 (an exemplar project for the
README), THR.0210 (a standing guard rail so that `projects/forge`
never carries the content of a subject project).

## 2.0 — 2026-08-15

Version 1 was an engine that turned briefs into assignments. Version 2
is a workshop: the chain is worked by naming the state you want, what
the chain produces is communicated by generated renders rather than
hand-kept documents, and the adversarial pressure on the thinking has
grown teeth. The guiding aesthetic also shifted: an assignment is no
longer prized for being short, but for being complete and precise.

**The chain is worked by target state.** `/clarify` and `/draft` were
retired in favour of `/forge`: bare, it maps the project's state;
with a target (`/forge intent`, `/forge assignment`) it iterates that
artefact. Each state declares its own inputs in its own definition
file, so the chain can grow new layers — or branch — without new
conventions.

**Renders became a first-class concept.** Audience-specific outputs —
a pitch, an architecture picture, the repository README — are
generated from versioned recipes (`recipes/<recipe>.md`: inputs,
audience, instructions, template) by `/render <recipe>`, carry
provenance front-matter, and are never edited by hand: a recipe fixes
structure, never wording, and each rendering re-derives the words from
the current inputs. The README is itself a render and is regenerated
automatically by every `/save` that touches the core, so it can no
longer go stale. This file is a render too.

**The challenger grew into a panel.** `/challenge <persona>` selects a
lens — one isolated agent per persona, `cto` first — and may target
any chain artefact, best before the next layer is first derived from
it. Calibration was hardened from the principal's own pre-forge
challenger prompt: severity grading (dealbreaker | major | minor), a
wider epistemic scale, and an anti-fabrication discipline under which
a precise "I don't know" beats an invented figure.

**Sources serve, tooling converts.** `/ingest` was reduced to pure
registration — store, catalogue, nothing more; how and when a source
is used is the principal's call alone. Related files live as bundles
with a `00-INDEX.md` catalogue, and every text extract of a binary
source is produced by `scripts/doc2md.ps1` (markitdown) — ad-hoc
parsing is banned.

**Saving became a procedure.** The forge lives in a GitLab-backed
repository driven by `forge-save` / `forge-pull`; `/save` is the
recommended door: re-render the README, run the scope-routed
conformance check, settle findings with the principal, confirm the
commit message, then push. Advisory throughout — nothing blocks the
principal. Protection settled on Claude Code's permission system
after OS-level sandboxing proved unavailable on Windows.

**From short to complete.** The founding "short and airy" paradigm
was dropped in two steps: first the fixed page target (length is
never the defect), then the paradigm itself — an assignment now
carries the complete in-scope substance of the intent, as precisely
as it can be written; a silent omission is a defect, and leaving a
matter out is legitimate only as an explicit delegation. What keeps
an assignment an assignment is the kind of content, never the amount.

**Open by design:** THR.0090 (multi-principal use), THR.0110
(additional briefs during a project's life), THR.0120 (final form of
the delivery-stage exclusion under the completeness paradigm).

## 1.0 — 2026-08-02

The founding baseline. A fixed chain of versioned documents — verbatim
brief, working intent, distilled assignment — with decisions and a
ledger beside it; two independent reviewers blind to the working
conversation (document critic and substance challenger); stable global
IDs aligned with the group BRD standard; conversation in Czech,
artefacts in English; write once per iteration round; conformance
commands (`/check`, `/check-forge`) advisory and read-only. Version 1
deliberately ended at the assignment, with the growth path toward BRD
and solution architecture declared but not built.
