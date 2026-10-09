---
generated: 2026-10-09
made: mirrored
inputs-hash: c702248d75754540
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - CLAUDE.md
---

# Checks

This page lists the five checks of the forge, one entry each: what the check is for, when it fits, what it reads, what it verifies and what it costs. It is for the user choosing a check and for the extender who wants to see what each one owns. Every check verifies conformance with the conventions. None is a critic of the documents or a challenger of the thinking.

Each check owns one concern and none another's. A check is run with `/check <check> [slug]`: it takes a project by its slug, or the engine. A run that finds nothing files nothing.

## Which checks a save and a release run

Which checks each runs is the definition of the command, in `.claude/skills/save/SKILL.md` and `.claude/skills/release/SKILL.md`. Checks never call each other: the composition is the caller's. Of the five, `light` is the one that fits a save, and `history` is never composed into a save or a release.

## light

**Description.** Verifies a project's bookkeeping: front-matter against the history companion, ledger tables against the files, dependencies and resource indexes against the directories. Fit for a save.

**Reads.** One project, the path the task names; for the engine that is `projects/forge`.

**Verifies.**

| Concern | What is checked |
|---|---|
| Front-matter and history | Every rule of Versioning & status in `CLAUDE.md`, for every versioned document and its companion: the placement of the history and the form of its log as `templates/history.md` gives it (fields in order, the kinds, one line per record, `Was` last). Whether a text belongs in the document or in its history is the `history` check's. |
| Ledger accuracy | The ledger is shaped as `templates/ledger.md` says for its kind. The documents table agrees with front-matter and files on disk. Findings and challenges agree with the files in `reviews/` and `challenges/`. Every file in `sources/` and `research/` is registered, with registration only and no content columns. The Renders table mirrors every render's front-matter provenance. The Published table and `published/` agree. "Waiting on principal" matches what is actually open. |
| Dependencies | Every path in the Dependencies table exists on disk (a missing library is an advisory finding). Every index entry, recipe or chain citation pointing outside the project has a row. No row points inside the project. |
| Resource indexes | `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories: no file or bundle without an entry, no entry without a file, no bundle entry whose inner `00-INDEX.md` is missing. What the entries say is not judged. |

Not findings: a binary without an extract and an extract without its original, a binary listed in `sources/.gitignore`, and whether a Published row is `current` or `stale`.

**Cost.** The ledger, the front-matter of every document, the newest records of the companions and the directory listings: seconds, not minutes.

## project

**Description.** Verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

**Reads.** One project, the path the task names, or, when the task names none, every project under `projects/` except `forge`, each reported on its own. The bookkeeping of a project is the `light` check's; run beside it at a release, this check verifies everything else.

**Verifies.**

| Concern | What is checked |
|---|---|
| Kind and repository | The ledger header declares `kind: thought` or `kind: library` (missing is read as `thought`, a finding with a one-line fix). `projects/<slug>/.git` exists; a project that is not a repository is reported as a fact with the way in, never as a finding. A library needs no chain, and its documents may be overwritten by their owner. `logo.png` is optional and its absence is never a finding. |
| Structure | The files and folders of Repository layout in `CLAUDE.md` exist; a layer the project does not have is never missing. `recipes/` and `renders/` are paired: every render traces to a recipe and carries provenance front-matter. Every file in `published/` traces to a recipe with a `## Format` section; a `.pptx` or `.docx` in `renders/` traces to a render beside it. The README and release-notes recipes exist. Every `00-brief*.md` has a row in the ledger's Briefs table and the reverse. Under Waiting on principal, a line that copies a thread, a decision or a history record instead of citing it by ID is a finding. |
| ID hygiene | Every rule of the ID scheme in `CLAUDE.md`, in every document that carries IDs. |
| Language | Prime directive 6 in `CLAUDE.md`, for every artefact and record; the briefs and renders are exempt. |
| Immutables | The immutable documents of Versioning & status are never edited after creation; signs of after-the-fact editing that the ledger or the history companions reveal are flagged. The `00-INDEX.md` catalogues are exempt. |
| Recipes and renders | Shape and freshness, never content. Recipes conform to `templates/recipe.md` in front-matter and sections. Every declared input exists on disk. The `output:` path, where declared, points inside the repository. The staleness of a render is never a finding. |

**Cost.** The project's files read once, with the conventions read from their owners.

## engine

**Description.** Verifies the core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

**Reads.** The engine root the task names: `CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`, and the forge intent `projects/forge/10-intent.md` with `projects/forge/threads.md` and `projects/forge/decisions.md`. The forge project's own conformance is the `project` and `light` checks'. Whether a rule is stated in more than one place is the `single-source-of-truth` check's.

**Verifies.**

| Concern | What is checked |
|---|---|
| Core internal consistency | The commands table in `CLAUDE.md` agrees with the skills in `.claude/skills/*/SKILL.md` (the reviewers' contracts excepted). Described agents agree with `.claude/agents/`. Every skill an agent names in its front-matter exists. Every file in `scripts/` is described in `CLAUDE.md` and nothing described there is missing on disk. The README agrees with `CLAUDE.md` on chain, conventions and command set (never on currency: the README and release notes are renders). `templates/` agree with the conventions in Versioning & status and the ID scheme. |
| Core and forge intent | Every position is honoured by the core documents. Nothing withdrawn or rejected is still advertised in the core. Decisions referenced from the intent exist in `decisions.md`, and every decision record is reflected in the intent where it applies. |
| Rename and removal sweep | The old names recorded in decision records, and terms the principal has explicitly dropped, are searched for. Only historical records (history companions, decisions, rejected directions, reviews, challenges, research) may still contain them. |

**Cost.** The core files once and the intent's positions once: minutes at most, so that a release can afford it every time.

## history

**Description.** Reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

**Reads.** One project, the path the task names (for the engine `projects/forge`), and in it every versioned document with its history and its archive, or the one document the task names.

**Verifies.** The division between a document and its history, by Versioning & status in `CLAUDE.md` and the intent's definition (`.claude/skills/forge/states/intent.md`, Threads and files).

- In the document, the way to an item (as Versioning & status lists it) is a finding. So is detail an item carries where the file that performs it exists.
- The other way, an item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

The form of the log is the `light` check's.

**Cost.** Whole documents with their histories: minutes rather than seconds.

## single-source-of-truth

**Description.** Verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across `CLAUDE.md`, skills, agents, templates and scripts, and no direct operation where a mechanism exists. The honest sweep, expensive by design: fit before a major release or after a round on the operating layer, not at every release.

**Reads.** The whole operating layer of the engine, never a changed subset: `CLAUDE.md`, every skill under `.claude/skills/` (supporting files included), every agent under `.claude/agents/`, every template under `templates/`, the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own `CLAUDE.md`, if any, against the owners in the engine.

**Verifies.**

| Concern | What is checked |
|---|---|
| One owner per rule | Every command, agent, contract and template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path, never restated; a restatement, in whatever wording, is a finding, fixed by a reference to the owner and deletion of the copy. Where a shape has no owner, the finding proposes one. |
| Reviewer files carry only their own | Every `critic-*.md`, `challenger-*.md` and `check-*.md` names its kind's contract skill and carries only its front-matter and its Lens section. |
| No direct operation where a mechanism exists | No skill or agent performs directly what a script, command or agent exists for: git outside the scripts in `scripts/`, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents. |

**Cost.** The whole layer, read and compared pairwise where the subjects overlap. Long by design; the report's first line says how many files were read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
