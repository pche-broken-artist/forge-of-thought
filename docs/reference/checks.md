---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 738dfed98a5453be
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

A check is a reviewer that verifies one concern of a project or of the engine against the conventions of the forge. This page lists the checks of today for the user and the extender: what each verifies, what it reads, what it costs, and which of them a save and a release run. Every check verifies conformance only; none judges the quality of the documents or the substance of the thinking. A finding is a check's result.

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter against the history companion, ledger tables against the files, dependencies and resource indexes against the directories | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders | A release, beside `light` | `.claude/agents/check-project.md` |
| `engine` | The core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent | A release of the engine | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned; never at a save or a release | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place and cited elsewhere | Before a major, or after a round on the operating layer; not at every release | `.claude/agents/check-single-source-of-truth.md` |

## What a save and a release run

- A save runs `light` on every repository in scope.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and `light` and `project` on `projects/forge`, the forge's own project.
- `history` and `single-source-of-truth` are run by hand only.

To run a check, see [Check conformance](../use/check-conformance.md). To add one, see [Add a check](../extend/add-a-check.md).

## light

**Description.** Verifies a project's bookkeeping: front-matter against the history companion, ledger tables against the files, dependencies and resource indexes against the directories. Fit for a save.

**Reads.** One project, the path the task names; for the engine that is `projects/forge`.

**Verifies.**

- Front-matter and history. Every rule of "Versioning & status" in `CLAUDE.md`, for every versioned document and its companion: where the history stands, and the form of its log as `templates/history.md` gives it. Whether a text belongs in the document or in its history belongs to `history`.
- Ledger accuracy. The ledger is shaped as `templates/ledger.md` says for its kind. Its documents table agrees with the front-matter and the files on disk. Its findings and challenges agree with the files in `reviews/` and `challenges/`. Every file in `sources/` and `research/` is registered, with registration only and no content columns. The Renders table mirrors the provenance of every render. The Published table and `published/` agree. "Waiting on principal" (the principal is the person whose thinking is forged) matches what is actually open.
- Not a finding. A binary without an extract, an extract without its original, a binary listed in `sources/.gitignore`, and whether a published row is `current` or `stale`.
- Dependencies. Every path in the Dependencies table exists on disk; a missing library is an advisory finding. Every citation that points outside the project has a row, and no row points inside the project.
- Resource indexes. `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories: no file without an entry, no entry without a file, no bundle entry without its inner index. What the entries say is not judged.

**Cost.** The ledger, the front-matter of every document, the newest records of the companions and the directory listings: seconds.

## project

**Description.** Verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

**Reads.** One project, the path the task names, or, when the task names none, every project under `projects/` except `forge`, each reported on its own. The bookkeeping that `light` verifies is left to `light`.

**Verifies.**

- Kind and repository. The ledger header declares `kind: thought | library`, as `templates/ledger.md` shows. `projects/<slug>/.git` exists; a project that is not a repository is reported as a fact, not as a finding. A library needs no chain.
- Structure. The files and folders of "Repository layout" in `CLAUDE.md` exist. A layer below the intent that the project does not have is not missing. `recipes/` and `renders/` are paired, and every render carries provenance front-matter. Every file in `published/` traces to a recipe with a `## Format` section. The README and release-notes recipes exist. Every brief has a row in the ledger's Briefs table and the reverse. Under "Waiting on principal", a line that copies instead of citing is a finding.
- ID hygiene. Every rule of the ID scheme in `CLAUDE.md`, in every document that carries IDs.
- Language. Prime directive 6 of `CLAUDE.md`, for every artefact and record; briefs and renders are exempt.
- Immutables. The immutable documents named in "Versioning & status" of `CLAUDE.md` are not edited after creation. The `00-INDEX.md` catalogues are exempt.
- Recipes and renders, in shape only. Recipes conform to `templates/recipe.md`, every declared input exists, and a declared `output:` path points inside the repository. The staleness of a render is never a finding.

**Cost.** The project's files, read once; the conventions are read from their owners.

## engine

**Description.** Verifies the core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

**Reads.** The engine root the task names: `CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`. Also the forge intent, its threads and its decisions, in `projects/forge`. The forge project's own conformance belongs to `project` and `light`. Whether a rule is stated in more than one place belongs to `single-source-of-truth`.

**Verifies.**

- Core internal consistency. The commands table of `CLAUDE.md` agrees with the skills on disk, and the agents it describes with `.claude/agents/`. Every skill an agent names in its front-matter exists. Every file in `scripts/` is described in `CLAUDE.md` and nothing described there is missing. The README agrees with `CLAUDE.md` on chain, conventions and command set; its currency is not checked. The templates agree with the conventions in "Versioning & status" and "ID scheme".
- Core and forge intent. Every position is honoured by the core documents. Nothing withdrawn or rejected is still advertised in the core. Every decision the intent cites exists in the decisions record, and every decision is reflected in the intent where it applies.
- Rename and removal sweep. Old names recorded in decisions, and terms explicitly dropped, are searched for; only historical records may still contain them.

**Cost.** The core files once and the intent's positions once: minutes at most.

## history

**Description.** Reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

**Reads.** One project, the path the task names (for the engine `projects/forge`), and in it every versioned document with its history and its archive, or the one document the task names.

**Verifies.** The division between a document and its history, by "Versioning & status" in `CLAUDE.md` and "Threads and files" in `.claude/skills/forge/states/intent.md`.

- In the document, the way to an item is a finding, and so is detail an item carries where the file that performs it exists.
- An item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.
- The form of the log belongs to `light`.

**Cost.** Whole documents with their histories: minutes rather than seconds.

## single-source-of-truth

**Description.** Verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across `CLAUDE.md`, skills, agents, templates and scripts, and no direct operation where a mechanism exists. The honest sweep, expensive by design: fit before a major or after a round on the operating layer, not at every release.

**Reads.** The whole operating layer of the engine, never a changed subset: `CLAUDE.md`, every skill under `.claude/skills/` with its supporting files, every agent under `.claude/agents/`, every template under `templates/`, and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and own `CLAUDE.md`, if any, against the owners in the engine.

**Verifies.**

- One owner per rule. Every command, agent, contract and template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path, never restated; a restatement is a finding. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own. Every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists. No skill or agent performs directly what a script, command or agent exists for: git outside the scripts, a conversion outside `scripts/doc2md.py`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents.

**Cost.** The whole layer, read and compared pairwise where the subjects overlap: long by design. The report's first line says how many files were read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
