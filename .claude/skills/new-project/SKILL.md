---
description: Scaffold a new project from templates — a thought project (the chain) or a library (material only); files only, never git
argument-hint: "<slug>"
disable-model-invocation: true
---

Create a new project under `projects/$0/`. Files only: the command
never touches git. A project is a repository of its own that the
engine does not track; initialising it and adding a remote are the
principal's one-off act, the way in named in CLAUDE.md, Persistence,
and a project that starts "not under git" is a property, not a
defect (CLAUDE.md, Persistence) — say so once at the end. The commit identity is git's,
resolved per host from his own configuration (CLAUDE.md,
Persistence) — nothing to propose; the command runs no git.

**Kind.** Every project has a kind, declared as `kind:` in its
ledger header (POS.0960): `thought` (default — the chain, everything
below) or `library` (slug prefix `lib-`, material shared across
projects, no chain). Infer `library` from the `lib-` prefix or the
principal's words; when unclear, ask.

**Language.** Every project declares the language of its chain
artefacts as `language:` in its ledger header (CLAUDE.md, prime directive 6;
POS.0060 of the forge intent): English unless the principal names
another; ask when his words leave it open.

**Library** (`kind: library`): create only `projects/$0/ledger.md`
from `templates/ledger.md` with `kind: library`, reduced as the
template's header says (POS.1070), plus `sources/00-INDEX.md`
and `research/00-INDEX.md` from `templates/index.md`, and
`recipes/readme.md` from `templates/recipe-readme.md` with library
inputs (ledger and the two indexes) and its companion
`recipes/readme.history.md` from `templates/history.md` — its README
is the catalogue (POS.1000). No brief, no decisions, no reviews or challenges, no
release notes. Finish by proposing `/ingest` for the first documents;
steps 3–5 below do not apply.

**Thought project** (`kind: thought`):

1. Validate the slug: lowercase, hyphens, no spaces. If `projects/$0/`
   already exists, stop and report — never overwrite.
2. Create the folder structure:
   - `projects/$0/sources/`, `projects/$0/reviews/`,
     `projects/$0/challenges/` and `projects/$0/research/` — empty
     except `sources/00-INDEX.md` and `research/00-INDEX.md` from
     `templates/index.md` (header filled, no entries)
   - `projects/$0/ledger.md` from `templates/ledger.md`, filled with
     project slug, `kind: thought`, the language and today's date;
     brief row as 0.1 draft, pending
   - `projects/$0/decisions.md` from `templates/decisions.md` — the
     slug filled, the sample record removed
   - `projects/$0/recipes/readme.md` from `templates/recipe-readme.md`
     and `projects/$0/recipes/release-notes.md` from
     `templates/recipe-release-notes.md` — slug and date filled, the
     template comments kept for the first `/recipe` iteration, each
     with its companion `recipes/<recipe>.history.md` from
     `templates/history.md` (its first records, 0.1 scaffolded); their renders
     are `/release`'s (CLAUDE.md, Document chain 7), not this command's
   - `projects/$0/logo.png` is the principal's to supply, optional
     (POS.1010) — mention it once, never ask for it
3. **00-brief.md:** ask the principal to paste or dictate the brief
   now and hand it to the `/forge brief` procedure
   (`.claude/skills/forge/states/brief.md`, its Course): it
   creates the file, its companion and its Briefs row, stores, asks
   whether the text is finished, locks or leaves the draft. Nothing
   of that procedure is restated here (POS.1070).
4. Do NOT create 10-intent.md or 20-assignment.md yet — intent is born from the
   first `/forge intent`, assignment from the first `/forge assignment`.
5. Update the ledger and finish by proposing the next step: run
   `/forge intent` to start the elicitation interview — and remind
   the principal that the project is not under git until he
   initialises its repository.
