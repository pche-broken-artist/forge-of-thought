---
description: Check a project's conformance with the current Forge conventions
argument-hint: [project-slug]
---

Check project $1 against the current conventions of the core
(CLAUDE.md, `templates/`). Without an argument, check every project
under `projects/` **except `forge`**, which has its own `/check-forge`.
Read-only: report compactly, per project; propose fixes and
apply only what the principal approves. Pure ledger bookkeeping may be
offered as an immediate fix.

Run in isolation: spawn one subagent (Agent tool, type
`general-purpose`, session model) whose prompt names the project path
(or paths) and instructs it to read `.claude/commands/check.md` and
execute the checks under *Checks per project* as written, returning
the report and nothing else. The subagent sees only the files, never
the working conversation (POS.0930); the checks live here, not in the
prompt (POS.1070). Back in the session: walk the findings through
with the principal (CLAUDE.md, Working methods); every fix is applied
here, on his word.

Checks per project:

0. **Kind and repository** — the ledger header declares `kind:
   thought | library` (missing = `thought`, report it as a finding
   with the one-line fix). `projects/<slug>/.git` exists; a project
   that is not a repository is reported as a fact, never a finding,
   with the one-line way in ("project is not a repository —
   `git -C projects/<slug> init -b main`, then a remote if wanted"),
   the one git-related check, since the engine does not track
   projects and a local-only project is a legitimate shape
   (POS.0940). A `library` needs no chain: checks 1, 2, 4 and 5
   reduce to `ledger.md`, `sources/00-INDEX.md`,
   `research/00-INDEX.md` and `recipes/readme.md` existing, the
   ledger shaped as `templates/ledger.md` says for `kind: library`;
   checks 3, 6, 7 and 8 apply as
   written, except
   that a library's documents may be overwritten by their owner
   (POS.0970) — not an immutability breach. `logo.png` is optional
   everywhere and its absence is never a finding (POS.1010).
1. **Structure** — expected files and folders exist: `00-brief.md`,
   `10-intent.md`, `decisions.md`, `ledger.md`; `20-assignment.md` once
   drafted; `sources/`, `reviews/`, `challenges/`, `research/`;
   `recipes/` and `renders/` where renders exist, paired — every render
   traces to a recipe and carries provenance front-matter matching the
   ledger's Renders table (legacy pre-recipe editions, dated filenames,
   are exempt). Every project carries `recipes/readme.md` with
   `output: README.md`, and a thought project `recipes/release-notes.md`
   with `output: RELEASE-NOTES.md` (POS.1000); a missing recipe is a
   finding (fix: scaffold from `templates/recipe-<genre>.md`), a missing
   or stale README or release notes a finding fixed by the next
   `/release`, which regenerates both. Every `00-brief*.md` in the directory has a row in the
   ledger's Briefs table and vice versa; a brief marked `mined` is
   cited somewhere in the intent.
2. **Front-matter and history** — against Versioning & status in
   CLAUDE.md, every rule there (POS.1070). Every versioned document
   (briefs, intent, assignment, later artefacts, recipes) has its
   companion `<file>.history.md` beside it, shaped as
   `templates/history.md`, the version of its newest row equal to the
   document's `version` and the document's `last_change` summarising
   that row. A Version History table in the body of any document is a
   finding, fix: move the rows into the companion and write
   `last_change` — that is how a project migrates to this convention,
   applied on the principal's word (POS.0820).
3. **Ledger accuracy** — documents table vs front-matter and files on
   disk; findings and challenges vs files in `reviews/` and
   `challenges/`; every file in `sources/` and `research/` registered
   (Sources and Research tables carry registration only, no content
   columns); a binary without an extract and an extract without its
   original are the normal case (POS.1040), never a finding, and a
   binary listed in `sources/.gitignore` is not an unregistered file;
   "Waiting on principal" matches what is actually open.
   **Dependencies** (POS.1020) — every path in the Dependencies table
   exists on disk (a missing library is the finding "library
   `<name>` not cloned alongside — `/import-project <its remote>`",
   advisory); every index entry, recipe or chain
   citation pointing outside the project (`projects/<other>/…`) has a
   row; no row points inside the project.
   **Resource indexes** — `sources/00-INDEX.md` and
   `research/00-INDEX.md` exist and agree with their directories: a
   file (or bundle) without an entry, an entry without a file, a bundle
   entry whose inner `00-INDEX.md` is missing. Never judge what the
   entries say.
4. **ID hygiene** — against the ID scheme in CLAUDE.md, every rule
   there (POS.1070), in every document that carries IDs.
5. **Assignment style** (where `20-assignment.md` exists) — against
   Requirement style in CLAUDE.md, every rule there (POS.1070); the
   Terms section lists only the prefixes and terms actually used, as
   `templates/assignment.md` says.
6. **Language** — all documents in English; only the briefs
   (`00-brief*.md`) may be in another language.
7. **Immutables** — locked briefs (status approved; a draft brief is
   still editable), sources, reviews, challenges and research
   are never edited after creation; flag any signs of after-the-fact
   editing that the ledger or the history companions reveal. The
   `00-INDEX.md` catalogues are exempt: they are rewritten freely.
8. **Recipes and renders** (shape and freshness, never content) —
   recipes conform to `templates/recipe.md`: front-matter complete
   (project, purpose, audience, version, updated, last_change;
   `output:` optional),
   sections Inputs / Instructions / Template present, every declared
   input exists on disk, the `output:` path, where declared, points
   inside the repository (genre skeletons `templates/recipe-<genre>.md`
   extend that shape with genre sections, never replace it). Render
   staleness (as `/render` step 5 defines it) is checked only for the
   README and the release notes, per step 1; the staleness of any
   other render is never a finding (POS.0570) — the `/forge` map shows
   it. The ledger's Renders table mirrors
   every render's front-matter provenance. Whether a recipe's content
   still matches the principal's thinking is substance, not
   conformance.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. This command checks conformance only.

Report per project: findings with `file:line` and a proposed fix, or a
single line saying the project conforms. Findings only: what conforms
is not reported, under no label ("observation", "note") — a rule
worth tightening is a matter for the intent, not for the check.
