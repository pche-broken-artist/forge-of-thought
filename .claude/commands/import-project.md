---
description: Bring an existing project into projects/ — clone through scripts/forge-clone.ps1, offering the commit identity from CLAUDE.local.md
argument-hint: <git-url>
disable-model-invocation: true
---

Bring the project at `$1` into the forge (POS.1060). Git is done by
`scripts/forge-clone.ps1` only — never run raw git commands, not even
to read state (POS.0550).

1. Require the URL. The target directory is
   `projects/<repository name>` — the name falls out of the URL (no
   slug parameter); if the directory already exists, stop and report.
2. The commit identity is a property of the project (POS.0950).
   Propose the identity from the git identities in `CLAUDE.local.md`
   matching the URL's host — an offer, never a rule — and on the
   principal's word run
   `scripts/forge-clone.ps1 <url> -Name <name> -Email <email>`. Run
   the script bare only when the principal says his own git
   configuration resolves the identity; either way the script
   reports which identity the clone ended up with.
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
