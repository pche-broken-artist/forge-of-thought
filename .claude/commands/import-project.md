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
2. Read the git identities in `CLAUDE.local.md`, propose the one
   matching the URL's host, and pass it as `-Name`/`-Email` on the
   principal's word. No match or no consent: clone without — the
   identity can be set later, and `forge-save` reports a repository
   whose identity is missing (POS.0950).
3. Run `scripts/forge-clone.ps1 <url> [-Name <n> -Email <e>]`.
4. Relay the script's facts: the last commit, the origin, and whether
   the project carries a ledger with a `kind:` header — its absence
   is a fact, not a defect.
5. Finish by recommending `/forge <slug>` as the first act of work:
   the engine does not track the project and cannot guess it, so the
   project is selected by naming it.

Conversation in the principal's language; nothing is written into the
imported project by this command.
