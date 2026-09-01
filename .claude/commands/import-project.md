---
description: Bring an existing project into projects/ — clone through scripts/forge-clone.ps1, offering the commit identity from CLAUDE.local.md
argument-hint: <git-url>
---

Bring the project at `$1` into the forge (POS.1060). Git is done by
`scripts/forge-clone.ps1` only — never run raw git commands, not even
to read state (POS.0550).

1. Require the URL. The target directory is
   `projects/<repository name>` — the name falls out of the URL (no
   slug parameter); if the directory already exists, stop and report.
2. Run `scripts/forge-clone.ps1 <url>` bare by default: with a
   per-host git configuration (POS.0950) the fresh clone resolves the
   right identity itself, and the script reports which. Pass
   `-Name`/`-Email` only as the fallback — the principal says this
   machine has no per-host configuration — proposed from the git
   identities in `CLAUDE.local.md` matching the URL's host, on his
   word.
3. Relay the script's facts: the last commit, the origin, the
   identity git resolves (a clone left with no identity is caught by
   `forge-save`, which reports and commits nothing), and whether
   the project carries a ledger with a `kind:` header — its absence
   is a fact, not a defect.
4. Finish by recommending `/forge <slug>` as the first act of work:
   the engine does not track the project and cannot guess it, so the
   project is selected by naming it.

Conversation in the principal's language; nothing is written into the
imported project by this command.
