---
name: check-project
description: Check "project" — verifies a project's structure, IDs, assignment style, language, immutables, recipes and renders against the conventions. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

You read one project — the path your task names — or, when the task
names none, every project under `projects/` except `forge`, each
reported on its own. The bookkeeping of a project — front-matter,
history companions, ledger tables, dependencies, resource indexes —
is the `light` check's, never yours; run beside it at a release
(`/release` step 2), you verify everything else.

What you verify:

0. **Kind and repository** — the ledger header declares `kind:
   thought | library` (missing = `thought`, a finding with the
   one-line fix). `projects/<slug>/.git` exists; a project that is
   not a repository is a fact, never a finding, reported with the
   one-line way in ("project is not a repository —
   the way in CLAUDE.md, Persistence, names"),
   the one git-related check, since the engine does not track
   projects and a local-only project is a legitimate shape
   (POS.0940). A `library` needs no chain: Structure reduces to the
   library's file set (CLAUDE.md, Repository layout); ID hygiene and
   Assignment style do not apply; Language, Immutables and Recipes
   and renders apply as written, except that a library's documents
   may be overwritten by their owner (POS.0970) — not an immutability
   breach. `logo.png` is optional everywhere and its absence is never
   a finding (POS.1010).
1. **Structure** — the files and folders of CLAUDE.md, Repository
   layout, exist; `20-assignment.md` once drafted, unless the ledger
   header's `terminal:` ends the chain elsewhere (CLAUDE.md, Ledger);
   `recipes/` and `renders/` paired — every render traces to a recipe
   and carries provenance front-matter (legacy pre-recipe editions,
   dated filenames, are exempt); whether that provenance matches the
   ledger's Renders table is the `light` check's;
   every file in `published/` traces to a recipe that carries a
   `## Format` section, and a `.pptx` or `.docx` in `renders/` to a
   render beside it (CLAUDE.md, Document chain 7). An older recipe
   still carrying `## Build instructions` (the alias:
   `templates/recipe.md`, Format) is a finding fixed at its next
   iteration.
   The README and release-notes recipes of CLAUDE.md, Document chain
   7, exist (fix: scaffold from `templates/recipe-<genre>.md`).
   Every `00-brief*.md` in the directory has
   a row in the ledger's Briefs table and vice versa; a brief marked
   `mined` is cited somewhere in the intent. Under the ledger's
   Waiting on principal, a line that copies a thread, a decision or a
   history record instead of citing it by ID is a finding (CLAUDE.md,
   Ledger).
2. **ID hygiene** — against the ID scheme in CLAUDE.md, every rule
   there (POS.1070), in every document that carries IDs.
3. **Language** — CLAUDE.md, prime directive 6, for every artefact
   and record; the briefs and renders are exempt as stated there.
4. **Immutables** — the immutable documents of CLAUDE.md, Versioning
   & status, never edited after creation; flag any signs of
   after-the-fact editing that the ledger or the history companions
   reveal. The `00-INDEX.md` catalogues are exempt: they are
   rewritten freely.
5. **Recipes and renders** (shape and freshness, never content) —
   recipes conform to `templates/recipe.md` in front-matter and
   sections (genre skeletons `templates/recipe-<genre>.md` extend that
   shape, never replace it); every declared input exists on disk; the
   `output:` path, where declared, points inside the repository. The
   staleness of a render (as `/render` step 5 defines it) is never a
   finding, the README and the release notes included (POS.0570): the
   `/forge` map shows it, and `/release` regenerates those two
   unconditionally. Whether a recipe's
   content still matches the principal's thinking is substance, not
   conformance.

Cost: the project's files, read once; the conventions read from their
owners.
