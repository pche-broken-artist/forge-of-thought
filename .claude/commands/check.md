---
description: Check a project's conformance with the current Forge conventions
argument-hint: [project-slug]
---

Check project $1 against the current conventions of the core
(CLAUDE.md, `templates/`). Without an argument, check every project
under `projects/` **except `forge`**, which has its own `/check-forge`.
Read-only: report in Czech, compactly, per project; propose fixes and
apply only what the principal approves. Pure ledger bookkeeping may be
offered as an immediate fix.

Checks per project:

0. **Kind and repository** — the ledger header declares `kind:
   thought | library` (missing = `thought`, report it as a finding
   with the one-line fix). `projects/<slug>/.git` exists; a project
   that is not a repository is a finding ("project is not a
   repository — `git -C projects/<slug> init -b main`, then a
   remote"), the one git-related check, since the engine does not
   track projects. A `library` needs no chain: checks 1, 2, 4 and 5
   reduce to `ledger.md`, `sources/00-INDEX.md`,
   `research/00-INDEX.md` and `recipes/readme.md` existing, and its
   ledger carrying only the Renders, Sources, Dependencies, Research
   and Waiting on principal tables; checks 3, 6, 7 and 8 apply as
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
   or stale render is a finding fixed by `/render` — or by the next
   `/save`, which regenerates both. Every `00-brief*.md` in the directory has a row in the
   ledger's Briefs table and vice versa; a brief marked `mined` is
   cited somewhere in the intent.
2. **Front-matter** — version, date, status present; status agrees with
   the version number (integer = `approved`); Version History table
   present and its top row matches the front-matter. Briefs carry no
   Version History: draft (0.x) or approved (1.0) in the header only.
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
   `<name>` not cloned alongside — `git clone <its remote>
   projects/<name>`", advisory); every index entry, recipe or chain
   citation pointing outside the project (`projects/<other>/…`) has a
   row; no row points inside the project.
   **Material indexes** — `sources/00-INDEX.md` and
   `research/00-INDEX.md` exist and agree with their directories: a
   file (or bundle) without an entry, an entry without a file, a bundle
   entry whose inner `00-INDEX.md` is missing. Never judge what the
   entries say.
4. **ID hygiene** — `PREFIX.NNNN` with the house prefixes in their
   proper documents; unique IDs, never renumbered; items in tens,
   groups starting at the next hundred; groups as plain headings with
   no IDs or metadata; depth max two levels.
5. **Assignment style** (where `20-assignment.md` exists) — shall /
   shall not; no would, could, should, might, may or MoSCoW wording; no
   priority markings except notes reading *optional*; one idea per
   item, full UK English sentences; Terms section lists the prefixes
   and domain terms actually used, defined Terms capitalised in item
   text; no item depends on an external link to be understood.
6. **Language** — all artefacts in English; only the briefs
   (`00-brief*.md`) may be in another language.
7. **Immutables** — locked briefs (status approved; a draft brief is
   still editable), sources, reviews, challenges and research
   are never edited after creation; flag any signs of after-the-fact
   editing that the ledger or Version Histories reveal. The
   `00-INDEX.md` catalogues are exempt: they are rewritten freely.
8. **Recipes and renders** (shape and freshness, never content) —
   recipes conform to `templates/recipe.md`: front-matter complete
   (project, purpose, audience, version, updated; `output:` optional),
   sections Inputs / Instructions / Template present, every declared
   input exists on disk (genre skeletons `templates/recipe-<genre>.md`
   extend that shape with genre sections, never replace it). Render staleness: front-matter provenance
   (recipe version, input versions) against the files as they are
   now — a render generated from versions that have since moved is a
   finding, fixed by `/render`. Whether a recipe's content still
   matches the principal's thinking is substance, not conformance.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. This command checks conformance only.

Report per project: findings with `file:line` and a proposed fix, or a
single line saying the project conforms.
