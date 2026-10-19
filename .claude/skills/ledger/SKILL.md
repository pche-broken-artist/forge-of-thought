---
description: Report project state from the ledger
argument-hint: "[project-slug]"
---

Make the ledger of project $0 (or of every project if none given),
`python scripts/forge-ledger.py <slug>` (SOL.0680), read it
and report it as the bare `/forge` map does — its step 3 in
`.claude/skills/forge/SKILL.md` is the one procedure for this report
(POS.1070); this command is the door for a ledger-only reading of
one project or of all of them.

Read-only but for the ledger the script writes. Its header's
`unparsed:` lines and its Reports section (templates/ledger.md) are
read aloud; the fixes are the `light` check's (`/check light`).
