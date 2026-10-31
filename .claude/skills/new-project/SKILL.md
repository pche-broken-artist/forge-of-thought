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
Persistence) — nothing to propose.

**Kind.** Every project has a kind, declared as `kind:` in its
project file (`project.md`, `templates/project.md`; POS.0960,
POS.1590): `thought` (default — the chain, everything
below) or `library` (slug prefix `lib-`, material shared across
projects, no chain). Infer `library` from the `lib-` prefix or the
principal's words; when unclear, ask.

**Language.** Every project declares the language of its chain
artefacts as `language:` in its project file (CLAUDE.md, prime
directive 6; POS.0060 of the forge intent): English unless the
principal names another; ask when his words leave it open.

**Every project** gets `project.md` from `templates/project.md`
(slug, kind, language; written once, SOL.0670), `.gitattributes`
from `templates/gitattributes` (the ways of merging by path,
SOL.0730) and `.gitignore` from `templates/gitignore`: the ledger,
made at read time by `python scripts/forge-ledger.py <slug>` and never
in git (SOL.0680), and the lock files of an open Office document.

**Library** (`kind: library`): create only those three files, plus
`sources/00-INDEX.md`
and `research/00-INDEX.md` from `templates/index.md`, and
`recipes/readme.md` from `templates/recipe-readme.md` with library
inputs (the ledger made by the script and the two indexes) and its companion
`recipes/readme.history.md` from `templates/history.md` — its README
is the catalogue (POS.1000). No brief, no decisions, no reviews or challenges, no
release notes. Finish by proposing `/ingest` for the first documents;
steps 3–5 below do not apply.

**Thought project** (`kind: thought`):

1. Validate the slug: lowercase, hyphens, no spaces. If `projects/$0/`
   already exists, stop and report — never overwrite.
2. Create the folder structure:
   - `projects/$0/sources/`, `projects/$0/reviews/`,
     `projects/$0/challenges/`, `projects/$0/research/` and
     `projects/$0/threads/` — empty
     except `sources/00-INDEX.md` and `research/00-INDEX.md` from
     `templates/index.md` (header filled, no entries)
   - `projects/$0/project.md`, `.gitattributes` and `.gitignore` as
     Every project says above
   - `projects/$0/decisions.md` from `templates/decisions.md` — the
     slug filled, the sample record removed
   - `projects/$0/recipes/readme.md` from `templates/recipe-readme.md`
     and `projects/$0/recipes/release-notes.md` from
     `templates/recipe-release-notes.md` — slug and date filled, the
     template comments kept for the first `/recipe` iteration, each
     with its companion `recipes/<recipe>.history.md` from
     `templates/history.md` (its first records, 0.1 scaffolded); their renders
     are `/release`'s (CLAUDE.md, Document chain, Renders), not this command's
   - `projects/$0/logo.png` is the principal's to supply, optional
     (POS.1010) — mention it once, never ask for it
3. **00-brief.md:** ask the principal to paste or dictate the brief
   now and hand it to the `/forge brief` procedure
   (`.claude/skills/forge/states/brief.md`, its Course): it
   creates the file and its companion, stores, asks
   whether the text is finished, approves or leaves the draft. Nothing
   of that procedure is restated here (POS.1070).
4. Do NOT create 10-intent.md or any layer below it yet — each is
   born from its own first `/forge <state>`.
5. Make the ledger once, `python scripts/forge-ledger.py $0`, and
   finish by proposing the next step: run
   `/forge intent` to start the elicitation interview — and remind
   the principal that the project is not under git until he
   initialises its repository.
