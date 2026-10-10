---
generated: 2026-10-10
made: mirrored
inputs-hash: 2cf325bd1582c103
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - CLAUDE.md
---

# Checks

This page lists the checks the forge has, one entry each: what the
check is for, when it fits, what it reads, what it verifies and what
it costs. It is for the person who runs a check and for the one who
extends the forge with another. Every check verifies conformance with
the conventions; none is a critic of the documents or a challenger of
the thinking.

A check is run with `/check <check> [slug]`. It takes a project by its
slug, or the engine.

## Which checks a save and a release run

A save runs its own check and a release runs its own; which checks
each runs is stated in the definition of that command
(`.claude/skills/save/SKILL.md`, `.claude/skills/release/SKILL.md`),
not in `CLAUDE.md`. From the check files: `light` is the check a save
can afford; `project` and `engine` run beside `light` at a release;
`history` is never run at a save or a release; `single-source-of-truth`
is not run at every release.

## light

- **Description:** verifies a project's bookkeeping: front-matter
  against the history companion, ledger tables against the files,
  dependencies and resource indexes against the directories. Fit for
  a save.
- **Reads:** one project, the path the task names; for the engine
  that is `projects/forge`.
- **Verifies:**
  1. Front-matter and history: every rule of Versioning & status in
     `CLAUDE.md`, for every versioned document and its companion; the
     placement of the history and the form of its log as
     `templates/history.md` gives it. Whether a text belongs in the
     document or in its history is the `history` check's.
  2. Ledger accuracy: the ledger shaped as `templates/ledger.md` says
     for its kind; the documents table against front-matter and files
     on disk; findings and challenges against the files in `reviews/`
     and `challenges/`; every file in `sources/` and `research/`
     registered; the Renders table against every render's
     front-matter provenance; the Published table against
     `published/`; "Waiting on principal" against what is open. A
     binary without an extract, and an extract without its original,
     is the normal case and not a finding.
  3. Dependencies: every path in the Dependencies table exists on
     disk (a library not cloned is an advisory finding); every
     citation pointing outside the project has a row; no row points
     inside the project.
  4. Resource indexes: `sources/00-INDEX.md` and
     `research/00-INDEX.md` exist and agree with their directories,
     including a bundle's inner index. What the entries say is not
     judged.
- **Findings:** mostly pure bookkeeping, marked as an immediate fix.
- **Cost:** seconds, not minutes: the ledger, the front-matter of
  every document, the newest records of the companions and the
  directory listings.

## project

- **Description:** verifies a project's structure, IDs, language,
  immutables, recipes and renders against the conventions.
- **Reads:** one project, the path the task names, or, when the task
  names none, every project under `projects/` except `forge`, each
  reported on its own. The bookkeeping the `light` check owns is not
  verified here.
- **Verifies:**
  0. Kind and repository: the ledger header declares
     `kind: thought | library`; `projects/<slug>/.git` exists. A
     project that is not a repository is reported as a fact with the
     one-line way in, not as a finding. A library needs no chain.
  1. Structure: the files and folders of Repository layout in
     `CLAUDE.md` exist; a layer the project does not have is not
     missing; recipes and renders are paired and every render carries
     provenance front-matter; every file in `published/` traces to a
     recipe with a `## Format` section; the README and release-notes
     recipes exist; every `00-brief*.md` has a row in the Briefs table
     and the reverse; a brief marked `mined` is cited in the intent; a
     "Waiting on principal" line that copies instead of citing is a
     finding.
  2. ID hygiene: every rule of the ID scheme in `CLAUDE.md`, in every
     document that carries IDs.
  3. Language: prime directive 6 of `CLAUDE.md`, for every artefact
     and record; briefs and renders are exempt.
  4. Immutables: the immutable documents are never edited after
     creation; signs of after-the-fact editing that the ledger or the
     history companions reveal are flagged. The `00-INDEX.md`
     catalogues are exempt.
  5. Recipes and renders, shape and freshness, never content: recipes
     conform to `templates/recipe.md`; every declared input exists;
     the `output:` path points inside the repository. The staleness of
     a render is never a finding.
- **Cost:** the project's files, read once; the conventions are read
  from their owners.

## engine

- **Description:** verifies the core (`CLAUDE.md`, templates, skills,
  agents, scripts) against itself and against the forge intent: every
  position honoured, nothing withdrawn still advertised, every
  decision reflected.
- **Reads:** the engine root the task names (`CLAUDE.md`,
  `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`) and
  the forge intent with its threads and decisions. Whether a rule is
  stated in more than one place is the `single-source-of-truth`
  check's.
- **Verifies:**
  1. Core internal consistency: the commands table against the skills
     on disk; described agents against `.claude/agents/`; every skill
     an agent names in its front-matter exists; scripts on disk
     against `CLAUDE.md`, both ways; the README against `CLAUDE.md`
     for chain, conventions and command set, never currency; the
     templates against the conventions of `CLAUDE.md`.
  2. Core against the forge intent: every position honoured; nothing
     withdrawn or rejected still advertised in the core; decisions
     referenced from the intent exist in `decisions.md` and every
     decision is reflected in the intent where it applies.
  3. Rename and removal sweep: old names recorded in decisions, and
     terms the principal has dropped, appear only in historical
     records.
- **Cost:** the core files once and the intent's positions once;
  minutes at most, so that a release can afford it every time.

## history

- **Description:** reads a document with its history and reports
  where the division between them does not hold, proposing each move
  in full. Fit when a document is cleaned, never at a save or a
  release.
- **Reads:** one project, the path the task names (for the engine
  `projects/forge`), and in it every versioned document with its
  history and archive, or the one document the task names.
- **Verifies:** the division between a document and its history, by
  Versioning & status in `CLAUDE.md` and the intent's definition
  (`.claude/skills/forge/states/intent.md`, Threads and files). In
  the document, the way to an item is a finding, and so is detail an
  item carries where the file that performs it exists. The other way,
  an item that can no longer be understood because what makes it hold
  stands only in the history is a finding. Each finding proposes the
  move in full: the text that leaves, word for word, and the record it
  becomes. The form of the log is the `light` check's.
- **Cost:** whole documents with their histories; minutes rather than
  seconds.

## single-source-of-truth

- **Description:** verifies that every rule, procedure and file shape
  is written in one place and cited everywhere else: no restatement
  across `CLAUDE.md`, skills, agents, templates and scripts, no direct
  operation where a mechanism exists. The honest sweep, expensive by
  design: fit before a major or after a round on the operating layer,
  not at every release.
- **Reads:** the whole operating layer of the engine: `CLAUDE.md`,
  every skill under `.claude/skills/` with its supporting files, every
  agent under `.claude/agents/`, every template under `templates/`,
  the help headers of `scripts/`. Always the whole, never a changed
  subset. Named a project instead, it reads that project's recipes,
  resource indexes, ledger comments and its own `CLAUDE.md`, if any,
  against the owners in the engine.
- **Verifies:**
  - One owner per rule: every command, agent, contract and template
    describes only its own job; a procedure, rule set or file shape
    that another file owns is cited by path, never restated. Where a
    shape has no owner, the finding proposes one.
  - Reviewer files carry only their own: every lens, persona and check
    file names its kind's contract skill and carries only its
    front-matter and its Lens section.
  - No direct operation where a mechanism exists: git outside
    `scripts/`, a conversion outside `doc2md.py`, a render outside
    `/render`, a review outside the reviewer agents, a check outside
    the check agents.
- **Cost:** the whole layer, read and compared pairwise where the
  subjects overlap; long by design. The report's first line says how
  many files were read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
