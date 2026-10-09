---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - CLAUDE.md
---

# Checks

The forge has five checks, each owning one concern of conformance with
the conventions. This page lists them for a user choosing one and for
an extender who wants to see what each already covers. A check is
never a critic of the documents and never a challenger of the
thinking.

A `/save` runs its check and then commits and pushes. A `/release`
runs its checks, re-renders the README and release notes, and then
saves. Which checks each runs is stated in the definitions of those
two commands (`.claude/skills/save/SKILL.md`,
`.claude/skills/release/SKILL.md`).

## light

**Description.** Verifies a project's bookkeeping: front-matter
against the history companion, ledger tables against the files,
dependencies and resource indexes against the directories. Fit for a
save.

**Reads.** One project; for the engine that is `projects/forge`.

**Verifies.**

| What | Owner of the rule |
|---|---|
| Front-matter and history of every versioned document and its companion: placement of the history, form of the log (fields in order, kinds, one line per record, `Was` last) | CLAUDE.md, Versioning & status; `templates/history.md` |
| Ledger shaped as its kind says; documents table against front-matter and files; findings and challenges against `reviews/` and `challenges/`; every file in `sources/` and `research/` registered; Renders table against each render's provenance; Published table against `published/`; "Waiting on principal" against what is open | `templates/ledger.md` |
| Dependencies: every path in the table exists; every citation pointing outside the project has a row; no row points inside the project | the dependencies rule of the forge |
| Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` agree with their directories (file without entry, entry without file, bundle without inner index) | CLAUDE.md, Document chain |

Not findings: a binary without an extract, an extract without its
original, a binary listed in `sources/.gitignore`, whether a
published row is `current` or `stale`. Whether a text belongs in the
document or in its history is the `history` check's.

**Cost.** The ledger, the front-matter of every document, the newest
records of the companions and the directory listings: seconds. Most
findings are bookkeeping, marked as an immediate fix.

## project

**Description.** Verifies a project's structure, IDs, language,
immutables, recipes and renders against the conventions.

**Reads.** One project, or, when none is named, every project under
`projects/` except `forge`, each reported on its own. The
bookkeeping the `light` check owns is not repeated here; the two run
side by side at a release.

**Verifies.**

| What | Owner of the rule |
|---|---|
| Kind and repository: ledger header declares `kind: thought \| library`; `projects/<slug>/.git` exists (a project that is not a repository is a fact, reported with the one-line way in, not a finding) | CLAUDE.md, Repository layout and Persistence |
| Structure: the files and folders of the layout exist; each render traces to a recipe and carries provenance; each file in `published/` traces to a recipe with a `## Format` section; the README and release-notes recipes exist; each `00-brief*.md` has a row in the Briefs table and the reverse; a brief marked `mined` is cited in the intent | CLAUDE.md, Repository layout, Document chain, Ledger; `templates/recipe.md` |
| ID hygiene in every document that carries IDs | CLAUDE.md, ID scheme |
| Language of every artefact and record (briefs and renders exempt) | CLAUDE.md, prime directive 6 |
| Immutables: reviews, challenges, sources and research not edited after creation (the `00-INDEX.md` catalogues exempt) | CLAUDE.md, Versioning & status |
| Recipes and renders, shape only: recipes conform to `templates/recipe.md`; declared inputs exist; `output:` points inside the repository | `templates/recipe.md` |

Not findings: a layer below the intent the project does not have, a
missing `logo.png`, the staleness of a render (README and release
notes included), whether a recipe still matches the principal's
thinking. A library needs no chain; its structure reduces to the
library's file set.

**Cost.** The project's files read once, the conventions read from
their owners.

## engine

**Description.** Verifies the core (CLAUDE.md, templates, skills,
agents, scripts) against itself and against the forge intent: every
position honoured, nothing withdrawn still advertised, every decision
reflected.

**Reads.** The engine root: CLAUDE.md, `templates/`,
`.claude/skills/`, `.claude/agents/`, `scripts/`, and
`projects/forge/10-intent.md` with `projects/forge/threads.md` and
`projects/forge/decisions.md`.

**Verifies.**

| What | Owner of the rule |
|---|---|
| Commands table of CLAUDE.md against the skills on disk; described agents against `.claude/agents/`; every skill an agent names exists | CLAUDE.md, Commands |
| Every file in `scripts/` described in CLAUDE.md, and nothing described there missing | CLAUDE.md, Repository layout and Persistence |
| README against CLAUDE.md: same chain, conventions and command set, no contradiction (never currency) | CLAUDE.md |
| `templates/` against the conventions: front-matter fields, history companion, prefixes, numbering, statuses | CLAUDE.md, Versioning & status and ID scheme |
| Every position of the forge intent honoured by the core; nothing withdrawn or rejected still advertised | the forge intent |
| Decisions referenced from the intent exist in `decisions.md`, and every decision is reflected in the intent where it applies | `decisions.md` |
| Rename and removal sweep: old names recorded in decisions and dropped terms appear only in historical records | `decisions.md` |

The forge project's own conformance is the `project` and `light`
checks'; whether a rule is stated in more than one place is the
`single-source-of-truth` check's.

**Cost.** The core files once and the intent's positions once:
minutes at most, so that a release can afford it every time.

## history

**Description.** Reads a document with its history and reports where
the division between them does not hold, proposing each move in full.
Fit when a document is cleaned, never at a save or a release.

**Reads.** One project (for the engine, `projects/forge`), and in it
every versioned document with its history and archive, or the one
document the task names.

**Verifies.**

| What | Owner of the rule |
|---|---|
| In the document: the way to an item (why it changed, what was said, trials, measurements) is a finding; so is detail an item carries where the file that performs it exists | CLAUDE.md, Versioning & status; `.claude/skills/forge/states/intent.md`, Threads and files |
| In the history: an item that can no longer be understood because what makes it hold stands only in the history is a finding | the same |

Each finding proposes the move in full: the text that leaves, word
for word, and the record it becomes. The form of the log is the
`light` check's.

**Cost.** Whole documents with their histories: minutes rather than
seconds. Never composed into `/save` or `/release`.

## single-source-of-truth

**Description.** Verifies that every rule, procedure and file shape
is written in one place and cited everywhere else: no restatement
across CLAUDE.md, skills, agents, templates and scripts, no direct
operation where a mechanism exists. The honest sweep, expensive by
design; fit before a major or after a round on the operating layer,
not at every release.

**Reads.** The whole operating layer: CLAUDE.md, every skill under
`.claude/skills/` (supporting files included), every agent under
`.claude/agents/`, every template under `templates/`, the help
headers of `scripts/`. Always the whole, never a changed subset.
Named a project instead, it reads that project's recipes, resource
indexes, ledger comments and its own CLAUDE.md, if any, against the
owners in the engine.

**Verifies.**

| What | Owner of the rule |
|---|---|
| One owner per rule: a procedure, rule set or file shape that another file owns is cited by path, never restated; where a shape has no owner, the finding proposes one | the forge's rule that one mechanism lives in one place |
| Reviewer files carry only their own: each `critic-*.md`, `challenger-*.md` and `check-*.md` names its kind's contract skill and holds only front-matter and its Lens section | the contract skill of the kind |
| No direct operation where a mechanism exists: git outside `scripts/`, a conversion outside `doc2md.ps1`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents | the script, command or agent concerned |

**Cost.** The whole layer, read and compared pairwise where the
subjects overlap. Long by design; the report's first line says how
many files were read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
