---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: dcf3e89f9e87faf7
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/agents/check-brd.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

A check is a reviewer that verifies one concern of conformance with the
conventions: it is neither a critic of the documents nor a challenger
of the thinking. This page lists the six checks of today for the
person who runs them and for the one who extends the forge, with what
each reads, what it verifies and what it costs. Terms of the forge are
in the [Glossary](glossary.md).

Each check is one agent file, `.claude/agents/check-<name>.md`. Every
check reads only, and it finds only what its own concern covers: where
a rule belongs to another check, the entry says so.

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger's own reports, published companions, thread files, dependencies and resource indexes | A save | `.claude/agents/check-light.md` |
| `project` | Everything else about a project: kind, structure, ID hygiene, language, immutables, recipes and renders | A release, beside `light` | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent | A release of the engine | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned; never a save or a release | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place and cited elsewhere | Before a major, or after a round on the operating layer; not at every release | `.claude/agents/check-single-source-of-truth.md` |
| `brd` | A BRD's mechanics: traceability, parents, phasing, terms | After a pass of `/forge brd` | `.claude/agents/check-brd.md` |

## What a save and a release run

A save runs the `light` check on every repository in scope, unless
`--quick` leaves it out. A release of a project runs `light` and
`project` on it. A release of the engine runs `engine` on the engine
root, and `light` and `project` on the forge's own project, launched at
once and awaited together. The other three checks are run by hand.

## Entries

### light

- **Description:** verifies a project's bookkeeping: front-matter and
  the history companions against the templates, the ledger script's
  own reports, the index entries, the published companions and the
  thread files against the directories and the rules. Fit for a save.
- **Reads:** one project. For the engine that is `projects/forge`.
- **Verifies:**
  - Front-matter and history: every rule of Versioning & status in
    `CLAUDE.md`, for every versioned document and its companion, the
    placement of the history and the form of its log as
    `templates/history.md` gives it. Whether a text belongs in the
    document or in its history belongs to the `history` check.
  - The ledger's own reports: each line of its Reports section and
    each `unparsed:` line of its header is a finding, with the file it
    names (owner: `templates/ledger.md`, Reports). A project whose
    ledger header says `shape: before the migration` is reported as
    `templates/project.md` says.
  - Records and companions: a published companion without its file is
    a finding, and a file without a companion is the principal's own
    and never one; every specification in `work/` has its history
    companion; a work file that cites an item by ID not named among its
    specification's Inputs is a finding; every thread file carries the
    header of `templates/thread.md`, and a closed one is unchanged
    since its closing; a state word that the templates do not know is a
    finding.
  - Dependencies: every path in the Dependencies table exists on disk.
    A library that is missing is an advisory finding.
  - Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md`
    exist and agree with their directories, bundles and their inner
    indexes included (owner: `templates/index.md`). A binary without an
    extract, or an extract without its original, is the normal case.
- **Cost:** seconds, not minutes: the ledger's header and Reports, the
  front-matter of every document, the newest records of the companions
  and the directory listings.
- **Fits:** a save. Most of what it finds is pure bookkeeping, marked
  as an immediate fix.

### project

- **Description:** verifies a project's structure, IDs, language,
  immutables, recipes and renders against the conventions.
- **Reads:** one project, or, when none is named, every project under
  `projects/` except `forge`, each reported on its own.
- **Verifies:**
  - Kind (owner: `templates/project.md`, `templates/gitattributes`):
    the project file declares `kind` and `language`, `.gitattributes`
    exists, and `threads/` exists in a thought project. A library needs
    no chain, and `logo.png` is optional everywhere.
  - Structure (owner: `CLAUDE.md`, Repository layout and Document
    chain): the files and folders of the layout exist; a layer below
    the intent that a project does not have is never a finding; every
    render with provenance front-matter traces to a recipe; a published
    file that a companion claims traces to a recipe with a `## Format`
    section; the README and release-notes recipes exist; a brief whose
    mining record says `mined` is cited in the intent. Any other file
    in `renders/` or `published/` is the principal's own and never a
    finding.
  - ID hygiene (owner: `CLAUDE.md`, ID scheme): every rule there, in
    every document that carries IDs.
  - Language (owner: `CLAUDE.md`, prime directive 6): for every
    artefact and record, the briefs and renders being exempt.
  - Immutables (owner: `CLAUDE.md`, Versioning & status): signs of
    after-the-fact editing of reviews, challenges, sources and
    research. The `00-INDEX.md` catalogues are exempt.
  - Recipes and renders (owner: `templates/recipe.md` and the genre
    skeletons): front-matter and sections, every declared input exists,
    an `output:` path points inside the repository. The staleness of a
    render is never a finding.
- **Cost:** the project's files, read once, and the conventions read
  from their owners.
- **Fits:** a release, run beside `light`. The bookkeeping that `light`
  verifies is not repeated here.

### engine

- **Description:** verifies the core (`CLAUDE.md`, templates, skills,
  agents, scripts) against itself and against the forge intent: every
  position honoured, nothing withdrawn still advertised, every decision
  reflected.
- **Reads:** the engine root: `CLAUDE.md`, `templates/`,
  `.claude/skills/`, `.claude/agents/`, `scripts/`, and the forge
  intent with its threads and decisions.
- **Verifies:**
  - Core internal consistency (owner: `CLAUDE.md`): the commands table
    matches the skills on disk; described agents match
    `.claude/agents/`; every skill an agent names exists; every file in
    `scripts/` is described in `CLAUDE.md` and nothing described is
    missing; the README agrees with `CLAUDE.md` on chain, conventions
    and commands, though never on currency; the templates agree with
    the conventions of Versioning & status and the ID scheme.
  - Core against the forge intent: every position is honoured by the
    core documents, nothing withdrawn or rejected is still advertised,
    decisions the intent cites exist in the decisions record and every
    decision is reflected where it applies.
  - Rename and removal sweep: old names recorded in decisions, and
    terms the principal has dropped, appear only in historical records.
- **Cost:** the core files once and the intent's positions once:
  minutes at most.
- **Fits:** every release of the engine. It leaves two concerns to
  other checks: the forge project's own conformance belongs to `project`
  and `light`, and whether a rule is stated in more than one place
  belongs to `single-source-of-truth`.

### history

- **Description:** reads a document with its history and reports where
  the division between them does not hold, proposing each move in full.
- **Reads:** one project, and in it every versioned document with its
  history and its archive, or the one document the task names.
- **Verifies:** the division between a document and its history, by
  `CLAUDE.md`, Versioning & status, and the intent's definition
  (`.claude/skills/forge/states/intent.md`, Threads and files).
  - In the document, the way to an item is a finding, and so is detail
    that an item carries where the file that performs it exists.
  - In the other direction, an item that can no longer be understood
    because what makes it hold stands only in the history is a finding.
  - Each finding proposes the move in full: the text that leaves, word
    for word, and the record it becomes.
  - The form of the log belongs to `light`.
- **Cost:** whole documents with their histories: minutes rather than
  seconds.
- **Fits:** when a document is cleaned. It is never part of a save or a
  release.

### single-source-of-truth

- **Description:** verifies that every rule, procedure and file shape
  is written in one place and cited everywhere else: no restatement
  across `CLAUDE.md`, skills, agents, templates and scripts, and no
  direct operation where a mechanism exists. The honest sweep, expensive
  by design.
- **Reads:** the whole operating layer of the engine, never a changed
  subset: `CLAUDE.md`, every skill with its supporting files, every
  agent, every template and the help headers of `scripts/`. Named a
  project instead, it reads that project's recipes, resource indexes,
  ledger comments and its own `CLAUDE.md`, if any, against the owners
  in the engine.
- **Verifies:**
  - One owner per rule: a procedure, rule set or file shape that
    another file owns is cited by path, never restated. A restatement
    is a finding, and the fix is a reference to the owner and the
    deletion of the copy. Where a shape has no owner, the finding
    proposes one.
  - Reviewer files carry only their own: every lens, persona and check
    file names its kind's contract skill and carries only its
    front-matter and its Lens section.
  - No direct operation where a mechanism exists: git outside the
    scripts, a conversion outside `doc2md.py`, a render outside
    `/render`, a review outside the reviewer agents, a check outside
    the check agents.
- **Cost:** the whole layer, read and compared pairwise where the
  subjects overlap. Long by design: the report's first line says how
  many files were read.
- **Fits:** before a major, or after a round on the operating layer,
  run on the principal's word. It is not run at every release.

### brd

- **Description:** verifies a BRD's mechanics: every parent item
  carried, every cited ID existing, every item with a parent, the
  phasing present, every term defined, no link in an item.
- **Reads:** one project's `30-brd.md`, or the BRD of the project the
  task names, with its parent as the BRD's header declares it (the
  assignment or the intent). A BRD made from a source is a work product
  in `work/`, read when the task names it. A project without a BRD is
  not a finding. The bookkeeping of the file belongs to `light`, and the
  ID scheme in general to `project`.
- **Verifies:**
  - Traceability: every in-scope item of the parent is carried by at
    least one BR or UC, unless an OOS, DEP or TBC of the BRD names it;
    every parent an item cites exists; the appendix table matches the
    items (owner: `templates/brd.md`, Appendix).
  - Every item has a parent: a BR and an NFR end with their parent, an
    NFR may end with its category instead, and a UC declares its parent
    in its `Carries` line (owner:
    `.claude/skills/forge/states/brd.md`, Requirement style). Where the
    parent is a source with speakers, a BR whose every cited place is
    another party's turn is a finding.
  - The sections that may not be silent: Phasing is present and not
    empty, and every BR and UC stands in a phase or in the `not phased`
    row; the Touched areas, Stakeholders and NFR tables are complete;
    an ASM that answers a TBC of the same BRD is a finding; every TBC
    has an owner and says whether it blocks estimation.
  - Terms and links: every capitalised term of an item is in the Terms
    table, no item depends on a link, and no name of a person stands
    where the template asks for a role.
  - Skeleton residue: no template comment, `…`, `<placeholder>` or
    `NNNN` is left in the file.
- **Cost:** the BRD and its parent, read once, and the roster the BRD
  cites, read for its list of areas only.
- **Fits:** after a pass of `/forge brd`.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
