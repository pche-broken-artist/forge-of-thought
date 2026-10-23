---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: a5d7df84554cdcb3
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

A check is a reviewer that verifies one concern of mechanical
conformance with the conventions, never the substance or the quality
of the documents. This page lists the five checks of today, what each
reads and verifies, and what each costs, for the reader who chooses a
check and for the one who extends the set.

Each check runs as an isolated subagent (a helper Claude starts that
sees none of the working conversation). A check takes a project by its
slug, or the engine. A run that finds nothing files nothing.

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | Bookkeeping of a project: front-matter, history companions, the ledger's own reports, records, dependencies, resource indexes | A save | `.claude/agents/check-light.md` |
| `project` | Everything else about a project: kind, structure, ID hygiene, language, immutables, recipes and renders | A release | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent | A release | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place | Before a major, or after a round on the operating layer | `.claude/agents/check-single-source-of-truth.md` |

## Which checks a save and a release run

- A save runs `light` on every repository in scope, unless it is
  given `--quick`, which leaves the check out.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and
  `light` and `project` on `projects/forge`, the engine's own
  project.
- `history` and `single-source-of-truth` are run by hand, never by a
  save or a release.

How to run a check is described in
[Check conformance](../use/check-conformance.md). How to add one is
described in [Add a check](../extend/add-a-check.md).

## light

Description: verifies a project's bookkeeping, that is, front-matter
and the history companions against the templates, the ledger script's
own reports, the index entries, the published companions and the
thread files against the directories and the rules. Fit for a save.

Reads: one project, by the path the task names. For the engine that
is `projects/forge`.

Verifies, with the owner of each rule:

- Front-matter and history of every versioned document and its
  companion: the placement of the history and the form of its log.
  Owners: the Versioning & status section of `CLAUDE.md` and
  `templates/history.md`.
- The ledger's own reports: each line of its Reports section and each
  `unparsed:` line of its header is a finding that names its file.
  A project whose ledger header says `shape: before the migration` is
  reported as `templates/project.md` says. Owner: `templates/ledger.md`.
- Records and companions:
  - A published companion `published/<recipe>.md` and the files of
    `published/` agree.
  - Every specification in `work/` has its history companion.
  - A work file does not cite an item by ID that its specification's
    Inputs do not name.
  - Every thread file carries the header of `templates/thread.md`, and
    a closed one is unchanged since its closing.
  - A state word that a record or a Verdict carries and the templates
    do not know is a finding.
- Dependencies: every path in the Dependencies table exists on disk.
  A missing library is an advisory finding.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md`
  exist and agree with their directories, bundles and their inner
  indexes included. A sources entry without its `Date` and `Form`
  fields is a finding. Owner: `templates/index.md`.

Does not verify: whether a text belongs in the document or in its
history (that is `history`), and anything else about a project (that
is `project`).

Cost: seconds, not minutes. It reads the ledger's header and Reports,
the front-matter of every document, the companions' newest records and
the directory listings. Most of what it finds is marked "immediate
fix".

## project

Description: verifies a project's structure, IDs, language,
immutables, recipes and renders against the conventions.

Reads: one project, by the path the task names, or, when the task
names none, every project under `projects/` except `forge`, each
reported on its own.

Verifies, with the owner of each rule:

- Kind: `project.md` declares `kind: thought | library` and
  `language`; `.gitattributes` exists; `threads/` exists in a thought
  project. Owners: `templates/project.md` and `templates/gitattributes`.
  A library needs no chain, so its structure reduces to the library's
  file set and ID hygiene does not apply to it.
- Structure: the files and folders of the Repository layout section of
  `CLAUDE.md` exist. A layer below the intent that the project does not
  have is not missing.
  - `recipes/` and `renders/` are paired, and every render traces to a
    recipe and carries provenance front-matter.
  - Every file in `published/` traces to a recipe that carries a
    `## Format` section.
  - The README and release-notes recipes exist.
  - A brief whose mining record says `mined` is cited somewhere in the
    intent.
- ID hygiene: every rule of the ID scheme in `CLAUDE.md`, in every
  document that carries IDs.
- Language: prime directive 6 of `CLAUDE.md`, for every artefact and
  record. The briefs and renders are exempt.
- Immutables: the immutable documents of `CLAUDE.md`, Versioning &
  status, are not edited after creation. The `00-INDEX.md` catalogues
  are exempt.
- Recipes and renders, shape only: recipes conform to
  `templates/recipe.md`, every declared input exists, and an `output:`
  path points inside the repository. The staleness of a render is never
  a finding.

Does not verify: the bookkeeping that `light` owns, and whether a
recipe still matches the principal's thinking.

Cost: the project's files, read once, and the conventions read from
their owners.

## engine

Description: verifies the core (`CLAUDE.md`, templates, skills,
agents, scripts) against itself and against the forge intent: every
position honoured, nothing withdrawn still advertised, every decision
reflected.

Reads: the engine root the task names (`CLAUDE.md`, `templates/`,
`.claude/skills/`, `.claude/agents/`, `scripts/`) and the forge
intent, `projects/forge/10-intent.md`, with its threads and
`projects/forge/decisions.md`.

Verifies, with the owner of each rule:

- Core internal consistency:
  - The commands table of `CLAUDE.md` agrees with the skills in
    `.claude/skills/*/SKILL.md`, and the described agents with
    `.claude/agents/`.
  - Every skill that an agent names in its front-matter exists.
  - Every file in `scripts/` is described in `CLAUDE.md`, and nothing
    described there is missing on disk.
  - The README agrees with `CLAUDE.md` (same chain, conventions and
    command set), never in currency.
  - `templates/` agree with the conventions of `CLAUDE.md`.
- Core against the forge intent: every position is honoured by the core
  documents, nothing withdrawn or rejected is still advertised, the
  decisions the intent references exist in `decisions.md`, and every
  decision record is reflected in the intent where it applies.
- Rename and removal sweep: old names recorded in decision records, and
  terms the principal has dropped, appear only in historical records.

Does not verify: the forge project's own conformance (that is `project`
and `light`), and whether a rule is stated in more than one place (that
is `single-source-of-truth`).

Cost: the core files once and the intent's positions once. Minutes at
most.

## history

Description: reads a document with its history and reports where the
division between them does not hold, proposing each move in full. Fit
when a document is cleaned, never at a save or a release.

Reads: one project, by the path the task names, and in it every
versioned document with its history and its archive, or the one
document the task names.

Verifies, with the owner of each rule: the division between a document
and its history. Owners: the Versioning & status section of `CLAUDE.md`
and the Threads and files section of
`.claude/skills/forge/states/intent.md`.

- The way to an item (why it changed, what was said, trials) stands in
  the document: a finding.
- Detail an item carries where the file that performs it exists: a
  finding.
- An item that can no longer be understood because what makes it hold
  stands only in the history: a finding.

Each finding proposes the move in full: the text that leaves, word for
word, and the record it becomes. The form of the log is checked by
`light`.

Cost: whole documents with their histories, minutes rather than
seconds.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is
written in one place and cited everywhere else, with no restatement
across `CLAUDE.md`, skills, agents, templates and scripts and no direct
operation where a mechanism exists. It is the honest sweep, expensive
by design.

Reads: the whole operating layer of the engine, never a changed subset:
`CLAUDE.md`, every skill under `.claude/skills/` with its supporting
files, every agent under `.claude/agents/`, every template under
`templates/` and the help headers of `scripts/`. Named a project
instead, it reads that project's recipes, resource indexes, ledger
comments and its own `CLAUDE.md`, if any, against the owners in the
engine.

Verifies:

- One owner per rule: a command, agent, contract or template describes
  only its own job. A procedure, rule set or file shape that another
  file owns is cited by path. A restatement is a finding, fixed by a
  reference to the owner and the deletion of the copy.
- Reviewer files carry only their own: every lens, persona and check
  file names its kind's contract skill and carries only its
  front-matter and its Lens section.
- No direct operation where a mechanism exists: git outside the scripts
  in `scripts/`, a conversion outside `doc2md.py`, a render outside
  `/render`, a review outside the reviewer agents, a check outside the
  check agents.

Cost: the whole layer, read and compared pairwise where the subjects
overlap. Long by design. Fit before a major or after a round on the
operating layer, not at every release. Its report says in its first
line how many files it read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
