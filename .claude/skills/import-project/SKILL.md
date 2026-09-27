---
description: Bring an existing project into projects/ — clone through scripts/forge-clone.ps1, which reports the commit identity git resolves
argument-hint: "<git-url>"
disable-model-invocation: true
---

Bring the project at `$1` into the forge (POS.1060). Git is done by
`scripts/forge-clone.ps1` only (CLAUDE.md, Persistence).

1. Require the URL. The target directory is
   `projects/<repository name>` — the name falls out of the URL (no
   slug parameter); if the directory already exists, stop and report.
2. On the principal's word run `scripts/forge-clone.ps1 <url>`. The
   commit identity is git's, resolved per host from his own
   configuration (CLAUDE.md, Persistence); the script sets none and
   reports the one the clone resolves.
3. Relay the script's facts: the last commit, the origin, the
   identity git resolves (a clone for which git resolves none is
   caught by `forge-save`, which reports and commits nothing), and whether
   the project carries a ledger with a `kind:` header — its absence
   is a fact, not a defect (CLAUDE.md, Persistence).
4. Finish by recommending `/forge <slug>` as the first act of work:
   the engine does not track the project and cannot guess it, so the
   project is selected by naming it.

Nothing is written into the imported project by this command.
