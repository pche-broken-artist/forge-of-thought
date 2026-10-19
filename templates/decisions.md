---
project: <slug>
---

# Decisions

<!-- Append-only (CLAUDE.md, Document kinds). One record per decision
of the principal, numbered DEC.NNNN in the global sequence of the ID
scheme, newest last; a record is never edited, a later decision
supersedes it by a new record that names it. A decision that
rules on a finding or a challenge carries a Verdict line per ID, as
many lines as IDs it rules on; a partial verdict is read as the
verdict on the whole ID, the rest a `changed` record of the history
(POS.1610). -->

## DEC.NNNN — <the decision in one line>
- **Decision:** <what was decided>
- **Reason:** <why, including what was weighed against it>
- **Verdict:** <ID> rejected | parked until <what> | obsolete   # only where the decision rules on a finding or a challenge, one line per ID
- **Date:** YYYY-MM-DD
