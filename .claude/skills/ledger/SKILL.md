---
description: Report project state from the ledger
argument-hint: "[project-slug]"
---

Read the ledger of project $1 (or all projects if none given) and report
compactly:

1. Documents: file, version, status, date.
2. Sources and research: the registered files; what is unregistered
   is the `light` check's to find.
3. Findings: open by severity; awaiting the principal's verdict.
4. Open questions owned by the principal (from 20-assignment.md and intent
   Open threads).
5. Recommended next step (one line — e.g. "intent stable, worth running
   /forge assignment" or "3 findings await verdicts").

Read-only. Reconciling the ledger with reality (versions, files on
disk, indexes) is the `light` check's (`/check light`), not restated here (POS.1070); if a
discrepancy is obvious while reporting, name it and point there.
