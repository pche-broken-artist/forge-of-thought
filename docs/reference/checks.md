---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 282f85ffe03f0859
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

A check is a reviewer that verifies one concern of mechanical conformance with the conventions, never the quality of the documents and never the substance of the thinking. This page lists the checks of today for the person who runs them and for the person who adds one: what each reads, what it verifies, what it costs and when it runs. A term of the forge that is not explained here is in the [Glossary](glossary.md).

Every check runs as a subagent (a helper that works in isolation and does not see the conversation). Every check reads only: it changes nothing and reports what it finds. The word "ledger" below means the project's table of state, the single source of truth for what documents, renders and resources the project has. The "principal" is the person whose thinking is forged.

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter against the history companion, ledger against the files, dependencies and resource indexes against the directories. | At a save. | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders. | At a release, beside `light`. | `.claude/agents/check-project.md` |
| `engine` | The core (the rules file, templates, skills, agents, scripts) against itself and against the forge intent. | At a release of the engine. | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history. | When a document is cleaned; never at a save or a release. | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place and cited everywhere else. | Before a major release or after a round on the operating layer; not at every release. | `.claude/agents/check-single-source-of-truth.md` |

## Which checks a save and a release run

- A save runs `light` on every repository in scope.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and `light` and `project` on its own project.
- `history` and `single-source-of-truth` run at neither; the principal asks for them.

To run a check, see [Check conformance](../use/check-conformance.md). To add one, see [Add a check](../extend/add-a-check.md).

## light

Description: verifies a project's bookkeeping. Fit for a save.

Reads: one project, the path the task names.

Verifies, with the owner of each rule in brackets:

- Front-matter and history, for every versioned document and its companion: the placement of the history and the form of its log (CLAUDE.md, Versioning & status; `templates/history.md`). Whether a text belongs in the document or in its history is the `history` check's.
- The ledger: its shape for its kind (`templates/ledger.md`).
- The documents table against the front-matter and the files on disk.
- Findings and challenges against the files in `reviews/` and `challenges/`.
- Every file in `sources/` and `research/` registered. A binary without an extract, and an extract without its original, are normal and never a finding.
- The Renders table against the provenance in each render's front-matter.
- The Published table against `published/`: a row without its file, a file without its row. Whether a row is `current` or `stale` is not a finding.
- The Work table against `work/`: every specification has a row and every row has its specification. A row whose file is not yet made is normal.
- "Waiting on principal" against what is actually open.
- A state word that the template no longer carries, which is fixed at once in the ledger only.
- Dependencies: every path in the Dependencies table exists on disk, every citation pointing outside the project has a row, and no row points inside the project. A missing library is an advisory finding.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories. What the entries say is never judged.

Cost: seconds, not minutes. It reads the ledger, the front-matter of every document, the newest records of the companions and the directory listings.

## project

Description: verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

Reads: one project, the path the task names; when the task names none, every project under `projects/` except `forge`, each reported on its own. The bookkeeping that `light` verifies is not repeated here.

Verifies, with the owner of each rule in brackets:

- Kind and repository: the ledger header declares `kind: thought | library` (`templates/ledger.md`, header), and `projects/<slug>/.git` exists. A project that is not a repository is a fact, reported with the way in (CLAUDE.md, Persistence). A library needs no chain.
- Structure: the files and folders of CLAUDE.md, Repository layout. A layer below the intent that the project does not have is never a finding.
- Recipes and renders are paired: every render traces to a recipe and carries provenance front-matter, every file in `published/` traces to a recipe with a `## Format` section, and a `.pptx` or `.docx` in `renders/` traces to a render beside it (CLAUDE.md, Document chain, Renders).
- The README and release-notes recipes exist.
- Briefs: every `00-brief*.md` has a row in the Briefs table and the reverse, and a brief marked `mined` is cited in the intent.
- Waiting on principal: a line that copies a thread, decision or history record instead of citing its ID is a finding (CLAUDE.md, Ledger).
- ID hygiene, in every document that carries IDs (CLAUDE.md, ID scheme). It does not apply to a library.
- Language, for every artefact and record (CLAUDE.md, prime directive 6). The briefs and renders are exempt.
- Immutables: the immutable documents are never edited after creation (CLAUDE.md, Versioning & status). The `00-INDEX.md` catalogues are exempt.
- Recipes and renders, in shape and freshness only: recipes conform to `templates/recipe.md` in front-matter and sections, every declared input exists, and a declared `output:` path points inside the repository. The staleness of a render is never a finding.

Cost: the project's files read once, and the conventions read from their owners.

## engine

Description: verifies the core (CLAUDE.md, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

Reads: the engine root the task names, that is CLAUDE.md, `templates/`, `.claude/skills/`, `.claude/agents/` and `scripts/`. It also reads the forge intent, its threads and its decisions. The conformance of the forge's own project is the `project` and `light` checks'. Whether a rule is stated in more than one place is the `single-source-of-truth` check's.

Verifies:

- Core internal consistency:
  - The commands table of CLAUDE.md against the skills in `.claude/skills/*/SKILL.md`. The reviewers' contracts are excepted.
  - The agents described against `.claude/agents/`.
  - Every skill an agent names in its front-matter exists.
  - Every file in `scripts/` is described in CLAUDE.md, and nothing described there is missing on disk.
  - The README against CLAUDE.md: same chain, same conventions, same command set, no contradiction. Currency is not checked, because the README is regenerated at the release.
  - The templates against the conventions of CLAUDE.md, Versioning & status and ID scheme: front-matter fields, the history companion, prefixes, numbering, statuses.
- Core against the forge intent:
  - Every position of the intent is honoured by the core documents.
  - Nothing withdrawn or rejected is still advertised in the core.
  - Decisions referenced from the intent exist in the decisions record, and every decision is reflected in the intent where it applies.
- Rename and removal sweep: the old names recorded in decisions and the terms the principal has dropped appear only in historical records (histories, decisions, rejected directions, reviews, challenges, research).

Cost: the core files once and the intent's positions once. Minutes at most, so that a release can afford it every time.

## history

Description: reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

Reads: one project, the path the task names, and in it every versioned document with its history and its archive, or the one document the task names.

Verifies the division between a document and its history (CLAUDE.md, Versioning & status; `.claude/skills/forge/states/intent.md`, Threads and files):

- In the document, the way to an item (as Versioning & status lists it) is a finding. So is detail that an item carries where the file that performs it exists.
- In the other direction, an item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

The form of the log is the `light` check's.

Cost: whole documents with their histories, minutes rather than seconds.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across CLAUDE.md, skills, agents, templates and scripts, and no direct operation where a mechanism exists. The honest sweep, expensive by design.

Reads: the whole operating layer of the engine, never a changed subset. That is CLAUDE.md, every skill with its supporting files, every agent, every template and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own CLAUDE.md, if any, against the owners in the engine.

Verifies:

- One owner per rule: a procedure, rule set or file shape that another file owns is cited by path and never restated. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own: every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists: git outside the scripts in `scripts/`, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents.

Cost: the whole layer, read and compared pairwise where the subjects overlap. Long by design. Its report says in the first line how many files it read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
